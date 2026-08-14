"""Check a task's commit range against the mechanically decidable rules.

The classification in ``derivations/GOVERNANCE-ENFORCEMENT_classification.md``
governs: only properties classified MECHANICAL or PARTIAL are checked here,
and every PARTIAL result carries ``does_not_establish`` so a reader of this
tool's JSON meets the limit without consulting the classification.

Result vocabulary, deliberately wider than pass/fail:

``PASS``            the property held over the range
``FAIL``            the property was evaluated and did not hold
``NOT_APPLICABLE``  the subject genuinely does not occur in the range
``NOT_DECLARED``    the subject set was not supplied by the caller
``NOT_PARSEABLE``   the input did not admit the property's grammar
``DECLARED_EMPTY``  the subject set was declared, and is empty
``DECLARATION_CONFLICT``
                    the specification and the config both declared the
                    subject set and they differ
``OUT_OF_SCOPE``    excluded by the prospectivity boundary

``NOT_DECLARED``, ``NOT_PARSEABLE`` and ``DECLARATION_CONFLICT`` make the run
INCOMPLETE and exit non-zero: a missing or contradicted subject must never
read as green. ``NOT_APPLICABLE`` does not, because a range with no merge
genuinely has no P5 subject.

``DECLARED_EMPTY`` does NOT make the run INCOMPLETE, and the distinction is
deliberate. It is a VALID declaration -- the specification said the applicable
set is empty -- unlike ``NOT_DECLARED``, where the specification said nothing.
The run continues. It is equally not ``PASS``: nothing was checked, and a
``PASS`` over nothing is the vacuous green this repository has met three times
(P7 over two empty maps, a pin validator that would have passed on zero pins,
and P3's own former reading of ``[]`` as NOT_APPLICABLE). A reader of the JSON
sees ``DECLARED_EMPTY`` and its reason, so a valid empty declaration cannot be
mistaken for a successful non-empty verification.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from .core import (
    GOVERNANCE_FAILURE,
    TOOL_ERROR,
    InputError,
    blob,
    emit,
    git,
    load_json,
    normalize_repo_path,
    path_exists_at_revision,
    resolve,
)

TASK_RECORD_PREFIXES = ("specs/", "reviews/", "reports/")
REVIEW_PREFIX = "reviews/"
SPEC_PREFIX = "specs/"
REPORT_PREFIX = "reports/"

INCLUSIVE = "INCLUSIVE"
EXCLUSIVE = "EXCLUSIVE"

DOES_NOT_ESTABLISH = {
    "P1": (
        "Does not establish that the manifest is correct, only that the total "
        "the specification declares in its 'stated:' record agrees, per "
        "category, with the paths that record's block enumerates; a "
        "specification declaring no total is reported NOT_PARSEABLE, which is "
        "not a pass and is not a finding about that specification's scope."
    ),
    "P3": (
        "Does not establish which files are append-only; the declared set is a "
        "caller-supplied parameter and the check is silent about whether that "
        "set is the right one, or complete."
    ),
    "P5": (
        "Does not establish that the executor derived the parentage values "
        "independently; three correct values are equally consistent with fresh "
        "recomputation and with one field copied into another. The diquark "
        "task's shared-rationale defect would pass this check."
    ),
    "P6": (
        "Does not establish absence of 'session identifier' or 'tool "
        "attribution', which no repository document defines; only "
        "Co-Authored-By trailers and URLs are matched, and the author and "
        "committer identity fields are not message content and are out of "
        "scope."
    ),
    "P7": (
        "Does not establish which gate sections were authorised to change; the "
        "authorised set is a caller-supplied parameter, and an empty set means "
        "'nothing may change', never 'nothing to check'."
    ),
}

PARTIAL_IDS = frozenset(DOES_NOT_ESTABLISH)
NON_GREEN = frozenset({"NOT_DECLARED", "NOT_PARSEABLE", "DECLARATION_CONFLICT"})


class Supply:
    """Where a declared set came from, and whether the sources agree.

    A specification declares its sets in its scope block, where a reviewer
    reads them. A config supplies them at run time, after the review. **The
    specification wins when both are present and agree.** When both are
    present and DIFFER that is a conflict, not a merge and not a silent
    override -- a config quietly overriding a reviewed declaration would
    reproduce, one layer along, the defect this mechanism exists to remove.
    """

    def __init__(self, key: str, from_spec: Any, spec_paths: list[str],
                 from_config: Any) -> None:
        self.key = key
        self.from_spec = from_spec
        self.spec_paths = spec_paths
        self.from_config = from_config
        self.conflict = ""
        if from_spec is not None and from_config is not None:
            if [normalize_repo_path(str(v)) for v in from_spec] != [
                normalize_repo_path(str(v)) for v in from_config
            ]:
                self.conflict = (
                    f"'{key}' is declared by the specification as "
                    f"{list(from_spec)!r} and supplied by config as "
                    f"{list(from_config)!r}. A reviewed declaration and a "
                    "run-time config disagree; this is a stop, not a merge, "
                    "and not a silent override."
                )
            self.source = "specification"
            self.value = from_spec
        elif from_spec is not None:
            self.source = "specification"
            self.value = from_spec
        elif from_config is not None:
            self.source = "config"
            self.value = from_config
        else:
            self.source = "none"
            self.value = None

    def evidence(self) -> dict[str, Any]:
        return {
            "declared_key": self.key,
            "declared_source": self.source,
            "declared_by_specification": self.from_spec,
            "supplied_by_config": self.from_config,
            "specification_paths_read": self.spec_paths,
            "declared": self.value,
        }


def _declarations_from_specs(
    repo: Path, specs: list[str], head: str, key: str
) -> tuple[Any, list[str]]:
    """The value ``key`` takes from the subject specifications, if any.

    Two subject specifications declaring DIFFERENT values is the same conflict
    as a specification differing from config, and is reported the same way.
    """
    seen: list[tuple[str, Any]] = []
    for path in specs:
        if not path_exists_at_revision(repo, head, path):
            continue
        parsed = parse_scope_block(blob(repo, head, path).decode("utf-8"))
        if parsed.get("parse") != "OK":
            continue
        if parsed.get(key) is not None:
            seen.append((path, parsed[key]))
    if not seen:
        return None, [p for p, _ in seen]
    values = [v for _, v in seen]
    if any(v != values[0] for v in values[1:]):
        raise InputError(
            f"subject specifications declare different '{key}' values: "
            + "; ".join(f"{p}={v!r}" for p, v in seen)
        )
    return values[0], [p for p, _ in seen]


def _commits(repo: Path, base: str, head: str) -> list[str]:
    """Every commit in base..head, oldest first, in topological order."""
    return str(
        git(repo, "rev-list", "--reverse", "--topo-order", f"{base}..{head}")
    ).split()


def _own_commits(repo: Path, base: str, head: str) -> list[str]:
    """The task's OWN commits: the first-parent line of base..head.

    Rule 15 governs the commits a task makes. Commits arriving by merge were
    made by the task that authored them and were governed there; walking them
    here would fail every integration, whose merged branch necessarily commits
    its work before the integrating task's review exists.
    """
    return str(
        git(repo, "rev-list", "--reverse", "--topo-order", "--first-parent",
            f"{base}..{head}")
    ).split()


def _parents(repo: Path, commit: str) -> list[str]:
    line = str(git(repo, "rev-list", "--parents", "-n", "1", commit)).split()
    return line[1:]


def _paths_touched(repo: Path, commit: str) -> list[str]:
    """Paths a commit changed against its first parent; all paths for a root."""
    parents = _parents(repo, commit)
    if not parents:
        raw = str(git(repo, "ls-tree", "-r", "--name-only", commit))
    else:
        raw = str(git(repo, "diff", "--name-only", f"{commit}^1", commit))
    return [line for line in raw.split("\n") if line]


def _is_task_record(path: str) -> bool:
    return path.startswith(TASK_RECORD_PREFIXES)


def _result(
    ident: str,
    title: str,
    status: str,
    evidence: Any,
    reason: str = "",
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": ident,
        "title": title,
        "classification": "PARTIAL" if ident in PARTIAL_IDS else "MECHANICAL",
        "status": status,
        "evidence": evidence,
    }
    if reason:
        record["reason"] = reason
    if ident in PARTIAL_IDS:
        record["does_not_establish"] = DOES_NOT_ESTABLISH[ident]
    return record


# ---------------------------------------------------------------------------
# P1 — scope manifest arithmetic, under a declared total
# ---------------------------------------------------------------------------
# The declared total is read from a ``stated:`` record inside the scope block
# and from nowhere else. No sentence anywhere in the document is consulted,
# which is why this module carries no prose-count pattern: "nearest preceding
# count" selected an author's intermediate dry-run sentence often enough that
# the property it tested was not the property it claimed.
#
# ``append_only`` and ``authorised_gates`` put P3's and P7's declared sets
# INSIDE THE ARTIFACT A REVIEWER READS. They were previously supplied by a
# run-time JSON config written after the review, so the reviewer approved a
# specification and something else decided what the checks were pointed at.
SCOPE_KEYS = ("stated", "base", "head", "mode", "add", "modify",
              "append_only", "authorised_gates",
              "forbidden_operations")
_KEY = re.compile(r"^(" + "|".join(SCOPE_KEYS) + r"):")

#: Keys whose value is a declared SET: absent, explicitly empty, or a list.
#: The three are distinguishable, which is the whole point -- ``[]`` is a
#: declaration that the applicable set is empty, and absence is a declaration
#: of nothing.
DECLARED_SET_KEYS = ("append_only", "authorised_gates")

# A ``stated:`` value is a comma-separated list of "<decimal> <noun>" items,
# each noun at most once. Number words are not accepted: a declaration read by
# a machine is not prose.
_STATED_ITEM = re.compile(r"^(\d+)\s+(additions?|modifications?)$")

# PATH SHAPE: one or more slash-separated segments, each segment non-empty and
# built only from ASCII letters, digits, '.', '_', '-', '{' and '}'. Braces are
# admitted because this repository's manifests carry '{HHMM}' placeholders. A
# single segment with no slash is a path: 'GATES.md' is one.
_PATH = re.compile(r"^[A-Za-z0-9._{}-]+(?:/[A-Za-z0-9._{}-]+)*$")


def _unparseable(detail: str) -> dict[str, Any]:
    return {"parse": "NOT_PARSEABLE", "detail": detail}


def _parse_stated(value: str) -> tuple[dict[str, int] | None, str]:
    """Read a ``stated:`` value into per-category counts, or say why not."""
    items = [part.strip() for part in value.split(",")]
    if not value.strip() or any(not part for part in items):
        return None, f"malformed 'stated:' record: {value.strip()!r}"
    counts: dict[str, int] = {}
    for part in items:
        match = _STATED_ITEM.match(part)
        if not match:
            return None, f"malformed 'stated:' item: {part!r}"
        noun = "additions" if match.group(2).startswith("addition") else "modifications"
        if noun in counts:
            return None, f"'stated:' names {noun} twice"
        counts[noun] = int(match.group(1))
    return counts, ""


def _declared_item(key: str, value: str) -> tuple[str | None, str]:
    """One item of a declared set, validated against that key's shape."""
    if key == "append_only":
        if not _PATH.match(value):
            return None, f"not a path under 'append_only:': {value!r}"
        return value, ""
    if not re.fullmatch(GATE_ID, value):
        return None, f"not a gate id under 'authorised_gates:': {value!r}"
    return value, ""


