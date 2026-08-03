# Concept note v2.2 (PROPOSED, not registered) — `P2-LATTICE-ONTOLOGY-01`: the H(4) lattice is declared physical substrate, with consequences

Status: HYPOTHESIS / concept discussion for Discriminator review.
Nothing here is registered or authorized. This is a **specification
gate**: its deliverable is a declaration plus its enumerated
consequences, not a computation.

Position in the chain: upstream of `P2-FIERZSUM-01` (which must state
its renormalization prescription against this declaration), of Route D
(whose D-pre stage consumes it), and ultimately of SI-2. Requested by
the Discriminator's Route-D review ("this yes/no ontology decision
cannot remain implicit").

---

## 0. Foundational specification table (what is fundamental, what is emergent)

Every downstream gate repeatedly asks "is this microscopic or
emergent?"; this table answers once.

| Fundamental (microscopic) | Emergent (collective) |
|---|---|
| the H(4) lattice and its spacing | the metric and curvature |
| the fermionic variables, conserved charges and filling convention | gravity (as vacuum elasticity) |
| the Euclidean lattice action and microscopic measure (canonical quartic coupling `G` as encoded there) | the transfer-matrix Hamiltonian and Hilbert-space description |
| — | gauge bosons and composite particles |
| boundary conditions, internal multiplicity `N` | Lorentz symmetry, the light cone |
| the lattice Dirac operator (once declared) | continuum spacetime itself |

## 1. The question and the proposed answer

**Is the H(4) lattice a physical substrate, a regulator, or an
effective discretization?**

**Proposed answer: physical substrate.** The lattice fermion condensate
is the microscopic content of the theory. Spacetime, its geometry, and
gravity are collective properties of this medium; particles are its
quasiparticles and topological defects ("knots"); the Dirac sea is not
a heuristic to be normal-ordered away but the physical ground state
whose structure carries the physics.

This is not a new choice being made here. The programme's existing
commitments — induced gravity from the condensate's elasticity, matter
as knots in the medium, dark energy from the condensate's vacuum
structure — are only coherent under the substrate reading. In the
regulator reading, "the elasticity of the sea" has no referent and SI-2
has no object. This note formalizes a commitment the theory has already
made implicitly, and prices it.

The stance places the programme in the analog-gravity / emergent
spacetime lineage (Volovik's condensed-matter gravity programme being
one well-known example): **spacetime is a material, particles are
its quasiparticles, gravity is its elasticity.** The Dirac sea here is
the condensed-matter version — real, structured, response-bearing, as a
filled valence band is — not the textbook computational image that
normal ordering deletes.

---

## 1b. Dynamical formulation: Euclidean-fundamental, Hamiltonian derived

**Declaration.** The fundamental formulation is EUCLIDEAN: the H(4)
lattice is a four-dimensional configuration-and-weight statistical
system with all four axes equivalent. There is no fundamental clock.
The Hamiltonian description is DERIVED: slicing along any axis defines
a transfer matrix `T`, and where `T = e^{−aH}` with self-adjoint `H`,
canonical quantum evolution, the Hilbert space, and the ground state
are reconstructed (Osterwalder–Schrader). Accordingly:

- **Reflection positivity is a frozen obligation**, not an assumption:
  the declared H(4) action must be reflection-positive, or no quantum
  theory corresponds to it. **Three propositions are distinct and may
  not be conflated:** (i) positivity of a particular finite transfer
  matrix (sufficient, in that finite model, to define
  `H = −a⁻¹ log T`); (ii) Osterwalder–Schrader reflection positivity of
  the Euclidean measure/action (the general reconstruction condition —
  for the H(4) fermion action with Grassmann measure, spin structure,
  interactions and determinant signs, this must be proved per declared
  kinetic operator, and cannot be transplanted from a bosonic Ising
  example); (iii) axis equivalence (the three-level deliverable below).
  The obligation has teeth — it constrains the kinetic-operator choice
  (§4) directly (e.g. standard Wilson formulations admit reflection-positive
  constructions under the relevant conditions; not every discretization
  does).
