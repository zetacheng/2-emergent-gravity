# `P2-PHASE-01` phase input / admissibility contract — ADOPTED

## Status

**ADOPTED.** Adopted by
`specs/2026-08-13T0740Z_adopt-admissibility-contract.md`, under the
pre-execution review committed alongside it. **This artifact is in force.**

**It freezes a rule and evaluates nothing.** No candidate has been assessed
against standard C by the task that adopted it.

## The labels this artifact uses, and their meanings

**Every kind label used below is defined here, and no others are used.**

    ADOPTED               this artifact is in force as the repository's
                          statement of the admissibility standard for
                          P2-PHASE-01
    FROZEN                fixed by this adoption; changed only by a later
                          task authorised to change it
    PI RULING             a decision recorded verbatim as issued by the PI.
                          It is a decision, not a derivation, and nothing
                          here presents it as a computed result
    STILL OPEN            not resolved, not closed, not downgraded and not
                          partly settled by this adoption
    EVALUATION-INPUT GAP  a missing input needed to APPLY the frozen rule,
                          as distinct from a gap in the rule's DEFINITION.
                          The rule is complete; the inputs are not
    SUPERSEDED            an earlier artifact retained as historical
                          evidence and not operative

**Four consecutive tasks on the parameter-domain artifact were spent repairing
labels that asserted a state their document was no longer in.** **This section
exists so that a later reader can check every label in this file against a
definition in this file.**

## The PI ruling

**PI RULING**, recorded verbatim as issued:

> **PI RULING.** `operational` is read in the first sense: a rule is
> operational once it can decide, for a given candidate, whether that
> candidate is admissible. It need not be applicable today. Accordingly,
> once standard C below is frozen, the PHASE INPUT / ADMISSIBILITY
> CONTRACT prerequisite is `SATISFIED`. **This does not mean any
> candidate has passed an admissibility assessment, and it does not mean
> the evaluation inputs are complete.**

## Standard C — the FROZEN rule

**FROZEN by this adoption.** Transcribed verbatim from §2 of the adopting
specification:

**A candidate stationary solution is ADMISSIBLE for `P2-PHASE-01` when
all three hold:**

    C-i    STATIONARITY AND LOCAL STABILITY
           it is a stationary point of the full effective action, and
           the full CONDENSATE-SPACE Hessian is positive definite on
           the space transverse to any flat directions required by an
           exact or remnant symmetry
           — NOT the restricted one-dimensional curvature, which is
             what every stored result to date carries

    C-ii   THERMODYNAMIC SELECTION
           define the COMPARISON SET S as every stationary solution
           satisfying C-i and C-iii — the non-thermodynamic conditions
           alone, with C-ii itself excluded from the test. A candidate
           satisfies C-ii when it is not shallower than any member of
           S, compared under a COMMON NORMALISATION across the channels
           in play — effective-potential or free-energy depth, not
           curvature.

           TIES ARE ADMITTED: "not shallower than" permits more than
           one member of S to satisfy C-ii, and SI-1's question is
           existential, so that is not a defect.

    C-iii  SYMMETRY ACCOUNTING
           the exact and remnant symmetries of the frozen microscopic
           action are determined, whether the condensate is an order
           parameter for any of them is stated, and any Goldstone
           directions are identified and excluded from C-i's positivity
           requirement

**C-ii's comparison set is defined without reference to admissibility,
and that is a repair rather than a stylistic choice.** An earlier
statement of `C-ii` compared a candidate against *competing ADMISSIBLE
stationary solutions*, while `ADMISSIBLE` was itself defined as
`C-i AND C-ii AND C-iii`. **That is a self-referential definition, not a
decision rule**: the set a candidate must beat would depend on the answer
being computed. **Defining `S` from `C-i` and `C-iii` alone removes the
recursion without changing the intended standard** — the deepest members
of `S` are admissible, and shallower members of `S` fail `C-ii`.

**The PI's ruling that a rule is operational once it can decide does not
repair this.** **A rule with a recursive quantifier cannot decide,
whatever its inputs.** The two issues are independent and both had to be
settled.

