# Execution report — `D-pre-B0`: what the transfer-matrix and reflection-positivity work actually is

**Specification:** `specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md`
**Specification evidence base:** `e70f55def26a96ffc325c0ae3231223e4623c76b`
**Branch:** `science/dpre-b0-tm-rp-scope`, cut from authoritative `main` @ `e70f55de…`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, VERIFIED, INTENDED or one
of §3's four dispositions.** **This report is written at commit 3 and measures
nothing at commit 4.**

**This task does not touch `main`. IT CONSTRUCTS NOTHING.**

---

## 1. Outcome

**Twelve of twelve cells are `NOT DETERMINABLE BY THIS TASK`, and that is the
assessment's principal finding**: nothing about any of the three propositions
can be settled, for any candidate, without performing construction work.
**Zero cells are `REFUTED`.**

**Only proposition `(ii)` would discriminate**, and that is derived from the
frozen text rather than assumed. **So four of the twelve cells could carry
discriminating information and eight cannot.**

**The measured overlap with `D-pre-B` is THREE of nine items — and the item
that made the two lines of work look joined is not among them.**
Transfer-matrix normalization belongs to `(i)` and to `D-pre-B`, not to the
obligation. **The shared items are measure and Jacobian factors, finite
temporal extent, and temporal boundary conditions — shared as inputs, not as
constructions.**

**RECOMMENDATION: two pieces of work, with a shared preliminary.** **Neither is
written**, and §4 forbids writing them.

**SIZE: between 7 and 11 distinct constructions**, with the basis stated and
the four-fold part irreducible while four candidates remain.

**MEASURED at commit 3:** 3 additions, 0 modifications; **426 of 426 paths at
the evidence base blob-identical**; validators unchanged at 324 passed, 2
deselected; all four checker invocations exit 0 with `overall: PASS` and `P7`
reading fourteen sections.

**No candidate is selected, eliminated, ranked or preferred.** §11 gives the
search, the treatment lengths, and why they are unequal.

---

## 2. Refs and inputs — A1

**MEASURED, `refs/heads/main` read from `origin` with `git ls-remote`:**

    refs/heads/main    e70f55def26a96ffc325c0ae3231223e4623c76b

**Matches the specification. No mismatch, no STOP.**

**Blob ids at the evidence base, MEASURED:**

    derivations/P2-LATTICE-ONTOLOGY-01.md                    6544fb1a72eff49b4af4a1767d63405ddb87e4b8
    derivations/P2-LATTICE-ROUTE-01.md                       42be438ff1a4eb1994545cbadabe85cb1f448ad8
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
                                                             0b227206f3561144b4d5ea869390341aeefddc29
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
                                                             fb2f51479bf03daeaed145a2ee48da58aab66f34
    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
                                                             5fccdda964800c93cfbedf0af3c2bbb823053bbd

---

## 3. The review binds to these bytes — A2

**Checked in the order the criterion sets: PRESENCE, then MATCH.**

    'reviewed specification SHA-256' occurrences     1
    64-hex strings in the review                     1

    SHA-256 of the arriving specification    5cad985767897d168e7f2d7a019a63c8d7970852e5ba34adc994941d9228de94
    SHA-256 the review records as reviewed   5cad985767897d168e7f2d7a019a63c8d7970852e5ba34adc994941d9228de94

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

---

## 4. The three propositions — A3

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

**The per-operator clause for `(ii)`, verbatim, MEASURED at lines 77–80:**

> for the H(4) fermion action with Grassmann measure, spin structure,
> interactions and determinant signs, this must be proved per declared
> kinetic operator, and cannot be transplanted from a bosonic Ising
> example

**CONFIRMED: this task proposes NO shared construction for `(ii)`.** §9's
recommendation is structured so that what is shared is `(i)`-level and setup
machinery. **The four `(ii)` treatments are counted separately in §10's
estimate and are named there as irreducible.**

**`(iii)`'s three levels, MEASURED at lines 86–95**, are quoted in the artifact
and matter to §10's range: level 1 is equality of the Euclidean partition
function under permitted axis relabellings; level 2 is reconstruction of a
positive transfer operator for every candidate slicing; level 3 is equivalence
of the resulting infrared observable algebras and spectra. **Line 93 records
that the Ising probe "does NOT establish levels 2–3 for the H(4) fermion
theory."**

