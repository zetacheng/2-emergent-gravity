# Execution report — `D-pre-A2`: two ontology readings, and whether either discriminates

**Specification:** `specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md`
**Specification evidence base:** `ae3604def317667b44ea59458569ba105463fd6b`
**Branch:** `science/dpre-a2-selection-discriminants`, cut from authoritative `main` @ `ae3604de…`
**Consumed, not merged:** `science/dpre-a-kinetic-operator-dossier` @ `27fabe17c2e56d62df4b686b57e6a654a8983520`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, VERIFIED, INTENDED or NOT
ESTABLISHED.** **This report is written at commit 3 and measures nothing at
commit 4.**

**This task does not touch `main`, and it does not merge the dossier branch.**
**It selects nothing and rules on nothing.**

---

## 1. Outcome

**Both questions discriminate, by different kinds, and the kinds are reported
separately because they put different questions to the PI.**

    QUESTION ONE   DISCRIMINATING — INTERPRETIVE
                   Reading A eliminates staggered, as standardly presented.
                   Reading B eliminates none.

    QUESTION TWO   DISCRIMINATING — ADDITIVE
                   Case A eliminates overlap, at the cost of a new ontology
                   commitment. Case B eliminates none.

**MEASURED at commit 3:** 3 additions, 0 modifications; **408 of 408 paths at
the evidence base blob-identical**; validators unchanged at 324 passed, 2
deselected; all four checker invocations exit 0 with `overall: PASS` and `P7`
reading fourteen sections.

**The single most consequential derived result is in §7:** line 115's
Lorentz-emergence mechanism uses "local" in the weaker sense, and **exponential
localisation satisfies it.** **So Case A would not be adopted in order to
protect that mechanism** — it would be adopted to make a claim about the
substrate that the ontology has not yet made.

**Neither elimination is a selection.** If both rulings went the eliminating
way, two candidates would remain.

---

## 2. Refs and inputs — A1

**MEASURED, read from `origin` with `git ls-remote`:**

    refs/heads/main                            ae3604def317667b44ea59458569ba105463fd6b
    science/dpre-a-kinetic-operator-dossier    27fabe17c2e56d62df4b686b57e6a654a8983520

**The STOP condition, MEASURED:**

    git merge-base --is-ancestor 27fabe17… origin/main    exit 1

**Exit 1 means the dossier is NOT an ancestor of `main` — it is
unintegrated.** **The head block's STOP does not fire**, the evidence base is
right, and **every dossier citation in this task names `27fabe17…`, not
`main`.**

**Blob ids, MEASURED:**

    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
      @ 27fabe17    0b227206f3561144b4d5ea869390341aeefddc29
    derivations/P2-LATTICE-ONTOLOGY-01.md
      @ ae3604de    6544fb1a72eff49b4af4a1767d63405ddb87e4b8

---

## 3. The review binds to these bytes — A2

**MEASURED.**

    SHA-256 of the arriving specification      dd93e9b242bc879fee4ec0e447438cb4486021a57f37915f0bc976a15018b4d5
    SHA-256 the review records as reviewed     dd93e9b242bc879fee4ec0e447438cb4486021a57f37915f0bc976a15018b4d5

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

The review's verdict is **APPROVED FOR EXECUTION**. Its non-blocking wording
note — that where the criteria refer informally to "one of the three" outcomes,
execution follows the explicit verdict definitions — **is honoured in §8**,
which reports the two discrimination kinds separately rather than collapsing
them to one of three labels.

**The review also withdrew its own earlier objection about the dossier**, and
§4 records that this task manufactured no Wilson or overlap incompatibility
from the unestablished mapping.

---

## 4. §0a's correction, verified against the dossier's bytes — A3

**MEASURED at `27fabe17…`, `derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md`,
lines 605–611, quoted as measured:**

> **For the Wilson ledger of §3.2 the branch masses are `m + 2n` with
> `n = 0…4`, which are not equal.** For the overlap ledger of §3.4 the massless
> and cutoff-scale branches are likewise not degenerate. **So treating a Wilson
> or overlap species ledger as additional flavours of the existing derivation
> would violate that derivation's own frozen ansatz**, and the gap condition at
> line 145 would have to be re-derived rather than re-used with a substituted
> `N`.

**The line numbers, MEASURED:** the sentence spans **605–611**, and **the
operative conditional clause sits at 607–609** — *"treating a Wilson or overlap
species ledger **as additional flavours** of the existing derivation would
violate that derivation's own frozen ansatz"*.

**The clause is conditional, and it is a result.** It eliminates **one of the
three candidate mappings** the dossier's §7.2 enumerates — route 1,
species-as-extra-flavours — **for two candidates.** **It does not assert that
those ledgers violate anything as they stand**, and the dossier leaves the
species-to-`N` mapping `NOT ESTABLISHED` for all four.

