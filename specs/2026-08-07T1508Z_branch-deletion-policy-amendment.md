# Task specification — amend the branch-deletion policy: `ABSENT_FROM_REMOTE` state and remote-refs-only authority

Specification evidence base: `f2da41aedc5d3b48cb9d228494272a945fada971`
(the head of `fix/branch-deletion-policy`, Stage 1 as landed)

Classification: **MATERIAL**. Branch only; integration is a separate
authorization. **Stage 2 of the deletion task does not run until this
amendment and Stage 1 are both merged into `main`.**

**This closes two governing gaps that Stage 1 exposed by executing.**
Neither is a defect in what Stage 1 produced — Stage 1 handled both
correctly and reported them. They are gaps in the policy Stage 1 was
executing under.

---

## 0. What Stage 1 found

**Gap 1 — the state machine has no state for "listed but absent from the
remote."** `gate/p2-integrate-fierz-and-sign-ruling` was created locally
during the integration task and never pushed. The executor recorded it
as `NOT_AUTHORIZED` with `verified_merged: n/a`, which authorizes
nothing and is the conservative direction — **the right call under the
policy as written.**

But it produces a record that has to explain itself: `not_merged_count`
is `0` while one entry is `NOT_AUTHORIZED`. **The two states mean
different things** — `NOT_AUTHORIZED` is "present but not eligible";
absence is "there is nothing to delete" — **and they have different
futures.** A branch that is absent may be pushed later; one that is
present but unmerged will not become deletable by anything happening on
the remote.

**Gap 2 — nothing says which refs are authoritative.** Stage 1 used
`git ls-remote` throughout, correctly. The policy does not require it,
and this repository's local refs are known to drift: local `main` sits
at `0f796174` while the remote is at `236f71c6`, and local
`run/p2-betav-arm-p-decisive` sits at `0f796174` while the remote
carries `48c5cc59`. **A Stage 2 driven from local refs would act on
wrong values inside an irreversible operation.**

**Also recorded: a correction to the earlier inventory, which was
mine.** An earlier statement that
`governance/execution-environment-refinements` was "not a merge parent"
was wrong — it is **parent 1** of `9f41dbe5340d1822bb9f5fa33bd495b528e8a841`.
The earlier check indexed only `^2`. The executor caught it by scanning
all parents and the landed record carries the corrected value. **The
structural picture is now: 27 merge commits on `main`; 24 tips are
second parents, 1 is a first parent, none is a non-parent.**

## 1. Objective

`docs/BRANCHING_POLICY.md` carries a three-state authorization machine
with a closed count identity and a remote-refs-only authority rule; the
landed deletion record is corrected to use the new state; and
`DECISION_LOG.md` records the amendment. Stage 2 then runs under these.

## 2. The policy text to land

### 2a. The authorization state machine

> **Deletion authorization has three Stage-1 outcomes, and every listed
> branch reaches exactly one:**
>
>     present on remote,  verified_merged true   -> PENDING_DELETE
>     present on remote,  verified_merged false  -> NOT_AUTHORIZED      (terminal)
>     listed, absent from remote                 -> ABSENT_FROM_REMOTE  (terminal)
>
> **Stage 2 acts on `PENDING_DELETE` entries and no others.**
> **Stage 3** resolves `PENDING_DELETE` to `DELETED` or `SKIPPED`;
> `NOT_AUTHORIZED` and `ABSENT_FROM_REMOTE` entries are left exactly as
> they are.
>
> **`verified_merged` is `n/a` for an `ABSENT_FROM_REMOTE` entry.**
> With no tip there is no ancestry to test, and recording `true` or
> `false` would assert something that does not exist.
>
> **The counts satisfy a closed identity, which is machine-checkable:**
>
>     listed_count = pending_delete_count
>                  + not_authorized_count
>                  + absent_from_remote_count
>
> **Report the identity as an equation with its arithmetic, not as a
> claim.** Its purpose is that a mis-stated entry shows up as a number
> that does not add up — the earlier count set had no identity, which is
> why a misplaced entry produced only a prose explanation.
>
> **The two terminal states are not interchangeable.**
> `NOT_AUTHORIZED` means present but not eligible; `ABSENT_FROM_REMOTE`
> means there is nothing to delete. A branch in the second state may be
> pushed later and would then be assessed afresh; a branch in the first
> will not become deletable by anything happening on the remote.

### 2b. Remote refs are the sole deletion authority

> **`git ls-remote origin` is the sole authority for every deletion
> decision.** Every tip value, every existence test and every ancestry
> check is read from `git ls-remote origin <ref>`, or from
> `refs/remotes/origin/*` **immediately after a fetch in the same
> sequence**.
>
> **Local branch refs MUST NOT be used for any deletion decision** —
> including `git rev-parse <branch>`, `git branch --merged`, and any
> shorthand that resolves to `refs/heads/*`.
>
> **This is not a precaution in the abstract.** Local refs in this
> repository are known to drift: at the time of writing, local `main` is
> `0f796174` against a remote `236f71c6`, and local
> `run/p2-betav-arm-p-decisive` is `0f796174` against a remote
> `48c5cc59`.
>
> **Re-verify each tip immediately before its deletion command**, from
> the remote. **A recorded tip is an authorization, not a statement of
> current fact.**
>
> **Deletion is performed with `git push origin --delete <ref>`**, and
> its raw output and exit status are reported. **`git branch -d` and
> `git branch -D` MUST NOT be used**: they touch only local refs and
> would leave the remote branch in place while appearing to have
> deleted it.

