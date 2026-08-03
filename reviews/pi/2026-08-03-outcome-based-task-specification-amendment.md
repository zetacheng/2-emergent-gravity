# Amendment to `CONVENTIONS.md` — role separation and outcome-based task specification

Status: **REVIEWED AND APPROVED** for adoption (reviewer verdict:
approve with minor revisions, all applied). This document is the
**RATIONALE RECORD** for that adoption: it preserves the diagnosis, the
review history, the questions raised and how each was settled.

It is not itself the normative text and is not an executable
instruction. The normative text landed in `CONVENTIONS.md` is supplied
separately as `ADOPT_rules_8_12_normative.md`; where the two differ in
wording, **the text in `CONVENTIONS.md` governs**.

Rule numbering note: during review the responsibility-separation rule
was drafted as rule 12 and the others as 8–11. On adoption they were
reordered so that `CONVENTIONS.md` reads 1–12 in sequence:
**8** responsibility separation (root rule), **9** outcome-based task
specification, **10** self-correction authority and its limit,
**11** task granularity and integration boundary, **12** acceptance
criteria must be mechanically checkable. References to "rule 12" as the
root rule in the discussion below are to the draft numbering; the
adopted root rule is **rule 8**.

Target: `CONVENTIONS.md`, as a new section following "Execution
discipline for decisive runs and merges" (rules 1–7), which it extends
and does not replace. Landing also requires a `DECISION_LOG.md` entry
per this file's change control.

---

## Why this is proposed

The Arm H incident was caused by a prompt that imposed three
*procedural* conditions — change the gate status, keep governance tests
green, do not edit tests — that could not be jointly satisfied, because
the existing test asserted the superseded status. The executor resolved
the contradiction rather than reporting it. Rules 1 and 2 fixed the
second half of that failure.

The first half is unaddressed: **the contradiction existed because the
prompt specified a method instead of an outcome.** Had it stated the
required end state (gate reads RUN; the verdict is in its own field;
governance tests pass) with the test update named as a permitted
consequence, no contradiction would have arisen.

Recent sessions supply the supporting evidence. In one working session
the executor stopped eleven times. Roughly seven of those stops were
caused by defects in the prompt's *procedural* content — a stale hash
pin, a wrong target repository, an unspecified working directory, a
prohibition that made a required validator unrunnable, a byte-freeze
requirement that collided with the repository's own lint, a lint check
that did not use the repository's configured rule set, and a `grep`
pattern that did not match the file's actual headings. Every one of
those stops was correct executor behaviour under rules 1 and 2, and
every one was avoidable: none concerned the task's objective, its
acceptance conditions, or its prohibitions, which were correct
throughout.

Procedural over-specification therefore does not increase safety. It
transfers the author's implementation assumptions into the executor's
critical path, where they fail.

## Reframing after review

The reviewer's diagnosis goes deeper than this draft's original one.
The recurring cost is not procedural specification as such; it is a
**responsibility boundary that was drawn in the wrong place**. The
specification author had been designing theory, experiment, AND
implementation, leaving the executor authorized only to replay
commands — so any defect in a command, path, hash, lint invocation or
merge strategy could only produce a stop and a round trip. Outcome-based
specification is the consequence of fixing the boundary, not the fix
itself. Rule 12 is therefore the root rule of this section, and 8–11
follow from it.

## The amendment

### 12. Responsibility separation (root rule of this section)

