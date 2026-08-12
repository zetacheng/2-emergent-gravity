# Task report — integrating the governance checker, and landing it (second attempt)

Specification:        `specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T1919Z_integrate-enforcement-checks-v2.md`
Evidence base:        `8939ff4a46445d88c6470fb4f27eec71f2f39172`
Source branch:        `governance/enforcement-checks` @ `fe8de65de8288593f39a74110c1ea370ce27021f`
Stopped first attempt: `governance/integrate-enforcement-checks` @ `58a996a46b1f446fee1517c583bf3b27a4561b74`
Branch:               `governance/integrate-enforcement-checks-v2`
Merge commit:         `c8357ec53e347f5ce7167804a03b3412519f906d` (commit 3)
Pre-report head:      `c8357ec53e347f5ce7167804a03b3412519f906d`
UTC token `{HHMM}Z`:  `1919`, fixed by commit 1; `XX` = `12`

**RUN 2 — the run the stop rule governs — PASSED, exit 0.** Both triggers
of the first attempt's false positive are gone: **stated 9, counted 9**,
measured on this specification, not predicted. **RUN 1 fails only on the
merged source specification's planted five-versus-six**, which is the tool
doing its job.

**Every figure below is labelled MEASURED or INTENDED.** **No statement in
this report claims to measure commit 4** — see §9.

---

## 1. A1 — Refs, and the stopped attempt

**MEASURED**, read from the remote:

```
  remote refs/heads/main                            8939ff4a46445d88c6470fb4f27eec71f2f39172
  refs/remotes/origin/main                          8939ff4a46445d88c6470fb4f27eec71f2f39172
  governance/enforcement-checks                     fe8de65de8288593f39a74110c1ea370ce27021f
  governance/integrate-enforcement-checks (stopped) 58a996a46b1f446fee1517c583bf3b27a4561b74
  local refs/heads/main (stale by design)           0f7961747abe2a18b436c0b1e5b928f425ea4d9a
```

**All four match. No mismatch, no STOP.** No stale base:

```
git merge-base --is-ancestor 8939ff4a fe8de65d   ->  exit 0
git merge-base 8939ff4a fe8de65d                 ->  8939ff4a46445d88c6470fb4f27eec71f2f39172
```

**§11's ancestry claim about the stopped attempt, verified independently
rather than accepted:**

```
  8939ff4a IS an ancestor of 58a996a4
  fe8de65d IS an ancestor of 58a996a4
  58a996a4 is NOT an ancestor of main
```

**This branch was cut fresh from `main` and merges `fe8de65d…`, so it does
not carry `58a996a4…`** — which is what makes a future register entry
naming the stopped attempt compatible with P4. **`58a996a4…` was not
touched, not deleted and not merged.**

## 2. A2 — Supply, and the provenance note

**Both artifacts arrived as files**, for the third task running.

```
spec   supplied  8a8b5037fc579340142195dec61519d98ddbe14ea9362210f80a76d8e50d87aa
spec   committed 8a8b5037fc579340142195dec61519d98ddbe14ea9362210f80a76d8e50d87aa
review supplied  a87902e4f6edd713967ba4e84aa03125a93b14b5b6edd20eb81a76cd23865221
review committed a87902e4f6edd713967ba4e84aa03125a93b14b5b6edd20eb81a76cd23865221
```

**Both byte-identical.** Review: zero occurrences of `REVIEW ARTIFACT`,
zero attachment-marker lines, correspondence by task name
`integrate-enforcement-checks-v2`. **No extraction of any kind.**

### The provenance note's two digests, and what I can and cannot confirm

The specification's provenance note asks me to report both digests and
confirm the delta.

    reviewer-approved, as STATED in the note   9253179cdec554a7f986cd62a5e376599111b400cefd43a4983b4f1a4242cfd7
    the file I received and committed          8a8b5037fc579340142195dec61519d98ddbe14ea9362210f80a76d8e50d87aa

**They differ, which is expected — the note says one change was applied
after approval.**

