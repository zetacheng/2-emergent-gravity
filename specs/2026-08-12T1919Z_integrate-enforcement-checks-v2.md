# Task specification — integrate the governance checker, and land it

Specification evidence base: `8939ff4a46445d88c6470fb4f27eec71f2f39172`

    Branch  governance/enforcement-checks
            fe8de65de8288593f39a74110c1ea370ce27021f

Classification: **MATERIAL**. The branch completed result review. This is
the integration authorization **and the landing authorization**; §6
carries the landing clause, so no second task is required.

**Provenance of this text.** The reviewer approved
`9253179cdec554a7f986cd62a5e376599111b400cefd43a4983b4f1a4242cfd7` and,
in the same review, proposed one wording change: that §2b say the
specification removes both TRIGGERS of the false positive rather than
that it carries both FIXES. **That change is applied here and is the
only delta.** It was applied because §2b's own next paragraph calls one
of the two an accommodation, so the earlier wording contradicted the text
two lines below it. **Report both digests and confirm the delta is what
this note says it is.**

**Rules 1–18 are in force.** Rule 15 governs: this task's pre-execution
review is a committed artifact — see §5 commit 2 and A2. **Rule 18
governs supply: the review arrives as a file** and is committed
byte-unchanged.

**One merge, one fast-forward.** Dry run from the evidence base with the
specification and review commits in place: **no conflict**, merge-base
`8939ff4a…`, **8 additions and 0 modifications** at the merge commit.
**If a conflict occurs, STOP.**

---

## 0. What is being integrated

**A classification of twenty-nine governance objects, a checker, and
forty-two tests of the checker.**

    classification  2 MECHANICAL (one only in part), 5 PARTIAL,
                    22 JUDGEMENT — 18 rules and 11 amendments
    task_checker.py nine properties, 710 lines, --repo and --config
    tests           42 functions; every property with a passing AND a
                    failing case

**The classification is the deliverable.** The checker is what the
classification licensed; the tests are what stopped the checker being
believed.

## 1. What this does NOT establish, and the count that makes it plain

**Landing this branch does not enforce anything.**

**Twenty-two of twenty-nine objects have no machine behind them at all.**
Rule 15 is the only rule mechanical without qualification. **Rule 18 is
`JUDGEMENT` with nothing behind it** — a byte-identical blob is equally
consistent with a file supply, a paste, and a reconstruction, so no check
was invented for it.

**The forty-two green tests are the most misleading artifact in this
merge.** They establish that the checker behaves as tested. **They
establish nothing about any repository change**, because
`.github/workflows/ci.yml` runs `python -m pytest` and **never invokes
`task_checker.py`**. After this lands, the accurate name is **available
governance verification, not enforced governance.**

**Do not describe this merge as closing the enforcement gap.** It moves
the gap from "no tool" to "a tool nothing calls", which is the harder
version to notice, because a tool's existence reads as reassurance.

**It settles no science.** No gate, no coefficient, no channel.
`P2-PHASE-01` stays `PROPOSED`.

## 2. A false line lands with this merge, deliberately and unrepaired

**`specs/2026-08-12T1256Z_governance-enforcement.md` contains a `MEASURED`
line under Amendment H that is false.** At line 607 it states that no
merge on `main` has a commit whose subject begins `spec:` as parent 1.
**Six do**, and the executor measured them:

    ce86b534  10f14f01  d8afb74e  d56335b5  46b2915d  f62fc89a

**The specification author produced that line by truncating a command's
output and recording the visible part as the measurement.** It was the
second such truncation in one session; the first, a register count read
from a diff cut at eighty lines, was caught by the Reviewer.

**Nothing material depends on it.** Those parent-1 commits add paths
under `specs/`, which is in the task-record set, so they are not work
commits and P2 is unaffected. **The correction is already committed**, in
§5 and §13 of `reports/2026-08-12T1256Z_governance-enforcement.md`, which
arrives in the same merge.

**Both the false line and its correction land together, and neither is
edited.** History is not rewritten and a reviewed artifact is not
retouched. **A3 requires the report to state where a reader who meets the
false line can find the correction** — that is the part this merge does
not solve, and §7 returns to it.

## 2b. This is a second attempt, and one clause accommodates a known defect

**A first integration was built, reviewed and executed. It STOPPED**, at
`governance/integrate-enforcement-checks @ 58a996a46b1f446fee1517c583bf3b27a4561b74`,
and that branch is a complete record of the stop. **It is not deleted and
nothing in it is rewritten.**

