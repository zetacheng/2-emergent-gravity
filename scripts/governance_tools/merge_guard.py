"""Read-only pre-merge and post-merge governance checks."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .core import (
    GOVERNANCE_FAILURE,
    TOOL_ERROR,
    InputError,
    emit,
    evaluate_scope,
    git,
    load_json,
    resolve,
    verify_pins,
)


def _scope(repo: Path, config: dict[str, Any]) -> dict[str, Any]:
    scope = config.get("scope_manifest")
    if isinstance(scope, str):
        return evaluate_scope(repo, load_json(scope))
    if isinstance(scope, dict):
        return evaluate_scope(repo, scope)
    raise InputError("merge guard requires scope_manifest object or path")


def _pins(repo: Path, revision: str, config: dict[str, Any]) -> list[dict[str, Any]]:
    return verify_pins(repo, revision, config.get("pinned_artifacts", []))


def pre_merge(repo: Path, config: dict[str, Any]) -> dict[str, Any]:
    worktree = config.get("worktree")
    branch = config.get("reviewed_branch")
    base = config.get("reviewed_base")
    merge_base = config.get("expected_merge_base")
    if not all(
        isinstance(value, str) for value in (worktree, branch, base, merge_base)
    ):
        raise InputError(
            "pre-merge requires worktree, reviewed_branch, reviewed_base, "
            "expected_merge_base"
        )
    status = str(git(worktree, "status", "--porcelain")).splitlines()
    worktree_head = resolve(worktree, "HEAD")
    branch_head = resolve(repo, branch)
    allow_detached = bool(config.get("allow_equivalent_detached_head", False))
    actual_merge_base = str(git(repo, "merge-base", base, branch)).strip()
    checks = [
        {
            "condition": "worktree_clean",
            "status": "PASS" if not status else "FAIL",
            "entries": status,
        },
        {
            "condition": "worktree_matches_reviewed_branch",
            "status": "PASS"
            if worktree_head == branch_head or allow_detached
            else "FAIL",
            "worktree_head": worktree_head,
            "reviewed_branch_head": branch_head,
        },
        {
            "condition": "merge_base",
            "status": "PASS" if actual_merge_base == merge_base else "FAIL",
            "actual": actual_merge_base,
            "expected": merge_base,
        },
    ]
    scope = _scope(repo, config)
    checks.append({"condition": "scope", "status": scope["overall"], "evidence": scope})
    pins = _pins(repo, branch_head, config)
    checks.append(
        {
            "condition": "pinned_artifacts",
            "status": "PASS"
            if all(pin["status"] == "PASS" for pin in pins)
            else "FAIL",
            "evidence": pins,
        }
    )
    return {
        "tool": "merge_guard",
        "mode": "PRE_MERGE",
        "checks": checks,
        "other_registered_worktrees": str(git(repo, "worktree", "list")).splitlines(),
        "overall": "PASS"
        if all(item["status"] == "PASS" for item in checks)
        else "FAIL",
    }


def post_merge(repo: Path, config: dict[str, Any]) -> dict[str, Any]:
    merge = config.get("merge_commit")
    parent1 = config.get("expected_parent_1")
    parent2 = config.get("expected_parent_2")
    merge_base = config.get("expected_merge_base")
    if not all(
        isinstance(value, str) for value in (merge, parent1, parent2, merge_base)
    ):
        raise InputError(
            "post-merge requires merge_commit and all expected parent values"
        )
    parents = str(git(repo, "show", "-s", "--format=%P", merge)).strip().split()
    actual_merge_base = str(git(repo, "merge-base", parent1, parent2)).strip()
    checks = [
        {
            "condition": "exactly_two_parents",
            "status": "PASS" if len(parents) == 2 else "FAIL",
            "actual": parents,
        },
        {
            "condition": "parent_1",
            "status": "PASS" if parents[:1] == [resolve(repo, parent1)] else "FAIL",
            "expected": resolve(repo, parent1),
        },
        {
            "condition": "parent_2",
            "status": "PASS" if parents[1:2] == [resolve(repo, parent2)] else "FAIL",
            "expected": resolve(repo, parent2),
        },
        {
            "condition": "merge_base",
            "status": "PASS"
            if actual_merge_base == resolve(repo, merge_base)
            else "FAIL",
            "actual": actual_merge_base,
            "expected": resolve(repo, merge_base),
        },
    ]
    scope = _scope(repo, config)
    checks.append(
        {
            "condition": "merged_tree_scope",
            "status": scope["overall"],
            "evidence": scope,
        }
    )
    pins = _pins(repo, resolve(repo, merge), config)
    checks.append(
        {
            "condition": "pinned_artifacts",
            "status": "PASS"
            if all(pin["status"] == "PASS" for pin in pins)
            else "FAIL",
            "evidence": pins,
        }
    )
    policy = config.get("remote_check_policy")
    if policy == "NOT_APPLICABLE_HISTORICAL_FIXTURE":
        checks.append({"condition": "remote_agreement", "status": "NOT_EVALUATED"})
    elif policy == "REQUIRED":
        ref, expected = (
            config.get("expected_remote_ref"),
            config.get("expected_remote_sha"),
        )
        if not isinstance(ref, str) or not isinstance(expected, str):
            raise InputError(
                "REQUIRED remote policy needs expected_remote_ref and "
                "expected_remote_sha"
            )
        actual = resolve(repo, ref)
        checks.append(
            {
                "condition": "remote_agreement",
                "status": "PASS" if actual == expected else "FAIL",
                "actual": actual,
                "expected": expected,
            }
        )
    else:
        raise InputError(
            "remote_check_policy must be REQUIRED or NOT_APPLICABLE_HISTORICAL_FIXTURE"
        )
    evaluated = [item for item in checks if item["status"] != "NOT_EVALUATED"]
    return {
        "tool": "merge_guard",
        "mode": "POST_MERGE",
        "checks": checks,
        "overall": "PASS"
        if all(item["status"] == "PASS" for item in evaluated)
        else "FAIL",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    try:
        config = load_json(args.config)
        mode = config.get("mode")
        result = (
            pre_merge(Path(args.repo), config)
            if mode == "PRE_MERGE"
            else post_merge(Path(args.repo), config)
            if mode == "POST_MERGE"
            else None
        )
        if result is None:
            raise InputError("mode must be PRE_MERGE or POST_MERGE")
        return emit(result, 0 if result["overall"] == "PASS" else GOVERNANCE_FAILURE)
    except (InputError, OSError) as error:
        return emit(
            {"tool": "merge_guard", "overall": "TOOL_ERROR", "error": str(error)},
            TOOL_ERROR,
        )


if __name__ == "__main__":
    raise SystemExit(main())
