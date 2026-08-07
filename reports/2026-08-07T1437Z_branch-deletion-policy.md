# Execution report — branch-deletion policy, Stage 1

Authority: `specs/2026-08-07T1437Z_branch-deletion-policy.md`
Evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`
Branch: `fix/branch-deletion-policy`
Classification: MATERIAL, and partly irreversible — **but nothing
irreversible happens in Stage 1.**

**No branch was deleted, renamed or force-pushed by this task.** Stage 1
lands the policy and the pre-deletion authorization record and then
stops. Stage 2 is not authorized until this work is merged into `main`.

Written at head `bc78be054c0a6f93a8433fff5598619b6f9c9fcc`; it does not
contain its own commit SHA or the final branch head.

---

## 1. A1 — the policy landed

Appended to `docs/BRANCHING_POLICY.md` as a new **Branch lifecycle**
section, in the file's existing style. The file previously said nothing
about deletion — it enumerated prefixes and stopped at
"Paper branches may update `.tex` only after reviewer acceptance."

    ## Branch lifecycle

    A branch may be deleted only after its content is merged into `main`.
    Deletion is subject to:

    - **Merged, tip recoverable as a merge parent** — may be deleted. The
      content, grouping and tip SHA survive in the merge commit.
    - **Merged, tip NOT a merge parent** — may be deleted **only after its
      tip SHA is recorded** in a committed deletion record. Without that,
      the ref is the sole pointer to the tip.
    - **Unmerged** — deletion destroys content, not merely a name. It
      requires an explicit PI decision naming the branch.
    - **Explicitly preserved** — never deleted, regardless of merge state.

    "Merged" here means a verified ancestor check against `main`, not a
    loose human label.

    **Every deletion is recorded, in two committed steps.**

    **Before deletion**, a committed AUTHORIZATION RECORD preserves each
    branch's name, tip SHA and, where one exists, the merge commit that
    integrated it, with `deletion_status: PENDING_DELETE` or
    `NOT_AUTHORIZED`. It is merged before any deletion, so that a failure
    during deletion cannot leave an unrecorded loss.

    **After deletion**, the same record is FINALIZED: each entry becomes
    `DELETED` or `SKIPPED`, with the reason for every skip. **A permanent
    record of what was intended to be deleted is not a record of what was
    deleted**, and for an irreversible operation the repository must carry
    the outcome, not only the intent.

    `NOT_AUTHORIZED` is terminal. Such an entry never enters the deletion
    step and is never rewritten; it stays in the record so that what was
    considered, and why it was not deleted, remains visible.

    **Permanently preserved:**
    `review/role-model-and-executors` @
    `10c260b96882ac12610f78840aeeabd07be2d7cb` — the unmerged record of a
    commit-metadata defect, retained as negative-provenance evidence.

    The current record is `docs/BRANCH_DELETION_RECORD_2026-08-07.md`.

Two sentences were added beyond the supplied text, both clarifying and
neither weakening: the sentence defining "merged" as a verified ancestor
check (which §0 of the specification requires — *"'Merged branch' as a
loose human label is not sufficient grounds; the ancestor check is"*),
and the sentence making `NOT_AUTHORIZED`'s terminality explicit in the
policy rather than only in the record. The four lifecycle cases, the
record-before-delete rule and the preserved branch with its SHA are
present verbatim.

## 2. A2 — the authorization record

Landed at `docs/BRANCH_DELETION_RECORD_2026-08-07.md`. **Every value was
computed from the repository and the live remote; none was copied from
the specification.** Method:

- tips: `git ls-remote origin refs/heads/<name>` — the live remote, not a
  local tracking ref. This matters: local `run/p2-betav-arm-p-decisive`
  is stale at `0f796174`, while the remote carries `48c5cc59`. The
  recorded value is the remote one.
- merge status: `git merge-base --is-ancestor <tip> 236f71c6…`, per
  branch, exit status read directly.
- merge commits: every parent of every merge commit reachable from
  `main` was enumerated and indexed, then each tip looked up in that
  index. **Parent position was not assumed to be 2** — see §5.

### The record, quoted in full

| branch_name | recorded_tip | merge_commit | verified_merged | deletion_status |
| --- | --- | --- | --- | --- |
| `claude/paper-2-independent-verification-dysdp0` | `5395d4b3f5c1d81dc9954f484802d9f534009dc1` | `720abccd30b8cb0f41be40eb6c061c69bff9eada` | true | `PENDING_DELETE` |
| `concepts/p2-dual-pipeline` | `9ee30ab3b5e6c368df147664de6fc25f8fdf2e7e` | `8d48798eaa3884a0a5104d5dc19e2e836468f1aa` | true | `PENDING_DELETE` |
| `docs/canonical-interaction` | `78872798c7f638434996f190450af3223b9cfedf` | `d51fea326ceea6a3748791b3f17a8a8a1562ca89` | true | `PENDING_DELETE` |
| `explore/p2-phase-01-scalar` | `a2ed2af813a4c33c2b56ea98d8706f07ef375c10` | `a3fc1532df7903b32bb33bd815f3b567dbc7d13d` | true | `PENDING_DELETE` |
| `gate/p2-betav-campaign-prereg` | `21efcf857d6f686be32af405c861d51116ae2baa` | `a686bf3a9d2269da750a04403f0bb815c72280df` | true | `PENDING_DELETE` |
| `gate/p2-betav-circ` | `ca334fe0361d76fadb68e1866f71f0c40a4ed858` | `30062c4cace7918173d7f44a558fb84a37392b57` | true | `PENDING_DELETE` |
| `gate/p2-betav-cleanup` | `602569db064a2c679fca45157932fda29217982c` | `fd5f6b967644f8866c7f4188fd10bd68e604ce18` | true | `PENDING_DELETE` |
| `gate/p2-betav-decomp` | `05a1e7f81eb814f0bb3e438e95e261aa07900031` | `4c70628fce287c97e5144cf3a65d37a866b72e63` | true | `PENDING_DELETE` |
| `gate/p2-channel-freeze` | `47e271bbf1a73b6d3f2fc779c1ffcd024abaa80b` | `e045aa5c6c4353ee539fa902b41ca8dffd3f3686` | true | `PENDING_DELETE` |
| `gate/p2-governance-amendment` | `d63f33b9df723a3a53c13a5126f85c47ffb77d30` | `d8ca67d80a8ac84e489a4c3532f214b45e705483` | true | `PENDING_DELETE` |
| `gate/p2-grassmann-crossing-sign` | `cf4c78959c0caf6bfed7c80f9451b6a3337972fe` | `81fd2f965c520be9791c61ab7a677b9343aeb70d` | true | `PENDING_DELETE` |
| `gate/p2-integrate-fierz-and-sign-ruling` | `236f71c69ef9abec33ef0d808724ce80af037710` | `NOT PRESENT ON REMOTE` | n/a | `NOT_AUTHORIZED` |
| `gate/p2-lattice-ontology-01` | `edb08c2a6244c330614d98b0b824db9dfe8d873f` | `de05e9e3f8e0ea9f74e37831342d98b8232edc0b` | true | `PENDING_DELETE` |
| `gate/p2-phase-01-fierz-and-branch-depths` | `dca522690b00ae6bc9b706492b09d7c60d7efc51` | `b9ca22ea448825347e4cd45b1a92b1b62e6b9ab4` | true | `PENDING_DELETE` |
| `gate/p2-si1-unblock` | `c1f1bec27085335b077dbdd26cb460f994acffd6` | `dc4ab9e7dfb21ddb0428d688bb257f2178da7f0a` | true | `PENDING_DELETE` |
| `governance/adopt-rules-8-12` | `75c84226cf39f552545d953606a11df104244a03` | `3302b612b954af6369fc01a2e9a85cfb4f682a07` | true | `PENDING_DELETE` |
| `governance/execution-environment-refinements` | `99aaa0e2c7dbd3a151241b464693e0ad80ee75d9` | `9f41dbe5340d1822bb9f5fa33bd495b528e8a841` | true | `PENDING_DELETE` |
| `governance/p2-phase-dependency-ruling` | `d69bc0f788df52d30f2954c118bc23578c046bb4` | `86a04cc32d603b3b1ea0c8619c57f2de204508e6` | true | `PENDING_DELETE` |
| `governance/rules-8-12-tools` | `376ec62f014703178ba8744f425608ff8c5802c5` | `1e8d56da124c2ae791fb7a00b23a188d329c56f8` | true | `PENDING_DELETE` |
| `recover/batch2-gfvec-and-foundations` | `324ef969476dd1c7488055971a3ed47dadf21767` | `1ff42fd86b1e51d27a2e7cece319f0546ea25505` | true | `PENDING_DELETE` |
| `recover/betav-complete` | `836bf1441603565ba8d07207f31fabee8f04e5fc` | `2bacfd09683d92152b71cddc6dcfba56c95b3c46` | true | `PENDING_DELETE` |
| `recover/lattice-gravity-engine` | `cdcbd840df8252d59ecfd29e662a797adc7216f9` | `d37974c5a201b785880c4a7fd4f131db4e381aad` | true | `PENDING_DELETE` |
| `review/role-model-and-executors-clean` | `6fee7ed48e6e09ef50d7deb51d11bf4ce895620e` | `9609677576b6d0d77a0813c93673aed81b0c4d5f` | true | `PENDING_DELETE` |
| `run/p2-betav-arm-h-decisive` | `9b0ceedf820d65d4f7b2bbeea7df043c88d8e72a` | `3c0c484dcac68f203b5dcae25d58245b759549d3` | true | `PENDING_DELETE` |
| `run/p2-betav-arm-p-decisive` | `48c5cc59f81b148da66cb4366199b59987e53a2a` | `8b64b895cac1e1c9b4e8f600449c15ce1ffc66c7` | true | `PENDING_DELETE` |
| `sea-ice/gate-stubs` | `b02c70279b382e05d415b23b9b5f562e3c5e2156` | `e21f81ea7f750c71fcfe2734ab86423cadf91b17` | true | `PENDING_DELETE` |

26 entries. The table in the committed record is byte-identical to the
generated one, verified by `diff`.

### Counts

    listed_count               26
    currently_present_count    25
    verified_merged_count      25
    not_merged_count            0
    pending_delete_count       25
    unexpected_remote_branches  1

`pending_delete_count == verified_merged_count` — 25 = 25, as A2
requires.

**No branch on the A2 list was found unmerged.** The specification asks
for "any branch you found NOT merged, with evidence"; the answer is
**none**. Every one of the 25 present branches returned exit 0 from
`git merge-base --is-ancestor <tip> 236f71c6…`.

**`not_merged_count` is 0 while one entry is `NOT_AUTHORIZED`.** These
are different numbers on purpose, and §3 explains why. Flagging it here
so the discrepancy is visible rather than buried, which is what A2 asks
these counts to do.

## 3. The two inventory discrepancies

The specification instructs that every name be treated "as a claim to
check against the live remote, not as a fact". Both directions produced a
discrepancy.

### 3.1 Listed but absent — `gate/p2-integrate-fierz-and-sign-ruling`

    $ git ls-remote origin refs/heads/gate/p2-integrate-fierz-and-sign-ruling
    (no output)

It was created locally during the 2026-08-07 integration task and never
pushed; that integration reached `main` by advancing `main` itself. Its
local ref resolves to `236f71c69ef9abec33ef0d808724ce80af037710`, which
**is** `main`, so no content is at risk under any outcome.

**Recorded as `NOT_AUTHORIZED`, with `verified_merged: n/a`.** The
reasoning is in §7, Stop 1: the specification's state machine has no
state for "listed but absent from the remote", and both available
literal readings are wrong. `n/a` + `NOT_AUTHORIZED` authorizes nothing,
which is the safe direction for an irreversible task.

### 3.2 On the remote but not listed — `fix/freeze-checker-sign-repair`

    fix/freeze-checker-sign-repair @ 0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b
    ancestor of main: false

**I created this branch myself**, earlier on 2026-08-07, executing
`specs/2026-08-07T1424Z_freeze-checker-sign-repair.md`. It was pushed
after this specification was written, which is why the A2 list does not
contain it. It is unmerged and awaiting its own result review.

Per §2 of the specification — *"If the remote carries a branch not on
this list, do not delete it: report it and stop the Stage-2 deletion for
that branch only"* — it is **not in the record**, is reported here and in
the record's counts, and **must not be deleted in Stage 2**.

This is worth stating plainly: the inventory drifted between
specification and execution because of my own action in an adjacent
task. That is exactly the drift the "treat every name as a claim" rule
exists to catch, and it caught it.

## 4. Live remote inventory

    $ git fetch --prune origin        (exit 0)
    $ git ls-remote --heads origin

    5395d4b3f5c1d81dc9954f484802d9f534009dc1  claude/paper-2-independent-verification-dysdp0
    9ee30ab3b5e6c368df147664de6fc25f8fdf2e7e  concepts/p2-dual-pipeline
    78872798c7f638434996f190450af3223b9cfedf  docs/canonical-interaction
    a2ed2af813a4c33c2b56ea98d8706f07ef375c10  explore/p2-phase-01-scalar
    0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b  fix/freeze-checker-sign-repair
    21efcf857d6f686be32af405c861d51116ae2baa  gate/p2-betav-campaign-prereg
    ca334fe0361d76fadb68e1866f71f0c40a4ed858  gate/p2-betav-circ
    602569db064a2c679fca45157932fda29217982c  gate/p2-betav-cleanup
    05a1e7f81eb814f0bb3e438e95e261aa07900031  gate/p2-betav-decomp
    47e271bbf1a73b6d3f2fc779c1ffcd024abaa80b  gate/p2-channel-freeze
    d63f33b9df723a3a53c13a5126f85c47ffb77d30  gate/p2-governance-amendment
    cf4c78959c0caf6bfed7c80f9451b6a3337972fe  gate/p2-grassmann-crossing-sign
    edb08c2a6244c330614d98b0b824db9dfe8d873f  gate/p2-lattice-ontology-01
    dca522690b00ae6bc9b706492b09d7c60d7efc51  gate/p2-phase-01-fierz-and-branch-depths
    c1f1bec27085335b077dbdd26cb460f994acffd6  gate/p2-si1-unblock
    75c84226cf39f552545d953606a11df104244a03  governance/adopt-rules-8-12
    99aaa0e2c7dbd3a151241b464693e0ad80ee75d9  governance/execution-environment-refinements
    d69bc0f788df52d30f2954c118bc23578c046bb4  governance/p2-phase-dependency-ruling
    376ec62f014703178ba8744f425608ff8c5802c5  governance/rules-8-12-tools
    236f71c69ef9abec33ef0d808724ce80af037710  main
    324ef969476dd1c7488055971a3ed47dadf21767  recover/batch2-gfvec-and-foundations
    836bf1441603565ba8d07207f31fabee8f04e5fc  recover/betav-complete
    cdcbd840df8252d59ecfd29e662a797adc7216f9  recover/lattice-gravity-engine
    10c260b96882ac12610f78840aeeabd07be2d7cb  review/role-model-and-executors
    6fee7ed48e6e09ef50d7deb51d11bf4ce895620e  review/role-model-and-executors-clean
    9b0ceedf820d65d4f7b2bbeea7df043c88d8e72a  run/p2-betav-arm-h-decisive
    48c5cc59f81b148da66cb4366199b59987e53a2a  run/p2-betav-arm-p-decisive
    b02c70279b382e05d415b23b9b5f562e3c5e2156  sea-ice/gate-stubs

28 remote branches = 26 in the deletion set as observed + `main` +
`review/role-model-and-executors`.

**The preserved branch, verified at the start of Stage 1:**

    review/role-model-and-executors  10c260b96882ac12610f78840aeeabd07be2d7cb   as expected

It is verified again at the end of this task (§10), and A6 requires it be
verified first **and last** around the Stage-2 deletion loop.

## 5. Structural facts, re-established rather than inherited

§0 requires these be re-established by me, not taken from the
specification.

**Merge subjects pin their source tips.** `main` carries **27** merge
commits (`git rev-list --merges 236f71c6… | wc -l`). Examples:

    81fd2f9  merge: integrate the Grassmann crossing-sign ratification (reviewed; pinned cf4c789)
    b9ca22e  merge: integrate the P2-PHASE-01 Fierz verification and branch depths (reviewed; pinned dca5226)
    9609677  merge: adopt the function-based role model and the dual-executor record (reviewed; pinned 6fee7ed)
    a3fc153  merge: integrate P2-PHASE-01 scalar exploratory study (reviewed; pinned a2ed2af)
    86bb394  merge: integrate P2-PHASE-01 ruling and execution-environment governance refinements (reviewed; pinned d69bc0f, 99aaa0e)

and their bodies repeat the tip in full, e.g. `81fd2f9`: *"Integrates
gate/p2-grassmann-crossing-sign at
cf4c78959c0caf6bfed7c80f9451b6a3337972fe into the integration branch."*

**Most tips are second parents; one is not.** Of the 25 recorded,
remote-present tips, **24 are second parents** of a merge commit on
`main`. The exception is
`governance/execution-environment-refinements` @ `99aaa0e`, which is the
**first** parent of `9f41dbe5340d1822bb9f5fa33bd495b528e8a841` — it
reached `main` through an intermediate combining merge
(`9f41dbe`, *"merge: combine phase dependency ruling with
execution-environment refinements"*), itself the second parent of
`86bb394`.

**A correction to my own method, recorded because it changed a value.**
My first pass indexed only `<merge>^2` and consequently reported
`governance/execution-environment-refinements` as `NOT A MERGE PARENT`.
That was an `OBSERVATION_METHOD_ERROR`: the specification's phrase "most
merged branch tips are second parents … and at least one is not" is about
parent *position*, and I let it narrow my query. Re-running over all
parents (`<merge>^@`) found it as parent 1. **The record carries the
corrected value**, `9f41dbe5…`. Had the error survived, the record would
have overstated the risk of deleting that branch.

**Consequently, no entry in this set is "merged but not a merge
parent".** All 25 fall in the first lifecycle case. The second case is
still stated in the policy because a future branch may fall into it —
a fast-forward or a rebase-merge would produce exactly that.

## 6. A9–A12

### 6.1 A10 — nothing else touched

    GATES.md        bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md  2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md       5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml  9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL

    $ git diff --name-status 236f71c6… HEAD -- scripts/ derivations/ results/ tests/
    (no output)
    changed-path count in those trees: 0

Checked at the tree level as well, which is stronger than a path diff —
a directory tree OID covers every path beneath it:

    scripts/      a84e1e2548114ae8e10dcf299bcaa8e522e33787   IDENTICAL
    derivations/  2b71991cdbbedc037679e8b64dff403987d67179   IDENTICAL
    results/      ccc39de0e06ecaf108b62cee0afaf715a47172e0   IDENTICAL
    tests/        620b23db969d17111772c3ee5b87a8f5556de8f4   IDENTICAL

    $ git diff --name-status 236f71c6… HEAD
    M	DECISION_LOG.md
    M	docs/BRANCHING_POLICY.md
    A	docs/BRANCH_DELETION_RECORD_2026-08-07.md
    A	specs/2026-08-07T1437Z_branch-deletion-policy.md

### 6.2 A9 — scope manifest template

Held with a `{PUSHED_HEAD}` placeholder so its digest does not depend on
the report commit. SHA-256:
`e65bbf7285ec779e2b5c2a5734a9134fb3d4d8b1bf57bf5a076c33ae76241aec`.

    {
      "base": "236f71c69ef9abec33ef0d808724ce80af037710",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-07T1437Z_branch-deletion-policy.md"},
        {"operation": "add", "path": "docs/BRANCH_DELETION_RECORD_2026-08-07.md"},
        {"operation": "add", "path": "reports/2026-08-07T1437Z_branch-deletion-policy.md"},
        {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Three additions and two modifications, matching A9. The resolved
manifest, its SHA-256 and the checker JSON at the pushed head are
post-report evidence.

Pre-report check at `bc78be05`, where the report commit does not yet
exist, so four operations rather than five:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "236f71c69ef9abec33ef0d808724ce80af037710",
      "failures": [],
      "head": "bc78be054c0a6f93a8433fff5598619b6f9c9fcc",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "DECISION_LOG.md"
        },
        {
          "operation": "modify",
          "path": "docs/BRANCHING_POLICY.md"
        },
        {
          "operation": "add",
          "path": "docs/BRANCH_DELETION_RECORD_2026-08-07.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-07T1437Z_branch-deletion-policy.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` empty; no forbidden operation — in particular no `delete`,
