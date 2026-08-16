# Task specification — integrate the pin-test newline repair, and land it

Specification evidence base: `bfef924c368658cac85c04ed18d96eb4450afba6`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   governance/integrate-pin-test-repair
    Cut from           authoritative main — refs/remotes/origin/main
    Source             governance/repair-pin-test-newline
                       202914f5…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `bfef924c…`, **5 additions and 1 modification at
the merge commit**, and **the suite at the merged head reports 324
passed, 2 deselected.** **Any conflict is an immediate STOP.**

---

## 0. What lands

**One line.**

    -    artifact.write_text("content\n", encoding="utf-8")
    +    artifact.write_text("content\n", encoding="utf-8", newline="")

**`tests/test_gate_pins.py`, one line added and one deleted.** Assertions,
`_HEX_A` and the fixture string untouched.

**What it repairs.** `test_a_stale_pin_is_detected` stated a byte
expectation — `b"content\n"` — while creating its fixture through a
platform-translating text mode. **On Windows the written bytes are
`b"content\r\n"`, and the second assertion cannot hold.** The digests
reproduce to the digit: `434728a4…` for LF, `fc06f482…` for CRLF.

**`_HEX_A` is `"a" * 64`**, and **both digests differ from it on every
platform**, so the first assertion is not the failure site. **An earlier
draft of the repair specification claimed otherwise under a `MEASURED`
label without the constant having been read; the Reviewer refuted it and
the specification records the retraction.**

## 1. The finding that inverts the usual reading

**`docs/local/execution_environment.md` declares the execution
environment to be Windows.**

**So the platform on which this test failed is the DECLARED one, and
every Linux environment in which this suite's results have been produced
is undeclared.**

**This is not "a Linux check misreporting on Windows".** **It is a check
written on an undeclared platform, failing on the declared one.**

**Report this**, and **report that it strengthens rather than weakens the
repository-defect classification**: the defect survived because
declaration and practice diverged and **nothing compares them.**

## 2. What this does NOT establish

- **One call site is repaired, not a class.** **Seventeen other
  `write_text` calls in `tests/` carry the same assumption**, including
  a second call in the repaired file at line 143. **None fails today.**
  **Nothing prevents the next author writing the same defect.**
- **No mechanism was added.** No `conftest.py`, no helper, no lint rule.
  **The source task reported that as its strongest temptation and
  declined it** — a mechanism arriving as a side effect of a one-line
  repair would come without review, scope manifest, or a decision that
  the suite should adopt it.
- **Nothing establishes that other validators are free of the same class
  of assumption.** **The source task did not look, and said so.**
- **The source repair task did not observe the Windows failure
  locally.** **Its Windows effect remains `DERIVED` in this task** — from
  the reported remote failure plus `newline=""`'s documented behaviour.
  **Say so.**

  **An earlier draft said the behaviour was "never observed by anyone in
  this programme's own runs".** **That is a global historical claim no
  provenance search supports**, and it contradicts the same sentence's
  reliance on a remote executor's report — **which was itself an
  observation.**

## 3. The environment finding, carried and not registered

**The source task's container was not conformant**, and Rule 13's
diagnostic order with Amendment D's step 0 is what caught it:

    (0) location    only that task's worktree existed
    (4) workspace   SHALLOW clone, 142 commits
    (5) packages    pytest, numpy, sympy ABSENT

**The first pytest invocation gave 5 failed, 319 passed, 2 deselected —
all five `git rev-parse … Needed a single revision`, none touching the
pin test.** **A report of five failures taken at face value would have
sent the programme after a defect that does not exist.**

**Two restorations were made under Rule 13's standing authorisation** —
packages installed, `git fetch --unshallow` (142 → 423 commits) — **and
no repository content was touched to make the environment work.**

**Report this.** **Do not register it** — the governance debt register is
frozen at eleven.

**And report the source executor's own `OBSERVATION_METHOD_ERROR`**: its
first instinct on the missing interpreter was to reach for a working one
rather than diagnose, **which is how an environment defect gets absorbed
instead of found.**

## 4. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file.** There are no authorised modifications.
- **Do not repair the other seventeen call sites**, and **do not add a
  `conftest.py`, helper, or lint rule.**
