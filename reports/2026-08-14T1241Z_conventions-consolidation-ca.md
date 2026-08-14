# Execution report — `C-a`: consolidate twelve observed failures into durable conventions

**Specification:** `specs/2026-08-14T1241Z_conventions-consolidation-ca.md`
**Specification evidence base:** `bec0117168144d54fb23338b673cf7a7e4771868`
**Branch:** `governance/conventions-consolidation-ca`, cut from authoritative `main` @ `bec01171…`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18.

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3 and measures nothing at commit 4.**

**This task does not touch `main`.** Integration is a separate task.

---

## 1. Outcome

**Thirteen source items consolidated into SEVEN principles: four amendments
and three new numbered rules.**

    Amendment M -> Rule 7    A4 A5 A6 A8    a recorded measurement's scope
    Amendment N -> Rule 18   A2 A3          supply as a file, bind by digest
    Amendment O -> Rule 12   A1 A7          machine-readable declarations, complete reading lists
    Amendment P -> Rule 5    B1 B3          landing outcome inline, line survival on auto-merge
    Rule 19                  B2             pinned-artifact integrity
    Rule 20                  B4             permitted pre-push hygiene repair
    Rule 21                  E2             artifact-state / statement-kind namespaces

**MEASURED:** `CONVENTIONS.md` gains 382 lines and loses **zero**. Four
hunks, every one a pure addition. **The file as it stood at the evidence base
is an exact in-order subsequence of the file as it stands now** — 1023 of
1023 lines matched in order — so nothing was renumbered, reordered or
re-worded.

    numbered rules      18 -> 21     contiguous, no gap, 19 20 21 new
    amendment letters   A-I K L  ->  A-I K L M N O P     no J created
    mechanism markers   7 principles, exactly one marker each
                        1 EXISTS   5 DEFERRED   1 RULE-ONLY

**FIVE OF SEVEN ARE `MECHANISM DEFERRED`, and that number is the honest
output of this task.** §14 states it as what `C-b` and `C-c` still owe.
**Nothing here is described as closing the governance gap.**

**All four of §2's known assignments were verified against the repository and
all four are CONFIRMED** — with one sharpening on `A1` that §6 records,
because `P1` does more than the specification says and the difference matters.

**A16, answered up front.** My harness's standing git guidance does instruct
a `Co-Authored-By` trailer and a session URL. **None was written on any of
the four commits**, nothing was suppressed by amendment, no commit was
amended.

---

## 2. Refs and inputs — A1, MEASURED

    refs/heads/main                          bec0117168144d54fb23338b673cf7a7e4771868   as specified
    supplied classification artifact         1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9   as specified
    CONVENTIONS.md, Git blob at the base     b3c96300a1f3eab967d3d141a1e81b278887342c

**No mismatch. No stop.**

**§12's structural figures, independently re-measured rather than quoted:**

    numbered rules '^### [0-9]+\.'          18      as §12 records
    amendment letters                       A B C D E F G H I K L — eleven, no J
    lines                                   1022    as §12 records
    'CONVENTIONS' references in GATES.md    13      as §12 records

**Every figure reproduces.**

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    2311e04d50861e14bcc24170be429b38dfa418c35ac698d0196a8587a684b591
    committed specification   2311e04d50861e14bcc24170be429b38dfa418c35ac698d0196a8587a684b591   equal
    supplied review           092be5c02d6cd3469f590f13d9fcebbe01e0aba14fa9b1395f0ed8cc90932cfc
    committed review          092be5c02d6cd3469f590f13d9fcebbe01e0aba14fa9b1395f0ed8cc90932cfc   equal

The review's `reviewed specification SHA-256:` is filled in and reads
`2311e04d50861e14bcc24170be429b38dfa418c35ac698d0196a8587a684b591` — **the
digest of the specification actually committed and executed.** Committed
unedited, per Rule 18, and before the work it authorises.

**Both the specification and the review arrived as FILES, not pasted.**
Recorded because Rule 18 requires the executor to say which way it arrived —
and because Amendment N(a), written by this very task, makes supplying the
specification as a file a producer-side obligation. **On this task it was
met.**

---

## 4. The traceability matrix — A3, MEASURED

**Thirteen source items. Thirteen rows. Each item exactly once.**

| # | Item | What it requires | Now covered by |
|---|---|---|---|
| 1 | `A1` | a scope block carries a `stated:` key | **Amendment O(a)** to Rule 12 |
| 2 | `A2` | a specification is supplied as a file | **Amendment N(a)** to Rule 18 |
| 3 | `A3` | a review records the digests it reviewed | **Amendment N(b)** to Rule 18 |
| 4 | `A4` | a measurement is taken over the whole subject | **Amendment M(a)** to Rule 7 |
| 5 | `A5` | a verification statement is clone-invariant | **Amendment M(b)** to Rule 7 |
| 6 | `A6` | a hunk count names its diff context | **Amendment M(c)** to Rule 7 |
| 7 | `A7` | a reading list names evidence-write sites | **Amendment O(b)** to Rule 12 |
| 8 | `A8` | evidence about a criterion is not its discharge | **Amendment M(d)** to Rule 7 |
| 9 | `B1` | an integration states its landing outcome inline | **Amendment P(a)** to Rule 5 |
| 10 | `B2` | a task modifying a pinned file re-pins it | **Rule 19** |
| 11 | `B3` | an auto-merge is verified by line survival | **Amendment P(b)** to Rule 5 |
| 12 | `B4` | a permitted pre-push hygiene amend | **Rule 20** |
| 13 | `E2` | artifact-state and statement-kind namespaces | **Rule 21** |

**Row count: 13. Confirmed thirteen.** **No row is empty.** **No item appears
twice.** The same matrix is carried in `CONVENTIONS.md` itself, so coverage
can be counted by a reader of the adopted text — §7 explains where it sits
and why.

### 4.1 Where my consolidation differs from the candidate grouping, and why

**The candidate grouping in §1 of the specification places `A7` with the
evidence principles and `A8` with the review-binding ones. I moved both.**
§1 permits replacement "with reasons"; here are the reasons.

**`A8` moved from group 2 to Amendment M (the evidence principle).** Group 2
is "artifact identity and review binding", and `A2`/`A3` are mechanically
about digests binding a review to a specification. **`A8` is not about
digests or artifacts at all** — it is about the scope of a claim: a
measurement over a range is evidence, and calling it a discharge claims more
than the measurement supports. **That is precisely the discipline `A4`, `A5`
and `A6` share.** Putting it with them makes Amendment M one principle in
four costumes rather than three costumes plus a stranger.

**`A7` moved from group 1 to Amendment O (the declarations principle).**
Group 1 is about statements whose scope exceeds their evidence, and `A7` can
be read that way — a reading list implicitly claims sufficiency. **But `A7`
binds the SPECIFIER at authoring time, not the reporter at recording time**,
and its remedy is a longer reading list rather than a narrower claim. `A1` is
the other specifier-side authoring obligation, and Rule 12 is the rule that
already binds the specifier to make a task checkable. **Grouping by who is
bound and when produced a cleaner split than grouping by surface
resemblance.**