which for this task is the criterion that matters most.

### 6.3 A11-pre — four validators, at head `bc78be05`

    $ python -m pytest tests/test_repository_structure.py   ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py         -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py           -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py       ->  8 passed              exit 0

Exit statuses were captured from `python -m pytest` itself, not from the
tail of a pipeline. A11-final at the pushed head is post-report evidence
and carries the verdict.

### 6.4 A12 — branch only

    refs/remotes/origin/main   236f71c69ef9abec33ef0d808724ce80af037710
    remote refs/heads/main     236f71c69ef9abec33ef0d808724ce80af037710
    local main                 0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)

`fix/branch-deletion-policy` was created from
`236f71c69ef9abec33ef0d808724ce80af037710` in a separate worktree. No
`main` ref was moved. **No branch was deleted or renamed.** No merge, no
PR, no force-push, no history rewrite.

## 7. Stops and clarifications

**Stop 1 — `SPECIFICATION_DEFECT`.** The state machine in §2 is
described as "closed and has exactly these transitions", but it has **no
state for a listed branch that is absent from the remote**. Both literal
readings are wrong:

- `verified_merged: true` (its local ref equals `main`, so the ancestor
  relation holds trivially) forces `PENDING_DELETE`, which would send
  Stage 2 to delete a branch that does not exist;