### 4.1 Which of the three would discriminate — only `(ii)`

**DERIVED from the frozen text, not assumed.**

**Line 71 states the obligation as a condition on the ACTION:** *"the declared
H(4) action must be reflection-positive, or no quantum theory corresponds to
it."* **That is proposition `(ii)`.** A candidate whose declared action is
`REFUTED` at `(ii)` fails an obligation the programme has already frozen, and
that would be negative candidate evidence.

**`(i)` would not discriminate, and the parenthesis is why.** It reads
*"sufficient, in that finite model"* — **sufficient, not necessary.** A
candidate for which some particular finite transfer matrix fails positivity has
failed one route to discharging the obligation, not the obligation.

**`(iii)` would not discriminate against line 181 either.** It is its own
deliverable, and line 85 says *"which axis is time is not a selection
problem"*. A candidate failing `(iii)` would have a different problem.

**So the twelve cells are not twelve equally weighted results.** **Four —
`(ii)` per candidate — could carry discriminating information; eight cannot.**
**An assessment treating the three as one requirement would have obscured
that**, which is what the frozen text's "may not be conflated" guards.

---

## 5. Twelve results — A4

    proposition               naive       Wilson      staggered   overlap
    (i)   finite T positivity  NOT DET.    NOT DET.    NOT DET.    NOT DET.
    (ii)  OS reflection pos.   NOT DET.    NOT DET.    NOT DET.    NOT DET.
    (iii) axis equivalence     NOT DET.    NOT DET.    NOT DET.    NOT DET.

    ESTABLISHED IN THE REPOSITORY     0
    NOT ESTABLISHED                   0    (as the reported disposition)
    REFUTED                           0
    NOT DETERMINABLE BY THIS TASK    12

**The repository state underlying all twelve is `NOT ESTABLISHED`.** The
reported disposition is the stronger statement: not merely that nobody has done
it, but that this task cannot.

**Reasons, per proposition:**

- **`(i)`** — settling it requires constructing a transfer matrix, which §4
  forbids. **MEASURED: no transfer matrix for any of the four candidate fermion
  actions appears anywhere in the repository**, and line 93 records that the
  Ising probe does not establish levels 2–3 for the H(4) fermion theory.
- **`(ii)`** — settling it requires an OS positivity proof or refutation for
  the declared action, which §4 forbids.
- **`(iii)`** — level 2 is *"reconstruction of a positive transfer operator for
  every candidate slicing"*, the construction §4 forbids; level 3 depends on
  it.

### 5.1 No cell is `REFUTED`, and that is a finding rather than an omission

**For no candidate did this assessment derive that the declared action fails
the condition.**

**The overlap's non-ultralocality is NOT a refutation and was not upgraded to
one.** The dossier derives an obstruction to **one family of methods** and
states explicitly that this is not a demonstration that reflection positivity
fails. **An obstruction to a proof method is not a property of the action.**

**For naive, Wilson and staggered nothing in the repository bears on `(ii)` at
all**, so there was nothing that could have been upgraded.

**`REFUTED` was reachable in principle and was not reached.** **`NOT
ESTABLISHED` and `NOT DETERMINABLE BY THIS TASK` supply no negative candidate
evidence**, and twelve uniform results carry none — as the dossier already
demonstrated with four.

### 5.2 The correction in §0, verified against the landed dossier

**MEASURED, and it confirms the specification's §0 rather than taking it on
trust.**

**The dossier's reflection-positivity section, `§4` at its lines 298–352, never
cites a transfer matrix as the reason for any of the four `NOT ESTABLISHED`
results.** A search for "transfer" across that section returns nothing.

**MEASURED: the dossier's transfer-operator dependencies sit at its lines 387
and 437–445** — line 387 in the section on ontology line 180
(Euclidean-fundamental, Hamiltonian derived), and lines 437–445 in the section
on **ontology line 184's vacuum-selection rule**. **Neither is the line 181
reflection-positivity obligation.**

**So the earlier draft's attribution was the Researcher's addition, and the
correction stands as measured.** **A transfer matrix is not a logical
prerequisite for `(ii)`**: OS positivity is a condition on the Euclidean action
and measure, and the reconstruction theorem produces the Hilbert space and the
time evolution *from* it.

---

## 6. Is `(ii)` directly addressable? — A4's four-result question

