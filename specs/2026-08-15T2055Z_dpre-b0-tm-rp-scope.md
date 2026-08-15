# Task specification — `D-pre-B0`: what the transfer-matrix and reflection-positivity work actually is

Specification evidence base: `e70f55def26a96ffc325c0ae3231223e4623c76b`

    Branch to create   science/dpre-b0-tm-rp-scope
    Cut from           authoritative main @ e70f55de…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**IT CONSTRUCTS NOTHING.** No transfer matrix, no reflection-positivity
proof, no spectral equivalence. **It determines what that work is,
before the programme commits to it.**

---

## 0. Why a scope assessment rather than the work

**Three cheap discriminants have been tried and none discriminates on
grounds already committed to.** The isotropy reading eliminates a
presentation and only under the stronger reading; the finite-range case
costs a new ontology commitment that line 115 does not require; the
plaquette phase turned out to be the Clifford structure all four
candidates carry.

**Reflection positivity is different in kind, and that is why it is
next.** **`P2-LATTICE-ONTOLOGY-01` line 181 freezes it as an
obligation.** **A candidate eliminated on reflection-positivity grounds
would be eliminated by a commitment the programme has ALREADY made** —
unlike `Case A`, which would require a new one.

**But nobody knows how large the work is, and an earlier draft of this
specification misstated why.**

**The dossier reports reflection positivity `NOT ESTABLISHED` for all
four candidates.** **It does NOT attribute that to a missing transfer
matrix.** Measured: for staggered it records that nothing in the
repository addresses it and nothing is derived there; for overlap it
derives an obstruction **to one family of methods** and says explicitly
that this **is not a demonstration that reflection positivity fails.**
**Where the dossier does tie something to a transfer operator is the
vacuum-selection rule of ontology line 184, not reflection positivity.**

**The earlier draft said the recorded reason was the absence of a
transfer matrix. That was the Researcher's addition, not the dossier's.**

**The correction matters because it changes what this task must
measure.** **For proposition `(ii)`, a transfer matrix is NOT a logical
prerequisite** — Osterwalder–Schrader positivity is a condition on the
Euclidean action and measure, and the reconstruction theorem produces the
Hilbert space and time evolution FROM it, not the other way round.
**Framing the assessment as "how much transfer-matrix machinery does RP
need" would have presupposed the answer.**

**This task measures the job before it is commissioned, and measures it
without that presupposition.**

## 1. What the obligation already says, and it constrains the answer

**Read `P2-LATTICE-ONTOLOGY-01` lines 68–80 before anything else.** The
frozen text **distinguishes three propositions and forbids conflating
them:**

    (i)    positivity of a particular finite transfer matrix —
           sufficient, in that finite model, to define H = a log T
    (ii)   Osterwalder-Schrader reflection positivity of the Euclidean
           measure and action — the general reconstruction condition
    (iii)  axis equivalence

**And the frozen text already answers part of this task's question.**
For `(ii)` it says: **this must be proved PER DECLARED KINETIC OPERATOR,
and cannot be transplanted** — naming a bosonic Ising example as exactly
what it cannot be transplanted from.

**So a single shared construction cannot discharge `(ii)` for four
candidates. The ontology says so, and this task must not propose
otherwise.**

**What remains genuinely open is what CAN be shared** — plausibly the
`(i)`-level machinery, and plausibly the normalisation `D-pre-B`
needs. **Determining that is the point.**

**Quote the three propositions as measured, with line numbers**, and
**state which of the three, if established or refuted per candidate,
would actually discriminate.** **They are not equivalent for that
purpose and the assessment must not treat them as one requirement.**

## 2. The overlap with `D-pre-B`

**`P2-LATTICE-ROUTE-01` line 195 makes Euclidean–spectral response
equivalence `D-pre-B`'s blocking deliverable**, and **line 201 lists
`transfer-matrix normalization` as the first of nine items it requires** —
alongside geometry-dependent measure and Jacobian factors, finite
temporal extent, temporal boundary conditions, vacuum degeneracy,
additive energy normalisation, contact terms, curvature-dependent
normalisation, and the static-to-four-geometry restriction.

**So the two lines of work touch at least at that item — but that item
belongs to proposition `(i)`, and it is `(ii)` that carries the
obligation.**

