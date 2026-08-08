# Task specification — channel character of the Fierz-induced interaction: attractive or repulsive

Specification evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Both deliverables are DERIVATIONS.** Neither decides a physics
question that the repository has not already decided, and neither
selects a Hubbard–Stratonovich channel — that remains `OPEN-AC-1` and
belongs to the PI.

**`P2-PHASE-01` remains `PROPOSED`.** Nothing here registers a gate,
changes a status, adopts a prerequisite draft, or reaches an
admissibility verdict.

---

## 0. What is established, and the question this asks

The landed Fierz verification established, for the frozen canonical
S+P interaction under the 2026-08-07 sign ruling:

- **S, P and T vanish exactly**; only V and A are induced;
- **V and A are equal, purely singlet**, with operator-level coefficient
  `−G/4` each;
- the exchanged form is **purely left-right**: `LL = RR = 0`.

**What is not established is whether that induced interaction is
attractive or repulsive**, and that is what this task computes. It
matters because it bears on whether a composite vector can form —
Paper 3's subject — and because it constrains, without deciding, the
`OPEN-AC-1` channel choice.

**An exploratory calculation on our side is reported here as a QUESTION,
not an answer.** It suggested that with the scalar singlet coefficient
`+G/N²` and the induced vector singlet coefficient `−G/4`, writing
`c·J² = (g/2)·J²`: the scalar channel gives `g > 0` (real HS field
admissible, `U''(0) > 0`) while the vector channel gives `g < 0` (no
real HS field, `U''(0) < 0`). **If your calculation disagrees, your
calculation is the evidence.** Report the disagreement rather than
reproducing the expectation.

**A second exploratory attempt failed and is reported so you do not
repeat it.** A diquark-channel projection returned zero in all four
families — an implausible result that most likely reflects a wrong
projector construction, and which additionally required choosing a
charge-conjugation matrix that the frozen material does not define. **It
is reported as a failed attempt, not as a finding.**

## 1. Objective

Paper 2 carries a derivation determining, under the frozen conventions,
**the algebraic channel character of the Fierz-induced singlet V and A
interactions, and whether the frozen material is sufficient to assign
attractive/repulsive labels to them**; and a determination of whether
the particle–particle (diquark) channel is computable at all from what
is frozen.

**The second clause is not a hedge.** Whether the repository can support
that label is itself a result, and reporting that it cannot is a
successful outcome.

## 2. Derivation (a) — channel character of the induced V and A

**Report the result in THREE LAYERS, and do not collapse them.**
Each depends on strictly more frozen material than the one before, and
the repository may support the first without supporting the later ones.

**Layer 1a — the frozen algebraic coefficient. Unconditional.**
Report `c` as it appears in the frozen interaction expression for the
scalar singlet, the induced V singlet and the induced A singlet:
its sign, its normalisation, and the expression it was read from.
**This requires no knowledge of how that expression enters the
Euclidean exponent.**

**Layer 1b — the exponent / HS coefficient. Conditional on the
mapping.** The Hubbard–Stratonovich identity
`exp[(g/2)J²] = ∫dΦ exp[−Φ²/(2g) + ΦJ]` converges only for `g > 0`, but
**`g` is an EXPONENT-level quantity and is not `2c`.** If the frozen
expression is a term of `S_E`, the Boltzmann weight carries
`exp[−S_E] ⊃ exp[−cJ²]` and the HS coefficient is `−2c`; if the
expression already sits in the exponent, it is `+2c`. **The two differ
by a sign, so real-HS admissibility cannot be reported without the
mapping.**

**Search the frozen material for how the canonical interaction enters
the Boltzmann exponent, and quote what you find.**

- **If the mapping IS fixed**: report `g` for each channel and whether a
  real linear HS field is admissible.
- **If it is NOT fixed**: report
  `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL`, and report
  Layer 1a in full regardless. **An earlier draft asked for the HS sign
  unconditionally while elsewhere admitting the mapping might not be
  frozen; those two could not both be satisfied.**

**Layer 2 — the physical label, which may not be available.** "Attractive"
and "repulsive" are claims about two-body forces and bound states, and
**real-HS admissibility is not the same statement** even when Layer 1b
resolves: a negative `g` forces an imaginary HS contour, which is not by
itself the absence of an interaction in that channel.

**Layer 2 therefore requires MORE than Layer 1b**, not merely the same
information relabelled.

- **If the frozen material fixes the exponent mapping AND its scalar
  usage is the same physical definition `P2-GAP-01` means by
  "attractive"**, then apply the labels and say on what basis.
- **Otherwise report `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN
  MATERIAL`** — and still report Layers 1a and 1b in full. **Layer 1a is
  the unconditional deliverable; Layers 1b and 2 are each conditional on
  the frozen material supporting them.**

**`U''(0)` is NOT an independent second route, and an earlier draft of
this specification wrongly presented it as one.** For the bare quadratic
term `U(Φ) = Φ²/(2g)`, `U''(0) = 1/g` — the same sign test restated. For
the fermion-integrated effective potential, `U''(0) = 1/g − Π(0)`, whose
sign **changes with the coupling**: an attractive scalar channel still
has `U''(0) > 0` below `G_c`. **So `attractive ⇔ U''(0) > 0` is simply
false.**