**One result per candidate.**

    naive       DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix first
    Wilson      DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix first
    staggered   DIRECTLY ADDRESSABLE IN PRINCIPLE — no transfer matrix first
    overlap     NOT DETERMINABLE — the identified direct route is obstructed,
                and no alternative is identified here

**The common ground, DERIVED.** OS reflection positivity asks that
`⟨θ(F) F⟩ ≥ 0` for observables supported on one side of a reflection plane.
**Checking it requires the action, the measure and a reflection — not a Hilbert
space.**

**naive, Wilson, staggered: the action is finite-range**, as the discriminants
artifact establishes at its §4.1 — each is a trigonometric polynomial of degree
one in momentum. **A nearest-neighbour action admits the split into a piece on
each half-lattice plus a cross-term on the reflection plane**, which is the
shape a direct argument needs. **Whether the argument then succeeds is exactly
what is `NOT DETERMINABLE BY THIS TASK`.**

**overlap: the action is not ultralocal**, derived in the dossier's §4.4, so
the couplings connect every pair of time slices and the split is not available.
**This is not a statement that `(ii)` fails for overlap, and not a statement
that no direct route exists.**

**The consequence for scope: for three of the four candidates the
reflection-positivity route does not wait on the transfer matrix at all.**

**This is a statement about which mathematics applies. It is NOT a statement
that any candidate is more likely to satisfy the obligation** — §12.2 gives the
reason that inference is unavailable.

### 6.1 One thing that turned out nearly free, reported so the estimate is not overstated

**Level 1 of `(iii)` — equality of the Euclidean partition function under
permitted axis relabellings — holds for all four at the free-field level.**

For a quadratic Grassmann action `Z = det D`.

- **naive, Wilson, overlap. DERIVED:** the operators are manifestly
  axis-permutation symmetric, per the discriminants artifact §1.2, so `D` is
  conjugated by a permutation matrix and `det D` is unchanged.
- **staggered. DERIVED and VERIFIED.** The permutation is a symmetry only after
  a sign redefinition `χ(x) → ε(x)χ(x)`. Under it `D → E D E` with
  `E = diag(ε)`, so `det(EDE) = det(E)² det D = det D` since `det E = ±1`, and
  the Berezin measure contributes `det(E)^{-2} = 1` for the same reason.
  **VERIFIED on a `2⁴` lattice at `m = 0.7`: `det D` unchanged under a random
  sign redefinition, and `max |det D(axis-permuted) − det D| = 0.00e+00` over
  all 23 non-trivial permutations.**

**This does not establish `(iii)`**, whose disposition stands at `NOT
DETERMINABLE BY THIS TASK`, and **it is free-field only** — the declared
four-fermion interaction was not included, and adding it changes `Z` from a
determinant to an integral.

**It is reported because a scope assessment that omitted it would overstate the
work**, and §10's lower bound depends on it.

---

## 7. Literature claims — A5

**The repository contains no literature and I had no access to any.** **Every
claim below is recalled, not consulted, and none is verified here.** **A
recalled citation is not a source.**

**Four claims are recorded. Three carry all four fields; one does not and is
expressly not counted as a claim.**

    L1  Osterwalder & Schrader, "Axioms for Euclidean Green's functions",
        Comm. Math. Phys., 1973 and 1975 — the reconstruction theorem.
        COVERAGE: DOES NOT COVER the declared action's reflection
        positivity. It makes RP the right condition to check and
        establishes nothing about any particular lattice action.

    L2  Osterwalder & Seiler, "Gauge field theories on a lattice",
        Ann. Phys., 1978 — RP for lattice gauge theories with Wilson
        fermions.
        COVERAGE: A RESTRICTION ONLY. The declared action is an H(4)
        fermion action with a four-fermion interaction and no gauge
        field.

    L3  staggered RP — AUTHOR/WORK NOT RECALLED, SCOPE NOT RECALLED,
        COVERAGE NOT RECALLED.
        NOT COUNTED AS A CLAIM. The specification is right that "a
        standard construction exists" is the absence of a claim, and L3
        as stated is that absence. It is written down so the next task
        knows there is something to look for.

    L4  Neuberger on the overlap operator, mid-1990s; Hernández, Jansen
        and Lüscher on its locality, approximately 1998.
        COVERAGE: THE LOCALISATION PROPERTY ONLY — and the free-field
        case of it is independently DERIVED in this repository. It
        establishes nothing about reflection positivity.

