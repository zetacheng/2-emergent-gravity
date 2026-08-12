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

## Superseded branches

**A branch is SUPERSEDED when its work has been re-issued or replaced
and it is preserved as evidence rather than for integration.**

**A superseded branch MUST NOT be integrated.** Its content may remain
correct — supersession is about integrability and task identity, not
about correctness — **but the authoritative instance is the branch that
replaced it.**

**This is an attribute, not a deletion state.** A superseded branch
still reaches exactly one Stage-1 deletion outcome, and the closed count
identity above is unchanged. **The two questions are independent:
whether a branch may be deleted, and whether it may be integrated.**
Each entry below is present on the remote and unmerged, so each is
`NOT_AUTHORIZED` for deletion; that is its deletion outcome, and it says
nothing about integrability.

**Supersession is recorded in the register below**, naming the branch,
its commit, what replaced it, and why. **A Git ref carries no such
marker, so the register is where it lives.**

**The register:**

```text
fix/pi-decisions-and-deferred @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
  superseded by  fix/pi-decisions-v2, then fix/pi-decisions-v3
  reason         re-issued on a clean branch after the second
                 execution overwrote the first execution's pushed
                 records on the same branch
  content        the substantive content was approved; the
                 representation was not

fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36
  superseded by  fix/pi-decisions-v3
  reason         stale base: main advanced through two governance
                 landings and the branch lost conflict-free
                 integrability
  content        APPROVED and unchanged; only its integrability
                 lapsed

governance/supply-protocol-v2
                          @ 40168469608618aef6812735ff70e32de0e3cbc8
  superseded by  governance/supply-protocol-v3
  reason         its A3 required the landed Rule 18 to contain
                 delimiter literals and a blank-line clause, while
                 the rule it directed abandoned both; the executor
                 stopped at that inconsistency
  content        no governance file was touched; the branch carries
                 a stop report and the first successful live test of
                 the file-supply rule

governance/supply-protocol-and-superseded
                          @ 7146a093c65788a57d63a747b71d86edb91eddc6
  superseded by  governance/supply-protocol-v3
  reason         its A2 required applying a Rule 18 whose own text
                 forbade the only available action; the executor
                 derived a boundary and continued where the
                 standing inconsistency invariant required a stop
  content        the governance work was correct and the committed
                 review was byte-correct; what failed was the rule
                 it was landing, which this version replaces

review/role-model-and-executors
                          @ 10c260b96882ac12610f78840aeeabd07be2d7cb
  superseded by  review/role-model-and-executors-clean, merged
  reason         rebuilt SOLELY to remove undeclared commit
                 metadata from history; the clean-rebuild
                 specification names the successor and the reason
  content        VERIFIED CORRECT before the rebuild — seven
                 declared paths, correct commit layering, protected
                 paths unchanged, the role model landed as approved
  note           this branch ALREADY carries a durable disposition:
                 "permanently preserved ... the unmerged record of a
                 commit-metadata defect, retained as
                 negative-provenance evidence". That disposition
                 stands unchanged. The two answer different
                 questions -- permanently preserved means do not
                 delete; superseded means do not integrate -- and
                 the register exists because they are independent.

gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192
  superseded by  gate/p2-land-diquark-line-v2
  reason         the specification stated an impossible merge-base
                 and the executor STOPPED at the pre-merge guard;
                 the re-issue corrected the value
  content        the branch carries a report of the stop and NO
                 merge; it is the record of a correct refusal, not
                 of failed work
```

**The entries differ in kind and the register does not flatten that.**
**Refer to them by BRANCH NAME, never by ordinal** — an ordinal is
correct only until the list grows, and a paragraph of this register has
already been wrong once for exactly that reason.

```text
approved work re-instantiated elsewhere
  fix/pi-decisions-and-deferred
  fix/pi-decisions-v2
  review/role-model-and-executors

no work at all: a defective specification, an executor that
stopped, and the evidence that a stop happened and why
  gate/p2-land-diquark-line
  governance/supply-protocol-v2

work completed but the execution contract breached, so not
integrable although the content was correct
  governance/supply-protocol-and-superseded
```

**Supersession covers all three kinds; the register records which.**

**Entry threshold.** **A branch is added to this register only where a
durable repository artifact records its re-issue, replacement or
supersession and identifies the replacement or the reason.** **The
artifact must record the FACT, not use a particular WORD** — a
specification that says a branch was rebuilt and names both the
successor and the reason satisfies this even if the word "superseded"
never appears. **Naming similarity, age, Git topology, or the mere
existence of a later branch do NOT suffice**, singly or together.
**Where evidence suggests supersession but does not establish it, the
branch is left out pending a PI decision** and the evidence is reported.
**Finding the artifact that already records a supersession is an
observation; classifying a branch as superseded is a decision.**

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
