# Migration Record

## There is no legacy source

This file exists to state plainly, and to place on the permanent record, a fact
that distinguishes Paper 2 from the other papers in the programme:

**Paper 2 has no legacy repository, no archived script, no stored result file,
and no reproducible provenance for its headline numbers.**

Papers 3, 4, and 5 were populated by *migrating* a pre-existing legacy code
base: their numbers could be traced to a script and re-run. Paper 2 cannot.
Its load-bearing quantities — the heat-kernel species coefficients
`β_B, β_F, β_V, β_B(ξ)`, the criticality inputs `G_c` and `I_0`, and the
lattice extractions of `β_B` and `β_V/β_B` — exist only as:

- numbers written in the paper text (`emergent_gr_paper_v2_15.tex`), and
- numbers quoted in old chat transcripts.

No script computes them. No archived output records them. Nothing can be
re-run. This absence of provenance is *itself a finding* and is recorded here
rather than being smoothed over.

## What this repository is instead

This repository is therefore **not a migration**. It is an **independent
verification**: a fresh, first-principles recomputation of Paper 2's
load-bearing inputs, performed under pre-registration discipline (compute and
commit the number *before* comparing it to the paper), followed by an explicit
comparison in `results/comparison/PAPER_COMPARISON.md`.

## Pre-registration discipline

Every computation gate (`P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-BETAV-01`)
was implemented and committed **before** the paper's claimed value for that
quantity was consulted. No script, test, docstring, or variable name in those
gates contains, references, or is tuned toward a paper value. Tolerances are
justified by the numerics themselves (convergence, discretization,
fit-systematics spread), never chosen so that the paper's number lands inside.

The comparison against `emergent_gr_paper_v2_15.tex` is a *separate*, later
commit. Where the independent recomputation disagrees with the paper, the
disagreement is recorded prominently and left for reviewer adjudication; no
convention is retrofitted to reconcile the two and then presented as the
finding.

## Status of the paper source

`paper/emergent_gr_paper_v2_15.tex` is to be supplied by the Principal
Investigator and imported during the comparison gate (Task 6). If it is not
present in the repository, the comparison is performed against the specific
numerical claims transcribed from the paper into the task specification, and
that substitution is recorded in `results/comparison/PAPER_COMPARISON.md`.

## Consequence for claim statuses

Because there is no reviewer record and no archived provenance yet:

- A recomputed quantity that the paper agrees with is marked `SUPPORTED`,
  never `VERIFIED`.
- A recomputed quantity that the paper disagrees with is marked `INCONCLUSIVE`,
  with both values recorded, pending reviewer adjudication.
- A quantity that was not computed in this sweep is marked `PROPOSED`, with
  evidence recorded as "paper text only, no archived provenance".