**CONFIRMED: the dossier requires no change, and none was made.** Its blob is
untouched; this task did not write to the dossier branch at all.

### 4.1 Whose error it was

**The loose claim was in the execution summary, and the execution summary was
mine.** It said the Wilson and overlap ledgers "violate outright" the frozen
common-mass ansatz. **The dossier says the narrower and correct thing; my
one-paragraph summary of it dropped the conditional.**

**MEASURED consequence, as A3 requires it reported:** the Researcher read that
summary rather than the dossier and told the PI the dossier contained an
internal contradiction. **It does not.** **The Reviewer raised the same
objection from the same summary**, and has since withdrawn it — the review
committed here records the prior concern as "based on an over-reading".

**The failure mode is worth naming precisely**, because it is not the one the
governance register already carries. `G-08` covers a specification asserting
something false about its own bytes. **This is a summary of an artifact
asserting something the artifact does not say, and two downstream readers
acting on the summary without opening the artifact.** **No entry is added
here** — §5 of the specification forbids adding a register entry, and this task
adds none.

---

## 5. Question one — the eight results — A4

**MEASURED, `P2-LATTICE-ONTOLOGY-01` line 94:** "H(4) isotropy (equal couplings
on all four axes) joins the freeze list." **The parenthesis is the operative
content and it does not say whether "equal" ranges over magnitudes alone or
over magnitudes and signs.**

    READING A   manifest axis symmetry of the action
    READING B   equality of couplings up to a field redefinition

### 5.1 The measurement that separates the readings

**VERIFIED HERE, exhaustively over the `2⁴` block and all 23 non-trivial axis
permutations: the standard staggered phases `η_μ(x) = (−1)^{x_1+…+x_{μ−1}}` are
manifestly symmetric under NONE of them — 23 of 23 fail.**

**VERIFIED HERE, by exhaustive search over all `2¹⁶` sign assignments
`ε: x ↦ ±1` on that block: for EVERY one of the 23 permutations a redefinition
`χ(x) → ε(x)χ(x)` exists that restores the standard phases — 23 of 23
succeed.**

**So the two readings separate exactly at staggered, and the separation is
measured rather than asserted.**

**VERIFIED HERE, the orientation condition:** the plaquette product
`η_μ(x)·η_ν(x+μ̂)·η_μ(x+ν̂)·η_ν(x)` equals `−1` in every case, over all sites
and all `μ ≠ ν`. That `−1` encodes the Clifford structure in the one-component
field.

**NOT ESTABLISHED: whether some other phase convention is manifestly
axis-symmetric while preserving that orientation condition.** No exhaustive
search over conventions was performed, and the plaquette condition alone was
not shown to forbid one. **The qualifier is carried into every Reading A
result** — the elimination below is of a presentation, not shown to be of the
formulation.

### 5.2 The eight results

                     READING A                         READING B
    naive        COMPATIBLE                        COMPATIBLE
    Wilson       COMPATIBLE                        COMPATIBLE
    staggered    ELIMINATED (as presented)         COMPATIBLE
    overlap      COMPATIBLE                        COMPATIBLE

**Derivations, per candidate, under Reading A:**

    naive       DERIVED: the hopping coefficient is the same on every axis and
                i Σ γ_μ sin p_μ is a symmetric sum over μ. The permutation is
                accompanied by the corresponding hypercubic action on the
                spinor index, which is part of H(4), not a field redefinition.
    Wilson      DERIVED: both i Σ γ_μ sin p_μ and r W(p) are symmetric sums
                over μ with a single r; the naive argument applies unchanged.
    staggered   VERIFIED: manifestly symmetric under none of the 23.
    overlap     DERIVED: D_ov is built from s(p) and W(p), both symmetric sums
                over μ, so it is axis-permutation symmetric by inspection.

**Derivations, per candidate, under Reading B:**

    naive       DERIVED: already manifest, so a fortiori compatible; the
                identity redefinition suffices.
    Wilson      DERIVED: as above; the identity redefinition suffices.
    staggered   VERIFIED: an explicit ε(x) was found for each of the 23
                permutations; it is local, invertible and involutive.
    overlap     DERIVED: already manifest, so compatible; identity suffices.

**All four candidates were derived under both readings.** **No candidate was
examined under one reading only**, which A4 makes a STOP condition.

### 5.3 A structural observation about Reading A, reported and not resolved

**DERIVED: "manifest symmetry of the action" is a property of how an action is
written**, and a field redefinition changes how it is written without changing
the theory. **Reading A therefore discriminates between presentations of a
formulation.**

