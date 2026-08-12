# Task report — integrating the governance checker: MERGED, NOT LANDED

Specification:        `specs/2026-08-12T1820Z_integrate-enforcement-checks.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T1820Z_integrate-enforcement-checks.md`
Evidence base:        `8939ff4a46445d88c6470fb4f27eec71f2f39172`
Source branch:        `governance/enforcement-checks` @ `fe8de65de8288593f39a74110c1ea370ce27021f`
Branch:               `governance/integrate-enforcement-checks`
Merge commit:         `cb93c996f06cf3d648506e99afba4076b94cb095` (commit 3)
Pre-report head:      `cb93c996f06cf3d648506e99afba4076b94cb095`
UTC token `{HHMM}Z`:  `1820`, fixed by commit 1; `XX` = `12`

## STOP — A10 RUN 2 failed. `main` was not advanced.

**The merge is clean and every other criterion passes. RUN 2 — the run
A10 makes the stop rule govern — reported `P1: FAIL` on this
specification, and A10 gives it no pre-authorised exception.**

**§9 forbids the two things that would have made it pass:** *"Do not
adjust the checker to make this task pass"* and *"Do not adjust the
CONFIG to make this task pass either."* **I did neither.** The checker
arrived unedited by A6, RUN 2's subject is the single path A10 names, and
the landing did not happen. **Nothing needs undoing:** `main` is still
`8939ff4a…`.

**This is the checker's first live use on a real specification, and it
produced a FALSE FAIL.** §4 gives both causes — one in the checker, one
in this specification — measured rather than argued.

---

## 1. A1 — Refs

```
  remote refs/heads/main   8939ff4a46445d88c6470fb4f27eec71f2f39172
  refs/remotes/origin/main 8939ff4a46445d88c6470fb4f27eec71f2f39172
  source branch            fe8de65de8288593f39a74110c1ea370ce27021f
  local  main              0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)
```

**All three match. No mismatch, no STOP on A1.** No stale base:

```
git merge-base --is-ancestor 8939ff4a fe8de65d   ->  exit 0
git merge-base 8939ff4a fe8de65d                 ->  8939ff4a46445d88c6470fb4f27eec71f2f39172
```

## 2. A2 — Supply, and how each artifact arrived

**Both arrived as files, for the second task running.**

```
spec   supplied cc5a4e1b70ef00b2d61bc7b8dbdc0c7e7c8861c7da5abb88af875f6bd522d107
spec   committed cc5a4e1b70ef00b2d61bc7b8dbdc0c7e7c8861c7da5abb88af875f6bd522d107
review supplied 1209b669a718c2f17648f8d1e8686b3232243e7870ade976cb4756a562141fde
review committed 1209b669a718c2f17648f8d1e8686b3232243e7870ade976cb4756a562141fde
```

**Both byte-identical.** Review: 113 lines, 5738 bytes; zero occurrences of
`REVIEW ARTIFACT`, zero attachment-marker lines. **Correspondence by task
name**, `integrate-enforcement-checks`, at the review's line 3. **No
extraction of any kind.**

**The specification arrived as a file too**, so commit 1's bytes are the
sender's and are digest-verifiable — not my transcription.

## 3. A3 — Merge parentage, three separately derived measurements

```
parent 1  git rev-parse cb93c996^1          c96dc14a71210217ca690b739cee5ac99af6bd32
parent 1  cat-file, first 'parent' line     c96dc14a71210217ca690b739cee5ac99af6bd32
parent 2  git rev-parse cb93c996^2          fe8de65de8288593f39a74110c1ea370ce27021f
parent 2  cat-file, second 'parent' line    fe8de65de8288593f39a74110c1ea370ce27021f
base      git merge-base <p1> <p2>          8939ff4a46445d88c6470fb4f27eec71f2f39172
base      git merge-base 8939ff4a <ref>     8939ff4a46445d88c6470fb4f27eec71f2f39172
```

