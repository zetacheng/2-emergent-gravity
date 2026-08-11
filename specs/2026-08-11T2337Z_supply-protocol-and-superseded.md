# Task specification — the review supply protocol, and a superseded-branch attribute

Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`

> **The diquark line is integrated**, and the register below reflects
> that. **Both `CONVENTIONS.md` and `docs/BRANCHING_POLICY.md` are
> byte-identical at this base to what they were before that
> integration** — it touched neither — **so A1's digests are unchanged
> from when this specification was drafted.**
>
> **The register gained one entry from that episode**, and it is the
> most instructive of the three: **a specification that stopped
> correctly.**

Classification: **MATERIAL**. Governed by Rule 15: this task's
pre-execution review is a committed artifact — see A0 commit 2 and A2.

**Two governance additions, both records of failures the programme has
already had.** No science, no gate, no computation.

**Review artifact delimiters**, each a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

---

## 0. Part one: the review supply protocol

**Rule 15 requires a pre-execution review to be committed. It says
nothing about how the review text reaches the executor**, and that gap
has produced **eight attempts and five distinct failure modes**:

    1  the instruction naming a delimiter contained that delimiter, so
       a first-occurrence search found the instruction
    2  the same again, in the next task
    3  no delimiter was supplied at all; the executor had to decide the
       boundary from the text's shape
    4  a preamble sentence preceded the BEGIN line
    5  a leading blank line: whether to strip it was an executor
       decision with no rule behind it

**Each was patched in the next specification.** **That is the pattern
worth ending** — a supply convention rediscovered per task is not a
convention.

**One attempt succeeded**, and the executor's own assessment should be
preserved: *the difference was how the message happened to be composed,
not anything the specification did differently.* **A success that
depends on the sender's habits is not a protocol.**

**Half the problem is already fixed, by the task that landed the
diquark line.** Its A5 carried a transport-artifact clause — strip at
most one leading and one trailing blank line — and **that closed the
one-byte residual seven previous reports had flagged as an unwritten
executor choice.** **It is the first piece of this protocol to be
written down**, and Rule 18 below generalises it from one
specification's clause to a standing rule.

**The other half recurred in that same task: mode 1, the shared line.**
**That is the eighth instance**, and it is the mode a standing rule
must fix, because **no amount of care by a sender prevents a
specification from containing the delimiter it names.**

### The rule to land, as Rule 18

> **18. Review supply protocol.**
>
> **A pre-execution review is supplied to the executor between two
> delimiter lines whose exact text is stated in the specification that
> requires the review.** The delimiters are:
>
>     === REVIEW ARTIFACT BEGINS ===
>     === REVIEW ARTIFACT ENDS ===
>
> **Matching is by COMPLETE LINE, never by first occurrence of the
> delimiter string.** A specification that states a delimiter contains
> it, as does any instruction accompanying the supply; **a substring
> search will find those instead of the boundary.**
>
> **The committed artifact is ALL text strictly between the delimiter
> lines.** **Any instruction accompanying the supply, and any preamble,
> MUST appear OUTSIDE the delimiter block.**
>
> **From the delimited text, at most one leading blank line and at most
> one trailing blank line are stripped as transport artifacts. No other
> byte is removed or normalised.**
>
> **The block is mechanically authoritative.** An earlier draft of this
> rule also excluded *"any instruction accompanying the supply"* from
> within the block — **which would have required the executor to decide
> which bytes are instruction, replacing a boundary judgement with a
> semantic one.** **The executor classifies nothing; the delimiters
> decide.**
>
> **If instruction text is found inside the block, that is a supply
> defect: STOP and report it.** Do not remove it.
>
> **If the supplied text is missing, carries no delimiter lines, or does
> not correspond to the specification, the executor STOPS and says
> which.** **The executor never infers a boundary**, and never authors,
> edits, summarises or reformats a review.
>
> **Placeholders inside a review's text stay as written.** Placeholders
> are resolved in the artifact's PATH only.

**The blank-line clause is the one addition beyond current practice.**
It exists because that decision was made silently by an executor, and
**a silent decision about the byte content of a governance record is
exactly what Rule 15 exists to prevent.**

## 1. Part two: a superseded-branch attribute

**Amendment K requires a superseded branch to be preserved and
identified as superseded, and forbids integrating one.**
`docs/BRANCHING_POLICY.md` has no way to express that.

**Its state machine is about DELETION**, and it is closed:

    present on remote,  verified_merged true   -> PENDING_DELETE
    present on remote,  verified_merged false  -> NOT_AUTHORIZED
    listed, absent from remote                 -> ABSENT_FROM_REMOTE

    listed_count = pending + not_authorized + absent_from_remote

**SUPERSEDED IS NOT A FOURTH STATE, and adding it as one would be
wrong twice over.** It would break that closed identity, and it would
conflate two questions: *may this branch be deleted* and *may this
branch be integrated*. **A superseded branch is correctly
`NOT_AUTHORIZED` for deletion** — it is present and unmerged. **What is
missing is the second question's answer.**

### What to add

**An ATTRIBUTE, orthogonal to the deletion states**, and a register of
branches carrying it.

> **Superseded branches.**
>
> **A branch is SUPERSEDED when its work has been re-issued or replaced
> and it is preserved as evidence rather than for integration.**
>
> **A superseded branch MUST NOT be integrated.** Its content may remain
> correct — supersession is about integrability and task identity, not
> about correctness — **but the authoritative instance is the branch
> that replaced it.**
>
> **This is an attribute, not a deletion state.** A superseded branch
> still reaches exactly one Stage-1 deletion outcome, and the closed
> count identity is unchanged. **The two questions are independent:
> whether a branch may be deleted, and whether it may be integrated.**
>
> **Supersession is recorded in the register below**, naming the branch,
> its commit, what replaced it, and why. **A Git ref carries no such
> marker, so the register is where it lives.**

**The register**, with the entries known at issue:

    fix/pi-decisions-and-deferred @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
      superseded by  fix/pi-decisions-v2, then fix/pi-decisions-v3
      reason         re-issued on a clean branch after the second
                     execution overwrote the first execution's pushed
                     records on the same branch
      content        the substantive content was approved; the
                     representation was not

    fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36
      superseded by  fix/pi-decisions-v3
      reason         stale base: main advanced through two governance
                     landings and the branch lost conflict-free
                     integrability
      content        APPROVED and unchanged; only its integrability
                     lapsed

    gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192
      superseded by  gate/p2-land-diquark-line-v2
      reason         the specification stated an impossible merge-base
                     and the executor STOPPED at the pre-merge guard;
                     the re-issue corrected the value
      content        the branch carries a report of the stop and NO
                     merge; it is the record of a correct refusal, not
                     of failed work

**The third entry differs in kind from the first two and the register
should not flatten that.** The first two carry approved work that was
re-instantiated elsewhere. **The third carries no work at all** — its
specification was defective, the executor stopped before any tree
changed, and **what it preserves is the evidence that a stop happened
and why.** **Supersession covers both; the register records which.**

**Verify all three are still present on the remote at those commits,
and that none is an ancestor of `main`.** **If any has been merged or
moved, STOP** — this register would then be describing something
else.

**Determine the register's complete membership yourself.** The three
above are the ones this specification knows of. **Enumerate the remote branches and classify each**, under this
threshold:

> **A branch is added to the register only where a DURABLE REPOSITORY
> ARTIFACT explicitly records its re-issue, replacement or supersession
> and identifies the replacement or the reason.**
>
> **Naming similarity, age, Git topology, or the mere existence of a
> later branch do NOT suffice**, singly or together. **Supersession is
> not established by topology**: a later branch with similar content or
> a similar name does not prove an earlier one was formally replaced.
>
> **Where evidence suggests supersession but does not establish it,
> report `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, name the
> branch and the evidence, and LEAVE IT OUT of the register** pending
> PI authority.

