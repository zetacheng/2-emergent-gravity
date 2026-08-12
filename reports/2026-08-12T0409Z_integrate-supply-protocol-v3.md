# Task report — integrating the review supply protocol and the superseded-branch register

Specification:        `specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T0409Z_integrate-supply-protocol-v3.md`
Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`
Source branch:        `governance/supply-protocol-v3` @ `aa531aeab3a98b51b2b55b1f79f9e21c139e7dde`
Integration branch:   `governance/integrate-supply-protocol-v3`
Merge commit:         `48268e6cae0d70dd4f34f88c780fb357e81e2b8c`
Pre-report head:      `48268e6cae0d70dd4f34f88c780fb357e81e2b8c`
UTC token `{HHMM}Z`:  `0409`, fixed by commit 1; `XX` = `12`

**One merge, no conflict.** `PRE_MERGE` PASS on all five conditions
including all six pins. At the merge commit: **5 additions and 3
modifications**, the figure the specification predicted. All six arriving
paths blob-identical to the source. `DECISION_LOG.md` append-only on both
measures. All six register commits confirmed **not** ancestors of the
merged head. Eighteen rules; **six register entries, listed by name**.

**Nothing here is enforced.** §9 states that where a reader will meet it,
and this report does not claim otherwise anywhere.

---

## 1. A1 — Refs, read from the remote

```
remote refs/heads/main                            0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
refs/remotes/origin/main                          0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
remote refs/heads/governance/supply-protocol-v3   aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
refs/remotes/origin/governance/supply-protocol-v3 aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
local  refs/heads/main                            0f7961747abe2a18b436c0b1e5b928f425ea4d9a
```

**Both `main` refs resolve to the evidence base; the source branch
resolves to the pinned head. No mismatch, no STOP.** **Local `main` is
stale by design and was not repaired.**

**§1(a) re-verified rather than taken from the specification:**

```
git merge-base --is-ancestor origin/main origin/governance/supply-protocol-v3
  exit 0 — main IS an ancestor of the source
git merge-base origin/main origin/governance/supply-protocol-v3
  0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
```

**The merge-base equals `main` exactly. No stale base** — the failure mode
that stopped two earlier tasks in this line is absent, and it was measured
here, not inherited.

## 2. A2 — Merge parentage, three separately derived measurements

**Each value has its own method. None was inferred from another.**

**Measurement 1 — parent 1.** Read from the merge object's parent list:

```
method: git rev-parse 48268e6c^1
value : 3e8494a07c3305541f739ab52b6544fa267ba033
method: git cat-file commit 48268e6c — first 'parent' line
parent 3e8494a07c3305541f739ab52b6544fa267ba033
```

**Measurement 2 — parent 2.** Read from the merge object's parent list:

```
method: git rev-parse 48268e6c^2
value : aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
method: git cat-file commit 48268e6c — second 'parent' line
parent aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
```

**Measurement 3 — merge-base.** Computed from the two parents, **not read
from either**, and cross-checked from the named refs by a second route:

```
method: git merge-base <parent1> <parent2>
value : 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
method: git merge-base 0ab6369a refs/remotes/origin/governance/supply-protocol-v3
value : 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
```

All three match the specification's expectations:

    parent 1    3e8494a0…  == commit 2, the review commit
    parent 2    aa531aea…  == the pinned source head
    merge-base  0ab6369a…  == the evidence base

**The distinctness the specification insists on, verified rather than
assumed:**

```
merge-base == parent 1 ?  NO — they differ, as specified
parent 1 carries this task's own two commits above the base:
  3e8494a review: pre-execution review for the supply-protocol-v3 integration
  5d627c2 spec: integrate the review supply protocol and the superseded register
