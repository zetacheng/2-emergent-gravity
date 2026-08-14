# Task specification — integrate the P7 repair and the pin validator, and land it

Specification evidence base: `88ef5eec08ab269eddcea8c617cf4f5b09b7336e`

    Branch to create   governance/integrate-p7-repair
    Cut from           authoritative main @ 88ef5eec…
    Source             governance/p7-repair-and-pin-validator
                       7102a60ef249da04e2ad3326a3b8135b688aa065

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base with the
specification and review commits in place: **no conflict**, merge-base
`88ef5eec…`, **6 additions and 3 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**`governance/p1-declared-total` is NOT integrated here** and its `A10`
is not discharged. §1a records what was measured about the two and what
that measurement does not support.

---

## 0. What lands

**Two checks that work, and one that did not.**

    the gate-heading grammar        14 of 14 real headings, where the
                                    landed one matched 0
    the completeness invariant      parsed sections must EQUAL the raw
                                    '^## P2-' count, or NOT_PARSEABLE
    tests/test_gate_pins.py         every GATES.md pin hashed against
                                    its target, on every suite run

**The suite gains detection power it did not have.** Measured by the
source task in a detached worktree, on the same deliberately stale pin:

    pre-repair    280 passed, exit 0
    post-repair   1 failed, 300 passed

**That is the gap this merge closes**: four consecutive tasks reported
`280 passed, 2 deselected` across revisions spanning a stale pin, a
repaired pin, an edited artifact and a re-pinned one, **and the count
never moved.**

## 1. What this does NOT establish

- **Governance is not enforced.** The classification still records
  **twenty-two of twenty-nine objects with no machine behind them**, and
  `P7` remains `PARTIAL` — the authorised-set discovery problem is
  untouched by this merge.
- **Two checks now work. That is the whole claim.**
- **`P7` returning `PASS` still means only what its inputs allow.** It
  now means *fourteen sections parsed, none changed without
  authorisation*, where before it meant *zero compared against zero*.
  **The improvement is that the sentence has content, not that the
  content is large.**
- **Nothing here bears on `P1`'s undischarged `A10`.**
- **`F1` and `F2` arrive unrepaired** — the harness's forbidden trailer,
  and `frozen Wilson D` at line 73 of the exploratory script. **Report
  them; do not fix them.**

## 1a. What was measured about `P1` and `P7`, and what it does not support

**Both integration orders were dry-run from this evidence base.**

    P7 then P1    P1 merges CLEAN; auto-merge of task_checker.py,
                  tests/test_task_checker.py and the classification
    P1 then P7    P7 merges CLEAN; the same three auto-merged

**That establishes TEXTUAL merge cleanliness in both orders. It
establishes nothing about the merged code being correct.** The three
shared files were auto-merged, and **an auto-merge is a statement about
line adjacency, not about whether `parse_scope_block` and
`gate_sections` still do their jobs side by side.**

**So: this specification claims that the P1 integration will not be
blocked by a textual conflict, and claims nothing further.** **Whoever
integrates `P1` must measure the merged behaviour** — at minimum, run the
full suite at the merged head and confirm `P7` still reports fourteen of
fourteen and `P1`'s declared-total grammar still parses its own
specification.

**An earlier specification in this line claimed order-independence from
evidence covering one file of three, and withdrew it.** **This section
exists so that the narrower claim does not drift back into the wider
one.**

## 2. What this task must not do

- **Do not touch `main` until §6's landing**, and do not merge anything
  but the named source.
- **Do not merge `governance/p1-declared-total`**, and do not discharge
  its `A10`.
- **Do not modify any arriving file.** The parser, the tests and the
  classification are integrated exactly as reviewed.
- **Do not modify `GATES.md`.** The source did not, and this task must
  not — **the new grammar reads that file, and changing it during the
  merge that lands the grammar would make the first meaningful `P7`
  result untrustworthy.**
- **Do not fix `F1` or `F2`.**
- **Do not extract the duplicated gate-heading grammar into a shared
  helper.** §7 records why it is a finding and not this task's work.
- **Do not write a superseded-register entry.** Nothing is superseded.

## 3. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`88ef5eec08ab269eddcea8c617cf4f5b09b7336e` and
`governance/p7-repair-and-pin-validator` to
`7102a60ef249da04e2ad3326a3b8135b688aa065`. **Any mismatch → STOP.**
**Also report `governance/p1-declared-total`'s tip and confirm it is
unchanged at `8ff032e7…` after this task.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 7102a60ef249da04e2ad3326a3b8135b688aa065
    merge-base(parent 1, parent 2)
             = 88ef5eec08ab269eddcea8c617cf4f5b09b7336e

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.
**The merge-base equals the evidence base and NOT parent 1.**