**The count is unchanged at seven**, and Amendment M still carries four items
and Amendment O two. **The review's instruction was to optimise for
non-overlapping durable principles rather than reproduce seven headings; the
number came out the same and the composition did not.**

---

## 5. Mechanism markers — A4, MEASURED

**Every principle this task writes carries exactly one marker.** Verified
mechanically: each principle's text was bounded by the next heading and its
`Mechanism marker:` lines counted.

| Principle | `CONVENTIONS.md` lines | Marker |
|---|---|---|
| Amendment P → Rule 5 | 262–309 | **RULE + MECHANISM DEFERRED** |
| Amendment M → Rule 7 | 386–450 | **RULE + MECHANISM DEFERRED** |
| Amendment O → Rule 12 | 894–936 | **RULE + MECHANISM DEFERRED** |
| Amendment N → Rule 18 | 1183–1230 | **RULE + MECHANISM DEFERRED** |
| Rule 19 — Pinned-artifact integrity | 1231–1262 | **RULE + MECHANISM EXISTS** |
| Rule 20 — Permitted pre-push hygiene repair | 1263–1312 | **RULE + MECHANISM DEFERRED** |
| Rule 21 — Artifact-state and statement-kind namespaces | 1313–1348 | **RULE-ONLY** |

    principles                     7
    exactly one marker each        True
    RULE + MECHANISM EXISTS        1
    RULE + MECHANISM DEFERRED      5
    RULE-ONLY                      1

**No rule is without a marker.** **The one `EXISTS` is the one whose check I
read; §6 records that verification.**

---

## 6. The four known assignments — A5, verified against the repository

**All four CONFIRMED. One carries a sharpening the specification did not
state, and it makes the assignment stronger rather than weaker.**

### `A1` — `stated:` in scope blocks → MECHANISM DEFERRED — **CONFIRMED, with a sharpening**

**§2 says: "`P1` already PARSES `stated:`, but no mechanism REQUIRES a newly
issued specification to supply it."**

**Confirmed, and `P1` does more than parse.** MEASURED by running the landed
`parse_scope_block` against a scope block with no `stated:` record:

    {'parse': 'NOT_PARSEABLE', 'detail': "no 'stated:' record in the scope block"}

**`P1` REFUSES a specification that lacks the key** — it does not merely fail
to read a total; it declines the whole block, and `NOT_PARSEABLE` makes the
run `INCOMPLETE` at a non-zero exit.

**The assignment is still `DEFERRED`, and the reason is sharper than "it only
parses".** **The refusal is opt-in.** It fires only when a task's own
specification asks for the checker to be run, names its own path in
`specification_paths`, and the executor runs it. **Nothing requires a
specification to be checked at all**, so nothing requires it to carry the
key. **Amendment O(a) states it in that form** rather than in §2's.

### `A3` — review cites digests → MECHANISM DEFERRED — **CONFIRMED**

**MEASURED:** no property compares a review's cited digest against the
specification committed beside it. Searching `scripts/governance_tools/` and
`tests/` for review-digest handling returns only unrelated hits —
`core.py`'s gate-pin schema and `spec_consistency_checker.py`'s `file_hash`
domain, neither of which reads a review. **The checker touches `reviews/`
only as a path prefix**, at `REVIEW_PREFIX` and in `P2`/`P8`, for ordering
and placement.

**And the check is fully specifiable inside the repository** — both blobs are
committed by the same task. Amendment N(b) says so, and says it is
registered nowhere.

### `B2` — re-pin on modification → MECHANISM EXISTS — **CONFIRMED**

**Verified by READING `tests/test_gate_pins.py`, as A5 directs.** **No stale
tree was constructed**; that measurement was made and reported by an earlier
task and is not repeated here.

    tests/test_gate_pins.py exists          7158 bytes at the evidence base
    test_every_pinned_artifact_matches_its_pin
        collects every (sha256 `<64 hex>`) occurrence in GATES.md,
        resolves the artifact path above it, hashes the bytes,
        and appends "GATES.md line N: <path> is stale -- pinned X, measured Y"
        then asserts the failure list is empty
    test_pin_set_is_not_empty               fails on zero pins
    test_every_pin_resolves_to_a_path       fails on an unresolvable pin

**`EXISTS` is the right marker and Rule 19 states its limits**: the check
enforces the obligation's effect, has no notion of "the same task", and runs
when the suite runs rather than at commit time.

### `B3` — line survival on auto-merge → MECHANISM DEFERRED — **CONFIRMED**

**MEASURED:** nothing in `scripts/` or `tests/` measures line survival. The
only `survival` matches are in `scripts/normalization_chain.py` and are
physics — a mass window, unrelated. `merge_guard.py` compares merge-base
identity; `P5` recomputes parentage and merge-base. **Neither examines file
content.**

**No assignment was found misstated.** The `A1` sharpening is an addition to
the reasoning, not a correction of the verdict.

---

## 7. Placement — A6, justified per principle

**`CONVENTIONS.md` uses two forms for principles and they are not
interchangeable: an amendment modifies an identified existing rule in place;
a numbered rule stands alone.** Each choice below is against the actual file.

**Amendment M → Rule 7, Evidence precedence.** Rule 7 already binds *"any
claim about the state of the repository … MUST be verified against the
committed artifacts before it is relied upon or recorded."* **What changes is
the SCOPE of that verification and how the result is worded** — a
verification performed correctly over part of a subject and recorded as
covering the whole satisfies Rule 7's letter and defeats it. **That is a
modification of an existing obligation, not a free-standing one**, so it is
an amendment.

**Amendment N → Rule 18, Review supply protocol.** Rule 18 already governs
how the review and specification are supplied and what the executor verifies.
**What changes: the SHOULD on supplying a specification as a file gains a
producer-side counterpart, and "by digest or by task name" is tightened to
require the digest where a file exists to digest.** **Rule 18's own text is
untouched**, and its executor-side permission for a pasted specification
survives unchanged — §8's diff shows the amendment appended, not woven in.

**Amendment O → Rule 12, Acceptance criteria must be mechanically
checkable.** Rule 12 already binds the specifier to make criteria
machine-checkable and to derive literals from the repository, and closes with
*"Rule 7 … applies to the authoring of specifications as much as to the
reporting of results."* **What changes: the scope declaration becomes a
machine-readable record rather than a sentence, and the reading list must
name where evidence is written.** Both are specifier-side obligations that
make a task answerable. Amendment.

**Amendment P → Rule 5, Minimum mandatory merge discipline.** Rule 5 is the
merge floor; Rule 11 names it as the source of the standardized integration
authorization. **What changes: one obligation before the floor — the
authorization states its landing outcome — and one after it — the auto-merge
verification measures line survival.** **Rule 5 point 4 already says correct
parentage does not imply a correct tree**, and B3 is that observation one
level down, which is what makes this an amendment rather than a new rule.

**Rule 19 — Pinned-artifact integrity. NEW NUMBERED RULE.** **No existing
rule carries the obligation.** Rule 5 point 5 requires pinned digests to
survive a merge unchanged, but that is merge-local; B2's obligation binds any
task that modifies a pinned file, merge or not. **Amending Rule 5 would have
scoped a general obligation to merges** and left the common case — a task
editing a pinned artifact directly — uncovered. Stands alone.