```

**This is the check that would catch a shared rationale.** A single
derivation that produced all three values could not distinguish
`merge-base == evidence base` from `merge-base == parent 1`; here they are
different objects and the measurements say so independently.

**Commit 1 is an ancestor of parent 1:**

```
git merge-base --is-ancestor 5d627c20 48268e6c^1   →  exit 0 — CONFIRMED
```

## 3. A5, §4 — How the review and the specification arrived

**Rule 18 is not in force at the evidence base — this task lands it — and
this task did not apply it.** §4's file-supply requirement is an
instruction of the integration specification, and I treated it as one.
**The circularity that stopped an earlier attempt is absent: no
specification here asks me to apply a rule that is not yet in authority.**

**The review arrived AS A FILE**, at
`…/1ef8b310-integratesupplyprotocolv3_approval_review.md`. 183 lines,
9344 bytes. Committed byte-unchanged:

```
supplied file  : fbea8b2e94b83a9899bc18721472dac52698419a6516adcb6616b44b5c5e6033
committed blob : fbea8b2e94b83a9899bc18721472dac52698419a6516adcb6616b44b5c5e6033
```

Supply-integrity checks on the file as received:

    occurrences of "REVIEW ARTIFACT"            0
    lines beginning with an attachment marker   0

**Nothing was extracted, stripped, normalised, authored or reformatted.**
**§4 names no delimiters and I searched for none.**

**Correspondence: identified by TASK NAME.** The review names
`integrate-supply-protocol-v3` at three points — line 1 (title), line 7
("**Specification reviewed:**"), and line 72 ("This review identifies the
specification by the task name `integrate-supply-protocol-v3`"). **It is
this specification, not another. No STOP.**

**The specification arrived PASTED, not as a file** — as the body of the
task message, with the review file's attachment marker fused ahead of its
title on line 0. §4 requires me to report how each arrived, and that is
the answer for each. **`specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md`
therefore carries my transcription**, and no digest can attest that it
matches the sender's text, because no sender's file exists to compare.
**This is the same asymmetry the source branch's report recorded**, and
the Rule 18 being landed here addresses it with a SHOULD rather than a
requirement.

## 4. A3 — `PRE_MERGE`, verbatim

Run before the merge. The `other_registered_worktrees` list is elided
here for length; it enumerated 36 worktrees and no check depends on it.

```json
{
  "checks": [
    {
      "condition": "worktree_clean",
      "entries": [],
      "status": "PASS"
    },
    {
      "attachment": "governance/integrate-supply-protocol-v3",
      "condition": "worktree_matches_declared_target",
      "expected_worktree_head": "3e8494a07c3305541f739ab52b6544fa267ba033",
      "status": "PASS",
      "worktree_head": "3e8494a07c3305541f739ab52b6544fa267ba033"
    },
    {
      "actual": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
      "condition": "merge_base",
      "expected": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
      "status": "PASS"
    },
    {
      "condition": "scope",
      "evidence": {
        "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
        "failures": [],
        "head": "3e8494a07c3305541f739ab52b6544fa267ba033",
        "mode": "exact",
        "observed_operations": [
          {
            "operation": "add",
            "path": "reviews/chatgpt/2026-08-12T0409Z_integrate-supply-protocol-v3.md"
          },
          {
            "operation": "add",
            "path": "specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md"
          }
        ],
        "overall": "PASS",
        "tool": "scope_checker"
      },
      "status": "PASS"
    },
    {
      "condition": "pinned_artifacts",
      "evidence": [
        {
          "actual": "928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d",
          "expected": "928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d",
          "path": "CONVENTIONS.md",
          "status": "PASS"
        },
        {
          "actual": "dc5d5361dd0ee49a4be6603f8d19b46f168ddf65663e24727caa26181f5dd2ca",
          "expected": "dc5d5361dd0ee49a4be6603f8d19b46f168ddf65663e24727caa26181f5dd2ca",
          "path": "DECISION_LOG.md",
          "status": "PASS"
        },
        {
          "actual": "9d99f8365f798cfc27b5a2612f21130b4534cd32ea4778be4be97f15b7daa3f0",
          "expected": "9d99f8365f798cfc27b5a2612f21130b4534cd32ea4778be4be97f15b7daa3f0",
          "path": "docs/BRANCHING_POLICY.md",
          "status": "PASS"
        },
        {
          "actual": "6eec114a29c5d1749de73eca159c7e555b8e2ba778b6725c7bc650429fa86355",
          "expected": "6eec114a29c5d1749de73eca159c7e555b8e2ba778b6725c7bc650429fa86355",
          "path": "reports/2026-08-12T0131Z_supply-protocol-v3.md",
          "status": "PASS"
        },
        {
          "actual": "206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719",
          "expected": "206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719",
          "path": "reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md",
          "status": "PASS"
        },
        {
          "actual": "7e7a2419b1e6933ee993dd630fe56f7b0d2ff41fa741a0381f7f979c47d385c8",
          "expected": "7e7a2419b1e6933ee993dd630fe56f7b0d2ff41fa741a0381f7f979c47d385c8",
          "path": "specs/2026-08-12T0131Z_supply-protocol-v3.md",
          "status": "PASS"
        }
      ],
      "status": "PASS"
    }
  ],
  "mode": "PRE_MERGE",
  "overall": "PASS",
  "tool": "merge_guard"
}
EXIT STATUS: 0
```

**`PRE_MERGE` pins are evaluated at the REVIEWED BRANCH HEAD**
(`merge_guard.py:76`, `pins = _pins(repo, branch_head, config)`), so the
six pinned values above are the source branch's, not the base's. **This is
a known property of the tool and the pins were aimed accordingly.**

**One tool-contract correction, reported under `OBSERVATION_METHOD_ERROR`
in §12.** My first `PRE_MERGE` config supplied A6's **Git blob ids** as
`pinned_artifacts`. The guard returned
`{"error": "each pin needs a 64-character sha256", "overall":
"TOOL_ERROR"}`, exit 3. `core.py:218–224` requires a 64-character SHA-256
under the key `sha256`; a 40-character blob id is rejected. **A6 states
its own comparison method — "These are Git blob ids… Compare with
`git rev-parse`" — so the two checks are separate, not contradictory.**
I did both: the guard carries SHA-256 content digests, and A6's blob-id
comparison is §5 below. **The guard is read-only and nothing was
modified.**

### The merge

```
Merge made by the 'ort' strategy.
 CONVENTIONS.md                                     |   32 +
 DECISION_LOG.md                                    |  142 +++
 docs/BRANCHING_POLICY.md                           |  127 +++
 reports/2026-08-12T0131Z_supply-protocol-v3.md     | 1201 ++++++++++++++++++++
 .../chatgpt/2026-08-12T0131Z_supply-protocol-v3.md |  181 +++
 specs/2026-08-12T0131Z_supply-protocol-v3.md       |  626 ++++++++++
 6 files changed, 2309 insertions(+)