**The full four-field records are in the artifact's §5.**

**Counts, MEASURED:**

    structured claims with all four fields                     3
    marked UNVERIFIED FROM THIS REPOSITORY                     4
    incomplete, not counted as a claim                         1

    COVERAGE reaching this programme's declared action         0
    COVERAGE reaching only a restriction of it, or unrelated   3

**ZERO of the recalled results cover the declared action, and that is the
number that determines how much work remains.**

**§10's estimate does not depend on any of them being right.** The claims are
unanimous in not reaching the declared action, so **if L2's coverage turned out
broader than recalled the estimate would shrink; it cannot grow.**

---

## 8. The nine `D-pre-B` items — A6

**MEASURED, `derivations/P2-LATTICE-ROUTE-01.md` lines 195–205.**

    #  item                                         classification
    1  transfer-matrix normalization                D-pre-B  ((i), not (ii))
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
    D-pre-B alone                     6
    NEITHER                           0

**Reasons for the three shared items, DERIVED:**

- **item 2** — `(ii)` is a condition on the **measure** as well as the action,
  and line 77 names the Grassmann measure explicitly. A reflection acts on the
  measure, so its geometry dependence and Jacobians are needed on both sides.
- **item 3** — RP is stated with respect to a reflection plane in a finite
  volume; the temporal extent determines which reflections exist.
- **item 4** — antiperiodic versus periodic fermion boundary conditions change
  the reflection structure and, for a Grassmann measure, the determinant signs
  — which line 78 names as part of what must be proved per operator.

**Item 1 is the one that made the two lines look joined, and it is NOT
shared.** A normalisation of `T` presupposes `T`, which is `(i)`-level
machinery, and `(ii)` does not need it. **Separating `(i)` from `(ii)` is what
moved it out of the overlap.**

**Items 5–9 are `D-pre-B` alone**: vacuum degeneracy is line 184's territory,
and `(ii)` requires no unique vacuum; an additive energy shift is invisible to
a positivity condition; contact terms, curvature-dependent normalisation and
the static-geometry restriction are features of the `Δ_EH` comparison and its
subtraction convention, not of the measure's positivity.

### 8.1 The overlap is small, and not where it was expected

**Expected: item 1, because both lines were described as waiting on a transfer
matrix. Measured: items 2, 3 and 4, and not item 1.**

**The three shared items are shared as INPUTS, not as constructions.** Each is
a specification of the setup — what the measure is, how long the lattice is,
what happens at the ends — rather than a theorem either line proves. **Two
lines needing the same setup fixed is a weaker overlap than two lines needing
the same theorem**, and §9 turns on that distinction.

---

## 9. The scoping recommendation — A7

**RECOMMENDATION: TWO pieces of work, with a shared preliminary.**

**The measured overlap does not support combining them.** Three of nine items
overlap; all three are setup specifications rather than constructions; and the
one construction-level item, transfer-matrix normalization, belongs to
`D-pre-B` and to `(i)`, not to the obligation.

**What a combined task would have to contain:**

- the shared setup — Grassmann measure with geometry dependence and Jacobians,
  finite temporal extent, temporal boundary conditions — fixed once;
- **four separate `(ii)` treatments**, one per declared kinetic operator, which
  the frozen text requires and forbids sharing;
- the transfer-matrix construction and its normalisation, for `(i)` and
  `D-pre-B`;
- the six `D-pre-B`-only items;
- the `Δ_EH` residual and the identical-subtraction-convention requirement of
  lines 209–210.

**Those parts do not constrain each other except through the shared setup.**
**A combined specification would be a container, not a synthesis.**

**What a split would duplicate: items 2, 3 and 4, and only those.**
**Duplicating a setup specification is cheap and detectable** — two tasks
fixing the same measure differently is a discrepancy a later check can find,
whereas two tasks inside one specification silently assuming different temporal
boundary conditions is not.

**NEITHER TASK IS WRITTEN HERE.** §4 forbids it, and **recommending a structure
is scoping; writing the task is the next task.**

---

## 10. The size estimate — A8

**Stated as a count of distinct constructions and which are independent, not as
an adjective.**

**Candidate-independent — ONE construction each:**

    the shared setup (items 2, 3, 4)                        1
    the transfer-matrix construction, for (i) and D-pre-B   1
    the six D-pre-B-only items, sharing that transfer
      matrix                                                1
    (iii) level 1, free-field                              ~0   §6.1 derives it

