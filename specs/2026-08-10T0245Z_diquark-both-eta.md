# Task specification — diquark channel character, carrying both `η` signs

Specification evidence base: `8701a97a6bb58550d4300f75c10638b057335731`

> **The `η` ruling is now on `main`.** It was integrated on 2026-08-09
> after two superseded executions and one stale-base replay; the
> authoritative record is the third PI-decision entry in
> `DECISION_LOG.md`. **A derivation must not depend on a decision that
> is not yet in the repository's authority** — that condition is now
> satisfied, and A2a verifies it rather than assuming it.
>
> **Rules 1–17 are in force at this evidence base**, so this task is
> governed by Rule 15: its pre-execution review is a committed artifact
> — see A0 commit 2 and A1a.
>
> **Evidence base advanced from `898aecd1…` while this specification was
> under review**, when the SI-1 cross-reference was integrated. **All
> five A1 pins were re-verified at the new base and are unchanged**;
> only `GATES.md`, which this task does not read, differs. **The
> specification was not otherwise altered.**

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This is a DERIVATION.** It performs a computation the channel-character
work found blocked, under a PI decision not to resolve the blocker but
to carry it. **`P2-PHASE-01` remains `PROPOSED`; nothing frozen is
touched.**

**`AGENTS.md` research rule 3 applies:** a derivation note before
production code.

---

## 0. What is blocked, what is being carried, and what is still blocked

The channel-character derivation established that the particle–particle
channel's obstruction is **not** the charge-conjugation matrix `C` — the
solution space of `C γ_μ^T C⁻¹ = −γ_μ` is one-dimensional and the
residual scalar cancels in the paired product. **Three other definitions
are missing:**

    eta        in psibar^c = eta psi^T C^-1. The earlier
               channel-character analysis found it entering ONCE in the
               paired-product construction, so changing eta by a sign is
               EXPECTED to reverse the corresponding coefficient WITHIN
               A FIXED particle-particle ordering convention. Because
               that ordering is not frozen, this task must RE-ESTABLISH
               rather than assume the resulting channel-character
               relation. Nothing in the frozen material fixes eta.
    pp Grassmann ordering    the frozen compound_index_order fixes the
               particle-hole crossing; it fixes NO particle-particle
               ordering
    diquark operator normalisation    not stated anywhere

**The PI ruling of 2026-08-09 addresses the first only.** Both `η = +1`
and `η = −1` are carried through and both results reported, rather than
one being selected. **This does not assert that the full convention
space is exactly two elements** — the residual phase freedom has not
been characterised — **only that the ambiguity shown to affect the
paired product is a sign.**

**The other two remain unfrozen, and this task must not supply them.**
Whether the computation can proceed without them, or only under stated
assumptions, is part of what this task determines. **If it cannot
proceed, that is a result.**

## 1. Objective

Paper 2 carries a derivation reporting the particle–particle channel
coefficients for both `η` representatives, or reporting precisely which
missing definition prevents that and why.

## 2. What to compute

**Step 1 — re-establish the blockers, do not inherit them.** Confirm
from the pinned material that `η`, the particle–particle Grassmann
ordering, and the diquark operator normalisation are each unfixed, and
quote the search. **If any is in fact fixed, that changes this task:
STOP and report.**

**Step 2 — `C` and its residual freedom.** Reconstruct the solution
space of `C γ_μ^T C⁻¹ = −γ_μ` under the frozen conventions, confirm its
dimension, and **demonstrate that the residual scalar cancels in the
paired product** rather than citing that it does.

**Step 3 — the particle–particle rearrangement, for both `η`.** Perform
the rearrangement and report the induced coefficients per family for
`η = +1` and for `η = −1`, side by side.

**The two remaining unfrozen definitions are the difficulty here, and
how you handle them is the substance of this task:**

- **If the channel coefficients are independent of the
  particle–particle Grassmann ordering and of the diquark
  normalisation**, demonstrate that and proceed. **Demonstrate, do not
  assume.**
