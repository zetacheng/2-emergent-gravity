# Concept note v6 (APPROVED FOR REGISTRATION AS SPECIFIED, not registered) — `P2-FIERZSUM-01`: what object does SI-2 compute, and is it representation-stable and free of double counting?

Status: HYPOTHESIS / concept discussion, revised after Discriminator
review (2026-07-26). Nothing here is registered or authorized.
Upstream of: `P2-VECPOLE-01` (concept, pending this gate) and
`P2-MULTIPHASE-GRAV-01` (SI-2, registered, honest prior FAIL).
Phase B may prepare inventory-independent infrastructure in parallel;
it may not finalize.
Architecture (Discriminator ruling 2026-07-26): this gate heads the
CONTINUUM pipeline; a parallel LATTICE-NATIVE pipeline (Route D, its
own concept note) independently consumes `P2-LATTICE-ONTOLOGY-01`;
SI-2 compares the two. Route D is therefore NOT a §7 route of this
gate — §7's Routes A–C are internal alternatives of the continuum
pipeline only.

    P2-LATTICE-ONTOLOGY-01
          │
          ├───────────────────┐
          │                   │
    Continuum pipeline   Lattice pipeline
    P2-FIERZSUM-01       Route D
          │                   │
    P2-VECPOLE-01         D0 → D1 (→ D2)
          └────────┬──────────┘
                   │
        Phase-B metric freeze
                   │
            SI-2 (death gate)

