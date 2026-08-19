# Decisions

**This directory holds PI decisions**, one file per decision.

## What this directory does NOT hold

**It does not hold reviews of specifications** — those are `reviews/`. It does
not hold physical assumptions or hypotheses — those are `assumptions/`. It does
not hold definitional conventions — those are `CONVENTIONS.md`.

## The four-way separation

    CONVENTIONS.md    definitions and conventions
    assumptions/      falsifiable or unestablished scientific propositions
    decisions/        PI rulings
    reviews/          reviews of specifications

## One file per decision, in two parts

    PART 1 — THE DECISION   what was decided, by whom, on what date, its
                            effect, and its scope
    PART 2 — THE REVIEW     the independent review of Part 1

**A decision whose Part 2 is not yet written is recorded with Part 2 marked
`REVIEW PENDING`, and the decision is in effect meanwhile.**

## When a PI decision takes effect

**PI RULING, adopted verbatim:**

> PI decisions take effect when issued. Their reviews are mandatory but
> non-gating. A review may identify defects and recommend revision or
> supersession, but does not suspend or delay the decision unless the PI
> explicitly so rules.

### Provenance — this replaced a PROVISIONAL disposition, it did not arrive settled

The question this rule answers was first landed as a **PROVISIONAL
execution-layer disposition** by `P2-REGISTRY-SPLIT-01`, explicitly reversible
and explicitly not a permanent repository rule. That task recorded that **the
Researcher did not have authority to fix it** and registered the adjudication
as owed rather than deciding it. The PI adjudicated it, and **the rule above is
that adjudication**.

**The superseded wording is reproduced here as historical text. It is
NON-OPERATIVE and must not be read as a rule:**

> **PROVISIONAL.** A review of a PI decision is recorded, not gating. The
> decision takes effect when the PI issues it. The review is an independent
> assessment landed in Part 2, and its function is to surface consequences,
> conflicts with landed records, and ambiguities — which may prompt the PI to
> revise or supersede the decision. **A review does not withhold effect from a
> PI decision**, because a gating review would place the Reviewer above the PI,
> inverting the authority model in `AGENTS.md`.

> **PENDING PI ADJUDICATION — when a PI decision takes effect, and whether its
> review is ever gating.** The Researcher does not have authority to fix this;
> the disposition above is a stopgap so the directory is usable, not an answer.
> Suggested ruling text for the PI to accept, amend or reject: *PI decisions
> take effect when issued; their reviews are mandatory but non-gating; a review
> may identify defects and recommend revision or supersession, but does not
> suspend the decision unless the PI so rules.*

**The adjudication recorded above as PENDING is no longer pending.** Both
quoted blocks are historical evidence of how the question was carried before it
was answered.

### The rule's first operation, recorded because it has already occurred

The Reviewer recommended against the retrospective reviews of ruling 4. Under
the rule above, **that recommendation does not suspend ruling 4, and ruling 4
proceeds.**

**This is recorded as the rule's first operation, not as a dispute.** A review
recommending against a decision is the review performing its function; the rule
settles only what such a recommendation does to the decision's effect, which is
nothing unless the PI so rules.

## Historical PI records

**Three PI records predate this directory and remain in place**, at
`reviews/pi/`. They are historical evidence, are not moved, not rewritten, and
not retrospectively reviewed — **the same treatment `reviews/README.md` already
gives records that predate its `Function:` header requirement.** PI decisions
are filed here going forward.

### One clause above is superseded by ruling 4 — recorded, not rewritten

**The clause "not retrospectively reviewed" is NO LONGER OPERATIVE.** The PI
ruled that each of the three records is to receive a retrospective review,
labelled `RETROSPECTIVE REVIEW — non-gating; does not alter the historical
effective date of the PI decision`, reviewing the exact historical bytes
actually in force. Under the rule at the head of this section that ruling took
effect when issued.

**The paragraph above is left verbatim rather than edited**, so that a reader
can see what the repository said before the ruling and what the ruling changed.
The rest of the paragraph stands: the three records are still not moved and
still not rewritten, and **a retrospective review is landed beside a record,
never into it.**

**The obligation is outstanding, not discharged.** No retrospective review has
been supplied. Where each is owed is registered in `docs/GOVERNANCE-DEBT.md`
with status `REVIEW PENDING`, naming each record by path and blob id.
