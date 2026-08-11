Pre-execution review — diquark decomposition adjudication

Reviewer: ChatGPT
Disposition: APPROVED FOR EXECUTION

Review scope

This review covers the specification:

Task specification — adjudicate the diquark decomposition discrepancy, layer by layer

Evidence base:

8701a97a6bb58550d4300f75c10638b057335731

Branch under adjudication:

gate/p2-diquark-both-eta @ bc1e5c743aada004c52dc7ab7ce2af61de439955

The review is limited to whether the specification is internally consistent, executable without requiring the Executor to invent missing authority, and sufficiently constrained to distinguish a genuine particle–particle ordering ambiguity from a tensor-construction, projector-basis, or implementation discrepancy.

It does not adjudicate the physics result itself and does not approve integration of the branch under adjudication.

Disposition

APPROVED FOR EXECUTION.

No mandatory specification change remains before execution.

The specification now correctly separates four materially different causes of the discrepancy and limits the permitted conclusion at each level. In particular, it no longer treats a difference in particle–particle slot maps as evidence of convention dependence unless both maps are independently shown to satisfy all frozen constraints and to differ only where the frozen material is silent.

What I verified

I verified that A7 now distinguishes the possible first divergences in the actual linear system being solved:

1. a difference in either canonical rank-4 tensor;
2. matching canonical tensors but different target vectors t, identifying an ordering or index-map divergence;
3. matching t but different design matrices M, identifying a basis or projector-convention divergence;
4. matching t and M but different coefficient vectors f, which is the only case in which an extraction or solver implementation defect may be asserted.

This hierarchy is materially important. Exact 256-component reconstruction by itself establishes only that each method reconstructs the tensor presented to its own extractor. It does not establish that the two methods solve the same M f = t problem.

I verified that the revised A7 does not automatically promote

both canonical tensors match but t_A != t_B

to particle–particle convention dependence. The stronger conclusion is permitted only if both L3 mappings are shown to satisfy every frozen constraint and to differ solely by an ordering convention the frozen material leaves open. If admissibility cannot be established, the required outcome is:

UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY.

That is the correct evidentiary threshold.

I verified that A8 now applies the same distinction to the branch’s independence claim. The specification permits exactly the strongest conclusion supported by the evidence: independence supported; independence contradicted with both mappings demonstrated admissible; or unresolved where the mappings differ but their admissibility is not established.

I verified that Method B is specified reproducibly rather than by reference to an external calculation. In particular, the charge-conjugation matrix is obtained from the null space of the complete homogeneous system

C γ_μ^T + γ_μ C = 0

over a general complex 4 x 4 matrix. This avoids the inadequate proxy of searching only a predefined 16-element basis.

I verified that Method A is required to be reproduced from its committed script without modification. Any defect found there must be reported rather than repaired in this task.

I verified that both methods must be run twice in the same environment and that determinism applies to the complete L1–L6 computational payload, not merely to the final family sums.

I verified that the specification requires scalar and pseudoscalar canonical tensors to be compared separately. A cancellation or difference in one must not be hidden by summing the two before comparison.

I verified that the scope is internally consistent: seven additions, zero modifications, with exactly one new test file and no modification to the branch under adjudication or to existing repository artifacts.

I verified that the report contract now requires A7 to be stated as exactly one of the four cases, while A6 still requires all downstream layers to be reported after the first divergence is identified.

What I could not verify in this review

I did not independently execute Method A or Method B and therefore did not verify either numerical coefficient pattern.

I did not verify the branch files’ measured SHA-256 values. The specification deliberately commit-pins those three branch artifacts and requires the Executor to compute and report their digests rather than treating an author-supplied digest as independent evidence.

I did not verify whether Method B’s source-to-diquark slot map is admissible under all frozen conventions. Determining that is one of the principal scientific and governance questions assigned to the execution task.

I did not determine whether either method contains an implementation defect. The specification correctly reserves that conclusion for the case where t_A == t_B and M_A == M_B but f_A != f_B.

I did not determine whether the branch’s claim of independence from the unfrozen particle–particle ordering survives adjudication.

Remaining non-blocking observations

The heading

The comparison, in order, stopping at the first divergence

is slightly misleading because the body correctly requires the Executor to identify the first divergence and then continue through all remaining layers. A clearer heading would say that the first divergence is identified rather than that execution stops there. The operative text is unambiguous, so this is not a blocker.

Likewise, A7’s four-case classification should be read as classification by the earliest divergence in the hierarchy. Downstream quantities may also differ and must still be reported under A6. The existing specification already requires that behaviour, so no additional authority is required.

Reviewer conclusion

The specification is sufficiently constrained to determine whether the S/P/T-versus-V/A discrepancy originates in the canonical tensor, the particle–particle ordering or slot map, the projector basis, or the coefficient extractor.

Most importantly, it does not allow a difference between two constructions to be silently promoted into a statement about an unfrozen physical convention. Demonstrating convention dependence requires demonstrating that both competing mappings are admissible under the frozen material.

Disposition: APPROVED FOR EXECUTION.
