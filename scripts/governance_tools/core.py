"""Shared implementation for the read-only governance CLIs.

Exit codes: 0 means every evaluated condition passed; 2 means a governance
condition failed; 3 means malformed input or an internal tool error.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any

GOVERNANCE_FAILURE = 2
TOOL_ERROR = 3


class InputError(ValueError):
    """A manifest is malformed or cannot be resolved."""


def load_json(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise InputError(f"cannot read JSON manifest {path}: {error}") from error
    if not isinstance(value, dict):
        raise InputError("manifest root must be an object")
    return value


def emit(result: dict[str, Any], exit_code: int) -> int:
    print(json.dumps(result, indent=2, sort_keys=True))
    return exit_code


def git(repo: str | Path, *args: str, text: bool = True) -> str | bytes:
    command = ["git", "-C", str(repo), *args]
    completed = subprocess.run(command, capture_output=True, check=False)
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise InputError(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout.decode("utf-8") if text else completed.stdout


def resolve(repo: str | Path, revision: str) -> str:
    return str(git(repo, "rev-parse", "--verify", f"{revision}^{{commit}}")).strip()


def normalize_repo_path(path: str) -> str:
    """Return one canonical repository-relative POSIX path."""
    if not isinstance(path, str) or not path:
        raise InputError("repository path must be a non-empty string")
    normalized = PurePosixPath(path.replace("\\", "/"))
    if normalized.is_absolute() or ".." in normalized.parts or str(normalized) == ".":
        raise InputError(f"path is not repository-relative: {path}")
    return normalized.as_posix()


def blob(repo: str | Path, revision: str, path: str) -> bytes:
    return bytes(git(repo, "show", f"{revision}:{path}", text=False))


def path_exists_at_revision(repo: str | Path, revision: str, path: str) -> bool:
    """Check a tree entry without reading its blob content."""
    listing = bytes(git(repo, "ls-tree", "-z", revision, "--", path, text=False))
    return bool(listing)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def operation_from_status(status: str) -> str:
    mapping = {
        "A": "add",
        "M": "modify",
        "D": "delete",
        "R": "rename",
        "C": "copy",
        "T": "type_change",
        "U": "unmerged",
    }
    return mapping.get(status[:1], "unknown")


def changed_operations(repo: str | Path, base: str, head: str) -> list[dict[str, str]]:
    raw = bytes(
        git(
            repo,
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            "--find-copies",
            base,
            head,
            text=False,
        )
    )
    fields = raw.decode("utf-8", errors="strict").split("\0")
    if fields and fields[-1] == "":
        fields.pop()
    records: list[dict[str, str]] = []
    index = 0
    while index < len(fields):
        status = fields[index]
        index += 1
        op = operation_from_status(status)
        if op in {"rename", "copy"}:
            if index + 1 >= len(fields):
                raise InputError(f"truncated {op} record from git diff")
            records.append(
                {
                    "operation": op,
                    "from": fields[index],
                    "to": fields[index + 1],
                }
            )
            index += 2
        else:
            if index >= len(fields):
                raise InputError(f"truncated {op} record from git diff")
            records.append({"operation": op, "path": fields[index]})
            index += 1
    return records


def operation_key(record: dict[str, str]) -> tuple[str, str, str]:
    operation = record.get("operation", "")
    if operation in {"rename", "copy"}:
        return operation, record.get("from", ""), record.get("to", "")
    return operation, record.get("path", ""), ""


def validate_operation(record: Any) -> dict[str, str]:
    if not isinstance(record, dict) or not isinstance(record.get("operation"), str):
        raise InputError("operation entries require an operation string")
    op = record["operation"]
    if op in {"rename", "copy"}:
        if not all(isinstance(record.get(key), str) for key in ("from", "to")):
            raise InputError(f"{op} entries require from and to")
        return {
            "operation": op,
            "from": normalize_repo_path(record["from"]),
            "to": normalize_repo_path(record["to"]),
        }
    if not isinstance(record.get("path"), str):
        raise InputError(f"{op} entries require path")
    return {"operation": op, "path": normalize_repo_path(record["path"])}


def evaluate_scope(repo: str | Path, manifest: dict[str, Any]) -> dict[str, Any]:
    base = manifest.get("base")
    head = manifest.get("head")
    if not isinstance(base, str) or not isinstance(head, str):
        raise InputError("scope manifest requires base and head revisions")
    required = [validate_operation(item) for item in manifest.get("required", [])]
    optional = [validate_operation(item) for item in manifest.get("optional", [])]
    forbidden_ops = manifest.get("forbidden_operations", [])
    if not isinstance(forbidden_ops, list) or not all(
        isinstance(x, str) for x in forbidden_ops
    ):
        raise InputError("forbidden_operations must be a list of operation names")
    mode = manifest.get("mode", "exact")
    if mode not in {"exact", "subset"}:
        raise InputError("scope mode must be exact or subset")
    resolved_base, resolved_head = resolve(repo, base), resolve(repo, head)
    observed = changed_operations(repo, resolved_base, resolved_head)
    observed_keys = {operation_key(item) for item in observed}
    required_keys = {operation_key(item) for item in required}
    optional_keys = {operation_key(item) for item in optional}
    failures: list[str] = []
    for item in observed:
        if item["operation"] in forbidden_ops:
            failures.append(f"forbidden operation observed: {item}")
    for key in observed_keys - required_keys - optional_keys:
        observed_record = next(item for item in observed if operation_key(item) == key)
        observed_path = observed_record.get("path") or observed_record.get("to")
        expected_record = next(
            (
                item
                for item in required + optional
                if (item.get("path") or item.get("to")) == observed_path
            ),
            None,
        )
        if expected_record is not None:
            failures.append(
                f"expected {expected_record['operation']}, observed "
                f"{observed_record['operation']}: {observed_path}"
            )
        else:
            failures.append(f"outside declared scope: {key}")
    if mode == "exact":
        for key in required_keys - observed_keys:
            failures.append(f"required operation missing: {key}")
    result = {
        "tool": "scope_checker",
        "base": resolved_base,
        "head": resolved_head,
        "mode": mode,
        "observed_operations": observed,
        "failures": failures,
        "overall": "PASS" if not failures else "FAIL",
    }
    return result


def verify_pins(repo: str | Path, revision: str, pins: Any) -> list[dict[str, Any]]:
    if not isinstance(pins, list):
        raise InputError("pinned_artifacts must be a list")
    results: list[dict[str, Any]] = []
    for pin in pins:
        if not isinstance(pin, dict) or not isinstance(pin.get("path"), str):
            raise InputError("each pin needs path and sha256")
        expected = pin.get("sha256")
        if (
            not isinstance(expected, str)
            or len(expected) != 64
            or any(char not in "0123456789abcdefABCDEF" for char in expected)
        ):
            raise InputError("each pin needs a 64-character sha256")
        path = normalize_repo_path(pin["path"])
        resolved_revision = resolve(repo, revision)
        actual = (
            sha256(blob(repo, resolved_revision, path))
            if path_exists_at_revision(repo, resolved_revision, path)
            else None
        )
        results.append(
            {
                "path": path,
                "expected": expected,
                "actual": actual,
                "status": "PASS" if actual == expected else "FAIL",
            }
        )
    return results
