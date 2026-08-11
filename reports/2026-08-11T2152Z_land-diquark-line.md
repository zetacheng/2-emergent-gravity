# Report — land the diquark line: **STOPPED BEFORE MERGE 1**

Specification: `specs/2026-08-11T2152Z_land-diquark-line.md`
Specification sha256:
`66d938e6f6c31d35d73de2cfee0469cc7da5e105efc26b632ff9e4dabcecf53d`
Pre-execution review: `reviews/chatgpt/2026-08-11T2152Z_land-diquark-line.md`
Evidence base: `57c5a6eb1de11bb7aaf27b779054070ee6870c29`
Branch: `gate/p2-land-diquark-line`
Classification: MATERIAL.

**Outcome: STOP. Neither merge was performed. `main` was not moved.**

---

## 0. The stop, stated first

**A3's mandated `PRE_MERGE` guard before merge 1 returned `overall: FAIL`,
exit 2, on the `merge_base` check:**

    condition   merge_base
    expected    57c5a6eb1de11bb7aaf27b779054070ee6870c29
    actual      8701a97a6bb58550d4300f75c10638b057335731
    status      FAIL

**Both source branches were cut from `8701a97a…`, which is `main`'s
previous head.** `main` has since advanced to `57c5a6eb…` through the
chirality-census work. So the evidence base is **not an ancestor of either
branch**, and the merge-base of each branch with it is their common
ancestor `8701a97a…`.

**A2 requires `merge-base = 57c5a6eb…` for both merges**, and §6's A2
gives the reason: *"Both merge-bases are the original base, because the
two source branches are siblings."* **The branches are indeed siblings of
each other — their shared merge-base is `8701a97a…`. What does not follow
is that either branch's merge-base with the current `main` is the current
`main`.** That inference holds only while `main` has not advanced past the
point the branches were cut from, and it has.

