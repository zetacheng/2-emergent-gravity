# Task report — integrate both `P2-PHASE-01` derivation branches and record the Fierz sign ruling

Function: Executor
Date: 2026-08-07
Task classification: MATERIAL
Executor: Claude Code (sandboxed container)

Authority: `specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md`

**Two source branches integrated by `--no-ff` merges, one PI ruling
recorded, one addendum added. Nothing else on `main` changes.** No gate,
gate status, verdict, digest or hash-pinned artifact is modified;
`P2-PHASE-01` and `P2-CHANNEL-FREEZE-01` both remain `PROPOSED`.

---

## 1. A1 — refs, verified before anything was created

```text
  refs/remotes/origin/main                       9609677576b6d0d77a0813c93673aed81b0c4d5f
  remote refs/heads/main (ls-remote)             9609677576b6d0d77a0813c93673aed81b0c4d5f
  local main (stale by design)                   0f7961747abe2a18b436c0b1e5b928f425ea4d9a
  Branch A local                                 dca522690b00ae6bc9b706492b09d7c60d7efc51
  Branch A remote                                dca522690b00ae6bc9b706492b09d7c60d7efc51
  Branch B local                                 cf4c78959c0caf6bfed7c80f9451b6a3337972fe
  Branch B remote                                cf4c78959c0caf6bfed7c80f9451b6a3337972fe
```

**Local `main` is stale by design and was neither fast-forwarded nor
repaired.**

## 2. Commit identities

| Item | Value |
| --- | --- |
| Integration branch | `gate/p2-integrate-fierz-and-sign-ruling` |
| Base | `9609677576b6d0d77a0813c93673aed81b0c4d5f` |
| Commit 1 — specification | `80c411497971881a4ee3ad7f380feef367c8479c` |
| Commit 2 — merge of Branch A | `b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4` |
| Commit 3 — merge of Branch B | `81fd2f965c520be9791c61ab7a677b9343aeb70d` |
| Commit 4 — DECISION_LOG + addendum | `4e5d43270ecf01338bb3b8e67edef33bd320c291` |
| Pre-report head (step 7) | `4e5d43270ecf01338bb3b8e67edef33bd320c291` |
| UTC token `{HHMM}` | `1320`, observed `2026-08-07T13:20:55Z` |

### A2 — merge parentage, as distinct values

```text
Merge A  = b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4
  parent 1            = 80c411497971881a4ee3ad7f380feef367c8479c   (the integration specification commit)
  parent 2            = dca522690b00ae6bc9b706492b09d7c60d7efc51   (Branch A)
  merge-base(p1,p2)   = 9609677576b6d0d77a0813c93673aed81b0c4d5f
  parents (raw %P)    = 80c411497971881a4ee3ad7f380feef367c8479c dca522690b00ae6bc9b706492b09d7c60d7efc51

Merge B  = 81fd2f965c520be9791c61ab7a677b9343aeb70d
  parent 1            = b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4   (the merge-A commit)
  parent 2            = cf4c78959c0caf6bfed7c80f9451b6a3337972fe   (Branch B)
  merge-base(p1,p2)   = 9609677576b6d0d77a0813c93673aed81b0c4d5f
  parents (raw %P)    = b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4 cf4c78959c0caf6bfed7c80f9451b6a3337972fe

  merge-base(A, B)    = 9609677576b6d0d77a0813c93673aed81b0c4d5f   (independent branches)
```

**Both merge-bases are the original base**, and they are distinct from
the parents. Merge A's first parent is the specification commit — not
the base — because parent 1 is fixed by the commit one is standing on,
and §4's commit order places the authorization document before the
merges it authorizes. **Merge B's merge-base is the original base, not
the merge-A commit**, because Branch B was cut from the base and does not
contain merge A.

### A10 — commit-message hygiene, per commit

Every proposed message was inspected before its commit and every stored
message read back from the commit object afterwards. **On all four
commits — including both merge commits — two trailers were suppressed at
authoring time**: a `Co-Authored-By:` line and a `Claude-Session:` URL
line that this executor's harness convention would otherwise append.
**The suppression is a fact to disclose, not an absence.**

| commit | stored-message trailer scan |
| --- | --- |
| 1 `80c4114` | 0 hits |
| 2 `b9ca22e` (merge A) | 0 hits |
| 3 `81fd2f9` (merge B) | 0 hits |
| 4 `4e5d432` | 0 hits |

