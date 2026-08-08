# Task specification — integrate the exponent-mapping ruling

Specification evidence base: `481f4ad77cb4ec92ef9d58471530784087e67a43`

Classification: **MATERIAL**. The source branch completed result review.
This is the integration authorization.

    Branch  fix/exponent-mapping-ruling
            79399dfd26eacb69a0ef0cba8432ec46e2366eea

**One merge.** Dry run: **2 additions, 1 modification**, no conflict,
merge-base is the original base. **If a conflict occurs, STOP**; none is
pre-authorized. The one modification is an append to `DECISION_LOG.md`
with zero deleted lines.

**This is a pure integration.** It merges reviewed content and authors
nothing but its own specification and report. **Two follow-up items are
deferred to a separate task and are named in §0 so they are not lost.**

---

## 0. What is being integrated, and what is deliberately deferred

**Integrated:** the PI ruling that the canonical interaction expression
is written as it appears in the Boltzmann exponent — `S_E = S_E,0 − X`,
hence `g = +2c` — recorded as **supplying a convention the frozen
material never carried**, not as recovering an original intent; and, as
a **separate** `DECISION_LOG.md` entry, the open derivation item that
`P2-GAP-01`'s `G_c = 1/(2·I_0)` is `UNESTABLISHED` for the full
generator-sum interaction.

**Deferred to a follow-up governance task, NOT performed here:**

**(a) The ruling's provenance should be stated more precisely.** The
executor's report established that `P2-GAP-01` does not state in words
that `Σ` is real — its equations treat it so, but the specification
asserted a quotation the material does not contain. **The harder
consistency evidence is `G_c` itself:** `1 = 2·G_c·I_0` with `I_0 > 0`
gives `G_c > 0`, and `P2-GAP-01`'s scalar convention is the attractive
`G > 0` branch. **The follow-up should promote the positive-`G_c`
evidence to the primary constraint and demote the real-`Σ` usage to
supporting evidence.**

**Neither is a derivation.** `P2-GAP-01` states no exponent or action
sign chain, so the correct description remains *a PI-supplied
convention, constrained for consistency by an executed calculation* —
**not** *`P2-GAP-01` proves the exponent mapping*. **The follow-up
strengthens the evidence, it does not upgrade the ruling's epistemic
status.**

**(b) The ruling should be indexed into `CONVENTIONS.md`.** It now
functions as an input convention for every downstream derivation, but it
exists only as a dated `DECISION_LOG.md` entry. **A future executor
consulting `CONVENTIONS.md` and the freeze files would conclude, again,
that the exponent mapping is not defined** — which is precisely the
finding that produced this ruling. The index entry **cites** the ruling;
it does not re-decide it.

**Both are deferred because an integration should merge reviewed content
and nothing else.** `CONVENTIONS.md` is a protected path in this
specification, as it has been in every recent one, and amending it
inside a merge would break that discipline for a change that has had no
review of its own.

**Do not re-run Layer 1b or Layer 2 here**, and do not anticipate their
results. The ruling makes them computable; computing them is a separate
authorized task, and it should follow (b) so that the provenance chain
reads ruling → registry → recomputation.

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
    8  fetch; final POST_MERGE guard with
       remote_check_policy = REQUIRED

**`--no-ff` is mandatory.** The source descends from the base, so an
ordinary merge would fast-forward and produce no merge commit.
**Everything verifiable locally is verified before the push.**

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `481f4ad77cb4ec92ef9d58471530784087e67a43`; the source
branch to `79399dfd…`. Any mismatch → STOP and report the new tip.
**Local `main` is stale by design — do not repair it.** Report all refs
separately, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on; it is not independently selectable.** With §4's commit
order it is the specification commit.

    parent 1 = the integration specification commit (commit 1)
    parent 2 = 79399dfd26eacb69a0ef0cba8432ec46e2366eea
    merge-base(parent 1, parent 2)
             = 481f4ad77cb4ec92ef9d58471530784087e67a43

**The merge-base is the ORIGINAL base**, verified by dry run — the
specification commit descends from it and the source branch was cut from
it.

**A3 — Guards.** `PRE_MERGE` at step 2 and one final `POST_MERGE` at
step 8.

