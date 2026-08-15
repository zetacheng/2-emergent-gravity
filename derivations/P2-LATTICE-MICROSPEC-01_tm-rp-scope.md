# `P2-LATTICE-MICROSPEC-01` — what the transfer-matrix and reflection-positivity work actually is

**THIS ARTIFACT CONSTRUCTS NOTHING.** No transfer matrix, no
reflection-positivity proof, no spectral equivalence. **It determines what that
work is, before the programme commits to it.**

**No candidate is selected, eliminated, ranked or preferred.** **Where the work
looks smaller for one candidate, that is a fact about the mathematics
available, not about the physics** — §10 states this where the size estimate
is, and not only here.

**Evidence base:** `e70f55def26a96ffc325c0ae3231223e4623c76b`.

---

## 1. The three propositions, quoted as measured

**MEASURED, `derivations/P2-LATTICE-ONTOLOGY-01.md` lines 70–80:**

> - **Reflection positivity is a frozen obligation**, not an assumption:
> the declared H(4) action must be reflection-positive, or no quantum
> theory corresponds to it. **Three propositions are distinct and may
> not be conflated:** (i) positivity of a particular finite transfer
> matrix (sufficient, in that finite model, to define
> `H = −a⁻¹ log T`); (ii) Osterwalder–Schrader reflection positivity of
> the Euclidean measure/action (the general reconstruction condition —
> for the H(4) fermion action with Grassmann measure, spin structure,
> interactions and determinant signs, this must be proved per declared
> kinetic operator, and cannot be transplanted from a bosonic Ising
> example); (iii) axis equivalence (the three-level deliverable below).

**The per-operator clause for `(ii)`, quoted verbatim, MEASURED at lines
77–80:**

> for the H(4) fermion action with Grassmann measure, spin structure,
> interactions and determinant signs, this must be proved per declared
> kinetic operator, and cannot be transplanted from a bosonic Ising
> example

**THIS ARTIFACT PROPOSES NO SHARED CONSTRUCTION FOR `(ii)`.** The frozen text
forbids transplanting it, and §8's recommendation is explicitly structured so
that what is shared is `(i)`-level and normalisation machinery, never `(ii)`.

**`(iii)`'s three levels, MEASURED at lines 86–95:**

> (1) equality of the Euclidean partition function under permitted axis
> relabellings; (2) reconstruction of a positive transfer operator for
> every candidate slicing; (3) equivalence, after the declared scale and
> orientation identifications, of the resulting infrared observable
> algebras and spectra. The exploratory Ising probe demonstrates
> level 1 exactly and a finite-dimensional example of
> transfer-Hamiltonian construction; it does NOT establish levels 2–3
> for the H(4) fermion theory.

## 2. Which of the three would discriminate

**Only `(ii)`. DERIVED from the frozen text.**

**Line 71 states the obligation:** *"the declared H(4) action must be
reflection-positive, or no quantum theory corresponds to it."* **That is a
condition on the action**, which is `(ii)`. **A candidate whose declared action
is `REFUTED` at `(ii)` fails an obligation the programme has already frozen**,
and that would be negative candidate evidence.

**`(i)` would not discriminate, and the parenthesis says why.** It is
*"sufficient, in that finite model, to define `H = −a⁻¹ log T`"* — **sufficient,
not necessary.** A candidate for which some particular finite transfer matrix
fails to be positive has not thereby failed line 71's obligation; it has failed
one route to discharging it. **`(i)` REFUTED supplies no negative candidate
evidence.**

**`(iii)` would not discriminate against line 181's obligation either.** It is
its own deliverable, about which axis is time, and line 85 states that *"which
axis is time is not a selection problem"*. **A candidate failing `(iii)` would
have a different problem, not a reflection-positivity problem.**

**So the twelve cells of §3 are not twelve equally weighted results.** **Four
of them — `(ii)` for each candidate — are the ones that could carry
discriminating information, and the other eight cannot.** **An assessment that
treated the three propositions as one requirement would have obscured that**,
which is what the frozen text's "may not be conflated" is guarding.

---

## 3. Twelve results — four candidates × three propositions

**Dispositions, per the specification:** `ESTABLISHED IN THE REPOSITORY`,
`NOT ESTABLISHED`, `REFUTED`, `NOT DETERMINABLE BY THIS TASK`.

