# Report — land the diquark line (re-issue)

Specification: `specs/2026-08-11T2207Z_land-diquark-line.md`
Specification sha256:
`122b174367ba782224a9923cc6d41398adb91beee5df86a79bf9b8c0a76a235c`
Pre-execution review: `reviews/chatgpt/2026-08-11T2207Z_land-diquark-line.md`
Evidence base: `57c5a6eb1de11bb7aaf27b779054070ee6870c29`
Branch 1: `gate/p2-diquark-adjudication` @ `3767973bf57c52f4dd2be1fddcf62916ec409c72`
Branch 2: `gate/p2-diquark-both-eta` @ `bc1e5c743aada004c52dc7ab7ce2af61de439955`
Branch: `gate/p2-land-diquark-line-v2`
Superseded first issue: `gate/p2-land-diquark-line` @ `d64cd912ca9ff78a85787f0e54f345f474cdb192` — preserved, untouched
Classification: MATERIAL.

---

## 0. Summary

**Both merges executed, both clean, in the specified order.** Two
`PRE_MERGE` guards, one immediately before each merge, both `PASS`. All
fourteen arriving blobs identical at their pins, at their sources, and at
the merged head. 201 pre-existing protected paths unchanged. `GATES.md`
blob-identical, fourteen `## P2-` sections, `P2-PHASE-01` `PROPOSED`,
`P2-GAP-01` `PASS`. All **eight** validators exit 0, including the two
arriving suites running against the merged tree for the first time.

**The repair worked.** The corrected merge-base `8701a97a…` verified at
both guards, and A2a's ancestry observation surfaced the stale-branch fact
as a fact rather than as a merge failure. §3 reports each merge's three
values derived separately from the objects, as A2 now requires.

**Two things worth the reader's attention:**

- **A2's separate-derivation requirement was necessary but not
  sufficient** (§9). It fixes the mechanism that carried the first issue's
  error into both entries — but the two merge-bases are *genuinely equal
  here*, so a repeated value is what correct execution produces. §9 says
  what makes the two indistinguishable and what would settle it.
- **A5's transport-artifact clause removed the last executor decision from
  the review-supply path** (§4). The delimiter still arrived on a shared
  line — eighth instance — but the one-byte normalisation is now
  specified, so I applied a rule rather than choosing one.

No STOP condition fired.

---

## 1. A1 — refs, read from the remote

    remote refs/heads/main                     57c5a6eb1de11bb7aaf27b779054070ee6870c29
    refs/remotes/origin/main                   57c5a6eb1de11bb7aaf27b779054070ee6870c29
    branch 1  gate/p2-diquark-adjudication     3767973bf57c52f4dd2be1fddcf62916ec409c72
    branch 2  gate/p2-diquark-both-eta         bc1e5c743aada004c52dc7ab7ce2af61de439955
    local main (stale by design)               0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    superseded gate/p2-land-diquark-line       d64cd912ca9ff78a85787f0e54f345f474cdb192

All four pinned refs match; no mismatch, so no STOP. Local `main` is stale
by design, neither consulted nor repaired. **The first issue's branch was
read only to confirm its head and was neither touched, reused nor
deleted.**

---

## 2. A2a — source-branch ancestry, as its own property

    git merge-base --is-ancestor 57c5a6eb 3767973b   ->  exit 1   NOT an ancestor
    git merge-base --is-ancestor 57c5a6eb bc1e5c74   ->  exit 1   NOT an ancestor

    control, a TRUE case for comparison:
    git merge-base --is-ancestor 8701a97a 3767973b   ->  exit 0   IS an ancestor

**Neither branch descends from this evidence base, and that is expected**:
both were cut from `8701a97a…` and waited while `main` advanced through the
chirality-census work. **Reported as an observed fact, not a failure.**

**Exit 1 is a definite negative answer from `git`, not an execution
failure**, and the review asks for that distinction explicitly. The control
line is included because a bare `exit 1` cannot by itself distinguish "the
answer is no" from "the command did not work" — running a case whose answer
is known to be yes, with the same command shape, shows the test
discriminates.

**This criterion is the one the first issue lacked**, and it does the work
it was added for: the stale-branch fact is now visible as a one-line
observation *before* the guard, instead of arriving as a merge-base
mismatch that looked like a failure.

---

## 3. A2 — merge parentage, each merge derived separately

