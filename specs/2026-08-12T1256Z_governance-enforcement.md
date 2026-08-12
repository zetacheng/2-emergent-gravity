# Task specification — mechanical enforcement for the governance rules that admit it

Specification evidence base: `8939ff4a46445d88c6470fb4f27eec71f2f39172`

> **The prerequisites are met.** `CONVENTIONS.md` at this base carries
> **eighteen** execution-discipline rules, `### 18.` being the review
> supply protocol, and `docs/BRANCHING_POLICY.md` carries a
> `Superseded branches` section with six entries. **A3's "all eighteen"
> and P4's register both have their objects.**
>
> **Rule 18 is operative**, so this task's review is supplied as a
> file — see A2. **The delimiter approach is not used and this
> specification names no delimiters.**

Classification: **MATERIAL**. Governed by Rule 15: this task's
pre-execution review is a committed artifact — see A0 commit 2 and A2.

**This is the first task authorised to write to `tests/` beyond adding
one suite of its own.** Every recent specification has protected that
directory; **this one adds enforcement to it, and nothing else.**

**Supply, per Rule 18.** **This specification names no delimiters.**
Rule 18 is operative at this evidence base and **the review is supplied
as a file** — there is no boundary to locate. **If a review arrives as
pasted text, that is a supply defect: STOP and say so.**

**This specification should also arrive as a file**, so commit 1's bytes
are verifiable against a digest rather than being your transcription.
**Report how each arrived.**

---

## 0. The gap, and the honest size of it

**No test checks any of the eighteen `CONVENTIONS.md` rules.** An
executor demonstrated this by deleting `P2-PHASE-01`'s entire 103-line
gate entry: `test_gate_anchors.py` and `test_si1_governance.py` both
stayed green.

**Six or more specification defects in this programme were caught by a
reviewer or an executor, and none by a machine**, including four
instances of one shape — a criterion changed while a clause referring to
it was not. **Two reached an executor and caused a correct stop**, which
is later than a reviewer catch and later still than a machine one.

**But "write tests for the eighteen rules" is not the task, and a
specification that asked for it would be asking for something
impossible.** Several rules are judgements. **Amendment G** — that a
structural change propagates — cannot be decided by a machine reading a
diff. **Rule 16** requires naming an inference a reader could draw.
**Amendment I** concerns whether an authority record is adequate.

**A suite that claimed to enforce eighteen rules while enforcing five
would be worse than one that enforces five and says so.** **The
classification is as much the deliverable as the tests.**

## 1. What to build

### (a) Classify every rule and every amendment

**For each numbered rule AND each lettered amendment in `CONVENTIONS.md`
AT YOUR EVIDENCE BASE, classify it.** **This specification expects
EIGHTEEN rules and ELEVEN amendments — twenty-nine objects.** The
amendments are lettered A–I, K and L; **there is no Amendment J**, and a
classification reporting twelve has counted something that is not there.

A1 requires you to confirm both counts before starting, and **the counts
govern, not this sentence.**

**Amendments are in scope deliberately.** §0's two worked examples of
`JUDGEMENT` — Amendment G and Amendment I — are amendments, so a
classification restricted to the eighteen numbered rules would omit the
objects this specification uses to explain its own categories.

    MECHANICAL     a machine can decide it from repository objects
    PARTIAL        a necessary condition is checkable; the rule is not
    JUDGEMENT      deciding it requires reading for meaning

**For `PARTIAL`, state exactly what the necessary condition is and what
it does not catch.** A partial check that is described as full is the
proxy substitution this programme's umbrella principle forbids.

**For `JUDGEMENT`, say why**, in one sentence. **Do not propose a
mechanism.** The classification's value is that a later reader knows
which rules have no machine behind them.

**Your classification governs (b).** If you find fewer mechanical rules
than this specification's §2 expects, **implement what you find and
report the difference** — do not stretch a rule to reach a count.

### (b) A checker over a commit range

**Write `scripts/governance_tools/task_checker.py`**, taking a base and
a head and emitting JSON in the existing tools' style, checking every
property your classification marked `MECHANICAL` or `PARTIAL`.