**This is reported because §8 of the specification expressly permits reporting
that a reading is structurally or textually distinguishable, and expressly
forbids concluding that it should therefore be adopted.** **I report it and
draw no conclusion.** §5.1 records as `NOT ESTABLISHED` whether staggered
admits a presentation that passes Reading A, so the observation does not even
settle the case it arose from.

---

## 6. Question one's cost elsewhere — A5

**MEASURED, `P2-LATTICE-ONTOLOGY-01` lines 113–126.** The relevant sentence
begins at line 115:

> For a **local, translation-invariant, axis-isotropic** lattice action whose
> relevant and marginal couplings have been tuned to an `O(4)`-symmetric
> critical surface, the leading hypercubic-invariant but `O(4)`-violating
> derivative corrections commonly enter at higher derivative order, giving
> corrections of order `(E·a)²`.

**MEASURED, lines 121–126**, the document's own qualifier: this is **"a
mechanism to be demonstrated for the declared fermion operator — H(4) symmetry
alone does not guarantee"** proximity to the right critical surface, exclusion
of marginal anisotropies, a common limiting velocity for all quasiparticle
species, or the absence of interaction-generated low-dimension Lorentz-breaking
structures.

**Under READING A: the mechanism has what it needs.** Manifest axis symmetry is
strictly stronger than line 115 names, so the hypercubic classification of
derivative corrections goes through directly. **The cost is that the input is
supplied for three candidates rather than four**, staggered having been
eliminated by the reading itself.

**Under READING B: the mechanism still has what it needs, and one extra step is
required and supplied.** **DERIVED:** if the action is invariant under an axis
permutation composed with a local invertible field redefinition, correlation
functions of the redefined fields transform covariantly under `H(4)`, so the
effective action's operator basis is still `H(4)`-classified and the
derivative-expansion argument is unaffected. **A symmetry realised after an
invertible local redefinition constrains the operator basis exactly as a
manifest one does.** The redefinition here is `ε(x) = ±1`, verified local,
invertible and involutive.

**Neither reading costs the mechanism what it needs.**

### 6.1 A finding about the reading's reach, not about a candidate

**Line 115 conjoins THREE conditions: local, translation-invariant, and
axis-isotropic.**

**VERIFIED HERE: for staggered, translation invariance holds in exactly the
same "up to a field redefinition" sense as axis isotropy.** The standard phases
are not invariant under a one-site translation — **96 mismatches over the `2⁴`
block** — and **for each of the four axes an explicit sign redefinition
restoring them was found by exhaustive search, 4 of 4.**

**So Reading A, applied consistently to line 115's conjunction, bears on
translation invariance and not only on isotropy.** A reading strict enough to
eliminate staggered on axis symmetry reaches the same conclusion by a second
route through the neighbouring conjunct.

**This is reported as a consequence of the reading and as a fact about its
scope.** **It is not a second argument against staggered**, and I do not treat
it as one: it is the same reading applied to the same sentence, so it is one
consequence with two expressions. **Whether the reading's reach is a reason to
resolve question one either way is the PI's to judge.**

---

## 7. Question two — the search, and what it settles — A6, A7

### 7.1 The search, reported in full including the null results

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

    115   "For a local, translation-invariant, axis-isotropic ..."
          the Lorentz-emergence mechanism — §7.3 examines its sense
    321   "Obligation 4 — microscopic consistency, locality and causal
           reconstruction."
    325   "... a positive Hilbert space, a local observable algebra, a stable
           causal cone, cluster decomposition, and an acceptable analytic
           continuation are separate requirements of this obligation."
    334   "... insensitive to microscopic orientation and locality data ..."
          Obligation 5 — about what the infrared must NOT depend on
    466   a Discriminator question asking whether Obligations 4–5 sufficiently
          price locality/causal reconstruction

**THE SEARCH RESULT: the ontology imposes NO finite-range requirement on the
microscopic action. It is silent.**

**Line 325 is the closest thing and is not a requirement of this kind.** It
requires **"a local observable algebra"** — a condition on the reconstructed
observable algebra, listed alongside a positive Hilbert space and a stable
causal cone under the reconstruction obligation. **That is not a statement
about the coupling range of the kinetic operator**, and nothing at lines
321–328 constrains that range.

**So question two is ADDITIVE and not interpretive**, and the case labels stand
as `CASE A` and `CASE B`. **They are not called readings anywhere in this
task's output.** **The PI is being asked whether to add a sentence, not how to
read one.**

### 7.2 The two cases, eight results

    CASE A   ADD finite-range microscopic coupling as an ontology REQUIREMENT.
             A NEW physical commitment.
    CASE B   RETAIN the present ontology; no finite-range requirement imposed.
             The absence of a requirement, not a commitment that infinite range
             is admissible.

                     CASE A                            CASE B
    naive        COMPATIBLE                        COMPATIBLE
    Wilson       COMPATIBLE                        COMPATIBLE
    staggered    COMPATIBLE                        COMPATIBLE
    overlap      ELIMINATED                        COMPATIBLE