def parse_scope_block(text: str) -> dict[str, Any]:
    """Locate the scope block, its counted set, and its DECLARED total.

    The SCOPE BLOCK is the contiguous indented run of records containing the
    document's single bare ``add:`` record; its extent runs from the highest
    line above ``add:`` that is non-empty and no less indented, down to the
    first dedent or trailing blank. The COUNTED SET is the path records under
    ``add:`` and ``modify:`` in that block. The DECLARED TOTAL is the block's
    ``stated:`` record, and no sentence is consulted.
    """
    lines = text.split("\n")
    starts = [
        n
        for n, line in enumerate(lines)
        if re.match(r"^\s+add:\s*$", line) or re.match(r"^\s+add:\s*\[\]\s*$", line)
    ]
    if len(starts) != 1:
        return _unparseable(f"{len(starts)} 'add:' records")
    start = starts[0]
    indent = len(lines[start]) - len(lines[start].lstrip())
    top = start
    while top > 0:
        above = lines[top - 1]
        if not above.strip() or len(above) - len(above.lstrip()) < indent:
            break
        top -= 1
    counted_add: list[str] = []
    counted_modify: list[str] = []
    bucket = {"add": counted_add, "modify": counted_modify}
    # ``None`` means the key was absent; a list means it was declared, and an
    # empty list means it was declared empty. Absence and emptiness must not
    # collapse into one value here, because P3 gives them different outcomes.
    declared: dict[str, list[str] | None] = {k: None for k in DECLARED_SET_KEYS}
    stated_line = None
    stated: dict[str, int] | None = None
    key = None
    for n in range(top, len(lines)):
        line = lines[n]
        if not line.strip():
            if key is not None and n > start:
                nxt = next((lines[m] for m in range(n + 1, len(lines))
                            if lines[m].strip()), "")
                if not nxt.startswith(" " * (indent + 1)):
                    break
            continue
        cur = len(line) - len(line.lstrip())
        if cur < indent:
            break
        stripped = line.strip()
        if _KEY.match(stripped):
            key, tail = (part.strip() for part in stripped.split(":", 1))
            if key == "stated":
                if stated is not None:
                    return _unparseable("two 'stated:' records in the scope block")
                stated, why = _parse_stated(tail)
                if stated is None:
                    return _unparseable(why)
                stated_line = stripped
                continue
            if key in DECLARED_SET_KEYS:
                if declared[key] is not None:
                    return _unparseable(f"two '{key}:' records in the scope block")
                declared[key] = []
                if tail and tail != "[]":
                    item, why = _declared_item(key, tail)
                    if item is None:
                        return _unparseable(why)
                    declared[key].append(item)
                continue
            if key in bucket and tail and tail != "[]":
                if not _PATH.match(tail):
                    return _unparseable(f"not a path under '{key}:': {tail!r}")
                bucket[key].append(tail)
            continue
        if key in DECLARED_SET_KEYS:
            item, why = _declared_item(key, stripped)
            if item is None:
                return _unparseable(why)
            declared[key].append(item)
            continue
        if key in bucket:
            if not _PATH.match(stripped):
                return _unparseable(f"not a path under '{key}:': {stripped!r}")
            bucket[key].append(stripped)
    if stated is None:
        return _unparseable("no 'stated:' record in the scope block")
    return {
        "parse": "OK",
        "counted_set": counted_add + counted_modify,
        "counted": len(counted_add) + len(counted_modify),
        "counted_add": len(counted_add),
        "counted_modify": len(counted_modify),
        "stated_record": stated_line,
        "stated_add": stated.get("additions", 0),
        "stated_modify": stated.get("modifications", 0),
        "stated": stated.get("additions", 0) + stated.get("modifications", 0),
        "append_only": declared["append_only"],
        "authorised_gates": declared["authorised_gates"],
    }


