# Agent Rules

These rules apply to all future AI work in this repository.

## Mandatory preparation

Before making changes, read `PROGRESS.md`, `GATES.md`, `DECISION_LOG.md`,
`CLAIMS.md`, `HANDOFF.md`, and `CONVENTIONS.md`.

## Role separation

- ChatGPT handles conceptual discussion, physical interpretation, analytic
  derivation planning, gate design, calculation specifications, assumptions,
  and competing interpretations. It does not certify numerical results.
- Codex handles repository maintenance, implementation, tests, regression
  anchors, reproducibility, result files, branches, and commits. It must not
  promote a result into a paper claim without review.
- Claude is the independent reviewer/discriminator, issues gate verdicts,
  identifies overclaims, and updates the paper only after accepted results.
- The User / Principal Investigator owns the programme, approves assumptions,
  gates, and scope changes, accepts or rejects verdicts, and authorizes paper
  updates.

## Research rules

1. Never reopen a closed gate unless a concrete inconsistency is documented.
2. Never silently change conventions.
3. Commit a derivation note before production code.
4. Tests and regression anchors are mandatory.
5. Never edit raw outputs manually.
6. Processed results must identify the script and raw input used.
7. Do not update any `.tex` paper source before reviewer acceptance.
8. Preserve failed results and their provenance.
9. Distinguish the original model, a model extension, a phenomenological EFT,
   and a numerical proxy.
10. Every result must identify its regulator, cutoff, normalization, random
    seeds, and operating point.
11. A branch must correspond to one scientific gate or one paper-edit task.

This repository contains Paper 2 only. Do not merge content from another paper
repository.