- **"Which axis is time" is not a selection problem — but the
  equivalence deliverable has THREE levels:** (1) equality of the
  Euclidean partition function under permitted axis relabellings;
  (2) reconstruction of a positive transfer operator for every
  candidate slicing; (3) equivalence, after the declared scale and
  orientation identifications, of the resulting infrared observable
  algebras and spectra. The exploratory Ising probe demonstrates
  level 1 exactly and a finite-dimensional example of
  transfer-Hamiltonian construction; it does NOT establish levels 2–3
  for the H(4) fermion theory. H(4) isotropy (equal couplings on all
  four axes) joins the freeze list.
- **The arrow of time is a separate, lower obligation**: once the
  derived evolution exists, entropy-increase unidirectionality is a
  statistical result (Hilbert-sixth-problem-type derivations, e.g.
  Deng–Hani–Ma, operate at this level — deriving irreversibility from
  reversible dynamics). Such results support the ARROW level only; they
  presuppose evolution and do not derive the time DIMENSION. The two
  levels may not be conflated.
- **Honesty note on the probes:** the 1D geometry-response script is
  Hamiltonian-native and does not bear on reconstruction. The Euclidean
  reconstruction probe (`EXPLORATORY_euclidean_reconstruction.py`, 2D
  Ising) demonstrates: transfer-matrix positivity in that finite
  bosonic model; exact partition-function axis equality; and finite-size spectral behaviour consistent with the expected c=1/2
  Ising critical theory, including `m₁L → 1/2` and `m₂/m₁ → 8`. It does NOT prove OS
  reflection positivity for the H(4) fermion action, unitary
  equivalence of slicings, signature emergence, or interacting-vacuum
  reconstruction.

**A structural dividend of the Euclidean choice (a candidate mechanism
for Bill 2):** the H(4) symmetry group is the finite hypercubic group,
not continuous O(4). For a local, translation-invariant, axis-isotropic
lattice action whose relevant and marginal couplings have been tuned to
an O(4)-symmetric critical surface, the leading hypercubic-invariant
but O(4)-violating derivative corrections commonly enter at higher
derivative order, giving corrections of order `(E·a)²`. **This is a
mechanism to be demonstrated for the declared fermion operator — H(4)
symmetry alone does not guarantee** proximity to the right critical
surface, exclusion of marginal anisotropies, a common limiting velocity
for all quasiparticle species, or the absence of interaction-generated
low-dimension Lorentz-breaking structures. Bill 2 thereby acquires a
candidate mechanism and a concrete scaling target, contingent on the
isotropy freeze above.

## 1c. Static or dynamical lattice

**Dynamical-substrate hypothesis, not yet microscopically specified.**
The present programme freezes an H(4) combinatorial background and
treats its geometry-coupling variables as external. The full theory is
hypothesized to promote a declared subset of substrate variables —
still to be identified (candidates: couplings `t_ij`, link/vierbein
variables, defect degrees of freedom; NOT necessarily connectivity or
spacing) — to dynamical variables. Until those variables and their
measure are specified, "dynamical lattice" is an ontology OBLIGATION,
not a completed microscopic declaration. All present gates (Route D,
Phase B, SI-2) operate in the static-background approximation; a
validity criterion (the back-reaction scale beyond which static
results cannot be trusted) is owed before any gate verdict is promoted
to a statement about the full dynamical theory.

## 1d. Vacuum selection rule

**Frozen operational rule.** At finite volume, the reference-vacuum
sector is the maximal-eigenvalue EIGENSPACE of the reconstructed
transfer matrix within the declared neutral sector. Where that
eigenvalue is non-degenerate, this selects a unique reference vacuum.
Where it is degenerate, a separately frozen sector-selection or
symmetry-breaking prescription is required before response observables
are defined. The neutral sector is defined by the conserved
microscopic charge, with charge conjugation mapping `Q → −Q`.

