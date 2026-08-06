# Agent Rules

These rules apply to all future AI work in this repository.

## Mandatory preparation

Before making changes, read `PROGRESS.md`, `GATES.md`, `DECISION_LOG.md`,
`CLAIMS.md`, `HANDOFF.md`, and `CONVENTIONS.md`.

## Role separation

**Roles are functions. Assignments are current, and change by PI
instruction.**

- **PI** — decides. Model conception, research direction, and all
  authorizations. *Currently: Zeta Cheng.*
- **Researcher** — builds the theory with the PI and supplies the
  background knowledge it needs; writes proposals; turns the PI's
  intent into verifiable specifications; revises against reviewer
  comment; and interprets executor results for the PI. *Currently:
  Claude (chat).*
- **Reviewer** — reviews specifications and executor results, and
  raises questions. **Every execution specification or other normative
  task instruction that establishes or changes the Executor's
  authority, and every integration authorization, requires the
  Reviewer's agreement before being issued to the Executor** — except
  where the governing rules expressly provide a standardized
  authorization or permit a recorded correction without a new review
  cycle. **Incidental implementation exchanges within an
  already-reviewed authorization are not separate review points**, per
  rules 8 and 11.
  *Currently: ChatGPT.*
- **Executor** — performs the work and is the only party that writes
  to the repository. *Currently: Codex and Claude Code, selected per
  task (see below).*

**The Researcher and Reviewer functions are exchanged from time to
time, by PI instruction, with the intent of placing the stronger
available capability in the Reviewer function.** An assignment
recorded here is current, not permanent.

**Minor corrections** may proceed without a further review cycle only
to the extent already authorized by `CONVENTIONS.md` rule 10 and the
current reviewed specification. They must be confined to
executor-editable artifacts; must not alter reviewed meaning,
objectives, claims, invariants, or frozen or hash-pinned content; and
must satisfy rule 10's reporting and mechanical-equivalence
requirements where applicable. **An instruction from the PI or the
Researcher does not by itself expand the Executor's authorized scope.**
Every such correction is recorded in the task report. Any substantive
or otherwise unauthorized change requires re-review, or a separately
committed PI authorization.

### Reconciliation with `CONVENTIONS.md` rule 8

`CONVENTIONS.md` rule 8 already states that specification, execution and
review are functions rather than fixed agents. The role text previously
in this section named fixed agents instead, and the two conflicted.
**Where the older role text and rule 8 conflicted, rule 8's
function-based model governs**, and the function-based model above is
the operative statement of it. Rule 8 is not modified, renumbered, or
reworded by this record.

### Dual-executor arrangement

**As recorded by PI decision on 2026-08-06**, two executors are in use,
selected per task by the PI according to quota and capability. **They
are not interchangeable, and the difference is material rather than
administrative.** The capability statements below are PI-supplied
operational findings and current observations; they are **not
re-verified by this task and are not permanent capability
guarantees:**

- **Codex** — runs on the PI's workstation, which has a GPU
  (RTX 4070 Ti) and no short process-termination limit. **Decisive
  runs, long campaigns, and any work needing sustained compute belong
  here.**
- **Claude Code** — runs in a sandboxed container. Verified to reach
  genuine exit 0 on the validator suite, which the workstation
  currently cannot; but it is ephemeral, starts from a stale tree each
  session, and has been observed to lose a long-running job. **Short
  deterministic verification, preparation and audit belong here;
  decisive multi-hour runs do not.**

The PI announces which executor is in use. **A task specification whose
acceptance criteria can only be met on one of them should say so.**

### Records carry their function

Because those two functions are exchanged, records must state the
function under which they were produced. The requirement
and its prospective scope are recorded in `reviews/README.md`.

### Historical role assignment — superseded 2026-08-06

The following text is preserved verbatim as historical evidence and is
non-operative. It is superseded by the function-based model above and
by `CONVENTIONS.md` rule 8. See `DECISION_LOG.md`, entry dated
2026-08-06.

- ChatGPT handles conceptual discussion, physical interpretation, analytic
  derivation planning, gate design, calculation specifications, assumptions,
  and competing interpretations. It does not certify numerical results.
- Codex handles repository maintenance, implementation, tests, regression
  anchors, reproducibility, result files, branches, and commits. It must not
  promote a result into a paper claim without review.
- Claude is the independent reviewer/discriminator, issues gate verdicts,
  identifies overclaims, and updates the paper only after accepted results.
- The User / Principal Investigator owns the programme, approves assumptions,
  gates, and scope changes, accepts or rejects verdicts, and authorizes paper
  updates.

## Research rules

1. Never reopen a closed gate unless a concrete inconsistency is documented.
2. Never silently change conventions.
3. Commit a derivation note before production code.
4. Tests and regression anchors are mandatory.
5. Never edit raw outputs manually.
6. Processed results must identify the script and raw input used.
7. Do not update any `.tex` paper source before reviewer acceptance.
8. Preserve failed results and their provenance.
9. Distinguish the original model, a model extension, a phenomenological EFT,
   and a numerical proxy.
10. Every result must identify its regulator, cutoff, normalization, random
    seeds, and operating point.
11. A branch must correspond to one scientific gate or one paper-edit task.
12. Follow `CONVENTIONS.md` “Execution discipline for decisive runs and merges” for decisive-run and merge work.

This repository contains Paper 2 only. Do not merge content from another paper
repository.
