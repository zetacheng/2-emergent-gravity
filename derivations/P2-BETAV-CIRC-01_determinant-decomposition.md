# Derivation — `P2-BETAV-CIRC-01` determinant decomposition (Phase 1, no scan)

**Kind:** operator-level adjudication of the recovered lattice Proca determinant.
**No k-scan is run.** Revised 2026-07-20 to work at the `q²` level (the level at
which `Z` is extracted), to neutralize premise-laden language, and to narrow the
verdict to what the evidence supports.

Evidence (committed before interpretation, no target encoded):
`scripts/betav_decomp_check.py` (operator structure) and
`scripts/betav_decomp_q2.py` (q²-level sector decomposition) →
`results/P2-BETAV-CIRC-01/decomp/regen/`.

Conventions: `a_μ(k) = e^{ik_μ}−1`, `ŝ² = Σ_μ|a_μ|² = Σ_μ 4sin²(k_μ/2) = p̂²`.

## 1. The exact determinant `proca_loop.py` computes

Flat kernel `M_{μν}(k) = (ŝ²+m²)δ_{μν} − a_μ a_ν*`. Spectrum (verified):
`{ŝ²+m² (×3 transverse), m² (×1 longitudinal)}`, `det M(k)=m²(ŝ²+m²)³`. Loop
`Γ=+½⟨ln det M⟩`; `Z` is the axis-TT `q²` slope of `g2_axis_proca` (bubble-only:
the seagull and CC are `q`-independent and drop from the slope — verified: the
recovered `g2_axis_proca` contains no seagull term). Propagator eigenvalues:
`1/(ŝ²+m²)` transverse, `1/m²` longitudinal.

## 2. Can an invariant transverse/longitudinal split of the induced `Z` be defined? — analyzed at the `q²` level

The relevant test is **not** whether the one-graviton vertex off-block norm
vanishes as `q→0`. `Z` is the `q²` coefficient of the induced kernel; a vertex
mixing `U_TL(q)=O(q)` still yields a **finite** mixed bubble
`U_TL·U_LT=O(q²)` — a leading-order contribution to `Z`. So the adjudication is
done on the bubble, in the correct basis: projectors `P_{T,L}(k)` and
`P_{T,L}(k+q)` built **independently** from `a(k)` and `a(k+q)`, decomposing

```
Π_bubble(q) = Π_TT + Π_TL + Π_LT + Π_LL,   G1→P_X(k)G1,  G2→P_Y(k+q)G2.
```

**Measured** (`scripts/betav_decomp_q2.py`, `m=0.3`, `n∈{10,12}`, q-ranges
R1/R2/R3; sector `q²` coeffs sum to the total to `<1e-12`):

| sector | `q²` coefficient | scaling exp of `Π−Π(0)` |
|---|---|---|
| TT | `≈ +2.12e-2` (≈96.5% of total) | `≈ 1.99` (q²) |
| LL | `≈ +6.8e-4` (≈3.1%) | `≈ 1.97` |
| **TL+LT (mixed)** | **`≈ +9.0e-5` (≈0.4%)** | **`≈ 1.98` (q²)** |
| total | `≈ +2.20e-2` | `≈ 1.99` |

Stable across `n=10,12` (mixed: `8.7e-5`↔`9.1e-5`) and across q-ranges.

**Findings.**
- The one-graviton vertex mixing `U_TL` **vanishes as `q→0`** (the earlier
  vertex-norm figure was measured in the wrong, single-momentum basis and is
  withdrawn).
- **But** the mixed bubble contributes at `O(q²)` (exponent `≈1.98`): the mixed
  `q²` coefficient is **nonzero** (`≈+9e-5`) and basis/grid-stable.
- It is, however, **small** — `≈0.4%` of the total `Z`. An *approximate*
  transverse/longitudinal split holds well (TT+LL ≈ 99.6%); an **exact
  invariant additive split fails only at the ≈0.4% (`q²`) level**.

So a separate, exactly-invariant longitudinal `Z` **cannot** be assigned (the
mixed cross-term is present at leading order), but the inseparability is **mild
and quantified**, not gross. We do not infer a separately additive scalar
contribution from the `1/m²` propagator term alone.

## 3. Is the external scalar loop the same operator as the Proca longitudinal? — NO (operator level)

- **External scalar** (`boson_loop`): kernel `Δ₀ = ŝ²+m²` (propagating),
  propagator `1/(ŝ²+m²)`.
- **Proca longitudinal spectral factor**: `m²` (ultralocal, verified invariant
  over `p̂²` to `3e-16`), propagator `1/m²`.

Their **flat spectral factors have different momentum dependence** (`m²`
ultralocal vs `ŝ²+m²` propagating). Therefore **equality of their induced
`m²ln m²` contributions cannot be assumed** and would require a full
metric-variation identity, which the recovered code does not provide. (We do
**not** infer the induced-`Z` log content from the flat vacuum `ln det`: the
extracted quantity is a second metric variation, and §2 shows the flat
factorization does not lift cleanly under `δh`.)

**Neutral statement:** the recovered external scalar loop is **not identical**
to the flat longitudinal eigenfactor and **cannot be substituted for it without
an additional operator identity.**

## 4. Determinant identities to adjudicate

- **(a)** complete curved `det M_Proca` — what the code computes;
- **(b)** flat spectral `det M = m²(ŝ²+m²)³` — `h=0` only; not a curved
  factorization (§2 mixing);
