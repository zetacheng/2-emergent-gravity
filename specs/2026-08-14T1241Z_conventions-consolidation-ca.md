# Task specification — `C-a`: consolidate twelve observed failures into durable conventions

Specification evidence base: `bec0117168144d54fb23338b673cf7a7e4771868`

    Branch to create   governance/conventions-consolidation-ca
    Cut from           authoritative main @ bec01171…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**It writes prose and changes no behaviour.** No checker property is
added, no test is written, no parser is touched. **What it must not do is
make the unrepaired gaps look repaired**, and §2's mechanism markers are
the whole defence against that.

---

## 0. What this is, and the PI ruling that scoped it

**Twenty-four governance debt items were classified in
`DRAFT_governance_debt_classification.md`, digest
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9`.**
**That artifact is the input to this task and is supplied with it.**

**PI RULING, recorded verbatim, scoping `C`:**

> **`C` is not made into a single twelve-rule task. It is split into
> `C-a`, `C-b` and `C-c`, in that order.**

**This is `C-a`.** It covers §A and §B of the classification —
`A1`–`A8` and `B1`–`B4`, twelve observed failures — **plus `E2`, the
namespace question the PI has ruled.**

**`C-b` (mechanisms `C1` and `C3`) and `C-c` (the debt register) are
separate tasks and this one performs neither.**

## 1. The target is CONSOLIDATION

**Twelve observations do not become twelve rules.**

`CONVENTIONS.md` at the evidence base carries **eighteen numbered rules
and eleven amendments in 1022 lines**, and is referenced **thirteen
times** in `GATES.md`. **Adding twelve rules would be the largest
governance change this programme has made, and would make the rules
themselves harder to govern.**

**Several of the twelve are one discipline in different clothes.**
`A4`, `A5`, `A6` and `A7` are all *a statement whose scope exceeds its
evidence*: output truncated by `head`, an object's presence in one local
clone, a hunk count without its diff context, a reading list naming
functions but not the sites where evidence is written. **Four incidents,
one principle.**

**The candidate grouping, from the classification draft. It may be
replaced with reasons; it may not be silently ignored.**

    1  Authoritative evidence and reproducibility     A4 A5 A6 A7
    2  Artifact identity and review binding           A2 A3 A8
    3  Machine-readable task declarations             A1
    4  Integration and landing discipline             B1 B3
    5  Pinned-artifact integrity                      B2
    6  Permitted pre-push repair                      B4
    7  Artifact-state / statement-kind namespaces     E2

**If your consolidation differs, say why, and keep the traceability
matrix complete.** **Fewer principles is better than more, provided §3's
matrix still shows every item covered.**

## 2. Every rule carries a mechanism marker

**This is the criterion that stops the task from producing a false
green.** Each rule written or amended by this task carries exactly one:

    RULE-ONLY
        no machine check of this rule's obligation is possible or
        wanted; say why

    RULE + MECHANISM EXISTS
        THE OBLIGATION THIS RULE IMPOSES is machine-enforced; name the
        check by property or test file

    RULE + MECHANISM DEFERRED
        the obligation this rule imposes is NOT fully machine-enforced;
        name any partial existing mechanism, name the missing
        enforcement, and name where it is registered

**The marker is about THE RULE'S OBLIGATION, not about whether any
related machinery exists nearby.** **A mechanism that reads a field is
not a mechanism that requires the field**, and marking the first as
`EXISTS` would report an obligation as enforced when it is not. **One
marker per rule; the definition above is what makes one sufficient.**

**Without the markers, twelve observations become rules and a reader
concludes the debt is paid.** **It is not: `C-b` and `C-c` are the rest
of it, and the markers are how a reader finds that out from
`CONVENTIONS.md` itself rather than from this specification.**

**Known assignments, measured, and you verify rather than assume:**

    A1  stated: in scope blocks     MECHANISM DEFERRED — P1 already
                                    PARSES stated:, but no mechanism
                                    REQUIRES a newly issued
                                    specification to supply it. The
                                    partial mechanism is P1; the missing
                                    enforcement is registered as C2.
                                    An earlier version of this
                                    specification marked A1 EXISTS,
                                    which reported an unenforced
                                    obligation as enforced.
    A3  review cites digests        MECHANISM DEFERRED — no check
                                    compares a review's cited digest
                                    against the specification committed
                                    beside it
    B2  re-pin on modification      MECHANISM EXISTS — tests/test_gate_pins.py
                                    landed at e3ce8063 and fails on a
                                    stale pin
    B3  line survival on auto-merge MECHANISM DEFERRED — measured by
                                    hand once, by an executor, beyond
                                    its criterion

**Verify each of these four against the repository before writing them
down.** **Report any you find misstated** — they are the specification
author's assignments and they have not been independently checked.

## 3. The traceability matrix

**A table, in the adopted text or immediately beside it, mapping every
one of `A1`–`A8`, `B1`–`B4` and `E2` to the rule or amendment that now
covers it.**

**Thirteen source items. Every one appears exactly once as a row.**
**A row with no rule is a STOP. An item appearing twice is a STOP unless
the duplication is stated and justified.**

**The matrix is what makes set-review possible.** Without it a reviewer
must hold twelve incidents and seven rules in mind simultaneously and
check the mapping by memory. **With it, coverage is a thing that can be
counted.**

## 4. Placement: rules, amendments, or a new section

**`CONVENTIONS.md` uses two forms and they are not interchangeable.**
Measured at the evidence base:

    ### 1. … through ### 18.     numbered rules, in
                                 '## Execution discipline for decisive
                                 runs and merges' and
                                 '## Role separation and outcome-based
                                 task specification'
    Amendments A-I, K, L         embedded INLINE beneath the rule they
                                 modify — Amendment H sits under
                                 '### 3. Declared frozen scope is
                                 normative'

**So an amendment modifies an existing rule in place; a numbered rule
stands alone.** **The distinction is structural and this task must respect
it rather than pick whichever is convenient.**

**The eighteen existing rules, so placement is decided against the actual
file and not from memory:**

     1 Contradiction-stop                    10 Self-correction authority
     2 Scope precedence                      11 Task granularity
     3 Declared frozen scope is normative    12 Mechanically checkable criteria
     4 Execution prompts are evidence        13 Execution environment
     5 Minimum mandatory merge discipline    14 Validator outcome contract
     6 Reporting honesty for merges          15 Governing artifacts committed
     7 Evidence precedence                   16 Accumulated reading
     8 Responsibility separation             17 Integrations add no classification
     9 Outcome-based task specification      18 Review supply protocol

**For each principle you write, decide and JUSTIFY its form:**

- **an amendment**, if it modifies an existing rule — **name the rule and
  say what of it changes**;
- **a new numbered rule**, if it stands alone — **the next numbers are
  19 onward**;
- **and if you judge a third form is needed, STOP and report it** rather
  than inventing one.

**The next amendment letter is `M`.** Measured: `A` through `I`, `K` and
`L` are used; **there is no `J`**, and this task does not create one.

**Do not renumber, reorder or re-word any existing rule or amendment.**
**An amendment adds; it does not rewrite.**

## 5. What the twelve observed failures and the additional `E2` ruling are

**Twelve observed failures plus one ruled item: thirteen rows in §3's
matrix.** **Read them from the classification artifact, not from this
specification.** §A and §B of
`DRAFT_governance_debt_classification.md` state each with the measurement
behind it. **This section names them only so the count is checkable:**

    A1 stated: key            A2 specification supplied as a file
    A3 review cites digests   A4 whole-subject measurement
    A5 clone-invariance       A6 hunk count names its context
    A7 reading lists name evidence-write sites
    A8 evidence is not discharge
    B1 landing clause inline  B2 re-pin on modification
    B3 line survival          B4 permitted pre-push amend
    E2 namespace distinction

**`E2` is ruled and its wording is fixed:**

> **Artifact-state labels and statement-kind labels are distinct
> vocabularies; an artifact-state label does not need to appear in the
> statement-kind vocabulary.**

**Adopt that sentence verbatim.** **`B4`'s ruling is also on record and
its durable form must decide one thing the ratification left open:
whether an amend requires every affected check re-run or only the failing
one.** **The executor of that instance re-ran all four voluntarily.**
**Decide it, state which you chose, and say that the ratified instance
did not settle it.**

## 6. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not write any code, test, checker property or parser change.**
  **`C-b` does that.**
- **Do not register `D1`–`D4` or rule on `E1`.** **`C-c` does the first;
  the second is the PI's and is not generalised in passing.**
- **Do not renumber or re-word an existing rule or amendment.**
- **Do not create an Amendment `J`.**
- **Do not mark any item's mechanism as EXISTS without naming the check
  and verifying it exists.**
- **Do not describe the governance gap as closed.** §7 governs.
- **Do not modify `GATES.md`**, and **do not touch anything under
  `scripts/`, `tests/`, `results/` or `derivations/`.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** After this lands, `CONVENTIONS.md` will carry rules covering
twelve failures that previously had none. **A reader may take that for
the failures being prevented.** **A rule marked `MECHANISM DEFERRED`
prevents nothing by itself** — it records what should happen and relies
on an author remembering. **Say how many of the new rules carry each
marker**, and **say that the count of `DEFERRED` is the size of what
`C-b` and later work still owe.**

**Second.** **The observed governance failures were not all prevented by
existing mechanisms.** **Some underlying violations WERE mechanically
detected** — `B4`'s commit-hygiene violation was caught by the checker at
exit 2, on an unpushed commit — **but the governance GAPS classified here
were identified, interpreted or repaired through human review or
re-measurement.**

**An earlier version of this section said none was caught by a machine.**
**`B4` refutes it**, and the claim was written in the section warning
against statements whose scope exceeds their evidence. **State the
accurate form**, and **say that writing a rule down is not detection**,
without overstating how little the machines did.

**Third.** **The classification these rules come from is a list of what
was noticed, not a survey.** Several items were found only because a
later task tripped over them. **Say that the rule set covers the observed
failures and is silent about the unobserved ones.**

## 8. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`bec0117168144d54fb23338b673cf7a7e4771868`. **The supplied classification
artifact digests to
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9`.**
**Any mismatch → STOP.** Report both. Report the Git blob id of
`CONVENTIONS.md`.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — The traceability matrix**, per §3. **Report it in full.**
**Thirteen rows, each item exactly once, each mapped to a named rule or
amendment.** **Report the count of rows and confirm it is thirteen.**

