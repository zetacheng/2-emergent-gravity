# Derivation — `P2-BETAV-CIRC-01` determinant decomposition (Phase 1, no scan)

**Kind:** operator-level adjudication of the recovered lattice Proca determinant.
**No k-scan is run.** Numerical evidence: `scripts/betav_decomp_check.py`
(committed first, no target) → `results/P2-BETAV-CIRC-01/decomp/regen/decomp_check.json`.

Conventions: `a_μ(k) = e^{ik_μ}−1`, `ŝ² = Σ_μ|a_μ|² = Σ_μ 4sin²(k_μ/2) = p̂²`.

## 1. The exact determinant `proca_loop.py` computes

The flat (background `h=0`) non-minimal Proca kernel is

```
M_{μν}(k) = (ŝ²+m²) δ_{μν} − a_μ a_ν* .
```

Its spectrum (verified numerically, `proca_eigenstructure`): the three
directions orthogonal to `a` give eigenvalue `ŝ²+m²` (transverse); the direction
`â = a/|a|` gives `M â = (ŝ²+m²)â − a(a*·a)/|a| = (ŝ²+m²)â − ŝ²â = m² â`, i.e.
eigenvalue **`m²`** (longitudinal). Hence

```
spec M = { ŝ²+m² (×3 transverse),  m² (×1 longitudinal) },
det M(k) = m² · (ŝ²+m²)³ .
```

Loop (boson, `Γ = +½⟨ln det M⟩`). `Z` is extracted as the axis-TT slope of
`g2_axis_proca`: the bubble `−½ Σ_recipe ⟨ tr[ G(k) U(k,q) G(k+q) U(k+q,−q) ] ⟩`,
projected on the 5 fixed, unit-normalized, `k`-independent `TT_RECIPES`, `/5`,
then `fit_even`/`fit_mlog` in `q²`/`m²`. `G_flat` is the Sherman–Morrison Proca
propagator with eigenvalues `1/(ŝ²+m²)` (transverse) and — acting on `â` —
`1/m²` (longitudinal, verified: `long_propagator_eig = 11.111 = 1/m²`).

## 2. Can an invariant longitudinal contribution to `Z` be defined? — NO

An additive "longitudinal `Z`" would require the flat transverse/longitudinal
block split to be preserved by the metric-variation (graviton) vertices. It is
**not** (see §6): the one-graviton vertex `δM` has nonzero off-block elements
`⟨T|δM|L⟩` (max `0.17`, `vertex_TL_mixing`). Therefore any separate longitudinal
`Z` assignment is **basis-dependent / non-invariant**, and none is assigned.

In particular we do **not** infer a separately additive scalar contribution from
the `1/m²` (longitudinal) term of `G_flat`: the `1/m²` pole is a propagator
matrix element, not an independent determinant factor whose loop can be added.

## 3. Is the external scalar loop the same operator as the Proca longitudinal? — NO

- **External scalar** (`boson_loop`/`g2_axis_boson`): kernel
  `Δ₀ = MB_flat = ŝ²+m²` — a **propagating** operator; propagator `1/(ŝ²+m²)`.
- **Proca longitudinal factor**: `m²` — **ultralocal**, momentum-independent
  (verified: eigenvalue spread over varying `p̂²` is `3×10⁻¹⁶`); propagator
  `1/m²`.

They are **different operators**: `Δ₀ = ŝ²+m²` vs `m²`. They differ at every
level that matters here:
- *momentum dependence:* `Δ₀` propagates; the longitudinal factor does not;
- *propagator:* `1/(ŝ²+m²)` vs `1/m²` (the latter drives the paper's
  documented `1/m²`-enhanced longitudinal artifact);
- *`m²ln m²` content:* `½ln det Δ₀` integrates a propagating spectrum over the
  BZ and carries the universal IR `m²ln m²` scalar coefficient; `½ln(m²)` is a
  momentum-independent constant contributing to the induced action differently
  (no propagating IR log of the `Δ₀` type).

**Consequence:** an external minimally-coupled scalar loop cannot legitimately
represent a change in the Proca compensator power, because the compensator is
the ultralocal `m²` factor, not `Δ₀`.

## 4. The determinant identities to adjudicate

- **(a) complete non-minimal Proca determinant** `det M_Proca` — what
  `proca_loop.py` actually computes on a *curved* background (via numerical
  `h`-derivatives of `M(h)`).
- **(b) flat spectral identity** `det M_Proca(k) = m²(ŝ²+m²)³` — holds at `h=0`
  only; it is *not* an operator factorization of the curved determinant
  (the factors mix under `δh`, §6).
- **(c) external scalar determinant** `det Δ₀`, `Δ₀ = ŝ²+m²` — a *different*
  operator (§3).
- **(d) gauge-fixed / Stueckelberg quotient** in the analytic paper:
  `det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)` — a *continuum, gauge-fixed*
  bookkeeping identity, valid in the covariant continuum, **not** an operator
  identity of the recovered lattice `M`.

**Which does the historical `k=1` correspond to?** The recovered pipeline
computes **(a)** (its flat check is (b)); it does **not** implement (c) or (d).
The analytic `−3` lives in (d); the recovered numerics live in (a). These are
different objects — which is exactly why the recovered numerics give `−16`/`−61`
(grid/artifact limited), not `−3`.

## 5. The generalized-`k` deformation — derived: none valid exists

We do **not** posit `3 ln(ŝ²+m²)+k ln m²` or `Γ_Proca+(k−1)Γ_scalar`. Deriving
from the operators:

- The compensator sector of `det M_Proca` is the ultralocal `m²` factor **inside
  the same 4×4 kernel** as the transverse block; on a curved background the two
  are **not** separate determinants (§6). So "raising the compensator power to
  `k`" is not an operation on `det M` — there is no `k`-labelled factor to raise.
- Replacing/adding the external scalar `det Δ₀` does **not** deform the
  compensator (§3: `Δ₀ ≠ m²`). `Γ_Proca + (k−1)Γ_scalar[Δ₀]` at `k=1` trivially
  equals `Γ_Proca` (the added term vanishes), but for `k≠1` it adds *external
  propagating scalars* — a **different multi-species theory**, not a deformation
  of the Proca compensator. And since the Proca already contains a longitudinal
  sector, adding scalars at any nonzero coefficient **double-counts** a
  longitudinal-type sector while using the wrong operator for it.

Therefore **no operator-defined compensator-power deformation of the recovered
Proca determinant exists** that (i) changes the compensator multiplicity,
(ii) reduces to recovered Proca at the physical point, and (iii) avoids
double-counting. This is the obstruction (Task 2).

## 6. Full metric-variation decomposition — block-diagonality FAILS

`M(h) = 2·kin_form(J2(h),·) + m² J(h)`, `J2 = √g\,g^{-1}⊗g^{-1}`, `J = √g\,g^{-1}`.
The one-graviton vertex `δM = U` (from `vertexV`) and the seagull `δ²M` are dense
4×4 in the vector index. Projected onto the flat eigenbasis `{3 transverse ⟂ a,
1 longitudinal ∝ a}`, `δM` has **nonzero** transverse↔longitudinal blocks:
`max|⟨T|δM|L⟩| = 0.17` (`vertex_TL_mixing`). Hence the bubble contains genuine
mixed terms

```
G_T δM G_L δM  and  G_L δM G_T δM  ≠ 0,
```

so the induced `Z` is **not** the sum of a pure three-transverse determinant and
an independently computable longitudinal/scalar determinant. The flat
factorization `det M = m²(ŝ²+m²)³` does **not** lift to an additive split of the
curved induced action. No sector split is manufactured by separating propagator
terms.

## 7. Non-linearity audit (precise)

Each historical extraction step, in input `Z`:
- `TT_RECIPES` averaging `Σ c·U`: **linear**;
- `/5`: **linear**;
- `fit_even`/`fit_mlog` (ordinary linear least squares): **linear** in the
  sampled `Z` values;
- ratio `β_V/β_B`: division by a **fixed, `k`-independent** `β_B` is **linear**
  in the varied numerator up to a constant scale.

So *if* one nonetheless formed the (invalid) `Z_V + k·Z_S` and divided by a
`k`-independent `β_B`, the map `k ↦ ratio` would be **exactly linear** — testing
only that the code reads `k`, not circularity. A non-linear circular mechanism
could exist **only** if `β_B` (its fit, window, or normalization) were recomputed
as a function of `k`; the recovered pipeline does **not** do this, and no such
`k`-dependent normalization is part of the historical extraction. **Every
relevant step is linear.**

## Task 2 — pointwise consistency / obstruction

Required identity: `Z_generalized(k=phys, m_i, n) ≡ Z_recovered_Proca(m_i, n)`
per grid — i.e. `−16` at `n=16`, **not** `−3`. The only construction that
reduces to recovered Proca at a physical `k` is `Γ_Proca+(k−k_phys)Γ_scalar`,
which reduces *trivially* (added term vanishes at `k=k_phys`) while for `k≠k_phys`
being a different theory built on the **wrong** operator (§3, §5). No
construction deforms the Proca *compensator power* while reducing pointwise.
**The obstruction is demonstrated, not bypassed.**

## Task 3 — verdict: **DECOMP-NOT-REPRESENTABLE**

The recovered Proca operator and the recovered scalar operator **cannot** be
combined into a compensator-power deformation while preserving the physical-point
Proca result and avoiding double-count, because:

1. the longitudinal `m²` sector is **not** operator-equivalent to an
   independently additive `boson_loop` scalar `Δ₀ = ŝ²+m²` (ultralocal vs
   propagating; `1/m²` vs `1/(ŝ²+m²)`; different `m²ln m²` content); and
2. the metric variations contain **inseparable** transverse–longitudinal mixing
   (`⟨T|δM|L⟩ ≠ 0`), so no invariant additive determinant split exists.

**No `k`-scan is scientifically defined from the recovered code alone.** A
reinforcing secondary observation (§7): even if the operator objection were
waved away, every relevant step is linear, so the algebraic `Z_V+k·Z_S` scan
would be `LINEAR-ONLY` (tests bookkeeping, not circularity). Either way the
recovered numerical pipeline **cannot** answer the historical circularity
question by itself.

**This is not a failure.** It is a real result: the circularity question must be
reformulated as an operator/determinant-identity audit (adjudicating identity
(d) against (a)), or addressed by a separate clean-room operator
(`P2-BETAV-RECON-01`), not by a `k`-scan on the recovered code.

## Gate statuses (unchanged by this adjudication)

`P2-BETAV-CIRC-01` = `SPECIFIED`; `P2-BETAV-NUMREPRO-01` = `PROPOSED`;
`P2-C9` = `PROPOSED`; `β_V/β_B = −3.2(5)` remains quarantined/unreproduced.
This Phase-1 adjudication changes none of them.