**The question this task answers is therefore two-sided, and neither side
may be assumed:**

    for each candidate, can proposition (ii) be addressed DIRECTLY at
    the Euclidean action and measure level, without first constructing
    a transfer matrix?

    does proposition (i) require a separate transfer-matrix
    construction, and is THAT what overlaps D-pre-B?

**A finding that the overlap is SMALL is a real and useful outcome**, and
**the framing must leave room for it.** **If `(ii)` is directly
addressable for some candidates, the reflection-positivity route may not
wait on the transfer matrix at all**, and the machinery shared with
`D-pre-B` would be `(i)` and the spectral normalisation rather than the
obligation itself.

**For each of the nine items, report:** whether it is required by the
reflection-positivity obligation as well, by `D-pre-B` alone, or by
neither once `(i)` is separated from `(ii)`. **Nine results.**

**Report the measured overlap**, and **then state whether the two should
be scoped as one piece of work or two.** **That statement is this task's
deliverable and is permitted.** **Writing the combined specification is
not** — §4 forbids it.

## 3. Candidate-independence, and the question that decides whether any of this discriminates

**For each of the four candidates, and for each of the three
propositions, report one of:**

    ESTABLISHED IN THE REPOSITORY   with the lines
    NOT ESTABLISHED                 nobody has done it here
    REFUTED                         the declared action FAILS the
                                    relevant positivity condition, with
                                    the derivation
    NOT DETERMINABLE BY THIS TASK   determining it requires the
                                    construction this task must not
                                    perform

**Twelve results.**

**`REFUTED`, not `IMPOSSIBLE`, and the change is substantive.** **An
earlier draft used `IMPOSSIBLE`, which conflates two different claims:**
*this action does not satisfy the condition*, and *no construction or
proof could ever exist*. **The first is what would eliminate a candidate.
The second is a far stronger theorem and is not what the programme
needs.**

**Only a `REFUTED` REQUIRED proposition supplies negative candidate
evidence.** **`NOT ESTABLISHED` and `NOT DETERMINABLE BY THIS TASK`
supply none** — **the dossier already demonstrated that four uniform
`NOT ESTABLISHED` results carry no discriminating information.**

**Expect `NOT DETERMINABLE BY THIS TASK` to be common, and report it
rather than guessing.**

**Report separately, per candidate and per proposition, whether a
STANDARD RESULT is known to exist.** **A claim that one exists is a
LITERATURE CLAIM, not a derivation**, and must be written as one.

**Each such claim carries four fields, separately:**

    AUTHOR/WORK   who established it, specifically enough that someone
                  with library access could find it
    STATEMENT     what was proved — the action, the operator, the
                  conditions
    SCOPE         free field only? with interactions? which geometries?
                  which r, which M0, which boundary conditions?
    COVERAGE      whether it covers THIS programme's declared action,
                  or a restriction of it, or a different action

**`COVERAGE` is the field that matters and the one most easily
skipped.** **A result for a free operator does not cover an interacting
one; a result for a bosonic model does not cover a Grassmann measure with
determinant signs** — the ontology says so at line 79.

**Mark every such claim `UNVERIFIED FROM THIS REPOSITORY`.** **The
repository contains no literature and you have no access to any.** **Do
not verify; state precisely enough to be verified later, and say you did
not.** **Report the count of claims so marked.**

**A claim given without all four fields is a STOP.** **"A standard
construction exists" is not a claim; it is the absence of one.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not construct a transfer matrix**, and **do not attempt a
  reflection-positivity proof for any candidate.**
- **Do not write the combined specification** that §2's recommendation
  may point to. **Recommending a structure is scoping; writing the task
  is the next task.**
- **Do not propose a shared construction for proposition `(ii)`.** **The
  frozen ontology forbids transplanting it.**
- **DO NOT SELECT, ELIMINATE, RANK OR PREFER A CANDIDATE.** **A candidate
  for which the work looks smaller is not a better candidate**, and
  reporting effort as if it were evidence is the failure this line has
  now avoided three times.
- **Do not rule on either `D-pre-A2` question**, and do not add an
  ontology requirement.
- **Do not modify any existing file.**
- **Do not add a register entry anywhere.**
- **Do not claim this task unblocks `C-iii` or `D0`.**

