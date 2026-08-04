"""Evaluate the deliberately bounded machine criteria language."""

from __future__ import annotations

import argparse
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
    sha256,
)


def _invalid(identifier: str, reason: str) -> dict[str, str]:
    return {
        "id": identifier,
        "classification": "INVALID_OR_UNDERSPECIFIED",
        "reason": reason,
    }


def evaluate(repo: Path, document: dict[str, Any]) -> dict[str, Any]:
    criteria = document.get("criteria")
    if not isinstance(criteria, list):
        raise InputError("criteria must be a list")
    results: list[dict[str, Any] | None] = [None] * len(criteria)
    hashes: dict[str, tuple[str, int]] = {}
    required: dict[str, int] = {}
    forbidden: dict[str, int] = {}
    for index, item in enumerate(criteria):
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("id"), str)
            or not isinstance(item.get("kind"), str)
        ):
            results[index] = _invalid(
                f"criterion-{index}", "criterion needs id and kind"
            )
            continue
        identifier, kind = item["id"], item["kind"]
        if kind == "file_hash":
            if not isinstance(item.get("path"), str) or not isinstance(
                item.get("sha256"), str
            ):
                results[index] = _invalid(
                    identifier, "file_hash requires path and sha256"
                )
            elif item["path"] in hashes and hashes[item["path"]][0] != item["sha256"]:
                other = hashes[item["path"]][1]
                results[index] = {
                    "id": identifier,
                    "classification": "CONTRADICTORY",
                    "conflicts_with": criteria[other]["id"],
                }
                results[other] = {
                    "id": criteria[other]["id"],
                    "classification": "CONTRADICTORY",
                    "conflicts_with": identifier,
                }
            else:
                hashes[item["path"]] = (item["sha256"], index)
        elif kind == "changed_files":
            if not isinstance(item.get("base"), str) or not isinstance(
                item.get("head"), str
            ):
                results[index] = _invalid(
                    identifier, "changed_files requires base and head"
                )
                continue
            for path in item.get("required_paths", []):
                if path in forbidden:
                    other = forbidden[path]
                    results[index] = {
                        "id": identifier,
                        "classification": "CONTRADICTORY",
                        "conflicts_with": criteria[other]["id"],
                        "path": path,
                    }
                    results[other] = {
                        "id": criteria[other]["id"],
                        "classification": "CONTRADICTORY",
                        "conflicts_with": identifier,
                        "path": path,
                    }
                required[path] = index
            for path in item.get("forbidden_paths", []):
                if path in required:
                    other = required[path]
                    results[index] = {
                        "id": identifier,
                        "classification": "CONTRADICTORY",
                        "conflicts_with": criteria[other]["id"],
                        "path": path,
                    }
                    results[other] = {
                        "id": criteria[other]["id"],
                        "classification": "CONTRADICTORY",
                        "conflicts_with": identifier,
                        "path": path,
                    }
                forbidden[path] = index
        elif kind == "prefix_hash" and "boundary" not in item:
            results[index] = _invalid(identifier, "undeclared region boundary")
        elif kind not in {"file_hash", "changed_files", "prefix_hash"}:
            results[index] = _invalid(identifier, f"unsupported criterion kind {kind}")
    for index, item in enumerate(criteria):
        if results[index] is not None:
            continue
        identifier, kind = item["id"], item["kind"]
        if kind == "file_hash":
            actual = sha256(blob(repo, item.get("revision", "HEAD"), item["path"]))
            results[index] = {
                "id": identifier,
                "classification": "SATISFIED"
                if actual == item["sha256"]
                else "UNSATISFIED",
                "actual": actual,
                "expected": item["sha256"],
            }
        elif kind == "changed_files":
            actual = set(
                str(
                    git(repo, "diff", "--name-only", item["base"], item["head"])
                ).splitlines()
            )
            missing = sorted(set(item.get("required_paths", [])) - actual)
            prohibited = sorted(set(item.get("forbidden_paths", [])) & actual)
            results[index] = {
                "id": identifier,
                "classification": "SATISFIED"
                if not missing and not prohibited
                else "UNSATISFIED",
                "missing": missing,
                "forbidden_present": prohibited,
            }
        else:
            boundary = item["boundary"]
            if not isinstance(boundary, dict) or not isinstance(
                boundary.get("line_count"), int
            ):
                results[index] = _invalid(identifier, "boundary requires line_count")
                continue
            base = blob(repo, item["base"], item["path"])
            head = blob(repo, item.get("head", "HEAD"), item["path"])
            actual = sha256(
                b"".join(head.splitlines(keepends=True)[: boundary["line_count"]])
            )
            expected = sha256(base)
            results[index] = {
                "id": identifier,
                "classification": "SATISFIED" if actual == expected else "UNSATISFIED",
                "actual": actual,
                "expected": expected,
            }
    completed = [result for result in results if result is not None]
    overall = (
        "PASS"
        if all(result["classification"] == "SATISFIED" for result in completed)
        else "FAIL"
    )
    return {
        "tool": "spec_consistency_checker",
        "criteria": completed,
        "overall": overall,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--spec", required=True)
    args = parser.parse_args(argv)
    try:
        result = evaluate(Path(args.repo), load_json(args.spec))
        return emit(result, 0 if result["overall"] == "PASS" else GOVERNANCE_FAILURE)
    except (InputError, OSError) as error:
        return emit(
            {
                "tool": "spec_consistency_checker",
                "overall": "TOOL_ERROR",
                "error": str(error),
            },
            TOOL_ERROR,
        )


if __name__ == "__main__":
    raise SystemExit(main())
