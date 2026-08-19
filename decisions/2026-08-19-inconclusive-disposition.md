# PI decision — disposition of `INCONCLUSIVE` results

**Function:** a PI decision, in the two parts `decisions/README.md` requires.

---

## PART 1 — THE DECISION

### What was decided

**An `INCONCLUSIVE` finding is not terminal when the assessment identifies a
finite, explicit set of missing bridges whose establishment could change the
result to a positive finding.**

Two consequences follow, and both are requirements:

1. **Every `INCONCLUSIVE` result carries one of two subclasses**, assigned when
   the result is recorded:

        INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
            A candidate positive argument already exists, and what is missing
            is a finite, explicit, separately investigable set of bridges.

        INCONCLUSIVE — EVIDENCE INSUFFICIENT
            No clear next step is identified.

   **Assigning a subclass is required, not optional.**

2. **Every `INCONCLUSIVE` assessment answers a named `Resolution path` field** —
   the minimum additional derivation, measurement, construction, or evidence
   that would be sufficient to RESOLVE the finding. **The path is symmetric:**
   a `Resolution path` naming only the confirming outcome is incomplete.

**The executor defines the path. The executor does not walk it.**

### Who, and when

**Decided by:** the PI.
**Date:** 2026-08-19.
**Landed by:** `P2-GOV-HOUSEKEEP-02`.

### Effect and scope

**In effect from this landing forward.** Under the rule at
`decisions/README.md`'s "When a PI decision takes effect", it took effect when
issued; this record is where it is filed, not what gives it effect.

**Prospective.** Existing `INCONCLUSIVE` records are not retroactively
subclassified by this landing. **How many existing records carry a constructive
gap is unmeasured and is not estimated here.** The audit that would classify
them is a separate task.

**Scope is the disposition of a finding, not its verdict.**

### Provenance — the form adopted is not the form proposed

**The Researcher proposed the mechanism in a different form**, with subclasses
turning on whether the resolution path was known rather than on whether a
candidate positive argument already exists. **The PI's distinction supersedes
that proposal**, and the PI's form is what is recorded above and adopted as
`CONVENTIONS.md` rule 22.

### What this decision does NOT change

**The prohibition on promoting a result that fails a pre-registered test stands
unchanged.** A test returning `INCONCLUSIVE` because a required part was
unsatisfied must continue to return `INCONCLUSIVE`. **Nothing here licenses
relaxing a criterion after seeing the evidence.**

The verdict standard is untouched. What changes is what happens after a
correctly inconclusive result.

### The evidence that motivated it

**An unowned obligation, observed.** `P2-RECON-01B-B0`'s re-measurement was
executed and verified on `science/recon-01b-b0-scope`, and **was never
integrated**; the landed baseline is still the earlier assessment. No one
objected, because no one carried it. `PASS` and `FAIL` close themselves;
`INCONCLUSIVE` created an obligation with no owner and no closing condition.

**An epistemic state the vocabulary could not express.** `P2-RECON-PROJ-01`'s
`Q1` returned `INCONCLUSIVE` with a Ward identity and a trace identity already
in the manuscript, already yielding a conclusion of the shape the test asks
for, and a finite number of named missing bridges. **That is not the same state
as not knowing the answer**, and the repository had one word for both.

**Recorded honestly:** the two pieces of evidence are not the same failure. The
unintegrated re-measurement is a workflow carry-forward; `Q1` is the epistemic
case. Both motivated the decision; only the second is what the subclasses
distinguish.

---

## PART 2 — THE REVIEW

**`REVIEW PENDING`.**

No review of this decision has been supplied. Under the rule at
`decisions/README.md`, **the decision is in effect meanwhile**, and a review
when supplied may identify defects and recommend revision or supersession
without suspending it.

**The pre-execution review of `P2-GOV-HOUSEKEEP-02` is not this review.** That
artifact,
`reviews/chatgpt/2026-08-19T2324Z_gov-housekeep-02.md`, reviewed the
specification that landed this record. A review of the decision itself is a
different object and is owed.
