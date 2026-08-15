# `P2-LATTICE-MICROSPEC-01` — two ontology readings, and whether either discriminates

**This artifact selects nothing and rules on nothing.** It prepares two PI
rulings on the ontology's own text and reports what each possible ruling would
imply for each of the four candidate kinetic operators. **The rulings are the
PI's. This artifact reports consequences, not resolutions.**

**Evidence base:** `ae3604def317667b44ea59458569ba105463fd6b`.

**The `D-pre-A` dossier is read at `27fabe17c2e56d62df4b686b57e6a654a8983520`
and is not merged.** It is unintegrated at the evidence base, so **every
citation of it below names that branch SHA and not `main`.**

**Every figure is marked DERIVED HERE, VERIFIED HERE, MEASURED or NOT
ESTABLISHED.**

---

## 0. One correction to the record, and its subject is a summary

**MEASURED at `27fabe17…`, lines 605–611 of
`derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md`:**

> **For the Wilson ledger of §3.2 the branch masses are `m + 2n` with
> `n = 0…4`, which are not equal.** For the overlap ledger of §3.4 the massless
> and cutoff-scale branches are likewise not degenerate. **So treating a Wilson
> or overlap species ledger as additional flavours of the existing derivation
> would violate that derivation's own frozen ansatz**, and the gap condition at
> line 145 would have to be re-derived rather than re-used with a substituted
> `N`.

**The operative clause is conditional and sits at lines 607–609**: *treating a
Wilson or overlap species ledger **as additional flavours** … would violate*.

**That is a result, not a contradiction.** It eliminates **one of three
candidate mappings** — route 1 of the dossier's §7.2, species-as-extra-flavours
— **for two candidates.** It does not assert that those ledgers violate
anything as they stand, and the dossier leaves the species-to-`N` mapping
`NOT ESTABLISHED` for all four candidates.

**The dossier requires no change**, and none is made here.

**The loose claim was in the execution summary, not in the dossier.** That
summary said the Wilson and overlap ledgers "violate outright" the frozen
ansatz, dropping the conditional. **The Researcher read the summary rather than
the dossier and reported an internal contradiction that does not exist; the
Reviewer raised the same objection from the same summary.** **No repair of the
dossier follows, and this artifact manufactures no Wilson or overlap
incompatibility from an unestablished mapping.**

---

## 1. Question one — what does the isotropy freeze mean?

**MEASURED, `P2-LATTICE-ONTOLOGY-01` line 94:**

> **H(4) isotropy (equal couplings on all four axes)** joins the freeze list.

**The parenthesis is the operative content, and it does not say whether "equal"
ranges over magnitudes alone or over magnitudes and signs together.** Two
readings are available and the text chooses neither:

    READING A   manifest axis symmetry of the action
    READING B   equality of couplings up to a field redefinition

### 1.1 The staggered phase structure, derived and verified

The dossier recorded at its §5.3, lines 414–424, that the staggered phases are
not symmetric under axis permutation. **This artifact re-derives that and
measures how far it goes.**

With `η_μ(x) = (−1)^{x_1 + … + x_{μ−1}}`:

**VERIFIED HERE, exhaustively over the `2⁴` block and all 23 non-trivial axis
permutations: the standard phases are manifestly symmetric under NONE of
them.** Not one of the 23 leaves `η` invariant.

**VERIFIED HERE, by exhaustive search over all `2¹⁶` sign assignments
`ε: x ↦ ±1` on the `2⁴` block: for EVERY one of the 23 permutations there
exists a redefinition `χ(x) → ε(x)χ(x)` that restores the standard phases.**
23 of 23, none failing.

**So the two readings separate exactly here, and the separation is measured
rather than asserted:** the staggered action has the axis-permutation symmetry
**up to a sign redefinition and not manifestly.**

**DERIVED HERE, and it is why no phase convention obviously escapes this:** the
staggered phases satisfy an orientation condition. **VERIFIED HERE, over all
sites and all `μ ≠ ν`, the plaquette product**

    η_μ(x) · η_ν(x + μ̂) · η_μ(x + ν̂) · η_ν(x)  =  −1

**takes the value −1 in every case.** That `−1` is what encodes the Clifford
structure in the one-component field, and it is antisymmetric in the plane it
is computed on.

**NOT ESTABLISHED: whether some other phase convention is manifestly
axis-symmetric while preserving the orientation condition.** No exhaustive
search over conventions was performed, and the plaquette condition alone was
not shown to forbid one. **This qualifier matters and is carried into every
Reading A result below.**

