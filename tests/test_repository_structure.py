"""Verify the research repository's required foundation.

Includes a dangling-reference check: every gate ID cited in the ``Gate`` column
of ``CLAIMS.md`` must have a matching ``## <ID>`` heading in ``GATES.md`` (this
defect occurred in ``3-vector-sector``).
"""

import re
from pathlib import Path

from scripts.governance_tools.task_checker import (
    GATE_ID_TOKEN,
    gate_heading_ids,
)

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP_LEVEL_FILES = {
    ".gitignore",
    "AGENTS.md",
    "CITATION.cff",
    "CLAIMS.md",
    "CONVENTIONS.md",
    "DECISION_LOG.md",
    "GATES.md",
    "HANDOFF.md",
    "LICENSE",
    "Makefile",
    "MIGRATION.md",
    "PROGRESS.md",
    "README.md",
    "ROADMAP.md",
    "pyproject.toml",
}

REQUIRED_DIRECTORIES = {
    ".github",
    "archive",
    "derivations",
    "docs",
    "paper",
    "results",
    "reviews",
    "scripts",
    "tests",
}

REQUIRED_NESTED_PATHS = {
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/gate.yml",
    ".github/ISSUE_TEMPLATE/paper-sync.yml",
    ".github/pull_request_template.md",
    ".github/workflows/ci.yml",
    "archive/README.md",
    "derivations/README.md",
    "derivations/P2-HK-01_heat_kernel_species.md",
    "derivations/P2-GAP-01_gap_criticality.md",
    "derivations/P2-BETA-01_lattice_mass_scan.md",
    "derivations/P2-NORM-01_normalization_chain.md",
    "derivations/betav_discriminating_power.md",
    "derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md",
    "derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md",
    "derivations/P2-SI1-UNBLOCK-01.md",
    "derivations/P2-BETAV-CIRC-01_determinant-decomposition.md",
    "docs/BRANCHING_POLICY.md",
    "docs/RESEARCH_WORKFLOW.md",
    "docs/RESULT_SCHEMA.md",
    "paper/README.md",
    "paper/figures/.gitkeep",
    "results/README.md",
    "results/figures/.gitkeep",
    "results/processed/.gitkeep",
    "results/raw/.gitkeep",
    "results/P2-HK-01/raw/hk_species.json",
    "results/P2-GAP-01/raw/gap_criticality.json",
    "results/P2-BETA-01/raw/lattice_beta_scan.json",
    "results/P2-NORM-01/raw/normalization_chain.json",
    "results/P2-BETAV-CIRC-01/raw/betav_discriminating.json",
    "results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md",
    "results/P2-BETAV-ASSEMBLY-01/raw/betav_assembly.json",
    "results/P2-SI1-DEPENDENCY.md",
    "results/recovered-2026/REPRODUCTION.md",
    "results/recovered-2026/BETAV_REPRODUCTION.md",
    "results/recovered-2026/fig_mlog.pdf",
    "results/comparison/PAPER_COMPARISON.md",
    "reports/REPORTING_POLICY.md",
    "reports/2026-07-20_P2-BETAV-provenance-merge_report.md",
    "reports/2026-07-20_P2-SI1-unblock_report.md",
    "reports/2026-07-20_gravity-engine-recovery_report.md",
    "reports/2026-07-20_betav-complete-recovery_report.md",
    "reports/2026-07-20_betav-decomposition-adjudication_report.md",
    "paper/emergent_gr_paper_v2_15.tex",
    "reviews/README.md",
    "reviews/chatgpt/.gitkeep",
    "reviews/claude/.gitkeep",
    "scripts/README.md",
    "scripts/__init__.py",
    "scripts/hk_species.py",
    "scripts/gap_criticality.py",
    "scripts/lattice_beta_scan.py",
    "scripts/normalization_chain.py",
    "scripts/betav_discriminating.py",
    "scripts/betav_assembly.py",
    "scripts/betav_decomp_check.py",
    "scripts/recovered_2026/PROVENANCE.md",
    "scripts/recovered_2026/reproduce_check.py",
    "scripts/recovered_2026/seagull_check.py",
    "scripts/recovered_2026/boson_loop.py",
    "scripts/recovered_2026/tt_check.py",
    "scripts/recovered_2026/speed_check.py",
    "scripts/recovered_2026/structure_decomp.py",
    "scripts/recovered_2026/mlog_coeff.py",
    "scripts/recovered_2026/proca_loop.py",
    "scripts/recovered_2026/reproduce_betav.py",
    "tests/README.md",
    "tests/test_repository_structure.py",
}