**Rule 20 — Permitted pre-push hygiene repair. NEW NUMBERED RULE.** **It
grants a permission rather than modifying an obligation.** No existing rule
addresses amending a commit; Rule 5's floor and Rule 15's timing both assume
commits are made once. **A permission grafted onto a rule about something
else would be hard to find and easy to over-read.** Stands alone.

**Rule 21 — Artifact-state and statement-kind namespaces. NEW NUMBERED
RULE.** **It resolves a category question about two vocabularies and modifies
no existing obligation.** There is no rule about label vocabularies to amend.
Stands alone, and carries the PI ruling verbatim.

**Numbering, MEASURED:** new rules are **19, 20, 21** — from 19 upward with
no gap, and the full sequence at the head is `1 … 21` contiguous. **The
amendment letters used are M, N, O and P** — the next four after L. **No
Amendment J was created**: `grep -c 'Amendment J'` returns **0**.

### 7.1 One placement decision that is NOT a principle, flagged for overrule

**The traceability matrix needed a home in the adopted text, and it is not a
principle**, so §4's rule-or-amendment choice does not decide it.

**I placed it in a new `## Consolidation record — C-a` section at the end of
the file.** **Reasoning:** §3 asks for the matrix "in the adopted text or
immediately beside it", and a reader of `CONVENTIONS.md` should be able to
count coverage without the report; `## ` sections are an existing structural
form in the file, used four times already; and the record explicitly states
that it binds nothing.

**I did not treat this as the "third form" §4 makes a STOP**, because §4
governs where a *principle* goes and this is a record. **I flag it here so
the Reviewer can overrule me** — if the intended reading is that any new
heading is a third form, then the correct action was a stop and the matrix
belongs in the report alone.

---

## 8. The diff — A7

**MEASURED, `CONVENTIONS.md` base to commit 3:**

    added lines      382
    deleted lines      0
    hunks              4, every one of the form @@ -N,0 +M,K @@ — a pure addition

    @@ -260,0  +261,49 @@    Amendment P, into Rule 5
    @@ -335,0  +385,66 @@    Amendment M, into Rule 7
    @@ -777,0  +893,44 @@    Amendment O, into Rule 12
    @@ -1022,0 +1182,223 @@   Amendment N, Rules 19-21, and the consolidation record

**The deleted-line count is zero**, measured two ways: `git diff --numstat`
reports `382  0`, and a count of diff lines beginning with `-` excluding the
`---` header returns **0**.

**A stronger check than a deleted-line count, because a count of zero is
consistent with a line having been altered in place if the diff were taken
oddly.** **MEASURED: the file at the evidence base is an exact IN-ORDER
SUBSEQUENCE of the file at commit 3** — every one of its 1023 lines appears,
in order, in the new file. **1023 of 1023 matched.** **Nothing was
renumbered, reordered or re-worded**, and all eighteen pre-existing `###`
rule headings and all eleven pre-existing `**Amendment X,` headings are
present verbatim, with zero missing.

