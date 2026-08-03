# Concept note v3.1 — **Route D: the lattice-native pipeline** (parallel to, not an addendum of, `P2-FIERZSUM-01`)

Status: HYPOTHESIS / for review. Not registered, not adopted. Revised
after Discriminator review (2026-07-26), which executed and verified the
accompanying probe. **Position (per Discriminator architecture ruling): one of TWO parallel
verification pipelines, both consuming `P2-LATTICE-ONTOLOGY-01` and
converging at SI-2.**
Consumes: `P2-LATTICE-ONTOLOGY-01` at stage D-pre — **registered
SPECIFIED** (Paper 2 `GATES.md`), specification pinned at sha256
`1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c`.
Parallel pipeline head: the latest reviewed `P2-FIERZSUM-01` concept
(v6, sha256 `a0f08d1d437771521792d5f9ad4e7353416a3d4200b7af0ab0c2578562b2cf3a`)
is approved IN PRINCIPLE for registration as SPECIFIED but is **NOT YET
REGISTERED** — no registry entry or review-record artifact exists for it
at the time of writing. Route D does not depend on that registration.
The two pipelines do not consume one another. Route D need not know about FIERZSUM and vice
versa. The continuum route (FIERZSUM → VECPOLE) is the currently PRIORITIZED
IMPLEMENTATION PATH to SI-2's re-specification — a scheduling decision,
not a statement that continuum results are more trustworthy. Route D is
its independent cross-check, and the architecture asserts no epistemic
ranking between the two pipelines.

---

## 1. The proposal

Compute the geometry response of the vacuum directly from the spectrum
of the programme's own lattice, by counting modes in a specified
background geometry — **at stages D0–D1**, without auxiliary fields,
channel decomposition, or Fierz rearrangement. (D2 may use auxiliary
fields only as a separately authorized representation whose stability
and normalization are independently demonstrated; Route D's
decoupling-free advantage therefore holds unconditionally only for
D0–D1.)

This is a **lattice-native analogue of the Sakharov mode-sum strategy**.
It becomes a computation of the programme's induced Einstein–Hilbert
coefficient only after the lattice–geometry map and the curvature
estimator are frozen and validated.

## 2. The argument for it

`ξ_ind` is UV-dominated. Routes A–C compute a UV-determined quantity
inside a framework lacking the UV data, then manage the resulting
ambiguity. This programme has a candidate UV completion; if the lattice
is the actual short-distance content, that ambiguity is in principle not
fundamental.

**The critical qualifier (§5):** this advantage is real only once the
lattice→geometry map is frozen. Before that, Route D exchanges the Fierz
ambiguity for a geometry-encoding ambiguity rather than resolving it.

## 3. Exploratory evidence (non-canonical; independently reproduced by the Discriminator)

1D tight-binding chain at half filling; geometry as a smooth local
dilation of all hoppings; `t₂` (next-nearest hopping) changes the UV
band while leaving `v_F = 2` for every `t₂` (since `sin 2k_F = 0` at
`k_F = π/2`; Fermi-sea topology also unchanged). Two responses separated
by fitting across wavelengths, quoted **normalized by `ε²`**:

| `t₂` | `a/ε²` (no-derivative) | `b/ε²` (gradient²) |
|---|---|---|
| 0.0 | −3.8×10⁻⁶ (≈0) | −2.659×10⁻² |
| 0.2 | −1.274×10⁻² | −3.256×10⁻² |
| 0.4 | −5.096×10⁻² | −5.886×10⁻² |

Controls now executed **inside the canonical script**: the locality
control is consistent with leading gradient-squared scaling —
`dE·L²/N` stable near −8.44×10⁻⁴ for L = 24–48, with a residual
wavelength-dependent (finite-size / higher-gradient) drift of ~7% over
L = 24–144, reaching −9.05×10⁻⁴ at L = 144; quadratic response
(`dE/ε²` stable to 0.15% across ε = 0.02, 0.04, 0.08); least-squares
residuals 10⁻⁵–10⁻⁴ relative.

**What it establishes, at the strength justified:**

> Two lattice Hamiltonians with the same leading half-filled linearized
> IR dispersion can have different coefficients in their response to the
> chosen smooth hopping modulation.