**§2 lists the properties this specification expects to be checkable.**
**Treat it as a starting point you may add to, and — where your
classification disagrees — subtract from with a stated reason.**

**Three of the seven are PARTIAL by construction, and §2 says why:** P1
without its grammar, P3 and P7 in the discovery of their declared sets,
and P5 always. **A checker that reports these as MECHANICAL has made the
substitution this task exists to detect.** **Where a property is
PARTIAL, the JSON must carry what the check does NOT establish**, in a
field a reader cannot miss — not only in the classification document.

### (c) Tests

**Write `tests/test_task_checker.py`**, exercising the checker on
synthetic fixtures in the style of `test_governance_tools.py`: **each
property must have a passing case and a failing case.** **A check that
is never observed to fail has not been shown to check anything.**

**And assert the checker against this repository's own recent history**,
from the prospectivity boundary of §3 to the evidence base.

## 2. Properties this specification expects to be checkable

**Each is stated as a property, not as an implementation.**

    P1  scope manifest arithmetic
        the path count in a specification's scope manifest equals the
        count stated by the sentence that governs that same manifest

        this is the defect shape that recurred four times; it is
        decidable from the specification text alone

        **MECHANICAL ONLY UNDER A GRAMMAR, and the grammar is part of
        the deliverable.** A specification carries several
        count-bearing sentences at different evidence layers; a parser
        that searches prose for a number will compare the right
        manifest against the wrong sentence and be right by accident
        or wrong by accident. Define, in the checker and in the
        classification:

          the SCOPE BLOCK      the fenced block containing the
                               'add:' and 'modify:' records
          the COUNTED SET      the path records under 'add:' plus
                               those under 'modify:' in THAT block
          the GOVERNING        the count stated in the criterion
          SENTENCE             heading or intro line immediately
                               preceding that block, and no other

        **If a specification's text does not admit that parse — no
        fenced scope block, or more than one candidate governing
        sentence — the checker reports NOT-PARSEABLE for P1 on that
        file. It does NOT guess, and NOT-PARSEABLE is not a pass.**
        **Absent the grammar, classify P1 as PARTIAL, not MECHANICAL.**

    P2  Rule 15 commit order
        on a task's commit range, a review commit precedes the first
        WORK COMMIT, where a work commit is any commit changing at
        least one path outside the TASK-RECORD SET

        the TASK-RECORD SET is specs/, reviews/ and reports/

        **reports/ is in the set deliberately.** An earlier draft named
        only specs/ and reviews/, which contradicted this section's own
        stopped-task exception below: a stopped task's report is
        outside specs/ and reviews/, so it became the first commit
        matching the predicate and the task failed a property it was
        supposed to satisfy. **The stopped case now follows FROM the
        property rather than from an exception bolted beside it.**

        **A report is a record of work, not the work.** If a task's
        range touches nothing but the task-record set, no work commit
        exists and P2 is satisfied with nothing to order.

    P3  append-only, on both measures
        for each file declared append-only, zero deleted lines from
        base to head AND for each commit against its parent, AND the
        base blob an exact byte prefix of the head blob

        **The measure is mechanical. WHICH FILES ARE DECLARED
        append-only is not**, unless the declaration has a fixed
        machine-readable syntax. **Reading it out of unrestricted prose
        is semantic extraction and makes the whole property PARTIAL.**

        **Two honest routes, and you choose one and say which:** take
        the declared set as a checker PARAMETER supplied by the caller,
        which is mechanical over a given set and silent about
        discovery; or define a fixed declaration syntax and check
        conformance to it. **Do not infer the set from prose and
        classify the result MECHANICAL.**

    P4  superseded branches are not merged
        no branch listed in the superseded register is an ancestor of
        the head

    P5  merge parentage is correct against freshly recomputed facts
        — PARTIAL, and the limit is the point
        for a merge commit:
          the recorded parent 1 equals the merge object's first parent
          the recorded parent 2 equals its second parent
          the recorded merge-base equals a FRESHLY COMPUTED
            git merge-base(parent 1, parent 2)
          every stated ancestry relation is true

        **NOT that the three SHAs are pairwise distinct.** A merge-base
        may legitimately equal a parent — it does whenever a task
        merges without having committed anything of its own first.
        **Testing distinctness would fail correct histories and pass a
        shared derivation that happened to produce three different
        values.**

        **AND NOT that the values were independently derived.** An
        earlier draft made independent derivation the machine property.
        **A repository checker cannot establish it.** Whether the
        executor recomputed each value or copied one field into another
        and happened to be right is a fact about the execution process,
        not about any object in the repository. **Three correct values
        are consistent with both.**

        **So P5 is PARTIAL by construction**, and the classification
        must say so: the recomputation above is a NECESSARY condition,
        the diquark task's shared-rationale defect would still pass it,
        and **independent derivation survives as a reporting obligation
        on the executor, not as a check.** **Claiming otherwise is the
        proxy substitution this whole task exists to prevent, committed
        by the tool built to prevent it.**

    P6  commit-message hygiene
        no Co-Authored-By, session identifier, URL or tool attribution
        in any commit message in the range

    P7  gate integrity
        every ## P2- section not in the AUTHORISED-MODIFIED set is
        byte-identical between base and head, and the section count is
        unchanged

        **Byte identity is the check; the count is only a guard against
        addition and removal.** A count survives an edit that keeps the
        number of headings — which is precisely how a 103-line gate
        entry was once deleted with the validators green.

        **Identifying the authorised set has the same discovery problem
        as P3**, and takes the same two routes: a caller-supplied
        parameter, or a fixed syntax. **Loosely inferred, P7 is
        PARTIAL.** **An empty authorised set must mean 'nothing may
        change', never 'nothing to check'.**

