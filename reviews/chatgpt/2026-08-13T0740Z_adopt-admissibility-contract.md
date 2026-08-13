# Pre-execution review --- adopt the phase input / admissibility contract

reviewed specification SHA-256:
`e19e45b48f092f189aa13658fcf814acca0d0a300e9f24f7be333d4e66edfe62`

## Verdict

**APPROVED FOR EXECUTION.**

I find no blocking specification defect in the submitted specification.

## Review basis

The review was performed against the submitted specification as written,
with particular attention to the previously identified recursion in the
`GATES.md` summary, the meaning of `operational`, the separation between
rule adoption and scientific evaluation, branch provenance, the
`OPEN-AC` dependency statements, scope, pin handling, evidence layering,
and Rule 16.

## Required correction from the prior review

**RESOLVED.**

The prior blocking issue was that the proposed `GATES.md` summary
described C-ii as requiring "no competing admissible solution deeper",
which reintroduced the circular definition that §2 had repaired.

The submitted specification no longer does this. A6 now states:

> "thermodynamic selection against the comparison set of stationary
> solutions satisfying the non-thermodynamic conditions C-i and C-iii,
> under a common normalisation"

and immediately makes the non-recursion explicit:

> "The comparison set is defined WITHOUT reference to admissibility,
> deliberately."

This now corresponds to Standard C's independently defined comparison
set `S`. The gate summary therefore no longer defines admissibility in
terms of admissibility.

## Operational ruling

The PI ruling is internally coherent and sufficiently narrow for this
task. `Operational` means that the frozen rule can decide admissibility
**given the required inputs**; it does not mean those inputs presently
exist or that any candidate has already been evaluated.

The specification consistently preserves the distinction:

**rule frozen ≠ inputs complete ≠ candidate assessed.**

Accordingly, changing the prerequisite state to `SATISFIED` while
leaving `P2-PHASE-01` at `Status: PROPOSED` is not internally
contradictory under the stated ruling.

## Standard C

Standard C is now a decision rule rather than a recursive predicate.

C-i requires stationarity of the full effective action and full
condensate-space Hessian positivity transverse to symmetry-required flat
directions. C-iii supplies the symmetry/Goldstone information needed to
interpret that transverse condition. C-ii compares members of a set
defined independently from C-ii itself: stationary solutions satisfying
C-i and C-iii.

The treatment of ties is explicit and compatible with an existential
downstream question.

I find no remaining circular quantifier in the adopted definition.

## OPEN-AC classification and dependency

The distinction between **EVALUATION-INPUT GAPS** and **RULE-DEFINITION
gaps** is clear and is used consistently.

`OPEN-AC-1`, `OPEN-AC-3`, and `OPEN-AC-4` remain open. The specification
does not claim that freezing Standard C resolves, closes, downgrades, or
partially settles them.

The order `OPEN-AC-4 → OPEN-AC-3 → OPEN-AC-1` is now stated as a
dependency order rather than a schedule. The justification is
appropriately narrow: AC-4 is logically prior to applying C-i because
symmetry determines whether Hessian positivity is ordinary or transverse
to required flat directions. The specification expressly does **not**
claim that AC-4 determines the form of C-ii or the construction
represented by AC-1.

## Branch provenance and integration

Cutting from authoritative `main @ 1cb5550f…` is acceptable.

The specification knowingly trades a possible adjacent `GATES.md`
integration conflict for independent provenance of the two adoption
lines. It identifies the affected blocks as substantively disjoint and
requires the later integrator to preserve both and verify the resulting
pins.

That is a controlled integration risk, not a defect in this task.

## Scope and evidence layering

The declared scope is internally consistent with the task:

-   four additions;
-   two modifications;
-   no changes under `results/`, `scripts/`, or `tests/`;
-   no gate `Status:` change;
-   no modification of the MICROSCOPIC PARAMETER DOMAIN block.

The commit ordering correctly places the adopted artifact before the
`GATES.md` commit because the latter embeds the former's committed-blob
digest.

The report/post-report split is also explicit: commit-5 facts are
post-report evidence and must not be represented in the committed report
as measurements already made at commit 4.

## Gate and pin checks

The specification does not rely on checker P7 for gate integrity. It
explicitly identifies P7 as vacuous for the real gate headings and
instead assigns the substantive integrity work to the literal A6/A7/A9
measurements.

This is the correct evidentiary treatment.

## Rule 16

The Rule 16 limitation is adequate and prominently stated.

A `SATISFIED` prerequisite after this task establishes that an
admissibility rule has been frozen. It does **not** establish that
admissibility itself has been settled, that any candidate satisfies
Standard C, or that new scientific evidence toward the physical gate
verdict has been produced.

The specification also correctly identifies the second junction: a
`PASS` from P7 must not be interpreted as evidence that gate integrity
was checked.

## Stops and clarifications

`SPECIFICATION_DEFECT`: none identified.

`ENVIRONMENT`: not assessed by this review; execution-time environment
checks remain operative.

`OBSERVATION_METHOD_ERROR`: none identified in the specification review.

`REPOSITORY_DEFECT`: none identified by this specification review.

`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`: none blocking execution.
The meaning of `operational` is a PI ruling and is explicitly recorded
as such rather than presented as a derived scientific result.

## Approval

**APPROVED FOR EXECUTION as submitted.**

No textual correction is required before commit 1, provided the
committed specification is byte-identical to the reviewed file and Rule
18 records the SHA-256 above.
