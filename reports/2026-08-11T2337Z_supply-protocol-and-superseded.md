# Task report — the review supply protocol, and a superseded-branch attribute

Specification:        `specs/2026-08-11T2337Z_supply-protocol-and-superseded.md`
Pre-execution review: `reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md`
Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`
Branch:               `governance/supply-protocol-and-superseded`
Pre-report head:      `c2c5471d373385c840f5ee37c37441a8f14a9b39`
UTC token `{HHMM}Z`:  `2337`, fixed by commit 1; `XX` = `11`

**Headline for the Reviewer, stated before the evidence.** **Rule 18,
applied to this task's own review supply, was NOT sufficient.** Its
blank-line clause worked exactly as designed and removed a decision that
would otherwise have been silent. **Its complete-line matching did not
resolve the shared-line mode** — it converted a silent mislocation into a
detectable no-match, which is an improvement and not a resolution — **and
a boundary judgement remained, of the kind Rule 18's own text forbids.**
§8 states this precisely, names the missing clause, and records that I
proceeded rather than stopped, and why.

---

## 1. A1 — Pinned inputs, verified before use

Method as specified: `git cat-file blob <rev>:<path> | sha256sum`, at
`0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`.

```
=== A1: CONVENTIONS.md ===
e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451  -
expected e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451
=== A1: docs/BRANCHING_POLICY.md ===
0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9  -
expected 0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9
```

**Both match. No STOP.** Verified before the worktree was created and
before either file was read for editing.

## 2. A11 — Branch only

```
=== A11-1: local main ===
0f7961747abe2a18b436c0b1e5b928f425ea4d9a
=== A11-2: refs/remotes/origin/main (before fetch) ===
0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
=== fetch main ===
From https://github.com/zetacheng/2-emergent-gravity
 * branch            main       -> FETCH_HEAD
=== A11-2: refs/remotes/origin/main (after fetch) ===
0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
=== A11-3: remote refs/heads/main via ls-remote ===
0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5	refs/heads/main
```

All three reported, as required:

    refs/remotes/origin/main      0ab6369a…   == evidence base
    remote refs/heads/main        0ab6369a…   == evidence base
    local refs/heads/main         0f796174…   STALE BY DESIGN, not repaired

**Local `main` is stale by design and was not touched.** No `main` ref
was moved. The branch was created from the evidence base:

```
Preparing worktree (new branch 'governance/supply-protocol-and-superseded')
HEAD is now at 0ab6369 docs: report the landing of the diquark line
=== head ===
0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
governance/supply-protocol-and-superseded
=== dirty count ===
0
```

**No branch was deleted.** No PR, no force-push, no history rewrite, no
merge into `main`.

## 3. A0, A12 — Commit order, paths, and message hygiene

    commit 1  51dcbfc4eba0c6244a88437e50509c192ada41cd
              A specs/2026-08-11T2337Z_supply-protocol-and-superseded.md
    commit 2  0804dbf7104c93ab7c9be4261d0e45dde18672c9
              A reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md
    commit 3  c2c5471d373385c840f5ee37c37441a8f14a9b39
              M CONVENTIONS.md
              M DECISION_LOG.md
              M docs/BRANCHING_POLICY.md

**Commit 2 precedes the work, per Rule 15.** The order and the paths are
the specification's; no path was chosen by me.

Blob identities at the pre-report head:

```
CONVENTIONS.md                    blob=030126ac0b6d54df2cfeecf37fc78d04b32c9fdc
  sha256=3b6a53c538768bec3d3ac7ae7d0cbd30fe9b66e22efea6fcf376e13507e2fa66
docs/BRANCHING_POLICY.md          blob=04aae373a9876c2613ba3e95a890558b33456092
  sha256=a95b00e45f15d0d2b8bc198285625aeb7c5d58452b0c272c226087d8ff0329ab
DECISION_LOG.md                   blob=6d0c9578e2f62cb197ff46e1b76767e09027e061
  sha256=ac20a351bef3b13334b4ab99743e26c0423d9696ea71ee5e49ac35fd73573444
specs/…2337Z_supply-protocol-and-superseded.md
                                  blob=856fd557cc48e0b7d7991fe683a5b0ee91a66de5
  sha256=98a1edfb50c9c9956784219148970f6e87b2a03226b6ec3bab434ff41171f3f8
reviews/chatgpt/…2337Z_supply-protocol-and-superseded.md
                                  blob=81de299078d381294b4f52b8d2a85915d8731c4f
  sha256=3f15d0c9992a14a312d01efe6af839765a76d542adb28f7135b5db8b4ef5d187
```

The committed specification is byte-identical to the file supplied with
the task: both sides measure
`98a1edfb50c9c9956784219148970f6e87b2a03226b6ec3bab434ff41171f3f8`.

### A12 — per commit, proposed message before and stored message after

**Method.** The exact proposed message was written to a file and scanned
before committing; the stored message was then read back from the commit
object and scanned again. Scan pattern:
`co-authored-by|claude-session|generated with|noreply@|https?://|opus|sonnet|anthropic`,
case-insensitive.

    commit 1   proposed scan: none found      stored scan: none found
               trailers suppressed: NONE — none was produced
    commit 2   proposed scan: none found      stored scan: none found
               trailers suppressed: NONE — none was produced
    commit 3   proposed scan: none found      stored scan: none found
               trailers suppressed: NONE — none was produced

**No trailer was suppressed on any commit, because none appeared.** No
`Co-Authored-By`, no session identifier or URL, no tool attribution, at
either the proposal or the stored stage. Commits were created with
`git -c commit.gpgsign=false commit -F <file>`; the repository carries no
`commit.template` and no `core.hooksPath`, so nothing was configured to
add a trailer. **No persistent user or global configuration was
changed** — the setting was passed per invocation.

Stored message of commit 3, read back from the object:

```
governance: add Rule 18 review supply protocol and a SUPERSEDED branch attribute

Rule 18 fixes how a pre-execution review reaches the executor: complete-line
delimiter matching, the committed artifact is all text strictly between the
delimiters, at most one leading and one trailing blank line stripped as
transport artifacts, instructions and preamble outside the block. Rules 1-17
are unchanged and unrenumbered.

docs/BRANCHING_POLICY.md gains SUPERSEDED as an attribute orthogonal to the
deletion states, with a register of three branches. The Stage-1 deletion
machine and its closed count identity are byte-identical.

DECISION_LOG.md records both additions as prospective, and records the one
branch examined and left out of the register pending PI authority.
```

**Intended commit 4 message**, inspected at authoring time. Its
authoring-time scan under the same pattern: **none found; no trailer to
suppress.** The stored message is post-report evidence.

