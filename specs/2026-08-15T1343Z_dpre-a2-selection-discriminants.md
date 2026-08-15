# Task specification — `D-pre-A2`: two ontology readings, and whether either discriminates

Specification evidence base: `ae3604def317667b44ea59458569ba105463fd6b`

    Branch to create   science/dpre-a2-selection-discriminants
    Cut from           authoritative main @ ae3604de…

    Consumed, not merged:
      science/dpre-a-kinetic-operator-dossier
      27fabe17…  — the D-pre-A dossier, NOT YET INTEGRATED

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**IT SELECTS NOTHING AND RULES ON NOTHING.** It prepares two PI rulings
on the ontology's own text, and **reports what each possible ruling would
imply for all four candidates.**

---

> ## THE DOSSIER IS NOT ON `main`
>
> **`D-pre-A`'s branch `27fabe17…` is unintegrated.** This task **reads
> it at that SHA** and **does not merge it.** **Every dossier citation
> must name the branch SHA**, not `main`.
>
> **If the dossier lands before this task runs, STOP and report** — the
> evidence base would then be wrong and the citations would need
> rewriting.

## 0. What the dossier established, and what it left open

**`D-pre-A` derived four species ledgers, each by its own formulation's
method**, and found **no candidate inconsistent with any frozen item**.
**It also found that none of the natural discriminators discriminates:**

    reflection positivity   NOT ESTABLISHED for all four
    compatibility           6 COMPATIBLE, 0 INCONSISTENT,
                            10 NOT ESTABLISHED
    species-to-N mapping    NOT ESTABLISHED for all four

**That is the dossier's most valuable result: it prevented a premature
selection.** **Selecting now would almost certainly select on
computational continuity, mathematical tidiness, or species count** —
**and the PI's ruling excludes the third explicitly and requires
"independent physical and structural grounds" for the others.**

**Two questions in the dossier were RECORDED, NOT RESOLVED**, and
**neither requires the transfer matrix that reflection positivity
needs.** **They are this task's subject.**

## 0a. One correction to the record, and it is the Researcher's

**The `D-pre-A` execution summary said the Wilson and overlap ledgers
"violate outright" the frozen common-mass ansatz.** **The dossier itself
says something narrower and correct** — at lines 605–611 of
`derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md` at
`27fabe17…`:

> treating a Wilson or overlap species ledger **as additional flavours**
> of the existing derivation would violate that derivation's own frozen
> ansatz

**That is conditional, and it is a result: it eliminates one of three
candidate mappings for two candidates.** **It is not a claim that those
ledgers violate anything as they stand.**

**The Researcher read the summary, did not check the dossier, and told
the PI the dossier contained an internal contradiction. It does not.**
**The Reviewer raised the same objection from the same summary.**
**Report this correction; the dossier needs no change.**

**Confirm the quoted sentence is present at those lines**, and **report
its line numbers as measured.**

## 1. Question one — what does the isotropy freeze mean?

**`P2-LATTICE-ONTOLOGY-01` line 94 freezes:**

> **H(4) isotropy (equal couplings on all four axes)**

**The dossier derived, at §5.3**, that the staggered phases
`η_μ(x) = (−1)^{x_1+…+x_{μ−1}}` are **not symmetric under permutation of
the axes** — `η_1 ≡ 1` while `η_4` depends on three coordinates — and
that **the couplings' MAGNITUDES are equal on all four axes while their
sign patterns single out an axis ordering.**

**Two readings are available and the text does not choose:**

    READING A   manifest axis symmetry of the action
    READING B   equality of couplings up to a field redefinition

**Produce, for EACH reading, the consequence for EACH of the four
candidates.** **Eight results.** **Do not stop at staggered** — a table
that examines one candidate under both readings and the others under
neither has ranked them.

**Then report what each reading costs elsewhere.** **Line 115–126 makes
axis-isotropy load-bearing for the emergence of Lorentz invariance**: an
`O(4)`-symmetric critical surface is reached by a *local,
translation-invariant, axis-isotropic* lattice action, and the document
states this is **a mechanism to be demonstrated for the declared fermion
operator**. **State, per reading, whether that mechanism still has what
it needs.**