def _p1_agrees(finding: dict[str, Any]) -> bool:
    return (finding["counted_add"] == finding["stated_add"]
            and finding["counted_modify"] == finding["stated_modify"])


def check_p1(repo: Path, specs: list[str], head: str) -> dict[str, Any]:
    if not specs:
        return _result("P1", "scope manifest arithmetic", "NOT_APPLICABLE",
                       {}, "no specification path supplied or added in range")
    findings = []
    for path in specs:
        if not path_exists_at_revision(repo, head, path):
            findings.append({"path": path, "parse": "NOT_PARSEABLE",
                             "detail": "path absent at head"})
            continue
        parsed = parse_scope_block(blob(repo, head, path).decode("utf-8"))
        parsed["path"] = path
        findings.append(parsed)
    if any(f["parse"] != "OK" for f in findings):
        return _result("P1", "scope manifest arithmetic", "NOT_PARSEABLE", findings)
    bad = [f for f in findings if not _p1_agrees(f)]
    status = "FAIL" if bad else "PASS"
    return _result("P1", "scope manifest arithmetic", status, findings)


# ---------------------------------------------------------------------------
# P2 — Rule 15 commit order
# ---------------------------------------------------------------------------
def check_p2(repo: Path, commits: list[str], in_scope: list[str]) -> dict[str, Any]:
    out_of_scope = [c for c in commits if c not in set(in_scope)]
    first_work = None
    first_review = None
    detail = []
    for commit in in_scope:
        paths = _paths_touched(repo, commit)
        work = [p for p in paths if not _is_task_record(p)]
        review = [p for p in paths if p.startswith(REVIEW_PREFIX)]
        detail.append({"commit": commit, "work_paths": work[:6],
                       "adds_review": bool(review)})
        if review and first_review is None:
            first_review = commit
        if work and first_work is None:
            first_work = commit
    evidence = {
        "in_scope": len(in_scope),
        "out_of_scope": out_of_scope,
        "first_review_commit": first_review,
        "first_work_commit": first_work,
        "commits": detail,
    }
    if not in_scope:
        return _result("P2", "Rule 15 commit order", "OUT_OF_SCOPE", evidence,
                       "every commit in range precedes the prospectivity boundary")
    if first_work is None:
        return _result("P2", "Rule 15 commit order", "PASS", evidence,
                       "no work commit in range; nothing to order")
    if first_review is None:
        return _result("P2", "Rule 15 commit order", "FAIL", evidence,
                       "a work commit exists and no review commit precedes it")
    order = in_scope.index(first_review) < in_scope.index(first_work)
    return _result("P2", "Rule 15 commit order", "PASS" if order else "FAIL",
                   evidence)