Scanned terms: `co-authored-by`, `claude-session`, `session_`,
`claude.ai`, `generated with`, `signed-off-by`.

Stored messages:

```text
--- commit 1 ---
specs: record the integration and Fierz sign-ruling authority

Commits the PI specification authorizing integration of both
P2-PHASE-01 derivation branches into main, together with the PI ruling
of 2026-08-07 on the Fierz matrix sign convention.

The specification exists in the branch history before the merges it
authorizes, which is why it is commit 1 and why merge A's first parent
is this commit rather than the base. The merge-base is unaffected and
remains the original base for both merges.

Nothing arriving by merge is edited. The freeze repair is a separate
authorized task and is not performed here.
--- commit 2 (merge A) ---
merge: integrate the P2-PHASE-01 Fierz verification and branch depths (reviewed; pinned dca5226)

Integrates gate/p2-phase-01-fierz-and-branch-depths at
dca522690b00ae6bc9b706492b09d7c60d7efc51 into the integration branch.

Six additions, all reviewed: the task specification, the derivation
note, the production script, the machine-readable results artifact, a
new test file, and the execution report. Nothing pre-existing is
touched; GATES.md, CONVENTIONS.md, AGENTS.md, pyproject.toml, the
Phase-A freeze and its checker are byte-identical to the base.

P2-PHASE-01 remains PROPOSED. No gate is registered, no status changed,
no prerequisite draft adopted, and no admissibility verdict reached.
--- commit 3 (merge B) ---
merge: integrate the Grassmann crossing-sign ratification (reviewed; pinned cf4c789)

Integrates gate/p2-grassmann-crossing-sign at
cf4c78959c0caf6bfed7c80f9451b6a3337972fe into the integration branch.

Six additions, all reviewed: the task specification, the derivation
note, the script, the results artifact, a new test file, and the
execution report. The branch establishes the operator-level Grassmann
exchange sign s_G = -1 by explicit four-fermion calculation and reports
the matrix storage convention as unresolved on the frozen material.

Branch B was cut from the same base as Branch A and does not contain
merge A, so the merge-base of this merge is the original base and not
the merge-A commit.

Nothing pre-existing is touched. The freeze, its checker and the
mutation suite are byte-identical to the base.
--- commit 4 ---
governance: record the Fierz sign ruling and its consequence

Adds the DECISION_LOG entry for the PI ruling of 2026-08-07 on the Fierz
matrix sign convention, and an addendum recording what that ruling means
for results already committed.

The ruling supplies a definition the frozen material never carried; it
does not recover an original intent. No defining kernel equation exists
anywhere in the freeze, and the ruling rests on indirect evidence only.
That distinction is stated in both records.

Consequence: the P2-PHASE-01 induced V and A coefficients are -G/4 at
the operator level, the matrix-level +G/4 values acquiring s_G = -1
exactly once. The structural results are unaffected.

Neither source branch's report or derivation note is altered. The freeze
repair is a separate authorized task and is not performed here.
```

### Intended report commit message

```text
docs: report the integration of both P2-PHASE-01 branches and the sign ruling

Records A1-A7, A9-pre and A10 for commits 1-4, both PRE_MERGE guard
JSONs verbatim, the merge parentage as distinct values, and the
DECISION_LOG entry and addendum as committed.

The final POST_MERGE guard, A8-final, A9-final, the push and this
commit's own stored message are post-report evidence by construction and
are deliberately absent here.
```

---

## 3. Guards

### 3.1 `PRE_MERGE(A)` — verbatim