**Four-fold — ONE construction PER CANDIDATE:**

    (ii), per declared kinetic operator                     4
    (iii) levels 2-3, per candidate slicing                 4

**RANGE: between 7 and 11 distinct constructions.**

**The basis, stated rather than implied:**

- **Lower bound 7** = 3 candidate-independent + 4 for `(ii)`, assuming
  `(iii)` levels 2–3 are absorbed by the transfer-matrix construction once it
  exists, since level 2 *is* a positive transfer operator per slicing.
- **Upper bound 11** = 3 + 4 + 4, if that absorption does not happen and each
  candidate needs its own.
- **Which bound applies is `NOT DETERMINABLE BY THIS TASK`**, because it
  depends on whether one transfer-matrix construction serves every slicing — a
  question about the construction, which §4 forbids performing.

**The four-fold part is irreducible.** Line 78 requires `(ii)` per declared
kinetic operator and forbids transplanting, so **no amount of shared machinery
reduces the count of `(ii)` treatments below four while four candidates
remain.** **The programme could reduce it by ruling on the operator first** —
which is a PI decision this task does not prepare and does not recommend.

**What the estimate does not rest on: any literature claim.** §7 measures that
zero recalled results cover the declared action.

---

## 11. No selection, no preference, and effort is not evidence — A9

### 11.1 The search

**Run over the artifact, this report and the commit messages**, for
`eliminat*`, `prefer*`, `favour`/`favor*`, `rank*`, `recommend*`, `superior`,
`better`, `worse`, `best`, `worst`, `easier`, `easiest`, `tractab*`,
`more likely to satisfy`/`succeed`, `advantage`.

**MEASURED in the artifact: 11 hits, none of which presents a candidate as
favourable.** They fall into three classes: **the explicit denials**; **the
scoping recommendation itself**, which is this task's permitted deliverable and
concerns task structure rather than candidates; and **the effort-is-not-evidence
statements**, which exist to block the inference the criterion guards against.

**MEASURED over the commit messages: 4 hits**, all denials or statements of the
disposition vocabulary.

**No sentence in the artifact, this report, or any commit message selects,
ranks, prefers, or presents a candidate as more tractable in a way that reads
as favourable.**

### 11.2 The treatment lengths, unequal, and why

**MEASURED, whole-artifact mentions by name:**

    naive        7
    Wilson      12
    staggered   10
    overlap     21

**THE LENGTHS ARE UNEQUAL, AND THEY SHOULD BE.** **This is a change from
`D-pre-A`'s `A10`, where equal treatment was the expectation, and the reason is
that here the size difference is the measurement.**

**overlap's 21 is the largest, and the reason is that it is the one candidate
whose `(ii)` assessment differs.** §6 reports three candidates as directly
addressable and overlap as `NOT DETERMINABLE`, and that asymmetric result needs
the non-ultralocality derivation, the obstruction's limits, and the explicit
statement that an obstruction is not a refutation. **The extra text is the
qualification, not the finding.**

**Note what direction the asymmetry runs.** **overlap receives the most text
and is the candidate whose route is least clear.** If length were tracking
favour it would be tracking it backwards. **It is tracking neither: it is
tracking how much had to be said to avoid overstating a result.**

**Wilson's 12 is second, and carries L2** — the one recalled literature claim
whose subject is a specific candidate — plus the repository's own Wilson
assertion at ontology lines 82–84. **naive's 7 is smallest because its
assessment is the shortest to state**, sharing every structural feature with
Wilson and needing no separate qualification.

**None of these lengths is evidence about any candidate**, and §12.2 says why
the inference from either direction is unavailable.

---

## 12. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions are addressed.**

### 12.1 First junction — a scope assessment is not a result

**Knowing what the work is does not make any candidate more or less
admissible.** **Nothing here brings the programme closer to a phase verdict**,
and nothing here settles any of the twelve cells.

**The assessment's value is in preventing a commitment made blind.** Before it,
the size of the reflection-positivity work was unknown and the overlap with
`D-pre-B` was assumed to run through the transfer matrix. **After it, the
overlap is measured at three of nine items, the transfer matrix is measured out
of the reflection-positivity path for three candidates, and the irreducible
four-fold part is counted.** **That is a better-posed question, not an
answer.**

