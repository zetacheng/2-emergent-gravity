"""Verify the research repository's required foundation.

Includes a dangling-reference check: every gate ID cited in the ``Gate`` column
of ``CLAIMS.md`` must have a matching ``## <ID>`` heading in ``GATES.md`` (this
defect occurred in ``3-vector-sector``).
"""

import re
from pathlib import Path

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
    "results/comparison/PAPER_COMPARISON.md",
    "reports/REPORTING_POLICY.md",
    "reports/2026-07-20_P2-BETAV-provenance-merge_report.md",
    "reports/2026-07-20_P2-SI1-unblock_report.md",
    "reports/2026-07-20_gravity-engine-recovery_report.md",
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
    "scripts/recovered_2026/PROVENANCE.md",
    "scripts/recovered_2026/reproduce_check.py",
    "scripts/recovered_2026/seagull_check.py",
    "scripts/recovered_2026/boson_loop.py",
    "scripts/recovered_2026/tt_check.py",
    "scripts/recovered_2026/speed_check.py",
    "scripts/recovered_2026/structure_decomp.py",
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
        for tok in re.findall(r"P2-[A-Z]+(?:-[A-Z]+)*-\d+", line):
            ids.add(tok)
    return ids


def _gate_headings() -> set:
    """Gate IDs that have a '## <ID>' heading in GATES.md."""
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")
    pattern = r"^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+)"
    return set(re.findall(pattern, text, flags=re.MULTILINE))


def test_every_cited_gate_id_has_a_gates_heading() -> None:
    cited = _cited_gate_ids()
    headings = _gate_headings()
    assert cited, "No gate IDs found in CLAIMS.md; parser or table changed."
    dangling = sorted(cited - headings)
    assert not dangling, (
        f"CLAIMS.md cites gate IDs with no '## <ID>' heading in GATES.md: "
        f"{dangling}"
    )
