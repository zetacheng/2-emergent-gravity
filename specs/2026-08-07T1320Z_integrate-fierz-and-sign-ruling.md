# Task specification — integrate both `P2-PHASE-01` derivation branches and record the Fierz sign ruling

Specification evidence base: `9609677576b6d0d77a0813c93673aed81b0c4d5f`

Classification: **MATERIAL**. Both source branches completed result
review. This is the integration authorization, plus one PI ruling that
must land with them because it changes how their results read.

**Two sources, no conflict expected.** Their path sets are disjoint —
verified by dry run: twelve additions, zero overlap, no `DECISION_LOG.md`
contention. **If a conflict nevertheless occurs, STOP**; none is
pre-authorized here.

    Branch A  gate/p2-phase-01-fierz-and-branch-depths
              dca522690b00ae6bc9b706492b09d7c60d7efc51
    Branch B  gate/p2-grassmann-crossing-sign
              cf4c78959c0caf6bfed7c80f9451b6a3337972fe

---

## 0. The PI ruling this task lands

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

**Record this as SUPPLYING a definition, not as recovering an original
intent.** The executor established that no defining kernel equation
exists anywhere in the frozen material — `K_exch`, `K_direct`,
`defining equation` and `kernel equation` all occur zero times, verified
independently. The ruling rests on three pieces of indirect evidence
(an unsigned reconstruction matches the frozen entries; the checker's
net effect is `+1`; the sign is declared as a separate convention
field), **none of which is a defining equation.** A record claiming the
ruling recovers what the freeze meant would overstate the evidence.

**Consequence, which is why the ruling lands with these branches.**
Branch A reported the induced coefficients as `+G/4` for V and A,
singlet, with an explicit sign caveat. Under this ruling the caveat is
discharged and the values become **`−G/4`**. Branch B reported the
storage convention as `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`;
this ruling closes it.

**Do not modify either branch's report or derivation note.** They
honestly record what was known when written, and rewriting them would
destroy that. The consequence is recorded in a separate addendum.

## 1. Objective

Paper 2 `main` contains both branches' content, integrated by merge
commits with correct parentage; the ruling is recorded in
`DECISION_LOG.md`; and a short addendum records the sign consequence for
the already-committed results. Nothing else on `main` changes.

## 2. Sequence

    1  verify refs (A1); create a local integration branch from the base
    2  PRE_MERGE guard for Branch A
    3  --no-ff merge Branch A
    4  PRE_MERGE guard for Branch B against the merge-A commit
    5  --no-ff merge Branch B
    6  commit the DECISION_LOG entry and the addendum
    7  on the UNPUSHED pre-report head: A5 protected paths,
       A6 arriving digests, A7 gate mapping, A9-pre validators
    8  commit the integration report (commit 5), carrying the step-7
       evidence
    9  any remaining locally-verifiable checks at the final head that
       do not depend on remote state
    10 push only if every check at steps 7 and 9 passed
    11 fetch; final POST_MERGE guard with
       remote_check_policy = REQUIRED

**The report commit precedes the push.** An earlier draft pushed at
step 8, before commit 5 existed — the report carries the step-7 evidence
and must therefore be committed first. **The pre-report head at step 7
is commit 4**, not the final head.

**Three guard runs, not two:** `PRE_MERGE(A)` at step 2,
`PRE_MERGE(B)` at step 4, and one final `POST_MERGE` at step 11.

**The final guard carries TWO DISTINCT SHAs, deliberately.** The final
head is the REPORT commit, not a merge commit. So: **the merge object
under verification is the Merge-B commit**, while **remote agreement is
checked against the final report-commit head**. Report both, and label
which is which. **If the guard implementation cannot represent those two
roles separately, STOP and report rather than substituting one for the
other** — a guard that silently verified the report commit as though it
were a merge would check parentage that does not exist.

**`--no-ff` is mandatory at both merges.** Both sources descend from
their respective bases, so an ordinary merge would fast-forward and
produce no merge commit.

**Everything verifiable locally is verified before the push**, because a
failure found after pushing has already changed `main`.

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `9609677576b6d0d77a0813c93673aed81b0c4d5f`; Branch A
resolves to `dca52269…`; Branch B to `cf4c7895…`. Any mismatch → STOP
and report the new tip. **Local `main` is stale by design; do not
fast-forward or repair it.** Report all refs separately.