**The stop was a false positive from `P1`, with one defect on each side
of the interface:**

    checker    the grammar is documented as reading the governing
               SENTENCE and implemented as reading the nearest LINE.
               The count sentence wrapped; the parser read the
               continuation "0 modifications" and took stated as 0.
    that spec  it wrote "modify:" followed by "(none)" — prose in a
               machine-read slot — and the parser counted the token as a
               tenth path.

**Measured, all four combinations:**

    as issued              stated 0  counted 10   FAIL
    fix the prose only     stated 0  counted  9   FAIL
    fix the wrap only      stated 9  counted 10   FAIL
    fix both               stated 9  counted  9   PASS

**This specification removes both TRIGGERS of the known false positive.
It fixes neither the parser nor the grammar**, and the distinction is not
pedantry: only one of the two changes below is a correction.

`modify: []` IS a correction. `[]` is the empty-set representation the
parser already handles, and prose never belonged in a machine-read slot.

**A5's count sentence sitting on one line is NOT a correction. It is an
accommodation of the checker defect above, and it is labelled as one so
nobody later mistakes it for a house style with a reason.** **After this
task lands, the line-versus-paragraph parser defect still exists on
`main`, and so does the classification's description of a grammar the
code does not implement. Landing this task repairs neither.** **The
accommodation lasts exactly one task.** The next task repairs the
grammar to read a blank-line-bounded paragraph, after which a wrapped
sentence parses correctly and this constraint disappears.

**Why accommodate rather than repair first.** A repair branch cut from
`fe8de65d…` would make the branch it declared superseded an ancestor of
itself, which `P4` catches deterministically; and every replacement
branch in this repository's history — `supply-protocol-v3`,
`p2-land-diquark-line-v2` — was cut fresh from `main`, never from its
predecessor. **Rebuilding the reviewed 710-line checker, its 42 tests
and the classification on a fresh branch would discard the commit-level
Rule 15 ordering of the task that produced them.** **A branch with a
fixable defect is repaired by a later task on `main`; it is not
superseded.** What was superseded here is the integration ATTEMPT, not
the work.

**The register entry for `58a996a4…` is deliberately NOT written by this
task.** Rule 17 forbids an integration adding a governance
classification, and a supersession entry is one. **It is a named
deferred item, not an oversight**, and it belongs to a task authorised to
write `docs/BRANCHING_POLICY.md`. **Report that you did not write it.**

## 3. What this task must not do

- **Do not edit anything arriving from the branch.** Not the false line,
  not the classification, not the checker. **A merge integrates what was
  reviewed.**
- **Do not add, remove or re-word a classification verdict.** Rule 17.
- **Do not modify `.github/workflows/ci.yml`.** Wiring the checker into
  CI is a separate task with its own review, and it has open design
  questions that this task is not authorised to answer.
- **Do not state that any rule is now enforced, tested or checked by
  CI.** §1 governs.

## 4. How the review arrives

Per Rule 18, now operative on `main`:

- **Supplied as a FILE.** No delimiters are named. **If a review arrives
  as pasted text, STOP and say so.**
- **The review must identify this specification**, by digest or task
  name. **If it identifies a different one, STOP and say which.**
- **Commit the file's bytes unchanged.** Resolve placeholders in the PATH
  only.
- **Report the supplied file's digest and the committed blob's digest,
  and show them equal.**
- **Report how this specification arrived.** It should arrive as a file;
  a pasted one makes commit 1 your transcription with nothing to check
  against.

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
    commit 3  --no-ff merge of the pinned remote ref
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the merge**,
per Rule 15's timing clause.

**The report is commit 4, so it cannot contain measurements of commit 4.**
An earlier version of this specification required exactly that, and it was
unsatisfiable: the checker was to run at commit 4 and its verbatim output
was to be inside commit 4. **The layering below resolves it by moving the
governing head to commit 3**, not by authorising a fifth commit and not by
letting the executor choose.

**Committed report — measured at commit 3, the pre-report head:**
raw output for A1–A4, A6–A9, A13-for-commits-1-to-3, and **A10's two
checker runs with both configs verbatim**; the `PRE_MERGE` JSON verbatim;
**A12-pre at commit 3**; **A5 as the INTENDED final manifest**, stated as
an intention rather than a measurement; commit 1–3 SHAs and stored
messages; commit 4's intended message; the intended fast-forward
parameters.

