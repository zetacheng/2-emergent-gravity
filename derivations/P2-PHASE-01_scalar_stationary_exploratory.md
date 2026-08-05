# Derivation note — `P2-PHASE-01` scalar stationary exploratory study

**Kind:** exploratory mean-field calculation. This note fixes the reduced
scalar calculation before any numerical output is produced. It does not
register a parameter domain, an admissibility criterion, or a gate result.

## Restricted object

The calculation is restricted to the explicitly declared `μ = 0` slice and to
the uniform scalar self-energy ansatz `M̂ = aM`. It is not a finite-density
enumeration and therefore is not an execution of `P2-PHASE-01` over its eventual
domain.

With Wilson parameter `r = 1`, define

```text
D(p; M̂) = Σ_μ sin² p_μ + W(p; M̂)²,
W(p; M̂) = M̂ + Σ_μ (1 − cos p_μ),
I₀(M̂) = ∫_BZ d⁴p/(2π)⁴ 1 / D(p; M̂).
```

The frozen scalar non-trivial gap equation is

```text
1 = 2 G I₀(M̂).
```

It is obtained from the complete reduced first derivative

```text
V′_red(M̂; G) = M̂ [1/(2G) − I₀(M̂)].
```

Thus `M̂ = 0` is retained as an algebraic stationary branch; the divided
non-trivial equation alone is never used to classify its curvature. The reduced
potential, with a declared common zero only within this scalar ansatz, is

```text
V_red(M̂; G) − V_red(0; G)
  = M̂²/(4G) − ∫₀^M̂ m I₀(m) dm.
```

The curvature used for the restricted one-dimensional check is the derivative
of the complete first derivative:

```text
V″_red(M̂; G) = 1/(2G) − I₀(M̂) − M̂ I₀′(M̂),
I₀′(M̂) = −2 ∫_BZ d⁴p/(2π)⁴ W(p; M̂) / D(p; M̂)².
```

Finite-difference curvature of the reconstructed potential is an independent
numerical regression check. Neither curvature is a full condensate-space
Hessian or a phase-admissibility statement.

## Symmetry check

The Wilson term enters `W` additively. The study therefore tests, rather than
assumes, whether `I₀(M̂) = I₀(−M̂)`. Positive and negative algebraic roots are
reported as distinct unless an exact symmetry is demonstrated.

## Numerical controls

Every reported integral uses product-midpoint Brillouin-zone quadrature at
three or more grid sizes and the offset-grid construction already used by
`P2-GAP-01`. The study reports straight/offset drift and only treats digits that
survive the finest refinement as stable. Root residuals are evaluated from the
undivided numerical integral. The onset analysis first inspects
`I₀(0) − I₀(M̂)` and then reports window-dependent bare-power fits and local
effective exponents; a logarithmic fit is attempted only if that inspection
supports one.

## Frozen-channel executability inventory

For each of S/P/V/A/T, a mean-field calculation is executable only if frozen
documents uniquely fix all of: HS normalization; the coefficient and sign of
the `G` quadratic term; a uniform condensate ansatz; for V/A/T the direction,
Lorentz/H(4) components and internal generators; and a common zero and measure
normalization for cross-family potential comparison. The scalar calculation is
the one explicitly fixed by `P2-GAP-01`. No Fierz projection, channel ansatz,
or cross-family normalization will be selected for any family that lacks these
inputs.

## Exclusions

The quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and the
historical Finding 5 extraction are not inputs to this calculation.