**Untested physical hypothesis (separate obligations, not claims).**
Where the microscopic occupation convention identifies `Q = 0` with
half filling, the neutral-sector rule corresponds to half filling.
Charge conjugation alone does NOT establish uniqueness, does not
exclude spontaneous C-breaking, and does not prove the selected vacuum
is symmetry-determined without spectral comparison — those are separate
obligations. The programme will test whether C symmetry, positivity,
and the declared interaction together make the neutral vacuum unique
and protect the derivative-free response (the exploratory probe's
particle-hole suppression is the 1D shadow of this conjecture, not its
proof). If proved, the principle selecting the vacuum and the one
protecting the cosmological term (Bill 1) would be unified — recorded
as HYPOTHESIS.

## 1e. Microscopic specification obligations (frozen here vs delegated)

The declaration does not itself complete the microscopic specification;
Two candidate realizations may be treated as the same declared
microscopic theory only if they agree on every frozen and delegated
item in this specification, together with any additional data later
shown to affect observables. No known item on this list may remain
implicit.

| Ingredient | Status |
|---|---|
| Formulation (Euclidean-fundamental; Hamiltonian derived) | FROZEN HERE (§1b) |
| Reflection positivity of the action | FROZEN HERE as obligation (§1b) |
| Isotropy of the four axes | FROZEN HERE (§1b) |
| Lattice: ontologically dynamical, operationally static | FROZEN HERE (§1c) |
| Vacuum selection rule (C-sector, dominant transfer eigenvector) | FROZEN HERE (§1d) |
| Microscopic Euclidean variables, state space and measure | DELEGATED: a subordinate `P2-LATTICE-MICROSPEC-01` artifact (or Route D D-pre acting as such) — NOT FIERZSUM |
| Continuum effective functional measure and renormalized prescription | DELEGATED: `P2-FIERZSUM-01` (must be compatible with, never determinative of, the microscopic theory) |
| Consistency/matching map between the two | DELEGATED: Phase-B matching deliverable |
| Which fields are summed over vs held fixed | DELEGATED: the MICROSPEC artifact |
| Canonical kinetic operator and species accounting | DELEGATED: D-pre (§4 obligation binds it) |
| Geometry map `{t_ij} ↔ g, e, ω` and curvature estimator | DELEGATED: D-pre |
| Reference equivalence class and matching conditions | DELEGATED: FIERZSUM §4.2 / D-pre (per §2 below) |
| Admissible thermodynamic / infinite-volume limits | DELEGATED: the gate that first needs them, with preregistration |

## 2. The arithmetic consequence: no regulator-removal UV divergence arises

Under the substrate reading, the declared finite lattice supplies a
**physical ultraviolet completion at fixed spacing and volume**: the
mode count is finite, no regulator-removal limit is required, no
counterterm tower is introduced. This is the defensible claim — NOT
"nothing diverges": extensive quantities grow in the thermodynamic
limit, response functions can turn singular at phase boundaries, and
operators can have zero modes. Infrared, thermodynamic and phase-limit
questions are distinct, listed obligations, not consequences of
finiteness. The exploratory probe
(`EXPLORATORY_lattice_geometry_response.py`) exhibits this concretely:
720 sites, 720 modes, every one summed, no regulator anywhere.

Contrast the regulator reading: a continuum theory has infinitely many
modes, the zero-point sum diverges, a cutoff `Λ` must be introduced by
hand, the answer depends on `Λ` and on the scheme, and the
renormalization apparatus exists to manage that arbitrariness.

