# Execution report — branch-deletion policy amendment

Authority: `specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md`
Evidence base: `f2da41aedc5d3b48cb9d228494272a945fada971`
(head of `fix/branch-deletion-policy`, Stage 1 as landed)
Branch: `fix/branch-deletion-policy-amendment`
Classification: MATERIAL. Branch only.

**No branch was deleted, and the deletion set is unchanged** at 25
`PENDING_DELETE` entries. This task amends policy and restates one
record entry.

Written at head `6275c21185f3a1c8fd5c32a7572beb64caf974ba`; it does not
contain its own commit SHA or the final branch head.

---

## 1. A2 — the counts, recomputed, and the identity

**Recomputed from the live remote before anything was written.** Method:
`git fetch --prune origin` (exit 0), `main` read as
`git ls-remote origin refs/heads/main` → `236f71c69ef9…`, then per
listed branch an existence test by `git ls-remote origin refs/heads/<b>`
and, where present, `git merge-base --is-ancestor <tip> <main>` with the
**exit code read as three-valued** — 0 ancestor, 1 not ancestor, ≥2
check failed. §5 explains why that third branch matters.

    branch                                           present  anc_exit  verified_merged  state
    claude/paper-2-independent-verification-dysdp0   yes      0         true             PENDING_DELETE
    concepts/p2-dual-pipeline                        yes      0         true             PENDING_DELETE
    docs/canonical-interaction                       yes      0         true             PENDING_DELETE
    explore/p2-phase-01-scalar                       yes      0         true             PENDING_DELETE
    gate/p2-betav-campaign-prereg                    yes      0         true             PENDING_DELETE
    gate/p2-betav-circ                               yes      0         true             PENDING_DELETE
    gate/p2-betav-cleanup                            yes      0         true             PENDING_DELETE
    gate/p2-betav-decomp                             yes      0         true             PENDING_DELETE
    gate/p2-channel-freeze                           yes      0         true             PENDING_DELETE
    gate/p2-governance-amendment                     yes      0         true             PENDING_DELETE
    gate/p2-grassmann-crossing-sign                  yes      0         true             PENDING_DELETE
    gate/p2-integrate-fierz-and-sign-ruling          no       -         n/a              ABSENT_FROM_REMOTE
    gate/p2-lattice-ontology-01                      yes      0         true             PENDING_DELETE
    gate/p2-phase-01-fierz-and-branch-depths         yes      0         true             PENDING_DELETE
    gate/p2-si1-unblock                              yes      0         true             PENDING_DELETE
    governance/adopt-rules-8-12                      yes      0         true             PENDING_DELETE
    governance/execution-environment-refinements     yes      0         true             PENDING_DELETE
    governance/p2-phase-dependency-ruling            yes      0         true             PENDING_DELETE
    governance/rules-8-12-tools                      yes      0         true             PENDING_DELETE
    recover/batch2-gfvec-and-foundations             yes      0         true             PENDING_DELETE
    recover/betav-complete                           yes      0         true             PENDING_DELETE
    recover/lattice-gravity-engine                   yes      0         true             PENDING_DELETE
    review/role-model-and-executors-clean            yes      0         true             PENDING_DELETE
    run/p2-betav-arm-h-decisive                      yes      0         true             PENDING_DELETE
    run/p2-betav-arm-p-decisive                      yes      0         true             PENDING_DELETE
    sea-ice/gate-stubs                               yes      0         true             PENDING_DELETE

    listed_count                26
    pending_delete_count        25
    not_authorized_count         0
    absent_from_remote_count     1
    check_failed_count           0

    identity: 25 + 0 + 1 = 26  vs listed_count 26  -> HOLDS

**My recomputation matches the specification's stated counts exactly, so
no STOP arose.** Nothing changed on the remote between Stage 1 and now
that bears on the deletion set.

A further integrity check, not required but cheap: every one of the 25
recorded tips still equals its live remote value. Only the absent entry
printed:

    gate/p2-integrate-fierz-and-sign-ruling          recorded=236f71c6  live=(absent)

No drift. **The record's tips are still statements of current fact** —
which the amended policy is careful not to assume they will remain.