**Merge 1**, values read from the merge object:

    merge 1 commit       5465d7d58484d782a312c693a16213edd35d9947
    parent 1             8a67614b963956dc0744f4a6cac87262e9a58958   = commit 2, the review
    parent 2             3767973bf57c52f4dd2be1fddcf62916ec409c72   = branch 1
    merge-base(p1,p2)    8701a97a6bb58550d4300f75c10638b057335731
    commit 1 is an ancestor of merge 1:  yes

**Merge 2**, values read from the merge object, computed after merge 1
existed and not carried from it:

    merge 2 commit       8542ec5747427e728df28b4447b51c10e32ae43e
    parent 1             5465d7d58484d782a312c693a16213edd35d9947   = merge 1
    parent 2             bc1e5c743aada004c52dc7ab7ce2af61de439955   = branch 2
    merge-base(p1,p2)    8701a97a6bb58550d4300f75c10638b057335731
    commit 1 is an ancestor of merge 2:  yes

Side by side, and **neither implied from the other**:

    merge  parent 1                                  parent 2                                  merge-base
    1      8a67614b963956dc0744f4a6cac87262e9a58958  3767973bf57c52f4dd2be1fddcf62916ec409c72  8701a97a…
    2      5465d7d58484d782a312c693a16213edd35d9947  bc1e5c743aada004c52dc7ab7ce2af61de439955  8701a97a…

**The three quantities A2 distinguishes, measured separately:**

    merge-base(evidence base, branch 1)   8701a97a…    <- what A2 constrains
    merge-base(evidence base, branch 2)   8701a97a…    <- what A2 constrains
    merge-base(branch 1, branch 2)        8701a97a…    <- a DIFFERENT quantity

**All three happen to be equal, and that is exactly the coincidence the
first issue tripped over.** The first issue reasoned from the third to the
first two. Here each was measured; §9 returns to whether measuring them
separately is enough when the answers agree.

---

## 4. A5 — the review, and the eighth delimiter instance

Committed at `reviews/chatgpt/2026-08-11T2207Z_land-diquark-line.md` in
commit 2, **before both merges**.

    committed blob sha256  42673c908bf5b074fd31d3d6570e231d5f2a932b3a245a2f3f2a838df9e605dc
    size                   8383 bytes, 8341 characters, 184 lines

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: []   ENDS: [line 187]

**Eighth instance of the shared-line supply.** The BEGIN delimiter shared
its line with the attachment marker; the same asserted rule was applied:

    END      whole line, exactly one occurrence
    BEGIN    the unique line whose content, after removing a prefix
             matching r'^@"[^"]+"\s+', equals the delimiter exactly

    prefix matches r'^@"[^"]+"\s+'   True
    remainder == the BEGIN literal   True

**The difference from the previous seven: the normalisation is now
specified.** A5 says *"strip at most one leading and one trailing blank
line as transport artifacts; apply no other normalisation."* Measured:

    literal slice          8384 bytes, 1 leading blank line, 1 trailing blank line
    committed              8383 bytes — one leading blank line stripped,
                           single trailing newline retained

**So the one-byte decision that every previous report flagged as an
unwritten executor choice is now a rule I followed.** That is the first
clause of the supply protocol to be written down, and it closed the part it
addresses.

**A5's correspondence test, now with strong markers.** The specification
asked the review to name both source-branch heads and this specification's
digest, and to record which markers were used otherwise. Measured, all
present in the review text:

    land the diquark line v2                     present
    3767973bf57c52f4dd2be1fddcf62916ec409c72     present   <- branch 1 head
    bc1e5c743aada004c52dc7ab7ce2af61de439955     present   <- branch 2 head
    57c5a6eb1de11bb7aaf27b779054070ee6870c29     present   <- evidence base
    gate/p2-land-diquark-line-v2                 present   <- prescribed branch
    d64cd912ca9ff78a85787f0e54f345f474cdb192     present   <- superseded branch
    A2a                                          present
    eighteen additions                           present

**The specification's own digest is not present, and cannot be**: the review
is written before commit 1 fixes the artifact. The review says so itself and
supplies the branch heads instead. **So correspondence rests on six exact
object identifiers rather than on wording** — a materially stronger footing
than the first issue, whose review named neither branch head.

