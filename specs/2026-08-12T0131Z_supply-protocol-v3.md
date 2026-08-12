# Task specification — the review supply protocol, and a superseded-branch attribute

Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`

> ## RE-ISSUE, second — Rule 18 v2 worked; A3 did not
>
> **`governance/supply-protocol-v2 @ 40168469…` is preserved, superseded
> for integration, and not carried forward.** No governance file was
> touched; the executor stopped at A3.
>
> **What happened.** §0 was rewritten to abandon delimiters. **A3 was
> carried over from the delimiter version unchanged**, still requiring
> the landed rule to contain the delimiter literals and the blank-line
> clause. **The rule §0 directs has neither, by design.** Two
> instructions, mutually unsatisfiable; the executor stopped rather than
> choose. **The defect is this specification's, and it is the same
> propagation shape Amendment G names.**
>
> **Rule 18 v2 itself worked, and this is the first time the answer is
> yes.** The review arrived as a file; its digest was identical at
> supply, staging and commit; **no step required a judgement of any
> kind, because there was no boundary to locate.**
>
> **Two further defects that version carried**, both found and neither
> reached: §1 said *"Verify all three"* while listing five, and its
> kind-distinction paragraph described an entry by ordinal that the list
> had since displaced — **landing it verbatim would have committed a
> false statement.** §1 now refers to entries by name.

> ## RE-ISSUE — the first issue found Rule 18 insufficient on its own first use
>
> **`governance/supply-protocol-and-superseded @ 7146a093…` is preserved,
> superseded for integration, and not carried forward.**
>
> **What happened.** The transport layer fused an attachment marker to
> line 0 of the pasted review, so `=== REVIEW ARTIFACT BEGINS ===` had
> **zero complete-line matches** while `END` had one. **The executor
> derived the boundary and continued**, disclosing exactly what it did.
> **The committed artifact was byte-correct** — verified: no delimiter,
> no transport residue, no preamble.
>
> **Why it is not integrated anyway.** A2 required applying Rule 18;
> Rule 18 forbade the only available action. **That is an inconsistency
> between instructions, and the standing invariant says to stop.** The
> executor did not. **The root defect is this specification's**: Rule 18
> carried a prohibition — *the executor never infers a boundary* —
> **with no matching STOP trigger**, so its four literal triggers all
> stayed silent while the prohibited act became necessary.
>
> **Rule 18 is not patched in this version. It is replaced.** §0 gives
> the reason.

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

**This task's own pre-execution review is supplied AS A FILE**, per the
Rule 18 this task lands. **No delimiters are used and none should be
looked for.** If a review arrives as pasted text instead, **that is a
supply defect: STOP and say so** — this task is the rule's first
subject and must not be the first exception to it.

---

## 0. Part one: the review supply protocol

**Rule 15 requires a pre-execution review to be committed. It says
nothing about how the review text reaches the executor**, and that gap
has produced **five distinct failure modes across nine attempts**:

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

**And the eighth attempt exposed a SIXTH failure mode: a transport
prefix fused to the BEGIN line**, leaving zero complete-line matches for
BEGIN and one for END. **That is not mode 5** — the blank-line rule
worked perfectly on its first live use, and the "at most one" bound was
never reached.

**The executor's finding on the sixth mode is why this version replaces
the approach rather than extending it:** complete-line matching turned a
silent wrong guess into a loud absence, **which is better and still a
failure.**

**One half was fixed once and is now moot.** The task that landed the
diquark line carried a transport-artifact clause — strip at most one
leading and one trailing blank line — which closed the one-byte
residual seven reports had flagged as an unwritten executor choice.
**Rule 18 below does NOT generalise it.** A file has no transport
artifact to strip, **so the clause it fixed no longer has a problem to
solve.** It is recorded here because the failure was real, not because
the remedy survives.

**The other half recurred in that same task: mode 1, the shared line.**
**That is the eighth instance**, and it is the mode a standing rule
must fix, because **no amount of care by a sender prevents a
specification from containing the delimiter it names.**

### The rule to land, as Rule 18

**The delimiter approach is abandoned, not repaired.** Eight attempts
produced five failure modes and every one was an extraction problem.
**A rule that patches extraction leaves a judgement point; removing the
need to extract leaves none.**

> **18. Review supply protocol.**
>
> **A pre-execution review is supplied to the executor AS A FILE, not
> as text pasted into a prompt.** The executor commits that file's
> bytes unchanged.
>
> **No extraction, no delimiters, no normalisation.** There is no
> boundary to locate, so **no boundary can be inferred**; there are no
> transport artifacts to strip, so **no stripping rule is needed.**
>
> **The specification SHOULD also be supplied as a file.** It is
> committed at a frozen path by the task's first commit, so **a pasted
> specification makes commit 1's bytes the executor's transcription with
> no supplied file to digest against** — verifiable in the way commit 2
> now is only if it too arrives as a file.
>
> **A pasted specification is permitted and is not a STOP**, because it
> is instruction rather than an artifact whose exact bytes carry
> authority. **But the executor reports which way it arrived**, and
> where it was pasted, says so.
>
> **The executor verifies correspondence before committing**: the
> supplied review must identify the specification it reviews, by digest
> or by task name. **If it does not, or if no file is supplied, or if
> the file corresponds to a different specification, STOP and say
> which.**
>
> **The executor never authors, edits, summarises or reformats a
> review**, and never reconstructs one from a conversation.
>
> **Placeholders inside a review's text stay as written.** Placeholders
> are resolved in the artifact's PATH only.

**Why a file rather than a delimited paste.** The five observed failure
modes — a delimiter string inside the instruction naming it, twice; no
delimiter supplied; a preamble before the BEGIN line; a transport prefix
fused to the BEGIN line — **are all consequences of asking an executor
to find a boundary inside a stream that other content shares.** **A file
has no such boundary.**

**The evidence for the swap is in the transport record itself.**
Specifications have been supplied as files throughout and have never
failed to arrive intact. **Reviews were pasted, and failed eight times.**

**What this rule gives up, stated plainly.** A pasted review is visible
in the conversation; a file is not. **The reviewer's text therefore
reaches the record without passing under the PI's eye in the same
message** — and the correspondence check is what stands in for that.
**If that trade is not wanted, the alternative is a delimiter protocol
with a transport-prefix clause, and this specification does not propose
one.**

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

    governance/supply-protocol-v2
                              @ 40168469608618aef6812735ff70e32de0e3cbc8
      superseded by  this task
      reason         its A3 required the landed Rule 18 to contain
                     delimiter literals and a blank-line clause, while
                     the rule it directed abandoned both; the executor
                     stopped at that inconsistency
      content        no governance file was touched; the branch carries
                     a stop report and the first successful live test of
                     the file-supply rule

    governance/supply-protocol-and-superseded
                              @ 7146a093c65788a57d63a747b71d86edb91eddc6
      superseded by  this task
      reason         its A2 required applying a Rule 18 whose own text
                     forbade the only available action; the executor
                     derived a boundary and continued where the
                     standing inconsistency invariant required a stop
      content        the governance work was correct and the committed
                     review was byte-correct; what failed was the rule
                     it was landing, which this version replaces

    review/role-model-and-executors
                              @ 10c260b96882ac12610f78840aeeabd07be2d7cb
      superseded by  review/role-model-and-executors-clean, merged
      reason         rebuilt SOLELY to remove undeclared commit
                     metadata from history; the clean-rebuild
                     specification names the successor and the reason
      content        VERIFIED CORRECT before the rebuild — seven
                     declared paths, correct commit layering, protected
                     paths unchanged, the role model landed as approved
      note           this branch ALREADY carries a durable disposition:
                     "permanently preserved ... the unmerged record of a
                     commit-metadata defect, retained as
                     negative-provenance evidence". **That disposition
                     stands unchanged.** The two answer different
                     questions -- permanently preserved means do not
                     delete; superseded means do not integrate -- and
                     the register exists because they are independent.
                     **Do not edit, replace or weaken the existing
                     preservation entry.**

    gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192
      superseded by  gate/p2-land-diquark-line-v2
      reason         the specification stated an impossible merge-base
                     and the executor STOPPED at the pre-merge guard;
                     the re-issue corrected the value
      content        the branch carries a report of the stop and NO
                     merge; it is the record of a correct refusal, not
                     of failed work

**The entries differ in kind and the register should not flatten
that.** **Refer to them by BRANCH NAME, never by ordinal** — an ordinal
is correct only until the list grows, and this paragraph has already
been wrong once for exactly that reason.

    approved work re-instantiated elsewhere
      fix/pi-decisions-and-deferred
      fix/pi-decisions-v2
      review/role-model-and-executors

    no work at all: a defective specification, an executor that
    stopped, and the evidence that a stop happened and why
      gate/p2-land-diquark-line
      governance/supply-protocol-v2

    work completed but the execution contract breached, so not
    integrable although the content was correct
      governance/supply-protocol-and-superseded

**Supersession covers all three kinds; the register records which.**

**Verify all six are still present on the remote at those commits, and
that none is an ancestor of `main`.** **If any has been merged or
moved, STOP** — this register would then be describing something
else.

**Determine the register's complete membership yourself.** The six
above are the ones this specification knows of. **Enumerate the remote branches and classify each**, under this
threshold:

> **A branch is added to the register only where a DURABLE REPOSITORY
> ARTIFACT records its re-issue, replacement or supersession and
> identifies the replacement or the reason.**
>
> **The artifact must record the FACT, not use a particular WORD.** A
> specification that says a branch was rebuilt and names both the
> successor and the reason satisfies this **even if the word
> "superseded" never appears.** **An earlier version said "explicitly
> records", which an executor correctly read as requiring the term** —
> and correctly declined to supply it. **The requirement is that the
> classification be findable in the record, not that it be phrased in
> the register's vocabulary.**
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

    commit 1  specs/2026-08-XXT{HHMM}Z_supply-protocol-v3.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_supply-protocol-v3.md
    commit 3  CONVENTIONS.md, docs/BRANCHING_POLICY.md, DECISION_LOG.md
    commit 4  reports/2026-08-XXT{HHMM}Z_supply-protocol-v3.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **The token MUST differ from
`2337` and from the token the v2 issue used.** **Commit 2 precedes the
work**, per Rule 15.

**If the task stops before commit 3**, commit the report at commit 4's
frozen path **as the next commit in sequence**, and **say which commit
number it actually is and why the intervening commit was not made.**
**Do not renumber silently and do not omit the report.**

**The programme has improvised this twice.** It is specified here so a
third executor does not have to.

**A1 — Pinned inputs**, verified before use; a mismatch is a STOP.
Method: `git cat-file blob <rev>:<path> | sha256sum`.

    CONVENTIONS.md
    e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

    docs/BRANCHING_POLICY.md
    0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9

**A2 — This task's pre-execution review committed, unedited**, per
Rule 18 as this task lands it: **supplied as a file, committed
byte-unchanged, no extraction of any kind.** Report the supplied file's
digest and the committed blob's digest and show them equal.

**Verify correspondence**: the review must identify this specification
by digest or task name. **If it does not, or no file is supplied, or it
corresponds to a different specification, STOP and say which.**

**Apply the rule you are landing**, and say in the report whether it was
sufficient — **this task is its own first test, and the previous
version's rule failed exactly this test.**

**A3 — Rule 18 added** as a new `### 18.` section after Rule 17, in the
file's existing style, carrying **the file-supply rule of §0** — not a
delimiter rule.

