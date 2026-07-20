# βV reproduction check — recovered Proca pipeline

**Producing script:** `scripts/recovered_2026/reproduce_betav.py`
(`python scripts/recovered_2026/reproduce_betav.py [--n N]`). Raw:
`results/recovered-2026/regen/reproduce_betav.json` (gitignored). Targets were
**pre-registered** from Paper 2 v2.15 / `fig_mlog.pdf` before running; nothing
was tuned to match.

## Verdict summary

The complete βV pipeline (`mlog_coeff.py` + `proca_loop.py`) **runs**. The
**scalar `β_B`** and the **vector `β_V` sign** reproduce. The **ratio
`β_V/β_B` magnitude is grid-limited** at accessible grids (longitudinal-artifact
dominated) — recorded as such, not tuned. This is a *reproduction* result, not a
discrimination verdict; the `−3.2(5)` value stays quarantined.

## Table

| Quantity | Paper v2.15 (pre-registered) | Recovered output | Verdict |
|---|---|---|---|
| scalar `β_B` (`m²ln m²`, paper window `m_B a=0.125–0.55`) | `+2.50×10⁻⁴` (measured, `fig_mlog.pdf`) / `1/(384π²)=+2.64×10⁻⁴` | `n=12: +3.00e-4`, `n=16: +3.09e-4`, `n=20: +2.82e-4` | **reproduces** (converging into target, finite-`n` residual) |
| vector `β_V` **sign** (`Z_V(m)` rise) | `< 0` (Finding 5) | `Z_V` rises with `m` ⟹ `β_V<0` (`β_V=−8.7e-3` light win, `n=12`) | **reproduces (sign)** |
| ratio `β_V/β_B` (light window `m_V a≈0.11–0.30`) | `−3.2(5)` (paper, `n=32`) / `−3` (analytic) | `n=12: −61`, `n=16: −16` | **sign-only / magnitude grid-limited** |
| ratio `β_V/β_B` (heavy-inclusive window `0.20–0.45`) | drift toward `−5` (longitudinal artifact) | `n=12: +16` (sign flips) | artifact-dominated (as documented) |

## Honest notes (reported whichever way it fell)

- **`β_B` reproduces.** On the paper's window it is `+3.0×10⁻⁴` at `n=12` and
  falls to `+2.82×10⁻⁴` at `n=20`, converging into the measured/continuum band
  `+2.50…+2.64×10⁻⁴` with a finite-`n` residual. (On a *light* window it reads
  `+1.4×10⁻⁴` — window-sensitive; the paper's window is the pre-registered one.)
- **`β_V` sign reproduces robustly.** `Z_V(m)` rises with `m` on the light
  window, so `β_V<0` — the Finding 5 result that the vector is the first species
  to flip the `M_Pl²`-sign contribution.
- **The ratio magnitude does NOT reproduce at feasible grids.** At `n=12/16` the
  light-window ratio is `−61 / −16` and the heavy-inclusive window even flips
  sign to `+16`. This is the **documented longitudinal flat-band artifact**: the
  `1/m²`-enhanced `m⁴ln m²` contamination is degenerate with the signal and
  dominates the fit at accessible masses/grids. The paper's `−3.2(5)` requires
  `n=32` with careful longitudinal handling, which is not feasible here
  (a single Proca `n=32` axis-TT slope is prohibitively slow). Recorded as
  **"sign reproduced, magnitude grid-limited,"** not tuned toward `−3.2`.
- **`−3.2(5)` remains an unpromoted, quarantined paper value.** Recovery ≠
  verification; the discrimination verdict is the separate `P2-BETAV-CIRC-01`
  `k`-scan, now made *runnable* by this recovery.

## Structural fact relevant to the (separate) circularity test

`TT_RECIPES` (in `mlog_coeff.py`) is 5 fixed, unit-normalized, **`k`-independent**
TT polarizations, applied identically to fermion/scalar/vector loops. It has no
mechanism to normalize a determinant power `k` away — so the circularity worry
is *testable by the `k`-scan*, not built into the projection. That test is not
run here.
