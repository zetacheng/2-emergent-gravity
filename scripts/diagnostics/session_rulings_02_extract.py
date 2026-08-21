"""Candidate-source extraction for P2-SESSION-RULINGS-02.

Reads the subject set from the LANDED census artifact and, for each citing
passage the census records, locates any delimited quotation block the passage
lies within or immediately introduces, and copies that block VERBATIM.

The script EXTRACTS. It classifies nothing: whether a located block presents
the adjudication's own words, rather than a description of them, is decided by
reading under the specification's `E3`, and this file contains no class
vocabulary for that judgement.

`E1` requires extraction rather than transcription. A block is therefore
located by its own delimiters and copied byte for byte from the blob; no line
is retyped, no ellipsis filled, no bracket expanded (`E4`).

`E2` requires one block per candidate in one artifact. This file never
concatenates two blocks, and never returns a span assembled from more than one
contiguous run.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

CENSUS = "derivations/P2-PROVENANCE-CENSUS-01_census.md"

# How far from a citing passage a block may begin and still count as one the
# passage introduces. A label line and a blank line is two; the window allows
# for a heading plus a "recorded verbatim" line plus blanks.
INTRO_WINDOW = 8


def git(*args: str) -> bytes:
    return subprocess.run(("git",) + args, capture_output=True, check=True).stdout


def blob_bytes(rev: str, path: str) -> bytes:
    return git("cat-file", "blob", f"{rev}:{path}")


def subject_set(rev: str) -> dict[str, dict]:
    """Read M1's set from the census artifact. Adds and removes nothing."""
    text = blob_bytes(rev, CENSUS).decode("utf-8")
    members: dict[str, dict] = {}
    current = None
    in_cited = False
    for line in text.split("\n"):
        m = re.match(r"^### `(ADJ-\d+)` — (.*)$", line)
        if m:
            current = m.group(1)
            members[current] = {"id": current, "title": m.group(2), "cited": []}
            in_cited = False
            continue
        if current is None:
            continue
        if line.startswith("**Cited at:**"):
            in_cited = True
            continue
        if in_cited:
            c = re.match(r"^    (\S+):(\d+)$", line)
            if c:
                members[current]["cited"].append((c.group(1), int(c.group(2))))
            elif line.startswith("### ") or line.startswith("**How "):
                in_cited = False
    return members


def blocks_in(lines: list[str]) -> list[tuple[int, int]]:
    """Every maximal contiguous run of blockquote lines, 1-indexed inclusive."""
    runs, start = [], None
    for i, line in enumerate(lines, start=1):
        if line.startswith(">"):
            if start is None:
                start = i
        else:
            if start is not None:
                runs.append((start, i - 1))
                start = None
    if start is not None:
        runs.append((start, len(lines)))
    return runs


def locate(rev: str, path: str, line: int) -> tuple[int, int] | None:
    """The block this passage lies within, or the next one it introduces."""
    lines = blob_bytes(rev, path).decode("utf-8").split("\n")
    for lo, hi in blocks_in(lines):
        if lo <= line <= hi:
            return (lo, hi)
    for lo, hi in blocks_in(lines):
        if 0 < lo - line <= INTRO_WINDOW:
            return (lo, hi)
    return None


def extract(rev: str, path: str, lo: int, hi: int) -> dict:
    """Copy the block byte for byte. Nothing is normalised or supplied."""
    raw = blob_bytes(rev, path)
    lines = raw.decode("utf-8").split("\n")
    block = "\n".join(lines[lo - 1:hi])
    return {
        "path": path,
        "line_span": f"{lo}-{hi}",
        "bytes": len(block.encode("utf-8")),
        "method": "git cat-file blob <rev>:<path>, split on newline, slice "
                  "[lo-1:hi] by the block's own delimiter bounds, joined on "
                  "newline; no line retyped, nothing normalised",
        "text": block,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rev", required=True)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    members = subject_set(args.rev)
    result = {"revision": args.rev, "census": CENSUS, "members": []}
    for mid, m in members.items():
        rec = {"id": mid, "title": m["title"], "passages": []}
        for path, line in m["cited"]:
            span = locate(args.rev, path, line)
            entry = {"path": path, "line": line, "block": None}
            if span:
                entry["block"] = extract(args.rev, path, *span)
            rec["passages"].append(entry)
        result["members"].append(rec)
    args.out.write_text(json.dumps(result, indent=1, ensure_ascii=False),
                        encoding="utf-8")

    print(f"revision {args.rev}")
    print(f"members  {len(result['members'])}")
    for rec in result["members"]:
        withblk = sum(1 for p in rec["passages"] if p["block"])
        print(f"  {rec['id']}  passages {len(rec['passages'])}  "
              f"with a located block {withblk}")


if __name__ == "__main__":
    main()