**Post-report evidence, returned to the Reviewer and NOT written back:**
**A5's final scope measured base-to-commit-4**; **A10-final, RUN 2
re-executed at commit 4**; **A13 for commit 4**, its stored message read
back from the object; **A12-final at the pushed `main`**; the push; the
final `POST_MERGE` JSON; A11 as re-verified after the advance; remote
`main` read back; final ancestry confirmation.

**Nothing in the committed report may claim to be a measurement of an
object that did not exist when it was written.** **Where the report
states an intention, it says so in that word.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 puts commits after it.

**The advance is a fast-forward. Verified available:** `8939ff4a…` is a
strict ancestor of the dry-run head. **If a fast-forward is not
available, STOP** — do not convert the landing into a merge.

**Push without `--force` and without `--force-with-lease`.** A plain push
being refused means the premise is already false.

**This clause exists because its absence cost a whole task.** The
previous integration was built, reviewed and verified, and then `main`
never moved, because the specification carried no authorisation to move
it and the executor correctly declined to infer one from the task's name.
**An integration specification states its landing outcome inline —
including when the outcome is "do not advance".**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
merge `main` carries a checker, forty-two passing tests, and a
classification saying twenty-two of twenty-nine objects have no machine
behind them. **The tests will be met before the classification is** — a
green suite is visible in CI, and the classification is a file someone
must open. **The reading to be prevented is "governance is now covered by
tests".**

**Second junction, and it is the one §2 leaves open.** A reader meeting
the false `MEASURED` line at line 607 of the integrated specification
**has no pointer from there to the report that corrects it.** The
correction is discoverable only by knowing to look. **Say where you would
put such a pointer, and whether any existing convention would have
created one.** **Do not create it in this task**; it is a repository-wide
question about correction discoverability, and Amendment L's known
instance is the same shape.

## 8. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/remotes/origin/main` and
remote `refs/heads/main` both resolve to
`8939ff4a46445d88c6470fb4f27eec71f2f39172`; the source branch to
`fe8de65de8288593f39a74110c1ea370ce27021f`; **and the stopped first
attempt `governance/integrate-enforcement-checks` to
`58a996a46b1f446fee1517c583bf3b27a4561b74`, which must still exist and
must not be touched.** Any mismatch → STOP. **Local `main` is stale by
design.**

**A2 — This task's pre-execution review committed, unedited**, per §4,
with the two digests shown equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = fe8de65de8288593f39a74110c1ea370ce27021f
    merge-base(parent 1, parent 2)
             = 8939ff4a46445d88c6470fb4f27eec71f2f39172

**Parent 1 is fixed by which commit you are standing on**, and with §5's
order that is the review commit. **Commit 1 MUST be an ancestor of parent
1**; verify and report that too. **The merge-base equals the evidence
base and NOT parent 1**, because parent 1 already carries two commits of
this task's own — so a single shared derivation would be detectable.
**Report three measurements with the method for each.**

**A4 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push, carrying **two distinct SHAs** — the merge object is the
merge commit, remote agreement is checked against the pushed `main`.
**If the guard cannot represent both roles separately, STOP.**

**A5 — Scope, frozen manifest.**

**Final base-to-head scope: 9 additions and 0 modifications.**

    base: 8939ff4a46445d88c6470fb4f27eec71f2f39172
    head: <commit 4>
    mode: exact
    add:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      reports/2026-08-12T1256Z_governance-enforcement.md
      reports/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
      reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
      scripts/governance_tools/task_checker.py
      specs/2026-08-12T1256Z_governance-enforcement.md
      specs/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md
      tests/test_task_checker.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Nine paths, all additions, nothing modified.** Six arrive from the
branch; three are authored here.

**At commit 3, before the report exists, the count is 8 additions and 0
modifications. That is the figure the committed report MEASURES.** **The
nine-path figure above is the INTENDED final manifest** — it can only be
measured once commit 4 exists, so it is verified as post-report evidence
and the committed report states it as an intention, in that word. **Both
figures are correct at their own head; say which head each came from.**

**A6 — Arriving artifacts intact.** After the merge, these six paths are
blob-identical to the source branch:

    derivations/GOVERNANCE-ENFORCEMENT_classification.md
    183df9468c986fd8ba4cd5c2ecaf95ee1561adb4

    reports/2026-08-12T1256Z_governance-enforcement.md
    1afd8497e7ddd1d9d5e2d946f72fb8623fea7741

    reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
    670a9fc35230ba82cf25d1ed9529088434d2a87a

    scripts/governance_tools/task_checker.py
    1922fe88f3a29909a006b2adf03cfb5229d20d84

    specs/2026-08-12T1256Z_governance-enforcement.md
    9ab2cb63138192fd9c7505b5b3f76eadafb0b817

    tests/test_task_checker.py
    a68568568f50b2bfbccbcbe4f87bcd70b55b6423

