# Task specification — integrate the chirality census

Specification evidence base: `8701a97a6bb58550d4300f75c10638b057335731`

    Branch  gate/p2-chirality-census
            e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see §4 commit 2 and A5.

**One merge.** Dry run: **7 additions, 0 modifications**, no conflict,
merge-base is the original base. **If a conflict occurs, STOP.**

**Review artifact delimiters**, each occupying a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

---

## 0. What is being integrated

**A structural explanation of a pattern the programme previously held as
two separate numerical facts.**

    The V/A-only support of the frozen interaction is a
    chirality-selection consequence, not an accidental Fierz
    cancellation.

**The argument survived a real falsification test.** Three predictions
were recorded in the derivation note **before** the computing script was
committed, and all three held:

    frozen  S^2 + P^2        census one-of-each   -> V, A only
    no-i    S^2 + (g5)^2     census doubled       -> S, P, T only
    P^2 alone                census mixed         -> nothing excluded

**The third case is the one that matters most**, and the executor's
reason for choosing it should not be lost: *a criterion that only ever
forbids things can look successful without discriminating.* **The
no-exclusion branch is where a criterion fitted after seeing the answer
would most likely fail**, so that is the branch worth testing.

**Representation independence confirmed** in two constructions.

## 1. Two corrections the branch made to the specification's own claims

**Both are recorded because the specification asserted them and was
wrong.**

**(a) The factorisation is an OPERATOR statement, not a tensor
identity.** The specification asked for verification of
`S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)`. **On the ordered rank-4 tensor that is
false** — the residual against `4·P_R⊗P_L` is 2. **The correct tensor
form is `2[P_R⊗P_L + P_L⊗P_R]`.** The factor-four form holds at operator
level because the two bilinears are Grassmann-even and commute.

**This distinction belongs in the record.** Operator algebra and ordered
tensor representation are easy to conflate, and **this specification's
predecessor conflated them.**

**(b) The "inversion" is in the field labels, not the projector
algebra.** The specification described the particle–hole and
particle–particle classifications as inverted. **The two projector
tables have IDENTICAL non-zero patterns.** What differs is the bar-flip
`ψ̄_L = ψ̄ P_R` on the particle–hole side and **its absence on the
particle–particle side** — and **`C γ₅^T C⁻¹ = +γ₅` is what delivers
that absence.** Had it been `−γ₅`, the pp side would have flipped too
and the two classifications would have **agreed** in field labels.

**That sign is load-bearing**, and the specification did not know it.

## 2. What this establishes, in three layers

**Layer 1 — settled.** For the frozen `S² + P²`, the V/A support is
determined by chirality structure. **The families that must vanish can
be predicted before any decomposition is performed.**

**Layer 2 — settled, and more precise than the specification's
account.** Both pairings select V/A, **but not because they share a
chirality classification.** §1(b) gives the actual mechanism.

**Layer 3 — NOT settled, and this integration must not blur it.** The
census explains **support only**. It does not explain:

    why V = +A in particle-hole but V = -A in particle-particle
    any coefficient magnitude
    any absolute attractive/repulsive character

**Those remain with the unfrozen conventions** — `η`, the
particle–particle Grassmann ordering, the diquark normalisation.

## 3. What this integration does NOT establish

- **It does not settle the diquark channel.** The particle–particle side
  was tested **structurally only** — no coefficient decomposition, no
  slot map — precisely because the ordering is unfrozen. **The two
  branches carrying pp coefficients remain unintegrated.**
- **The evidence is not symmetric between channels.**
  Particle–hole has structural selection *and* numerical falsification;
  **particle–particle has structural selection only.**
- **It says nothing about composite states.** This is an argument about
  which operators can form, **not a bound-state calculation.**
- **It selects no Hubbard–Stratonovich channel** and revisits no ruling.
- **No gate status, no new programme coefficient.** Coefficients in the
  artifacts are **diagnostic reproductions** used to test the
  explanation.

**One unresolved minor difference, recorded rather than suppressed.** An
independent spot-check of the third test case reproduced four of the
five family coefficients and **differed in the sign of `P`**. **It does
not bear on that case's verdict** — the prediction was that no family is
excluded, and both computations agree all five are non-zero. **It is
recorded as unresolved, not as agreement.**

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-chirality-census.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-chirality-census.md
    commit 3  --no-ff merge of the source branch
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-chirality-census.md

**Commit 2 precedes the merge**, per Rule 15's timing clause.

**Committed report:** raw output for A1, A2, A6–A9, A10-pre, A11 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A10-final, the
push, the report commit's stored message read back from the object, and
ancestry confirmation.

## 5. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `8701a97a6bb58550d4300f75c10638b057335731`; the source
branch to `e4bea1c9…`. Any mismatch → STOP. **Local `main` is stale by
design.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §4's commit order the merge follows the review
commit, **so parent 1 is the review commit, not the specification
commit.**

    parent 1 = the integration pre-execution review commit (commit 2)
    parent 2 = e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb
    merge-base(parent 1, parent 2)
             = 8701a97a6bb58550d4300f75c10638b057335731