```json
{
  "checks": [
    {
      "condition": "worktree_clean",
      "entries": [],
      "status": "PASS"
    },
    {
      "attachment": "gate/p2-integrate-fierz-and-sign-ruling",
      "condition": "worktree_matches_declared_target",
      "expected_worktree_head": "80c411497971881a4ee3ad7f380feef367c8479c",
      "status": "PASS",
      "worktree_head": "80c411497971881a4ee3ad7f380feef367c8479c"
    },
    {
      "actual": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
      "condition": "merge_base",
      "expected": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
      "status": "PASS"
    },
    {
      "condition": "scope",
      "evidence": {
        "base": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
        "failures": [],
        "head": "dca522690b00ae6bc9b706492b09d7c60d7efc51",
        "mode": "exact",
        "observed_operations": [
          {
            "operation": "add",
            "path": "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md"
          },
          {
            "operation": "add",
            "path": "reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md"
          },
          {
            "operation": "add",
            "path": "results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json"
          },
          {
            "operation": "add",
            "path": "scripts/p2_phase01_fierz_and_depths.py"
          },
          {
            "operation": "add",
            "path": "specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md"
          },
          {
            "operation": "add",
            "path": "tests/test_p2_phase01_fierz_and_depths.py"
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
          "actual": "1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c",
          "expected": "1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c",
          "path": "derivations/P2-LATTICE-ONTOLOGY-01.md",
          "status": "PASS"
        },
        {
          "actual": "30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78",
          "expected": "30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78",
          "path": "scripts/euclidean_reconstruction.py",
          "status": "PASS"
        },
        {
          "actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
          "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
          "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
          "status": "PASS"
        },
        {
          "actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
          "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
          "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
          "status": "PASS"
        }
      ],
      "status": "PASS"
    }
  ],
  "mode": "PRE_MERGE",
  "other_registered_worktrees": [
    "/home/user/2-emergent-gravity                                                                       cf4c789 [gate/p2-grassmann-crossing-sign]",
    "/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ   9609677 [integration/role-model-clean]",
    "/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2  80c4114 [gate/p2-integrate-fierz-and-sign-ruling]"
  ],
  "overall": "PASS",
  "tool": "merge_guard"
}
```

exit status 0.

### 3.2 `PRE_MERGE(B)` — verbatim

```json
{
  "checks": [
    {
      "condition": "worktree_clean",
      "entries": [],
      "status": "PASS"
    },
    {
      "attachment": "gate/p2-integrate-fierz-and-sign-ruling",
      "condition": "worktree_matches_declared_target",
      "expected_worktree_head": "b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4",
      "status": "PASS",
      "worktree_head": "b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4"
    },
    {
      "actual": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
      "condition": "merge_base",
      "expected": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
      "status": "PASS"
    },
    {
      "condition": "scope",
      "evidence": {
        "base": "9609677576b6d0d77a0813c93673aed81b0c4d5f",
        "failures": [],
        "head": "cf4c78959c0caf6bfed7c80f9451b6a3337972fe",
        "mode": "exact",
        "observed_operations": [
          {
            "operation": "add",
            "path": "derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md"
          },
          {
            "operation": "add",
            "path": "reports/2026-08-07T1159Z_grassmann-crossing-sign.md"
          },
          {
            "operation": "add",
            "path": "results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json"
          },
          {
            "operation": "add",
            "path": "scripts/p2_grassmann_crossing_sign.py"
          },
          {
            "operation": "add",
            "path": "specs/2026-08-07T1159Z_grassmann-crossing-sign.md"
          },
          {
            "operation": "add",
            "path": "tests/test_p2_grassmann_crossing_sign.py"
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
          "actual": "1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c",
          "expected": "1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c",
          "path": "derivations/P2-LATTICE-ONTOLOGY-01.md",
          "status": "PASS"
        },
        {
          "actual": "30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78",
          "expected": "30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78",
          "path": "scripts/euclidean_reconstruction.py",
          "status": "PASS"
        },
        {
          "actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
          "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
          "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
          "status": "PASS"
        },
        {
          "actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
          "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
          "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
          "status": "PASS"
        }
      ],
      "status": "PASS"
    }
  ],
  "mode": "PRE_MERGE",
  "other_registered_worktrees": [
    "/home/user/2-emergent-gravity                                                                       cf4c789 [gate/p2-grassmann-crossing-sign]",
    "/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ   9609677 [integration/role-model-clean]",
    "/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2  b9ca22e [gate/p2-integrate-fierz-and-sign-ruling]"
  ],
  "overall": "PASS",
  "tool": "merge_guard"
}
```

exit status 0.

### 3.3 The merges themselves

Both merges used `git merge --no-ff --no-commit` against the **pinned
remote refs**, then `git commit -F`. Both reported
`Automatic merge went well; stopped before committing as requested`, and
`git ls-files --unmerged` was **empty** in each case. **No conflict
occurred**, as the disjoint path sets predicted; none was pre-authorized
and none had to be resolved.

