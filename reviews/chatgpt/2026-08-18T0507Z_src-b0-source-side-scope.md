# Review --- SRC-B0 Source-Side Scope Specification

**Reviewed artifact:** `SPEC src b0 source side scope(3).md`\
**Reviewed specification SHA-256:**
`a14625c4ca6aa4a629752a7f391b786fd5f236a884379f6b79b02a9675c2cce2`\
**Review date:** 2026-08-18\
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes
identified by the SHA-256 above and supersedes any review bound to an
earlier pre-rebase version.

I reviewed the rebased SRC-B0 specification against the landed DET-01
state at evidence base `0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`, with
particular attention to the source-side/geometry-side distinction, the
absence of the halo configuration from this repository, circularity
risk, the functional-measure issue, dimensional scope of the DET-01
rider, absolute versus dimensionless use of `G_ind`, failure
pre-registration, Rule 16 boundaries, and the no-computation/no-import
scope.

## 1. Evidence base and rebase --- PASS

The specification is now based on authoritative main at:

`0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`

This is the landed INTEGRATE-DET-01 head. The specification therefore
correctly treats DET-01 as repository evidence rather than as an
unintegrated branch result.

The pre-execution review must be committed with the SHA-256 above. An
earlier review SHA must not be reused after the rebase.

## 2. Primary scientific question --- PASS

SRC-B0 asks the correct next structural question: the programme has so
far developed the gravitational-response side, while the proposed
halo/attraction test requires a source-side object.

The specification correctly distinguishes:

-   an induced Einstein-Hilbert coefficient or `G_ind`;
-   a localized condensate configuration;
-   the stress tensor sourced by that configuration; and
-   the resulting gravitational solution or potential.

Establishing the first does not establish the latter three.

The statement about a homogeneous Lorentz-invariant vacuum is also
correctly narrowed. A cosmological-constant-type stress tensor can
gravitate, but it is not the localized clustering source required for a
halo/rotation-curve comparison.

## 3. Configuration availability and circularity --- PASS

The specification correctly makes repository availability the first
substantive question.

If no usable condensate configuration is present, the admissible verdict
is:

`NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`

The executor must not infer from filenames, memory, or an external
manuscript whether a missing profile was derived or fitted.

The circularity rule is also correct: if a profile were fitted to the
same rotation-curve data against which the reconstructed potential is
then judged, reproducing that data would not constitute an independent
test.

Importantly, `NOT PRESENT` is a repository-scope finding, not a
statement that the underlying physics is false.

## 4. DET-01 measure issue and T_mu_nu --- PASS WITH REQUIRED INTERPRETATION

The rebased specification correctly prevents DET-01's beta-function
rider from being extended automatically to the stress tensor.

DET-01 established that the specific measure ambiguity is ultralocal and
mass-independent and therefore does not move the present `m^2 log m^2` /
`beta_V` target. It did **not** establish that the functional derivative
of the same ambiguity vanishes.

For an ultralocal contribution

`Delta Gamma[g] = sum_x F(g(x))`,

the functional derivative with respect to the metric is generically
local but non-zero. SRC-B0 is therefore right to require this point to
be derived rather than inherited from DET-01.

One interpretation must remain explicit during execution: the statement
that `T_mu_nu` requires the unfixed functional measure is true when the
source observable is defined from the full quantum effective action
`Gamma`. It is **not** a universal statement that every possible
classical condensate stress tensor requires that measure. If repository
material later supplies a classical source action, its metric variation
would be a distinct construction. SRC-B0 must report which object the
repository actually supports rather than converting the `Gamma`
definition into a universal theorem.

This does not require another specification revision because A6 itself
asks whether the dependence exists and permits a negative or conditional
answer.

## 5. Background subtraction --- PASS

The new A6 separation is scientifically useful.

An explicitly defined background subtraction could in principle remove a
common vacuum-like ultralocal contribution, but that cannot be assumed
merely from ultralocality. The subtraction prescription, the two
backgrounds being compared, and the metric dependence must be defined.

The specification correctly requires a repository search for such a
prescription and treats its absence as a dependency rather than silently
inventing one.

## 6. Dimensional scope of the DET-01 rider --- PASS

The specification correctly requires the general relation

`det[sqrt(g) g^-1] = (det g)^(d/2 - 1)`.

Therefore the particularly simple equality with `det g` is
four-dimensional:

`d = 4  ->  det G1 = det g`.

At `d = 2` the determinant is unity. The specification correctly
prevents the four-dimensional RECON-01a identity from being presented as
dimension-independent.

