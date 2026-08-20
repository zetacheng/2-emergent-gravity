# `P2-PROJ-01-CLASS-01` — retrospective classification of `Q1` under rule 22

    KIND            CLASSIFICATION. Documentary reading only. No computation.
    SUBJECT         P2-RECON-PROJ-01, Q1
    SUBJECT BRANCH  science/recon-proj-01 @ e333b8a025c39fe66931a9763fe740d71209dc0a
    BASE            15796ed3f1e68d6e91b90f9e404d55b25cee9f80

> RETROSPECTIVE CLASSIFICATION — assigned after rule 22 was landed; does not
> alter the finding, its verdict, or the date it was recorded.

    Q1 VERDICT      INCONCLUSIVE          unchanged, and not re-adjudicated here
    SUBCLASS        INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
    GAPS            two, independent of each other

**This artifact does not resolve `Q1`, does not resolve `H-EXT-01`, and does
not make either bridge more or less likely to hold.** It records which of rule
22's two subclasses `Q1`'s finding carries, and the `Resolution path` rule 22
requires.

---

## 0. Why this is a separate reviewed task and not part of an integration

`Q1` was recorded before rule 22 existed, so its result carries no subclass and
no `Resolution path`. Two landed rules then meet:

**`CONVENTIONS.md` rule 22**, at the base, `:1498-1508`: "Every `INCONCLUSIVE`
result carries one of two subclasses, assigned when the result is recorded…
**Assigning a subclass is required, not optional.**"

**`CONVENTIONS.md` rule 17**, at the base, `:1280-1288`, verbatim:

> ### 17. Integrations do not add epistemic or governance classifications
>
> **An integration, derivation, or any task that carries reviewed
> results forward MUST NOT add a governance or epistemic classification
> the reviewed results did not carry.**
>
> Recording what a result did not establish is required. **Assigning it
> to an open item, a gate, a status, or a category it was never assigned
> to is not.**

**Adding the subclass at `PROJ-01`'s integration would have violated rule 17.**
The classification is therefore produced here, as this task's own reviewed
result. A later integration transports a classification that *was* reviewed,
which is what rule 17 requires, and adds nothing.

**Neither rule is amended, relaxed, or reinterpreted by this task.**

---

## 1. `M1` — `Q1`'s finding as recorded, on the subject branch

All citations below are to the subject branch at `e333b8a0`, where the
`PROJ-01` artifacts live. They are **not** on `main` at the base. Pinned by
blob id so a reader can resolve them:

    1cd5fa20431ced8265e0ceba9f8cedd9afd99d7d
        derivations/P2-RECON-PROJ-01_projection-adjudication.md
    bd67f42b834e8d8c83980bae96c3cd87d67a14f0
        reports/2026-08-19T2214Z_recon-proj-01.md
    544cb449877ddab3fc13e65989b7ad759620ccbe
        reviews/chatgpt/2026-08-19T2214Z_recon-proj-01.md
    37bdd57ff928a27e01bb369f09bc6bbfd9a650e2
        specs/2026-08-19T2214Z_recon-proj-01.md

### 1.1 The verdict as recorded

`derivations/P2-RECON-PROJ-01_projection-adjudication.md:5-7`:

>     Q1          INCONCLUSIVE — reason: one location's status under the §3 test
>                 cannot be settled by reading. §4 records which and what would
>                 settle it.

`reports/2026-08-19T2214Z_recon-proj-01.md:4`:

>                 Q1  INCONCLUSIVE, reason UNDETERMINED BY READING

**The verdict is `INCONCLUSIVE`.** It is unchanged by this artifact.

### 1.2 The question, and the test it was measured against

`specs/2026-08-19T2214Z_recon-proj-01.md:47-50`:

>     Q1   Does the repository contain a DERIVATIONAL ground for the axis-TT
>          projection — an argument from symmetry, a Ward identity, gauge
>          redundancy, or representation theory — that establishes the
>          discarded complement makes no contribution to the target observable?

`specs/2026-08-19T2214Z_recon-proj-01.md:142-149`, the two-part test, fixed
before the evidence was read:

>     PART 1   it supplies a DERIVATIONAL ARGUMENT — for example from symmetry,
>              a Ward or gauge identity, representation theory, dynamics, an
>              exact identity, or any other explicit derivation — rather than
>              merely defining, asserting, or assuming the projection; AND
>     PART 2   it concludes something about the CONTRIBUTION OF THE DISCARDED
>              COMPLEMENT to the target observable.

