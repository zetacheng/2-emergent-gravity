# Review — P2-REGISTRY-SPLIT-01

**Reviewed artifact:** `P2-REGISTRY-SPLIT-01(1).md`  
**Reviewed specification SHA-256:** `6a90c815d4e1912c431e827e0887eb723f2d6bde507782e6245238ad94a49bad`  
**Review date:** 2026-08-19  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Registry-split purpose — PASS

The specification correctly separates four epistemic/governance classes that had previously been mixed across repository files:

- definitional conventions;
- physical assumptions/hypotheses;
- PI decisions;
- specification reviews.

The split improves auditability without rewriting scientific history.

## 2. Definitional conventions — PASS

The revised specification correctly excludes definitional conventions from `assumptions/`.

Definitional material remains canonical in `CONVENTIONS.md`.

This preserves the distinction:

`definition != physical assumption`.

A-EXT-01 therefore remains in `CONVENTIONS.md` and is not duplicated as an assumption entry.

## 3. Physical assumptions and hypotheses — PASS

`assumptions/` is correctly scoped to physical assumptions and physical hypotheses.

H-EXT-01 is a proper candidate for this registry because it is a directional, unestablished scientific proposition rather than a definition.

The specification does not force definitional conventions into the assumption taxonomy.

## 4. PI decisions — PASS

`decisions/` is correctly scoped to PI rulings and decisions.

This preserves the distinction between scientific propositions and programme/governance authority.

Historical decision provenance is retained rather than rewritten.

## 5. Specification reviews — PASS

`reviews/` remains the home for specification reviews and other review artifacts under the repository's existing review-layout conventions.

The task does not unnecessarily create a competing by-kind review hierarchy where the repository already uses a by-author convention.

## 6. Statement SHA semantics — RESOLVED / PASS

The prior ambiguity around `Review SHA` is resolved.

The specification now distinguishes:

`Statement SHA = SHA256(exact statement bytes)`

from:

`Review Artifact SHA = SHA256(review artifact bytes)`.

The first is the binding pin between a scientific statement and the review that applies to that exact wording.

The second identifies the review artifact itself.

This is the correct semantic split.

## 7. Statement-edit invalidation rule — PASS

The specification correctly requires that editing an exact registered statement invalidates the previous review binding.

A materially changed statement therefore requires a new review rather than inheriting approval from an older wording.

This is consistent with the repository's exact-byte review discipline.

## 8. M8 migration safeguard — PASS

Before renaming or relabelling legacy SHA fields, M8 re-checks what the existing pin actually hashes.

If the legacy value does not match the expected statement bytes, execution stops rather than silently normalising the historical record.

This is an appropriate migration safeguard.

## 9. A-EXT-01 migration — PASS

A-EXT-01 remains in `CONVENTIONS.md`.

No assumption stub is required.

Cross-reference may be provided by registry documentation, but the canonical record stays with definitional conventions.

This avoids reintroducing the taxonomy error the split is designed to fix.

## 10. H-EXT-01 migration — PASS

H-EXT-01 is moved or represented canonically under `assumptions/` while preserving the historical DECISION_LOG record as provenance.

The old record is not erased.

A relocation/canonical-location note is preferable to rewriting history.

## 11. Decision-log provenance — PASS

The specification correctly preserves historical entries in `DECISION_LOG.md`.

Where a scientific hypothesis is moved to a new canonical registry, the historical location remains part of the provenance chain.

This prevents the migration from creating a false impression that the repository always had the new taxonomy.

## 12. PI-decision review status — PASS

The revised specification does not present the effect of PI-decision reviews as a permanent rule enacted by the Researcher.

It is explicitly labelled a:

`PROVISIONAL execution-layer disposition`

and remains reversible by PI adjudication.

This is the correct authority boundary for the present task.

## 13. Recommended future PI ruling — NON-BLOCKING

The specification appropriately leaves the following authority rule for explicit PI adjudication:

PI decisions take effect when issued; reviews of those decisions are mandatory but non-gating; a review may identify defects and recommend revision or supersession but does not suspend the decision unless the PI so rules.

This is not falsely represented as already enacted.

## 14. Historical review layout — PASS

Existing `reviews/pi/` or other historical review paths may remain grandfathered where required by repository history.

The registry split does not require retroactive renaming solely for aesthetic uniformity.

## 15. No historical rewrite — PASS

The task preserves provenance.

Legacy entries are retained, cross-referenced, or marked with canonical relocation rather than deleted and recreated as if the new taxonomy had always existed.

This is the correct migration model.

## 16. Repository semantics — PASS

The revised taxonomy is coherent:

`CONVENTIONS.md -> definitions/conventions`

`assumptions/ -> physical assumptions and hypotheses`

`decisions/ -> PI decisions`

`reviews/ -> reviews`

This gives future tasks a stable answer to the question: what kind of epistemic object is this statement?

## 17. Review co-location and provenance — PASS

Where assumption/hypothesis records carry a review reference, the exact statement pin and review-artifact identity are both preserved.

This supports long-term auditing without forcing all review artifacts into a new directory convention.

## 18. Acceptance structure — PASS

The revised acceptance criteria are consistent with the migration rules.

No criterion requires the executor to invent a new epistemic class, register status, or SHA meaning.

Legacy records are checked before migration, and canonical locations are determined from the revised taxonomy.

## 19. Remaining specification defects

None found at STOP level.

The substantive issues identified in the previous review have been resolved:

1. definitional conventions are no longer placed inside `assumptions/`;
2. Statement SHA and Review Artifact SHA are semantically separated;
3. PI-decision review effectiveness is explicitly provisional rather than misrepresented as a permanent Researcher-made authority rule.

One minor wording point remains non-blocking: broad prose suggesting every epistemic record “carries its review with it” should be read in the context of reviewed scientific propositions and decisions, not as a claim that every conventional definition necessarily uses the same Part-1/Part-2 layout.

## Final verdict

**`APPROVE FOR EXECUTION`**

`P2-REGISTRY-SPLIT-01(1).md` may be executed.

This approval is bound exclusively to the exact uploaded specification bytes with SHA-256:

`6a90c815d4e1912c431e827e0887eb723f2d6bde507782e6245238ad94a49bad`

The central governance result to preserve is:

**Definitions, physical assumptions/hypotheses, PI decisions, and reviews are distinct epistemic objects with distinct canonical homes. Exact scientific statements are review-bound by a Statement SHA, review artifacts retain their own independent identity, and historical provenance is migrated by cross-reference rather than rewritten.**