- **Do not push, move, or fast-forward any session branch.** **The
  source task measured a local session branch sitting exactly at
  `origin/main` with zero commits ahead, and a stale remote pointer at
  the merge-base**; the apparent "405 commits" was `main`'s own published
  history becoming countable after `--unshallow`. **It declined to push
  and reported instead.** **This task does the same.**
- **Do not normalise the `origin` URL.** The source measured it without a
  `.git` suffix and **neither stopped nor silently normalised it**,
  because `A1`'s stop is scoped by its own words to the ref, which
  matched. **Report the URL as measured and do the same.**
- **Do not add a register entry anywhere.**
- **Do not claim this GUARANTEES `D-1`'s completion.** **This removes
  the pin-test blocker.** **It does not establish that `D-1` will
  complete successfully on its next execution, and it does not establish
  that no further blocker exists.**

  **Equally, do not write that `D-1` remains blocked.** **The absence of
  a proof that no unknown obstacle exists is not evidence that a known
  one does.** §7 governs.

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured
— **report it verbatim, including whether it carries a `.git` suffix, and
do not normalise it.** **Confirm it identifies
`zetacheng/2-emergent-gravity`.** Fetch, then report
`refs/remotes/origin/main` and confirm it is
`bfef924c368658cac85c04ed18d96eb4450afba6`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.** Report
`governance/repair-pin-test-newline` and confirm it is `202914f5…`, and
**that it is not an ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, BEFORE any measurement.** **Run Rule
13's diagnostic order including Amendment D's step 0**, and **report
location, workspace depth, and package availability.**

**Report whether the clone is shallow and the commit count.** **If any
restoration is needed, report it in one line each and confirm no
repository content was touched.**

**This criterion exists because the source task's container was not
conformant and its first pytest run gave five failures that had nothing
to do with the subject.** **A suite result taken before this check is
uninterpretable.**

**A4 — Merge parentage, three separately derived measurements**, with
parent 1 this task's review commit, parent 2 `202914f5…`, and the
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The diff at the merged head.** Report `git diff` for
`tests/test_gate_pins.py`, base to head, in full. **Exactly one line
added and one deleted.** **Report the numstat.** **Confirm the assertions,
`_HEX_A` and the fixture string are unchanged.**

**A7 — The suite at the merged head.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts.** **Expected 324
passed, 2 deselected** — measured by the Researcher at the merged head in
a dry run, 25.6 seconds. **A different count is a finding and must be
explained**, and **if it is 5 failed / 319 passed, re-read `A3`.**

**A8 — Scope, frozen manifest. Final base-to-head scope: 6 additions and
1 modification.**

    stated: 6 additions, 1 modification
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: bfef924c368658cac85c04ed18d96eb4450afba6
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
      reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
      specs/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
      specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
    modify:
      tests/test_gate_pins.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive from the source — three additions and one
modification — and three are authored here.** **Report the ARRIVING PATH
count and the ARRIVING ADDITION count separately, and state whether they
coincide.** **They do not: four paths, three additions.**

**At the merge commit the count is 5 additions and 1 modification.**
**Report which head each figure was measured at.**

**The arriving filenames carry the source task's own `{HHMM}Z` token,
which this specification does not know.** **Report the actual arriving
paths as measured and confirm they match this manifest in every
component but that token.**

**A9 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the blob comparisons. **All four arriving paths blob-identical
to the source tip.**

**A10 — Protected paths.** Every path at the evidence base other than
`tests/test_gate_pins.py` is blob-identical at the head. **Report the
count compared**, and confirm explicitly for `GATES.md`,
`CONVENTIONS.md`, `docs/GOVERNANCE-DEBT.md`, `docs/local/execution_environment.md`,
and everything under `scripts/`, `derivations/` and `results/`.

**A11 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match their targets. **Report all four.**

**A12 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A13 — The checker over this task's own range**, base `bfef924c…`, head
**commit 3, the merge commit**. Two runs, `RUN 1` observational and
`RUN 2` naming only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` has two specifications in range**;
**report what it actually did.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A14 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
    commit 3  --no-ff merge of 202914f5…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A12 and A14 for commits
1–3; **A13's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A8's final scope stated
as INTENDED, with the measured 5/1 figure at commit 3.**

**Post-report evidence, NOT written back:** A8's final scope measured
base-to-commit-4; A13-final; A7 and A11 re-run after the advance; A14 for
commit 4; the push; remote `main` read back; final ancestry confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The advance
is a fast-forward; `bfef924c…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no other
ref.** **The source branch is not deleted and does not move**; verify and
report its tip.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **This closes one known blocker.** `D-1` has stopped four
times — a scholarly-egress precondition, a lagging local ref, the wrong
repository, and this test.