**The UV problem is not solved by the substrate reading; it never
arises in it.** **But finite ≠ unique.** The absence of UV
divergences does not eliminate ambiguity; it transfers the burden from
renormalization choices to microscopic specification. The ontology gate
therefore freezes the microscopic ingredients that define the finite
theory — the answer is a functional
`ξ = ξ[D_lat, e^a_μ, geometry map, N, BC, …]` until every argument is
declared canonical. What must be frozen is not "finiteness" but
**microscopic specification completeness**. In one sentence: *the
absence of UV divergences does not imply uniqueness; it transfers the
burden from renormalization choices to microscopic specification, and
this gate freezes that specification.* This also retrodicts the programme's own betaV
experience: computing `β_V` in an effective continuum framework
produced an eps-grid-dominated INCONCLUSIVE — **consistent with** (not
yet explained by) the reading that a substrate-determined question was
being asked inside a regulator framework. Only an actual Route-D
computation reproducing or resolving the betaV-class quantity would
promote this from interpretation to retrodiction.

**Precision 1 — finite ≠ subtraction-free.** The observable is the
*response* of the sea to geometry (`dE`), not its total energy; a
baseline subtraction (relative to the flat/reference configuration)
remains. The difference from the regulator reading is its status:
in a continuum regulator treatment, subtraction generally requires a
regulator and renormalization prescription, and residual scheme
dependence must be tested rather than assumed absent; here, the required structure is stronger than
"both configurations are finite": the theory must freeze a **reference
EQUIVALENCE CLASS** — a relational prescription ("compare
configurations satisfying these matching conditions": boundary
conditions and volume matching; filling/particle number; phase and
topological sector; lattice orientation and geometry map; which
microscopic quantities are held fixed; the comparison path; the
additive energy convention) — together with an **invariance
requirement**: all admissible representatives of the class must yield
the same response. If different admissible references yield different
responses, that is prescription-dependence with the same governance
consequence as scheme-dependence: the result is not uniquely
predicted.
**Verifiable form:** `ΔE[r₁] = ΔE[r₂]` for all admissible
representatives `r₁, r₂`, within a preregistered tolerance — a
checkable deliverable of whichever gate first computes a response. The renormalization
deliverable that the Discriminator required of `P2-FIERZSUM-01` does
not disappear under this declaration — it **collapses into a finite,
explicit subtraction-and-matching rule**, which FIERZSUM must still
freeze.

**Precision 2 — scale matching survives.** Expressing the finite
lattice answer in continuum units (identifying `a`, the spacing, with a
physical length; matching lattice couplings to low-energy observables)
is still a frozen prescription. Substrate removes the divergence, not
the bookkeeping.

---

## 3. The three bills (what the declaration costs)

Declaring the sea physical signs three known liabilities. They are not
reasons to avoid the declaration — they are its price, and each maps to
an existing or required programme line.

**Bill 1 — the cosmological constant, in its sharpest form.** A
regulator-based nongravitational treatment may remove or redefine a
common vacuum-energy baseline through normal ordering or
renormalization conventions; once gravity is dynamical, whether and
how that absolute contribution sources geometry is a separate physical
question. The substrate reading may not delete that contribution by
convention. Naive estimates of a Planck-density medium overshoot the observed dark-energy density by an enormous factor,
conventionally quoted as up to ~10¹²⁰ when a Planck-scale vacuum
density is compared with it (a heuristic magnitude, not a
model-computed number). Any substrate programme must exhibit
a suppression mechanism (Volovik's: the pressure of a self-sustained
equilibrium medium cancels its energy density — with its own
premises). The probe's incidental finding — the derivative-free
response suppressed by particle-hole symmetry and switched on by its
breaking — is a 1D toy of exactly this problem and is recorded
(non-evidentially) in the Paper-4 ideas line. **Owner: Paper 4.** **Governance separation (frozen):** the response
subtraction of §2 authorizes removing the common baseline from RESPONSE
observables only; it does not authorize deleting the substrate energy
from the cosmological SOURCE. Conversely, whether the absolute sea
energy gravitates at all is not presupposed — it awaits the
geometry/source map. Response energy and source energy are separate
ledger entries until that map is frozen.

