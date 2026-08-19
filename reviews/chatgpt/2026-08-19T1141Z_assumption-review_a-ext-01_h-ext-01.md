# Assumption review — `A-EXT-01` and `H-EXT-01`

    Function: Reviewer

    Kind        ASSUMPTION REVIEW. This is NOT a specification review.
    Subjects    A-EXT-01, a definitional convention
                H-EXT-01, a physical hypothesis
    Date        2026-08-19

**Landed as its own artifact so that each register entry can pin it, and so
that the review is not summarised into the entry it reviews.**

---

## 0. Provenance of this record, stated first

**The executor did not receive a free-standing assumption-review document.**
The Reviewer's assessment of these two statements was delivered inside the
pre-execution review of the integration specification
`P2-RECON-EXT-01-INTEG`, bound to specification bytes
`ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697`, and
committed at
`reviews/chatgpt/2026-08-19T1141Z_integrate-recon-ext-01.md`
(sha256 `3c91d17d1748b4d6c8fc1701098ebdda3e15c3799b51d9c64b0136fe28e79666`).

**This record quotes that review verbatim and attributes nothing to the
Reviewer that the Reviewer did not write.** The section numbers below are
that review's own. **The executor authored the framing sentences and the
digests; every indented block is the Reviewer's text.**

---

## 1. `A-EXT-01` — reviewed as a definitional convention

**Statement reviewed**, pinned by digest:

    sha256  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378

> For `RECON-01b`, `Z_axis-TT` is defined as the coefficient extracted after
> the repository's axis-TT projection. This is a definition of the observable
> used by the reconstruction pipeline, not a derived statement that the
> discarded external complement is physically negligible. All `RECON-01b`
> results must therefore be stated relative to `Z_axis-TT`, and must not be
> identified with the full gravitational response unless that equivalence is
> independently established.

**The Reviewer's assessment, §2, verdict `RESOLVED / PASS`:**

> A-EXT-01 is now explicitly classified as a **DEFINITIONAL CONVENTION**, not
> as a physical assumption.
>
> It defines the quantity used by RECON-01b:
>
> `Z_axis-TT`
>
> as the coefficient extracted relative to the repository's axis-TT
> projection.
>
> The specification correctly states that this definition does not establish
> physical completeness of the projection.

## 2. `H-EXT-01` — reviewed as a physical hypothesis

**Statement reviewed**, pinned by digest:

    sha256  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

> The discarded external complement makes no contribution to the physically
> relevant gravitational observable, so that `Z_axis-TT = Z_physical`.

**The Reviewer's assessment, §3, verdict `RESOLVED / PASS`:**

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

## 3. The distinction between them, as reviewed

**The Reviewer's assessment, §4, verdict `PASS`:**

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

## 4. What the correction changed

**The Reviewer's assessment, §19, listing what the prior review's substantive
issues were and recording them resolved:**

> 1. A-EXT-01 is a definitional convention rather than a physical assumption.
> 2. H-EXT-01 is a directional, falsifiable physical hypothesis.
> 3. H-EXT-01 is explicitly not assumed by RECON-01b.

**The Researcher's earlier draft treated the definition as itself falsifiable
— a type error.** The two-entry form, the directional wording of `H-EXT-01`,
and its `NOT ASSUMED` status all follow this review. **The correction is
recorded here, not silently absorbed.**

## 5. Consequence for `RECON-01b` claims, as reviewed

**The Reviewer's assessment, §5 and §6, both `PASS`:**

> Results must be stated relative to the axis-TT-defined observable and must
> not be promoted to an unqualified full gravitational `Z` unless H-EXT-01 or
> an equivalent completeness result is independently established.
>
> This makes RECON-01b a conditional spin-2-sector reconstruction test.

> The specification correctly records that a calculation defined inside the
> axis-TT subspace cannot independently establish that spin-1/0 residues
> vanish.
>
> The beta-V reconstruction line therefore cannot be used as independent
> evidence for channel selection when that selection is already built into the
> observable definition.

## 6. Binding rule

**A `Review SHA` binds to the exact bytes reviewed.** The digests in `§1` and
`§2` are taken over the statement text as landed, byte for byte.

**If either statement is later edited, its digest changes and the pin visibly
breaks. The review recorded here no longer applies to the edited statement,
and a new review is required.** A review is never carried across a wording
change — the same exact-byte principle the specification reviews already use.

**The bound review's own verdict:** `APPROVE FOR EXECUTION`, bound exclusively
to `ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697`.