**P2 and P5 have legitimate exceptions and the checker must handle
them**, not fail on them:

- **A task may make more than one merge.** The second merge's parent 1
  is the first merge, not a review commit. **That is correct and must
  pass.**
- **A task may stop before its work commits.** A range with a
  specification, a review and a report and no work commit **satisfies
  P2 because no work commit exists** — this now follows from P2's own
  definition of the task-record set, and is listed here as a case to
  FIXTURE, not as an exception to code around.

## 3. Prospectivity

**Rule 15 is prospective, and the history predates it.** Merges made
before Rule 15 existed do not have a review commit as parent 1. **Their
parent 1 is variously a report commit, a `docs:` commit, a `conventions:`
commit or another merge — NOT a specification commit**, and a fixture
built from the wrong assumption will test the wrong thing. **Determine
the actual shapes by reading the history; do not take this sentence as
the inventory.**

**Rule 18 is also prospective — it is operative at your evidence base —
but §2 commissions no property that checks it**, because how a review
file reached the executor is not recoverable from repository objects.
**The boundary this section requires is Rule 15's, and one boundary is
enough**, since P2 is the only property it governs. **Classify Rule 18 in
(a) and say there that no check stands behind it**; do not invent one.

**The checker MUST take a prospectivity boundary as a parameter**, not
assume one. **Commits before it are out of scope for P2, and the
checker reports them as such rather than as passing or failing.**

**The boundary's inclusivity must be stated, not chosen silently.** Two
readings are available and they are not equivalent in principle:

    INCLUSIVE   the commit that introduces Rule 15 is itself in scope
    EXCLUSIVE   only task ranges beginning after Rule 15 became
                authoritative on main are in scope

**The checker takes the reading as an explicit parameter** and **the
report names which was used.** **Run it both ways over the tested range
and report whether any merge classification differs.** If none does, say
so — that is a useful negative result and it retires the question for
this range only. **If any differs, report the difference and do not pick
a winner**; which reading is correct is a governance decision, not the
checker's.

**Determine the boundary from the repository**: the commit at which
Rule 15 became operative on `main`. **Report how you determined it, and
report what the checker says about the merges on either side of it.**

**Do not backfill.** **Do not modify any historical commit**, and **do
not weaken a check so that history passes it.** **If a post-boundary
commit fails a check, that is a finding: report it and do not repair
it.**

