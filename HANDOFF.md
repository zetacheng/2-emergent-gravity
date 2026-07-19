# Current Handoff

## Current task

The Paper 2 normalization/gap/βV-circularity follow-up is **reviewed and
accepted** (`reviews/claude/2026-07-19-paper2-followup.md`). There is **no
current merge blocker** from D1, the normalization factor 2, or the `I_0` gap —
all resolved. **βV circularity remains unresolved at the full lattice level**
(`P2-BETAV-CIRC-01` = OPEN). Nothing is promoted to `VERIFIED`.

## Scientific question

Do Paper 2's headline inputs (`β_B, β_F, β_V, β_B(ξ)`, `G_c`, `I_0`, and the
consequent `ξ_ind`, `4G_cβ_F`) survive an independent first-principles
recomputation?

## Locked inputs

`CONVENTIONS.md` (fixed before computation). Sharp Euclidean 4-ball continuum
regulator; Wilson `r=1` lattice; heat-kernel `Δ=−∇²+E`, `a_1=(1/6)R−E`.

## Do not reopen

- The closed recomputation gates, unless a concrete numerical inconsistency is
  documented. D1 (`β_F` Weyl-vs-Dirac) and D2 (`I_0` gap) are **withdrawn** and
  must not be re-raised as disagreements — they were convention-mismatch
  artifacts.

## Required next input

- The **curved-background lattice Proca extraction for a `k ≠ 1` structure**
  (the decisive `P2-BETAV-CIRC-01` test): does it return `-(k+2)` or stay fixed
  near `-3`? This is the next scientific input.

## Expected Codex output

Reproducible gate scripts, frozen raw results, regression anchors with mutation
detection, and the imported paper source — all present. No paper `.tex` content
was edited (import only).

## Questions for ChatGPT

For `P2-BETAV-CIRC-01`: is the paper's longitudinal-artifact hypothesis
(heavy-mass windows drifting "to ratios near −5", i.e. the `k=3` value)
consistent with a compensating-power contamination of the Proca structure?

## Questions for Claude

Adjudicate `P2-NORM-01` outcome (a): accept that the `β`/`G` factor 2 is a `Z`
definition and that the paper is self-consistent; confirm the physics conclusion
(`ξ_ind<0` for `L≫1`) is unaffected.

## Role boundaries

ChatGPT plans concepts, interpretation, derivations, gates, and calculation
specifications but does not certify numerical results. Codex maintains and
implements reproducible work but cannot promote results to paper claims. Claude
independently reviews gates and updates paper text only after acceptance. The
User / Principal Investigator owns scope and assumptions, accepts or rejects
verdicts, and authorizes paper updates.