If you compute a curvature, state which one and treat it accordingly:
the bare curvature is the HS sign test restated and **must not be
reported as corroboration**; the full curvature is an
instability/condensation diagnostic, **not an attraction diagnostic**.

**Include the SCALAR channel as a control, not as an afterthought.**
`P2-GAP-01` found a critical coupling in the scalar channel, so a
correct calculation must return the attractive sign there. **If your
machinery returns anything else for the scalar channel, STOP** — the
sign chain is wrong and the vector result cannot be trusted either.

**Calibrate the control against the operator `P2-GAP-01` actually
used**, pinned in A1: it states an attractive scalar `ψ̄ψ` channel and
the normalisation `L_int = G_N(ψ̄ψ)²` with `G = 4·G_N`. **Confirm you are
testing the same operator, the same internal normalisation and the same
factor-of-two convention.** Do not take a scalar singlet coefficient
from this specification as given — **a control calibrated against a
different operator is not a control.**

**State the convention dependence explicitly.** The result depends on
the Euclidean signature and on the 2026-08-07 ruling that `s_G = −1` is
applied once at operator use. **Say what would change if that ruling
were reversed.**

**Report what this does and does not establish about a composite
vector.** A repulsive `ψ̄ψ` channel does not by itself exclude a bound
state in some other channel. **Do not write that Paper 3's massive
composite vector is excluded** — that would be a claim about a channel
this derivation does not examine.

## 3. Derivation (b) — is the diquark channel computable?

**This is an executability determination first, and a computation only
if it passes.**

A particle–particle (diquark) rearrangement pairs the fermions
differently and requires a **charge-conjugation matrix** `C` satisfying
`C γ_μ^T C⁻¹ = −γ_μ` under the frozen conventions.

**Determine whether `C` is fixed by the frozen material.** Our search
found no charge-conjugation convention in
`P2-CHANNEL-FREEZE-01_phaseA_freeze.md` or `CANONICAL_INTERACTION.md`.
**Verify this yourself.**

- **If `C` IS determined**: perform the diquark rearrangement, report the
  induced coefficients per family, and apply the same
  attractive/repulsive criterion as in (a).
- **If `C` is NOT determined by the frozen material, do NOT stop
  there.** Absence of a frozen `C` is not the same as an undetermined
  result. Work through these in order:

      0  are ALL operator definitions needed to build the
         particle-particle bilinear fixed or convention-independent —
         not only C, but the charge-conjugated field definition, the
         bilinear and Grassmann ordering, and the diquark operator
         normalisation?
      1  is C fixed by the frozen material?
      2  if not, does the defining relation fix C up to a phase or
         normalisation that cannot affect the channel coefficients?
      3  if so, do ALL admissible C give the same channel character?
      4  only if the result genuinely depends on the unfixed choice is
         it UNRESOLVED

  **Report `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` only at step
  4**, and show the dependence that forces it. **If steps 2–3 give a
  convention-independent answer, that answer stands** and is worth more
  than a frozen convention would have been. **Do not select a `C` in
  order to get a number.**

  **Step 0 matters as much as the rest:** a settled `C` does not license
  supplying the remaining diquark conventions yourself. **A blocked (b)
  is a satisfactory outcome and does not block (a).**

**Whether `C` should be frozen, and to what, is a PI decision this task
informs and does not take.**

## 4. Acceptance criteria

**A0 — Commit order.** Commit 1 is this specification under `specs/`.
Commit 2 is the derivation note under `derivations/`, before any
production code, per `AGENTS.md` rule 3. Commits 3+ carry the script,
results, test file and report. **Parent 1 of any commit is whatever you
are standing on; do not specify it independently.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

    derivations/CANONICAL_INTERACTION.md
    27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81

    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
    c7e5744c9744780b6eb205c08ff9b65393e0055d7ebf04f2e0fc406d028edeb5

    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
    9bf14f51cc1fbdf4523debe70ad91164bc6d9c96d75f3450b7bce6d43514ec1d

    derivations/P2-PHASE-01_fierz_sign_addendum.md
    a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df

    derivations/P2-GAP-01_gap_criticality.md
    17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00

**A2 — Scalar control passes, at LAYER 1a ONLY.** Using exactly the
scalar operator, internal normalisation and factor-of-two convention of
`P2-GAP-01` as pinned in A1, the Layer-1a algebraic coefficient and its
normalisation chain must be consistent with that established
critical-coupling calculation. **If they are not, STOP** — the
coefficient chain is wrong and the V and A results cannot be trusted.

**Neither Layer 1b nor Layer 2 is part of this gate.** If the exponent
mapping is frozen, the scalar HS sign must be consistent with
`P2-GAP-01`'s attractive scalar channel; **if it is not frozen, both
`REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL` and
`ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL` are
satisfactory outcomes and are NOT failures of the scalar control.**
Earlier drafts gated on each of those in turn, which would have forced
you to supply interpretations the repository has not defined.