**Derivations of each candidate's range:**

    naive       FINITE RANGE      DERIVED: i Σ γ_μ sin p_μ is a trigonometric
                                  polynomial of degree one, so the kernel is
                                  supported on separations ≤ 1.
    Wilson      FINITE RANGE      DERIVED: adding m + r W(p) keeps it a degree-
                                  one trigonometric polynomial; the r-term adds
                                  nearest-neighbour and on-site couplings only.
    staggered   FINITE RANGE      DERIVED: the one-component operator carries
                                  signs η_μ(x) on nearest-neighbour hops and
                                  nothing longer; signs do not extend range.
    overlap     NOT FINITE RANGE  DERIVED at the dossier's §4.4 line 333 and
                                  re-derived here: the inverse square root of a
                                  non-constant positive trigonometric
                                  polynomial is not one, so no finite support.

**Under Case B all four are compatible**, because nothing frozen requires more
than each has, and §7.3 establishes that the one frozen mechanism naming
locality is satisfied by what the overlap does have.

### 7.3 What the overlap's range actually is — the derivation that matters

**A range that is not finite is not thereby unbounded, and that distinction is
the whole content of Case B.**

**DERIVED:** the kernel `[s(p) + (W(p) − M_0)²]^{−1/2}` is singular only where
`s + (W − M_0)² = 0`. Since `s = 0` only at the sixteen corners, where
`W = 2n`, **the kernel is singular exactly when `M_0 ∈ {0,2,4,6,8}`** — which
are precisely the boundaries of the dossier's species-count table.

**VERIFIED by scanning the Brillouin zone on a `48⁴` grid:**

    M_0 = 0, 2, 4, 6, 8    min over the zone of s + (W − M_0)²  =  0    SINGULAR
    M_0 = 1, 3, 5, 7, 9    min over the zone of s + (W − M_0)²  =  1    strictly positive

**DERIVED:** away from those degenerate values the integrand is strictly
positive and smooth on the whole torus, so `sign(H_W)(p)` is analytic there,
and **a periodic analytic function has exponentially decaying Fourier
coefficients** — the position-space kernel is exponentially localised.

**VERIFIED**, kernel magnitude along one axis by separation:

    M_0 = 1   3.45e-01  5.06e-02  1.17e-02  3.12e-03  9.14e-04  2.87e-04 …
    M_0 = 3   5.28e-01  3.91e-02  1.59e-02  2.55e-03  1.43e-03  2.46e-04 …

    successive ratios ≈ 0.28 and 0.32 per lattice spacing — geometric decay

**So the overlap is NOT finite-range and IS exponentially localised**, for
`M_0` away from the degenerate values.

### 7.4 The sense of "local" at line 115 — A7

**DERIVED: line 115 uses "local" in the WEAKER sense.**

The argument there is a derivative expansion. What "local" must supply is that
the momentum-space kernel is analytic near `p = 0`, so the action can be
expanded in powers of `p` and the corrections organised by derivative order,
with the `O(4)`-violating hypercubic invariants first appearing at the order
the sentence claims. **Analyticity of the kernel in a neighbourhood of the real
torus is equivalent to exponential decay of the position-space couplings.**

**Finite range is sufficient and strictly stronger than necessary.** A
finite-range kernel is a trigonometric polynomial, hence entire; an
exponentially localised kernel is analytic in a strip, which is all the
expansion needs, and gives it a finite radius of convergence.

**Consequence, stated plainly: nothing frozen in `P2-LATTICE-ONTOLOGY-01`
requires finite range in order for the Lorentz-emergence mechanism to have what
it needs.** **So Case A would not be adopted in order to protect that
mechanism.** **What Case A would protect instead is a claim about the
substrate's physical reality that the ontology has not yet made** — which is
precisely why the specification insists it is an addition and not an
interpretation.

**NOT ESTABLISHED: whether any other frozen item depends on finite range.**
§7.1's search found no finite-range requirement under any of the terms
searched, so there is no further candidate dependency to check — **but a
dependency phrased without those words would not have been found, and no
line-by-line reading of the whole document for implicit range assumptions was
performed.**

---

## 8. The verdict — A8, unsoftened

**Both kinds occur. They are reported separately and are never merged.**

### 8.1 `DISCRIMINATING — INTERPRETIVE`

    question      one — what does line 94's "equal couplings on all four
                  axes" mean?
    reading       READING A, manifest axis symmetry of the action
    eliminated    staggered, as standardly presented — and no other
    under B       no candidate eliminated

