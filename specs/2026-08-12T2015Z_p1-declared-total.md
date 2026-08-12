# Task specification — replace P1's prose inference with a declared total

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   governance/p1-declared-total
    Cut from           authoritative main @ 1cb5550f…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main`.** It produces a branch. **Integration
and landing are a separate task**, which will pin this branch's tip.

**The branch is cut from `main`, which now carries `task_checker.py`.**
No branch is superseded, no register entry is written, and the ancestry
conflict that stopped an earlier draft of this task cannot arise.

---

## 0. The measurement that changed this task's scope

**An earlier draft proposed replacing P1's "nearest preceding LINE" with
"nearest preceding PARAGRAPH", to fix a governing count sentence that
wrapped. That fix is correct and it is nearly worthless.**

**Every specification on `main` carrying a scope block — twenty-nine of
them — was run through P1.**

    current parser                     10 PASS   19 FAIL
    with the paragraph rule instead    10 PASS   19 FAIL

**The paragraph rule changes the pass rate by zero.**

**The dominant failure is not wrapping. It is that "nearest preceding
count" selects the wrong sentence.** House style places a dry-run count
immediately before the scope block, and that count is taken at an
intermediate head, not at the manifest's head. Measured:

    integrate-chirality-census     manifest 10 paths;  read "7 additions"
                                   from the dry-run sentence
    integrate-supply-protocol-v3   manifest  9 paths;  read "5 additions,
                                   3 modifications" from the dry run
    land-diquark-line              manifest 18 paths;  read "14 additions"
                                   from the dry run

**All three manifests are correct. All three failures are false
positives.** Two further specifications carry no count sentence at all
before their block and report `NOT_PARSEABLE`.

**So P1 as landed reports failure on roughly two thirds of this
repository's specifications, and the repair previously proposed would
have left that untouched.** **Forty-two fixtures did not establish this;
one measurement over real documents did.**

## 1. What to build

### (a) A declared total inside the scope block

**Stop inferring the count from prose. Read it from a declared key.**

    stated: 3 additions, 3 modifications   <- the new key
    add:  (unchanged, one path per line)
    modify:  (unchanged, or [])
    forbidden_operations:  (unchanged)

**The illustration above deliberately does not use the bare `add:` form.**
A specification's text is itself parser input, and a second block with a
bare `add:` line would make this file carry two scope blocks and become
`NOT_PARSEABLE`. **The author's pre-issue run caught exactly that in an
earlier draft of this specification.** **Your fixtures must not
reintroduce it**; keep illustrative blocks distinguishable from the real
one.

**`stated:` belongs to the scope block, is parsed from that one line, and
is the only source of the stated count.** **No sentence anywhere in the
document is consulted.**

**This removes three failure modes at once and not one at a time:** a
wrapped sentence has nothing to wrap into, a dry-run count sitting
nearer the block is no longer a candidate, and a paragraph carrying two
count sentences raises no question. **`stated:` disagreeing with the
manifest remains a `FAIL`, which is the defect shape P1 exists to
catch.**

### (b) No declaration → NOT_PARSEABLE, and this changes a reported result

**A specification with no `stated:` key is `NOT_PARSEABLE`.** Not
`PASS`, not `FAIL`. **`NOT_PARSEABLE` makes a run `INCOMPLETE` and exits
non-zero**, as now.

**State the consequence plainly, because it is a regression in one
place:** `specs/2026-08-12T1256Z_governance-enforcement.md` carries a
deliberately planted mismatch — five stated, six listed — and P1
currently reports it `FAIL`. **After this change it reports
`NOT_PARSEABLE`.** **The planted defect stops being detected on that
file.**

**That is accepted, and the reasoning is recorded here so a reviewer can
reject it:** the file is a pre-syntax document, and *"I cannot judge
this"* is true of it, while *"this is wrong for the reason I computed"*
was true only by coincidence of the old grammar. **The detection is
preserved as a fixture** under §1(d), where a declared total disagreeing
with its manifest must still `FAIL`.

**Do not add a prose fallback.** A fallback reinstates all nineteen false
positives for exactly the documents that most need judging.

### (c) A non-path token under `add:` or `modify:` → NOT_PARSEABLE

**Today the parser appends any stripped line under those keys to the
counted set.** `(none)` was counted as a path and produced a false
failure on a live integration.

**A token that is not a path shape must make the file `NOT_PARSEABLE`,
not silently increase a count.** **This is the PI's explicit decision
over the narrower option of only correcting authors**: correcting the
author prevents one recurrence; correcting the consumer prevents the
class. **A silently wrong count is the most dangerous green this tool can
produce.**

**`[]` remains the empty-set representation** and is already handled.
**Define "path shape" narrowly and state your definition.** A definition
loose enough to admit `(none)` has fixed nothing; one tight enough to
reject a legitimate path will surface in (d).

### (d) Fixtures

**Every change gets a passing AND a failing fixture**, named for what it
is. At minimum:

    stated: agrees with the manifest                        → PASS
    stated: disagrees with the manifest                     → FAIL
      (this preserves the planted five-versus-six detection
       as a property, on a file that declares its total)
    no stated: key at all                                   → NOT_PARSEABLE
    a non-path token under modify:                          → NOT_PARSEABLE
    modify: [] with a stated: naming zero modifications     → PASS
    a dry-run count sentence sitting immediately before the
      block, contradicting stated:                          → PASS,
      because prose is no longer consulted. THIS IS THE
      FIXTURE FOR THE DEFECT THAT MOTIVATED THIS TASK.
    a stated: key whose own two numbers do not sum to the
      manifest total                                        → FAIL

**The forty-two existing tests must continue to pass**, or any that
should not must be reported with the reason. **Do not delete a test to
make the suite green.** **Any P1 test that encodes prose selection is
expected to change; name each one and say what it now asserts.**

### (e) The classification, corrected

**Two statements in
`derivations/GOVERNANCE-ENFORCEMENT_classification.md` describe P1's
grammar as selecting a governing sentence** — near lines 53 and 143.
**They described a grammar the code never implemented**, since the
code's own docstring said "line". **Now they must describe a grammar
that consults no sentence at all.**

**Do not change any verdict.** P1 stays `PARTIAL`. **No object is
reclassified and no `does_not_establish` sentence is weakened.**

**Add to P1's limitation what this task measured:** that P1 is decidable
only over specifications that declare their total, that forty-two
fixtures did not establish behaviour over real documents, and that **on
the twenty-nine real specifications present at
`1cb5550f…`, the pre-repair pass rate was ten.**

## 2. What this task must not do

- **Do not touch `main`**, do not merge, do not fast-forward.
- **Do not edit any specification** to add a `stated:` key, including
  the two this task measures. **Documents are what they are**; the tool
  reports what it can judge.
- **Do not refactor P2 through P9.** The failure localisation is clean
  and a wider rewrite dilutes it. **No property is added or removed.**
- **Do not add a prose fallback**, per §1(b).
- **Do not wire anything into `.github/workflows/ci.yml`.**
- **Do not write a superseded-register entry.** Nothing is superseded by
  this task.
- **Do not state that any rule is now enforced.** Nothing invokes this
  checker automatically, before or after this task.

## 3. How the review arrives

Per Rule 18: **supplied as a FILE**, no delimiters, committed
byte-unchanged. **If it arrives pasted, STOP and say so.** It must
identify this specification by digest or task name; if it identifies a
different one, **STOP and say which**. **Report the supplied file's
digest and the committed blob's digest, and show them equal.** **Report
how this specification arrived.**

## 4. Commit order and evidence layering

Cut `governance/p1-declared-total` from
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.

    commit 1  specs/2026-08-XXT{HHMM}Z_p1-declared-total.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_p1-declared-total.md
    commit 3  scripts/governance_tools/task_checker.py
              tests/test_task_checker.py
    commit 4  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    commit 5  reports/2026-08-XXT{HHMM}Z_p1-declared-total.md

    stated: 3 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_p1-declared-total.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_p1-declared-total.md
      specs/2026-08-XXT{HHMM}Z_p1-declared-total.md
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**This specification is the first document written in the syntax it
commissions**, and A7 checks it against the parser it produces. **If your
implementation cannot parse this file, the syntax is wrong, not this
file.**

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Code and tests move together
in commit 3** — a commit where the parser changed and its fixtures had
not would be a green that means nothing.

**Committed report — measured at commit 4, the pre-report head:** raw
output for A1–A9 and A11–A12; **A10's two checker runs with both configs
verbatim**; commit 1–4 SHAs and stored messages; commit 5's intended
message; **the final scope stated as INTENDED, since commit 5 does not
yet exist.**

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope measured base-to-commit-5; **A10-final re-run at commit
5**; A12 for commit 5, its stored message read back; validators at
commit 5; the push; the branch tip read back from the remote.

**Nothing in the committed report may claim to measure commit 5.**

## 5. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. Any mismatch → STOP.

**A2 — This task's pre-execution review committed, unedited**, per §3,
with the two digests shown equal.

**A3 — Pinned inputs at the evidence base**, Git blob ids:

    scripts/governance_tools/task_checker.py
    1922fe88f3a29909a006b2adf03cfb5229d20d84

    tests/test_task_checker.py
    a68568568f50b2bfbccbcbe4f87bcd70b55b6423

    derivations/GOVERNANCE-ENFORCEMENT_classification.md
    183df9468c986fd8ba4cd5c2ecaf95ee1561adb4

**Any mismatch → STOP.** These are Git blob ids, not SHA-256 digests.

**A4 — Every fixture's OLD-parser result recorded; each new failure mode
demonstrated.** Two obligations, and they are not the same:

**(i) Record, per fixture, what the parser at `1922fe88…` does with it.**
**Per fixture, not in aggregate.** **A fixture that also passes under the
old parser is NOT thereby worthless** — a correct manifest that passed
before and passes after demonstrates that the new syntax did not break
the agreeing case, which is worth knowing.

**(ii) For EACH new failure mode, at least one fixture must be one the
old parser cannot get right.** The old parser does not know `stated:` at
all, so this is about outcomes, not about the key: the fixture must be
one where the old parser reaches a different verdict, or reaches the
right verdict for the wrong reason, or cannot reach one.

**The mode this task exists for is the binding case:** a contradictory
dry-run count sitting immediately before the block. **The old parser
selects it and fails; the new parser must ignore it and pass.** **If that
fixture does not behave differently under the two parsers, the repair is
not doing what §0 says it does.**

**Say, per new failure mode, which fixture discharges (ii).**

**A5 — The whole corpus re-measured.** Run P1 against **every `.md` file
under `specs/` at the new head** — not only those with a scope block —
and **report the full table**: path, status, and for each
`NOT_PARSEABLE` the reason.

**The corpus arithmetic, measured at the evidence base:**

    37  specification files in total
    29  carry exactly one scope block
     6  carry none
     2  carry MORE THAN ONE, and are NOT_PARSEABLE for that reason
        alone, before any question of a declared total

**At the new head there are 38**, this task's specification being the
thirty-eighth.

**Expected: one `PASS` and thirty-seven `NOT_PARSEABLE`**, the latter
splitting 29 / 6 / 2 by the three reasons above. **The table has
THIRTY-EIGHT rows.** **Report what you actually measured, and report the
split.**

**A `FAIL` anywhere in that table is a finding**: it would mean a
document declares a total that disagrees with its manifest, and that
document must be named.

**This criterion is the point of the task.** The tool's behaviour over
real documents is measured, not asserted. **Note that the two
multiple-block files were already unjudgeable and remain so** — this
change neither helps nor harms them, and reporting them as newly
`NOT_PARSEABLE` would overstate what it did.

**A6 — The nineteen false positives are gone.** For the three named in
§0 — `integrate-chirality-census`, `integrate-supply-protocol-v3`,
`land-diquark-line` — **report the before and after status of each.**
**Before: `FAIL`. After: `NOT_PARSEABLE`.** **If any still reports
`FAIL`, prose is still being consulted somewhere.**

**A7 — This specification parses and passes.** Run P1 against
`specs/2026-08-XXT{HHMM}Z_p1-declared-total.md` at the new head.
**Expected `PASS`: `stated:` names three additions and three
modifications, and the manifest lists three and three.** **If it does
not parse, report that as a defect of the syntax, not of this file.**

**A8 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, `tests/test_task_checker.py`.
**Report the test count before and after**, and **name every pre-existing
test whose behaviour changed and what it now asserts.**

**A9 — The classification carries no verdict change.** Diff
`derivations/GOVERNANCE-ENFORCEMENT_classification.md` base to head and
**confirm that every `MECHANICAL`, `PARTIAL` and `JUDGEMENT` label is
unchanged**, and that the only changes are the grammar description and
P1's limitation. **Report the diff.**

**A10 — The checker is run against this task's own range**, base
`1cb5550f…`, head **commit 4** — not commit 5, which is the report that
must carry this output. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_p1-declared-total.md

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.** **Name what
RUN 2 excluded and why.**

**A10-final, post-report evidence:** re-run RUN 2 at commit 5, where this
task's own report first becomes a P9 subject. **If it fails, STOP.**

**A11 — Protected paths.** Every path existing at the evidence base other
than the three in §4's `modify:` list is blob-identical at commit 5. In
particular `GATES.md` at `849a4fbf…`, `CONVENTIONS.md`,
`DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`,
`.github/workflows/ci.yml`, and every other file under `scripts/`.
**Compare path by path.** **No specification under `specs/` is
modified.**

**A12 — Commit-message hygiene** on all five commits: proposed message
inspected before, stored message after; no `Co-Authored-By`, no session
identifier or URL, no tool attribution. **Commits 1–4 go in the report;
commit 5 is post-report evidence.**

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task, **P1 will judge exactly one document in this repository** — the one
that declares a total. **Every other specification will be
`NOT_PARSEABLE`.**

**A reader may take a corpus of `NOT_PARSEABLE` for a corpus that has
been checked and found acceptable. It has not been checked at all.**
**Say so where a reader will meet it**, and say what would change it:
that the syntax must be adopted by convention before P1 covers anything,
and **that adoption is a separate task this one does not perform.**

**Also state the narrower limit.** Ten specifications passed P1 before
this change. **After it, one does.** **A tool that judges fewer documents
more honestly is the intended outcome here, but it is a reduction in
coverage and must not be reported as an improvement in coverage.**

## 7. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  three paths in §4's `modify:` list. **Nothing else.**
- **Do not adjust a fixture to make the suite green.** If a pre-existing
  test now fails, that is a finding and it is reported.
- **Do not adjust the config to make RUN 2 pass.** Narrowing a subject
  set, supplying an empty declared set or dropping a property is a
  specification stop.
- **Do not edit any file under `specs/`.**
- No gate, gate status, verdict, or hash-pinned artifact may be modified.
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 8. Report contract

- everything listed in §4 under its correct layer, **each committed
  figure labelled MEASURED or INTENDED**;
- **A4(i)'s per-fixture old-parser results**, and **A4(ii)'s statement of
  which fixture discharges each new failure mode** — this is the
  criterion most easily satisfied in appearance and not in fact;
- **A5's full THIRTY-EIGHT-row table**, not a summary, with the
  29 / 6 / 2 split of the `NOT_PARSEABLE` reasons;
- **A6's before and after for the three named specifications**;
- **your definition of "path shape"**, and what it would reject that a
  reasonable author might write;
- **the `stated:` grammar as implemented** — what it accepts, what it
  rejects, and whether a malformed `stated:` is distinguishable from an
  absent one;
- **A9's diff**, and confirmation that no verdict changed;
- **A10's two runs**, both configs and both JSON verbatim;
- **§6's Rule 16 assessment**, both limits stated;
- **whether the reduction from ten passing documents to one reads as a
  regression.** It is a reduction in coverage and an increase in
  honesty; **say which it reads as**;
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
clone.** **No measurement was taken through a truncated view** — counts
were obtained over the whole set, and every listing is complete.

    target      the three pinned blob ids of A3
    method      git rev-parse 1cb5550f:<path>, one per path
    MEASURED    all three, as listed in A3. Identical to their values at
                fe8de65d, so the landing carried them unchanged.

    target      P1 over the whole corpus at 1cb5550f
    method      the parser at 1922fe88… re-implemented line for line and
                run against EVERY file under specs/ carrying exactly one
                'add:' record — twenty-nine files, none omitted
    MEASURED    10 PASS, 19 FAIL. The nineteen include two reporting
                NOT_PARSEABLE for absence of any count sentence.

    target      whether the paragraph rule would have helped
    method      the same corpus, the same re-implementation, with the
                backward walk taken over blank-line-bounded paragraphs
    MEASURED    10 PASS, 19 FAIL. IDENTICAL. Some stated values change;
                no file changes verdict.

    target      the dominant failure mode
    method      for three failing files, the manifest counted and the
                selected governing text printed side by side
    MEASURED    integrate-chirality-census: manifest 10 (10 add, 0
                modify); selected text is the dry-run sentence stating
                7 additions, 0 modifications.
                integrate-supply-protocol-v3: manifest 9 (6 add, 3
                modify); selected text states 5 additions, 3
                modifications — the dry run at the merge commit.
                land-diquark-line: manifest 18; selected text states 14
                additions from a two-merge dry run.
                ALL THREE MANIFESTS ARE CORRECT.

    target      the specification corpus, counted exhaustively
    method      git ls-tree -r --name-only 1cb5550f specs/, then count
                'add:' records in every .md file, no file omitted
    MEASURED    37 files. 29 carry exactly one scope block; 6 carry
                none; 2 carry MORE THAN ONE and are therefore
                NOT_PARSEABLE independently of any declared total.
                A5's table has 38 rows at the new head.

    target      the two files with no count sentence
    method      the same run
    MEASURED    2026-08-07T1424Z_freeze-checker-sign-repair.md and
                2026-08-07T1508Z_branch-deletion-policy-amendment.md
                carry a scope block and no count sentence before it.

    target      the planted five-versus-six file
    method      the same run, before and after the proposed change
    MEASURED    currently FAIL, stated 5 counted 6. Under a declared-total
                grammar it becomes NOT_PARSEABLE, because it declares no
                total. §1(b) records this as an accepted regression and
                §1(d) preserves the property as a fixture.

    target      this specification under the syntax it commissions
    method      read the 'stated:' line of §4 and count the manifest
                records beneath it
    MEASURED    stated: 3 additions, 3 modifications; the manifest lists
                three additions and three modifications; six paths.
                They agree.

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    main = 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