**The full diff follows.**

    diff --git a/CONVENTIONS.md b/CONVENTIONS.md
    index b3c9630..85b4378 100644
    --- a/CONVENTIONS.md
    +++ b/CONVENTIONS.md
    @@ -258,6 +258,55 @@ specification does not describe, that is a stop-before-push and a
     request for authorization — not a resolution.** Re-issue is the worked
     example below; the next instance will not be a re-issue.
     
    +
    +**Amendment P, adopted 2026-08-14 — the integration authorization states its landing outcome, and an auto-merge is verified by content and not only by blob.**
    +
    +**Mechanism marker: RULE + MECHANISM DEFERRED.**
    +
    +Rule 5's numbered floor governs the merge itself. **This amendment adds one
    +obligation before it and one after it.**
    +
    +**(a) AN INTEGRATION SPECIFICATION STATES ITS LANDING OUTCOME INLINE**,
    +including when the outcome is "do not advance". **A complete, reviewed
    +integration whose specification is silent about the landing leaves `main`
    +unmoved**, because no clause authorises the advance and the executor may not
    +supply one. *Incident: exactly that occurred, and the branch sat integrated
    +and unlanded.*
    +
    +**The landing target is named as the task's own final report commit, not as a
    +SHA.** **A SHA naming a commit that carries the task's review is unreachable
    +as a landing target**, because Rule 15 places the report commit after it. A
    +specification that names a SHA has named something the task will have moved
    +past by the time it lands.
    +
    +**(b) FOR AN AUTO-MERGED FILE, BLOB DIFFERENCE FROM BOTH SIDES IS A NECESSARY
    +CONDITION AND NOT A SUFFICIENT ONE.** Rule 5 point 4 already records that
    +correct parentage does not imply a correct tree; **this is the same
    +observation one level down.** A merged blob differing from both parents rules
    +out one side having been taken wholesale **and rules out nothing else.**
    +
    +**Where a file was auto-merged from two sides that both changed it, the
    +verification MEASURES LINE SURVIVAL: every line each side added over the
    +merge-base, checked for presence in the merged file, with the count missing
    +reported and expected to be zero.** *Incident: an executor measured 90/57,
    +104/133 and 24/61 added lines across three auto-merged files with zero
    +missing — beyond what its criterion required, which had asked only for blob
    +difference.*
    +
    +**This is a necessary condition too, not a sufficient one.** Line survival is
    +set membership; **it does not establish correct interleaving, and it is not a
    +substitute for running the merged behaviour.** The verification that a merged
    +parser still works is the suite, not the diff.
    +
    +**What is deferred.** **No mechanism enforces either obligation.** For (a),
    +nothing inspects a specification for a landing clause. For (b), **no
    +mechanism measures line survival**: `merge_guard.py` compares merge-base
    +identity and `P5` recomputes parentage, and neither examines file content.
    +**The line-survival check is fully specifiable and cheap** — it needs the
    +merge-base, two sides and the merged file, all of which the checker already
    +resolves — **and it is not currently registered as a mechanism item.**
    +**Registering it is `C-c`'s.**
    +
     ### 6. Reporting honesty for merges
     
     A report MUST distinguish "the main worktree carries approved untracked
    @@ -333,6 +382,72 @@ issue** — the PI may amend a task in flight without a review cycle. It
     requires only that the amendment become visible in the artifact the
     reviewers read.
     
    +
    +**Amendment M, adopted 2026-08-14 — a recorded measurement states its scope, and does not exceed it.**
    +
    +**Mechanism marker: RULE + MECHANISM DEFERRED.**
    +
    +Rule 7 requires a claim about repository state to be verified against the
    +committed artifacts. **This amendment governs the SCOPE of that verification
    +and how the resulting statement is worded.** A verification performed
    +correctly over part of a subject, and recorded as though it covered the
    +whole, satisfies Rule 7's letter and defeats its purpose.
    +
    +**Four obligations, which are one discipline in four costumes: a recorded
    +statement may not claim more than the measurement behind it supports.**
    +
    +**(a) A measurement written into a verification record is taken over the
    +WHOLE subject.** No `head`, no `tail`, no sampled or scrolled view.
    +**Where a tool truncates by default, the record names the flag or method
    +that defeated the truncation**, or states that the full output was read.
    +*Incident: three recording errors came from truncated output — a register
    +count cut at eighty lines, a merge list cut at twenty-two, an open-item list
    +cut at sixty.*
    +
    +**(b) A verification statement is CLONE-INVARIANT.** A statement about the
    +repository must be true in any clone of it. **"The object is not present" is
    +a function of local garbage collection; "the object is not an ancestor of any
    +ref" is a property of the repository.** Where only the clone-local form was
    +measured, the record says so and does not present it as a repository
    +property. *Incident: a `MEASURED` line asserted the former and was true only
    +in the clone that produced it.*
    +
    +**(c) A count of diff hunks NAMES THE DIFF CONTEXT it was taken at.** A hunk
    +count is not a property of a change; it is a property of a change and a
    +context setting together. *Incident: three logical edits produced three hunks
    +at `--unified=0` and one at git's default, and the criterion said only "three
    +hunks".*
    +
    +**(d) EVIDENCE ABOUT A CRITERION IS LABELLED EVIDENCE, NEVER DISCHARGE.**
    +**A criterion is discharged by the task that carries it, over that task's own
    +range, under its own review.** A later measurement showing that a stopped
    +criterion would pass today is evidence about a counterfactual. **It does not
    +retroactively discharge the criterion, and a report that blurs the two is
    +wrong however favourable the measurement was.** **Where such evidence is
    +gathered, the range it is taken over is named explicitly**, because a range
    +chosen loosely measures a different criterion than the one that stopped.
    +*Incident: a counterfactual run over the correct range differed from one over
    +the branch tip by exactly one property, and naming the wrong range would have
    +measured a different criterion.*
    +
    +**What is deferred.** **No mechanism enforces any of (a)–(d).** No partial
    +mechanism exists: `P1` through `P9` read repository state and none inspects
    +the relation between a prose statement and the method behind it. **Sub-cases
    +of (b) and (c) are mechanisable** — a lint could reject clone-local idioms
    +offered as evidence of absence, and could require a context flag beside any
    +hunk count — **and neither lint exists.** **This missing enforcement is not
    +currently registered under any item of the mechanism bucket**; `C4`
    +(cross-document factual consistency) is the nearest registered item and is a
    +different gap, being about statements disagreeing across documents rather
    +than about a statement exceeding its own evidence. **Registering it is
    +`C-c`'s.**
    +
    +**Why the general obligation is not simply machinable.** The subject of a
    +prose measurement is defined in prose. A machine can read the statement; it
    +cannot read the method the author used, and (a) and (d) are about that
    +relation. **That is a reason to register the gap, not to call the rule
    +self-enforcing.**
    +
     ## Role separation and outcome-based task specification
     
     These rules extend, and do not replace, rules 1–7 above. They bind
    @@ -775,6 +890,50 @@ nothing.
     
     **Stop behaviour is tested separately** from mutation reach.
     
    +
    +**Amendment O, adopted 2026-08-14 — a specification's declarations are machine-readable, and its reading list names where evidence is written.**
    +
    +**Mechanism marker: RULE + MECHANISM DEFERRED.**
    +
    +Rule 12 binds the specifier to make each acceptance criterion mechanically
    +checkable and to derive its literals from the repository. **This amendment
    +adds two obligations that make a task answerable at all.**
    +
    +**(a) A SCOPE BLOCK CARRIES A `stated:` KEY** declaring the total the
    +manifest is asserted to contain, per category — additions and modifications —
    +**as a machine-readable record and not as a sentence elsewhere in the
    +document.** The declared total is what a checker compares the manifest
    +against. **A count inferred from prose is not a declaration**: it depends on
    +which sentence a parser reaches first, and a grammar that walks backwards
    +through a document for the nearest number is reading the author's layout
    +rather than the author's intent.
    +
    +**(b) A READING LIST NAMES THE SITES WHERE EVIDENCE FIELDS ARE WRITTEN, not
    +only the functions that compute them.** A specification that directs an
    +executor to the routine producing a quantity, but not to the place the
    +quantity is recorded, has under-described its own question. *Incident: a
    +task's answer lay at three lines outside its specification's reading list,
    +and its executor found them anyway — which is not a property the next
    +specification may rely on.*
    +
    +**A reading list is a claim about sufficiency**, and Amendment M applies to
    +it: it may not assert a scope its author did not check.
    +
    +**What is deferred, and (a) and (b) differ.**
    +
    +**For (a) there IS a partial mechanism and it is not the obligation.** `P1`
    +reads the `stated:` record, and returns `NOT_PARSEABLE` for a scope block
    +that lacks one — **so it does more than parse; it refuses.** **But the
    +refusal is opt-in.** It occurs only when a task's own specification asks for
    +the checker to be run against it, names its own path, and the executor runs
    +it. **Nothing requires a newly issued specification to carry the key**, and
    +compliance is currently maintained by an authoring habit rather than by a
    +repository mechanism. **The partial mechanism is `P1`; the missing
    +enforcement is registered as `C2`.**
    +
    +**For (b) there is no mechanism at all**, partial or otherwise, and none is
    +currently registered. **Registering it is `C-c`'s.**
    +
     ### 13. Execution environment
     
     The repository declares its execution environment in an execution-environment
    @@ -1020,3 +1179,226 @@ and never reconstructs one from a conversation.
     
     **Placeholders inside a review's text stay as written.** Placeholders are
     resolved in the artifact's PATH only.
    +
    +**Amendment N, adopted 2026-08-14 — the specification is supplied as a file, and the review binds to it by digest.**
    +
    +**Mechanism marker: RULE + MECHANISM DEFERRED.**
    +
    +Rule 18 governs how a review reaches the executor and what the executor
    +verifies on receipt. **This amendment adds a producer-side obligation and
    +tightens what the review must record. It does not alter Rule 18's
    +executor-side handling of a pasted specification**, which remains permitted
    +and remains not a stop.
    +
    +**(a) A SPECIFICATION IS SUPPLIED TO THE REVIEWER AND THE EXECUTOR AS A
    +FILE.** Rule 18 states this as a SHOULD and states the consequence: a pasted
    +specification makes commit 1's bytes the executor's transcription, with no
    +supplied file to digest against. **This amendment makes it an obligation ON
    +THE PARTY ISSUING THE SPECIFICATION.** **The two are not in tension:** the
    +producer must supply a file; the executor still does not stop when the
    +producer fails to, and still reports which way it arrived. *Incident: the
    +specification was pasted rather than supplied on at least four occasions, and
    +one review declined to record a digest because of it.*
    +
    +**(b) A REVIEW ARTIFACT RECORDS `reviewed specification SHA-256:`**, filled
    +in, naming the digest of the specification it reviewed. **Where it reviews a
    +further artifact, it also records `reviewed artifact SHA-256:`.** **Both are
    +required where both apply**: recording only the artifact's leaves the
    +substitution case open, in which a review of one specification is presented
    +beside a different one. *Incident: a review of a stale specification version
    +occurred twice in one session and was undetectable from the text.*
    +
    +**A review that names a task by title and not by digest binds to nothing a
    +later reader can check.** Rule 18 permits identification "by digest or by
    +task name"; **this amendment requires the digest where a specification file
    +exists to digest.**
    +
    +**What is deferred, and (a) and (b) differ sharply.**
    +
    +**(a) is not checkable inside the repository.** The supplied file is outside
    +it, and whether a specification arrived as a file or as pasted text leaves no
    +trace in the committed bytes. **The executor's report is the only record, and
    +that is a disclosure obligation rather than a mechanism.**
    +
    +**(b) IS fully checkable inside the repository, and no check does it.** The
    +review blob and the specification blob are both committed by the same task;
    +extracting the cited digest and comparing it to the specification's measured
    +digest requires nothing the checker does not already have. **No property does
    +this — `P1` through `P9` treat `reviews/` only as a path prefix, for ordering
    +and placement.** **This missing enforcement is not currently registered as a
    +mechanism item.** **Registering it is `C-c`'s.**
    +
    +### 19. Pinned-artifact integrity
    +
    +**Mechanism marker: RULE + MECHANISM EXISTS.**
    +
    +**A task that modifies a file pinned by digest in a registered gate RE-PINS
    +IT IN THE SAME TASK.** The re-pin is part of the modification, not a
    +follow-up: a gate whose pin names a digest its artifact no longer has is a
    +gate asserting something false, and it asserts it from the moment the
    +artifact changes until someone notices.
    +
    +**A task that modifies no pinned file owes no re-pin, and establishes that by
    +measurement rather than by assumption.** The check is cheap — locate every
    +pin, resolve the artifact each names, compare against the changed-file set —
    +and the assumption is exactly the kind Rule 7 forbids.
    +
    +*Incident: three consecutive tasks required a re-pin written in by hand, and
    +nothing detected the omission. The rule was ratified once by PI ruling for a
    +single instance; this is its durable form.*
    +
    +**The mechanism, named and verified.** `tests/test_gate_pins.py`, landed at
    +`e3ce8063`, resolves every `` (sha256 `<64 hex>`) `` occurrence in `GATES.md`
    +to the artifact path named above it, hashes that file's bytes and fails on
    +any mismatch. It also fails on a pin whose path cannot be resolved, and on a
    +`GATES.md` carrying no pin at all.
    +
    +**What the mechanism does and does not enforce.** It enforces the
    +obligation's effect: a task that modified a pinned artifact without re-pinning
    +cannot report a green suite, because the pin is stale at its head. **It does
    +not enforce the words "in the same task"** — it has no notion of tasks — and
    +**it runs when the suite runs**, not at commit time. **A branch that never
    +runs its validators is not protected by it.**
    +
    +### 20. Permitted pre-push hygiene repair
    +
    +**Mechanism marker: RULE + MECHANISM DEFERRED.**
    +
    +**An unpushed commit MAY be amended solely to remove a MECHANICALLY DETECTED
    +commit-message hygiene violation, before any branch publication, provided
    +both the rejected and the replacement commit ids are recorded in the task
    +report.**
    +
    +**Four conditions, and each is load-bearing:**
    +
    +1. **MECHANICALLY DETECTED.** The violation was reported by a check with a
    +   non-zero exit, and **the executor exercised no judgement about whether a
    +   violation existed.** A permission to amend on an executor's own opinion of
    +   a message would be a different and much wider rule.
    +2. **UNPUSHED, and before any publication.** No other party can have seen the
    +   rejected commit.
    +3. **HYGIENE ONLY.** The commit's tree is unchanged by the amendment; only
    +   the message differs.
    +4. **BOTH COMMIT IDS RECORDED** in the report, so the amendment is visible
    +   rather than silent.
    +
    +**This authorises nothing about pushed or reviewed history**, and it is not a
    +general licence to rewrite.
    +
    +**The open question, decided here.** The ratification of the single instance
    +left open whether the repair requires EVERY AFFECTED CHECK re-run or only the
    +failing one. **It requires every affected check.**
    +
    +**The reason is the same one Amendment M(b) gives.** An amend changes the
    +commit object and therefore its identifier, and every property computed over
    +a range ending at or containing that commit was measured against an
    +identifier that no longer exists. **Re-running only the check that failed
    +would leave the other results true of a superseded state** — the defect class
    +Amendment M exists to prevent — **and the cost of re-running all of them is
    +seconds.**
    +
    +**The ratified instance did not settle this.** Its executor re-ran all
    +affected checks voluntarily, and a voluntary act is not a precedent.
    +**Recording it as though it were would be the substitution Amendment N(b)
    +guards against, in a different currency.**
    +
    +**What is deferred.** **The trigger is mechanised and the obligations are
    +not.** `P6` detects the commit-hygiene violation that opens this permission —
    +that is the partial mechanism, and it is why condition 1 is checkable at all.
    +**Nothing verifies that both commit ids were recorded, that the tree was
    +unchanged across the amendment, or that the affected checks were re-run.**
    +**None of that is currently registered as a mechanism item.** **Registering
    +it is `C-c`'s.**
    +
    +### 21. Artifact-state and statement-kind namespaces
    +
    +**Mechanism marker: RULE-ONLY.**
    +
    +**PI RULING, adopted verbatim:**
    +
    +> **Artifact-state labels and statement-kind labels are distinct
    +> vocabularies; an artifact-state label does not need to appear in the
    +> statement-kind vocabulary.**
    +
    +`ADOPTED`, `PROPOSED`, `SUPERSEDED` and `DRAFT` describe **the state of an
    +artifact**. `MEASURED`, `DERIVED`, `RECOMMENDATION` and `CAUTION` describe
    +**the kind of a statement**. **Two namespaces. An entry in one is not a gap
    +in the other**, and a label census over one vocabulary does not report a
    +defect merely because a label from the other is absent from it.
    +
    +**A document that defines its kind labels is not obliged to define its state
    +labels in the same list**, and a reviewer finding a state label outside the
    +kind vocabulary has found a category difference rather than an undefined
    +term.
    +
    +*Provenance, because it bears on how the rule was reached.* An executor met
    +the question, **reported it rather than deciding it**, and recorded that
    +calling `ADOPTED` "not a kind label" would be a judgement. The Reviewer
    +proposed the namespace distinction and its wording; **the PI issued the
    +ruling.** **A reviewer proposing a ruling and the PI issuing it are different
    +acts**, and this item was open precisely because the executor declined to
    +decide it.
    +
    +**Why RULE-ONLY.** The rule resolves a category error between two
    +vocabularies. **It imposes no obligation on any artifact that a machine could
    +test**: it does not require a label to be present, absent, or of any form. It
    +tells a reader — and a reviewer — that a question does not arise. **There is
    +nothing here to check, which is different from there being something to check
    +that nobody has built.**
    +
    +## Consolidation record — `C-a`
    +
    +**This section is a record, not a principle.** It exists so that the coverage
    +claimed by the four amendments and three rules adopted on 2026-08-14 can be
    +COUNTED rather than reconstructed from memory. **Nothing here binds; the
    +rules and amendments it points to are what bind.**
    +
    +**Source: the governance debt classification, digest
    +`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9`**, §A and
    +§B — twelve observed failures — plus `E2`, ruled by the PI.
    +
    +**Thirteen source items, thirteen rows, each item exactly once.**
    +
    +| Item | What it requires | Now covered by |
    +|---|---|---|
    +| `A1` | a scope block carries a `stated:` key | Amendment O(a) to Rule 12 |
    +| `A2` | a specification is supplied as a file | Amendment N(a) to Rule 18 |
    +| `A3` | a review records the digests it reviewed | Amendment N(b) to Rule 18 |
    +| `A4` | a measurement is taken over the whole subject | Amendment M(a) to Rule 7 |
    +| `A5` | a verification statement is clone-invariant | Amendment M(b) to Rule 7 |
    +| `A6` | a hunk count names its diff context | Amendment M(c) to Rule 7 |
    +| `A7` | a reading list names evidence-write sites | Amendment O(b) to Rule 12 |
    +| `A8` | evidence about a criterion is not its discharge | Amendment M(d) to Rule 7 |
    +| `B1` | an integration states its landing outcome inline | Amendment P(a) to Rule 5 |
    +| `B2` | a task modifying a pinned file re-pins it | Rule 19 |
    +| `B3` | an auto-merge is verified by line survival | Amendment P(b) to Rule 5 |
    +| `B4` | a permitted pre-push hygiene amend | Rule 20 |
    +| `E2` | artifact-state and statement-kind namespaces | Rule 21 |
    +
    +**Mechanism markers, counted.**
    +
    +    RULE + MECHANISM EXISTS      1     Rule 19
    +    RULE + MECHANISM DEFERRED    5     Amendments M, N, O, P and Rule 20
    +    RULE-ONLY                    1     Rule 21
    +    -----------------------------------
    +    principles adopted           7     covering 13 source items
    +
    +**FIVE OF THE SEVEN ARE DEFERRED, AND THAT NUMBER IS THE POINT OF THIS
    +RECORD.** **A rule marked `MECHANISM DEFERRED` prevents nothing by itself.**
    +It records what should happen and relies on an author remembering to do it.
    +**The debt these rules were written from is not paid by their adoption**;
    +`C-b` and `C-c` are the rest of it, and the deferred count is the size of
    +what they still owe.
    +
    +**Two of the deferred obligations are fully specifiable inside the repository
    +and are registered nowhere**: the review-digest comparison of Amendment N(b),
    +and the line-survival check of Amendment P(b). **Amendment O(a)'s missing
    +enforcement is registered as `C2`.** The remainder are named in their own
    +amendments.
    +
    +**What this rule set does NOT cover.** **It covers the observed failures and
    +is silent about the unobserved ones.** The classification it comes from is a
    +list of what was noticed across one working session, and several of its items
    +were found only because a later task tripped over them. **A list assembled by
    +noticing is not a survey**, and the absence of a rule here is not evidence
    +that the corresponding failure cannot occur.