**A4 — Mechanism markers.** **Every rule or amendment this task writes
carries exactly one marker.** **Report the full list with its marker**,
and **report the count of each of the three markers.** **A rule without a
marker is a STOP.**

**A5 — The four known assignments verified.** For `A1`, `A3`, `B2` and
`B3` — §2's assignments — **verify each against the repository and report
CONFIRMED or MISSTATED with the evidence.** **`B2`'s claim that
`tests/test_gate_pins.py` exists and fails on a stale pin is checkable
without constructing a stale tree: read the file.** **Do not construct
one; that measurement was made and reported by an earlier task.**

**A6 — Placement justified per principle**, per §4. For each, report
whether it is an amendment or a new numbered rule, **and the
justification.** **Amendments name the rule they modify.** **New rules
are numbered from 19 upward with no gap.** **The next amendment letter is
`M` and no `J` is created.**

**A7 — Nothing existing renumbered or re-worded.** Diff `CONVENTIONS.md`
base to head and **report it in full.** **Every hunk must be an
addition.** **A hunk that deletes or alters an existing rule's text is a
STOP**, and **report the count of deleted lines, which must be zero.**

**A8 — Rule and amendment counts after.** Report the numbered-rule count
and the amendment letters present. **Both must have grown by exactly the
number of new rules and new amendments A6 reports**, and **the pre-existing
eighteen rules and eleven amendments must all still be present.**