**What I confirmed by measurement:** the applied wording is present.
§2b line 124 reads **"This specification removes both TRIGGERS of the
known false positive."** — not "carries both FIXES". The note's own
account of why is borne out two lines below it, where `modify: []` is
called a correction and the one-line count sentence an accommodation.

**What I CANNOT confirm, and will not imply otherwise: that this is the
ONLY delta.** **The artifact digesting to `9253179c…` was not supplied to
me**, so I have nothing to diff against. **I verified the presence of the
stated change, not the absence of others.** A reader should treat the
"only delta" claim as the specification author's assertion, not as
something this execution established. **Supplying the approved artifact
alongside the amended one would make the claim checkable in one command.**

## 3. A3 — Merge parentage, three separately derived measurements

**MEASURED**, each by its own method:

```
parent 1  git rev-parse c8357ec5^1        f7f483802640c8fd853610793b7408430db0ec63
parent 1  cat-file, first 'parent' line   f7f483802640c8fd853610793b7408430db0ec63
parent 2  git rev-parse c8357ec5^2        fe8de65de8288593f39a74110c1ea370ce27021f
parent 2  cat-file, second 'parent' line  fe8de65de8288593f39a74110c1ea370ce27021f
base      git merge-base <p1> <p2>        8939ff4a46445d88c6470fb4f27eec71f2f39172
base      git merge-base 8939ff4a <ref>   8939ff4a46445d88c6470fb4f27eec71f2f39172
```

**The merge-base equals the evidence base and NOT parent 1** — measured,
so a single shared derivation would have been detectable. **Commit 1 is an
ancestor of parent 1:** `exit 0`, CONFIRMED.

The merge was clean: **0 unmerged paths, 0 deletions**, `--no-ff` of the
pinned remote ref.

## 4. A4 — `PRE_MERGE`

**MEASURED before the merge:**

```
overall: PASS
  worktree_clean                     PASS
  worktree_matches_declared_target   PASS
  merge_base                         PASS
  scope                              PASS  (2 ops, failures=[])
  pinned_artifacts                   PASS  (6/6 pins)
EXIT: 0
```

**Both identifier kinds were run and neither substituted for the other**,
as A6 requires: the guard's `pinned_artifacts` on SHA-256 content digests
above, and A6's Git blob ids in §6.

**The final `POST_MERGE` carries two distinct SHA roles** — `merge_commit`
for the object under verification, `expected_remote_sha` for agreement
against the pushed `main`. The guard represents both separately, so A4's
stop condition does not apply. **It is post-report evidence.**

## 5. A10 — The two runs, MEASURED at commit 3

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

**Subject list as MEASURED** — the default selection did expose the merged
source specification:

```
specs/2026-08-12T1256Z_governance-enforcement.md              parse OK  stated 5  counted 6
specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md     parse OK  stated 9  counted 9
```

```
overall: FAIL   exit 2
  P1 PARTIAL    FAIL            P2 MECHANICAL PASS      P3 PARTIAL NOT_APPLICABLE
  P4 MECHANICAL PASS            P5 PARTIAL    PASS      P6 PARTIAL PASS
  P7 PARTIAL    PASS            P8 MECHANICAL PASS      P9 MECHANICAL PASS
```

**The five-versus-six hit is the planted defect being caught**, which A10
pre-classifies as correct behaviour and not a defect of this integration.
**RUN 1 governs nothing and stopped nothing**, and it is the evidence that
the config was not tuned to produce green: **the same config, run without
a subject restriction, still fails.**

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
  "specification_paths": ["specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md"]
}
```

**What RUN 2 excluded, and why — stated on its face.** **RUN 2 excludes
`specs/2026-08-12T1256Z_governance-enforcement.md`**, the specification
arriving with the merge. **It is excluded because its P1 mismatch is
deliberate, was reviewed, and is preserved byte-identically by A6 and
unerasable by §3** — not because it is inconvenient. **A caller who may
choose the subject may also choose a subject that passes**, which is the
same discovery boundary the integrated classification marks `PARTIAL` for
P3 and P7. **This exclusion is the reason RUN 1 exists**: RUN 1 shows what
the unrestricted config reports, so the narrowing cannot hide anything.

```
specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md     parse OK  stated 9  counted 9