### 3.1 Proposition `(i)` — positivity of a particular finite transfer matrix

    naive       NOT DETERMINABLE BY THIS TASK
    Wilson      NOT DETERMINABLE BY THIS TASK
    staggered   NOT DETERMINABLE BY THIS TASK
    overlap     NOT DETERMINABLE BY THIS TASK

**Common reason, and it is the same for all four: settling `(i)` requires
constructing a transfer matrix**, which §4 of the governing specification
forbids. **The repository state is `NOT ESTABLISHED` for all four** — MEASURED,
line 93 says the Ising probe *"does NOT establish levels 2–3 for the H(4)
fermion theory"*, and no transfer matrix for any of the four candidate fermion
actions appears anywhere in the repository.

**The disposition reported is the stronger statement**: not merely that nobody
has done it, but that this task cannot.

### 3.2 Proposition `(ii)` — OS reflection positivity of the Euclidean measure/action

    naive       NOT DETERMINABLE BY THIS TASK
    Wilson      NOT DETERMINABLE BY THIS TASK
    staggered   NOT DETERMINABLE BY THIS TASK
    overlap     NOT DETERMINABLE BY THIS TASK

**Common reason: settling `(ii)` requires an Osterwalder–Schrader positivity
proof or refutation for the declared action**, which §4 forbids. **The
repository state is `NOT ESTABLISHED` for all four**, as the dossier records.

**NO CELL IS `REFUTED`, and the distinction is the point of the vocabulary.**
**For no candidate did this assessment derive that the declared action fails
the condition.** In particular:

- **The overlap's non-ultralocality is NOT a refutation.** The dossier derives
  an obstruction to **one family of methods** — the split-plus-nearest-neighbour
  constructions — and states explicitly that this is not a demonstration that
  reflection positivity fails. **This artifact does not upgrade it**, and an
  obstruction to a proof method is not a property of the action.
- **For naive, Wilson and staggered nothing in the repository bears on `(ii)`
  at all**, so there is nothing that could be upgraded.

**MEASURED, and it corrects a claim that was in circulation:** the dossier's
reflection-positivity section, `§4` at its lines 298–352, **never cites a
transfer matrix as the reason for any of the four `NOT ESTABLISHED` results.**
The dossier's transfer-operator dependency sits at its lines 437–445, in the
section on **ontology line 184's vacuum-selection rule**, which is a different
obligation. **A transfer matrix is not a logical prerequisite for `(ii)`**:
Osterwalder–Schrader positivity is a condition on the Euclidean action and
measure, and the reconstruction theorem produces the Hilbert space and the time
evolution *from* it.

### 3.3 Proposition `(iii)` — axis equivalence

    naive       NOT DETERMINABLE BY THIS TASK
    Wilson      NOT DETERMINABLE BY THIS TASK
    staggered   NOT DETERMINABLE BY THIS TASK
    overlap     NOT DETERMINABLE BY THIS TASK

**Common reason: `(iii)` is a three-level deliverable and level 2 is
"reconstruction of a positive transfer operator for every candidate slicing"**,
which is the construction §4 forbids. **Level 3 depends on level 2.** So no
candidate's `(iii)` can be settled here.

**But level 1 is separable, and it is nearly free. DERIVED, and reported
because a scope assessment that omitted it would overstate the work.**

**Level 1 is "equality of the Euclidean partition function under permitted axis
relabellings".** For a quadratic Grassmann action, `Z = det D`.

- **naive, Wilson, overlap. DERIVED:** the operators are manifestly symmetric
  under axis permutation, as the discriminants artifact establishes at its
  §1.2, so `D` is conjugated by a permutation matrix and `det D` is unchanged.
- **staggered. DERIVED, and VERIFIED HERE.** The permutation is a symmetry only
  after a sign redefinition `χ(x) → ε(x)χ(x)`, `ε = ±1`. Under it
  `D → E D E` with `E = diag(ε)`, so `det(EDE) = det(E)² det D = det D`, since
  `det E = ±1`. **The Berezin measure contributes `det(E)^{-2} = 1` for the same
  reason.** **VERIFIED on a `2⁴` lattice at `m = 0.7`: `det D` is unchanged by a
  random sign redefinition, and `max |det D(axis-permuted) − det D| = 0.00e+00`
  over all 23 non-trivial permutations.**