## 4. What must not happen

- **Do not modify any existing test.** You add two files to `tests/`
  and change nothing there.
- **Do not modify `CONVENTIONS.md`.** This task enforces rules; it does
  not write them. **If a rule is unenforceable as written, report that
  as a finding** — amending it is a separate task with its own review.
- **Do not claim coverage you have not demonstrated.** Every property
  the checker reports on must have a failing fixture.
- **Do not add a check for anything you classified `JUDGEMENT`.** A
  check that approximates a judgement will be read as enforcing it.
- **Do not run the checker against any branch other than this
  repository's own history**, and do not modify any branch.

## 5. This task is its own first subject

**Run the checker against this task's own commit range before the
report, and put the result in the report.**

**If it fails a check, do not adjust the check.** **Fix the task, or
report the failure and stop.** **A suite whose first act was to be
weakened for its author is worth nothing.**

**ONE pre-authorised exception, and only one.** **A9's planted P1
mismatch is the sole checker failure this specification authorises in
advance. It does NOT trigger the stop above.** It must be reported
exactly as a detected specification defect, with the correct count
stated, and the task proceeds on the manifest.

**Every other checker failure triggers the stop normally.** **The
exception is narrow deliberately**: without it, §5 and A9 are two
imperatives in conflict and the executor would have to decide which
governs — **which is the judgement this programme's specifications
exist to remove.**

**In particular P1 applies to this specification.** A9's manifest and
its summary sentence must agree — **and if they do not, that is a
specification defect this task should catch before an executor does.**

## 6. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_governance-enforcement.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_governance-enforcement.md
    commit 3  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    commit 4  scripts/governance_tools/task_checker.py,
              tests/test_task_checker.py
    commit 5  reports/2026-08-XXT{HHMM}Z_governance-enforcement.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
work**, per Rule 15. **Commit 3 is the classification and precedes the
code it governs.**

**A1 — Pinned inputs**, verified before use; a mismatch is a STOP.
Method: `git cat-file blob <rev>:<path> | sha256sum`.

    CONVENTIONS.md
    928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d

    docs/BRANCHING_POLICY.md
    9d99f8365f798cfc27b5a2612f21130b4534cd32ea4778be4be97f15b7daa3f0

    scripts/governance_tools/core.py
    c927be3eee4c773d6b9ef5944ecf992d434e8d466518285f38e96734f220b73f

**All three measured at this evidence base.** `core.py`'s value is
unchanged from before the supply-protocol landing, as expected — that
task did not touch it.

**Confirm both counts before classifying: EIGHTEEN rules and ELEVEN
amendments.** If either differs, **STOP** — A3's scope is stated in those
terms and a different count means the classification covers something
other than what this specification commissioned.

**A2 — This task's pre-execution review committed, unedited**, per
Rule 18, which is operative at this evidence base: **supplied as a
file, committed byte-unchanged, no extraction of any kind.**

**Report the supplied file's digest and the committed blob's digest and
show them equal.** **Verify correspondence** — the review must identify
this specification by digest or task name. **If it does not, if no file
is supplied, if it arrives pasted instead, or if it corresponds to a
different specification, STOP and say which.**

**The specification should also arrive as a file**, per Rule 18's
clause; **if it arrives pasted, say so**, since commit 1 then carries
your transcription with nothing to digest against.

**A3 — The classification**, per §1(a): all eighteen rules and all
eleven amendments classified, `PARTIAL` conditions stated with what they
miss, `JUDGEMENT` entries justified in one sentence.

**A4 — The checker**, per §1(b), emitting JSON in the existing tools'
style, with a non-zero exit on governance failure distinguishable from
a non-zero exit on tool error. **Rule 14's outcome contract applies to
a tool this task writes.**

**A5 — The tests**, per §1(c): **every property has a passing and a
failing fixture.** Report the count of each.

**These cases must each have a fixture**, because each is a shape §2
names and none is hypothetical: a task with two merges, where the second
merge's parent 1 is the first merge; a stopped task whose range holds
only a specification, a review and a report; a merge whose merge-base
legitimately equals parent 1; a specification with more than one
count-bearing sentence, where P1 must select the governing one; and a
file the checker was NOT told is append-only, which P3 must not silently
pass.