```
docs: execution report for the supply protocol and superseded attribute

Records A1-A12 raw output, A4's body comparison of rules 1-17, A5's
before-and-after of the deletion state machine, the full enumeration
and classification of all 48 remote branches, and the finding that
Rule 18's complete-line matching did not resolve the shared-line
supply mode on its first live application.
```

## 4. A2 — This task's pre-execution review, committed unedited

Committed at
`reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md`,
SHA-256 `3f15d0c9992a14a312d01efe6af839765a76d542adb28f7135b5db8b4ef5d187`,
byte-identical to the text extracted from the delimiter block:

```
3f15d0c9992a14a312d01efe6af839765a76d542adb28f7135b5db8b4ef5d187  (extracted block)
3f15d0c9992a14a312d01efe6af839765a76d542adb28f7135b5db8b4ef5d187  (committed file)
```

122 lines, 7732 bytes. **Nothing was authored, edited, summarised or
reformatted.** The extraction procedure and its residual judgement are in
§8, which is the substantive answer A2 asks for.

## 5. A3 — Rule 18 added, and quoted in full as landed

Added as a new `### 18.` section after Rule 17. Heading positions after
the edit:

```
923:### 15. Governing artifacts are committed
943:### 16. Accumulated reading
982:### 17. Integrations do not add epistemic or governance classifications
992:### 18. Review supply protocol
```

`CONVENTIONS.md`: 990 lines → 1030 lines. Delimiter literals present at
lines 998–999; the blank-line clause at line 1010. Neither string
occurred in the file before this task (`REVIEW ARTIFACT`: 0 occurrences
at the base). The heading carries no trailing period, matching rules
1–17; the specification's draft heading showed one.

**Rule 18 as landed, quoted in full:**

> ### 18. Review supply protocol
>
> **A pre-execution review is supplied to the executor between two
> delimiter lines whose exact text is stated in the specification that
> requires the review.** The delimiters are:
>
>     === REVIEW ARTIFACT BEGINS ===
>     === REVIEW ARTIFACT ENDS ===
>
> **Matching is by COMPLETE LINE, never by first occurrence of the
> delimiter string.** A specification that states a delimiter contains it,
> as does any instruction accompanying the supply; **a substring search
> will find those instead of the boundary.**
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

## 6. A4 — Rules 1–17 unchanged, by body comparison

**Heading equality is reported as a proxy, and the body comparison is
reported as the measure.**

Method: locate the single occurrence of `### 18. Review supply protocol`;
remove from the blank line preceding it to end of file, keeping the
single newline that terminated Rule 17; digest the remainder.

```
base bytes: 53250  sha256: e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451
new  bytes: 54967  sha256: 3b6a53c538768bec3d3ac7ae7d0cbd30fe9b66e22efea6fcf376e13507e2fa66
Rule 18 heading occurrences: 1
stripped bytes: 53250  sha256: e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

A4 RESULT — rules 1-17 byte-identical after removing the Rule 18 section: True
byte-length delta of the Rule 18 section: 1717

A4 heading proxy — base rule headings: 17  new: 18
base headings identical to the first 17 of new: True
the single new heading: ['### 18. Review supply protocol']
```

**The body comparison is exact**: with the Rule 18 section removed, the
file's SHA-256 is `e3afa521…`, which is A1's pinned digest. **Rules 1–17
are byte-identical, not merely equal in their headings.** No rule was
renumbered, reworded or reordered; the addition is 1717 bytes appended
after Rule 17.

## 7. A5 — The superseded attribute and register

Placed as a new `## Superseded branches` section **immediately after
`## Deletion authorization states`**, so that a reader meets "this is not
a fourth state" adjacent to the closed three-state machine it disclaims.
Amendment K contemplated exactly this choice — "Either that state is
added or this prohibition is stated where an integrator will meet it" —
and this is the second option.

```
=== section headings after the edit ===
3:## Branch names
13:## Rules
24:## Branch lifecycle
66:## Deletion authorization states
104:## Superseded branches
172:## Remote refs are the sole deletion authority
```

`docs/BRANCHING_POLICY.md`: 129 lines → 196 lines.

### A5's before and after for the deletion state machine

**BEFORE**, `## Deletion authorization states` at the evidence base:

`````
## Deletion authorization states

**Deletion authorization has three Stage-1 outcomes, and every listed
branch reaches exactly one:**

```text
present on remote,  verified_merged true   -> PENDING_DELETE
present on remote,  verified_merged false  -> NOT_AUTHORIZED      (terminal)
listed, absent from remote                 -> ABSENT_FROM_REMOTE  (terminal)
```

**Stage 2 acts on `PENDING_DELETE` entries and no others.**
**Stage 3** resolves `PENDING_DELETE` to `DELETED` or `SKIPPED`;
`NOT_AUTHORIZED` and `ABSENT_FROM_REMOTE` entries are left exactly as
they are.

**`verified_merged` is `n/a` for an `ABSENT_FROM_REMOTE` entry.** With
no tip there is no ancestry to test, and recording `true` or `false`
would assert something that does not exist.

**The counts satisfy a closed identity, which is machine-checkable:**

```text
listed_count = pending_delete_count
             + not_authorized_count
             + absent_from_remote_count
```

**Report the identity as an equation with its arithmetic, not as a
claim.** Its purpose is that a mis-stated entry shows up as a number
that does not add up.

**The two terminal states are not interchangeable.** `NOT_AUTHORIZED`
means present but not eligible; `ABSENT_FROM_REMOTE` means there is
nothing to delete. A branch in the second state may be pushed later and
would then be assessed afresh; a branch in the first will not become
deletable by anything happening on the remote.
`````

    bytes 1435   sha256 dced093f6baa1bd1da2155ad360000209aaa42626ed633aac7df53406d210ca2

**AFTER**, the same section at the working head: **identical byte for
byte**, same 1435 bytes, same digest `dced093f…`. The extracted text is
reproduced above once rather than twice; the machine result is:

```
A5 RESULT — deletion state machine section BYTE-IDENTICAL: True

  literal 'PENDING_DELETE'                       base_count=3   new_count=3
  literal 'NOT_AUTHORIZED'                       base_count=3   new_count=4
  literal 'ABSENT_FROM_REMOTE'                   base_count=4   new_count=4
  literal 'listed_count = pending_delete_count'  base_count=1   new_count=1

closed-identity block byte-identical: True

  ## Branch names                                    identical=True
  ## Rules                                           identical=True
  ## Branch lifecycle                                identical=True
  ## Deletion authorization states                   identical=True
  ## Remote refs are the sole deletion authority     identical=True
```