### 3.4 Intended final `POST_MERGE` parameters

**The final guard is post-report evidence by construction** — it runs
after the push, which runs after this commit. Its output is therefore
not here. The parameters it will be given are:

```text
mode                 : POST_MERGE
merge_commit         : 81fd2f965c520be9791c61ab7a677b9343aeb70d      <- the MERGE OBJECT under verification (merge B)
expected_parent_1    : b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4
expected_parent_2    : cf4c78959c0caf6bfed7c80f9451b6a3337972fe
expected_merge_base  : 9609677576b6d0d77a0813c93673aed81b0c4d5f
scope_manifest       : the frozen A8 manifest, head = the report commit
remote_check_policy  : REQUIRED
expected_remote_ref  : refs/remotes/origin/main
expected_remote_sha  : the report commit   <- REMOTE AGREEMENT target, the FINAL HEAD
pinned_artifacts     : the four A6 pins
```

**The two SHAs are deliberately distinct and the guard represents them
separately**, so no substitution was needed and no stop arose: the
`merge_commit` field takes the merge object whose parentage is being
checked, while `expected_remote_sha` takes the final head that `main`
must agree with. A guard that verified the report commit as though it
were a merge would be checking parentage that does not exist.

---

## 4. A5, A6, A7 — at the unpushed pre-report head

```text
=== A5 — protected paths, blob-identical base -> pre-report head (read from objects) ===
  GATES.md                                                 IDENTICAL  bd4820513217ae7e1c493328dc49536e69b8cfb8
  CONVENTIONS.md                                           IDENTICAL  2d4f735c55a14fdfc5d1031a58698a8ca075fbbd
  AGENTS.md                                                IDENTICAL  5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3
  pyproject.toml                                           IDENTICAL  9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4
  derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md        IDENTICAL  0be773f6a52c759abd23438c66da6b43bca44930
  scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py          IDENTICAL  c26920627eb38e2ef01349f23e3b7b63608278e4
  scripts/P2-CHANNEL-FREEZE/vocab_parser.py                IDENTICAL  20800bc649924fd0629b3232615dae4c4fac36a7
  tests/test_channel_freeze_phase_a.py                     IDENTICAL  cce7be76b667b2a1bb7a5e0169325603419dda63
  tests/test_channel_freeze_mutations.py                   IDENTICAL  d938e2c4d2ca460c344fe1cda4a713794f7fd0c0
  results/P2-CHANNEL-FREEZE/fierz_matrix.json              IDENTICAL  5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8
  results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256       IDENTICAL  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf

=== A5 — tests/ and scripts/ prefixes: only the four source-branch additions ===
$ git diff --name-status --find-renames --find-copies 9609677576b6d0d77a0813c93673aed81b0c4d5f 4e5d43270ecf01338bb3b8e67edef33bd320c291 -- tests/ scripts/
A	scripts/p2_grassmann_crossing_sign.py
A	scripts/p2_phase01_fierz_and_depths.py
A	tests/test_p2_grassmann_crossing_sign.py
A	tests/test_p2_phase01_fierz_and_depths.py
[end — expect exactly 4 A-lines: 2 scripts, 2 tests]

=== A6 — the twelve arriving paths, present at the merged head ===
  derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md        PRESENT
  derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md            PRESENT
  reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md        PRESENT
  reports/2026-08-07T1159Z_grassmann-crossing-sign.md                    PRESENT
  results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json      PRESENT
  results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json   PRESENT
  scripts/p2_phase01_fierz_and_depths.py                                 PRESENT
  scripts/p2_grassmann_crossing_sign.py                                  PRESENT
  specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md          PRESENT
  specs/2026-08-07T1159Z_grassmann-crossing-sign.md                      PRESENT
  tests/test_p2_phase01_fierz_and_depths.py                              PRESENT
  tests/test_p2_grassmann_crossing_sign.py                               PRESENT

=== A6 — the four pinned surviving artifacts, digests at the merged head ===
  MATCH     derivations/P2-LATTICE-ONTOLOGY-01.md
            1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c
  MATCH     scripts/euclidean_reconstruction.py
            30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78
  MATCH     derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
            fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
  MATCH     results/P2-CHANNEL-FREEZE/fierz_matrix.json
            5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

=== A7 — no gate changed ===
  GATES.md blob base : bd4820513217ae7e1c493328dc49536e69b8cfb8
  GATES.md blob head : bd4820513217ae7e1c493328dc49536e69b8cfb8
  identical          : true
  ^## P2- count base : 14
  ^## P2- count head : 14
  P2-PHASE-01 status at head:
    Status: PROPOSED
```