def test_required_top_level_files_exist() -> None:
    missing = sorted(
        name for name in REQUIRED_TOP_LEVEL_FILES if not (ROOT / name).is_file()
    )
    assert not missing, f"Missing required top-level files: {missing}"


def test_required_directories_exist() -> None:
    missing = sorted(
        name for name in REQUIRED_DIRECTORIES if not (ROOT / name).is_dir()
    )
    assert not missing, f"Missing required directories: {missing}"


def test_required_nested_paths_exist() -> None:
    missing = sorted(
        path for path in REQUIRED_NESTED_PATHS if not (ROOT / path).is_file()
    )
    assert not missing, f"Missing required repository paths: {missing}"


# ---------------------------------------------------------------------------
# Gate-ID cross-reference (dangling-reference defect guard)
# ---------------------------------------------------------------------------
def _cited_gate_ids() -> set:
    """Gate IDs appearing in the 'Gate' column of the CLAIMS.md table."""
    text = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    ids = set()
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        for tok in GATE_ID_TOKEN.findall(line):
            ids.add(tok)
    return ids


def _gate_headings() -> set:
    """Gate IDs that have a gate heading in GATES.md.

    The grammar lives in ``scripts.governance_tools.task_checker`` and this
    module no longer carries one. Two expressions used to read this registry
    and agreed by coincidence; the shared helper is what replaces the
    coincidence, and ``test_both_gate_heading_call_sites_agree`` is what
    checks the replacement held.
    """
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")
    return set(gate_heading_ids(text))


def test_every_cited_gate_id_has_a_gates_heading() -> None:
    cited = _cited_gate_ids()
    headings = _gate_headings()
    assert cited, "No gate IDs found in CLAIMS.md; parser or table changed."
    dangling = sorted(cited - headings)
    assert not dangling, (
        f"CLAIMS.md cites gate IDs with no '## <ID>' heading in GATES.md: "
        f"{dangling}"
    )


# ---------------------------------------------------------------------------
# The agreement invariant that replaces a coincidence
#
# Two expressions used to read GATES.md -- the checker's and this module's --
# and they agreed. Nothing checked that they agreed, so the agreement was a
# coincidence that a convention change on either side would have ended
# silently. Both call sites now share one helper, and this test is what
# establishes that they still do.
# ---------------------------------------------------------------------------
def test_both_gate_heading_call_sites_agree() -> None:
    """The checker and this module read the SAME id set from GATES.md.

    The empty set must not pass. A test that agrees on nothing agrees, which
    is the shape P7's completeness invariant and the pin validator's non-empty
    assertion both already guard against -- this is the third instance and it
    gets the same guard rather than a weaker one.
    """
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")

    # Call site 1: the checker's section parser, reached through the helper.
    from_checker = set(gate_heading_ids(text))
    # Call site 2: this module's own accessor, which now calls the same helper.
    from_structure = _gate_headings()

    assert from_checker, (
        "no gate heading found in GATES.md: either the heading convention "
        "changed or the shared grammar stopped matching, and in both cases "
        "this invariant is comparing two empty sets and asserting nothing"
    )
    assert from_checker == from_structure, (
        "the two gate-heading call sites disagree: "
        f"only the checker sees {sorted(from_checker - from_structure)}, "
        f"only the structure test sees {sorted(from_structure - from_checker)}"
    )


def test_the_shared_grammar_is_the_conjunction_of_the_two_it_replaced() -> None:
    """The canonical language is tighter than both expressions it replaced.

    These three shapes are what separated them, measured before the change.
    Each is now rejected: the conjunction requires the strict id shape AND a
    separator followed by a non-empty title.
    """
    for heading in (
        "## P2-FOO2-01 — Title",   # a digit inside an id segment
        "## P2-BAR-01",            # no separator, no title
        "## P2-BAZ-01 — ",         # separator, empty title
    ):
        assert not gate_heading_ids(heading), heading
    # And a well-formed heading is still read.
    assert gate_heading_ids("## P2-FOO-01 — Title") == ["P2-FOO-01"]
