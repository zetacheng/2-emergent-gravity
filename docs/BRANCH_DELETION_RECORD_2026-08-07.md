# Branch deletion record — 2026-08-07

**Status: AUTHORIZATION RECORD (pre-deletion). Nothing has been deleted.**

This record exists so that an irreversible operation is preceded by a
permanent statement of what it was to act on. It is committed and merged
into `main` **before** any branch is deleted, so that a failure during
deletion cannot leave an unrecorded loss.

**This is not a record of what was deleted.** Stage 3 finalizes it, after
deletion, by turning each `PENDING_DELETE` into `DELETED` or `SKIPPED`.
Until then, every entry states intent only.

Authority: `specs/2026-08-07T1437Z_branch-deletion-policy.md`
Policy: `docs/BRANCHING_POLICY.md`, "Branch lifecycle"
Evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`
`main` verified against: `236f71c69ef9abec33ef0d808724ce80af037710`
(remote `refs/heads/main` at the time of recording)

All values below were **computed from the repository and the live
remote**, not transcribed from the specification. Tips were read with
`git ls-remote origin refs/heads/<name>`; merge status is a live
`git merge-base --is-ancestor <tip> <main>` check; merge commits were
found by scanning every parent of every merge commit reachable from
`main`.

## Permanently preserved — never deleted

    review/role-model-and-executors @ 10c260b96882ac12610f78840aeeabd07be2d7cb

Unmerged. Deleting it would destroy content, not merely a name. It is
the record of a commit-metadata defect, retained as negative-provenance
evidence. It appears in no deletion set, at any stage.

## Entries

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
| `gate/p2-integrate-fierz-and-sign-ruling` | `236f71c69ef9abec33ef0d808724ce80af037710` | `NOT PRESENT ON REMOTE` | n/a | `ABSENT_FROM_REMOTE` |
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

## The one `ABSENT_FROM_REMOTE` entry, and why

`gate/p2-integrate-fierz-and-sign-ruling` **is not present on the
remote.** It was created locally during the 2026-08-07 integration task
and never pushed; the integration reached `main` by advancing `main`
itself, not by pushing the branch.

Its local ref resolves to `236f71c69ef9abec33ef0d808724ce80af037710`,
which is `main` itself, so no content is at risk under any outcome. It
is `ABSENT_FROM_REMOTE` because **there is no remote ref to delete**,
and Stage 2 deletes remote branches only.

**Its `verified_merged` is recorded as `n/a`, not `true` or `false`.**
Recording `true` would make it `PENDING_DELETE` under the state machine
and send Stage 2 to delete a branch that does not exist; recording
`false` would assert something untrue about its ancestry.

**This entry was first recorded as `NOT_AUTHORIZED`**, because the
policy then in force had no state for "listed but absent from the
remote". That was the conservative reading — it authorized nothing —
but it conflated two different situations. The 2026-08-07 policy
amendment added `ABSENT_FROM_REMOTE` as a distinct terminal state, and
this entry is restated under it. The distinction matters for the future:
a branch absent from the remote may be pushed later and would then be
assessed afresh, whereas a branch that is present but unmerged will not
become deletable by anything happening on the remote. Both remain
terminal for this deletion round, and neither enters Stage 2.

## Counts

    listed_count               26
    currently_present_count    25
    verified_merged_count      25
    not_merged_count            0
    pending_delete_count       25
    unexpected_remote_branches  1

`pending_delete_count` equals `verified_merged_count`, as required.

**`not_merged_count` is 0 while one entry is `ABSENT_FROM_REMOTE`.** The
two are not the same number here, and the discrepancy is deliberate and
explained above: the single `ABSENT_FROM_REMOTE` entry is unauthorized
for absence from the remote, not for being unmerged. **No branch on the
list failed the merge check.**

### Count identity

Under the 2026-08-07 policy amendment the authorization states partition
the listed set, so the counts must add up. Recomputed from the live
remote:

    listed_count               26
    pending_delete_count       25
    not_authorized_count        0
    absent_from_remote_count    1
    25 + 0 + 1 = 26 = listed_count   ✓

The identity is stated as arithmetic rather than as a claim so that a
mis-stated entry shows up as a number that does not add up.

The one unexpected remote branch is `fix/freeze-checker-sign-repair` @
`0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b`, pushed on 2026-08-07 by the
freeze-checker sign-repair task, after this specification was written. It
is not an ancestor of `main` and is awaiting its own review. **It is not
in this record and must not be deleted in Stage 2.**

## Structural facts, re-established from the repository

- `main` carries **27** merge commits. Their subjects pin their source
  tips, for example
  `merge: integrate the Grassmann crossing-sign ratification (reviewed; pinned cf4c789)`,
  and their bodies repeat the tip in full.
- **All 25** recorded, remote-present tips are parents of a merge commit
  on `main`. **24 are second parents**; one,
  `governance/execution-environment-refinements` @ `99aaa0e`, is the
  **first** parent of `9f41dbe5340d1822bb9f5fa33bd495b528e8a841`, having
  reached `main` through an intermediate combining merge rather than
  directly.
- **No recorded tip is unreachable as a merge parent**, so the second
  lifecycle case — merged but not a merge parent — does not arise in this
  set. The policy states it because a future branch may fall into it.

## Stage boundaries

    Stage 1  this record, PENDING_DELETE / NOT_AUTHORIZED   <- current
    Stage 2  deletion, only after Stage 1 is merged into main
    Stage 3  finalization, PENDING_DELETE -> DELETED or SKIPPED

`NOT_AUTHORIZED` is terminal: it never enters Stage 2 and is never
rewritten in Stage 3.
