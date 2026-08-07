# Branching Policy

## Branch names

```text
gate/<gate-name>
paper/<paper-version>
review/<review-topic>
fix/<issue>
archive/<retired-route>
```

## Rules

- `main` contains accepted infrastructure and accepted closed gates only.
- Active calculations remain on a dedicated gate branch.
- Failed gate branches are preserved.
- Never squash scientific derivation history.
- Prefer conventional commits.
- Tags mark accepted scientific milestones.
- One branch corresponds to one scientific gate or one paper-edit task.
- Paper branches may update `.tex` only after reviewer acceptance.

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
integrated it, with a `deletion_status` from the state machine below. It
is merged before any deletion, so that a failure during deletion cannot
leave an unrecorded loss.

**After deletion**, the same record is FINALIZED: each entry becomes
`DELETED` or `SKIPPED`, with the reason for every skip. **A permanent
record of what was intended to be deleted is not a record of what was
deleted**, and for an irreversible operation the repository must carry
the outcome, not only the intent.

A terminal state is never rewritten; such an entry stays in the record
so that what was considered, and why it was not deleted, remains
visible.

**Permanently preserved:**
`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` — the unmerged record of a
commit-metadata defect, retained as negative-provenance evidence.

The current record is `docs/BRANCH_DELETION_RECORD_2026-08-07.md`.

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