MERGE EXIT STATUS: 0

unmerged paths: 0
worktree dirty: 0
```

**No conflict.** `--no-ff` of the **pinned remote ref**
`refs/remotes/origin/governance/supply-protocol-v3`. **No fast-forward,
no squash, no rebase.** 2309 insertions, **0 deletions.**

## 5. A6 — Arriving artifacts intact, all six

Compared with `git rev-parse <rev>:<path>`, as A6 directs — **Git blob
ids, not content digests** — at the merged head, at the source branch, and
against the specification's pinned values:

```
  CONVENTIONS.md                                           merged=b3c96300a1f3 source=b3c96300a1f3 pinned=b3c96300a1f3  PASS
  DECISION_LOG.md                                          merged=d9dd2bf3a8cc source=d9dd2bf3a8cc pinned=d9dd2bf3a8cc  PASS
  docs/BRANCHING_POLICY.md                                 merged=3f0f35d4da44 source=3f0f35d4da44 pinned=3f0f35d4da44  PASS
  reports/2026-08-12T0131Z_supply-protocol-v3.md           merged=f1250e759eac source=f1250e759eac pinned=f1250e759eac  PASS
  reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md   merged=b0d9afd17f00 source=b0d9afd17f00 pinned=b0d9afd17f00  PASS
  specs/2026-08-12T0131Z_supply-protocol-v3.md             merged=ac91efeb012c source=ac91efeb012c pinned=ac91efeb012c  PASS
```

**All six identical on all three readings. Nothing arriving by merge was
edited.**

## 6. A7 — Protected paths, path by path

### The three authorised modifications, excluded from the protected set deliberately

**Stated explicitly because the report contract requires it.**
`CONVENTIONS.md`, `DECISION_LOG.md` and `docs/BRANCHING_POLICY.md` **are
the paths this integration exists to change.** They are **not** in the
protected set; A6 pins their post-merge blobs instead. **Carrying them in
the protected set — as recent specifications' lists do — would have made
A7 unsatisfiable**, since the task's purpose is to change them. The
specification says so and I confirm the exclusion was deliberate, not an
omission I exploited:

```
    CONVENTIONS.md               base=0db56c39d44e merged=b3c96300a1f3  CHANGED, as authorised
    DECISION_LOG.md              base=04539f26a6bc merged=d9dd2bf3a8cc  CHANGED, as authorised
    docs/BRANCHING_POLICY.md     base=3fad8856b0d6 merged=3f0f35d4da44  CHANGED, as authorised
