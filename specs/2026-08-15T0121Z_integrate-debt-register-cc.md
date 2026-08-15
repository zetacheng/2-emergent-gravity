# Task specification — integrate the governance debt register, and land it

Specification evidence base: `80595d4cd575d1d024d1415b9b599947bf847677`

    Branch to create   governance/integrate-debt-register-cc
    Cut from           authoritative main @ 80595d4c…
    Source             governance/debt-register-cc
                       023b8b026d8e2040ae818e93e3630e85dee999e3

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `80595d4c…`, **6 additions and 1 modification at
the merge commit.** **Any conflict is an immediate STOP.**

**This is the last task in the `C` line.** `C-a`, `C-b` and `C-c` and
their integrations complete the scoping ruling the PI issued. **Nothing
in that line remains after this lands.**

---

## 0. What lands

**A governance debt register, and one pointer so it can be found.**

    docs/GOVERNANCE-DEBT.md    eleven entries, G-01 to G-11
    CONVENTIONS.md             two lines, a pointer, nothing else

**Dispositions, counted from the file at the source tip:**

    REPAIRABLE            1    G-02
    SPECIFIABLE           3    G-04  G-05  G-06
    NOT REPAIRABLE HERE   1    G-01
    RULED                 1    G-07
    METHOD NOTE           1    G-11
    OPEN                  4    G-03  G-08  G-09  G-10

**`G-09` and `G-10` are `OPEN`, not `SPECIFIABLE`** — an independent
oracle for a grammar and a detector for a vacuous guard are problems
whose shape is not defined, and the source task did not claim one.

**`D4` is not entered.** It is already registered as `OPEN-CC-3` in
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, and the register
cross-references it. **Duplicating it would have created a second place
for one status to drift.**

## 1. What this does NOT establish

- **Nothing in the register is repaired by being written down.**
  **`SPECIFIABLE` means specifiable, not specified.** Three entries name
  a mechanism shape; **none of the three mechanisms exists.**
- **The register has no mechanism of its own.** Nothing requires an
  entry when debt is found, and nothing checks that entries stay
  current. **`G-03`'s reservation applies to this file as much as to the
  `CORRECTIONS.md` it describes.**
- **It is a list of what was noticed, not a survey.** Three entries were
  found only because a later task tripped over them.
- **The governance gap is not closed.** The classification's count of
  objects with no machine behind them is unchanged by this merge.

## 2. Two findings the source task surfaced, carried forward here

**Neither is repaired by this integration, and neither is registered.**
**The register is frozen at eleven and this task does not extend it.**

### 2a. A revision-attribution error in the `C-c` specification

**The `C-c` specification stated `13 of 50` for `f179b45e…`.** **That
figure belongs to `bec01171…`.** Measured, at three revisions:

    bec01171    13 of 50
    f179b45e    15 of 52
    80595d4c    17 of 54

**The number was right and the anchor was wrong.** It was measured while
the `C-a` specification was being written, against `bec01171…`, and
carried into `C-c` with a different revision attached.

**The executor did not take the specification's figure as true. It
re-measured and corrected the attribution in its report.** **That is the
behaviour `A5` was written to produce**, and it worked.

**Report this correction. Do not register it.**

### 2b. The classification artifact is not in the repository

