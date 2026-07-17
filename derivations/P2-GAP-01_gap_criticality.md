# Derivation note — `P2-GAP-01`: gap-equation criticality

**Kind:** original-model calculation (leading-order / mean-field gap equation).

## Scientific question

The critical four-fermion coupling `G_c` of the scalar-channel gap equation, in
(1) the continuum with a sharp Euclidean 4-ball cutoff `|p| < Λ`, and (2) the
lattice with Wilson fermions (`r = 1`). Derive — not assume — the relation
between `G_c` and the gap-equation integral `I_0`.

## Which criticality this is

This is the **gap-equation (leading-order effective-potential) criticality**:
the point at which the mean-field effective potential `V(Σ)` for the scalar
self-energy `Σ` first develops a nontrivial stationary point, equivalently
where the linearized gap equation has a nontrivial solution. It is **not** a
channel *bubble* criticality (the location of a pole/zero in a specific
scattering channel's resummed bubble sum). The leading-order gap equation is a
single tadpole self-consistency; it does not by itself resolve the different
channel bubbles, so this derivation **cannot distinguish** the gap-equation
criticality from the bubble criticalities beyond leading order — that
distinction is out of scope here and is flagged rather than glossed.

## Assumptions and conventions

See `CONVENTIONS.md`. Euclidean `d=4`; attractive scalar (`ψ̄ψ`) channel;
Wilson `r=1`, `s̄_μ=sin p_μ`, `W(p)=Σ_μ(1−cos p_μ)`.

## Derivation of `G_c = 1/(2 I_0)`

Mean-field (Hubbard–Stratonovich) treatment of the attractive scalar-channel
four-fermion interaction. Introducing the scalar auxiliary `Σ` (the dynamical
self-energy), the gap equation is the tadpole self-consistency

```
Σ = 2 G · Σ · B(Σ),      B(Σ) = (untraced scalar bubble) = ∫ d⁴p/(2π)⁴ 1/D(p;Σ),
```

where `D` is the propagator denominator and `G` is the **channel coupling**:
we absorb the Dirac trace (`tr 𝟙₄ = 4`) into the definition of `G`, so that the
combinatorial prefactor of the gap equation is exactly `2`. (In the alternative
"NJL" normalization `L_int = G_N(ψ̄ψ)²`, one has `G = 4 G_N` and the gap
equation reads `1 = 8 G_N B`; the physics — the value of `I_0` and the ratio of
continuum to lattice `G_c` — is normalization-independent.)

A nontrivial solution `Σ ≠ 0` bifurcates from `Σ = 0` when

```
1 = 2 G_c B(0)  ≡  2 G_c I_0,     I_0 ≡ B(0).      (★)
```

Hence **`G_c = 1/(2 I_0)`**, with `I_0` the untraced scalar bubble evaluated at
the chiral point.

### Continuum, sharp 4-ball

`D = p² + Σ²`, so `I_0 = ∫_{|p|<Λ} d⁴p/(2π)⁴ 1/p²`. With `∫d⁴p = 2π² p³ dp`,

```
I_0^cont = (2π²/(2π)⁴) ∫_0^Λ p dp = (1/(8π²))·(Λ²/2) = Λ²/(16π²).
```

Therefore

```
G_c^cont = 1/(2 I_0^cont) = 8π²/Λ²  =  c · π²/Λ²  with  c = 8  (exact).
```

### Lattice, Wilson `r = 1`

The Wilson propagator denominator at self-energy `Σ` is
`D = Σ_μ sin²p_μ + (W(p)+Σ)²`. At the chiral point `Σ→0`, `D = Σ_μ sin²p_μ +
W(p)²` (the Wilson term acts as the momentum-dependent regulating mass that
lifts the doublers). Hence

```
I_0^lat = ∫_{BZ} d⁴p/(2π)⁴  1 / ( Σ_μ sin²p_μ + W(p)² ),   W(p)=Σ_μ(1−cos p_μ),
```

`p_μ ∈ (−π,π]`, and `G_c^lat = 1/(2 I_0^lat)` by (★).

`I_0^lat` is computed by product-midpoint quadrature over the Brillouin zone,
with convergence demonstrated by grid refinement and an **offset (half-shifted)
grid** cross-check (the two grids sample the integrand differently and must
agree at the ≈1% level or better).

## Expected limiting cases / cross-checks

- `c = 8` exact in the continuum.
- The lattice integrand reduces to the continuum `1/p²` in the small-`p` region
  (`Σsin²p→p²`, `W²→(p²/2)²→0` faster), so the lattice `I_0` inherits the same
  IR behaviour and differs from the continuum only by UV lattice artifacts.

## Known failure modes / caveats

- **Wilson chiral-symmetry breaking.** The Wilson term explicitly breaks chiral
  symmetry, so `⟨ψ̄ψ⟩ ≠ 0` at `Σ=0` (additive mass shift). The leading-order
  `I_0` defined above uses `W` as the tree-level regulating mass at `Σ=0`; a
  fully consistent treatment would tune the bare mass to the critical value
  `κ_c` to restore effective chiral symmetry. This subtlety is recorded, not
  hidden; it affects the absolute lattice `G_c` at the level of lattice
  artifacts, not the definition of `I_0`.
- The absolute value of `G_c` depends on the coupling normalization (the `2`);
  `I_0` (the integral) is the convention-independent, pre-registered deliverable.

## Pre-registered verdict

Report `I_0^cont = Λ²/(16π²)`, `G_c^cont = 8π²/Λ²` (`c=8`); `I_0^lat` from the
Brillouin-zone integral with its convergence/offset spread, and
`G_c^lat = 1/(2 I_0^lat)`. Compare to the paper **only** in Task 6.

## Implementing script

`scripts/gap_criticality.py` (`python -m scripts.gap_criticality`).