## 5. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`e70f55def26a96ffc325c0ae3231223e4623c76b`. Report the Git blob ids of
`derivations/P2-LATTICE-ONTOLOGY-01.md`,
`derivations/P2-LATTICE-ROUTE-01.md`, and all three
`P2-LATTICE-MICROSPEC-01_*` artifacts. **Any ref mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**
**If absent, blank, or naming a different digest, STOP and say which.**

**A3 — The three propositions, quoted as measured**, with line numbers,
**and which of the three would discriminate if settled per candidate.**
**Report the per-operator clause for `(ii)` verbatim**, and **confirm
this task proposes no shared construction for it.**

**A4 — Twelve results**, per §3: four candidates × three propositions,
each with one of the four dispositions and its evidence. **Report the
count of each disposition.** **A `REFUTED` without a derivation is a
STOP.**

**And report, FOR EACH CANDIDATE — four results, not twelve — whether
proposition `(ii)` was assessed as directly addressable at the Euclidean
level or as requiring a transfer matrix first.** **Proposition `(ii)`
occupies four cells, one per candidate**, and **an earlier draft said
"for each of the twelve", which would have invited three identical
answers per candidate to satisfy a count.** **Per §2, the answer is not
to be assumed either way.**

**A5 — Literature claims, structured and marked.** Per candidate and
per proposition, report any claim that a standard result exists, **with
all four fields of §3 — `AUTHOR/WORK`, `STATEMENT`, `SCOPE`,
`COVERAGE`.** **A claim missing any field is a STOP.**

**Mark every one `UNVERIFIED FROM THIS REPOSITORY` and report the
count.** **Report separately how many claims have `COVERAGE` reaching
this programme's declared action, and how many cover only a restriction
of it** — **that second number is the one that determines how much work
remains.**

**A6 — The nine `D-pre-B` items, classified**, per §2. **Nine results.**
**Report them as a table**, and **report the count required by both
lines of work.**

**A7 — The scoping recommendation.** **One piece of work or two**, with
the measured overlap behind it. **State what a combined task would have
to contain and what a split would duplicate.** **Do not write either.**

**A8 — A size estimate, stated as a range and as its basis.** **How much
of the work is candidate-independent and how much is four-fold**, given
`(ii)`'s per-operator requirement. **State the basis for the estimate.**
**"Large" is not an estimate**; **a count of distinct constructions
required, and which of them are independent, is.**

**A9 — No selection, no preference, and effort is not evidence.**
**Search the artifact, the report and the commit messages for any
sentence that selects, ranks, prefers, or presents a candidate as more
tractable in a way that reads as favourable.** **Report the search and
the finding.**

**Report the treatment length per candidate**, and **report explicitly
whether the lengths are unequal and why** — **if the work genuinely
differs in size between candidates, the lengths SHOULD differ, and the
requirement is to say so rather than to level them.** **This is a change
from `D-pre-A`'s `A10`, where equal treatment was the expectation**, and
the reason is that here the size difference is the measurement.

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: e70f55def26a96ffc325c0ae3231223e4623c76b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md
      reports/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md
      specs/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**A11 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, both lattice artifacts, all three microspec
artifacts, both registers, `docs/GOVERNANCE-DEBT.md`, and everything
under `scripts/`, `tests/` and `results/`.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A13 — The checker over this task's own range**, base `e70f55de…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` selects one specification in this
range** — **report what it actually did.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A14 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected.**

**A15 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md
    commit 4  reports/2026-08-XXT{HHMM}Z_dpre-b0-tm-rp-scope.md

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

**First.** **A scope assessment is not a result.** **Knowing what the
work is does not make any candidate more or less admissible**, and
**nothing here brings the programme closer to a phase verdict.** **Say
that**, and **say that the assessment's value is in preventing a
commitment made blind.**

**Second, and it is the one most likely to be misread.** **Effort is not
evidence.** **If the construction turns out smaller for one candidate,
that is a fact about the mathematics available, not about the physics.**
**Say so where a reader meets the size estimate**, and **do not let a
tractability difference read as a selection ground.**

**Third.** **Even a completed reflection-positivity result may not
discriminate.** **Four `NOT ESTABLISHED` results carry no information,
and the dossier already demonstrated that.** **Whether this route
discriminates depends on `REFUTED` being reachable for at least one
candidate** — **the declared action failing the condition, not a theorem
that no proof could exist** — and **this task reports whether that is
determinable, not whether it is true.**