overall: PASS   exit 0
  P1 PARTIAL    PASS            P2 MECHANICAL PASS      P3 PARTIAL NOT_APPLICABLE
  P4 MECHANICAL PASS            P5 PARTIAL    PASS      P6 PARTIAL PASS
  P7 PARTIAL    PASS            P8 MECHANICAL PASS      P9 MECHANICAL PASS
```

**MEASURED, not predicted: stated 9, counted 9, PASS.** §11 predicted the
same values; **this report states what the run produced.** The governing
line the parser selected was
`**Final base-to-head scope: 9 additions and 0 modifications.**`, and the
nine counted entries are the nine manifest paths — **`modify: []`
contributed none**, which is the whole of the `(none)` correction.

### Properties reporting other than PASS/FAIL, with what they mean

- **P3 `NOT_APPLICABLE`** — the caller declared an **empty** append-only
  set, and this range genuinely appends to nothing: `DECISION_LOG.md` is
  blob-identical base to commit 3. **This is not `NOT_DECLARED`**, which
  would have meant "the caller never said" and would have made the run
  `INCOMPLETE` and non-zero.
- **P9 `PASS`, and the pass is narrower than the token.** At commit 3 P9's
  only subject is `reports/2026-08-12T1256Z_governance-enforcement.md`,
  arriving with the merge. **It does NOT check this task's own report,
  which did not exist when the run was made.** A10 requires that said
  explicitly rather than a bare `PASS`, and this is it. **This task's
  report first becomes a P9 subject at A10-final**, which is post-report
  evidence.
- **No property reported `NOT_DECLARED` or `NOT_PARSEABLE`** under either
  run.

## 6. A5, A6, A7, A8, A9 — MEASURED at commit 3

### A5 — scope

```
  A	derivations/GOVERNANCE-ENFORCEMENT_classification.md
  A	reports/2026-08-12T1256Z_governance-enforcement.md
  A	reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
  A	reviews/chatgpt/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
  A	scripts/governance_tools/task_checker.py
  A	specs/2026-08-12T1256Z_governance-enforcement.md
  A	specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
  A	tests/test_task_checker.py

  counts: 8 A, 0 M
```

**MEASURED at commit 3: 8 additions, 0 modifications.**

**INTENDED, not measured — the final manifest** reaches nine additions and
zero modifications once commit 4 exists, the ninth being this report.
**That figure is an intention in this report and a measurement only in the
post-report layer.** The intended manifest is A5's, verbatim, with
`{HHMM}Z` resolved to `1919`:

```
    base: 8939ff4a46445d88c6470fb4f27eec71f2f39172
    head: <commit 4>
    mode: exact
    add:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      reports/2026-08-12T1256Z_governance-enforcement.md
      reports/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
      reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
      reviews/chatgpt/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
      scripts/governance_tools/task_checker.py
      specs/2026-08-12T1256Z_governance-enforcement.md
      specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
      tests/test_task_checker.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown
```

### A6 — six arriving paths, blob-identical

```
  derivations/GOVERNANCE-ENFORCEMENT_classification.md       merged=183df9468c98 source=183df9468c98 PASS
  reports/2026-08-12T1256Z_governance-enforcement.md         merged=1afd8497e7dd source=1afd8497e7dd PASS
  reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md merged=670a9fc35230 source=670a9fc35230 PASS
  scripts/governance_tools/task_checker.py                   merged=1922fe88f3a2 source=1922fe88f3a2 PASS
  specs/2026-08-12T1256Z_governance-enforcement.md           merged=9ab2cb631381 source=9ab2cb631381 PASS
  tests/test_task_checker.py                                 merged=a68568568f50 source=a68568568f50 PASS