## 2. A1, A3, A4 — the record diff

Exactly one table row changed, and only in its state column. `git diff`
against the evidence base:

    -| `gate/p2-integrate-fierz-and-sign-ruling` | `236f71c6…037710` | `NOT PRESENT ON REMOTE` | n/a | `NOT_AUTHORIZED` |
    +| `gate/p2-integrate-fierz-and-sign-ruling` | `236f71c6…037710` | `NOT PRESENT ON REMOTE` | n/a | `ABSENT_FROM_REMOTE` |

    added table rows:   1
    removed table rows: 1

`recorded_tip` and `merge_commit` are byte-identical, as A4 requires.
**No other entry, tip, merge commit or state changed.**

The section heading changed from
`## The one NOT_AUTHORIZED entry, and why` to
`## The one ABSENT_FROM_REMOTE entry, and why`. Its explanation of what
happened is **kept in full** — that the branch was created locally
during the integration task and never pushed, that the integration
reached `main` by advancing `main` itself, and that its local ref equals
`main` so no content is at risk. Two sentences describing the old policy
gap were replaced by a paragraph recording that the entry was first
recorded as `NOT_AUTHORIZED`, why that was the conservative reading at
the time, and why the two states are not interchangeable. **Nothing was
deleted that a later reader needs**; the reason the branch was never
pushed survives verbatim.

The count identity was added as a `### Count identity` subsection under
the existing `## Counts`, with its arithmetic shown.

**One further prose change, which I want the Reviewer to rule on.** The
`## Counts` section contained the sentence *"`not_merged_count` is 0
while one entry is `NOT_AUTHORIZED`"*. After the restatement that
sentence is false — no entry is `NOT_AUTHORIZED` any more. I applied a
pure state-name substitution to it, which A1 authorises for prose about
this entry (*"only the state name and the heading change"*) but which
sits in a different section than the one A4 enumerates. **I judged that
leaving a knowingly false sentence in an authorization record was the
worse option**, and that the alternative reading of A4 — freeze that
sentence — would put the record in contradiction with the count identity
A2 requires me to add on the very next line. Flagged rather than assumed;
it is a two-word revert if the Reviewer disagrees.

**A3 — `unexpected_remote_branches` was not touched.** The record still
reads `unexpected_remote_branches 1` and still names
`fix/freeze-checker-sign-repair` as excluded. `fix/freeze-checker-sign-repair`
was **not** added to the deletion set, and neither was anything else.
See §6, Finding 2, for what has since changed about that count and why I
left it alone.

## 3. A5 — the policy as landed

Two new sections were appended to `docs/BRANCHING_POLICY.md`, quoted
here as they now stand in the file:

    ## Deletion authorization states

    **Deletion authorization has three Stage-1 outcomes, and every listed
    branch reaches exactly one:**

    ```text
    present on remote,  verified_merged true   -> PENDING_DELETE
    present on remote,  verified_merged false  -> NOT_AUTHORIZED      (terminal)
    listed, absent from remote                 -> ABSENT_FROM_REMOTE  (terminal)
    ```

    **Stage 2 acts on `PENDING_DELETE` entries and no others.**
    **Stage 3** resolves `PENDING_DELETE` to `DELETED` or `SKIPPED`;
    `NOT_AUTHORIZED` and `ABSENT_FROM_REMOTE` entries are left exactly as
    they are.

    **`verified_merged` is `n/a` for an `ABSENT_FROM_REMOTE` entry.** With
    no tip there is no ancestry to test, and recording `true` or `false`
    would assert something that does not exist.

    **The counts satisfy a closed identity, which is machine-checkable:**

    ```text
    listed_count = pending_delete_count
                 + not_authorized_count
                 + absent_from_remote_count
    ```

    **Report the identity as an equation with its arithmetic, not as a
    claim.** Its purpose is that a mis-stated entry shows up as a number
    that does not add up.

    **The two terminal states are not interchangeable.** `NOT_AUTHORIZED`
    means present but not eligible; `ABSENT_FROM_REMOTE` means there is
    nothing to delete. A branch in the second state may be pushed later and
    would then be assessed afresh; a branch in the first will not become
    deletable by anything happening on the remote.

    ## Remote refs are the sole deletion authority

    **`git ls-remote origin` is the sole authority for every deletion
    decision.** Every tip value, every existence test and every ancestry
    check is read from `git ls-remote origin <ref>`, or from
    `refs/remotes/origin/*` **immediately after a fetch in the same
    sequence**.

    **Local branch refs MUST NOT be used for any deletion decision** —
    including `git rev-parse <branch>`, `git branch --merged`, and any
    shorthand that resolves to `refs/heads/*`.

    **This is not a precaution in the abstract.** Local refs in this
    repository are known to drift: at the time of writing, local `main` is
    `0f796174` against a remote `236f71c6`, and local
    `run/p2-betav-arm-p-decisive` is `0f796174` against a remote `48c5cc59`.

    **Re-verify each tip immediately before its deletion command**, from the
    remote. **A recorded tip is an authorization, not a statement of current
    fact.**

    **Deletion is performed with `git push origin --delete <ref>`**, and its
    raw output and exit status are reported. **`git branch -d` and
    `git branch -D` MUST NOT be used**: they touch only local refs and would
    leave the remote branch in place while appearing to have deleted it.