### 1.2 Reading A — manifest axis symmetry of the action

    naive       COMPATIBLE       DERIVED HERE: the hopping coefficient is the
                                 same on every axis and the momentum-space
                                 operator i Σ γ_μ sin p_μ is a symmetric sum
                                 over μ. The axis permutation is accompanied
                                 by the corresponding hypercubic action on the
                                 spinor index, which is part of H(4) and not a
                                 field redefinition.

    Wilson      COMPATIBLE       DERIVED HERE: both i Σ γ_μ sin p_μ and r W(p)
                                 are symmetric sums over μ with a single r, so
                                 the same argument applies unchanged.

    staggered   ELIMINATED       VERIFIED HERE: manifestly symmetric under none
                (as standardly    of the 23 non-trivial axis permutations.
                 presented)       QUALIFIER: this is a property of the standard
                                 presentation. §1.1 records as NOT ESTABLISHED
                                 whether another convention escapes it, so the
                                 elimination is of a presentation and is not
                                 shown to be of the formulation.

    overlap     COMPATIBLE       DERIVED HERE: D_ov = 1 + [i Σ γ_μ sin p_μ
                                 + (W − M_0)] / √(s + (W − M_0)²) is built from
                                 s(p) and W(p), both symmetric sums over μ, so
                                 the operator is axis-permutation symmetric by
                                 inspection.

### 1.3 Reading B — equality of couplings up to a field redefinition

    naive       COMPATIBLE       DERIVED HERE: already manifest under Reading A,
                                 so a fortiori compatible with the weaker
                                 requirement. The redefinition may be taken as
                                 the identity.

    Wilson      COMPATIBLE       DERIVED HERE: as above; the identity
                                 redefinition suffices.

    staggered   COMPATIBLE       VERIFIED HERE: for each of the 23 permutations
                                 an explicit sign redefinition ε(x) restoring
                                 the standard phases was found by exhaustive
                                 search. The redefinition is local, invertible
                                 and involutive.

    overlap     COMPATIBLE       DERIVED HERE: already manifest under Reading A,
                                 so compatible here; the identity redefinition
                                 suffices.

### 1.4 The eight results

                     READING A                         READING B
    naive        COMPATIBLE                        COMPATIBLE
    Wilson       COMPATIBLE                        COMPATIBLE
    staggered    ELIMINATED (as presented)         COMPATIBLE
    overlap      COMPATIBLE                        COMPATIBLE

**Reading A eliminates one candidate. Reading B eliminates none.**

**All four candidates were derived under both readings.** No candidate was
examined under one reading only.

### 1.5 A structural observation about Reading A, reported and not resolved

**DERIVED HERE:** "manifest symmetry of the action" is a property of how an
action is written, and a field redefinition changes how it is written without
changing the theory. **Reading A therefore discriminates between presentations
of a formulation**, and §1.1 records as `NOT ESTABLISHED` whether staggered
admits a presentation that passes it.

**This is reported as a structural fact about what Reading A measures. It is
not a recommendation to adopt Reading B**, and this artifact does not say which
reading the ontology should be given. **The PI rules on that.**

---

## 2. Question one's cost elsewhere — the Lorentz-emergence mechanism

**MEASURED, `P2-LATTICE-ONTOLOGY-01` lines 113–126.** The relevant sentence
begins at line 115:

> For a **local, translation-invariant, axis-isotropic** lattice action whose
> relevant and marginal couplings have been tuned to an `O(4)`-symmetric
> critical surface, the leading hypercubic-invariant but `O(4)`-violating
> derivative corrections commonly enter at higher derivative order, giving
> corrections of order `(E·a)²`.

and the document adds, at lines 121–126, that this is **"a mechanism to be
demonstrated for the declared fermion operator — H(4) symmetry alone does not
guarantee"** proximity to the right critical surface, exclusion of marginal
anisotropies, a common limiting velocity for all quasiparticle species, or the
absence of interaction-generated low-dimension Lorentz-breaking structures.

### 2.1 Under Reading A

**The mechanism has what it needs.** Manifest axis symmetry is strictly
stronger than what line 115 names, so the hypercubic classification of
derivative corrections goes through directly. **For any candidate that survives
Reading A, the axis-isotropy input is supplied in its strongest form.**

**The cost is that the input is supplied for three candidates rather than
four**, staggered having been eliminated by the reading itself.