So: **the leading IR theory specified only by the common Fermi velocity
does not determine this coefficient; UV matching or irrelevant-operator
data are required.** (The earlier phrasing "leading-order effective
theory therefore cannot predict it" was too strong — an EFT can predict
it once the relevant Wilson coefficient is supplied by matching. The
probe shows non-universality, not the impossibility of an EFT
description.)

**`b` is NOT yet a curvature coefficient.** Calling it "curvature-like"
is an analogy only. A genuine curvature coefficient requires the map
`{t_ij} ↔ g_μν(x), e^a_μ(x), ω_μ^ab(x)`. In this 1D chain, intrinsic
Riemann curvature is trivial, `(∂g)²` is not a 1D Einstein–Hilbert
invariant, and modulating nearest- and next-nearest hoppings by the same
local factor is one microscopic prescription, not one uniquely implied
by geometry. The probe is a geometry-response prototype, not an induced
Einstein–Hilbert calculation. **Until the geometry-map validation is
complete, every reported coefficient is to be interpreted as a
geometry-response coefficient of the declared lattice prescription, not
as a unique continuum Einstein–Hilbert coefficient.**

**Corrections recorded.** (i) An earlier version reported a 250× change;
that compared two different quantities (the `∫g²` term dominates at
`t₂≠0`) — corrected to ~2.2× by separating the fits. (ii) An earlier
version claimed the locality control ran L=24…144 while the uploaded
script ran L=36…144; the control has now been restored to the canonical
script so the claim is executable.

---

## 4. Doubling is a choice of matter spectrum, not a numerical sensitivity

If the lattice is physical, choosing Wilson, staggered, or overlap
fermions **is choosing the matter content**: every light or UV-active
species contributes to the spectral trace, so doublers can multiply or
qualitatively alter `ξ_ind`. This may not be treated as discretization
noise. Accordingly, the D0 output is not a single number but

    ξ₀[ D_lat, G_geom, a, N, BC ]

— a function of the lattice Dirac operator, geometry encoding, spacing,
internal multiplicity, and boundary conditions. It becomes "the"
baseline only after those choices are declared canonical.

---

## 5. The upstream ontology decision — RESOLVED

**This section's question has been answered since v2.1.**
`P2-LATTICE-ONTOLOGY-01` is registered SPECIFIED and declares the H(4)
lattice a **physical substrate**, Euclidean-fundamental with the
Hamiltonian derived by transfer-matrix reconstruction. The consequences
that section previously listed as conditional are now binding:

- finite spacing is a physical parameter; no continuum limit is
  necessarily required;
- doublers, if present in the declared kinetic operator's spectrum, are
  candidate physical species (§4);
- Wilson / staggered / overlap are *different microscopic models*, not
  interchangeable regulators;
- the geometry coupling is part of the ontology, not of the numerics.

**What this does and does not buy Route D.** The asymmetry noted in
v2.1 stands: a Fierz decoupling parameter is representational redundancy
that should vanish in an exact treatment, whereas different geometry
encodings may describe *genuinely different microscopic theories*. The
substrate declaration therefore converts the geometry-encoding choice
from an arbitrary scheme into a physics commitment — **but the
commitment itself is not yet made.** The ontology's §1e delegation table
assigns the geometry map `{t_ij} ↔ g, e, ω`, the curvature estimator,
the microscopic measure, and the species ledger to D-pre and
`P2-LATTICE-MICROSPEC-01`, none of which is complete. Until D-pre
discharges them, Route D has a *licensed* geometry-encoding ambiguity
rather than a resolved one.

## 6. Gate chain (each stage a SEPARATE gate, not phases of one)

Per review: D-pre, D0, D1 and D2 differ in kind — a microscopic
specification gate, a free-theory numerical validation campaign, an
interacting perturbative computation, and an open-method
non-perturbative programme. Their prerequisites, failure semantics,
artifact types and review requirements differ, so folding them into one
gate would reproduce exactly the SPECIFIED/RUN/PASS confusion that
`P2-FIERZSUM-01` §0 exists to prevent — and would leave "did D0 fail?"
ambiguous between prescription failure and scientific failure.

    P2-LATTICE-ROUTE-01      architecture / admissibility specification
            |                 (registrable as SPECIFIED now)
    P2-LATTICE-MICROSPEC-01   D-pre: operator, measure, species, geometry
            |                 map, Euclidean–spectral matching, subtraction
    P2-LATTICE-XI0-01         D0: free baseline validation
            |
    P2-LATTICE-XI1-01         D1: strict O(G) interaction increment
            |
    P2-LATTICE-XINP-01        D2: optional non-perturbative extension

