"""Candidate discovery for P2-PROVENANCE-CENSUS-01.

Reads the FROZEN SCOPE at a named revision and emits candidate passages that
cite, describe, or rely on an adjudication, ruling, PI decision, or ratified
disposition.

The script DISCOVERS candidates. It classifies nothing: membership of ``S_A``
and of ``S_P`` is decided by reading, under the specification's section 3, and
this file deliberately contains no class vocabulary.

Content is read from ``git cat-file blob <rev>:<path>`` so that the measurement
is over committed bytes at a stated revision rather than over a worktree.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

# The frozen scope, from the specification's section 1. Directories are walked
# at the revision; the three files are named because they sit at the root.
SCOPE_DIRS = ("specs/", "derivations/", "decisions/", "docs/")
SCOPE_FILES = ("CONVENTIONS.md", "GATES.md", "DECISION_LOG.md")
NOT_SEARCHED = ("reviews/", "reports/")

# Five search forms. Each is named, and each carries the exclusions applied to
# it, so that the search is reproducible and its blind spots are visible.
FORMS = {
    "A_NUMBERED": {
        "pattern": r"\b(?:PI\s+)?(?:ruling|adjudication|decision)s?\s+"
                   r"(?:item\s+)?(\d{1,2})\b",
        "describes": "a citation identifying an adjudication by number",
        "exclusions": [
            "a following four-digit year, so that 'decision 2026-08-06' is a "
            "date reference and not a numbered citation",
            "'Rule N' and 'Amendment X', which name governance rules rather "
            "than adjudications",
        ],
    },
    "B_LABELLED": {
        "pattern": r"PI RULING|(?:adopted|registered|recorded|reproduced)\s+verbatim",
        "describes": "a block labelled as carrying or reproducing a ruling",
        "exclusions": [
            "'verbatim' unqualified by one of the four verbs, which in this "
            "repository is ordinary usage about preserved text",
        ],
    },
    "C_PI_ACT": {
        "pattern": r"\bPI\s+(?:ruled|decided|decides|agreed|directed|confirmed|"
                   r"ratified|adjudicated|accepted|authoris\w*|authoriz\w*)\b"
                   r"|\bPI-(?:confirmed|ratified|authoris\w*|authoriz\w*|"
                   r"supplied|VERIFIED|level)\b",
        "describes": "prose asserting that the PI performed an adjudicative act",
        "exclusions": [
            "'PI' as part of a longer token, excluded by the word boundary",
        ],
    },
    "D_INDIRECT": {
        "pattern": r"\b(?:was|were|has been|had been|is)\s+ruled\b"
                   r"|\bby\s+PI\s+(?:decision|ruling|adjudication)\b"
                   r"|\bPI\s+(?:decision|ruling|adjudication)s?\b"
                   r"|\bthe\s+PI\s+(?:has|so|now)\b",
        "describes": "an indirect or passive assertion that an adjudication "
                     "occurred, including references to the act as a noun",
        "exclusions": [
            "'ruled' with no adjudicative subject, e.g. 'ruled open' is kept "
            "and read, while 'ruler' and 'ruled out' are excluded by the "
            "word boundary and the verb list",
        ],
    },
    "E_REGISTER": {
        "pattern": r"\bdecisions/|\breviews/pi/",
        "describes": "a pointer to a register where adjudications are filed",
        "exclusions": [
            "none applied at match time; a bare directory mention that cites "
            "no particular adjudication is excluded by reading, not by regex",
        ],
    },
}

_YEAR = re.compile(r"\d{4}")


def git(*args: str) -> str:
    out = subprocess.run(("git",) + args, capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def scope_paths(rev: str) -> list[str]:
    paths = git("ls-tree", "-r", "--name-only", rev, "--", *SCOPE_DIRS).split()
    return sorted(paths + list(SCOPE_FILES))


def blob(rev: str, path: str) -> list[str]:
    return git("cat-file", "blob", f"{rev}:{path}").split("\n")


def excluded(form: str, line: str, match: re.Match) -> bool:
    if form == "A_NUMBERED":
        tail = line[match.start():match.start() + 40]
        if _YEAR.search(tail):
            return True
    return False


def scan(rev: str) -> dict:
    compiled = {k: re.compile(v["pattern"]) for k, v in FORMS.items()}
    hits: dict[tuple[str, int], dict] = {}
    for path in scope_paths(rev):
        for n, line in enumerate(blob(rev, path), start=1):
            for form, rx in compiled.items():
                m = rx.search(line)
                if not m or excluded(form, line, m):
                    continue
                key = (path, n)
                rec = hits.setdefault(key, {"path": path, "line": n,
                                            "text": line, "forms": []})
                rec["forms"].append(form)
    return {
        "revision": rev,
        "scope_dirs": list(SCOPE_DIRS),
        "scope_files": list(SCOPE_FILES),
        "not_searched": list(NOT_SEARCHED),
        "files_scanned": len(scope_paths(rev)),
        "forms": FORMS,
        "hits": [hits[k] for k in sorted(hits)],
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rev", required=True, help="revision whose blobs are read")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    result = scan(args.rev)
    args.out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    per_form: dict[str, int] = {}
    for h in result["hits"]:
        for f in h["forms"]:
            per_form[f] = per_form.get(f, 0) + 1
    print(f"revision      {result['revision']}")
    print(f"files scanned {result['files_scanned']}")
    print(f"unique hits   {len(result['hits'])}")
    for f in FORMS:
        print(f"  {f:<12} {per_form.get(f, 0)}")


if __name__ == "__main__":
    main()
