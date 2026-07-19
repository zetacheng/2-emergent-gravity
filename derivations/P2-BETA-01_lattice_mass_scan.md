# Derivation note — `P2-BETA-01`: lattice mass-scan extraction of `β_B`

**Kind:** numerical proxy (lattice-regularized realization of the continuum
heat-kernel coefficient).

## Scientific question

Extract the `m² ln m²` coefficient `β_B` of the induced Einstein–Hilbert
kinetic coefficient `Z(m²)` for a minimally coupled real scalar (the condensate
scalar) from a **lattice mass scan**, with an honest uncertainty derived from
*our own* fit systematics — independently of the analytic result of
`P2-HK-01` and of any paper value.

## Assumptions and conventions

See `CONVENTIONS.md`. Euclidean `d=4`; scalar lattice propagator
`1/(p̂²+m²)`, `p̂² = Σ_μ 4 sin²(p_μ/2)`; `m` in lattice units (`m ≡ m_B a`).

## The lattice observable

The induced EH coefficient of a non-minimally coupled scalar is, at the level
of its `m²ln m²` (logarithmic) piece,

```
Z(m²) = (1/6 − ξ) · (1/2) · ⟨φ²⟩,      ⟨φ²⟩ = ∫ d⁴p/(2π)⁴ 1/(p²+m²),
```

because the `m²ln m²` coefficient of the induced `R` term is governed by the
same Seeley–DeWitt `a_1 = (1/6−ξ)R` that also multiplies the scalar tadpole
`⟨φ²⟩`. The tadpole's `m²ln m²` coefficient is universal (it comes from the IR
region `p ~ m`, identical on lattice and in continuum):

```
⟨φ²⟩ = (1/16π²)[Λ_UV² − m² ln(Λ_UV²/m²) + …]
     ⟹ coefficient of m² ln m² in ⟨φ²⟩ is + 1/(16π²).
```

For a **minimally coupled** scalar (`ξ = 0`) we therefore define the lattice
observable

```
Z_lat(m²) = (1/12) ∫_BZ d⁴p/(2π)⁴ 1/(p̂² + m²),     p̂² = Σ_μ 4 sin²(p_μ/2),
```

whose `m²ln m²` coefficient is the lattice estimate of `β_B`. Because the log
is IR-universal, the fitted coefficient reproduces the continuum
`β_B = (1/12)(1/16π²) = 1/(192π²)` up to fit systematics and lattice-analytic
contamination — which is exactly what the scan quantifies.

## Fit

Fit, by linear least squares in the basis `{1, m², m² ln m², m⁴}`,

```
Z(m) = z_0 + z_1 m² + β m² ln m² + z_2 m⁴,    m ∈ [0.125, 0.55].
```

`β` is the extracted `β_B`.

## Honest uncertainty (our own systematics)

Report the **spread** of `β` over:

1. **fit window** — vary the lower/upper ends of `m ∈ [0.125, 0.55]`;
2. **ansatz** — with and without the `z_2 m⁴` term;
3. **lattice volume** — infinite-volume BZ integral vs finite `L⁴` momentum
   sums (`L = 16, 24, 32`).

The reported uncertainty is the full spread across these variations, **not** the
formal least-squares error of a single fit.

## Expected value / cross-check

`β_B ≈ +1/(192π²) ≈ 5.28e−4` (sign in the `Z=(1/12)⟨φ²⟩` convention; the
`P2-HK-01` convention carries the opposite overall sign — the magnitude is the
robust quantity). The raw tadpole coefficient should be `≈ +1/(16π²) ≈
6.33e−3`.

## Known failure modes

- `m²` and `m² ln m²` are partially collinear over a bounded window, so the
  fitted `β` is sensitive to window and ansatz — this is precisely why the
  systematic spread (not a formal error) is reported.
- Lattice-analytic terms (`z_1, z_2`) absorb UV artifacts; too small a window
  starves the log, too large a window lets higher `m⁴ ln m²` terms leak in.

## Pre-registered verdict

Report the central `β_B` and its systematic spread. Compare to the continuum
`P2-HK-01` value and to the paper **only** in Task 6.

## Implementing script

`scripts/lattice_beta_scan.py` (`python -m scripts.lattice_beta_scan`).