**Merge-base equals the evidence base and NOT parent 1** — measured, not
assumed — so a single shared derivation would have been detectable.
**Commit 1 is an ancestor of parent 1:** `exit 0`, CONFIRMED.

The merge was clean: `6 files changed, 3199 insertions(+)`, **0 unmerged
paths, 0 deletions**, `--no-ff` of the pinned remote ref.

## 4. A10 — The two runs, and the stop

### RUN 1 — default subject selection, observational only

Config, verbatim:

```json
{
  "base": "8939ff4a46445d88c6470fb4f27eec71f2f39172",
  "head": "HEAD",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": [],
  "authorised_modified_gates": []
}
```

**Subject list as MEASURED, not predicted** — the default selection did
expose the merged source specification:

```
specs/2026-08-12T1256Z_governance-enforcement.md        parse OK  stated 5  counted 6
specs/2026-08-12T1820Z_integrate-enforcement-checks.md  parse OK  stated 0  counted 10
```

```
overall: FAIL   exit 2
  P1 PARTIAL    FAIL          P2 MECHANICAL PASS      P3 PARTIAL NOT_APPLICABLE
  P4 MECHANICAL PASS          P5 PARTIAL    PASS      P6 PARTIAL PASS
  P7 PARTIAL    PASS          P8 MECHANICAL PASS      P9 MECHANICAL PASS
```

**The 5-versus-6 hit on the source specification is the planted defect
doing exactly what it was planted to do**, and §8 of A10 says so: it is
the correct behaviour of a tool doing its job, not a defect of this
integration. **RUN 1 governs nothing and stopped nothing.** It is reported
as evidence that the config was not tuned to produce green — and it could
not have been, because RUN 2 failed too.

### RUN 2 — explicit subject, the run the stop rule governs

Config, verbatim — **identical to RUN 1 but for the added
`specification_paths`**:

```json
{
  "base": "8939ff4a46445d88c6470fb4f27eec71f2f39172",
  "head": "HEAD",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": [],
  "authorised_modified_gates": [],
  "specification_paths": ["specs/2026-08-12T1820Z_integrate-enforcement-checks.md"]
}
```

**What RUN 2 excluded, and why — stated on its face as A10 requires.**
**RUN 2 excludes `specs/2026-08-12T1256Z_governance-enforcement.md`**, the
specification arriving with the merge. **It is excluded because its P1
mismatch is deliberate, was reviewed, and is preserved byte-identically by
A6 and unerasable by §3** — not because it fails. **A caller who may
choose the subject may also choose a subject that passes**, which is the
same discovery boundary the integrated classification marks `PARTIAL` for
P3 and P7. **In this instance the narrowing bought nothing: RUN 2 failed
anyway.**

```
specs/2026-08-12T1820Z_integrate-enforcement-checks.md  parse OK  stated 0  counted 10

overall: FAIL   exit 2
  P1 PARTIAL    FAIL          P2 MECHANICAL PASS      P3 PARTIAL NOT_APPLICABLE
  P4 MECHANICAL PASS          P5 PARTIAL    PASS      P6 PARTIAL PASS
  P7 PARTIAL    PASS          P8 MECHANICAL PASS      P9 MECHANICAL PASS
```

### Why P1 failed: two defects, one on each side

**A10 predicted "A5's governing sentence states nine additions immediately
before its scope block, and the manifest lists nine paths". Measured, the
first half is not true of the file's lines and the second is not true of
the block's records.**

**Defect (a) — in the CHECKER. A5's governing sentence wraps across two
physical lines:**

```
   L228: '**A5 — Scope, frozen manifest. Final base-to-head scope: 9 additions and'
   L229: '0 modifications.**'          <-- SELECTED as governing
   L230: ''
   L231: '    base: 8939ff4a46445d88c6470fb4f27eec71f2f39172'
   L232: '    head: <commit 4>'
   L233: '    mode: exact'
   L234: '    add:'
```