**So level 1 holds for all four at the free-field level**, three trivially and
one by the redefinition argument. **This is a statement about level 1 only. It
does not establish `(iii)`**, and the disposition above stands.

**NOT ESTABLISHED at level 1 for the interacting action.** The verification
above is quadratic-action only; the declared four-fermion interaction was not
included, and adding it changes `Z` from a determinant to an integral.

### 3.4 Disposition counts

    ESTABLISHED IN THE REPOSITORY     0
    NOT ESTABLISHED                   0    (as the reported disposition)
    REFUTED                           0
    NOT DETERMINABLE BY THIS TASK    12

**Twelve of twelve `NOT DETERMINABLE BY THIS TASK`.** **The specification
expected this disposition to be common and it is universal**, which is itself
the assessment's principal finding: **nothing about any of the three
propositions can be settled without performing construction work, for any
candidate.**

**The repository state underlying all twelve is `NOT ESTABLISHED`.** **Twelve
uniform results carry no discriminating information**, and the dossier already
demonstrated that four do.

---

## 4. Is `(ii)` directly addressable at the Euclidean level? — four results

**One result per candidate, not per cell.** The question is whether proposition
`(ii)` can be attacked at the Euclidean action and measure level **without
first constructing a transfer matrix**.

    naive       DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix required first
    Wilson      DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix required first
    staggered   DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix required first
    overlap     NOT DETERMINABLE — the standard direct route is obstructed, and
                no alternative is identified here

**The common ground, DERIVED.** Osterwalder–Schrader reflection positivity is a
condition on the Euclidean measure and action: that
`⟨θ(F) F⟩ ≥ 0` for observables `F` supported on one side of a reflection plane.
**Checking it requires the action, the measure and a reflection — not a Hilbert
space.** The reconstruction theorem runs the other way, producing the Hilbert
space and `H` from a measure that satisfies the condition. **So for a
formulation whose action splits appropriately across a reflection plane, the
question is posed entirely at the Euclidean level.**

**naive, Wilson, staggered: the action is finite-range**, as the discriminants
artifact establishes at its §4.1 — each is a trigonometric polynomial of degree
one in momentum, so the position-space couplings connect only nearest
neighbours.
**A nearest-neighbour action admits the standard split into a piece on each
half-lattice plus a cross-term on the reflection plane**, which is the shape a
direct Euclidean argument needs. **Whether the argument then succeeds is
exactly what is `NOT DETERMINABLE BY THIS TASK`** — the Grassmann measure, the
spin structure and the determinant signs are what the frozen text names as the
reason it must be proved per operator.

**overlap: the action is not ultralocal**, derived in the dossier's §4.4 —
`[s + (W − M_0)²]^{−1/2}` is not a trigonometric polynomial, so the couplings
connect every pair of time slices. **The split the direct route needs is not
available.** **This is not a statement that `(ii)` fails for overlap, and not a
statement that no direct route exists** — it is that the one this assessment
can identify does not apply, and no alternative is identified here.

**The consequence for scope, stated plainly: for three of the four candidates
the reflection-positivity route does not wait on the transfer matrix at all.**
**The machinery shared with `D-pre-B` is `(i)`-level and normalisation
machinery, not the obligation itself.**

**This is a statement about which mathematics applies. It is not a statement
that any candidate is more likely to satisfy the obligation**, and §10 says why
that inference is not available.

---

## 5. Literature claims — all `UNVERIFIED FROM THIS REPOSITORY`

**The repository contains no literature and this assessment had no access to
any.** **Every claim below is recalled, not consulted.** They are stated
precisely enough to be found and checked by someone with library access, and
**none is verified here.**

**A recalled citation is not a source.** Where a field below is uncertain it
says so rather than being filled in to look complete.

### Claim L1 — the reconstruction framework

    AUTHOR/WORK   K. Osterwalder and R. Schrader, "Axioms for Euclidean
                  Green's functions", Communications in Mathematical
                  Physics, two papers, 1973 and 1975.
    STATEMENT     Euclidean Green's functions satisfying a set of axioms
                  including reflection positivity reconstruct a Wightman
                  quantum field theory, with a positive Hilbert space and
                  a self-adjoint Hamiltonian.
    SCOPE         Continuum Euclidean field theory. A fermionic version is
                  treated; the precise axiom set differs between the two
                  papers, and this assessment does not recall which
                  formulation is the one usually cited for Grassmann
                  fields.
    COVERAGE      DOES NOT COVER the declared action's reflection
                  positivity. This is the theorem that makes RP the right
                  condition to check; it establishes nothing about whether
                  any particular lattice action satisfies it.
    STATUS        UNVERIFIED FROM THIS REPOSITORY.

