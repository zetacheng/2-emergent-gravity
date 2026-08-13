# Pre-execution review — `OPEN-AC-4`: exact and remnant symmetry, and whether `C-i` reads plainly

**Review disposition: APPROVED FOR EXECUTION.**

**Reviewed specification SHA-256:** `bf145fe83deff22aae028badc7f44c17820a6cd5e2253d4ea04b35b699a63d7b`

**Reviewed specification:** `Task specification — OPEN-AC-4: exact and remnant symmetry, and whether C-i reads plainly`

**Specification evidence base:** `1b569851a914589242024c4dde7d2eb020e3800c`

## 1. Review conclusion

The specification is internally coherent and is approved for execution as written.

The previous blocking inconsistency has been corrected. Section 7 now contains three distinct Rule 16 junctions, and the report contract correctly requires **all three junctions**. There is no remaining conflict between the Rule 16 section and the reporting obligation.

The scientific scope is also appropriately narrowed. The specification no longer promotes the exploratory Wilson-form kernel into the frozen microscopic theory. It separates:

1. the conditional symmetry result for the **uniform flavour-singlet scalar candidate under the exploratory Wilson-form kernel**; and
2. the repository-level question of whether `OPEN-AC-4` can close before the canonical lattice Dirac operator is frozen.

That separation is essential and is correctly represented by Verdict A and Verdict B.

## 2. Verdict architecture

The two-verdict structure is approved.

Verdict A is explicitly candidate- and kernel-scoped. The specification requires the candidate class and kernel to appear in the same sentence as the verdict, and repeats that scope in the corresponding consequence. This prevents a conditional Wilson-kernel result from being misreported as a statement about all condensates or about the frozen microscopic action.

Verdict B separately determines whether the repository has enough ontological information to close `OPEN-AC-4`. The expected `B-NOT-CLOSABLE` outcome is framed as a prediction rather than an instruction, and its consequence correctly preserves `OPEN-AC-4` as open if the canonical lattice operator is not frozen.

The two verdicts therefore answer genuinely different questions and do not collapse conditional physics into a governance conclusion.

## 3. Symmetry and Goldstone logic

The revised Wilson statement is acceptable and appropriately precise:

> The standard Wilson operator does not satisfy the Ginsparg-Wilson relation and therefore does not possess the corresponding exact lattice chiral symmetry at finite lattice spacing.

This is materially better than the earlier phrase about carrying no “Ginsparg-Wilson remnant”.

The specification also correctly distinguishes continuous from discrete symmetry breaking. It does not infer Hessian stability from the absence of Goldstone directions. Instead, it asks only how `C-i` must be read for the examined candidate class. That is the correct boundary for this task.

The failure-mode list in §2(e) is sufficiently adversarial: non-singlet breaking of exact `U(N)_V`, an unidentified continuous remnant, and lattice exact symmetries are each treated as possible falsifiers rather than assumed away.

## 4. Acceptance-criteria consistency

A4 is now internally correct: it requires **seven** individual checks — §2(a), §2(b), §2(c), §2(d), and the three failure modes in §2(e).

A5 correctly requires both verdicts and makes omission of Verdict A's scope a STOP.

A6 correctly protects pre-registration by requiring the selected consequences to be transcribed rather than rewritten.

A8 and A9 preserve the task's central evidentiary property: four additions, zero modifications, and no existing repository file changed.

A10 appropriately treats `P7` as evidentially vacuous and places the proof of non-modification on A9 instead.

The report contract is now consistent with the body of the specification, including the requirement to report **all three** Rule 16 junctions.

## 5. Rule 16

The three junctions are appropriately separated and all should remain in the execution report:

1. **No Goldstone directions is not a stability result.** It only determines how the stability criterion is to be read.
2. **Continuum frozen-action symmetry is not automatically the symmetry of the regularised exploratory kernel.**
3. **A narrow Verdict A does not close `OPEN-AC-4`; closure is Verdict B's question.**

These are all material limits. None is redundant.

## 6. Non-blocking observations

The specification intentionally records that the author had not personally read the lattice ontology and route documents even though §0a contains quoted findings from them. In context this is understandable as provenance inherited from review rather than an assertion of personal inspection, and A4 explicitly requires the executor to verify the relevant statements from those documents. I do not treat this as a defect.

No further wording or structural correction is required before execution.

## 7. Review disposition

**APPROVED FOR EXECUTION.**

The executor should use the specification exactly at SHA-256 `bf145fe83deff22aae028badc7f44c17820a6cd5e2253d4ea04b35b699a63d7b`. A different digest is a different specification and is not covered by this review.