**`C-a` and `C-c` both cite the governance debt classification —
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9` —
as the source of the `C1`–`C5` and `D1`–`D4` identifiers.** **That
artifact was never committed.**

**So a reader of `main` can see debt identifiers referenced and cannot
reconstruct their authoritative definitions.** **This is a provenance
gap, not a discoverability one**: the file is not merely hard to find,
it is absent.

**IDENTIFIED BUT NOT REGISTERED BY THIS TASK.** **Say exactly that.**
**Do not imply it is registered, and do not add a twelfth entry** — the
register's scope is frozen, and a register that grows during its own
integration has no frozen scope either.

**A later task may register it.** **This one records that it was
found.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any arriving file**, including the register.
- **Do not add a twelfth entry**, and **do not change any
  disposition.**
- **Do not register `2b`**, and **do not create the classification
  artifact in the repository.**
- **Do not repair `G-02`.** One line, still out of scope.
- **Do not build `G-04`, `G-05` or `G-06`.**
- **Do not modify `GATES.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md`, or either existing register.**
- **Do not describe the `C` line as closing the governance gap.**

## 4. Acceptance criteria

**A1 — Refs.** `refs/heads/main` resolves to
`80595d4cd575d1d024d1415b9b599947bf847677` and
`governance/debt-register-cc` to
`023b8b026d8e2040ae818e93e3630e85dee999e3`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank or naming a different digest, STOP and say
which.** Report both digests equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 023b8b026d8e2040ae818e93e3630e85dee999e3
    merge-base(parent 1, parent 2)
             = 80595d4cd575d1d024d1415b9b599947bf847677

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.

**A4 — No conflict.** Report the merge's conflict list. **It must be
empty.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 7 additions and
1 modification.**

    stated: 7 additions, 1 modification
    append_only: DECISION_LOG.md
    authorised_gates: []
    base: 80595d4cd575d1d024d1415b9b599947bf847677
    head: <commit 4>
    mode: exact
    add:
      docs/GOVERNANCE-DEBT.md
      reports/2026-08-15T0008Z_debt-register-cc.md
      reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
      reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
      specs/2026-08-15T0008Z_debt-register-cc.md
      specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    modify:
      CONVENTIONS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Eight paths.** **Five come from the source — four additions and one
modification — and three are authored here, all additions.**

    source      4 additions + 1 modification = 5
    this task   3 additions                  = 3
    total       7 additions + 1 modification = 8

**At the merge commit, before the report exists, the count is 6 additions
and 1 modification.** **Report which head each figure was measured at.**

**A6 — Source-branch paths, derived from the SOURCE and not from A5.**
**Report the set of paths `023b8b02…` changes relative to `80595d4c…`.**
**Expected four additions and one modification.** **Report a
disagreement with A5 if one exists.**

**A7 — Which merge case, established BEFORE any blob comparison is
interpreted.** **Report the merge-base and whether `main` has touched
`CONVENTIONS.md` since the source was cut.**

    only one side changed it    merged blob EQUALS the source side, and
                                that is correct
    both sides changed it       merged blob equals one side means a
                                side was LOST

**Report which case applies, and then the blob comparison.** **A blob
comparison reported without its case is uninterpretable.** **If the
two-sided case applies, the line-survival measurement Amendment `P(b)`
mandates is required instead.**

**A8 — `CONVENTIONS.md` grows by addition only, verified two ways.**
**Zero deleted lines**, and **the base file is an exact in-order
subsequence of the merged file** — report the matched count against the
base line count. **Expected 1405 of 1405.** **Two independent
measurements of one property; neither substitutes for the other.**

**Report the rule and amendment counts at the head: twenty-one rules,
fifteen amendment letters A–P, no `J`** — **unchanged**, because the
source adds neither.

**A9 — The register is intact and non-binding.** Report:
**eleven entries `G-01` to `G-11`**; **the disposition of each and the
count of each disposition**, matching §0; **that no entry reads
`CLOSED`**; and **the count of lines containing `MUST`, `SHALL` or
`binds`** — **expected one, the sentence saying nothing in it binds.**
**If that count exceeds one, name each and justify it.**

**A10 — `D4` is cross-referenced, not duplicated.** Report that
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` is **blob-identical at
base and head**, that `OPEN-CC-3` is in it, and that the register points
at it rather than restating it.

**A11 — The two carried findings, reported and not registered.** Report
**§2a's three figures, independently measured at their respective
revisions** — `bec01171…`, `f179b45e…` and `80595d4c…`. **They cannot
all be figures at this base, and an earlier version of this criterion
said they were** — the same anchor error the finding itself records.
**Confirm the register still contains eleven entries.** Report **§2b in the words
`identified but not registered by this task`.** **A report that implies
either is registered fails this criterion.**

**A12 — Protected paths.** Every path existing at the evidence base other
than `CONVENTIONS.md` is blob-identical at the head. **In particular
`GATES.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`, both existing
registers, and everything under `scripts/`, `tests/` and `results/`.**
Compare path by path and report the count.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets**, and **`CONVENTIONS.md` is
named by neither.** **Report all five.**

**A14 — The checker over this task's own range**, base `80595d4c…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`register_path` names `docs/BRANCHING_POLICY.md` and NOT
`docs/GOVERNANCE-DEBT.md`.** **`P4` checks the superseded-branch
register; the file landing here is not that register and this task does
not make it one.** **Say so in the report** — after this merge the
repository holds two files a reader might call "the register", and the
adjacency is exactly what produces a wrong reading later.

**This specification's scope block declares the same two sets, written to
agree with the config.** **Report `declared_source` for each** and
**confirm no `DECLARATION_CONFLICT` arose.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A15 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected: unchanged at 324 passed, 2 deselected** — neither the source
nor this task adds a test. **A change is a finding and must be
explained.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    commit 3  --no-ff merge of 023b8b02…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A13, A15–A17 for commits
1–3; **A14's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A5's final scope stated
as INTENDED, with the measured 6/1 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A14-final; A13 and A16 re-run after the advance; A17
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward. Verified available:** `80595d4c…` is the
base of this branch. **Verify `--is-ancestor` before the push and report
the exit status as a measurement.** **If a fast-forward is not available,
STOP.**

**Push without `--force` and without `--force-with-lease`.**

**`governance/debt-register-cc` is not deleted and does not move.**
Verify and report its tip after the advance.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** After this lands, **the planned `C-a` / `C-b` / `C-c`
sequence is complete**: rules consolidated, two mechanisms built, debt
registered. **That is a plan completing, not governance work
completing.** **A reader may take a completed line for a closed gap.** **Three of eleven entries name a
mechanism that does not exist, four are `OPEN`, and one is not
repairable inside this repository.** **Report the disposition counts
beside any statement that the line is complete.**