All six A5 items are present: the three states; the `n/a` rule; the
count identity; the `ls-remote`-only rule; the `git branch -d/-D`
prohibition; and the re-verify-immediately-before-deletion requirement.
The one prose adaptation is that the code fences use ```` ```text ````,
matching the file's existing `## Branch names` block.

**Two pre-existing sentences were also amended, because the amendment
made them false.** Both are in the same file, which is an authorised
modify path:

    -integrated it, with `deletion_status: PENDING_DELETE` or
    -`NOT_AUTHORIZED`. It is merged before any deletion, so that a failure
    -during deletion cannot leave an unrecorded loss.
    +integrated it, with a `deletion_status` from the state machine below. It
    +is merged before any deletion, so that a failure during deletion cannot
    +leave an unrecorded loss.

    -`NOT_AUTHORIZED` is terminal. Such an entry never enters the deletion
    -step and is never rewritten; it stays in the record so that what was
    -considered, and why it was not deleted, remains visible.
    +A terminal state is never rewritten; such an entry stays in the record
    +so that what was considered, and why it was not deleted, remains
    +visible.

The first enumerated two states where there are now three; the second
attributed terminality to `NOT_AUTHORIZED` alone. Leaving either would
have made the policy self-contradictory at the point where Stage 2 reads
it. Neither weakens anything.

## 4. A6 — the `DECISION_LOG.md` entry

Appended in the file's existing format —
`## <date> — <title>`, then `Date:`, `Decision owner:`, `Effect:`, then
`### Decision`, `### Evidence`, `### Consequences`, `### Related gate`,
`### Related branch and files`.

It records: both amendments; that **they arose from Stage 1's execution
rather than from review**, with the observed drift figures as evidence;
that the record was corrected without altering any recorded tip or merge
commit; and that **Stage 2 is gated on this amendment and Stage 1 both
being merged into `main`**. It also restates that
`fix/freeze-checker-sign-repair` stays excluded and that
`review/role-model-and-executors` @ `10c260b9…` stays preserved.

## 5. Are the three states exhaustive?

**Over repository states, yes. Over observations, no — there is a fourth
case, and I hit its edge in Stage 1 without noticing.**

The machine partitions on *(present on remote?)* × *(verified_merged?)*.
That is exhaustive **if and only if `verified_merged` is a total boolean
function on present branches.** Mechanically it is not.
`git merge-base --is-ancestor A B` has three outcomes, not two:

    exit 0    A is an ancestor of B
    exit 1    A is NOT an ancestor of B
    exit >=2  the check did not run — bad object, object not fetched, bad revision

**My Stage-1 harness tested `returncode == 0` and folded everything else
into `false`.** Had a tip's object been missing — a partial fetch, an
interrupted transfer, a repository with a shallow clone — Stage 1 would
have recorded `verified_merged: false` and `NOT_AUTHORIZED` for a branch
whose merge status was simply **unknown**. It did not happen: I fetched
first and every object was present, and in this task's recomputation I
made the harness three-valued and `check_failed_count` came out `0`. But
the harness was one failed fetch away from writing a false statement
into a record whose purpose is to survive an irreversible operation.