# ---------------------------------------------------------------------------
# P3 — append-only, on both measures
# ---------------------------------------------------------------------------
def check_p3(
    repo: Path, base: str, head: str, commits: list[str], supply: "Supply"
) -> dict[str, Any]:
    if supply.conflict:
        return _result("P3", "append-only on both measures",
                       "DECLARATION_CONFLICT", supply.evidence(), supply.conflict)
    declared = supply.value
    if declared is None:
        return _result("P3", "append-only on both measures", "NOT_DECLARED",
                       supply.evidence(),
                       "no append-only set declared by the specification or "
                       "supplied by config; the set is not inferred")
    paths = [normalize_repo_path(p) for p in declared]
    if not paths:
        # DECLARED_EMPTY, and deliberately neither NOT_APPLICABLE nor PASS.
        # An empty declared set is something the specification SAID; absence is
        # something it did not say, and the two must not share an outcome. It
        # is not PASS either: nothing was checked, and PASS over nothing is the
        # vacuous green this repository has now met three times.
        return _result("P3", "append-only on both measures", "DECLARED_EMPTY",
                       supply.evidence(),
                       "nothing was checked because nothing was declared "
                       "applicable: the declared append-only set is empty, "
                       "which is a declaration and not an exemption")
    findings = []
    for path in paths:
        numstat = str(git(repo, "diff", "--numstat", base, head, "--", path))
        deleted_total = 0
        for line in numstat.split("\n"):
            if not line.strip():
                continue
            fields = line.split("\t")
            if len(fields) >= 2 and fields[1].isdigit():
                deleted_total += int(fields[1])
        per_commit = []
        for commit in commits:
            if not _parents(repo, commit):
                continue
            raw = str(git(repo, "diff", "--numstat", f"{commit}^1", commit,
                          "--", path))
            for line in raw.split("\n"):
                if not line.strip():
                    continue
                fields = line.split("\t")
                if len(fields) >= 2 and fields[1].isdigit() and int(fields[1]):
                    per_commit.append({"commit": commit, "deleted": int(fields[1])})
        prefix = None
        if path_exists_at_revision(repo, base, path) and path_exists_at_revision(
            repo, head, path
        ):
            before = blob(repo, base, path)
            after = blob(repo, head, path)
            prefix = after.startswith(before)
            sizes = {"base_bytes": len(before), "head_bytes": len(after)}
        else:
            sizes = {"base_bytes": None, "head_bytes": None}
        ok = deleted_total == 0 and not per_commit and prefix is True
        findings.append({"path": path, "deleted_lines_base_to_head": deleted_total,
                         "commits_with_deletions": per_commit,
                         "base_is_byte_prefix_of_head": prefix, **sizes,
                         "status": "PASS" if ok else "FAIL"})
    status = "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS"
    evidence = supply.evidence()
    evidence["paths"] = findings
    return _result("P3", "append-only on both measures", status, evidence)