---

## 9. Rule and amendment counts — A8, MEASURED

    numbered rules      before 18      after 21      +3
    new rule numbers    19, 20, 21     contiguous from 19, no gap
    full sequence       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

    amendment letters   before  A B C D E F G H I K L        11
                        after   A B C D E F G H I K L M N O P   15      +4
    Amendment J         0 occurrences — none created

**Both grew by exactly the number A6 reports: three new rules and four new
amendments.**

**The pre-existing eighteen rules and eleven amendments are all still
present**, verified by extracting every `### ` heading and every
`**Amendment X,` heading from the base file and checking each appears
verbatim in the new one: **18 of 18 and 11 of 11, zero missing.**

---

## 10. `E2`'s sentence — A9, MEASURED

**Adopted verbatim. Diffed against two independent sources**, not one:

    from the SPECIFICATION §5   Artifact-state labels and statement-kind labels are distinct
                                vocabularies; an artifact-state label does not need to appear
                                in the statement-kind vocabulary.
    from the CLASSIFICATION E2  (identical)
    adopted in Rule 21          (identical)

    specification == adopted    True
    classification == adopted   True

**They correspond.** The sentence is carried in Rule 21 as a block quotation
attributed to the PI ruling, with the surrounding text explaining the two
vocabularies but not restating the ruling in other words.

