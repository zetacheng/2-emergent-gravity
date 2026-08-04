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
    normalize_repo_path,
    path_exists_at_revision,
    resolve,
    sha256,
)


def _invalid(identifier: str, reason: str) -> dict[str, str]:
    return {
        "id": identifier,
        "classification": "INVALID_OR_UNDERSPECIFIED",
        "reason": reason,
    }


def _sha256_literal(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(char in "0123456789abcdefABCDEF" for char in value)
    )


def _string_list(value: Any) -> list[str] | None:
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    return None


def evaluate(repo: Path, document: dict[str, Any]) -> dict[str, Any]:
    criteria = document.get("criteria")
    if not isinstance(criteria, list):
        raise InputError("criteria must be a list")
    if not criteria:
        return {
            "tool": "spec_consistency_checker",
            "criteria": [_invalid("document", "criteria list must not be empty")],
            "overall": "FAIL",
        }
    identifiers = [item.get("id") for item in criteria if isinstance(item, dict)]
    duplicate_ids = {
        identifier for identifier in identifiers if identifiers.count(identifier) > 1
    }
    if duplicate_ids:
        reason = f"duplicate criterion IDs: {', '.join(sorted(duplicate_ids))}"
        return {
            "tool": "spec_consistency_checker",
            "criteria": [
                _invalid(str(item.get("id", f"criterion-{index}")), reason)
                for index, item in enumerate(criteria)
            ],
            "overall": "FAIL",
        }
    results: list[dict[str, Any] | None] = [None] * len(criteria)
    hashes: dict[tuple[str, str, str], tuple[str, int]] = {}
    required: dict[tuple[str, str, str, str], int] = {}
    forbidden: dict[tuple[str, str, str, str], int] = {}
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
            if not isinstance(item.get("path"), str) or not _sha256_literal(
                item.get("sha256")
            ):
                results[index] = _invalid(
                    identifier, "file_hash requires path and a 64-hex sha256"
                )
                continue
            revision = item.get("revision", "HEAD")
            if not isinstance(revision, str):
                results[index] = _invalid(
                    identifier, "file_hash revision must be a string"
                )
                continue
            path = normalize_repo_path(item["path"])
            domain = (kind, resolve(repo, revision), path)
            if domain in hashes and hashes[domain][0].lower() != item["sha256"].lower():
                other = hashes[domain][1]
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
            else:
                hashes[domain] = (item["sha256"], index)
        elif kind == "changed_files":
            required_paths = _string_list(item.get("required_paths", []))
            forbidden_paths = _string_list(item.get("forbidden_paths", []))
            if (
                not isinstance(item.get("base"), str)
                or not isinstance(item.get("head"), str)
                or required_paths is None
                or forbidden_paths is None
            ):
                results[index] = _invalid(
                    identifier,
                    "changed_files requires base, head, and string path lists",
                )
                continue
            resolved_base, resolved_head = (
                resolve(repo, item["base"]),
                resolve(repo, item["head"]),
            )
            for raw_path in required_paths:
                path = normalize_repo_path(raw_path)
                domain = (kind, resolved_base, resolved_head, path)
                if domain in forbidden:
                    other = forbidden[domain]
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
                required[domain] = index
            for raw_path in forbidden_paths:
                path = normalize_repo_path(raw_path)
                domain = (kind, resolved_base, resolved_head, path)
                if domain in required:
                    other = required[domain]
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
                forbidden[domain] = index
        elif kind == "prefix_hash":
            boundary = item.get("boundary")
            if "boundary" not in item:
                results[index] = _invalid(identifier, "undeclared region boundary")
            elif not isinstance(item.get("path"), str) or not isinstance(
                item.get("base"), str
            ):
                results[index] = _invalid(
                    identifier, "prefix_hash requires path and base"
                )
            elif (
                not isinstance(boundary, dict)
                or not isinstance(boundary.get("line_count"), int)
                or boundary["line_count"] < 0
            ):
                results[index] = _invalid(
                    identifier, "boundary requires non-negative line_count"
                )
            else:
                normalize_repo_path(item["path"])
        elif kind not in {"file_hash", "changed_files", "prefix_hash"}:
            results[index] = _invalid(identifier, f"unsupported criterion kind {kind}")
    for index, item in enumerate(criteria):
        if results[index] is not None:
            continue
        identifier, kind = item["id"], item["kind"]
        if kind == "file_hash":
            path = normalize_repo_path(item["path"])
            revision = resolve(repo, item.get("revision", "HEAD"))
            actual = (
                sha256(blob(repo, revision, path))
                if path_exists_at_revision(repo, revision, path)
                else None
            )
            results[index] = {
                "id": identifier,
                "classification": "SATISFIED"
                if actual == item["sha256"].lower()
                else "UNSATISFIED",
                "actual": actual,
                "expected": item["sha256"],
            }
        elif kind == "changed_files":
            base, head = resolve(repo, item["base"]), resolve(repo, item["head"])
            actual = set(str(git(repo, "diff", "--name-only", base, head)).splitlines())
            required_paths = {
                normalize_repo_path(path) for path in item.get("required_paths", [])
            }
            forbidden_paths = {
                normalize_repo_path(path) for path in item.get("forbidden_paths", [])
            }
            missing = sorted(required_paths - actual)
            prohibited = sorted(forbidden_paths & actual)
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
            path = normalize_repo_path(item["path"])
            base, head = (
                resolve(repo, item["base"]),
                resolve(repo, item.get("head", "HEAD")),
            )
            if not path_exists_at_revision(
                repo, base, path
            ) or not path_exists_at_revision(repo, head, path):
                results[index] = {
                    "id": identifier,
                    "classification": "UNSATISFIED",
                    "reason": "path absent at revision",
                }
                continue
            actual = sha256(
                b"".join(
                    blob(repo, head, path).splitlines(keepends=True)[
                        : boundary["line_count"]
                    ]
                )
            )
            expected = sha256(blob(repo, base, path))
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