> The **specification author** defines objectives, invariants and
> acceptance criteria.
>
> The **executor** determines the implementation necessary to satisfy
> them.
>
> The **reviewer** verifies the sufficiency and internal consistency of
> the specification before execution, and after execution independently
> assesses whether the resulting evidence actually supports the claimed
> outcome — including whether the acceptance criteria tested the
> intended object rather than merely passing implemented assertions.
> (Phase A's verifier rounds are the precedent: tests can pass while
> testing the wrong thing. A reviewer restricted to "did the criteria
> pass" would not catch that.)
>
> Two distinct review functions may be exercised by two independent
> reviewers: a **theory reviewer** (completeness, definitions, physics
> and mathematics) and an **evidence verifier** (repository results,
> computation, non-circularity of checkers, and whether claims exceed
> what was shown). These are functions, not fixed assignments to a
> particular agent.
>
> These are FUNCTIONS, not fixed agents: specification/theory,
> execution/experimentation, and independent review/verification. **PI
> authorization sits above all three** — adoption, exceptions, and final
> decisions are the PI's, and no rule in this section transfers that
> authority.
>
> **Revision 2 (scope of the non-interference rule):** no role
> prescribes another role's INCIDENTAL implementation process. A method
> MAY be prescribed where it is itself load-bearing to scientific
> validity, independence, reproducibility, provenance, or governance —
> for example: separation of blind compute from comparison; exact
> rational rather than floating-point arithmetic; independent
> reproduction; clean-clone validation; the prohibition on one program
> generating both expected and actual values; mutation tests; sample
> size, seed, and regulator prescriptions; merge parentage and the
> no-force-push rule. **Every prescribed method MUST carry a stated
> reason**, so that ordinary implementation cannot be re-labelled
> "load-bearing" to smuggle procedural control back in.
>
> Concretely: the specifier does not choose the executor's git strategy,
> working directory, or command sequence; the executor does not alter
> objectives, invariants, or scientific content; the reviewer does not
> design the implementation.
>
> **Review of specifications, not of executions.** Theory and
> acceptance criteria are reviewed BEFORE the task; the resulting state
> is reviewed AFTER it. Individual implementation steps are not
> submitted for review.

### 8. Outcome-based task specification

> A task specification MUST define **what must be true when the task is
> complete**. It SHOULD avoid prescribing implementation details unless
> those details are themselves governance objects — merge protocol
> (rule 5) and blind-campaign procedure are governance objects, and
> remain prescribed; git strategy, working directories, command
> sequences and tool invocations are not.
>
> A conforming specification has four MANDATORY NORMATIVE sections.
> Other material — context, governing sources, dependency state,
> authority and scope, definitions, outcome taxonomy, known limitations
> — may be present; only these four carry execution authority:
>
> **(a) Objective** — the required end state, stated as a condition of
> the repository, not as a sequence of actions.
>
> **(b) Acceptance criteria** — conditions, each independently
> checkable, whose conjunction is sufficient for the objective. Every
> criterion MUST have a machine-executable verification procedure and a
> defined expected outcome; the specification MAY identify the verifier
> interface and required outputs WITHOUT prescribing incidental command
> syntax, environment paths, or working-directory details. A procedure
> may be a checker script, a symbolic identity, a statistical decision
> rule, a generated manifest, or a structured comparison — it need not
> be a shell one-liner. A criterion requiring human judgement is not an
> acceptance criterion and belongs in (c) or in review.
>
> **(c) Invariants and prohibitions** — what may not change or be done
> under any circumstance. This part is authored by the specifier and is
> never inferred by the executor.
>
> **(d) Report contract** — what the executor must return: the raw
> output of every acceptance criterion, every self-correction with its
> before/after hashes and its reason, and any condition it could not
> satisfy.
>
> Within the bounds of (c), the executor MAY choose its own method,
> explore alternatives, retry, and correct its own working artifacts.
> **It MUST NOT infer, extend, or relax (c).**

### 9. Self-correction authority and its limit

> Self-correction is permitted ONLY for artifacts the specification
> explicitly classifies as **executor-editable**. Supplied-frozen,
> reviewer-approved, canonical-candidate, and content-authoritative
> artifacts remain immutable even when not yet registered, unless the
> objective explicitly authorizes substantive editing.
>
> For an executor-editable artifact, the executor MAY correct it without
> returning for authorization where all of the following hold: it is not
> registered and not hash-pinned by any registry entry; the correction
> is required to satisfy a stated acceptance criterion; the correction
> does not change reviewed scientific meaning, the objective, or any
> claim; the executor reports before/after hashes, the exact diff, and
> the reason; and result-equivalence is demonstrated by machine means.
> **If equivalence cannot be demonstrated mechanically, return for
> review.** Result-equivalence is required only where the correction is
> represented as non-semantic or output-preserving; substantively
> authorized development is judged against the acceptance criteria
> instead.
>
> An executor MUST NOT correct, reformat, or re-pin: any artifact
> hash-pinned by a registered gate; any gate status, verdict, or digest;
> any file outside the declared scope; or any repository configuration.
>
> **Tests:** tests may be created or updated within the current task
> ONLY where the specification expressly includes them in the authorized
> scope and acceptance criteria. Any test change not so authorized
> requires a separate specification and review. **An unexpected test
> failure never authorizes the executor to modify the test merely to
> obtain a green result.** (The Arm H lesson stated exactly:
> pre-authorized — permitted; not pre-authorized — stop; for a green
> suite — never.) These require a separate authorization with its own
> review.
>
> The executor MAY revise its own intermediate working artifacts as many
> times as required — generate, lint, fix, re-lint is ordinary
> engineering and does not warrant a round trip — provided the final
> state satisfies the acceptance criteria and the report records what
> changed.
>
> A re-pin under this rule does not create a precedent for registered
> artifacts.

### 10. Task granularity and integration boundary

> A task SHOULD combine implementation, local verification and branch
> preparation into ONE authorization. Implementation steps within it are
> not individually reviewed.
>
> **Integration is a separate authorization.** Merging into `main`
> requires a separate authorization, issued only AFTER clean-clone
> review of the resulting branch.
>
> **The default classification is MATERIAL.** A task may bypass separate
> result review and integration authorization only where its REVIEWED
> specification explicitly marks it `SINGLE-AUTHORIZATION-ELIGIBLE` and
> states why the change is low-risk. **The executor must not infer that
> classification, and may not upgrade a task into it.**
>
> Material work always includes: theory or concept specifications; gate
> registrations; decisive scientific runs; governance conventions;
> canonical or hash-pinned artifacts; and anything affecting a
> downstream gate. Non-exhaustive examples of what MAY be marked
> eligible: typo-only documentation corrections; a generated index
> refresh with no semantic change; formatting-only changes to unpinned
> files; removal of clearly identified scratch artifacts; mechanical
> metadata updates. Matching an example is not sufficient — the marking
> must be explicit in the reviewed specification.
>
> **Two review points and one integration boundary — and no others:**
> 1. *Specification review* — before execution: the objective,
>    invariants, acceptance criteria, and the theory behind them.
> 2. *Result review* — after execution, before integration: the
>    resulting branch, from a clean clone.
> 3. *Integration* — under rule 5's merge discipline, which does not
>    require a freshly hand-written procedural specification each time
>    (see rule 5's standardized authorization).
>
> Nothing between those boundaries is submitted for review. No
> additional approval boundary is required unless the specification
> itself preregisters a scientific, safety, cost, or governance
> checkpoint.

### 11. Acceptance criteria must be mechanically checkable

> Each acceptance criterion MUST have a machine-executable verification
> procedure with a defined expected outcome. The specification must
> identify the verifier interface, required inputs, and expected result,
> but need not prescribe incidental command syntax, environment paths,
> working directories, or tool invocation details.
>
> Where a criterion concerns the changed-file set, the declared manifest
> and the checker invocation are normative; the executor may choose how
> to prepare the inputs.
>
> The specifier MUST derive every literal in an acceptance criterion —
> hashes, file paths, grep patterns, rule sets, test names — from the
> repository as it actually is at specification time, not from
> recollection. Each specification MUST record a single line,
> `Specification evidence base: <full commit SHA>`; every
> repository-derived literal in it must be reproducible at that commit.
> Per-literal citation is not required.
>
> Recording the evidence base does NOT by itself freeze the execution
> base. Where base identity is load-bearing, it must ALSO appear
> explicitly as an invariant in part (c). Rule 7 (evidence precedence) applies to the authoring of
> specifications as much as to the reporting of results.

## Dependency this creates

Rule 11 makes the scope checker of the execution-discipline amendment
(**Amendment B**, currently recorded as "to be implemented separately")
load-bearing rather than optional: acceptance criteria over changed-file
sets need a manifest comparison that runs, not a prose instruction. That
work should precede or accompany adoption of this section.

## What this does not change

- Rules 1–7 stand unaltered. Contradiction-stop, scope precedence,
  normative frozen scope, prompt archival, minimum merge discipline,
  reporting honesty, and evidence precedence all continue to bind.
- No gate status, verdict, or scientific result is affected.
- Prospective only.
- The executor's obligation to stop on a contradiction is *strengthened*
  by this section, not weakened: with method no longer prescribed, a
  genuine contradiction can only arise in (a) or (c), where it is
  material and must be reported.

## Questions for the reviewer

1. (ANSWERED: not "exploratory" as such, but an explicit
   **executor-editable** classification is required; registered/pinned
   is only the minimum protection line and does not cover
   supplied-frozen or reviewer-approved material.)
2. (ANSWERED by review: post-task review alone would risk a long run
   proceeding on a misunderstood objective. Rule 10 now mandates TWO
   review points — specification before, resulting state after — with
   implementation steps unreviewed in between.)
3. (ANSWERED: yes — one `Specification evidence base: <SHA>` line per
   specification, not per-literal citation.)
4. (ANSWERED: it was too NARROW, not too loose. Broadened in rule 12 to
   methods load-bearing to scientific validity, independence,
   reproducibility, provenance, or governance — each with a stated
   reason.)
5. (ANSWERED: rule 5 stays procedural — merge discipline is a
   governance object. But a standardized merge authorization/tool should
   generate and verify its commands, so that a fresh hand-written
   procedural specification is not required for each merge. **This tool
   is a prerequisite of rule 10's third boundary and should be built
   before or alongside adoption.**)
6. (ANSWERED: yes, root rule; roles restated as functions with PI
   authorization above all three.)

7. (ANSWERED: default MATERIAL, with `SINGLE-AUTHORIZATION-ELIGIBLE`
   applied only by explicit marking in a reviewed specification. No
   exhaustive low-risk list is attempted, and the executor may not
   self-classify.)

Remaining question for the PI, not the reviewer: this section is
programme-wide in scope but is proposed for Paper 2's `CONVENTIONS.md`,
alongside rules 1–7. The recommendation is to land it there (immediately
usable, and it keeps rules 1–12 together), then ratify the approved
summary into `0-programme` as canonical with pointers from the other
paper repositories — the same two-step the ontology declaration still
owes. Copying the full text into five repositories is not proposed; it
would drift.