```

### Named protected files

```
  GATES.md             identical=True  blob=849a4fbfe62d
  AGENTS.md            identical=True  blob=5e60b5fcd6e9
  pyproject.toml       identical=True  blob=9fc6fdd196dd
```

### Every base path under the six protected prefixes

**Compared path by path, not as tree objects:**

```
  scripts/       pre-existing checked=59   identical=59   differing=0  base-absent gained=[]
  results/       pre-existing checked=69   identical=69   differing=0  base-absent gained=[]
  tests/         pre-existing checked=19   identical=19   differing=0  base-absent gained=[]
  derivations/   pre-existing checked=34   identical=34   differing=0  base-absent gained=[]
  docs/          pre-existing checked=6    identical=6    differing=0  base-absent gained=[]
  reviews/       pre-existing checked=20   identical=20   differing=0  base-absent gained=[
                   'reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md',
                   'reviews/chatgpt/2026-08-12T0409Z_integrate-supply-protocol-v3.md']
  TOTAL pre-existing paths checked under the six prefixes: 207
  differing: NONE
```

**207 pre-existing paths checked individually; none differs.** `docs/`
holds 7 pre-existing paths, of which 6 are protected and
`docs/BRANCHING_POLICY.md` is the authorised exception. `reviews/` gains
two base-absent authorised paths — the arriving branch review and this
task's own. `specs/` and `reports/` likewise gain authorised additions,
enumerated in §7.

### `tests/`

```
  all paths under tests/       base=19  merged=19  same set=True
  test_*.py files              base=17  merged=17
  any modified?                NONE
```

**A7 states "17 files before, 17 after". That is exact for
`test_*.py` files, and I confirm it.** The directory holds **19** paths in
total, the other two being `tests/README.md` and `tests/__init__.py`.
**Both numbers are correct under their own reading and neither indicates a
change** — the set is identical and nothing under `tests/` was modified.
**I report both so the figure cannot be misread as a discrepancy**; the
source branch touches no path under `tests/` at all.

## 7. A4 — Scope, at both heads

**At the merge commit** — the figure the specification predicted:

```
overall: PASS
head: 48268e6cae0d70dd4f34f88c780fb357e81e2b8c
failures: []
additions: 5  modifications: 3
EXIT: 0
```

The eight operations, enumerated:

```
  additions (5):
    A  reports/2026-08-12T0131Z_supply-protocol-v3.md
    A  reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md
    A  reviews/chatgpt/2026-08-12T0409Z_integrate-supply-protocol-v3.md
    A  specs/2026-08-12T0131Z_supply-protocol-v3.md
    A  specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md
  modifications (3):
    M  CONVENTIONS.md
    M  DECISION_LOG.md
    M  docs/BRANCHING_POLICY.md
  deletions: NONE