### 2.2 Under Reading B

**The mechanism still has what it needs, and the argument requires one extra
step which is given here.**

**DERIVED HERE:** if the action is invariant under an axis permutation composed
with a local invertible field redefinition, then correlation functions of the
redefined fields transform covariantly under `H(4)`. The effective action's
operator basis is therefore still classified by `H(4)` representations, and the
derivative-expansion argument that leading `O(4)`-violating corrections enter at
higher derivative order is unaffected. **A symmetry realised after an
invertible local redefinition constrains the operator basis exactly as a
manifest one does.**

**The redefinition in question is `ε(x) = ±1`** — local, invertible and
involutive, as verified in §1.1.

### 2.3 A finding that applies to the reading itself, not to a candidate

**Line 115 conjoins THREE conditions: local, translation-invariant, and
axis-isotropic.** **DERIVED HERE and VERIFIED HERE: for the staggered
formulation, translation invariance holds in exactly the same "up to a field
redefinition" sense as axis isotropy.**

**VERIFIED HERE:** the standard phases are not invariant under a one-site
translation — 96 mismatches over the `2⁴` block — **and for each of the four
axes an explicit sign redefinition restoring them was found by exhaustive
search, 4 of 4.**

**So Reading A, if applied consistently to line 115's conjunction, bears on
translation invariance and not only on isotropy.** A reading strict enough to
eliminate staggered on axis symmetry would, applied to the same sentence's
neighbouring conjunct, reach the same conclusion by a second route.

**This is reported as a consequence of the reading, not as an additional
argument against a candidate.** **It is equally a fact about Reading A's
scope**: the reading's reach extends past the clause the question was framed
around. **Whether that is a reason to prefer either reading is the PI's to
judge, and this artifact does not judge it.**

---

## 3. Question two — the search

**A6 requires the search reported whether or not it finds anything.**

**MEASURED, `derivations/P2-LATTICE-ONTOLOGY-01.md` at `ae3604de`, whole-file,
case-insensitive:**

    "ultralocal"           0 occurrences
    "finite range"         0 occurrences
    "finite-range"         0 occurrences
    "nearest-neighbour"    0 occurrences
    "nearest neighbor"     0 occurrences
    "compact support"      0 occurrences
    "locality"             3 occurrences
    "local"                5 occurrences

**Every occurrence of `local*`, MEASURED with line numbers:**

    line 115   "For a local, translation-invariant, axis-isotropic ..."
               the Lorentz-emergence mechanism — §4 examines its sense
    line 321   "Obligation 4 — microscopic consistency, locality and causal
                reconstruction."
    line 325   "... a positive Hilbert space, a local observable algebra, a
                stable causal cone, cluster decomposition, and an acceptable
                analytic continuation are separate requirements ..."
    line 334   "... insensitive to microscopic orientation and locality data ..."
               Obligation 5 — about what the infrared must NOT depend on
    line 466   a question for the Discriminator, asking whether Obligations 4–5
               sufficiently price locality/causal reconstruction

**THE SEARCH RESULT: the ontology imposes NO finite-range requirement on the
microscopic action.**

**Line 325 is the closest thing to a locality requirement and it is not one of
this kind.** It requires **"a local observable algebra"** — a condition on the
reconstructed observable algebra, listed alongside a positive Hilbert space and
a stable causal cone, all under the reconstruction obligation. **A local
observable algebra is not a statement about the coupling range of the kinetic
operator**, and nothing at lines 321–328 constrains that range.

**So question two is ADDITIVE, not interpretive.** The ontology carries no
sentence to read two ways; the PI is being asked whether to add one. **The case
labels of §4 stand as `CASE A` and `CASE B`, and they are not called
readings.**

---

## 4. Question two — the two cases, eight results

    CASE A   ADD finite-range microscopic coupling as an ontology REQUIREMENT.
             A NEW physical commitment, not an interpretation of an existing
             one.
    CASE B   RETAIN the present ontology, under which no finite-range
             requirement is imposed. Not a positive commitment that infinite
             range is admissible — the absence of a requirement.

