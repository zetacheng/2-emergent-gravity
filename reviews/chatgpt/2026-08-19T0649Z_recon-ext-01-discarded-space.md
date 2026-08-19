# Review — P2-RECON-EXT-01

**Reviewed artifact:** `P2-RECON-EXT-01(1).md`  
**Reviewed specification SHA-256:** `e0effac3ac0584c36f225542ced16fa5a72ec07f08366ed6b924c3784879c7cd`  
**Review date:** 2026-08-19  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Purpose and scientific boundary — PASS

The specification correctly defines a target-blind diagnostic of the external space discarded by the RECON-01b axis-TT projection.

It does not execute RECON-01b, does not compute the target-bearing beta ratio, and does not adjudicate whether the discarded space is physically acceptable.

The task supplies evidence for that later decision.

## 2. Existing blind target — PASS

The previously frozen blind target is retained unchanged.

This task does not modify it, re-register it, evaluate it, or compare any diagnostic result against it.

The revised specification also avoids reproducing the target literal in its own operative text.

## 3. Blind-output discipline — RESOLVED / PASS

The previous review identified a self-referential compliance problem: the specification reproduced a literal that C7 simultaneously prohibited from task output.

The revised specification resolves this.

C7 now applies to the measurement artifact, newly added diagnostic script, and diagnostic outputs, while pre-existing governance inputs such as the specification and bound review are excluded from that content check.

The scientific outputs remain target-blind.

## 4. Pre-registration of k — PASS

The diagnostic momentum is pre-registered before the result-producing execution.

The pre-registration commit must precede the result commit.

This prevents selecting the diagnostic point after observing the discarded-space result.

## 5. One pre-registered k only — PASS

The task measures the discarded/retained decomposition at one pre-registered k.

It does not perform a k-scan.

The revised wording no longer incorrectly describes the output as a single number when M5 requires multiple component measurements.

## 6. Discarded-space measurement — PASS

M5 measures the relevant discarded external components and retained space, including their magnitudes and fractions.

The measurement is descriptive.

No threshold is pre-imposed and no numerical result automatically becomes a PASS or FAIL verdict.

## 7. No post-hoc kill criterion — PASS

The task does not invent a kill threshold before observing the diagnostic structure.

The intended epistemic order is:

`measure -> report -> PI adjudication`

Only after the evidence exists may a later task determine whether symmetry, scaling, or another structural argument justifies a kill criterion.

## 8. Internal versus external projection distinction — PASS

The task is correctly motivated by the RECON-01B-B0 finding that all four internal Proca T/L sectors lie inside the axis-TT construction.

That finding removes the earlier mixed-sector blind-spot concern but does not establish completeness of the external projection.

EXT-01 therefore measures the remaining external discarded space rather than repeating the internal-sector analysis.

## 9. TT_RECIPES provenance evidence — PASS

M7 appropriately gathers documentary provenance for `TT_RECIPES`.

It distinguishes evidence that a document merely uses or selects the recipe from evidence that supplies a reason or derivation for that selection.

The task does not itself adjudicate whether the recipe is sufficiently derived, frozen, inherited, or merely implemented.

That governance/scientific-authority decision remains with the PI after the evidence is collected.

## 10. Component 5 boundary — PASS

The task may inform the later Component 5 governance adjudication but does not silently upgrade or downgrade Component 5.

This preserves the distinction between measurement of the projection and authority for choosing the projection.

## 11. Component 9 boundary — PASS

Component 9 specification sufficiency remains outside this task.

EXT-01 does not use its diagnostic result to reclassify Component 9.

A separate documentary sufficiency determination may follow if still required before RECON-01b execution.

## 12. Existing-code discipline — PASS

Existing reconstruction code remains frozen.

If the diagnostic cannot be performed without modifying existing `scripts/` content contrary to the specification, execution stops rather than contaminating the clean-room construction.

Any authorized diagnostic code is separately scoped and auditable.

## 13. Recovered-code disclosure — PASS

M6 requires disclosure of any imported recovered-pipeline code and any target-bearing imports.

This is an important clean-room safeguard.

A diagnostic that accidentally imports historical target-bearing machinery cannot be presented as an independent target-blind measurement.

## 14. Measurement versus adjudication — PASS

The specification maintains a clear division:

- EXT-01 measures what the projection discards;
- EXT-01 records documentary provenance;
- EXT-01 does not decide whether the discarded contribution is acceptable;
- EXT-01 does not decide whether `TT_RECIPES` has sufficient authority;
- EXT-01 does not decide the final RECON-01b target comparison.

This is the correct scope.

## 15. Repository effect — PASS

The task is a measurement task, not a landing task.

Authoritative `main` must remain unchanged.

Any later integration requires its own reviewed integration specification under the repository's `science/*` policy.

## 16. Abort conditions and kill conditions — PASS

A1-A5 are genuine execution stop conditions.

K1-K4 constrain the scientific measurement without turning an observed magnitude into an unauthorized scientific verdict.

The two classes are not conflated.

## 17. Acceptance criteria — PASS

C1-C10 are mutually compatible after the revision.

In particular:

- pre-registration precedes measurement;
- the diagnostic remains target-blind;
- the relevant output extent is explicitly defined;
- no beta/k scan is performed;
- provenance is recorded without adjudication;
- existing construction code is preserved;
- `main` remains unmoved.

## 18. Relation to the RECON-01b readiness decision — PASS

A successful EXT-01 execution does not validate RECON-01b.

It closes one residual uncertainty: whether the external axis-TT projection discards a numerically or structurally relevant space at the pre-registered diagnostic point.

The result then informs the PI's decision about whether a projection-completeness criterion is needed before blinded RECON-01b execution.

## 19. Remaining specification defects

None found at STOP level.

The two issues identified in the previous review have been resolved:

1. the self-referential blind-target/output contradiction; and
2. the inaccurate description of a multi-component decomposition as “one number”.

## Final verdict

**`APPROVE FOR EXECUTION`**

`P2-RECON-EXT-01(1).md` may be executed.

This approval is bound exclusively to the exact uploaded specification bytes with SHA-256:

`e0effac3ac0584c36f225542ced16fa5a72ec07f08366ed6b924c3784879c7cd`

The central scientific constraint to preserve is:

**Measure the external discarded/retained decomposition at the pre-registered diagnostic momentum without exposing or evaluating the blind beta target, without imposing a post-hoc threshold, and without converting the measurement into a premature adjudication of projection completeness or TT_RECIPES authority.**
