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
from scripts.governance_tools.task_checker import (
    GATE_HEADING,
    RAW_GATE_HEADING,
    evaluate,
    gate_heading_id,
    gate_heading_ids,
    parse_scope_block,
)
from scripts.governance_tools.task_checker import main as checker_main

ROOT = Path(__file__).resolve().parents[1]

SPEC_TEMPLATE = """# Task specification -- fixture

## 6. Acceptance criteria

**A4 -- Scope from the old main.** Base X, head Y: **9 additions and 3
modifications**, mode exact.

**A9 -- Scope**, {prose} additions:

    stated: {declared}
    base: X
    head: Y
    mode: exact
    add:
{added}
    modify: {modify}
    forbidden_operations:
      delete, rename
"""

# The prose sentences above are decoration under the declared-total grammar and
# the fixtures below rely on that: the '9 additions and 3 modifications' of A4
# and the '{prose} additions' of A9 are both ignored.
WORD = {"zero": 0, "one": 1, "two": 2, "three": 3, "five": 5}

# The binding regression fixture, written out rather than generated, because
# the position of 'stated:' is the whole point of it. The old parser walked
# backward from 'add:' to the nearest line carrying a count; with 'stated:'
# BELOW the manifest that walk reaches A9's contradicting dry-run sentence and
# the old parser fails. The declared-total grammar reads 'stated:' wherever in
# the block it sits, ignores the sentence, and passes.
DRY_RUN_SPEC = """# Task specification -- fixture

## 6. Acceptance criteria

**A9 -- Scope**, seven additions:

    base: X
    head: Y
    mode: exact
    add:
      a
      b
      c
    modify: []
    forbidden_operations:
      delete, rename
    stated: 3 additions, 0 modifications
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


def spec_text(
    stated: str,
    paths: list[str],
    modify: list[str] | None = None,
    declared: str | None = None,
) -> str:
    """A fixture specification.

    ``stated`` is the word an old-parser fixture put in A9's prose sentence.
    It now sets BOTH the decorative prose and the declared ``stated:`` record,
    so a call unchanged from before the declared-total grammar keeps its
    meaning: 'five' against six paths disagreed then and disagrees now.
    ``declared`` overrides the record alone, leaving the prose to contradict
    it, which is how the malformed-declaration fixtures are written.
    """
    body = "\n".join(f"      {p}" for p in paths)
    if modify is None:
        modify_text = "[]"
    else:
        modify_text = "\n" + "\n".join(f"      {p}" for p in modify)
    if declared is None:
        declared = f"{WORD[stated]} additions, {len(modify or [])} modifications"
    return SPEC_TEMPLATE.format(
        prose=stated, declared=declared, added=body, modify=modify_text
    )


FIXTURE_REGISTER = (
    "# Branching Policy\n\n"
    "## Superseded branches\n\n"
    "```text\n"
    "fix/old-thing @ " + "0" * 40 + "\n"
    "  superseded by  fix/new-thing\n"
    "```\n\n"
    "## Remote refs\n\ntail\n"
)

FIXTURE_GATES = (
    "# Gates\n\n"
    "## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha\n\n"
    "## P2-BETA-01 — Beta gate\n\nStatus: PROPOSED\n\nbody beta\n"
)


def base_repo_with_gates(tmp_path: Path, gates: str) -> tuple[Path, str]:
    """``base_repo`` with the gate file's contents chosen by the caller.

    The register and the log come from the same source as ``base_repo`` so a
    P7 fixture cannot fail P4 or P3 for reasons of its own making.
    """
    repo = new_repo(tmp_path)
    base = commit(
        repo,
        {
            "GATES.md": gates,
            "docs/BRANCHING_POLICY.md": FIXTURE_REGISTER,
            "DECISION_LOG.md": "# Decision Log\n\nentry one\n",
        },
        "chore: fixture base",
    )
    return repo, base


def base_repo(tmp_path: Path) -> tuple[Path, str]:
    """A repo with a gate file, a log and a register, ready for a task range.

    The gate headings carry titles because the real ones do. An earlier
    version of this fixture used the bare ``## P2-ID`` shape, which no
    heading in ``GATES.md`` has ever used -- and which was the only shape the
    pre-repair grammar matched. The suite therefore confirmed the grammar
    against a file shaped to suit it.
    """
    return base_repo_with_gates(tmp_path, FIXTURE_GATES)


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
def test_p1_passes_when_the_declared_total_matches_the_manifest(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": spec_text("two", ["a.py", "b.py"])}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "PASS"


def test_p1_fails_when_the_declared_total_disagrees(tmp_path):
    """The planted five-versus-six defect, preserved on a declaring document.

    The historical specification carrying that defect declares no total and is
    now NOT_PARSEABLE, so the property it demonstrated lives here instead.
    """
    repo, base = base_repo(tmp_path)
    commit(
        repo, {"specs/s.md": spec_text("five", ["a", "b", "c", "d", "e", "f"])},
        "spec: fixture",
    )
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "FAIL"
    assert result["overall"] == "FAIL"


def test_p1_fails_when_the_declared_categories_do_not_sum_to_the_manifest(tmp_path):
    """A 'stated:' record whose two numbers do not sum to the paths listed."""
    text = spec_text("three", ["a", "b", "c"], modify=["m"],
                     declared="3 additions, 3 modifications")
    parsed = parse_scope_block(text)
    assert parsed["parse"] == "OK"
    assert (parsed["stated"], parsed["counted"]) == (6, 4)
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": text}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "FAIL"


def test_p1_fails_when_only_one_category_disagrees(tmp_path):
    """Per-category comparison: totals that agree while the split does not."""
    text = spec_text("two", ["a", "b", "c"], modify=["m"],
                     declared="2 additions, 2 modifications")
    parsed = parse_scope_block(text)
    assert parsed["stated"] == parsed["counted"] == 4
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": text}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "FAIL"


def test_p1_consults_no_sentence_when_a_nearer_one_contradicts(tmp_path):
    """NAMED CASE, and the defect this grammar exists to remove.

    A dry-run count sits immediately before the block and contradicts it, which
    is this repository's house style. The old grammar took that sentence; the
    declared total must be read instead, and the document must PASS.
    """
    parsed = parse_scope_block(DRY_RUN_SPEC)
    assert parsed["parse"] == "OK"
    assert parsed["stated_record"] == "stated: 3 additions, 0 modifications"
    assert (parsed["stated_add"], parsed["counted_add"]) == (3, 3)
    assert (parsed["stated_modify"], parsed["counted_modify"]) == (0, 0)
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": DRY_RUN_SPEC}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "PASS"


def test_p1_reads_a_stated_record_placed_below_the_manifest(tmp_path):
    """'stated:' is read from anywhere in the block, not from a fixed line."""
    assert DRY_RUN_SPEC.index("stated:") > DRY_RUN_SPEC.index("modify:")
    assert parse_scope_block(DRY_RUN_SPEC)["stated"] == 3


def test_p1_passes_with_an_empty_modify_and_a_declared_zero(tmp_path):
    text = spec_text("two", ["a", "b"], declared="2 additions, 0 modifications")
    assert "modify: []" in text
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": text}, "spec: fixture")
    assert prop(check(repo, base), "P1")["status"] == "PASS"


def test_p1_reports_not_parseable_and_that_is_not_a_pass(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": "# no scope block at all\n"}, "spec: fixture")
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "NOT_PARSEABLE"
    assert result["overall"] == "INCOMPLETE"


def test_p1_reports_not_parseable_when_no_total_is_declared(tmp_path):
    """A legacy specification: a well-formed block with no 'stated:' record."""
    text = spec_text("two", ["a", "b"]).replace(
        "    stated: 2 additions, 0 modifications\n", ""
    )
    assert "stated:" not in text
    assert parse_scope_block(text)["detail"] == (
        "no 'stated:' record in the scope block"
    )
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": text}, "spec: fixture")
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "NOT_PARSEABLE"
    assert result["overall"] == "INCOMPLETE"


def test_p1_distinguishes_a_malformed_declaration_from_an_absent_one(tmp_path):
    """Number words are prose and are not accepted; the reason says which."""
    parsed = parse_scope_block(
        spec_text("three", ["a", "b", "c"], declared="three additions")
    )
    assert parsed["parse"] == "NOT_PARSEABLE"
    assert parsed["detail"] == "malformed 'stated:' item: 'three additions'"
    assert parsed["detail"] != "no 'stated:' record in the scope block"


def test_p1_rejects_a_declaration_naming_a_category_twice(tmp_path):
    parsed = parse_scope_block(
        spec_text("one", ["a"], declared="1 additions, 2 additions")
    )
    assert parsed["detail"] == "'stated:' names additions twice"


def test_p1_reports_not_parseable_for_a_non_path_token_under_modify(tmp_path):
    """The live '(none)' incident: it was counted as a path and failed a merge."""
    text = spec_text("one", ["a"], modify=["(none)"], declared="1 additions")
    parsed = parse_scope_block(text)
    assert parsed["parse"] == "NOT_PARSEABLE"
    assert parsed["detail"] == "not a path under 'modify:': '(none)'"
    repo, base = base_repo(tmp_path)
    commit(repo, {"specs/s.md": text}, "spec: fixture")
    result = check(repo, base)
    assert prop(result, "P1")["status"] == "NOT_PARSEABLE"
    assert result["overall"] == "INCOMPLETE"


def test_p1_accepts_the_path_shapes_this_repository_writes(tmp_path):
    """Braces, a leading dot, and a top-level name with no slash are paths."""
    paths = ["GATES.md", ".github/workflows/ci.yml",
             "specs/2026-08-XXT{HHMM}Z_a-task.md"]
    parsed = parse_scope_block(
        spec_text("three", paths, declared="3 additions, 0 modifications")
    )
    assert parsed["parse"] == "OK"
    assert parsed["counted_set"] == paths


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
    assert record["evidence"]["paths"][0]["base_is_byte_prefix_of_head"] is True


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
    assert record["evidence"]["paths"][0]["base_is_byte_prefix_of_head"] is False


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
        "# Gates\n\n## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01 — Beta gate\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    commit(repo, {"GATES.md": gates}, "docs: edit a gate body")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "FAIL"
    assert "P2-ALPHA-01" in record["evidence"]["unauthorised_changed"]


def test_p7_catches_a_deleted_section_that_keeps_the_body_of_another(tmp_path):
    """The count guards addition and removal; byte identity guards the rest."""
    repo, base = base_repo(tmp_path)
    kept = "# Gates\n\n## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha\n"
    commit(repo, {"GATES.md": kept}, "docs: delete a whole gate entry")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "FAIL"
    assert "P2-BETA-01" in record["evidence"]["removed_sections"]


def test_p7_allows_an_authorised_gate_to_change(tmp_path):
    repo, base = base_repo(tmp_path)
    gates = (
        "# Gates\n\n## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01 — Beta gate\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    commit(repo, {"GATES.md": gates}, "docs: edit an authorised gate")
    assert prop(check(repo, base, authorised_modified_gates=["P2-ALPHA-01"]),
                "P7")["status"] == "PASS"


def test_p7_empty_authorised_set_means_nothing_may_change(tmp_path):
    repo, base = base_repo(tmp_path)
    commit(repo, {"GATES.md": "# Gates\n\n## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nedited\n"},
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
# P7 -- the heading grammar, and the completeness invariant that guards it
#
# The grammar this repository shipped was ``^## (P2-[A-Z0-9-]+)\s*$``, which
# matches a heading carrying no title. No heading in the real GATES.md has
# that shape -- all fourteen are ``## <id> - <title>`` -- so gate_sections
# returned {} at every revision and check_p7 compared two empty maps and
# returned PASS, in every task that ran it. The fixtures above used the bare
# shape too, which is why the suite confirmed the grammar instead of catching
# it: they were shaped to suit the parser rather than to resemble the file.
#
# Every fixture below fails against the pre-repair code.
# ---------------------------------------------------------------------------
def gates_with(*headings: str) -> str:
    """A gate file built from whole heading lines, given verbatim."""
    body = "\n\n".join(f"{h}\n\nStatus: PASS\n\nbody for {n}"
                       for n, h in enumerate(headings))
    return "# Gates\n\n" + body + "\n"


def test_gate_grammar_reads_every_heading_of_the_real_gates_file():
    """The shipped GATES.md, not a fixture: fourteen raw, fourteen parsed."""
    lines = (ROOT / "GATES.md").read_text(encoding="utf-8").split("\n")
    raw = [line for line in lines if RAW_GATE_HEADING.match(line)]
    parsed = [GATE_HEADING.match(line) for line in lines]
    ids = [m.group(1) for m in parsed if m]
    assert len(raw) == 14, f"expected 14 raw '## P2-' headings, found {len(raw)}"
    assert len(ids) == len(raw), (
        "the grammar does not read every heading of the real gate file: "
        f"{len(ids)} parsed of {len(raw)} raw"
    )
    assert len(set(ids)) == len(ids), "duplicate gate id in GATES.md"


def test_gate_grammar_rejects_the_bare_heading_the_old_grammar_accepted():
    """A titleless ``## P2-ID`` is not a gate section, and that is deliberate.

    It is the one shape the pre-repair grammar did match. Rejecting it means
    a file written in that shape reports NOT_PARSEABLE rather than quietly
    parsing, which is the honest answer for a registry that does not look
    like the registry.
    """
    assert GATE_HEADING.match("## P2-ALPHA-01 — Alpha gate")
    assert GATE_HEADING.match("## P2-ALPHA-01 – Alpha gate")
    assert GATE_HEADING.match("## P2-ALPHA-01 - Alpha gate")
    assert not GATE_HEADING.match("## P2-ALPHA-01")
    assert not GATE_HEADING.match("## P2-ALPHA-01 ")
    assert not GATE_HEADING.match("## P2-ALPHA-01 —")
    # The raw counter must still see every one of them, or the invariant
    # would have nothing to compare against.
    for line in ("## P2-ALPHA-01", "## P2-ALPHA-01 — t", "## P2-lower-01"):
        assert RAW_GATE_HEADING.match(line)


def test_p7_is_not_parseable_when_the_grammar_reads_none_of_the_headings(
    tmp_path,
):
    """The 0 / N case: headings present, grammar matches none.

    This is the repository's actual defect, reproduced. The pre-repair code
    returns PASS here.
    """
    repo, base = base_repo_with_gates(
        tmp_path,
        gates_with("## P2-ALPHA-01", "## P2-BETA-01", "## P2-GAMMA-01"),
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["raw_heading_count_base"] == 3
    assert record["evidence"]["section_count_base"] == 0


def test_p7_is_not_parseable_when_one_heading_of_many_is_unread(tmp_path):
    """The 14 / 15 case, and it is the point of the invariant.

    A guard that fired only at zero would pass this: the fourteen the parser
    sees are unchanged, and the fifteenth is invisible to it. One unseen gate
    is enough.
    """
    good = [f"## P2-FIX-{n:02d} — Gate {n}" for n in range(1, 15)]
    repo, base = base_repo_with_gates(
        tmp_path, gates_with(*good, "## P2-lower-01")
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["raw_heading_count_base"] == 15
    assert record["evidence"]["section_count_base"] == 14
    assert record["evidence"]["unrecognised_headings_base"] == ["## P2-lower-01"]


def test_p7_is_not_parseable_when_a_heading_parses_at_base_but_not_at_head(
    tmp_path,
):
    """The asymmetric case the invariant exists for: readable, then not."""
    repo, base = base_repo_with_gates(
        tmp_path, gates_with("## P2-ALPHA-01 — Alpha gate")
    )
    commit(repo, {"GATES.md": gates_with("## P2-ALPHA-01")},
           "docs: drop the title from a gate heading")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["section_count_base"] == 1
    assert record["evidence"]["section_count_head"] == 0


def test_p7_is_not_parseable_when_the_gate_file_has_no_headings_at_all(
    tmp_path,
):
    """0 raw / 0 parsed. Equality holds and it is still not a pass.

    A registry in which nothing readable was found has not been checked,
    which is not the same as having been read and found clean.
    """
    repo, base = base_repo_with_gates(
        tmp_path, "# Gates\n\nNothing here yet.\n"
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["raw_heading_count_base"] == 0
    assert record["evidence"]["section_count_base"] == 0


def test_p7_zero_sections_is_not_a_pass_even_with_an_empty_authorised_set(
    tmp_path,
):
    """``authorised_modified_gates: []`` is the strongest declaration.

    It must not be reachable as a green over an unread registry, which is
    exactly the combination every task in this repository has been running.
    """
    repo, base = base_repo_with_gates(
        tmp_path, gates_with("## P2-ALPHA-01")
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] != "PASS"
    assert record["status"] == "NOT_PARSEABLE"


def test_p7_zero_sections_is_not_a_pass_when_base_and_head_are_identical(
    tmp_path,
):
    """Nothing changed is not a defence: an unread registry is unread."""
    repo, base = base_repo_with_gates(
        tmp_path, gates_with("## P2-ALPHA-01")
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: touches no gate file")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["evidence"]["section_count_base"] == \
        record["evidence"]["section_count_head"]
    assert record["status"] == "NOT_PARSEABLE"


def test_p7_not_parseable_makes_the_run_incomplete_and_exits_non_zero(
    tmp_path,
):
    """NOT_PARSEABLE, not FAIL -- cannot judge is not judged wrong.

    It must still be non-zero, or an unreadable registry would read as green.
    """
    repo, base = base_repo_with_gates(
        tmp_path, gates_with("## P2-ALPHA-01")
    )
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    result = check(repo, base, authorised_modified_gates=[])
    assert prop(result, "P7")["status"] == "NOT_PARSEABLE"
    assert result["overall"] == "INCOMPLETE"


def test_p7_still_fails_on_an_unauthorised_change_it_can_read(tmp_path):
    """The repair does not convert a real FAIL into a parse complaint."""
    repo, base = base_repo(tmp_path)
    edited = (
        "# Gates\n\n"
        "## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01 — Beta gate\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    commit(repo, {"GATES.md": edited}, "docs: edit a gate body")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "FAIL"
    assert record["evidence"]["raw_heading_count_base"] == 2
    assert record["evidence"]["section_count_base"] == 2


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


# ---------------------------------------------------------------------------
# C1 -- one gate-heading grammar
#
# Two expressions read this registry and agreed by coincidence. The canonical
# language is now the CONJUNCTION of the two, in one helper both call sites
# use. It is strictly tighter than either, and anything it rejects surfaces
# through P7's completeness invariant rather than disappearing -- which is the
# property these fixtures exist to hold.
# ---------------------------------------------------------------------------
def test_the_helper_reads_the_real_gates_file():
    """REGRESSION. The shipped GATES.md, through the helper: fourteen ids."""
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")
    ids = gate_heading_ids(text)
    assert len(ids) == 14, f"expected 14 gate headings, read {len(ids)}"
    assert len(set(ids)) == 14, "duplicate gate id in GATES.md"


def test_the_helper_is_the_conjunction_and_rejects_what_separated_the_two():
    """CHANGE-DISCRIMINATING. Each shape was accepted by exactly one side."""
    assert gate_heading_id("## P2-FOO2-01 — Title") is None   # digit in a segment
    assert gate_heading_id("## P2-BAR-01") is None             # no separator
    assert gate_heading_id("## P2-BAZ-01 — ") is None          # empty title
    assert gate_heading_id("## P2-FOO-01 — Title") == "P2-FOO-01"
    assert gate_heading_id("## P2-A-B-01 — T") == "P2-A-B-01"


def test_a_digit_inside_an_id_segment_surfaces_through_p7(tmp_path):
    """CHANGE-DISCRIMINATING. Tightening is safe because P7 reports the loss."""
    repo, base = base_repo_with_gates(
        tmp_path,
        gates_with("## P2-ALPHA-01 — Alpha gate", "## P2-FOO2-01 — Title"),
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["raw_heading_count_base"] == 2
    assert record["evidence"]["section_count_base"] == 1
    assert record["evidence"]["unrecognised_headings_base"] == ["## P2-FOO2-01 — Title"]


def test_a_heading_with_no_title_surfaces_through_p7(tmp_path):
    """REGRESSION. The landed grammar already rejected this; it still does."""
    repo, base = base_repo_with_gates(
        tmp_path, gates_with("## P2-ALPHA-01 — Alpha gate", "## P2-BAZ-01 — ")
    )
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, authorised_modified_gates=[]), "P7")
    assert record["status"] == "NOT_PARSEABLE"
    assert record["evidence"]["section_count_base"] == 1


# ---------------------------------------------------------------------------
# C3 -- declared sets a reviewer sees
#
# P3's and P7's declared sets came from a run-time config written after the
# review. They now come from the specification's scope block, where a reviewer
# read them; config is a fallback, and disagreement is a conflict rather than
# a silent override.
# ---------------------------------------------------------------------------
def declaring_spec(paths: list[str], append_only: str, gates: str = "[]") -> str:
    """A fixture specification whose scope block declares its own sets."""
    body = "\n".join(f"      {p}" for p in paths)
    return f"""# Task specification -- fixture