- **If they are not**, you may proceed **only** by stating an explicit
  assumption, labelling every result that depends on it, and reporting
  **what changes under the explicit alternatives you can define —
  without claiming they exhaust the admissible convention space.** **Do
  not adopt an assumption silently, and do not present an
  assumption-dependent coefficient as a frozen-material result.**

  **Do not infer that the admissible particle–particle ordering space
  consists only of the alternatives you test.** The frozen material says
  no ordering is fixed; **it does not enumerate which are admissible**,
  and the same caution applies here as to `η`.
- **If no assumption makes the computation well-defined**, report
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, name exactly what is
  missing, and stop there. **That is a satisfactory outcome.**

**For the diquark normalisation, distinguish three cases**, because
conflating them would send a magnitude question to an
`UNRESOLVED` verdict it does not deserve:

    positive real rescaling   changes coefficient MAGNITUDE; channel
                              character invariant
    sign or phase convention  may change the SIGN, and so the character
    complex normalisation     may make a simple ATTRACTIVE/REPULSIVE
                              label inapplicable at all

**Magnitude dependence alone is not a sign ambiguity.** What this task
cares about is whether the CHANNEL CHARACTER depends on an unresolved
convention, not whether the coefficient has a unique magnitude.

**Step 4 — channel character, under the standing rulings.** For each
`η`, apply `g = 2c` and the attraction/repulsion labels of the
2026-08-08 rulings, cited from `DECISION_LOG.md`. **The same scope limit
applies: a channel-character label is not a bound-state or pole
calculation.**

**Step 5 — the diagnostic question this task exists to answer.**
**Where Step 3 makes the comparison well-defined**, state whether the
two `η` representatives give the **same** channel character or
**opposite** ones. **Where it does not, no verdict is licensed** — say
so, per A6's third outcome.

- **Same** — the exposed `η = ±1` sign ambiguity does not affect the
  channel character, and that sign question closes. **The wider phase
  freedom remains uncharacterised either way; say so.**
- **Opposite** — the diquark channel character depends on an unresolved
  sign convention. **Report it plainly.** This is the outcome the PI
  decision was designed to expose, and **it is more valuable than a
  single answer would have been.**

## 3. What must not be concluded

- **Do not select `η`**, the particle–particle Grassmann ordering, or
  the diquark normalisation. Freezing any of them is the PI's.
- **Do not state that a composite vector exists or is absent**, in
  either `η` case. A channel label is not a pole calculation, and the
  particle–particle channel being computed does not change that.
- **Do not state that the channel picture is now complete.**
- **Do not select a Hubbard–Stratonovich channel.** The 2026-08-09
  ruling selected the scalar channel for mean-field work; **this task
  computes a channel character and does not revisit that.**
- **Do not revisit `G_c`, the exploratory positions, or the
  parameter-domain draft.**

## 4. Acceptance criteria

**A0 — Commit order.**

    commit 1  this specification, under specs/
    commit 2  reviews/chatgpt/…  — the pre-execution review
    commit 3  the derivation note, under derivations/
    commit 4  script, results artifact, test file
    commit 5  the report

**Commits 4 and 5 are separate**, and the split is not cosmetic: the
report carries the step-4 evidence, so it cannot be part of the commit
whose evidence it records. **The script, results and test file belong
together in one work commit** — they are produced by one execution and
splitting them would suggest a sequence that did not occur.

**Commit 2 precedes the derivation note**, per Rule 15's timing clause:
the review is committed before the work it authorises proceeds. **Commit
3 precedes any production code**, per `AGENTS.md` rule 3. **Parent 1 of
any commit is whatever you are standing on.**

**A1a — The pre-execution review committed, unedited**, at the
`reviews/chatgpt/` path of A11, **byte-identical to the text supplied
between the supplied delimiters, excluding the delimiter lines and any
accompanying instruction.**

**The delimiters are these two lines**, each occupying a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

