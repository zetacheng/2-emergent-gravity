# Execution report — integrate the transfer-matrix and reflection-positivity scope assessment, and land it

**Specification:** `specs/2026-08-15T2142Z_integrate-dpre-b0.md`
**Specification evidence base:** `e70f55def26a96ffc325c0ae3231223e4623c76b`
**Branch:** `science/integrate-dpre-b0`, cut from authoritative `main` @ `e70f55de…`
**Source merged:** `science/dpre-b0-tm-rp-scope` @ `fbb37c572fb04c4ab7324835e97c205e348e662d`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, VERIFIED or INTENDED.**
**This report is written at commit 3, the merge commit, and measures nothing at
commit 4.**

---

## 1. Outcome

**One merge, clean. Nothing auto-merged. Nothing modified.**

**The four load-bearing conclusions were each RE-DERIVED from the artifact and
the frozen text, not read from the source report.** §7 of the specification
makes that the landing precondition, and all four are below:

    A5   twelve cells NOT DETERMINABLE, zero REFUTED   — counted from the table
    A6   only (ii) can discriminate: 4 cells vs 8      — re-derived from lines 71, 74, 85
    A7   overlap 3 of 9, shared as INPUTS              — re-derived item by item
    A8   7 to 11 constructions, lower bound not firm   — re-derived with its basis

**MEASURED at commit 3:** conflict list empty; merge-base the evidence base;
**6 additions and 0 modifications**; all four arriving paths blob-identical to
the source tip; **426 of 426 paths at the evidence base blob-identical**;
validators unchanged at 324 passed, 2 deselected; all four checker invocations
exit 0 with `overall: PASS` and `P7` reading fourteen sections.

**A5's separation of vocabularies is the measurement most easily got wrong, and
it came out exactly as the specification anticipated:** the table gives twelve
and zero; the whole-file greps give **17 and 5**. **Those are not cell counts.**

**No candidate is eliminated, preferred or ranked. No construction was begun.**

---

## 2. Refs — A1

**MEASURED, read from `origin` with `git ls-remote`:**

    refs/heads/main                    e70f55def26a96ffc325c0ae3231223e4623c76b
    science/dpre-b0-tm-rp-scope        fbb37c572fb04c4ab7324835e97c205e348e662d

**Both match the specification. No mismatch, no STOP.**

    git merge-base --is-ancestor fbb37c57… origin/main      exit 1

**Non-zero, as expected — the source is not an ancestor of `main`.**

---

## 3. The review binds to these bytes — A2

**Checked in the order the criterion sets: PRESENCE, then MATCH.**

    'reviewed specification SHA-256' occurrences     1
    64-hex strings in the review                     1

    SHA-256 of the arriving specification    f9f7573ecd029a1ad00c6d5f17b74950f166befe58b5f7944023e02066cb3f22
    SHA-256 the review records as reviewed   f9f7573ecd029a1ad00c6d5f17b74950f166befe58b5f7944023e02066cb3f22

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

---

## 4. Merge parentage and the absence of conflict — A3, A4

**Three values, separately derived. MEASURED:**

    parent 1          fec6a3fad03bd4b07686437a23cee025f7f98805   this task's review commit
    parent 2          fbb37c572fb04c4ab7324835e97c205e348e662d   the source tip
    merge-base(1,2)   e70f55def26a96ffc325c0ae3231223e4623c76b   the evidence base

**MEASURED: commit 1 is an ancestor of parent 1** — `--is-ancestor` exit 0.
Specification precedes review, which precedes the merge, per Rule 15's timing
clause.

**A4, MEASURED: the conflict list is empty.** `git diff --diff-filter=U`
returns nothing; the index carries **0** unmerged entries; **no `Auto-merging`
line was emitted.**

---

## 5. Which merge case — A13, established BEFORE the blob comparisons

**MEASURED, before any blob comparison was interpreted:**

    merge-base(HEAD, source)           e70f55def26a96ffc325c0ae3231223e4623c76b
    authoritative main tip             e70f55def26a96ffc325c0ae3231223e4623c76b
    commits on main after the base     0

**The merge-base IS `main`. No commit on `main` could have touched an arriving
path**, and **all four arriving paths are additions**, so a path that did not
exist at the base cannot have a second side.

