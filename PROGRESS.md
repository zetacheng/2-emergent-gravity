# Progress

## Paper identity

Paper 2 — Emergent Gravity from Lattice Fermion Fields.

## Current version

v2.15 (paper `.tex` imported; see `MIGRATION.md` and
`results/comparison/PAPER_COMPARISON.md`).

## Current scientific status

Independent verification sweep completed and, after importing the paper source,
**re-adjudicated**: gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-NORM-01`
(PASS) and `P2-BETAV-CIRC-01` (OPEN). The recomputation **confirms Paper 2
v2.15** once conventions are matched. No legacy source exists (`MIGRATION.md`).

The normalization/gap/circularity follow-up has **one independent reviewer
record and is accepted** (`reviews/claude/2026-07-19-paper2-followup.md`,
`DECISION_LOG.md` 2026-07-19). Acceptance does not promote anything to
`VERIFIED`. `P2-BETAV-CIRC-01` **remains OPEN**.

## Verified results

None. No claim is `VERIFIED` (no reviewer record, no archived provenance).
`SUPPORTED`: `β_F/β_B=2`, `β_V/β_B=−3`, `β_B(ξ)/β_B=1−6ξ`, continuum `G_c`
(`c=8`), lattice `I_0` (at `ma=0.02`), the `Z` factor-2 normalization
(`P2-NORM-01`), and the structure-dependence of the `β_V` target. See `CLAIMS.md`.

## Failed or retired routes

The first report's D1 (`β_F` Weyl-vs-Dirac) and D2 (`I_0` ≈1.2%) are both
**withdrawn** — artifacts of comparing across conventions before the source was
available (see `DECISION_LOG.md`). Superseded entries preserved.

## Active work

The **full curved-background lattice Proca discrimination test with `k ≠ 1`**
(the decisive `P2-BETAV-CIRC-01` layer: does the actual lattice extraction
return `-(k+2)` or stay fixed near `-3`?) is the active/open scientific work.
`P2-BETAV-CIRC-01` remains `OPEN`. Paper 3's numerical βV dependency remains
unresolved/suspended (not cleared) until this test is completed;
`P3-C-004` (`C_6 = -G_V/2`) is structurally independent and unaffected.

## Blocked items

- `P2-BETAV-CIRC-01` full lattice pipeline — substantial implementation, not run.
- `P2-BETAV-01` (reproduce `−3.2(5)`) — deferred.

## Next administrative action

Schedule the full lattice Proca `k ≠ 1` discrimination run for
`P2-BETAV-CIRC-01`.

## Last updated

2026-07-19
