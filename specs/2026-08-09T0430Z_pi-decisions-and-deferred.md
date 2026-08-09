# Task specification — record three PI decisions and open a deferred-items register

Specification evidence base: `f309f61c9c14b0e2c63e078f9c0d0809422742e7`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This task records decisions and computes nothing.** No gate status
changes, no frozen artifact is touched, and no result is recomputed.

---

## 0. Three PI decisions, and one thing they are not

**Decision 1 — Hubbard–Stratonovich channel.**

> **PI ruling, 2026-08-09 — mean-field channel for `P2-PHASE-01`.**
>
> Mean-field work proceeds in the **scalar channel with a real auxiliary
> field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`
> and admits the standard real linear Hubbard–Stratonovich
> representation; the induced V and A singlets have `g < 0` and do not.
>
> **This is a choice of direct route, not a judgement that the V/A
> representation is wrong.** The programme's existing machinery — the
> gap equation, `I_0`, the stationary-branch study — is built on a real
> auxiliary field. **The V/A channel does not admit the standard real
> linear HS contour that machinery uses, and would require a non-real
> contour or an otherwise reformulated bosonisation apparatus.**
>
> **No evidence indicates the V/A representation is unphysical, and the
> PI's position is that it may contain physically relevant information
> and must be returned to. It is deferred, not excluded** — see
> `DEFERRED-01`.
>
> **This does not close `OPEN-AC-1`.** It selects the channel for
> mean-field work; the Fierz ambiguity — that channels equivalent as
> operators are inequivalent after truncation — is unaffected by which
> one is used.

**Decision 2 — the charge-conjugation phase `η`.**

> **PI ruling, 2026-08-09 — `η` is not selected; both signs are
> computed.**
>
> The diquark rearrangement requires `ψ̄^c = η ψ^T C⁻¹`. **The frozen
> material fixes no value of `η`, and unlike the exponent mapping no
> executed calculation constrains it.**
>
> **For the SIGN AMBIGUITY exposed by the channel-character derivation,
> the programme evaluates both the `η = +1` and the `η = −1`
> representative rather than selecting between them.** This does not
> assert that the full convention space is exactly two elements — the
> residual phase freedom has not been characterised — only that the
> ambiguity shown to affect the paired product is a sign, and both signs
> are to be carried through and reported.
>
> **The reason is diagnostic.** If both signs give the same channel
> character, **the exposed `η = ±1` sign ambiguity does not affect that
> character, and that sign question closes** — the wider phase freedom
> remains uncharacterised either way. **If they give opposite
> characters, then the diquark channel character depends on an
> unresolved sign convention — and that is something the programme must
> know rather than conceal behind a choice.**

**Decision 3 — the negative-mass branch.**

> **PI ruling, 2026-08-09 — the negative-mass branch is DEFERRED, not
> excluded.**
>
> The exploratory study found a second stationary branch at
> `M̂ ≈ −7.59`, the exact Wilson complement of the trivial branch, **with
> positive restricted curvature in the explored one-dimensional
> stationary analysis, including below `G_c`.**
>
> **"Restricted", not "stable", is the accurate word.** The pinned
> exploratory note states of exactly that quantity: *"Neither curvature
> is a full condensate-space Hessian or a phase-admissibility
> statement."* **A bare "stable" would let a later reader take the
> premise as stronger than the evidence.**
>
> **It is not classified as a lattice artifact.** The complement
> relation and the observed restricted stability **tie the branch
> structurally to the Wilson term; they do not establish full
> condensate-space stability, phase admissibility, or absence of
> physical content.** Under the substrate reading there is no continuum limit, so
> **the standard continuum-decoupling argument cannot by itself classify
> this branch as an unphysical lattice artifact.**
>
> **The PI's position is that a solution stable under the analysis
> actually performed corresponds to something that warrants physical
> interpretation rather than automatic dismissal.** The branch is
> deferred pending the main line — see `DEFERRED-02`.
>
> **The qualifier is load-bearing.** Written as *a stable solution
> corresponds to something real*, the position would quietly restore the
> stability claim narrowed two paragraphs above.
>
> **Consequence for SI-1, recorded now so it is not met by surprise.**
> `P2-PHASE-01`'s kill criterion asks whether any admissible phase exists
> in the frozen space. **With this branch neither admitted nor excluded,
> that criterion's quantifier range is undetermined**, and the SI-1
> specification must state whether the branch falls inside it. **This
> ruling does not answer that; it records that the question is now
> unavoidable.**

**What these are not.** None of the three is a physics result. **Decision
1 selects a route, Decision 2 declines to select, Decision 3 declines to
classify.** All three are recorded as PI decisions, not derived from the
frozen material.

## 1. The deferred-items register

**Land `derivations/P2-DEFERRED-ITEMS.md`.** Its purpose is stated in
the file:

> **This register holds work that has been CONSIDERED and consciously
> postponed.** It is not a list of open questions or of things not yet
> thought about. **The distinction is the point**: an open item may
> simply never have been examined, while an entry here was examined and
> deferred with a reason, and carries the PI's position at the time of
> deferral.

**Three entries:**

    DEFERRED-01  V/A mean-field representation
      Status:    deferred, not excluded
      Reason:    the scalar channel is the direct route and the existing
                 machinery is built for a real auxiliary field
      PI position: the V/A representation may contain physically
                 relevant information and must be returned to
      Evidence:  g_V = g_A = -G/2, no real linear HS field admissible
                 (channel-character layers derivation)
      Blocks:    nothing; the scalar route proceeds independently

    DEFERRED-02  Negative-mass stationary branch, M-hat ~ -7.59
      Status:    deferred, neither admitted nor excluded
      Reason:    the main line proceeds first
      Evidence strength: positive RESTRICTED one-dimensional curvature,
                 which the pinned note states is neither a full
                 condensate-space Hessian nor a phase-admissibility
                 statement
      PI position: a solution stable under the analysis actually
                 performed warrants physical interpretation rather than
                 automatic dismissal;
                 classifying it as an artifact is not supported, because
                 the substrate reading has no continuum limit and the
                 standard continuum-decoupling argument cannot by itself
                 classify it as an unphysical lattice artifact
      Evidence:  exact Wilson complement I_0(M) = I_0(-8-M); positive
                 restricted curvature below G_c (exploratory scalar
                 stationary study report and results artifact)
      Blocks:    the quantifier range of the SI-1 kill criterion, which
                 must state whether this branch falls inside it

    DEFERRED-03  Possible relation between DEFERRED-01 and DEFERRED-02
      Status:    PI hypothesis, UNTESTED
      Content:   both arise in sectors outside the presently selected
                 real-scalar mean-field route. The PI's hypothesis is
                 that they are related.
      Candidate link, offered as a starting point and not as a finding:
                 the Wilson term both generates the exact complement
                 structure of the negative-mass branch and explicitly
                 breaks chiral symmetry; whether that breaking is
                 related in any way to the deferred V/A representation
                 is an untested PI hypothesis
      Evidence:  none. This entry records a hypothesis and its
                 motivation, not a result.

**`DEFERRED-03` must be visibly marked as untested.** A hypothesis
recorded beside two evidence-backed entries will otherwise be read as
carrying comparable support. **State in the entry that it has none.**

## 2. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-09T{HHMM}Z_pi-decisions-and-deferred.md
    commit 2  DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
    commit 3  reports/2026-08-09T{HHMM}Z_pi-decisions-and-deferred.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.** **No derivation note is required**: this task performs no
derivation, and `AGENTS.md` rule 3 governs production code, of which
there is none.

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    derivations/P2-PHASE-01_channel_character_layers.md
    4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711

    results/P2-PHASE-01/channel-character-layers/layers.json
    fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542

    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
    70ab88eda32483420c0bfd522babd2ca4a73941bc2d2d20f8414976641756cbe

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028

**The last two are pinned because `DEFERRED-02`'s evidence lives there,
not in the exploratory derivation note.** That note is a
pre-registration: it records that the complement symmetry would be
tested, not the roots, curvatures or complement relation themselves. **A
previous issue of this specification pinned only the note, so A2 could
not be satisfied from A1's enumerated set** — a specification defect,
not an evidence failure.

**A2 — Cited evidence verified, not assumed.** For each
**evidence-backed** `Evidence:` line in §1 — `DEFERRED-01` and
`DEFERRED-02` — locate the supporting statement in the pinned material
and quote it. **If either is not there, STOP and report** — a register
entry whose evidence line points at nothing is worse than no register.

**For `DEFERRED-03`, verify instead that the entry states
`Evidence: none` and supplies no evidentiary citation. The absence of
evidence is intentional content there, not a failed lookup**, and
treating it as one would be exactly the confusion between *not observed*
and *observed negative* that this programme has met four times.

**A3 — Three `DECISION_LOG.md` entries**, in the file's existing format,
**one per decision, not one combined entry.** The substantive ruling
text of §0 is reproduced verbatim within each; structural metadata the
format requires may be added around it.

**Check required phrases against NORMALISED text**: strip blockquote
prefixes (`> `), strip Markdown emphasis and code delimiters (`**` and
backticks), collapse whitespace to single spaces. **Keep en dashes as
they are.** Each entry must contain:

    entry 1   scalar channel with a real auxiliary field
              This is a choice of direct route
              It is deferred, not excluded
              This does not close OPEN-AC-1
    entry 2   the programme evaluates both the
              rather than selecting between them
              depends on an unresolved sign convention

**These phrases may appear in the entry's surrounding prose rather than
inside the verbatim ruling**, where the ruling's own wording does not
contain them. **Do not edit the ruling text to make a check pass** — the
requirement is that the entry contains the phrase, not that the
blockquote does. A previous issue's `rests on an arbitrary sign` could
not be satisfied inside the ruling and was correctly placed in the
`### Reason` prose.
    entry 3   DEFERRED, not excluded
              they do not establish full condensate-space stability,
                phase admissibility, or absence of physical content
              cannot by itself classify this branch as an unphysical
                lattice artifact
              that criterion's quantifier range is undetermined

