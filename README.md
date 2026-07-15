# 2-emergent-gravity

Paper 2 — **Emergent Gravity from Lattice Fermion Fields**

Core scientific responsibility: induced metric, spin-2 sector, Einstein-Hilbert
term, Newtonian limit, and induced gravitational source.

This repository contains **one paper only**: Paper 2. Material belonging to the
other papers in the programme must remain in their respective repositories.

## Current status

`INFRASTRUCTURE INITIALIZED`

Historical scientific progress will be imported separately. No scientific
progress or result is inferred by this initialization.

## Role separation

### ChatGPT

ChatGPT supports conceptual discussion, physical interpretation, analytic
derivation planning, gate design, calculation specifications, and the
identification of assumptions and competing interpretations. ChatGPT does not
certify numerical results.

### Codex

Codex maintains the repository, implements symbolic and numerical work, writes
tests and regression anchors, preserves reproducibility and result files, and
enforces branch and commit discipline. Codex must not promote a result into a
paper claim without review.

### Claude

Claude acts as an independent reviewer and discriminator: reviewing derivations
and results, issuing gate verdicts, identifying overclaims, and updating the
paper only after results are accepted.

### User / Principal Investigator

The User / Principal Investigator owns the physical programme, approves
assumptions, gates, and scope changes, accepts or rejects final verdicts, and
decides when paper text may be updated.

## Directory guide

- `paper/` — imported paper source and paper-specific figures.
- `derivations/` — pre-implementation analytic derivation notes.
- `scripts/` — reproducible symbolic and numerical implementations.
- `tests/` — structure, unit, and regression checks.
- `results/` — immutable raw outputs and provenance-linked processed artifacts.
- `reviews/` — independent review records grouped by reviewer.
- `archive/` — preserved retired material and failed routes.
- `docs/` — workflow, result schema, and branching policy.

## Standard gate workflow

1. Propose a scientific question in `GATES.md`.
2. Lock scope, assumptions, conventions, anchors, and kill criteria.
3. Commit the derivation note before production implementation.
4. Run the calculation on one `gate/<gate-name>` branch.
5. Store immutable raw output and provenance-linked processed artifacts.
6. Run tests and regression anchors.
7. Obtain an independent Claude verdict.
8. Ask the Principal Investigator to accept or reject the verdict.
9. Update claims or paper text only after acceptance.

## Reproducibility commands

```text
make check
make test
make lint
make structure
```

Install the development environment with Python 3.11 or later:

```text
python -m pip install -e ".[dev]"
```

## Acceptance warning

No result is accepted merely because code runs. A result requires analytic and
regression anchors, tests, stored outputs, complete provenance, and independent
review.
