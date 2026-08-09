# Task specification — land the attraction/repulsion ruling and recompute Layer 1b and Layer 2

Specification evidence base: `3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Two things, in one task, in this order:** a PI ruling is recorded, and
the two layers it unblocks are recomputed. **The ruling is landed
first** — the recomputation consumes it, and a derivation must not
depend on a convention that is not yet in the repository.

**`AGENTS.md` research rule 3 applies** to the recomputation: a
derivation note before production code.

---

## 0. The ruling to land, verbatim

> **PI ruling, 2026-08-08 — attraction/repulsion sign convention.**
>
> Under the Euclidean exponent mapping ruling of the same date, a channel
> whose Hubbard–Stratonovich coefficient satisfies **`g > 0` is labelled
> ATTRACTIVE**; **`g < 0` is labelled REPULSIVE**.
>
> **The basis, in three separated steps.** Under the Euclidean exponent
> mapping, a channel term with coefficient `g` appears as
> `exp(+(g/2)J²)`. For `g > 0` the standard linear
> Hubbard–Stratonovich representation uses a real Gaussian auxiliary
> field; for `g < 0` that real contour is not available — **that is the
> algebraic fact.** **The programme adopts ATTRACTIVE as the label for
> the `g > 0` sign and REPULSIVE for the `g < 0` sign** — that is the
> convention. This is consistent with `P2-GAP-01`'s description of its
> positive-coupling scalar channel as attractive — that is the
> consistency check. **The naming is not derived from
> Hubbard–Stratonovich admissibility; it is assigned to that sign.**
>
> **`J = ψ̄Γψ` is a Grassmann composite.** Before bosonisation there is
> no c-number configuration space on which "larger `|J|`" can be
> compared pointwise, so **no appeal to enhanced configurations is made
> here.** An earlier formulation did make one and was wrong to.
>
> **This ruling depends on the exponent mapping ruling of the same
> date.** If that mapping were reversed, every channel's `g` reverses
> and so does every label this ruling assigns. **The two are a chain,
> not independent constraints**, and neither is derived from the frozen
> material.
>
> **Scope limit.** The label characterises the sign of the interaction
> in the specified Hubbard–Stratonovich channel. It is conventionally
> associated with an attractive or repulsive tendency in that channel;
> **it does not establish that condensation actually occurs.** Whether
> it does depends on the full quadratic kernel — `Γ⁽²⁾(0) = 1/g − Π(0)`
> — the fermion determinant, stability, and the critical coupling.
> **Nor does it by itself establish the existence or absence of a
> two-body bound state, resonance, or composite excitation.**
>
> **In particular: REPULSIVE in a `ψ̄ψ` channel does NOT imply that a
> composite vector is absent.** That question requires its own
> bound-state or pole analysis, and may also involve a differently
> paired channel. **A channel-character label is not a pole
> calculation.**
>
> **This supplies a convention for the item currently recorded in the
> programme registry as `NOT DEFINED`. It is not a derivation.**

**Why the composite-vector sentence is stated explicitly.** An earlier
formulation relied on the reader inferring it from "does not exclude
binding in a differently-paired channel". **That is not sufficient**:
someone can reasonably answer that the vector composite lives in exactly
the channel just labelled repulsive. **The forbidden inference is the
general one** — `g < 0` does not imply the absence of a composite state,
because a mean-field channel label is not a bound-state calculation.
**This programme made that inference once already, in an early
exploratory reading, and caught it. A governance rule should not depend
on a reader repeating that catch.**

## 1. What the recomputation now has that it lacked

The channel-character derivation returned, deliberately:

    Layer 1a   delivered      c per channel
    Layer 1b   NOT DEFINED    exponent mapping not frozen
    Layer 2    NOT DEFINED    no sign-to-label rule anywhere

**Both blockers are now removed.** The exponent mapping was ruled on
2026-08-08 and is on `main`: `S_E = S_E,0 − X`, hence `g = +2c`. The
sign-to-label rule is §0 of this task.

**A point that will otherwise cost you time.** `Layer 1b` computes
`g = 2c` from the interaction-expression coefficient `c`. **It has
nothing to do with `G_c`.** The generator-sum result
`G_c = N/(8·I_0)` concerns the critical coupling, not the channel
coefficient, and **does not enter this computation at all.** Do not
attempt to reconcile them.

## 2. What to compute

**Recompute Layer 1a as a control**, from the pinned channel-character
artifacts, and confirm it reproduces `c` per channel. **If it does not,
STOP** — everything downstream is a function of `c`.

**Layer 1b.** For the scalar singlet, the induced V singlet and the
induced A singlet, report `g = 2c` and whether a real linear
Hubbard–Stratonovich field is admissible (`g > 0`). **Cite the exponent
mapping ruling as the frozen basis**, by `DECISION_LOG.md` entry.

**Layer 2.** Apply §0's labels. Report ATTRACTIVE or REPULSIVE per
channel, **with the ruling cited as the basis and not as a derivation.**

**A control that must hold.** The scalar singlet must come out
ATTRACTIVE, consistent with `P2-GAP-01`. **If it does not, STOP** — the
chain from `c` through `g` to the label is wrong, and the V and A
results cannot be trusted either.

**Report what remains undetermined.** The diquark channel is still
blocked on `η`, the particle–particle Grassmann ordering, and the
diquark normalisation. **This task does not touch it**, and the report
must say so rather than leaving a reader to assume the channel picture
is now complete.

## 3. What must not be concluded

- **Do not write that a composite vector is excluded, absent,
  impossible, or ruled out.** §0 forbids the inference explicitly.
- **Do not select a Hubbard–Stratonovich channel.** Knowing which
  channels admit a real auxiliary field constrains `OPEN-AC-1`; it does
  not decide it, and the decision is the PI's.
- **Do not freeze `η` or any diquark convention.**
- **Do not update the programme registry.** Changing the
  `Sign convention for attraction and repulsion` row from `NOT DEFINED`
  is a `0-programme` task and should follow this one — **the registry
  should record a convention that has been used, not one only
  declared.**
- **Do not revisit `G_c`, the exploratory positions, or the
  parameter-domain draft.** The addendum settled that they are
  unaffected.

## 4. Acceptance criteria

**A0 — Commit order.**

    commit 1  specs/2026-08-09T{HHMM}Z_attraction-ruling-and-layers.md
    commit 2  DECISION_LOG.md            (the ruling, landed first)
    commit 3  derivations/P2-PHASE-01_channel_character_layers.md
    commit 4+ script, results, test file, report

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.** **Commit 2 precedes the derivation note**, because the note
records a computation that consumes the ruling. **Parent 1 of any commit
is whatever you are standing on.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    results/P2-PHASE-01/channel-character/channel_character.json
    093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f

    scripts/p2_channel_character.py
    521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

**A2 — The exponent mapping ruling located and quoted** from
`DECISION_LOG.md` on `main`, with its date and the `g = +2c` statement.
**If it is not there, STOP** — this task's premise is that it landed.

**A3 — Ruling recorded.** One `DECISION_LOG.md` entry in the file's
existing format. **The substantive ruling text of §0 is reproduced
verbatim within the entry; the structural metadata that format requires
may be added around it.** The entry must contain these exact phrases:

    Date: 2026-08-08
    Decision owner: Principal Investigator
    g > 0 is labelled ATTRACTIVE
    The naming is not derived from Hubbard–Stratonovich admissibility
    The two are a chain, not independent constraints
    REPULSIVE in a
    is not a pole calculation
    It is not a derivation

**Check these against NORMALISED text, and normalise all four things
that would otherwise defeat the check:**

    1  strip blockquote markers (`> `)
    2  strip Markdown emphasis and code delimiters (`**` and backticks)
    3  collapse all whitespace to single spaces
    4  keep the en dashes as they are — `Hubbard–Stratonovich` uses
       `–`, not a hyphen

**What is being verified is the substantive text, not its Markdown
representation.** An earlier draft normalised only the quote markers and
whitespace, leaving the backticks in place, so
`g > 0 is labelled ATTRACTIVE` still would not have matched — the same
observation-method trap one step further in.

**Append-only: zero deleted lines.**

**A4 — Layer 1a control reproduced**, `c` per channel matching the
pinned artifacts. **Gating: if it does not, STOP.**

**A5 — Layer 1b delivered:** `g` and real-HS admissibility for the three
channels, computed by the script rather than asserted, citing the
exponent mapping ruling.

**A6 — Layer 2 delivered:** the label per channel, citing §0.

**A7 — Scalar control ATTRACTIVE.** **Gating: if it is not, STOP.**

**A8 — Diquark status restated**, not silently omitted.

**A9 — No forbidden conclusion.** Provide a fixed-string check over the
artifacts you author — derivation note, script, results artifact, test
file, report, **excluding the committed specification**, which
necessarily contains the terms in its own prohibitions — for:
`composite vector is excluded`, `no composite vector`, `rules out`,
`we choose`, `the HS channel is`. **Report every hit with its
sentence.** A hit that disclaims is legitimate; one that asserts is not.
**The count is not to be driven to zero, and a required disclaimer must
not be reworded to avoid one.**

**A10 — Deliverables.** Derivation note, script under `scripts/`,
results artifact under `results/`, test file under `tests/`, report.
**Tests are required**, and they must lock the FULL mapping for all
three channels, not only the scalar control — otherwise the ruling is
recorded but its consumption is not regression-locked:

    c_S > 0  =>  g_S > 0  =>  ATTRACTIVE
    c_V < 0  =>  g_V < 0  =>  REPULSIVE
    c_A < 0  =>  g_A < 0  =>  REPULSIVE

plus the Layer-1a control, and `g = 2c` **computed rather than
hard-coded**.

**A11 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, or `pyproject.toml` is modified. Verify
`GATES.md`'s blob from the object. **`DECISION_LOG.md` is modified by
A3 and only by A3.**

**A12 — Scope**, six additions and one modification:

    add:
      specs/2026-08-09T{HHMM}Z_attraction-ruling-and-layers.md
      derivations/P2-PHASE-01_channel_character_layers.md
      scripts/p2_channel_character_layers.py
      results/P2-PHASE-01/channel-character-layers/layers.json
      tests/test_p2_channel_character_layers.py
      reports/2026-08-09T{HHMM}Z_attraction-ruling-and-layers.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 6 additions and 1 modification.** Report the
template, the resolved manifest, its SHA-256, and the scope-checker JSON
including `observed_operations`.

**A13 — Validators, exit status 0**, run individually with
`python -m pytest <path>` — that exact invocation, since `pytest` and
`python -m pytest` resolve to different versions on this host:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_channel_character.py`,
`tests/test_p2_generator_sum_criticality.py`, and your new test file.
**A13-pre** at the pre-report head goes in the report; **A13-final** at
the pushed head is post-report evidence and carries the verdict.

**A14 — Lint clean:**
`ruff check scripts/p2_channel_character_layers.py tests/test_p2_channel_character_layers.py`.
**Those two files only** — the other four you author are Markdown and
JSON, which `ruff` does not lint. Report the exact command and its
output. Pre-existing diagnostics elsewhere are not yours to fix.

**A15 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

## 5. Evidence layering

**Committed report:** A1–A12, A13-pre, A14, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A13-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the seven paths of A12 only.
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
- Branch naming: use `gate/p2-attraction-ruling-and-layers`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- raw output for A1–A14, scope-checker JSON verbatim including
  `observed_operations`;
- the ruling entry quoted, with the zero-deletion diff;
- the Layer-1a control first, since everything else depends on it;
- Layer 1b and Layer 2 per channel, with their citations;
- the A9 fixed-string results, each hit with its sentence and its
  classification;
- the diquark status restated;
- **what this narrows for `OPEN-AC-1`, stated as evidence and not as a
  recommendation**;
- **whether any acceptance criterion here would have been satisfiable by
  a computation that never used the ruling.** If the ruling could be
  removed without changing any output, the recomputation did not consume
  it, and we need to know that;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