### Claim L2 — reflection positivity for Wilson-type lattice fermions

    AUTHOR/WORK   K. Osterwalder and E. Seiler, "Gauge field theories on a
                  lattice", Annals of Physics, 1978.
    STATEMENT     Reflection positivity is established for a class of
                  lattice gauge theories with Wilson fermions, using a
                  reflection in a plane between or through lattice sites.
    SCOPE         Recalled as covering the Wilson fermion action coupled to
                  gauge fields, at r = 1, for a specified reflection type.
                  Whether both site- and link-reflection cases are covered,
                  and under exactly which conditions, is NOT RECALLED with
                  confidence.
    COVERAGE      COVERS A RESTRICTION ONLY. The programme's declared
                  action is an H(4) fermion action with a four-fermion
                  interaction and no gauge field. Whether a Wilson-type RP
                  construction extends to it is precisely what the frozen
                  text says must be proved per declared kinetic operator.
    STATUS        UNVERIFIED FROM THIS REPOSITORY.

### Claim L3 — reflection positivity for staggered fermions

    AUTHOR/WORK   NOT RECALLED with sufficient specificity to name a work.
    STATEMENT     This assessment recalls that reflection positivity for
                  staggered fermions is treated in the literature and is
                  understood to be more delicate than the Wilson case,
                  the available reflections being constrained by the
                  two-site structure the spin diagonalisation induces.
    SCOPE         NOT RECALLED.
    COVERAGE      NOT RECALLED.
    STATUS        UNVERIFIED FROM THIS REPOSITORY, AND INCOMPLETE.

**This is recorded as an incomplete claim and is NOT counted among the
structured claims.** **The specification is right that "a standard construction
exists" is not a claim but the absence of one**, and L3 as stated is that
absence. **It is written down so that the next task knows there is something
to look for, and not so that anything may be built on it.**

### Claim L4 — the overlap operator and locality

    AUTHOR/WORK   H. Neuberger, papers introducing the overlap Dirac
                  operator, mid-1990s; and P. Hernández, K. Jansen and
                  M. Lüscher on the locality of the overlap operator,
                  approximately 1998.
    STATEMENT     The overlap operator is not ultralocal but is
                  exponentially localised for suitable kernel parameters.
    SCOPE         Free and gauge-field cases, with conditions on the gauge
                  field for the localisation bound.
    COVERAGE      COVERS THE LOCALISATION PROPERTY ONLY, and the free-field
                  case of it is independently DERIVED in this repository
                  by the dossier's §4.4 and re-derived by the
                  discriminants artifact. It establishes nothing about
                  reflection positivity, and this assessment does not
                  recall a work establishing RP for the overlap action.
    STATUS        UNVERIFIED FROM THIS REPOSITORY.

### 5.1 Counts

    structured claims with all four fields          3    (L1, L2, L4)
    marked UNVERIFIED FROM THIS REPOSITORY          4    (L1, L2, L3, L4)
    incomplete, not counted as a claim              1    (L3)

    COVERAGE reaching this programme's declared action        0
    COVERAGE reaching only a restriction of it, or unrelated  3

**ZERO of the recalled results cover the declared action.** **That number is
the one that determines how much work remains**, and it is zero.

**A scope estimate resting on unverified coverage claims is only as good as
those claims** — and here the claims are unanimous in *not* reaching the
declared action, so the estimate below does not depend on any of them being
right. **If L2's coverage turned out broader than recalled, the estimate would
shrink; it cannot grow.**

---

## 6. The nine `D-pre-B` items, classified

**MEASURED, `derivations/P2-LATTICE-ROUTE-01.md` lines 195–205.** The blocking
deliverable is Euclidean–spectral response equivalence, and it requires nine
items.