**Bill 2 — Lorentz symmetry becomes emergent.** In a medium, the "speed
of light" is a collective-mode velocity; at energies approaching the
substrate scale, Lorentz invariance generically deforms (as sound
ceases to be universal near the lattice scale of a crystal).
Observational LIV constraints are among the most stringent in physics.
The backlog item "BS/interacting kernel for `G_V` and LIV" is hereby
**upgraded from optional to mandatory** under this declaration.
**Owner: the LIV gate line (Paper 1/3 interface).**

**Bill 3 — preferred microscopic structure exists (frame: conditional).**
Once the transfer-matrix reconstruction is established, the
reconstructed sea defines a preferred microscopic rest frame. Before
that reconstruction, the binding conclusion is only that the substrate
possesses preferred microscopic structure and orientations; the bill is
owed in its full (rest-frame) form only after §1b's reconstruction is
in place.  The
standard escape (Volovik-style) is that all detectors are themselves
quasiparticles of the sea and can only measure its intrinsic geometry,
so the frame is unobservable at low energy — but this is a theorem to
be proved in this model, not an assumption. **Owner: a future
intrinsic-geometry gate (not yet registered; listed as a known open
obligation).**

**Two further ontology-level obligations (completing the list):**

**Obligation 4 — microscopic consistency, locality and causal
reconstruction.** The declared measure, state space, and derived
evolution must define a consistent quantum (or probabilistic)
interpretation. Reflection positivity (§1b) is the core checkable
condition but NOT the whole: a positive Hilbert space, a local
observable algebra, a stable causal cone, cluster decomposition, and an
acceptable analytic continuation are separate requirements of this
obligation.

**Obligation 5 — emergent redundancy and universality.** If metric and
gauge structures are emergent, the programme must distinguish genuine
low-energy redundancies from additional physical lattice degrees of
freedom, and state what makes the infrared description insensitive to
microscopic orientation and locality data (the hypercubic→O(4)
mechanism of §1b is the template). This obligation also owns the
diffeomorphism question: how continuum diffeomorphism redundancy arises
from microscopic lattice variables, and which lattice observables
belong to the same emergent gauge orbit.

---

## 4. Doubling becomes a physics choice

Under the regulator reading, fermion doublers are artifacts to be
removed en route to the continuum. Under the substrate reading there is
no continuum to escape to: **doublers, IF present in the spectrum of the declared kinetic operator, are candidate physical species**,
and the choice among naive / Wilson / staggered / overlap kinetic terms
is a choice of the theory's matter content, with direct effect on every
spectral-trace quantity (including `ξ_ind`).

Consequently the declaration imposes on Route D's D-pre stage (and on
any future lattice computation) the obligation to either:
(a) specify the canonical H(4) kinetic term and count its species as
physics; or (b) demonstrate that H(4)'s structure dynamically removes
or gaps the unwanted species. Option (b) is a computation; until it is
done, (a) is the honest default and the species multiplicity enters
`N`-accounting explicitly.
**Sequencing (per review):** D-pre may be authorized with this
obligation open, but D0 may NOT be authorized until the kinetic
operator and its species ledger are frozen — a blocking deliverable of
D-pre, not a separate gate.

---

## 5. What changes downstream (binding consequences if registered)

1. **`P2-FIERZSUM-01` §4.2** (renormalization prescription): must be
   written as a finite subtraction-and-matching rule per §2, not as a
   continuum scheme choice.
2. **Route D, D-pre**: the geometry-encoding choice changes character —
   from "scheme ambiguity" to "physics commitment the model must make
   anyway". D-pre must still freeze the map `{t_ij} ↔ g, e, ω`; this
   declaration makes that map part of the theory's definition rather
   than of its numerics.
3. **Doubling**: §4's obligation binds D-pre and any lattice gate.
4. **LIV line**: upgraded to mandatory (Bill 2).
5. **Paper 4**: Bill 1 formally acknowledged as the programme's largest
   open liability; the symmetry-suppression toy recorded as
   non-evidential.
6. **SI-2**: no change to its status (blocked), but its eventual
   re-specification inherits the finite-subtraction framing.