**C-i's transverse clause is not decoration.** If the condensate breaks
an exact symmetry, the Hessian carries zero eigenvalues along the
Goldstone directions and **cannot be positive definite**. A rule
demanding plain positive definiteness would then reject every
symmetry-breaking phase, **not because such a phase is unstable, but
because the criterion was written wrongly.** **`C-iii` therefore governs
how `C-i` is read**, which is why §4 orders the work as it does.

## The three remaining `OPEN-AC` items, reclassified

**Transcribed verbatim from §4 of the adopting specification.** **All three are
`STILL OPEN`.** **None is resolved, closed, downgraded or partly settled by this
adoption.**

**They are EVALUATION-INPUT GAPS, not RULE-DEFINITION gaps.** **This
distinction is the whole reason the prerequisite can be `SATISFIED`
without overstating scientific progress, and the adopted contract must
carry it in those words.**

**None of the three is resolved by this task. None is closed. None is
downgraded.**

    OPEN-AC-1  P/V/A/T mean-field construction.
               STILL OPEN. An input to C-ii whenever a channel beyond
               the scalar enters the comparison. Not required for a
               scalar-only evaluation, and the PI's route choice is
               scalar. It is the largest of the three and it has not
               been started.

    OPEN-AC-3  Cross-family and within-scalar potential comparison.
               STILL OPEN. THE input to C-ii. The cross-family part
               needs the common normalisation that does not exist. The
               within-scalar part the draft records as possibly already
               available, since the algebraic branches share one
               potential and one stated zero — but what physical
               meaning such a comparison carries is undecided, and the
               draft says so.

    OPEN-AC-4  Exact/remnant symmetry and Goldstone implications.
               STILL OPEN. THE input to C-iii, and through C-iii it
               governs how C-i is read. The existing material
               establishes only that Mhat -> -Mhat is not a symmetry of
               the Wilson scalar functional, and reports the complement
               relation. The draft states that the symmetry
               interpretation is a review inference, not a computed
               result.

**Work order: `OPEN-AC-4`, then `OPEN-AC-3`, then `OPEN-AC-1`.** **Stated
with its reason, and the reason is narrower than it may look:**

**`AC-4` is logically prior to APPLYING `C-i`, and therefore prior to any
complete standard-C assessment**, because it determines whether `C-i`'s
positivity is read plainly or transverse to flat directions.

**It is NOT claimed that `AC-4` fixes the form of the criteria `AC-3` or
`AC-1` feed.** `C-ii`'s comparison is a depth comparison under a common
normalisation whatever the symmetry analysis returns, and `AC-1` is a
construction input. **An earlier draft asserted the wider dependency; it
was stronger than the actual graph.**

## What adoption does NOT establish

**A standalone section, because a reader must meet it without searching.**

- **It does not establish that admissibility has been settled.** **A rule now
  exists and nothing has been measured against it.**
- **It does not establish that any candidate is admissible.** The negative-mass
  branch, the ordinary branch and the trivial vacuum are exactly where they
  were. **None has been assessed against standard C.**
- **It does not supply the evaluation inputs.** Three are `STILL OPEN` and are
  recorded above as `EVALUATION-INPUT GAP`s. **One of them, `OPEN-AC-1`, has not
  been started at all.**
- **It does not make `P2-PHASE-01` runnable.** The gate's own *Required
  computations* and *Required deliverables* sections both read `(not started)`,
  and this adoption does not start them.
- **It produces no scientific evidence toward the gate's physical verdict.** **A
  procedural step was completed and nothing was measured.** **A prerequisite
  transition is a step; it is not a scientific one.**
- **Standard C was chosen knowing it is not evaluable now**, and will not be for
  some time. **The PI selected it over two weaker standards that would have let
  the gate pass on a reason weaker than the question it asks.**
- **Nothing here bears on the microscopic parameter domain prerequisite**, whose
  adoption sits on a separate branch that this adoption neither carries nor
  references.

## The superseded draft

**SUPERSEDED:** `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.

**It is retained as historical evidence and is not operative.** **Its `OPEN-AC`
entries are unchanged and remain open**; this artifact reclassifies three of
them as `EVALUATION-INPUT GAP`s without resolving any of them, and does not
touch `OPEN-AC-2` or `OPEN-AC-5`, which are the subject of a separate line.