**Every pre-existing section is byte-identical.** **No fourth deletion
state was added** and the closed count identity is untouched.

**`NOT_AUTHORIZED` gains one occurrence, and it is mine**, in the new
section's orthogonality sentence: the register's three entries are each
present-on-remote and unmerged, so each is `NOT_AUTHORIZED` for
deletion. That is a use of the existing state, not a new one, and it is
reported here because a bare count would otherwise look like a change to
the machine.

### The superseded section, quoted in full as landed

> ## Superseded branches
>
> **A branch is SUPERSEDED when its work has been re-issued or replaced
> and it is preserved as evidence rather than for integration.**
>
> **A superseded branch MUST NOT be integrated.** Its content may remain
> correct — supersession is about integrability and task identity, not
> about correctness — **but the authoritative instance is the branch that
> replaced it.**
>
> **This is an attribute, not a deletion state.** A superseded branch
> still reaches exactly one Stage-1 deletion outcome, and the closed count
> identity above is unchanged. **The two questions are independent:
> whether a branch may be deleted, and whether it may be integrated.**
> Each entry below is present on the remote and unmerged, so each is
> `NOT_AUTHORIZED` for deletion; that is its deletion outcome, and it says
> nothing about integrability.
>
> **Supersession is recorded in the register below**, naming the branch,
> its commit, what replaced it, and why. **A Git ref carries no such
> marker, so the register is where it lives.**
>
> **The register:**
>
>     fix/pi-decisions-and-deferred @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
>       superseded by  fix/pi-decisions-v2, then fix/pi-decisions-v3
>       reason         re-issued on a clean branch after the second
>                      execution overwrote the first execution's pushed
>                      records on the same branch
>       content        the substantive content was approved; the
>                      representation was not
>
>     fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36
>       superseded by  fix/pi-decisions-v3
>       reason         stale base: main advanced through two governance
>                      landings and the branch lost conflict-free
>                      integrability
>       content        APPROVED and unchanged; only its integrability
>                      lapsed
>
>     gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192
>       superseded by  gate/p2-land-diquark-line-v2
>       reason         the specification stated an impossible merge-base
>                      and the executor STOPPED at the pre-merge guard;
>                      the re-issue corrected the value
>       content        the branch carries a report of the stop and NO
>                      merge; it is the record of a correct refusal, not
>                      of failed work
>
> **The third entry differs in kind from the first two and the register
> does not flatten that.** The first two carry approved work that was
> re-instantiated elsewhere. **The third carries no work at all** — its
> specification was defective, the executor stopped before any tree
> changed, and **what it preserves is the evidence that a stop happened
> and why.** **Supersession covers both; the register records which.**
>
> **Entry threshold.** **A branch is added to this register only where a
> durable repository artifact explicitly records its re-issue, replacement
> or supersession and identifies the replacement or the reason.** **Naming
> similarity, age, Git topology, or the mere existence of a later branch
> do NOT suffice**, singly or together. **Where evidence suggests
> supersession but does not establish it, the branch is left out pending a
> PI decision** and the evidence is reported. **Finding the artifact that
> already records a supersession is an observation; classifying a branch
> as superseded is a decision.**

**The entry threshold is landed in the file, not only in this report.**
The specification stated it as a rule for me; a register whose threshold
lives only in an execution report cannot be applied by the next task.

## 8. A2's substantive answer — was Rule 18 sufficient?

**No.** One of its two halves worked; the other did not.

### 8.1 What the supply actually looked like

The message carrying this task's review was measured before anything was
extracted. 125 lines, 7902 bytes.

```
--- substring occurrence counts ---
BEGIN substring: 1
END   substring: 1
--- COMPLETE-LINE matches (Rule 18) ---
BEGIN whole-line indices: []
END   whole-line indices: [124]
--- lines containing the BEGIN substring, shown raw ---
  [0] '@"/root/.claude/uploads/30ed7c63-4aac-52db-8b0d-16eb01e07bca/8c265173-SPEC_supply_protocol_and_superseded.md" === REVIEW ARTIFACT BEGINS ==='
--- lines containing the END substring, shown raw ---
  [124] '=== REVIEW ARTIFACT ENDS ==='
```

**The END delimiter is a complete line, exactly once. The BEGIN delimiter
is not a complete line at all** — the transport prepended the
specification's attachment marker to line 0, and the delimiter shares
that line. **This is the ninth instance of the shared-line mode**, the
one §0 identifies as "the mode a standing rule must fix".

### 8.2 Did complete-line matching resolve the shared-line mode?

**No.** Under Rule 18, complete-line matching yields **zero** BEGIN
candidates. The rule does not locate the boundary; it establishes that
the boundary is not there.

**That is not worthless — it is a real improvement, and it is worth being
precise about what kind.** §0 diagnoses mode 1 as "a first-occurrence
search found the instruction". That diagnosis describes the danger
correctly but locates it in the wrong place for this supply. Here the
BEGIN substring occurs **once**, so a first-occurrence substring search
would have found line 0 and silently taken the text after the substring
— arriving at roughly the right content **by luck, with no signal that
anything was malformed.** Complete-line matching replaces that silent
luck with a loud absence. **A detectable failure is strictly better than
an undetectable near-miss. It is still a failure.**

### 8.3 Did the blank-line clause remove a decision I would otherwise
have made silently?

**Yes — completely, and on its first live use.** The block strictly
between the boundaries was 123 lines. Measured:

```
block lines strictly between: 123
first repr: ''
last  repr: 'No blocking specification defect remains. Execution may proceed subject to the specification’s own pinned-input, branch-state, review-supply, scope, validator and STOP conditions.'
stripped leading: 1  trailing: 0
after strip, first repr: 'Pre-execution review — review supply protocol and superseded-branch attribute'
after strip, last  repr: 'No blocking specification defect remains. …'
residual leading blank remains: False
residual trailing blank remains: False
```

**Exactly one leading blank line was present and was stripped under the
written rule. There was no trailing blank line, so nothing was stripped
there.** No second blank line existed at either end, so the clause's "at
most one" bound was never reached and never had to be adjudicated. **This
is the one byte that seven previous reports flagged as an unwritten
executor choice, and it is now a rule I applied rather than a decision I
made.** 122 lines, 7732 bytes committed.

**This half of the protocol is finished.** It should not be revisited.

### 8.4 Did any text inside the block require me to judge whether it was
instruction?

**No.** The "mechanically authoritative" clause held cleanly:

    occurrences of "REVIEW ARTIFACT" inside the committed artifact   0
    occurrences of "TEXT ONLY" inside the committed artifact         0

