# Task specification — integrate the generator-sum criticality derivation, with a calibration addendum

Specification evidence base: `51d4bbe1a2e965b0793b18f4ead5a11dab54c364`

    Branch  gate/p2-generator-sum-criticality
            84aad96d97bab67f636812939bb00ac917f35273

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization, plus one addendum that must land with
it because a sentence in the reviewed artifacts overstates a
consequence.

**One merge.** Dry run: **6 additions, 0 modifications**, no conflict,
merge-base is the original base. **If a conflict occurs, STOP.**

---

## 0. The result, and the one sentence that needs an addendum

**The derivation's substance is accepted.** The singlet-only control
reproduces `P2-GAP-01` (`1 = 8·G_N·I_0`, channel coupling `G = 4·G_N`,
prefactor 2, `G_c = 1/(2·I_0)`); the full U(N) generator sum gives
`1 = (8/N)·G·I_0` and `G_c = N/(8·I_0)`; the ratio is `N`, equal to 1
only at `N = 1`, which is the correct degeneration since the generator
sum collapses to the singlet interaction there. `P2-GAP-01`'s `PASS`
stands for the form it computed.

**One sentence in the committed artifacts overstates what follows.** The
`verdict` field of
`results/P2-PHASE-01/generator-sum-criticality/criticality.json` ends:

    The exploratory G/G_c positions carry an N/4 factor.

**They do not.** Both gap equations have the form `1 = c·G·I_0(M̂)`. At a
fixed `M̂`, `G(M̂) = 1/(c·I_0(M̂))` and `G_c = 1/(c·I_0(0))`, so

    G/G_c = I_0(0)/I_0(M̂)      in BOTH cases — the prefactor c cancels.

**The map from `G/G_c` to `M̂` is therefore identical**, and the
exploratory study scanned exactly that dimensionless ratio.

**The invariance has a condition, and it must be stated.** It holds
because the generator-sum derivation changes only the overall
gap-equation prefactor and leaves the same regulated `I_0(M̂)`:
`1 = 2·G·I_0(M̂)` becomes `1 = (8/N)·G·I_0(M̂)`. **It would NOT follow
from a change that altered the `M̂`-dependence of the gap equation.**
The addendum must carry this condition. Verified
numerically: solving each gap equation at the same `G/G_c` with `c = 2`,
`c = 8/3` and `c = 4` gives `M̂` agreeing to nine decimal places, and
`M̂ = 1` sits at `G/G_c = 1.769` in all three.

**What does change, and what does not:**

    unchanged     the M-hat versus G/G_c curve
                  the M-hat = 1 crossing at G/G_c = 1.769
                  the 282-row branch-depth table, indexed by G/G_c
                  the drafted parameter domain, expressed in G/G_c

    changed       the value of G_c in terms of I_0 and N:
                    1/(2 I_0)  ->  N/(8 I_0)
                  the absolute coupling G at a given G/G_c: factor N/4