**THE CASE IS ONE-SIDED. A merged blob equal to the source side is the CORRECT
outcome**, not evidence that a side was lost.

**The blob comparisons, now interpretable. MEASURED:**

    derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md      ed11f8680dc5   IDENTICAL
    reports/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md         476aabcb7d53   IDENTICAL
    reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md e1d608072321   IDENTICAL
    specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md           4f113d835b34   IDENTICAL

**Four of four identical. Nothing arriving by merge was edited.**

---

## 6. The twelve cells — A5, counted from the table

**MEASURED by reading the artifact's §3.1, §3.2 and §3.3 row by row.**

    proposition                        naive       Wilson      staggered   overlap
    (i)   finite transfer-matrix pos.  NOT DET.    NOT DET.    NOT DET.    NOT DET.
    (ii)  OS reflection positivity     NOT DET.    NOT DET.    NOT DET.    NOT DET.
    (iii) axis equivalence             NOT DET.    NOT DET.    NOT DET.    NOT DET.

**Disposition counts, MEASURED from the table:**

    ESTABLISHED IN THE REPOSITORY     0
    NOT ESTABLISHED                   0    (as the reported disposition)
    REFUTED                           0
    NOT DETERMINABLE BY THIS TASK    12

**Twelve and zero, as expected.**

### 6.1 The whole-file grep figures, stated beside the table counts

**MEASURED over the arriving artifact, for the TWO cell-disposition strings:**

    grep 'NOT DETERMINABLE BY THIS TASK'    17     table count: 12
    grep 'REFUTED'                           5     table count:  0

**These are not cell counts, and the discrepancy is structural rather than an
error.** The artifact **defines its own vocabulary**: the disposition list in
its §3 preamble contributes hits, the §3.4 count block contributes hits, and
prose explaining why no cell is `REFUTED` contributes five hits for a string
that labels zero cells.

**`REFUTED` is the clearest case: five occurrences, zero cells.** Every
occurrence is a definition or a statement that the disposition was *not*
reached. **A reader taking the grep count for a cell count would read five
refutations off a table that contains none.**

**A count taken by grep over a document that defines its own vocabulary is not
a count of the thing defined.** Both figures are on the record so the
difference is anticipated rather than discovered later.

### 6.2 The literature label, reported separately

**MEASURED:**

    grep 'UNVERIFIED FROM THIS REPOSITORY'     6

**This is a literature-evidence label, not a cell disposition**, and it belongs
with §10's counts rather than with the twelve cells. **It is reported here only
to state that it is not part of the table**, and the source task's own figures
— four claims, three structured, zero with covering `COVERAGE` — are in §10.

### 6.3 What the twelve results mean, bounded

**They are a determinate finding about what `B0` could settle WITHIN ITS
ADMITTED EVIDENCE AND METHODS, and nothing more.**

**They are NOT a theorem that no route could settle them.** `B0` leaves
literature verification undone, and **a theorem whose hypotheses were shown to
cover the declared action could in principle settle a cell by applicability
rather than by construction.**

**They are NOT evidence about any candidate.** Twelve uniform results carry no
discriminating information, exactly as four uniform `NOT ESTABLISHED` results
did in the dossier.

---

## 7. Only `(ii)` can discriminate — A6, re-derived from the ontology

**Re-derived from `derivations/P2-LATTICE-ONTOLOGY-01.md` AS MEASURED AT THE
HEAD. The source report was not consulted for this derivation.**

**Line 71, quoted as measured:**

>   the declared H(4) action must be reflection-positive, or no quantum

**Line 74, quoted as measured:**

