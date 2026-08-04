"""Positive, negative, and historical self-application tests for governance tools."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from scripts.governance_tools import core
from scripts.governance_tools.content_checker import evaluate_content
from scripts.governance_tools.core import (
    GOVERNANCE_FAILURE,
    TOOL_ERROR,
    changed_operations,
    evaluate_scope,
    sha256,
)
from scripts.governance_tools.merge_guard import post_merge, pre_merge
from scripts.governance_tools.scope_checker import main as scope_main
from scripts.governance_tools.spec_consistency_checker import evaluate
from scripts.governance_tools.spec_consistency_checker import main as consistency_main

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


def test_content_checker_distinguishes_all_frozen_match_modes(tmp_path: Path) -> None:
    target = tmp_path / "target.txt"
    target.write_text("There is no role here\nno role\n", encoding="utf-8")
    result = evaluate_content(
        {
            "file": str(target),
            "required_literals": [
                {"value": "no role", "match_mode": "substring"},
                {"value": "no role", "match_mode": "line_substring"},
                {"value": "no role", "match_mode": "exact_line"},
            ],
        }
    )
    assert [item["count"] for item in result["checks"]] == [2, 2, 1]
    without_exact_line = evaluate_content(
        {
            "file": str(target),
            "forbidden_literals": [{"value": "no role", "match_mode": "exact_line"}],
        }
    )
    assert without_exact_line["overall"] == "FAIL"
    target.write_text("There is no role here\n", encoding="utf-8")
    exact = evaluate_content(
        {
            "file": str(target),
            "required_literals": [{"value": "no role", "match_mode": "exact_line"}],
            "forbidden_literals": [{"value": "no role", "match_mode": "substring"}],
        }
    )
    assert [item["count"] for item in exact["checks"]] == [0, 1]


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
    run(repo, "checkout", "--detach", base)
    detached = pre_merge(
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
    correspondence = next(
        item
        for item in detached["checks"]
        if item["condition"] == "worktree_matches_reviewed_branch"
    )
    assert correspondence["status"] == "FAIL"
    assert correspondence["attachment"] == "detached"
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
    config["pinned_artifacts"] = [{"path": "absent.txt", "sha256": "0" * 64}]
    absent_pin = post_merge(repo, config)
    assert absent_pin["overall"] == "FAIL"
    assert (
        next(
            item
            for item in absent_pin["checks"]
            if item["condition"] == "pinned_artifacts"
        )["evidence"][0]["actual"]
        is None
    )
    one_parent = post_merge(
        repo,
        {
            "mode": "POST_MERGE",
            "merge_commit": parent1,
            "expected_parent_1": base,
            "expected_parent_2": reviewed,
            "expected_merge_base": base,
            "scope_manifest": {**operations(), "base": parent1, "head": parent1},
            "pinned_artifacts": [],
            "remote_check_policy": "NOT_APPLICABLE_HISTORICAL_FIXTURE",
        },
    )
    assert one_parent["overall"] == "FAIL"
    assert (
        next(
            item
            for item in one_parent["checks"]
            if item["condition"] == "exactly_two_parents"
        )["status"]
        == "FAIL"
    )


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


def test_consistency_checker_uses_resolved_domains_and_validates_schema(
    tmp_path: Path,
) -> None:
    gates_at_base = sha256(core.blob(ROOT, BASE, "GATES.md"))
    cross_domain = {
        "criteria": [
            {
                "id": "base",
                "kind": "file_hash",
                "path": "GATES.md",
                "revision": BASE,
                "sha256": gates_at_base,
            },
            {
                "id": "merge",
                "kind": "file_hash",
                "path": "GATES.md",
                "revision": MERGE,
                "sha256": "0" * 64,
            },
            {
                "id": "required",
                "kind": "changed_files",
                "base": BASE,
                "head": MERGE,
                "required_paths": ["CONVENTIONS.md"],
                "forbidden_paths": [],
            },
            {
                "id": "forbidden",
                "kind": "changed_files",
                "base": MERGE,
                "head": "HEAD",
                "required_paths": [],
                "forbidden_paths": ["CONVENTIONS.md"],
            },
        ]
    }
    result = evaluate(ROOT, cross_domain)
    assert all(item["classification"] != "CONTRADICTORY" for item in result["criteria"])
    same_domain = {
        "criteria": [
            {
                "id": "left",
                "kind": "file_hash",
                "path": "GATES.md",
                "revision": BASE,
                "sha256": gates_at_base,
            },
            {
                "id": "right",
                "kind": "file_hash",
                "path": "GATES.md",
                "revision": BASE,
                "sha256": "0" * 64,
            },
        ]
    }
    result = evaluate(ROOT, same_domain)
    assert {item["classification"] for item in result["criteria"]} == {"CONTRADICTORY"}
    cases = {
        "duplicate": {
            "criteria": [
                {
                    "id": "same",
                    "kind": "changed_files",
                    "base": BASE,
                    "head": MERGE,
                    "required_paths": [],
                    "forbidden_paths": [],
                },
                {
                    "id": "same",
                    "kind": "changed_files",
                    "base": BASE,
                    "head": MERGE,
                    "required_paths": [],
                    "forbidden_paths": [],
                },
            ]
        },
        "empty": {"criteria": []},
        "bad-hash": {
            "criteria": [
                {
                    "id": "hash",
                    "kind": "file_hash",
                    "path": "GATES.md",
                    "revision": BASE,
                    "sha256": "not-a-hash",
                }
            ]
        },
    }
    for name, document in cases.items():
        path = write_json(tmp_path / f"{name}.json", document)
        assert (
            consistency_main(["--repo", str(ROOT), "--spec", str(path)])
            == GOVERNANCE_FAILURE
        )
        assert all(
            item["classification"] == "INVALID_OR_UNDERSPECIFIED"
            for item in evaluate(ROOT, document)["criteria"]
        )
    missing_path = {
        "criteria": [
            {
                "id": "missing",
                "kind": "file_hash",
                "path": "missing.txt",
                "revision": BASE,
                "sha256": "0" * 64,
            }
        ]
    }
    assert (
        evaluate(ROOT, missing_path)["criteria"][0]["classification"] == "UNSATISFIED"
    )
    unresolved = write_json(
        tmp_path / "unresolved.json",
        {
            "criteria": [
                {
                    "id": "missing-object",
                    "kind": "file_hash",
                    "path": "GATES.md",
                    "revision": "deadbeef",
                    "sha256": "0" * 64,
                }
            ]
        },
    )
    assert (
        consistency_main(["--repo", str(ROOT), "--spec", str(unresolved)]) == TOOL_ERROR
    )


def test_scope_parser_handles_extended_operation_taxonomy(
    monkeypatch: object, tmp_path: Path
) -> None:
    raw = (
        b"R100\x00old.txt\x00new.txt\x00"
        b"C100\x00source.txt\x00copy.txt\x00T\x00mode.txt\x00"
    )

    def fake_git(_: object, *args: str, text: bool = True) -> str | bytes:
        if args[0] == "diff":
            return raw
        return "a" * 40 + "\n"

    monkeypatch.setattr(core, "git", fake_git)
    records = changed_operations(".", "base", "head")
    assert records == [
        {"operation": "rename", "from": "old.txt", "to": "new.txt"},
        {"operation": "copy", "from": "source.txt", "to": "copy.txt"},
        {"operation": "type_change", "path": "mode.txt"},
    ]
    manifest = {
        "base": "base",
        "head": "head",
        "mode": "exact",
        "required": records,
        "optional": [],
        "forbidden_operations": [],
    }
    assert evaluate_scope(".", manifest)["overall"] == "PASS"
    malformed = write_json(
        tmp_path / "bad.json",
        {
            "base": "base",
            "head": "head",
            "required": [{"operation": "rename", "path": "wrong"}],
        },
    )
    assert scope_main(["--repo", ".", "--manifest", str(malformed)]) == TOOL_ERROR


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
                    "match_mode": "line_substring",
                }
            ],
            "forbidden_literals": [{"value": "no role", "match_mode": "exact_line"}],
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