```

**All six identical and all six match A6's pinned values.** **Nothing
arriving by merge was edited** — including the false `MEASURED` line, the
classification and the checker whose defect stopped the first attempt.

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
    scripts/       pre-existing=59   identical=59   differing=0  gained=1
    results/       pre-existing=69   identical=69   differing=0  gained=0
    tests/         pre-existing=19   identical=19   differing=0  gained=1
    derivations/   pre-existing=34   identical=34   differing=0  gained=1
    docs/          pre-existing=7    identical=7    differing=0  gained=0
    reviews/       pre-existing=23   identical=23   differing=0  gained=2
    TOTAL pre-existing checked: 211
```

**211 pre-existing paths compared individually. No modification was
authorised and none occurred** — the previous integration's three-path
exception was not carried over. **`.github/workflows/ci.yml` is
blob-identical**, so no CI claim is available to this task and none is
made.

**`tests/`, with its predicate named: 17 `test_*.py` at the base, 18 at
commit 3.** The directory holds 19 and 20 total paths respectively
counting `README.md` and `__init__.py`. **Three predicates, three
answers.** **`tests/` and `scripts/governance_tools/` each gain exactly
one path, so their tree objects differ from the base — correct here, and
the opposite of what the last two specifications asserted.**

### A8 — append-only and gates

`DECISION_LOG.md` blob-identical (`d9dd2bf3a8cc…` both sides), so
**append-only holds with nothing appended.** `GATES.md` blob
`849a4fbfe62d6478f092a84b0175357a74bbbb06`, **14** `^## P2-` sections,
**`P2-PHASE-01` still `PROPOSED`.**

### A9 — six register commits against commit 3

```
  52f65117 exit=1 NOT ancestor — PASS      7146a093 exit=1 NOT ancestor — PASS
  ebd531ab exit=1 NOT ancestor — PASS      10c260b9 exit=1 NOT ancestor — PASS
  40168469 exit=1 NOT ancestor — PASS      d64cd912 exit=1 NOT ancestor — PASS
```

**Six separate exit statuses.** **The post-advance re-check is post-report
evidence.**

## 7. A12-pre and A13

### A12-pre — five validators at commit 3

```
  tests/test_repository_structure.py     exit=0
  tests/test_si1_governance.py           exit=0
  tests/test_gate_anchors.py             exit=0
  tests/test_governance_tools.py         exit=0
  tests/test_task_checker.py             exit=0
```

**All five exit 0, including the 42-test suite arriving with this merge.**

### A13 — commits 1 to 3

Method: proposed message written to a file and scanned before committing;
stored message read back from the object and scanned again. Pattern,
case-insensitive:
`co-authored-by|claude-session|noreply@|https?://|opus|sonnet|anthropic`.

    commit 1 (4ddafa53)  proposed: none   stored: none   suppressed: NONE
    commit 2 (f7f48380)  proposed: none   stored: none   suppressed: NONE
    commit 3 (c8357ec5)  proposed: none   stored: none   suppressed: NONE  — the merge

**No trailer was suppressed on any commit, because none appeared.** The
author identity field matches `noreply@` on the raw object; **it is not
message content**, and is the repository's standing identity.

Commit 1–3 SHAs and stored messages:

    4ddafa53cd61fcfc3648ac908a504f7164a10009
      spec: integrate the governance checker and land it (second attempt)
    f7f483802640c8fd853610793b7408430db0ec63
      review: pre-execution review for the enforcement-checks integration v2
    c8357ec53e347f5ce7167804a03b3412519f906d
      merge: land the governance classification, checker and its tests
      (full body as quoted in the merge output; stored scan clean)

**Commit 4's stored message is post-report evidence.** Its intended text,
scanned clean at authoring time:

```
docs: report the enforcement-checks integration and its landing

Records A1-A13 measured at commit 3, both A10 runs with their configs
verbatim, and the intended final manifest as an intention rather than a
measurement.

RUN 2 passed at stated 9, counted 9. RUN 1 fails only on the merged
source specification's planted five-versus-six, which is the checker
working. The line-versus-paragraph grammar defect is untouched and the
one-line count sentence is an accommodation that lasts one task.

No register entry was written; the stopped first attempt is preserved.
```

**Intended fast-forward parameters:** advance remote `refs/heads/main` to
commit 4 by `git push origin <commit 4>:refs/heads/main`, **no `--force`,
no `--force-with-lease`**, after A10-final passes at commit 4.

