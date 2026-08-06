# Task specification — rebuild the role-model branch with clean commit metadata

Specification evidence base: `a0e9d11b7281f0c2185aa8d517bae009ab54807f`
Required verification target: the same commit.

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**No scientific or substantive governance decision in the reviewed
content is wrong.** This task makes only the standing-document wording
clarification expressly authorized in A4. The reviewed branch
`review/role-model-and-executors` @ `10c260b9…` was verified: seven
declared paths, correct commit layering, protected paths unchanged, the
role model landed as approved. **This task rebuilds it solely to remove
undeclared commit metadata from history.**

**What is being removed and why.** Commit
`031540028a57c4132f395aa9ad4b1e573c910ea6` carries two tooling-added
trailers that no specification authorized:

    Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01Fb9niiqHuwhAx8T17nHbpv

The PI's reason is **provenance, not secrecy**: this metadata would
enter `main`'s permanent history without review, and it is a class the
scope checker cannot catch — it verifies seven paths, not commit
messages. Commit messages are immutable, so "fix it later" is not
available. Accepting it once leaves no mechanism to prevent the next
occurrence.

**Your handling of it was correct.** You disclosed it and did not
rewrite history to remove it, because the task forbade that. This
specification authorizes the rebuild that the previous one could not.

---

## 1. Objective

A new branch reproduces the reviewed source artifacts exactly, EXCEPT
for the single PI-authorized `AGENTS.md` correction in A4, and records
the rebuild in three commits whose messages contain no trailer that this
specification does not authorize. `main` is unchanged. **The existing branch
`review/role-model-and-executors` is preserved untouched** as the
execution and negative-provenance record.

## 2. Commit-message hygiene — the point of this task

**Before creating each commit, inspect the exact proposed commit message
INCLUDING any trailers your tooling adds automatically.** If a trailer
appears that this specification does not authorize, **use a commit
method that stores only the authorized message.** You may choose the
mechanism, but: do not install tools; **do not change persistent user or
global configuration**; do not introduce any other attribution; and do
not modify any existing branch. If you cannot store a clean message by
any available means, **stop and report** rather than committing and
disclosing afterwards.

**Authorized message content, and nothing else:** a subject line, and an
optional body. **No `Co-Authored-By`, no session identifier or URL, no
tool version string, no automatically generated attribution.**

*(For information: the reviewed commit 2, `a021eed…`, carried no
trailers — the metadata defect was in commit 1 only. That does not
narrow this requirement: the same tooling may add trailers at any
commit.)*

**After each commit, inspect the COMPLETE STORED message from the commit
object** — `git log -1 --format=%B <commit>`. Pre-commit inspection is
not sufficient: the trailer that caused this task was added at commit
creation. **If unauthorized metadata appears despite the pre-commit
inspection, STOP IMMEDIATELY. Do not create the next commit and do not
push.**

Report, for each of the three commits, the **complete** stored message,
and state explicitly whether any trailer was suppressed and which.

This is a standing concern rather than a one-off: **the same tooling
will add the same trailers again unless each commit message is inspected
before it is created.**

## 3. Acceptance criteria

**A0 — New branch, from the pinned base.** Create
`review/role-model-and-executors-clean` from
`a0e9d11b7281f0c2185aa8d517bae009ab54807f`. **Do not delete, rename,
force-push, or modify `review/role-model-and-executors`** — verify at
task end that it still resolves to `10c260b96882ac12610f78840aeeabd07be2d7cb`.

**A1 — Content reproduced from the reviewed branch, subject only to
A4.** These are the SOURCE blob ids on
`review/role-model-and-executors` @ `10c260b9…`. Verify them there
first, then reproduce:

    specs/2026-08-06T0456Z_role-model-and-executors.md  05472d8d339b1f89e6dee265ea7a14190ee01d21
    AGENTS.md                                           15a29880d5196cee79dbd76eeab59224eb83d994
    reviews/README.md                                   9ef4ec5e68091e6f7f226a5ad69e64aa81d0b038
    HANDOFF.md                                          e60026120d933c1977ad0568506d292721cce2e8
    PROGRESS.md                                         5ef6e65a1e3f927d92b708c6527eab0f839d569c
    DECISION_LOG.md                                     0464b854c8adf57b2e79841a2d754bccf2c68a05

**At your commit 2:**

- the original specification, `reviews/README.md`, `HANDOFF.md`,
  `PROGRESS.md` and `DECISION_LOG.md` must have EXACTLY the blob ids
  above;