**A2 — Merge parentage. Both merge-bases are the ORIGINAL base, and the
second one is the point most likely to be mis-specified.**

    Merge A   parent 1 = the integration specification commit (commit 1)
              parent 2 = dca522690b00ae6bc9b706492b09d7c60d7efc51
              merge-base(parent 1, parent 2)
                       = 9609677576b6d0d77a0813c93673aed81b0c4d5f

**PARENT and MERGE-BASE are different things, and conflating them was
this specification's second parent-ordering defect.** Parent 1 is fixed
by which commit you are standing on — it is not selectable — so with
§4's commit order it is necessarily the specification commit, not the
base. **That does not change the merge-base**: the specification commit
descends from the base and Branch A was cut from the base, so their
common ancestor is still `9609677…`.

**PI ruling: Reading 1 governs.** §4's commit order stands — the
authorization document exists in the branch history before the merges it
authorizes. An earlier draft stated parent 1 as the base, which is
unsatisfiable together with §4. **You were right to stop.**

    Merge B   parent 1 = the merge-A commit
              parent 2 = cf4c78959c0caf6bfed7c80f9451b6a3337972fe
              merge-base(parent 1, parent 2)
                       = 9609677576b6d0d77a0813c93673aed81b0c4d5f

**Merge B's merge-base is the original base, NOT the merge-A commit.**
Branch B was cut from `9609677…` and does not contain merge A, so their
common ancestor is `9609677…`. Verified by dry run. **An earlier draft
of this specification stated the merge-A commit here and was wrong; had
you found the discrepancy you would have been right to stop.**

Report both merge commits with their parents and merge-bases as distinct
values.

**A3 — `DECISION_LOG.md` entry.** One entry in the file's existing
`## <date> — <title>` / `### Decision` / `### Reason` format, reproducing
the §0 ruling **verbatim** and containing these facts:

    Date: 2026-08-07
    Decision owner: Principal Investigator
    Effect: supplies a definition absent from the frozen material
    Not a recovery of original intent
    s_G = -1, applied exactly once at operator use
    matrix_rational is stored unsigned
    basis_freeze_check.py double application is ineffective validation
    Consequence: P2-PHASE-01 induced V and A coefficients are -G/4
    Freeze repair (tenth mutation, checker correction, vocab_parser pin)
      is queued as a separate task and is NOT performed here

**A4 — Addendum.** Add
`derivations/P2-PHASE-01_fierz_sign_addendum.md` recording: the ruling;
that Branch A reported `+G/4` for the MATRIX-LEVEL induced V and A
coefficients **while explicitly leaving the operator-level sign
unresolved**, and that under this ruling, applying `s_G = −1` exactly
once gives the OPERATOR-LEVEL coefficients `−G/4`. **Do not write that
the earlier report was "correct under an unsigned matrix"** — it did not
know the storage convention, and saying so would misdescribe what was
known when it was written; that Branch B's
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` is now closed by ruling
rather than by evidence; and that the structural results — S, P and T
vanish; V and A equal and purely singlet; the exchanged form purely
left-right with `LL = RR = 0` — are **unaffected by the sign**.

**State plainly that neither original report was altered**, and cite
both by path.

**A5 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`pyproject.toml`, the Phase-A freeze, `basis_freeze_check.py`,
`vocab_parser.py`, both freeze test files, `fierz_matrix.json` and its
sidecar: blob-identical between base and merged head. **Read from the
objects.** No path added, deleted, renamed or type-changed under
`tests/` or `scripts/` beyond the four source-branch additions in those
prefixes — two scripts and two test files. **The protected-prefix check
concerns those prefixes, not the full arriving set.**

**A6 — Arriving artifacts.** The twelve paths below arrive; verify each
is present and that the four pinned digests match:

    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
    derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md
    reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
    reports/2026-08-07T1159Z_grassmann-crossing-sign.md
    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
    results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
    scripts/p2_phase01_fierz_and_depths.py
    scripts/p2_grassmann_crossing_sign.py
    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
    specs/2026-08-07T1159Z_grassmann-crossing-sign.md
    tests/test_p2_phase01_fierz_and_depths.py
    tests/test_p2_grassmann_crossing_sign.py

Pinned surviving artifacts, unchanged:

    derivations/P2-LATTICE-ONTOLOGY-01.md
    1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c

    scripts/euclidean_reconstruction.py
    30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

**A7 — No gate changed.** `GATES.md` blob-identical to the base;
`^## P2-` count 14 before and after; `P2-PHASE-01` still `PROPOSED`.
**This ruling changes a convention, not a gate.**

