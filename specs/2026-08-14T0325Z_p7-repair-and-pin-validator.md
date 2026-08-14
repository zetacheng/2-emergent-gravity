# Task specification — repair `P7`, forbid the vacuous pass, and validate the gate pins

Specification evidence base: `88ef5eec08ab269eddcea8c617cf4f5b09b7336e`

    Branch to create   governance/p7-repair-and-pin-validator
    Cut from           authoritative main @ 88ef5eec…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**Cut from `main`, not from `governance/p1-declared-total`.** §1a records
the measurement that makes the two independent.

**Three repairs in one unit, because they close one gap between them.**
Splitting them would land a parser that sees the gates but still cannot
be trusted to fail, or a failure mode with nothing to detect it.

---

## 0. The gap, measured three times over

**`P7` has returned `PASS` while checking nothing, in every task that ran
it — including two that modified `GATES.md` and one that flipped a gate
prerequisite.**

    GATE_HEADING = re.compile(r"^## (P2-[A-Z0-9-]+)\s*$")

**`GATES.md` at the evidence base carries FOURTEEN headings and the
expression matches ZERO of them**, because every real heading carries a
title after an em dash:

    ## P2-HK-01 — Heat-kernel species coefficients
    ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    ## P2-MULTIPHASE-GRAV-01 — Programme-death: does any phase give …

`gate_sections` therefore returns `{}` at both base and head, `check_p7`
compares two empty maps, finds nothing changed, and returns `PASS`.

**"An empty match returning True is the most dangerous kind of green"**
is this programme's own phrasing, recorded in the landed amendments.
**It is now demonstrated in the tool built to prevent it.**

**And the suite cannot see it.** Measured across four revisions spanning
a stale pin, a repaired pin, an edited artifact and a re-pinned one:
**280 passed, 2 deselected — the count never moved.** **A suite invariant
across the property in question is not testing that property.**

## 1. What is built

### (a) A grammar that matches the real headings

**Replace `GATE_HEADING` so that it matches every one of the fourteen**
and captures the gate id alone. The shape is `## <id> — <title>`, where
the id is the existing `P2-[A-Z0-9-]+` and the title is free text after a
separator.

**Define the separator you accept and state it.** **Do not accept a bare
`## P2-…` with no title as equivalent unless you say so and fixture it.**
**Report the count matched: fourteen, or your number with the list.**

### (b) A heading-completeness invariant, and it is the point of the task

**Count independently every line matching `^## P2-`. `check_p7` MUST NOT
return `PASS` unless the number of parsed gate sections EQUALS that raw
count.** **Any raw `P2` heading the grammar does not recognise makes `P7`
return `NOT_PARSEABLE`.**

**`NOT_PARSEABLE`, not `FAIL`, and the choice is fixed here rather than
left open.** The state means *the grammar cannot fully read the gate
registry*, **not** *an unauthorised gate change has been shown*. **Cannot
judge is not judged wrong** — the same distinction `P1` already carries.

**Equality, not merely non-zero, and this is the substantive point.** A
guard that fires only at zero closes one instance and leaves the defect
class open: **a grammar that parses fourteen of fifteen headings would
still return `PASS`**, because the fourteen it sees are unchanged and the
one it misses is invisible to it. **The failure this task exists to
prevent is a gate going unseen, and one unseen gate is enough.**

**The count is taken over a cheap independent signal precisely so that it
does not depend on the grammar it guards.** **A guard written in terms of
the parser it protects would fail with it.**

**Both sides are counted.** The equality must hold at base and at head;
**a heading that parses at one revision and not the other is exactly the
case the invariant is for.**

**And the all-zero case is fixed here rather than left to the
executor: if the independent raw heading count is ZERO, `P7` returns
`NOT_PARSEABLE`.** **A gate file in which the grammar finds no readable
gate is not a file that has been checked**, whatever the parsed count
equals. **The same reasoning as above: the registry could not be read,
which is not the same as having been read and found clean.**

**This must hold even when the authorised set is empty and even when base
and head are identical.** **Zero sections is never a clean bill of
health, and neither is thirteen of fourteen.**