**Commit 1 MUST be an ancestor of parent 1.** Verify and report that
too.

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push. **The final guard carries TWO DISTINCT SHAs**: the merge
object is the merge commit; remote agreement is checked against the
final report-commit head. **If the guard cannot represent both roles
separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 8701a97a6bb58550d4300f75c10638b057335731
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-PHASE-01_chirality_census.md
      reports/2026-08-11T1134Z_chirality-census.md
      reports/2026-08-XXT{HHMM}Z_integrate-chirality-census.md
      results/P2-PHASE-01/chirality-census/census.json
      reviews/chatgpt/2026-08-11T1134Z_chirality-census.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-chirality-census.md
      scripts/p2_chirality_census.py
      specs/2026-08-11T1134Z_chirality-census.md
      specs/2026-08-XXT{HHMM}Z_integrate-chirality-census.md
      tests/test_p2_chirality_census.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 10 additions and 0 modifications**, matching
the ten paths above. Seven arrive from the branch; three are authored
here.

**A5 — This task's pre-execution review committed, unedited**, at
`reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-chirality-census.md`,
**byte-identical to the text between the delimiter literals at the head
of this specification, excluding the delimiter lines, any preamble
before the BEGIN line, and any accompanying instruction.**

**Match the delimiters as COMPLETE LINES**, not as first occurrences —
this specification contains them. **Placeholders inside the review's
text stay as written**; resolve them in the path only. **If the supplied
text is missing, has no delimiters, or does not correspond to this
specification, STOP and say which.**

**A6 — Arriving artifacts intact.** The seven additions arriving from
the source branch are blob-identical to:

    derivations/P2-PHASE-01_chirality_census.md
    b8a403aecb86e0aca6d029454b63e099d3f98145

    reports/2026-08-11T1134Z_chirality-census.md
    b7c521d3d5d2f0b0b66977435d7956d235098973

    results/P2-PHASE-01/chirality-census/census.json
    31c8d7012938438b13f16b26f98c41be842b5da0

    reviews/chatgpt/2026-08-11T1134Z_chirality-census.md
    9b331993bdcecd69a915da88b191275f507e7f93

    scripts/p2_chirality_census.py
    eb02aebc3a53f905d37f224423a5c07e700aa47b

    specs/2026-08-11T1134Z_chirality-census.md
    b6529e4b86917b0f94db3ed95086e89ccc73ec02

    tests/test_p2_chirality_census.py
    17513abecb0f8f55e5a98ae63c68b8e6680799de

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**A7 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`, and **every path under `scripts/`,
`results/`, `tests/`, `derivations/`, `docs/` and `reviews/` that exists
at the evidence base**: blob-identical between base and merged head.
**Compare path by path, not as tree objects** — several directories gain
base-absent authorised paths.

**`tests/` gains exactly one arriving file and no existing test is
modified.**

**A8 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; `P2-PHASE-01` still `PROPOSED`; `P2-GAP-01` still
`PASS`.

**A9 — The unintegrated diquark branches untouched.**
`gate/p2-diquark-both-eta` still resolves to `bc1e5c74…` and
`gate/p2-diquark-adjudication` to `3767973b…`. **Neither is merged by
this task**, and **nothing in the merged state may present their
coefficients as main-line results.**

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, `tests/test_p2_channel_character.py`,
`tests/test_p2_chirality_census.py`. **A10-pre** at the pre-report head
goes in the report; **A10-final** at the pushed head is post-report
evidence.

**A11 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

**A12 — Branches preserved.** The source branch still resolves to
`e4bea1c9…`; **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 6. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
merge `main` will carry a chirality selection rule, a particle–hole
coefficient table, and a structural particle–particle classification.
**A reader could conclude the diquark channel's character is
determined.** **It is not** — §2's Layer 3 lists what the census does
not explain, and **the coefficients that would settle it are on two
unintegrated branches under three unfrozen conventions.**

## 7. Invariants and prohibitions

- Executor-writable: the integration specification, its pre-execution
  review, and the integration report. **Everything arriving by merge is
  integrated exactly as reviewed and may not be edited.**
- **Do not merge or read from either diquark branch.**
- **Do not state that the diquark channel is settled**, that a composite
  state exists or is absent, or that the two channels are equally
  tested.
- **Do not present the census as explaining coefficient signs or
  magnitudes.** §2's Layer 3 governs.
- **Do not resolve the `P`-sign difference of §3.** It is recorded as
  unresolved; **resolving it is a separate task if it is ever worth
  one.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref.**
- Any merge conflict is an immediate stop.
- Branch naming: use `gate/p2-integrate-chirality-census`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 8. Report contract

- everything listed in §4 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **A6's blob comparison for all seven arriving artifacts**;
- **A7's path-by-path comparison**, with the count of pre-existing paths
  checked;
- confirmation that both diquark branches remain at their recorded
  commits and are not ancestors of the merged head;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **§6's Rule 16 assessment**, junction named or search described;
- **whether the merged state reads as though the census explains
  coefficient signs**, or as though the particle–particle side were
  numerically tested. **Neither is true**, and §2 Layer 3 and §3 say so;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 9. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      the source branch at e4bea1c9…
    method      git rev-parse <rev>:<path>, and a dry-run merge
    check type  GIT OBJECT IDENTITY, and numerical re-verification

    CONFIRMED   dry-run merge: 7 additions, 0 modifications, no
                conflict, merge-base 8701a97a…
    CONFIRMED   the seven blob ids of A6, read from the branch
    CONFIRMED   S^2 + P^2 vs 4*P_R(x)P_L        -> FALSE
    CONFIRMED   S^2 + P^2 vs 2*[P_R(x)P_L + P_L(x)P_R] -> TRUE
                which is §1(a)'s correction, re-verified independently

**The `P`-sign difference of §3 was found in the author's own
spot-check** and is **not** claimed to be an error on either side.