**None of A5's three STOP conditions applies**: the text is present, both
delimiter lines are present, and it corresponds.

### The review's eight required re-verifications

Approval certified none of the specification's §10 observations. All eight
were reproduced independently:

    1  both remote source refs and remote main                §1        PASS
    2  merge-base of each source branch                       §3        PASS
    3  A2a's two --is-ancestor negatives, exit 1 vs failure   §2        PASS
    4  both conflict-free PRE_MERGE guards                    §5        PASS
    5  all fourteen arriving blob ids                         §6        PASS
    6  the final 18-addition / 0-modification scope           §7, §11   PASS
    7  all protected-path comparisons                         §6        PASS
    8  all eight validator executions                         §8        PASS
    9  both source branches and the review branch unmoved     §10       PASS
    10 final POST_MERGE with both roles distinct              §5, §11   intended params

---

## 5. A3 — the two guards

### `PRE_MERGE` 1, immediately before merge 1

    worktree_clean                         PASS
    worktree_matches_declared_target       PASS   head 8a67614b…
    merge_base                             PASS   expected 8701a97a… actual 8701a97a…
    scope                                  PASS   2 operations, failures []
    pinned_artifacts                       PASS   GATES.md, CONVENTIONS.md,
                                                  the phase-A freeze
    OVERALL                                PASS   EXIT=0

    dry run: predicted tree 5b810bd6164a8e55334d107aab2f027a28cb4afb, 0 conflict lines

### `PRE_MERGE` 2, immediately before merge 2

    worktree_clean                         PASS
    worktree_matches_declared_target       PASS   head 5465d7d5… (= merge 1)
    merge_base                             PASS   expected 8701a97a… actual 8701a97a…
    scope                                  PASS   9 operations, failures []
    pinned_artifacts                       PASS   same three
    OVERALL                                PASS   EXIT=0

    dry run: predicted tree 540baa32765b147d7435364ebda72627fbfc2047, 0 conflict lines

**The second guard is not a repeat of the first.** Its declared worktree
head is merge 1, its scope observes nine operations rather than two, and
its `reviewed_branch` is branch 2. **It is what confirms merge 1 landed
exactly the seven paths it should have before merge 2 begins** — which is
the specific value of placing a guard before *each* merge rather than one
before the pair.

**The pins are the arriving-side values** for `GATES.md`, `CONVENTIONS.md`
and the phase-A freeze, all of which both branches leave alone, so pinning
them asserts that neither branch touches them. That is the assertion worth
making at `PRE_MERGE`, and the reason an earlier integration's guard failed
when a pin was aimed at the base instead.

### `POST_MERGE`, intended parameters

A3 requires **two distinct SHAs in two distinct roles**. The tool supports
it: `merge_commit` names the object under verification and
`expected_remote_sha` the ref-agreement target, as separate keys. **Both
roles can be represented separately, so no STOP.**

    mode                    POST_MERGE
    merge_commit            8542ec5747427e728df28b4447b51c10e32ae43e   <- merge 2, the final merge object
    expected_parent_1       5465d7d58484d782a312c693a16213edd35d9947
    expected_parent_2       bc1e5c743aada004c52dc7ab7ce2af61de439955
    expected_merge_base     8701a97a6bb58550d4300f75c10638b057335731
    scope_manifest          the final manifest of §7
    pinned_artifacts        GATES.md                                  8ce38b8a…072e526
                            CONVENTIONS.md                            e3afa521…f94a451
                            derivations/P2-CHANNEL-FREEZE-01_phaseA…  fe68b9c6…12a4e67a
    remote_check_policy     REQUIRED
    expected_remote_ref     refs/remotes/origin/main
    expected_remote_sha     <the final report-commit head>            <- ref agreement

**One observation about the guard's reach with two merges.** `POST_MERGE`
verifies **one** merge object. Verifying merge 2 checks the final merge and
its parentage, and merge 1 is reachable as merge 2's parent 1 — but the
guard does not itself re-verify merge 1's own parentage. **§3 above is where
merge 1's three values are evidenced**, and §9 counts this among the
batching's costs.

---

## 6. A6, A7 — fourteen arriving blobs; A8 — protected paths; A9 — no gate changed