**Match them as COMPLETE LINES**, not as first occurrences of the
string — this specification and any accompanying instruction both
contain them. **Exclude any preamble sentence that precedes the BEGIN
line.**
**If a placeholder appears inside the review's text it stays as
written**; resolve placeholders in the path only. **If the supplied text
is missing or does not correspond to this specification, STOP.**

**A2a — The `η` ruling located and quoted** from `DECISION_LOG.md` at
the evidence base, with its date and the instruction to evaluate both
representatives. **If it is not there, STOP** — this task's premise is
that it landed, and computing under a ruling the repository does not
carry would be exactly the provenance failure this programme corrected
in the exponent-mapping work.

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    derivations/P2-PHASE-01_channel_character_layers.md
    4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711

    results/P2-PHASE-01/channel-character-layers/layers.json
    fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542

**A2 — Blockers re-established**, per Step 1, with the search quoted.

**A3 — `C`'s residual freedom demonstrated to cancel**, per Step 2, not
cited.

**A4 — Both `η` results reported side by side IF the coefficients are
obtainable**, per Step 3, with any assumption explicitly labelled and
its alternatives stated. **If they are not obtainable without supplying
an unauthorized convention, A4 is satisfied by the
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` report.**

**A5 — Channel character per `η`, where A4 produced coefficients**, per
Step 4, citing the rulings.

**A6 — Diagnostic verdict delivered to the strongest level the
computation supports.** Exactly one of:

- **the coefficients and their channel characters are well-defined
  independently of the two remaining unfrozen definitions** — state
  explicitly whether the `η = ±1` representatives give the same or
  opposite character;
- **the verdict depends on an explicit assumption** — state it
  conditional on that assumption and report the alternatives;
- **the coefficients cannot be made well-defined without supplying an
  unauthorized convention** — report
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`; **no same/opposite
  verdict is then required.**

**An earlier draft required the verdict unconditionally while Step 3
permitted stopping. Those could not both be satisfied.**

**A7 — A particle–hole control.** Recompute the particle–hole
coefficients from the pinned channel-character material and confirm they
reproduce `c_S > 0`, `c_V = c_A = −G/4` in normalisation L. **Gating: if
they do not, the machinery is wrong and the particle–particle results
cannot be trusted. STOP.**

**A8 — No forbidden conclusion.**

    check type    character-exact substring, CASE-INSENSITIVE, on each
                  authored file's raw UTF-8 text; no normalisation;
                  matches do not span file boundaries

**Case-insensitive is deliberate**: the target is a forbidden
assertion, not a particular capitalisation, so `Composite vector` and
`WE SELECT` are hits. **Report each matched text as it appears**, not
lower-cased.

Provide this check over the artifacts you author — derivation note, script, results artifact, test
file, report, **excluding the committed specification** — for:
`composite vector`, `we select`, `we choose`, `the channel picture is
complete`, `rules out`. **Report every hit with its containing line or prose sentence, as
applicable** — a JSON value or a line of code has no sentence — and
classify each as a disclaimer or an assertion. **The count is not to be
driven to zero, and a required disclaimer must not be reworded to avoid
a hit.**

**A9 — Deliverables.** Derivation note, script under `scripts/`, results
artifact under `results/`, test file under `tests/`, report.

**Tests are required for every quantity the derivation actually
reaches.**

    always required   the particle–hole control
                      the C defining relation  C γ_μ^T C⁻¹ = −γ_μ
                      the residual-scalar cancellation

    if Step 3 produces coefficient sets
                      the relation between the η = +1 and η = −1 sets,
                      COMPUTED rather than hard-coded

    if Step 3 terminates at UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY
    before coefficient sets are defined
                      that relation test is INAPPLICABLE; the test file
                      MUST instead verify the demonstrated obstruction

**An earlier version required the relation test unconditionally** while
A6 permitted terminating before any coefficient set exists. **Those
could not both be satisfied**, and the executor would have faced a
required test of a quantity the correct outcome does not produce.