## 8. §7 — Rule 16 assessment, both junctions

**Junction one, confirmed.** After this merge `main` carries a checker,
forty-two passing tests, and a classification saying twenty-two of
twenty-nine objects have no machine behind them. **The tests will be met
before the classification is** — a green suite is visible, the
classification is a file someone must open. **The reading to be prevented
is "governance is now covered by tests".**

**The first attempt is the strongest available evidence against that
reading, and it lands as part of the record.** `58a996a4…` holds a
complete account of the checker's first live use on a real specification
**producing a false FAIL.** Forty-two green tests did not predict it,
because **no fixture in the suite uses a governing sentence that wraps**,
and every real specification wraps. **A green suite tells you the checker
behaves as its author imagined, not as documents actually are.**

**Junction two — correction discoverability, unchanged by this task.** A
reader meeting the false `MEASURED` line at line 607 of
`specs/2026-08-12T1256Z_governance-enforcement.md` **has no pointer from
there to its correction**, which lives in §5 and §13 of
`reports/2026-08-12T1256Z_governance-enforcement.md` — arriving in the
same merge, discoverable only by knowing to look.

**Where I would put such a pointer — asked, answered, and NOT created
here.** **A repository-level `CORRECTIONS.md` index keyed by `path:line`**
is the honest placement. A note beneath the false line would be better for
the reader and is unavailable: **the specification is a reviewed artifact
that may not be retouched**, which is the constraint that created the gap.

**Would any existing convention have created one? No, and I checked
three.** **Rule 15** commits the artifacts and says nothing about linking
them. **Rule 7** tells a reader which source wins when sources disagree,
but presumes the reader already has both — it is downstream of the
discovery this gap prevents. **Amendment L is the closest and is the same
shape**: it requires a consumed convention to be discoverable *through the
conventions index*, and there is no equivalent index for corrections. **Its
own known instance is still unresolved, so the pattern has produced two
instances and no mechanism.**

**A third junction I add.** **This report and the stopped attempt's report
both exist and disagree about nothing, but only one is on `main`.** After
this lands, `58a996a4…` remains unmerged and unregistered — §2b defers the
register entry deliberately — **so the record of why a v2 exists is
reachable only from a branch name.** That is the same discoverability
shape as junction two, one level up.

## 9. What this report does not claim

**No statement in this report claims to measure commit 4.** Every figure
is either **MEASURED at commit 3 or earlier** or explicitly labelled
**INTENDED**:

- A5's 8 additions / 0 modifications — **MEASURED** at commit 3;
- A5's nine-path final manifest — **INTENDED**;
- A10's two runs, A6, A7, A8, A9, A12-pre, A13 for commits 1–3 — **MEASURED**
  at commit 3;
- commit 4's stored message, the fast-forward parameters — **INTENDED**;
- A10-final, A12-final, the final scope, the final `POST_MERGE`, the push,
  the post-advance A9 and the remote read-back — **not present in any
  form**, because they belong to the post-report layer.

## 10. Stops and clarifications

### `SPECIFICATION_DEFECT`

**None blocking. No stop occurred.**

**One non-blocking, and it is about what I could verify rather than what
is wrong.** The provenance note asserts the §2b wording change is **the
only delta** from the approved `9253179c…`. **I confirmed the change is
present; I could not confirm it is the only one, because the approved
artifact was not supplied.** §2 states that limit rather than letting
"confirm the delta" read as done.

**A9's planted defect in the merged specification is not a stop** — RUN 1
found it, A10 pre-classifies it as correct behaviour, RUN 2 excludes it
for the stated reason.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

**None in this task.** No measure was retracted and none returned a
vacuous result.

**The one from the first attempt is unrepaired and lands with this
merge**, deliberately: **P1's grammar is documented as reading the
governing SENTENCE and implemented as reading the nearest LINE.** §2b
labels the one-line count sentence an accommodation, not a fix, and this
report does not treat it as one.

### `REPOSITORY_DEFECT`