# ---------------------------------------------------------------------------
# P4 — superseded branches are not merged
# ---------------------------------------------------------------------------
REGISTER_HEADING = "## Superseded branches"


def register_commits(repo: Path, revision: str, path: str) -> list[dict[str, str]]:
    """Entry records inside the first fenced block under the register heading."""
    text = blob(repo, revision, path).decode("utf-8")
    lines = text.split("\n")
    if REGISTER_HEADING not in lines:
        raise InputError(f"no '{REGISTER_HEADING}' section in {path}")
    start = lines.index(REGISTER_HEADING)
    stop = next(
        (n for n in range(start + 1, len(lines)) if lines[n].startswith("## ")),
        len(lines),
    )
    section = lines[start:stop]
    fences = [n for n, line in enumerate(section) if line.startswith("```")]
    if len(fences) < 2:
        raise InputError("register section has no fenced block")
    block = section[fences[0] + 1: fences[1]]
    entries = []
    for n, line in enumerate(block):
        if not re.match(r"^[a-z][A-Za-z0-9._/-]*/[A-Za-z0-9._-]", line):
            continue
        match = re.search(r"@\s*([0-9a-f]{40})", line)
        if match is None and n + 1 < len(block):
            match = re.search(r"@\s*([0-9a-f]{40})", block[n + 1])
        if match:
            entries.append({"branch": line.split()[0], "commit": match.group(1)})
    return entries


def check_p4(repo: Path, head: str, register_path: str) -> dict[str, Any]:
    if not path_exists_at_revision(repo, head, register_path):
        return _result("P4", "superseded branches are not merged", "NOT_APPLICABLE",
                       {"register_path": register_path},
                       "register file absent at head")
    entries = register_commits(repo, head, register_path)
    if not entries:
        return _result("P4", "superseded branches are not merged", "NOT_APPLICABLE",
                       {"register_path": register_path, "entries": 0},
                       "register carries no entries")
    findings = []
    for entry in entries:
        known = True
        try:
            resolve(repo, entry["commit"])
        except InputError:
            known = False
        if known:
            code = _ancestor(repo, entry["commit"], head)
        else:
            code = None
        findings.append({**entry, "object_present": known,
                         "is_ancestor_of_head": code is True,
                         "status": "FAIL" if code is True else "PASS"})
    status = "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS"
    return _result("P4", "superseded branches are not merged", status,
                   {"register_path": register_path, "entries": findings})


def _ancestor(repo: Path, maybe: str, of: str) -> bool:
    try:
        git(repo, "merge-base", "--is-ancestor", maybe, of)
        return True
    except InputError:
        return False


# ---------------------------------------------------------------------------
# P5 — merge parentage against freshly recomputed facts
# ---------------------------------------------------------------------------
def check_p5(repo: Path, commits: list[str], recorded: Any) -> dict[str, Any]:
    merges = [c for c in commits if len(_parents(repo, c)) > 1]
    if not merges:
        return _result("P5", "merge parentage against recomputed facts",
                       "NOT_APPLICABLE", {"merges": []},
                       "no merge commit in range")
    stated = {r["merge"]: r for r in recorded} if recorded else {}
    findings = []
    for merge in merges:
        parents = _parents(repo, merge)
        fresh = str(git(repo, "merge-base", parents[0], parents[1])).strip()
        record = {
            "merge": merge,
            "recomputed_parent_1": parents[0],
            "recomputed_parent_2": parents[1],
            "recomputed_merge_base": fresh,
            "merge_base_equals_parent_1": fresh == parents[0],
        }
        claim = stated.get(merge)
        if claim is None:
            record["compared_to_recorded"] = "UNAVAILABLE"
            record["status"] = "PASS"
        else:
            agree = (
                claim.get("parent_1") == parents[0]
                and claim.get("parent_2") == parents[1]
                and claim.get("merge_base") == fresh
            )
            record["compared_to_recorded"] = "AGREES" if agree else "DISAGREES"
            record["recorded"] = claim
            record["status"] = "PASS" if agree else "FAIL"
        findings.append(record)
    status = "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS"
    return _result("P5", "merge parentage against recomputed facts", status,
                   findings)


# ---------------------------------------------------------------------------
# P6 — commit-message hygiene
# ---------------------------------------------------------------------------
_TRAILER = re.compile(r"^\s*co-authored-by\s*:", re.I | re.M)
_URL = re.compile(r"https?://\S+", re.I)


