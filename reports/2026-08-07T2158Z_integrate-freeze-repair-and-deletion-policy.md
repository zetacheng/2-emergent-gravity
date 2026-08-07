# Execution report — integrate the freeze-checker repair and the branch-deletion policy

Authority: `specs/2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md`
Evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`
Branch: `fix/integrate-freeze-repair-and-deletion-policy`
Classification: MATERIAL.

**Two merges, both clean, no conflict.** Written at the pre-report head
`d9638f1095cdd7d0eaca9557910113612f6e3006`, before the push. It does not
contain its own commit SHA, the final branch head, or any evidence whose
production depends on the report commit.

**Nothing is deleted by this integration, and Stage 2 remains
unauthorized.** See §9.

---

## 1. A1 — refs, read from the remote

    $ git fetch --prune origin                                   exit 0
    $ git ls-remote origin …

    236f71c69ef9abec33ef0d808724ce80af037710  refs/heads/main
    0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b  refs/heads/fix/freeze-checker-sign-repair
    1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e  refs/heads/fix/branch-deletion-policy-amendment
    f2da41aedc5d3b48cb9d228494272a945fada971  refs/heads/fix/branch-deletion-policy
    10c260b96882ac12610f78840aeeabd07be2d7cb  refs/heads/review/role-model-and-executors

Remote-tracking refs after the fetch, reported separately:

    refs/remotes/origin/main                                  236f71c69ef9abec33ef0d808724ce80af037710
    refs/remotes/origin/fix/freeze-checker-sign-repair        0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b
    refs/remotes/origin/fix/branch-deletion-policy-amendment  1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e
    refs/remotes/origin/fix/branch-deletion-policy            f2da41aedc5d3b48cb9d228494272a945fada971

Local `main`, reported separately and **not repaired**:

    refs/heads/main                                           0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**Every A1 value matched. No STOP.** Both merges were performed against
`refs/remotes/origin/*` immediately after the fetch, never against a
local branch ref.

## 2. The specification's structural claims, verified independently

The specification states these as dry-run results. I re-derived each
before merging rather than inheriting them.

**Stage 1 is an ancestor of Branch B — two merges, not three.**

    $ git merge-base --is-ancestor f2da41ae… 1c106372…      exit 0

So merging Branch B brings `fix/branch-deletion-policy` with it, and a
separate merge would have integrated nothing. It was not merged
separately.

**Neither source contains the other.**

    $ git merge-base --is-ancestor 0ab0ca9d… 1c106372…      exit 1
    $ git merge-base --is-ancestor 1c106372… 0ab0ca9d…      exit 1

**All three merge-bases are the original base.**

    merge-base(base, A) = 236f71c69ef9abec33ef0d808724ce80af037710
    merge-base(base, B) = 236f71c69ef9abec33ef0d808724ce80af037710
    merge-base(A,    B) = 236f71c69ef9abec33ef0d808724ce80af037710

**The changed-path sets are disjoint.**

    Branch A (5 paths)                          Branch B (7 paths)
    A derivations/…_checker_sign_repair.md      M DECISION_LOG.md
    A reports/…1424Z_freeze-checker-…md         M docs/BRANCHING_POLICY.md
    M scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
                                                A docs/BRANCH_DELETION_RECORD_2026-08-07.md
    A specs/…1424Z_freeze-checker-…md           A reports/…1437Z_branch-deletion-policy.md
    M tests/test_p2_grassmann_crossing_sign.py  A reports/…1508Z_…amendment.md
                                                A specs/…1437Z_branch-deletion-policy.md
                                                A specs/…1508Z_…amendment.md

    overlap count: 0

5 + 7 = 12 arriving operations: **8 additions and 4 modifications**, as
the specification states.

**`DECISION_LOG.md` arrives only from Branch B.**

    $ git diff --name-only 236f71c6… 0ab0ca9d… -- DECISION_LOG.md
    (no output)

Branch A does not touch it. §5 shows the merged blob equal to Branch B's.

## 3. A2 — merge parentage, as distinct values

**Merge A** — `f62fc89a1ba6d6786ee00cdabd2a17d80b801bc0`

    parent 1    cf427532090a8059fca7710a35e5f379f4823cf2   the integration spec commit (commit 1)
    parent 2    0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b   Branch A tip
    merge-base  236f71c69ef9abec33ef0d808724ce80af037710   the ORIGINAL base

**Merge B** — `d9638f1095cdd7d0eaca9557910113612f6e3006`

    parent 1    f62fc89a1ba6d6786ee00cdabd2a17d80b801bc0   the Merge-A commit
    parent 2    1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e   Branch B tip
    merge-base  236f71c69ef9abec33ef0d808724ce80af037710   the ORIGINAL base

The two merge commits are distinct objects. Parent 1 in each case was
fixed by the commit being stood on, not selected: commit 1 for Merge A,
Merge A for Merge B. Merge B's merge-base is the original base and
**not** the Merge-A commit, because Branch B was cut from the same base
and does not contain Merge A.

Both merges used `--no-ff` and both produced a real merge commit with
exactly two parents. Neither reported a conflict:

    Merge made by the 'ort' strategy.
     …5 files changed, 1331 insertions(+), 2 deletions(-)     [Merge A]
     …7 files changed, 2165 insertions(+)                     [Merge B]

    $ git status --porcelain=v1     (after each merge)
    (empty)

## 4. A3 — guards

### 4.1 `PRE_MERGE(A)`, at the spec commit, before Merge A

    {
      "checks": [
        {
          "condition": "worktree_clean",
          "entries": [],
          "status": "PASS"
        },
        {
          "attachment": "fix/integrate-freeze-repair-and-deletion-policy",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "cf427532090a8059fca7710a35e5f379f4823cf2",
          "status": "PASS",
          "worktree_head": "cf427532090a8059fca7710a35e5f379f4823cf2"
        },
        {
          "actual": "236f71c69ef9abec33ef0d808724ce80af037710",
          "condition": "merge_base",
          "expected": "236f71c69ef9abec33ef0d808724ce80af037710",
          "status": "PASS"
        },
        {
          "condition": "scope",
          "evidence": {
            "base": "236f71c69ef9abec33ef0d808724ce80af037710",
            "failures": [],
            "head": "0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b",
            "mode": "exact",
            "observed_operations": [
              {"operation": "add", "path": "derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md"},
              {"operation": "add", "path": "reports/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
              {"operation": "modify", "path": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"},
              {"operation": "add", "path": "specs/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
              {"operation": "modify", "path": "tests/test_p2_grassmann_crossing_sign.py"}
            ],
            "overall": "PASS",
            "tool": "scope_checker"
          },
          "status": "PASS"
        },
        {
          "condition": "pinned_artifacts",
          "evidence": [
            {"actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS"},
            {"actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json", "status": "PASS"},
            {"actual": "40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606",
             "expected": "40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606",
             "path": "scripts/P2-CHANNEL-FREEZE/vocab_parser.py", "status": "PASS"},
            {"actual": "4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0",
             "expected": "4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0",
             "path": "tests/test_channel_freeze_mutations.py", "status": "PASS"}
          ],
          "status": "PASS"
        }
      ],
      "mode": "PRE_MERGE",
      "other_registered_worktrees": [
        "/home/user/2-emergent-gravity                                    cf4c789 [gate/p2-grassmann-crossing-sign]",
        "…/scratchpad/fixA    0ab0ca9 [fix/freeze-checker-sign-repair]",
        "…/scratchpad/fixB    f2da41a [fix/branch-deletion-policy]",
        "…/scratchpad/fixC    1c10637 [fix/branch-deletion-policy-amendment]",
        "…/scratchpad/integ   9609677 [integration/role-model-clean]",
        "…/scratchpad/integ2  236f71c [gate/p2-integrate-fierz-and-sign-ruling]",
        "…/scratchpad/integ3  cf42753 [fix/integrate-freeze-repair-and-deletion-policy]"
      ],
      "overall": "PASS",
      "tool": "merge_guard"
    }
    === exit 0 ===

The `other_registered_worktrees` paths are abbreviated above for width;
§8 states the worktree inventory in full.

### 4.2 `PRE_MERGE(B)`, at the Merge-A commit, before Merge B

Same four pinned artifacts, all `PASS`. Check summary:

    overall: PASS
      worktree_clean                    -> PASS
      worktree_matches_declared_target  -> PASS   (head f62fc89a…, the Merge-A commit)
      merge_base                        -> PASS   (236f71c6…, the ORIGINAL base)
      scope                             -> PASS   (base 236f71c6… head 1c106372…)
      pinned_artifacts                  -> PASS
    === exit 0 ===

    observed_operations:
      add    docs/BRANCH_DELETION_RECORD_2026-08-07.md
      add    reports/2026-08-07T1437Z_branch-deletion-policy.md
      add    reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md
      add    specs/2026-08-07T1437Z_branch-deletion-policy.md
      add    specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md
      modify DECISION_LOG.md
      modify docs/BRANCHING_POLICY.md

### 4.3 The final `POST_MERGE` — intended parameters

**The two roles are representable separately, so no stop arose.**
`merge_guard.post_merge` takes `merge_commit` and `expected_remote_sha`
as independent config keys; the first drives the parentage and merge-base
checks, the second drives `remote_agreement`. Intended parameters:

    mode                  POST_MERGE
    merge_commit          d9638f1095cdd7d0eaca9557910113612f6e3006   <- the MERGE OBJECT under verification (Merge B)
    expected_parent_1     f62fc89a1ba6d6786ee00cdabd2a17d80b801bc0
    expected_parent_2     1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e
    expected_merge_base   236f71c69ef9abec33ef0d808724ce80af037710
    remote_check_policy   REQUIRED
    expected_remote_ref   refs/remotes/origin/main
    expected_remote_sha   <the final REPORT-commit head>              <- a DIFFERENT SHA from merge_commit
    scope_manifest        the A4 manifest below, head = final head
    pinned_artifacts      the same four as the PRE_MERGE guards

`merge_commit` is a merge object; `expected_remote_sha` is the report
commit that will be `main`'s tip. They are different commits and are
supplied to different keys. The executed guard is post-report evidence.

## 5. A5–A8 — content checks at the merged head

### 5.1 A5 — protected paths, blob-identical base vs merged head

Read from the objects, not the worktree:

    GATES.md                                            bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                      2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml                                      9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md   0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json         5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf   IDENTICAL
    scripts/P2-CHANNEL-FREEZE/vocab_parser.py           20800bc649924fd0629b3232615dae4c4fac36a7   IDENTICAL
    tests/test_channel_freeze_mutations.py              d938e2c4d2ca460c344fe1cda4a713794f7fd0c0   IDENTICAL
    tests/test_channel_freeze_phase_a.py                cce7be76b667b2a1bb7a5e0169325603419dda63   IDENTICAL

### 5.2 A6 — arriving content intact, blob-compared against the source tips

From Branch A @ `0ab0ca9d…`:

    derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md    f53707dff3ee43be16c7428fc31494b352249eed   IDENTICAL
    reports/2026-08-07T1424Z_freeze-checker-sign-repair.md     482c5c440f4a80fc6ce627dc6c29eb17ced0c6bc   IDENTICAL
    specs/2026-08-07T1424Z_freeze-checker-sign-repair.md       080c8c1b22265b109b094641c573e2d8ab9c57a4   IDENTICAL
    scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py            8be4f5de8a3b08230835c55a24ff3b95dfc5196b   IDENTICAL
    tests/test_p2_grassmann_crossing_sign.py                   8b8bcc6f506c1591bca6e96883eda9112714c025   IDENTICAL

From Branch B @ `1c106372…`:

    docs/BRANCH_DELETION_RECORD_2026-08-07.md                    c91126d39d79b6c9441414553b1ed8503bc81d2e   IDENTICAL
    reports/2026-08-07T1437Z_branch-deletion-policy.md           69dfbe54fcc3d8f7a66102690dab285839d7ef02   IDENTICAL
    reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md a02652a654ed348a3d6a2a6748d91342fd6fdc1c   IDENTICAL
    specs/2026-08-07T1437Z_branch-deletion-policy.md             b1a86c227c29563b884617445014df608644c010   IDENTICAL
    specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md   439faabcebdce47e54c8d74a96d18ac973b26731   IDENTICAL
    docs/BRANCHING_POLICY.md                                     3fad8856b0d64bce4b119429890867e97ff910d4   IDENTICAL
    DECISION_LOG.md                                              0bc14ab020464c8dad56cdd6785914a8fa445992   IDENTICAL

All eight arriving additions present; all four arriving modifications
byte-identical to their source. **Nothing arriving by merge was edited.**

### 5.3 A8 — `DECISION_LOG.md` blob-identical to Branch B

    base     c9cc8a8084f4645905f3660f738d63bc943c4ee5
    Branch A c9cc8a8084f4645905f3660f738d63bc943c4ee5   <- equal to base: Branch A never touched it
    Branch B 0bc14ab020464c8dad56cdd6785914a8fa445992
    merged   0bc14ab020464c8dad56cdd6785914a8fa445992   <- equal to Branch B

**The question of append ordering does not arise**, because only one
branch appended. The specification's own correction of an earlier draft
— which had inferred that both branches appended — is confirmed against
the objects here.

`docs/BRANCH_DELETION_RECORD_2026-08-07.md` at the merged head is
`c91126d3…`, blob-identical to Branch B (§5.2). **Every recorded tip
survives verbatim.** No merge resolution touched it.

### 5.4 A7 — no gate changed

    GATES.md base vs merged head                        IDENTICAL (bd482051…)
    '^## P2-' count at base                             14
    '^## P2-' count at merged head                      14
    P2-PHASE-01                                         Status: PROPOSED

This integration changes validation machinery and branch policy. **No
gate, gate status, verdict, digest or hash-pinned artifact was
modified.**

## 6. A4 — scope

### 6.1 Manifest template

Held with a `{PUSHED_HEAD}` placeholder so its digest does not depend on
the report commit. SHA-256:
`a01c35b18163dc64b411e5cbc7051698a175531ea0e6c569d6e0b94fc1f16b40`.

    {
      "base": "236f71c69ef9abec33ef0d808724ce80af037710",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md"},
        {"operation": "add", "path": "docs/BRANCH_DELETION_RECORD_2026-08-07.md"},
        {"operation": "add", "path": "reports/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
        {"operation": "add", "path": "reports/2026-08-07T1437Z_branch-deletion-policy.md"},
        {"operation": "add", "path": "reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md"},
        {"operation": "add", "path": "reports/2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md"},
        {"operation": "add", "path": "specs/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
        {"operation": "add", "path": "specs/2026-08-07T1437Z_branch-deletion-policy.md"},
        {"operation": "add", "path": "specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md"},
        {"operation": "add", "path": "specs/2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"},
        {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"},
        {"operation": "modify", "path": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"},
        {"operation": "modify", "path": "tests/test_p2_grassmann_crossing_sign.py"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**10 additions + 4 modifications = 14 operations**, matching A4. The
`{HHMM}` token resolved to `2158` at commit 1 and is reused throughout.
There is no fifteenth path.

### 6.2 Observed at the pre-report head

At `d9638f10…` the report commit does not yet exist, so **9 additions**
appear rather than 10:

    M	DECISION_LOG.md
    A	derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md
    M	docs/BRANCHING_POLICY.md
    A	docs/BRANCH_DELETION_RECORD_2026-08-07.md
    A	reports/2026-08-07T1424Z_freeze-checker-sign-repair.md
    A	reports/2026-08-07T1437Z_branch-deletion-policy.md
    A	reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md
    M	scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
    A	specs/2026-08-07T1424Z_freeze-checker-sign-repair.md
    A	specs/2026-08-07T1437Z_branch-deletion-policy.md
    A	specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md
    A	specs/2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md
    M	tests/test_p2_grassmann_crossing_sign.py

    additions: 9   modifications: 4

9 arriving-plus-spec additions + the report = 10. The authoritative
14-operation check at the pushed head is post-report evidence.

## 7. A9-pre — nine validators, at head `d9638f10`

    $ python -m pytest tests/test_repository_structure.py            ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py                  -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py                    -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py                ->  8 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_scalar_exploratory.py   ->  5 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py     -> 14 passed              exit 0
    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py      -> 19 passed              exit 0
    $ python -m pytest tests/test_channel_freeze_phase_a.py          ->  3 passed              exit 0
    $ python -m pytest tests/test_channel_freeze_mutations.py        -> 18 passed              exit 0

All nine exit 0. Exit statuses were captured from `python -m pytest`
itself, not from the tail of a pipeline.

**Both freeze suites pass unchanged — the regression evidence for the
checker edit.** `test_channel_freeze_phase_a.py` (3) and
`test_channel_freeze_mutations.py` (18) are blob-identical to the base
(§5.1) and both still pass against the edited
`basis_freeze_check.py`. The `matrix` mutation in particular still
rejects with `computed Fierz matrix mismatch`, so the equality assertion
the edit touched remains live and discriminating.

`tests/test_p2_grassmann_crossing_sign.py` runs 19 tests, up from 15 at
the base: the four operator-layer tests Branch A added.

`pytest` on `PATH` is 9.0.2 and `python -m pytest` is 9.1.1 in this
environment; the specification mandates `python -m pytest`, which is
what was run.

## 8. Worktree states, stated separately

**The merge worktree** —
`…/scratchpad/integ3`, attached to
`fix/integrate-freeze-repair-and-deletion-policy`, at
`d9638f1095cdd7d0eaca9557910113612f6e3006`.
`git status --porcelain=v1` empty after both merges. All merging and all
checks in this report were performed here.

**The main worktree** — `/home/user/2-emergent-gravity`, attached to
`gate/p2-grassmann-crossing-sign` at `cf4c789`. **It was not touched by
this task** beyond read-only `fetch` and `ls-remote`; `git status
--porcelain=v1` reported 0 entries before the work began and its
attachment is unchanged. Local `main` was not checked out, fast-forwarded
or repaired.

**Five other registered worktrees**, none altered, none cleaned, none
stashed, all reporting 0 dirty entries at the start of this task:

    …/scratchpad/fixA    0ab0ca9  [fix/freeze-checker-sign-repair]
    …/scratchpad/fixB    f2da41a  [fix/branch-deletion-policy]
    …/scratchpad/fixC    1c10637  [fix/branch-deletion-policy-amendment]
    …/scratchpad/integ   9609677  [integration/role-model-clean]
    …/scratchpad/integ2  236f71c  [gate/p2-integrate-fierz-and-sign-ruling]

## 9. A11 — branches preserved; nothing deleted

Read from the remote at the pre-report head:

    fix/freeze-checker-sign-repair              0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b   as pinned
    fix/branch-deletion-policy-amendment        1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e   as pinned
    fix/branch-deletion-policy                  f2da41aedc5d3b48cb9d228494272a945fada971   as pinned
    review/role-model-and-executors             10c260b96882ac12610f78840aeeabd07be2d7cb   untouched

    remote branch count                          30   (unchanged by this task)

**No branch was deleted or renamed**, including the two now merged.
Deleting them is Stage 2's business, under the record and controls that
this integration merely lands.

**Stage 2 is NOT authorized by this integration**, and landing it does
not make Stage 2 ready to run. The policy prerequisite is satisfied; the
execution controls are not written. Per §0 of the authority, a Stage-2
specification must add at least: three-valued handling of
`git merge-base --is-ancestor` exit codes, with anything `>= 2` a STOP
rather than a mapping to `verified_merged: false`; and a
re-enumeration of the live remote branch set at Stage-2 time, including
`unexpected_remote_branches`.

**The `DECLARED_CROSSING_SIGN` gap is not closed here.**
`scripts/p2_grassmann_crossing_sign.py` still carries the literal and
still never reads `grassmann_crossing_sign` from the freeze, so a flip of
the freeze field reaches no comparison anywhere. That file was not
touched by this task. It is a separate task.

## 10. Stops and clarifications

**Stops: none.** No A1 ref mismatched, no merge conflicted, no guard
returned `FAIL`, and the `POST_MERGE` guard proved able to carry the
merge object and the remote head as distinct values — so A3's stop
condition did not arise.

**Finding 1 — `OBSERVATION_METHOD_ERROR`, mine, caught immediately and
before any state changed.** My first `PRE_MERGE(A)` invocation passed
`--mode PRE_MERGE` on the command line. `merge_guard.py` takes `--repo`
and `--config` only and reads `mode` from inside the config JSON, so
argparse rejected it with exit 2 and printed a usage error. **No guard
result was produced, and nothing was merged on the strength of it.** I
moved `mode` into the config and re-ran; the guard then returned
`overall: PASS` with exit 0. Recorded because a tool-invocation error
that yields no output is easy to mistake for a governance failure — or,
worse, to wave through — and the exit code alone (2) does not
distinguish the two.

**Finding 2 — secondary, carried forward, not this task's to fix.** The
`DECLARED_CROSSING_SIGN` gap of §9. Reported here so the integration
record does not read as though the coverage were complete.

**Finding 3 — secondary, carried forward.** The Stage-1 deletion record
now integrated states `unexpected_remote_branches 1`. That count was
correct when taken and is now stale: three unlisted branches sit on the
remote, all from this authorized sequence of tasks. The record is a
snapshot and was deliberately left unedited; Stage 2 must re-enumerate.
This is already recorded inside the arriving reports and is repeated
here because a reader arriving at `main` sees the record before the
report.

**Clarification 1 — where commit 1 sits in §2's sequence.** §2 lists ten
steps and does not name the specification commit; §4 requires it as
commit 1 and A2 requires it to be parent 1 of Merge A. I took it as part
of step 1 — create the branch, land the spec — which is the only
placement satisfying both. No inconsistency, just an unlisted step.

**Clarification 2 — which ref was merged.** §5 requires merging the
pinned remote refs rather than local copies. I merged
`refs/remotes/origin/<branch>` immediately after `git fetch --prune`,
having first confirmed each equals both its `git ls-remote` value and
its pinned SHA. Merging the bare SHA would have been equally pinned but
would have produced a less legible merge; the message names the branch
and its tip explicitly in either case.

## 11. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A11 were met as written, and the
specification's structural claims all held on independent re-derivation.

**(a) I would state the guard's calling convention once.** `mode` living
inside the config file rather than on the command line is the one thing
in this toolchain that is not guessable from the CLI surface, and it
cost me a failed invocation. A single line in the specification — or a
`--mode` alias in `merge_guard.py` — removes the trap. I am not
proposing the code change here; it is out of scope.

**(b) §2's step list and §4's commit order should be one list.**
Clarification 1. Two orderings that must be interleaved to be executed
invite exactly the parent-1 defect that an earlier integration
specification in this programme actually contained. This one is
self-consistent, but the interleaving is left to the reader.

**(c) A4 says "a fifteenth path is a defect" but not what to do about
it.** Every other criterion with a failure mode names the response —
STOP, report, skip. Here I would have stopped, but the criterion does
not say so. It did not arise: the count is exactly 14.

One thing I would keep exactly as written: **the correction in the
preamble**, recording that an earlier draft had asserted both branches
appended to `DECISION_LOG.md` and that this was inferred rather than
checked. Carrying a retracted claim in the authority document — rather
than quietly fixing it — is what let me verify the corrected version
against the objects instead of taking it on trust, and §5.3 is the
result.

## 12. Commits, and commit-message hygiene

Commits 1–3, at the pre-report head. The report commit's SHA is
necessarily absent from the report it commits; its intended message is
given below and its stored message is read back as post-report evidence.

**Commit 1** — `cf427532090a8059fca7710a35e5f379f4823cf2`

    spec: integrate the freeze-checker repair and the branch-deletion policy

    Records the PI integration authorization, evidence base
    236f71c69ef9abec33ef0d808724ce80af037710, transcribed verbatim.

    Two merges, not three: fix/branch-deletion-policy is an ancestor of
    fix/branch-deletion-policy-amendment, so merging the amendment brings
    Stage 1 with it and a separate merge would integrate nothing. The two
    sources have disjoint changed-path sets and DECISION_LOG.md arrives only
    from Branch B.

    The specification also records what this integration does not close: the
    operator-layer consumer still hardcodes its declared crossing sign, so a
    flip of the freeze field reaches no comparison; and Stage 2 of the
    deletion task remains unauthorized pending two further execution
    controls.

**Commit 2 (Merge A)** — `f62fc89a1ba6d6786ee00cdabd2a17d80b801bc0`

    merge: integrate the freeze-checker sign repair (reviewed; pinned 0ab0ca9)

    Integrates fix/freeze-checker-sign-repair at
    0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b into the integration branch.

    Five operations, all reviewed: the task specification, the derivation
    note, the execution report, the checker edit and the extended operator-
    layer test file.

    basis_freeze_check.py now applies the Grassmann crossing sign zero
    times. It previously applied it twice around a transposition, which
    cancelled to the identity for either declared value. matrix_rational is
    stored unsigned and s_G is applied once at operator use, so the correct
    count inside this checker is zero; applying it once would leave the
    reconstruction an overall -1 from the frozen table. computed_fierz is
    unchanged by the edit, equal in all 25 entries as exact rationals, and
    parse_grassmann_sign still runs so a malformed value is still rejected.

    The freeze, its data artifacts, vocab_parser.py and the mutation suite
    are byte-identical to the base. No grassmann entry was added to
    MUTATIONS: the checker is correctly blind to that field, so such an
    entry would assert a rejection that must not happen.

**Commit 3 (Merge B)** — `d9638f1095cdd7d0eaca9557910113612f6e3006`

    merge: integrate the branch-deletion policy and its amendment (reviewed; pinned 1c10637)

    Integrates fix/branch-deletion-policy-amendment at
    1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e into the integration branch.
    That branch contains fix/branch-deletion-policy at
    f2da41aedc5d3b48cb9d228494272a945fada971 as an ancestor, so Stage 1
    arrives with it; merging Stage 1 separately would have integrated
    nothing and added a misleading merge commit.

    Seven operations, all reviewed: two task specifications, two execution
    reports, the deletion record, and edits to BRANCHING_POLICY.md and
    DECISION_LOG.md.

    BRANCHING_POLICY.md gains a branch lifecycle, a three-state
    authorization machine with a closed count identity, and a rule making
    git ls-remote the sole deletion authority.
    BRANCH_DELETION_RECORD_2026-08-07.md is the pre-deletion authorization
    record: 26 entries, 25 PENDING_DELETE, one ABSENT_FROM_REMOTE, identity
    25 + 0 + 1 = 26.

    Nothing is deleted by this merge. Stage 2 remains unauthorized: it needs
    a specification adding three-valued ancestry exit handling and a
    re-enumeration of the live remote branch set. review/role-model-and-
    executors is permanently preserved and appears in no deletion set.

    Branch B was cut from the same base as Branch A and does not contain
    merge A, so the merge-base of this merge is the original base and not
    the merge-A commit.

**Intended report commit message** (commit 4):

    docs: report the integration of the freeze repair and the deletion policy

    Records A1-A3, A5-A8, A9-pre and A10 for the two merges, with both
    merge commits' parents and merge-bases as distinct values, both
    PRE_MERGE guard results, and the intended final manifest and POST_MERGE
    parameters.

    DECISION_LOG.md at the merged head is blob-identical to Branch B, which
    is also blob-identical to the base on Branch A: only one branch
    appended, so no ordering question arises. The deletion record survives
    verbatim, GATES.md is unchanged at 14 P2 gates, and both freeze suites
    pass unchanged against the edited checker.

    Nothing is deleted and Stage 2 stays unauthorized. Records one
    tool-invocation error of mine, caught before any merge.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this
branch — **including both merge commits** — by composing each message in
a file and passing it with `-F`, never `-m`, and never through a path
that would append them.

    commit 1  cf427532   spec       suppressed: Co-Authored-By, Claude-Session
    commit 2  f62fc89a   MERGE A    suppressed: Co-Authored-By, Claude-Session
    commit 3  d9638f10   MERGE B    suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)              suppression applied identically; stored
                                    message read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` returned no match on either the proposed or the
stored form, for all three commits. **No trailer appeared despite
inspection, so A10's pre-push STOP did not trigger.**

**Suppression is a fact disclosed here, not an absence.** The trailers
were not merely missing; a convention that would have added them was
deliberately bypassed, and the merge commits — where an auto-generated
message would ordinarily be accepted with `--no-edit` — were given
authored messages by file for exactly this reason.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
They are noted so the Reviewer is not surprised by them.