The accompanying instruction — the message directing how to respond —
arrived **after** the END line, outside the block, exactly as Rule 18
requires. **No byte inside the block was classified, and none needed to
be.** The earlier draft's semantic test, which the review specifically
praises the removal of, would have had nothing to bite on here; that is
consistent with the removal being right, and is not evidence for it.

### 8.5 The judgement that remained, stated exactly

**I located BEGIN by a rule Rule 18 does not contain.** Precisely: the
unique line whose content, after removing a prefix matching the regular
expression

    ^@"[^"]+"\s+

equals the BEGIN delimiter exactly. Asserted, not assumed — the
candidate set was measured and asserted to have exactly one member, and
END was asserted to be a whole line occurring exactly once.

```
complete-line BEGIN: []   complete-line END: [124]
prefix-stripped BEGIN candidates: [0]
```

**This is a boundary inference, and Rule 18 says "The executor never
infers a boundary."** I disclose it as such rather than presenting it as
compliance. It is the same derived rule I have applied in eight previous
tasks; **its consistency across nine supplies is a fact about my habits,
not a property of the protocol** — which is the same objection §0 raises
against the one supply that succeeded by accident.

### 8.6 Why I proceeded rather than stopped

**None of Rule 18's four literal STOP triggers fired.** Checked one by
one:

    supplied text missing                    NO — 7902 bytes present
    carries no delimiter lines               NO — END is a complete line,
                                             exactly one occurrence
    does not correspond to the specification NO — the review names the
                                             specification, its evidence
                                             base and both pinned digests
    instruction text found inside the block  NO — see §8.4

**What failed is coverage, not a trigger.** Rule 18 does not say what to
do when exactly one of the two boundaries is on a complete line, and its
transport clause is scoped to blank lines with an explicit "No other byte
is removed or normalised" — which forbids the normalisation the supply
requires, without providing an alternative.

**Three things made proceeding the better reading, and I state them so
the PI can overrule them.** A2 asks me to "say in the report whether it
was sufficient", and §7 says "**If any judgement remained, the protocol
is still incomplete and the next task should know**" — both presuppose a
completed report carrying a "no" answer, rather than a stop. Second, the
transport behaviour is deterministic: the attachment marker is prepended
to line 0 of every such message, so a stop here would recur identically
on re-issue and Rule 18 would never land, while the defect it exists to
fix stayed open. Third, the residual risk to the artifact is nil — line
0 minus the marker prefix *is* the delimiter, so there is no competing
boundary to have chosen wrongly, and the committed bytes are the same
under either reading.

**If the PI intended Rule 18 to compel a STOP on a non-complete-line
BEGIN, then this task should have stopped and did not.** That is a ruling
I did not take and am not entitled to take; it is recorded in §12 under
`SPECIFICATION_DEFECT` so it is not buried in prose.

### 8.7 The clause the protocol still needs

Offered as the fix, not as a change I made — **I added nothing to Rule 18
beyond the specification's text.**

> **Transport prefixes.** A delimiter line is matched after removing any
> transport prefix the supply channel prepends to the line — an
> attachment or upload marker of the form `@"<path>"` followed by
> whitespace, and nothing else. **The prefix must be removable by a
> stated pattern, the match must then be EXACT, and the candidate line
> must be UNIQUE**; if two lines qualify, or none, the executor STOPS.
> **The removed prefix is never part of the artifact.** This is a
> transport clause of the same kind as the blank-line clause, and for the
> same reason: the alternative is an executor deciding silently.

**Why a clause and not a sender instruction.** §0's own argument settles
this: "no amount of care by a sender prevents a specification from
containing the delimiter it names." The symmetric point is that no amount
of care by a sender prevents a channel from prefixing line 0. **A
protocol that requires the BEGIN delimiter never to be the first line of
a message is a protocol that depends on the sender's habits** — the exact
failure §0 rejects.

**A second, independent option, and I recommend it alongside the
clause:** put the BEGIN delimiter on a line of its own by never making it
line 0 — a single blank or any preamble line before it suffices, and the
existing rule already requires preamble to be outside the block. That
costs one keystroke per supply and needs no new rule. **The clause is
still needed**, because it is what makes the protocol independent of
whether that keystroke happens.

## 9. A6 — Register membership determined

### 9.1 The three supplied entries, verified

`git ls-remote origin refs/heads/<branch>` is the sole authority, per
`docs/BRANCHING_POLICY.md`.

```
fix/pi-decisions-and-deferred    52f651174dc1fef03b4fb9276078fa1f08d94bd7	refs/heads/fix/pi-decisions-and-deferred
fix/pi-decisions-v2              ebd531ab568aaffabd86a4a94d925a711e62aa36	refs/heads/fix/pi-decisions-v2
gate/p2-land-diquark-line        d64cd912ca9ff78a85787f0e54f345f474cdb192	refs/heads/gate/p2-land-diquark-line
fix/pi-decisions-v3              93de3218095cafdabcd0fda92abc31af33109879	refs/heads/fix/pi-decisions-v3

=== ancestry against main (0ab6369a) ===
52f651174dc1fef03b4fb9276078fa1f08d94bd7      NOT an ancestor of main
ebd531ab568aaffabd86a4a94d925a711e62aa36      NOT an ancestor of main
d64cd912ca9ff78a85787f0e54f345f474cdb192      NOT an ancestor of main
93de3218                                      IS an ancestor of main
```

**All three are present at exactly the stated commits and none is an
ancestor of `main`. No STOP.** The specification's own observations are
reproduced, not relied on.

**`fix/pi-decisions-v3` is an ancestor of `main`** — the surviving
instance of that line, correctly **not** in the register. The
specification's §8 said so and it still holds at execution.

### 9.2 Enumeration of all 48 remote branches

**Two independent methods were run, and they agree.**

**Method 1 — vocabulary search over the whole tracked tree at the
evidence base.** For each of the 48 branch names, every line of every
tracked file containing that name was collected, and each was tested —
first on the line itself, then in a ±6-line window — against
`supersed|re-?issu|replac|abandon|obsolet|withdraw|instead of`,
case-insensitive. **The same-line pass was discarded as unsound as soon
as it was run**: it scored `fix/pi-decisions-v2` at zero, and that branch
is a known register member, so same-line proximity demonstrably misses
real supersessions. The windowed pass is the one reported.

**Method 2 — integration status.** A branch that is an ancestor of `main`
was integrated, so it cannot be "preserved as evidence rather than for
integration". **Topology is used here only to EXCLUDE, never to include**
— §1 forbids the converse, and the register's three members were each
established from artifacts, not from topology.