**A related statement that is correct but answers a different
question.** For a FIXED physical `G`, the two dimensionless labels
differ: `(G/G_c)_canonical = (4/N)·(G/G_c)_old`. **That is true.** But
the exploratory study never fixed a physical `G` — it scanned the
dimensionless ratio and solved for `M̂`. **The two statements do not conflict; they are about different
quantities.** **The fixed-physical-`G` conversion does not bear on the
exploratory scan. The prefactor cancellation in the normalised
`G/G_c`-to-`M̂` relation does.** (An earlier draft said "only the second
bears on the exploratory results", which referred to the wrong one.)

**Why this cannot wait for a later task.** Left as it stands, the
verdict would send a later reader to rescale a 282-row table, a
parameter-domain draft and a crossing position that do not need
rescaling. **The correction is cheap now and expensive to undo later.**

**A second, smaller correction.** The reviewed material states that the
singlet is the only condensate the frozen material supports, because an
adjoint condensate would break the frozen U(N) symmetry. **The first
half is right as a statement about the ansatz used; the second does not
follow.** A symmetric action admits symmetry-breaking saddles, and
"would break the symmetry" is not "is not supported by the theory".
**The addendum must state the accurate version: under the
U(N)-symmetric mean-field ansatz this task adopted, only the singlet
condensate is retained; adjoint condensates belong to symmetry-breaking
ansätze and were not analysed. Out of scope must not become
non-existent.**

## 1. Objective

`main` contains the branch's content, integrated by a merge commit with
correct parentage, plus one addendum recording the calibration
correction and the ansatz-scope correction. **The reviewed artifacts are
not edited.**

## 2. The addendum

Land `derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md`
containing:

- the derivation's accepted result, restated in one paragraph;
- **the invariance argument** of §0, algebraically first — the
  cancellation of `c` in `G/G_c = I_0(0)/I_0(M̂)` is the argument, and
  the numerics are a regression check on it, not the proof;
- **the condition under which the invariance holds**, per §0: only the
  overall prefactor changed and `I_0(M̂)` is the same regulated
  function;
- the numerical demonstration at `c = 2`, `c = 8/3`, `c = 4`, **with
  each prefactor labelled** by the `N` it corresponds to;
- **the unchanged/changed table** of §0, verbatim in substance;
- **the fixed-`G` statement**, with the explanation of why it does not
  conflict and why it does not bear on the exploratory results;
- **the ansatz-scope correction**, in the accurate form of §0;
- an explicit statement that **the `verdict` field of the results
  artifact is left as committed**, that this addendum corrects the
  consequence it draws, and that **the artifact's field name
  `exploratory_correction_factor_vs_half_I0` is itself accurate** — it
  names a correction to `G_c`, not to positions.

**Do not edit `criticality.json`, the derivation note, or the report.**
They record what was concluded at the time, and rewriting them destroys
that. **The addendum is how a consequence is corrected here.**

**Reproduce the numerical demonstration yourself, and do not copy the
figures from this specification.**

**Use exactly the regulated `I_0(M̂)`, the cutoff and unit conventions,
and the root prescription of
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` and its
existing implementation. Change ONLY the prefactor `c`.** Without that
constraint two honest executors could pick different regularisations and
report different numbers while the algebraic conclusion held either way
— and the `M̂ = 1` position at `1.769` comes from that specific
regulated integral, not from the cancellation.

**Label the three prefactors, so a later reader does not take them for
three arbitrary models:**

    c = 2      the original exploratory / control prefactor;
               numerically also the canonical prefactor at N = 4
    c = 8/3    canonical, N = 3
    c = 4      canonical, N = 2

Solve at `G/G_c ∈ {1.05, 1.2, 1.4, 1.769, 2.0, 3.0}` for each and report
the `M̂` values. **If the reproduced `M̂` values do not agree across `c`, STOP and do not
write the addendum.** Report the discrepancy, and determine whether the
supposedly common `I_0(M̂)`, the regulator and unit conventions, the
root prescription, or the numerical implementation actually differed.

**A numerical disagreement is evidence that the stated invariance
conditions have not been reproduced. It does not by itself overturn the
algebraic cancellation**, which is an exact identity once the three
cases share one `I_0(M̂)`. **An earlier draft said a disagreement would
mean the invariance argument is wrong — that would convert a failure to
reproduce into a substantive negative result, which is the error class
this programme has already met three times this week.**

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `51d4bbe1a2e965b0793b18f4ead5a11dab54c364`; the source
branch to `84aad96d…`. Any mismatch → STOP. **Local `main` is stale by
design — do not repair it.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §4's commit order it is the specification commit.

    parent 1 = the integration specification commit (commit 1)
    parent 2 = 84aad96d97bab67f636812939bb00ac917f35273
    merge-base(parent 1, parent 2)
             = 51d4bbe1a2e965b0793b18f4ead5a11dab54c364

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push, `remote_check_policy = REQUIRED`.

**The final guard carries TWO DISTINCT SHAs.** The merge object under
verification is the merge commit; remote agreement is checked against
the final report-commit head. **If the guard cannot represent both roles
separately, STOP.**

**A4 — The invariance demonstration reproduced**, per §2, before the
addendum is written. **This gates the addendum: if the `M̂` values
disagree across `c`, do not write it.**

**A5 — Scope, frozen manifest:**

    base: 51d4bbe1a2e965b0793b18f4ead5a11dab54c364
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-GENERATOR-SUM-CRITICALITY_01.md
      derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md
      reports/2026-08-08T2350Z_generator-sum-criticality.md
      reports/2026-08-09T{HHMM}Z_integrate-generator-sum-criticality.md
      results/P2-PHASE-01/generator-sum-criticality/criticality.json
      scripts/p2_generator_sum_criticality.py
      specs/2026-08-08T2350Z_generator-sum-criticality.md
      specs/2026-08-09T{HHMM}Z_integrate-generator-sum-criticality.md
      tests/test_p2_generator_sum_criticality.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 9 additions and 0 modifications.** Six
arrive from the branch; three are authored here. **A tenth path is a
defect, and any modification at all is a defect.**

**A6 — Arriving artifacts intact.** The six arriving additions are
blob-identical to their source-branch values. **In particular
`criticality.json` is unchanged**, verdict field included.

**A7 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`,
`derivations/P2-GAP-01_gap_criticality.md`,
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md`,
`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`,
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`:
blob-identical between base and merged head. **Read from the objects.**

**The exploratory artifacts and the parameter-domain draft are on that
list deliberately.** The addendum's conclusion is that they need no
change; **the integration must demonstrate that none was made.**

**A8 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; **`P2-GAP-01` still `PASS` with no caveat added**;
`P2-PHASE-01` still `PROPOSED`.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_channel_character.py`,
`tests/test_p2_generator_sum_criticality.py`. **A9-pre** at the
pre-report head goes in the report; **A9-final** at the pushed head is
post-report evidence and carries the verdict.

**A10 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.** If
one appears despite pre-commit inspection, STOP before pushing.

**A11 — Branch preserved.** `gate/p2-generator-sum-criticality` still
resolves to `84aad96d…`. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-09T{HHMM}Z_integrate-generator-sum-criticality.md
    commit 2  --no-ff merge of the source branch
    commit 3  derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md
    commit 4  reports/2026-08-09T{HHMM}Z_integrate-generator-sum-criticality.md

**Committed report:** raw output for A1, A2, A4, A6–A8, A9-pre, A10 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A5's final scope check, A9-final, the push,
the report commit's stored message read back from the object, and
ancestry confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the integration specification, the addendum, and
  the integration report. **Everything arriving by merge is integrated
  exactly as reviewed and may not be edited.**
- **Do not edit `criticality.json`, the generator-sum derivation note,
  or its report.** The addendum corrects a consequence; it does not
  rewrite a record.
- **Do not rescale, restate or amend any exploratory result**, the
  branch-depth table, or the parameter-domain draft. **The addendum's
  point is that they need no change.**
- **Do not edit `P2-GAP-01` in any way**, and do not qualify its `PASS`.
- **Do not analyse adjoint condensates.** The addendum records that they
  were not analysed; analysing them is a separate task.
- **Do not update the programme registry.** `0-programme` is a separate
  repository and a separate authorization.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref, not a
  local copy.**
- Any merge conflict is an immediate stop.
- Branch naming: use `gate/p2-integrate-generator-sum-criticality`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- everything listed in §4 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **the invariance demonstration you reproduced**, with the `M̂` values
  at each `c`;
- the addendum quoted in full;
- confirmation that **the base-to-head scope contains zero `M`
  operations and that no pre-existing file was modified**, and that the
  exploratory artifacts and parameter-domain draft are blob-identical;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **whether you agree the exploratory `G/G_c` positions are unaffected**
  — you performed the derivation and are better placed than we are to
  see a step the invariance argument misses. **If you disagree, say so:
  a disagreement here is worth more than a clean integration**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