```

**Which head each measurement was taken at, as A4 requires:**

    5 additions + 3 modifications   at 48268e6c…, the MERGE COMMIT,
                                    before this report existed
    6 additions + 3 modifications   at the FINAL HEAD, once this report
                                    is committed — nine paths

**Both are correct at their own head.** Six paths arrive from the branch
(three additions and all three modifications); three are authored here
(this specification, its review, this report). **The final measurement is
post-report evidence** — it cannot be taken from inside the report it
counts.

**Intended final manifest:**

```json
{
  "mode": "exact",
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "head": "<final head>",
  "required": [
    {"operation": "add", "path": "reports/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "add", "path": "reports/2026-08-12T0409Z_integrate-supply-protocol-v3.md"},
    {"operation": "add", "path": "reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "add", "path": "reviews/chatgpt/2026-08-12T0409Z_integrate-supply-protocol-v3.md"},
    {"operation": "add", "path": "specs/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "add", "path": "specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md"},
    {"operation": "modify", "path": "CONVENTIONS.md"},
    {"operation": "modify", "path": "DECISION_LOG.md"},
    {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"}
  ],
  "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
}
```

**Intended final `POST_MERGE` parameters**, with A3's two distinct SHAs in
their two distinct roles:

    mode                   POST_MERGE
    merge_commit           48268e6cae0d70dd4f34f88c780fb357e81e2b8c
    expected_parent_1      3e8494a07c3305541f739ab52b6544fa267ba033
    expected_parent_2      aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
    expected_remote_sha    <the final report-commit head>
    scope_manifest         the final manifest above

**The guard represents both roles separately** — `merge_commit` for the
object under verification, `expected_remote_sha` for remote agreement — so
A3's stop condition does not apply. **If it could not, A3 required a STOP;
it can, and the final run is post-report evidence.**

## 8. A8 — `DECISION_LOG.md` append-only, two measures reported separately

**Measure 1 — deleted lines, base to merged head:**

```
142	0	DECISION_LOG.md
  (added removed path)
```

**142 added, 0 deleted.**

**Measure 2 — exact byte prefix:**

```
  base bytes  : 82337   (specification expects 82337)
  merged bytes: 89541   (specification expects 89541)
  added bytes : 7204
  base is an EXACT BYTE PREFIX of merged: True
```

**Both measures pass, and they are different properties.** A zero-deletion
count alone would not establish the prefix relation — a rewritten line
paired with an equal-count insertion satisfies the line measure and fails
the byte measure. **Both byte lengths match the specification's
expectations exactly.**

## 9. A9 — Superseded branches not merged, all six

`git merge-base --is-ancestor <commit> 48268e6c`, run once per commit.
**Exit 1 means not an ancestor, which is the passing outcome:**

```
  52f65117  exit=1  NOT an ancestor — PASS    fix/pi-decisions-and-deferred
  ebd531ab  exit=1  NOT an ancestor — PASS    fix/pi-decisions-v2
  40168469  exit=1  NOT an ancestor — PASS    governance/supply-protocol-v2
  7146a093  exit=1  NOT an ancestor — PASS    governance/supply-protocol-and-superseded
  10c260b9  exit=1  NOT an ancestor — PASS    review/role-model-and-executors
  d64cd912  exit=1  NOT an ancestor — PASS    gate/p2-land-diquark-line
```

**Six separate exit statuses, all six checked.** **The two branches §3
names are not a sufficient check and were not treated as one** — the
register this merge lands governs every branch in it, and a criterion
covering two of six would be a proxy for the property rather than the
property. **This is the first occasion on which the register governs, and
it governs the task that lands it.**

**No branch in the register was merged, read from, cherry-picked or
deleted.** Their contents were not used as task input; only Git graph
metadata — ref resolution and ancestry — was inspected, which A9 requires.
**The Reviewer's non-blocking observation names exactly this distinction**
and I confirm it applies: "do not read from" is broader than the
operations A9 needs, and "do not read branch contents" is the precise
reading. **No branch's content was consulted.**

The six tips read back after the task are post-report evidence.

## 10. A10, A11 — No gate changed; rule and register counts

### A10

```
  GATES.md blob at base   : 849a4fbfe62d6478f092a84b0175357a74bbbb06
  GATES.md blob at merged : 849a4fbfe62d6478f092a84b0175357a74bbbb06
  pinned                  : 849a4fbfe62d6478f092a84b0175357a74bbbb06
  '^## P2-' count base    : 14
  '^## P2-' count merged  : 14
  P2-PHASE-01 at merged head:  Status: PROPOSED
```

**Blob-identical at the pinned value, 14 gate sections either side,
`P2-PHASE-01` still `PROPOSED`.** No gate status changed and no gate was
registered.

### A11 — eighteen rules

```
  '^### N.' numbered headings, base   : 17
  '^### N.' numbered headings, merged : 18
  the eighteenth heading: ### 18. Review supply protocol
```

### A11 — six register entries, with the counting method and the names

**Method, as A11 requires — entry records, not vocabulary hits and not
headings.** Locate `## Superseded branches`; take the section up to the
next `## ` heading; take the **first** fenced block inside it, which is
the register; within that block, an **entry record** is a line beginning
at column 0 with a branch path, and its commit is read from the same line
or the next. Measured:

```
  section lines 104..230; register fence at section-relative 25..90; block lines 64
  ENTRY RECORD COUNT: 6
    fix/pi-decisions-and-deferred                @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
    fix/pi-decisions-v2                          @ ebd531ab568aaffabd86a4a94d925a711e62aa36
    governance/supply-protocol-v2                @ 40168469608618aef6812735ff70e32de0e3cbc8
    governance/supply-protocol-and-superseded    @ 7146a093c65788a57d63a747b71d86edb91eddc6
    review/role-model-and-executors              @ 10c260b96882ac12610f78840aeeabd07be2d7cb
    gate/p2-land-diquark-line                    @ d64cd912ca9ff78a85787f0e54f345f474cdb192
```

**Six entries, and the six names and commits are exactly the expected
set** — so the count is not concealing a wrong target set, which is what
A11's name requirement exists to prevent. **The whole object was read, not
a truncated diff**; the specification's `RETRACTED` note records that a
truncation at 80 lines removed the sixth entry and produced a count of
five, and I mention it because the method that failed there is the method
this criterion forbids.

**No entry was added, re-worded, or given a deletion outcome.** Rule 17.
The register arrived by merge exactly as reviewed.

## 11. A12-pre, A13, and the two worktrees

### A12-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`. Python 3.11.15;
`python -m pytest` = **pytest 9.1.1**, the mandated invocation; the
`pytest` on `PATH` is a different version and was not used.

```
--- tests/test_repository_structure.py ---   4 passed   EXIT STATUS: 0
--- tests/test_si1_governance.py ---        14 passed   EXIT STATUS: 0
--- tests/test_gate_anchors.py ---          18 passed, 2 deselected   EXIT STATUS: 0
--- tests/test_governance_tools.py ---       8 passed   EXIT STATUS: 0
```

**All four exit 0.** The 2 deselected are `@pytest.mark.slow`, excluded by
`pyproject.toml`'s `addopts = "-m 'not slow'"` — pre-existing and
unchanged. **These four passing says nothing about Rule 18 or the
register**; §12's `REPOSITORY_DEFECT` entry and §13 say what they do and
do not reach.

### A13 — commit-message hygiene, per commit including the merge

**Method.** The proposed message was written to a file and scanned before
committing; the stored message was read back from the commit object and
scanned again. Pattern, case-insensitive:
`co-authored-by|claude-session|generated with|noreply@|https?://|opus|sonnet|anthropic`.

    commit 1 (5d627c20)  proposed: none found   stored: none found
                         trailers suppressed: NONE — none was produced
    commit 2 (3e8494a0)  proposed: none found   stored: none found
                         trailers suppressed: NONE — none was produced
    commit 3 (48268e6c)  proposed: none found   stored: none found
                         trailers suppressed: NONE — none was produced
                         — the MERGE commit, scanned like any other
    commit 4             proposed: none found at authoring time
                         trailers suppressed: NONE — none was produced

**No trailer was suppressed on any commit, because none appeared.** No
`Co-Authored-By`, no session identifier or URL, no tool attribution.
Commits used `git -c commit.gpgsign=false commit`/`merge -F <file>`; the
repository carries no `commit.template` and no `core.hooksPath`. **No
persistent user or global configuration was changed.**

**One distinction reported rather than glossed.** Scanning the *raw commit
object* matches `author Claude <noreply@anthropic.com>`. That is the
author/committer identity field, **not a message trailer** — A13 governs
the message, and every message scans clean. That identity is the
repository's standing one, on 204 of `main`'s commits including the
evidence base. Nothing was introduced here.

Commit 1–3 SHAs and their messages:

    5d627c2017c428fe1ba5414b44e0cf57c29bf3b0
      spec: integrate the review supply protocol and the superseded register
    3e8494a07c3305541f739ab52b6544fa267ba033
      review: pre-execution review for the supply-protocol-v3 integration
    48268e6cae0d70dd4f34f88c780fb357e81e2b8c
      merge: land the review supply protocol and the superseded-branch register
      (full stored body read back from the object, quoted below)

```
merge: land the review supply protocol and the superseded-branch register

Merges governance/supply-protocol-v3 at aa531aeab3a98b51b2b55b1f79f9e21c139e7dde.

CONVENTIONS.md gains Rule 18: a pre-execution review is supplied as a file
and committed byte-unchanged, with no delimiters, no extraction and no
normalisation, plus a correspondence check and its STOP conditions. Rules
1-17 are unchanged and unrenumbered.

docs/BRANCHING_POLICY.md gains SUPERSEDED as an attribute orthogonal to the
Stage-1 deletion states, with a six-entry register. The deletion state
machine and its closed count identity are byte-identical.

DECISION_LOG.md records both additions as prospective. No gate, verdict or
hash-pinned artifact changes.
```

**Intended report commit message**, inspected at authoring time; its scan
under the same pattern found none, so there is no trailer to suppress:

```
docs: integration report for the supply protocol and superseded register

Records A1-A13 raw output, the PRE_MERGE JSON, the merge commit's two
parents and merge-base as three separately derived values, A6's blob
comparison for all six arriving paths, A7's 207-path protected comparison,
A8's two append-only measures, A9's six ancestry exit statuses, and A11's
six register entries counted by entry record and listed by name.

Rule 18 and the superseded register are recorded, not enforced. No test
checks either.
```

### The two worktrees, stated separately

    MERGE worktree  <scratch>/int13
                    branch governance/integrate-supply-protocol-v3
                    at the merge commit, 0 dirty
    MAIN worktree   /home/user/2-emergent-gravity
                    branch gate/p2-grassmann-crossing-sign @ cf4c789
                    0 dirty — NOT on main, NOT touched by this task

**The main worktree was not used for the merge and was not modified.** Its
attachment to an unrelated gate branch is pre-existing. **All merge work
happened in the dedicated worktree**, and `PRE_MERGE`'s
`worktree_matches_declared_target` check confirmed the worktree it
inspected was the right one, attached to
`governance/integrate-supply-protocol-v3`.

## 12. Rule 16 assessment, and whether anything reads as enforced

**Rule 16 is operative: this integration brings previously separate
governance artifacts onto one authoritative branch**, so the assessment is
owed against the merged state, not the branch state.

**§7's candidate junction is confirmed, and I adopt it.** Named precisely:

    CONVENTIONS.md Rule 18 (eighteen numbered rules)
      + docs/BRANCHING_POLICY.md's six-entry superseded register
      + DECISION_LOG.md's entry recording both
      + four validators green at the merged head
    ------------------------------------------------------------------
    available inference:  review supply is now VERIFIED, and superseded
                          branches CANNOT be integrated

**Neither is mechanically true, and the report contract asks the question
directly, so here is the direct answer: no, the merged state does not make
any rule enforced, and nothing in this report should be read as saying it
does.**

- **No test checks Rule 18.** The four validators at the merged head
  assert file existence, gate-ID cross-references, numerical anchors and
  the governance tools' own evaluator logic. **None reads Rule 18. None
  reads the register.** Rule 18 could have arrived worded differently, or
  the register with a wrong entry, and all four would still exit 0.
- **Nothing but a reader stops a superseded branch from being merged.**
  This task's A9 is the strongest form the check currently takes, and it
  is **a hand-run criterion in one specification**, not a gate the
  repository applies. **The next integration will consult the register
  only if its specification tells it to.**
- **The register constrains what a person may do, not what the repository
  will accept.**

**Two additions of my own that the candidate does not cover.**

- **The four green validators are the most misleading element of the
  merged state**, because they sit next to the new rules and are reported
  in the same breath. **Their passing is evidence that nothing existing
  broke — not evidence that anything new works.** That is why §11 states
  what they do not reach immediately after stating that they passed.
- **The register now contains two branches whose supersession this very
  merge is what establishes** — `governance/supply-protocol-v2` and
  `governance/supply-protocol-and-superseded`, both superseded by the
  branch being merged. **A reader could infer the register is
  self-maintaining.** It is not: each entry was written by hand in the
  superseding task, and **nothing detects a superseded branch that no one
  entered.** The register's completeness rests on the enumeration recorded
  in the source branch's report, not on any mechanism.

## 13. Stops and clarifications

**One primary category per stop; secondary findings separate. Included
even where there were none.**

### `SPECIFICATION_DEFECT`

**None blocking. No stop occurred**, and no instruction was inconsistent
with a repository rule or with another instruction — so §8's
stop-and-report clause was not triggered.

**Two secondary findings, both non-blocking.**

**A7's `tests/` figure is exact under one reading and not the other, and
both readings are true of an unchanged directory.** "17 files before, 17
after" is exact for `test_*.py`; the directory holds 19 paths counting
`README.md` and `__init__.py`. **The property A7 asserts — gains nothing,
loses nothing, none modified — holds on both counts** (§6), so this is a
reporting ambiguity rather than a defect, and I record both numbers so a
later reader does not read 19 as a change.

**The Reviewer's two non-blocking observations, both confirmed.** (i) §0's
"ninth attempt" and "five preceding failure modes" is historical prose no
criterion uses, and this line has carried differing tallies; **the
governance content is pinned by object identity and A6, so nothing
depends on it.** (ii) "do not read from" a register branch is broader than
what A9 needs — ref resolution and ancestry are Git graph metadata, not
branch content. **I confirm I consumed no branch content** (§9), and agree
"do not read branch contents" is the precise wording for reuse.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Rule 13 carrying two conflicting
orders remains a known open item, untouched here. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

**One, caught by the tool before anything rested on it.** **My first
`PRE_MERGE` config passed A6's Git blob ids as `pinned_artifacts`.** The
guard returned `TOOL_ERROR`, exit 3: `"each pin needs a 64-character
sha256"`. `core.py:218–224` validates a 64-character hex `sha256` key and
rejects a 40-character blob id. **A6 names its own method — `git
rev-parse` on blob ids — and the guard's pin format is content SHA-256;
these are two different checks of the same six paths, and I ran both**
(§4, §5) rather than substituting one for the other. **Nothing was
modified**; the guard is read-only and the error was in my input. **Read
the tool's own source before changing the input**, which is what located
the contract.

### `REPOSITORY_DEFECT`

**None introduced.** Everything arriving by merge is byte-identical to the
reviewed source; nothing was edited by hand.

**One pre-existing gap, restated because this merge makes it more visible
rather than less: no test asserts anything about `CONVENTIONS.md`'s rule
count or `docs/BRANCHING_POLICY.md`'s structure.** Both files gained
substantial governance content here and both remain existence-checked
only. **This is the known open item §2 and §7 name, and this task is
forbidden to close it** — no test was added.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None.** The register arrived with six entries whose membership was
established on the source branch and verified here by name and commit. **I
added no entry, re-characterised none, and assigned no branch a deletion
outcome.** No branch sits in the suggestive-but-unestablished category.

## 14. Ambiguous, unsatisfiable, or would have specified differently

- **A6's pinned values and the merge guard's pin format are different
  kinds of identifier**, and a reader could reasonably try A6's values in
  the guard, as I did. **A future specification could say which identifier
  each check takes** — A6 already says "These are Git blob ids, not
  content SHA-256 digests", which is what made the resolution immediate;
  a matching note that the guard's `pinned_artifacts` takes SHA-256 would
  have prevented the round trip entirely.
- **A7's `tests/` count would be unambiguous as "17 `test_*.py` files"**,
  since the directory holds 19 paths. Flagged above.
- **A4's two figures are handled well and I would keep the pattern.**
  Stating both the merge-commit count and the final count, and requiring
  the report to say which head each was taken at, removes the temptation
  to report one number and let a reader assume it applies everywhere.
- **A2's "derive the three values independently" is the strongest form of
  this criterion I have executed**, and its value is concrete here: the
  merge-base and parent 1 are genuinely different objects, so a single
  shared derivation would have been detectable. **Keep it.**
- **Nothing was unsatisfiable.** A7 would have been, had the three
  authorised modifications been carried in the protected set; the
  specification anticipated that and excluded them, and §6 confirms the
  exclusion was deliberate.

## 15. What this integration did not do

**It enforces nothing.** No test checks Rule 18 or the register; the
register constrains people, not the repository. **It settles no science** —
no gate, coefficient, channel or verdict; `P2-PHASE-01` remains
`PROPOSED` and `GATES.md` is blob-identical. **It does not reach tasks
already in flight**: Rule 18 is prospective from this merge. **It assigns
no branch a status it did not already carry** — no seventh register entry,
no re-characterisation, no deletion outcome. **No branch in the register
was merged, read from, cherry-picked or deleted**, including the two that
are this task's own predecessors. **Nothing arriving by merge was
edited**, and neither `CONVENTIONS.md` nor `docs/BRANCHING_POLICY.md` was
touched by hand. No fast-forward, no squash, no rebase, no force-push, no
history rewrite, no PR. **No test was added.** `AGENTS.md`,
`pyproject.toml` and all 207 checked pre-existing protected paths are
unchanged.