**A3 — Layer 1a delivered for all three channels** — scalar singlet,
induced V singlet, induced A singlet: the algebraic coefficient `c`, its
sign and normalisation, computed by the script rather than asserted.
**This layer is unconditional.**

**A3a — Layer 1b delivered or explicitly withheld.** Either `g` and
real-HS admissibility per channel with the frozen exponent mapping
cited, or `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL`
with the search that established it.

**A3b — Layer 2 delivered or explicitly withheld.** Either the
attractive/repulsive labels with the frozen basis for them cited, or
`ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.

**Withholding at 1b or 2 is a satisfactory outcome**, and the three
layers must be reported separately, never collapsed.

**A4 — Convention dependence stated**, including what reverses if the
`s_G` ruling is reversed.

**A5 — Diquark executability determined**, per §3, with the frozen
material quoted.

**A6 — No decision taken, verified rather than declared.** Provide a
fixed-string check over the artifacts you author — the derivation note,
script, results artifact, test file and report, **excluding the
committed specification**, which necessarily contains these terms in its
own prohibitions — for: `we choose`, `we select`, `the HS channel is`,
`Paper 3 is excluded`, `no composite vector`. **Report every hit with
its sentence.** A hit that disclaims is legitimate; a hit that asserts
is not. **The count is not to be driven to zero.**

**A7 — Deliverables.** Derivation note, script under `scripts/`, results
artifact under `results/`, test file under `tests/`, report. **Tests are
required, and they follow the three layers** — a test of a quantity this
specification permits to be undefined would be unsatisfiable. At
minimum:

- the scalar **Layer-1a** control;
- the algebraic coefficient `c` and its sign in each channel,
  **computed by the script rather than asserted**;
- **if the exponent mapping is established**, the resulting
  exponent-level `g` and real-HS admissibility;
- **if (b) executes**, the defining relation `C γ_μ^T C⁻¹ = −γ_μ`.

**A8 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, or `pyproject.toml` is modified. Verify
`GATES.md`'s blob is unchanged by reading the object.

**A9 — Scope**, six additions; you choose none of the paths except the
`{HHMM}Z` token, fixed once by commit 1 and reused:

    specs/2026-08-08T{HHMM}Z_channel-character.md
    derivations/P2-PHASE-01_channel_character.md
    scripts/p2_channel_character.py
    results/P2-PHASE-01/channel-character/channel_character.json
    tests/test_p2_channel_character.py
    reports/2026-08-08T{HHMM}Z_channel-character.md

**Final base-to-head scope: 6 additions, 0 modifications.** Report the
template, the resolved manifest, its SHA-256, and the checker JSON
including `observed_operations`.

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>` — that exact invocation, since `pytest` and
`python -m pytest` resolve to different versions on this host:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`, and your new test file.
**A10-pre** at the pre-report head goes in the report; **A10-final** at
the pushed head is post-report evidence and carries the verdict.

**A11 — Lint clean** with `ruff check` under the repository's
configuration on the files you author. Pre-existing diagnostics
elsewhere are not yours to fix.

**A12 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`eb88a2c9174cfda746c266924e741a6f88134234`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design — do not
repair it.** Report all three. Push the task branch only. **Delete no
branch.**

## 5. Evidence layering

**Committed report:** A1–A8, A10-pre, A11, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A10-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the six paths of A9 only.
- **Do not select a Hubbard–Stratonovich channel.** Reporting which
  channels admit a real auxiliary field is the task; choosing one is
  `OPEN-AC-1` and is the PI's.
- **Do not arbitrarily select a charge-conjugation convention in order
  to obtain a result.** If the frozen material does not fix `C`,
  **continue through §3's steps 2–4**: determine whether the defining
  relation fixes an equivalence class whose residual freedom leaves the
  channel coefficients invariant. **Report ambiguity only if the channel
  result genuinely depends on an unfixed choice.** An earlier draft
  stopped at step 1, which would have discarded a possibly
  convention-independent answer.
- **Do not claim that a composite vector is excluded.** A repulsive
  `ψ̄ψ` channel is not a statement about every channel.
- **Do not modify any frozen artifact**, and do not consume the
  quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, or the
  historical Finding 5 extraction. **List every repository input your
  work actually read, by path**, and show that none of the three appears.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which — an authoring-time
  suppression is a fact to disclose, not an absence.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `gate/p2-channel-character`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything**; report anything missing as a finding.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own development iteration.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- raw output for A1–A11, scope-checker JSON verbatim including
  `observed_operations`;
- the scalar control result, first, since everything else depends on it;
- the channel character for V and A, with the criterion and its
  justification;
- the convention dependence, including the `s_G` reversal case;
- the diquark executability determination, with the frozen material
  quoted;
- **what this narrows for `OPEN-AC-1`, stated as evidence and not as a
  recommendation**;
- **whether an exit code, tool failure or missing convention was at any
  point treated as a negative result rather than as a failure to
  observe.** Three defects of that shape have surfaced this week; if you
  meet a fourth, it is worth more than the derivation;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