**The grammar defines "the GOVERNING SENTENCE" but implements "the
governing LINE".** It walks back to the nearest preceding line carrying a
count, finds the continuation `0 modifications.**`, and reads
**stated = 0**. **The "9 additions" on line 228 is never seen.** A
sentence that wraps is invisible to a line-oriented parser, and every
specification in this programme wraps at ~72 columns.

**Defect (b) — in THIS SPECIFICATION.** The manifest writes:

```
    modify:
      (none)
```

**`(none)` is prose in a machine-readable slot.** The checker counts the
records under `add:` and `modify:`, so it counts `(none)` as a tenth path
and reads **counted = 10**. Every other specification in this line writes
`modify: []`, which the grammar handles, or lists real paths.

**Net: stated 0, counted 10, on a manifest whose human arithmetic — nine
additions, zero modifications, nine paths — is correct.** **P1 reported a
FALSE FAIL.**

**I did not repair either defect.** §9 forbids adjusting the checker;
§3 forbids editing anything arriving from the branch, and
`task_checker.py` arrives from it; and A6 pins its blob, which §5 of the
guard verified. **The specification's `(none)` is likewise not mine to
edit** — it is committed at commit 1 exactly as supplied.

### Properties reporting other than PASS/FAIL, with what they mean

- **P3 `NOT_APPLICABLE`** — the caller declared an empty append-only set
  for this range. **This range genuinely appends to nothing**:
  `DECISION_LOG.md` is blob-identical base to commit 3. It is not
  `NOT_DECLARED`, which would have made the run `INCOMPLETE`.
- **P9 `PASS`, and the pass is narrower than the token.** At commit 3 P9's
  only subject is `reports/2026-08-12T1256Z_governance-enforcement.md`,
  which arrives with the merge. **It does NOT check this task's own
  report, which did not exist when the run was made.** A10 requires that
  said explicitly rather than a bare `PASS`, and this is it.
- **No property reported `NOT_DECLARED` or `NOT_PARSEABLE`** on this
  range under either run.

## 5. A5, A6, A7, A8, A9 — everything else, all passing

### A5 — scope, MEASURED at commit 3

```
  A	derivations/GOVERNANCE-ENFORCEMENT_classification.md
  A	reports/2026-08-12T1256Z_governance-enforcement.md
  A	reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
  A	reviews/chatgpt/2026-08-12T1820Z_integrate-enforcement-checks.md
  A	scripts/governance_tools/task_checker.py
  A	specs/2026-08-12T1256Z_governance-enforcement.md
  A	specs/2026-08-12T1820Z_integrate-enforcement-checks.md
  A	tests/test_task_checker.py

  counts: 8 A, 0 M
```

**MEASURED at commit 3: 8 additions, 0 modifications**, which is A5's
stated commit-3 figure.

**INTENDED, not measured:** the nine-path final manifest of A5 would be
reached at commit 4. **Because the task stops, the intention is recorded
and no landing follows it.** **Nothing in this report claims to measure
commit 4** — see §8.

### A6 — six arriving paths, blob-identical

```
  derivations/GOVERNANCE-ENFORCEMENT_classification.md       merged=183df9468c98 source=183df9468c98 PASS
  reports/2026-08-12T1256Z_governance-enforcement.md         merged=1afd8497e7dd source=1afd8497e7dd PASS
  reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md merged=670a9fc35230 source=670a9fc35230 PASS
  scripts/governance_tools/task_checker.py                   merged=1922fe88f3a2 source=1922fe88f3a2 PASS
  specs/2026-08-12T1256Z_governance-enforcement.md           merged=9ab2cb631381 source=9ab2cb631381 PASS
  tests/test_task_checker.py                                 merged=a68568568f50 source=a68568568f50 PASS
```

**All six identical, and all six match A6's pinned values.** The guard's
`pinned_artifacts` were run separately on SHA-256 digests — **both were
run, neither substituted for the other**, as A6 requires.

### A7 — protected paths, path by path