---

## 11. `B4`'s open question — A10, DECIDED

**The choice: EVERY AFFECTED CHECK is re-run, not only the failing one.**

**Rule 20 states it and gives the reason:** an amend changes the commit
object and therefore its identifier, and every property computed over a range
ending at or containing that commit was measured against an identifier that
no longer exists. **Re-running only the check that failed would leave the
other results true of a superseded state** — which is the defect class
Amendment M was written to prevent, so deciding it the other way would have
put two clauses of this same task in tension. **The cost of re-running all of
them is seconds.**

**The sentence stating that the ratified instance did not settle it, as
adopted in Rule 20:**

> **The ratified instance did not settle this.** Its executor re-ran all
> affected checks voluntarily, and a voluntary act is not a precedent.
> **Recording it as though it were would be the substitution Amendment N(b)
> guards against, in a different currency.**

**The distinction matters because the ratification was of one instance.** An
executor doing more than its criterion required is evidence about that
executor, not a rule. **Reading it as settled practice is how an unwritten
convention acquires false provenance.**

---

## 12. Scope, protected paths, gates — A11, A12, A13

### 12.1 A11 — scope

**MEASURED at commit 3:**

    M  CONVENTIONS.md
    A  reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md
    A  specs/2026-08-14T1241Z_conventions-consolidation-ca.md

    additions 2   modifications 1

**INTENDED at commit 4:** 3 additions and 1 modification — the three above
plus `reports/2026-08-14T1241Z_conventions-consolidation-ca.md`, giving the
manifest's four paths. **`CONVENTIONS.md` is the only file this task
changes.**

### 12.2 A12 — protected paths, MEASURED

    paths existing at the evidence base          389
    excluded (CONVENTIONS.md, the one modified)    1
    compared                                     388
    differing                                      0

    scripts/      0 differing        GATES.md                   2b3bd5069414f009e1a0466c4990db2949519bd8   IDENTICAL
    tests/        0 differing        DECISION_LOG.md            d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2   IDENTICAL
    results/      0 differing        docs/BRANCHING_POLICY.md   3f0f35d4da448eb444d223fd003a5b0601792dc3   IDENTICAL
    derivations/  0 differing

### 12.3 A13 — gate invariants, MEASURED

    1.  ^## P2- section count          14
    2.  P2-PHASE-01                    Status: PROPOSED        (GATES.md line 973)
    3.  prerequisites                  ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                       ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                       zero occurrences of "### Unsatisfied prerequisite"
    4.  pins                           2 found, both MATCH
                                         line 1017  derivations/P2-PHASE-01_microscopic_parameter_domain.md
                                         line 1040  derivations/P2-PHASE-01_input_admissibility_contract.md

**All four reported. `GATES.md` is blob-identical to the evidence base**, so
no gate, gate status, prerequisite state or pin changed.

### 12.4 A13 — is `CONVENTIONS.md` pinned? VERIFIED, not assumed

**This matters because a task that modified a pinned file would owe a re-pin
— and this task modifies `CONVENTIONS.md`.**

    'CONVENTIONS' references in GATES.md        13
    pin-bearing lines in GATES.md               1017, 1040 — two, and only two
    pin at 1017: is CONVENTIONS named within the 5 lines above it?    False
    pin at 1040: is CONVENTIONS named within the 5 lines above it?    False
    any pin line itself naming CONVENTIONS                            False