### (c) A pin validator that runs in the suite

**Add a test under `tests/` that, for every occurrence of
`` (sha256 `<64 hex>`) `` in `GATES.md` at the working revision, resolves
the artifact path named immediately above it, hashes that file's bytes,
and fails on any mismatch.**

**It must also fail if it finds ZERO pins.** **A pin validator that
passes on an empty pin set is the same defect as `P7`'s**, one level
along, and this programme has now met that shape twice.

**Why a test and not a checker property.** The measured failure was that
**the suite could not distinguish a stale pin from a correct one**. A
checker property runs when someone invokes the checker with a config; a
test runs whenever anyone runs the suite. **The demonstrated gap is the
suite's, so the repair goes in the suite.** **If you also want a checker
property, say so and do not add it here.**

**State how the test locates the artifact path**, and **what it does when
a pin has no resolvable path above it** — that case must fail, not be
skipped.

### (d) Fixtures

**Every change gets a passing AND a failing fixture**, and **each new
failure mode must have at least one fixture the pre-repair code cannot
get right.** Name each fixture for the mode it covers. At minimum:

    the real GATES.md heading shape                → 14 sections found
    14 raw headings / 14 parsed                    → normal evaluation
    15 raw headings / 14 parsed                    → NOT_PARSEABLE
    a file with '## P2-' lines and a grammar that
      matches none of them  (0 / N)                → NOT_PARSEABLE
    an authorised set of [] with zero sections     → NOT PASS
    base and head identical, zero sections         → NOT PASS
    a heading parsed at base but not at head       → NOT_PARSEABLE
    a gate file with NO '## P2-' lines at all
      (0 raw / 0 parsed)                           → NOT_PARSEABLE
    a gate section modified without authorisation  → FAIL, as before
    a pin whose target does not match              → test fails
    a GATES.md with no pins at all                 → test fails
    a pin with no resolvable path above it         → test fails

**The pre-existing tests must continue to pass, or any that should not
must be reported with the reason.** **Do not delete a test to make the
suite green.**

### (e) The classification, corrected

**`derivations/GOVERNANCE-ENFORCEMENT_classification.md` describes `P7`
and does not record that it matched nothing.** **Correct that entry**:
state what the property now checks, and **add to its limitation what this
task measured** — that a heading grammar which matches no heading
produced a `PASS` across every task that ran it, and that the guard of
(b) is what prevents the recurrence.

**Do not change any verdict.** `P7` stays `PARTIAL`; **the
declared-set discovery problem is untouched by this task and remains its
reason.** **No other property's entry is edited.**

**Add an entry for the pin validator, as a VALIDATOR and not as a
property.** It is not one of the nine and must not be numbered among
them. **This is required, not conditional** — an earlier version said
*if it warrants an entry*, which left the executor to judge and made A8's
"only `P7` changed" unsatisfiable in one branch of that judgement.

## 1a. Why this is cut from `main` and not from `governance/p1-declared-total`

**Both branches modify `scripts/governance_tools/task_checker.py`, and
the question was whether they would collide. Measured: they do not.**

    P1's hunks              lines 52–292: constants, _result,
                            parse_scope_block, check_p1
    this task's targets     GATE_HEADING at 487, gate_sections at 490,
                            check_p7 at 502, plus a new test file

**Nearly two hundred lines apart, in different functions.** **And
`governance/p1-declared-total @ 8ff032e7…` merges into current `main`
cleanly**, measured in a dry run.

**That measurement covers `task_checker.py` and nothing else, and the
claim is narrowed to match it.**

**The two tasks also modify two files in common**, and `P1`'s changes to
them are not small:

    tests/test_task_checker.py                    188 lines changed
    derivations/GOVERNANCE-ENFORCEMENT_classification.md
                                                   33 lines changed

**This task modifies both as well.** **So `P1` merging cleanly into
today's `main` shows that `P1` and today's `main` do not conflict; it
does NOT show that `P1` and a not-yet-existing `P7` branch can be
integrated in either order.**