### 4.1 The range of each candidate, derived

    naive       FINITE RANGE      DERIVED HERE: the operator connects only
                                  nearest neighbours; i Σ γ_μ sin p_μ is a
                                  trigonometric polynomial of degree one, whose
                                  position-space kernel is supported on
                                  separations |x − y| ≤ 1.

    Wilson      FINITE RANGE      DERIVED HERE: i Σ γ_μ sin p_μ + m + r W(p) is
                                  again a trigonometric polynomial of degree
                                  one; the r-term adds nearest-neighbour and
                                  on-site couplings only.

    staggered   FINITE RANGE      DERIVED HERE: the one-component operator
                                  carries the phases η_μ(x) on nearest-neighbour
                                  hops and nothing longer; the phases are signs
                                  and do not extend the range.

    overlap     NOT FINITE RANGE  DERIVED at the dossier's §4.4, line 333, and
                                  re-derived here: D_ov contains
                                  [s + (W − M_0)²]^{−1/2}, and the inverse
                                  square root of a non-constant positive
                                  trigonometric polynomial is not a
                                  trigonometric polynomial, so the kernel has
                                  no finite support.

### 4.2 What the overlap's range actually is, derived and verified

**A range that is not finite is not thereby unbounded, and the distinction is
the whole content of Case B.**

**DERIVED HERE:** the kernel `[s(p) + (W(p) − M_0)²]^{−1/2}` is singular only
where `s + (W − M_0)² = 0`. Since `s = 0` only at the sixteen corners, where
`W = 2n`, **the kernel is singular exactly when `M_0 ∈ {0, 2, 4, 6, 8}`** —
which are precisely the boundaries of the dossier's species-count table.

**VERIFIED HERE** by scanning the Brillouin zone on a `48⁴` grid:

    M_0 = 0, 2, 4, 6, 8      min over the zone of s + (W − M_0)²  =  0    SINGULAR
    M_0 = 1, 3, 5, 7, 9      min over the zone of s + (W − M_0)²  =  1    strictly positive

**DERIVED HERE:** for `M_0` away from those degenerate values, the integrand is
strictly positive and smooth on the whole torus, so `sign(H_W)(p)` is analytic
in `p` there, and **a periodic analytic function has exponentially decaying
Fourier coefficients** — the position-space kernel is exponentially localised.

**VERIFIED HERE**, kernel magnitude along one axis by separation:

    M_0 = 1   3.45e-01  5.06e-02  1.17e-02  3.12e-03  9.14e-04  2.87e-04 …
    M_0 = 3   5.28e-01  3.91e-02  1.59e-02  2.55e-03  1.43e-03  2.46e-04 …

    successive ratios ≈ 0.28 and 0.32 per lattice spacing — geometric decay

**So the overlap is NOT finite-range and IS exponentially localised**, for
`M_0` away from the degenerate values. **Both halves matter**: the first is
what Case A would exclude; the second is what §5 shows the frozen mechanism
actually needs.

### 4.3 The eight results

                     CASE A — finite range REQUIRED      CASE B — present ontology
    naive        COMPATIBLE                          COMPATIBLE
    Wilson       COMPATIBLE                          COMPATIBLE
    staggered    COMPATIBLE                          COMPATIBLE
    overlap      ELIMINATED                          COMPATIBLE

**Case A eliminates one candidate. Case B eliminates none.**

**Under Case B the overlap is compatible because nothing frozen requires more
than it has**, and §5 establishes that the one frozen mechanism naming locality
is satisfied by exponential localisation.

**The Case A elimination costs a new physical commitment.** It does not follow
from anything the ontology currently carries. **A report that described it as
"ontology interpretation eliminates overlap" would be false**; the accurate
statement is that **adding finite range as a new ontology commitment would
eliminate overlap, given the established non-ultralocality result.**

---

## 5. The sense of "local" at line 115 — is it finite-range or weaker?

**MEASURED, line 115: "For a local, translation-invariant, axis-isotropic
lattice action whose relevant and marginal couplings have been tuned to an
`O(4)`-symmetric critical surface, the leading hypercubic-invariant but
`O(4)`-violating derivative corrections commonly enter at higher derivative
order, giving corrections of order `(E·a)²`."**

**DERIVED HERE: the sense is the WEAKER one.**

The argument is a derivative expansion. What "local" must supply is that the
momentum-space kernel is analytic near `p = 0`, so the action can be expanded in
powers of `p` and the corrections organised by derivative order, with the
`O(4)`-violating hypercubic invariants appearing first at the order the sentence
claims. **Analyticity of the kernel in a neighbourhood of the real torus is
equivalent to exponential decay of the position-space couplings.**