Consumes: `P2-LATTICE-ONTOLOGY-01` — **registered SPECIFIED** on
2026-08-01 (Paper 2 `GATES.md`), specification pinned at sha256
`1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c`.
This gate's §4.2 renormalization prescription must be written as the
finite subtraction-and-matching rule that declaration requires, and
must be compatible with, never determinative of, the microscopic
theory (per that gate's §1e delegation table).

---

## 0a. Scope of the review approval (recorded verbatim)

> This approval freezes the computational prescription architecture
> only. It is not a PASS on representation stability, diagram
> uniqueness, Fierz coverage, factorization, continuum–microscopic
> matching, `P2-VECPOLE-01`, or SI-2 admissibility.

## 0. Gate structure: two phases, one gate

This gate has a SPECIFICATION phase and an EXECUTION phase, and the two
must never be conflated.

**SPECIFIED (this document's deliverable).** Freezes: the target
observable and baseline; the continuum–microscopic matching rule and its
interface; the decoupling family; the truncation ladder; the diagram
ledger schema; the uncertainty schema; the factorization method; the
admissibility and outcome taxonomy; the checker designs.

**RUN / completed (a later, separately authorized task).** Executes: the
decoupling scan; `Δ_Fierz^(F,k)`; `Δ_mix^(k)`; the diagram-uniqueness
comparison; the convergence sequence; and the determination of whether
SI-2 may recover dispositive status.

> **Registration as SPECIFIED freezes only the prescription. It does NOT
> establish representation stability, absence of double counting,
> factorization accuracy, matching validity, or any numerical
> uncertainty band.** Every numerical quantity named in this document is
> a *deliverable of the RUN phase*, not a claim of this one.

## 1. Why this gate exists

Phase A established by machine verification that the frozen canonical
interaction has `interaction_coordinate_rank = 1`: one independent
microscopic coupling `G`, with five Fierz families (S,P,V,A,T) and
`16N²` component-level `K_ij` candidates.

**These two facts are not in tension by themselves, and this note does
not claim they are.** A theory with a single coupling can perfectly
well possess several bound states, distinct spin/parity states, radial
excitations, resonances, and mixed eigenmodes. Phase A's rank statement
constrains how many coordinates may be independently scanned; it says
nothing about how many poles the full two-point-function matrix has.

The genuine exposure is narrower:

> The potential problem arises only if Fierz-related representations of
> the same diagrammatic content are promoted to independent functional
> degrees of freedom and their determinants are added without a
> derivation of the measure, the constraints, and the factorization.

That is the classic **Fierz ambiguity** of mean-field / partially
bosonized four-fermion models: the exact theory is
decoupling-independent, but finite-order truncations acquire a
dependence on an unphysical decoupling choice.

SI-2 is a programme-death gate. Its verdict must not be an artefact of
that choice.

---

## 2. The precise question

**Which exact generating functional is SI-2 approximating, by what
truncation, and with what evidence that the answer is stable under
algebraically equivalent representations of the frozen interaction?**

The unambiguous starting point is the curved-background fermionic path
integral

    Z[g] = ∫ Dψ̄ Dψ  exp( − S_free[ψ̄,ψ;g] − S_int[ψ̄,ψ] )

with `S_int` the frozen generator-sum interaction. `ξ_ind` is defined
from the `R`-linear part of `−log Z[g]`. **The prescription required to define
and eventually match that coefficient as a unique physical number is
frozen as a deliverable of this gate (§4.2). Until the microscopic
matching dependencies are discharged, only the continuum-side
renormalized coefficient and its transformation law are available.** Auxiliary fields, channels,
composite propagators, and channel determinants are *representations*,
and each must be shown to approximate this object.

---

## 3. Level-typed map (replaces "choose one reading")

The five families can legitimately be described differently at
different levels; the gate's job is to state the MAPPINGS between
levels, not to pick one description.

| Level | What must be classified |
|---|---|
| Microscopic operator | how Fierz-related expressions represent the same frozen interaction |
| Functional measure | which auxiliary variables are introduced, with what constraints and Jacobian |
| Approximation scheme | which saddle / loop / RG / 2PI / large-N truncation is used |
| Renormalization / matching level | which subtraction, scheme and matching prescription converts a bare functional into a number (the same bare functional yields different `ξ` under different matching) |
| Effective-kernel / diagrammatic level | which 1PI, 2PI, bubble, ladder or ring topologies are retained and resummed; the inverse-propagator / Bethe–Salpeter / RPA structure |
| Correlator space | which currents and operators are probed |
| Physical spectrum | poles and eigenmodes of the FULL correlator matrix |

The prescription must supply the explicit MAPPING between each adjacent
pair, not merely the list of levels:
`microscopic operator → HS measure → truncation → K_ab → G_ab →
spectral structures`.

Statements true at one level (e.g. "redundant coordinates" at operator
level) do not transfer to another (e.g. "no independent modes" at
spectrum level) without an explicit mapping. This mirrors Phase A's
level-typing rule.

---

## 4. What the gate must freeze (deliverables)

1. **Target observable, with baseline decided.** Is SI-2 measuring the
   total matter-induced coefficient `ξ(G)`, the interaction-induced
   increment `Δξ(G) = ξ(G) − ξ(0)`, or the composite-sector
   contribution? Without this, "which term dominates" comparisons are
   comparisons of different observables.
2. **Renormalization, matching, and normalization prescription —
   THREE distinct layers that may not be conflated.** The registered
   substrate ontology fixes the status of each: the microscopic answer
   is finite on the lattice; a continuum regulator is a computational
   representation only; counterterms and subtractions may NOT
   independently determine the answer.

   **2a — Microscopic target (primary).** The finite
   reference-equivalence subtraction and matching REQUIREMENT AND
   INTERFACE inherited from `P2-LATTICE-ONTOLOGY-01` §2: a difference of
   two finite, fully specified configurations, requiring the reference
   equivalence class and its matching conditions to be frozen by their
   named owners, and the invariance requirement `ΔE[r₁] = ΔE[r₂]`
   satisfied within a preregistered tolerance, before Test II (§4.2c)
   becomes executable. This is what the gate is ultimately measuring —
   not what it can currently evaluate.

   **2b — Continuum implementation (representation only).** The
   regulator, renormalization scale `μ`, subtraction convention,
   counterterm bookkeeping, treatment of power divergences, and
   scheme-change transformation — used to COMPUTE the effective
   representation, never to define the physical answer.

   **2c — Matching: TWO distinct tests, only one of which is currently
   executable.**

   *Test I — continuum internal covariance (executable now).* Changing
   the continuum scheme while transforming the matching coefficients
   consistently must leave the effective coefficient invariant:

       ξ_EFT^(S₁)(C^(S₁)) = ξ_EFT^(S₂)(C^(S₂))   within preregistered tolerance

   *Test II — microscopic matching (NOT executable yet).*

       ξ_EFT,matched = ξ_lattice

   **Standing limitation.** `P2-LATTICE-ONTOLOGY-01` froze the
   OBLIGATION to have a finite reference-equivalence prescription; it
   did not complete the microscopic measure, kinetic operator, species
   ledger, geometry map, curvature estimator, the actual definition of
   the reference equivalence class, or the continuum–lattice matching
   map. Those are owned by `P2-LATTICE-MICROSPEC-01`, Route D D-pre, and
   Phase B. **Until they are frozen, `ξ_matched` is a required INTERFACE,
   not an available numerical observable.** This gate may verify Test I
   and freeze the transformation law and the placeholder matching
   interface; it may NOT claim microscopic scheme independence, and it
   may NOT supply a death-gate coefficient. Test II is recorded as an
   UNRESOLVED UPSTREAM DEPENDENCY, listed by owner.

   The gate must state whether a given reported number is bare,
   renormalized, or matched; the answer the ontology ultimately requires
   is the MATCHED one, which is presently unavailable.

   **Deliverables 1 and 2 are jointly first-rank**: the primary question
   is *what observable, matched how, relative to what baseline*. Note
   that `Δξ(G) = ξ(G) − ξ(0)` does NOT automatically cancel divergences
   or scheme dependence, since the interaction can change the dynamical
   mass, wavefunction normalization, non-minimal coupling, and threshold
   structure.

3. **The exact functional** (§2) and the named truncation.
4. **The decoupling prescription**: auxiliary variables, constraints,
   Jacobian, and an explicit statement of what is generated
   dynamically rather than introduced as an independent field.
5. **Diagrammatic ledger** (replaces "over-counting bound"): the
   truncation order; the vacuum/skeleton diagrams included; symmetry
   factors; the correspondence of each channel representation; and a
   demonstration that each topology appears exactly once. If only an
   approximate bound is offered, the norm, the observable, and the
   truncation domain defining that bound must be frozen — a
   basis-independent "percentage of over-counting" may not exist.
6. **Basis-independent spectrum definition** (§5).
7. **Factorization status** with the Schur-complement correction
   quantified (§6).
8. **Representation-stability disclosure**: how far `ξ_ind` moves under
   change of decoupling within a preregistered family (§7, Route B) —
   reported as a number with its qualifications, never asserted zero.

---

## 5. Basis-independent spectrum = correlator MATRIX

The basis-safe object is not a single projected correlator but the full
connected matrix over a **preregistered operator basis, complete within
the declared symmetry sector and truncation order** (absolute
completeness is unattainable in an interacting theory: derivative,
higher-dimension and multi-particle operators are unbounded in number):

    G_ab(q) = ⟨ J_a(q) J_b(−q) ⟩_conn

The spectral information comprises **poles, resonances and branch cuts,
together with their operator-dependent spectral weights, within the
declared analytic continuation** (the weights describe operator overlap
with those structures; they are not themselves states) — identified from
eigenvalue singularities of `G`, or equivalently determinant zeros of
its inverse kernel; not poles alone. **All spectral statements are
truncation-relative:** the object is the full correlator matrix *within
the frozen operator basis and truncation*. Downstream, `P2-VECPOLE-01`
may conclude only "no pole detected in the frozen correlator matrix" —
never "the theory contains no vector state" — unless operator-basis
convergence has separately been demonstrated. Individual
projected correlators supply operator-dependent spectral weights and
**may miss states to which the chosen current has zero overlap**.

Note the distinction the gate must maintain: Fierz rearrangement
concerns the four-fermion *interaction* basis. Currents carrying
different Dirac/Lorentz quantum numbers are not made into the same
observable by the phrase "Fierz-related". Three bases must be kept
separate: interaction basis, source/operator basis, physical-state
basis.

This is what makes the downstream `P2-VECPOLE-01` well-posed: "does the
vector channel have a pole" acquires meaning only once the correlator
matrix whose singularities are being asked about is named.

---

## 6. Factorization: Schur complement, not off-diagonal norms

Channel-by-channel accounting assumes

    Tr log K[g]  =  Σ_c Tr log K_c[g]

which holds only if `K` is block-diagonal in the chosen decomposition
or another factorization is proved. For

    K = [[A, B], [C, D]]

the exact statement is

    log det K = log det A + log det (D − C A⁻¹ B)

so a naive channel sum replaces the Schur complement by `log det D`.
The deliverable is therefore not merely an off-diagonal block norm or a
mixing percentage, but

    ΔΓ_mix = Tr log(D − C A⁻¹ B) − Tr log D

and in particular its `R`-linear part `Δξ_mix`, which is the direct
effect of mixing on SI-2's observable.

The formula requires `A⁻¹` to exist. At loci where the selected diagonal
block is singular or near-singular (zero modes, poles, phase-transition
neighbourhoods), the factorization must be reformulated using the full
determinant or an alternative block ordering; **the Schur-complement
formula may not be applied through the singularity**. The
exceptional-locus discipline must therefore report: zero modes of `A`;
condition number; whether a pseudo-inverse is admitted; block-ordering
dependence; determinant phase/branch; and the analytic continuation
used.

**Multiplicative anomaly.** If the block factorization is implemented as
a product of separately regularized infinite-dimensional operators, the
chosen determinant prescription must either establish multiplicativity
or compute the associated multiplicative anomaly. **No anomaly is to be
assumed by analogy**: its presence, and its contribution to the `R`
term, must be derived for the actual operator class and regularization
in use. Equally, it may not be ignored — a finite-dimensional Schur
identity does not by itself establish equality of separately regularized
functional determinants.

**On the existing 0.4% datum:** the recovered
`DECOMP-UNAVAILABLE-AS-RECOVERED` adjudication quantified 0.4%
**transverse–longitudinal** mixing. That demonstrates that at least one
recovered sector decomposition is not exact, and it motivates an
explicit factorization audit. It is a *different decomposition axis*
from S/P/V/A/T family mixing and provides **no quantitative prior** for
off-diagonal mixing between those families. This note previously
overstated that connection; the correction is recorded here rather than
silently removed.

---

## 7. Three candidate routes

**Route A — controlled Fierz-stable treatment.** Fierz-complete RG,
dynamical rebosonization, 2PI, or Schwinger–Dyson closure. These are
not equivalent to one another and none removes ambiguity "by
construction": each still requires a specified truncation, a closure
argument, convergence tests, and regulator-dependence checks. The
achievable claim is therefore **demonstrated Fierz stability within a
preregistered controlled truncation**, not exact Fierz invariance.
*Most rigorous; highest cost.*

**Route B — quantify the ambiguity (designated fallback).** Compute
`ξ_ind` across a family of decouplings and report the spread. To be
trustworthy rather than decorative, the following must be preregistered:
(i) the decoupling parameter `α` and its definition; (ii) its
admissible domain; (iii) proof that every admissible `α` represents the
SAME frozen interaction at the untruncated level; (iv) the sampling
grid; (v) adaptive refinement rules; (vi) singular/exceptional loci;
(vii) fixed regulator and renormalization scheme across the scan;
(viii) numerical convergence tolerance; (ix) whether the band is an
envelope, a confidence interval, or a systematic range; (x) behaviour
as truncation order increases. Two sample points are not a band —
non-monotonic dependence, interior extrema, and singular decouplings
must be excluded by the scan design, not by assumption.

The result must be labelled **`Δ_Fierz^(F)`** — the ambiguity observed
within the preregistered family `F`. It is not a global bound over all
possible Fierz truncations unless separately proved.

**Family admissibility verdict (required before any death-verdict
use).** A narrow family can be chosen to yield an artificially small
band, so the gate MUST classify `F` as one of:
`JUSTIFIED-COVERAGE-WITHIN-CLASS`, `LOCAL-DIAGNOSTIC-ONLY`, or
`UNJUSTIFIED`. **Only `JUSTIFIED-COVERAGE-WITHIN-CLASS` may enter the
aggregate death-verdict uncertainty band as a bounded Fierz
systematic**; the other two are exploratory.

Minimum conditions for `JUSTIFIED-COVERAGE-WITHIN-CLASS` (frozen here,
so the verdict is not a matter of taste):
(i) every `α` in the family exactly reconstructs the same canonical
interaction, verified symbolically;
(ii) the family contains every connected non-singular branch generated
by the declared HS/Fierz parametrization class;
(iii) boundaries, singular loci and disconnected branches are
enumerated;
(iv) any excluded decoupling class carries an explicit stated reason;
(v) coverage is claimed ONLY for the frozen parametrization class — the
name carries "WITHIN-CLASS" precisely because it is not a bound over all
possible bosonizations.

**Headline statistic (not a single band).** A narrow Fierz band is not
evidence of reliability: every decoupling can be wrong together within
one coarse truncation. The primary record is therefore the
truncation-indexed convergence sequence

    { ξ^(k), Δ_Fierz^(F,k), Δ_reg^(k), Δ_mix^(k), Δ_match^(k) }  for k = 1 … k_max

where `Δ_match^(k)` is the continuum scheme-covariance residual (Test I
of §4.2c). A lattice matching residual joins this sequence once the
microscopic interface of Test II becomes executable.

with the headline read from it: is the SIGN stable, is the band
CONTRACTING, is the central value CONVERGING, is the scheme/regulator
spread CONTROLLED. A single aggregate band is a summary of this record,
never a replacement for it.

**Route C — direct fermionic expansion without HS channel selection.**
*(Corrected name and content.)* This is **not** "the fermionic
determinant": with a four-fermion interaction the fermionic integral is
not Gaussian and is not a single ordinary determinant. What is meant is
a direct expansion of the curved-background generating functional —
cumulant/perturbative vacuum diagrams, 2PI, Schwinger–Dyson, large-N,
or FRG — **without choosing an HS channel decomposition**.

Route C removes *auxiliary-field decoupling* ambiguity at the
representation level. It does **not** automatically remove all
representation dependence: selective resummation, channel-selective
self-energy ansätze, incomplete vertex truncation, or a particular gap
equation closure can each reintroduce it. Any Route-C truncation must
still be tested for invariance under algebraically equivalent
representations of the frozen interaction.

A hypothesis worth testing but NOT asserted here: if a
representation-free baseline contribution to `ξ_ind` is large compared
with the interaction-induced increment, the channel inventory may be
subleading for SI-2. Whether that is even a meaningful comparison
depends entirely on deliverables §4.1–§4.2–§4.3 (target observable and
baseline; renormalization/matching prescription; exact functional and
truncation) — comparing
`ξ(G)` with `ξ(0)`-inclusive quantities without fixing the target
observable would compare different observables and prove nothing.

---

## 8. Machine-checkable conditions (what makes this a gate)

- **Exact-equivalence test.** For each decoupling `α`, integrating out
  the auxiliary fields must symbolically reproduce the frozen
  `S_int`. Verified by checker, not asserted in prose.
- **Diagram-uniqueness test.** Expand the channel determinants,
  `Tr log(1+X) = Tr X − ½ Tr X² + …`, and compare against the direct
  fermionic cumulant expansion **through at least O(G²)**. The checker
  separately reports whether the `O(G)` contribution survives the frozen
  vacuum-normalization, saddle and baseline-subtraction prescription (it
  can vanish by normal ordering, tadpole subtraction, symmetry, or
  expansion around a gap-equation saddle). **The first order at which a
  topology multiplicity differs is an OUTPUT, never a presupposition** —
  the gate may not assume double counting first appears at `O(G)` or at
  `O(G²)`.
  **Finite-order evidence is NOT an all-order proof.** The checker MUST
  report the highest verified order and classify the result as either
  (i) *no duplicate topology detected through `O(G^k)` within the frozen
  diagram class* — finite-order evidence, or (ii) *all-order
  non-double-counting proof*, which requires one of: an all-order
  generating-functional identity; a skeleton/topology bijection proof; a
  full combinatorial map between the determinant expansion and the
  fermionic cumulant expansion; or a demonstration that higher orders
  are uniquely generated by a verified recursion. **These two statuses
  may not be conflated in any downstream use.** Double counting can
  first appear above `O(G²)` through mixed-channel rings, vertex
  corrections, or resummed topologies.
- **HS-normalization / Jacobian curvature test.** For every admissible
  decoupling `α`, verify not only recovery of the frozen quartic
  interaction but the full identity
  `Z_HS^(α)[g] = N_α[g] · Z_fermionic[g]`, and determine whether
  `δ log N_α[g] / δR` vanishes. A field-independent normalization is
  harmless in flat-space scattering, but here the observable IS
  `−log Z[g]`: any metric-, regulator- or curvature-dependent
  normalization, contour phase, or Jacobian contributes to the
  cosmological and `R` terms and **must be included in `ξ_ind`, not
  discarded as an irrelevant constant**.
- **Sum rules / completeness** of channel spectral weights against the
  full correlator matrix.
- **Factorization audit** producing `ΔΓ_mix` and `Δξ_mix` (§6).
- **Representation-stability scan** producing `Δ_Fierz^(F)` (§7B).

---

## 9. Outcome table — consequences for SI-2

| Finding | Consequence |
|---|---|
| Representation stability and diagram uniqueness demonstrated to the frozen truncation order (Route A or C), with EITHER an all-order proof OR a separately reported residual truncation uncertainty | The continuum prescription becomes admissible for downstream specification. `P2-VECPOLE-01` may then be SPECIFIED against the frozen correlator/kernel framework (it additionally requires its own frozen operator basis, analytic continuation, vector quantum-number sector, residue/pole criteria, and exceptional-locus rules). **SI-2 may be re-specified only after all remaining matching and Phase-B dependencies are discharged.** With finite-order evidence only, any eventual death-gate status rests on the aggregate uncertainty band, not on the word "established" |
| Quantified ambiguity band which, **combined with all preregistered regulator, factorization, numerical and truncation uncertainties**, excludes zero with the required margin | SI-2 may retain death-gate status, with the aggregate band recorded in the verdict |
| `Δ_Fierz^(F)` alone excludes zero, but other load-bearing errors remain unbounded | SI-2 remains **non-dispositive** |
| Aggregate band straddles zero | SI-2 may compute; **no death verdict** |
| No consistent prescription found | SI-2 as specified is invalid; withdraw or rebuild before any promotion or exclusion relies on it |
| Inconclusive | SI-2 may run only as exploratory / non-dispositive; no death-gate verdict, promotion, or exclusion may rely on the unresolved channel accounting |

**"Required margin" is not defined by this gate.** Excluding zero is
meaningless if `ξ_min = 10⁻¹²` while numerical/systematic precision is
`10⁻⁸`. The prescription artifact carries an explicit unresolved field
`death_verdict_margin: PHASE_B_REQUIRED`; Phase B must define the margin
(absolute tolerance, relative tolerance, multiple of numerical error, or
robustness margin) before any death verdict is admissible.

---

## 10. Deliverable artifacts (hash-pinned, parallel to the canonical set)

    derivations/P2-FIERZSUM-01_prescription.md        # frozen prescription
    derivations/P2-FIERZSUM-01_prescription.json      # machine companion
    derivations/P2-FIERZSUM-01_uncertainty_schema.json # error taxonomy
    scripts/P2-FIERZSUM/check_prescription.py         # verifier
    scripts/P2-FIERZSUM/check_diagram_ledger.py       # diagram uniqueness
    results/P2-FIERZSUM/<run-id>/run_manifest.json    # per-RUN provenance
    results/P2-FIERZSUM/<run-id>/...                   # scan outputs
    reports/<date>_P2-FIERZSUM-01_*.md

`run_manifest.json` lives with its run, NOT in `derivations/`: it is
execution-specific provenance, not a derivation or a frozen
prescription, and must not share the prescription's amendment
authority. It records the pinned prescription hashes, chosen route,
truncation orders, regulator, decoupling family, software/environment
pins, upstream dependency hashes, and the unresolved
microscopic-matching fields; its hash is pinned by the run report. The
prescription JSON freezes only the manifest's SCHEMA and required
fields. (If the repository later adopts a `manifests/` convention, the
manifest moves there; that is a separate decision.)

`uncertainty_schema.json` separately defines: Fierz-family spread;
regulator spread; truncation sequence; factorization correction;
numerical error; and the aggregation rule. This artifact set stays
INDEPENDENT of the canonical set — `CANONICAL_INTERACTION` is the
microscopic source of truth, this prescription is a downstream
computational scheme, they have different amendment authority, and
merging them would force the canonical hash chain to churn whenever the
computational scheme changes.

The markdown freezes: target observable and baseline subtraction;
functional and truncation; measure and constraints; decoupling family;
diagrammatic ledger; factorization rule; uncertainty aggregation rule;
downstream admissibility conditions. The JSON companion carries the
machine-readable form so that `P2-VECPOLE-01`, Phase B, and SI-2 can
pin it by hash — the same source-fidelity architecture Phase A now uses.

---

## 11. Known weaknesses (Generator's own flags)

1. **Regress risk.** SI-2 → VECPOLE → FIERZSUM: each audit has found an
   upstream question. Route B is the designated terminating fallback,
   converting an unresolved formal question into a reported systematic.
   The PI should treat any further upstream discovery as a signal to
   invoke Route B rather than to open a fourth gate.
2. **Scope risk.** Route A is a research programme in itself; the gate
   must be specified so that it can actually be run.
3. **Specification gate, not a numerical one.** The deliverable is a
   frozen prescription plus a small number of checkable conditions —
   a different shape from betaV or Phase A.
4. **Generator reliability.** The Generator has erred in this class of
   reasoning, including twice within this note's own review cycle
   (rank↔species conflation; the 0.4% mixing over-extension). The
   prescription must be independently reviewed before any downstream
   gate consumes it.

---

## 12. Questions for the Discriminator (v3 — Round 2 scope)

1. Is the level-typed map in §3 complete, or is a level missing between
   "approximation" and "correlator space"?
2. (ANSWERED by review: SI-2's eventual verdict object is the total
   MATCHED coefficient `ξ_matched(G) = ξ_matched(0) + Δξ_matched(G)`,
   with all three recorded separately as a mandatory decomposition
   ledger — `ξ(0)` the substrate/free baseline, `Δξ(G)` the
   interaction-induced increment, `ξ(G)` the total that determines the
   gravitational sign. A composite-sector contribution alone is
   diagnostic and may NOT serve as the death-verdict object.)
   Retained for the record: is the baseline-subtraction deliverable
   (§4.1) correctly identified
   as the primary one — i.e. does the programme intend SI-2 to measure
   `ξ(G)`, `Δξ(G) = ξ(G) − ξ(0)`, or the composite-sector piece?
3. For the diagram-uniqueness test (§8), what is the lowest order at
   which double counting would actually become visible in this
   interaction?
4. Is `Δ_Fierz^(F)` the right primary statistic, or should the gate
   report a truncation-order convergence sequence as the headline?
5. Is the artifact structure in §10 the right granularity, or should
   the prescription be folded into the existing canonical set?