**The threshold exists so that an exhaustive search does not become an
invitation to create a governance classification.** **Classifying a
branch as superseded is a decision; finding the artifact that already
records one is an observation.** **This task performs the second.**

**If you find no further members, say that you searched and how** —
Rule 16's discipline applies to a register as much as to a report.

## 2. What must not happen

- **Do not renumber rules 1–17**, and do not reword them.
- **Do not delete any branch**, or change any branch ref.
- **Do not add a fourth deletion state**, and do not alter the closed
  count identity.
- **Do not integrate any superseded branch**, and do not assess whether
  any branch's content is correct. **Supersession is not a verdict on
  content.**
- **Do not add any test.** The enforcement gap — that no test checks any
  of these rules — is a known open item and **a separate task.**
- **Do not modify `AGENTS.md`.**

## 3. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md
    commit 3  CONVENTIONS.md, docs/BRANCHING_POLICY.md, DECISION_LOG.md
    commit 4  reports/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
work**, per Rule 15.

**A1 — Pinned inputs**, verified before use; a mismatch is a STOP.
Method: `git cat-file blob <rev>:<path> | sha256sum`.

    CONVENTIONS.md
    e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

    docs/BRANCHING_POLICY.md
    0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9

**A2 — This task's pre-execution review committed, unedited**, per
Rule 18 as this task lands it. **Apply the rule you are landing**, and
say in the report whether it was sufficient — **this task is its own
first test.**

