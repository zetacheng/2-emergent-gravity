Pre-execution review — chirality census

Reviewer: ChatGPT
Disposition: APPROVED

Review scope

I reviewed the task specification titled “the chirality census: why S, P and T vanish in both channels” against its stated objective, evidence boundaries, execution ordering, acceptance criteria, and the distinctions required between particle–hole and particle–particle chirality structure.

This review addresses whether the specification is internally executable and whether the proposed computation can test the claimed structural explanation without silently supplying an unfrozen particle–particle convention.

It does not independently execute the repository calculations, verify the pinned SHA-256 values against repository objects, or establish that the chirality-census hypothesis is physically or algebraically correct. Those are execution-time obligations under A1 and A3–A9.

What I verified

The principal structural defect in the earlier draft has been corrected.

The particle–hole and particle–particle chirality classifications are no longer treated as the same rule. The specification now requires them to be established independently:

* for particle–hole bilinears, through the complete set of P_X\Gamma P_Y;
* for particle–particle bilinears, through the complete set of P_X^T C^{-1}\Gamma P_Y.

The proposed inversion between the two classifications is tied explicitly to

C\gamma_5^T C^{-1}=+\gamma_5,

rather than being carried over by analogy from the particle–hole channel.

The specification also now requires the complete 2\times2 chirality tables for both pairings. No projector entry may be omitted as redundant. This is an appropriate mechanical protection against the projector-placement error that motivated the revision.

I verified that the particle–particle part of the task remains structural. C2 asks only which chiral pairs the kernels can support. It explicitly forbids a particle–particle coefficient decomposition and forbids choosing a slot map. Therefore the task does not need to invent the unfrozen particle–particle Grassmann ordering or diquark normalisation in order to answer C2.

The evidence strength of the two channels is now stated correctly and asymmetrically:

* particle–hole: structural selection plus a numerical predict-then-compute falsification;
* particle–particle: structural selection only.

The no-i decomposition in Step D is expressly a particle–hole falsification test. The specification no longer implies that the particle–particle claim has received the same numerical test when doing so would require an unfrozen pp ordering.

The no-i test is also methodologically stronger than the earlier LL/RR restriction proposal. The prediction must be written down from the census before the decomposition is computed, and the task requires a second independently chosen interaction under the same predict-then-compute discipline. This makes the proposed criterion genuinely falsifiable rather than an explanation fitted after seeing the answer.

The provenance boundary is clear. The authoritative particle–hole result is pinned from main. The particle–particle coefficient branches are explicitly identified as unintegrated context, not authoritative inputs, and the executor is forbidden from reading either of them. Step C therefore has to establish its particle–particle structural statement independently.

The specification also distinguishes correctly between what a successful census would explain and what it would leave unexplained. In particular, it does not claim to derive the relative V/A sign, a channel character, a bound state, a Hubbard–Stratonovich choice, or a settled diquark channel.

The execution lifecycle is internally consistent: review precedes work, derivation precedes production code, the seven-path scope is consistent with the manifest, and the new test obligation is limited to one new test file.

What I could not verify in this review

I did not verify that the three A1 digests match the repository objects at evidence base 8701a97a6bb58550d4300f75c10638b057335731.

I did not independently verify that the frozen derivation actually contains the quoted i\gamma_5, axial, and tensor conventions. A3 correctly makes that an execution-time check and requires a STOP if the repository does not say what the specification attributes to it.

I did not execute the rank-four factorisation identities in Step A, the complete projector tables in C1/C2, the representation-independence comparison, or either Step D prediction. Accordingly, this approval does not endorse the pre-issue numerical confirmations in §12 as results.

I also do not verify in advance that the proposed census criterion is sufficient. The specification correctly permits Step A, C, or D to falsify it and explicitly forbids repairing the explanation after such a failure.

Reviewer assessment

The revised specification now separates three propositions that must not be conflated:

1. the frozen interaction has a particular chirality census;
2. that census structurally constrains which bilinear families are available in each pairing;
3. a numerical decomposition confirms a prediction of that criterion.

For the particle–hole channel, the task tests all three.

For the particle–particle channel, it tests the first two only, because the third would require conventions the repository has deliberately left unfrozen.

That limitation is explicit and appropriate.

If the proposed argument survives A4–A9, the strongest licensed conclusion is structural: the vanishing of S, P and T is explained by chirality support rather than merely observed as a numerical cancellation, with different PH and PP selection rules producing the same V/A support.

It would still not establish that the diquark channel is fully defined, that its absolute channel character is settled, or that any composite state exists.

No unresolved specification contradiction requiring a pre-execution STOP was identified.

Disposition: APPROVED for execution as written.
