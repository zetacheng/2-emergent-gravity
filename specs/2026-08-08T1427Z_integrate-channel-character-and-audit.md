# Task specification — integrate the channel-character derivation and the normalisation audit

Specification evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`

Classification: **MATERIAL**. Both sources completed result review. This
is the integration authorization.

    Branch A  gate/p2-channel-character
              cb604a4e3a96f9120787a685120f205d8e4c7c88
    Branch B  fix/normalisation-audit-g-omega
              9c6ff5b3ed8c0071abed058c4567f4b50c974d76

**No conflict expected** — verified by dry run: **11 additions, 0
modifications**, disjoint path sets, no shared file. **If a conflict
occurs, STOP**; none is pre-authorized. Both merge-bases are the
original base.

---

## 0. What is being integrated

**Branch A** delivers the channel character of the Fierz-induced
interaction in three layers, with two of them deliberately withheld:

- **Layer 1a, unconditional:** scalar singlet `+G/(2N)` and induced V
  and A singlets `−G/4` in the λ⁰-bilinear normalisation
  (`+G/N²` and `−G/(2N)` in the plain-bilinear normalisation). **Signs
  are opposite; magnitudes are only comparable within one
  normalisation.**
- **Layer 1b:** `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN
  MATERIAL` — the mapping from the interaction expression into the
  Boltzmann exponent is not frozen, and both branches were computed.
- **Layer 2:** `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN
  MATERIAL`.

It also establishes that the diquark channel's obstruction is **not** the
charge-conjugation matrix — `C` is unique up to a scalar that cancels in
the paired product — but the un-frozen `η` in `ψ̄^c = η ψ^T C⁻¹`, the
particle–particle Grassmann ordering, and the diquark normalisation.

**Branch B** produces one row of the evidence table that
`CANONICAL_INTERACTION.md` requires for its own ratification: the
apparent `G_ω = −G/N` versus `−G/(2N)` gap is a **`NORMALISATION
MAPPING`**, not a defect. Paper 3 writes `L_V = (G_V/2) J_μJ^μ`, and at
line 189 of its note writes the `J·J` coefficient explicitly as
`−(G/2N)` — the same number, the same normalisation, before naming
`G_ω`. Agreement holds at every intermediate level, not only the
endpoint.

**Withheld verdicts are results.** Layer 1b and Layer 2 returning
`NOT DEFINED` is what this programme wanted to learn: it names
conventions that are missing. **The Euclidean exponent mapping bears
directly on an `OPEN-AC-1` decision; the three diquark-definition gaps
are unresolved inputs whose governance placement is not settled here.**

**What remains open, and must not be read as closed by this
integration:**

- `CANONICAL_INTERACTION.md` keeps its `DRAFT v0.5` banner. **One row of
  its evidence table exists; the others do not.**
- **Four conventions are now known to be missing**: the Euclidean
  exponent mapping, `η`, the particle–particle Grassmann ordering, and
  the diquark normalisation. **This integration freezes none of them.**
- `OPEN-AC-1` is narrowed, not answered. **No Hubbard–Stratonovich
  channel is selected here.**

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

**`--no-ff` is mandatory at both merges.** Both sources descend from the
base, so an ordinary merge would fast-forward and produce no merge
commit. **Everything verifiable locally is verified before the push.**

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `eb88a2c9174cfda746c266924e741a6f88134234`; Branch A to
`cb604a4e…`; Branch B to `9c6ff5b3…`. Any mismatch → STOP and report the
new tip. **Local `main` is stale by design — do not repair it.** Report
all refs separately, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on; it is not independently selectable.** With §4's commit
order, parent 1 of merge A is the specification commit.

    Merge A   parent 1 = the integration specification commit (commit 1)
              parent 2 = cb604a4e3a96f9120787a685120f205d8e4c7c88
              merge-base(parent 1, parent 2)
                       = eb88a2c9174cfda746c266924e741a6f88134234

    Merge B   parent 1 = the merge-A commit
              parent 2 = 9c6ff5b3ed8c0071abed058c4567f4b50c974d76
              merge-base(parent 1, parent 2)
                       = eb88a2c9174cfda746c266924e741a6f88134234

**Both merge-bases are the ORIGINAL base**, verified by dry run. Report
both merges with parents and merge-bases as distinct values.

**A3 — Guards.** `PRE_MERGE(A)` at step 2, `PRE_MERGE(B)` at step 4, and
one final `POST_MERGE` at step 10.

**The final guard carries TWO DISTINCT SHAs.** The final head is the
REPORT commit, not a merge commit. **The merge object under verification
is the Merge-B commit**; **remote agreement is checked against the final
report-commit head.** Report both and label which is which. **If the
guard cannot represent those two roles separately, STOP** rather than
substituting one for the other.

**A4 — Scope, frozen manifest.** The `head` and `{HHMM}` placeholders
are the only permitted substitutions:

    base: eb88a2c9174cfda746c266924e741a6f88134234
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-NORMALISATION-AUDIT_g_omega.md
      derivations/P2-PHASE-01_channel_character.md
      reports/2026-08-08T1321Z_channel-character.md
      reports/2026-08-08T1354Z_normalisation-audit.md
      reports/2026-08-08T{HHMM}Z_integrate-channel-character-and-audit.md
      results/P2-PHASE-01/channel-character/channel_character.json
      results/P2-PHASE-01/normalisation-audit/g_omega_audit.json
      scripts/p2_channel_character.py
      scripts/p2_normalisation_audit.py
      specs/2026-08-08T1321Z_channel-character.md
      specs/2026-08-08T1354Z_normalisation-audit.md
      specs/2026-08-08T{HHMM}Z_integrate-channel-character-and-audit.md
      tests/test_p2_channel_character.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 13 additions and 0 modifications.** Eleven
arrive from the two branches; two are authored here. **A fourteenth path
is a defect, and any modification at all is a defect** — neither branch
changes an existing file.

**A5 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`,
`derivations/CANONICAL_INTERACTION.md`,
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
`results/P2-CHANNEL-FREEZE/fierz_matrix.json` and its `.sha256`,
`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py`,
`scripts/P2-CHANNEL-FREEZE/vocab_parser.py`: blob-identical between base
and merged head. **Read from the objects.**