**Do not recommend a reading.** **The PI rules on what the ontology
means. This task reports what each meaning implies.**

## 2. Question two — is a non-ultralocal action admissible for a physically real lattice?

**The dossier derived, at §4.4, that the free overlap operator is not
ultralocal** — the inverse square root of a non-constant trigonometric
polynomial is not a polynomial, so the operator has no finite range.

**In ordinary lattice field theory this is a technical inconvenience,
because the lattice is a regulator and only the continuum limit is
claimed to be physical.** **`P2-LATTICE-ONTOLOGY-01` does not take that
view.** §183 freezes the lattice as **ontologically dynamical,
operationally static** — **a physically real substrate.**

**So the question is not the usual one.** **A physically real substrate
whose couplings extend without bound is a different claim from a
calculational tool that is non-ultralocal.**

**Report:**

- **whether `P2-LATTICE-ONTOLOGY-01` says anything about locality or
  finite range as a requirement.** **Search it and report the search**,
  including if the answer is that it says nothing;
- **the consequence for each of the four candidates** — **four results,
  not one** — under **each of two CASES.**

**The two cases are not two readings, and calling them readings would
misdescribe what the PI is being asked.**

    CASE A   ADD finite-range microscopic coupling as an ontology
             REQUIREMENT. This is a NEW physical commitment, not an
             interpretation of an existing one.
    CASE B   RETAIN the present ontology, under which no finite-range
             requirement is imposed. This is not a positive commitment
             that infinite range is admissible; it is the absence of a
             requirement.

**Question one offers two readings of a sentence that exists.** **Question
two, if the search comes back silent, offers a choice between adding a
sentence and not adding one.** **An earlier version of this section
called both "readings", which would have let a result be reported as
"ontology interpretation eliminates overlap" when the accurate statement
is "adding finite range as a new ontology commitment would eliminate
overlap, given the established non-ultralocality result."**

**If the search finds that the ontology DOES impose locality in a
finite-range sense, say so — then question two becomes interpretive like
question one, and the case labels must be restated accordingly.**
- **whether anything already frozen depends on finite range.** **Line
  115's Lorentz-emergence mechanism names locality explicitly** —
  **check whether it uses locality in the finite-range sense or a weaker
  one, and report which.**

**If the ontology is silent, say it is silent.** **A silence is a
finding and is the honest answer if it is the true one** — it means the
PI is being asked to add a requirement, not to interpret one.

## 3. What this task must answer at the end

**Does either question, resolved either way, eliminate any candidate?**

**Report one of the following, and where `DISCRIMINATING` applies,
report WHICH KIND — both kinds may apply at once:**

    DISCRIMINATING — INTERPRETIVE
        elimination follows from one reasonable reading of wording the
        ontology ALREADY carries. Name the reading, the question, and
        every candidate eliminated.

    DISCRIMINATING — ADDITIVE
        elimination follows only if a NEW ontology requirement is
        adopted. Name the requirement, the question, and every
        candidate eliminated. State plainly that the elimination costs
        a new physical commitment.

    NOT DISCRIMINATING
        neither question eliminates any candidate under any reading or
        case. Say so plainly.

    NOT ESTABLISHED
        the consequences could not be derived.

**The two kinds of discrimination must not share a label.** **They put
different questions to the PI**: *what have we already committed to?*
and *what new commitment would we have to adopt?* **A verdict that
merges them hands the PI one question where there are two.**

**`NOT DISCRIMINATING` is an acceptable and useful outcome.** **It means
the cheap discriminators are exhausted and the transfer-matrix
construction is the remaining route** — **which is a finding worth having
before committing to that construction, and is why this task runs
first.**

**Do not manufacture a third discriminator if these two come up
empty.** **Report the emptiness.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge, **and do not merge the
  `D-pre-A` branch.**
- **DO NOT SELECT A CANDIDATE**, rank, recommend, or prefer.
- **Do not rule on either question.** **Both are the PI's.**
- **Do not construct a transfer matrix**, and do not attempt reflection
  positivity for any candidate.
- **Do not modify the dossier.** It is read at `27fabe17…` and is
  correct as written; §0a records a correction to a SUMMARY of it, not to
  it.