This is an important improvement over a review that merely repeated the
four-dimensional result.

## 7. Absolute G_ind versus dimensionless comparison --- PASS

The specification correctly preserves the RECON-B0/DET-01 distinction:
the ratio-side result does not provide an absolute induced Newton
constant while the relevant normalization dependencies remain open.

A7 is therefore appropriately framed as an assessment question:
determine whether a repository-grounded shape, scaling, or ratio
comparison can avoid absolute `G_ind`.

The executor must not invent such a comparison merely because one is
conceivable in principle. If the missing profile/potential prevents a
concrete dimensionless observable from being identified from repository
material, the correct finding is that no repository-grounded comparison
has yet been established.

## 8. Paper 1 boundary --- PASS

The specification correctly treats Paper 1 and this repository as
separate evidence domains.

A profile, fitted potential, or `r_c` scaling relation existing only in
an external manuscript is not available to this task. SRC-B0 may
identify what must be imported or landed, but may not reconstruct the
missing material from memory.

This is essential for preserving provenance and for avoiding a hidden
circularity judgment about evidence the task has not actually inspected.

## 9. Failure criterion --- PASS

The specification correctly requires a future pre-registration to fix,
before seeing the result:

-   the quantity being compared;
-   the tolerance; and
-   the direction of the criterion.

It also correctly prohibits SRC-B0 from choosing those values.

The factor-of-three example is methodologically sound: without a
pre-fixed tolerance, the same discrepancy can be redescribed after the
fact as either agreement in scale or failure.

## 10. Component inventory --- PASS

A10 is properly an implementation/specification inventory rather than an
effort estimate.

The four states are mutually exclusive and the arithmetic identity
provides an auditable completeness check.

The condition that an implementation count only when potentially
applicable prevents unrelated code from artificially improving
readiness.

## 11. No-computation boundary --- PASS

The specification's statement that the task "computes nothing" is
consistent with A6 when read in its stated scientific sense: no physical
source, potential, profile, comparison, fitted quantity, or
order-of-magnitude result may be computed.

The permitted symbolic derivation of the structure of a functional
derivative and the determinant's dimensional dependence is scope
analysis, not execution of the proposed physical calculation.

The executor should preserve that distinction explicitly in the report.

## 12. Search methodology --- PASS

A4 and A5 correctly require whole-tree searches rather than relying on
the specification author's narrower `derivations/` observations.

Non-zero lexical hits must be classified rather than treated as evidence
by token count alone. This is particularly important given the repeated
self-referential and governance-text search hazards already encountered
in this programme.

The specification also correctly requires A11 to distinguish scientific
computations from governance measurements, SHAs, line numbers, file
counts, and quoted repository values.

## 13. Scope and evidence layering --- PASS

The four-commit structure is coherent:

1.  specification;
2.  review;
3.  scope artifact;
4.  report.

The committed report is measured at commit 3; commit-4 checks remain
post-report evidence and must not be written back as though the report
measured its own future commit.

The declared scope is four additions and zero modifications.
`DECISION_LOG.md` is correctly identified as checker configuration only,
not as write authorization.

## 14. Rule 16 boundaries --- PASS

All five required junctions are appropriate.

In particular, the specification correctly requires the executor to
distinguish:

-   repository absence from physical falsity;
-   this repository from external Paper 1 material;
-   induced gravitational elasticity from a sourced gravitational
    solution;
-   absence of a localized clustering source from absence of
    gravitational effect; and
-   component count from scientific difficulty or probability of
    success.

These prevent SRC-B0 from turning a scope assessment into either a
positive or negative physics result.

## 15. Remaining programme boundary --- PASS

SRC-B0 does not reopen `R1`--`R5`, RECON-01b, or the `r = 1` conflict,
and does not register a new gate.

That is the correct boundary. Its job is to determine whether the
proposed source-side test is presently poseable and to enumerate the
dependencies if it is not.

## Final verdict

**`APPROVE FOR EXECUTION`**

The rebased specification is materially sound and is correctly based on
the landed DET-01 head.

The principal execution caution is the A6 distinction: a stress tensor
derived from the full quantum effective action inherits the unfixed
functional-measure issue, whereas a classical condensate stress tensor
derived from a separately supplied classical action need not. The
executor must determine which object is actually supported by repository
evidence and must not universalize the `Gamma`-based definition.

That clarification is already compatible with A6's question-form
acceptance criterion and does not require another specification edit.

This approval applies **only** to the specification with SHA-256:

`a14625c4ca6aa4a629752a7f391b786fd5f236a884379f6b79b02a9675c2cce2`