**This elimination follows from wording the ontology ALREADY carries.** No new
commitment is required; the PI would be deciding what an existing sentence
means.

**Qualifier, carried from §5.1 and not dropped here:** the elimination is
established for the standard phase presentation. **Whether staggered admits a
manifestly axis-symmetric presentation preserving the plaquette orientation
condition is NOT ESTABLISHED.**

### 8.2 `DISCRIMINATING — ADDITIVE`

    question      two — should the ontology add a finite-range requirement it
                  does not currently carry?
    requirement   finite-range microscopic coupling, adopted as a NEW ontology
                  requirement
    eliminated    overlap — and no other
    under B       no candidate eliminated

**This elimination costs a new physical commitment.** §7.1's search establishes
that the ontology currently says nothing about finite range, so **the
elimination does not follow from anything already frozen.**

**And §7.4 records what the new commitment would not buy:** the one frozen
mechanism naming locality is satisfied by exponential localisation, which the
overlap has for `M_0` away from the degenerate values.

### 8.3 Why the two must not share a label

**A single `DISCRIMINATING` verdict would hand the PI one question where there
are two:**

    interpretive   what have we already committed to?
                   → staggered, under Reading A

    additive       what new commitment would we have to adopt?
                   → overlap, under Case A

**Neither elimination is a selection, and this task makes none.** **If both
rulings went the eliminating way, two candidates would remain and no candidate
would have been chosen.** That is arithmetic, not a recommendation about the
rulings.

**`NOT DISCRIMINATING` was a live possible outcome and is not the outcome.**
The specification anticipated it, and I did not have to reach for a third
discriminator: **neither question came up empty, and none was manufactured.**

---

## 9. No selection, no ruling — A9

### 9.1 The search

**Run over the artifact, this report and the commit messages**, for
`recommend`, `prefer`, `preferable`, `superior`, `better`, `best`, `worse`,
`worst`, `favour`/`favor`, `should be chosen`/`selected`/`adopted`,
`we choose`/`select`/`adopt`, `the right`/`correct reading`/`choice`,
`therefore adopt`, and for any sentence resolving either question.

**MEASURED in the artifact: four hits, all denials or explicit refusals to
judge.**

    line 242   "Whether that is a reason to prefer either reading is the PI's
                to judge, and this artifact does not judge it."
    line 491   "It does not select, rank, recommend or prefer a candidate"
    line 492   "...not say which reading or case should be adopted."
    line 519   "...should be adopted, and this artifact takes no position."

**MEASURED over the commit messages in this task's range: zero hits.**

**MEASURED over this report: nine hits, in three classes and none a
selection** — the search-term list quoted just above; the four artifact hits
re-quoted beneath it; and one denial, "Neither statement says which reading or
case should be adopted".

**No sentence in the artifact, this report, or any commit message selects a
candidate, ranks candidates, or resolves either question.**

### 9.2 The treatment lengths, and the asymmetry reported rather than smoothed

**MEASURED, derivation lines per candidate in the three derivation-bearing
result tables of the artifact:**

    table                naive   Wilson   staggered   overlap
    §1.2 Reading A          7       3          7         5
    §1.3 Reading B          4       2          5         3
    §4.1 range              5       4          4         7
    ------------------------------------------------------------
    TOTAL                  16       9         16        15

**MEASURED: each candidate appears in exactly 5 result-table rows** — two
readings, two cases, and the range table — **with a derivation in every one.**

**Whole-artifact mentions by name, MEASURED: naive 5, Wilson 10, staggered 16,
overlap 18.**

**The asymmetry is real and runs toward the ELIMINATED candidates, not the
surviving ones.** staggered and overlap attract more text because each is the
candidate where something happens — an elimination that has to be derived,
verified and qualified. naive and Wilson are `COMPATIBLE` in all four cells and
their derivations are correspondingly short.

**Wilson's 9 derivation lines is the lowest figure in the table, and the reason
is stated rather than left to be inferred:** its Reading A and Reading B
entries reference the naive argument — "the same argument applies unchanged" —
instead of repeating it. **That is a saving in words, not in scrutiny**, and I
report the number as measured rather than padding the entry to level the
table.

**A9's concern is that a candidate discussed at length under both readings has
been ranked without saying so.** **Here the depth follows the results**, and
the results were derived before the lengths were measured. **A reader who
distrusts that ordering has the per-cell figures above to check it against.**

### 9.3 The two statements that could be mistaken for rulings

**§5.3** records that Reading A discriminates between presentations rather than
theories. **§7.4** records that line 115's mechanism does not need finite
range.

