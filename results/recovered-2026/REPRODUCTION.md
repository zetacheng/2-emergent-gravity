# Reproduction check — recovered Class-A gravity engine

**Producing script:** `scripts/recovered_2026/reproduce_check.py`
(`python scripts/recovered_2026/reproduce_check.py`). Raw:
`results/recovered-2026/regen/reproduce_check.json` (gitignored). Targets were
**pre-registered** from `paper/emergent_gr_paper_v2_15.tex` before running; no
value was tuned to match.

## Verdict summary

All five Class-A files **run** and reproduce the paper's sign structure;
`speed_check` reproduces the paper's light-cone numbers **quantitatively**.

## Quantitative table

| File | Quantity | Paper v2.15 (pre-registered) | Recovered output | Agreement |
|---|---|---|---|---|
| `speed_check` (A, `m=0.5`, `n=40`) | `c_χ²−1` (dim-4, protected) | `~5×10⁻¹³` (≈0) | `−5.46×10⁻¹³` | **reproduces (exact)** |
| | `ξ_χ` (boson dim-6) | `−0.078` (line 953) | `−0.0777` | **reproduces** |
| | `ξ_f` (fermion, analytic) | `−0.250` (line 954) | `−0.250` | **reproduces (exact)** |
| | `Δξ = ξ_χ−ξ_f` | `+0.17` (line 955) | `+0.172` | **reproduces** |
| `speed_check` (B, `n=96`) | `c_χ²` @ `ma=0.02,0.10,0.50,1.00` | `1.22, 1.42, 2.44, 3.77` (lines 983–986) | `1.251, 1.421, 2.438, 3.774` | **reproduces (≤2.6%)** |
| `seagull_check` (`m=0.5`) | `Z_h` sign (`M_Pl²=4NZ_h`) | `> 0` (eq:Mpl, `c₂>0`) | `+1.48×10⁻³` (`n=16`) | **reproduces (sign)** |
| | `xi_h` (graviton dim-6) | `< 0`, order `−1/6 ≈ −0.167` (Finding 4) | `n=8:−0.109`, `n=16:−0.142` | **reproduces (sign; → −1/6, finite-n residual)** |
| | `rho_v` (induced CC / one-point) | negative (induced Λ⁴) | `−4.057` | consistent (sign) |
| `tt_check` (`m=0.5`, bubble-only) | `Z_h` sign | `> 0` | `+4.86×10⁻³` | **reproduces (sign)** |
| | isotropy `Z_s/Z_t` (light-cone) | `= 1` | `1.0000000000` | **reproduces (exact)** |
| | `ξ_f` (analytic) | `−0.250` | `−0.250` | **reproduces (exact)** |
| | `xi_h` (bubble-only; seagull deferred) | `< 0` | `−0.052` | reproduces (sign) |
| `boson_loop` (`m_B=0.5`) | `Z_cov^B` sign (scalar induced kinetic) | `> 0` | `+6.72×10⁻³` | **reproduces (sign)** |
| | const-`h` validation (internal) | pert = exact | diff `~1×10⁻⁸` | **reproduces (self-consistent)** |
| `structure_decomp` | tool import + basis | (decomposition tool, no `run()`) | imports; `W` shape `(8,6)`, rank `4` | runs (tool) |

## Honest notes (recorded whichever way it fell)

- **`speed_check` is the strongest reproduction:** Case A matches to machine
  precision (dim-4 protected zero `5.46e-13`) and the dim-6 `ξ` values to `<1%`;
  Case B to `≤2.6%` (the `ma=0.02` point is `1.251` vs the paper's `1.22`, a
  finite-`n` difference, within `5%`).
- **`seagull_check` reproduces the sign structure of Finding 4** (`Z_h>0`,
  `xi_h<0`) — the load-bearing qualitative claim that minimal matter contributes
  negatively (`ξ_ind<0`). The **magnitude** of `xi_h` converges toward `−1/6`
  (`n=8→−0.109`, `n=16→−0.142`); at accessible grids it retains a `~15%`
  finite-`n` residual to the exact `−0.167`. Recorded as **reproduced (sign);
  magnitude approaching −1/6, not yet at paper precision at `n≤16`.** The paper
  itself flags the `Λ²`-level `Z_h`/`c₂` value as scheme-dependent and `c₂>0` as
  "at present a defining assumption" (lines 722–739), so the reproduced quantity
  here is the sign/structure, consistent with the paper's own honesty.
- **`tt_check`** is a bubble-only first-pass (contact/seagull deferred, per its
  own docstring); it reproduces `Z_h>0`, exact isotropy, and the analytic
  `ξ_f=−0.250`. Its `xi_h=−0.052` is the bubble-only value, not the
  Ward-complete one (that is `seagull_check`).
- **No file failed to reproduce.** None was "recovered but unverified."