**THIS SPECIFICATION MAKES NO SUCH CLAIM.** **Whoever integrates must
measure the merge result over all three shared files** —
`task_checker.py`, `tests/test_task_checker.py` and the classification —
**and must not assume order-independence from anything recorded here.**
**An earlier version of this section did claim it, on evidence covering
one file of three.**

**What the measurement DOES support is the choice of base.** Cutting from
`main` gives this task a current base and leaves `P1`'s undischarged
`A10` with `P1`. **Do not merge `governance/p1-declared-total` here, and
do not discharge its `A10`.**

## 2. What this task must not do

- **Do not touch `main`**, do not merge, do not fast-forward.
- **Do not change any gate, gate status, prerequisite state, or any line
  of `GATES.md`.** **The file is read by everything this task builds and
  modified by none of it.**
- **Do not repair `P1` through `P6`, `P8` or `P9`.** **No property is
  added or removed.** The nine stay nine.
- **Do not repair the stale-pin instances themselves** — there are none
  at the evidence base; both pins match. **This task builds the check,
  not a correction.**
- **Do not fix `F1`** — the harness's forbidden trailer — **or `F2`**,
  the `frozen Wilson D` docstring at line 73 of the exploratory script.
  **Report them as open if you meet them; `scripts/` is otherwise
  protected by A9.**
- **Do not weaken any existing check to make the suite green.**
- **Do not answer `C2`**, and do not read the exploratory script for
  physics.

## 3. How the review arrives

Per Rule 18: **supplied as a FILE**, no delimiters, committed
byte-unchanged. **If it arrives pasted, STOP and say so.** **It must
carry `reviewed specification SHA-256:` filled in**; if blank or naming a
different digest, **STOP and say which.** Report the supplied file's
digest and the committed blob's digest and show them equal.

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md
    commit 3  scripts/governance_tools/task_checker.py
              tests/test_task_checker.py
              tests/test_gate_pins.py
    commit 4  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    commit 5  reports/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md

    stated: 4 additions, 3 modifications
    base: 88ef5eec08ab269eddcea8c617cf4f5b09b7336e
    head: <commit 5>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md
      specs/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md
      tests/test_gate_pins.py
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**`tests/test_gate_pins.py` is the pin validator's path** and is fixed
here so you choose no path. **If you judge it belongs elsewhere, STOP and
say where** — do not relocate it.

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Code and tests move together
in commit 3** — a commit where the parser changed and its fixtures had
not would be a green that means nothing.

**Committed report — measured at commit 4:** A1–A8 and A10–A11; **A9's
two checker runs with both configs verbatim**; commit 1–4 SHAs and stored
messages; commit 5's intended message; **the final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-5; A9-final at commit 5; A11 for commit 5; validators at
commit 5; the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 5. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`88ef5eec08ab269eddcea8c617cf4f5b09b7336e`. Measure and report the Git
blob ids of `GATES.md`, `scripts/governance_tools/task_checker.py`,
`tests/test_task_checker.py` and
`derivations/GOVERNANCE-ENFORCEMENT_classification.md`. **Any ref
mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per §3.

**A3 — The grammar, demonstrated on the real file.** Run the new
`gate_sections` against `GATES.md` at the evidence base and **report the
count and the full list of ids found.** **Expected fourteen.** **Report
what you actually got**, and **report the same count against the
pre-repair grammar** — expected zero. **Both numbers, from the same
file.**

**A4 — The completeness invariant, demonstrated against the OLD code.**
**Construct BOTH failing cases — the `0 / N` case and the `14 / 15`
case — and run each against the parser at the evidence base**, and
**report what the old code returns for each.** **The `14 / 15` case is
the one that matters**: it must show the old code returning `PASS` or
otherwise ignoring the unmatched heading. **If the old
code already refuses it, the fixture is not testing the repair and must
be replaced.** **Report per fixture, not in aggregate.**