def check_p6(repo: Path, commits: list[str]) -> dict[str, Any]:
    if not commits:
        return _result("P6", "commit-message hygiene", "NOT_APPLICABLE", [],
                       "no commit in range")
    findings = []
    for commit in commits:
        message = str(git(repo, "log", "-1", "--format=%B", commit))
        hits = []
        if _TRAILER.search(message):
            hits.append("Co-Authored-By")
        for url in _URL.findall(message):
            hits.append(url)
        findings.append({"commit": commit, "matches": hits,
                         "status": "FAIL" if hits else "PASS"})
    status = "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS"
    return _result("P6", "commit-message hygiene", status, findings)


# ---------------------------------------------------------------------------
# P7 — gate integrity
# ---------------------------------------------------------------------------
# THE ONE GATE-HEADING GRAMMAR.
#
# This repository carried TWO expressions reading the same registry: this one,
# and ``tests/test_repository_structure.py``'s. They returned the same fourteen
# ids and their symmetric difference was empty -- by coincidence, not by
# construction. They were not the same language, and three shapes separated
# them in both directions:
#
#     '## P2-FOO2-01 - Title'   this one accepted, the structure test rejected
#     '## P2-BAR-01'            this one rejected, the structure test accepted
#     '## P2-BAZ-01 - '         this one rejected, the structure test accepted
#
# Nothing compared them, so a convention changed on one side would have left
# the other reading a different registry, silently.
#
# The canonical language is the CONJUNCTION of the two, and both call sites now
# use this module. It is STRICTLY TIGHTER than either, so every heading it
# accepts both former expressions already accepted: the consolidation cannot
# admit anything neither side admitted. Each side contributed a real check --
# the strict id shape encodes a naming convention, the title requirement
# encodes that a registry entry without a title is not usable -- and dropping
# either would have lost one.
#
# Anything the tightened grammar rejects does not disappear. ``check_p7``'s
# completeness invariant compares parsed sections against the independent raw
# ``^## P2-`` count and returns NOT_PARSEABLE when they differ, which is what
# makes tightening safe.
GATE_ID = r"P2-[A-Z]+(?:-[A-Z]+)*-\d+"
GATE_SEPARATORS = "—–-"  # EM DASH, EN DASH, HYPHEN-MINUS
GATE_HEADING = re.compile(
    rf"^## ({GATE_ID})[ \t]+[—–-][ \t]+\S.*$"
)
#: The gate id shape alone, for callers matching ids in running text rather
#: than headings. Shares :data:`GATE_ID` with the heading grammar so the two
#: cannot drift.
GATE_ID_TOKEN = re.compile(GATE_ID)


def gate_heading_id(line: str) -> str | None:
    """The gate id this line declares as a heading, or ``None``.

    The single entry point for "is this a gate heading, and which gate". Both
    the checker and the repository-structure test call it; neither carries an
    expression of its own.
    """
    match = GATE_HEADING.match(line)
    return match.group(1) if match else None


def gate_heading_ids(text: str) -> list[str]:
    """Every gate id declared by a heading in ``text``, in file order.

    Order is preserved and duplicates are kept: a registry declaring one id
    twice is a defect ``check_p7``'s completeness invariant reports, and
    de-duplicating here would hide it.
    """
    return [gid for gid in (gate_heading_id(l) for l in text.split("\n")) if gid]

# Deliberately NOT written in terms of ``GATE_HEADING``. This is the cheap
# independent signal the completeness invariant is measured against: a guard
# expressed through the parser it protects would fail together with it.
RAW_GATE_HEADING = re.compile(r"^## P2-")


def gate_sections(repo: Path, revision: str, path: str) -> dict[str, str]:
    text = blob(repo, revision, path).decode("utf-8")
    lines = text.split("\n")
    marks = [(n, GATE_HEADING.match(line)) for n, line in enumerate(lines)]
    heads = [(n, m.group(1)) for n, m in marks if m]
    sections = {}
    for index, (line_no, name) in enumerate(heads):
        stop = heads[index + 1][0] if index + 1 < len(heads) else len(lines)
        sections[name] = "\n".join(lines[line_no:stop])
    return sections


def raw_gate_headings(repo: Path, revision: str, path: str) -> list[str]:
    """Every ``## P2-`` line, counted without consulting ``GATE_HEADING``."""
    text = blob(repo, revision, path).decode("utf-8")
    return [line for line in text.split("\n") if RAW_GATE_HEADING.match(line)]