**None introduced.** Nothing arriving by merge was edited; 211
pre-existing paths blob-identical; no modification occurred.

**Three pre-existing and unchanged.** The line-versus-paragraph grammar
defect; **the classification's description of a grammar the code does not
implement**, which lands saying `SENTENCE` while the code reads `LINE`;
and the enforcement gap — the workflow runs `pytest` and never invokes
`task_checker.py`. **§3 forbids touching the last of these and §9 the
first two.**

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None requiring a ruling.** The prospectivity boundary was `ce86b534…`
under the INCLUSIVE reading, named in both configs; that question was
retired for post-boundary ranges by an earlier measurement.

## 11. The specific questions the report contract asks

**Did I write a register entry? No.** **`docs/BRANCHING_POLICY.md` is
blob-identical between base and commit 3**, and no supersession entry for
`58a996a4…` was written. §2b defers it to a task authorised to modify that
file, because Rule 17 forbids an integration adding a governance
classification. **`58a996a4…` still resolves to
`58a996a46b1f446fee1517c583bf3b27a4561b74` and was not touched.**

**Does A5's one-line count sentence read as a style choice rather than a
labelled accommodation? On its own, yes — and that is the risk worth
naming.** In `specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md`
the sentence is simply a heading that happens not to wrap; **nothing at
the point of use marks it as temporary.** The label lives in §2b, ~180
lines earlier, and in this report. **A reader copying A5 as a template
will copy the accommodation and not the label** — which is exactly how a
workaround becomes a house style. **The next task removes the constraint;
the label must not outlive it, and the surest way to ensure that is for
the grammar repair to land before another specification is drafted from
this one.**

**Does `main` now read as though governance were enforced?** **It will,
and it is not.** The workflow runs `ruff` and `python -m pytest`; **there
is no occurrence of `task_checker` in it.** The accurate name for what
lands is **available governance verification, not enforced governance.**
**This merge moves the gap from "no tool" to "a tool nothing calls"**,
which is harder to notice because a tool's existence reads as reassurance.
**No claim to the contrary appears anywhere in this report.**

## 12. Ambiguous, unsatisfiable, or would have specified differently

- **The provenance note asks for a confirmation the supplied evidence
  cannot support.** "Report both digests and confirm the delta is what
  this note says it is" is satisfiable only with both artifacts. **Supply
  the approved file alongside the amended one**, and the confirmation
  becomes a one-command diff instead of a partial attestation.
- **A10's `stated 9, counted 9` prediction in §11 is now a measurement**,
  and the specification was right to demand the executor report what was
  measured rather than echo it. **The first attempt is why that sentence
  exists**, and it earned its place.
- **§2b's accommodation is correctly labelled but structurally fragile**,
  for the reason in §11 above. **I would put the label at the point of
  use** — one line inside A5 reading "one line by accommodation, see §2b;
  removed by the grammar repair" — since that is where a copyist looks.
  **I did not add it: the specification is committed as supplied.**
- **RUN 1 and RUN 2 together are a good design and I would keep them.**
  RUN 1 is what makes RUN 2's narrowing auditable rather than a choice
  that produced green, and here it did real work: **the same config
  without the subject restriction still fails**, which is the strongest
  available evidence that nothing was tuned.
- **Nothing was unsatisfiable.** No instruction conflicted with a
  repository rule or with another instruction.

## 13. What this task did not do

**It edited nothing arriving from the branch** — not the false `MEASURED`
line, not the classification, not the checker. **It added, removed and
re-worded no classification verdict.** **It wrote no register entry.**
**It did not modify `.github/workflows/ci.yml`** and claims no CI
enforcement. **It did not adjust the checker or the config to pass** —
RUN 2's subject is the single path A10 names, no property was dropped and
no declared set was emptied to obtain green. **It deleted no branch**,
including the six in the register and the stopped first attempt. **It
repaired neither the grammar defect nor the classification's description
of it.** No gate, gate status, verdict, digest or hash-pinned artifact was
modified. **No history was rewritten**, and the merge is a genuine
`--no-ff` with two parents.