**A10 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, `DECISION_LOG.md`, or `pyproject.toml` is
modified. Verify `GATES.md`'s blob from the object.

**A11 — Scope**, seven additions:

    add:
      specs/2026-08-XXT{HHMM}Z_diquark-both-eta.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_diquark-both-eta.md
      derivations/P2-PHASE-01_diquark_both_eta.md
      scripts/p2_diquark_both_eta.py
      results/P2-PHASE-01/diquark-both-eta/diquark.json
      tests/test_p2_diquark_both_eta.py
      reports/2026-08-XXT{HHMM}Z_diquark-both-eta.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 7 additions and 0 modifications.**

**`tests/` is written by this task.** Every recent specification has
protected it; **this one authorises exactly one new file there and
nothing else** — no existing test is modified, renamed or removed. Report the
template, the resolved manifest, its SHA-256, and the scope-checker JSON
including `observed_operations`.

**A12 — Validators, exit status 0**, run individually with
`python -m pytest <path>` — that exact invocation, since `pytest` and
`python -m pytest` resolve to different versions on this host:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_channel_character.py`,
`tests/test_p2_channel_character_layers.py`, and your new test file.
**A12-pre** at the pre-report head goes in the report; **A12-final** at
the pushed head is post-report evidence and carries the verdict.

**A13 — Lint clean:**
`ruff check scripts/p2_diquark_both_eta.py tests/test_p2_diquark_both_eta.py`.
**Those two files only.** Report the exact command and its output.

**A14 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`8701a97a6bb58550d4300f75c10638b057335731`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

## 5. Evidence layering

**Committed report:** A1–A11, A12-pre, A13, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A12-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the seven paths of A11 only.
- **Do not freeze any convention**, and do not supply a missing one
  silently.
- **Do not draw any conclusion §3 forbids.**
- **Do not modify any frozen or pinned artifact**, and do not consume
  the quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, or
  the historical Finding 5 extraction. **List every repository input you
  actually read, by path.**
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which — your harness appends
  them by default, so suppression is expected and its disclosure is
  required.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `gate/p2-diquark-both-eta`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- raw output for A1–A13, scope-checker JSON verbatim including
  `observed_operations`;
- the particle–hole control first, since everything else depends on it;
- the blocker re-establishment with its quoted search;
- the `C` solution space and the demonstrated cancellation;
- **both `η` coefficient sets side by side WHERE A4 PRODUCES THEM**,
  with every assumption-dependent value labelled; **otherwise the
  precise obstruction, named**;
- **the same/opposite verdict WHERE DEFINED; otherwise an explicit
  statement that no such verdict is licensed** — a missing verdict under
  the `UNRESOLVED` outcome is the correct result, not an omission;
- **what remains unfrozen after this task** — the particle–particle
  Grassmann ordering and the diquark normalisation at minimum;
- **whether an earlier exploratory attempt's failure mode recurred.** A
  projection performed outside this repository returned zero in all four
  families, which was almost certainly a wrong projector construction.
  **If your result also vanishes identically, say so and say why** —
  a vanishing result and a broken projector look alike;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 8. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      DECISION_LOG.md at 8701a97a…, the η ruling entry
    method      Python substring containment after normalisation
    check type  NORMALISED SUBSTANTIVE — one function applied to both
                sides: strip "> " prefixes, strip ** and backticks,
                collapse whitespace; en dashes preserved

    PASS   the programme evaluates both the
    PASS   rather than selecting between them
    PASS   depends on an unresolved sign convention

**The eta ruling is present on `main` and says what A2a requires you to
confirm.** **Re-run this yourself** — A2a is satisfied by your check,
not by this record.

    target      derivations/P2-PHASE-01_channel_character.md
    check type  STRUCTURAL

    CONFIRMED  the three unfrozen definitions of §0 — eta, the
               particle-particle Grassmann ordering, and the diquark
               operator normalisation — are stated there as unfixed,
               and C's residual freedom is stated to cancel