Authorization order: D-pre must complete before D0 is authorized; D0
must PASS before D1 is authorized; D1 carries no commitment to reach the
broken phase; D2 is registered separately and its method is NOT
pre-committed here.

### Stage content

**D-pre — microscopic specification and geometry prescription.**

*Consume, do not reopen:* pin the physical-substrate declaration of
`P2-LATTICE-ONTOLOGY-01` by hash. D-pre has NO authority to reopen or
reinterpret it.

*Freeze:* microscopic variables and measure; the canonical lattice Dirac
operator; the species ledger and doubling treatment; the
metric/vierbein/spin-connection map; the curvature-invariant estimator;
the subtraction / reference-equivalence class; finite-volume and
thermodynamic rules; boundary conditions.

*Blocking deliverable — **Euclidean–spectral response equivalence**.*
The ontology declares the Euclidean formulation fundamental and the
Hamiltonian derived, but Route D's proposal is a spectral mode sum.
These are not interchangeable without proof. D-pre must derive the
relation between the Euclidean generating functional and the
reconstructed Hamiltonian vacuum response for the declared geometry
class, including: transfer-matrix normalization; geometry-dependent
measure and Jacobian factors; finite temporal extent; temporal boundary
conditions; vacuum degeneracy; additive energy normalization; contact
terms; curvature-dependent normalization; and the restriction relating a
static geometry to a Euclidean four-geometry.

    Δ_EH = ξ_Euclidean − ξ_spectral        (machine-checkable residual)

Both sides MUST be evaluated under an IDENTICAL subtraction convention
and reference configuration; otherwise a constant offset guarantees
`Δ_EH ≠ 0` regardless of whether the equivalence actually holds.

**A spectral mode sum may be identified with the `R`-linear coefficient
of `−log Z[g]` only after this equivalence is established.** Until then,
D0's output is a *candidate spectral geometry-response coefficient*, NOT
a lattice-defined `ξ₀`. This is the same standard `P2-FIERZSUM-01`
applies to HS normalization: a normalization carrying geometry
dependence contributes to the `R` term and may not be discarded.

*Failure here leaves Route D exploratory.*

**D0 — free baseline.** Required controls: flat-spectrum reproduction; a
geometry with known continuum spectral behaviour; `ε²` scaling;
wavelength/derivative expansion; volume scaling; separation of
zero-derivative and derivative terms; discretization comparison;
doubling decomposition; and recovery of a known continuum spectral invariant
where a continuum comparison exists (a heat-kernel coefficient where the
operator is of Laplace type; the benchmark is not restricted to that
case). Output: a **candidate spectral geometry-response coefficient**
`ξ₀[D_lat, G_geom, a, N, BC]` — it becomes a lattice-defined `ξ₀`, and
thereafter the programme's `ξ(0)`, only after D-pre's Euclidean–spectral
equivalence is established AND these validations pass.

**D1 — direct `O(G)` increment, HS-free.** Compute `∂ξ/∂G |_{G=0}` from the CONNECTED CUMULANT expansion

    −log Z[g] = −log Z₀[g] + ⟨S_int⟩_{0,g,c} − ½⟨S_int²⟩_{0,g,c} + …

so that with `S_int = G·O`,

    ∂(−log Z[g])/∂G |_{G=0} = ⟨O⟩_{0,g,c}

using the complete frozen quartic operator with **all** direct and
exchange Wick contractions at canonical internal normalization and
correct symmetry factors, projecting onto no channel. D1 must
additionally verify: that disconnected vacuum factors cancel; that
geometry-dependent normalization is retained rather than dropped;
whether the flat/reference subtraction is applied before or after
`∂/∂G`; and whether the derivative and the subtraction commute.
This privileges no HS decoupling and is machine-checkable. It yields

    Δξ(G) = G·ξ₁ + O(G²)

— **the leading perturbative increment, not the full `Δξ(G)`.** D1 must
report: `ξ₁`; the perturbative validity domain; the expansion parameter;
finite-size scaling; proximity to criticality; and whether SI-2's
intended `G` lies inside that domain. In NJL-like systems the physically
relevant phase may be non-analytic at `G = 0`, so expansion around the
free sea may not reach the broken phase. D1 can still be a valuable
matching calculation even then.