## 3. Corrections to the landed record

**A1 — Restate the absent entry.** In
`docs/BRANCH_DELETION_RECORD_2026-08-07.md`, change
`gate/p2-integrate-fierz-and-sign-ruling` from `NOT_AUTHORIZED` to
**`ABSENT_FROM_REMOTE`**, keeping `verified_merged: n/a` and
`merge_commit: NOT PRESENT ON REMOTE` as they are.

**Update the surrounding prose section accordingly** — it is currently
headed as explaining "the one `NOT_AUTHORIZED` entry". **Keep its
explanation of what happened**; only the state name and the heading
change. **Do not delete the explanation**: why a listed branch was never
pushed is exactly what a later reader needs.

**A2 — Add the count identity** to the record, with its arithmetic
shown:

    listed_count               26
    pending_delete_count       25
    not_authorized_count        0
    absent_from_remote_count    1
    25 + 0 + 1 = 26 = listed_count   ✓

**Recompute every count yourself from the live remote; do not copy
these.** They are stated so a mismatch is visible, not so they can be
transcribed. **If your recomputation differs, report the difference and
STOP** — something changed on the remote between Stage 1 and now, and
that is exactly what Stage 2 must not run blind into.

**A3 — `unexpected_remote_branches` stays as recorded.**
`fix/freeze-checker-sign-repair` appeared on the remote after the
Stage-1 inventory was taken. **It remains excluded and must not be
deleted in Stage 2.** **Do not add it to the deletion set to make the
inventory look tidy** — adding a name that no review has passed would
widen an irreversible operation on the basis of neatness. It is handled
in a later inventory.

**A4 — Do not change any other entry**, tip, merge commit, or state.
Verify by diff that the record's changes are exactly: one state value,
the heading and prose of that one section, and the added count block.

## 4. Acceptance criteria

**A5 — Policy landed.** `docs/BRANCHING_POLICY.md` contains both §2a and
§2b in the file's existing style, including: the three states; the
`n/a` rule; the count identity; the `ls-remote`-only rule; the
prohibition on `git branch -d/-D`; and the requirement to re-verify each
tip immediately before deletion.

**A6 — `DECISION_LOG.md` entry** in the file's existing format,
recording the amendment, that it arose from Stage 1's execution rather
than from review, and that Stage 2 is gated on this amendment being
merged.

**A7 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, and every path under `scripts/`,
`derivations/`, `results/` and `tests/`: blob-identical to the evidence
base. Read from the objects.

**A8 — Scope:**

    base: f2da41aedc5d3b48cb9d228494272a945fada971
    mode: exact
    add:
      specs/2026-08-07T{HHMM}Z_branch-deletion-policy-amendment.md
      reports/2026-08-07T{HHMM}Z_branch-deletion-policy-amendment.md
    modify:
      docs/BRANCHING_POLICY.md
      docs/BRANCH_DELETION_RECORD_2026-08-07.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 2 additions and 3 modifications.** Report
the template, the resolved manifest, its SHA-256, and the checker JSON
including `observed_operations`.

**Note the base.** This branches from `fix/branch-deletion-policy`, not
from `main`, because it amends what that branch landed. **Both branches
merge into `main` before Stage 2 runs**; whether they merge separately
or as one is an integration decision, not yours.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A9-pre** at the pre-report head goes
in the report; **A9-final** at the pushed head is post-report evidence
and carries the verdict.

**A10 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main`, and report both; neither is moved. **Local `main` is
stale by design — do not repair it.** Push the task branch only.
**Delete no branch.**

## 5. Evidence layering

**Committed report:** A1–A9-pre, A10, the earlier commit SHAs and
messages, the pre-report head, the intended report commit message and
its authoring-time trailer suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A9-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the five paths of A8 only.
- **Delete no branch.** This task amends policy and a record; it
  performs no deletion.
- **Do not add `fix/freeze-checker-sign-repair`, or any other
  unlisted branch, to the deletion set.**
- **Do not alter any recorded tip or merge commit** in the deletion
  record. They are pre-deletion evidence.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/branch-deletion-policy-amendment`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- raw output for A1–A10, scope-checker JSON verbatim including
  `observed_operations`;
- the count identity with its arithmetic, recomputed;
- the record diff, showing that only the state value, that section's
  heading and prose, and the count block changed;
- the policy text as landed, quoted;
- **whether the three states are in fact exhaustive** — you executed
  Stage 1 and are better placed than we are to see a fourth case. If one
  exists, say so; a state machine described as closed that is not is
  worse than one described as open;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
