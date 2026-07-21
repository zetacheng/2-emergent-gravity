# Canonical report — complete the βV recovery; revive P2-BETAV-CIRC-01

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `recover/betav-complete` (off `recover/lattice-gravity-engine`).
**Type:** provenance completion + gate revival (scripts/docs/tests only).

## 1. Executive summary

The previously-missing `mlog_coeff.py` is recovered, so the βV (Proca) pipeline
is **complete and runs**. It **reproduces** the scalar `β_B` and the vector
`β_V` **sign** (Finding 5). The ratio `β_V/β_B` *magnitude* is grid-limited
(longitudinal-artifact dominated) at accessible grids and does **not** reach the
paper's `−3.2(5)`. Because the historical pipeline is no longer missing,
`P2-BETAV-CIRC-01` is revived `SUSPENDED → SPECIFIED` (discrimination `k`-scan
**runnable but not yet run**) — **no PASS/FAIL**. `β_V/β_B = −3.2(5)` remains an
**unpromoted, quarantined** paper value; the governance quarantine test is kept
as-is and still passes. This task lands + reproduces + makes-runnable; the
verdict is the separate `k`-scan.

## 2. Files landed (verbatim) and sha256

| File | Role | sha256 |
|---|---|---|
| `scripts/recovered_2026/mlog_coeff.py` | `TT_RECIPES` (5 fixed, `k`-independent TT projections) + `fit_mlog` | `9f4343f14e70e57122e62d4aa12a3c8b7f708455af03fa74cd18d87751d107f3` |
| `scripts/recovered_2026/proca_loop.py` | βV body — lattice Proca graviton loop `Z_V(m)` | `b2361db94eae0995a5a81b16552bb8cd5b4afa049d015ea9401e3b8eac1bc8f5` |
| `results/recovered-2026/fig_mlog.pdf` | historical scalar `β_B` figure | `11cdd36c19b73f67200802a87e5720a7700239d2d94e081a5f118bc069bf565e` |

All byte-identical to the PI's attachments (`cmp`); unedited (ruff-excluded).

## 3. Reproduction table (pre-registered targets vs recovered output)

| Quantity | Paper v2.15 | Recovered | Verdict |
|---|---|---|---|
| scalar `β_B` (paper window `0.125–0.55`) | `+2.50e-4` (meas.) / `+2.64e-4` (`1/384π²`) | `n=12:+3.00e-4, n=16:+3.09e-4, n=20:+2.82e-4` | **reproduces** (converging, finite-`n`) |
| vector `β_V` **sign** (`Z_V(m)` rise) | `<0` (Finding 5) | `Z_V` rises ⟹ `β_V<0` | **reproduces (sign)** |
| ratio `β_V/β_B` (light window) | `−3.2(5)` (`n=32`) / `−3` (analytic) | `n=12:−61, n=16:−16` | **sign-only / magnitude grid-limited** |
| ratio (heavy-inclusive window) | drift toward `−5` | `n=12: +16` (sign flips) | artifact-dominated (documented) |

Detail: `results/recovered-2026/BETAV_REPRODUCTION.md`. Raw:
`results/recovered-2026/regen/reproduce_betav.json` (gitignored).

## 4. Gate change: SUSPENDED → SPECIFIED (justification)

`P2-BETAV-CIRC-01` was `SUSPENDED` because the historical pipeline was missing.
It is now recovered and reproduces the scalar `β_B` and vector sign, so the
provenance block is gone and the discrimination `k`-scan is **runnable**. The
gate is therefore `SPECIFIED` — runnable, **not run**, **no verdict**. The
verdict (does `β_V/β_B` track `−(k+2)` or stay `−3`?) belongs to the separate
`k`-scan task. Structural hypothesis recorded (not a verdict): `TT_RECIPES` is
`k`-independent, so the projection cannot by construction force `−3`.

## 5. `−3.2(5)` remains unpromoted / quarantined

Recovery ≠ verification. The βV magnitude is not reproduced at accessible grids.
`P2-C9` (the `−3.2(5)` claim) stays `PROPOSED` — `CLAIMS.md` is unchanged. The
quarantine holds until the `k`-scan discrimination test passes.

## 6. Governance-test changes (honest, not a weakening)

- `test_circ01_remains_suspended` → `test_circ01_is_specified_after_recovery`:
  asserts the gate is in the **allowed** state `SPECIFIED`, with the recovery
  recorded and never PASS/FAIL. It left SUSPENDED only because the pipeline was
  recovered.
- `test_finding5_value_quarantined_as_unreproduced`: **kept as-is** and still
  passes. `−3.2(5)` is still not verified; the quarantine is intact.
- `test_finding5_claim_not_promoted`: still passes (`P2-C9` = `PROPOSED`).
- 9/9 governance tests green; no invariant kept green by weakening the
  quarantine.

## 7. Tests

`python -m pytest tests -q` (clean checkout): **31 passed, 2 deselected**
(full `-m "slow or not slow"` = 33). Structure test extended to require the
βV files, `BETAV_REPRODUCTION.md`, `fig_mlog.pdf`, `reproduce_betav.py`, and this
report.

## 8. What comes next (NOT this task)

The `P2-BETAV-CIRC-01` `k`-scan: vary `k ∈ {0,1,2,3,½}` with `TT_RECIPES` and
normalization fixed; if `β_V/β_B` tracks `−(k+2)` → PASS (and `−3.2(5)` may be
promoted); if it stays `−3` → circular (historical extraction impugned). This
task only makes it runnable.

## 9. git status / commits / remote

- `git status --porcelain`: clean.
- Commits (off `cdcbd84`):
  - `fb1da32` provenance: complete the betaV pipeline recovery (mlog_coeff.py recovered)
  - `5d5d1fc` provenance: betaV reproduction check (scalar beta_B, vector sign, ratio)
  - `c25df33` gate: revive P2-BETAV-CIRC-01 (SUSPENDED -> SPECIFIED); betaV pipeline recovered
  - `bcd6c3d` test: update governance guard for the betaV recovery
  - (this report + structure guard)
- `git ls-remote --heads origin`: recorded in the terminal summary after push.

## 10. Limitations

- βV *magnitude* is grid-limited (longitudinal artifact); `n=32` + longitudinal
  handling not feasible here. The sign is the robust reproduced result.
- The circularity **verdict** is not decided by this task.