**Classification: required by the reflection-positivity obligation as well
(`BOTH`), by `D-pre-B` alone (`D-pre-B`), or by neither once `(i)` is separated
from `(ii)` (`NEITHER`).**

    #  item                                         classification
    1  transfer-matrix normalization                D-pre-B  (and (i), not (ii))
    2  geometry-dependent measure and Jacobian      BOTH
       factors
    3  finite temporal extent                       BOTH
    4  temporal boundary conditions                 BOTH
    5  vacuum degeneracy                            D-pre-B
    6  additive energy normalization                D-pre-B
    7  contact terms                                D-pre-B
    8  curvature-dependent normalization            D-pre-B
    9  static geometry ↔ Euclidean four-geometry    D-pre-B
       restriction

    required by BOTH lines of work    3    (items 2, 3, 4)
    D-pre-B alone                     6    (items 1, 5, 6, 7, 8, 9)
    NEITHER                           0

**Reasons, per item:**

1. **transfer-matrix normalization — `D-pre-B`, and `(i)`, not `(ii)`.** This
   is the item the overlap was assumed to run through, and separating `(i)`
   from `(ii)` is what moves it. A normalisation of `T` presupposes `T`, which
   is `(i)`-level machinery. **`(ii)` does not need it**, per §4.
2. **geometry-dependent measure and Jacobian factors — `BOTH`.** `(ii)` is a
   condition on the *measure* as well as the action, and the frozen text names
   the Grassmann measure explicitly at line 77. A reflection acts on the
   measure, so its geometry dependence and Jacobians are needed on both sides.
3. **finite temporal extent — `BOTH`.** Reflection positivity is stated with
   respect to a reflection plane in a finite volume; the temporal extent
   determines which reflections are available and whether the two half-lattices
   are what the split assumes.
4. **temporal boundary conditions — `BOTH`.** The same reason. Antiperiodic
   versus periodic fermion boundary conditions change the reflection structure,
   and for a Grassmann measure they change determinant signs — which line 78
   names as part of what must be proved per operator.
5. **vacuum degeneracy — `D-pre-B`.** This is line 184's vacuum-selection rule
   territory, which the dossier ties to the reconstructed transfer operator.
   **`(ii)` does not require a unique vacuum**; the reconstruction produces
   whatever vacuum structure the measure carries.
6. **additive energy normalization — `D-pre-B`.** A shift of the zero of energy
   is invisible to a positivity condition on the measure.
7. **contact terms — `D-pre-B`.** These are a feature of the response function
   comparison and of the subtraction convention lines 209–210 require. `(ii)`
   is a statement about the measure, not about a correlator's short-distance
   behaviour.
8. **curvature-dependent normalization — `D-pre-B`.** Same reason as 6 and 7.
   The declared geometry class enters `Δ_EH`, not the positivity condition.
9. **static-geometry to Euclidean-four-geometry restriction — `D-pre-B`.**
   This relates the two sides of `Δ_EH`. It is a statement about which
   configurations are compared, not about the measure's positivity.

**MEASURED OVERLAP: three of nine.** **And item 1 — the one that named the
transfer matrix and made the two lines of work look joined — is NOT among
them** once `(i)` is separated from `(ii)`.

---

## 7. What the overlap is, stated before the recommendation

**The measured overlap is small, and it is not where it was expected.**

**Expected:** item 1, transfer-matrix normalization, because both lines of work
were described as waiting on a transfer matrix.

**Measured:** items 2, 3 and 4 — measure and Jacobian factors, finite temporal
extent, temporal boundary conditions. **These are shared because reflection
positivity is a condition on a measure over a finite lattice with boundary
conditions, and `D-pre-B` needs the same objects for a different purpose.**
**Item 1 is not shared**, because `(ii)` does not need a transfer matrix.

**The three shared items are shared as INPUTS, not as constructions.** Each is
a specification of the setup — what the measure is, how long the lattice is,
what happens at the ends — rather than a theorem either line proves. **Two
lines of work needing the same setup fixed is a weaker form of overlap than two
lines needing the same theorem**, and the distinction matters for §8.

---

## 8. The scoping recommendation — one piece of work or two

**RECOMMENDATION: TWO pieces of work, with a shared preliminary.**

**The measured overlap does not support combining them.** Three of nine items
overlap; all three are setup specifications rather than constructions; and the
one construction-level item, transfer-matrix normalization, belongs to
`D-pre-B` and to `(i)`, not to the obligation.

**What a combined task would have to contain:**

- the shared setup — the Grassmann measure with its geometry dependence and
  Jacobians, the finite temporal extent, and the temporal boundary conditions
  — fixed once;
- **four separate `(ii)` treatments**, one per declared kinetic operator, which
  the frozen text requires and forbids sharing;