**Report whether any other KNOWN blocker remains**, and **do not infer
from their absence that no unknown blocker exists.**

**`D-1`'s literature question remains unanswered** — that is a fact about
what has been done, not about what stands in the way. **Do not write that
`D-1` is still blocked**, and **do not write that it will now complete.**
**An earlier draft of this junction said the repair "does not unblock"
`D-1`, inferring a present obstruction from the absence of a proof that
none exists.** **That inference does not hold.**

**Second.** **One call site is repaired and seventeen carry the same
assumption.** **Report the count**, and **say that the defect class is
open while the instance is closed.**

**Third.** **The declared execution environment is Windows and this
suite's results have been produced on undeclared Linux environments.**
**Report that**, and **say that nothing in the repository compares the
declared environment to the one in use** — which is why the defect
survived.

**Fourth.** **The source task's container was non-conformant and its
first suite run gave five unrelated failures.** **Say that a suite result
is uninterpretable before Rule 13's diagnostic order has been run**, and
**that this task ran it.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run and reported rather than assumed.** **Rule 13
  carries two such orders, a known open item; if no environment failure
  occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL**, including the `.git` question, **not
  normalised**;
- **A3's environment diagnosis in Rule 13's order**, with any
  restoration reported in one line each;
- **A4's three values, separately derived**;
- **A6's full diff and numstat**;
- **A7's counts**;
- **A8's two scope figures, the arriving-path and arriving-addition
  counts stated separately with the statement that they do NOT
  coincide**, and the actual arriving paths as measured;
- **A9's merge case, stated BEFORE the blob comparisons**;
- **A10's path count**;
- **A11's four invariants**;
- **A12's six exit statuses, before and after**;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  **confirmation that no session branch was pushed**;
- **§7's four Rule 16 junctions**;
- **whether integrating a one-line repair made you want to fix the other
  seventeen or add a helper.** **Say so, and confirm you did not** —
  **the source task named this its strongest temptation**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the repository, the base, and the source
    method      git remote get-url origin; git fetch; git rev-parse
    MEASURED    https://github.com/zetacheng/2-emergent-gravity.git in
                the Researcher's clone; origin/main =
                bfef924c368658cac85c04ed18d96eb4450afba6;
                governance/repair-pin-test-newline = 202914f5…, NOT an
                ancestor of main.
    NOTE        the source executor measured its own origin URL WITHOUT
                a .git suffix. Both identify the same repository. A1
                requires the URL reported verbatim and not normalised.

    target      the merge and the suite at the merged head
    method      dry run from bfef924c with two placeholder commits, then
                git merge --no-ff; then python3 -m pytest -q
    MEASURED    CLEAN; merge-base = bfef924c; 5 additions and 1
                modification at the merge commit; 6 and 1 with a
                placeholder report; bfef924c is an ancestor of that
                head. THE SUITE AT THE MERGED HEAD: 324 passed, 2
                deselected in 25.6 seconds.

    target      the change itself
    method      git diff bfef924c 202914f5 -- tests/test_gate_pins.py
    MEASURED    exactly one line added and one deleted; numstat 1 1. The
                added line is the same call with newline="" appended.

    target      _HEX_A, read rather than inferred
    method      read line 138 of tests/test_gate_pins.py and evaluate it
    MEASURED    "a" * 64. Both 434728a4… and fc06f482… differ from it on
                every platform, so the first assertion is not the
                failure site.

    target      the declared execution environment
    method      read docs/local/execution_environment.md at the source
                tip
    MEASURED    it declares a Windows execution environment, naming
                C:\\p2-validator and Windows-specific concerns. The
                source executor's inversion is confirmed: the failing
                platform is the declared one.

    target      the seventeen other call sites
    method      grep write_text and newline= across tests/
    MEASURED    EIGHTEEN calls, ZERO with newline=; after the repair,
                seventeen remain without it, including a second call in
                the repaired file.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 6 additions, 1 modification;
                parse OK, counted equals stated per category.
