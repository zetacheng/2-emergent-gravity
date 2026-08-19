# `H-EXT-01` — physical completeness of the axis-TT projection

**Canonical location for this entry.** It was first landed at
`ff21836549d9f9e18deab172f1f3f8e02cf8064f` as a `DECISION_LOG.md` entry dated
2026-08-19; **that entry is unchanged and stands as historical record.** This
file is where the entry lives going forward.

---

# PART 1 — THE ENTRY

    ID       H-EXT-01
    Type     PHYSICAL HYPOTHESIS — directional, falsifiable.
    Status   UNESTABLISHED — **NOT ASSUMED BY `RECON-01b`.**

**Exact statement:**

> The discarded external complement makes no contribution to the physically
> relevant gravitational observable, so that `Z_axis-TT = Z_physical`.

    Scope    The axis-TT projection as the repository defines it, and the
             observable RECON-01b extracts.

    What depends on it
             Nothing currently in the repository. No landed result asserts
             it and no pending task requires it.

    What does NOT depend on it
             RECON-01b. **RECON-01b requires only the definition
             A-EXT-01; it does not require H-EXT-01 to be true, and does
             not assume it.** A reader who takes RECON-01b to presuppose
             H-EXT-01 has read the design backwards.

    Evidence derivations/P2-RECON-EXT-01_discarded-external-space.md.
             The measurement bears on the hypothesis and does not settle
             it: it establishes that the discarded directions cannot be
             neglected on grounds of magnitude, and establishes nothing
             about whether they contribute to the physically relevant
             observable.

    Falsifier or resolution condition
             REFUTED if the complement is shown to contribute irreducibly
             to the target observable. ESTABLISHED if the complement is
             derived to make no contribution to it. The adjudication is
             routed to RECON-PROJ-01 and is not performed by any landed
             task.

    Review   PART 2 of this file. The review artifact it reproduces is
             reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md,
             which remains in place as the landed original.

    Statement SHA
             e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
             THIS IS THE BINDING PIN — the SHA-256 of the exact-statement
             bytes above, and of nothing else. Editing the statement
             invalidates the attached review and requires re-review.

    Review Artifact SHA
             e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953
             Provenance, not a pin. It identifies the review artifact.

    Date     2026-08-19
    Supersedes
             A single earlier draft that merged this hypothesis with the
             definition A-EXT-01 and treated the definition as itself
             falsifiable. That draft is superseded by the two-entry form.

**The field labels above are the disambiguated ones.** The entry as landed at
`ff218365` carried a single field named `Review SHA` whose content was in fact
the statement digest — the name said review, the content was a statement
binding. **The digest is unchanged**; only the labels are, and a label change
does not touch the pin.

## The definitional counterpart

**`A-EXT-01` is canonical in `CONVENTIONS.md`** and has no entry in
`assumptions/`. It is a **DEFINITIONAL CONVENTION**, not a hypothesis: it
cannot be refuted, and `Z_axis-TT` remains well-defined whatever is later
established about `H-EXT-01`.

**`H-EXT-01` is the falsifiable half of the pair.** If the complement is later
derived to make no contribution to the target observable, what is upgraded to a
theorem is *the physical completeness of the projection for this observable*.
If the complement is shown to contribute irreducibly, **`H-EXT-01` is refuted,
and the outcome is not that `A-EXT-01` was wrong but that `Z_axis-TT` is not
the full physical `Z`.**

---

# PART 2 — THE REVIEW

    Function: Reviewer
    Kind      ASSUMPTION REVIEW of Part 1 of this file.
              NOT a specification review.
    Author    the Reviewer function, ChatGPT
    Date      2026-08-19
    Original  reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md
              sha256 e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953

## What this review is, stated before it is read

**The executor did not receive a free-standing assumption-review document.**
The Reviewer's assessment of `H-EXT-01` was delivered inside the pre-execution
review of the integration specification `P2-RECON-EXT-01-INTEG`, bound to
specification bytes
`ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697`. **The
indented and quoted blocks below are the Reviewer's text, with that review's
own section numbers. Nothing is attributed to the Reviewer that the Reviewer
did not write.**

## What the review accepted

**§3 of the bound review, verdict `RESOLVED / PASS`:**

> H-EXT-01 is now a directional physical hypothesis:
>
> `Z_axis-TT = Z_physical`
>
> with the corresponding claim that the discarded external complement does not
> alter the physically relevant gravitational observable.
>
> Its status is explicitly:
>
> `UNESTABLISHED — NOT ASSUMED BY RECON-01b`
>
> This is the critical separation required for RECON-01b to proceed without
> silently assuming the conclusion of the projection-completeness question.

**§4, verdict `PASS`, on the separation from the definitional entry:**

> The specification preserves the distinction:
>
> `definition != completeness hypothesis`
>
> RECON-01b may depend on A-EXT-01.
>
> RECON-01b does not depend on H-EXT-01 being true.
>
> A future proof that the complement is irrelevant would establish the
> physical-completeness proposition; it would not retroactively turn the
> definition itself into a falsifiable claim.

## What the review required to be changed

**§19 records the substantive issues the prior draft carried, and that they are
resolved:**

> 1. A-EXT-01 is a definitional convention rather than a physical assumption.
> 2. H-EXT-01 is a directional, falsifiable physical hypothesis.
> 3. H-EXT-01 is explicitly not assumed by RECON-01b.

**The Researcher's earlier draft merged the hypothesis with the definition and
treated the definition as itself falsifiable — a type error.** The two-entry
form, the directional wording, and the `NOT ASSUMED` status all follow this
review. **The correction is recorded, not silently absorbed.**

## What the review did not address

**It did not assess whether `H-EXT-01` is true.** No part of the review bears
on the physics; it assesses the classification, the wording, and the dependency
claim.

**It did not address the field labels of Part 1.** The `Statement SHA` /
`Review Artifact SHA` split postdates this review and is a label change; the
statement it reviewed is byte-identical to the one above, and the pin verifies.

**It did not adjudicate `RECON-PROJ-01`**, which is where the falsifier's
resolution is routed.