**These are Git blob ids, not content SHA-256 digests**, and they are not
the guard's `pinned_artifacts` input, which takes SHA-256. **If you run
both, run both — do not substitute one for the other.**

**A7 — Protected paths. This task modifies NOTHING.**

`CONVENTIONS.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`,
`GATES.md`, `AGENTS.md`, `pyproject.toml`, `.github/workflows/ci.yml`,
and **every path under `scripts/`, `results/`, `tests/`, `derivations/`,
`docs/` and `reviews/` that exists at the evidence base**: blob-identical
between base and **commit 3**, and re-confirmed at commit 4 as
post-report evidence. **Compare path by path.** Commit 4 adds one path
under `reports/` and touches nothing else, so a difference between the
two heads outside that path is a stop.

**The previous integration authorised three modifications and excluded
them from this set. THIS ONE AUTHORISES NONE.** Do not carry that
exception over.

**`tests/` and `scripts/governance_tools/` each gain exactly one path**,
and **their tree objects therefore DIFFER from the base — that is
correct here.** The last two specifications asserted `tests/` tree
identity; **that assertion is wrong for this task.** The check is: every
file existing under `tests/` at the base is blob-identical, and
`tests/test_task_checker.py` is the sole addition. **17 test files at the
base, 18 at commit 3**, counted as `test_*.py`; report the predicate with
the number.

**A8 — Append-only and gates, trivially but explicitly.**
`DECISION_LOG.md` and `GATES.md` are **untouched**, so append-only holds
with nothing appended. Report `GATES.md` blob
`849a4fbfe62d6478f092a84b0175357a74bbbb06`, **14** sections matching
`^## P2-`, and `P2-PHASE-01` still `PROPOSED`.

**A9 — Superseded branches not merged, all six.** No commit in the
register is an ancestor of commit 3, and none of commit 4 when
re-checked after the advance:

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, re-checked after the advance as well as
before it.

**A10 — The checker is run against this task's own range.** This is the
first use of the tool being integrated. **The governing head is COMMIT 3,
the merge commit — not commit 4**, because commit 4 is the report that
must carry this output. Base `8939ff4a…`. **Report the JSON verbatim
together with the config verbatim** — the declared append-only set, the
authorised-modified gate set, the prospectivity boundary and which
reading was used.

**`P9` at commit 3 has a subject and is not vacuous.** The range already
contains `reports/2026-08-12T1256Z_governance-enforcement.md`, which
arrives with the merge, so P9 checks that report. **What it does NOT
check at commit 3 is this task's own report, which does not yet exist.**
**Say so explicitly rather than reporting a bare `PASS`** — a P9 pass at
this head establishes a property of the arriving report only.

**A10-final, post-report evidence:** re-execute RUN 2 at commit 4, base
unchanged, **before the landing**. This is where this task's own report
first becomes a P9 subject. **If A10-final fails, STOP before advancing
`main`** — the landing has not happened and nothing needs undoing.

**Run it TWICE, and report both runs.** The range introduces two
specifications: this one, and the merged source specification whose
planted P1 mismatch — stated five, counted six — is preserved
byte-identically by A6 and may not be edited by §9. **A single run cannot
both honour the stop rule and integrate a deliberately defective artifact
unchanged.** Two runs separate the questions instead of choosing between
them.

    RUN 1  default subject selection: omit specification_paths from the
           config and let the checker take every specification added in
           the range
    RUN 2  explicit subject: specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md

**RUN 2 is the run the stop rule governs. Any failure there is a STOP**,
with no pre-authorised exception. **P1 must parse and pass on this
specification**: A5's governing sentence sits on ONE line immediately
before the scope block and states nine additions and zero modifications,
the manifest lists nine paths, and `modify:` carries `[]` rather than
prose. **The author ran the checker's P1 against this specification
before issuing it and measured stated 9, counted 9** — §11 records it.
**Report what you actually measured, not what §11 predicts.**
**If P1 reports `NOT_PARSEABLE` on it, that is a finding about this
specification and it is reported, not worked around.**