**§10's pre-issue record states `CONFIRMED both branches share the
merge-base 57c5a6eb…`. That is not reproducible.** They share the
merge-base `8701a97a…`. The second half of the same line — *"so neither is
an ancestor of the other"* — is true and reproduces.

**This is a narrow defect. Everything else in the specification
reproduces**, and §4 records exactly what, so a re-issue should be cheap.
In particular both merges are **conflict-free** and the arriving content
is intact.

**Why I stopped rather than proceeding.** Four independent grounds, any one
sufficient:

- **A3 mandates the guard and the guard failed.** Exit 2 is a governance
  failure, not a tool error.
- **A2 is an acceptance criterion and is not satisfiable as written** (§3
  proves this rather than asserting it).
- **§8:** *"If any instruction here is inconsistent with a repository rule
  or with another instruction, stop and report; do not decide which
  prevails."* A2's assertion is inconsistent with the repository's object
  graph.
- **The pre-execution review's own STOP list** names *"any pinned ref or
  blob fails verification"* and *"either merge-base"* among the conditions
  on which execution should stop.

**What I did not do.** I did not merge; did not move any `main` ref; did
not rebase either branch; did not adjust the guard configuration to make
it pass; did not write the addendum; and did not report A2 as satisfied.
**Making the guard pass would have required setting `reviewed_base` to
`8701a97a…`, a construction the specification does not describe** — and it
would then contradict A4, whose manifest `base` is `57c5a6eb…`. That is
Amendment K's trigger exactly: resolving an apparent inconsistency by a
construction the specification does not describe is a stop and a request
for authorization, not a resolution.

---

## 1. A1 — refs, all verified, all matching

    remote refs/heads/main                     57c5a6eb1de11bb7aaf27b779054070ee6870c29
    refs/remotes/origin/main                   57c5a6eb1de11bb7aaf27b779054070ee6870c29
    branch 1  gate/p2-diquark-adjudication     3767973bf57c52f4dd2be1fddcf62916ec409c72
    branch 2  gate/p2-diquark-both-eta         bc1e5c743aada004c52dc7ab7ce2af61de439955
    local main (stale by design)               0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**A1 passes.** All three pinned refs resolve exactly as specified. Local
`main` is stale by design and was neither consulted nor repaired. **The
stop is not a ref mismatch** — the refs are right; the relationship
between them is not what the specification states.

---

## 2. The object graph, measured

    merge-base(57c5a6eb, 3767973b)   =  8701a97a6bb58550d4300f75c10638b057335731
    merge-base(57c5a6eb, bc1e5c74)   =  8701a97a6bb58550d4300f75c10638b057335731
    merge-base(3767973b, bc1e5c74)   =  8701a97a6bb58550d4300f75c10638b057335731

    is 57c5a6eb an ancestor of branch 1?   NO
    is 57c5a6eb an ancestor of branch 2?   NO
    is 8701a97a an ancestor of branch 1?   yes
    is 8701a97a an ancestor of branch 2?   yes
    is 8701a97a an ancestor of 57c5a6eb?   yes

**Branch 1**, five commits, all from `8701a97a`:

    79fae72  spec: adjudicate the diquark decomposition discrepancy layer by layer
    a370725  review: commit the pre-execution review for the diquark adjudication
    ebac158  adjudicate: locate the first divergence between the two decompositions
    03110a9  compute: the layer-by-layer adjudication, script results and tests
    3767973  docs: report the diquark decomposition adjudication

**Branch 2**, five commits, all from `8701a97a`:

    fcde56d  spec: diquark channel character carrying both eta signs
    757a0b6  review: commit the pre-execution review for the diquark both-eta derivation
    941aa78  derive: diquark channel character carrying both eta signs
    fd02a2e  compute: the diquark both-eta particle-particle rearrangement
    bc1e5c7  docs: report the diquark both-eta channel-character derivation

**`main` since `8701a97a`**, nine commits, none of them on either branch:

    544e5ea  spec: the chirality census, why S P and T vanish in both channels
    87ebc44  review: commit the pre-execution review for the chirality census
    9c9fd7f  derive: the chirality census, with the Step D predictions recorded first
    b9a402b  compute: the chirality census, script results and tests
    e4bea1c  docs: report the chirality census
    0534be2  spec: integrate the chirality census
    8ab819e  review: commit the pre-execution review for the chirality census integration
    3d3493a  merge: integrate the chirality census (reviewed; pinned e4bea1c)
    57c5a6e  docs: report the integration of the chirality census

**This is the ordinary shape of two sibling branches after `main` has
advanced. It is not a defect in either branch**, and it does not make
either branch stale in any sense that matters to the merge — §4 shows the
merge is clean.

---

## 3. Why A2 is not satisfiable as written

Not asserted; argued from what the criterion fixes.

    A2 requires   merge-base(parent 1, parent 2) = 57c5a6eb, for BOTH merges

    parent 1 of merge 1 must be commit 2 (A2 states it, and §5's order
      forces it) — and commit 2 descends from 57c5a6eb
    parent 2 must be the pinned branch head (§8: "merge the pinned remote
      refs") — and it does NOT descend from 57c5a6eb

    therefore  merge-base(parent 1, parent 2) is their common ancestor,
               which is 8701a97a, necessarily

The only two ways to change that value are both prohibited:

- **rebase a source branch onto `57c5a6eb`** — §8: *"no rebase"*;
- **merge something other than the pinned refs** — §8: *"Merge the pinned
  remote refs"*, and A6/A7 pin the arriving blobs.

**So A2 cannot be met by any action this specification permits.** The
criterion is not merely unverified; it is unsatisfiable.

**The corrected values, offered for the re-issue:**

    merge 1   parent 1 = commit 2       parent 2 = 3767973b   merge-base = 8701a97a
    merge 2   parent 1 = merge 1        parent 2 = bc1e5c74   merge-base = 8701a97a

and §6 A2's rationale would read: *both merge-bases are `8701a97a…`, the
commit both source branches were cut from, because `main` has since
advanced past it.*

---

## 4. What does reproduce — everything else I could check without merging

**Both merges are conflict-free**, established by a sequential dry run.

    merge 1   git merge-tree --write-tree HEAD 3767973b
              predicted tree  4d98d158e7cbcb2343a508a962eba55617e56e3d
              conflict output (none)

    merge 2   simulated against merge 1's tree
              predicted tree  c3225897b87b7e457eebedd505b63a90616ba3f2
              conflict output (none)

**Method, stated because it required care.** `git merge-tree` takes
commits, so sequencing the second dry run needed a commit object for the
first result: one was created with `git commit-tree` and left
**unreferenced**. That writes objects to the store and **moves no ref,
creates no branch, and modifies no worktree** — verified afterwards, §6.
§10's own method is a *"sequential dry-run merge"*, so the sequence is the
author's own procedure, performed here read-only.

**Predicted combined base-to-head at the merge-2 tree:**

    16 additions, 0 modifications, 0 deletions

    derivations/P2-PHASE-01_diquark_adjudication.md
    derivations/P2-PHASE-01_diquark_both_eta.md
    reports/2026-08-10T0245Z_diquark-both-eta.md
    reports/2026-08-10T1112Z_diquark-adjudication.md
    results/P2-PHASE-01/diquark-adjudication/adjudication.json
    results/P2-PHASE-01/diquark-both-eta/diquark.json
    reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md
    reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md
    reviews/chatgpt/2026-08-11T2152Z_land-diquark-line.md
    scripts/p2_diquark_adjudication.py
    scripts/p2_diquark_both_eta.py
    specs/2026-08-10T0245Z_diquark-both-eta.md
    specs/2026-08-10T1112Z_diquark-adjudication.md
    specs/2026-08-11T2152Z_land-diquark-line.md
    tests/test_p2_diquark_adjudication.py
    tests/test_p2_diquark_both_eta.py

**Fourteen arrive from the two branches** and two are this task's already
committed artifacts; the addendum and the report would bring the total to
**18 additions and 0 modifications**, matching A4's manifest exactly.
**A4's arithmetic is correct** and **no deletions appear** — which is worth
saying, because the raw `git diff base..branch1` does show `D` entries for
the chirality-census files, purely because branch 1 predates them. A
three-way merge from `8701a97a` keeps additions made on either side, and
the predicted tree confirms it: **zero deletions.**

**A6 — branch 1's seven arriving blobs**, `git rev-parse <rev>:<path>` at
`3767973b`, **all match:**

    derivations/P2-PHASE-01_diquark_adjudication.md              7983d4ba…  MATCH
    reports/2026-08-10T1112Z_diquark-adjudication.md             48bc2965…  MATCH
    results/P2-PHASE-01/diquark-adjudication/adjudication.json   77805645…  MATCH
    reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md     2c7806f9…  MATCH
    scripts/p2_diquark_adjudication.py                           529d5ef0…  MATCH
    specs/2026-08-10T1112Z_diquark-adjudication.md               f74ccb54…  MATCH
    tests/test_p2_diquark_adjudication.py                        e9792963…  MATCH

**A7 — branch 2's seven arriving blobs**, at `bc1e5c74`, **all match:**

    derivations/P2-PHASE-01_diquark_both_eta.md                  e0eff746…  MATCH
    reports/2026-08-10T0245Z_diquark-both-eta.md                 dd21f90c…  MATCH
    results/P2-PHASE-01/diquark-both-eta/diquark.json            b9af37d0…  MATCH
    reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md         63d09ee9…  MATCH
    scripts/p2_diquark_both_eta.py                               51582012…  MATCH
    specs/2026-08-10T0245Z_diquark-both-eta.md                   2ee21681…  MATCH
    tests/test_p2_diquark_both_eta.py                            abcd0a22…  MATCH

**All fourteen match their pinned ids.** A6 and A7 pass at the source.
Their at-merged-head halves are necessarily unreported: there is no merged
head.

---

## 5. A5 — the review, and the seventh delimiter failure

Committed at `reviews/chatgpt/2026-08-11T2152Z_land-diquark-line.md` in
commit 2, before any merge would have occurred.

    committed blob sha256  191f847e2bd280d951d1efdcc5df12e716b482c7e6462d4b6c042e2f26c528cd
    size                   8151 bytes, 8107 characters, 145 lines
    identical to the extracted text:  True

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: []   ENDS: [line 148]

**Seventh instance.** The BEGIN delimiter shared its line with the
attachment marker; the previous task's supply happened to put it on its
own line and this one does not. Same asserted rule as before:

    END      whole line, exactly one occurrence (line 148)
    BEGIN    the unique line whose content, after removing a prefix
             matching r'^@"[^"]+"\s+', equals the delimiter exactly

    prefix matches r'^@"[^"]+"\s+'   True
    remainder == the BEGIN literal   True

**One point of care on A5's correspondence test, reported because I
checked it and it is not clean.** A5 says to STOP if the supplied text
*"does not correspond to this specification"*. The review corresponds —
but **it does not contain either source-branch SHA**; it says only that
*"the two source branches are individually pinned"*. So my correspondence
determination rests on the other markers, all present: the task title, the
evidence base `57c5a6eb…`, the six-commit lifecycle, the eighteen-path
scope, `OPPOSITE`, and criteria `A1`–`A13`. **I record which markers I
used, because "corresponds" is a judgement and the two SHAs would have
been the strongest evidence for it.**

Residual normalisation, unchanged and still one byte: the literal slice is
8152 bytes with one leading and one trailing newline; committed with the
leading blank line dropped.

### The review's four findings, and where each stands

The Reviewer named four things the report must preserve. **Three are now
moot for this execution and one is directly engaged:**

1. *"Two merges in one task … the executor should report whether batching
   caused any ambiguity in guard state, parentage, scope attribution, or
   post-merge verification."* **Engaged, and answered in §8.**
2. *"`OPPOSITE` is the highest-risk semantic boundary."* **Moot here** — no
   result landed, so this report makes no `OPPOSITE` claim at all. §7 says
   what it would have had to say.
3. *"The addendum must distinguish frozen sensitivity from unresolved
   convention dependence."* **Moot** — the addendum was not written, per
   §0.
4. *"The adjudication's negative result about ordering must remain
   negative."* **Moot for this report**, and preserved by omission: this
   report asserts nothing about the pp ordering.

**The Reviewer's closing condition is the one that bit:** *"Execution
should STOP if … any pinned ref or blob fails verification … or either
merge-base …"*. The refs and blobs verified; the merge-base did not.

---

## 6. What state the repository is in

**Nothing pre-existing was disturbed.**

    paths at base 57c5a6eb   307
    paths at head            309
    base-present paths modified or missing     0

    GATES.md, CONVENTIONS.md, AGENTS.md, DECISION_LOG.md,
    pyproject.toml                            all identical

    tests/   17 at base, all identical; 17 at head
             — no arriving test file, because no merge happened

Base-absent paths at head, two, both authorised and both authored by this
task:

    specs/2026-08-11T2152Z_land-diquark-line.md
    reviews/chatgpt/2026-08-11T2152Z_land-diquark-line.md

**A9's gate state, unchanged:** `GATES.md` blob
`849a4fbfe62d6478f092a84b0175357a74bbbb06` at both base and head, `^## P2-`
count 14.

