# Pre-execution review — D-pre-A3 plaquette provenance

**Review status:** APPROVED FOR EXECUTION

reviewed specification SHA-256: `df46da1f7d52dd7fb8633d5c860f570a33fecac7b214c4c27d3a2295e06251bf`

Reviewed specification: `SPEC dpre a3 plaquette provenance(1).md`

## Determination

**APPROVED. No blocking scientific, evidentiary, or specification defect remains.**

This review is bound to the exact specification bytes identified by the SHA-256 digest above.

## Scientific review

The revised specification correctly limits the main question to the provenance of the uniform, site-sign-redefinition-invariant staggered plaquette value `P_mu_nu = -1`.

It no longer assumes that this invariant is already a physical difference between candidate kinetic formulations. The task must determine whether the staggered plaquette structure is representation-equivalent to the Clifford anticommutation structure under spin diagonalisation, is genuinely staggered-specific at the tested structural level, or cannot be established from the permitted derivation.

The three preregistered verdicts — `REPRESENTATION-EQUIVALENT`, `STAGGERED-SPECIFIC`, and `NOT ESTABLISHED` — provide an appropriate bounded outcome space. If the derivation produces a materially different logical case not covered by those definitions, the specification correctly requires a stop rather than an improvised verdict.

The specification also correctly prevents a `STAGGERED-SPECIFIC` result from being converted automatically into an admissibility, elimination, ranking, or operator-selection conclusion.

## Plaquette invariance

The revised A3 evidence hierarchy is approved.

The site-sign transformation is to be treated analytically for arbitrary `epsilon(x)`, with cancellation around the closed plaquette establishing redefinition invariance. A fixed-seed numerical transformation is only a reproducible sanity check and cannot substitute for the analytic proof.

This is stronger and more appropriate than relying on a single random redefinition.

## Representation-equivalence criterion

A numerical coincidence of `-1` on the two sides is not sufficient.

The load-bearing derivation must track the spin diagonalisation relation

`Gamma(x)^dagger gamma_mu Gamma(x+mu) = eta_mu(x) I`

through the closed plaquette and establish, if possible, how the Clifford loop sign is represented by the staggered link-phase holonomy.

Only such a structural mapping can support `REPRESENTATION-EQUIVALENT`.

## Consequence boundary

If the result is `REPRESENTATION-EQUIVALENT`, the permitted conclusion is that this plaquette-level cheap discriminator is closed.

Among the formulation-discriminating requirements already identified by the programme, reflection positivity remains outstanding and requires transfer-matrix work. The task does **not** establish that reflection positivity is the only possible remaining discriminator, nor that no other redefinition-invariant structure can distinguish the candidates.

The translation companion question is acceptable within scope because it probes the same redefinition structure, permits `NOT ESTABLISHED`, and does not control the principal verdict.

A successful plaquette mapping also does not independently corroborate the earlier species reconstruction where the two arguments share the same reconstruction machinery.

## Governance and execution boundary

The stated task architecture, frozen scope, commit layering, evidence-base preservation, checker runs, and validator requirements are approved.

The pre-issue record describing an earlier random numerical check is historical evidence and need not be rewritten to match the stronger execution criterion. Execution must follow the formal A3 requirement: arbitrary-site-sign analytic proof plus fixed-seed numerical sanity check.

The review/specification binding requirement is satisfied by the digest at the head of this artifact. Any byte-level change to the specification requires that binding to be reconsidered.

## Verdict

**APPROVED FOR EXECUTION.**

No further specification revision is required by this review.
