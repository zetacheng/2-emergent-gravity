# Result — `P2-BETA-01`: lattice mass-scan extraction of `β_B`

**Scientific question.** Extract the `m² ln m²` coefficient `β_B` of the
induced EH kinetic coefficient `Z(m²)` for a minimally coupled real scalar from
a lattice mass scan, with an honest uncertainty from our own fit systematics.

**Gate:** `P2-BETA-01`. **Derivation:** `derivations/P2-BETA-01_lattice_mass_scan.md`.
**Producing script:** `scripts/lattice_beta_scan.py` (`python -m scripts.lattice_beta_scan`).

## Artifact map

- `raw/lattice_beta_scan.json` — authoritative frozen output.
- `regen/` — non-authoritative re-runs (gitignored).
- `environment.txt`, `branch.txt`, `commit_parent.txt` — provenance.

## Computed value (pre-registration: computed before consulting the paper)

`Z_lat(m²) = (1/12) ∫_BZ 1/(p̂²+m²)`, fit `z0 + z1 m² + β m²ln m² + z2 m⁴`
over `m ∈ [0.125, 0.55]` (18 points):

| Quantity | Value |
|---|---|
| **`β_B` (central)** | **`5.44e-4`** |
| primary systematic spread (window + ansatz) | `±0.50e-4` (range `5.39–5.89e-4`) |
| primary std over variants | `1.7e-5` |
| continuum reference `1/(192π²)` | `5.277e-4` |
| central offset above continuum | `+3.1 %` |

**Uncertainty.** The primary uncertainty is the spread over fit window and
ansatz (with/without `m⁴`) at infinite volume: `β_B = 5.4(5)e-4`. The dominant
single contributor is the ansatz — dropping `m⁴` raises `β` to `5.89e-4`
because the window extends to `m=0.55` where `m⁴` contamination is real.

**Lattice-volume convergence (reported separately).** Finite `L⁴` momentum
sums converge to the infinite-volume value as `L` grows:
`L=24→6.99e-4, L=32→5.73e-4, L=48→5.45e-4, L=∞→5.44e-4`. Small `L` is
quadrature-limited (too few modes resolve the IR log), so it is a convergence
trend, not an equal-weight systematic.

## Interpretation

The lattice mass scan recovers `β_B ≈ 5.4e-4`, agreeing with the continuum
`1/(192π²) = 5.28e-4` at the few-percent level (central `+3.1 %`, within the
`±9 %` fit systematics). The residual positive offset is the expected upward
bias of a finite-window fit (higher `m⁴ ln m²` terms leaking into the log
coefficient); tightening the window toward `m→0` lowers `β` toward the
continuum value (`win_0.125_0.45 → 5.39e-4`).

**Sign.** `β_B` is positive in the `Z=(1/12)⟨φ²⟩` convention used here; the
`P2-HK-01` heat-kernel convention carries the opposite overall sign. The
magnitude is the robust, convention-independent quantity.
