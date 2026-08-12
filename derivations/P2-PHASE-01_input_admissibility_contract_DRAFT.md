# `P2-PHASE-01` phase input / admissibility contract — DRAFT, NOT ADOPTED

**Cross-reference.** `OPEN-AC-2` is **RESOLVED FOR ENUMERATION**:
the negative-mass branch is included as a candidate, and is NOT
certified as admissible or stable, by the PI ruling recorded in
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`.
`OPEN-AC-5` is **CLOSED** — `Mhat = 1` is NOT an admissibility
bound — by the same answer that closes `OPEN-PD-1` in that artifact.
`OPEN-AC-1`, `OPEN-AC-3` and `OPEN-AC-4` **remain OPEN**.

**`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the difference is
the point.** `OPEN-AC-2` asks whether the branch is physical; the
ruling answers only where it may appear in an enumeration.

## Status and evidence boundary

This is a **DRAFT, NOT ADOPTED** prerequisite artifact.  It does not define an
admissibility rule or adopt a phase-input contract, and `P2-PHASE-01` remains
`PROPOSED`.  Its evidence is the integrated exploratory scalar study:
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md`,
`reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`, and
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`.

## Scalar evidence already available

For the declared `mu = 0`, uniform scalar ansatz, the integrated derivation
uses

```text
V'_red(Mhat) = Mhat [1/(2G) - I0(Mhat)].
```

It reconstructs the reduced potential with `V_red(0)=0` and takes curvature
from the complete first derivative, including the prefactor which retains the
trivial branch.  It does not differentiate the gap equation after division by
`Mhat`.  The reported curvature is restricted to this one scalar ansatz;
full multichannel-Hessian stability is **NOT ESTABLISHED**.  Sources:
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` and the integrated
report §Method and §§A2--A3.

Any later `P2-PHASE-01` work must honour the exclusions recorded in the
integrated report §§A8--A10: the quarantined `-3.2(5)`, the suspended
`P2-BETAV-CIRC-01` result, and the historical Finding 5 extraction.

## Decisions retained as OPEN

### OPEN-AC-1  P/V/A/T construction

**OPEN.** The Phase-A freeze defines candidate S/P/V/A/T families but does not
uniquely fix non-scalar mean-field functionals.  For P, the needed HS
normalisation, projection coefficient and sign, condensate ansatz, and common
potential-zero/measure normalisation are not frozen.  For V and A, those
inputs remain missing together with uniform direction/component structure and
internal generators.  For T, they remain missing together with tensor
plane/component structure and internal generators.  No Fierz projection, HS
normalisation, ansatz, direction, component structure, or comparison
normalisation is supplied here.  Sources: integrated report §A4 and
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` §§B--D.

### OPEN-AC-2  Interpretation of the negative-mass branch

**OPEN.** The integrated report's finest-offset table gives a negative-
`Mhat` left branch at `Mhat = -7.589264` with restricted curvature `0.417872`
at `G/Gc = 0.80`, and related negative roots throughout the reported scan.
Its reported residual ceiling is `1.85e-5`.  This is a traceable scalar
algebraic result, not a physical-phase classification.  Whether this branch is
physical, a doubler-related artifact, or included in the kill criterion's
quantifier is a PI/reviewer decision.

### OPEN-AC-3  Cross-family and within-scalar potential comparison

**OPEN.** Cross-family vacuum-depth comparison is not established: a common
HS normalisation, measure, and potential-zero normalisation across S/P/V/A/T
is not frozen.  Within the one reconstructed scalar potential, its algebraic
branches share that potential and its stated zero, so a mathematical
within-scalar comparison may be available.  What physical interpretation a
such comparison carries remains undecided; it is not an admissibility verdict.

### OPEN-AC-4  Exact/remnant symmetry and Goldstone implications

**OPEN.** The computation establishes only that simple `Mhat -> -Mhat`
reflection is not a symmetry of this Wilson scalar functional and reports the
Wilson-complement relation `I0(Mhat) = I0(-8-Mhat)`.  It does not establish
which exact or remnant symmetries the frozen microscopic action possesses,
whether the scalar condensate is an order parameter for one, or whether any
Goldstone conclusion follows.  This symmetry interpretation is a review
inference, not a computed result.  No programme-level implication is
established: in particular, this draft asserts neither absence of a Goldstone
mode nor anything about infrared symmetry restoration.

### OPEN-AC-5  Whether Mhat = 1 is an admissibility bound

**OPEN.** The integrated result observes `Mhat = 1` near `G/Gc ~= 1.77`; it
does not state whether that observation should bound admissibility or provide a
physical ground for doing so.

## Non-adoption statement

No stationary solution is called admissible, inadmissible, preferred, excluded,
or a physical phase by this draft.