**`CONVENTIONS.md` is referenced thirteen times and pinned by neither pin.**
**This task therefore owes no re-pin**, and Rule 19 — which this task
writes — requires exactly this to be established by measurement rather than
assumption. **It was.**

---

## 13. The checker — A14, MEASURED at commit 3

    base   bec0117168144d54fb23338b673cf7a7e4771868
    head   e8308d3d3f7a284fabb4d02f1f724a396c4d5002   (commit 3)

**Both prospectivity readings for each of the two runs, so four invocations.
All four exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 a3340ae9d94befb962faa678e8d8992e405f7b9f62ac701d3cab5bc3a74553b1
    run 1 EXCLUSIVE   exit 0   PASS   sha256 b2d04e882cd77ebedd7fe15254645f7d525d088cbed64e9a4457f58fb6b47e1d
    run 2 INCLUSIVE   exit 0   PASS   sha256 a3340ae9d94befb962faa678e8d8992e405f7b9f62ac701d3cab5bc3a74553b1
    run 2 EXCLUSIVE   exit 0   PASS   sha256 b2d04e882cd77ebedd7fe15254645f7d525d088cbed64e9a4457f58fb6b47e1d

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

`P5` is `NOT_APPLICABLE` because the range contains no merge; `P9` because it
adds no report — the report is commit 4.