Reading these:

- **A5** — all eleven protected paths are blob-identical between base and
  merged head, read from the objects. Under `tests/` and `scripts/` the
  only changes are the **four** source-branch additions: two scripts and
  two test files. Nothing added, deleted, renamed or type-changed beyond
  them.
- **A6** — all twelve arriving paths are present, and all four pinned
  surviving digests match.
- **A7** — `GATES.md` is blob-identical (`bd482051…`), the `^## P2-`
  count is **14 before and after**, and `P2-PHASE-01` is still
  `PROPOSED`. **This ruling changes a convention, not a gate.**

---

## 5. A3 — the `DECISION_LOG.md` entry, as committed

`DECISION_LOG.md` was extended by a **pure byte-prefix append** of 3,083
bytes; the pre-existing bytes are unchanged. All nine required factual
phrases are present.

```text
## 2026-08-07 — Fierz matrix sign convention: `matrix_rational` is stored unsigned

Date: 2026-08-07
Decision owner: Principal Investigator
Effect: supplies a definition absent from the frozen material

### Decision

The PI ruling of 2026-08-07, reproduced verbatim:

> **PI ruling, 2026-08-07 — Fierz matrix sign convention.**
>
> `matrix_rational` stores the Dirac/internal exchange matrix **without**
> the operator-level Grassmann crossing factor. The four-fermion operator
> exchange is therefore
>
>     K_exch = s_G · M · K_direct,     s_G = -1
>
> The declared `grassmann_crossing_sign` is applied **exactly once at
> operator use**. The existing double application in
> `basis_freeze_check.py` is an ineffective validation and does not
> define the storage convention.

In short: s_G = -1, applied exactly once at operator use;
matrix_rational is stored unsigned; and the
basis_freeze_check.py double application is ineffective validation.

### Reason

Not a recovery of original intent. The executor established that no
defining kernel equation exists anywhere in the frozen material —
`K_exch`, `K_direct`, `defining equation` and `kernel equation` all occur
zero times, verified independently. The ruling rests on three pieces of
indirect evidence — an unsigned reconstruction matches the frozen
entries; the checker's net effect is `+1`; the sign is declared as a
separate convention field — **none of which is a defining equation**. The
ruling therefore supplies a definition the freeze never carried, rather
than recovering one it did. A record claiming otherwise would overstate
the evidence.

### Evidence

`derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md` and
`results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json`
establish the operator-level sign `s_G = -1` by explicit four-fermion
exchange under a frozen permutation, by four independent routes, and
record the storage convention as unresolved on the frozen material.
`reports/2026-08-07T1159Z_grassmann-crossing-sign.md` reports both.

### Consequences

Consequence: P2-PHASE-01 induced V and A coefficients are -G/4 at the
operator level, the singlet values reported as `+G/4` at the matrix level
in `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
acquiring the factor `s_G = -1` exactly once. The structural results are
unaffected: S, P and T vanish; V and A are equal and purely singlet; the
exchanged form is purely left-right with `LL = RR = 0`.

Neither original report was altered. The consequence is recorded in
`derivations/P2-PHASE-01_fierz_sign_addendum.md`.

Freeze repair (tenth mutation, checker correction, vocab_parser pin) is
queued as a separate task and is NOT performed here.

### Related gate

None. This ruling changes a convention, not a gate. `P2-CHANNEL-FREEZE-01`
remains `PROPOSED` and `P2-PHASE-01` remains `PROPOSED`.

### Related branch and files

`gate/p2-integrate-fierz-and-sign-ruling`;
`derivations/P2-PHASE-01_fierz_sign_addendum.md`, `DECISION_LOG.md`,
`specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md`.
```

---

## 6. A4 — the addendum, as committed

`derivations/P2-PHASE-01_fierz_sign_addendum.md`:

```text
# Addendum — the Fierz sign ruling and its consequence for `P2-PHASE-01`

**Kind:** addendum. It records a consequence for results already
committed. It computes nothing new and revises no earlier document.

**Neither original report was altered.** Both are preserved exactly as
written:

