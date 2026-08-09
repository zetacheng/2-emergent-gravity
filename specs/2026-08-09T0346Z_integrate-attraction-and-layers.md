# Task specification — integrate the attraction/repulsion ruling and the Layer 1b / Layer 2 recomputation

Specification evidence base: `3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`

    Branch  gate/p2-attraction-ruling-and-layers
            878b632ced8caa5ef2c6255022a44291d50ccfe2

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**One merge.** Dry run: **6 additions, 1 modification**, no conflict,
merge-base is the original base. The one modification appends a single
entry to `DECISION_LOG.md` with zero deleted lines. **If a conflict
occurs, STOP.**

---

## 0. What is being integrated

A PI ruling assigning **ATTRACTIVE** to `g > 0` and **REPULSIVE** to
`g < 0`, and the recomputation it unblocks:

    channel                 c [L]        g [L]      real HS   label
    scalar singlet          +G/(2N)      +G/N       yes       ATTRACTIVE
    induced V singlet       −G/4         −G/2       no        REPULSIVE
    induced A singlet       −G/4         −G/2       no        REPULSIVE

The Layer-1a control reproduced every pinned coefficient with exact
symbolic difference zero, and the scalar control returned ATTRACTIVE
consistent with `P2-GAP-01`.

**This closes two verdicts that the channel-character derivation
deliberately withheld** — `REAL-HS ADMISSIBILITY NOT DEFINED` and
`ATTRACTIVE/REPULSIVE NOT DEFINED`. **Withholding them was correct at
the time; both blockers have since been ruled on.**

**The rulings are consumed, not merely cited.** The script parses both
from `DECISION_LOG.md`. **Removing either would stop the computation,
not merely change a label** — which is what the specification's final
report question was written to test.

**What this does NOT establish, recorded so a later reader does not
infer it:**

- **Nothing about whether a composite vector exists.** A
  channel-character label is not a bound-state or pole calculation, and
  the ruling forbids that inference explicitly. **`REPULSIVE` in a
  `ψ̄ψ` channel does not imply a composite vector is absent.**
- **Nothing about whether condensation occurs.** That depends on the
  full quadratic kernel `Γ⁽²⁾(0) = 1/g − Π(0)`, the fermion determinant,
  stability, and the critical coupling.
- **Nothing about the particle–particle channel.** `η`, the
  particle–particle Grassmann ordering, and the diquark normalisation
  remain unfrozen; **the two rulings supply a mapping and a naming
  convention, neither of which is a particle–particle operator
  definition.** The channel picture is not complete.
- **No Hubbard–Stratonovich channel is selected.** `OPEN-AC-1` is
  narrowed by evidence, not decided.
- **Nothing about `G_c`.** The generator-sum critical coupling does not
  enter this computation, and no reconciliation with it was attempted or
  is implied.

## 1. Objective

`main` contains the branch's content, integrated by a merge commit with
correct parentage. Nothing else on `main` changes.

## 2. Sequence

    1  fetch; verify refs (A1); create a local integration branch
       from the base
    2  PRE_MERGE guard
    3  --no-ff merge the source branch
    4  on the UNPUSHED pre-report head: A5, A6, A7, A8-pre
    5  commit the integration report, carrying the step-4 evidence
    6  any remaining locally-verifiable checks at the final head
    7  push only if every check at steps 4 and 6 passed
    8  fetch; final POST_MERGE guard, remote_check_policy = REQUIRED

**`--no-ff` is mandatory.** The source descends from the base.
**Everything verifiable locally is verified before the push.**

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`; the source
branch to `878b632c…`. Any mismatch → STOP. **Local `main` is stale by
design — do not repair it.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §4's commit order it is the specification commit.

    parent 1 = the integration specification commit (commit 1)
    parent 2 = 878b632ced8caa5ef2c6255022a44291d50ccfe2
    merge-base(parent 1, parent 2)
             = 3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push.

**The final guard carries TWO DISTINCT SHAs.** The merge object under
verification is the merge commit; remote agreement is checked against
the final report-commit head. **If the guard cannot represent both roles
separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-PHASE-01_channel_character_layers.md
      reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
      reports/2026-08-09T{HHMM}Z_integrate-attraction-and-layers.md
      results/P2-PHASE-01/channel-character-layers/layers.json
      scripts/p2_channel_character_layers.py
      specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
      specs/2026-08-09T{HHMM}Z_integrate-attraction-and-layers.md
      tests/test_p2_channel_character_layers.py
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 8 additions and 1 modification.** Six
additions arrive from the branch; two are authored here. **A tenth path
is a defect.**

**A5 — `DECISION_LOG.md` arrives intact and append-only.**
Blob-identical to its source-branch value; the base-to-head diff
contains **zero deleted lines**; and the attraction/repulsion entry is
present as a top-level `## ` entry. **The two earlier 2026-08-08 entries
— the Euclidean exponent mapping and the generator-sum open item — must
still be present and unaltered.**