`specs/2026-08-19T2214Z_recon-proj-01.md:173`, the positive outcome:

>     FOUND              at least one location satisfies both parts of §3.

### 1.3 The location whose status could not be settled

`derivations/P2-RECON-PROJ-01_projection-adjudication.md:207`:

> **`L2`, `paper/emergent_gr_paper_v2_15.tex:770-788`.**

quoted there at `:209-220`, concluding

> $\Gamma^{(2)}_{\mu\nu,\rho\sigma}(p) = Z_h\,p^2\,\mathcal{P}^{\mathrm{TT}}_{\mu\nu,\rho\sigma}(p) + \mathcal{O}\!\left(\frac{p^4}{\Lambda^2}\right)\times(\text{non-TT})$

`:222-225`:

> **Part 1 is satisfied and is not in doubt.** This is a derivation: a Ward
> identity established at `L1` from diffeomorphism invariance and Symanzik power
> counting, combined with a trace identity, applied in a named projector basis.
> It defines nothing and assumes nothing about the projection.

`:227-234`:

> **Part 2 is where it cannot be settled.** `L2` concludes that **non-TT
> structures enter at `O(p⁴/Λ²)`** while the TT block carries the `p²` term. **If
> the manuscript's "non-TT" set is the complement the axis-TT projection
> discards, then Part 2 is satisfied**, and satisfied strongly: a structure
> entering at `p⁴` contributes nothing to the `p²` coefficient, and the `p²`
> coefficient is the target observable — `L9` records the paper's `Z` as exactly
> "the coefficient of `p²` in the transverse-traceless graviton self-energy", and
> `:781` writes `Z_h p²` in the retained block.

`:236`:

> **What is not stated anywhere is that the two sets are the same.**

`:238-240`, the measurement that established it:

> **MEASURED.** Every repository location mentioning both the axis-TT projection
> and the Barnes–Rivers decomposition was read. **There are three, and all three
> instruct the reader to distinguish them:**

`:301-304`:

> **`L2` is nonetheless the closest existing material in the repository**, and it
> is recorded here so that a later derivation knows where to start: it already
> carries the physics conclusion in the Barnes–Rivers language, and what it lacks
> is the bridge to the basis the extraction actually uses.

---

## 2. `M2` — the gaps, recorded separately

`Q1`'s artifact names **two**, and records them as independent.

### `GAP-A` — the basis identification

**What the artifact states is missing.**
`derivations/P2-RECON-PROJ-01_projection-adjudication.md:261-264`, under
`### 4.1 What would settle it`:

> **One statement, of either sign, in a document:** that for `q` along an axis
> the Barnes–Rivers TT block and the span of `TT_RECIPES` are the same
> five-dimensional space, and that the Barnes–Rivers non-TT blocks are the five
> components `EXT-01` enumerates as discarded — or that they are not.

**What the artifact states about whether it could be established.**
`:266-269`:

> **That statement would be a derivation, not a reading**, which is why this
> outcome is `INCONCLUSIVE` and the reason recorded under `R1` is **`UNDETERMINED
> BY READING`.** The computation it would require is a structural identification
> of two projector bases, and it was not performed.

**The artifact states the work, names its kind — a structural identification of
two projector bases — and records that it was not performed. It does not state
that it cannot be performed.**

### `GAP-B` — the regime transfer

**What the artifact states is missing.**
`:273-287`, under `### 4.2 A second gap, recorded because it is independent of
the first`:

> **Even granting the set identification, `L2` and the repository's own
> measurement are not obviously about the same object.**
>
> `L2` derives its suppression for `Γ⁽²⁾`, the **infrared effective kernel**,
> under Symanzik power counting, **for the improved stress tensor, up to contact
> terms**. `L15` measured a **lattice Proca bubble** at `a = 1`, `m = 0.3`,
> finite `n`, **unimproved**, and found the discarded components' `q²`
> coefficients comparable in magnitude to the retained ones, with every observed
> scaling exponent in `[1.9887, 1.9982]`.
>
> **These are not presented here as contradicting.** They concern different
> objects — an IR effective kernel versus a finite-spacing bubble — and different
> regimes. **But whether `L2`'s conclusion transfers to the object `EXT-01`
> measured is a second question that reading does not answer**, and it would
> survive even if the set identification of `§4` were supplied.