- `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
- `reports/2026-08-07T1159Z_grassmann-crossing-sign.md`

They record honestly what was known when each was written. Rewriting
them would destroy that record, which is why this addendum exists
instead.

## 1. The ruling

> **PI ruling, 2026-08-07 — Fierz matrix sign convention.**
>
> `matrix_rational` stores the Dirac/internal exchange matrix **without**
> the operator-level Grassmann crossing factor. The four-fermion operator
> exchange is therefore
>
>     K_exch = s_G · M · K_direct,     s_G = -1
>
> The declared `grassmann_crossing_sign` is applied **exactly once at
> operator use**. The existing double application in
> `basis_freeze_check.py` is an ineffective validation and does not
> define the storage convention.

**The ruling supplies a definition; it does not recover an original
intent.** No defining kernel equation exists anywhere in the frozen
material — `K_exch`, `K_direct`, `defining equation` and
`kernel equation` all occur zero times, verified independently. The
ruling rests on three pieces of indirect evidence, none of which is a
defining equation. `DECISION_LOG.md`, entry dated 2026-08-07, carries
the full record.

## 2. Consequence for the induced V and A coefficients

`reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
reported the induced singlet coefficients

    S: 0     P: 0     V: G/4     A: G/4     T: 0

**These are MATRIX-LEVEL values**, obtained by applying the frozen
`matrix_rational` to the converted coefficient vector. That report
**explicitly left the operator-level sign unresolved**, recording the
placement of `grassmann_crossing_sign` as a first-class finding and
stating that, were the `-1` applied on top, every induced coefficient
would flip while the magnitudes, the vanishing families and the
purely-singlet structure would be unaffected.

**Under this ruling that contingency is discharged.** Applying
`s_G = -1` exactly once at operator use gives the **OPERATOR-LEVEL**
coefficients

    S: 0     P: 0     V: -G/4     A: -G/4     T: 0

The matrix-level values are unchanged; what the ruling fixes is the one
further factor between them and the operator.

## 3. What the sign does not touch

The structural results are **unaffected by the sign**:

- **S, P and T vanish.** A vanishing coefficient is a result, not an
  omission, and no overall factor changes it.
- **V and A are equal and purely singlet.** The traceless induced
  coefficient is exactly zero, which follows from
  `lam(0) = sqrt(2/N) Id_N` and the frozen generator normalisation.
- **The exchanged form is purely left-right**, `LL = RR = 0`, with
  `LR = RL = 2` under the symmetric split. That check is sign-blind by
  construction: an overall sign multiplies all four coefficients
  equally.

Nothing in derivation (b) of the earlier task — the stationary-branch
potential depths — depends on the Fierz sign at all.

## 4. Consequence for the storage question

`reports/2026-08-07T1159Z_grassmann-crossing-sign.md` reported the
matrix storage convention as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, having established that
the frozen material contains no defining kernel equation.

**That question is now closed by ruling rather than by evidence.** The
distinction matters and is preserved here: the frozen material still
contains no defining equation, and the earlier report's finding remains
accurate as a statement about the frozen material. What has changed is
that a definition now exists, supplied by the PI and recorded in
`DECISION_LOG.md`.

The operator-level sign `s_G = -1` was and remains **established by
calculation**, independently of the ruling.

## 5. Out of scope

The freeze repair — a tenth mutation covering `grassmann_crossing_sign`,
correction of the double application in `basis_freeze_check.py`, and
pinning `scripts/P2-CHANNEL-FREEZE/vocab_parser.py` — is queued as a
separate authorized task and is **not** performed here. The Phase-A
freeze, its checker and its mutation suite are byte-identical to the
integration base.

`P2-CHANNEL-FREEZE-01` and `P2-PHASE-01` both remain `PROPOSED`. This
ruling changes a convention, not a gate.
```

**Neither original report was altered**, and both are cited by path in
the addendum itself:
`reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` and
`reports/2026-08-07T1159Z_grassmann-crossing-sign.md`. Their blobs
arrive from the merges exactly as reviewed.

---

## 7. A8 — the frozen manifest, and the intended final scope check

Template, with `head` the only permitted substitution:

```text
base: 9609677576b6d0d77a0813c93673aed81b0c4d5f
head: <computed final head>
mode: exact
add:
  derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
  derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md
  derivations/P2-PHASE-01_fierz_sign_addendum.md
  reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
  reports/2026-08-07T1159Z_grassmann-crossing-sign.md
  results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
  results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
  scripts/p2_phase01_fierz_and_depths.py
  scripts/p2_grassmann_crossing_sign.py
  specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
  specs/2026-08-07T1159Z_grassmann-crossing-sign.md
  specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md
  tests/test_p2_phase01_fierz_and_depths.py
  tests/test_p2_grassmann_crossing_sign.py
