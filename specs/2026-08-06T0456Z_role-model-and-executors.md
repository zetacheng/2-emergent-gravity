# Task specification — adopt the function-based role model and record the dual-executor arrangement

Specification evidence base: `a0e9d11b7281f0c2185aa8d517bae009ab54807f`
Required verification target: the same commit.

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This task records decisions the PI has already made. It decides
nothing.** No scientific content changes, no gate is touched, and no
rule 1–15 is created or renumbered.

**Why it must run before the Rule 15 task.** An independent review found
a live conflict inside the repository: `AGENTS.md` and
`reviews/README.md` assign fixed roles that contradict the arrangement
actually in use, while `CONVENTIONS.md` rule 8 states that the review
functions are "functions, not fixed assignments to a particular agent"
— and **no committed artifact says rule 8 supersedes the older text.**
Any further governance work would be built on that contradiction.

---

## 0. The conflict, quoted from the target revision

    AGENTS.md:12  ChatGPT handles conceptual discussion, physical
                  interpretation, analytic derivation planning, gate design,
                  calculation specifications ... It does not certify
                  numerical results.
    AGENTS.md:15  Codex handles repository maintenance, implementation,
                  tests, regression anchors, reproducibility, result files,
                  branches, and commits.
    AGENTS.md:18  Claude is the independent reviewer/discriminator, issues
                  gate verdicts, identifies overclaims ...

    reviews/README.md  ChatGPT material may document planning and
                       interpretation but does not certify numerical
                       results. Claude reviews derivations and results ...

Verify these quotations against the target revision before relying on
them. If they differ, that is a finding: stop and report.

## 1. Objective

`AGENTS.md` and `reviews/README.md` describe roles as **functions with
current assignments**, rather than as fixed agents; the dual-executor
arrangement and its capability difference are recorded;
`DECISION_LOG.md` records the adoption. `main` is unchanged.

### The role model to record

> **Roles are functions. Assignments are current, and change by PI
> instruction.**
>
> - **PI** — decides. Model conception, research direction, and all
>   authorizations. *Currently: Zeta Cheng.*
> - **Researcher** — builds the theory with the PI and supplies the
>   background knowledge it needs; writes proposals; turns the PI's
>   intent into verifiable specifications; revises against reviewer
>   comment; and interprets executor results for the PI. *Currently:
>   Claude (chat).*
> - **Reviewer** — reviews specifications and executor results, and
>   raises questions. **Every execution specification or other normative
>   task instruction that establishes or changes the Executor's
>   authority, and every integration authorization, requires the
>   Reviewer's agreement before being issued to the Executor** — except
>   where the governing rules expressly provide a standardized
>   authorization or permit a recorded correction without a new review
>   cycle. **Incidental implementation exchanges within an
>   already-reviewed authorization are not separate review points**, per
>   rules 8 and 11.
>   *Currently: ChatGPT.*
> - **Executor** — performs the work and is the only party that writes
>   to the repository. *Currently: Codex and Claude Code, selected per
>   task (see below).*
>
> **The Researcher and Reviewer functions are exchanged from time to
> time, by PI instruction, with the intent of placing the stronger
> available capability in the Reviewer function.** An assignment
> recorded here is current, not permanent.
>
> **Minor corrections** may proceed without a further review cycle only
> to the extent already authorized by `CONVENTIONS.md` rule 10 and the
> current reviewed specification. They must be confined to
> executor-editable artifacts; must not alter reviewed meaning,
> objectives, claims, invariants, or frozen or hash-pinned content; and
> must satisfy rule 10's reporting and mechanical-equivalence
> requirements where applicable. **An instruction from the PI or the
> Researcher does not by itself expand the Executor's authorized
> scope.** Every such correction is recorded in the task report. Any
> substantive or otherwise unauthorized change requires re-review, or a
> separately committed PI authorization.

### The dual-executor arrangement

> **As recorded by PI decision on 2026-08-06**, two executors are in
> use, selected per task by the PI according to quota and capability.
> **They are not interchangeable, and the difference is material rather
> than administrative.** The capability statements below are
> PI-supplied operational findings and current observations; they are
> **not re-verified by this task and are not permanent capability
> guarantees:**
>
> - **Codex** — runs on the PI's workstation, which has a GPU
>   (RTX 4070 Ti) and no short process-termination limit. **Decisive
>   runs, long campaigns, and any work needing sustained compute belong
>   here.**
> - **Claude Code** — runs in a sandboxed container. Verified to reach
>   genuine exit 0 on the validator suite, which the workstation
>   currently cannot; but it is ephemeral, starts from a stale tree each
>   session, and has been observed to lose a long-running job. **Short
>   deterministic verification, preparation and audit belong here;
>   decisive multi-hour runs do not.**
>
> The PI announces which executor is in use. **A task specification
> whose acceptance criteria can only be met on one of them should say
> so.**