7. **Architecture (dual pipeline):** this declaration is consumed by
   TWO independent verification chains, not one:

                        P2-LATTICE-ONTOLOGY-01
                     (foundational specification)
                                │
              ┌─────────────────┴─────────────────┐
       Continuum effective route         Lattice-native route
              │                                   │
        P2-FIERZSUM-01                    Route D (D-pre → D0 → D1 → D2)
              │                                   │
        P2-VECPOLE-01                             │
              └───────────────┬───────────────────┘
                              ▼
                    Phase-B metric freeze
                              ▼
                       SI-2 (death gate)

   FIERZSUM need not know about D; D need not know about FIERZSUM; both
   consume only this declaration, and SI-2 compares them. Their dominant
   systematics are largely orthogonal (Fierz/regulator/truncation vs
   geometry-encoding/lattice-operator/finite-size), so convergence of
   the two chains on the sign, magnitude, or trend of `ξ_ind` would be
   substantially more informative than repetition within either chain.

---

## 6. Falsifiability of the declaration itself

A specification gate should still be falsifiable. This declaration is
committed to consequences that can fail:

- If no H(4) kinetic term yields an acceptable species content (§4b
  fails and §4a yields phenomenologically excluded multiplicities), the
  substrate reading of *this* lattice is in trouble.
- If the LIV line (Bill 2) produces deformations excluded by
  observation for every admissible parameter choice, the substrate
  scale or structure is wrong.
- If Bill 1 admits no suppression mechanism within the model's
  symmetries, the declaration survives formally but the model fails
  phenomenologically.

**Three-level distinction (frozen):** a failure can kill
(i) a particular microscopic REALIZATION (one kinetic operator, one
parameter point); (ii) the declared H(4) MODEL CLASS — but only if the
admissible realization class was closed IN ADVANCE; (iii) the general
proposition that SOME physical discrete substrate exists — which §6's
routes do not reach and this declaration does not claim to make
falsifiable. **Anti-escape rule:** the admissible kinetic-operator
class, parameter domains, and suppression-mechanism class must be
frozen BEFORE the corresponding failure route is run; after a failure,
the class may not be widened to rescue the declaration — widening
constitutes a NEW declaration with a new version number and its own
review. Subject to that rule, the declaration routes into genuinely
falsifiable lines at levels (i) and (ii).

---

## 6b. Consumers

This declaration is consumed by:
- `P2-FIERZSUM-01` (continuum pipeline head; renormalization deliverable
  written against §2)
- Route D, stage D-pre (lattice pipeline head; geometry map and species
  accounting per §4)
- Phase B (metric freeze inherits the finite-subtraction framing)
- SI-2 (eventual re-specification; compares the two pipelines)

## 7. Questions for the Discriminator

1. (RESOLVED per joint review: the binding declaration is PHYSICAL
   SUBSTRATE. The third reading — "effective discretization of an
   unknown deeper theory" — is retained as a recorded ALTERNATIVE
   HYPOTHESIS, explicitly non-operative: **it is not consumed by any
   downstream gate**, and no downstream consequence is conditional on
   it. It is preserved rather than deleted so that a future failure of
   the substrate reading has a documented successor hypothesis instead
   of a vacuum.)
2. Is the proposed reference-equivalence-class and invariance
   criterion (§2, verifiable form `ΔE[r₁] = ΔE[r₂]`) sufficient as the
   governance replacement for continuum scheme independence?
3. Is the doubling default (§4a: count species as physics until §4b is
   computed) the right conservative order, or should §4b be a
   registered gate before any Route-D authorization?
4. Do Obligations 4–5 sufficiently price locality/causal
   reconstruction, diffeomorphism redundancy and gauge emergence, or
   should any be promoted to a separate bill with its own owner?
5. (RESOLVED per review: register and review as `P2-LATTICE-ONTOLOGY-01`
   first — versionable, auditable content; after approval, ratify its
   approved-version SUMMARY to `0-programme`, since it binds Papers 1–4
   but placing the full document in the programme constitution would
   make amendment too costly.)
