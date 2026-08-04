"""Positive, negative, and historical self-application tests for governance tools."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from scripts.governance_tools.content_checker import evaluate_content
from scripts.governance_tools.core import GOVERNANCE_FAILURE
from scripts.governance_tools.merge_guard import post_merge, pre_merge
from scripts.governance_tools.scope_checker import main as scope_main
from scripts.governance_tools.spec_consistency_checker import evaluate

ROOT = Path(__file__).resolve().parents[1]
BASE = "8d48798eaa3884a0a5104d5dc19e2e836468f1aa"
MERGE = "3302b612b954af6369fc01a2e9a85cfb4f682a07"
BRANCH = "75c84226cf39f552545d953606a11df104244a03"
REVIEW = "reviews/pi/2026-08-03-outcome-based-task-specification-amendment.md"


def run(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def write_json(path: Path, value: dict) -> Path:
    path.write_text(json.dumps(value), encoding="utf-8")
    return path


def operations(*records: dict) -> dict:
    return {
        "base": "BASE",
        "head": "HEAD",
        "mode": "exact",
        "required": list(records),
        "optional": [],
        "forbidden_operations": ["delete", "rename", "type_change"],
    }


def fixture_repo(tmp_path: Path) -> tuple[Path, str, str, str]:
    repo = tmp_path / "repo"
    run(tmp_path, "init", str(repo))
    run(repo, "config", "user.email", "tests@example.invalid")
    run(repo, "config", "user.name", "Governance tests")
    (repo / "tracked.txt").write_text("base\n", encoding="utf-8")
    run(repo, "add", "tracked.txt")
    run(repo, "commit", "-m", "base")
    base = run(repo, "rev-parse", "HEAD")
    run(repo, "checkout", "-b", "reviewed")
    (repo / "tracked.txt").write_text("reviewed\n", encoding="utf-8")
    (repo / "added.txt").write_text("added\n", encoding="utf-8")
    run(repo, "add", "tracked.txt", "added.txt")
    run(repo, "commit", "-m", "reviewed")
    reviewed = run(repo, "rev-parse", "HEAD")
    return repo, base, reviewed, run(repo, "merge-base", base, reviewed)


def test_scope_checker_accepts_and_rejects_operation_taxonomy(tmp_path: Path) -> None:
    repo, base, reviewed, _ = fixture_repo(tmp_path)
    manifest = operations(
        {"operation": "modify", "path": "tracked.txt"},
        {"operation": "add", "path": "added.txt"},
    )
    manifest["base"], manifest["head"] = base, reviewed
    path = write_json(tmp_path / "scope.json", manifest)
    assert scope_main(["--repo", str(repo), "--manifest", str(path)]) == 0
    manifest["required"][0]["operation"] = "add"
    path = write_json(tmp_path / "wrong-operation.json", manifest)
    assert (
        scope_main(["--repo", str(repo), "--manifest", str(path)]) == GOVERNANCE_FAILURE
    )


def test_content_checker_rejects_required_missing_and_forbidden_present(
    tmp_path: Path,
) -> None:
    target = tmp_path / "target.md"
    target.write_text("# title\nforbidden\n### 1. One\n", encoding="utf-8")
    result = evaluate_content(
        {
            "file": str(target),
            "required_literals": ["missing"],
            "forbidden_literals": ["forbidden"],
        }
    )
    assert result["overall"] == "FAIL"
    assert {check["kind"] for check in result["checks"]} == {
        "required_literal",
        "forbidden_literal",
    }


def test_merge_guard_pre_and_post_rejects_wrong_parentage_and_scope(
    tmp_path: Path,
) -> None:
    repo, base, reviewed, merge_base = fixture_repo(tmp_path)
    scope = operations(
        {"operation": "modify", "path": "tracked.txt"},
        {"operation": "add", "path": "added.txt"},
    )
    scope["base"], scope["head"] = base, reviewed
    pre = pre_merge(
        repo,
        {
            "worktree": str(repo),
            "reviewed_branch": reviewed,
            "reviewed_base": base,
            "expected_merge_base": merge_base,
            "scope_manifest": scope,
            "pinned_artifacts": [],
        },
    )
    assert pre["overall"] == "PASS"
    run(repo, "checkout", "-b", "integration", base)
    (repo / "integration.txt").write_text("integration\n", encoding="utf-8")
    run(repo, "add", "integration.txt")
    run(repo, "commit", "-m", "integration")
    parent1 = run(repo, "rev-parse", "HEAD")
    run(repo, "merge", "--no-ff", "reviewed", "-m", "merge")
    merge = run(repo, "rev-parse", "HEAD")
    merged_scope = operations(
        {"operation": "modify", "path": "tracked.txt"},
        {"operation": "add", "path": "added.txt"},
    )
    merged_scope["base"], merged_scope["head"] = parent1, merge
    config = {
        "mode": "POST_MERGE",
        "merge_commit": merge,
        "expected_parent_1": parent1,
        "expected_parent_2": reviewed,
        "expected_merge_base": base,
        "scope_manifest": merged_scope,
        "pinned_artifacts": [],
        "remote_check_policy": "NOT_APPLICABLE_HISTORICAL_FIXTURE",
    }
    assert post_merge(repo, config)["overall"] == "PASS"
    remote = tmp_path / "remote.git"
    run(tmp_path, "init", "--bare", str(remote))
    run(repo, "remote", "add", "origin", str(remote))
    run(repo, "push", "origin", "HEAD:main")
    run(repo, "fetch", "origin")
    config.update(
        {
            "remote_check_policy": "REQUIRED",
            "expected_remote_ref": "refs/remotes/origin/main",
            "expected_remote_sha": merge,
        }
    )
    assert post_merge(repo, config)["overall"] == "PASS"
    config["expected_remote_sha"] = parent1
    assert post_merge(repo, config)["overall"] == "FAIL"
    config.update(
        {
            "remote_check_policy": "NOT_APPLICABLE_HISTORICAL_FIXTURE",
            "expected_remote_ref": None,
            "expected_remote_sha": None,
        }
    )
    config["expected_parent_2"] = base
    assert post_merge(repo, config)["overall"] == "FAIL"
    config["expected_parent_2"] = reviewed
    merged_scope["required"][0]["operation"] = "add"
    failed = post_merge(repo, config)
    assert failed["overall"] == "FAIL"
    assert "expected add, observed modify" in str(failed)


def test_consistency_checker_distinguishes_conflict_and_underspecification() -> None:
    contradictory = {
        "criteria": [
            {
                "id": "requires-a",
                "kind": "changed_files",
                "base": BASE,
                "head": MERGE,
                "required_paths": ["A"],
                "forbidden_paths": [],
            },
            {
                "id": "forbids-a",
                "kind": "changed_files",
                "base": BASE,
                "head": MERGE,
                "required_paths": [],
                "forbidden_paths": ["A"],
            },
        ]
    }
    result = evaluate(ROOT, contradictory)
    assert {item["classification"] for item in result["criteria"]} == {"CONTRADICTORY"}
    original_a5 = {
        "criteria": [
            {"id": "a5", "kind": "prefix_hash", "path": "CONVENTIONS.md", "base": BASE}
        ]
    }
    result = evaluate(ROOT, original_a5)
    assert result["criteria"][0]["classification"] == "INVALID_OR_UNDERSPECIFIED"
    assert "boundary" in result["criteria"][0]["reason"]


def test_self_application_of_all_four_tools(tmp_path: Path) -> None:
    scope = {
        "base": BASE,
        "head": MERGE,
        "mode": "exact",
        "required": [
            {"operation": "modify", "path": "CONVENTIONS.md"},
            {"operation": "modify", "path": "DECISION_LOG.md"},
            {"operation": "add", "path": REVIEW},
        ],
        "optional": [],
        "forbidden_operations": ["delete", "rename", "type_change"],
    }
    scope_path = write_json(tmp_path / "historical-scope.json", scope)
    assert scope_main(["--repo", str(ROOT), "--manifest", str(scope_path)]) == 0
    scope["required"].pop()
    assert (
        scope_main(
            [
                "--repo",
                str(ROOT),
                "--manifest",
                str(write_json(tmp_path / "missing.json", scope)),
            ]
        )
        == GOVERNANCE_FAILURE
    )
    content = evaluate_content(
        {
            "file": str(ROOT / "CONVENTIONS.md"),
            "required_literals": [
                {
                    "value": (
                        "No role prescribes another role's INCIDENTAL "
                        "implementation process."
                    ),
                    "single_line": True,
                }
            ],
            "forbidden_literals": [{"value": "no role", "single_line": True}],
            "heading_prefixes": [f"### {number}." for number in range(1, 13)],
        }
    )
    assert content["overall"] == "PASS"
    pins = [
        {
            "path": "derivations/P2-LATTICE-ONTOLOGY-01.md",
            "sha256": (
                "1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c"
            ),
        },
        {
            "path": "scripts/euclidean_reconstruction.py",
            "sha256": (
                "30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78"
            ),
        },
    ]
    config = {
        "mode": "POST_MERGE",
        "merge_commit": MERGE,
        "expected_parent_1": BASE,
        "expected_parent_2": BRANCH,
        "expected_merge_base": BASE,
        "scope_manifest": {
            **scope,
            "required": [
                {"operation": "modify", "path": "CONVENTIONS.md"},
                {"operation": "modify", "path": "DECISION_LOG.md"},
                {"operation": "add", "path": REVIEW},
            ],
        },
        "pinned_artifacts": pins,
        "remote_check_policy": "NOT_APPLICABLE_HISTORICAL_FIXTURE",
    }
    result = post_merge(ROOT, config)
    assert result["overall"] == "PASS"
    assert (
        next(
            item for item in result["checks"] if item["condition"] == "remote_agreement"
        )["status"]
        == "NOT_EVALUATED"
    )
    consistency = evaluate(
        ROOT,
        {
            "criteria": [
                {
                    "id": "original-a5",
                    "kind": "prefix_hash",
                    "path": "CONVENTIONS.md",
                    "base": BASE,
                }
            ]
        },
    )
    assert consistency["criteria"][0]["classification"] == "INVALID_OR_UNDERSPECIFIED"