### 13.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "head": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "head": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
      "specification_paths": ["specs/2026-08-14T1241Z_conventions-consolidation-ca.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A14.** **`append_only_paths` is `["DECISION_LOG.md"]` and not
`[]`**, so `P3` is live. **`authorised_modified_gates` is `[]`, and here that
is truthful: no gate may change.** **The config was never adjusted to make
RUN 2 pass; it passed on its first invocation.**

### 13.3 The measured RUN 1 subject set

**RUN 1's default selection chose one specification:**

    specs/2026-08-14T1241Z_conventions-consolidation-ca.md
      "stated: 3 additions, 1 modification"
      stated add 3 modify 1   counted add 3 modify 1   parse OK

**The same single path RUN 2 names explicitly**, so the two runs' outputs are
byte-identical at each prospectivity reading — the digests above are equal in
pairs. The two readings differ in exactly one line and in no verdict:

    224c224
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

**`P1` compares per category** — `stated add 3 modify 1` against `counted add
3 modify 1` — which is the declared-total grammar landed one task ago doing
its work on the specification that writes the rule requiring it.

### 13.4 `P7`, and the section count it saw

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []   removed_sections  []

**`PASS` at fourteen sections. `PASS` at zero would have been a STOP.**

### 13.5 RUN 1 output, verbatim

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "counted": 4,
              "counted_add": 3,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "specs/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T1241Z_conventions-consolidation-ca.md",
              "stated": 4,
              "stated_add": 3,
              "stated_modify": 1,
              "stated_record": "stated: 3 additions, 1 modification"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "829442de6029f233b1f3b1c2a2ab9f816cd0af5d",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
                "work_paths": [
                  "CONVENTIONS.md"
                ]
              }
            ],
            "first_review_commit": "829442de6029f233b1f3b1c2a2ab9f816cd0af5d",
            "first_work_commit": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": [
            {
              "base_bytes": 89541,
              "base_is_byte_prefix_of_head": true,
              "commits_with_deletions": [],
              "deleted_lines_base_to_head": 0,
              "head_bytes": 89541,
              "path": "DECISION_LOG.md",
              "status": "PASS"
            }
          ],
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "829442de6029f233b1f3b1c2a2ab9f816cd0af5d",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09",
            "first_commit_paths": [
              "specs/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 14. Validators — A15, MEASURED

    before, at the evidence base bec0117…    310 passed, 2 deselected
    after,  at commit 3 e8308d3d…            310 passed, 2 deselected     exit 0

**Unchanged, as A15 expects: this task adds no test.** **No change to
explain.**

**The "before" figure was measured** by checking out the evidence base in a
separate worktree and running the suite there, **not quoted from the previous
task's report** — §12 of the specification records that its own 310 was
quoted and requires it re-measured. **It re-measured to the same number.**
The temporary worktree was removed.

---

## 15. Commits — A16, MEASURED for commits 1–3

    commit 1   4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09   specs/2026-08-14T1241Z_conventions-consolidation-ca.md
    commit 2   829442de6029f233b1f3b1c2a2ab9f816cd0af5d   reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md
    commit 3   e8308d3d3f7a284fabb4d02f1f724a396c4d5002   CONVENTIONS.md

    UTC token fixed by commit 1:  1241Z        day at execution: 14

**Stored subjects, MEASURED:**

    commit 1   spec: C-a, consolidate twelve observed failures into durable conventions
    commit 2   review: pre-execution review for C-a, conventions consolidation
    commit 3   conventions: C-a, consolidate thirteen governance items into seven principles

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |

**Commit 4's message, INTENDED:**

    report: C-a lands seven principles covering thirteen governance items

**Commit 4 is post-report evidence. Nothing in this report measures it.**

**`F1`, met and unrepaired.** My harness's standing git guidance instructs a
`Co-Authored-By` trailer and a session URL. Each message was composed without
them at first writing; no commit was amended and no history was rewritten.
**`P6` reports `PASS` on all three commits in every one of the four checker
invocations.**

**Note on Rule 20, which this task writes.** Rule 20 would have permitted an
amend had a trailer reached a commit. **It did not, and Rule 20 is in any
case not operative for this task** — §10 of the specification records that
rules bind prospectively from their landing, and this branch has not landed.
**No amend was made and none was needed.**

---

## 16. Rule 16 assessment — all three junctions

### 16.1 First — a rule marked DEFERRED prevents nothing by itself

**After this lands, `CONVENTIONS.md` carries rules covering twelve failures
that previously had none. A reader may take that for the failures being
prevented. It is not.**

**MEASURED, and the count is the point:**

    RULE + MECHANISM EXISTS      1     Rule 19 — tests/test_gate_pins.py
    RULE + MECHANISM DEFERRED    5     Amendments M, N, O, P and Rule 20
    RULE-ONLY                    1     Rule 21

**Five of the seven principles are `MECHANISM DEFERRED`.** **A rule so marked
records what should happen and relies on an author remembering to do it.**
**That count is the size of what `C-b` and later work still owe**, and it is
stated in `CONVENTIONS.md` itself — in the consolidation record — so a reader
finds it from the adopted text rather than from this report.

**Two of the five are fully specifiable inside the repository and are
registered nowhere:** Amendment N(b)'s review-digest comparison, and
Amendment P(b)'s line-survival check. **Amendment O(a)'s missing enforcement
is registered as `C2`.** **The remaining gaps — M's measurement-scope lints,
O(b)'s reading-list obligation, Rule 20's recording and re-run obligations —
are named in their own text and are likewise unregistered.** **Registering
them is `C-c`'s, and this task does not do it.**

### 16.2 Second — the machines were not idle, and the accurate form matters

**The observed governance failures were not all prevented by existing
mechanisms — but some underlying violations WERE mechanically detected.**

**`B4` is the counterexample and it is concrete:** the commit-hygiene
violation that occasioned the ratified amend **was caught by the checker at
exit 2**, on an unpushed commit, before any publication. **A machine found
it.**

**What the machines did not do is identify, interpret or repair the
GOVERNANCE GAP.** `P6` reported a forbidden trailer; it did not observe that
the harness would supply one on every future task, that no rule permitted the
repair, or that the permission needed conditions. **Each of those came from
human review or re-measurement.**

**An earlier version of the specification's §7 said none of the underlying
violations was caught by a machine.** **`B4` refutes it**, and the claim
appeared in the section warning against statements whose scope exceeds their
evidence — the discipline Amendment M now carries. **The accurate form is the
one above: detection of a violation and identification of a gap are different
acts, and only the first was mechanical.**

**And writing a rule down is not detection.** **Seven principles now exist
where none did; not one of them observes anything.** Six of the seven rely
entirely on an author or reviewer applying them, and the seventh relies on a
suite someone must run.

### 16.3 Third — the rule set covers what was noticed, not what exists

**The classification these rules come from is a list of what was noticed, not
a survey.** It records twenty-four items gathered across one working session,
and **several were found only because a later task tripped over them** —
`A7`'s reading-list gap surfaced because an executor found evidence outside
its own reading list; `B3`'s insufficiency surfaced because an executor
measured beyond its criterion.

**So the seven principles cover the observed failures and are silent about
the unobserved ones.** **The absence of a rule here is not evidence that the
corresponding failure cannot occur** — it is evidence that nobody has yet
tripped over it and written it down. **That sentence is carried in the
consolidation record in `CONVENTIONS.md`**, so the limit travels with the
rules rather than only with this report.

**A search I did not perform.** I did not attempt to derive additional
failure modes from first principles, and this task was not scoped to. **The
rule set's completeness is exactly the classification's completeness, which
the classification itself declines to claim.**

---

## 17. Did writing these rules make me want to write the mechanism?

**Yes — twice, specifically, and I wrote neither.**

**Amendment N(b), the review-digest comparison.** While writing it I could
see the whole check: read the review blob, extract the digest after
`reviewed specification SHA-256:`, hash the specification blob committed by
the same task, compare, fail on mismatch. **Both artifacts are already
committed at frozen paths and the checker already resolves blobs at a
revision.** It is perhaps thirty lines and it would have closed a gap that
has already admitted two stale-specification reviews. **I did not write it.**
§6 of the specification reserves mechanisms to `C-b`, and a checker property
written inside a prose task would be exactly the half-done shape the
classification warns about — landing without the fixtures and review a
mechanism needs.

**Amendment P(b), the line-survival check.** Same pull, stronger: **I have
run this measurement by hand, in a previous task, and it is the reason `B3`
exists as an item.** I know its inputs are all available to the checker.
**I did not write it.**

**I confirm that no code, test, checker property or parser change was made by
this task.** **MEASURED:** `scripts/`, `tests/`, `results/` and
`derivations/` are each 0 paths differing between the evidence base and
commit 3, and the whole changed-file set is `CONVENTIONS.md` plus this task's
own two records.

**The temptation is itself the argument for the marker discipline.** An
executor who can see the mechanism is the executor most likely to describe
the rule as though the mechanism existed. **`DEFERRED` is what stops that**,
and it is why five of seven carry it.

---

## 18. Stops and clarifications

### 18.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's two digests matched; A2's review names the executed digest;
A3's matrix has thirteen rows with no empty row and no duplicate; A4 found
every principle carrying exactly one marker; A7's deleted-line count is zero;
A13 shows `GATES.md` unchanged; A14's RUN 2 exited 0 with `P7` at fourteen
sections. **§4's "if you judge a third form is needed, STOP" did not
trigger** — every principle is an amendment or a numbered rule; §7.1 records
the one non-principle placement decision and flags it for overrule rather
than treating it as a third form.

### 18.2 Secondary findings

**S1 — `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, reported not decided.**
**Two of the missing enforcements this task names are registered nowhere.**
The classification's mechanism bucket runs `C1`–`C5` and covers the
gate-heading grammar, the `stated:` requirement, declared-set supply,
cross-document consistency and the vacuous-guard regress. **It does not cover
the review-digest comparison (Amendment N(b)) or the line-survival check
(Amendment P(b))**, both of which are fully specifiable inside the repository
and neither of which has an item. **I named the gap in each amendment's text
and assigned registration to `C-c`. I did not register them**, because §6
forbids this task from registering `D1`–`D4` and creating new mechanism items
would be the same act on the other side of the ledger. **`C-c` should be told
its list has grown.**

**S2 — observation, sharpening rather than correcting §2.** `P1` does not
merely parse `stated:`; it **refuses** a scope block that lacks one,
returning `NOT_PARSEABLE`. The assignment stays `DEFERRED` for a sharper
reason — the refusal is opt-in — and Amendment O(a) states it in that form.
**§6 gives the measurement.**

**S3 — the eighteen rule titles in §4 of the specification reproduce the
file.** I read them from `CONVENTIONS.md` rather than from the specification
before deciding placement, as §4 instructs, and they correspond. **No
discrepancy to report.**

**F1 and F2.** `F1` — the harness's forbidden trailer — **met and
unrepaired**, §15. `F2` — the `frozen Wilson D` docstring — **not met in this
task's reading**, and `scripts/` is 0 paths differing, so it stands
unrepaired where it was.

### 18.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule or with another instruction.** Four observations:

1. **§3 asks for the matrix "in the adopted text or immediately beside it",
   while §4 makes a third structural form a STOP.** For a table that is not a
   principle the two clauses leave a small gap, and §7.1 records how I read
   it. **I would have specified where a non-principle record goes**, since
   the matrix is the specification's own instrument for making set-review
   possible.
2. **A15 says "before and after" without naming the two revisions.** I read
   them as the evidence base and commit 3 and measured both. **§12 of the
   specification is admirably explicit that its own 310 was quoted and not
   measured**, which is the practice Amendment M(a) now requires — and it is
   worth noting that the specification applied the rule to itself before the
   rule existed.
3. **§2's four known assignments were worth checking and one was worth
   sharpening.** The instruction to "verify rather than assume" produced a
   real refinement on `A1`. **I would keep it.**
4. **The candidate grouping is offered as replaceable and I replaced part of
   it.** §4.1 gives the reasons. **The instruction to say why, rather than to
   follow or ignore silently, is what made the regrouping reviewable** — a
   specification that had frozen the seven groups would have got a worse set
   and no record of the disagreement.

### 18.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carries two such orders, a known open item;
I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 19. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13, A15 and A16 for
commits 1–3; A14's four invocations with both configs and the JSON output;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A11's final scope
of 3 additions and 1 modification.

**Post-report evidence, returned to the Reviewer and NOT written back:**
A11's final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at
commit 4; A15 at commit 4; A16 for commit 4; the push; the branch tip read
back.

**Nothing in this report claims to measure commit 4.**

**`main` was not touched, nothing was merged, and no branch was deleted.**
**Integration is a separate task**, and this report authorises none of it.