```
  MODIFICATIONS: NONE — none authorised, none occurred
  DELETIONS   : NONE
    CONVENTIONS.md                   identical=True
    DECISION_LOG.md                  identical=True
    docs/BRANCHING_POLICY.md         identical=True
    GATES.md                         identical=True
    AGENTS.md                        identical=True
    pyproject.toml                   identical=True
    .github/workflows/ci.yml         identical=True
    scripts/       pre-existing=59   identical=59   differing=0  gained=['scripts/governance_tools/task_checker.py']
    results/       pre-existing=69   identical=69   differing=0  gained=[]
    tests/         pre-existing=19   identical=19   differing=0  gained=['tests/test_task_checker.py']
    derivations/   pre-existing=34   identical=34   differing=0  gained=['derivations/GOVERNANCE-ENFORCEMENT_classification.md']
    docs/          pre-existing=7    identical=7    differing=0  gained=[]
    reviews/       pre-existing=23   identical=23   differing=0  gained=[2 authorised paths]
    TOTAL pre-existing checked: 211
```

**211 pre-existing paths compared individually. No modification was
authorised and none occurred** — the previous integration's three-path
exception was not carried over. **`.github/workflows/ci.yml` is
blob-identical**, as §3 requires.

**`tests/`, with its predicate named: 17 `test_*.py` at the base, 18 at
commit 3.** The directory holds 19 and 20 total paths respectively
counting `README.md` and `__init__.py`. **Three predicates, three
answers** — the ambiguity the last two tasks hit, stated here rather than
left to a reader. **`tests/` and `scripts/governance_tools/` each gain
exactly one path, so their tree objects differ from the base, and that is
correct for this task.**

### A8 — append-only and gates, trivially

`DECISION_LOG.md` blob-identical (`d9dd2bf3a8cc…` both sides), so
append-only holds **with nothing appended**. `GATES.md` blob
`849a4fbfe62d6478f092a84b0175357a74bbbb06`, **14** `^## P2-` sections,
**`P2-PHASE-01` still `PROPOSED`.**

### A9 — six register commits against commit 3

```
  52f65117 exit=1 NOT ancestor — PASS      7146a093 exit=1 NOT ancestor — PASS
  ebd531ab exit=1 NOT ancestor — PASS      10c260b9 exit=1 NOT ancestor — PASS
  40168469 exit=1 NOT ancestor — PASS      d64cd912 exit=1 NOT ancestor — PASS
```

**Six separate exit statuses.** **The post-advance re-check A9 also
requires did not occur, because no advance occurred.**

## 6. A4, A12-pre, A13

### A4 — `PRE_MERGE`

```
overall: PASS
  worktree_clean                     PASS
  worktree_matches_declared_target   PASS
  merge_base                         PASS
  scope                              PASS  (2 ops, failures=[])
  pinned_artifacts                   PASS  (6/6 pins)
EXIT: 0
```

**The final `POST_MERGE` was NOT run**, because it verifies remote
agreement against the pushed `main` and no push occurred. **Its two
distinct SHA roles are representable** — `merge_commit` and
`expected_remote_sha` — so A4's stop condition on the guard's expressive
power does not apply; the guard simply has no second subject yet.

### A12-pre at commit 3

```
  tests/test_repository_structure.py     exit=0
  tests/test_si1_governance.py           exit=0
  tests/test_gate_anchors.py             exit=0
  tests/test_governance_tools.py         exit=0
  tests/test_task_checker.py             exit=0
```

**All five exit 0, including the 42-test suite arriving with the merge.**

### A13 — commits 1 to 3

Method: proposed message written to a file and scanned before committing;
stored message read back from the object and scanned again. Pattern,
case-insensitive:
`co-authored-by|claude-session|noreply@|https?://|opus|sonnet|anthropic`.

    commit 1 (bc4c44ab)  proposed: none   stored: none   suppressed: NONE
    commit 2 (c96dc14a)  proposed: none   stored: none   suppressed: NONE
    commit 3 (cb93c996)  proposed: none   stored: none   suppressed: NONE  — the merge