**A4 — No conflict.** Report the merge's conflict list. **It must be
empty.** **Any conflict is a STOP.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 7 additions and
3 modifications.**

    stated: 7 additions, 3 modifications
    base: 88ef5eec08ab269eddcea8c617cf4f5b09b7336e
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md
      reports/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
      reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
      specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md
      specs/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
      tests/test_gate_pins.py
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Ten paths.** **At the merge commit, before the report exists, the count
is 6 additions and 3 modifications.** **Report which head each figure was
measured at.**

**A6 — SOURCE-BRANCH artifacts intact.** **Of the nine paths changed
base-to-merge-commit, SEVEN are contributed by source branch
`7102a60e…`** — its four added paths and its three modified paths.
**Compare those seven at the merge commit against the source tip and
require blob identity. Report all seven.**

**The other two additions are this integration task's own specification
and review**, written here and existing on no source branch. **They are
outside this comparison by construction, not by omission.**

    at the merge commit          9 changed paths
      from the source branch     7  ← A6 compares these
      authored by this task      2  (this specification, this review)

**The count is spelled out because 6 additions at the merge commit, 7
source paths and 9 changed paths are three different figures that all
appear in this specification**, and an earlier version of this criterion
said "arriving paths" without saying which.

**A7 — `GATES.md` untouched.** Blob-identical at the evidence base and at
the head — `2b3bd5069414f009e1a0466c4990db2949519bd8`. **Report both.**
**A difference is a STOP**, and it would invalidate A8.

**A8 — The first meaningful `P7`, measured at the merged head.** Run the
integrated `gate_sections` and the raw counter against `GATES.md` at the
head and **report three numbers**:

    raw '^## P2-' count          expected 14
    parsed section count         expected 14
    equality holds               expected true

**Also report what the PRE-MERGE grammar returns on the same file** —
expected **zero** — **so that both numbers come from one measurement
rather than from this specification.**

**A `P7` `PASS` at the head with a section count of zero is a STOP.**

**A9 — Both pins match at the head.** For each occurrence of
`` (sha256 `<64 hex>`) `` in `GATES.md`, resolve the artifact path named
immediately above it, hash it at the head, and report the pair.
**Expected: two pins, both matching, both unchanged from the evidence
base.** **Assert the count is at least one**, and **report the count
found.**

**A10 — The pin validator runs in the suite.** Run `python -m pytest`
from the repository root at the head and **report the pass and deselect
counts.** **The count MUST rise from 280.** **Report the delta and what
accounts for it**, and **confirm `tests/test_gate_pins.py` was
collected** — a delta that did not include it would mean the file
landed without being run.

**A11 — Protected paths.** Every path existing at the evidence base other
than the three in A5's `modify:` list is blob-identical at the head. **In
particular `GATES.md`, `CONVENTIONS.md`, `DECISION_LOG.md`,
`docs/BRANCHING_POLICY.md`, everything under `results/`, and every other
file under `scripts/`.** Compare path by path and report the count.

**A12 — Gate invariants.** `^## P2-` count **14**; `P2-PHASE-01` reads
`Status: PROPOSED`; both prerequisites read `SATISFIED`; every `Status:`
line textually identical to the evidence base. **Report all four.**

**A13 — Superseded branches not merged, all six.** No commit in the
register is an ancestor of the head:

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A14 — The checker over this task's own range**, base `88ef5eec…`, head
**commit 3, the merge commit** — not commit 4, which is the report that
must carry this output. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-p7-repair.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.** **`authorised_modified_gates` IS
`[]`, and here that is truthful**: no gate may change in this task.