Result of method 2: of 48 remote branches, 44 are ancestors of `main`
(including `main` itself). **Exactly four are not:**

    fix/pi-decisions-and-deferred      52f65117   register member
    fix/pi-decisions-v2                ebd531ab   register member
    gate/p2-land-diquark-line          d64cd912   register member
    review/role-model-and-executors    10c260b9   EXCLUDED — see §9.4

Full classification of all 48:

| branch | tip | ancestor of `main` | windowed vocab hits | classification |
|---|---|---|---|---|
| `main` | 0ab6369a | yes | — | not a candidate |
| `claude/paper-2-independent-verification-dysdp0` | 5395d4b3 | yes | 2 | integrated; hits are `GATES.md` "Repository branch" fields |
| `concepts/p2-dual-pipeline` | 9ee30ab3 | yes | 0 | integrated |
| `docs/canonical-interaction` | 78872798 | yes | 0 | integrated |
| `explore/p2-phase-01-scalar` | a2ed2af8 | yes | 0 | integrated |
| `fix/branch-deletion-policy` | f2da41ae | yes | 0 | integrated |
| `fix/branch-deletion-policy-amendment` | 1c106372 | yes | 0 | integrated; an amendment to the policy, not a replacement of the branch |
| `fix/exponent-mapping-ruling` | 79399dfd | yes | 0 | integrated |
| `fix/freeze-checker-sign-repair` | 0ab0ca9d | yes | 0 | integrated |
| `fix/integrate-si1-crossref` | 8701a97a | yes | 0 | integrated |
| `fix/normalisation-audit-g-omega` | 9c6ff5b3 | yes | 0 | integrated |
| `fix/pi-decisions-and-deferred` | 52f65117 | **no** | 2 | **REGISTER MEMBER** |
| `fix/pi-decisions-v2` | ebd531ab | **no** | 6 | **REGISTER MEMBER** |
| `fix/pi-decisions-v3` | 93de3218 | yes | 4 | surviving instance; NOT superseded |
| `fix/si1-deferred-02-crossref` | 38302141 | yes | 1 | integrated; hit is an Amendment-H verification record |
| `gate/p2-attraction-ruling-and-layers` | 878b632c | yes | 1 | integrated; hit is a derivation superseding *verdicts*, not a branch |
| `gate/p2-betav-campaign-prereg` | 21efcf85 | yes | 0 | integrated |
| `gate/p2-betav-circ` | ca334fe0 | yes | 0 | integrated |
| `gate/p2-betav-cleanup` | 602569db | yes | 0 | integrated |
| `gate/p2-betav-decomp` | 05a1e7f8 | yes | 1 | integrated; hit is an observed remote SHA record |
| `gate/p2-channel-character` | cb604a4e | yes | 0 | integrated |
| `gate/p2-channel-freeze` | 47e271bb | yes | 0 | integrated |
| `gate/p2-chirality-census` | e4bea1c9 | yes | 0 | integrated |
| `gate/p2-diquark-adjudication` | 3767973b | yes | 3 | integrated by the v2 landing; hits describe that landing |
| `gate/p2-diquark-both-eta` | bc1e5c74 | yes | 4 | integrated by the v2 landing; hits describe that landing |
| `gate/p2-generator-sum-criticality` | 84aad96d | yes | 0 | integrated |
| `gate/p2-governance-amendment` | d63f33b9 | yes | 0 | integrated |
| `gate/p2-grassmann-crossing-sign` | cf4c7895 | yes | 0 | integrated |
| `gate/p2-integrate-chirality-census` | 57c5a6eb | yes | 0 | integrated |
| `gate/p2-land-diquark-line` | d64cd912 | **no** | 9 | **REGISTER MEMBER** |
| `gate/p2-land-diquark-line-v2` | 0ab6369a | yes | 5 | the replacement; integrated, and *is* `main` |
| `gate/p2-lattice-ontology-01` | edb08c2a | yes | 0 | integrated |
| `gate/p2-phase-01-fierz-and-branch-depths` | dca52269 | yes | 0 | integrated |
| `gate/p2-si1-unblock` | c1f1bec2 | yes | 0 | integrated |
| `governance/adopt-rules-8-12` | 75c84226 | yes | 0 | integrated |
| `governance/execution-environment-refinements` | 99aaa0e2 | yes | 0 | integrated |
| `governance/land-amendments-e-to-l` | c58f1b91 | yes | 0 | integrated |
| `governance/land-rules-14-15` | e045ee00 | yes | 0 | integrated |
| `governance/p2-phase-dependency-ruling` | d69bc0f7 | yes | 0 | integrated |
| `governance/rules-8-12-tools` | 376ec62f | yes | 0 | integrated |
| `recover/batch2-gfvec-and-foundations` | 324ef969 | yes | 0 | integrated |
| `recover/betav-complete` | 836bf144 | yes | 0 | integrated |
| `recover/lattice-gravity-engine` | cdcbd840 | yes | 1 | integrated; hit is `MIGRATION.md` text being superseded |
| `review/role-model-and-executors` | 10c260b9 | **no** | 3 | **EXCLUDED — unresolved, see §9.4** |
| `review/role-model-and-executors-clean` | 6fee7ed4 | yes | 1 | the replacement instance; integrated |
| `run/p2-betav-arm-h-decisive` | 9b0ceedf | yes | 1 | integrated; hit is *wording* superseded, and a must-remain-present note |
| `run/p2-betav-arm-p-decisive` | 48c5cc59 | yes | 0 | integrated |
| `sea-ice/gate-stubs` | b02c7027 | yes | 0 | integrated |

### 9.3 Additions to the register beyond the three supplied: none

**I added none.** The three supplied entries are the register's complete
membership as landed.

### 9.4 The one branch I did not add, and why it fell short

**`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb`** — reported as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, named here, **left out of
the register pending PI authority.**

**The evidence I found, which is substantial.** A durable committed
specification, `specs/2026-08-06T1218Z_role-model-clean-rebuild.md`,
titled "rebuild the role-model branch with clean commit metadata", says:

    The reviewed branch `review/role-model-and-executors` @ `10c260b9…`
    was verified … **This task rebuilds it solely to remove undeclared
    commit metadata from history.**

    A new branch reproduces the reviewed source artifacts exactly, EXCEPT
    for the single PI-authorized `AGENTS.md` correction in A4 …
    **The existing branch `review/role-model-and-executors` is preserved
    untouched** as the execution and negative-provenance record.

    - **Do not modify, delete, rename or force-push
      `review/role-model-and-executors`.** It is preserved as the record
      of what happened, including the metadata defect.

