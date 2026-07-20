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

## Cross-repository flag (do not edit the other repository)

Gate `P2-BETAV-CIRC-01` audits whether Paper 2's Finding 5 lattice test of
`β_V/β_B = −3` has discriminating power. The companion vector-sector repository
`3-vector-sector` (claim `P3-C-004`, status `VERIFIED`) quotes
`β_V/β_B = −3.2(5)` in its abstract. **If `P2-BETAV-CIRC-01` ever fires** (the
lattice extraction found to return `−3` regardless of the determinant
structure), that quotation is affected and `P3-C-004` would need review. This is
a **flag only**: `3-vector-sector` is not read from or written to here. The
analytic layer of `P2-BETAV-CIRC-01` finds the target ratio *is*
structure-dependent (`−(k+2)`), so the test is not degenerate; the full lattice
reproduction remains `OPEN`.

## SI-1 dependency clarification (`P2-SI1-UNBLOCK-01`, 2026-07-20)

Governance clarification of the operational dependency graph — **no historical
claim was upgraded or downgraded, and no numerical value was changed.**

- **Historical Finding 5 status:** `β_V/β_B = −3.2(5)` is **unreproduced**.
- **Historical audit status:** `P2-BETAV-CIRC-01` = `SUSPENDED` (historical
  pipeline NOT LOCATED).
- **Operational replacement path:** `P2-BETAV-RECON-01`, status `PROPOSED` —
  **not yet run** and **not yet an operational replacement**. Only a *proposed*
  replacement path; not a completed one.
- **Alternative operational input path:** the Paper 3 analytic vector input,
  `P3-C-001` / `P3-FIERZ-01`, pinned at
  `8c363ef08368f5c022278ea5f36e01496be3d5ca`. Repulsive `G_ω = −G/N`; a
  headwind; it receives **no** validation from the suspended `−3.2(5)`.

Explicitly: `P2-BETAV-RECON-01` is only a proposed replacement path, not a
completed replacement; no historical claim was upgraded; no historical claim was
downgraded; no numerical value was changed; only the operational dependency
graph was clarified.

## Consequence for claim statuses

Because there is no reviewer record and no archived provenance yet:

- A recomputed quantity that the paper agrees with is marked `SUPPORTED`,
  never `VERIFIED`.
- A recomputed quantity that the paper disagrees with is marked `INCONCLUSIVE`,
  with both values recorded, pending reviewer adjudication.
- A quantity that was not computed in this sweep is marked `PROPOSED`, with
  evidence recorded as "paper text only, no archived provenance".