**`CANONICAL_INTERACTION.md` is on that list deliberately.** Branch B
produces evidence about it and must not have altered it, banner
included.

**A6 — Arriving content intact.** The eleven arriving additions are
present and blob-identical to their source-branch values. Verify by
comparison against the branch tips.

**A7 — No gate changed.** `GATES.md` blob-identical to the base; `^## P2-`
count 14 before and after; `P2-PHASE-01` still `PROPOSED`.

**A8 — Nothing outside the manifest.** No path added, deleted, renamed
or type-changed anywhere except the thirteen of A4.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`,
`tests/test_p2_channel_character.py`,
`tests/test_channel_freeze_phase_a.py`,
`tests/test_channel_freeze_mutations.py`. **A9-pre** at the pre-report
head goes in the report; **A9-final** at the pushed head is post-report
evidence and carries the verdict.

**A10 — Commit-message hygiene** on every commit including both merge
commits: inspect the proposed message before, and the stored message
after; permit no `Co-Authored-By`, no session identifier or URL, no tool
attribution. **Report per commit whether any trailer was suppressed and
which — an authoring-time suppression is a fact to disclose, not an
absence.** If one appears despite pre-commit inspection, STOP before
pushing.

**A11 — Branches preserved.** Both source branches still resolve to
their pinned commits after the merge. **`review/role-model-and-executors`
@ `10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-08T{HHMM}Z_integrate-channel-character-and-audit.md
    commit 2  --no-ff merge of Branch A
    commit 3  --no-ff merge of Branch B
    commit 4  reports/2026-08-08T{HHMM}Z_integrate-channel-character-and-audit.md

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
- **Do not freeze any of the four missing conventions**, and do not
  select a Hubbard–Stratonovich channel. **The HS-channel decision
  remains `OPEN-AC-1` and belongs to the PI.** The Euclidean exponent
  mapping bears on it directly. **The three diquark-definition gaps —
  `η`, the particle–particle Grassmann ordering, and the diquark
  normalisation — are unresolved inputs exposed by the channel-character
  derivation; this integration does NOT assign them to any governance
  item and does not close them.** An integration must not add a
  governance interpretation the results did not carry.
- **Do not modify `CANONICAL_INTERACTION.md` or remove its banner.**
- **Do not upgrade any withheld verdict.** Layer 1b and Layer 2 stand as
  `NOT DEFINED`; an integration is not the place to decide them.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commits only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote refs, not
  local copies — local refs in this repository are known to drift.**
- Any merge conflict is an immediate stop.
- Branch naming: use `gate/p2-integrate-channel-character-and-audit`.
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
- confirmation that **zero files were modified** — this integration is
  additive only, and a single modification would be a finding;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