modify:
  DECISION_LOG.md
forbidden_operations:
  delete, rename, copy, type_change, unmerged, unknown
```

`{HHMM}` resolves to `1320`, the token of the specification commit.
**Fifteen additions and one modification** — twelve arriving from the two
source branches, three authored here (the integration specification, the
addendum, and this report). **A sixteenth path would be a defect.**

The resolved manifest, its SHA-256 and the checker JSON are post-report
evidence: the manifest's `head` is this report's own commit.

For completeness, the base-to-head change set at the **pre-report** head
is 14 additions and 1 modification — this report is the fifteenth
addition and does not yet exist.

---

## 8. A9-pre — validators at the pre-report head

```text
A9-pre — validators at the pre-report head 4e5d43270ecf01338bb3b8e67edef33bd320c291
$ git rev-parse HEAD
4e5d43270ecf01338bb3b8e67edef33bd320c291
$ git status --porcelain (before)
[end]
$ python --version
Python 3.11.15
$ python -m pytest --version
pytest 9.1.1
----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_repository_structure.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 4 items

tests/test_repository_structure.py ....                                  [100%]

============================== 4 passed in 0.02s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.42 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_si1_governance.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 14 items

tests/test_si1_governance.py ..............                              [100%]

============================== 14 passed in 0.05s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.24 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_gate_anchors.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 20 items / 2 deselected / 18 selected

tests/test_gate_anchors.py ..................                            [100%]

======================= 18 passed, 2 deselected in 6.78s =======================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 7.10 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_governance_tools.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 8 items

tests/test_governance_tools.py ........                                  [100%]

============================== 8 passed in 1.16s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 1.34 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_scalar_exploratory.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 5 items

tests/test_p2_phase01_scalar_exploratory.py .....                        [100%]

============================== 5 passed in 0.19s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.39 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_fierz_and_depths.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 14 items

tests/test_p2_phase01_fierz_and_depths.py ..............                 [100%]

============================== 14 passed in 1.87s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 2.18 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_grassmann_crossing_sign.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 15 items

tests/test_p2_grassmann_crossing_sign.py ...............                 [100%]

============================== 15 passed in 0.31s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.58 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_channel_freeze_phase_a.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 3 items

tests/test_channel_freeze_phase_a.py ...                                 [100%]

============================== 3 passed in 0.44s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.62 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_channel_freeze_mutations.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ibt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/integ2
configfile: pyproject.toml
collected 18 items

tests/test_channel_freeze_mutations.py ..................                [100%]

============================== 18 passed in 1.78s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 2.08 s

$ git status --porcelain (after)
[end]
```

**All nine reached genuine exit 0** with tests collected and run; none
reported "no tests ran". `python -m pytest` throughout, as required,
because `pytest` and `python -m pytest` resolve to different versions on
this host. The two freeze suites are included as regression evidence
that this integration changed no freeze behaviour, and they pass
unchanged.

---

## 9. Worktree states, stated separately

**Integration (merge) worktree** — where every commit and both merges
were made:

```text
path           : <scratch>/integ2
branch         : gate/p2-integrate-fierz-and-sign-ruling
HEAD           : 4e5d43270ecf01338bb3b8e67edef33bd320c291   (pre-report head)
status         : clean
```

**Main worktree** — `/home/user/2-emergent-gravity`. It was **not used
for the integration**. `main` was never checked out there or anywhere
else; the merges were performed entirely in the isolated worktree above.
Its state is reported with the post-commit evidence, after the report
commit moves the branch it is not on.

A third worktree, `<scratch>/integ`, carries the earlier
`integration/role-model-clean` branch and holds no uncommitted content;
it was not touched.

---

## 10. A11 — branches preserved

```text
  gate/p2-phase-01-fierz-and-branch-depths       dca522690b00ae6bc9b706492b09d7c60d7efc51
  gate/p2-grassmann-crossing-sign                cf4c78959c0caf6bfed7c80f9451b6a3337972fe
  review/role-model-and-executors                10c260b96882ac12610f78840aeeabd07be2d7cb
  review/role-model-and-executors-clean          6fee7ed48e6e09ef50d7deb51d11bf4ce895620e
  branches deleted or renamed by this task: none
