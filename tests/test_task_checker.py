"""Passing and failing cases for every property the task checker reports.

A check that is never observed to fail has not been shown to check anything,
so each property has at least one fixture in each direction. The five shapes
the specification names by hand -- two merges, a stopped task, a merge-base
that legitimately equals parent 1, a specification with several count-bearing
sentences, and an append-only file the checker was never told about -- have
fixtures of their own and are named for it.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from scripts.governance_tools.core import GOVERNANCE_FAILURE, TOOL_ERROR
from scripts.governance_tools.task_checker import evaluate, parse_scope_block
from scripts.governance_tools.task_checker import main as checker_main

ROOT = Path(__file__).resolve().parents[1]

SPEC_TEMPLATE = """# Task specification -- fixture

## 6. Acceptance criteria

**A4 -- Scope from the old main.** Base X, head Y: **9 additions and 3
modifications**, mode exact.

**A9 -- Scope**, {stated} additions:

    add:
{added}
    modify: []
    forbidden_operations:
      delete, rename
"""


def run(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def new_repo(tmp_path: Path, name: str = "repo") -> Path:
    repo = tmp_path / name
    run(tmp_path, "init", "-b", "main", str(repo))
    run(repo, "config", "user.email", "tests@example.invalid")
    run(repo, "config", "user.name", "Task checker tests")
    return repo


def commit(repo: Path, paths: dict[str, str], message: str) -> str:
    for rel, text in paths.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        run(repo, "add", rel)
    run(repo, "commit", "-m", message)
    return run(repo, "rev-parse", "HEAD")


def spec_text(stated: str, paths: list[str]) -> str:
    body = "\n".join(f"      {p}" for p in paths)
    return SPEC_TEMPLATE.format(stated=stated, added=body)


def base_repo(tmp_path: Path) -> tuple[Path, str]:
    """A repo with a gate file, a log and a register, ready for a task range."""
    repo = new_repo(tmp_path)
    gates = (
        "# Gates\n\n"
        "## P2-ALPHA-01\n\nStatus: PASS\n\nbody alpha\n\n"
        "## P2-BETA-01\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    register = (
        "# Branching Policy\n\n"
        "## Superseded branches\n\n"
        "```text\n"
        "fix/old-thing @ " + "0" * 40 + "\n"
        "  superseded by  fix/new-thing\n"
        "```\n\n"
        "## Remote refs\n\ntail\n"
    )
    base = commit(
        repo,
        {
            "GATES.md": gates,
            "docs/BRANCHING_POLICY.md": register,
            "DECISION_LOG.md": "# Decision Log\n\nentry one\n",
        },
        "chore: fixture base",
    )
    return repo, base


def reviewed_base(tmp_path: Path) -> tuple[Path, str]:
    """A base whose range opens with a review, so a work commit has one to follow.

    P2 is a real check: without this, every fixture that commits work would
    fail it, which is the checker behaving correctly and the fixture asking
    the wrong question.
    """
    repo, base = base_repo(tmp_path)
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    return repo, base


def config(repo: Path, base: str, head: str = "HEAD", **extra) -> dict:
    value = {"base": base, "head": head}
    value.update(extra)
    return value


def check(repo: Path, base: str, head: str = "HEAD", **extra) -> dict:
    return evaluate(repo, config(repo, base, head, **extra))


def prop(result: dict, ident: str) -> dict:
    return next(p for p in result["properties"] if p["id"] == ident)


# ---------------------------------------------------------------------------
# P1 -- scope manifest arithmetic
# ---------------------------------------------------------------------------
def test_p1_passes_when_manifest_count_matches_governing_sentence(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("two", ["a.py", "b.py"])}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "PASS"


def test_p1_fails_when_manifest_count_disagrees(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(
        repo, {"specs/s.md": spec_text("five", ["a", "b", "c", "d", "e", "f"])},
        "spec: fixture",
    )
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


def test_p1_selects_the_governing_sentence_not_another_count(tmp_path):
    """NAMED CASE: a specification with more than one count-bearing sentence.

    A4's '9 additions and 3 modifications' precedes A9's sentence in the same
    document. The grammar must take the nearest preceding count, not the first
    or the largest.
    """
    text = spec_text("three", ["a", "b", "c"])
    parsed = parse_scope_block(text)
    assert parsed["parse"] == "OK"
    assert parsed["stated"] == 3
    assert parsed["counted"] == 3
    assert "A9" in parsed["governing_sentence"]
    assert "9 additions" not in parsed["governing_sentence"]


def test_p1_reports_not_parseable_and_that_is_not_a_pass(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": "# no scope block at all\n"}, "spec: fixture")
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "NOT_PARSEABLE"
    assert result["overall"] == "INCOMPLETE"


def test_p1_partial_carries_its_limitation_in_the_json(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    record = prop(check(repo, base), "P1")
    assert record["classification"] == "PARTIAL"
    assert "does not establish" in record["does_not_establish"].lower()


# ---------------------------------------------------------------------------
# P2 -- Rule 15 commit order
# ---------------------------------------------------------------------------
def test_p2_passes_when_review_precedes_the_work_commit(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    commit(repo, {"scripts/thing.py": "x = 1\n"}, "feat: the work")
    assert prop(check(repo, base), "P2")["status"] == "PASS"


def test_p2_fails_when_work_precedes_the_review(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"scripts/thing.py": "x = 1\n"}, "feat: the work")
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    result = check(repo, base)
    assert prop(result, "P2")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


def test_p2_stopped_task_has_no_work_commit_to_order(tmp_path):
    """NAMED CASE: a range holding only a specification, a review and a report.

    reports/ is in the task-record set, so the report is not a work commit and
    P2 is satisfied with nothing to order -- from the definition, not from an
    exception beside it.
    """
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    commit(repo, {"reports/r.md": "# stop\n\n## Stops and clarifications\n\nnone\n"},
           "docs: stop report")
    record = prop(check(repo, base), "P2")
    assert record["status"] == "PASS"
    assert record["evidence"]["first_work_commit"] is None


def test_p2_reports_pre_boundary_commits_as_out_of_scope(tmp_path):
    repo, base = base_repo(tmp_path)
    early = commit(repo, {"scripts/early.py": "x = 1\n"}, "feat: before boundary")
    boundary = commit(repo, {"scripts/mid.py": "y = 2\n"}, "feat: boundary")
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"reviews/chatgpt/r.md": "ok\n"}, "review: fixture")
    commit(repo, {"scripts/late.py": "z = 3\n"}, "feat: after boundary")
    result = check(
        repo, base,
        prospectivity={"boundary": boundary, "inclusivity": "EXCLUSIVE"},
    )
    record = prop(result, "P2")
    assert early in record["evidence"]["out_of_scope"]
    assert boundary in record["evidence"]["out_of_scope"]
    assert record["status"] == "PASS"


def test_p2_inclusivity_changes_which_commits_are_in_scope(tmp_path):
    repo, base = base_repo(tmp_path)
    boundary = commit(repo, {"scripts/mid.py": "y = 2\n"}, "feat: boundary")
    commit(repo, {"reviews/chatgpt/r.md": "ok\n"}, "review: fixture")
    inclusive = check(
        repo, base, prospectivity={"boundary": boundary, "inclusivity": "INCLUSIVE"}
    )
    exclusive = check(
        repo, base, prospectivity={"boundary": boundary, "inclusivity": "EXCLUSIVE"}
    )
    assert inclusive["prospectivity"]["commits_in_scope"] == 2
    assert exclusive["prospectivity"]["commits_in_scope"] == 1
    assert prop(inclusive, "P2")["status"] == "FAIL"
    assert prop(exclusive, "P2")["status"] == "PASS"


# ---------------------------------------------------------------------------
# P3 -- append-only on both measures
# ---------------------------------------------------------------------------
def test_p3_passes_when_the_declared_file_is_only_appended_to(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"DECISION_LOG.md": "# Decision Log\n\nentry one\nentry two\n"},
           "docs: append")
    record = prop(check(repo, base, append_only_paths=["DECISION_LOG.md"]), "P3")
    assert record["status"] == "PASS"
    assert record["evidence"][0]["base_is_byte_prefix_of_head"] is True


def test_p3_fails_on_a_deletion(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"DECISION_LOG.md": "# Decision Log\n"}, "docs: truncate")
    record = prop(check(repo, base, append_only_paths=["DECISION_LOG.md"]), "P3")
    assert record["status"] == "FAIL"


def test_p3_fails_on_a_rewrite_that_deletes_no_net_lines(tmp_path):
    """The byte-prefix measure catches what the line count does not."""
    repo, base = base_repo(tmp_path)
    commit(repo, {"DECISION_LOG.md": "# Decision Log\n\nentry ONE\nentry two\n"},
           "docs: rewrite one line and append another")
    record = prop(check(repo, base, append_only_paths=["DECISION_LOG.md"]), "P3")
    assert record["status"] == "FAIL"
    assert record["evidence"][0]["base_is_byte_prefix_of_head"] is False


def test_p3_not_told_a_file_is_append_only_must_not_silently_pass(tmp_path):
    """NAMED CASE: no declaration supplied. The result must not read green."""
    repo, base = reviewed_base(tmp_path)
    commit(repo, {"DECISION_LOG.md": "# Decision Log\n"}, "docs: truncate")
    result = check(repo, base)
    record = prop(result, "P3")
    assert record["status"] == "NOT_DECLARED"
    assert record["status"] != "PASS"
    assert result["overall"] == "INCOMPLETE"


# ---------------------------------------------------------------------------
# P4 -- superseded branches are not merged
# ---------------------------------------------------------------------------
def test_p4_passes_when_no_register_commit_is_an_ancestor(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    assert prop(check(repo, base), "P4")["status"] == "PASS"


def test_p4_fails_when_a_register_commit_is_an_ancestor(tmp_path):
    repo, base = base_repo(tmp_path)
    superseded = commit(repo, {"stray.txt": "s\n"}, "chore: superseded work")
    register = (
        "# Branching Policy\n\n## Superseded branches\n\n```text\n"
        f"fix/old-thing @ {superseded}\n  superseded by  fix/new-thing\n"
        "```\n\n## Remote refs\n\ntail\n"
    )
    commit(repo, {"docs/BRANCHING_POLICY.md": register}, "docs: register it")
    result = check(repo, base)
    assert prop(result, "P4")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


# ---------------------------------------------------------------------------
# P5 -- merge parentage against freshly recomputed facts
# ---------------------------------------------------------------------------
def merge_fixture(tmp_path: Path) -> tuple[Path, str, str]:
    repo, base = base_repo(tmp_path)
    run(repo, "checkout", "-b", "side", base)
    commit(repo, {"side.txt": "s\n"}, "feat: side work")
    run(repo, "checkout", "main")
    commit(repo, {"reviews/chatgpt/r.md": "ok\n"}, "review: fixture")
    run(repo, "merge", "--no-ff", "side", "-m", "merge: land side")
    return repo, base, run(repo, "rev-parse", "HEAD")


def test_p5_passes_against_freshly_recomputed_parentage(tmp_path):
    repo, base, merge = merge_fixture(tmp_path)
    record = prop(check(repo, base), "P5")
    assert record["status"] == "PASS"
    found = record["evidence"][0]
    assert found["merge"] == merge
    assert found["recomputed_merge_base"] == base


def test_p5_fails_when_recorded_values_disagree_with_the_object(tmp_path):
    repo, base, merge = merge_fixture(tmp_path)
    result = check(
        repo, base,
        recorded_merge_facts=[
            {"merge": merge, "parent_1": "0" * 40, "parent_2": "1" * 40,
             "merge_base": base}
        ],
    )
    assert prop(result, "P5")["status"] == "FAIL"


def test_p5_accepts_a_merge_base_equal_to_parent_1(tmp_path):
    """NAMED CASE: a task that merges without committing anything of its own.

    The merge-base then legitimately equals parent 1. Testing distinctness
    would fail this correct history, so the checker must not.
    """
    repo, base = base_repo(tmp_path)
    run(repo, "checkout", "-b", "side")
    commit(repo, {"side.txt": "s\n"}, "feat: side work")
    run(repo, "checkout", "main")
    run(repo, "merge", "--no-ff", "side", "-m", "merge: land side")
    record = prop(check(repo, base), "P5")
    found = record["evidence"][0]
    assert found["merge_base_equals_parent_1"] is True
    assert record["status"] == "PASS"


def test_p5_two_merges_where_parent_1_is_the_first_merge(tmp_path):
    """NAMED CASE: a task making two merges. The second's parent 1 is the first."""
    repo, base = base_repo(tmp_path)
    run(repo, "checkout", "-b", "one", base)
    commit(repo, {"one.txt": "1\n"}, "feat: one")
    run(repo, "checkout", "main")
    run(repo, "checkout", "-b", "two", "main")
    commit(repo, {"two.txt": "2\n"}, "feat: two")
    run(repo, "checkout", "main")
    commit(repo, {"reviews/chatgpt/r.md": "ok\n"}, "review: fixture")
    run(repo, "merge", "--no-ff", "one", "-m", "merge: land one")
    first = run(repo, "rev-parse", "HEAD")
    run(repo, "merge", "--no-ff", "two", "-m", "merge: land two")
    second = run(repo, "rev-parse", "HEAD")
    record = prop(check(repo, base), "P5")
    assert record["status"] == "PASS"
    later = next(f for f in record["evidence"] if f["merge"] == second)
    assert later["recomputed_parent_1"] == first
    assert prop(check(repo, base), "P2")["status"] == "PASS"