**Both are derived structural findings** — one about what a reading measures,
one about what the frozen text requires. **§8 of the specification expressly
permits reporting that a reading is structurally or textually distinguishable
and expressly forbids concluding that it should therefore be adopted.**
**Neither statement says which reading or case should be adopted, and neither
this report nor the artifact takes a position.**

---

## 10. Scope, protected paths, gates — A10, A11, A12

**A10, MEASURED at commit 3:**

    A  derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
    A  reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
    A  specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md

    3 additions, 0 modifications

**MEASURED: no status code other than `A` appears.** **`modify:` is `[]` and
remained so** — no file existing at the evidence base was modified by any
commit in this range.

**INTENDED, base to commit 4:** 4 additions and 0 modifications, the fourth
addition being this report. **That figure is INTENDED, not MEASURED: this
report is written before the commit containing it.**

**A11, MEASURED path by path:**

    paths at the evidence base       408
    compared                         408
    blob-identical                   408
    differing                          0
    missing at head                    0

**Nothing existing changed — the comparison excludes no path**, because this
task's manifest modifies none.

**The named ones, MEASURED individually:**

    GATES.md                                  2b3bd5069414   IDENTICAL
    CONVENTIONS.md                            8badc51f38d8   IDENTICAL
    derivations/P2-LATTICE-ONTOLOGY-01.md     6544fb1a72ef   IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md          33b3a664e057   IDENTICAL

    everything under scripts/ and results/:   0 paths changed

**The ontology was consumed and not reopened. The dossier was read at
`27fabe17…` and not merged, not modified, and not written to. No register entry
was added anywhere. No script was run.**

**A12, all four checks, MEASURED at commit 3:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match their targets:
      line 1017   derivations/P2-PHASE-01_microscopic_parameter_domain.md   MATCH
      line 1040   derivations/P2-PHASE-01_input_admissibility_contract.md   MATCH

**No gate state was changed.** This task modifies no file that any gate pins,
so no re-pin is owed under Rule 19.

---

## 11. The checker — A13, MEASURED at commit 3

    base   ae3604def317667b44ea59458569ba105463fd6b
    head   2dee195b74887e2d49207d6b8c6df4639450bb26   (commit 3)

**All four invocations exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 9595002913bbb2f2d9b22bb8edd8e047a832a0ec86ae8197c10705571cb692b9
    run 1 EXCLUSIVE   exit 0   PASS   sha256 5fc09c123ea56c66ae37bca729af4f926cc41f54081166b14767ad270a5bef2e
    run 2 INCLUSIVE   exit 0   PASS   sha256 9595002913bbb2f2d9b22bb8edd8e047a832a0ec86ae8197c10705571cb692b9
    run 2 EXCLUSIVE   exit 0   PASS   sha256 5fc09c123ea56c66ae37bca729af4f926cc41f54081166b14767ad270a5bef2e

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

**`P5` and `P9` are `NOT_APPLICABLE` because this task has no merge.** **No
property returned `NOT_DECLARED`, `NOT_PARSEABLE` or `DECLARATION_CONFLICT`.**