- **Do not modify `derivations/P2-LATTICE-ONTOLOGY-01.md`.** It is
  consumed, not reopened.
- **Do not compute anything new about the exploratory kernel**, and do
  not run any script.
- **Do not modify `GATES.md`** or any gate state.
- **Do not add a register entry anywhere.**
- **Do not claim this task unblocks `C-iii` or `D0`.**

## 5. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`ae3604def317667b44ea59458569ba105463fd6b`, **and
`science/dpre-a-kinetic-operator-dossier` resolves to `27fabe17…` and is
NOT an ancestor of `main`.** **Report both, and report the exit status of
the ancestry check.** **If the dossier has landed, STOP** per the block
at the head. Report the Git blob ids of the dossier and of
`P2-LATTICE-ONTOLOGY-01.md`.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** Report both digests equal.

**A3 — §0a's correction verified.** **Quote the dossier's sentence at
lines 605–611 as measured**, report its line numbers, **and confirm the
dossier requires no change.** **Report that the loose claim was in the
execution summary and that the Researcher and the Reviewer both repeated
it.**

**A4 — Question one: eight results.** Two readings × four candidates.
**Report all eight**, each with its derivation. **A result reported for
one candidate and not another under the same reading is a STOP.**

**A5 — Question one's cost elsewhere.** Per reading, **whether the
Lorentz-emergence mechanism at lines 115–126 still has what it needs.**
**Report the lines you relied on.**

**A6 — Question two: the search, then eight results.** **Report the
search over `P2-LATTICE-ONTOLOGY-01` for any locality or finite-range
requirement, including a null result.** Then **two CASES × four
candidates**, each with its derivation.

**Report explicitly whether the search made question two interpretive or
additive**, and **label the cases accordingly.** **A result reported
under the label "reading" when the case is additive fails this
criterion.**

**A7 — Question two's dependency check.** **Whether line 115's use of
"local" is finite-range or weaker**, with the lines quoted.

**A8 — The §3 verdict**, one of the three, **with its named
consequences.** **If `DISCRIMINATING`, name the reading, the question and
every candidate eliminated.** **If `NOT DISCRIMINATING`, say so without
softening it.**

**A9 — No selection, no ruling.** **Search the artifact, the report and
the commit messages for any sentence that selects a candidate, ranks
candidates, or resolves either question.** **Report the search and the
finding.** **Report the treatment length per candidate**, as `D-pre-A`'s
`A10` required — **a table that discusses one candidate at length under
both readings has ranked them without saying so.**

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: ae3604def317667b44ea59458569ba105463fd6b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
      reports/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md
      specs/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**A11 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`,
`P2-LATTICE-ONTOLOGY-01.md`, `P2-DEFERRED-ITEMS.md` and everything under
`scripts/` and `results/`.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A13 — The checker over this task's own range**, base `ae3604de…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.** **Report the subject set RUN 1 actually selected.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A14 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected.** **A change is a finding.**

**A15 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
    commit 4  reports/2026-08-XXT{HHMM}Z_dpre-a2-selection-discriminants.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Committed report — measured at commit 3:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A10's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A13-final; A14 at commit 4; A15 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **Neither question discovers a physical fact.** **Question
one asks what a frozen sentence means. Question two, if the ontology is
silent, asks whether to write a new one.** **A ruling on either changes
what the programme has committed to, not what is true.**

**Say that, and say which of the two a candidate's elimination rests on**
— **a candidate eliminated interpretively is eliminated by a commitment
already made; a candidate eliminated additively is eliminated by a
commitment made in order to eliminate it**, and **that ordering is
exactly the selection bias this line of work exists to avoid.**
**Reporting it is not avoiding it, but concealing it would guarantee
it.**

**Second, and it is this task's characteristic risk.** **A ruling made
while its consequences for each candidate are visible is a ruling that
can function as a selection.** **The eight-result tables exist so the PI
rules on the ontology with all consequences symmetric before them.**
**Say whether the tables are in fact symmetric** — equal derivation depth
per candidate per reading — **and report the per-candidate treatment
lengths.**