def check_p7(
    repo: Path, base: str, head: str, gates_path: str, supply: "Supply"
) -> dict[str, Any]:
    if supply.conflict:
        return _result("P7", "gate integrity", "DECLARATION_CONFLICT",
                       supply.evidence(), supply.conflict)
    authorised = supply.value
    if authorised is None:
        return _result("P7", "gate integrity", "NOT_DECLARED",
                       supply.evidence(),
                       "no authorised gate set declared by the specification "
                       "or supplied by config; the set is not inferred")
    if not path_exists_at_revision(repo, base, gates_path):
        return _result("P7", "gate integrity", "NOT_APPLICABLE",
                       {"gates_path": gates_path}, "gate file absent at base")
    before = gate_sections(repo, base, gates_path)
    after = gate_sections(repo, head, gates_path)
    raw_base = raw_gate_headings(repo, base, gates_path)
    raw_head = raw_gate_headings(repo, head, gates_path)
    allowed = set(authorised)
    changed = [
        name
        for name in sorted(set(before) & set(after))
        if before[name] != after[name] and name not in allowed
    ]
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    evidence = {
        **supply.evidence(),
        "gates_path": gates_path,
        "authorised_modified": sorted(allowed),
        "raw_heading_count_base": len(raw_base),
        "raw_heading_count_head": len(raw_head),
        "section_count_base": len(before),
        "section_count_head": len(after),
        "unauthorised_changed": changed,
        "added_sections": added,
        "removed_sections": removed,
    }
    # The completeness invariant, and it is checked BEFORE the comparison so
    # that no arrangement of the authorised set, and no identity between base
    # and head, can reach a PASS through an incompletely read registry.
    #
    # Zero readable gate headings is never a clean bill of health: a registry
    # the grammar could not read has not been checked, which is not the same
    # as having been read and found clean.
    if not raw_base or not raw_head:
        return _result(
            "P7", "gate integrity", "NOT_PARSEABLE", evidence,
            "no '## P2-' gate heading found at "
            + ("base" if not raw_base else "head")
            + "; the gate registry could not be read, which is not the same "
              "as having been read and found unchanged",
        )
    # EQUALITY, not merely non-zero. A grammar that reads fourteen of fifteen
    # headings would otherwise PASS on the fourteen it sees, while the one it
    # misses stays invisible -- and one unseen gate is enough.
    if len(before) != len(raw_base) or len(after) != len(raw_head):
        evidence = dict(evidence)
        for label, raw in (("base", raw_base), ("head", raw_head)):
            matches = [GATE_HEADING.match(line) for line in raw]
            evidence[f"unrecognised_headings_{label}"] = [
                line for line, m in zip(raw, matches) if not m
            ]
            ids = [m.group(1) for m in matches if m]
            # A heading the grammar reads twice collapses in the section map,
            # so the counts can differ with nothing unrecognised.
            evidence[f"duplicate_ids_{label}"] = sorted(
                {name for name in ids if ids.count(name) > 1}
            )
        return _result(
            "P7", "gate integrity", "NOT_PARSEABLE", evidence,
            "parsed gate sections do not equal the independently counted "
            "'## P2-' headings "
            f"(base {len(before)}/{len(raw_base)}, "
            f"head {len(after)}/{len(raw_head)}); the grammar cannot fully "
            "read the gate registry, which is not a finding that a gate "
            "changed without authorisation",
        )
    ok = not changed and not added and not removed
    return _result("P7", "gate integrity", "PASS" if ok else "FAIL", evidence)


# ---------------------------------------------------------------------------
# P8 — Rule 15 placement and specification-first
# ---------------------------------------------------------------------------
def check_p8(repo: Path, in_scope: list[str]) -> dict[str, Any]:
    if not in_scope:
        return _result("P8", "Rule 15 placement and specification-first",
                       "OUT_OF_SCOPE", {},
                       "every commit in range precedes the prospectivity boundary")
    added_specs, added_reviews, added_reports, misplaced = [], [], [], []
    for commit in in_scope:
        for path in _paths_touched(repo, commit):
            if path.startswith(SPEC_PREFIX):
                added_specs.append((commit, path))
            elif path.startswith(REPORT_PREFIX):
                added_reports.append((commit, path))
            elif path.startswith(REVIEW_PREFIX):
                added_reviews.append((commit, path))
                if len(Path(path).parts) < 3:
                    misplaced.append(path)
    first_paths = _paths_touched(repo, in_scope[0])
    spec_first = bool(first_paths) and all(
        p.startswith(SPEC_PREFIX) for p in first_paths
    )
    evidence = {
        "first_commit": in_scope[0],
        "first_commit_paths": first_paths,
        "specification_is_first_commit": spec_first,
        "reviews_missing_function_directory": misplaced,
        "specs_added": [p for _c, p in added_specs],
        "reviews_added": [p for _c, p in added_reviews],
        "reports_added": [p for _c, p in added_reports],
    }
    if not added_specs:
        return _result("P8", "Rule 15 placement and specification-first",
                       "NOT_APPLICABLE", evidence,
                       "range adds no specification; not a task range")
    ok = spec_first and not misplaced
    return _result("P8", "Rule 15 placement and specification-first",
                   "PASS" if ok else "FAIL", evidence)


# ---------------------------------------------------------------------------
# P9 — every report carries a "Stops and clarifications" section
# ---------------------------------------------------------------------------
STOPS_HEADING = re.compile(r"^#{1,6}\s.*stops and clarifications", re.I | re.M)