- **`AGENTS.md` must differ from `15a29880…` by exactly the A4
  replacement and nothing else.**

**The reviewed commit-2 tree `752de58f149f2a25a27caa1b1199b2e4f1f1066a`
is a SOURCE-REFERENCE tree, not the expected final tree, and does not
carry the verdict** — A4 necessarily changes it. Compute and report your
actual commit-2 tree id.

**The verdict is carried by three things:** exact blob equality for the
five unchanged reproduced artifacts; an exact one-hunk A4 diff for
`AGENTS.md`; and the A6 scope checks.

**A2 — Commit layering. Note that TWO specifications are involved and
they are not the same artifact.**

    commit 1  specs/2026-08-06T{HHMM}Z_role-model-clean-rebuild.md
                  <- THIS specification, the one you are executing
    commit 2  specs/2026-08-06T0456Z_role-model-and-executors.md
                  <- the ORIGINAL specification, reproduced as content
              AGENTS.md, reviews/README.md, HANDOFF.md, PROGRESS.md,
              DECISION_LOG.md
    commit 3  reports/2026-08-06T0456Z_role-model-and-executors.md

**Why they are separated.** Commit 1 must record the instruction that
authorized THIS execution, so the report has a corresponding
specification in the repository. The original specification is different
content and is reproduced in commit 2 alongside the other artifacts it
produced. Conflating them would leave the rebuild's own authority
unrecorded — the very defect this programme keeps closing.

`{HHMM}Z` is a UTC token obtained immediately before creating commit 1.
**The `0456` token in the two reproduced filenames is NOT regenerated**;
it belongs to the original task.

**A3 — The report.** The new report follows the reviewed report's
structure and preserves its historical descriptions where still
applicable, **but ALL branch-specific and execution-specific evidence
must be REGENERATED for the clean branch.**

**It must not copy the old raw outputs as though they were produced by
this rebuild.** Old scope JSON, old validator stdout, old commit
identities and old tree ids describe a different branch; reproducing
them here would be a false claim of verification.

Differences from the old report are limited in PURPOSE, not in literal
bytes: new commit identities and messages; clean-rebuild specification
provenance, including its path and digest; A4's single authorized
content delta; regenerated A0–A7 evidence; commit-message hygiene
evidence; and a statement that
`review/role-model-and-executors` @ `10c260b9…` is preserved unmodified
as the execution and negative-provenance record.

**The report must open with an identification section** naming all
three, because its filename alone will mislead a later reader:

    Execution authority:  specs/2026-08-06T{HHMM}Z_role-model-clean-rebuild.md
    Reproduced original:  specs/2026-08-06T0456Z_role-model-and-executors.md
    Report path:          reports/2026-08-06T0456Z_role-model-and-executors.md

**State that the report filename retains `0456` in order to produce the
intended final repository path, and that this does NOT mean the
rebuild's own specification carries the `0456` token.** The report is
the execution report for the rebuild, not only for the original task.

**The committed report does not record commit 3's SHA or the final
branch head** — that layering is unchanged.

**A4 — `this task` wording corrected.** In `AGENTS.md`, the phrase
`not re-verified by this task` loses its antecedent once it sits in a
standing document. **PI-authorized correction**, and the ONLY content
change permitted in this task: replace `this task` in that sentence with
`the task recorded in specs/2026-08-06T0456Z_role-model-and-executors.md`.

**This makes `AGENTS.md`'s blob differ from its source value.** Report
the new blob id and confirm by a one-hunk diff that this sentence is the
only change from `15a29880…`. Report your actual commit-2 tree id
alongside the source-reference tree `752de58f…`, with the difference
attributed to A4 and nothing else.

*(Reported by you, and correct: the specification's own supplied
blockquotes had no byte-for-byte criteria, which is how a four-word
omission passed unnoticed. That gap is queued for the rules amendment.)*

**A5 — Protected paths unchanged.** `CONVENTIONS.md`, `GATES.md`,
`pyproject.toml`, and every blob path present under `tests/`,
`scripts/`, `derivations/`, `results/` at the base: blob ids identical
between base and head, and no path added, deleted, renamed or
type-changed under those prefixes.

**A6 — Scope, run twice, manifests frozen here.**

**A6-pre manifest TEMPLATE, run against commit 2:**

    base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
    mode: exact
    add:
      specs/2026-08-06T{HHMM}Z_role-model-clean-rebuild.md
      specs/2026-08-06T0456Z_role-model-and-executors.md
    modify:
      AGENTS.md
      reviews/README.md
      HANDOFF.md
      PROGRESS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**A6-final manifest TEMPLATE, run against commit 3:** the same, plus