### Records carry their function

> `reviews/` is organised by AUTHOR. Because the Researcher and Reviewer
> functions are exchanged, **every review, Researcher record, Executor
> record, or PI authorization CREATED OR SUBSTANTIVELY AMENDED AFTER
> adoption of this decision MUST state in its header the function under
> which it was produced** — Researcher, Reviewer, Executor, or PI
> authorization.
>
> **Existing records remain valid historical evidence and are NOT
> retrospectively non-conforming merely for lacking this header.**
> Without the header a later reader cannot tell whether a record in
> `reviews/claude/` was a review or a Researcher artifact, and the
> by-author layout alone will not say — but that is a reason to require
> it going forward, not a reason to rewrite the past.

## 2. Acceptance criteria

**Each criterion names a verifier and an expected outcome.** Incidental
command syntax is yours; the checks are not.

**A0 — The approved specification is committed by you, as commit 1.**

**PI decision, 2026-08-06:** Researcher–Reviewer review exchanges are
NOT committed — there would be too many. **What is committed is the
approved specification the Executor actually received**, so that every
report has a corresponding instruction in the repository.

**Faithfully transcribe the complete specification supplied for
execution** — without intentional rewording, omission or normalization —
to:

    specs/2026-08-06T{HHMM}Z_role-model-and-executors.md

where `{HHMM}Z` is a UTC token obtained IMMEDIATELY BEFORE creating
commit 1 and used for both filenames. **Record the observed UTC
timestamp in the report. The token is fixed once commit 1 exists and is
not changed if later commits fall in another minute** — the filename
minute is not required to match Git commit metadata exactly. **Then compute its
SHA-256 from the committed blob**, and use that value wherever this
specification calls for "the specification's SHA-256".

**This resolves what would otherwise be undefined.** The digest is of
the blob YOU committed, not of conversation text whose encoding and line
endings two honest executors could read differently. There is no
canonical form to reconstruct — you create it.

**Correlation is by timestamp.** The report of the layering section uses
the SAME `{HHMM}Z` token in its filename, pairing specification and
report by name without either citing the other's digest.

**A0 has a mechanical part and an attestation part, and they are not
the same kind of evidence.**

*Mechanical, verifiable:* commit 1 adds exactly one concrete `specs/…`
path and nothing else; its blob SHA-256 is computed and recorded; every
later commit descends from commit 1; the specification path and the
report path carry the SAME `{HHMM}Z` token.

*Attestation, not machine-provable:* state whether you are aware of any
truncation, transcription, encoding or line-ending change introduced
while creating the committed artifact. **There is no canonical input
object to compare against, so this is your declaration, not a proof of
equality with conversation text.** Report any known transformation
rather than normalising silently.

**A1 — `AGENTS.md` role section replaced.** Verify by fixed-string
checks on the file at the branch head:

    present exactly once, operative region:
      "Roles are functions. Assignments are current"
      "The Researcher and Reviewer functions are exchanged"
      "does not by itself expand the Executor's authorized scope"
      "Incidental implementation exchanges"

    present AT LEAST once, operative region (the generic words
    necessarily recur, so an exact count of 1 is unsatisfiable):
      "Researcher"   "Reviewer"   "Executor"
    present exactly once, historical region only:
      "Claude is the independent reviewer/discriminator"
    count in operative region of each superseded phrase: 0
      "ChatGPT handles conceptual discussion"
      "Codex handles repository maintenance"
      "Claude is the independent reviewer/discriminator"

**The operative region is everything before the historical heading of
A1a; the historical region is from that heading to the next heading of
the same or higher level.** No region may contain both an operative and
a historical copy of the same phrase.

**A1a — The historical block, supplied verbatim.** Insert exactly this,
and verify it byte-for-byte:

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

**Do not reflow, reorder, or reword the preserved bullets.**

