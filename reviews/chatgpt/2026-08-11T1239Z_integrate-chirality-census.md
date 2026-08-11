Pre-execution review — integrate the chirality census

Reviewer: ChatGPT
Disposition: APPROVED FOR EXECUTION

Review scope

I reviewed the task specification “integrate the chirality census” against its stated evidence base 8701a97a6bb58550d4300f75c10638b057335731, the pinned source branch gate/p2-chirality-census @ e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb, and the execution/governance constraints stated in the specification.

This review covers specification consistency, authority boundaries, merge sequencing, scope accounting, evidence layering, protection of the unintegrated diquark work, and whether the conclusions attributed to the chirality census exceed what the reviewed source task established.

It is a pre-execution review only. I have not executed the merge, re-run the validators, inspected the live remote refs, or independently reproduced the Git object IDs listed in A6.

What I verified from the specification

The commit lifecycle is internally consistent with Rule 15: specification, pre-execution review, merge, then report. A2 correctly identifies the review commit as merge parent 1 and separately requires the specification commit to be its ancestor.

The scope arithmetic is consistent. Seven files arrive from the source branch and three integration artifacts are authored by this task, giving 10 additions and 0 modifications. The manifest in A4 lists exactly those ten paths.

The specification preserves the two material corrections produced by the source task rather than silently retaining the earlier account.

First, it distinguishes the operator identity

S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)

from the ordered rank-4 tensor identity

2[P_R⊗P_L + P_L⊗P_R].

That distinction is material and is correctly required to remain in the integrated record.

Second, it corrects the explanation of the particle–hole / particle–particle chirality “inversion”. The projector non-zero patterns are not themselves inverted. The differing field-label interpretation comes from the particle–hole bar flip ψ̄_L = ψ̄ P_R, together with its absence on the particle–particle side; C γ₅^T C⁻¹ = +γ₅ is load-bearing because it prevents the corresponding extra flip in the pp construction.

The specification also correctly separates what is settled from what is not. The integration establishes a chirality-based support selection rule for the frozen interaction. It does not claim to determine the relative V/A sign, coefficient magnitudes, or absolute attractive/repulsive character.

The evidence asymmetry between the two pairings is stated correctly and repeatedly: particle–hole has structural classification plus numerical falsification, whereas particle–particle has structural classification only. No pp coefficient decomposition or slot-map choice is authorised here.

A9 and the prohibitions in §7 correctly preserve both unintegrated diquark branches and prohibit their coefficients from being promoted into main-line results through this integration.

The unresolved sign difference in the independently checked P² diagnostic is also handled appropriately. Both computations agree on the proposition relevant to this task — all five families are non-zero — while the coefficient-sign disagreement is explicitly preserved as unresolved rather than being silently harmonised.

The Rule 16 assessment is appropriate. Combining a main-line chirality selection rule, a particle–hole coefficient table and a structural particle–particle classification could naturally be over-read as a settled diquark channel. The specification explicitly prevents that inference.

What I did not verify

I did not independently verify that remote main currently resolves to 8701a97a6b…, that the source branch resolves to e4bea1c9…, or that the merge remains conflict-free. Those are execution-time checks under A1–A3.

I did not independently read the seven Git blobs listed in A6, reproduce their object IDs, or re-run the numerical tensor identity stated in §9. The executor must perform the specified object and validator checks.

I did not independently determine whether every pre-existing path protected by A7 remains blob-identical after the merge. That must be established path by path from Git objects as required.

I also did not adjudicate the unresolved P-coefficient sign difference mentioned in §3. This specification correctly places that outside its authority.

Reviewer finding

One wording point should be kept under discipline during execution, but it is not blocking.

Section 0 describes the historical pattern as two separate numerical facts, including the particle–particle V/A-only result. The specification itself later makes clear that the pp coefficient branches are unintegrated and are not authoritative main-line inputs. Therefore the integration report must preserve that distinction: the chirality census may explain why the structural pp support is V/A-only, but it must not present the unintegrated pp coefficient values or their channel character as results now established on main.

A9, §3 and §7 already impose that restriction, so no specification amendment is required.

Disposition

APPROVED FOR EXECUTION.

I find no blocking specification contradiction, unresolved authority conflict, scope inconsistency, or required inference that the executor would need to invent.

Execution should proceed only if the pinned refs, no-conflict premise, incoming blob identities, protected-path comparison, validators and final scope check reproduce exactly as specified. Any failure of those checks should be handled under the specification’s stated STOP rules rather than reconciled during integration.
