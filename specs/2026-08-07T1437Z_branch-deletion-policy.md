# Task specification — adopt a branch-deletion policy and clean up merged branches

Specification evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`

Classification: **MATERIAL**, and **partly irreversible**. Branch
deletion cannot be undone by this repository's own history; the
protections below exist because of that.

**Three stages, one authorization, with hard boundaries between them.**
Stage 1 adopts the policy and lands the AUTHORIZATION record. **Stage 2
deletes branches and runs only after Stage 1 is merged into `main`** —
so that if anything goes wrong during deletion, the record of what was
to be deleted is already permanent. **Stage 3 finalizes the record with
what was actually deleted**, because for an irreversible operation the
repository must carry the outcome and not only the intent.

---

## 0. The inventory, verified

`docs/BRANCHING_POLICY.md` currently says **nothing about deletion** —
it enumerates prefixes and states one branch per gate or paper-edit
task, and stops there. This task supplies the missing lifecycle rule.

**The inventory is RECOMPUTED in Stage 1; no count in this
specification is an authorization input.** Earlier drafts quoted counts
taken before the latest integrations, which made this specification
internally inconsistent — it called them evidence-base-verified while
also warning they were stale. **Both statements cannot hold, and for an
irreversible task that ambiguity is not acceptable.**

**The authoritative deletion set is the explicit name list in A2**,
subject to per-branch live verification. Structural facts that motivate
the policy — that `main` carries merge commits whose subjects pin their
source tips, that most merged branch tips are second parents of those
merges, and that at least one is not — are to be **re-established by
you** in Stage 1, not inherited from here.

**What deletion actually costs.** **For a branch whose recorded tip is
VERIFIED to be an ancestor of `main`**, deleting the ref does not make
that tip's reachable commit history unreachable through `main` — the
content, the grouping and a descriptive summary survive in the merge
commit. **"Merged branch" as a loose human label is not sufficient
grounds; the ancestor check is.** What is lost is the human-readable name.
**The deletion record of A2 preserves that**, and a committed record is
more durable than a ref, which anyone can delete.

## 1. Objective

`docs/BRANCHING_POLICY.md` states a deletion policy; a committed record
lists every branch deleted with its tip SHA and merge commit; and the
merged branches are deleted, with the protected ones demonstrably
untouched.

## 2. Stage 1 — policy and record

**The policy to land**, in the file's existing style:

> **Branch lifecycle.** A branch may be deleted only after its content
> is merged into `main`. Deletion is subject to:
>
> - **Merged, tip recoverable as a merge parent** — may be deleted. The
>   content, grouping and tip SHA survive in the merge commit.
> - **Merged, tip NOT a merge parent** — may be deleted **only after its
>   tip SHA is recorded** in a committed deletion record. Without that,
>   the ref is the sole pointer to the tip.
> - **Unmerged** — deletion destroys content, not merely a name. It
>   requires an explicit PI decision naming the branch.
> - **Explicitly preserved** — never deleted, regardless of merge state.
>
> **Every deletion is recorded, in two committed steps.**
>
> **Before deletion**, a committed AUTHORIZATION RECORD preserves each
> branch's name, tip SHA and, where one exists, the merge commit that
> integrated it, with `deletion_status: PENDING_DELETE` or
> `NOT_AUTHORIZED`. It is merged before
> any deletion, so that a failure during deletion cannot leave an
> unrecorded loss.
>
> **After deletion**, the same record is FINALIZED: each entry becomes
> `DELETED` or `SKIPPED`, with the reason for every skip. **A permanent
> record of what was intended to be deleted is not a record of what was
> deleted**, and for an irreversible operation the repository must carry
> the outcome, not only the intent.
>
> **Permanently preserved:**
> `review/role-model-and-executors` @
> `10c260b96882ac12610f78840aeeabd07be2d7cb` — the unmerged record of a
> commit-metadata defect, retained as negative-provenance evidence.

**A2 — the AUTHORIZATION record.** Land
`docs/BRANCH_DELETION_RECORD_2026-08-07.md` with one entry per branch in
the deletion set, each carrying:

    branch_name
    recorded_tip
    merge_commit            (or NOT A MERGE PARENT)
    verified_merged         (true/false, from a live ancestor check)
    deletion_status         PENDING_DELETE  or  NOT_AUTHORIZED

**The state machine is closed and has exactly these transitions:**

    Stage 1   verified_merged true   -> PENDING_DELETE
              verified_merged false  -> NOT_AUTHORIZED  (terminal)
    Stage 2   acts on PENDING_DELETE entries only
    Stage 3   PENDING_DELETE -> DELETED  or  SKIPPED
              NOT_AUTHORIZED -> unchanged, never enters Stage 2

**A `NOT_AUTHORIZED` entry is terminal and stays in the record.** It is
not removed: the record documents what was considered and why it was not
deleted, which is more useful than silence. **`verified_merged: false`
paired with a pending status would read as "still awaiting deletion",
which is the opposite of the truth** — hence the separate terminal
state.

**This is a pre-deletion authorization record, not a completed-deletion
record.** Stage 3 finalizes it. **Compute all values yourself from the
repository; do not copy them from this specification** — this
specification lists the set, not the SHAs, precisely so that the record
is verified rather than transcribed.

**Report these counts explicitly**, so that a discrepancy is visible
rather than buried:

    listed_count               (names in A2 below)
    currently_present_count    (of those, present on the remote now)
    verified_merged_count      (of those present, ancestors of main)
    not_merged_count           (-> NOT_AUTHORIZED)
    pending_delete_count       (must equal verified_merged_count)
    unexpected_remote_branches (on the remote, not in A2, not preserved)

**The deletion set** — every branch currently on the remote EXCEPT
`main` and the permanently preserved one:

    claude/paper-2-independent-verification-dysdp0
    concepts/p2-dual-pipeline
    docs/canonical-interaction
    explore/p2-phase-01-scalar
    gate/p2-betav-campaign-prereg
    gate/p2-betav-circ
    gate/p2-betav-cleanup
    gate/p2-betav-decomp
    gate/p2-channel-freeze
    gate/p2-governance-amendment
    gate/p2-grassmann-crossing-sign
    gate/p2-integrate-fierz-and-sign-ruling
    gate/p2-lattice-ontology-01
    gate/p2-phase-01-fierz-and-branch-depths
    gate/p2-si1-unblock
    governance/adopt-rules-8-12
    governance/execution-environment-refinements
    governance/p2-phase-dependency-ruling
    governance/rules-8-12-tools
    recover/batch2-gfvec-and-foundations
    recover/betav-complete
    recover/lattice-gravity-engine
    review/role-model-and-executors-clean
    run/p2-betav-arm-h-decisive
    run/p2-betav-arm-p-decisive
    sea-ice/gate-stubs

**Before recording, verify every one is merged** — an ancestor of
`main`. **If any is not, do NOT remove it from the record: give it
`verified_merged: false` and `deletion_status: NOT_AUTHORIZED`, state
the reason, and report it.** It stays in the record permanently and
never enters Stage 2. Treat every name above as a claim to check against the live
remote, not as a fact: a branch may have been added, deleted or renamed
since this specification was written.

**If the remote carries a branch not on this list**, do not delete it:
report it and stop the Stage-2 deletion for that branch only.

**A3 — `DECISION_LOG.md` entry** recording the policy adoption, the
size of the deletion set, and that `review/role-model-and-executors` is
permanently preserved.

**Then stop.** Stage 1 goes through result review and merge before
Stage 2.

## 3. Stage 2 — deletion

**Authorized only after Stage 1 is merged into `main`.** Verify that
before deleting anything, and report the `main` SHA you verified
against.

**A4 — Re-verify at deletion time**, not from the record: each branch to
be deleted is still an ancestor of `main`, and its tip still equals the
recorded value. **Any mismatch: skip that branch, report, continue with
the others.**

**A5 — Delete remote branches only.** Local branches and worktrees are
not this task's concern.

**A6 — The preserved branch is untouched.** Verify before and after that
`review/role-model-and-executors` still resolves to
`10c260b96882ac12610f78840aeeabd07be2d7cb` on the remote. **Verify it
LAST as well as first** — a deletion loop with a wrong filter would take
it, and the final check is what catches that.

**A7 — Report every deletion command with its raw output and exit
status.** A deletion reported without its output cannot be audited.

**A8 — `main` untouched throughout**, all three refs.

## 3a. Stage 3 — finalize the record

**Authorized only after Stage 2 completes.** On a new branch from
whatever `main` then is:

**A13 — Finalize.** Update each `PENDING_DELETE` entry to `DELETED` or
`SKIPPED`, giving the reason for every `SKIPPED`. **`NOT_AUTHORIZED`
entries are left exactly as they are** — they were never eligible, and
rewriting them would erase that fact.
**Change nothing else in the record** — the recorded tips and merge
commits are the pre-deletion evidence and must survive verbatim.

**A14 — Reconcile against the live remote.** List the remote branches
after deletion, and show that the set of `DELETED` entries is exactly
the set of names no longer present. **`NOT_AUTHORIZED` and `SKIPPED`
entries must still be present on the remote**; if one is absent,
something deleted a branch this task did not authorize. **Any discrepancy is a STOP and a
`REPOSITORY_DEFECT` finding**, not something to reconcile by editing the
record.

**A15 — The preserved branch appears in neither set** and still resolves
to `10c260b96882ac12610f78840aeeabd07be2d7cb`.

Stage 3 scope: `docs/BRANCH_DELETION_RECORD_2026-08-07.md` modified, plus
its own specification and report. **One modification, two additions.**

## 4. Acceptance criteria for Stage 1

**A1 — Policy landed** in `docs/BRANCHING_POLICY.md`, containing the
four lifecycle cases, the record-before-delete rule, and the preserved
branch with its SHA.

**A9 — Scope, Stage 1:**

    add:
      specs/2026-08-07T{HHMM}Z_branch-deletion-policy.md
      docs/BRANCH_DELETION_RECORD_2026-08-07.md
      reports/2026-08-07T{HHMM}Z_branch-deletion-policy.md
    modify:
      docs/BRANCHING_POLICY.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope for Stage 1: 3 additions and 2
modifications.**

**A10 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, every path under `scripts/`,
`derivations/`, `results/` and `tests/`: blob-identical to the evidence
base.

**A11 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A11-pre** at the pre-report head
goes in the report; **A11-final** at the pushed head is post-report
evidence and carries the verdict.

**A12 — Branch only for Stage 1.** Create from `236f71c6…`; move no
`main` ref; push the task branch only.

## 5. Invariants and prohibitions

- **Stage 2 does not run until Stage 1 is merged**, and **Stage 3 does
  not run until Stage 2 completes.** These orderings are the point: the
  authorization record must be permanent before the irreversible act,
  and the outcome must be recorded after it.
- **`review/role-model-and-executors` is never deleted.** It is
  unmerged; deleting it destroys content.
- **Delete no branch not on the A2 list**, and none whose merged status
  you could not verify.
- Executor-writable in Stage 1: the five paths of A9 only.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite in
  either stage.
- Branch naming: use `fix/branch-deletion-policy`. This prefix is within
  `docs/BRANCHING_POLICY.md` as written.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

**Stage 1 report (committed):** raw output for A1–A3 and A9–A12;
scope-checker JSON verbatim; the deletion record quoted in full; the
policy text quoted; **any branch you found NOT merged, with evidence**;
the earlier commit SHAs and messages; the intended report commit
message.

**Stage 1 post-report evidence:** the final scope check, A11-final, the
push, the report commit's stored message read back, ancestry.

**Stage 3 report (committed):** the finalized record quoted in full;
A13-A15 raw output; the remote branch list after deletion; and the
reconciliation showing DELETED entries match the names now absent.

**Stage 2 report (conversational):** the `main` SHA verified against;
per branch, the re-verification result and the deletion command with raw
output and exit status; the preserved branch checked first and last;
the remote branch list before and after.

Both stages: a **Stops and clarifications** section using the five
primary categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
`OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
secondary findings separate, included even if there were none; and
anything ambiguous, unsatisfiable, or that you would have specified
differently.