**A9 — `E2`'s sentence adopted verbatim.** Diff the adopted wording
against §5's and **report that they correspond.**

**A10 — `B4`'s open question decided.** **Report which you chose** — every
affected check re-run, or only the failing one — **and report the sentence
stating that the ratified instance did not settle it.**

**A11 — Scope, frozen manifest.**

    stated: 3 additions, 1 modification
    base: bec0117168144d54fb23338b673cf7a7e4771868
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md
      specs/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md
    modify:
      CONVENTIONS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `CONVENTIONS.md` is the only file this task changes.**

**A12 — Protected paths.** Every path existing at the evidence base other
than `CONVENTIONS.md` is blob-identical at the head. **In particular
`GATES.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`, and everything
under `scripts/`, `tests/`, `results/` and `derivations/`.** Compare path
by path and report the count.

**A13 — Gate invariants.** `^## P2-` count **14**; `P2-PHASE-01` reads
`Status: PROPOSED`; both prerequisites read `SATISFIED`; both pins match
their targets. **Report all four.** **`CONVENTIONS.md` is referenced
thirteen times in `GATES.md` and is not pinned by digest** — **verify
that and report it**, because a task that modified a pinned file would
owe a re-pin and this one must establish that it does not.

**A14 — The checker over this task's own range**, base `bec01171…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4.