**A8 — Scope, frozen manifest.** The `head` placeholder is the only
permitted substitution:

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
      specs/2026-08-07T{HHMM}Z_integrate-fierz-and-sign-ruling.md
      tests/test_p2_phase01_fierz_and_depths.py
      tests/test_p2_grassmann_crossing_sign.py
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 15 additions and 1 modification.** Twelve
arrive from the two source branches; three are authored here — the
integration specification, the addendum, and the integration report.
**A sixteenth path is a defect, and stating the count makes that
visible.**

Resolve `{HHMM}` to the token of your specification commit. Report the
template, the resolved manifest, its SHA-256, and the checker JSON
including `observed_operations`.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`. **A9-pre** at the pre-push head goes in the
report; **A9-final** at the pushed head is post-report evidence and
carries the verdict. Both passes cover:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`,
`tests/test_channel_freeze_phase_a.py`,
`tests/test_channel_freeze_mutations.py`.

**A10 — Commit-message hygiene** on every commit including both merge
commits: inspect the proposed message before, and the stored message
after; permit no `Co-Authored-By`, no session identifier or URL, no tool
attribution. **Report per commit whether any trailer was suppressed and
which — an authoring-time suppression is a fact to disclose, not an
absence.** If one appears despite pre-commit inspection, STOP before
pushing.

**A11 — Branches preserved.** Both source branches still resolve to
their pinned commits after the merge. **`review/role-model-and-executors`
@ `10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched** — it is
unmerged and deliberately preserved; deleting it would destroy content,
not just a name. **This task deletes no branch.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-07T{HHMM}Z_integrate-fierz-and-sign-ruling.md
    commit 2  --no-ff merge of Branch A
    commit 3  --no-ff merge of Branch B
    commit 4  DECISION_LOG.md and the addendum
    commit 5  reports/2026-08-07T{HHMM}Z_integrate-fierz-and-sign-ruling.md

**Committed report:** everything available before the report commit —
A1–A7, A9-pre, A10 for commits 1–4, the intended final manifest, and the
intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
A8-final at the pushed head; **the final `POST_MERGE` guard's complete
JSON including `observed_operations`**; A9-final; the push; the report
commit's stored message read back from the object; and ancestry
confirmation.

**The final `POST_MERGE` guard is post-report evidence by construction**
— it runs after the push, which runs after the report commit. **The
committed report carries `PRE_MERGE(A)` and `PRE_MERGE(B)` verbatim and
states the INTENDED final `POST_MERGE` parameters**, not its output.
**Do not amend the report to insert evidence whose production depends on
the report commit.**

## 5. Invariants and prohibitions

- Executor-writable: the specification, `DECISION_LOG.md`, the addendum,
  and the report. **Everything arriving by merge is integrated exactly
  as reviewed and may not be edited.**
- **Do not modify either branch's report or derivation note.**
- **Do not perform the freeze repair** — the tenth mutation, the checker
  double-application correction, and pinning `vocab_parser.py` are a
  separate authorized task.
- **Do not delete or rename any branch.**
- Merge commits only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. Merge the pinned remote refs.
- Any merge conflict is an immediate stop.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified. `CONVENTIONS.md`, `AGENTS.md` and `pyproject.toml` are out of
  scope.
- Branch naming: use `gate/p2-integrate-fierz-and-sign-ruling`. The
  policy-versus-practice contradiction remains an open PI item.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- Do not alter any existing worktree containing uncommitted content, and
  do not clean, stash, or discard untracked files anywhere.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A7, A9-pre and A10 in the committed report; **A8,
  A9-final, the push and the report-commit hygiene as post-report
  evidence**;
- **`PRE_MERGE(A)` and `PRE_MERGE(B)` verbatim in the committed
  report**, with the intended final `POST_MERGE` parameters stated;
  **the final `POST_MERGE` JSON verbatim as post-report evidence** —
  all including `observed_operations`;
- both merge commit SHAs, their parents and merge-bases, as distinct
  values;
- the `DECISION_LOG.md` entry and the addendum, quoted;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
