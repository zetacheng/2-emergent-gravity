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
| P2-C9 | `β_V/β_B = −3.2(5)` lattice (Finding 5 value) | PROPOSED | not computed this sweep; paper text only, no archived provenance | P2-BETAV-CIRC-01 | Finding 5 (lattice Proca) | 2026-07-17 |
| P2-C10 | the `β`/`G` factor 2 is a uniform (`R_Z=2`) `Z` normalization, not physics | SUPPORTED | `P2-NORM-01`; `R_Z=2` for scalar/Dirac/Proca | P2-NORM-01 | Findings 3–4 | 2026-07-17 |
| P2-C11 | Finding 5's `β_V` extraction target is structure-dependent `−(k+2)` (so the test is not degenerate) | SUPPORTED | `P2-BETAV-CIRC-01`; analytic layer | P2-BETAV-CIRC-01 | Finding 5 | 2026-07-17 |
| P2-C12 | whether the paper's *lattice* `β_V` pipeline tracks the structure (non-circular) | PROPOSED | full curved-lattice Proca reproduction OPEN; not run | P2-BETAV-CIRC-01 | Finding 5 | 2026-07-17 |

## Notes

- No `VERIFIED` status is used (no reviewer acceptance, no archived provenance).
- `P2-C2`, `P2-C6`, `P2-C8` were `INCONCLUSIVE` in the first report and are now
  `SUPPORTED` after the corrected, source-based comparison; the superseded
  entries are preserved in `DECISION_LOG.md`.
- `P2-C11` (structure-dependence, computed) and `P2-C12` (is the lattice
  pipeline circular, not run) are deliberately separate: the analytic test
  passes; the numerical audit stays `OPEN` and is not closed by assertion.
