# Task specification — adopt the phase input / admissibility contract

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   science/adopt-admissibility-contract
    Cut from           authoritative main @ 1cb5550f…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task freezes a rule. It evaluates nothing.** No phase is admitted,
no Hessian is computed, no symmetry is determined, and no candidate is
assessed against the rule it adopts.

**It modifies `GATES.md`** and re-pins one artifact. §3 states exactly
which lines and why.

**It is cut from `main`, not from the parameter-domain adoption line.**
That is the PI's instruction, taken **to keep the provenance of the two
adoptions independent**, and it accepts a small `GATES.md` integration
conflict as the price. §2a records what that conflict will look like so
that whoever integrates is not surprised by it.

---

## 0. What is being adopted, and what is not

**An operational admissibility standard**, and nothing else.

**`GATES.md`'s statement of this prerequisite is one sentence:** *no
operational stability or admissibility rule is presently frozen.*
**This task freezes one.**

**What it does NOT do, stated first because it is the thing most easily
over-read:**

- **It does not assess any candidate.** The negative-mass branch, the
  ordinary branch and the trivial vacuum are all exactly where they were.
- **It does not supply the evaluation inputs.** Three remain missing and
  §4 records them as such.
- **It does not make `P2-PHASE-01` runnable.** The gate's own *Required
  computations* section reads `(not started)` and this task does not
  start them.
- **It computes nothing.**

**Having a rule and being able to apply it are different**, and the
PI ruling at §1 turns on exactly that distinction.

## 1. The PI ruling

**Recorded verbatim. It is a ruling, not a derivation.**

> **PI RULING.** `operational` is read in the first sense: a rule is
> operational once it can decide, for a given candidate, whether that
> candidate is admissible. It need not be applicable today. Accordingly,
> once standard C below is frozen, the PHASE INPUT / ADMISSIBILITY
> CONTRACT prerequisite is `SATISFIED`. **This does not mean any
> candidate has passed an admissibility assessment, and it does not mean
> the evaluation inputs are complete.**

**The gate's own text supports the reading, and the support is recorded
so the ruling is not doing work the text already does.** The prerequisite
speaks of a rule being *frozen*, not of a rule being *evaluated*; the
MICROSCOPIC PARAMETER DOMAIN prerequisite has the same shape and was
satisfied by a decision rather than a computation; and the gate's
*Quantifier note* names only the parameter-domain prerequisite as what
the kill criterion waits on.

**What the ruling settles is the residual ambiguity in the word
`operational`**, which the text does not define: whether a rule requiring
inputs that do not yet exist counts as operational. **It does.**

## 2. Standard C, the adopted rule

**A candidate stationary solution is ADMISSIBLE for `P2-PHASE-01` when
all three hold:**

    C-i    STATIONARITY AND LOCAL STABILITY
           it is a stationary point of the full effective action, and
           the full CONDENSATE-SPACE Hessian is positive definite on
           the space transverse to any flat directions required by an
           exact or remnant symmetry
           — NOT the restricted one-dimensional curvature, which is
             what every stored result to date carries

    C-ii   THERMODYNAMIC SELECTION
           define the COMPARISON SET S as every stationary solution
           satisfying C-i and C-iii — the non-thermodynamic conditions
           alone, with C-ii itself excluded from the test. A candidate
           satisfies C-ii when it is not shallower than any member of
           S, compared under a COMMON NORMALISATION across the channels
           in play — effective-potential or free-energy depth, not
           curvature.

           TIES ARE ADMITTED: "not shallower than" permits more than
           one member of S to satisfy C-ii, and SI-1's question is
           existential, so that is not a defect.

    C-iii  SYMMETRY ACCOUNTING
           the exact and remnant symmetries of the frozen microscopic
           action are determined, whether the condensate is an order
           parameter for any of them is stated, and any Goldstone
           directions are identified and excluded from C-i's positivity
           requirement

**C-ii's comparison set is defined without reference to admissibility,
and that is a repair rather than a stylistic choice.** An earlier
statement of `C-ii` compared a candidate against *competing ADMISSIBLE
stationary solutions*, while `ADMISSIBLE` was itself defined as
`C-i AND C-ii AND C-iii`. **That is a self-referential definition, not a
decision rule**: the set a candidate must beat would depend on the answer
being computed. **Defining `S` from `C-i` and `C-iii` alone removes the
recursion without changing the intended standard** — the deepest members
of `S` are admissible, and shallower members of `S` fail `C-ii`.