**Finite range is sufficient for this and is strictly stronger than
necessary.** A finite-range kernel is a trigonometric polynomial, hence entire;
an exponentially localised kernel is analytic in a strip, which is all the
derivative expansion requires, and supplies it with a finite radius of
convergence.

**So: line 115 uses "local" in a sense that exponential localisation
satisfies.** **DERIVED, and the consequence is stated plainly: nothing frozen
in `P2-LATTICE-ONTOLOGY-01` requires finite range in order for the
Lorentz-emergence mechanism to have what it needs.**

**This bears on the cost of Case A and is reported as such.** Adopting Case A
would eliminate a candidate; **it would not be adopted in order to protect line
115's mechanism, because that mechanism is satisfied without it** for `M_0`
away from the degenerate values. **What Case A would protect instead is a claim
about the substrate's physical reality that the ontology has not yet made.**
**Whether to make it is the PI's.**

**NOT ESTABLISHED:** whether any other frozen item depends on finite range. The
search of §3 found no finite-range requirement anywhere, so there is no
candidate dependency to check beyond line 115; **but a dependency phrased
without the words searched for would not have been found**, and no
line-by-line reading of the whole document for implicit range assumptions was
performed.

---

## 6. The verdict

**Both kinds of discrimination occur, and they are reported separately because
they put different questions to the PI.**

### 6.1 Question one — `DISCRIMINATING — INTERPRETIVE`

**The reading:** READING A, manifest axis symmetry of the action.

**The question:** what does line 94's "equal couplings on all four axes" mean?

**Candidates eliminated: staggered**, as standardly presented, and no other.

**This elimination follows from wording the ontology ALREADY carries.** No new
commitment is required; the PI would be deciding what an existing sentence
means.

**Qualifier, carried from §1.1:** the elimination is established for the
standard phase presentation. **Whether staggered admits a manifestly
axis-symmetric presentation preserving the orientation condition is NOT
ESTABLISHED.**

**Under READING B, question one eliminates no candidate.**

### 6.2 Question two — `DISCRIMINATING — ADDITIVE`

**The requirement:** finite-range microscopic coupling, adopted as a new
ontology requirement.

**The question:** should the ontology add a finite-range requirement it does
not currently carry?

**Candidates eliminated: overlap**, and no other.

**This elimination costs a new physical commitment.** §3's search establishes
that the ontology currently says nothing about finite range, so the
elimination does not follow from anything already frozen. **Under CASE B,
retaining the present ontology, question two eliminates no candidate.**

**And §5 records what the new commitment would not buy:** the one frozen
mechanism that names locality is satisfied by exponential localisation, which
the overlap has.

### 6.3 The two verdicts must not be merged

**A single "DISCRIMINATING" verdict would hand the PI one question where there
are two.**

    interpretive   what have we already committed to?
                   → staggered, under Reading A

    additive       what new commitment would we have to adopt?
                   → overlap, under Case A

**Neither elimination is a selection**, and this artifact makes none. **If both
rulings went the eliminating way, two candidates would remain and no candidate
would have been chosen** — which is a fact about the arithmetic, not a
recommendation about the rulings.

---

## 7. What this artifact does not establish

- **It does not resolve either question.** Both are the PI's.
- **It does not select, rank, recommend or prefer a candidate**, and it does
  not say which reading or case should be adopted.
- **It touches neither reflection positivity, nor the species-to-`N` mapping,
  nor the transfer matrix.** **The dossier's three uniform `NOT ESTABLISHED`
  results stand unchanged after this artifact.**
- **Neither question discovers a physical fact.** Question one asks what a
  frozen sentence means; question two asks whether to write a new one. **A
  ruling on either changes what the programme has committed to, not what is
  true.**
- **It does not establish that these are the only available discriminants**,
  nor that the four candidates are the complete set.
- **It does not unblock `C-iii` or `D0`.**

## 8. No selection, and no ruling

**No candidate is selected, ranked, recommended or preferred.** **Neither
question is resolved, and no reading or case is endorsed.**

**All four candidates are derived under both readings of question one and both
cases of question two — sixteen results, none omitted.** Where a candidate
appears under one heading and not another, it is because the result differs,
not because the candidate was examined less.

**Two statements in this artifact could be mistaken for rulings and are
not.** §1.5 records that Reading A discriminates between presentations rather
than theories, and §5 records that line 115's mechanism does not need finite
range. **Both are derived structural findings about what the readings measure
and what the frozen text requires.** **Neither says which reading or case
should be adopted, and this artifact takes no position on that.**