**What the artifact states about whether it could be established.** It states
that reading does not answer it, and that it is a *question* — not that it is
unanswerable. It states the two objects and the two regimes precisely enough
that the question has a subject.

**Independence, in the artifact's own words:** the heading records the gap as
"independent of the first", and the closing clause records that it "would
survive even if the set identification of `§4` were supplied".

### What the artifact records about neither gap

`:289-290`:

> **Neither gap is evidence that `H-EXT-01` is false, and neither is recorded as
> one.**

That remains true of this classification.

---

## 3. `M3` — rule 22's two subclasses, verbatim at the base

`CONVENTIONS.md:1501-1506`:

>     INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
>         A candidate positive argument already exists, and what is missing is
>         a finite, explicit, separately investigable set of bridges.
>
>     INCONCLUSIVE — EVIDENCE INSUFFICIENT
>         No clear next step is identified.

`CONVENTIONS.md:1494-1496`, the ruling the subclasses serve:

> An `INCONCLUSIVE` finding is not terminal when the assessment identifies a
> finite, explicit set of missing bridges whose establishment could change the
> result to a positive finding.

---

## 4. The classification, determined against `M3`

`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`

Each clause of the definition, tested against `M1` and `M2`:

    "a candidate positive argument already exists"
        SATISFIED. L2 satisfies Part 1 of Q1's own test, and the artifact
        records that as "satisfied and is not in doubt" (:222). L2 also
        carries a conclusion of the shape Part 2 asks for — non-TT structures
        entering at O(p⁴/Λ²) while the TT block carries p² — and the artifact
        records at :228-234 what would follow IF the two sets are the same.
        The artifact calls L2 "the closest existing material in the
        repository" and records that it "already carries the physics
        conclusion in the Barnes–Rivers language" (:301-304).

        THE ARGUMENT IS A CANDIDATE, NOT AN ESTABLISHED ONE. Rule 22's
        threshold is that a candidate exists, and a candidate is what is
        measured here.

    "a finite … set of bridges"
        SATISFIED. Two, enumerated by the artifact at §4.1 and §4.2. Not "a
        number of open questions" — two, each with a stated subject.

    "explicit"
        SATISFIED. GAP-A's settling statement is written out verbatim at
        :261-264, in one sentence, with both signs admitted. GAP-B names the
        two objects and the two regimes that would have to be related.

    "separately investigable"
        SATISFIED, and stated by the artifact rather than inferred: §4.2 is
        headed "independent of the first" and records that the second gap
        "would survive even if the set identification of §4 were supplied".

    "whose establishment COULD change the result to a positive finding"
        SATISFIED. Q1's positive outcome is FOUND — "at least one location
        satisfies both parts of §3". The artifact records at :228-230 that if
        the set identification held, "then Part 2 is satisfied". Closing the
        gaps could therefore change Q1's outcome. COULD, not would: the
        artifact admits both signs, and this classification asserts nothing
        about which sign obtains.

**The complementary subclass does not fit.** `INCONCLUSIVE — EVIDENCE
INSUFFICIENT` is defined as "No clear next step is identified." Measured, a
clear next step **is** identified, by the finding itself, in a section the
finding titled "What would settle it".

**This determination is a reading of `Q1`'s own record against rule 22's text.
It re-weighs no evidence and revisits no location.** `Q1` remains
`INCONCLUSIVE`; every location `PROJ-01` classified keeps the classification
`PROJ-01` gave it.

---

## 5. `Resolution path`

    Resolution path
        What is the minimum additional derivation, measurement,
        construction, or evidence that would be sufficient to RESOLVE this
        finding?

**Answered per gap, and symmetrically. Each gap states what would establish the
bridge and what that would then permit, AND what would refute it and what that
would then mean.**