The mislabel is conservative in *effect* — it authorizes nothing — but
it is wrong in *substance*, and specifically it is wrong about the
future. The amended policy says a `NOT_AUTHORIZED` branch "will not
become deletable by anything happening on the remote". For a branch
whose check merely failed, that is a false prediction: a successful
fetch would settle it either way.

**What I would do about it.** I would not add a fourth state. I would
require that **the ancestry check distinguish exit 1 from exit ≥2, and
that exit ≥2 be a STOP** — an indeterminate merge status inside an
irreversible operation is exactly the case that wants a human, and
giving it a state invites recording the uncertainty and moving on. One
sentence in §2b would do it: *"The ancestry check's exit status is read
as three-valued; any status other than 0 or 1 is a STOP, not a
`false`."*

Three weaker candidates I considered and rejected as separate states:

- **A ref that moves between the existence test and the ancestry test.**
  Real, but a Stage-1 transient, and Stage 2's re-verification-before-
  deletion rule already covers it.
- **A listed name whose remote ref does not resolve to a commit** — a
  `refs/heads/*` pointing at a non-commit object. `ls-remote` returns an
  OID and `merge-base` errors, so this folds into the fourth case above
  rather than forming its own.
- **A listed name that appears twice.** A malformed list, not a
  repository state.

**One further structural point, not a missing state but a gap in the
identity.** The identity `listed_count = pending + not_authorized +
absent_from_remote` quantifies only over the *listed* set. Remote
branches that are **not** listed reach none of the three states and are
counted only by `unexpected_remote_branches`, which appears in no
identity and constrains nothing. That count is already moving — see §6,
Finding 2 — and it is the count that governs whether the inventory is
complete. I would add a second identity over the remote:

    remote_branch_count = listed_and_present_count
                        + preserved_count
                        + main
                        + unexpected_remote_branch_count

so that a branch appearing on the remote cannot go unnoticed by
arithmetic alone.

## 6. Stops and clarifications

**Stops: none.** A2's recomputation matched the specification's counts,
so its STOP condition did not fire. No other condition triggered a stop.

**Finding 1 — `OBSERVATION_METHOD_ERROR`, mine, latent in Stage 1, not
triggered.** The two-valued reading of `git merge-base --is-ancestor`
described in §5. It produced no wrong value in either run, because every
object was present both times, and the harness used in this task is
three-valued. Recorded because a latent method defect in the machinery
that authorizes an irreversible operation is worth naming before it
bites, not after.

**Finding 2 — secondary, an inventory count that is now stale.** The
record states `unexpected_remote_branches 1` and names
`fix/freeze-checker-sign-repair`. As of this task there are **two** such
branches on the remote — `fix/freeze-checker-sign-repair` and
`fix/branch-deletion-policy` — and **three** once this task's own branch
is pushed. All three are mine, from this sequence of authorized tasks.

**I did not update the count.** A3 says `unexpected_remote_branches`
stays as recorded and that the matter "is handled in a later inventory";
A4 confines the record's diff. The record is a Stage-1 snapshot and is
correct as such. But a reader of Stage 2 must not treat that `1` as
current. **Whatever runs Stage 2 must recompute the unexpected set from
the live remote at that moment**, and delete nothing outside the 25
`PENDING_DELETE` entries. This is the concrete reason for the second
identity proposed at the end of §5.

**Finding 3 — secondary, observational, carried forward from Stage 1.**
Local `main` remains stale at `0f796174` and local
`run/p2-betav-arm-p-decisive` at `0f796174` against a remote `48c5cc59`.
Both figures are now written into the policy itself as the evidence for
§2b. They were re-verified at the start of this task and are unchanged.
**Local `main` was not repaired**, as instructed.

**Clarification 1 — the prose sentence in `## Counts`.** Detailed in §2.
I applied a state-name substitution to a sentence outside the section A4
enumerates, because the alternative was to leave a false statement
sitting immediately above the count identity that contradicts it. Ruling
requested; trivially revertible.