It names the replacement (`review/role-model-and-executors-clean`, A0),
names the reason (two tooling-added trailers that "would enter `main`'s
permanent history without review"), and the replacement **is** an
ancestor of `main` while the original is not. `docs/BRANCHING_POLICY.md`
independently records the original as "Permanently preserved … the
unmerged record of a commit-metadata defect, retained as
negative-provenance evidence."

**On its face that satisfies §1's threshold**, and I want to be plain
that this is a close call rather than a comfortable exclusion.

**Why it nonetheless falls short.** §1 draws the line at observation
versus decision: "**Classifying a branch as superseded is a decision;
finding the artifact that already records one is an observation.**"

- **No artifact calls this branch superseded.** The vocabulary search
  found the words "rebuilt", "preserved", "negative-provenance record" —
  never "superseded", and never of this branch.
- **No artifact forbids its integration.** The three register members are
  each covered by Amendment K's explicit "A superseded branch MUST NOT be
  integrated". This episode predates Amendment K (2026-08-06 against
  2026-08-09) and no artifact from it states an integration prohibition.
  That integrating it *would* reimport the defect the rebuild existed to
  exclude is an inference I would be drawing, not a record I would be
  reading.
- **It already carries a different, purpose-built durable disposition** —
  permanently preserved, with its own stated reason. Adding SUPERSEDED
  would be the **first** time that word attaches to it.

**So writing the entry would make me the author of the classification,
not its finder.** §1 provides exactly one instruction for that situation
and I followed it: report the category, name the branch, show the
evidence, leave it out.

**What would settle it, in one line of PI authority:** a ruling that
the clean-rebuild specification's record of a rebuild *is* a record of
supersession for register purposes. **I recommend that ruling** — the
substance is present and the gap is lexical — but it is a decision, and
§2 forbids me to take it. The branch's standing "never deleted or
touched" protection is unaffected either way; **nothing in this task
touched it**, and a register entry would not.

### 9.5 The search, described

Rule 16's discipline applied to the register, as §1 requires:

- **325 tracked paths** at the evidence base were read for the
  vocabulary scan; every tracked file was decoded and searched, not a
  subset.
- **48 remote branch names** were each searched across all of them, at
  both same-line and ±6-line window scope.
- **The same-line method was falsified by its own output** and discarded;
  reported here because a discarded method that is not reported looks
  like a method that was never tried.
- **Every non-zero windowed hit outside the four unmerged branches was
  read in context and is a false positive**, and the false positives fall
  into recognisable kinds: supersession of *claims*, *verdicts*, or
  *wording* (`gate/p2-attraction-ruling-and-layers`,
  `run/p2-betav-arm-h-decisive`, `recover/lattice-gravity-engine`);
  `GATES.md` "Repository branch" fields adjacent to unrelated prose
  (`claude/paper-2-…`); observed-SHA records (`gate/p2-betav-decomp`);
  and descriptions of a *landing* rather than a replacement
  (`gate/p2-diquark-*`). **In no case does supersession language attach
  to a branch as its subject.**
- **Result: no further register members. One unresolved exclusion**, §9.4.

## 10. A7 — `DECISION_LOG.md`, append-only on both measures

Entry added at line 2005:
`## 2026-08-11 — CONVENTIONS.md Rule 18 added; docs/BRANCHING_POLICY.md gains a SUPERSEDED attribute and register`,
in the file's existing format — `Date:` / `Decision owner:` / `Effect:`
header, then `### Decision`, `### Reason`, `### Prospective only`,
`### Consequences`, `### Supersedes`, `### Related gate`,
`### Related branch and files`. 2003 → 2129 lines.

**Measure 1 — against the evidence base:**

```
=== A7 measure 1: append-only against the EVIDENCE BASE ===
126	0	DECISION_LOG.md
(added removed path)
base is an exact byte PREFIX of new: True
base bytes: 82337  new bytes: 88631  appended: 6294
base sha256:   c1366d67f0485da1414d3838d5b42632143cce71b32943c9aedc672b9ebabbde
prefix sha256: c1366d67f0485da1414d3838d5b42632143cce71b32943c9aedc672b9ebabbde
```

**126 lines added, 0 deleted**, and the base version is an exact byte
prefix of the new one — a stronger statement than the line counts, since
it excludes an in-place edit compensated by an equal-length insertion.

**Measure 2 — per commit against its parent:**

```
=== A7 measure 2: append-only PER COMMIT against its parent ===
51dcbfc4eba0  DECISION_LOG.md not touched by this commit
0804dbf7104c  DECISION_LOG.md not touched by this commit
c2c5471d3733  added/removed/path: 126	0	DECISION_LOG.md
```

**Zero deleted lines on both measures.** The entry records both additions
and states that they are prospective, under its own
`### Prospective only` heading.

## 11. A8, A9 — Nothing else touched; scope

### A8, path by path

```
base paths: 325  head paths: 327

ADDED   : ['reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md',
           'specs/2026-08-11T2337Z_supply-protocol-and-superseded.md']
REMOVED : []
CHANGED : ['CONVENTIONS.md', 'DECISION_LOG.md', 'docs/BRANCHING_POLICY.md']

unauthorised additions: NONE
unauthorised modifications: NONE
deletions: NONE

=== A8: named protected files, blob-identical ===
  GATES.md                                                   identical=True  blob=849a4fbfe62d
  AGENTS.md                                                  identical=True  blob=5e60b5fcd6e9
  pyproject.toml                                             identical=True  blob=9fc6fdd196dd
  CLAIMS.md                                                  identical=True  blob=df75ff4de214
  PROGRESS.md                                                identical=True  blob=5ef6e65a1e3f
  MIGRATION.md                                               identical=True  blob=464d4ab5e6ef
  docs/BRANCH_DELETION_RECORD_2026-08-07.md                  identical=True  blob=c91126d39d79
  docs/amendments/2026-08-09_observation-and-propagation.md   identical=True  blob=642b2541571d

=== A8: every base path under the five protected prefixes, path by path ===
  scripts/       base_paths=59   identical=59   differing=0  base-absent_gained=[]
  results/       base_paths=69   identical=69   differing=0  base-absent_gained=[]
  tests/         base_paths=19   identical=19   differing=0  base-absent_gained=[]
  derivations/   base_paths=34   identical=34   differing=0  base-absent_gained=[]
  reviews/       base_paths=20   identical=20   differing=0  base-absent_gained=['reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md']
  total base paths verified under the five prefixes: 201

=== A8: gate status tokens in GATES.md unchanged ===
  base status tokens: 15  head: 15  identical: True
  GATES.md blob identical: True
```