**A15 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected: unchanged at 310 passed, 2 deselected** — this task adds no
test. **A change is a finding and must be explained.**

**A16 — Commit-message hygiene** on all four commits. **`F1` says your
harness will try; report what happened per commit.** **Commits 1–3 go in
the report; commit 4 is post-report evidence.**

## 9. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md
    commit 3  CONVENTIONS.md
    commit 4  reports/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Committed report — measured at commit 3:** A1–A13, A15 and A16;
**A14's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A11's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the push;
the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 10. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and
  `CONVENTIONS.md`. **Nothing else.**
- **No deletion from `CONVENTIONS.md`, for any reason.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not mark a mechanism as EXISTS without naming and verifying it.**
- No force-push, no history rewrite, no branch deletion. **`B4`'s
  ratification covers a past instance and confers nothing here** — and
  **writing the durable form of `B4` in this task does not make it
  operative for this task**, since rules bind prospectively from their
  landing.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 11. Report contract

- everything in §9 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's thirteen-row matrix in full**, with the row count;
- **A4's marker list and the count of each marker**;
- **A5's four verifications**, CONFIRMED or MISSTATED with evidence;
- **A6's placement justification per principle**;
- **A7's full diff**, with the deleted-line count confirmed zero;
- **A8's before-and-after counts**;
- **A10's decision on `B4`**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  and the measured RUN 1 subject set;
- **A15's counts**;
- **how many of the new rules carry `MECHANISM DEFERRED`**, stated as
  what `C-b` and later work still owe;
- **whether writing these rules made you want to write the mechanism.**
  **Say so, and confirm you did not**;
- **§7's three Rule 16 junctions**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 12. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view, and no
statement below is clone-dependent.**

    target      CONVENTIONS.md's shape
    method      grep -cE '^### [0-9]+\.'; grep -oE 'Amendment [A-Z]\b'
                | sort -u; wc -l; grep -c CONVENTIONS on GATES.md
    MEASURED    18 numbered rules; amendments A-I, K, L — eleven, no J;
                1022 lines; referenced 13 times in GATES.md.

    target      the two forms and how they differ
    method      read the file structure and one amendment in situ
    MEASURED    numbered rules sit under two '## ' sections. Amendments
                are embedded INLINE beneath the rule they modify:
                Amendment H sits under '### 3. Declared frozen scope is
                normative'. AN AMENDMENT MODIFIES A RULE IN PLACE; A
                NUMBERED RULE STANDS ALONE.

    target      the eighteen rule titles
    method      grep -nE '^### [0-9]+\.'
    MEASURED    the list reproduced in §4, read from the file.

    target      whether CONVENTIONS.md is pinned by a gate
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md and read the
                path named above each
    MEASURED    TWO pins, naming the adopted parameter-domain artifact
                and the adopted admissibility contract. NEITHER names
                CONVENTIONS.md. This task therefore owes no re-pin, and
                A13 requires that verified rather than assumed.

    target      the classification artifact
    method      sha256sum of the supplied file
    MEASURED    1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9

    target      the suite at the evidence base
    method      the previous task's post-report evidence
    MEASURED    310 passed, 2 deselected. A15 expects it unchanged.
    NOT MEASURED by this author in this session; it is quoted from the
                previous task's report and A15 requires it re-measured.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                bec01171 and executed — not re-implemented
    MEASURED    one scope block; stated 3 additions, 1 modification;
                the manifest lists three and one; parse OK, counted
                equals stated.