**Clarification 2 — two pre-existing policy sentences amended.**
Detailed in §3. Both named `NOT_AUTHORIZED` as the only alternative to
`PENDING_DELETE`, or as the only terminal state. `docs/BRANCHING_POLICY.md`
is an authorised modify path and A5 requires the three-state machine to
be *in* that file, so leaving them would have made the file contradict
itself. Reported rather than silently absorbed.

**Clarification 3 — `verified_merged` for the absent entry.** The record
carries `n/a`, which §2a now blesses explicitly. This was already the
Stage-1 value; the amendment changes its justification from "the
conservative resolution of an unspecified case" to "the specified
value", which is the substantive improvement.

## 7. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A10 were met as written.

**(a) The state machine is called closed, and over observations it is
not.** §5 is my answer to the report contract's question. The
specification asks whether a fourth case exists; one does, it is a
measurement failure rather than a repository state, and I would close it
with a STOP rather than a state. This is the substantive thing I would
change.

**(b) A4's diff enumeration does not cover prose about the same entry
located elsewhere in the file.** Clarification 1. Naming the entry
rather than the section — *"prose describing this entry, wherever it
appears"* — would have removed the judgement call entirely.

**(c) The identity quantifies only over the listed set.** §5, final
part. The count that actually governs inventory completeness —
`unexpected_remote_branches` — is outside every identity and is already
drifting. For a task whose whole design is "make a mis-stated entry fail
to add up", leaving the one growing count outside the arithmetic is the
weaker half of an otherwise good mechanism.

**(d) A small ordering observation.** §2b requires re-verifying each tip
immediately before its deletion command, which is right, and the record
is explicitly demoted to "an authorization, not a statement of current
fact". Given that, the record's tips serve as a *tripwire* rather than
an input — Stage 2 compares and stops on mismatch. That is worth saying
in the policy, because a reader could otherwise conclude the recorded
tips are now decorative and skip the comparison.

One thing I would keep exactly as written: **making `ABSENT_FROM_REMOTE`
terminal but distinguishing its future from `NOT_AUTHORIZED`'s.** That
distinction is the part a later reader will actually need, and it is the
part a simpler amendment — just renaming the state — would have lost.

## 8. A7, A8, A9-pre, A10

### 8.1 A7 — nothing else touched

Read from the objects at the evidence base:

    GATES.md        bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md  2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md       5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml  9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL

Checked at the tree level, which covers every path beneath each
directory:

    scripts/      a84e1e2548114ae8e10dcf299bcaa8e522e33787   IDENTICAL
    derivations/  2b71991cdbbedc037679e8b64dff403987d67179   IDENTICAL
    results/      ccc39de0e06ecaf108b62cee0afaf715a47172e0   IDENTICAL
    tests/        620b23db969d17111772c3ee5b87a8f5556de8f4   IDENTICAL

### 8.2 A8 — scope manifest template

