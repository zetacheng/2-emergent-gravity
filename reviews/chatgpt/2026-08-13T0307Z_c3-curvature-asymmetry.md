# Pre-execution review — C3 curvature asymmetry

**Task:** `C3: is the curvature asymmetry physical or coordinate-induced?`

**Disposition: APPROVED FOR EXECUTION.**

**reviewed specification SHA-256:** `0d0898be55c14af3bb9c6e77c119869160bc744c4b214ff089e8965d954b7734`

## 1. Review conclusion

The blocking contradiction identified in the previous review is corrected.

`OPEN-CC-1` now states that only the first provenance question is settled: the production complement root is separately recovered rather than constructed. It explicitly leaves the bit-exact mirroring mechanism unresolved and points to `OPEN-CC-3`. This is consistent with §0 and with `OPEN-CC-3`.

I find no remaining substantive internal contradiction that should prevent execution under the stated scope.

## 2. Previously identified issues

### `OPEN-CC-1` — RESOLVED

The earlier wording asserted both that exactness was a search-structure artefact and that its mechanism was unresolved. The revised entry now distinguishes them correctly:

- root provenance: settled as separately recovered;
- bit-exact mirroring mechanism: unresolved.

The entry also records that the earlier contradictory wording was corrected. This closes the previous blocking defect.

### `OPEN-CC-2` — RESOLVED

The specification does not claim that the `2.0e-4` de-duplication threshold proves a root-completeness defect. It records the observed suppression of the near-zero searched representative and leaves open whether a distinct stationary root is lost at criticality.

### `OPEN-CC-3` — RESOLVED AS AN OPEN ITEM

The specification correctly treats the mechanism of bit-exact mirroring as unresolved. It records both deficiencies in the earlier explanation: the reflected-bisection argument has a counterexample, and membership of a common dyadic lattice does not force complementary lattice indices.

This status is now consistent throughout the specification.

### C3 consequence — RESOLVED

The `COORDINATE-INDUCED` consequence no longer depends on a settled explanation of bit-exactness. It relies only on the Wilson-complement positional identity and the algebraically determined curvature ratio.

The wording “no independent content of any kind that has been demonstrated” appropriately limits the evidential claim.

## 3. Mathematical scope

The proposed derivation is coherent with the stated implementation:

`V'(m) = m(1/(2G)-I0(m))`

and

`V''(m) = 1/(2G)-I0(m)-m I0'(m)`.

At a non-trivial stationary root, the gap condition removes the first two terms, giving

`V''(m*) = -m* I0'(m*)`.

Given the Wilson-complement identity and its differentiated relation, the predicted ratio `V''(m2)/V''(m1) = -m2/m1` follows algebraically.

The specification also correctly avoids turning this into a stronger covariance claim. Under its own terminology, `COORDINATE-INDUCED` means definition-induced/algebraically determined for this restricted curvature; it does not establish that the effect is purely a coordinate-transformation Jacobian artefact.

## 4. Ordinary explanations and Rule 16

The task can test whether the observed asymmetry is already fixed by the restricted-curvature definition and the complement relation. It does not establish covariance of that curvature under a general field reparameterisation or exclude additional measure/Jacobian contributions in a fuller formulation.

Likewise, a `COORDINATE-INDUCED` verdict would remove demonstrated independent evidential content from the currently measured position and restricted curvature of the complement branch. It would not establish that the branch is unphysical or absent.

The specification correctly preserves the narrower limitation that the calculation concerns a one-dimensional restricted curvature in the uniform scalar ansatz at `mu = 0`; the full condensate-space Hessian remains outside C3.

## 5. Governance and execution structure

The five-addition, zero-modification manifest is internally consistent with the stated commit layering. The two derivation artifacts are correctly required to move together in commit 3.

The distinction between committed evidence measured at commit 3 and post-report evidence measured at commit 4 is explicit.

The checker configuration is fixed rather than executor-selected, and the specification correctly states that `P7` is not evidence of gate integrity; A9 supplies the relevant blob-identity check.

No amendment of existing artifacts, gate state, PI ruling, deferred-items register, script, or results is authorised.

## 6. Clarification retained for execution

The ninety-pair numerical comparison is a check using stored evidence, not a new model evaluation. The executor should preserve the specification's caution concerning the observed finite deviations: without decomposing root-resolution, stationarity-residual, and quadrature contributions, the near-critical pattern may be described as consistent with resolution amplification but not attributed exclusively to it.

The executor must also make the required anchoring disclosure. Because the closed-form prediction is present in the specification before execution, an executor who reads §2 before deriving it should not describe the derivation as blind or independent.

## 7. Disposition

**APPROVED FOR EXECUTION.**

The previous blocking defect has been corrected, and I find no remaining substantive specification defect in the supplied revision that requires amendment before execution.

This review is tied to the exact uploaded specification bytes by the SHA-256 recorded above. Any subsequent change to the specification requires a new review or an explicitly governed treatment under the repository's applicable rules.