**A5 — The pin validator, demonstrated three ways.** Report, each as a
separate run: **(i)** the validator against `GATES.md` at the evidence
base — **expected pass, two pins, both matching**; **(ii)** against a
fixture whose pin does not match — **expected fail**; **(iii)** against a
fixture with zero pins — **expected fail.** **Report the failure messages
verbatim for (ii) and (iii)**, because a test that fails for the wrong
reason passes this criterion in appearance only.

**A6 — The suite now distinguishes what it could not.**

**Construct the stale tree in a DISPOSABLE TEMPORARY COPY or a detached
temporary worktree that is NOT the task branch's working tree.** **No
byte of the task branch's working tree is altered for this test**, and
**the temporary tree is never committed and is removed afterwards.**
**Report where it was created and that it was removed.**

**This is stated because §2 forbids modifying `GATES.md` and §7 forbids
writing outside the manifest**, and a stale tree built in place would
collide with both. **The temporary tree is a measurement instrument, not
a change to the repository.**

In that tree, make one `GATES.md` pin stale, **run `python -m pytest`
from its root**, and **report that it FAILS**, with the pass and deselect
counts.

**The command is named so that the measurement is reproducible.** **Do
not substitute a narrower selection** — the claim being established is
about the suite a person actually runs, and a hand-picked subset would
not establish it. **This is the measurement the
task exists to make possible**: the same suite returned `280 passed`
across four revisions spanning a stale pin and a repaired one. **Report
the pass and deselect counts for that deliberately stale tree**, and
**confirm the stale tree is not committed.**

**A7 — Scope, per §4. Final base-to-head scope: 4 additions and 3
modifications.** **`GATES.md` is NOT among them.**

**A8 — Classification.** Diff
`derivations/GOVERNANCE-ENFORCEMENT_classification.md` base to head and
**report it in full.** **Confirm that every `MECHANICAL`, `PARTIAL` and
`JUDGEMENT` verdict is unchanged** and that **no property was added or
removed — the nine stay nine.**

**Exactly two changes are authorised**: `P7`'s description and
limitation, **and one new VALIDATOR entry for the pin check**. **A third
change is a STOP.**

**A9 — The checker over this task's own range**, base `88ef5eec…`, head
**commit 4**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.** **`authorised_modified_gates` IS
`[]`, and here that is truthful**: no gate may change in this task.

**`P7` will run against its own repair.** **This is the first task in
which a `P7` result means anything**, and the meaning is narrow: the
range modifies no gate, so a correct `P7` returns `PASS` **for the right
reason** — zero unauthorised gate changes over fourteen parsed sections,
not zero over zero. **Report the section count `P7` saw.** **A `PASS`
with a section count of zero is a STOP**, and it is the outcome this task
was written to make impossible.

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A9-final, post-report evidence:** re-run RUN 2 at commit 5.

**A10 — Validators, exit status 0.** Report pass and deselect counts
before and after. **The count MUST rise**, because `tests/test_gate_pins.py`
is new and `tests/test_task_checker.py` gains fixtures. **Report the
delta and what accounts for it.** **A count that did not move would mean
the new tests are not being collected.**

**A11 — Commit-message hygiene** on all five commits: proposed message
inspected before, stored message after; **no `Co-Authored-By`, no session
identifier or URL, no tool attribution.** **`F1` says your harness will
try; report what happened.** **Commits 1–4 go in the report; commit 5 is
post-report evidence.**

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** After this task `P7` sees fourteen gates and the pin validator
runs in the suite. **A reader may take that for governance being
enforced.** **It is not.** **The classification still records twenty-two
of twenty-nine objects with no machine behind them**, and `P7` remains
`PARTIAL` because the authorised-set discovery problem is untouched.
**Two checks now work. That is the claim.**

**Second.** **This task fixes the instances it can see.** **It does not
establish that no other check in the suite passes vacuously.** **Report
whether you looked** — and if you did, say over what, and say plainly
that a search you performed once is not a check that runs.

**Third.** **The pin validator's own non-empty assertion is a guard
written by the same hand that wrote the guard it is imitating.** **Say
what would detect the pin validator itself going vacuous**, and **do not
build it here.**