**Append-only: zero deleted lines.**

**A4 — Register landed** with the three entries and the purpose
statement of §1, `DEFERRED-03` marked untested.

**A5 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, every path under `scripts/`, `results/`
and `tests/`, and every existing file under `derivations/`:
blob-identical to the evidence base. **Read from the objects.**

**No gate status changes.** `P2-PHASE-01` remains `PROPOSED`;
`P2-GAP-01` remains `PASS`. **Decision 3 in particular does not alter
any gate** — it records that a question about SI-1's quantifier range is
now unavoidable, which is not a change to SI-1.

**A6 — Scope**, three additions and one modification:

    add:
      specs/2026-08-09T{HHMM}Z_pi-decisions-and-deferred.md
      derivations/P2-DEFERRED-ITEMS.md
      reports/2026-08-09T{HHMM}Z_pi-decisions-and-deferred.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 3 additions and 1 modification.**
`derivations/P2-DEFERRED-ITEMS.md` does not exist at the evidence base,
so it is an addition. Report the template, the resolved manifest, its
SHA-256, and the scope-checker JSON including `observed_operations`.

**A7 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A7-pre** at the pre-report head goes
in the report; **A7-final** at the pushed head is post-report evidence.

**A8 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`f309f61c9c14b0e2c63e078f9c0d0809422742e7`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

## 3. Evidence layering

**Committed report:** A1–A6, A7-pre, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A7-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 4. Invariants and prohibitions

- Executor-writable: the four paths of A6 only.
- **Decide nothing.** These are the PI's decisions; record them. If any
  is ambiguous, stop and report rather than resolving it.
- **Do not compute anything**, and do not perform the diquark
  calculation Decision 2 authorizes — that is a separate task.
- **Do not classify the negative-mass branch**, and do not amend the
  SI-1 gate text.
- **Do not modify any frozen or pinned artifact.**
- **Do not present `DEFERRED-03` as supported.** It is a hypothesis with
  no evidence, recorded as such.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which — your harness appends
  them by default, so suppression is expected and its disclosure is
  required.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/pi-decisions-and-deferred`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 5. Report contract

- raw output for A1–A7, scope-checker JSON verbatim including
  `observed_operations`;
- the three `DECISION_LOG.md` entries quoted, with the zero-deletion
  diff;
- the register quoted in full;
- **the quoted evidence for each `Evidence:` line**, with its source
  path;
- **whether the register reads as a list of open questions rather than
  of consciously deferred work.** The distinction is the register's
  reason for existing, and if the text does not carry it, say so;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