**A2 — `reviews/README.md` updated.** Verify present exactly once:
`created or substantively amended after`; `Existing records remain valid
historical evidence`; `Function:`. Verify the by-author directory set is
unchanged — `chatgpt`, `claude`, `codex`, `pi` — by comparing the tree
listing of `reviews/` at base and head. **No pre-existing file under `reviews/` is modified EXCEPT
`reviews/README.md`, whose modification this criterion requires.**
Verify blob equality for every OTHER pre-existing file under `reviews/`.

For the layout check, compare only the IMMEDIATE CHILD DIRECTORY NAMES
of `reviews/` at base and head. Expected at both: `chatgpt`, `claude`,
`codex`, `pi`.

**A3 — Dual-executor arrangement recorded** in `AGENTS.md`. Verify
present: `Codex`; `Claude Code`; `RTX 4070 Ti`; `sandboxed`;
`As recorded by PI decision on 2026-08-06`. The capability difference
must be stated, not only the names.

**A4 — Rule 8 reconciliation stated.** Verify present in `AGENTS.md`:
`rule 8`, together with a statement that where the older role text and
rule 8 conflicted, rule 8's function-based model governs. **Verify
`CONVENTIONS.md` is byte-identical between base and head** by blob
comparison — this task creates, renumbers and rewords no rule.

**A5 — `DECISION_LOG.md` entry.** The file is append-only and uses
`## <date> — <title>` headings with `### Decision` / `### Reason` prose
sections. **Use that existing format.** The entry must contain the
following exact factual phrases, which need NOT appear as key-value
labels where that would break the format:

    Date: 2026-08-06
    Decision owner: Principal Investigator
    Superseded documents: AGENTS.md role section; reviews/README.md
    Effect: prospective only
    No retrospective relabelling of existing reviews/ records
    Reference: CONVENTIONS.md rule 8
    Specification SHA-256: <computed from the commit-1 blob>
    Specification path: specs/2026-08-06T{HHMM}Z_role-model-and-executors.md

Verify each field literal is present.

**A6 — Staleness notices, supplied verbatim.** Insert exactly this
notice immediately below the title line of `HANDOFF.md`, and exactly
this notice immediately below the title line of `PROGRESS.md`:

    > **Staleness notice (2026-08-06):** This document is retained as
    > historical handoff/progress context and is not current. For the
    > latest committed P2-PHASE-01 integration and prerequisite status,
    > see `reports/2026-08-05_p2-phase-01_integration-and-drafts.md`.

**Verify by diff that each file's change is exactly this insertion and
nothing else**: the base bytes must be unchanged apart from the inserted
block. Do not choose a report yourself — the path above is specified
because "most recent report" is not unique at this revision, and
selecting one would be a scientific-status judgement this task has no
authority to make.

**A7 — Protected paths unchanged.** **Enumerate every BLOB path present
under `tests/`, `scripts/`, `derivations/`, `results/` in the BASE
tree**, plus `GATES.md`, `CONVENTIONS.md`, `pyproject.toml`. For each
enumerated path, compare base and head blob ids. Expected: identical for
all. **Additionally verify the head contains no added, deleted, renamed
or type-changed path under those prefixes.** Read these from the
objects; do not accept a value quoted to you.

**A8 — Scope, run twice: A8-pre and A8-final.** The same self-reference
that forced A9 to be split applies here through the manifest's `head`
field: a final manifest whose head is commit 3 cannot be written into
commit 3.

- **A8-pre** runs against commit 2. Its resolved manifest uses commit 2
  as `head`. The template, the resolved A8-pre manifest, its SHA-256,
  and the complete scope-check output go **into the committed report**.
- **A8-final** runs after commit 3, on a clean worktree at commit 3. Its
  resolved manifest uses commit 3 as `head`. The resolved manifest, its
  SHA-256, and the complete output are returned as **post-commit
  evidence** and are NOT written back into the report.

**A8-final carries the scope verdict.** A8-pre shows only that the
content changes were within scope before the report was added — and note
that only A8-final can confirm the report path itself is inside the
frozen manifest.

**Two manifests, because commit 2 and commit 3 are different states.**
A8-pre cannot use the final manifest: at commit 2 the report does not
yet exist, and under `mode: exact` a manifest demanding it would fail
for a reason that has nothing to do with scope compliance. Both
manifests are frozen here; neither is derived by you.

**A8-pre manifest — run against commit 2:**

    base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
    mode: exact
    add:
      specs/2026-08-06T{HHMM}Z_role-model-and-executors.md
    modify:
      AGENTS.md
      reviews/README.md
      HANDOFF.md
      PROGRESS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**A8-final manifest — run against commit 3:** The manifest block below