## 6. Acceptance criteria

    stated: {len(paths)} additions, 0 modifications
    base: X
    head: Y
    mode: exact
    add:
{body}
    modify: []
    append_only: {append_only}
    authorised_gates: {gates}
    forbidden_operations:
      delete, rename
"""


def test_p3_uses_the_declaration_in_the_scope_block(tmp_path):
    """CHANGE-DISCRIMINATING. No config at all, and P3 still has a subject."""
    repo, base = base_repo(tmp_path)
    spec = declaring_spec(["a.py"], "\n      DECISION_LOG.md")
    commit(repo, {"specs/s.md": spec, "a.py": "x\n"}, "spec: fixture")
    record = prop(check(repo, base), "P3")
    assert record["status"] == "PASS"
    assert record["evidence"]["declared_source"] == "specification"
    assert record["evidence"]["declared"] == ["DECISION_LOG.md"]


def test_p3_says_when_the_value_came_from_config(tmp_path):
    """REGRESSION. Config-only still works, and now says so in the JSON."""
    repo, base = base_repo(tmp_path)
    commit(repo, {"notes.txt": "x\n"}, "chore: unrelated")
    record = prop(check(repo, base, append_only_paths=["DECISION_LOG.md"]), "P3")
    assert record["status"] == "PASS"
    assert record["evidence"]["declared_source"] == "config"
    assert record["evidence"]["declared_by_specification"] is None


def test_a_specification_and_a_config_that_differ_is_a_conflict(tmp_path):
    """CHANGE-DISCRIMINATING. Not a merge, not a silent override.

    The range is ordered specification-then-review so P2 and P8 are both
    satisfied and the conflict is the ONLY non-green result: the run is
    INCOMPLETE *because of* the conflict and not incidentally.
    """
    repo, base = base_repo(tmp_path)
    spec = declaring_spec(["specs/s.md"], "\n      DECISION_LOG.md")
    commit(repo, {"specs/s.md": spec}, "spec: fixture")
    commit(repo, {"reviews/chatgpt/r.md": "approved\n"}, "review: fixture")
    result = check(repo, base, append_only_paths=["GATES.md"])
    record = prop(result, "P3")
    assert record["status"] == "DECLARATION_CONFLICT"
    assert "disagree" in record["reason"]
    assert record["evidence"]["declared_by_specification"] == ["DECISION_LOG.md"]
    assert record["evidence"]["supplied_by_config"] == ["GATES.md"]
    assert result["overall"] == "INCOMPLETE"


def test_a_specification_and_a_config_that_agree_is_not_a_conflict(tmp_path):
    """REGRESSION. Agreement is the ordinary case and must stay quiet."""
    repo, base = base_repo(tmp_path)
    spec = declaring_spec(["a.py"], "\n      DECISION_LOG.md")
    commit(repo, {"specs/s.md": spec, "a.py": "x\n"}, "spec: fixture")
    record = prop(
        check(repo, base, append_only_paths=["DECISION_LOG.md"]), "P3")
    assert record["status"] == "PASS"
    assert record["evidence"]["declared_source"] == "specification"


def test_an_empty_declaration_is_declared_empty_and_not_a_pass(tmp_path):
    """CHANGE-DISCRIMINATING, and the point of C3.

    The old code returned NOT_APPLICABLE for an empty set -- the check off,
    not passed -- and one landed integration went green that way.
    """
    repo, base = base_repo(tmp_path)
    spec = declaring_spec(["a.py"], "[]")
    commit(repo, {"specs/s.md": spec, "a.py": "x\n"}, "spec: fixture")
    result = check(repo, base)
    record = prop(result, "P3")
    assert record["status"] == "DECLARED_EMPTY"
    assert record["status"] != "PASS"
    assert record["status"] != "NOT_APPLICABLE"
    assert "nothing was declared applicable" in record["reason"]
    # A valid declaration, unlike NOT_DECLARED: the run continues.
    assert result["overall"] != "INCOMPLETE"


def test_no_declaration_anywhere_is_still_not_declared(tmp_path):
    """REGRESSION. Absence and emptiness must not share an outcome."""
    repo, base = reviewed_base(tmp_path)
    commit(repo, {"DECISION_LOG.md": "# Decision Log\n"}, "docs: truncate")
    result = check(repo, base)
    record = prop(result, "P3")
    assert record["status"] == "NOT_DECLARED"
    assert record["evidence"]["declared_source"] == "none"
    assert result["overall"] == "INCOMPLETE"


def test_p7_reads_its_authorised_set_from_the_scope_block(tmp_path):
    """CHANGE-DISCRIMINATING. P7's declared set is reviewable too."""
    repo, base = base_repo(tmp_path)
    edited = (
        "# Gates\n\n"
        "## P2-ALPHA-01 — Alpha gate\n\nStatus: PASS\n\nbody alpha EDITED\n\n"
        "## P2-BETA-01 — Beta gate\n\nStatus: PROPOSED\n\nbody beta\n"
    )
    spec = declaring_spec(["a.py"], "[]", "\n      P2-ALPHA-01")
    commit(repo, {"specs/s.md": spec, "a.py": "x\n", "GATES.md": edited},
           "spec: fixture authorising one gate")
    record = prop(check(repo, base), "P7")
    assert record["status"] == "PASS"
    assert record["evidence"]["declared_source"] == "specification"
    assert record["evidence"]["authorised_modified"] == ["P2-ALPHA-01"]


def test_a_non_gate_id_under_authorised_gates_is_not_parseable(tmp_path):
    """CHANGE-DISCRIMINATING. The key has a shape and it is enforced."""
    repo, base = base_repo(tmp_path)
    spec = declaring_spec(["a.py"], "[]", "\n      not-a-gate")
    commit(repo, {"specs/s.md": spec, "a.py": "x\n"}, "spec: fixture")
    record = prop(check(repo, base), "P1")
    assert record["status"] == "NOT_PARSEABLE"
    assert "not a gate id" in record["evidence"][0]["detail"]