- `verified_merged: false` asserts something untrue about its ancestry,
  and the specification defines that state as "not merged", which it is
  not.

**Resolution used, and why I did not halt Stage 1 over it.** The entry
is recorded with `verified_merged: n/a` and
`deletion_status: NOT_AUTHORIZED`, with the reason stated in the record.
This authorizes nothing and cannot cause an irreversible action; the
conservative direction is available and unambiguous. Halting would have
delivered nothing while the branch in question is one whose local ref
equals `main` and whose deletion is impossible anyway. **A PI ruling is
requested before Stage 2** on whether `n/a` is the intended encoding or
whether a distinct state such as `ABSENT` should be added to the policy.

Stage 2 is in any case gated on this work being merged and reviewed, so
the ruling has a natural place to land and nothing is blocked by
deferring it.

**Stop 2 — none.** No other condition triggered a stop.

**Finding 1 — `OBSERVATION_METHOD_ERROR`, mine, self-caught and
corrected.** My first inventory pass indexed only second parents of
merges and therefore recorded
`governance/execution-environment-refinements` as
`NOT A MERGE PARENT`. Re-running over all parents showed it is parent 1
of `9f41dbe5…`. **The committed record carries the corrected value**, and
§5 states the correction rather than hiding it. The error would have
been conservative in effect — it would have placed the branch in the
stricter lifecycle case — but it was still a false statement about the
repository, and for a record whose purpose is to survive an irreversible
act, a false entry is the wrong kind of mistake to leave in.

