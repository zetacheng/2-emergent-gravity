"""Check declared content conditions in one UTF-8 text file."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .core import GOVERNANCE_FAILURE, TOOL_ERROR, InputError, emit, load_json

MATCH_MODES = {"substring", "line_substring", "exact_line"}


def _entry(item: Any, label: str) -> tuple[str, str]:
    if isinstance(item, str):
        return item, "substring"
    if isinstance(item, dict) and isinstance(item.get("value"), str):
        mode = item.get("match_mode", "substring")
        if mode not in MATCH_MODES:
            raise InputError(f"{label} match_mode must be one of {sorted(MATCH_MODES)}")
        return item["value"], mode
    raise InputError(f"{label} entries require a string or {{value, match_mode}}")


def _count(text: str, lines: list[str], value: str, mode: str) -> int:
    if mode == "substring":
        return text.count(value)
    if mode == "line_substring":
        return sum(value in line for line in lines)
    return sum(line == value for line in lines)


def evaluate_content(manifest: dict[str, Any]) -> dict[str, Any]:
    path = manifest.get("file")
    if not isinstance(path, str):
        raise InputError("content manifest requires file")
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    checks: list[dict[str, Any]] = []
    for item in manifest.get("required_literals", []):
        value, match_mode = _entry(item, "required_literals")
        count = _count(text, lines, value, match_mode)
        checks.append(
            {
                "kind": "required_literal",
                "value": value,
                "count": count,
                "match_mode": match_mode,
                "status": "PASS" if count else "FAIL",
            }
        )
    for item in manifest.get("forbidden_literals", []):
        value, match_mode = _entry(item, "forbidden_literals")
        count = _count(text, lines, value, match_mode)
        checks.append(
            {
                "kind": "forbidden_literal",
                "value": value,
                "count": count,
                "match_mode": match_mode,
                "status": "PASS" if not count else "FAIL",
            }
        )
    positions: list[int] = []
    for heading in manifest.get("headings", []):
        if not isinstance(heading, str):
            raise InputError("headings must be literal heading strings")
        found = [index for index, line in enumerate(lines) if line == heading]
        positions.append(found[0] if len(found) == 1 else -1)
        checks.append(
            {
                "kind": "heading",
                "value": heading,
                "count": len(found),
                "status": "PASS" if len(found) == 1 else "FAIL",
            }
        )
    for prefix in manifest.get("heading_prefixes", []):
        if not isinstance(prefix, str):
            raise InputError("heading_prefixes must be literal strings")
        found = [index for index, line in enumerate(lines) if line.startswith(prefix)]
        positions.append(found[0] if len(found) == 1 else -1)
        checks.append(
            {
                "kind": "heading_prefix",
                "value": prefix,
                "count": len(found),
                "status": "PASS" if len(found) == 1 else "FAIL",
            }
        )
    if manifest.get("headings") or manifest.get("heading_prefixes"):
        ordered = positions == sorted(positions) and all(
            position >= 0 for position in positions
        )
        checks.append(
            {
                "kind": "heading_order",
                "positions": positions,
                "status": "PASS" if ordered else "FAIL",
            }
        )
    overall = "PASS" if all(check["status"] == "PASS" for check in checks) else "FAIL"
    return {
        "tool": "content_checker",
        "file": path,
        "checks": checks,
        "overall": overall,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args(argv)
    try:
        result = evaluate_content(load_json(args.manifest))
        return emit(result, 0 if result["overall"] == "PASS" else GOVERNANCE_FAILURE)
    except (InputError, OSError, UnicodeError) as error:
        return emit(
            {"tool": "content_checker", "overall": "TOOL_ERROR", "error": str(error)},
            TOOL_ERROR,
        )


if __name__ == "__main__":
    raise SystemExit(main())