**No trailer was suppressed on any commit, because none appeared.** The
author identity field matches `noreply@` on the raw object; **it is not
message content**, and is the repository's standing identity.

**Commit 4's stored message is post-report evidence** and is not claimed
here.

## 7. Rule 16 assessment — both junctions

**Rule 16 is operative.**

**Junction one, confirmed.** After this merge the branch carries a
checker, forty-two passing tests, and a classification saying twenty-two
of twenty-nine objects have no machine behind them. **The tests will be
met before the classification is** — a green suite is visible, the
classification is a file someone must open. **The reading to be prevented
is "governance is now covered by tests".**

**And this task is the sharpest available evidence against that reading.**
**The checker's first live use on a real specification produced a false
FAIL** on a manifest that is arithmetically correct. **Forty-two green
tests did not predict that**, because they test the checker against
fixtures the checker's author wrote. §4(a) is a defect no fixture
contained: **no test in the suite uses a governing sentence that wraps**,
and every real specification wraps.

**Junction two — the correction-discoverability gap, which this merge does
not close.** A reader meeting the false `MEASURED` line at line 607 of
`specs/2026-08-12T1256Z_governance-enforcement.md` **has no pointer from
there to its correction**, which lives in §5 and §13 of
`reports/2026-08-12T1256Z_governance-enforcement.md` — arriving in the
same merge, discoverable only by knowing to look.

**Where I would put such a pointer, asked and answered — I did not create
one.** A one-line `> CORRECTED: see <report path> §5` immediately beneath
the false line, in the *report* rather than the specification, would be
wrong: the specification is where the reader is. **The honest placement is
a repository-level `CORRECTIONS.md` index keyed by `path:line`**, because
the specification itself is a reviewed artifact that may not be retouched
— which is exactly the constraint that created the gap.

**Would any existing convention have created one? No, and I checked
three.** **Rule 15** commits the artifacts but says nothing about linking
them. **Rule 7** (evidence precedence) tells a reader which source wins
when they disagree, but only once the reader has both — it presumes the
discovery this gap prevents. **Amendment L** is the closest and the same
shape: it requires a consumed convention to be discoverable *through the
conventions index*. **There is no equivalent index for corrections.**
Amendment L's own known instance is unresolved, so the pattern has now
produced two instances and no mechanism.

## 8. What this report does not claim

**No statement in this report claims to measure commit 4.** Every figure
is either **MEASURED at commit 3 or earlier**, or explicitly labelled
**INTENDED**. Specifically:

- A5's 8-additions figure is **MEASURED** at commit 3;
- A5's 9-path final manifest is **INTENDED** and, because of the stop,
  never became a measurement;
- A10's two runs are **MEASURED** at commit 3;
- commit 4's stored message, A10-final, A12-final, the final scope, the
  final `POST_MERGE`, the push and the post-advance A9 are **not present
  in any form**, because none of them happened.

**`main` did not advance, so the entire post-advance evidence layer is
empty rather than partial.**

## 9. Stops and clarifications

### `SPECIFICATION_DEFECT`

**One, BLOCKING — the stop, jointly with the checker defect below.**
**A5's manifest writes `(none)` under `modify:`.** Every other manifest in
this line writes `modify: []` or lists paths. **A machine-readable slot
carrying prose is a defect in a document whose own A10 requires a machine
to parse it**, and it contributes 1 of the 10 counted records.

**One, non-blocking, and it is an Amendment H literal.** A10 asserts
*"A5's governing sentence states nine additions immediately before its
scope block"*. **Measured, the line immediately before the block is
`mode: exact`, and the nearest preceding line carrying a count is
`0 modifications.**`.** The assertion is true of the *sentence* and false
of the *lines*, and P1 reads lines. **This is the third Amendment H
literal in three tasks that did not survive measurement**, after the
register count read from a truncated diff and the `spec:` parent-1 claim.

**A9's planted defect in the merged specification is NOT a stop** — RUN 1
found it, A10 §8 pre-classifies it as correct behaviour, and RUN 2
excludes it for the stated reason in §4.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