**Second.** **The register has no mechanism.** Nothing adds an entry
when debt is found; nothing checks an entry is current. **Say that, and
say that `G-03`'s own reservation applies to the file carrying it.**

**Third.** **§2b's provenance gap is real and unregistered.** **The
identifiers `C1`–`C5` and `D1`–`D4` are cited on `main` and their
authoritative source is not there.** **Say `identified but not
registered by this task`**, and **do not present the register as
covering it.**

**Fourth.** **`main` will carry two files a reader might call the
register.** One is checked by `P4`; the other is checked by nothing.
**Say which is which**, and **say that the second's contents bind
nobody.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify no arriving file, and modify `GATES.md` for no reason.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not add to, remove from, or re-dispose any register entry.**
- **No force-push and no branch deletion.** **No history rewrite except
  the narrowly permitted pre-push hygiene repair under Rule 20.**

  **An earlier version of this clause read "no force-push, no history
  rewrite, no branch deletion except as Rule 20 permits", whose grammar
  attaches the exception to all three.** **Rule 20 permits none of
  force-push or branch deletion**: it permits amending an UNPUSHED
  commit to remove a mechanically detected hygiene violation, and
  nothing else. **The ambiguity is removed here rather than left for the
  executor**, because this specification's own last clause forbids the
  executor from deciding which of two inconsistent instructions
  prevails.
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's three values, separately derived**;
- **A5's two scope figures**, with the head each was measured at;
- **A6's source-derived path set**, and any disagreement with A5;
- **A7's merge case, stated BEFORE the blob comparison**;
- **A8's zero-deletion count, the subsequence match, and the unchanged
  rule and amendment counts**;
- **A9's eleven entries, dispositions, counts, and the binding-vocabulary
  line count**;
- **A10's cross-reference and byte-identity confirmation**;
- **A11's three figures and the `identified but not registered by this
  task` sentence, verbatim**;
- **A12's path count**;
- **A13's five checks**;
- **A14's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, the measured RUN 1 subject set, and **the
  statement distinguishing the two registers**;
- **A15's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§7's four Rule 16 junctions**;
- **whether completing the `C` line made you want to repair `G-02` or
  build `G-05`.** **Say so, and confirm you did not**;
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

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    main = 80595d4cd575d1d024d1415b9b599947bf847677;
                governance/debt-register-cc =
                023b8b026d8e2040ae818e93e3630e85dee999e3; the source is
                NOT an ancestor of main.

    target      the merge
    method      dry run from 80595d4c with two placeholder commits, then
                git merge --no-ff of the pinned ref
    MEASURED    CLEAN; merge-base = 80595d4c; 6 additions and 1
                modification at the merge commit; 7 and 1 with a
                placeholder report; 80595d4c is an ancestor of that
                head, so the landing fast-forward is available.

    target      the merge case for CONVENTIONS.md
    method      the merge-base equals main, so no commit exists on main
                since the source was cut
    MEASURED    ONE-SIDED: only the source changed it. A7 requires this
                re-derived rather than taken from here.

    target      CONVENTIONS.md across the source branch
    method      git diff --numstat; and an in-order subsequence test
    MEASURED    2 lines added, ZERO deleted, one hunk. The base file is
                an exact in-order subsequence: 1405 of 1405. Rules 21,
                amendments A-P, no J — unchanged.

    target      the register at the source tip
    method      count entry headings and Disposition lines; count
                binding vocabulary
    MEASURED    ELEVEN entries G-01 to G-11. Dispositions: 1
                REPAIRABLE, 3 SPECIFIABLE, 1 NOT REPAIRABLE HERE, 1
                RULED, 1 METHOD NOTE, 4 OPEN — eleven, one each.
                MUST/SHALL/binds occurs on ONE line: "Nothing in this
                file binds."

    target      the untouched files
    method      git rev-parse <rev>:<path> at both revisions
    MEASURED    GATES.md, DECISION_LOG.md, docs/BRANCHING_POLICY.md and
                BOTH existing registers are blob-identical.

    target      §2a's three figures
    method      count .md files under specs/ and those carrying a
                'stated:' record, at each of three revisions
    MEASURED    bec01171 13 of 50; f179b45e 15 of 52; 80595d4c 17 of 54.
    RETRACTED   the C-c specification attributed 13 of 50 to f179b45e.
                The figure belongs to bec01171 and was carried across
                documents with the wrong revision attached. The number
                was right; the anchor was wrong.

    target      §2b, the classification artifact
    method      git ls-tree over the whole tree at 80595d4c for the
                classification file
    MEASURED    it is not in the repository at any path. C-a and C-c
                both cite its digest as the source of C1-C5 and D1-D4.
                IDENTIFIED, NOT REGISTERED.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. Both declarations
                present; A14 checks them against the committed bytes
                rather than trusting this line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                80595d4c and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 1 modification;
                the manifest lists seven and one; parse OK, counted
                equals stated per category.
