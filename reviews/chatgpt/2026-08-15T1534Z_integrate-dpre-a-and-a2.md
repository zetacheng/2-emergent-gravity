# Pre-execution review — integrate D-pre-A and D-pre-A2

**Review status:** APPROVED FOR EXECUTION AND LANDING

reviewed specification SHA-256: `5e0cf03d6aeed76c8c48ad5713451d731a515a2cf2cda3c0a9a56df7baeef795`

Reviewed specification: `SPEC integrate dpre a and a2(1).md`

## Determination

**APPROVED. No blocking scientific or specification defect remains.**

This review is bound to the exact specification bytes identified by the SHA-256 digest above.

## Review findings

The revised integration specification correctly treats the staggered plaquette structure as an unresolved provenance question rather than as an already-established physical difference between candidate kinetic formulations.

The established statement is limited to the following: the staggered formulation carries a uniform, site-sign-redefinition-invariant plaquette value `P_mu_nu = -1`. Whether that invariant is staggered-specific microscopic content or the spin-diagonalised representation of the Clifford anticommutation structure already present in the other formulations is **NOT ESTABLISHED**.

The integration task must therefore not use the plaquette invariant to favour, eliminate, rank, or otherwise weigh staggered. It brings the unresolved junction onto `main`; it does not bring an answer to that junction onto `main`.

The ancestry criterion has also been repaired. A1 now requires exactly two ancestry exit statuses and identifies both tests explicitly. No third ancestry measurement must be inferred by the executor.

## Integration architecture

The merge order is approved.

D-pre-A must enter the ancestry before D-pre-A2 because the discriminants artifact contains load-bearing references to the dossier. Integrating D-pre-A first and D-pre-A2 second converts those dependencies into ordinary ancestry rather than landing citations to an unintegrated branch.

The stated scope arithmetic is coherent with that structure. The specification correctly distinguishes one-sided merge cases from genuine two-sided auto-merges before interpreting blob equality.

The byte-prefix requirement for `P2-DEFERRED-ITEMS.md` is appropriate because it tests the repository's actual append-only semantics rather than substituting a weaker subsequence property.

The prospective `P3` and `P7` declarations are appropriately exercised by this integration task itself.

## Scientific boundary

The specification correctly does **not** select a canonical kinetic operator.

At the present evidence state, no candidate has been eliminated by an already-adopted ontology commitment. Under the weaker Reading B / Case B treatment, all four candidates remain viable. The integration must not claim that `C-iii` or `D0` is unlocked.

The staggered plaquette-provenance question remains a legitimate downstream scientific junction:

`P_mu_nu(staggered) = -1`

versus the possibility that this is representation-equivalent to the Clifford loop sign

`gamma_mu gamma_nu gamma_mu^-1 gamma_nu^-1 = -1`.

That equivalence or inequivalence is not decided by this integration task.

## Landing disposition

Execution and landing may proceed only if every stop-governing acceptance criterion in the reviewed specification passes, including the merge-order checks, source-integrity checks, protected-path comparisons, checker runs, validators, and fast-forward-only landing conditions.

**Final verdict: APPROVED FOR EXECUTION AND LANDING.**

Any byte-level modification of the reviewed specification requires the review binding to be reconsidered.
