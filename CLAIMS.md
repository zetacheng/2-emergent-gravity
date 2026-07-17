# Claim Ledger

Allowed statuses are `PROPOSED`, `SUPPORTED`, `VERIFIED`, `FAILED`, `RETIRED`,
`CONDITIONAL`, and `INCONCLUSIVE`.

`VERIFIED` requires a closed gate, reproducible artifacts, and reviewer
acceptance. **No claim in this repository is `VERIFIED`:** there is no reviewer
record and no archived provenance (see `MIGRATION.md`). Independent
recomputations that the paper agrees with are `SUPPORTED`; recomputations that
the paper disagrees with record **both** values and are `INCONCLUSIVE` pending
reviewer adjudication; quantities not computed are `PROPOSED`. Failed and
retired claims must remain recorded.

| Claim ID | Claim | Status | Evidence | Gate | Paper section | Last reviewed |
|---|---|---|---|---|---|---|
| P2-C1 | `β_B = −1/(192π²)` (real scalar, minimal), continuum | SUPPORTED | `P2-HK-01`; symbolic; matches paper magnitude `1/(192π²)` | P2-HK-01 | induced EH / heat kernel | 2026-07-17 |
| P2-C2 | `β_F = −1/(96π²)` (Dirac), `β_F/β_B = 2` | INCONCLUSIVE | `P2-HK-01`; paper uses `β_F=1/(192π²)`, `β_F/β_B=1`; factor-2 (Dirac vs Weyl) disagreement, both recorded | P2-HK-01 | fermion-induced gravity | 2026-07-17 |
| P2-C3 | `β_V/β_B = −3` (Proca, analytic) | SUPPORTED | `P2-HK-01`; symbolic; matches paper analytic `−3` | P2-HK-01 | Finding 5 (Proca) | 2026-07-17 |
| P2-C4 | `β_B(ξ)/β_B = 1 − 6ξ` (conformal null at `ξ=1/6`) | CONDITIONAL | `P2-HK-01`; computed; direct paper comparison pending `.tex` import | P2-HK-01 | non-minimal coupling | 2026-07-17 |
| P2-C5 | `G_c = 8π²/Λ²` (`c=8`), continuum sharp 4-ball | SUPPORTED | `P2-GAP-01`; exact; matches paper-implied `8π²` | P2-GAP-01 | gap-equation criticality | 2026-07-17 |
| P2-C6 | `I_0 = 0.085388(20)`, `G_c = 5.856`, lattice Wilson `r=1` | INCONCLUSIVE | `P2-GAP-01`; paper `I_0=0.0844`, `G_c=5.924`; `≈1.2%` disagreement outside numeric unc., both recorded | P2-GAP-01 | lattice criticality | 2026-07-17 |
| P2-C7 | `β_B = 5.44e-4` lattice mass scan, `+3.1%` of continuum | SUPPORTED | `P2-BETA-01`; within `±9%` fit systematics; consistent with paper's "5%" | P2-BETA-01 | lattice β_B extraction | 2026-07-17 |
| P2-C8 | `4G_cβ_F = 1/3` (Dirac) and survival `m > 0.287 Λ` | INCONCLUSIVE | inherits P2-C2 factor-2; paper `4G_cβ_F=1/6`, `m>0.368Λ`; both recorded | P2-HK-01 | survival condition | 2026-07-17 |
| P2-C9 | `β_V/β_B = −3.2(5)` lattice (longitudinal artifacts) | PROPOSED | not computed this sweep; paper text only, no archived provenance | P2-BETAV-01 | Finding 5 (lattice Proca) | 2026-07-17 |

## Notes

- No `VERIFIED` status is used: there is no reviewer acceptance record and no
  archived provenance for any Paper 2 number (see `MIGRATION.md`).
- Disagreements (`P2-C2`, `P2-C6`, `P2-C8`) are detailed in
  `results/comparison/PAPER_COMPARISON.md`, with candidate reconciliations
  recorded separately from the disagreements and left for reviewer adjudication.