**Finding 2 — secondary, mine, disclosed.** The unexpected remote branch
`fix/freeze-checker-sign-repair` is one I pushed earlier the same day
under a separate specification. It is reported, excluded from the
record, and must not be deleted. See §3.2.

**Finding 3 — secondary, observational.** Local `main` is stale at
`0f796174` and local `run/p2-betav-arm-p-decisive` is stale at
`0f796174` while the remote carries `48c5cc59`. All recorded tips were
therefore read from `git ls-remote`, never from local refs. Local `main`
was not repaired, as instructed. **If Stage 2 is ever run from local
refs rather than the remote, it will act on wrong values** — that is a
concrete hazard for the next stage, not a defect here.

**Clarification 1 — which `main` the ancestor checks used.** Remote
`refs/heads/main` = `236f71c6…`, which equals the evidence base and
`refs/remotes/origin/main`. Local `main` was not used for any check.

**Clarification 2 — two sentences added to the supplied policy text.**
Recorded in §1, both clarifying, neither weakening. If the PI wants the
supplied text verbatim with nothing added, that is a one-line change.

## 8. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** All Stage-1 criteria — A1, A2, A3, A9,
A10, A11, A12 — were met as written, with the single encoding gap of
Stop 1.

Three things I would have specified differently:

**(a) The state machine needs an `ABSENT` state.** §2 calls it "closed",
and closedness is the property being relied on for an irreversible
operation. It is not closed: a listed branch may simply not exist on the
remote, which is neither "merged" nor "not merged". This is the only
real defect I found, and it appeared on the very first inventory.