**RUN 1 governs nothing and stops nothing. It is reported as evidence
that the config was not tuned to produce green.** **Report the subject
list the default selection actually produced, as measured** — do not
assume it; whether a merge commit exposes the source specification's path
depends on how touched paths are derived, and that is a fact to observe
rather than predict. **If RUN 1's P1 fails on the source specification
for the planted five-versus-six reason, that is the expected and correct
behaviour of a tool doing its job**, and it is not a defect of this
integration.

**The exclusion in RUN 2 must be visible, never silent.** `P1`'s subject
is a caller-supplied set, which is the same discovery boundary the
classification marks `PARTIAL` for `P3` and `P7` — **a caller who may
choose the subject may also choose a subject that passes.** So: **both
configs verbatim in the report, both subject lists, and an explicit
sentence naming what RUN 2 excluded and why.** **A green RUN 2 whose
exclusion is not stated on its face is exactly the substitution the
integrated classification exists to prevent.**

**A11 — After the advance.** Remote `refs/heads/main` resolves to
commit 4; `8939ff4a…` and `fe8de65d…` are both ancestors of it;
`8939ff4a…` is still reachable with the same commit object — **no history
rewritten.** `governance/enforcement-checks` still resolves to
`fe8de65d…`, **not to commit 4.**

**A12 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, **and `tests/test_task_checker.py`,
which arrives with this merge.** **A12-pre is run at COMMIT 3 and goes in
the report** — commit 4 adds only a report file and changes no test.
**A12-final at the pushed `main` is post-report evidence.**

**A13 — Commit-message hygiene** on all four commits including the merge.
**Commits 1–3 are inspected before the report and go in it; commit 4's
stored message can only be read after it exists, so it is post-report
evidence.** For each:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its pre-execution review, and
  its report. **Everything arriving by merge is integrated exactly as
  reviewed and may not be edited.**
- **Do not edit `CONVENTIONS.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md` or `.github/workflows/ci.yml` by hand.**
- **Do not delete any branch**, including the six in the register and
  **the stopped first attempt at `58a996a4…`, which is the only record
  of why this task exists.**
- **Do not write a register entry.** §2b says why, and says whose job it
  is.
- **Do not adjust the checker to make this task pass.** If it fails,
  report the failure. **A tool whose first live use was to be weakened
  for its integrator is worth nothing.**
- **Do not adjust the CONFIG to make this task pass either.** RUN 2's
  subject is fixed by A10 at one named path. **Narrowing a subject set,
  supplying an empty declared set, or dropping a property is a
  specification stop, not an execution choice.**
- No gate, gate status, verdict, digest or hash-pinned artifact may be
  modified.
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase, no force-push, no history rewrite. **The landing is
  a fast-forward or a stop.**
- Any merge conflict is an immediate stop.
- Branch naming: use `governance/integrate-enforcement-checks-v2`. **The name is v2 because a first attempt exists and stopped; see §2b.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything listed in §5 under its correct layer, **with every
  committed figure labelled MEASURED or INTENDED**;
- **explicit confirmation that no statement in the committed report
  claims to measure commit 4**, which did not exist when the report was
  written;
- **A3's three values separately derived**, with the method for each;
- **A6's blob comparison for all six arriving paths**;
- **A7's path-by-path comparison**, the count of pre-existing paths
  checked, and **explicit confirmation that no modification was
  authorised and none occurred**;
- **A7's `tests/` statement with its predicate named** — 17 and 18 are
  both true of that directory under different predicates, and the
  previous task hit exactly that ambiguity;
- **A10's BOTH runs**: both configs verbatim, both JSON outputs
  verbatim, both subject lists as measured, and **the sentence naming
  what RUN 2 excluded and why**;
- whether any property reported `NOT_APPLICABLE`, `NOT_DECLARED` or
  `NOT_PARSEABLE` on this range, **with what that means rather than only
  the token**;
- **A9's six exit statuses, before and after the advance**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, and the remote ref read back;
- **§7's Rule 16 assessment**, both junctions addressed;
- **where a reader meeting line 607 of the integrated specification would
  find its correction**, and whether any existing convention would have
  pointed there;
- **whether `main` now reads as though governance were enforced.** It is
  not; §1 says so;
- **confirmation that you wrote no register entry**, and that
  `58a996a4…` still resolves and is untouched;
- **whether A5's one-line count sentence reads as a style choice rather
  than the labelled accommodation §2b says it is** — if it does, say so,
  because the next task removes the constraint and the label must not
  outlive it;
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
clone.**

