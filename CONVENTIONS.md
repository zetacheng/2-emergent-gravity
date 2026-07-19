# Convention Registry

No calculation may begin until every relevant convention below is filled,
reviewed, and locked for the applicable gate. **These conventions were fixed
before any computation in gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, and
`P2-BETAV-01`, and were not adjusted afterwards to reproduce a paper value.**

## Locked conventions for the independent-verification sweep

| Convention | Value |
|---|---|
| Metric signature | Euclidean, `(+,+,+,+)`, `d = 4`. Curvature sign: `R > 0` on a sphere (`R = +d(d-1)/a²` for a `d`-sphere of radius `a`). |
| Wick rotation | All loop integrals performed in Euclidean signature. `∫ d⁴p_E` with `p²≡p_E² ≥ 0`. |
| Fourier transform | `f(x) = ∫ d⁴p/(2π)⁴ e^{ipx} f̃(p)`; loop measure `∫ d⁴p/(2π)⁴`. |
| Heat-kernel operator | `Δ = −∇² + E` (Laplace-type). `E` is the endomorphism (potential/bundle) term; **sign convention: `E` enters with a `+` so that a scalar curvature coupling `ξR` appears inside `E` as `E ⊃ +ξR`.** The mass `m²` is separated out explicitly (`Δ + m²`) and is **not** counted inside `E` for the `a_k`. |
| Heat-kernel expansion | `Tr e^{−τΔ} = (4πτ)^{−d/2} ∫ d^dx √g Σ_{k≥0} a_k(x) τ^k`, `d=4`. Indexing: `a_0 = tr 𝟙`, and `a_1 = tr[(1/6)R·𝟙 − E]` (the `R`-linear Seeley–DeWitt coefficient). This is the "`a_1`/`b_2`" in the τ-power indexing; some references call it `b_4`. |
| Curvature coupling of scalar | Non-minimal coupling term `½ ξ R φ²` in the action ⟹ `E = ξ R` for the scalar; minimal coupling is `ξ = 0`. The conformal value in `d=4` is `ξ = 1/6`. |
| Dirac operator squaring | `−(γ·∇)² = −∇² + (1/4)R` (Lichnerowicz), so for a Dirac fermion `E = (1/4)R·𝟙₄` on the 4-component spinor bundle; the fermion loop carries an overall statistics sign `−1` relative to a real boson. |
| Massive-vector (Proca) structure | `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. This determinant structure is taken as an input from the paper; the coefficient it implies is what we compute. |
| Definition of `Z(m²)` | The induced axis/transverse-traceless (TT) graviton kinetic coefficient, i.e. the coefficient of the induced Einstein–Hilbert term `∫√g R` normalized **per unit `4N`** of fermionic degrees of freedom (`4` spinor components × `N` flavors). Concretely `Z ≡ 1/(16πG_ind)` in the TT channel, expressed per `4N`. The `m²ln m²` piece defines the species coefficient: `Z ⊃ β_s · m² ln m²`. |
| Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`. |
| Definition of `L` | `L ≡ ln(Λ²/m²)`. The mass `m` is measured **in units of the cutoff `Λ`** (i.e. `Λ ≡ 1` unless a gate states otherwise), so `L = −ln m²` in those units. `ln m²` and `L` differ only by sign and the `ln Λ²` reference. |
| Regularization | **Sharp Euclidean 4-ball `|p| < Λ`** for all continuum momentum integrals, unless a gate explicitly states another regulator. |
| Lattice regularization | Hypercubic lattice, spacing `a` (`a ≡ 1` in lattice units), Brillouin zone `p_μ ∈ (−π, π]`. Free-field lattice momenta: `p̂² = Σ_μ 4 sin²(p_μ/2)` (naive/scalar), `s̄_μ = sin p_μ`, Wilson term `W(p) = r Σ_μ (1 − cos p_μ)` with Wilson parameter `r = 1`. |
| Sign of the action | Euclidean action `S_E ≥ 0`; `Z = ∫ e^{−S_E}`, effective action `W = −ln Z`. Boson: `W = +½ Tr ln(Δ+m²)`. Dirac fermion: `W = −Tr ln(iγ·D − m) = −½ Tr ln(−(γD)² + m²)`. |
| Gamma matrices | Euclidean, Hermitian `γ_μ = γ_μ^†`, `{γ_μ,γ_ν} = 2δ_{μν}`, `tr 𝟙₄ = 4`. |
| Gamma5 | `γ_5 = γ_1γ_2γ_3γ_4`, Hermitian, `γ_5² = 𝟙`, `{γ_5,γ_μ}=0`. |
| Generator normalization | Not used in gates `P2-*` (single-species loops); `tr(T^aT^b)=½δ^{ab}` if flavor generators are ever needed. |
| Flavor basis | `N` degenerate flavors; the induced coefficient is reported per unit `4N`. |
| Field dimensions | Canonical: scalar `[φ]=1`, Dirac `[ψ]=3/2` in `d=4`. |
| Cutoff and lattice units | `Λ ≡ 1` (continuum), `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |
| Definition of attractive and repulsive channels | Scalar (`ψ̄ψ`) condensate channel is the attractive channel driving the gap; the four-fermion coupling `G > 0` is attractive there. |
| Normalization of Green functions | Euclidean Wilson propagator `S(p) = 1/(iγ·s̄(p) + W(p) + m)`; scalar `1/(p̂²+m²)`. |
| Gap-equation integral `I_0` | `I_0` is defined by the linearization of the mean-field gap equation about zero condensate, `1 = 2 G_c I_0`; the precise integrand and the derivation of the relation `G_c = 1/(2I_0)` are given in the `P2-GAP-01` derivation note and script. |
| Statistical-error convention | Numerical uncertainties are reported as spreads over discretization / fit-window / ansatz variations (systematic), not as formal fit errors alone. Convergence is demonstrated by grid refinement and half-shifted (offset) grid cross-checks. |

## Change control

Any change to a locked convention after a gate has been committed must be
recorded as a new `DECISION_LOG.md` entry that supersedes the prior one, and
must trigger re-examination of every gate that consumed it. Conventions are
never changed silently, and never changed in order to reach a target number.