**Refs after the dry run — nothing moved:**

    worktree HEAD                      7a4a443f5221551d1d035a7df1c6a5586f752c80
    gate/p2-diquark-adjudication       3767973bf57c52f4dd2be1fddcf62916ec409c72
    gate/p2-diquark-both-eta           bc1e5c743aada004c52dc7ab7ce2af61de439955
    local main                         0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote main                        57c5a6eb1de11bb7aaf27b779054070ee6870c29
    worktree                           clean

**A13 — branches preserved.** Both source branches are at their recorded
commits and `review/role-model-and-executors` @ `10c260b9…` is untouched.
**This task deleted no branch.**

**A11 — validators, partially applicable.** The six that exist in the tree,
run individually with `python -m pytest <path>`:

    tests/test_repository_structure.py         4 passed in 0.02s                 EXIT=0
    tests/test_si1_governance.py              14 passed in 0.05s                 EXIT=0
    tests/test_gate_anchors.py                18 passed, 2 deselected in 10.11s  EXIT=0
    tests/test_governance_tools.py             8 passed in 1.66s                 EXIT=0
    tests/test_p2_channel_character.py        23 passed in 1.36s                 EXIT=0
    tests/test_p2_chirality_census.py         21 passed in 0.54s                 EXIT=0

    tests/test_p2_diquark_both_eta.py         NOT IN TREE — inapplicable
    tests/test_p2_diquark_adjudication.py     NOT IN TREE — inapplicable