**No measurement below was taken through a truncated view.** The author
produced two false records this session by piping output through `head`
or `tail` and recording the visible part; **counts here were obtained by
counting the whole set, and any listing shown is the complete set, not a
sample.**

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    origin/main = 8939ff4a…;
                governance/enforcement-checks = fe8de65d…;
                fe8de65d is NOT an ancestor of main

    target      stale base
    method      git merge-base --is-ancestor 8939ff4a fe8de65d;
                git merge-base
    MEASURED    exit 0; merge-base = 8939ff4a = main exactly.
                NO STALE BASE.

    target      the merge
    method      dry run from 8939ff4a with a placeholder specification
                commit and a placeholder review commit, then
                git merge --no-ff of the pinned ref
    MEASURED    no conflict; parent 1 = the placeholder review commit;
                parent 2 = fe8de65d; merge-base = 8939ff4a
    MEASURED    at the merge commit: 8 additions, 0 modifications
    MEASURED    with a placeholder report added: 9 additions,
                0 modifications, no other operation
    MEASURED    8939ff4a is a strict ancestor of that head, so the
                landing fast-forward is available

    target      the six arriving blob ids of A6
    method      git rev-parse fe8de65d:<path>, one per path
    MEASURED    all six, as listed in A6

    target      the false MEASURED line of §2
    method      git cat-file blob fe8de65d:specs/…governance-enforcement.md
                | grep -n "spec:"
    MEASURED    line 607. Counting ALL 42 merges reachable from main and
                classifying each parent-1 subject: SIX begin 'spec:' —
                ce86b534, 10f14f01, d8afb74e, d56335b5, 46b2915d,
                f62fc89a. The line is false.
    MEASURED    the correction is already committed, in §5 and §13 of
                reports/2026-08-12T1256Z_governance-enforcement.md,
                which arrives in the same merge

    target      protected paths and the two directories that grow
    method      git rev-parse <rev>:<path> per path; git ls-tree -r
    MEASURED    CONVENTIONS.md, DECISION_LOG.md, GATES.md,
                docs/BRANCHING_POLICY.md all blob-identical at
                8939ff4a and fe8de65d
    MEASURED    tests/ holds 17 test_*.py at the base and 18 at the
                branch head; 19 and 20 paths respectively counting
                README.md and __init__.py. THREE PREDICATES, THREE
                ANSWERS — A7 names its predicate for this reason.
    MEASURED    GATES.md 849a4fbf…, 14 P2- sections,
                P2-PHASE-01 PROPOSED

    target      the six register commits against the dry-run head
    method      git merge-base --is-ancestor, one per commit
    MEASURED    none is an ancestor; six separate exit statuses

    target      CI
    method      git cat-file blob fe8de65d:.github/workflows/ci.yml
    MEASURED    the workflow runs ruff and `python -m pytest`. There is
                NO occurrence of task_checker anywhere in it. The
                checker is not invoked by any automation.

    target      P1 run against THIS specification before issue
    method      the parser at 1922fe88… re-implemented line for line and
                run against this file's own text
    MEASURED    parse OK; governing line
                '**Final base-to-head scope: 9 additions and 0
                modifications.**'; stated 9; counted 9; PASS.
                The nine counted entries are the nine manifest paths and
                nothing else; 'modify: []' contributes none.

    target      whether a replacement branch is ever cut from its
                predecessor in this repository
    method      git merge-base --is-ancestor, predecessor against
                successor, for every superseded pair with a live
                successor
    MEASURED    supply-protocol-v2 40168469 is NOT an ancestor of
                supply-protocol-v3 aa531aea; their merge-base is
                0ab6369a, main at the time.
                supply-protocol-and-superseded 7146a093 is NOT an
                ancestor of aa531aea.
                gate/p2-land-diquark-line d64cd912 is NOT an ancestor of
                its v2.
                EVERY replacement branch was cut fresh from main.

    target      the stopped first attempt
    method      git rev-parse; git merge-base --is-ancestor
    MEASURED    58a996a4 exists; it descends from BOTH 8939ff4a and
                fe8de65d; it is NOT an ancestor of main. A branch cut
                fresh from main and merging fe8de65d does not carry it,
                so a future register entry naming it will not collide
                with P4.

    target      the checker's interface
    method      read scripts/governance_tools/task_checker.py at
                fe8de65d
    MEASURED    argparse with --repo defaulting to '.' and --config
                REQUIRED, which is why A10 requires the config verbatim
                rather than only the result