**A6 and A7**, compared as git blob ids with `git rev-parse <rev>:<path>` —
not content digests — at three places each: the pinned value, the source
branch, and the merged head.

    A6, branch 1 @ 3767973b
      derivations/P2-PHASE-01_diquark_adjudication.md              7983d4ba…  MATCH
      reports/2026-08-10T1112Z_diquark-adjudication.md             48bc2965…  MATCH
      results/P2-PHASE-01/diquark-adjudication/adjudication.json   77805645…  MATCH
      reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md     2c7806f9…  MATCH
      scripts/p2_diquark_adjudication.py                           529d5ef0…  MATCH
      specs/2026-08-10T1112Z_diquark-adjudication.md               f74ccb54…  MATCH
      tests/test_p2_diquark_adjudication.py                        e9792963…  MATCH

    A7, branch 2 @ bc1e5c74
      derivations/P2-PHASE-01_diquark_both_eta.md                  e0eff746…  MATCH
      reports/2026-08-10T0245Z_diquark-both-eta.md                 dd21f90c…  MATCH
      results/P2-PHASE-01/diquark-both-eta/diquark.json            b9af37d0…  MATCH
      reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md         63d09ee9…  MATCH
      scripts/p2_diquark_both_eta.py                               51582012…  MATCH
      specs/2026-08-10T0245Z_diquark-both-eta.md                   2ee21681…  MATCH
      tests/test_p2_diquark_both_eta.py                            abcd0a22…  MATCH

**All fourteen identical at pin, source and merged head.** Everything
arriving by merge is integrated exactly as reviewed; nothing was edited.

**A8**, compared as individual blob object ids from `git ls-tree -r`, path
by path:

    pre-existing protected paths checked        201
    differing at the merged head                 0

    GATES.md, CONVENTIONS.md, AGENTS.md,
    DECISION_LOG.md, pyproject.toml            all identical

    per-prefix counts of base-present paths, all blob-identical:
      scripts/ 57   results/ 67   tests/ 17   derivations/ 31
      docs/ 7       reviews/ 17

**`tests/` count before and after, as A8 requires:**

    BEFORE  17        AFTER  19        +2 arriving
    all 17 pre-existing test files blob-identical:  True

Base-absent paths at the merged head, sixteen: the fourteen arriving, plus
this task's specification and review. Base-present paths absent at head:
none.

**A9 — no gate changed:**

    GATES.md blob   base 849a4fbfe62d6478f092a84b0175357a74bbbb06
                    head 849a4fbfe62d6478f092a84b0175357a74bbbb06   identical
    ^## P2- count   base 14   head 14
    P2-PHASE-01     Status: PROPOSED
    P2-GAP-01       Status: PASS (continuum exact; lattice `I_0` agrees with paper…)

---