**The final guard carries TWO DISTINCT SHAs.** The final head is the
REPORT commit, not the merge commit. **The merge object under
verification is the merge commit**; **remote agreement is checked
against the final report-commit head.** Report both and label which is
which. **If the guard cannot represent those two roles separately,
STOP** rather than substituting one for the other.

**A4 — Scope, frozen manifest.** The `head` and `{HHMM}` placeholders
are the only permitted substitutions:

    base: 481f4ad77cb4ec92ef9d58471530784087e67a43
    head: <computed final head>
    mode: exact
    add:
      reports/2026-08-08T1634Z_exponent-mapping-ruling.md
      reports/2026-08-08T{HHMM}Z_integrate-exponent-mapping-ruling.md
      specs/2026-08-08T1634Z_exponent-mapping-ruling.md
      specs/2026-08-08T{HHMM}Z_integrate-exponent-mapping-ruling.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 4 additions and 1 modification.** Two
additions arrive from the branch; two are authored here. **A sixth path
is a defect.**

**A5 — `DECISION_LOG.md` arrives intact and append-only.** Blob-identical
to its value on the source branch, and the base-to-head diff contains
**zero deleted lines**. **Both new entries are present and remain
separate top-level entries** — the second must not have become a
subsection of the first through the merge.

**A6 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`pyproject.toml`, `derivations/CANONICAL_INTERACTION.md`,
`derivations/P2-GAP-01_gap_criticality.md`,
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
`results/P2-CHANNEL-FREEZE/fierz_matrix.json` and its `.sha256`, and
every path under `scripts/`, `results/` and `tests/`: blob-identical
between base and merged head. **Read from the objects.**

**`CONVENTIONS.md` is on that list deliberately.** The deferred index
entry of §0(b) belongs to a later task; **this integration must not
anticipate it.**

**A7 — No gate changed.** `GATES.md` blob-identical to the base; `^## P2-`
count 14 before and after; **`P2-GAP-01` still reads `PASS` with no
caveat added**, and `P2-PHASE-01` still `PROPOSED`.

**A8 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`,
`tests/test_p2_channel_character.py`. **A8-pre** at the pre-report head
goes in the report; **A8-final** at the pushed head is post-report
evidence and carries the verdict.

**A9 — Commit-message hygiene** on every commit including the merge
commit: inspect the proposed message before, and the stored message
after; permit no `Co-Authored-By`, no session identifier or URL, no tool
attribution. **Report per commit whether any trailer was suppressed and
which — an authoring-time suppression is a fact to disclose, not an
absence.** If one appears despite pre-commit inspection, STOP before
pushing.

**A10 — Branch preserved.** `fix/exponent-mapping-ruling` still resolves
to `79399dfd…` after the merge. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-08T{HHMM}Z_integrate-exponent-mapping-ruling.md
    commit 2  --no-ff merge of the source branch
    commit 3  reports/2026-08-08T{HHMM}Z_integrate-exponent-mapping-ruling.md

**Committed report:** raw output for A1, A2, A5–A7, A8-pre, A9 for
commits 1–2; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–2 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check at the pushed head,
A8-final, the push, the report commit's stored message read back from
the object, and ancestry confirmation. **Do not amend the report to
insert evidence whose production depends on the report commit.**

## 5. Invariants and prohibitions

- Executor-writable: the integration specification and the integration
  report. **Everything arriving by merge is integrated exactly as
  reviewed and may not be edited.**
- **Do not perform either deferred item of §0.** No `CONVENTIONS.md`
  index entry, no provenance restatement.
- **Do not re-run Layer 1b or Layer 2**, and do not anticipate their
  results in the report.
- **Do not select a Hubbard–Stratonovich channel**, and do not freeze
  `η`, the particle–particle Grassmann ordering, or the diquark
  normalisation.
- **Do not edit `P2-GAP-01`'s gate entry or derivation**, and do not
  qualify its `PASS`.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref, not a
  local copy — local refs in this repository are known to drift.**
- Any merge conflict is an immediate stop, including in
  `DECISION_LOG.md`.
- Branch naming: use `fix/integrate-exponent-mapping-ruling`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- Do not alter any existing worktree containing uncommitted content, and
  do not clean, stash, or discard untracked files anywhere.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- everything listed in §4 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- the `DECISION_LOG.md` merged result: **both entries quoted, shown
  still separate, and the diff shown to contain zero deletions**;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