is the **content-authoritative supplied manifest**. **The manifest below is a TEMPLATE.** Before invocation you MUST
resolve both `{HHMM}` occurrences to the single UTC token fixed by the
specification commit's filename. **Exactly two transformations are
permitted, and no others:**

1. replace both `{HHMM}` placeholders with that same four-digit token;
2. add the computed `head` field.

No path, operation assignment, `mode`, `base`, or forbidden-operation
entry may change. You may create the resolved JSON OUTSIDE the
repository solely for invocation. **No manifest file is
committed.** **The DESIGNATED EVIDENCE LAYER** reproduces, separately: the supplied
manifest TEMPLATE; the RESOLVED invocation manifest; the resolved
manifest's SHA-256; and proof that all resolved paths carry the token
fixed by commit 1.

- For **A8-pre**, the designated layer is the COMMITTED REPORT.
- For **A8-final**, the designated layer is the POST-COMMIT EVIDENCE
  returned to the Reviewer — **not the report**, which cannot contain a
  manifest whose `head` is the report's own commit.

    base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
    mode: exact
    add:
      specs/2026-08-06T{HHMM}Z_role-model-and-executors.md
      reports/2026-08-06T{HHMM}Z_role-model-and-executors.md
    modify:
      AGENTS.md
      reviews/README.md
      HANDOFF.md
      PROGRESS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Run the scope checker separately:** against commit 2 with the A8-pre
manifest, and against commit 3 with the A8-final manifest. Record each
complete JSON output — including `observed_operations` — in its
designated evidence layer: A8-pre in the committed report, A8-final in
the post-commit evidence.

For each manifest, exactly two TYPES of transformation are permitted:

1. replace EVERY `{HHMM}` placeholder present in THAT manifest with the
   single token fixed by commit 1 — **one occurrence in A8-pre, two in
   A8-final**;
2. add the corresponding computed `head` field.

No other transformation is permitted in either manifest.

**A9 — Validators, run twice.** **`A9-pre` runs on a clean worktree at
commit 2, before the report file exists**; its output goes into the
committed report. **`A9-final` runs on a clean worktree at commit 3**
and is returned as post-commit evidence. **A9-final carries the
acceptance verdict**; A9-pre shows only that the content changes passed
before the report was added. Run each of these five individually, in
both passes:

    tests/test_repository_structure.py
    tests/test_si1_governance.py
    tests/test_gate_anchors.py
    tests/test_governance_tools.py
    tests/test_p2_phase01_scalar_exploratory.py

Interface: `python -m pytest <path>` with the cache provider disabled,
bytecode writing suppressed, and `basetemp` outside the repository.
Report for each: the exact command, complete stdout, **process exit
status**, wall time, and the interpreter and pytest versions.

    Expected on Claude Code: genuine exit 0, with output showing tests
      were collected and run. "No tests ran" or "no applicable files"
      is NOT a pass.
    Expected on Codex: report the outcome as observed. If the harness
      terminates the run, record it as
      NOT COMPLETED — DECLARED HOST LIMITATION,
      which is neither PASS nor FAIL, and do not write it back as a pass.

**A10 — Branch only, with `main` precisely defined.** The task branch is
created from the exact base `a0e9d11b7281f0c2185aa8d517bae009ab54807f`.
**You must not check out, modify, reset, merge into, or push `main`** —
local or remote. Push the task branch only.

Record separately the final values of: local `main`; `origin/main`; and
the task branch's base. **If `origin/main` has advanced through other
authorized work, report it — do not alter it and do not stop.** A remote
advance is not something this task controls, so it is reported, not
enforced.

## Evidence layering, to avoid self-reference

The report cannot contain its own final blob digest or the final branch
head. Therefore:

1. **Commit 1** — the approved specification artifact required by A0,
   at `specs/2026-08-06T{HHMM}Z_role-model-and-executors.md`.
2. **Commit 2** — the content changes (A1–A7).
3. **Commit 3** — the report at
   `reports/2026-08-06T{HHMM}Z_role-model-and-executors.md`, sharing the
   `{HHMM}Z` token with the specification of A0.

**The committed report records:** branch name; the base commit;
commit 1's SHA and message; commit 2's SHA and message; the pre-report
head (commit 2); the intended commit-3 message; raw output for A0–A7;
**A8-pre scope evidence**; and **A9-pre**, the validator run performed
before report finalization.