## 7. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  four paths in §4's manifest other than the specification, review and
  report. **Nothing else.**
- **Do not modify `GATES.md`, `CONVENTIONS.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md`, or anything under `results/` or
  `derivations/` other than the classification.**
- **Do not delete or weaken an existing test.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not commit any deliberately stale fixture tree** built for A6.
- No force-push, no history rewrite, no branch deletion. **The
  ratification recorded for a past unpushed amend confers nothing here.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 8. Report contract

- everything in §4 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's two counts from the same file**, with the fourteen ids listed;
- **the separator the grammar accepts**, and what it rejects that a
  reasonable author might write;
- **A4's per-fixture demonstration against the OLD parser**;
- **the raw and parsed heading counts at base and at head**, and
  confirmation that the completeness invariant compares them for
  EQUALITY and not merely for non-zero;
- **A5's three runs**, with verbatim failure messages for (ii) and (iii);
- **A6's stale-tree measurement**, the counts, **where the temporary
  tree was created**, and confirmation that it was never committed, that
  it was removed, and that **no byte of the task branch's working tree
  was altered for it**;
- **A8's full classification diff**, with verdicts confirmed unchanged;
- **A9's two runs**, both configs verbatim, **the section count `P7`
  saw**, and the measured RUN 1 subject set;
- **A10's delta and what accounts for it**;
- **`F1` and `F2` if met, reported and unrepaired**;
- **§6's three Rule 16 junctions**;
- **whether building these checks made you want to fix something else.**
  **Say what, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 9. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view**, and **no
statement below is clone-dependent** — a lesson from the previous task,
where an object's presence in a local database was recorded as though it
were a property of the repository.

    target      the gate headings and what the grammar matches
    method      grep -n '^## P2-' over GATES.md at 88ef5eec; then apply
                ^## (P2-[A-Z0-9-]+)\s*$ to the same file
    MEASURED    FOURTEEN headings, every one of the form
                '## <id> — <title>'. The expression matches ZERO of
                them. gate_sections therefore returns {} at any
                revision, and check_p7 compares two empty maps.

    target      the parser as landed
    method      read scripts/governance_tools/task_checker.py at
                88ef5eec, lines 485-520
    MEASURED    GATE_HEADING at 487; gate_sections at 490; check_p7 at
                502. check_p7's only guards are 'authorised is None'
                and 'gate file absent at base'. THERE IS NO GUARD FOR
                AN EMPTY SECTION MAP.

    target      the suite's blindness
    method      the executed reports of four consecutive tasks spanning
                a stale pin, a repaired pin, an edited artifact and a
                re-pinned one
    MEASURED    280 passed, 2 deselected at every one. The count never
                moved.

    target      collision with governance/p1-declared-total
    method      git diff -U0 of task_checker.py between 1cb5550f and
                8ff032e7 for the hunk ranges; and a dry-run merge of
                8ff032e7 into current main
    MEASURED    P1's hunks in task_checker.py lie in lines 52-292; this
                task's targets are at 487, 490 and 502. Disjoint, ~200
                lines apart. The dry-run merge of 8ff032e7 into
                88ef5eec is CLEAN.
    MEASURED    P1 also changes tests/test_task_checker.py by 188 lines
                and the classification by 33. This task changes both.
    SCOPE OF THE ABOVE
                this establishes disjoint implementation regions in
                task_checker.py, and a clean P1-to-current-main merge.
                IT DOES NOT ESTABLISH that the completed P1 and P7
                branches are conflict-free or order-independent; §1a
                requires that to be measured at integration.
    RETRACTED   an earlier version of this record ended "The two
                branches are independent." That inference was drawn
                from one file of three and is withdrawn. It must not
                survive as a MEASURED line after §1a withdrew the
                claim it supported.

    target      pins at the evidence base
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md, then hash
                each named target
    MEASURED    TWO pins, both MATCH. There is no stale pin to repair;
                A6 must construct one.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 3 modifications;
                the manifest lists four and three; parse OK, counted
                equals stated.