**A6 — Prospectivity handled**, per §3: the boundary determined and
reported, pre-boundary commits reported as out of scope rather than
passing, and the merges on either side reported. **The inclusive and
exclusive readings both run, the reading used is named, and any merge
whose classification differs between them is reported.** **If none
differs, say so.**

**A7 — The checker run against this task's own range**, per §5, with
the result in the report.

**A8 — Nothing else touched.** `CONVENTIONS.md`, `AGENTS.md`,
`GATES.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`,
`pyproject.toml`, every existing file under `tests/`, and every path
under `results/`, `derivations/` and `reviews/` that exists at the
evidence base: blob-identical. **No gate status changes.**

**A9 — Scope**, five additions:

    add:
      specs/2026-08-XXT{HHMM}Z_governance-enforcement.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_governance-enforcement.md
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
      reports/2026-08-XXT{HHMM}Z_governance-enforcement.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 6 additions and 0 modifications.**

**The manifest above lists SIX paths and the sentence before it says
five. That is a P1 violation, planted deliberately.** **Report it, state
the correct count, and proceed on the manifest** — **this specification
is P1's first test subject, and a checker that cannot catch a defect in
its own commissioning document is not worth committing.**

**This is §5's single pre-authorised exception.** **The checker MUST
report P1 as failing here**, and that failure does not stop the task.
**Any other failure does.**

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, and your new test file. **A10-pre** at
the pre-report head goes in the report; **A10-final** at the pushed head
is post-report evidence.

**A11 — Lint clean:**
`ruff check scripts/governance_tools/task_checker.py tests/test_task_checker.py`.

**A12 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`8939ff4a46445d88c6470fb4f27eec71f2f39172`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

**A13 — Commit-message hygiene** on every commit: inspect the proposed
message before, the stored message after; permit no `Co-Authored-By`, no
session identifier or URL, no tool attribution. **Report per commit
whether any trailer was suppressed and which.**

## 7. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task the repository will hold eighteen rules and a checker that tests
some of them. **A reader could conclude the rules are enforced.**
**Only the mechanical subset is** — and **nothing runs the checker
automatically.** A checker that exists but is not invoked by any
workflow is **available**, not **enforcing**, and the difference should
be stated where a reader will meet it.

## 8. Evidence layering

**Committed report:** A1–A9, A10-pre, A11, A13, the earlier commit SHAs
and messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A10-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 9. Invariants and prohibitions

- Executor-writable: the six paths of A9 only.
- **Do not do anything §4 forbids.**
- **Do not modify `CONVENTIONS.md` even to fix a rule you find
  unenforceable.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `governance/enforcement-checks`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- raw output for **A1–A13**, scope-checker JSON verbatim including
  `observed_operations`;
- **the classification in full**, all eighteen rules and all eleven
  amendments, with `PARTIAL` gaps and `JUDGEMENT` justifications;
- **the passing and failing fixture count per property**;
- the prospectivity boundary, how you determined it, and the merges on
  either side;
- **the checker's output on this task's own range**;
- **A9's planted P1 violation**, caught or not, and how;
- **which rules you found unenforceable as written**, with the specific
  wording that makes them so. **This is a finding about
  `CONVENTIONS.md`, not a licence to change it**;
- **whether any check you wrote is a proxy for the property it claims
  to test.** **This task exists because proxies were mistaken for
  properties**; if one of yours is, it is better said now;
- **for every property classified PARTIAL, the sentence stating what it
  does NOT establish**, and confirmation that the sentence is in the
  checker's JSON and not only in the classification document;
- **P5 explicitly**: confirmation that the checker recomputes all three
  Git facts freshly, and that it makes NO claim about whether the
  executor derived them independently;
- **§7's Rule 16 assessment**, junction named or search described;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