### 12.2 Second junction — effort is not evidence

**This is the junction most likely to be misread, and the artifact states it
where the size estimate is rather than only in a closing section.**

**If the construction turns out smaller for one candidate, that is a fact about
the mathematics available, not about the physics.**

**A candidate for which a proof route is available is not thereby more likely
to satisfy the obligation** — an available route can end in a refutation, and
`REFUTED` is the outcome that would eliminate. **A candidate for which the
identified route is obstructed has not thereby failed** — the dossier says
exactly this about the overlap, and neither the artifact nor this report says
more.

**Tractability is a fact about the mathematics available to us. Admissibility
is a fact about the theory.** **Reporting the first as though it bore on the
second would be easiest to commit here**, where the whole deliverable is an
estimate of effort.

### 12.3 Third junction — even a completed result may not discriminate

**Four `NOT ESTABLISHED` results carry no information, and the dossier already
demonstrated that.** **Twelve carry none either**, which is what §5's count
records.

**Whether this route discriminates depends on `REFUTED` being reachable for at
least one candidate** — **the declared action failing the condition, not a
theorem that no proof could exist.**

**This task reports whether that is determinable, not whether it is true.**
**MEASURED: it is not determinable here, for any candidate.** So the programme
could complete the reflection-positivity work in full and find four
`ESTABLISHED` results, which would discriminate exactly as little as four `NOT
ESTABLISHED` results do.

**That possibility is not remote and is not priced into the estimate.** §10
counts constructions, not outcomes.

### 12.4 Fourth junction — the literature claims are a different kind of claim

**The repository contains no literature and I had no access to any.** **Every
claim that a standard result exists is `UNVERIFIED FROM THIS REPOSITORY`** — a
different kind of claim from the derivations this programme has been producing,
and **one no criterion in this specification can check.**

**MEASURED: 4 claims made, all marked unverified; 3 structured with all four
fields; 1 incomplete and not counted as a claim; and ZERO with `COVERAGE`
reaching the declared action.**

**A scope estimate resting on unverified coverage claims is only as good as
those claims.** **Verifying them is work this task cannot do and the next one
must.**

**Here the dependency is unusually weak and that is worth stating precisely:**
because all four claims fail to reach the declared action, **§10's estimate
holds whether or not they are correctly recalled.** **A future task that finds
L2's coverage broader than recalled would shrink the estimate; none of them
could enlarge it.** **But that is a property of this particular set of claims,
not a general safety margin**, and a later assessment recalling a result that
*did* appear to cover the declared action would be in a materially weaker
position.

---

## 13. Did assessing the work make me want to start it, or to select a candidate?

**Asked by §9, and the previous task reported this pull as its strongest. It
was strongest again, and it changed shape.**

**On starting the work: yes, and more concretely than before.** §6 establishes
that for three candidates `(ii)` is directly addressable at the Euclidean
level, and §6.1 derives level 1 of `(iii)` in a few lines. **Having derived one
piece, the next piece looks like the same kind of thing** — the reflection
split for a nearest-neighbour action is a page of algebra away, and I could see
its shape while writing §6. **§4 forbids attempting it, and I did not.**

**The specific danger here was different from the previous task's.** There the
pull was to *scope* the transfer matrix — to propose a structure. **Here the
pull was to take one step of the actual proof**, because §6's argument stops
one step short of it, and the step is small. **A small step into forbidden work
is still forbidden work, and it would have arrived unreviewed inside a scope
assessment.**

**On selecting a candidate: no, but I had to watch a specific inference.** §6
splits three-to-one and §6.1 needed an extra argument for staggered only.
**Two asymmetric results in adjacent sections invite a reading in which the
candidates are sorting themselves.** They are not: one asymmetry is about
coupling range and the other about phase conventions, they point at different
candidates, and neither bears on admissibility.

**A third pull, and it is the one I would flag to the PI as the standing
risk.** **The estimate's lower bound, 7, is reachable only if `(iii)` levels
2–3 are absorbed by the transfer-matrix construction.** I do not know that they
are, and I wanted to assume it because the tighter range is the more useful
deliverable. **§10 records it as `NOT DETERMINABLE BY THIS TASK` instead, and
the range stays wide.**