**A3 — Rule 18 added** as a new `### 18.` section after Rule 17, in the
file's existing style, with the delimiter literals and the blank-line
clause present.

**A4 — Rules 1–17 unchanged.** Their numbers and titles are identical,
**and — after removing only the Rule 18 section — the remaining text is
byte-identical to the evidence-base version.** **Heading equality is a
proxy; report the body comparison.**

**A5 — The superseded attribute and register added** to
`docs/BRANCHING_POLICY.md`, per §1, **with the deletion state machine
and its closed count identity byte-identical to the evidence-base
version.** Report that section's before and after explicitly.

**A6 — Register membership determined**, per §1: **all three known
entries** verified present at their commits and not ancestors of
`main`, plus your own enumeration and classification of the remaining
remote branches under §1's evidence threshold.

**A7 — `DECISION_LOG.md` entry** in the file's existing format,
recording both additions and that they are prospective. **Append-only:
zero deleted lines, verified both against the evidence base AND for each
commit against its parent.**

**A8 — Nothing else touched.** `GATES.md`, `AGENTS.md`,
`pyproject.toml`, and **every path under `scripts/`, `results/`,
`tests/`, `derivations/` and `reviews/` that exists at the evidence
base**: blob-identical. **Compare path by path** — `reviews/` gains one
base-absent authorised path. **No gate status changes.**

**A9 — Scope**, three additions and three modifications:

    add:
      specs/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md
      reports/2026-08-XXT{HHMM}Z_supply-protocol-and-superseded.md
    modify:
      CONVENTIONS.md
      docs/BRANCHING_POLICY.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 3 additions and 3 modifications**, matching
the six paths above.

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A10-pre** at the pre-report head
goes in the report; **A10-final** at the pushed head is post-report
evidence.

**If any validator asserts a rule count or the branching policy's
structure, report what it asserts.** Both files gain content here.

**A11 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to the evidence base; create the branch
from that commit; move no `main` ref. **Local `main` is stale by
design.** Report all three. Push the task branch only. **Delete no
branch.**

**A12 — Commit-message hygiene** on every commit: inspect the proposed
message before, the stored message after; permit no `Co-Authored-By`, no
session identifier or URL, no tool attribution. **Report per commit
whether any trailer was suppressed and which.**