- **(c)** external scalar `det Δ₀ = ŝ²+m²` — a *different* operator (§3);
- **(d)** continuum gauge-fixed / Stueckelberg determinant quotient
  `det^{−1/2}(Δ^{(1)}+m²)det^{+1/2}(Δ^{(0)}+m²)` — where the analytic `−3` lives.
  **No such gauge-fixed / Stueckelberg determinant-quotient identity is
  implemented or demonstrated by the recovered code; the equivalence to (a)
  remains unestablished (neither proven nor refuted).**

The recovered `k=1` corresponds to **(a)** (flat check (b)); the analytic `−3`
to **(d)**. That they differ is consistent with the recovered numerics giving
`−16`/`−61` (grid/artifact limited), not `−3`.

## 5. Generalized-`k` deformation — none available from the recovered code as-is

Neutral operator language (not "compensator sector"):

- The longitudinal spectral factor of the complete non-minimal Proca operator is
  the ultralocal `m²` eigenfactor, sitting **inside the same 4×4 kernel** as the
  transverse block; on a curved background the transverse and longitudinal
  sectors are not exactly separable determinants (§2, mild mixed `q²` term).
- Replacing/adding the recovered external scalar `det Δ₀` does not reproduce a
  change of the longitudinal spectral factor, because `Δ₀ ≠ m²` (§3). The
  additive `Γ_Proca + (k−k_phys)Γ_scalar[Δ₀]` reduces to `Γ_Proca` only
  trivially at `k=k_phys` and is a different multi-species theory for
  `k≠k_phys` — built on the wrong operator.

Whether an *alternative* clean-room lattice Stueckelberg / gauge-fixed
construction could define such a deformation is **not excluded** (it is (d),
unestablished). What is established is that **no valid compensator-power
deformation is available from the recovered implementation as-is.**

## 6. Metric-variation decomposition at the `q²` level

Established (§2): the flat `T/L` split does **not** lift to an exactly invariant
additive split of the induced `Z`; there is a nonzero but small (`≈0.4%`) mixed
`q²` cross-term `Π_TL+LT`. The seagull is `q`-independent (structural — `δ²M`
and the single-propagator tadpole carry no external `q`) and contributes to
`Π(0)` only, **not** to the `q²` coefficient (verified, not assumed): the
recovered slope extractor is bubble-only.

## 7. Non-linearity audit (precise)

`TT_RECIPES` averaging (linear), `/5` (linear), `fit_even`/`fit_mlog` = ordinary
linear least squares (linear), ratio by a **fixed, `k`-independent** `β_B`
(linear up to constant scale). A non-linear circular mechanism could live only
in a `k`-dependent `β_B`/window/normalization, which the recovered pipeline does
not have. **Every relevant step is linear** ⟹ the withdrawn additive
`Z_V+k·Z_S` scan would be `LINEAR-ONLY` (tests bookkeeping, not circularity).

## Task 2 — pointwise consistency / obstruction

Required: `Z_generalized(k=phys,m_i,n) ≡ Z_recovered_Proca(m_i,n)` per grid
(i.e. the recovered `−16` at `n=16`, **not** `−3`). The only additive
construction reducing to recovered Proca at a physical `k` does so trivially
(added term vanishes) and is a different theory on the wrong operator for
`k≠k_phys` (§3, §5). No construction from the recovered code deforms the
longitudinal spectral factor while reducing pointwise. Obstruction demonstrated.

## Task 3 — verdict: **DECOMP-UNAVAILABLE-AS-RECOVERED**

No valid compensator-power deformation is available from the recovered
implementation as-is; the `boson_loop` scalar is not the flat longitudinal
eigenfactor and cannot be substituted without an extra identity; the original
additive k-scan is invalid (and would in any case be `LINEAR-ONLY`); **but** an
alternative clean-room lattice Stueckelberg / gauge-fixed construction is **not
excluded**.

**Supports that actually hold after the `q²` revision:**
- **(a)** the original additive `Z_V+k·Z_S` k-scan design is invalid — and would
  in any case be `LINEAR-ONLY` (§7). *Holds, solid.*
- **(b)** the recovered external `boson_loop` scalar (`Δ₀=ŝ²+m²`, propagating)
  is **not** the flat Proca longitudinal eigenfactor (`m²`, ultralocal) and
  cannot be substituted without an additional operator identity. *Holds, solid.*
- **(c)** the induced `Z` does not admit an **exactly invariant** transverse/
  longitudinal additive split: the mixed `q²` contribution is nonzero
  (`≈+9e-5`) and basis/grid-stable. *Holds, but mild — the effect is only
  `≈0.4%` of `Z`; an approximate split holds at the 99.6% level.*

**Dropped/qualified:** the earlier unqualified "no operator-defined deformation
can exist" and the gross "inseparable mixing" (0.17) claim — the vertex mixing
in fact vanishes as `q→0`; the surviving inseparability is the small `O(q²)`
mixed bubble.

The practical next step is unchanged: **do not run the original k-scan**; the
circularity question is addressed by an operator/determinant-identity audit
((a) vs (d)) or a clean-room `P2-BETAV-RECON-01`, not by a k-scan on the
recovered code. This is a statement about the *design*, not a CIRC verdict.

## Gate statuses (unchanged by this adjudication)

`P2-BETAV-CIRC-01` = `SPECIFIED` (the CIRC gate has not passed or failed);
`P2-BETAV-NUMREPRO-01` = `PROPOSED`; `P2-C9` = `PROPOSED`;
`β_V/β_B = −3.2(5)` remains quarantined/unreproduced.