**Third.** **`NOT DISCRIMINATING` would leave reflection positivity as
the remaining route, and reflection positivity needs a transfer matrix
that does not exist.** **That construction overlaps `D-pre-B`'s
Euclidean–spectral equivalence, which also needs transfer-matrix
normalisation.** **Say whether the two should be scoped together** —
**and do not scope them here.**

**Fourth.** **This task does not touch reflection positivity, the
species-to-`N` mapping, or the transfer matrix.** **The dossier's three
uniform `NOT ESTABLISHED` results stand unchanged after it.** **Say
that**, so a reader does not take two resolved readings for a resolved
selection problem.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  discriminants artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not resolve either question**, and do not indicate which reading
  you would resolve them to. **Reporting that one reading is textually
  better supported IS a finding and is permitted; reporting that it
  should therefore be adopted is not.**
- **Do not adjust the config or this specification's declarations to make
  RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's quoted sentence with its measured line numbers**, and the
  confirmation the dossier needs no change;
- **A4's eight results with derivations**;
- **A5's per-reading cost to the Lorentz-emergence mechanism**;
- **A6's search, including a null result if that is what it is**, and
  its eight results;
- **A7's finding on the sense of "local" at line 115**;
- **A8's verdict, unsoftened**, and **where `DISCRIMINATING`, which
  kind — `INTERPRETIVE` or `ADDITIVE` — with the requirement named if
  additive;**
- **A9's search, finding, and per-candidate treatment lengths**;
- **A13's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and the measured RUN 1 subject set;
- **§7's four Rule 16 junctions**, including whether the tables are
  symmetric;
- **whether working through the readings made you want to resolve one.**
  **Say which and why, and confirm you did not** — **that answer is
  useful to the PI and is not a ruling**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.** **This record covers facts about the repository AND facts
this specification asserts about itself.**

    target      the dossier branch
    method      git fetch; git rev-parse; git merge-base --is-ancestor
    MEASURED    science/dpre-a-kinetic-operator-dossier = 27fabe17…,
                NOT an ancestor of main. The dossier is unintegrated and
                this task reads it at that SHA.

    target      the isotropy freeze
    method      read P2-LATTICE-ONTOLOGY-01 line 94 at ae3604de
    MEASURED    "H(4) isotropy (equal couplings on all four axes) joins
                the freeze list." The parenthesis is the operative
                content and it does not say whether "equal" ranges over
                magnitudes or over magnitudes and signs.

    target      the dossier's isotropy treatment
    method      read §5.3 of the dossier at 27fabe17, lines 403-424
    MEASURED    naive COMPATIBLE, Wilson COMPATIBLE, staggered NOT
                ESTABLISHED. The derivation records that the staggered
                magnitudes are equal on all four axes and the sign
                patterns single out an axis ordering, and that the text
                does not settle which reading applies. RECORDED, NOT
                RESOLVED. Overlap's row was not read by this author and
                A4 requires all four under both readings.

    target      the ultralocality derivation
    method      read §4.4 of the dossier at 27fabe17, line 333
    MEASURED    "DERIVED HERE: the free overlap operator is not
                ultralocal." Line 276 records that the dossier did not
                establish whether non-ultralocality obstructs any frozen
                obligation.

    target      the ansatz sentence the Researcher mischaracterised
    method      read lines 605-611 of the dossier at 27fabe17
    MEASURED    the sentence is conditional — "treating a Wilson or
                overlap species ledger AS ADDITIONAL FLAVOURS ... would
                violate". It eliminates one candidate mapping; it does
                not assert a violation.
    RETRACTED   the Researcher told the PI the dossier contained an
                internal contradiction, having read the execution
                summary rather than the dossier. It does not. §0a
                records the correction and A3 requires it verified
                against the file.

    target      the Lorentz-emergence dependency
    method      read P2-LATTICE-ONTOLOGY-01 lines 115-126
    MEASURED    the mechanism is stated for "a local, translation-
                invariant, axis-isotropic lattice action", and the
                document says H(4) symmetry alone does not guarantee
                proximity to the right critical surface. Both questions
                of this task bear on that sentence.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path, one per line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                ae3604de and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                the manifest lists four and 'modify: []' contributes
                none; parse OK, counted equals stated per category.