## 4. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task `CONVENTIONS.md` will carry eighteen rules and
`docs/BRANCHING_POLICY.md` a superseded register. **A reader could
conclude that supersession and review supply are now enforced.** **They
are recorded, not enforced** — **no test checks any of the eighteen
rules**, and nothing prevents a superseded branch from being merged by a
task that does not consult the register. **That gap is the known open
item this task is forbidden to close.**

## 5. Evidence layering

**Committed report:** A1–A9, A10-pre, A12, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A10-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the six paths of A9 only.
- **Do not do anything §2 forbids.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `governance/supply-protocol-and-superseded`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- raw output for A1–A10, scope-checker JSON verbatim including
  `observed_operations`;
- **A4's body comparison**, showing rules 1–17 unchanged after removing
  the Rule 18 section;
- **A5's before and after for the deletion state machine**, shown
  byte-identical;
- Rule 18 and the superseded section quoted in full as landed;
- **A6's enumeration**: every remote branch classified, with your reason
  for any addition to the register beyond the THREE supplied;
- **both append-only measures of A7**;
- **whether Rule 18, applied to this task's own review supply, was
  sufficient** — specifically: **did the complete-line matching resolve
  the shared-line mode, did the blank-line clause remove a decision you
  would otherwise have made silently, and did any text inside the
  delimiter block require you to judge whether it was instruction?**
  **If any judgement remained, the protocol is still incomplete and the
  next task should know**;
- **for any branch you did NOT add to the register**, the evidence you
  found and why it fell short of §1's threshold. **A register whose
  exclusions are invisible cannot be audited**;
- **§4's Rule 16 assessment**, junction named or search described;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 8. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      CONVENTIONS.md at 0ab6369a…
    method      git cat-file blob 0ab6369a:CONVENTIONS.md | sha256sum
    check type  BYTE-EXACT SHA-256
    CONFIRMED   e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

    target      docs/BRANCHING_POLICY.md at 0ab6369a…
    method      git cat-file blob 0ab6369a:docs/BRANCHING_POLICY.md | sha256sum
    check type  BYTE-EXACT SHA-256
    CONFIRMED   0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9

**Both re-measured at the fixed evidence base.** An earlier draft of
this record said the digests were absent because the base was set only
at issue, and that an issuer would add them later. **That described a
drafting state this specification is no longer in** — the base is fixed
and A1 supplies both values, **so the record must contain the executed
checks rather than a promise that someone will run them.**

    target      docs/BRANCHING_POLICY.md at 0ab6369a…
    method      section extraction and substring containment
    check type  EXACT LITERAL SUBSTRING, no normalisation

    CONFIRMED   the three Stage-1 outcomes are PENDING_DELETE,
                NOT_AUTHORIZED and ABSENT_FROM_REMOTE
    CONFIRMED   the closed identity
                listed_count = pending + not_authorized + absent
    CONFIRMED   no occurrence of "SUPERSEDED" anywhere in the file

    target      the remote branch list at 0ab6369a…
    CONFIRMED   fix/pi-decisions-and-deferred at 52f65117…, present,
                not an ancestor of main
    CONFIRMED   fix/pi-decisions-v2 at ebd531ab…, present, not an
                ancestor of main
    CONFIRMED   fix/pi-decisions-v3 at 93de3218…, present, IS an
                ancestor of main — it is the surviving instance and is
                NOT superseded
    CONFIRMED   gate/p2-land-diquark-line at d64cd912…, present, not an
                ancestor of main
    CONFIRMED   "SUPERSEDED" occurs 0 times in docs/BRANCHING_POLICY.md

**Every check in this record was measured at `0ab6369a…`, the fixed
evidence base.** An earlier draft carried some of them at `57c5a6eb…`,
before the diquark line was integrated; **they were re-run rather than
relabelled.**

**A6 still requires you to verify them yourself**: a branch's status can
change between a specification's drafting and its execution, and **this
specification has already been overtaken once.**