Fierz dependence can re-enter at D1 only if it drops exchange
contractions, retains selected terms after rewriting, uses a
channel-selective self-energy, inserts a gap mass from one decoupling,
or resums incompletely — all avoidable at strict first order, and **these
conditions are machine-checkable against the frozen operator ledger**,
not matters for reviewer judgement.

**D2 — optional non-perturbative extension**, only if D0/D1 pass:
fermion bag, diagrammatic Monte Carlo, tensor/network methods, lattice
2PI/FRG, or a carefully justified HS formulation with demonstrated
representation stability.

---

## 7. What Route D would and would not resolve

**The principal value of Route D is not only that it avoids
auxiliary-field decoupling, but that its dominant systematic
uncertainties (geometry encoding, lattice operator, finite size) are
largely orthogonal to those of Routes A–C (Fierz family, regulator,
truncation), making agreement between the two routes substantially more
informative than repeated calculations within either framework.**

**Would:** the auxiliary-field decoupling ambiguity at D0–D1; the
cutoff-estimation problem (the lattice *is* the cutoff); the
baseline/increment separation (D0 vs D1 computed separately); and an
independent **total-response** reference for SI-2.

**Would not:** the geometry-encoding ambiguity before D-pre; the
doubling-prescription dependence; truncation dependence at D2; and — an
earlier overstatement, corrected — it does **not** automatically give
`P2-VECPOLE-01` a reference answer. A VECPOLE cross-check would require
a separate lattice current–current correlator computation
`⟨J_μ^A(x) J_ν^B(y)⟩` with spectral reconstruction or transfer-matrix
analysis, finite-volume pole extraction, and residue/overlap study.

---

## 8. The particle-hole observation (disposition)

At `t₂ = 0` the derivative-free response `a` is suppressed; breaking
particle-hole symmetry turns it on. This is mathematically real but
**must not enter the Paper-4 argument yet**: it concerns the
second-order response to one specific hopping modulation, not the
absolute vacuum energy; it is "cosmological-constant-like" only under
the proposed geometric interpretation; particle-hole symmetry commonly
enforces cancellations in bipartite half-filled systems, which alone
does not establish a vacuum-energy protection mechanism; and a physical
cosmological constant additionally requires the measure, normalization,
interactions, dimensionality, and gravitational matching. **Disposition:
record in an exploratory Paper-4 ideas note, explicitly marked
non-evidential.** No registered Paper-4 gate.

---

## 8b. Dependency table

| Dependency | Status | Required before |
|---|---|---|
| `P2-LATTICE-ONTOLOGY-01` | SPECIFIED (registered, Paper 2) | D-pre |
| `P2-LATTICE-ROUTE-01` (this architecture) | proposed | D-pre |
| `P2-LATTICE-MICROSPEC-01` (D-pre) | not created | D0 |
| Euclidean–spectral equivalence (`Δ_EH`) | not derived | D0 output may be called `ξ₀` |
| `P2-LATTICE-XI0-01` (D0) | not created | D1 |
| `P2-LATTICE-XI1-01` (D1) | not created | SI-2 cross-comparison |
| `P2-FIERZSUM-01` | reviewed, NOT registered | nothing in Route D — the pipelines are independent |

## 9. Open questions

1. (RESOLVED: physical substrate, Euclidean-fundamental; registered as
   the standalone gate `P2-LATTICE-ONTOLOGY-01`, not as a FIERZSUM
   section.)
2. At D0, is there a curved geometry with known continuum spectral
   behaviour appropriate to H(4) against which convergence can be
   validated?
3. Does the programme's intended `G` plausibly lie inside D1's
   perturbative domain, or is the physical regime non-analytic at
   `G = 0` — i.e. is D1 a matching calculation rather than an answer?
4. (RESOLVED: before. `P2-LATTICE-ONTOLOGY-01` is registered SPECIFIED;
   `P2-FIERZSUM-01` v6 is approved for registration and consumes it.)
5. (ANSWERED in §6: separate gates, not phases of one.) Remaining
   question for the reviewer: is the proposed five-gate chain and its
   authorization order correct as drawn?