**The last two are inapplicable rather than failing**: they arrive with the
merges, and the merges did not happen. Reporting them as anything other
than inapplicable would misstate what was measured.

**Environment.** Python 3.11.15; `python -m pytest` 9.1.1 (the version A11
mandates); ruff 0.15.8. Nothing was installed. **No environment failure
occurred, so neither of Rule 13's two diagnostic orders was exercised.**

---

## 7. §9's substantive questions, answered at the level this stop permits

§9 asks whether the merged state reads as though the diquark channel's
character were determined, or as though `OPPOSITE` were an absolute label.
**There is no merged state, so the honest answer is that the questions do
not yet arise** — and it matters that this report does not answer them
prematurely.

**What I will say, because it costs nothing and preserves the boundary the
Reviewer flagged as highest-risk:** this report makes **no** claim about
the diquark channel's character, does **not** use `OPPOSITE` in any form,
and asserts **nothing** about the particle–particle ordering. Those
statements belong in the report of a task that actually lands the result,
under the limits §3 of the specification sets.

**§7's Rule 16 assessment.** Rule 16 is operative and I confirm the
candidate junction **as a prediction about the state this task would have
produced**, not as a description of `main`:

> After this task `main` would carry a particle–hole coefficient table, a
> particle–particle coefficient table, a chirality selection rule, an
> adjudication, and a sensitivity addendum. A reader could conclude the
> interaction's channel structure is understood. It is not.

