# Pre-execution review — integrate governance debt register C-c

**Review status:** APPROVED FOR EXECUTION AND LANDING

reviewed specification SHA-256: `e99e39a53e0222d1ba8a3e065b3968e48408508e341b0d3d0a175ea365d3d8f1`

Reviewed specification: `SPEC integrate debt register cc(1).md`

## Determination

**APPROVED. No blocking specification defect remains.**

This review is bound to the exact specification digest recorded above.

## Review findings

The previous Rule 20 ambiguity has been corrected. The specification now permits only the narrowly defined pre-push hygiene amendment under Rule 20; force-push and branch deletion remain prohibited without exception.

The revision-attribution requirement is also corrected. The historical `13/50`, `15/52`, and `17/54` measurements are to be re-measured at their respective revisions rather than described as if all three belonged to one evidence base.

The Rule 16 wording has likewise been narrowed appropriately: completion refers to the planned `C-a` / `C-b` / `C-c` sequence, not to closure of the wider governance gap.

## Integration architecture

The integration design is acceptable. It requires merge semantics to be classified before blob equality is interpreted, preserves both zero-deletion and direct in-order subsequence measurements, and keeps the eleven-entry governance-debt register frozen during integration.

The specification correctly preserves `OPEN-CC-3` as a cross-reference rather than duplicating the science-side open item, and it distinguishes the governance-debt register from the P4 superseded-branch register in `docs/BRANCHING_POLICY.md`.

The newly identified classification/provenance gap is handled correctly as **identified but not registered by this task**. The integration task is not authorised to create an additional debt entry, and it must not silently expand the frozen register from eleven entries.

## Evidence and governance boundaries

The task appropriately distinguishes repository facts from factual assertions made by specifications about their own bytes and historical revisions. This is consistent with the governance lessons incorporated in C-a and C-b.

The integration must not represent landing C-c as closing governance debt. Landing completes the planned C-a/C-b/C-c sequence: prose conventions have been consolidated, two selected mechanisms have been built, and the known debt set has an authoritative register. Residual enforcement and provenance gaps remain open as recorded.

The phrase that nothing remains in "that line" should be read only as referring to the planned C-a/C-b/C-c task sequence. The execution report should use the specification's narrower Rule 16 formulation and must not broaden this into a claim that no governance work remains.

## Landing disposition

Execution and landing may proceed only if all stop-governing acceptance criteria pass, including the specified merge checks, protected-path comparisons, register invariants, checker runs, validators, and fast-forward-only landing conditions.

**Final verdict: APPROVED FOR EXECUTION AND LANDING.**

Any byte change to the reviewed specification requires the review binding to be reconsidered.
