# Review — INTEGRATE-SRC-B0 Specification

**Reviewed artifact:** `SPEC integrate src b0(1).md`  
**Reviewed specification SHA-256:** `a93e84b8e1a6a8a92196ef96b50997e23ed9821cac2654a66586636bc3df5fac`  
**Review date:** 2026-08-18  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above.

The revised INTEGRATE-SRC-B0 specification was reviewed for source/base binding, preservation of the SRC-B0 repository-state verdict, conditional versus unconditional source-side prerequisites, the scope of the existing response subtraction, treatment of Γ-defined versus classical-action-defined stress tensors, dimensional measure variation, merge and landing discipline, scope arithmetic, provenance correction, and protection against premature source-side computation or physical adjudication.

## 1. SRC-B0 source verdict — PASS

The integration correctly preserves the source verdict:

`NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`.

The repository does not presently contain a usable source-side configuration with sufficient provenance and structure to execute the proposed attraction/halo calculation.

This remains a repository-state finding, not a claim that the underlying physics is false or absent outside the repository.

## 2. Unconditional prerequisite — PASS

The revised specification correctly identifies one unconditional missing prerequisite:

a usable source configuration.

Without that object, neither a classical source stress tensor nor a full effective-action source observable can be evaluated for the proposed configuration.

## 3. Conditional measure/subtraction prerequisite — PASS

The revised specification correctly removes the earlier overstatement that the programme universally has two prerequisites.

A second prerequisite arises only if the source observable is defined through the full quantum effective action `Γ`, because in that case the unfrozen functional measure reaches the metric variation.

A classical-action-defined stress tensor does not automatically inherit this measure prerequisite.

The integration task does not decide which source definition the programme must ultimately adopt.

## 4. Γ-defined versus S-defined stress tensor — PASS

The specification correctly preserves the SRC-B0 distinction:

- for `T_mu_nu` defined from `Γ`, the measure ambiguity contributes under metric variation;
- for a stress tensor defined directly from a classical source action `S`, that specific functional-measure ambiguity is not automatically present.

The integration does not universalize either route beyond what SRC-B0 established.

## 5. Existing subtraction prescription — PASS

The revised wording correctly states that the repository does contain a frozen subtraction rule, but its scope is limited.

The existing subtraction is authorized for RESPONSE observables and is explicitly scoped away from deleting cosmological SOURCE energy.

Therefore the correct repository statement is not “no subtraction prescription exists,” but rather:

no repository prescription currently authorizes the required SOURCE-side subtraction.

## 6. Metric-variation commutation — PASS

The specification correctly preserves the separate open question of whether subtraction commutes with metric variation.

This is distinct from the existence of the response subtraction itself and must not be silently assumed.

## 7. Measure variation and dimensionality — PASS

The integration correctly preserves the dimensional relation

`det[sqrt(g) g^-1] = (det g)^(d/2 - 1)`.

In four dimensions this becomes `det g`, and the corresponding metric variation is non-zero.

Thus the special four-dimensional simplification does not remove the Γ-defined source ambiguity.

## 8. Source-side subtraction logic — PASS

The revised specification correctly avoids inferring that an ultralocal, configuration-independent term may automatically be subtracted from the cosmological source.

A fixed-metric configuration contrast may cancel such a term algebraically, but a programme-level source subtraction requires an explicit authorized prescription.

The integration therefore preserves the distinction between algebraic cancellation and a governed physical definition.

## 9. Paper 1 provenance boundary — PASS

The integration correctly preserves SRC-B0's finding that this repository cannot determine whether the external source profile is derived, fitted, or otherwise characterized.

Conflicting in-repository descriptions of the external work do not justify adjudicating that provenance.

No external profile, scaling relation, or observable is imported during integration.

## 10. Source-side readiness — PASS

The specification correctly lands SRC-B0 as a scope result rather than as a numerical failure.

The source-side line is not ready for the proposed calculation because the configuration and several interface components are absent or unresolved.

This does not authorize constructing a replacement profile during the integration task.

## 11. No premature source definition ruling — PASS

The integration does not choose between:

- classical-action-defined source stress energy;
- full-effective-action-defined source stress energy;
- absolute source;
- background-subtracted source contrast.

Those remain later scientific decisions once a usable source configuration and its provenance are available.

## 12. Source SHA and provenance — PASS

The revised specification requires the source branch/tip to be re-resolved rather than trusted from an earlier session state.

This is appropriate after rebase/landing activity.

The integration also preserves the prior execution record without rewriting source history.

## 13. Merge, scope, and landing discipline — PASS

The specification maintains the governed integration sequence:

- commit specification;
- commit this review unedited;
- integrate the SRC-B0 source result with the specified merge discipline;
- write the integration report;
- run final verification;
- advance authoritative main only through the specified fast-forward landing path.

The declared scope remains bounded to the authorized additions and zero modifications.

## 14. Report contract — PASS

The final report must preserve, without compression into a stronger statement:

- `NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`;
- one unconditional prerequisite: a usable source configuration;
- one conditional prerequisite: measure/subtraction only for a `Γ`-defined source;
- the existence but inapplicability of the current response subtraction to cosmological source energy;
- the open commutation question between subtraction and metric variation;
- the unresolved choice between `Γ`-defined and classical-action-defined source stress tensors.

This is consistent with the SRC-B0 evidence and the revised specification.

## Final verdict

**`APPROVE FOR EXECUTION`**

The revised integration specification correctly fixes the two prior overstatements:

1. it replaces “two universal prerequisites” with one unconditional and one conditional prerequisite; and
2. it replaces “no subtraction prescription exists” with the more precise finding that the existing frozen subtraction is scoped to response observables and does not authorize the required source-side use.

I find no remaining scientific-scope, source-definition, measure/subtraction, provenance, merge-history, scope, repository-integrity, or governance defect requiring another revision before execution.

This approval applies **only** to the specification with SHA-256:

`a93e84b8e1a6a8a92196ef96b50997e23ed9821cac2654a66586636bc3df5fac`