Held with a `{PUSHED_HEAD}` placeholder so its digest does not depend on
the report commit. SHA-256:
`e7b921d20aa5a0cb452117318d48599093453dff0c0ec6d314d173f8694f51c8`.

    {
      "base": "f2da41aedc5d3b48cb9d228494272a945fada971",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md"},
        {"operation": "add", "path": "reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md"},
        {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"},
        {"operation": "modify", "path": "docs/BRANCH_DELETION_RECORD_2026-08-07.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Two additions and three modifications, matching A8. The resolved
manifest, its SHA-256 and the checker JSON at the pushed head are
post-report evidence.

Pre-report check at `6275c211`, where the report commit does not yet
exist, so four operations rather than five:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "f2da41aedc5d3b48cb9d228494272a945fada971",
      "failures": [],
      "head": "6275c21185f3a1c8fd5c32a7572beb64caf974ba",
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
          "operation": "modify",
          "path": "docs/BRANCH_DELETION_RECORD_2026-08-07.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` empty; **no `delete` operation**, which for this task family
is the criterion that matters most.

### 8.3 A9-pre — four validators, at head `6275c211`

    $ python -m pytest tests/test_repository_structure.py   ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py         -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py           -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py       ->  8 passed              exit 0

Exit statuses captured from `python -m pytest` itself, not from the tail
of a pipeline. A9-final at the pushed head is post-report evidence and
carries the verdict.

### 8.4 A10 — branch only

    refs/remotes/origin/main   236f71c69ef9abec33ef0d808724ce80af037710
    remote refs/heads/main     236f71c69ef9abec33ef0d808724ce80af037710
    local main                 0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)

Neither `main` ref was moved and local `main` was not repaired.
`fix/branch-deletion-policy-amendment` was created from
`f2da41aedc5d3b48cb9d228494272a945fada971` — the head of
`fix/branch-deletion-policy`, not `main`, as A8 specifies — in a
separate worktree. **No branch was deleted or renamed.** No merge, no
PR, no force-push, no history rewrite.

## 9. Commits, and commit-message hygiene

**Commit 1** — `f0bf6ccc18eecb192804e8b0ebdd196d82ccb377`

    spec: amend the branch-deletion policy with a third authorization state

    Records the PI specification for the amendment, evidence base
    f2da41aedc5d3b48cb9d228494272a945fada971, transcribed verbatim.

    Closes two gaps that Stage 1 exposed by executing. The state machine
    gains ABSENT_FROM_REMOTE, distinct from NOT_AUTHORIZED because absence
    and ineligibility mean different things and have different futures, and
    a closed count identity that makes a misplaced entry fail to add up. The
    policy gains a rule making git ls-remote the sole deletion authority,
    since this repository's local refs are known to drift.

    Neither gap was a defect in Stage 1's output; Stage 1 handled both
    correctly and reported them.

**Commit 2** — `6275c21185f3a1c8fd5c32a7572beb64caf974ba`

    docs: add ABSENT_FROM_REMOTE and make remote refs the deletion authority

    Nothing is deleted here, and the deletion set is unchanged at 25
    PENDING_DELETE entries.

    BRANCHING_POLICY.md gains two sections. Deletion authorization now has
    three Stage-1 outcomes with a closed count identity; ABSENT_FROM_REMOTE
    is terminal and distinct from NOT_AUTHORIZED because absence and
    ineligibility have different futures. git ls-remote becomes the sole
    authority for every tip, existence test and ancestry check, each tip is
    re-verified immediately before its deletion command, and git branch
    -d/-D are prohibited for touching only local refs.

    BRANCH_DELETION_RECORD_2026-08-07.md restates its one absent entry under
    the new state, keeping the explanation and adding why it was
    restated, and gains the count identity: 25 + 0 + 1 = 26. Every count was
    recomputed from the live remote and matched. No recorded tip or merge
    commit was altered.

**Intended report commit message** (commit 3):

    docs: report the branch-deletion policy amendment

    Records A1-A9-pre and A10 for the ABSENT_FROM_REMOTE state and the
    remote-refs-only authority rule, with the recomputed counts and their
    identity, the record diff showing that only one state value changed,
    and the landed policy text quoted.

    Answers the exhaustiveness question: the three states are exhaustive
    over repository states but not over observations. git merge-base
    --is-ancestor has a third exit class that the Stage-1 harness folded
    into false, which would have mislabelled an unverifiable branch as
    unmerged. It did not occur in either run. Recommends a STOP on that
    exit class rather than a fourth state.

    Also reports that unexpected_remote_branches, left as recorded per A3,
    is now stale and must be recomputed at Stage 2.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers. This specification permits neither. Both were
**actively suppressed** on every commit of this branch by composing the
message in a file and committing with `git commit -F`, never with `-m`.

    commit 1  f0bf6ccc   suppressed: Co-Authored-By, Claude-Session
    commit 2  6275c211   suppressed: Co-Authored-By, Claude-Session
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

## 10. What remains gated

**Stage 2 is not authorized.** It requires this amendment **and** Stage 1
both merged into `main`. Whether they merge separately or as one is an
integration decision and not mine.

When Stage 2 runs it must, per the policy now landed: read every value
from `git ls-remote origin`; re-verify each tip immediately before its
deletion command; delete with `git push origin --delete`; act on the 25
`PENDING_DELETE` entries and no others; recompute the unexpected-remote
set rather than trusting the recorded `1`; and verify
`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` **first and last**.