## 7. A4 — the intended final manifest

    {
      "mode": "exact",
      "base": "57c5a6eb1de11bb7aaf27b779054070ee6870c29",
      "head": "<the final report-commit head>",
      "required": [
        {"operation": "add", "path": "derivations/P2-PHASE-01_diquark_adjudication.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_diquark_both_eta.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_diquark_sensitivity_addendum.md"},
        {"operation": "add", "path": "reports/2026-08-10T0245Z_diquark-both-eta.md"},
        {"operation": "add", "path": "reports/2026-08-10T1112Z_diquark-adjudication.md"},
        {"operation": "add", "path": "reports/2026-08-11T2207Z_land-diquark-line.md"},
        {"operation": "add", "path": "results/P2-PHASE-01/diquark-adjudication/adjudication.json"},
        {"operation": "add", "path": "results/P2-PHASE-01/diquark-both-eta/diquark.json"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-11T2207Z_land-diquark-line.md"},
        {"operation": "add", "path": "scripts/p2_diquark_adjudication.py"},
        {"operation": "add", "path": "scripts/p2_diquark_both_eta.py"},
        {"operation": "add", "path": "specs/2026-08-10T0245Z_diquark-both-eta.md"},
        {"operation": "add", "path": "specs/2026-08-10T1112Z_diquark-adjudication.md"},
        {"operation": "add", "path": "specs/2026-08-11T2207Z_land-diquark-line.md"},
        {"operation": "add", "path": "tests/test_p2_diquark_adjudication.py"},
        {"operation": "add", "path": "tests/test_p2_diquark_both_eta.py"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**18 additions, 0 modifications**: fourteen arriving, four authored here.
At the pre-report head the count is **17 additions, 0 modifications, 0
deletions** — this report is the eighteenth. The final scope check is
post-report evidence per §5.

---

## 8. A11-pre — validators

Run individually with `python -m pytest <path>` at the pre-report head
`478a0e6a…`:

    tests/test_repository_structure.py         4 passed in 0.10s                 EXIT=0
    tests/test_si1_governance.py              14 passed in 0.06s                 EXIT=0
    tests/test_gate_anchors.py                18 passed, 2 deselected in 7.71s   EXIT=0
    tests/test_governance_tools.py             8 passed in 1.79s                 EXIT=0
    tests/test_p2_channel_character.py        23 passed in 1.23s                 EXIT=0
    tests/test_p2_chirality_census.py         21 passed in 1.59s                 EXIT=0
    tests/test_p2_diquark_both_eta.py         20 passed in 7.80s                 EXIT=0
    tests/test_p2_diquark_adjudication.py     24 passed in 0.78s                 EXIT=0

**All eight exit 0.** The last two matter most: they were written on their
branches and had never run in the presence of `main`'s other content. **In
the first issue they were `NOT IN TREE — inapplicable`; here they run and
pass**, which is the substantive difference between the stop and the
landing.

**Environment.** Python 3.11.15; `python -m pytest` 9.1.1 (the version A11
mandates); ruff 0.15.8. Nothing was installed. **No environment failure
occurred, so neither of Rule 13's two diagnostic orders was exercised.**

---

## 9. Did batching two merges cost anything? — tested, not repeated

§9 asks for this to be tested rather than restated. The first issue's answer
was that the cost was not the merge count but **a shared rationale under
which one derivation served two entries.** A2 now requires each merge's
values derived separately.

**Was that sufficient? Partly — and the reason it is only partly is worth
more than the fix.**

**What it fixed.** The mechanism is gone. §3 reports six values obtained
from six separate object reads, and §5 reports two guards whose declared
heads, scopes and branches all differ. Nothing in this execution was
carried from one merge to the other.

**What it does not fix, and cannot.** **The two merge-bases are genuinely
equal here — both `8701a97a…`.** So the output of correct separate
derivation is *indistinguishable* from the output of the incorrect shared
derivation the first issue performed. A reader of §3 cannot tell, from the
values alone, whether I measured twice or measured once and copied.
**A2's requirement is unfalsifiable from its own artifact.**

That is not hypothetical: it is precisely the configuration in which the
first issue's error survived review. Both entries agreed, agreement looked
like corroboration, and the shared rationale was invisible in the result.

**What would settle it.** The evidence that distinguishes the two cases is
not the merge-base at all — it is **A2a**. `merge-base --is-ancestor` per
branch is a *different* question with a *branch-specific* answer, and
running it twice produces two observations that a single shared derivation
could not have produced. **A2a is therefore doing double duty**: it supplies
the stale-branch fact, and it is the only part of §2–§3 whose repetition
carries information. Were I specifying this, I would say so — A2's
separate-derivation clause is good discipline that cannot audit itself, and
A2a is what audits it.

**Two further batching costs, both small and both real:**

- **`POST_MERGE` verifies one merge object** (§5). With two merges, merge
  1's parentage is evidenced only by this report, not by the guard. A second
  `POST_MERGE` naming merge 1 would close that, at the cost of a run.
- **The scope manifest cannot distinguish which merge brought which
  path.** The final check sees 18 additions and cannot attribute seven to
  merge 1 and seven to merge 2. **`PRE_MERGE` 2's nine-operation scope is
  what recovers the attribution** — it observes exactly the state after
  merge 1 — so the guard placement A3 mandates is load-bearing for more
  than conflict detection.

**Nothing about the batching made the science harder to verify**, and the
episode genuinely is one: §10's addendum records a relation between the two
arriving bodies of evidence and could not have been written after either
merge alone.

---

## 10. A10 — the addendum, in full, and it corrects nothing

**Stated explicitly, as A10 requires: the addendum corrects nothing.** The
both-`η` derivation is right, uses the frozen conventions and states them.
The addendum records that its family support *rests on* two of them.

Committed as commit 5, **after both merges**, because it records a relation
among the both-`η` result, the adjudication and the already-integrated
chirality census. Every factual claim in it was verified against the
artifacts as they stand on this branch after the merges — the ablation rows
were read from `adjudication.json`, the coefficients and verdict from
`diquark.json`, the census's Step E from `census.json`, and the
`(iγ₅)⊗(iγ₅) = −(γ₅⊗γ₅)` identity recomputed directly (residual exactly
`0`).

**Each of §2's six required elements, and where it appears:**

    the sensitivity, with the mechanism and the ablation's outcome   §1
    that both conventions are FROZEN, not free                       §2
    why it is recorded anyway                                       §3
    the relation to the chirality census, support only               §4
    the independence claim at the licensed level                     §5
    what remains unfrozen                                           §6

The addendum's own §7 states what it does not do. Its content:

- **§1 — the sensitivity.** The two conventions; the mechanism
  `(iγ₅)⊗(iγ₅) = −(γ₅⊗γ₅)`, with the pseudoscalar operator entering the
  rank-4 tensor twice so the two canonical terms of `S²+P²` add where they
  would otherwise cancel; the narrower `A`/`T` mechanism, where `f_pp`
  carries `Γ_p` twice so a factor `i` gives `i⁻² = −1` and flips those two
  coefficients only; and the full six-row ablation table showing that
  restoring `iγ₅` alone moves the support from `S`/`P`/`T` to `V`/`A`, that
  restoring the `A`/`T` factor alone flips `A` and `T`, and that the gamma
  representation is not causal.
- **§2 — both conventions are FROZEN, not free.** Quoted from the phase-A
  freeze in prose and machine block. **The addendum refuses to compress
  "sensitive to a decided convention" and "dependent on an undecided
  convention" into a generic convention dependence**, and tabulates the two
  categories separately: `iγ₅` and the `A`/`T` factor as frozen and
  load-bearing; `η`, the pp ordering and the diquark normalisation as still
  unfrozen.
- **§3 — why it is recorded anyway**, with three concrete uses: a future
  Phase-B revisit of the freeze; a future independent recomputation, for
  which this is the first pair to check; and because *"S, P and T vanish"*
  is short and memorable and true only under the frozen conventions, so the
  provenance should travel with it.
- **§4 — the relation to the census.** The census explains **support
  only**; its own Step E lists the inter-channel sign and the magnitudes
  among what it is silent on. The addendum states the two accounts are
  complementary rather than duplicative, and records that **the census's own
  falsification test independently reproduces the ablation's first row**, by
  a different route and in the other channel.
- **§5 — the independence claim.** The adjudication **found no evidence
  against** it, since `L3` was `IDENTICAL` and the divergence was not an
  ordering effect. **It did not establish independence over untested
  admissible pp orderings**, and no alternative slot map was tried. **The
  negative result stays negative.**
- **§6 — what remains unfrozen**, with the state of each of the three.

---

## 11. §7 — Rule 16 assessment

Rule 16 is operative. **I confirm §7's candidate and add a stronger
junction.**

After this task `main` carries a particle–hole coefficient table, a
particle–particle coefficient table, a chirality selection rule, an
adjudication resolving a discrepancy, and a sensitivity addendum. **A reader
could conclude the interaction's channel structure is now understood. It is
not.** Three conventions remain unfrozen; the absolute channel character is
undetermined; the inter-channel sign is unexplained; and the pp ordering
question was neither confirmed nor refuted.

**The stronger junction, and it is specific to what this task changed.**
Before this merge, the particle–particle coefficients existed on `main` only
as a single **disclaimed** row quoted as context inside the census
specification — the chirality-census integration report measured that as
`0 → 1` and recorded that no main-line artifact named the branches or their
status. **After this task the coefficients are on `main` as a result, with
their script, their tests and their adjudication.** The disclaimed-context
framing is gone, replaced by the real thing.

**That is the right outcome and it removes one protection.** What now
carries the limits is prose inside the arriving reports and the addendum —
which is stronger than before, because those documents are the result's own
record rather than a passing mention. But **nothing mechanical enforces
it.** Specifically:

    no test asserts that OPPOSITE is a relative statement
    no test asserts that the pp ordering question is open
    GATES.md records P2-PHASE-01 as PROPOSED with no pp result, which is
      correct but says nothing about what the pp result does not establish

**Search.** I looked for what would resist the over-reading: the addendum's
§7 and §5, the both-`η` report's scope sections, the adjudication's
`case_decision.ordering_index_map_case_applies = false`, and
`diquark.json`'s `scope_limits`, which a test does assert. **The strongest
mechanical protection that exists is `diquark.json`'s scope fields**, and
they constrain the artifact rather than any reader's summary of it. **The
gap is the same one the SI-1 cross-reference task addressed for
`DEFERRED-02`**: a limit that is recorded but not reachable from where a
reader starts. Whether the diquark limits deserve the same remedy — a
pointer from `GATES.md`, or a register entry — **is a PI decision and not
this task's.**

---

## 12. Does the merged state read as though the channel were determined?

§9 asks, and **neither reading is true.**

**Does it read as though the diquark channel's character were
determined?** No. The merged artifacts state the opposite in their own
words, in several places and at several levels of formality: the both-`η`
derivation carries `η`, `s_pp` and `ν` as symbols and reports the absolute
label as **not** well-defined; `diquark.json` carries
`still_unfrozen_after_this_computation` with three entries and
`conventions_frozen_by_this_computation` empty, both asserted by tests; the
adjudication reports the ordering case as not applying; the addendum's §5
and §6 say it directly; and both merge messages say it.

**Does it read as though `OPPOSITE` were an absolute label?** No, and this
is the boundary the review called highest-risk, so it is worth being exact.
**`OPPOSITE` means: `η → −η` reverses the non-zero coefficient signs for a
fixed remainder of the construction.** Measured ratios `−1` for both `V`
and `A`, with `s_pp` and `ν` still symbolic and cancelling. **It does not
say which representative is attractive and which repulsive**, because that
requires the two unfrozen conventions the ratio cancels. **This report uses
`OPPOSITE` nowhere without that qualification**, and merge 2's own message
carries the qualification into the history.

**One thing I will not say, because the specification forbids it and the
evidence does not support it:** that the census explains the coefficient
signs. It explains support only.

---

## 13. A12 — commit-message hygiene, and intended final state

Each message inspected before writing (proposed file) and after
(`git log -1 --format='%B'`, from the object). Scan pattern, case
insensitive: `co-authored-by|claude|session|https?://|generated with|
anthropic`. **Both merges included, as A12 requires.**

    commit 1  de5fac582cc67b93db341c3898cee5facd262745
      specs/2026-08-11T2207Z_land-diquark-line.md
      "spec: land the diquark line, re-issued with the merge-base corrected"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  8a67614b963956dc0744f4a6cac87262e9a58958
      reviews/chatgpt/2026-08-11T2207Z_land-diquark-line.md
      "review: commit the pre-execution review for landing the diquark line v2"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 3  5465d7d58484d782a312c693a16213edd35d9947   (merge 1)
      "merge: integrate the diquark decomposition adjudication
       (reviewed; pinned 3767973)"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 4  8542ec5747427e728df28b4447b51c10e32ae43e   (merge 2)
      "merge: integrate the diquark both-eta channel character
       (reviewed; pinned bc1e5c7)"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 5  478a0e6aeab8b68c38c9965afa17020830bcc71b
      derivations/P2-PHASE-01_diquark_sensitivity_addendum.md
      "derive: a sensitivity addendum to the diquark both-eta result"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

**§5's commit order was followed exactly**, including the token: `2207`
differs from the superseded first issue's `2152`, so the two executions are
distinguishable by path as Amendment K requires. **The aborted-path clause
was not needed** — the task did not stop — but it is worth recording that
it existed: the first issue met that case and had to improvise, and this
report is written under an order that covers both outcomes.

**Pre-report head:** `478a0e6aeab8b68c38c9965afa17020830bcc71b`

**Intended report commit message:**

    docs: report the landing of the diquark line

    Records A1, A2, A2a, A6-A10, A11-pre and A12 for commits 1-5. Both
    merges executed and clean, in order, each with its own PRE_MERGE guard
    immediately before it and both PASS on the corrected merge-base
    8701a97a. All fourteen arriving blobs identical at pin, source and
    merged head; 201 pre-existing protected paths unchanged; tests/ 17
    before and 19 after with no existing test modified; GATES.md
    blob-identical with fourteen P2- sections, P2-PHASE-01 PROPOSED and
    P2-GAP-01 PASS. All eight validators exit 0, including the two
    arriving suites, which in the first issue were inapplicable.

    A2a did the work it was added for: the stale-branch fact is now a
    one-line observation before the guard rather than a merge-base
    mismatch that looked like a failure, and exit 1 is distinguished from
    execution failure by a control case.

    The batching question, tested rather than repeated: A2's
    separate-derivation requirement removes the mechanism that carried the
    first issue's error into both entries, but the two merge-bases are
    genuinely equal here, so correct separate derivation is
    indistinguishable from the incorrect shared derivation by its own
    output. A2a is what audits it, because its answer is branch-specific.
    Two smaller costs recorded: POST_MERGE verifies one merge object, and
    the final scope cannot attribute paths to either merge -- PRE_MERGE 2
    is what recovers that.

    The addendum corrects nothing. OPPOSITE stays relative: eta -> -eta
    reverses the non-zero coefficient signs for a fixed remainder, and
    assigns no absolute character. Three conventions remain unfrozen and
    the pp ordering question is open in both directions.

---

## 14. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — none in this re-issue.**

The first issue's blocking defect is repaired and the repair verified at
both guards. Two secondary observations:

*The shared-line delimiter supply recurred, an eighth time* (§4) — but **A5
now specifies the normalisation**, so the one-byte residual that every
previous report flagged as an unwritten executor choice is now a rule. **The
part of the protocol that was written down closed; the part that was not —
locating a delimiter that shares its line — did not.** The proposed
`CONVENTIONS.md` paragraph still covers both.

*A2's separate-derivation requirement is unfalsifiable from its own
artifact* (§9). Both merge-bases are genuinely equal, so its output cannot
distinguish compliance from the first issue's error. **A2a is what audits
it.** I would say so in the specification rather than leaving the reader of
§3 to notice.

**`OBSERVATION_METHOD_ERROR` — none.**

Two secondary observations to the specification's credit:

*A2a's request to distinguish exit 1 from execution failure is the right
shape*, and I acted on it with a control case whose answer is known to be
yes. A bare `exit 1` cannot by itself distinguish "no" from "the command did
not run"; the control makes the test discriminate.

*A5's demand that the review name the source-branch heads worked.* The first
issue's review named neither and correspondence rested on wording; this one
names six exact object identifiers. **The specification also correctly
anticipated that its own digest could not appear**, and asked for the
markers used instead.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

One secondary finding, and it is the substantive one: **the diquark result's
limits are recorded but not mechanically enforced** (§11). No test asserts
that `OPPOSITE` is relative or that the pp ordering is open; the strongest
mechanical protection is `diquark.json`'s `scope_limits` fields, which
constrain the artifact and not a reader's summary of it. **Structurally the
same gap the SI-1 cross-reference task addressed for `DEFERRED-02`.** Not
repaired here — this task may write four paths and may not touch `GATES.md`
or add a register — and whether it deserves the same remedy is a PI
decision.

Carried forward unchanged: **`CONVENTIONS.md`'s seventeen rules still have
no structural validator**, which now includes the review supply protocol at
its eighth instance.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two, both preserved
deliberately.**

**The pp ordering question is open in both directions**, and the addendum's
§5 keeps the adjudication's negative result negative: an identical `L3`
excludes the observed discrepancy from being ordering evidence and excludes
nothing else. **The `P`-sign difference recorded in the chirality-census
integration remains unresolved** and was not adjudicated here, per §4 of the
specification.

Both are subject-matter limitations rather than execution ambiguities, which
is how the review classified them.

**`ENVIRONMENT` — none.** No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised. Nothing was installed.

**Things I would have specified differently.**

*A3 should require a `POST_MERGE` per merge, or say why one suffices.* With
two merges, the final guard verifies merge 2 and reaches merge 1 only as a
parent. §3 carries merge 1's parentage on the report's authority alone. One
more guard run would put it on the tool's.

*The final scope manifest cannot attribute paths to a merge, and A4 could
say that `PRE_MERGE` 2 is what recovers the attribution.* It is true and
load-bearing, and I only noticed it because A3 happened to mandate the
second guard for a different reason.

*The re-issue's §10 is the model for an Amendment H record.* It replaced one
unexecuted `CONFIRMED` with four measured lines and an explicit `RETRACTED`,
naming the command used. **The retraction is the part worth generalising**:
recording that a prior check was never run, rather than quietly replacing
it, is what let this report treat the first issue as evidence instead of as
an embarrassment.