**A stronger junction, specific to the stop.** `main` currently carries
the chirality census, which includes a **structural** particle–particle
classification, and — since the census integration — one **particle–particle
coefficient row**, quoted as context inside a specification. What `main`
does **not** carry is the computation that produced those coefficients, or
the adjudication that resolved the challenge to them. **So the present
state of `main` is the one that most invites over-reading**: a structural
pp classification plus a disclaimed coefficient row, with the supporting
work and its adjudication both absent. The stop leaves that state in
place, which is a reason to re-issue rather than to abandon.

**Search.** I checked what resists the inference: `GATES.md` is unchanged
and records `P2-PHASE-01` as `PROPOSED`; no test mentions either diquark
branch; neither branch is an ancestor of `main`. **No main-line artifact
names the two branches or their status** — the same gap the chirality-census
integration report recorded, and it is unchanged by this stop.

---

## 8. Did batching two merges cost anything?

§9 asks directly, and the batching was a deliberate choice whose cost
should be recorded.

**It cost nothing in this execution, and it saved something.** The stop
occurred at the first guard, before either merge, so no question of
attribution between the two merges ever arose. And because A3 requires a
guard **before each** merge rather than one guard for the pair, **the
failure surfaced at the earliest possible point** — before any tree
changed. A single combined guard run after both merges would have found the
same failure with two merges already made.