**Fourth.** **The repository contains no literature and the executor has
no access to any.** **Every claim that a standard result exists is
`UNVERIFIED FROM THIS REPOSITORY`** — **a different kind of claim from
the derivations this programme has been producing, and one no criterion
here can check.**

**Report how many such claims the assessment makes, and how many have
`COVERAGE` reaching the declared action.** **Say that a scope estimate
resting on unverified coverage claims is only as good as those claims**,
and **that verifying them is work this task cannot do and the next one
must.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  scope artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not construct, prove, select, rank, or write the next
  specification.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
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
- **A3's three propositions quoted with line numbers**, the per-operator
  clause verbatim, and which would discriminate;
- **A4's twelve results with disposition counts**;
- **A5's literature claims with all four fields each**, the count marked
  `UNVERIFIED FROM THIS REPOSITORY`, and **the count whose `COVERAGE`
  reaches the declared action**;
- **A6's nine-item table and the both-lines count**;
- **A7's recommendation, one piece or two, with the overlap behind it**;
- **A8's estimate as a range with its basis**, and the count of distinct
  constructions required;
- **A9's search, finding, and per-candidate treatment lengths with the
  reason for any inequality**;
- **A13's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and what `RUN 1` did;
- **§7's four Rule 16 junctions**;
- **whether assessing the work made you want to start it, or to select a
  candidate.** **Say which and why, and confirm you did not** — **the
  previous task reported this pull as its strongest**;
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

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    e70f55def26a96ffc325c0ae3231223e4623c76b, the head
                landed by the D-pre-A3 integration.

    target      the reflection-positivity obligation
    method      read P2-LATTICE-ONTOLOGY-01 lines 68-80 and line 181
    MEASURED    line 181 freezes reflection positivity of the action as
                an OBLIGATION. Lines 70-80 distinguish THREE
                propositions that may not be conflated: (i) positivity
                of a particular finite transfer matrix; (ii) OS
                reflection positivity of the Euclidean measure and
                action; (iii) axis equivalence. For (ii) the text says
                it "must be proved per declared kinetic operator, and
                cannot be transplanted from a bosonic Ising example".
    CONSEQUENCE the frozen text already forbids a single shared
                construction for (ii). §1 states this, and §4 forbids
                the task from proposing one.

    target      D-pre-B's blocking deliverable
    method      read P2-LATTICE-ROUTE-01 lines 195-210
    MEASURED    Euclidean-spectral response equivalence is the blocking
                deliverable. Line 201 onward lists NINE items it
                requires, the first being transfer-matrix
                normalization. Line 207 gives the machine-checkable
                residual, and lines 209-210 require both sides evaluated
                under an identical subtraction convention and reference
                configuration.
    NOT DERIVED how far beyond that first item the two lines of work
                overlap. A6 requires it measured item by item.

    target      the dossier's reflection-positivity result
    method      the D-pre-A dossier as landed on main
    MEASURED    NOT ESTABLISHED for all four candidates. THE DOSSIER
                DOES NOT GIVE THE ABSENCE OF A TRANSFER MATRIX AS THEIR
                COMMON CAUSE. For staggered it records that the
                repository does not address reflection positivity and
                derives none there; for overlap it derives an
                obstruction to ONE FAMILY OF METHODS and explicitly does
                not infer failure of reflection positivity. The
                transfer-operator dependency recorded elsewhere in the
                dossier concerns the ontology line 184 vacuum-selection
                rule, NOT the line 181 reflection-positivity obligation.
    RETRACTED   an earlier draft of this record gave the absence of a
                transfer matrix as the cause. That claim was corrected
                in §0 of this revision and was left standing here under
                a MEASURED label — the label an executor is obliged to
                treat as an author-verified repository fact. A
                correction that does not reach the verification record
                has not been made.
    STANDING    four uniform results carry no discriminating
                information, which is why §3 separates NOT ESTABLISHED
                from REFUTED. An earlier draft of §3 used IMPOSSIBLE,
                which conflates "this action fails the condition" with
                "no proof could ever exist"; only the first would
                eliminate a candidate and only the first is needed.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path, one per line, matching A13's config.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                e70f55de and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                the manifest lists four and 'modify: []' contributes
                none; parse OK, counted equals stated per category.
