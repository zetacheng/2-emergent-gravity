# Current Handoff

## Current task

Independent verification sweep of Paper 2's load-bearing inputs (gates
`P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`) complete; `P2-BETAV-01` deferred.

## Scientific question

Do Paper 2's headline inputs (`β_B, β_F, β_V, β_B(ξ)`, `G_c`, `I_0`, and the
consequent `ξ_ind`, `4G_cβ_F`) survive an independent first-principles
recomputation?

## Locked inputs

`CONVENTIONS.md` (fixed before computation). Sharp Euclidean 4-ball continuum
regulator; Wilson `r=1` lattice; heat-kernel `Δ=−∇²+E`, `a_1=(1/6)R−E`.

## Do not reopen

- The closed recomputation gates, unless a concrete numerical inconsistency is
  documented. The `β_F` factor-2 (Dirac vs Weyl) is a *recorded disagreement
  awaiting reviewer adjudication*, not an open bug to silently patch.

## Required next input

- `paper/emergent_gr_paper_v2_15.tex` (for a direct textual comparison).
- A reviewer verdict on the `β_F` (Dirac vs Weyl) and lattice `I_0`/`G_c`
  disagreements recorded in `results/comparison/PAPER_COMPARISON.md`.

## Expected Codex output

Reproducible gate scripts, frozen raw results, regression anchors with mutation
detection — all present. No paper `.tex` was edited.

## Questions for ChatGPT

Is Paper 2's fermion content intended to be 4-component Dirac or 2-component
Weyl? The paper's `β_F = 1/(192π²)` matches Weyl; a Dirac fermion gives
`1/(96π²)` and shifts the survival window.

## Questions for Claude

Adjudicate: (1) the `β_F` factor-2 disagreement and its propagation to
`4G_cβ_F` and the survival window; (2) the ≈1.2% lattice `I_0`/`G_c` gap.

## Role boundaries

ChatGPT plans concepts, interpretation, derivations, gates, and calculation
specifications but does not certify numerical results. Codex maintains and
implements reproducible work but cannot promote results to paper claims. Claude
independently reviews gates and updates paper text only after acceptance. The
User / Principal Investigator owns scope and assumptions, accepts or rejects
verdicts, and authorizes paper updates.