**One cost is visible even so, and it is worth recording for the
re-issue.** A2 states both merges' merge-bases in a single block with a
shared rationale (*"Both merge-bases are the original base, because the two
source branches are siblings"*). **The shared rationale is what carried the
error into both entries at once.** Had each merge's merge-base been derived
separately — as A2's own instruction *"do not report one and imply the
other"* requires of the executor — the second entry would have been a
second chance to catch it. **The specification asks the executor not to
imply one from the other, and then does exactly that itself.**

**Nothing about the batching made verification harder.** Each merge's
parentage, blobs and guard are separately specified, and §4 shows the
sequential dry run is straightforward. **If the re-issue keeps the two
merges together, that remains sound**; the finding is about how A2 states
the merge-bases, not about how many merges the task carries.

---

## 9. Commits made, and the deviation from A0's frozen order

    commit 1  b92e405c84fa45930f6574a235d6ce470dccd1ba
      specs/2026-08-11T2152Z_land-diquark-line.md
      "spec: land the diquark line -- adjudication, both-eta result, and an addendum"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  7a4a443f5221551d1d035a7df1c6a5586f752c80
      reviews/chatgpt/2026-08-11T2152Z_land-diquark-line.md
      "review: commit the pre-execution review for landing the diquark line"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 3  THIS REPORT
      "docs: STOP report -- the diquark line was not landed"
      trailers suppressed: reported post-report, per §5.

**Commits 3, 4 and 5 of A0's order were not made**: commits 3 and 4 are
the two merges, and commit 5 is the addendum, which §5 places *after* both
merges because it records a relation between the two arriving bodies of
evidence. **With neither body of evidence in the tree, writing the addendum
would have recorded a relation between things that are not there.**

**So this report occupies commit 3 on this branch rather than commit 6.**
That is a deviation from A0's frozen commit order, and it is forced by the
stop rather than chosen: the alternative is a stop that produces no report,
which would leave the finding nowhere. **A0's order presumes the task
completes, and no clause covers the aborted case.** I record the deviation
rather than renumbering silently.

**A12 — hygiene** was applied to both commits made: each message inspected
before writing (proposed file) and after (`git log -1 --format='%B'`, from
the object), scan pattern
`co-authored-by|claude|session|https?://|generated with|anthropic`, case
insensitive, no match either side, default trailers suppressed at authoring
time.

**Pre-report head:** `7a4a443f5221551d1d035a7df1c6a5586f752c80`

**Intended report commit message:**

    docs: STOP report -- the diquark line was not landed

    A3's mandated PRE_MERGE guard before merge 1 returned overall FAIL,
    exit 2, on merge_base: expected 57c5a6eb, actual 8701a97a. Both source
    branches were cut from 8701a97a, main has since advanced to 57c5a6eb
    through the chirality-census work, and 57c5a6eb is an ancestor of
    neither branch. A2 requires merge-base = 57c5a6eb for both merges and
    cannot be satisfied by any action the specification permits: the only
    ways to change that value are to rebase a source branch or to merge
    something other than the pinned refs, and section 8 forbids both.
    Section 10's "CONFIRMED both branches share the merge-base 57c5a6eb"
    does not reproduce; they share 8701a97a.

    Neither merge was performed, main was not moved, no branch was
    rebased, the addendum was not written, and the guard configuration was
    not adjusted to make it pass.

    Everything else reproduces. A1's three refs match. All fourteen
    arriving blob ids match at their branches. A sequential read-only dry
    run shows both merges conflict-free, and the predicted combined
    base-to-head is 16 additions, 0 modifications, 0 deletions -- 18 with
    the addendum and this report, matching A4's manifest. The corrected
    merge-base for both merges is 8701a97a.

    P2-PHASE-01 stays PROPOSED; 307 base paths unchanged; the six
    applicable validators exit 0 and the two arriving test files are
    inapplicable because they did not arrive.

---

## 10. Stops and clarifications

**`SPECIFICATION_DEFECT` — one, and it is the stop.**

**A2's stated merge-base is factually wrong for both merges, and
unsatisfiable.** `merge-base(evidence base, either source branch)` is
`8701a97a…`, not `57c5a6eb…`, because both branches were cut from
`8701a97a…` and `main` has since advanced. §6 A2's rationale — *"Both
merge-bases are the original base, because the two source branches are
siblings"* — conflates the branches' merge-base *with each other* (true,
`8701a97a…`) with each branch's merge-base *with the current base* (false).
**§10's `CONFIRMED both branches share the merge-base 57c5a6eb…` does not
reproduce.**

