"""Verify the research repository's required foundation."""

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
    "docs/BRANCHING_POLICY.md",
    "docs/RESEARCH_WORKFLOW.md",
    "docs/RESULT_SCHEMA.md",
    "paper/README.md",
    "paper/figures/.gitkeep",
    "results/README.md",
    "results/figures/.gitkeep",
    "results/processed/.gitkeep",
    "results/raw/.gitkeep",
    "reviews/README.md",
    "reviews/chatgpt/.gitkeep",
    "reviews/claude/.gitkeep",
    "scripts/README.md",
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