**The PI's ruling that a rule is operational once it can decide does not
repair this.** **A rule with a recursive quantifier cannot decide,
whatever its inputs.** The two issues are independent and both had to be
settled.

**C-i's transverse clause is not decoration.** If the condensate breaks
an exact symmetry, the Hessian carries zero eigenvalues along the
Goldstone directions and **cannot be positive definite**. A rule
demanding plain positive definiteness would then reject every
symmetry-breaking phase, **not because such a phase is unstable, but
because the criterion was written wrongly.** **`C-iii` therefore governs
how `C-i` is read**, which is why §4 orders the work as it does.

**The PI selected this standard over two weaker ones.** The alternatives
were local stability alone, and local stability plus within-scalar depth.
**Both would let the gate pass on a reason weaker than the question it
asks**, and the programme has already met that shape once in the
negative-mass branch. **The cost is accepted knowingly: standard C is not
evaluable now, and will not be for some time.**

## 2a. The `GATES.md` conflict this task creates, named in advance

**`science/adopt-parameter-domain-labels @ 8b79fad4…` edits the
MICROSCOPIC PARAMETER DOMAIN prerequisite block. This task edits the
PHASE INPUT / ADMISSIBILITY CONTRACT block**, which begins about three
lines below it.

**Both branches therefore modify `GATES.md` in nearby regions.**
**Measured, ten lines separate the two blocks**, so a textual conflict at
integration is **possible rather than certain** — close enough that
`git` may fold them into one hunk, far enough that it may not. **It would
be a conflict of adjacency, not of substance**: the two edits touch
disjoint blocks and neither depends on the other.

**Whoever integrates resolves it by taking both blocks**, and **must
verify afterwards that all four pins in the merged file match their
targets** — the parameter-domain line moves one pin twice and this task
moves another.

**This was the PI's choice, made to keep the two adoptions'
provenance independent.** **It is recorded here rather than discovered
later.**

## 3. The `GATES.md` edit

**Replace the block beginning
`### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT`
and ending at the line before `### Integrated exploratory evidence`,
with the text in A6.** **`GATES.md` changes there and nowhere else.**

**No gate `Status:` line changes.** `P2-PHASE-01` stays `PROPOSED`,
because the parameter-domain prerequisite is `UNSATISFIED` **at this
evidence base** — its adoption sits on a branch this task does not carry.
**Report that as the reason**, so that a reader does not conclude the
domain question is unresolved.

## 4. The three OPEN-AC items, reclassified

**They are EVALUATION-INPUT GAPS, not RULE-DEFINITION gaps.** **This
distinction is the whole reason the prerequisite can be `SATISFIED`
without overstating scientific progress, and the adopted contract must
carry it in those words.**

**None of the three is resolved by this task. None is closed. None is
downgraded.**

    OPEN-AC-1  P/V/A/T mean-field construction.
               STILL OPEN. An input to C-ii whenever a channel beyond
               the scalar enters the comparison. Not required for a
               scalar-only evaluation, and the PI's route choice is
               scalar. It is the largest of the three and it has not
               been started.

    OPEN-AC-3  Cross-family and within-scalar potential comparison.
               STILL OPEN. THE input to C-ii. The cross-family part
               needs the common normalisation that does not exist. The
               within-scalar part the draft records as possibly already
               available, since the algebraic branches share one
               potential and one stated zero — but what physical
               meaning such a comparison carries is undecided, and the
               draft says so.

    OPEN-AC-4  Exact/remnant symmetry and Goldstone implications.
               STILL OPEN. THE input to C-iii, and through C-iii it
               governs how C-i is read. The existing material
               establishes only that Mhat -> -Mhat is not a symmetry of
               the Wilson scalar functional, and reports the complement
               relation. The draft states that the symmetry
               interpretation is a review inference, not a computed
               result.

**Work order: `OPEN-AC-4`, then `OPEN-AC-3`, then `OPEN-AC-1`.** **Stated
with its reason, and the reason is narrower than it may look:**