**Every line below was produced by RUNNING the stated method against a
clean clone at `8939ff4a…`, the fixed evidence base.** Nothing here is
asserted. **`MEASURED` means a method was run and its output recorded;
`CONFIRMED` without a method line is not used**, because a record whose
purpose is separating executed from asserted must not itself blur them.

**An earlier draft carried two of these at `0ab6369a…` as predictions of
what the supply-protocol landing would produce. They were re-run at this
base rather than relabelled**, and both held exactly.

    target      CONVENTIONS.md at 8939ff4a…
    method      git cat-file blob 8939ff4a:CONVENTIONS.md | sha256sum
    check type  BYTE-EXACT SHA-256
    MEASURED    928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d
                — carried as PREDICTED before the landing; held

    target      docs/BRANCHING_POLICY.md at 8939ff4a…
    method      as above, on that path
    MEASURED    9d99f8365f798cfc27b5a2612f21130b4534cd32ea4778be4be97f15b7daa3f0
                — carried as PREDICTED before the landing; held

    target      scripts/governance_tools/core.py at 8939ff4a…
    method      as above, and again at 0ab6369a and aa531aea
    MEASURED    c927be3eee4c773d6b9ef5944ecf992d434e8d466518285f38e96734f220b73f
                identical at all three revisions; nothing in the
                landing sequence touched it

    target      rule and amendment counts at 8939ff4a…
    method      grep -cE '^### [0-9]+\.' for rules; grep -oE
                'Amendment [A-Z]\b' | sort -u for amendments
    MEASURED    18 rules, '### 18.' being "Review supply protocol";
                11 amendments, lettered A-I, K and L.
                THERE IS NO AMENDMENT J.

    target      the superseded register at 8939ff4a…
    method      count entry records inside the fenced block under
                '## Superseded branches', names read back
    MEASURED    one section, SIX entries:
                fix/pi-decisions-and-deferred, fix/pi-decisions-v2,
                governance/supply-protocol-v2,
                governance/supply-protocol-and-superseded,
                review/role-model-and-executors,
                gate/p2-land-diquark-line
    RETRACTED   an earlier draft of this record stated FIVE. That value
                was read from a diff truncated at 80 lines, which cut
                the sixth entry exactly, and was never measured against
                the whole object. The reviewer caught it. It is
                corrected here rather than silently replaced.

    target      main's merge commits at 8939ff4a…
    method      git rev-list --merges, then git log -1 --format=%s on
                parent 1 of each
    MEASURED    merges predating Rule 15 do NOT have a review commit as
                parent 1. Their parent 1 is a report commit, a 'docs:'
                commit, a 'conventions:' commit, or another merge.
                NO merge on main has a commit whose subject begins
                'spec:' as parent 1.
    RETRACTED   an earlier draft said "the two oldest merges have a
                SPECIFICATION commit as parent 1". That was carried
                forward unmeasured and is wrong. §3 is corrected to
                match; a P2 fixture built from the old sentence would
                have tested a shape that does not occur.
    MEASURED    at least one merge has another merge as parent 1 —
                the legitimate two-merge case §2 requires the checker
                to pass

    target      tests/ at 8939ff4a…
    method      git ls-tree -r --name-only, counted three ways;
                git grep -n CONVENTIONS -- tests/
    MEASURED    19 paths in total; 18 ending '.py'; 17 matching
                'test_*.py'. **THREE DIFFERENT COUNTS ARE CORRECT
                UNDER THREE DIFFERENT PREDICATES**, so any criterion
                using one MUST name its predicate. An earlier draft
                said "18 test files" with no method; the integration
                task hit the same ambiguity as 17-versus-19.
    MEASURED    tests/ tree object a0afbde6…, IDENTICAL to the tree at
                0ab6369a — the landing changed no test
    MEASURED    the CONVENTIONS grep returns 8 hits, 7 in
                test_governance_tools.py and 1 in
                test_repository_structure.py, all path literals or
                fixture paths. **EIGHTEEN RULES AND A SIX-ENTRY
                REGISTER ARE NOW ON AUTHORITATIVE main, AND NOTHING
                CHECKS ANY OF THEM.** Three governance tasks moved the
                gap onto main; none closed it.