`reports/2026-08-06T0456Z_role-model-and-executors.md` under `add`.

**Both blocks are frozen TEMPLATES, not directly executable
manifests.** The only permitted transformations are: resolving the
single `{HHMM}` placeholder to the token fixed by commit 1, and adding
the computed `head`.

For each pass, record in its designated evidence layer: the supplied
TEMPLATE; the RESOLVED invocation manifest; the resolved manifest's
SHA-256; and the complete checker output including
`observed_operations`. **A6-final
carries the scope verdict.**

**A7 — Validators, run twice.** `A7-pre` on a clean worktree at
commit 2, before the report exists; `A7-final` on a clean worktree at
commit 3. **A7-final carries the acceptance verdict.** Run individually:

    tests/test_repository_structure.py
    tests/test_si1_governance.py
    tests/test_gate_anchors.py
    tests/test_governance_tools.py
    tests/test_p2_phase01_scalar_exploratory.py

Interface: `python -m pytest <path>`, cache provider disabled, bytecode
writing suppressed, `basetemp` outside the repository. Report for each:
exact command, **complete stdout and stderr**, process **exit status**,
wall time, and the Python and pytest versions. Genuine exit 0 is
required; "no tests ran" is not a pass.

**A8 — Branch only.** `main` — local and remote — is not checked out,
modified, reset, merged into, or pushed. Report the final values of
local `main`, `origin/main`, and the branch base separately. **If
`origin/main` has advanced through other authorized work, report it; do
not alter it and do not stop.**

## 4. Evidence layering

    commit 1  specification artifact
    commit 2  content changes
    commit 3  report

**Committed report:** branch name; base; commit 1 and commit 2 SHAs and
messages; the pre-report head; the intended commit-3 message; raw output
for A0–A5; A6-pre scope evidence; A7-pre validator output.

**Post-commit evidence, returned to the Reviewer and NOT written back
into the report:** commit 3's SHA and message; the final branch head;
A6-final; A7-final; push confirmation; ancestry confirmation.

**Raw means raw.** The previous review could not verify A6-final and
A7-final because they arrived summarised. **Summaries are not evidence
in this programme.** Return complete manifests, complete JSON including
`observed_operations`, complete stdout and stderr, and exact commands.

## 5. Invariants and prohibitions

- **Executor-writable paths are exactly these eight:**
  `specs/2026-08-06T{HHMM}Z_role-model-clean-rebuild.md`; the six of A1;
  and `reports/2026-08-06T0456Z_role-model-and-executors.md`. Nothing
  else.
- **Among the SIX SOURCE ARTIFACTS listed in A1, A4 is the only
  authorized content delta:**
  - the original role-model specification, `reviews/README.md`,
    `HANDOFF.md`, `PROGRESS.md` and `DECISION_LOG.md` are reproduced
    byte-for-byte from the reviewed branch;
  - `AGENTS.md` may differ only by the exact A4 replacement.
  **No other source-artifact content change is authorized.**
- **Two artifacts are NOT source artifacts and are not expected to be
  byte-identical to anything:** the clean-rebuild specification created
  in commit 1, which is a new authority artifact and does not exist on
  the reviewed branch; and the report created in commit 3, which is
  regenerated evidence for THIS branch.
- **Do not modify, delete, rename or force-push
  `review/role-model-and-executors`.** It is preserved as the record of
  what happened, including the metadata defect.
- **No commit may carry a trailer this specification does not
  authorize.** See §2.
- Do not edit `CONVENTIONS.md`. No rule is created, renumbered or
  reworded.
- **Do not fix the stale role text in `docs/RESEARCH_WORKFLOW.md`,
  `README.md`, or `docs/local/execution_environment.md`.** You found
  these and were right to report them; they are a separate authorized
  task and are out of scope here.
- No merge into `main`, no PR, no force-push, no history rewrite on any
  existing branch.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything**; report anything missing as a finding.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own scratch tooling. Correct your own
  tooling and say that you did.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- the three complete commit messages exactly as stored, and whether any
  trailer was suppressed;
- the commit-2 tree id, `AGENTS.md`'s new blob id, and the single-file
  diff proving A4 is the only content difference;
- everything listed in §4 under its correct layer;
- confirmation that `review/role-model-and-executors` still resolves to
  `10c260b96882ac12610f78840aeeabd07be2d7cb`;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings classified separately, included even if there were
  no stops;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