### 11.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "2dee195b74887e2d49207d6b8c6df4639450bb26",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 11.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "2dee195b74887e2d49207d6b8c6df4639450bb26",
      "specification_paths": ["specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**; all are fixed by A13. **Neither
the config nor this specification's declarations were adjusted to make RUN 2
pass** — §8 of the specification forbids both, and neither was needed.

### 11.3 The measured RUN 1 subject set

**MEASURED: RUN 1's default selection chose exactly one specification**, and it
is the one RUN 2 names:

    specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
        stated add 4 modify 0    counted add 4 modify 0    parse OK

**`modify: []` contributes nothing to the count and parses cleanly.** The range
adds no other specification, so the default and named selections coincide and
**the two runs' outputs are byte-identical at each prospectivity reading** —
the sha256 pairs above are equal. **Both are still given verbatim below.**

### 11.4 `declared_source`, `P3` and `P7`

**MEASURED, identical in all four invocations:**

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
           DECISION_LOG.md    PASS   deleted 0   base is byte prefix of head: True
    P7   PASS   declared_source: specification   declared: []
           raw_heading_count_head 14      section_count_head 14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**

**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.** The config supplied the same set the scope block declares, so the
precedence rule resolved to `specification`.

### 11.5 RUN 1 output, verbatim

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
                "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
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
                "commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md"
                ]
              }
            ],
            "first_review_commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
            "first_work_commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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
              "commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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
            "first_commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
            "first_commit_paths": [
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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

### 11.6 RUN 2 output, verbatim

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
                "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
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
                "commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md"
                ]
              }
            ],
            "first_review_commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
            "first_work_commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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
              "commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
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
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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
            "first_commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
            "first_commit_paths": [
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
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

## 12. Validators and hygiene — A14, A15

**A14, MEASURED, `python -m pytest` from the repository root, exit status 0
both times:**

    before, at the base ae3604de     324 passed, 2 deselected
    after,  at commit 3              324 passed, 2 deselected

**Unchanged, as expected: this task adds no test.** **No change to explain.**
The "before" figure was measured in a separate worktree at the evidence base.

**A15, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   8979e83c   spec: two ontology readings, and whether either discriminates
               trailer hits 0      not amended
    commit 2   a90da041   review: pre-execution review for the selection discriminants
               trailer hits 0      not amended
    commit 3   2dee195b   derivations: two ontology readings, and what each would imply
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** No commit was written with a
hygiene violation to repair. **No force-push, no branch deletion, no history
rewrite of any kind occurred.**

---

## 13. Commits

    commit 1   8979e83c59663bfd8adac86c7e20dfcb97ac29b2   specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
    commit 2   a90da0410b2bd6151e7e3afc2bb7d68b981541aa   reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
    commit 3   2dee195b74887e2d49207d6b8c6df4639450bb26   derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md

**Commit 4's message, INTENDED:**

    report: two readings, two cases, and both kinds of discrimination

---

## 14. Did working through the readings make me want to resolve one?

**Asked by §9, and the answer is yes, to both questions and in opposite
directions. Naming which and why is the useful part.**

**On question one the pull was toward Reading B**, and it arrived with §5.3's
observation. Once I had derived that "manifest symmetry of the action" is a
property of a presentation rather than of a theory, Reading A looked like a
category error rather than a competing interpretation, and the step from "this
is what Reading A measures" to "so the ontology cannot have meant it" is one
sentence. **I did not take it, and there are two reasons beyond being forbidden
to.** First, §5.1 leaves it `NOT ESTABLISHED` whether staggered admits a
presentation passing Reading A — so the observation does not even settle its
own case. Second, an ontology declaring a *physically real* substrate may
intend exactly a statement about the substrate's presentation-independent
description, and whether that is coherent is not mine to decide.

**On question two the pull was toward Case B**, and it was stronger. §7.4
derives that line 115's mechanism does not need finite range. Having shown the
one frozen thing that names locality is satisfied without the new requirement,
**it is very tempting to conclude the requirement is unmotivated** — which
would be resolving the question. **It is not unmotivated; it is unmotivated *by
line 115*.** A substrate claimed to be physically real is a different argument
for finite range than a technical one, and the ontology's §183 makes exactly
that claim. **I derived what line 115 needs and stopped there.**

**The two pulls point at different candidates**, which is worth stating
plainly: resolving question one my way would have kept staggered, and resolving
question two my way would have kept overlap. **Neither pull was toward a
selection, and neither was acted on.**

**I confirm I resolved neither question, endorsed neither reading nor case, and
selected, ranked, recommended and preferred no candidate.** §9 gives the search
and the treatment lengths.

---

## 15. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions the specification names are
addressed.**

### 15.1 First junction — neither question discovers a physical fact

**Question one asks what a frozen sentence means. Question two asks whether to
write a new one.** **A ruling on either changes what the programme has
committed to, not what is true.** No experiment distinguishes the two readings
of line 94; no measurement decides whether the ontology should carry a
finite-range clause.

**Which of the two a candidate's elimination rests on, stated for each:**

    staggered   eliminated INTERPRETIVELY, under Reading A — by a commitment
                already made, whose meaning is being settled
    overlap     eliminated ADDITIVELY, under Case A — by a commitment made in
                order to eliminate it

**The second ordering is exactly the selection bias this line of work exists to
avoid.** A requirement adopted after its consequences for each candidate are
known is not the same object as a requirement adopted before. **Reporting that
is not avoiding it. Concealing it would guarantee it**, which is why §8.2 names
the cost in the verdict itself rather than in a footnote.

### 15.2 Second junction — are the tables symmetric?

**This task's characteristic risk is that a ruling made while its consequences
are visible can function as a selection.** The eight-result tables exist so the
PI rules with all consequences symmetric before them.

**MEASURED, and the answer is: symmetric in structure, not in length.**

**Every candidate appears in every table with a derivation** — 5 result-table
rows each, none omitted, no candidate examined under one reading or case only.
**That is the symmetry the tables were built for and it holds exactly.**

**Derivation lengths are not equal:** naive 16, Wilson 9, staggered 16, overlap
15 lines across the three derivation-bearing tables. §9.2 gives the per-cell
figures and the reasons — the eliminated candidates attract more text because
an elimination must be derived, verified and qualified, and Wilson's entries
reference naive's argument rather than repeat it.

**I report this as a limit on the symmetry claim rather than asserting the
tables are symmetric without qualification.** **A PI reading them should know
that equal structural treatment is established and equal verbal weight is
not.**

### 15.3 Third junction — what remains, and whether it should be scoped together

**Both questions discriminated, so `NOT DISCRIMINATING` is not this task's
outcome** and the "cheap discriminators are exhausted" branch does not apply as
stated.

**But the discrimination is contingent on rulings that have not been made.**
**Until the PI rules, no candidate is eliminated**, and if both rulings go the
non-eliminating way — Reading B and Case B — **all four candidates survive and
reflection positivity is again the remaining route.**

**Reflection positivity needs a transfer matrix that does not exist**, and that
construction overlaps `D-pre-B`'s Euclidean–spectral equivalence, which also
needs transfer-matrix normalisation. **The two share their principal
construction, and on that ground scoping them together is worth the PI's
consideration.**

**This task does not scope them**, and does not begin either construction.
**Naming the overlap is not scoping it.**

### 15.4 Fourth junction — the dossier's three uniform results stand unchanged

**This task did not touch reflection positivity, the species-to-`N` mapping, or
the transfer matrix.**

**MEASURED: after this task, the dossier's three uniform results are exactly as
they were:**

    reflection positivity   NOT ESTABLISHED for all four
    compatibility           6 COMPATIBLE, 0 INCONSISTENT, 10 NOT ESTABLISHED
    species-to-N mapping    NOT ESTABLISHED for all four

**Two resolved readings are not a resolved selection problem.** Even if the PI
rules both questions the eliminating way, **two candidates remain and nothing
in the repository distinguishes them** — the three results above are what would
have to distinguish them, and none of them does.

---

## 16. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, the dossier was confirmed unintegrated so the head
block's STOP did not fire, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 16.1 `OBSERVATION_METHOD_ERROR` — one finding, and it is mine, from the previous task

**My `D-pre-A` execution summary said the Wilson and overlap ledgers "violate
outright" the frozen common-mass ansatz.** **The dossier says the narrower and
correct thing**, and §4 quotes it from the committed bytes. **The summary
dropped the conditional.**

**The error was in a summary of a correct artifact, and two readers acted on
the summary without opening the artifact** — the Researcher reported a
non-existent internal contradiction to the PI, and the Reviewer raised the same
objection, since withdrawn.

**Recorded, and the shape named:** the governance register's `G-08` covers a
specification asserting something false about its own bytes. **This is a
different shape — a summary asserting something the summarised artifact does
not say.** **No register entry is added**, because §4 of the specification
forbids adding one, and the shape is reported here for whoever holds the
register.

**The corrective is not subtle and I state it as the lesson:** a summary that
drops a conditional is not a shorter true statement, it is a different and
false one.

### 16.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings

**First: line 94's isotropy freeze admits two readings and the text settles
neither.** §5 gives the eight results. **Recorded, not resolved** — the ruling
is the PI's.

**Second: the ontology is silent on finite range.** §7.1's search establishes
it under eight search terms. **The silence is the finding**, and it is what
makes question two additive rather than interpretive. **A silence is not a
permission**: Case B is the absence of a requirement, not a commitment that
infinite range is admissible, and this report does not treat it as one.

### 16.3 `ENVIRONMENT` and `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present. **No script was run**, as §4 of the specification requires.

**No defect in the repository was found by this task.**

### 16.4 What I would have specified differently

**A4 requires eight results and A6 requires eight more, but neither asks
whether the two questions interact.** They do: §6.1 finds that Reading A's
reach extends to line 115's translation-invariance conjunct, which is a
consequence of question one that lands on the same sentence question two's A7
examines. **I reported it under A5 because that is where it fits, but no
criterion asked for it**, and a task with a less discursive report contract
could have produced sixteen correct results and missed the interaction
entirely.

**I would have added a criterion asking whether either question's resolution
constrains the other's.** As it happens the answer here is no — Reading A and
Case A eliminate different candidates on independent grounds — **but that is a
result, and it was not required to be checked.**

**Nothing in the specification was unsatisfiable or ambiguous enough to require
a stop.** The one place the wording could have misled — calling question two's
branches "readings" — the specification had already corrected, and §7.1's
search confirmed the correction was the right one.

---

## 17. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A12, A14 and A15 for
commits 1–3; A13's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A10's final
base-to-commit-4 scope of 4 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A10's
final scope measured base-to-commit-4; A13-final, being RUN 2 re-run at commit
4; A14 at commit 4; A15 for commit 4; the push; the branch tip read back.

**Nothing in this report claims to measure commit 4.**

**This task does not touch `main` and does not merge the dossier branch.** The
branch is the outcome; integration is a separate task. **It selects nothing and
rules on nothing, and it does not unblock `C-iii` or `D0`.**