**(b) `not_merged_count` and the count of `NOT_AUTHORIZED` entries are
conflated.** §2 annotates `not_merged_count` with `(-> NOT_AUTHORIZED)`,
implying they are the same number. Here they are 0 and 1. The counts are
meant to make discrepancies visible, so I would add
`not_authorized_count` as its own line rather than leave a reader to
infer the difference.

**(c) A2 says "one entry per branch in the deletion set" without saying
whether an absent branch is in the set.** Related to (a): the deletion
set is defined as "every branch currently on the remote EXCEPT…", which
by its own terms excludes an absent branch — yet the explicit name list
includes one. I kept the entry, because a record documenting what was
considered is more useful than silence, and because dropping it would
have hidden the discrepancy. Stating the precedence would settle it.

One thing I would keep exactly as written: **the three-stage boundary
with the record merged before deletion**, and the instruction to verify
the preserved branch **first and last**. The value of that ordering is
visible already — the inventory drifted between specification and
execution in both directions within a single day, and a record written
before the act is the only thing that makes such drift auditable
afterwards.

## 9. Commits, and commit-message hygiene

**Commit 1** — `2a99442e25e97cdfa08a0f2adb5e1cd057a66b47`

    spec: adopt a branch-deletion policy and clean up merged branches

    Records the PI specification for the branch-deletion programme, evidence
    base 236f71c69ef9abec33ef0d808724ce80af037710, transcribed verbatim.

    Three stages with hard boundaries: Stage 1 lands the policy and the
    pre-deletion authorization record; Stage 2 deletes only after Stage 1 is
    merged into main; Stage 3 finalizes the record with what was actually
    deleted. This commit belongs to Stage 1, which stops after review.

    review/role-model-and-executors is permanently preserved: it is
    unmerged, so deleting it would destroy content rather than a name.