**The committed report does NOT record commit 3's SHA or the final
branch head** — it cannot, since commit 3 is the report itself.

4. **After commit 3**, run **A8-final** and **A9-final** against a clean
   worktree at commit 3. **Return as post-commit evidence to the
   Reviewer**, not written back into the report: commit 3's SHA and
   message; the final branch head; the final scope-check output; the
   A9-final validator outputs; and confirmation that every commit
   descends from commit 1.

**A9-final carries the acceptance verdict. A9-pre shows only that the
content changes passed before the report was added.**

## 3. Invariants and prohibitions

- **Executor-writable paths are exactly these seven:**
  `specs/2026-08-06T{HHMM}Z_role-model-and-executors.md`; `AGENTS.md`;
  `reviews/README.md`; `HANDOFF.md`; `PROGRESS.md`; `DECISION_LOG.md`;
  and `reports/2026-08-06T{HHMM}Z_role-model-and-executors.md`. Nothing
  else.
- **The specification file is supplied-frozen content, not
  executor-editable content:** you commit it; you do not rewrite,
  reflow, or amend it. `specs/` does not yet exist and is created here.
- **Do not edit `CONVENTIONS.md`.** No rule is created, renumbered, or
  reworded by this task.
- **Do not decide anything.** This task records decisions the PI has
  made. If the model as stated in §1 is ambiguous at any point, stop and
  report rather than resolving it.
- Do not delete, rename, or empty `reviews/codex/`, and do not
  retroactively relabel existing review records.
- Do not rewrite the scientific content of `HANDOFF.md` or
  `PROGRESS.md`; add the staleness notice only.
- Preserve superseded role text under an explicitly labelled
  historical/superseded subsection; it must not remain in any operative
  field.
- Branch naming: `docs/BRANCHING_POLICY.md` enumerates `gate/`,
  `paper/`, `review/`, `fix/`, `archive/`. **The policy-versus-practice
  contradiction is an open PI item and is not resolved here.** Use
  `review/role-model-and-executors`. If you judge that this still
  conflicts, stop and report.
- No merge into `main`, no PR, no force-push, no history rewrite. Push
  the branch.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything**; report anything missing as a finding.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own scratch tooling. Correct your own
  tooling and say that you did.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 4. Report contract

**Everything identified below as committed-report evidence goes into the
commit-3 report; everything identified as post-commit evidence is
returned separately to the Reviewer.** The report is created by the
evidence-layering section, not by any acceptance criterion — it is not
an A9 artifact. The conversational summary is a convenience; **the
committed report is the deliverable.**

- **in the COMMITTED report:** raw output for A0–A7 and **A9-pre**;
  branch name; the base commit; commit 1's SHA and message; commit 2's
  SHA and message; the pre-report head (commit 2); and the intended
  commit-3 message;
- **returned as POST-COMMIT evidence, not written into the report:**
  commit 3's SHA and message; the final branch head; **A8-final** and
  **A9-final**; push confirmation; and confirmation that every commit
  descends from commit 1;
- **in the committed report:** the A8-pre manifest TEMPLATE; the
  resolved A8-pre invocation manifest; its SHA-256; and the complete
  A8-pre scope-check output;
- **returned as post-commit evidence:** the A8-final manifest TEMPLATE;
  the resolved A8-final invocation manifest; its SHA-256; and the
  complete A8-final scope-check output;
- the authorization provenance of this specification, and any mid-task
  amendment reproduced verbatim;

- the superseded and superseding role text, quoted side by side;
- **which capability statements this task verified directly, which are
  PI-supplied facts, and which are current environment observations that
  are not permanent guarantees** — the dual-executor text asserts things
  this task does not re-test, and the report must not let them read as
  though it did;
- **whether recording this model exposes any further conflict** with
  `CONVENTIONS.md`, `docs/`, or any other committed artifact. The
  conflict this task resolves was found by a reviewer reading the
  repository, not by us; there may be more;
- a **Stops and clarifications** section. The five allowed PRIMARY
  categories, listed here so this specification is self-sufficient:

      SPECIFICATION_DEFECT
      ENVIRONMENT
      OBSERVATION_METHOD_ERROR
      REPOSITORY_DEFECT
      UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY

  **Exactly one primary category per stop.** Secondary findings
  discovered through a stop are recorded separately and classified
  independently. **Where an event has several causes, the primary is the
  one that caused the stop**, not the most serious consequence. If there
  were no stops, include the section and state that explicitly;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