**`AC-4` is logically prior to APPLYING `C-i`, and therefore prior to any
complete standard-C assessment**, because it determines whether `C-i`'s
positivity is read plainly or transverse to flat directions.

**It is NOT claimed that `AC-4` fixes the form of the criteria `AC-3` or
`AC-1` feed.** `C-ii`'s comparison is a depth comparison under a common
normalisation whatever the symmetry analysis returns, and `AC-1` is a
construction input. **An earlier draft asserted the wider dependency; it
was stronger than the actual graph.**

**Do not record this order as a schedule or a commitment.** It is a
dependency statement.

## 5. The adopted artifact

Create `derivations/P2-PHASE-01_input_admissibility_contract.md`
containing, in this order:

1. **status**, adopted, naming this task's specification;
2. **the PI ruling of §1, verbatim**;
3. **standard C, verbatim from §2**, including the transverse clause and
   the paragraph explaining why it is there;
4. **§4's reclassification, verbatim**, with all three items marked
   `STILL OPEN` and the work order with its reason;
5. **what adoption does NOT establish**, per §7, **as a standalone
   section a reader meets without searching**;
6. **a pointer to the superseded draft.**

**Every kind label used must be defined in the artifact.** **Four
consecutive tasks on the parameter-domain artifact were spent repairing
labels that asserted a state the document was no longer in**; **do not
reproduce that.** **Before writing, list the labels you intend to use and
their meanings, and use no others.**

## 6. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md` measures
`a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73`,
which equals the pin at `GATES.md:1026`. `GATES.md` blob
`849a4fbfe62d6478f092a84b0175357a74bbbb06`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — The adopted artifact**, per §5. **Report its digest**, and
**report the list of kind labels used with their definitions**, and
**confirm every label used is defined in the artifact.**

**A4 — Standard C transcribed, not paraphrased.** Diff `C-i`, `C-ii`,
`C-iii` and the transverse-clause paragraph in the artifact against §2
and **report that they correspond.** **A rewritten criterion is a STOP.**

**AND: no summary anywhere in the adopted artifact may phrase `C-ii` in
terms of competing ADMISSIBLE solutions.** **Search the artifact for
every restatement of `C-ii` and report each one**, confirming that each
names the `C-i`-and-`C-iii` comparison set rather than admissibility.
**A summary that reintroduces the recursion is a STOP, even where the
criterion itself is transcribed correctly** — §2 was repaired once and
the repair did not propagate to this specification's own `GATES.md`
summary, which is how the defect reached a reviewer a second time.

**A5 — §4 transcribed, not paraphrased**, all three items marked
`STILL OPEN`, the work order and its reason present. **Report the
correspondence.** **An item recorded as resolved, closed, downgraded or
partly settled is a STOP.**

**A6 — The `GATES.md` block replacement**, exactly:

    ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
    Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
    Owner: Paper 2. Canonical label: **PHASE INPUT / ADMISSIBILITY
    CONTRACT**; not a gate ID. Adopted artifact:
    `derivations/P2-PHASE-01_input_admissibility_contract.md`
    (sha256 `<the digest measured in A3, from the COMMITTED BLOB>`).
    Superseded draft:
    `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.

    An operational admissibility standard is frozen: full
    condensate-space Hessian positivity transverse to symmetry-required
    flat directions; thermodynamic selection against the comparison set
    of stationary solutions satisfying the non-thermodynamic conditions
    C-i and C-iii, under a common normalisation; and symmetry accounting
    sufficient to identify those flat directions. Per PI ruling, a rule
    that can decide a candidate is operational whether or not its inputs
    presently exist.

    The comparison set is defined WITHOUT reference to admissibility,
    deliberately. A summary phrased as "no competing ADMISSIBLE solution
    deeper" would define admissibility in terms of itself; the adopted
    artifact does not, and this block must not.

    **This prerequisite being SATISFIED means a rule exists. It does not
    mean any candidate has been assessed, and it does not mean the
    evaluation inputs are complete.** Three remain open —
    `OPEN-AC-1`, `OPEN-AC-3`, `OPEN-AC-4` — and they are
    evaluation-input gaps, not rule-definition gaps.

**A7 — Gate invariants.** At commit 4: `^## P2-` count **14**; every
`Status:` line textually identical to the evidence base; `P2-PHASE-01`
reads `Status: PROPOSED`; **the MICROSCOPIC PARAMETER DOMAIN prerequisite
still reads `UNSATISFIED`**, because its adoption is on a branch this
task does not carry. **Report all four**, and **report the reason for the
fourth** so it is not read as a regression.

