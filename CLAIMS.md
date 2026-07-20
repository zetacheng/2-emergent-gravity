# Claim Ledger

Allowed statuses are `PROPOSED`, `SUPPORTED`, `VERIFIED`, `FAILED`, `RETIRED`,
`CONDITIONAL`, and `INCONCLUSIVE`.

`VERIFIED` requires a closed gate, reproducible artifacts, and reviewer
acceptance. **No claim in this repository is `VERIFIED`:** there is no reviewer
record and no archived provenance (see `MIGRATION.md`). Independent
recomputations that the paper agrees with are `SUPPORTED`; recomputations that
the paper disagrees with record **both** values and are `INCONCLUSIVE`;
quantities not computed are `PROPOSED`. Superseded claims are preserved.

## Status of the first report's disagreements (both withdrawn)

The first report's D1 (`β_F` Weyl-vs-Dirac) and D2 (`I_0` ≈1.2%) were both
**artifacts of comparing across conventions** with the paper source unavailable.
With the source imported, both are withdrawn (see `DECISION_LOG.md`): the
recomputation **agrees** with Paper 2 v2.15 once the uniform `Z` normalization
(`P2-NORM-01`) and the `I_0` evaluation mass (`ma=0.02`, `P2-GAP-01`) are
matched.

| Claim ID | Claim | Status | Evidence | Gate | Paper section | Last reviewed |
|---|---|---|---|---|---|---|
| P2-C1 | `β_B` (real scalar, minimal) equals the paper's continuum value in one `Z` normalization | SUPPORTED | `P2-HK-01`; paper `1/(384π²)` (eq. `betaB`) = this repo in paper `Z` | P2-HK-01 | induced EH / heat kernel | 2026-07-17 |
| P2-C2 | `β_F/β_B = 2` (fermion:scalar) | SUPPORTED | `P2-HK-01`; paper "`β_F=2β_B`" (line 1155); D1 withdrawn | P2-HK-01 | fermion-induced gravity | 2026-07-17 |
| P2-C3 | `β_V/β_B = −3` (Proca, analytic) | SUPPORTED | `P2-HK-01`; paper `β_V=−3β_B` (line 1287) | P2-HK-01 | Finding 5 | 2026-07-17 |
| P2-C4 | `β_B(ξ)/β_B = 1 − 6ξ` (conformal null at `ξ=1/6`) | SUPPORTED | `P2-HK-01`; paper `β_B(ξ)=(1−6ξ)/(384π²)` (line 1171) | P2-HK-01 | non-minimal coupling | 2026-07-17 |
| P2-C5 | `G_c = 8π²/Λ²` (`c=8`), continuum sharp 4-ball | SUPPORTED | `P2-GAP-01`; paper `G_c=8π²/Λ²` (line 1221) | P2-GAP-01 | gap-equation criticality | 2026-07-17 |
| P2-C6 | lattice `I_0` (Wilson `r=1`, `ma=0.02`) equals the paper's | SUPPORTED | `P2-GAP-01`; `0.084341`/`0.084465` vs paper `0.0844`/`0.0845` (<0.1%); D2 withdrawn | P2-GAP-01 | lattice criticality | 2026-07-17 |
| P2-C7 | `β_B` lattice mass scan agrees with continuum at the few-% level | SUPPORTED | `P2-BETA-01`; `+3%` (this repo) / `5%` (paper, line 1148) | P2-BETA-01 | lattice β_B extraction | 2026-07-17 |
| P2-C8 | `4G_cβ_F = 1/6` (paper `Z` convention) and `ξ_ind<0` for `L≫1` | SUPPORTED | `P2-NORM-01`; `1/6` in paper `Z`; the report's `1/3` was convention-mixing | P2-NORM-01 | survival condition | 2026-07-17 |
| P2-C9 | `β_V/β_B = −3.2(5)` lattice (Finding 5 value) | PROPOSED | unreproduced paper value; historical pipeline NOT LOCATED (`PROVENANCE_SEARCH.md`) | P2-BETAV-CIRC-01 | Finding 5 (lattice Proca) | 2026-07-19 |
| P2-C10 | the `β`/`G` factor 2 is a uniform (`R_Z=2`) `Z` normalization, not physics | SUPPORTED | `P2-NORM-01`; `R_Z=2` for scalar/Dirac/Proca | P2-NORM-01 | Findings 3–4 | 2026-07-17 |
| P2-C11 | the `k`-generalized determinant assembly preserves `k`-dependence on the shared lattice tadpole (`R_k=−(k+2)`, no hardcoded `−3`) — bookkeeping, NOT a test of the historical projection | SUPPORTED | `P2-BETAV-ASSEMBLY-01`; `C` cancels, ratio spread `≤9e-16`; mutation collapses to `−3` | P2-BETAV-ASSEMBLY-01 | Finding 5 | 2026-07-19 |
| P2-C12 | whether the historical Finding 5 `β_V` lattice pipeline is circular | INCONCLUSIVE | **blocked by provenance** — historical pipeline NOT LOCATED; gate `SUSPENDED`; neither demonstrated nor ruled out | P2-BETAV-CIRC-01 | Finding 5 | 2026-07-19 |
| P2-C13 | a clean-room curved-background Proca reconstruction (distinct from the historical question) | PROPOSED | not run; substantial implementation; scope-labelled reconstruction ≠ historical test | P2-BETAV-RECON-01 | Finding 5 | 2026-07-19 |

## Notes

- No `VERIFIED` status is used (no reviewer acceptance, no archived provenance).
- `P2-C2`, `P2-C6`, `P2-C8` were `INCONCLUSIVE` in the first report and are now
  `SUPPORTED` after the corrected, source-based comparison; the superseded
  entries are preserved in `DECISION_LOG.md`.
- `P2-C11` (determinant bookkeeping preserves `k`, `P2-BETAV-ASSEMBLY-01`) and
  `P2-C12` (is the historical pipeline circular?) are deliberately separate: the
  bookkeeping regression passes but the shared integral cancels in its ratio, so
  it has no power over the historical projection. `P2-C12` is
  `INCONCLUSIVE`/blocked by provenance (the historical pipeline is NOT LOCATED —
  `results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`); gate `P2-BETAV-CIRC-01` is
  `SUSPENDED`, not closed by assertion. `P2-C13` (`P2-BETAV-RECON-01`) is the
  proposed reconstruction path, explicitly distinct from the historical test.