```

**This task deletes and renames no branch.** Both source branches remain
at their pinned commits, and `review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched — it is
unmerged and deliberately preserved, since deleting it would destroy
content and not merely a name.

---

## 11. Stops and clarifications

**One stop occurred, before any work was done, and it was resolved by PI
ruling.**

### 11.1 `SPECIFICATION_DEFECT` — A2 and §4 were mutually unsatisfiable

The earlier draft required merge A's parent 1 to be the base while §4
required the specification commit to precede merge A on the same branch.
Parent 1 is fixed by the commit one is standing on and is not
selectable, so the two could not both hold. **I stopped before creating
any branch or commit and reported both readings**, noting that A2's
*merge-base* requirement holds under either — only the literal parent-1
SHA distinguished them.

The PI ruled that Reading 1 governs: the commit order stands and merge
A's parent 1 is the specification commit. **The current specification
records that ruling**, and this report's §2 shows the resulting
parentage. Nothing was decided by me.

### 11.2 No other stop

No pinned digest mismatched. No merge conflict occurred. No unauthorized
trailer appeared in any stored message. `main` was not moved, checked out
or repaired.

### 11.3 `ENVIRONMENT` — two pytest versions, nothing installed

`pytest` resolves to 9.0.2 on `PATH`, `python -m pytest` to 9.1.1. The
specification fixes the latter and every run used it. Nothing was
installed and no configuration was changed.

### 11.4 Secondary findings, carried forward and not acted on

- The freeze repair — a tenth mutation covering
  `grassmann_crossing_sign`, correction of the double application in
  `basis_freeze_check.py`, and pinning `vocab_parser.py` — remains
  queued as a separate authorized task and was **not** performed. All
  three files are blob-identical to the base (§4).
- The erroneous `vocabulary.gamma5` entry in
  `derivations/CANONICAL_INTERACTION.json`, ruled on by the PI on
  2026-08-07, remains an open `REPOSITORY_DEFECT` and is out of scope
  here.
- The stale role text in `docs/RESEARCH_WORKFLOW.md`, `README.md` and
  `docs/local/execution_environment.md` remains open.

---

## 12. Ambiguous, unsatisfiable, or what I would have specified differently

- **The A2/§4 defect was worth stopping on, and the specification's own
  design is why it was catchable.** Because A2 stated parents *and*
  merge-bases as separate values, the inconsistency was visible before
  any commit existed rather than after a merge had landed on `main`. **A
  specification that had stated only "merge A onto the base" would have
  hidden it.** The current text's distinction between PARENT and
  MERGE-BASE is the fix and should be kept in future integration
  specifications.
- **Stating the expected path count was the single most useful line in
  A8.** "Fifteen additions and one modification… a sixteenth path is a
  defect" converts a scope check from a judgement into an arithmetic
  one. I would put a count in every `mode: exact` manifest.
- **The two-distinct-SHAs instruction in §2 anticipated a real hazard.**
  The final head is not a merge commit, and a guard given the report
  commit as `merge_commit` would have checked parentage that does not
  exist — silently, since it would simply find no second parent. Naming
  the two roles and requiring a stop if they could not be represented
  separately is the right shape. **The guard does represent them
  separately, so no stop arose.**
- **One asymmetry I would resolve.** A9 says `A9-pre` runs "at the
  pre-push head" while §2 step 7 places it at the pre-report head
  (commit 4). Those differ once the report commit exists. Since the
  report must *carry* A9-pre, only the step-7 reading is executable, and
  that is what I did — but the two sentences should be made to agree.
- **A5's phrasing needed its own clarifying sentence and got one.** "No
  path added… beyond the four source-branch additions in those prefixes"
  plus "the protected-prefix check concerns those prefixes, not the full
  arriving set" is what makes the criterion checkable; without the
  second sentence the twelve arriving paths would appear to violate it.
  Worth keeping as a pattern wherever a prefix check coexists with a
  larger authorized change set.
