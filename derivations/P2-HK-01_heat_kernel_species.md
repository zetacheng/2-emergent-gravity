# Derivation note — `P2-HK-01`: heat-kernel species coefficients

**Kind:** original-model calculation (one-loop induced Einstein–Hilbert term).

## Scientific question

For each matter species, what is the universal coefficient `β_s` of the
`m² ln m²` term in the induced Einstein–Hilbert (EH) kinetic coefficient
`Z(m²)`, computed from the Seeley–DeWitt (heat-kernel) expansion? Report the
convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`.

## Assumptions and locked conventions

See `CONVENTIONS.md`. In particular: Euclidean `d=4`; `Δ = −∇² + E` with
`a_1 = tr[(1/6)R·𝟙 − E]`; mass separated as `Δ + m²`; boson `W = +½ Tr ln`,
Dirac `W = −½ Tr ln` over the 4-component spinor bundle; Proca determinant
structure `det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`.

## Analytic derivation

### Effective action and the `m² ln m²` term

For a species with `W = p · Tr ln(Δ+m²)` (`p = +½` per bosonic `det^{−1/2}`
factor, `p = −½` per `det^{+1/2}` factor / fermion loop),

```
W = p Tr ln(Δ+m²) = −p ∫₀^∞ (dτ/τ) Tr e^{−τ(Δ+m²)}
  = −p ∫₀^∞ (dτ/τ) (4πτ)^{−2} e^{−τm²} ∫√g Σ_k a_k τ^k .
```

The EH term is the `k=1` (`R`-linear) coefficient `a_1`:

```
W ⊃ −p (4π)^{−2} ∫√g a_1 · ∫₀^∞ dτ τ^{−2} e^{−τm²} .
```

**Route 2 (proper-time / incomplete gamma).** With a proper-time UV cutoff
`τ > 1/Λ²`,

```
∫_{1/Λ²}^∞ dτ τ^{−2} e^{−τm²} = m² Γ(−1, m²/Λ²)
  = Λ² + m² ln(m²/Λ²) + m²(γ−1) + O(m⁴/Λ²),
```

using `Γ(−1,x) = 1/x + ln x + (γ−1) + O(x)`. The coefficient of `m² ln m²`
is therefore **exactly `+1`** (`ln(m²/Λ²) = ln m² − ln Λ²`, and `m` is in
units of `Λ`). Hence

```
Z(m²) ⊃ β_s m² ln m²,   with   β_s = −p_s (4π)^{−2} (tr a_1 / R).
```

This `+1` coefficient of `m² ln m²` from the proper-time integral is the
independent second route; it fixes the *m-dependence*, while `a_1` supplies
the *species content*.

### Bundle traces (`a_1 = (1/6)R·𝟙 − E`)

Let `d_s = tr 𝟙` (bundle dimension) and `e_s ≡ tr E / R`. Then
`tr a_1 / R = d_s/6 − e_s`.

| Species | det factor(s) | `d_s` | `E` | `e_s = tr E/R` | `tr a_1/R = d_s/6 − e_s` | `p_s` |
|---|---|---|---|---|---|---|
| Real scalar (minimal) | `det^{−1/2}` | 1 | 0 | 0 | `1/6` | `+½` |
| Non-minimal scalar `ξ` | `det^{−1/2}` | 1 | `ξR` | `ξ` | `1/6 − ξ` | `+½` |
| Dirac fermion | `det^{−1/2}` (squared op) | 4 | `(1/4)R·𝟙₄` | `1` | `4/6 − 1 = −1/3` | `−½` |
| Proca vector part | `det^{−1/2}` | 4 | `R^{μ}{}_{ν}` | `1` | `4/6 − 1 = −1/3` | `+½` |
| Proca scalar part | `det^{+1/2}` | 1 | 0 | 0 | `1/6` | `−½` |

Justifications:
- Scalar: `E = ξR`, minimal `ξ=0`. Conformal value `ξ=1/6`.
- Dirac: Lichnerowicz `−(γ·∇)² = −∇² + (1/4)R` ⟹ `E = (1/4)R·𝟙₄`,
  `tr E = 4·(1/4)R = R`. Fermion loop sign `p = −½`. Well-known result:
  a single Dirac field's `R`-linear coefficient is `tr a_1 = −R/3`.
- Proca vector: 1-form (Hodge) Laplacian has `E^{μ}{}_{ν}=R^{μ}{}_{ν}`,
  `tr E = R^{μ}{}_{μ} = R`. Compensating Stueckelberg scalar carries the
  opposite determinant power (`p = −½`), `E=0`.

### Species coefficients

With `K ≡ (4π)^{−2} = 1/(16π²)` and `β_s = −p_s K (tr a_1/R)`:

```
β_B      = −(+½) K (1/6)      = −K/12  = −1/(192π²)
β_B(ξ)   = −(+½) K (1/6 − ξ)  = −K(1/6 − ξ)/2
β_F      = −(−½) K (−1/3)     = −K/6   = −1/(96π²)
β_V      = [−(+½)K(−1/3)] + [−(−½)K(1/6)] = K/6 + K/12 = K/4 = +1/(64π²)
```

### Ratios (convention-independent)

```
β_B(ξ)/β_B = (1/6 − ξ)/(1/6) = 1 − 6ξ
β_F/β_B    = (−K/6)/(−K/12)  = +2
β_V/β_B    = (K/4)/(−K/12)   = −3
```

## Expected limiting cases and cross-checks

- `β_B(ξ=1/6) = 0`: a conformally coupled scalar induces no `R` term at the
  `m² ln m²` order — correct (conformal coupling kills `a_1`'s `R` part).
- `β_V/β_B = −3` reproduces the analytic value the paper quotes for the Proca
  ratio (recorded here as a pre-registered prediction, **not** as a target).
- Route-2 proper-time integral independently yields the `+1` coefficient of
  `m² ln m²`, decoupled from the `a_1` bundle-trace route.

## Known failure modes

- Sign of `E` and of the fermion loop must be tracked consistently; the
  *ratios* are robust to an overall normalization/sign convention, so they are
  the primary deliverable.
- The overall normalization of `β_s` (absolute value, and the `4N` divisor in
  the definition of `Z`) is convention-dependent; both the raw value and the
  ratios are reported so a convention mismatch can be diagnosed, not hidden.

## Pre-registered verdict

Report `β_B = −1/(192π²)`, `β_F = −1/(96π²)`, `β_V = +1/(64π²)`,
`β_B(ξ) = −(1/6−ξ)/(32π²)`, and ratios `(2, −3, 1−6ξ)`. Compare to the paper
**only** in Task 6.

## Implementing script

`scripts/hk_species.py` (run `python -m scripts.hk_species`).
