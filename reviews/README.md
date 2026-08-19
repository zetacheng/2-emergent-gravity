# Reviews

Store independent review records here, organised by author directory
(`chatgpt/`, `claude/`, `codex/`, `pi/`). Roles are functions with current
assignments rather than fixed agents; the operative model is in `AGENTS.md`
and in `CONVENTIONS.md` rule 8.

## What this directory holds, and what moved out

**`reviews/` holds reviews of specifications.** The by-author layout above and
the `Function:` header rule below are unchanged for what remains here.

**Two kinds of record now live elsewhere:**

    assumption reviews    in assumptions/, as PART 2 of the entry they review
    PI decisions          in decisions/, as PART 1 with their review as PART 2

**An assumption review is not a review of a specification**, and a PI decision
is not a review at all. Filing each with the object it belongs to means a
reader finds the entry and its review together, and can tell what kind of
epistemic object a file is by where it sits:

    CONVENTIONS.md    definitions and conventions
    assumptions/      falsifiable or unestablished scientific propositions
    decisions/        PI rulings
    reviews/          reviews of specifications

**Nothing already here is moved.** `reviews/pi/`'s three records — a PI
authorization record, an amendment rationale record, and a PI amendment record
— **remain valid historical evidence in place**, are not rewritten, and are not
retrospectively reviewed. **PI decisions are filed under `decisions/` going
forward.** This is the same treatment this README already gives records that
predate the `Function:` header requirement.

**The assumption review landed at `reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md`
also remains in place**, as the landed original that
`assumptions/H-EXT-01.md`'s Part 2 reproduces and pins.

## Records carry their function

Because the Researcher and Reviewer functions are exchanged by PI
instruction, the author directory alone does not say in which function a
record was produced. Every review, Researcher record, Executor record, or
PI authorization **created or substantively amended after** the 2026-08-06
role-model decision must state in its header the function under which it
was produced, as a header field:

    Function: Researcher | Reviewer | Executor | PI authorization

**Existing records remain valid historical evidence** and are not
retrospectively non-conforming merely for lacking this header. Without the
header a later reader cannot tell whether a record in `claude/` was a
review or a Researcher artifact, and the by-author layout alone will not
say — but that is a reason to require it going forward, not a reason to
rewrite the past.

## Historical role assignment — superseded 2026-08-06

The following text is preserved verbatim as historical evidence and is
non-operative. It is superseded by the function-based model in `AGENTS.md`
and by `CONVENTIONS.md` rule 8. See `DECISION_LOG.md`, entry dated
2026-08-06.

> Store independent review records here. ChatGPT material may document planning
> and interpretation but does not certify numerical results. Claude reviews
> derivations and results, identifies overclaims, and records a gate verdict.
> Final acceptance or rejection belongs to the Principal Investigator.