**Check for its actual content**, and report each:

    "AS A FILE"                     present
    "no delimiters"                 present
    a correspondence requirement    present
    a STOP for a missing, pasted or non-corresponding review   present

    "=== REVIEW ARTIFACT"           ABSENT
    "blank line"                    ABSENT

**The last two are absences and must be verified as such.** **An earlier
version of this criterion required the delimiter literals and the
blank-line clause to be PRESENT** — carried over unchanged from the
delimiter version while §0 was rewritten around them. **That made A3
and §0 mutually unsatisfiable, and an executor correctly stopped rather
than choose between them.**

**A4 — Rules 1–17 unchanged.** Their numbers and titles are identical,
**and — after removing only the Rule 18 section — the remaining text is
byte-identical to the evidence-base version.** **Heading equality is a
proxy; report the body comparison.**

**A5 — The superseded attribute and register added** to
`docs/BRANCHING_POLICY.md`, per §1, **with the deletion state machine
and its closed count identity byte-identical to the evidence-base
version.** Report that section's before and after explicitly.

**A6 — Register membership determined**, per §1: **all six known
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
      specs/2026-08-XXT{HHMM}Z_supply-protocol-v3.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_supply-protocol-v3.md
      reports/2026-08-XXT{HHMM}Z_supply-protocol-v3.md
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
- Branch naming: use `governance/supply-protocol-v3`. **Both superseded
  branches are preserved — `7146a093…` and `40168469…`; do not touch,
  reuse or delete either.**
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
  for any addition to the register beyond the SIX supplied;
- **both append-only measures of A7**;
- **whether Rule 18, applied to this task's own review supply, was
  sufficient** — specifically: **did the review arrive as a file, did
  its bytes reach the commit unchanged, and did ANY step require a
  judgement of any kind?** **The previous version's rule failed exactly
  this question; if this one leaves any judgement, the protocol is
  still incomplete and the next task should know**;
- **the supplied file's digest and the committed blob's digest**, shown
  equal;
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