- the transfer-matrix construction and its normalisation, for `(i)` and for
  `D-pre-B`;
- the six `D-pre-B`-only items;
- the `Δ_EH` residual and the identical-subtraction-convention requirement of
  lines 209–210.

**That is a task whose parts do not constrain each other**, except through the
shared setup. **A combined specification would be a container, not a
synthesis.**

**What a split would duplicate: the shared setup, items 2, 3 and 4 — and only
those.** **Duplicating a setup specification is cheap and detectable**; two
tasks fixing the same measure differently is a discrepancy a later check can
find, whereas two tasks inside one specification silently assuming different
temporal boundary conditions is not.

**Hence: a short preliminary fixing items 2, 3 and 4, then two independent
tasks.** **This artifact does not write any of them** — §4 forbids it, and a
recommendation is not a specification.

---

## 9. Size estimate

**Stated as a count of distinct constructions and which are independent, not as
an adjective.**

**Candidate-independent work — ONE construction each:**

    the shared setup (items 2, 3, 4)                        1
    the transfer-matrix construction, for (i) and D-pre-B   1
    the six D-pre-B-only items (5-9 plus item 1's
      normalisation), sharing the transfer matrix           1
    (iii) level 1, free-field                               ~0   — §3.3 derives
                                                                  it for all four

**Four-fold work — ONE construction PER CANDIDATE:**

    (ii), per declared kinetic operator                     4
    (iii) levels 2-3, per candidate slicing                 4

**RANGE: between 7 and 11 distinct constructions.**

**The basis for the range, stated rather than implied:**

- **Lower bound 7** = 3 candidate-independent + 4 for `(ii)`. This assumes
  `(iii)` levels 2–3 are absorbed by the transfer-matrix construction once it
  exists, since level 2 *is* a positive transfer operator per slicing.
- **Upper bound 11** = 3 + 4 + 4, if `(iii)`'s per-slicing requirement is not
  absorbed and each candidate needs its own.
- **Which bound applies is `NOT DETERMINABLE BY THIS TASK`**, because it
  depends on whether one transfer-matrix construction serves every slicing —
  a question about the construction, which §4 forbids performing.

**The four-fold part is irreducible.** Line 78 requires `(ii)` per declared
kinetic operator and forbids transplanting, so **no amount of shared machinery
reduces the count of `(ii)` treatments below four** while four candidates
remain. **The programme could reduce it by ruling on the operator first** —
which is a PI decision this artifact does not prepare and does not recommend.

**What the estimate does NOT rest on:** any literature claim. §5 measures that
zero recalled results cover the declared action, so the count above is what
remains whether or not L1, L2 and L4 are right.

---

## 10. Effort is not evidence

**Stated here, where the size estimate is, and not only in a closing section.**

**§4 reports that `(ii)` is directly addressable for three candidates and
obstructed for one. §3.3 reports that level 1 of `(iii)` is nearly free for all
four, and that the staggered case needed an argument the others did not.**

**None of that is evidence about any candidate's admissibility.**

**A candidate for which a proof route is available is not thereby more likely
to satisfy the obligation** — an available route can end in a refutation. **A
candidate for which the identified route is obstructed has not thereby failed**
— the dossier says exactly this about the overlap, and this artifact does not
say more.

**Tractability is a fact about the mathematics available to us. Admissibility
is a fact about the theory.** **Reporting the first as though it bore on the
second is the failure this line has now avoided three times**, and it would be
easiest to commit here, where the whole deliverable is an estimate of effort.

---

## 11. What this artifact does not establish

- **It constructs nothing** — no transfer matrix, no reflection-positivity
  proof, no spectral equivalence.
- **It selects, eliminates, ranks and prefers no candidate.**
- **It settles none of the twelve cells.** All twelve are `NOT DETERMINABLE BY
  THIS TASK`, and the repository state under all twelve is `NOT ESTABLISHED`.
- **It proposes no shared construction for `(ii)`**, which the frozen text
  forbids.
- **It does not write the next specification**, whether one task or two.
- **Its literature claims are recalled and unverified**, and zero of them cover
  the declared action.
- **A scope assessment is not a result.** Knowing what the work is makes no
  candidate more or less admissible, and brings the programme no closer to a
  phase verdict. **Its value is in preventing a commitment made blind.**
- **`C-iii` and `D0` are not unblocked.**