**I confirm I constructed nothing, attempted no reflection-positivity proof,
proposed no shared construction for `(ii)`, wrote neither next specification,
selected, eliminated, ranked and preferred no candidate, ruled on neither
`D-pre-A2` question, added no ontology requirement, added no register entry,
and modified no existing file.**

---

## 14. Scope, protected paths, gates — A10, A11, A12

**A10, MEASURED at commit 3:**

    A  derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md
    A  reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
    A  specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md

    3 additions, 0 modifications

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.**

**INTENDED, base to commit 4:** 4 additions and 0 modifications, the fourth
being this report. **INTENDED, not MEASURED.**

**A11, MEASURED path by path:**

    paths at the evidence base      426
    compared                        426
    blob-identical                  426
    differing                         0
    missing at head                   0

**The named ones, MEASURED individually — all IDENTICAL:**

    GATES.md
    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-LATTICE-ROUTE-01.md
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
    derivations/P2-DEFERRED-ITEMS.md
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
    docs/GOVERNANCE-DEBT.md

    everything under scripts/, tests/, results/:   0 paths changed

**Both lattice artifacts and all three microspec artifacts were read and not
modified. Neither register was touched. No register entry was added.**

**A12, all four invariants, MEASURED at commit 3:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match:  line 1017 MATCH,  line 1040 MATCH

**No gate state changed and no pinned file was modified**, so no re-pin is owed
under Rule 19.

---

## 15. The checker — A13, MEASURED at commit 3

    base   e70f55def26a96ffc325c0ae3231223e4623c76b
    head   8c6042126e5919c0006a818cdf184f3f6c8d185a   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   sha256 7233f867ab61146a425fcfc12ff6c252e4c0ce442ef4b83b60f991cf5c1731fc
    run 1 EXCLUSIVE   exit 0   PASS   sha256 309aab658eb6099142cfaab9fd0e87ffbd7cdd2cd0e7b096d275a0fe8f61af22
    run 2 INCLUSIVE   exit 0   PASS   sha256 7233f867ab61146a425fcfc12ff6c252e4c0ce442ef4b83b60f991cf5c1731fc
    run 2 EXCLUSIVE   exit 0   PASS   sha256 309aab658eb6099142cfaab9fd0e87ffbd7cdd2cd0e7b096d275a0fe8f61af22

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

### 15.1 What `RUN 1` did

**MEASURED: `RUN 1` completed and selected one specification**, as A13
predicts:

    specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md   stated 4 / 0   counted 4 / 0   parse OK

**MEASURED: `RUN 1` and `RUN 2` are byte-identical at each prospectivity
reading**, the default and named selections coinciding.

**The `C3` multi-specification residual does not arise in a single-branch
range** and remains unregistered.

