.PHONY: check test test-slow lint structure regen

check: lint test

test:
	python -m pytest

test-slow:
	python -m pytest -m slow

lint:
	python -m ruff check .

structure:
	python -m pytest tests/test_repository_structure.py

# Re-run every gate script; writes to results/<gate>/regen/ (gitignored).
regen:
	python -m scripts.hk_species
	python -m scripts.gap_criticality
	python -m scripts.lattice_beta_scan