def check_p9(repo: Path, head: str, in_scope: list[str]) -> dict[str, Any]:
    reports = sorted({
        path
        for commit in in_scope
        for path in _paths_touched(repo, commit)
        if path.startswith(REPORT_PREFIX) and path.endswith(".md")
    })
    if not reports:
        return _result("P9", "reports carry a Stops and clarifications section",
                       "NOT_APPLICABLE", {}, "range adds no report")
    findings = []
    for path in reports:
        if not path_exists_at_revision(repo, head, path):
            findings.append({"path": path, "present": False, "status": "FAIL"})
            continue
        text = blob(repo, head, path).decode("utf-8")
        found = bool(STOPS_HEADING.search(text))
        findings.append({"path": path, "heading_present": found,
                         "status": "PASS" if found else "FAIL"})
    status = "FAIL" if any(f["status"] == "FAIL" for f in findings) else "PASS"
    return _result("P9", "reports carry a Stops and clarifications section",
                   status, findings)


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
def evaluate(repo: Path, config: dict[str, Any]) -> dict[str, Any]:
    base = config.get("base")
    head = config.get("head")
    if not isinstance(base, str) or not isinstance(head, str):
        raise InputError("task checker requires base and head")
    base_sha, head_sha = resolve(repo, base), resolve(repo, head)
    commits = _commits(repo, base_sha, head_sha)
    own = _own_commits(repo, base_sha, head_sha)

    prospectivity = config.get("prospectivity") or {}
    boundary = prospectivity.get("boundary")
    inclusivity = prospectivity.get("inclusivity", INCLUSIVE)
    if inclusivity not in (INCLUSIVE, EXCLUSIVE):
        raise InputError("prospectivity inclusivity must be INCLUSIVE or EXCLUSIVE")
    if boundary is None:
        in_scope = list(own)
        boundary_sha = None
    else:
        boundary_sha = resolve(repo, boundary)
        in_scope = [
            c
            for c in own
            if _ancestor(repo, boundary_sha, c)
            and (inclusivity == INCLUSIVE or c != boundary_sha)
        ]

    subject_specs = config.get("specification_paths") or _added_specs(
        repo, commits)
    # C3: the declared sets are read from the subject specifications FIRST --
    # where a reviewer saw them -- and from the run-time config only as a
    # fallback. Disagreement is a conflict, reported by the property.
    spec_append, append_paths = _declarations_from_specs(
        repo, subject_specs, head_sha, "append_only")
    spec_gates, gates_paths = _declarations_from_specs(
        repo, subject_specs, head_sha, "authorised_gates")
    append_supply = Supply("append_only", spec_append, append_paths,
                           config.get("append_only_paths"))
    gates_supply = Supply("authorised_gates", spec_gates, gates_paths,
                          config.get("authorised_modified_gates"))

    properties = [
        check_p1(repo, subject_specs, head_sha),
        check_p2(repo, own, in_scope),
        check_p3(repo, base_sha, head_sha, commits, append_supply),
        check_p4(repo, head_sha,
                 config.get("register_path", "docs/BRANCHING_POLICY.md")),
        check_p5(repo, own, config.get("recorded_merge_facts")),
        check_p6(repo, commits),
        check_p7(repo, base_sha, head_sha, config.get("gates_path", "GATES.md"),
                 gates_supply),
        check_p8(repo, in_scope),
        check_p9(repo, head_sha, in_scope),
    ]

    statuses = {p["status"] for p in properties}
    if "FAIL" in statuses:
        overall = "FAIL"
    elif statuses & NON_GREEN:
        overall = "INCOMPLETE"
    else:
        overall = "PASS"
    return {
        "tool": "task_checker",
        "base": base_sha,
        "head": head_sha,
        "commits_in_range": len(commits),
        "commits_on_first_parent_line": len(own),
        "prospectivity": {
            "boundary": boundary_sha,
            "inclusivity": inclusivity,
            "commits_in_scope": len(in_scope),
            "commits_out_of_scope": [c for c in own if c not in set(in_scope)],
            "scope_note": (
                "P2, P5, P8 and P9 walk the task's own first-parent line; "
                "commits arriving by merge were governed by the task that "
                "made them."
            ),
        },
        "properties": properties,
        "overall": overall,
        "overall_note": (
            "INCOMPLETE is non-zero deliberately: NOT_DECLARED and "
            "NOT_PARSEABLE mean a subject was missing, and a missing subject "
            "must never read as a pass."
        ),
    }


def _added_specs(repo: Path, commits: list[str]) -> list[str]:
    return sorted({
        path
        for commit in commits
        for path in _paths_touched(repo, commit)
        if path.startswith(SPEC_PREFIX) and path.endswith(".md")
    })


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    try:
        result = evaluate(Path(args.repo), load_json(args.config))
        code = 0 if result["overall"] == "PASS" else GOVERNANCE_FAILURE
        return emit(result, code)
    except (InputError, OSError) as error:
        return emit(
            {"tool": "task_checker", "overall": "TOOL_ERROR", "error": str(error)},
            TOOL_ERROR,
        )


if __name__ == "__main__":
    raise SystemExit(main())