**All 201 base paths under `scripts/`, `results/`, `tests/`,
`derivations/` and `reviews/` are blob-identical, compared individually
rather than by a directory digest.** `reviews/` gains exactly one
base-absent path, the authorised one. **`AGENTS.md` is unmodified**, as
§2 requires. **No gate status changed**; `GATES.md` is blob-identical, so
the status comparison is redundant and is reported as a second
independent check rather than as the primary one. **No test was added** —
`tests/` holds 19 paths at both the base and the head.

### A9 — scope check at the pre-report head, verbatim

Manifest mode `exact`; `mode` must be `exact` or `subset` — a first
invocation with `BRANCH_SCOPE` returned `TOOL_ERROR` exit 3, which is the
tool contract and is reported in §12 as an observation-method correction.

```
{
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "failures": [],
  "head": "c2c5471d373385c840f5ee37c37441a8f14a9b39",
  "mode": "exact",
  "observed_operations": [
    {
      "operation": "modify",
      "path": "CONVENTIONS.md"
    },
    {
      "operation": "modify",
      "path": "DECISION_LOG.md"
    },
    {
      "operation": "modify",
      "path": "docs/BRANCHING_POLICY.md"
    },
    {
      "operation": "add",
      "path": "reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-11T2337Z_supply-protocol-and-superseded.md"
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}
EXIT STATUS: 0
```

**PASS, exit 0.** 2 additions and 3 modifications at the pre-report head;
`forbidden_operations` `delete, rename, copy, type_change, unmerged,
unknown` — none observed.

**Intended final manifest**, identical but for the report path, giving
A9's required **3 additions and 3 modifications**:

```json
{
  "mode": "exact",
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "head": "HEAD",
  "required": [
    {"operation": "add", "path": "specs/2026-08-11T2337Z_supply-protocol-and-superseded.md"},
    {"operation": "add", "path": "reviews/chatgpt/2026-08-11T2337Z_supply-protocol-and-superseded.md"},
    {"operation": "add", "path": "reports/2026-08-11T2337Z_supply-protocol-and-superseded.md"},
    {"operation": "modify", "path": "CONVENTIONS.md"},
    {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"},
    {"operation": "modify", "path": "DECISION_LOG.md"}
  ],
  "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
}
```

The final scope check at the pushed head is post-report evidence.

## 12. A10-pre — Validators

Run individually with `python -m pytest <path>`. Environment: Python
3.11.15, `python -m pytest` = **pytest 9.1.1**, which is the mandated
invocation. The `pytest` binary on `PATH` is a different version and was
not used.

```
########## python -m pytest tests/test_repository_structure.py ##########
....                                                                     [100%]
4 passed in 0.02s
EXIT STATUS: 0

########## python -m pytest tests/test_si1_governance.py ##########
..............                                                           [100%]
14 passed in 0.05s
EXIT STATUS: 0

########## python -m pytest tests/test_gate_anchors.py ##########
..................                                                       [100%]
18 passed, 2 deselected in 7.07s
EXIT STATUS: 0

########## python -m pytest tests/test_governance_tools.py ##########
........                                                                 [100%]
8 passed in 1.30s
EXIT STATUS: 0
```

**All four exit 0.** The 2 deselected in `test_gate_anchors.py` are
`@pytest.mark.slow` cases excluded by `pyproject.toml`'s
`addopts = "-m 'not slow'"` — pre-existing configuration, unchanged by
this task.

### What the validators assert about rule count and branching-policy structure

**Asked because both files gain content here. The answer is: nothing.**

- **`tests/test_repository_structure.py`** names `CONVENTIONS.md` in
  `REQUIRED_TOP_LEVEL_FILES` and `docs/BRANCHING_POLICY.md` in
  `REQUIRED_NESTED_PATHS`. Both are tested by `is_file()` **existence
  only**. The file's remaining test cross-references gate IDs between
  `CLAIMS.md` and `GATES.md`. **No rule count, no rule heading, no
  branching-policy section, no deletion state, no count identity is
  asserted anywhere in it.**
- **`tests/test_governance_tools.py`** mentions `CONVENTIONS.md` as a
  real repository path used as a **fixture** for the manifest evaluator's
  own logic — a `prefix_hash` criterion expected to classify as
  `INVALID_OR_UNDERSPECIFIED`, and `required_paths` / `forbidden_paths`
  entries used to exercise contradiction detection. **It asserts the
  evaluator's classifications, never the file's content.**
- **`tests/test_si1_governance.py`** reads `GATES.md`, `CLAIMS.md`, two
  derivations, two campaign scripts and one report. **It never opens
  `CONVENTIONS.md` or `docs/BRANCHING_POLICY.md`.**
- **`tests/test_gate_anchors.py`** contains zero `read_text`/`open` calls
  and zero occurrences of `GATES`; it recomputes numerical anchors and
  reads no repository document at all.

**Consequence, stated plainly.** Rules 1–17 could have been renumbered,
reworded or deleted, and the deletion state machine's closed identity
broken, **and all four validators would still exit 0.** A4's and A5's
byte comparisons are the only thing standing behind those invariants on
this branch, and they are executed once, by me, in this report. **This is
the enforcement gap §4 names, measured rather than asserted** — and §2
forbids this task to close it.

## 13. Rule 16 assessment

**Rule 16 is operative: this task adds MATERIAL governance artifacts
bearing on a question other authoritative artifacts already address** —
Amendment K on supersession, and Rule 15 on committed reviews.

**§4's candidate junction is confirmed, not replaced.** Named precisely:

    CONVENTIONS.md Rule 18 (eighteen rules)
      + docs/BRANCHING_POLICY.md's superseded register
      + DECISION_LOG.md's entry recording both
    ---------------------------------------------------------------
    available inference:  supersession and review supply are now
                          ENFORCED

**They are recorded, not enforced**, and §12 measures exactly how far
short of enforcement the repository stands: **no test checks any of the
eighteen rules**, and nothing prevents an integration task from merging a
superseded branch without ever reading the register. **The register is a
document a task must choose to consult.**

**Two additions of my own, which the candidate does not cover.**

- **The register's silence is itself an available misreading.** After
  this task the register has three members, and a reader may infer that
  the programme has had exactly three supersessions. **What it records is
  three supersessions that durable artifacts establish** — §9.4 documents
  a fourth branch with substantial evidence, deliberately excluded. **An
  under-populated register reads as a complete census unless its
  exclusions are visible**, which is why §9.4 exists and why the entry
  threshold was landed in the file rather than left in this report.
- **Rule 18's presence in `CONVENTIONS.md` will read as a solved
  problem.** It is not: §8 records that it did not resolve the mode it
  was written to fix, **on the very first supply it governed.** A reader
  meeting the rule in the file, without this report, would reasonably
  conclude the supply protocol is closed. **The rule is half closed** —
  the blank-line half is finished, the boundary-location half is not.