def test_p5_is_not_applicable_without_a_merge_and_does_not_poison_overall(tmp_path):
    repo, base = reviewed_base(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: no merge here")
    result = check(repo, base, append_only_paths=[], authorised_modified_gates=[])
    assert prop(result, "P5")["status"] == "NOT_APPLICABLE"
    assert result["overall"] == "PASS"


def test_p5_makes_no_claim_about_independent_derivation(tmp_path):
    repo, base, _merge = merge_fixture(tmp_path)
    record = prop(check(repo, base), "P5")
    assert record["classification"] == "PARTIAL"
    assert "independently" in record["does_not_establish"]


# ---------------------------------------------------------------------------
# P6 -- commit-message hygiene
# ---------------------------------------------------------------------------
def test_p6_passes_on_clean_messages(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: a clean message")
    assert prop(check(repo, base), "P6")["status"] == "PASS"


def test_p6_fails_on_a_co_authored_by_trailer(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"},
           "chore: work\n\nCo-Authored-By: Someone <someone@example.invalid>")
    record = prop(check(repo, base), "P6")
    assert record["status"] == "FAIL"
    assert "Co-Authored-By" in record["evidence"][0]["matches"]


def test_p6_fails_on_a_url_in_the_message(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: work\n\nSee https://example.invalid/x")
    assert prop(check(repo, base), "P6")["status"] == "FAIL"


def test_p6_does_not_claim_to_catch_undefined_vocabulary(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: clean")
    record = prop(check(repo, base), "P6")
    assert record["classification"] == "PARTIAL"
    assert "session identifier" in record["does_not_establish"]


# ---------------------------------------------------------------------------
# P7 -- gate integrity
# ---------------------------------------------------------------------------
def test_p7_passes_when_no_gate_section_changes(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    assert prop(check(repo, base, authorised_modified_gates=[]), "P7")[
        "status"] == "PASS"


def test_p7_fails_on_an_unauthorised_gate_body_edit(tmp_path):
    repo, base = base_repo(tmp_path)
    gates = (
        "# Gates\n\n## P2-ALPHA-01\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    commit(repo, {"GATES.md": gates}, "docs: edit a gate body")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "FAIL"
    assert "P2-ALPHA-01" in record["evidence"]["unauthorised_changed"]


def test_p7_catches_a_deleted_section_that_keeps_the_body_of_another(tmp_path):
    """The count guards addition and removal; byte identity guards the rest."""
    repo, base = base_repo(tmp_path)
    kept = "# Gates\n\n## P2-ALPHA-01\n\nStatus: PASS\n\nbody alpha\n"
    commit(repo, {"GATES.md": kept}, "docs: delete a whole gate entry")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "FAIL"
    assert "P2-BETA-01" in record["evidence"]["removed_sections"]


def test_p7_allows_an_authorised_gate_to_change(tmp_path):
    repo, base = base_repo(tmp_path)
    gates = (
        "# Gates\n\n## P2-ALPHA-01\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    commit(repo, {"GATES.md": gates}, "docs: edit an authorised gate")
    assert prop(check(repo, base, authorised_modified_gates=["P2-ALPHA-01"]),
                "P7")["status"] == "PASS"


def test_p7_empty_authorised_set_means_nothing_may_change(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"GATES.md": "# Gates\n\n## P2-ALPHA-01\n\nStatus: PASS\n\nedited\n"},
           "docs: change everything")
    assert prop(check(repo, base, authorised_modified_gates=[]),
                "P7")["status"] == "FAIL"


def test_p7_without_a_declaration_is_not_declared_not_pass(tmp_path):
    repo, base = reviewed_base(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    result = check(repo, base)
    assert prop(result, "P7")["status"] == "NOT_DECLARED"
    assert result["overall"] == "INCOMPLETE"


# ---------------------------------------------------------------------------
# P8 -- Rule 15 placement and specification-first
# ---------------------------------------------------------------------------
def test_p8_passes_when_the_specification_is_the_first_commit(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"reviews/chatgpt/r.md": "ok\n"}, "review: fixture")
    assert prop(check(repo, base), "P8")["status"] == "PASS"


def test_p8_fails_when_work_precedes_the_specification(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"scripts/thing.py": "x = 1\n"}, "feat: work first")
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    result = check(repo, base)
    assert prop(result, "P8")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


def test_p8_fails_when_a_review_has_no_function_directory(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    commit(repo, {"reviews/loose.md": "ok\n"}, "review: misplaced")
    record = prop(check(repo, base), "P8")
    assert record["status"] == "FAIL"
    assert "reviews/loose.md" in record["evidence"][
        "reviews_missing_function_directory"]


# ---------------------------------------------------------------------------
# P9 -- reports carry a Stops and clarifications section
# ---------------------------------------------------------------------------
def test_p9_passes_when_the_report_carries_the_section(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"reports/r.md": "# Report\n\n## Stops and clarifications\n\nnone\n"},
           "docs: report")
    assert prop(check(repo, base), "P9")["status"] == "PASS"


def test_p9_fails_when_the_section_is_missing(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"reports/r.md": "# Report\n\nno such section here\n"},
           "docs: report")
    result = check(repo, base)
    assert prop(result, "P9")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


# ---------------------------------------------------------------------------
# Tool contract
# ---------------------------------------------------------------------------
def test_exit_zero_only_when_everything_green(tmp_path, capsys):
    repo, base = reviewed_base(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: clean")
    path = tmp_path / "config.json"
    path.write_text(
        json.dumps({"base": base, "head": "HEAD", "append_only_paths": [],
                    "authorised_modified_gates": []}),
        encoding="utf-8",
    )
    assert checker_main(["--repo", str(repo), "--config", str(path)]) == 0
    assert json.loads(capsys.readouterr().out)["overall"] == "PASS"


def test_governance_failure_exit_is_distinct_from_tool_error(tmp_path, capsys):
    repo, base = base_repo(tmp_path)
    commit(repo, {"reports/r.md": "# Report\n\nno section\n"}, "docs: report")
    failing = tmp_path / "failing.json"
    failing.write_text(json.dumps({"base": base, "head": "HEAD"}), encoding="utf-8")
    assert checker_main(
        ["--repo", str(repo), "--config", str(failing)]
    ) == GOVERNANCE_FAILURE
    capsys.readouterr()

    broken = tmp_path / "broken.json"
    broken.write_text(json.dumps({"head": "HEAD"}), encoding="utf-8")
    assert checker_main(["--repo", str(repo), "--config", str(broken)]) == TOOL_ERROR
    assert json.loads(capsys.readouterr().out)["overall"] == "TOOL_ERROR"


def test_every_partial_property_carries_its_limitation(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("one", ["a"])}, "spec: fixture")
    result = check(repo, base, append_only_paths=["DECISION_LOG.md"],
                   authorised_modified_gates=[])
    for record in result["properties"]:
        if record["classification"] == "PARTIAL":
            assert record["does_not_establish"].strip()
        else:
            assert "does_not_establish" not in record


# ---------------------------------------------------------------------------
# This repository's own recent history
# ---------------------------------------------------------------------------
BOUNDARY = "ce86b534fff6febb5291842e4eb60769affd12db"
SUPPLY_LANDING_BASE = "cc8adaa04ed75f5118ae2c25926a05e51a0056ff"
SUPPLY_LANDING_HEAD = "8939ff4a46445d88c6470fb4f27eec71f2f39172"


def test_real_history_landing_task_satisfies_rule_15_order(tmp_path):
    """The landing task's own range, checked against the shipped repository."""
    result = evaluate(
        ROOT,
        {
            "base": SUPPLY_LANDING_BASE,
            "head": SUPPLY_LANDING_HEAD,
            "prospectivity": {"boundary": BOUNDARY, "inclusivity": "INCLUSIVE"},
            "append_only_paths": [],
            "authorised_modified_gates": [],
        },
    )
    assert prop(result, "P2")["status"] == "PASS"
    assert prop(result, "P8")["status"] == "PASS"
    assert prop(result, "P9")["status"] == "PASS"
    assert prop(result, "P4")["status"] == "PASS"
    assert prop(result, "P6")["status"] == "PASS"


def test_real_history_register_is_read_from_the_shipped_policy(tmp_path):
    result = evaluate(
        ROOT,
        {"base": SUPPLY_LANDING_BASE, "head": SUPPLY_LANDING_HEAD,
         "append_only_paths": [], "authorised_modified_gates": []},
    )
    entries = prop(result, "P4")["evidence"]["entries"]
    assert len(entries) == 6
    assert {e["branch"] for e in entries} == {
        "fix/pi-decisions-and-deferred",
        "fix/pi-decisions-v2",
        "governance/supply-protocol-v2",
        "governance/supply-protocol-and-superseded",
        "review/role-model-and-executors",
        "gate/p2-land-diquark-line",
    }
