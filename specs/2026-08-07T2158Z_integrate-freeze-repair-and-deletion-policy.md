# Task specification — integrate the freeze-checker repair and the branch-deletion policy

Specification evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`

Classification: **MATERIAL**. Both sources completed result review. This
is the integration authorization.

**Two merges, not three.** `fix/branch-deletion-policy` @ `f2da41ae…` is
an ANCESTOR of `fix/branch-deletion-policy-amendment` @ `1c106372…` —
verified by dry run — so merging the amendment brings Stage 1 with it.
**Merging Stage 1 separately would add a merge commit that integrates
nothing.**

    Branch A  fix/freeze-checker-sign-repair
              0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b
    Branch B  fix/branch-deletion-policy-amendment
              1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e
              (contains fix/branch-deletion-policy @ f2da41ae…)

**No conflict expected** — verified by dry run: 8 additions and 4
modifications, and **the two sources have DISJOINT changed-path sets.**
**If a conflict occurs, STOP**; none is pre-authorized.

**`DECISION_LOG.md` arrives ONLY from Branch B**, verified against the
branch tips:

    Branch A changed paths: derivations/…_checker_sign_repair.md,
      reports/…1424Z…, specs/…1424Z…,
      scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py,
      tests/test_p2_grassmann_crossing_sign.py

Branch A does not touch it. **At the merged head `DECISION_LOG.md` must
be blob-identical to Branch B**, which removes any question of append
ordering. **An earlier draft of this specification said both branches
appended to it; that was inferred rather than checked, and was wrong.**

---

## 0. What is being integrated, and what remains open

**Branch A** removes the inert double application of the Grassmann
crossing sign from `basis_freeze_check.py`, leaving it applied **zero**
times, per the 2026-08-07 ruling that `matrix_rational` is stored
unsigned and `s_G` is applied once at operator use. `computed_fierz` is
unchanged by the edit — the two factors already cancelled — and this was
verified entry-by-entry as exact rationals. `parse_grassmann_sign` still
runs, so a malformed value is still rejected.

**Branch B** adopts a branch-deletion policy with a three-state
authorization machine (`PENDING_DELETE`, `NOT_AUTHORIZED`,
`ABSENT_FROM_REMOTE`), a closed count identity, and a rule making
`git ls-remote` the sole deletion authority; and lands the Stage-1
authorization record with 26 entries.

**A gap this integration does NOT close, recorded so it is not
forgotten.** `scripts/p2_grassmann_crossing_sign.py` carries
`DECLARED_CROSSING_SIGN = -1` as a literal; that consumer never reads
`grassmann_crossing_sign` from the freeze. **So a flip of the freeze
field still reaches no comparison anywhere.** Branch A's new test catches
"the consumer's constant disagrees with the computed sign", which is not
the same thing. The executor reported this rather than overstating the
coverage. **Closing it needs a change to the consumer and is a separate
task; do not attempt it here.**

**Stage 2 of the deletion task is NOT authorized by this
specification**, and landing this integration does not make it ready to
run. The policy prerequisite will be satisfied; the execution controls
are not yet written.

**Stage 2 may be separately authorized only under a specification that
adds at least these two controls:**

1. **`git merge-base --is-ancestor` exit codes are three-valued, not
   two.** `0` means merged, `1` means not merged, and **anything `>= 2`
   is an execution failure and MUST be a STOP** — it must not be mapped
   to `verified_merged: false`. A failed observation is not a negative
   result, and treating it as one would silently move a branch into a
   terminal state on the strength of a command that did not run.
2. **The live remote branch set must be re-enumerated at Stage-2 time**,
   including `unexpected_remote_branches`. The Stage-1 record is an
   authorization, not a current inventory, and the remote has already
   changed once since it was taken.

**Do not read this integration as "ready for deletion".**

## 1. Objective

`main` contains both branches' content, integrated by merge commits with
correct parentage. Nothing else on `main` changes.

## 2. Sequence

    1  fetch; verify refs (A1); create a local integration branch
       from the base
    2  PRE_MERGE guard for Branch A
    3  --no-ff merge Branch A
    4  PRE_MERGE guard for Branch B against the merge-A commit
    5  --no-ff merge Branch B
    6  on the UNPUSHED pre-report head: A5, A6, A7, A9-pre
    7  commit the integration report, carrying the step-6 evidence
    8  any remaining locally-verifiable checks at the final head
    9  push only if every check at steps 6 and 8 passed
    10 fetch; final POST_MERGE guard with
       remote_check_policy = REQUIRED

**`--no-ff` is mandatory at both merges.** Both sources descend from
their bases, so an ordinary merge would fast-forward and produce no
merge commit.

**Everything verifiable locally is verified before the push.** A failure
found after pushing has already changed `main`.

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `236f71c69ef9abec33ef0d808724ce80af037710`; Branch A to
`0ab0ca9d…`; Branch B to `1c106372…`. Any mismatch → STOP and report the
new tip. **Local `main` is stale by design — do not fast-forward or
repair it.** Report all refs separately, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on; it is not independently selectable.** With the commit order
of §4, parent 1 of merge A is the specification commit.

    Merge A   parent 1 = the integration specification commit (commit 1)
              parent 2 = 0ab0ca9d4a6dcdd2762d5a03fe83207b18b6b49b
              merge-base(parent 1, parent 2)
                       = 236f71c69ef9abec33ef0d808724ce80af037710

    Merge B   parent 1 = the merge-A commit
              parent 2 = 1c1063726bd4ea3facdc2b6b3cfd7b0939c3506e
              merge-base(parent 1, parent 2)
                       = 236f71c69ef9abec33ef0d808724ce80af037710

**Both merge-bases are the ORIGINAL base**, verified by dry run — the
specification commit descends from it and both branches were cut from
it. Report both merges with parents and merge-bases as distinct values.

**A3 — Guards.** `PRE_MERGE(A)` at step 2, `PRE_MERGE(B)` at step 4, and
one final `POST_MERGE` at step 10.

**The final guard carries TWO DISTINCT SHAs.** The final head is the
REPORT commit, not a merge commit. **The merge object under verification
is the Merge-B commit**; **remote agreement is checked against the final
report-commit head**. Report both and label which is which. **If the
guard cannot represent those two roles separately, STOP** rather than
substituting one for the other.

**A4 — Scope, frozen manifest.** The `head` and `{HHMM}` placeholders
are the only permitted substitutions:

    base: 236f71c69ef9abec33ef0d808724ce80af037710
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md
      docs/BRANCH_DELETION_RECORD_2026-08-07.md
      reports/2026-08-07T1424Z_freeze-checker-sign-repair.md
      reports/2026-08-07T1437Z_branch-deletion-policy.md
      reports/2026-08-07T1508Z_branch-deletion-policy-amendment.md
      reports/2026-08-07T{HHMM}Z_integrate-freeze-repair-and-deletion-policy.md
      specs/2026-08-07T1424Z_freeze-checker-sign-repair.md
      specs/2026-08-07T1437Z_branch-deletion-policy.md
      specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md
      specs/2026-08-07T{HHMM}Z_integrate-freeze-repair-and-deletion-policy.md
    modify:
      DECISION_LOG.md
      docs/BRANCHING_POLICY.md
      scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
      tests/test_p2_grassmann_crossing_sign.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 10 additions and 4 modifications.** Eight
additions and four modifications arrive from the two branches; two
additions are authored here. **A fifteenth path is a defect.**

**A5 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`pyproject.toml`, `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
`results/P2-CHANNEL-FREEZE/fierz_matrix.json` and its `.sha256`,
`scripts/P2-CHANNEL-FREEZE/vocab_parser.py`,
`tests/test_channel_freeze_mutations.py`,
`tests/test_channel_freeze_phase_a.py`: blob-identical between base and
merged head. **Read from the objects.**

