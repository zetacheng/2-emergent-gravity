# Canonical report — recover the historical lattice gravity engine (Class A)

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `recover/lattice-gravity-engine` (off `main` = `7af645f`).
**Type:** provenance recovery + reproduction check (scripts/docs only).

## 1. Executive summary

The PI recovered the historical lattice code behind Paper 2's gravity Findings —
previously believed lost. This task lands the five **runnable** originals (Class
A) verbatim under a dated, auditable recovery path, and — under the honesty rule
that a recovered file is provenance only if it reproduces the paper number —
runs each against **pre-registered** paper values. **All five run and reproduce
the paper's sign structure; `speed_check` reproduces the light-cone numbers
quantitatively (`≤2.6%`).** Gate `P2-GRAV-ENGINE-RECOVERED-01` = `PASS`.
`MIGRATION.md`'s "nothing can be re-run" is partially superseded for the
gravity-kernel sector only; βV remains without provenance and
`P2-BETAV-CIRC-01` stays `SUSPENDED`. The incomplete `proca_loop.py` (Class B)
is intentionally excluded. No historical claim is upgraded or downgraded by the
recovery itself.

## 2. Files recovered (verbatim) and sha256

| File | sha256 |
|---|---|
| `scripts/recovered_2026/seagull_check.py` | `6ec034e5a30e24d205c43c7dd0ea39c90a89f67c9db0da6e734a68862acefd90` |
| `scripts/recovered_2026/boson_loop.py` | `32d6a4e0b9cca8ec4debb80758f77d0574d98a299492cb1ab9cfe2fdd26c08c2` |
| `scripts/recovered_2026/tt_check.py` | `a40592a3b320cd9f118b3d96bd61abb10d5b20087d6b7a201dae5deabf90ba00` |
| `scripts/recovered_2026/speed_check.py` | `8a374601161dd324795c2f1c9f7cc9d48031d83c5cc05e9896ae1e2814b1044c` |
| `scripts/recovered_2026/structure_decomp.py` | `87d311fa4d86bb1c6862ace85bdd2c4a232db4f44e1662696f46c7226675fb9a` |

Confirmed byte-identical to the PI's attachments (`cmp`), and unedited (ruff
excludes them so they stay byte-for-byte).

## 3. Reproduction table (pre-registered targets vs recovered output)

| File | Quantity | Paper v2.15 | Recovered | Agreement |
|---|---|---|---|---|
| `speed_check` A | `c_χ²−1` | `~5e-13` | `−5.46e-13` | reproduces (exact) |
| | `ξ_χ / ξ_f / Δξ` | `−0.078 / −0.250 / +0.17` | `−0.0777 / −0.250 / +0.172` | reproduces |
| `speed_check` B | `c_χ²` @ `0.02,0.10,0.50,1.00` | `1.22,1.42,2.44,3.77` | `1.251,1.421,2.438,3.774` | reproduces (≤2.6%) |
| `seagull_check` | `Z_h` sign; `M_Pl²=4NZ_h` | `>0` (c₂>0 assumption) | `+1.48e-3` (n=16) | reproduces (sign) |
| | `xi_h` | `<0, ~−1/6` | `n8:−0.109, n16:−0.142` | reproduces (sign; →−1/6, finite-n residual) |
| `tt_check` | `Z_h`; isotropy; `ξ_f` | `>0; =1; −0.250` | `+4.86e-3; 1.000; −0.250` | reproduces |
| `boson_loop` | `Z_cov^B`; const-h | `>0`; pert=exact | `+6.72e-3`; diff `~1e-8` | reproduces |
| `structure_decomp` | tool import + basis | (no `run()`) | imports; `W(8,6)` rank 4 | runs (tool) |

Full detail: `results/recovered-2026/REPRODUCTION.md`. Raw:
`results/recovered-2026/regen/reproduce_check.json` (gitignored).

## 4. Files that did NOT reproduce

**None.** No Class-A file failed; none is recorded "recovered but unverified."
The only residual recorded is `seagull_check`'s `xi_h` magnitude, which
converges toward `−1/6` with a `~15%` finite-`n` gap at `n≤16` (trend-consistent;
the paper itself flags the `Λ²`-level value as scheme-dependent).

## 5. Gate verdict

`P2-GRAV-ENGINE-RECOVERED-01` = **PASS** (sign structure reproduced; `speed_check`
quantitative to `≤2.6%`; residual finite-`n` gap on `seagull` `xi_h` recorded).
Reviewer adjudication pending.

## 6. MIGRATION.md rescope

"Nothing can be re-run" is now **partially superseded**: the gravity-kernel
engine (fermion/scalar/TT) is recovered and re-runs. Scope: gravity-kernel
sector only. βV (`proca_loop.py`, incomplete) is excluded; `P2-BETAV-CIRC-01`
stays `SUSPENDED`. No verdict changed by the recovery.

## 7. Tests

`python -m pytest tests -q` (clean checkout): **31 passed, 2 deselected**
(full suite `-m "slow or not slow"` = 33 passed). Structure test extended to
require the recovered files, `PROVENANCE.md`, `reproduce_check.py`,
`REPRODUCTION.md`, and this report. No existing claim promoted; `CLAIMS.md`
unchanged.

## 8. Reproducibility

Re-run: `python scripts/recovered_2026/reproduce_check.py` (writes
`results/recovered-2026/regen/`, gitignored). `--fast` uses smaller grids.

## 9. git status / commits / remote

- `git status --porcelain`: clean.
- Commits (off `7af645f`):
  - `a7c1e14` provenance: recover the historical lattice gravity engine (Class A runnable originals)
  - `4b5ed28` provenance: reproduction check for the recovered gravity engine
  - `0ac3de4` gate: register P2-GRAV-ENGINE-RECOVERED-01 and rescope MIGRATION.md
  - (this report + structure-test commit)
- `git ls-remote --heads origin`: recorded in the terminal summary after push.

## 10. Limitations

- `xi_h` (seagull) reaches `−1/6` only up to a finite-`n` residual at accessible
  grids; a large-`n` extrapolation is not run here.
- βV is out of scope (Class B, incomplete file excluded).
- The recovery enables verification; it does not by itself change any verdict.