**A8 — The pointer insertion.** Insert immediately after the first
heading line of
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`:

    **SUPERSEDED.** Adopted as
    `derivations/P2-PHASE-01_input_admissibility_contract.md`. This file
    is retained as historical evidence and is not operative. Its
    `OPEN-AC` entries are unchanged and remain OPEN; the adopted
    artifact reclassifies them as evaluation-input gaps without
    resolving any of them.

**No pre-existing text in that file is edited or replaced.** **No
`OPEN-AC` body and no verdict is altered.** Report the diff in full.

**A9 — Both pins match at the head.** For each occurrence of
`` (sha256 `<64 hex>`) `` in `GATES.md`, identify the artifact path named
immediately above it, measure that path's SHA-256 at the head, and report
the pair. **Expected: two pins.** **The contract pin must have moved to
the adopted artifact's digest; the parameter-domain draft pin at
`d8e15469…` must still match its target**, which this task does not
touch. **Assert the count is at least one**, and **report the count
found.**

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 2 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5>
    mode: exact
    add:
      derivations/P2-PHASE-01_input_admissibility_contract.md
      reports/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md
      specs/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Six paths. Nothing under `results/`, `scripts/`, `tests/` is touched.**

**A11 — Protected paths.** Every path existing at the evidence base other
than the two in A10's `modify:` list is blob-identical at commit 5. **In
particular the exploratory script, the results file, and
`derivations/P2-DEFERRED-ITEMS.md`.** Compare path by path and report the
count.

**A12 — The checker over this task's own range**, base `1cb5550f…`, head
**commit 4**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  ["P2-PHASE-01"]
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`** — an empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE`, the check switched off rather than
passed.

**`P7` will return `PASS` and it is evidence of nothing** —
`GATE_HEADING` matches zero of the fourteen real gate headings. **This
task modifies `GATES.md`, so the vacuous green is again where it is most
dangerous.** **A6's and A9's measurements are what establish the edit's
confinement, not `P7`.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.**

**A12-final, post-report evidence:** re-run RUN 2 at commit 5.

**A13 — Commit-message hygiene** on all five commits. **Commits 1–4 go in
the report; commit 5 is post-report evidence.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task `GATES.md` will read `SATISFIED` for the admissibility prerequisite.
**A reader may infer that admissibility has been settled, or that the
gate is closer to an answer.** **Neither is true.** **A rule now exists
and nothing has been measured against it.**

**No candidate is closer to an admissibility verdict, and no additional
scientific evidence toward the gate's physical verdict has been
produced.** **A procedural step was completed and nothing was measured.**
The three inputs the rule needs remain open — **one of them,
`OPEN-AC-1`, not started at all.**

**An earlier form of this sentence said the gate was no closer to a
verdict at all**, which denied that a prerequisite transition is a step.
**It is a step. It is just not a scientific one.**

**Say that where a reader will meet it**, and say that **standard C was
chosen knowing it is not evaluable now.**

**Second junction.** `P7` will report `PASS` in this task's own checker
output while checking nothing, in a task that modifies `GATES.md`.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, the
  adopted artifact, and the two paths in A10's `modify:` list. **Nothing
  else.**
- **Do not evaluate anything against standard C.** Not the negative-mass
  branch, not the ordinary branch, not the trivial vacuum.
- **Do not resolve, close, downgrade or partly settle any `OPEN-AC`
  item**, and **do not add a fourth.**
- **Do not edit any `OPEN-AC` body text in the draft**, and do not alter
  any verdict in it.
- **Do not change any gate `Status:` line**, and **do not touch the
  MICROSCOPIC PARAMETER DOMAIN block** — it is another branch's.
- **Do not answer `C2`**, and do not read the exploratory script.
- **Do not touch `main`**, do not merge, and **do not merge or reference
  the parameter-domain adoption branch.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md
    commit 3  derivations/P2-PHASE-01_input_admissibility_contract.md
    commit 4  GATES.md
              derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    commit 5  reports/2026-08-XXT{HHMM}Z_adopt-admissibility-contract.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Commit 3 precedes commit 4 because A6's replacement embeds commit 3's
blob digest.** Measure it from the committed blob, not from a
working-tree file.

**Committed report — measured at commit 4:** A1–A11 and A13 for commits
1–4; **A12's two runs with both configs verbatim**; commit 1–4 SHAs and
stored messages; commit 5's intended message; **the final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-5; A12-final; A9 re-run at commit 5; A13 for commit 5;
validators at commit 5; the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 10. Report contract

- everything in §9 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's label list with definitions**, and confirmation every label used
  is defined;
- **A4's and A5's correspondence**, and confirmation that no `OPEN-AC`
  item was recorded as anything other than `STILL OPEN`;
- **A6's and A8's diffs in full**;
- **A9's pin table** with the count found;
- **A7's four invariants and the reason for the fourth**;
- **A12's two runs, both configs verbatim**, and the `P7` statement;
- **whether the adopted artifact reads as though admissibility had been
  settled.** It has not;
- **whether freezing standard C made you want to evaluate anything
  against it.** **Say so, and confirm you did not**;
- **§7's Rule 16 assessment**, both junctions;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.**

    target      the prerequisite's stated requirement
    method      read the block verbatim from GATES.md at 1cb5550f
    MEASURED    seven lines. The only substantive requirement is "No
                operational stability or admissibility rule is presently
                frozen." It speaks of a rule being FROZEN, not
                evaluated.

    target      whether anything else in GATES.md states what this
                prerequisite must deliver
    method      grep -n -i 'admissib' over the whole file
    MEASURED    fifteen occurrences. None adds a requirement to this
                prerequisite. The gate's Quantifier note names only the
                MICROSCOPIC PARAMETER DOMAIN prerequisite as what the
                kill criterion waits on. Required computations and
                Required deliverables both read "(not started)".

    target      the draft and its pin
    method      sha256sum and git rev-parse at 1cb5550f; read
                GATES.md:1026
    MEASURED    draft sha256 a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73,
                blob 5f020f33a9230d1aaa7c98c79db49b1efcb822f6, and the
                pin at line 1026 carries the same value. The pin is
                correct at the evidence base and this task's A8 will
                stale it, which is why A6 moves it.

    target      pins in GATES.md, counted over the whole file
    method      grep -n 'sha256 `[0-9a-f]{64}`'
    MEASURED    exactly TWO, at lines 1015 and 1026. Line 1015 names the
                parameter-domain draft and is not touched here.

    target      the three OPEN-AC items, read in full
    method      read derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
                at 1cb5550f — 88 lines, whole file, no head, no tail
    MEASURED    five OPEN-AC items exist. AC-2 and AC-5 are addressed by
                the parameter-domain adoption line and are not this
                task's subject. AC-1, AC-3 and AC-4 are the three §4
                reclassifies. AC-3's text records that a within-scalar
                comparison "may be available" and that its physical
                interpretation is undecided. AC-4's text records that
                the symmetry interpretation is "a review inference, not
                a computed result".

    target      GATES.md at the evidence base
    method      git rev-parse; grep -c '^## P2-'; read the
                P2-PHASE-01 Status line
    MEASURED    blob 849a4fbfe62d6478f092a84b0175357a74bbbb06; 14
                sections; Status: PROPOSED; the MICROSCOPIC PARAMETER
                DOMAIN prerequisite reads UNSATISFIED at this base,
                because its adoption is on an unmerged branch.

    target      the adjacency of the two branches' GATES.md edits
    method      read the two blocks' line ranges at 1cb5550f
    MEASURED    the MICROSCOPIC PARAMETER DOMAIN block begins at line
                1010; the PHASE INPUT / ADMISSIBILITY CONTRACT block
                spans lines 1021 to 1028. TEN lines separate the end of
                one from the start of the other. A textual conflict at
                integration is POSSIBLE rather than likely at that
                separation, and §2a records it either way.
    RETRACTED   an earlier draft of this record said "two lines apart"
                and "likely". Both were written before the line numbers
                were measured; the measurement gives ten lines, and the
                characterisation is corrected with it.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 2 modifications;
                manifest lists four and two; parse OK, counted equals
                stated.