### 15.2 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "head": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 15.3 RUN 2 config, verbatim — stop-governing

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "head": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
      "specification_paths": ["specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make RUN 2 pass** — §8 forbids
both, and neither was touched.

### 15.4 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
           DECISION_LOG.md   PASS   deleted 0   base is byte prefix of head: True
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**
**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property.

### 15.5 RUN 2 output, verbatim, INCLUSIVE reading

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "a2009f858fd5d11019273da3f1e2a6272f0726e9",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6197575576fb1b17523dd98709a0dda969d4d3b2",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md"
                ]
              }
            ],
            "first_review_commit": "6197575576fb1b17523dd98709a0dda969d4d3b2",
            "first_work_commit": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "a2009f858fd5d11019273da3f1e2a6272f0726e9",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6197575576fb1b17523dd98709a0dda969d4d3b2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8c6042126e5919c0006a818cdf184f3f6c8d185a",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "a2009f858fd5d11019273da3f1e2a6272f0726e9",
            "first_commit_paths": [
              "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 16. Validators, hygiene, commits — A14, A15

**A14, MEASURED, `python -m pytest` from the repository root, exit status 0
both times:**

    before, at the base e70f55de     324 passed, 2 deselected
    after,  at commit 3              324 passed, 2 deselected

**Unchanged, as expected: this task adds no test.**

**A15, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   a2009f85   spec: what the transfer-matrix and reflection-positivity work actually is
               trailer hits 0      not amended
    commit 2   61975755   review: pre-execution review for the TM and RP scope assessment
               trailer hits 0      not amended
    commit 3   8c604212   derivations: what the transfer-matrix and reflection-positivity work actually is
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite of any kind.**

**Commits:**

    commit 1   a2009f858fd5d11019273da3f1e2a6272f0726e9   specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
    commit 2   6197575576fb1b17523dd98709a0dda969d4d3b2   reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
    commit 3   8c6042126e5919c0006a818cdf184f3f6c8d185a   derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md

**Commit 4's message, INTENDED:**

    report: the transfer-matrix and reflection-positivity scope, measured

---

## 17. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, no literature claim was made without its four
fields, no `REFUTED` was reported without a derivation because none was
reported at all, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 1 finding

### 17.1 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught before commit

**Two cross-references in the artifact were written from memory and were
wrong.** I cited the manifest-symmetry derivations as the discriminants
artifact's §5.2 — §5.2 is a section of the *dossier*, not of that artifact —
and the finite-range result as the dossier's §4.1, when it is the
*discriminants artifact's* §4.1; the dossier's §4.1 is naive reflection
positivity.

**Both were corrected before commit 3**, and **every remaining cross-reference
was then re-verified against the landed files**: the discriminants artifact's
§1.2 is "Reading A — manifest axis symmetry of the action", its §4.1 is "The
range of each candidate, derived", and the dossier's §4.4 is the overlap
obstruction. **All three targets exist and say what the artifact claims.**

**This is `G-11`'s shape once removed.** The entry records that a hand-written
probe contradicting a committed check is likelier wrong than the check; **here
nothing contradicted anything, because a wrong section number is silently
plausible.** **The only thing that catches it is checking, and the reason I
checked is that three artifacts now share a `P2-LATTICE-MICROSPEC-01_` prefix
and near-identical section numbering.**

**Recorded as a standing hazard rather than a one-off**: the microspec family
has grown to four artifacts with parallel structures, and a cross-reference to
"§4.1" is ambiguous between them without the filename.

### 17.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one finding, carried

**Every literature claim this task makes is unverifiable from this
repository**, §12.4. **No criterion in the specification can check them**, and
the protocol — four fields, precise enough to find, explicitly marked
unverified — is a way of making them checkable later rather than a way of
checking them.

**This is a new kind of evidence for this programme.** Every prior artifact in
this line rested on derivations performed and verified in the container.
**These four claims rest on recall**, and §7 says so in the artifact itself.

**Reported and not registered.** §4 forbids adding a register entry, and the
governance register is frozen.

### 17.3 `SPECIFICATION_DEFECT`, `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or about
its own bytes.** **§5.2 verified §0's central correction against the landed
dossier rather than accepting it**, and it holds as stated.

**The specification's §10 records something worth noting as a positive: it
carries a `RETRACTED` entry stating that an earlier draft's misattribution "was
left standing here under a MEASURED label — the label an executor is obliged to
treat as an author-verified repository fact", and that "a correction that does
not reach the verification record has not been made."** **MEASURED: the
verification record in the issued specification carries the correction.**

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No defect in the repository was found by this task.**

### 17.4 What I would have specified differently

**A4 offers four dispositions and two of them overlap in a way the criterion
does not resolve.** `NOT ESTABLISHED` means "nobody has done it here" and `NOT
DETERMINABLE BY THIS TASK` means "settling it requires the forbidden
construction". **For all twelve cells both are true.** I reported the second
because it carries more information, and said the first underlies it — **but
the criterion asks for "one of", and a reader comparing this report to the
dossier's four `NOT ESTABLISHED` results may take the different words for
different states.**

**I would have had the disposition set be explicitly layered** — a repository
state and a determinability state, reported as a pair — **which is what §5
reports anyway.** As written, a future task could report the same twelve cells
under the other label without contradicting this one.

**Nothing in the specification was unsatisfiable.** The one place where a
criterion's expectation and the outcome diverged — A4 expecting `NOT
DETERMINABLE BY THIS TASK` to be "common" where it turned out universal — is a
result, not a defect.

---

## 18. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A12, A14 and A15 for
commits 1–3; A13's four invocations with both configs and the output; commits
1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A10's final
base-to-commit-4 scope of 4 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A10's
final scope measured base-to-commit-4; A13-final, being RUN 2 re-run at commit
4; A14 at commit 4; A15 for commit 4; the push; the branch tip read back.

**Nothing in this report claims to measure commit 4.**

**This task does not touch `main`.** The branch is the outcome; integration is
a separate task. **It constructs nothing, and it does not unblock `C-iii` or
`D0`.**