The correction is in §3 and is two values. **No other criterion is
affected**: A4's arithmetic, A6's and A7's fourteen blob ids, the
conflict-free premise and the 18-path manifest all reproduce, so a
re-issue changing A2's two merge-base values and its rationale, and §10's
one line, should execute straight through.

**`OBSERVATION_METHOD_ERROR` — none.**

One secondary observation to the specification's credit: **A3 requiring a
guard before *each* merge rather than one for the pair is what made this
cheap.** The failure surfaced before any tree changed. A single
post-merge guard would have found the same thing with both merges already
made, and unwinding would then have been the executor's problem.

A second, about my own method: the sequential dry run needed a commit
object for the first result, so `git commit-tree` created one and left it
**unreferenced**. I report that because it writes to the object store; it
moves no ref, creates no branch, and §6 verifies every ref afterwards.
§10's own method is a sequential dry run, so the procedure is the
specification author's, performed read-only.

**`REPOSITORY_DEFECT` — none.** 307 base paths unchanged; the five named
files blob-identical; `GATES.md` untouched; both source branches and the
protected review branch at their recorded commits.

Two secondary observations carried forward unchanged: **no main-line
artifact names the two unintegrated diquark branches or their status**
(§7), and **`CONVENTIONS.md`'s seventeen rules still have no structural
validator** — which now includes the review supply protocol, at its seventh
failure (§5).

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none reached the
threshold of a stop.**

One secondary finding: **A0's frozen commit order has no aborted case**
(§9). This report occupies commit 3 rather than commit 6 because commits
3–5 are the merges and the addendum. A clause covering the stop path —
"if the task stops, the report is the next commit" — would remove an
executor decision from a situation that is already going badly.

Also carried forward: **A5's correspondence test rests on judgement**, and
here the supplied review omits both source-branch SHAs (§5), so I recorded
which markers I used instead of asserting correspondence bare.

**`ENVIRONMENT` — none.** No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised. Nothing was installed.

**Things I would have specified differently.**

*A2 should derive each merge-base rather than assert both from one
rationale.* Its own instruction to the executor — *"do not report one and
imply the other"* — is the right discipline, and A2 does not apply it to
itself. Applying it would have caught this before issue.

*§10's pre-issue record should say which command produced each
`CONFIRMED`.* *"CONFIRMED both branches share the merge-base 57c5a6eb…"*
is one line covering two different claims — that the branches share a
merge-base, and that its value is `57c5a6eb…`. The first is true, the
second is not, and a single `CONFIRMED` cannot distinguish them. Amendment
H's discipline is about the *check type*; this is the neighbouring point
that a record should be **one line per checkable proposition**.

*A criterion should exist for "the source branch descends from the
evidence base", separately from the merge-base value.* It is the
underlying property, it is a one-line
`git merge-base --is-ancestor` test, and stating it directly would have
made the failure legible immediately rather than through a merge-base
mismatch. **Every previous integration in this sequence happened to merge
a branch cut from the then-current `main`, so the question never arose.**
This is the first task in the sequence where two branches waited while
`main` advanced, and it is exactly the case the deferred-items work warned
about: a branch can become awkward to integrate silently, with nothing
telling anyone to look.
