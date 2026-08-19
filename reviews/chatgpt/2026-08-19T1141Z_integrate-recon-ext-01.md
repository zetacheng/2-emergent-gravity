# Review — P2-RECON-EXT-01-INTEG

**Reviewed artifact:** `P2-RECON-EXT-01-INTEG(1).md`  
**Reviewed specification SHA-256:** `ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697`  
**Review date:** 2026-08-19  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Integration purpose and scope — PASS

The specification correctly scopes the integration of the completed EXT-01 measurement and its epistemic consequences.

It does not convert the discarded-space measurement into a post-hoc numerical criterion, does not execute RECON-01b, and does not claim that the axis-TT complement is physically negligible.

## 2. A-EXT-01 taxonomy — RESOLVED / PASS

A-EXT-01 is now explicitly classified as a **DEFINITIONAL CONVENTION**, not as a physical assumption.

It defines the quantity used by RECON-01b:

`Z_axis-TT`

as the coefficient extracted relative to the repository's axis-TT projection.

The specification correctly states that this definition does not establish physical completeness of the projection.

## 3. H-EXT-01 — RESOLVED / PASS

H-EXT-01 is now a directional physical hypothesis:

`Z_axis-TT = Z_physical`

with the corresponding claim that the discarded external complement does not alter the physically relevant gravitational observable.

Its status is explicitly:

`UNESTABLISHED — NOT ASSUMED BY RECON-01b`

This is the critical separation required for RECON-01b to proceed without silently assuming the conclusion of the projection-completeness question.

## 4. Definition versus physical completeness — PASS

The specification preserves the distinction:

`definition != completeness hypothesis`

RECON-01b may depend on A-EXT-01.

RECON-01b does not depend on H-EXT-01 being true.

A future proof that the complement is irrelevant would establish the physical-completeness proposition; it would not retroactively turn the definition itself into a falsifiable claim.

## 5. Scope of future RECON-01b claims — PASS

The specification correctly narrows the interpretation of future RECON-01b results.

Results must be stated relative to the axis-TT-defined observable and must not be promoted to an unqualified full gravitational `Z` unless H-EXT-01 or an equivalent completeness result is independently established.

This makes RECON-01b a conditional spin-2-sector reconstruction test.

## 6. Channel-separation evidence boundary — PASS

The specification correctly records that a calculation defined inside the axis-TT subspace cannot independently establish that spin-1/0 residues vanish.

The beta-V reconstruction line therefore cannot be used as independent evidence for channel selection when that selection is already built into the observable definition.

A separate unprojected channel/pole calculation is required for the manuscript's stronger channel-separation claim.

## 7. EXT-01 magnitude finding — PASS

The integration preserves the measurement that the discarded external space is not numerically negligible at the pre-registered diagnostic point.

The specification requires the robust summary quantities to be re-derived from the landed coefficients rather than inferred from signed percentage shares.

In particular, the intended summaries distinguish the aggregate discarded-to-retained magnitude from the largest individual discarded component relative to a typical retained component.

## 8. No post-hoc threshold — PASS

No numerical kill criterion is created from the observed EXT-01 result.

This correctly preserves the measure-first ruling.

Any future criterion must arise from a separate physical or structural adjudication rather than being selected after seeing the discarded-space magnitude.

## 9. TT_RECIPES / Component 5 boundary — PASS

The integration records the documentary finding that axis-TT is used and has programme-level definitional motivation, while the physical irrelevance of its complement has not been derived.

It does not silently upgrade this into a proof of projection completeness.

The remaining authority/completeness question is kept explicit.

## 10. Component 9 boundary — RESOLVED / PASS

Component 9 is now described as deferred until the **projection/completeness adjudication** is settled.

This is consistent with A-EXT-01 already settling the operational observable definition.

The earlier wording, which implied that the observable definition itself remained unsettled, has been removed.

## 11. Execution-layer dispositions — RESOLVED / PASS

D-1 through D-3 are correctly classified as execution-layer dispositions adopted for this task and reversible by PI adjudication.

They are not presented as permanent scientific rulings by the Researcher.

Open findings remain distinct from decisions.

## 12. Assumption / hypothesis review governance — PASS

The specification introduces a strong forward governance rule for programme-level assumptions, hypotheses, and definitional conventions.

The proposed record schema includes:

`ID / Type / Status / Exact statement / Scope / What depends on it / What does NOT depend on it / Evidence / Falsifier or resolution condition / Review / Review SHA / Date / Supersedes`

This is sufficient to preserve the epistemic status and provenance of future assumptions.

## 13. Review binding for assumptions — PASS

The specification correctly requires the review to be bound to the exact reviewed statement.

If the registered statement is edited later, the previous review no longer applies and a new review is required.

This prevents a historical approval from silently attaching to materially different assumption wording.

## 14. Register-location discipline — PASS

The executor must inspect the scopes and vocabularies of the repository's existing registers before placing A-EXT-01, H-EXT-01, or their review record.

If no existing register admits a required class, the executor must return the issue rather than inventing a new location or status vocabulary.

This is the correct governance boundary.

## 15. Evidence-architecture separation — PASS

The specification appropriately records two distinct validation questions:

- whether the selected axis-TT sector reconstructs the expected gravitational structure; and
- whether the microscopic theory dynamically selects the spin-2 channel with vanishing unwanted residues.

These may be sequentially complementary, but the first cannot serve as independent evidence for the second when the projection is definitional.

This is a model-level evidence-architecture clarification, not a contradiction in the EXT-01 measurement.

## 16. Existing scientific claims — PASS

The integration does not claim that EXT-01 disproves the axis-TT observable.

Nor does it claim that the large discarded components are physical spin-0/1 poles.

EXT-01 establishes that numerical smallness cannot presently justify discarding the complement; pole content and physical relevance remain separate questions.

## 17. Repository and landing discipline — PASS

The specification separates the integration task from later RECON-01b execution.

The scientific source result is to be integrated without rewriting its measured result into a stronger conclusion.

Branch and landing behavior remain governed by the repository's science-branch integration policy and the task-specific manifest.

## 18. Acceptance criteria — PASS

The acceptance criteria are mutually compatible with the scientific and governance rules above.

The only minor editorial issue observed is the phrase `a execution-layer disposition`, which grammatically should read `an execution-layer disposition`.

This is non-substantive and does not alter execution semantics or require re-issuance.

## 19. Remaining STOP-level defects

None found.

The substantive issues identified in the prior review have been resolved:

1. A-EXT-01 is a definitional convention rather than a physical assumption.
2. H-EXT-01 is a directional, falsifiable physical hypothesis.
3. H-EXT-01 is explicitly not assumed by RECON-01b.
4. D-1 through D-3 have the correct execution-layer authority.
5. Component 9 is deferred on projection/completeness adjudication rather than observable definition.
6. Assumption/hypothesis reviews are version-bound and preserved as repository provenance.

## Final verdict

**`APPROVE FOR EXECUTION`**

`P2-RECON-EXT-01-INTEG(1).md` may be executed.

This approval is bound exclusively to the exact uploaded specification bytes with SHA-256:

`ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697`

The central scientific constraint to preserve is:

**RECON-01b may use the axis-TT observable as an explicit definitional convention, but it must not assume or imply that this observable equals the full physical gravitational response. That equivalence remains the separately reviewable and falsifiable H-EXT-01 question, and the beta-V reconstruction result cannot independently establish channel separation that is already built into its projection.**