**Commit 2** — `bc78be054c0a6f93a8433fff5598619b6f9c9fcc`

    docs: adopt a branch lifecycle policy and record the deletion set

    Stage 1 of three. Nothing is deleted here.

    BRANCHING_POLICY.md gains a Branch lifecycle section: four cases, the
    rule that every deletion is recorded in two committed steps, and the
    permanently preserved branch with its SHA.

    BRANCH_DELETION_RECORD_2026-08-07.md is the pre-deletion authorization
    record: 26 listed branches, 25 present on the remote and all 25 verified
    as ancestors of main, giving 25 PENDING_DELETE entries. All values were
    computed from the repository and the live remote. The one NOT_AUTHORIZED
    entry, gate/p2-integrate-fierz-and-sign-ruling, is absent from the
    remote and so has nothing to delete; its local ref equals main.

    One remote branch is outside the set, fix/freeze-checker-sign-repair,
    pushed after the specification was written; it is recorded as
    unexpected and must not be deleted.

**Intended report commit message** (commit 3):

    docs: report Stage 1 of the branch-deletion policy

    Records A1-A3 and A9-A12 for the policy adoption and the pre-deletion
    authorization record, with the record quoted in full, the policy text
    quoted, the live remote inventory, and the counts.

    Reports two inventory discrepancies against the specification's name
    list: gate/p2-integrate-fierz-and-sign-ruling is absent from the remote,
    and fix/freeze-checker-sign-repair is present but unlisted. Reports one
    specification defect, the missing state for a listed-but-absent branch,
    and one observation-method error of mine, corrected in the record.

    Stage 1 stops here. Stage 2 is not authorized until this is merged.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers. This specification permits neither. Both were
**actively suppressed** on every commit of this branch by composing the
message in a file and committing with `git commit -F`, never with `-m`.

    commit 1  2a99442e   suppressed: Co-Authored-By, Claude-Session
    commit 2  bc78be05   suppressed: Co-Authored-By, Claude-Session
    commit 3  (report)   suppression applied identically; stored message
                         read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` matched nothing in either form, for both commits.

**Suppression is a fact disclosed here, not an absence** — a convention
that would have added the trailers was deliberately bypassed.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.

## 10. Stage 1 ends here

**Stage 2 is not authorized.** It runs only after this branch is merged
into `main`, and it must re-verify each branch at deletion time rather
than trusting this record.

The preserved branch, verified again at the end of Stage 1:

    review/role-model-and-executors  10c260b96882ac12610f78840aeeabd07be2d7cb

unchanged from the check at the start of §4. **No deletion loop has run,
and none is authorized by this report.**