### `GAP-A` — the basis identification

    WHAT WOULD ESTABLISH IT
        A reviewed derivation stating that, for q along an axis, the
        Barnes–Rivers TT block and the span of TT_RECIPES are the same
        five-dimensional space, and that the Barnes–Rivers non-TT blocks are
        the five components EXT-01 enumerates as discarded.

        The artifact names the kind of work: "a structural identification of
        two projector bases" (:268-269).

    ... AND WHAT THAT WOULD THEN PERMIT
        L2 would satisfy Part 2 of Q1's §3 test as well as Part 1, making it a
        location that satisfies both parts. Q1 could then be re-run against
        its own pre-registered outcomes and could return FOUND.

        IT WOULD NOT DO SO AUTOMATICALLY. Q1's outcome is set by a task
        executing Q1's test, not by this path. And GAP-B would remain open.

    WHAT WOULD REFUTE IT
        A reviewed derivation stating that the two sets are NOT the same — the
        artifact admits this sign explicitly: "or that they are not" (:264).

    ... AND WHAT THAT WOULD THEN MEAN
        L2 would fail Part 2 and would cease to be a candidate ground. Q1's
        pre-registered NOT FOUND IN REPOSITORY outcome would be supported on
        this location, and the three repository locations that presently
        instruct a reader to DISTINGUISH the two decompositions (:242-252)
        would be shown to have been right to.

        A refutation is a resolution of GAP-A. It closes the gap.

    WHAT IT WOULD SETTLE ON ITS OWN
        GAP-A only. It does not touch GAP-B, and the artifact says so at
        :285-287.

### `GAP-B` — the regime transfer

    WHAT WOULD ESTABLISH IT
        A reviewed derivation stating that L2's O(p⁴/Λ²) suppression — derived
        for the infrared effective kernel Γ⁽²⁾, under Symanzik power counting,
        for the improved stress tensor up to contact terms — transfers to the
        object EXT-01 measured: a lattice Proca bubble at a = 1, m = 0.3,
        finite n, unimproved.

    ... AND WHAT THAT WOULD THEN PERMIT
        The conclusion L2 carries would be about the object the repository
        actually measures, rather than about a different object in a different
        regime. Combined with GAP-A, that is what a positive Q1 outcome would
        need.

        IT WOULD NOT DO SO ON ITS OWN. Without GAP-A, L2's conclusion is
        about a set not shown to be the discarded complement, whichever regime
        it holds in.

    WHAT WOULD REFUTE IT
        A reviewed derivation stating that the suppression does NOT transfer —
        that the IR improved-kernel statement and the finite-spacing
        unimproved object are related in a way that does not carry the
        conclusion across.

    ... AND WHAT THAT WOULD THEN MEAN
        L2's conclusion would not bear on the measured object even with GAP-A
        closed. EXT-01's measurement — discarded q² coefficients comparable in
        magnitude to the retained ones, exponents in [1.9887, 1.9982] — would
        stand as a measurement of a regime L2's derivation does not reach, and
        Q1 would need a derivational ground other than L2, or none exists.

        This too is a resolution. It ends the line rather than failing it.

    WHAT IT WOULD SETTLE ON ITS OWN
        GAP-B only.

### The two limits, recorded with the path

**1. Establishing any one bridge does not by itself change `Q1`'s verdict while
the other remains open.** Each gap's entry above states what it settles on its
own, and in both cases the answer is: that gap, and not the other. A bounded
task that closes one gap has completed its own work and has not resolved `Q1`.

**2. A bridge may be refuted, and refutation is a resolution.** Both refuting
directions above are written out with what they would mean, and neither is
described as a failure of the task that produced it. A bounded task opened on
either gap is not opened in search of a wanted answer, and returning the
negative sign completes it.

---

## 6. What this classification does not do

**It does not change `Q1`'s verdict.** `Q1` is `INCONCLUSIVE`, with reason
`UNDETERMINED BY READING`, as recorded on the subject branch, at the date
recorded there.

**It does not resolve `H-EXT-01`**, which remains `UNESTABLISHED — NOT ASSUMED
BY RECON-01b`, and it does not bear on `A-EXT-01`, which is definitional and
settled.

**It does not make either bridge more or less likely to hold**, and states
nothing about which sign either would take.

**It performs no part of either bridge.** No derivation, sketch, or outline of
a structural identification of two projector bases, or of a relation between an
infrared effective kernel and a finite-spacing lattice object, appears above.
Defining what would settle a question is permitted; settling it is not.

**It computes nothing.** No `β_V`, no `k`-scan, no pole calculation, no
discarded-space re-measurement. It moves no gate and does not advance
`P2-PHASE-01`.

**It classifies no other `INCONCLUSIVE` record.** The retrospective audit is a
separate task, and this artifact makes no claim about how many other records
would classify either way.

---

## 7. What a later integration may carry, and what it may not

`PROJ-01`'s integration may transport the subclass and the `Resolution path`
above, because they are this task's reviewed result and rule 17 permits
carrying a reviewed classification forward.

**It may not enlarge, narrow, or reinterpret them, and it may not assign a
classification of its own.** Rule 17's prohibition is unchanged by this
artifact.