**`P7` in RUN 2 is running the repair it is integrating.** **Report the
section count it saw.** **`PASS` at fourteen sections is the expected
result; `PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **If it fails, STOP before advancing `main`.**

**A15 — Commit-message hygiene** on all four commits including the merge.
**`F1` says your harness will try; report what happened per commit.**
**Commits 1–3 go in the report; commit 4 is post-report evidence.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
    commit 3  --no-ff merge of 7102a60e…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-p7-repair.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A13 and A15 for commits
1–3; **A14's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A5's final scope stated
as INTENDED, with the measured 6/3 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A14-final; A9, A10 and A13 re-run after the advance;
A15 for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 5. Landing preconditions specific to this merge

**Do not advance `main` unless A8 reports fourteen parsed of fourteen
raw, and A10 reports a risen count including `tests/test_gate_pins.py`.**

**These two are the reason the merge exists.** **A landing that carried
the files without the behaviour would put a repaired parser on `main`
while leaving the vacuous result in place**, and nothing downstream would
notice — which is the failure mode this whole line has been chasing.

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward. Verified available:** `88ef5eec…` is the
base of this branch. **Verify `--is-ancestor` before the push and report
the exit status as a measurement.** **If a fast-forward is not available,
STOP.**

**Push without `--force` and without `--force-with-lease`.**

**`governance/p7-repair-and-pin-validator` is not deleted and does not
move.** Verify and report its tip after the advance.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** After this lands, `P7` reports a real number and a pin
validator runs on every suite invocation. **A reader may take that for
governance being enforced.** **Twenty-two of twenty-nine objects still
have no machine behind them.** **Say where a reader meets that.**

**Second, and it is the finding worth carrying forward.** The source task
discovered that `tests/test_repository_structure.py` **already contained
a working gate-heading pattern with a non-empty guard**, at the same
revision as the broken parser, **and nothing had ever compared them.**
**After this merge the repository holds TWO gate-heading grammars that
happen to agree.** **Nothing keeps them agreeing.** **State that; do not
unify them here** — the unification, or an invariant test requiring both
to return the same id set, belongs to the conventions task.

**Third.** **The pin validator's own non-empty assertion is a guard of
the kind it exists to enforce, written by the same hand.** **Say what
would detect the pin validator going vacuous**, and **do not build it
here.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify no arriving file, and modify `GATES.md` for no reason.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not claim, in the report or the commit messages, that `P1` and
  `P7` are order-independent.** §1a says what was measured.
- No force-push, no history rewrite, no branch deletion. **The
  ratification recorded for a past unpushed amend confers nothing here.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §4 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's three values, separately derived**;
- **A5's two scope figures**, with the head each was measured at;
- **A6's seven source-branch blob comparisons**, with the two
  task-authored additions named as excluded and why;
- **A8's three numbers plus the pre-merge grammar's zero**, all from one
  measurement session;
- **A9's pin table** and the count found;
- **A10's counts, the delta, and confirmation `tests/test_gate_pins.py`
  was collected**;
- **A11's path count**;
- **A12's four gate invariants**;
- **A13's six exit statuses, before and after the advance**;
- **A14's two runs**, both configs verbatim, **the section count `P7`
  saw**, and the measured RUN 1 subject set;
- **A15 per commit**, and whether your harness attempted a forbidden
  trailer;
- **`F1` and `F2` reported as arriving and unrepaired**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§7's three Rule 16 junctions**, including the two coexisting
  grammars;
- **whether `main` now reads as though governance were enforced.** It is
  not;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view, and no
statement below is clone-dependent.**

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    main = 88ef5eec08ab269eddcea8c617cf4f5b09b7336e;
                governance/p7-repair-and-pin-validator =
                7102a60ef249da04e2ad3326a3b8135b688aa065; the source is
                NOT an ancestor of main

    target      the merge
    method      dry run from 88ef5eec with a placeholder specification
                commit and a placeholder review commit, then
                git merge --no-ff of the pinned ref
    MEASURED    CLEAN, no conflict; parent 2 = 7102a60e; merge-base =
                88ef5eec; 6 additions and 3 modifications at the merge
                commit; 7 and 3 with a placeholder report; 88ef5eec is
                an ancestor of that head, so the landing fast-forward is
                available.

    target      the repaired grammar at the merged head
    method      apply the integrated GATE_HEADING and the raw counter to
                GATES.md in the dry-run tree
    MEASURED    raw 14, parsed 14, equality holds.

    target      the grammars, at the source head
    method      read GATE_HEADING and RAW_GATE_HEADING from
                task_checker.py at 7102a60e, then apply each and the
                pre-repair expression to GATES.md
    MEASURED    GATE_HEADING = ^## (P2-[A-Z0-9-]+)[ \\t]+[—–-][ \\t]+\\S.*$
                RAW_GATE_HEADING = ^## P2-
                raw 14; pre-repair grammar 0; repaired grammar 14.
                The raw counter does not use the grammar it guards.

    target      the pin validator's guards
    method      read tests/test_gate_pins.py at 7102a60e
    MEASURED    test_pin_set_is_not_empty and
                test_every_pin_resolves_to_a_path are present, alongside
                the per-pin hash comparison.

    target      GATES.md across the source branch
    method      git rev-parse <rev>:GATES.md
    MEASURED    2b3bd5069414f009e1a0466c4990db2949519bd8 at both
                88ef5eec and 7102a60e. The source modified no gate.

    target      both integration orders with governance/p1-declared-total
    method      two dry runs from 88ef5eec: P7 then P1, and P1 then P7
    MEASURED    both CLEAN; task_checker.py,
                tests/test_task_checker.py and the classification were
                AUTO-MERGED in each.
    SCOPE OF THE ABOVE
                this establishes TEXTUAL merge cleanliness in both
                orders and nothing about the merged code being correct.
                An auto-merge is a statement about line adjacency. §1a
                states the narrower claim and requires the P1
                integration to measure merged behaviour.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 3 modifications;
                the manifest lists seven and three; parse OK, counted
                equals stated.
