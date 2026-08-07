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