**A6 — Arriving content intact.** The eight arriving additions are
present; `basis_freeze_check.py` and `tests/test_p2_grassmann_crossing_sign.py`
arrive as Branch A had them; `docs/BRANCHING_POLICY.md` and
`docs/BRANCH_DELETION_RECORD_2026-08-07.md` arrive as Branch B had them.
Verify by blob comparison against the source branch tips.

**A7 — No gate changed.** `GATES.md` blob-identical to the base; `^## P2-`
count 14 before and after; `P2-PHASE-01` still `PROPOSED`. **This
integration changes validation machinery and branch policy, not a gate.**

**A8 — The deletion record survives verbatim.**
`docs/BRANCH_DELETION_RECORD_2026-08-07.md` at the merged head is
blob-identical to its value on Branch B. **Every recorded tip is
pre-deletion evidence for an irreversible operation; a merge that
altered one would be a serious defect.**

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`,
`tests/test_channel_freeze_phase_a.py`,
`tests/test_channel_freeze_mutations.py`. **A9-pre** at the pre-report
head goes in the report; **A9-final** at the pushed head is post-report
evidence and carries the verdict. **Both freeze suites must still pass
unchanged** — that is the regression evidence for the checker edit.

**A10 — Commit-message hygiene** on every commit including both merge
commits: inspect the proposed message before, and the stored message
after; permit no `Co-Authored-By`, no session identifier or URL, no tool
attribution. **Report per commit whether any trailer was suppressed and
which — an authoring-time suppression is a fact to disclose, not an
absence.** If one appears despite pre-commit inspection, STOP before
pushing.

**A11 — Branches preserved.** Both source branches, and
`fix/branch-deletion-policy` @ `f2da41ae…`, still resolve to their
pinned commits after the merge. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch** — including the ones now merged, which are
Stage 2's business and not this task's.

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-07T{HHMM}Z_integrate-freeze-repair-and-deletion-policy.md
    commit 2  --no-ff merge of Branch A
    commit 3  --no-ff merge of Branch B
    commit 4  reports/2026-08-07T{HHMM}Z_integrate-freeze-repair-and-deletion-policy.md

**Committed report:** raw output for A1, A2, A5–A8, A9-pre, A10 for
commits 1–3; both `PRE_MERGE` JSONs verbatim; the intended final
manifest and the intended final `POST_MERGE` parameters; commit 1–3 SHAs
and messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check at the pushed head,
A9-final, the push, the report commit's stored message read back from
the object, and ancestry confirmation. **Do not amend the report to
insert evidence whose production depends on the report commit.**

## 5. Invariants and prohibitions

- Executor-writable: the integration specification and the integration
  report. **Everything arriving by merge is integrated exactly as
  reviewed and may not be edited.**
- **Do not merge `fix/branch-deletion-policy` separately.** It is an
  ancestor of Branch B; a separate merge would integrate nothing and
  add a misleading merge commit.
- **Do not perform Stage 2**, and do not delete any branch.
- **Do not touch `scripts/p2_grassmann_crossing_sign.py`.** The
  hard-coded `DECLARED_CROSSING_SIGN` gap of §0 is a separate task.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commits only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. Merge the pinned remote refs, not
  local copies — **local refs in this repository are known to drift.**
- Any merge conflict is an immediate stop, including in
  `DECISION_LOG.md`.
- Branch naming: use `fix/integrate-freeze-repair-and-deletion-policy`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- Do not alter any existing worktree containing uncommitted content, and
  do not clean, stash, or discard untracked files anywhere.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- everything listed in §4 under its correct layer;
- both merge commit SHAs, their parents and merge-bases, as distinct
  values;
- `DECISION_LOG.md` at the merged head shown **blob-identical to Branch
  B**;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
