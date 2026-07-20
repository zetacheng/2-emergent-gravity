# Progress

## Paper identity

Paper 2 — Emergent Gravity from Lattice Fermion Fields.

## Current version

v2.15 (paper `.tex` imported; see `MIGRATION.md` and
`results/comparison/PAPER_COMPARISON.md`).

## Current scientific status

Independent verification sweep completed and, after importing the paper source,
**re-adjudicated**: gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-NORM-01`
(PASS), `P2-BETAV-ASSEMBLY-01` (PASS, implementation only), `P2-BETAV-CIRC-01`
(**SUSPENDED**, blocked by provenance) and `P2-BETAV-RECON-01` (PROPOSED). The
recomputation **confirms Paper 2 v2.15** once conventions are matched. No legacy
source exists (`MIGRATION.md`).

The normalization/gap/circularity follow-up has **one independent reviewer
record and is accepted** (`reviews/claude/2026-07-19-paper2-followup.md`,
`DECISION_LOG.md` 2026-07-19). Acceptance does not promote anything to
`VERIFIED`. `P2-BETAV-CIRC-01` is now **SUSPENDED**: the historical Finding 5
lattice pipeline is **NOT LOCATED** in the repository
(`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`), so the circularity question
cannot be tested directly and is neither demonstrated nor ruled out.

## Verified results

None. No claim is `VERIFIED` (no reviewer record, no archived provenance).
`SUPPORTED`: `β_F/β_B=2`, `β_V/β_B=−3`, `β_B(ξ)/β_B=1−6ξ`, continuum `G_c`
(`c=8`), lattice `I_0` (at `ma=0.02`), the `Z` factor-2 normalization
(`P2-NORM-01`), and the determinant-bookkeeping regression (`R_k=−(k+2)`,
`P2-BETAV-ASSEMBLY-01` — implementation only, does **not** test the historical
projection). See `CLAIMS.md`.

## Failed or retired routes

The first report's D1 (`β_F` Weyl-vs-Dirac) and D2 (`I_0` ≈1.2%) are both
**withdrawn** — artifacts of comparing across conventions before the source was
available (see `DECISION_LOG.md`). Superseded entries preserved.

## Active work

The **clean-room curved-background lattice Proca reconstruction with `k ≠ 1`**
(`P2-BETAV-RECON-01`, PROPOSED — a *new* pipeline, explicitly distinct from the
absent historical one) is the next scientific work; if built and faithful it
would inform, but not close, `P2-BETAV-CIRC-01`. Paper 3's numerical βV
dependency remains unresolved/suspended (not cleared); `P3-C-004`
(`C_6 = -G_V/2`) is structurally independent and unaffected.

## Blocked items

- `P2-BETAV-CIRC-01` — `SUSPENDED`, blocked by provenance (historical pipeline
  NOT LOCATED); cannot be tested directly.
- `P2-BETAV-RECON-01` full lattice pipeline — substantial implementation, not run.
- `P2-BETAV-01` (reproduce `−3.2(5)`) — deferred.

## Next administrative action

Scope and schedule `P2-BETAV-RECON-01` (clean-room Proca reconstruction).

## Last updated

2026-07-19