>   matrix (sufficient, in that finite model, to define

**Line 85, quoted as measured:**

> - **"Which axis is time" is not a selection problem — but the

**The derivation:**

**Line 71 states the obligation as a condition on the ACTION.** The action
being reflection-positive is proposition `(ii)` — Osterwalder–Schrader
reflection positivity of the Euclidean measure and action. **A candidate whose
declared action is `REFUTED` at `(ii)` fails an obligation already frozen, and
that is negative candidate evidence.**

**Line 74 describes the finite transfer matrix as *sufficient, in that finite
model*.** **DERIVED: sufficiency is not necessity.** A candidate for which some
particular finite transfer matrix fails positivity has lost one route to
discharging the obligation, not the obligation. **So `(i)` REFUTED supplies no
negative candidate evidence.**

**Line 85 states that which axis is time *is not a selection problem*.**
`(iii)` is its own three-level deliverable. **A candidate failing `(iii)` would
have a different problem, not a reflection-positivity problem.**

**COUNTS, MEASURED against the twelve-cell table:**

    cells that could carry discriminating information    4    ((ii) × four candidates)
    cells that structurally cannot                       8    ((i) and (iii) × four)

### 7.1 What this conclusion does and does not determine

**It determines the potential OPERATOR-SELECTION VALUE of the coming work.**

**It does NOT determine whether the frozen reflection-positivity obligation is
worth discharging.** **Line 181 freezes it**, and **discharging it is required
whether or not it eliminates anything.**

**Eliminating a candidate is a possible outcome of the work, not its success
criterion.** **A report framing the coming work as a selection tool would
misstate why it must be done** — and would make a frozen obligation contingent
on its selection value, which nothing in the ontology supports.

---

## 8. The overlap with `D-pre-B` — A7, re-derived item by item

**The nine items, MEASURED from `derivations/P2-LATTICE-ROUTE-01.md` lines
201–205 at the head:** transfer-matrix normalization; geometry-dependent
measure and Jacobian factors; finite temporal extent; temporal boundary
conditions; vacuum degeneracy; additive energy normalization; contact terms;
curvature-dependent normalization; and the restriction relating a static
geometry to a Euclidean four-geometry.

**Nine results, re-derived:**

    #  item                                    classification   shared as
    1  transfer-matrix normalization           D-pre-B          —
    2  geometry-dependent measure and          BOTH             INPUT
       Jacobian factors
    3  finite temporal extent                  BOTH             INPUT
    4  temporal boundary conditions            BOTH             INPUT
    5  vacuum degeneracy                       D-pre-B          —
    6  additive energy normalization           D-pre-B          —
    7  contact terms                           D-pre-B          —
    8  curvature-dependent normalization       D-pre-B          —
    9  static geometry ↔ Euclidean             D-pre-B          —
       four-geometry restriction

    required by BOTH lines of work    3    (items 2, 3, 4)
    D-pre-B alone                     6
    NEITHER                           0

**Re-derivation of the three shared items:**

- **item 2** — `(ii)` is a condition on the **measure** as well as the action;
  ontology line 77 names the Grassmann measure explicitly. A reflection acts on
  the measure, so its geometry dependence and Jacobians are needed on both
  sides.
- **item 3** — reflection positivity is stated with respect to a reflection
  plane in a finite volume; the temporal extent determines which reflections
  exist.
- **item 4** — periodic versus antiperiodic fermion boundary conditions change
  the reflection structure and, for a Grassmann measure, the determinant signs,
  which line 78 names as part of what must be proved per operator.

### 8.1 Transfer-matrix normalisation is NOT among the shared items — CONFIRMED

**This is the single result that reversed both the Researcher's and the
Reviewer's expectation, and it is confirmed rather than repeated.**

**DERIVED: a normalisation of `T` presupposes `T`.** Constructing `T` is
`(i)`-level machinery. **`(ii)` does not need it** — §7's re-derivation
establishes that the obligation is a condition on the Euclidean action and
measure, and the reconstruction theorem produces the Hilbert space and time
evolution *from* it.

**So item 1 belongs to `D-pre-B` and to `(i)`, and not to the obligation.**
**Once `(i)` is separated from `(ii)`, the item that looked like the joint is
not one.**

### 8.2 Shared as INPUTS, not as CONSTRUCTIONS — re-derived

**Each of items 2, 3 and 4 is a specification of the setup — what the measure
is, how long the lattice is, what happens at the ends — rather than a theorem
either line proves.**

**Neither line reuses the other's operator construction, proof machinery or
theorem.** They agree on what the objects are and then prove different things
about them.

**Two lines needing the same setup fixed is weaker overlap than two needing the
same theorem**, and **that distinction is what turns one large task into two
with a preliminary.** **The Reviewer's caution is met exactly here**: none of
the three is reported as a shared construction, because none reuses the same
theorem or operator construction.

---

## 9. The seven-to-eleven estimate — A8, re-derived with its basis

**Candidate-independent — ONE construction each:**

    the shared setup (items 2, 3, 4)                        1
    the transfer-matrix construction, for (i) and D-pre-B   1
    the six D-pre-B-only items, sharing that transfer
      matrix                                                1

**Four-fold — ONE construction PER CANDIDATE:**

    (ii), per declared kinetic operator                     4
    (iii) levels 2-3, per candidate slicing                 4

**RANGE: between 7 and 11 distinct constructions.**

    lower bound  7 = 3 + 4, assuming (iii) levels 2-3 are absorbed by the
                   transfer-matrix construction once it exists, since level 2
                   IS a positive transfer operator per slicing
    upper bound 11 = 3 + 4 + 4, if that absorption does not happen

**CONFIRMED: whether `(iii)` levels 2–3 are absorbed by the transfer-matrix
construction is itself `NOT DETERMINABLE BY THIS TASK`** — it depends on
whether one construction serves every slicing, which is a question about the
construction, and §4 forbids performing it.

**THE RANGE STAYS WIDE BECAUSE OF THAT.** The lower bound is not firm, and the
estimate is **a scope estimate, not an established construction count.**

**The four-fold part is irreducible.** Ontology line 78 requires `(ii)` per
declared kinetic operator and forbids transplanting, so **no amount of shared
machinery reduces the count of `(ii)` treatments below four while four
candidates remain.**

### 9.1 The estimate counts constructions, not outcomes — stated where the reader meets it

**Four `ESTABLISHED` results would discriminate exactly as little as four `NOT
ESTABLISHED` results.**

**A completed programme of this work may leave the selection problem exactly
where it is**, and **that possibility is not priced into the seven-to-eleven
figure.** The figure counts what would have to be built, not what building it
would reveal.

---

## 10. The staggered determinant identity, recomputed — A9

**Recomputed on the ACTUAL operator, not on a random matrix.**

    OPERATOR    staggered one-component Dirac operator,
                D = m·1 + (1/2) Σ_μ η_μ(x) [shift_{+μ} − shift_{−μ}],  m = 0.7
    EXTENT      L = 2, a 2⁴ lattice, 16 sites, periodic
    CONVENTION  neighbours taken with modular wrap, which is safe HERE because
                L = 2 is EVEN and η_μ is periodic under even shifts. The hazard
                D-pre-A3 recorded concerns the PLAQUETTE PHASE at ODD extent,
                where x + L ≡ x flips signs that are not part of the local
                structure. This is a determinant of the operator on a finite
                periodic lattice, not a plaquette, and the extent is even.

**MEASURED:**

    det(D)                                       +0.003323293056960
    det(E)                                       ±1  (both branches exercised)
    det(E)²                                      +1
    |det(E D E) − det(E)² det(D)|                0.00e+00
    |det(E D E) − det(D)|                        0.00e+00

**Both branches of `det(E)` were exercised deliberately.** A first draw
happened to give `det(E) = +1`, which under-exercises the `det(E)² = 1` step;
**the identity was re-checked with an odd number of negative entries, giving
`det(E) = −1`, and with several other sign patterns:**

    even # of −1  →  det(E) = +1  →  |det(EDE) − det(D)| = 0.00e+00
    odd  # of −1  →  det(E) = −1  →  |det(EDE) − det(D)| = 0.00e+00
    7 negatives   →  det(E) = −1  →  |det(EDE) − det(D)| = 0.00e+00
    8 negatives   →  det(E) = +1  →  |det(EDE) − det(D)| = 0.00e+00

**The axis-permutation measurement, MEASURED:**

    max |det D(permuted) − det D| over all 23 non-trivial permutations
                                                 0.00e+00

**Expected `0.00e+00`, measured `0.00e+00`.**

---

## 11. Literature claims, counted — A10

**MEASURED from the arriving artifact's §5:**

    claims recorded                                            4
    claims with all four fields                                 3    (L1, L2, L4)
    marked UNVERIFIED FROM THIS REPOSITORY                      4
    COVERAGE reaching this programme's declared action          0
    COVERAGE reaching only a restriction of it, or unrelated    3

**The last is ZERO, as expected.**

**The one claim expressly not counted as a claim is L3**, on reflection
positivity for staggered fermions. **The source records `AUTHOR/WORK NOT
RECALLED`, `SCOPE NOT RECALLED` and `COVERAGE NOT RECALLED`**, and does not
count it **because "a standard construction exists" is not a claim but the
absence of one.** It is written down so a later task knows there is something
to look for, and **nothing is built on it.**

**The estimate's robustness to these claims is a property of THIS claim set,
not a general margin.** All four fail to reach the declared action, so §9's
count holds whether or not they are correctly recalled — **a broader L2 could
only shrink the estimate, never enlarge it.** **A future assessment recalling a
result that did appear to cover the declared action would be in a materially
weaker position.**

---

## 12. The dossier does not attribute its RP results to a missing transfer matrix — A11, re-verified

**Searched at the head, not taken from the source report.**

**MEASURED: the dossier's reflection-positivity section is `§4`, spanning lines
298 to 361. Transfer-matrix mentions inside it: ZERO.**

**Every `transfer` mention in the whole dossier, MEASURED with line numbers:**

    line 271   "...does not transfer to the..."          — unrelated; about a
                                                           licence not transferring
    line 387   "...transfer operator; whether one is
                constructible..."                        — §5.1, ONTOLOGY LINE 180
    line 437   "...reconstructed transfer matrix..."     — §5.4, ONTOLOGY LINE 184
    line 441   "...presupposes a reconstructed transfer" — §5.4, ONTOLOGY LINE 184
    line 445   "...without the transfer operator."       — §5.4, ONTOLOGY LINE 184

**Section attribution VERIFIED by locating each line within the dossier's
subsection headings:** line 387 falls under `### 5.1 Line 180 —
Euclidean-fundamental formulation, Hamiltonian derived`; lines 437–445 fall
under `### 5.4 Line 184 — the vacuum selection rule`.

**Neither is the line 181 reflection-positivity obligation.** **MEASURED: the
dossier's `§5.2 Line 181 — reflection positivity as obligation` contains no
transfer mention either.**

**The source task's correction stands, re-verified.** **A transfer matrix is
not a logical prerequisite for `(ii)`**, and the earlier attribution was an
addition rather than a reading.

---

## 13. Scope, protected paths, gates — A12, A14, A15, A16

**A12, MEASURED at commit 3, the merge commit:**

    6 additions, 0 modifications

**INTENDED, base to commit 4:** 7 additions and 0 modifications, the seventh
being this report. **INTENDED, not MEASURED: this report is written before the
commit containing it.**

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.**

**The arriving counts, stated separately AND with the statement the criterion
asks for:**

    arriving ADDITIONS       4
    arriving MODIFICATIONS   0
    arriving PATHS           4

    THEY COINCIDE, at four.

**`D-pre-A3`'s executor observed that a guard should stay visible when it does
nothing, and this is that case.** The two counts differ only when a
modification arrives; none does here, so the distinction does no work — **and
saying so is what keeps it from being quietly dropped by a later task in which
it would.**

**A14, MEASURED path by path:**

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
    derivations/P2-DEFERRED-ITEMS.md          (the deferred register)
    docs/BRANCHING_POLICY.md                  (the superseded-branch register)
    docs/GOVERNANCE-DEBT.md                   (the governance-debt register)

    everything under scripts/, tests/, results/:   0 paths changed

**No register entry was added anywhere**, including for §3b's cross-reference
hazard.

**A15, all four invariants, MEASURED at commit 3:**

    ^## P2- count                14
    P2-PHASE-01                  Status: PROPOSED
    first prerequisite           Prerequisite state: SATISFIED
    second prerequisite          Prerequisite state: SATISFIED
    both pins match:             line 1017 MATCH,  line 1040 MATCH

**A16, MEASURED before the advance. Six separate exit statuses, all 1 — not
merged:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

---

## 14. The checker — A17, MEASURED at commit 3

    base   e70f55def26a96ffc325c0ae3231223e4623c76b
    head   0f12104b367e3b451dd1f953d023217fc42702b0   (commit 3, the merge commit)

    run 1 INCLUSIVE   exit 0   PASS   sha256 1e98892f042416163d2681b34646d265ba7138022a51101ede4fd20b6fcf86ba
    run 1 EXCLUSIVE   exit 0   PASS   sha256 6f58ea6ccae55fc379c7f9a94a7041e7fd1122c2341059c83ce182c0227474e6
    run 2 INCLUSIVE   exit 0   PASS   sha256 b5af1eca14c3392226f41feeab7db904bbca3eb7d7acffa9147b94286c728ed2
    run 2 EXCLUSIVE   exit 0   PASS   sha256 6ff1f751a28892e6cb36ba618a6b55a9e8d7aae512ee03b5dc357cc67d7f3e88

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**Nine of nine in every invocation.**

### 14.1 What `RUN 1` did

**MEASURED: `RUN 1` completed and selected two specifications**, as A17
predicts:

    specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md   stated 4 / 0   counted 4 / 0   parse OK
    specs/2026-08-15T2142Z_integrate-dpre-b0.md     stated 7 / 0   counted 7 / 0   parse OK

**MEASURED: `P3` resolved to a single declared set, `['DECISION_LOG.md']`, with
`declared_source: specification`** — the checker reporting that the two subject
specifications agree, since a difference is what `_declarations_from_specs`
raises on.

**The `C3` multi-specification conflict did not arise**, and the reason is that
the two declarations agree rather than that there are only two. **That remains
the correct diagnosis**: the trigger is a difference between declarations, not
their number. **The residual is unchanged and unregistered.**

### 14.2 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "head": "0f12104b367e3b451dd1f953d023217fc42702b0",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 14.3 RUN 2 config, verbatim — stop-governing

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "head": "0f12104b367e3b451dd1f953d023217fc42702b0",
      "specification_paths": ["specs/2026-08-15T2142Z_integrate-dpre-b0.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make RUN 2 pass** — §9 forbids
both, and neither was touched.

### 14.4 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**
**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property.

### 14.5 RUN 2 output, verbatim, INCLUSIVE reading

    {
      "base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "0f12104b367e3b451dd1f953d023217fc42702b0",
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
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md",
                "reports/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md",
                "reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md",
                "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T2142Z_integrate-dpre-b0.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
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
                "commit": "e6752931426fbbe0ed3ed9cd280f4e97f7ebfa35",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "fec6a3fad03bd4b07686437a23cee025f7f98805",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "0f12104b367e3b451dd1f953d023217fc42702b0",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md"
                ]
              }
            ],
            "first_review_commit": "fec6a3fad03bd4b07686437a23cee025f7f98805",
            "first_work_commit": "0f12104b367e3b451dd1f953d023217fc42702b0",
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
              "specs/2026-08-15T2142Z_integrate-dpre-b0.md"
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "0f12104b367e3b451dd1f953d023217fc42702b0",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "e70f55def26a96ffc325c0ae3231223e4623c76b",
              "recomputed_parent_1": "fec6a3fad03bd4b07686437a23cee025f7f98805",
              "recomputed_parent_2": "fbb37c572fb04c4ab7324835e97c205e348e662d",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "e6752931426fbbe0ed3ed9cd280f4e97f7ebfa35",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "fec6a3fad03bd4b07686437a23cee025f7f98805",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "fbb37c572fb04c4ab7324835e97c205e348e662d",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0f12104b367e3b451dd1f953d023217fc42702b0",
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
              "specs/2026-08-15T2142Z_integrate-dpre-b0.md"
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
            "first_commit": "e6752931426fbbe0ed3ed9cd280f4e97f7ebfa35",
            "first_commit_paths": [
              "specs/2026-08-15T2142Z_integrate-dpre-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T2142Z_integrate-dpre-b0.md",
              "reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T2142Z_integrate-dpre-b0.md",
              "specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
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

## 15. Validators, hygiene, commits — A18, A19

**A18, MEASURED, `python -m pytest` from the repository root, exit status 0:**

    at commit 3      324 passed, 2 deselected

**Unchanged from the base, as expected: neither the source nor this task adds a
test.**

**A19, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   e6752931   spec: integrate the transfer-matrix and reflection-positivity scope, and land it
               trailer hits 0      not amended
    commit 2   fec6a3fa   review: pre-execution review for the TM and RP scope integration
               trailer hits 0      not amended
    commit 3   0f12104b   merge: integrate the transfer-matrix and reflection-positivity scope assessment
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite of any kind.**

**Commits:**

    commit 1   e6752931426fbbe0ed3ed9cd280f4e97f7ebfa35   specs/2026-08-15T2142Z_integrate-dpre-b0.md
    commit 2   fec6a3fad03bd4b07686437a23cee025f7f98805   reviews/chatgpt/2026-08-15T2142Z_integrate-dpre-b0.md
    commit 3   0f12104b367e3b451dd1f953d023217fc42702b0   --no-ff merge of fbb37c57…

**Commit 4's message, INTENDED:**

    report: the transfer-matrix and reflection-positivity scope lands on main

---

## 16. The cross-reference hazard — §3b, reported and not registered

**MEASURED at the head: four artifacts now share the
`derivations/P2-LATTICE-MICROSPEC-01_*` prefix** — the kinetic-operator
dossier, the selection discriminants, the plaquette provenance, and the
arriving scope assessment.

**All four carry a `§4.1`, and several carry a `§5.2`.** **A citation of the
form `§4.1` without a filename is ambiguous across four landed artifacts.**

**The source task wrote two such cross-references from memory and both pointed
at the wrong file** — the manifest-symmetry derivation cited as the
discriminants artifact's `§5.2` when `§5.2` is a *dossier* section, and the
finite-range result cited as the dossier's `§4.1` when it is the
*discriminants*' `§4.1`. **It caught both before committing and re-verified
every remaining reference.**

**This is adjacent to `G-08` and is a different shape.** `G-08` covers an
artifact asserting something false about its own bytes. **This is a cross-file
reference that cannot be self-checked because the namespace collides** — the
citing artifact is internally consistent, and only opening the cited file
reveals the error.

**Reported. NOT REGISTERED** — §4 forbids adding an entry, and the governance
register is frozen at eleven.

---

## 17. Did re-deriving the scope make me want to begin the work?

**Asked by §10, and the source task reported this as its strongest pull and
named the remaining step small. It was weaker here, and the reason is worth
recording.**

**Re-deriving is a different activity from assessing.** The source task was
building the argument and could see where it stopped; **this task was checking
an argument that already exists, and checking has a natural terminus that
building does not.** Each of A5 through A8 ended in a comparison — table count
against grep count, quoted line against derived claim, item against
classification — and a comparison that comes out equal does not invite a next
step.

**The one place the pull returned was A9.** Recomputing `det(EDE) = det(D)` on
the actual operator put a working staggered Dirac matrix in front of me, and
**a transfer matrix for that operator is a slicing of the same object.** **§4
forbids constructing one, and I did not**, but the distance is one function.

**A second, subtler pull: the temptation to tighten the range.** §9's lower
bound of 7 rests on an absorption question that is undetermined, and having
re-derived everything else to a definite answer, **leaving one input
undetermined feels like incomplete work rather than accurate work.** It is
accurate work. **The range stays 7 to 11.**

**A third, and it is the one I would flag.** §7's re-derivation makes it clean
that eight of twelve cells structurally cannot discriminate. **That invites the
thought that the coming work is mostly not worth doing** — which §7.1 answers,
and which would have been a serious misreading: **line 181 freezes the
obligation, and discharging it is required whether or not it eliminates
anything.** **A task that re-derived the selection value and then quietly let
it stand in for the obligation's value would have inverted the ontology.**

**I confirm I began no construction — not the reflection split, not a transfer
matrix, not a normalisation — selected, eliminated, ranked and preferred no
candidate, wrote no next specification, did not decide whether the
reflection-positivity work is one task or four, did not upgrade the overlap
obstruction to a refutation, added no register entry, and modified no file.**

---

## 18. Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 18.1 First junction — what twelve `NOT DETERMINABLE` results are, and are not

**They are a determinate finding about what `B0` could settle WITHIN ITS
ADMITTED EVIDENCE AND METHODS, and nothing more.**

**They are NOT a theorem that no route could settle them.** `B0` left
literature verification undone; a theorem whose hypotheses were shown to cover
the declared action could settle a cell by applicability rather than by
construction. **No scope assessment can establish a claim about all future
methods**, and this one does not.

**They are NOT evidence about any candidate.** **Zero `REFUTED` means no
negative candidate evidence exists**, and twelve uniform results carry no
discriminating information — as four uniform results already did in the
dossier.

**Both statements are placed in §6.3, where a reader meets the table**, and not
only here.

### 18.2 Second junction — a frozen obligation, not a selection tool

**Reflection positivity is frozen at ontology line 181, and discharging it is
required whether or not it eliminates anything.**

**Framing the coming work as a selection tool would misstate why it must be
done.** §7 re-derives that only `(ii)` could carry discriminating information —
**that bears on the work's selection VALUE, not on whether the obligation must
be discharged.**

**The two are separable and this report keeps them separate.** A candidate
could satisfy `(ii)`, contribute nothing to selection, and the work would still
have been necessary.

### 18.3 Third junction — the estimate counts constructions, not outcomes

**Four `ESTABLISHED` results would discriminate exactly as little as four `NOT
ESTABLISHED` results.**

**A completed programme of this work may leave the selection problem exactly
where it is.** §9.1 states this beside the seven-to-eleven figure, which is
where a reader meets it.

**The estimate prices what would have to be built. It does not price what
building it would reveal**, and nothing in it should be read as an expectation
that effort converts into discrimination.

### 18.4 Fourth junction — zero literature claims cover the declared action

**MEASURED: four claims recorded, all `UNVERIFIED FROM THIS REPOSITORY`, and
ZERO with `COVERAGE` reaching the declared action.**

**The estimate's robustness to their accuracy is a property of this claim set,
not a general margin.** Because none of them reaches the declared action, §9's
count holds whether or not they are correctly recalled.

**Verifying them is work no task so far has been able to do.** The repository
contains no literature and no executor in this line has had access to any.
**This integration does not close that gap** — it lands the claims marked as
unverified, which is the honest disposition and not a repair.

---

## 19. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, the conflict list was empty, `RUN 1` completed,
and no acceptance criterion failed. **A5, A6, A7 and A8 were each re-derived
and reported**, which §7 of the specification makes the landing precondition.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 19.1 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught within the task

**A9's first determinant check drew a sign pattern giving `det(E) = +1`**,
which satisfies the identity trivially and **under-exercises the `det(E)² = 1`
step the identity turns on.** A check that passes for the wrong reason is not a
check.

**Re-run with an odd number of negative entries — `det(E) = −1` — and with
further patterns, and the identity holds in every case**, §10. **Both branches
are now on the record.**

**Recorded because the criterion asked for `det(E)² det(D)` and a `+1` draw
never distinguishes it from `det(E) det(D)`.**

### 19.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings, both carried

**First: the cross-reference namespace collision**, §16. Four microspec
artifacts with parallel section numbering, and cross-file citations that cannot
be self-checked. **Reported, not registered.**

**Second: every literature claim landing here is unverifiable from this
repository**, §18.4. **No criterion in this specification can check them**, and
the four-field protocol makes them checkable later rather than checking them.
**Reported, not registered.**

### 19.3 `SPECIFICATION_DEFECT`, `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or about
its own bytes.** Its pre-issue record anticipated the grep-versus-table
discrepancy at 17, 5 and 6, and **MEASURED: 17, 5 and 6 is what the greps
return.** **The record's own figures were correct and its warning was
warranted.**

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No defect in the repository was found by this task.**

### 19.4 What I would have specified differently

**A5 requires the grep figures reported beside the table counts, and that is
right — but it does not ask for the two to be reconciled.** I reported both and
explained the gap in §6.1, and **the explanation is the part that makes the
pair useful**: without it, a reader has two numbers and no account of why they
differ.

**I would have had A5 require the reconciliation and not only the pair.** The
`REFUTED` case makes the point sharply — **five occurrences, zero cells, and
every occurrence a definition or a denial** — and a report that gave "5" beside
"0" without saying that all five are denials would have left the more alarming
number unexplained.

**Nothing in the specification was unsatisfiable.** The four re-derivations
were each performable from the artifact and the frozen text without consulting
the source report, which is what A6 requires explicitly and what I did for all
four.

---

## 20. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A16, A18 and A19 for
commits 1–3; A17's four invocations with both configs and the output; commits
1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A12's final
base-to-commit-4 scope of 7 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A12's
final scope measured base-to-commit-4; A17-final, being RUN 2 re-run at commit
4 before the landing; A15 and A16 re-run after the advance; A19 for commit 4;
the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; the source tip unchanged; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