**One, in the checker I wrote and this task integrates — and it is half
the stop.** **P1's grammar implements "the governing LINE" while its
documentation, the classification and A10 all say "the governing
SENTENCE".** A sentence wrapped across two physical lines is read from its
tail. **Its own test suite does not catch this**: the fixture
`test_p1_selects_the_governing_sentence_not_another_count` uses a
single-line governing sentence, so the 42 green tests are silent on the
one shape every real specification has.

**I did not fix it.** §9 forbids adjusting the checker to make this task
pass, and the fix would have done exactly that. **A tool whose first live
use was to be weakened for its integrator is worth nothing** — and the
converse holds too: a tool whose first live use exposes a real defect has
earned its keep, provided the defect is reported rather than patched
away.

### `REPOSITORY_DEFECT`

**None introduced.** Nothing arriving by merge was edited; 211
pre-existing paths are blob-identical; no modification occurred.

**Two pre-existing and unchanged.** The enforcement gap — the workflow
runs `pytest` and never invokes `task_checker.py` — is untouched, and §3
forbids touching it. **The correction-discoverability gap of §7 remains
open**, deliberately.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None requiring a ruling.** The prospectivity boundary was taken as
`ce86b534…` under the INCLUSIVE reading, as named in both configs; that
question was retired for post-boundary ranges by the previous task's
measurement and nothing here reopens it.

## 10. Does `main` now read as though governance were enforced?

**`main` is unchanged, so the question is about what the branch would have
landed — and the answer would have been yes, misleadingly.**

**Nothing that lands here enforces anything.** The workflow runs `ruff` and
`python -m pytest`; **there is no occurrence of `task_checker` in it.** The
accurate name for what this branch carries is **available governance
verification, not enforced governance** — and §1 of the specification is
right that moving the gap from "no tool" to "a tool nothing calls" is the
harder version to notice, because a tool's existence reads as reassurance.

**This task adds one datum to that argument.** The tool nothing calls was
called once, by hand, on a real specification, **and was wrong.**

## 11. Ambiguous, unsatisfiable, or would have specified differently

- **A10's stop rule and A6's integrate-unedited rule are jointly
  satisfiable only because RUN 2's failure was not in the merged
  artifact.** Had P1 failed on something arriving from the branch, §3
  would have forbidden the fix and A10 would have demanded a stop, with no
  path forward but a re-issue. **That is the right design** — it is what
  kept this stop clean — but it is worth naming that the two rules are in
  tension by construction.
- **A10's prediction about A5 should have been a measurement.** The
  specification asserts what P1 will find without having run P1 on itself.
  **Running the checker against its own commissioning document before
  issue would have caught both defects** — the wrap and the `(none)` — and
  the tool to do it was already committed at `fe8de65d…`. **That is the
  single change I would make to this specification.**
- **A5's `modify: (none)` should be `modify: []`.** The previous
  specification in this line used `modify: []` and parsed.
- **The report contract asks for post-advance evidence that a stop makes
  unavailable.** The review's §7 anticipated this and said to interpret
  §10 across both layers without collapsing them; **§8 above records the
  post-advance layer as empty rather than omitting it silently.**
- **Nothing else was unsatisfiable.** No instruction conflicted with a
  repository rule.

## 12. What this task did not do

**It did not land.** `main` is `8939ff4a…`, unmoved; no fast-forward was
attempted; no push to `main` occurred. **It did not adjust the checker or
the config to pass.** **It edited nothing arriving from the branch** — the
false `MEASURED` line, the classification and the checker are all
integrated exactly as reviewed. **It modified `.github/workflows/ci.yml`
not at all**, and claims no CI enforcement. **It added, removed and
re-worded no classification verdict.** No branch was deleted; the six
register branches are untouched and none is an ancestor. No gate, gate
status, verdict, digest or hash-pinned artifact was modified. **No history
was rewritten**, and the merge is a genuine `--no-ff` with two parents.