**A6 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`pyproject.toml`, `derivations/P2-GAP-01_gap_criticality.md`,
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
`derivations/P2-PHASE-01_channel_character.md`,
`results/P2-PHASE-01/channel-character/channel_character.json`,
`scripts/p2_channel_character.py`,
`derivations/P2-GENERATOR-SUM-CRITICALITY_01.md` and its addendum,
`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`,
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`:
blob-identical between base and merged head. **Read from the objects.**

**The channel-character artifacts are on that list deliberately.** This
task closes two verdicts they recorded as `NOT DEFINED`; **it must not
edit them to say so.** The new derivation supersedes those verdicts by
being later evidence, not by rewriting the earlier record.

**A6a — Arriving artifacts intact.** The six additions arriving from
`gate/p2-attraction-ruling-and-layers @ 878b632c…` are present at the
merged head and **blob-identical to their source-branch values**. Verify
each by Git object comparison against these blob ids:

    derivations/P2-PHASE-01_channel_character_layers.md
    55e60b2f072edab7504920ae9fbb8cdf16f0fea1

    reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
    5c22cee6355bdde3798697ede98b06249a04dcc4

    results/P2-PHASE-01/channel-character-layers/layers.json
    73ae5a522a37c310dcee797d24035a5cbc7f6443

    scripts/p2_channel_character_layers.py
    68ba9bb87a6600c8ae0b34972b26c1eafba8007f

    specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
    3a18acd22bfded37c13f6968090e143ebb4fc86f

    tests/test_p2_channel_character_layers.py
    9d863215731f98fb4fe0a87e5b37dfc1930fa231

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**In particular the derivation note, script, results artifact, test
file, source-task specification and source-task report are not edited
during integration.** §5 states that arriving content may not be edited;
**without this criterion that statement had no independent
verification** — an edited arriving file would still be an `A`
operation, would still satisfy A4's path set, and might not be caught by
any test.

**A7 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; `P2-PHASE-01` still `PROPOSED`; `P2-GAP-01` still
`PASS`.

**A8 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_channel_character.py`,
`tests/test_p2_generator_sum_criticality.py`,
`tests/test_p2_channel_character_layers.py`. **A8-pre** at the
pre-report head goes in the report; **A8-final** at the pushed head is
post-report evidence and carries the verdict.

**A9 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.** If
one appears despite pre-commit inspection, STOP before pushing.

**A10 — Branch preserved.** `gate/p2-attraction-ruling-and-layers`
still resolves to `878b632c…`. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-09T{HHMM}Z_integrate-attraction-and-layers.md
    commit 2  --no-ff merge of the source branch
    commit 3  reports/2026-08-09T{HHMM}Z_integrate-attraction-and-layers.md

**Committed report:** raw output for A1, A2, A5, A6, A6a, A7, A8-pre, A9 for
commits 1–2; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–2 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A8-final, the push,
the report commit's stored message read back from the object, and
ancestry confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the integration specification and the integration
  report. **Everything arriving by merge is integrated exactly as
  reviewed and may not be edited.**
- **Do not edit the channel-character derivation, its results artifact,
  or its script** to reflect that its withheld verdicts are now
  resolved. Later evidence supersedes; it does not rewrite.
- **Do not select a Hubbard–Stratonovich channel**, and do not freeze
  `η`, the particle–particle Grassmann ordering, or the diquark
  normalisation.
- **Do not state or imply that a composite vector is absent**, that
  condensation occurs, or that the channel picture is complete.
- **Do not update the programme registry.** Changing the
  `Sign convention for attraction and repulsion` row from `NOT DEFINED`
  is a `0-programme` task and follows this one.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref, not a
  local copy.**
- Any merge conflict is an immediate stop, including in
  `DECISION_LOG.md`.
- Branch naming: use `gate/p2-integrate-attraction-and-layers`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- everything listed in §4 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **the three 2026-08-08 `DECISION_LOG.md` entries listed by heading**,
  shown all present and all top-level, with the zero-deletion diff;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **whether anything in the merged state now reads as though the
  composite-vector question, the condensation question, or the diquark
  channel had been settled.** Three rulings and four derivations have
  landed on this topic in two days, and **the risk is no longer a wrong
  number but a reader assembling a stronger conclusion than any single
  artifact states**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