## 14. Stops and clarifications

**One primary category per stop; secondary findings listed separately.**
Included even where there were none.

### `SPECIFICATION_DEFECT`

**One, non-blocking, and it is this task's own subject matter.** **Rule
18 does not close the failure mode §0 says it closes.** §0 diagnoses mode
1 as a first-occurrence search finding the instruction, and prescribes
complete-line matching. Applied to this task's supply, complete-line
matching returned **zero** BEGIN candidates: the shared line is created
by the transport prepending an attachment marker to line 0, not by the
specification containing the delimiter. **A boundary inference was still
required, of the kind Rule 18's own text forbids.** §8 gives the
measurements and §8.7 the clause that would close it. **I landed Rule 18
exactly as specified and added nothing to it.**

**The dependent ruling I did not take, flagged so it is not buried.** If
the PI intended Rule 18 to compel a STOP whenever BEGIN is not a complete
line, **this task should have stopped and did not.** §8.6 states the
three reasons I read A2 and §7 as requiring a completed report with a
"no" answer instead, and states that none of Rule 18's four literal STOP
triggers fired. **Deciding between those readings is PI authority, not
mine.**

**Secondary, non-blocking, already identified by the Reviewer and
confirmed:** §0's "eight attempts and five distinct failure modes"
counts items 1 and 2 as distinct modes when its own text describes them
as the same mode in consecutive tasks. Deduplicated, it is **four modes
across eight attempts** — and with this task, **nine attempts.** Affects
no criterion. Not corrected: §2 authorises no edit to the specification,
and the specification is committed verbatim.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Rule 13 carrying two conflicting
orders remains a known open item, untouched here. Nothing was installed.
Python 3.11.15; `python -m pytest` 9.1.1 used throughout; the different
`pytest` on `PATH` was not used.

### `OBSERVATION_METHOD_ERROR`

**Two, both caught by my own checks before any conclusion rested on
them.**

1. **My first branch-scan method was unsound, and its own output proved
   it.** Same-line proximity between a branch name and supersession
   vocabulary scored `fix/pi-decisions-v2` at **zero** — a branch the
   specification supplies as a register member. A method that misses a
   known positive cannot support a negative finding about 44 others.
   Replaced with a ±6-line windowed scan, then every non-zero hit read in
   context. **Reported rather than quietly dropped**: §9.2 and §9.5 both
   record the discarded method, because an unreported false start looks
   like a method never tried.
2. **The scope manifest's `mode` field.** I first passed
   `"mode": "BRANCH_SCOPE"`, which returned
   `{"error": "scope mode must be exact or subset", "overall":
   "TOOL_ERROR"}` at exit 3. The tool's contract is `exact` or `subset`;
   re-run with `exact`, PASS at exit 0. **The tool is read-only and
   nothing was modified**; the error was in my input, not in the
   repository.

### `REPOSITORY_DEFECT`

**None introduced. One pre-existing gap measured rather than asserted**,
and it is the known open item §4 names: **no validator asserts anything
about `CONVENTIONS.md`'s rule count or `docs/BRANCHING_POLICY.md`'s
structure** — both are existence-checked only, and the two files' content
invariants have no mechanical guard at all. §12 gives the evidence per
validator. **§2 forbids this task to add a test, and none was added.**

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**One.** **`review/role-model-and-executors` @ `10c260b9…`** — evidence
suggests supersession without establishing it under §1's threshold, so it
is **named and left out of the register pending PI authority.** §9.4
gives the full evidence, including the durable specification that names
both the successor branch and the reason, and states exactly what is
missing: **no artifact calls the branch superseded, none forbids its
integration, and it already carries a different durable disposition**, so
writing SUPERSEDED against it would be the first such classification —
a decision, not an observation. **I recommend the PI rule that the
clean-rebuild record suffices**, which would add a fourth entry; I am not
entitled to take that decision. The branch was not touched.

## 15. Ambiguous, unsatisfiable, or would have specified differently

- **A2 is the only criterion in tension with itself, and deliberately
  so.** "Apply the rule you are landing" and "commit this task's review"
  cannot both be satisfied strictly when the rule cannot locate a
  boundary that the supply does not provide. **The specification
  anticipated the tension** — A2 and §7 ask for a sufficiency verdict in
  the report, not a stop — **and I have answered it there rather than
  resolving it silently.** I would still add one sentence to a future
  A2: *"if the rule proves insufficient, report and proceed"* or *"if the
  rule proves insufficient, STOP"*. Either is fine; the absence is what
  left the choice to me. **This is the one place I made a call the
  specification could have made.**
- **A5's "report that section's before and after explicitly" is
  satisfiable but literally redundant** when the two are byte-identical:
  printing 1435 identical bytes twice makes the digest equality harder to
  see, not easier. §7 shows the section once and reports the digest match
  and the boolean. **Flagged in case the intent was two literal
  printings.**
- **§1's threshold and §2's "do not add" are in productive tension**, and
  §9.4 is where it bites. The threshold's wording ("re-issue, replacement
  **or** supersession") is broad enough to admit the role-model branch;
  its rationale ("finding the artifact that already records one is an
  observation") is narrow enough to exclude it. **I resolved it toward
  the rationale**, since §2 forbids adding classifications and §1
  supplies an explicit instruction for the suggestive-but-unestablished
  case. **A future specification could close this by saying whether the
  threshold is lexical** — must an artifact use the word — **or
  substantive.**
- **A4's phrasing "after removing only the Rule 18 section" leaves the
  section's boundary undefined at its start** — whether the blank line
  separating it from Rule 17 belongs to the section. Both readings were
  tried; only one recovers A1's digest, so the ambiguity is
  self-resolving and is recorded rather than raised as a defect. §6 states
  the boundary used.
- **Nothing else was unsatisfiable.** No instruction conflicted with a
  repository rule, so §6's stop-and-report clause was not triggered on
  any point other than the one recorded under `SPECIFICATION_DEFECT`,
  where I have named the ruling rather than taken it.

## 16. What this task did not do

**No science, no gate, no computation**, as the specification states. No
gate status changed and no gate was registered. No verdict, digest or
hash-pinned artifact was modified. **No branch was deleted and no branch
ref was changed.** **No superseded branch was integrated**, and no
assessment was made of whether any branch's content is correct —
**supersession is not a verdict on content.** **No fourth deletion state
was added** and the closed count identity is byte-identical. **No test
was added.** **`AGENTS.md` was not modified.** Rules 1–17 were neither
renumbered nor reworded. `main` was not moved and nothing was merged into
it.
