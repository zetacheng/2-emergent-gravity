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
``OUT_OF_SCOPE``    excluded by the prospectivity boundary

``NOT_DECLARED`` and ``NOT_PARSEABLE`` make the run INCOMPLETE and exit
non-zero: a missing subject must never read as green. ``NOT_APPLICABLE``
does not, because a range with no merge genuinely has no P5 subject.
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
        "Does not establish that the manifest is correct, only that its path "
        "count matches the count in the sentence the grammar selects as "
        "governing; a specification whose text does not admit the parse is "
        "reported NOT_PARSEABLE, which is not a pass."
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
NON_GREEN = frozenset({"NOT_DECLARED", "NOT_PARSEABLE"})


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
# P1 — scope manifest arithmetic, under a stated grammar
# ---------------------------------------------------------------------------
COUNT_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12,
}
_COUNT = re.compile(
    r"\b(\d+|" + "|".join(COUNT_WORDS) + r")\b\s+"
    r"(additions?|modifications?|paths?)\b",
    re.I,
)


def _count_value(token: str) -> int:
    token = token.lower()
    return int(token) if token.isdigit() else COUNT_WORDS[token]


def parse_scope_block(text: str) -> dict[str, Any]:
    """Locate the scope block, its counted set, and its governing sentence.

    The SCOPE BLOCK is the indented or fenced block carrying both an
    ``add:`` and a ``modify:`` record. The COUNTED SET is the path records
    under those two keys in THAT block. The GOVERNING SENTENCE is the
    nearest preceding non-empty line stating a count, and no other.
    """
    lines = text.split("\n")
    starts = [
        n
        for n, line in enumerate(lines)
        if re.match(r"^\s+add:\s*$", line) or re.match(r"^\s+add:\s*\[\]\s*$", line)
    ]
    if len(starts) != 1:
        return {"parse": "NOT_PARSEABLE", "detail": f"{len(starts)} 'add:' records"}
    start = starts[0]
    indent = len(lines[start]) - len(lines[start].lstrip())
    counted: list[str] = []
    key = None
    for n in range(start, len(lines)):
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
        if re.match(r"^(add|modify|forbidden_operations):", stripped):
            key = stripped.split(":", 1)[0]
            tail = stripped.split(":", 1)[1].strip()
            if key in ("add", "modify") and tail and tail != "[]":
                counted.append(tail)
            continue
        if key in ("add", "modify"):
            counted.append(stripped)
    governing = None
    governing_line = None
    for n in range(start - 1, -1, -1):
        if not lines[n].strip():
            continue
        match = _COUNT.search(lines[n])
        if match:
            governing = match
            governing_line = n
            break
        if lines[n].strip().startswith("#"):
            break
    if governing is None:
        return {"parse": "NOT_PARSEABLE", "detail": "no governing count sentence"}
    stated_total = 0
    for token, _noun in _COUNT.findall(lines[governing_line]):
        stated_total += _count_value(token)
    return {
        "parse": "OK",
        "counted_set": counted,
        "counted": len(counted),
        "governing_sentence": lines[governing_line].strip(),
        "stated": stated_total,
    }


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
    bad = [f for f in findings if f["counted"] != f["stated"]]
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
    repo: Path, base: str, head: str, commits: list[str], declared: Any
) -> dict[str, Any]:
    if declared is None:
        return _result("P3", "append-only on both measures", "NOT_DECLARED", {},
                       "no append_only_paths supplied; the set is not inferred")
    paths = [normalize_repo_path(p) for p in declared]
    if not paths:
        return _result("P3", "append-only on both measures", "NOT_APPLICABLE",
                       {"declared": []},
                       "caller declared an empty append-only set for this range")
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
    return _result("P3", "append-only on both measures", status, findings)


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
GATE_HEADING = re.compile(r"^## (P2-[A-Z0-9-]+)\s*$")


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


def check_p7(
    repo: Path, base: str, head: str, gates_path: str, authorised: Any
) -> dict[str, Any]:
    if authorised is None:
        return _result("P7", "gate integrity", "NOT_DECLARED", {},
                       "no authorised_modified_gates supplied; the set is not "
                       "inferred")
    if not path_exists_at_revision(repo, base, gates_path):
        return _result("P7", "gate integrity", "NOT_APPLICABLE",
                       {"gates_path": gates_path}, "gate file absent at base")
    before = gate_sections(repo, base, gates_path)
    after = gate_sections(repo, head, gates_path)
    allowed = set(authorised)
    changed = [
        name
        for name in sorted(set(before) & set(after))
        if before[name] != after[name] and name not in allowed
    ]
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    evidence = {
        "gates_path": gates_path,
        "authorised_modified": sorted(allowed),
        "section_count_base": len(before),
        "section_count_head": len(after),
        "unauthorised_changed": changed,
        "added_sections": added,
        "removed_sections": removed,
    }
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

    properties = [
        check_p1(repo, config.get("specification_paths") or _added_specs(
            repo, commits), head_sha),
        check_p2(repo, own, in_scope),
        check_p3(repo, base_sha, head_sha, commits, config.get("append_only_paths")),
        check_p4(repo, head_sha,
                 config.get("register_path", "docs/BRANCHING_POLICY.md")),
        check_p5(repo, own, config.get("recorded_merge_facts")),
        check_p6(repo, commits),
        check_p7(repo, base_sha, head_sha, config.get("gates_path", "GATES.md"),
                 config.get("authorised_modified_gates")),
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
