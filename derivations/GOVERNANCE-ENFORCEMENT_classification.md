# Governance enforcement — classification of every rule and amendment

Evidence base: `8939ff4a46445d88c6470fb4f27eec71f2f39172`
Source: `CONVENTIONS.md`, SHA-256
`928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d`

**Counts measured before classifying, and they govern:** **18 numbered
rules** (`^### N.`) and **11 lettered amendments** — A, B, C, D, E, F, G,
H, I, K, L. **There is no Amendment J.** 29 objects.

## The categories

    MECHANICAL     a machine can decide it from repository objects
    PARTIAL        a necessary condition is checkable; the rule is not
    JUDGEMENT      deciding it requires reading for meaning

**A rule is classified MECHANICAL or PARTIAL only where a property in
this document actually checks it.** "Could be checked by some tool" is
not the test — a classification that says MECHANICAL with nothing behind
it is exactly the mislabelling this task exists to prevent. **Where a
rule admits no check, it is JUDGEMENT and the one-sentence reason says
why, and proposes no mechanism.**

**For every PARTIAL, the sentence stating what the check does NOT
establish is reproduced in the checker's JSON**, not only here. A reader
of the tool's output must meet the limit without consulting this file.

---

## 1. The properties the checker implements

Nine, of which **four are MECHANICAL and five are PARTIAL**. §2 of the
specification listed seven; **P8 and P9 are added**, and the reasons are
under each.

| id | property | class | enforces |
|---|---|---|---|
| P1 | scope manifest arithmetic | PARTIAL | Rule 12 (instance) |
| P2 | Rule 15 commit order — review precedes first work commit | MECHANICAL | Rule 15 (timing) |
| P3 | append-only on both measures, over a set the specification declares | PARTIAL | no rule; a recurring criterion |
| P4 | superseded branches are not merged | MECHANICAL | Amendment K |
| P5 | merge parentage against freshly recomputed facts | PARTIAL | Rule 5 (part) |
| P6 | commit-message hygiene | PARTIAL | **no rule** — see §3 |
| P7 | gate integrity — every `## P2-` heading is parsed, and no unauthorised section changed, over a set the specification declares | PARTIAL | Rule 3 (part) |
| P8 | Rule 15 placement and specification-first | MECHANICAL | Rule 15 (placement) |
| P9 | every report carries "Stops and clarifications" | MECHANICAL | Amendment B |

### What each PARTIAL does not establish

**These sentences are the checker's `does_not_establish` field verbatim.**

- **P1** — *Does not establish that the manifest is correct, only that
  the total the specification declares in its `stated:` record agrees,
  per category, with the paths that record's block enumerates; a
  specification declaring no total is reported NOT_PARSEABLE, which is
  not a pass and is not a finding about that specification's scope.*
- **P3** — *Does not establish which files are append-only; the declared
  set is a caller-supplied parameter and the check is silent about
  whether that set is the right one, or complete.*
- **P5** — *Does not establish that the executor derived the parentage
  values independently; three correct values are equally consistent with
  fresh recomputation and with one field copied into another. The
  diquark task's shared-rationale defect would pass this check.*
- **P6** — *Does not establish absence of "session identifier" or "tool
  attribution", which no repository document defines; only
  `Co-Authored-By` trailers and URLs are matched, and the author and
  committer identity fields are not message content and are out of
  scope.*
- **P7** — *Does not establish which gate sections were authorised to
  change; the authorised set is a caller-supplied parameter, and an empty
  set means "nothing may change", never "nothing to check".*

**P7's limitation, extended by measurement rather than by argument.** The
paragraph below is **not** part of the `does_not_establish` field quoted
above; it records what `P7` was found to be doing, and what now prevents it.

**`P7` returned `PASS` while checking nothing, in every task that ran it.**
Its heading grammar was `^## (P2-[A-Z0-9-]+)\s*$`, which requires the line to
end after the gate id. **Every one of the fourteen headings in `GATES.md` is
`## <id> — <title>`, so the expression matched none of them**: `gate_sections`
returned an empty map at both base and head, `check_p7` compared two empty
maps, found nothing changed, and returned `PASS`. **Among the tasks that
green were two which modified `GATES.md` and one which flipped a gate
prerequisite.** **An empty match returning True is the most dangerous kind of
green, and it was demonstrated in the tool built to prevent it.**

**What prevents the recurrence is the completeness invariant, not the new
grammar.** A better grammar closes the instance; **only the invariant closes
the class.** `check_p7` now counts `## P2-` lines through a pattern written
independently of the grammar it guards, and returns **`NOT_PARSEABLE` unless
the parsed section count EQUALS that raw count, at base and at head.**
**Equality, not merely non-zero:** a guard firing only at zero would still
pass a grammar that read fourteen of fifteen headings, because the fourteen
it sees are unchanged and the fifteenth is invisible to it — and one unseen
gate is enough. **A raw count of zero is `NOT_PARSEABLE` too**, because a
registry the grammar could not read has not been checked, which is not the
same as having been read and found clean. **Both hold when the authorised set
is empty and when base and head are identical.**

**`NOT_PARSEABLE` and not `FAIL`, deliberately.** The state means the grammar
cannot fully read the gate registry, **not** that an unauthorised change has
been shown. **Cannot judge is not judged wrong** — the distinction `P1`
already carries. It still makes the run `INCOMPLETE` and exits non-zero.

**`P7` remains `PARTIAL`, and for the unchanged reason:** the authorised set
is still a caller-supplied parameter and the discovery problem behind it is
untouched by this repair.

**`P3` and `P7`, extended again — where the declared set now comes from.**
The paragraphs below are **not** part of either `does_not_establish` field
quoted above; they record what changed and what did not.

**Both properties now read their declared set from the SPECIFICATION'S SCOPE
BLOCK**, through the `append_only:` and `authorised_gates:` keys, and from the
run-time config only as a fallback. **The config was written after the review**,
so a reviewer approved a specification while something else decided what the
checks were pointed at. **When the specification declares, it wins. When only
config supplies, the check proceeds and the JSON names `config` as the
source. When both declare and they DIFFER, the property returns
`DECLARATION_CONFLICT` and the run is non-zero** — a config silently
overriding a reviewed declaration would reproduce, one layer along, the defect
this change removes.

**`P3`'s reading of an empty set is corrected.** It formerly returned
`NOT_APPLICABLE` for `[]` — the check switched OFF, not passed — and one
landed integration supplied `append_only_paths: []` and went green on it.
**An empty declared set now returns `DECLARED_EMPTY`**: not `NOT_APPLICABLE`,
because the specification SAID the applicable set is empty and absence says
nothing; and **not `PASS`, because nothing was checked** and a pass over
nothing is the vacuous green this repository has met three times. **It does
not make the run `INCOMPLETE`**, because unlike `NOT_DECLARED` it is a valid
declaration.

**Both remain `PARTIAL`, and the reason is narrowed rather than removed.**
**A specification still declares its own sets, and a specification can declare
wrongly.** Nothing verifies that a declared append-only set is complete, or
that an authorised-gate set names only gates the task was authorised to
change. **What changed is that the declaration is now inside the artifact a
reviewer reads**, so a wrong declaration is visible at review time instead of
being invented afterwards. **That is a narrower discovery problem, not an
absent one.**

**And nothing requires a specification to carry the keys at all.** A
specification that declares neither still reaches `NOT_DECLARED`, exactly as
before. **Making the declarations mandatory is `C2`**, which is unbuilt;
**compliance therefore still rests on an authoring habit.**

### P8 and P9, added, with reasons

**P8 — Rule 15 placement and specification-first.** Rule 15's *Placement*
and *Timing* paragraphs are pure path and ordering facts: specifications
under `specs/`, reports under `reports/`, reviews under
`reviews/<function>/`, and the specification committed as the task's
first commit. **§2 commissioned no property for them and they are the
most mechanical thing in the whole document**, so leaving them
unenforced while P2 enforces Rule 15's other half would have been an
arbitrary gap.

**P9 — Amendment B.** Every task report must contain a "Stops and
clarifications" section. **The presence of a heading is decidable from
the blob.** What that section must *contain* is not, so P9 checks
presence only and says so — it is MECHANICAL about the heading and makes
no claim about the section's adequacy.

### Validators — suite checks, and NOT properties of the checker

**These are not among the nine and must never be numbered among them.** A
property runs when someone invokes the checker with a config; a validator
runs whenever anyone runs the suite. **They are listed here because the
document's purpose is to say what has a machine behind it**, and a check that
runs only in the suite still has one.

| id | validator | class | what it guards |
|---|---|---|---|
| V1 | gate pin integrity — `tests/test_gate_pins.py` | MECHANICAL | that every artifact pinned by SHA-256 in `GATES.md` still hashes to its pin |

**V1 — why it is a test and not a property.** The measured failure was that
**the suite could not distinguish a stale pin from a correct one**:
`python -m pytest` returned `280 passed, 2 deselected` across four
consecutive revisions spanning a stale pin, a repaired pin, an edited
artifact and a re-pinned one. **The count never moved.** **A suite invariant
across the property in question is not testing that property.** The
demonstrated gap was the suite's, so the repair went in the suite.

**V1 fails on three things, and the third is the one that matters:** a pin
whose target does not hash to it; a pin with no resolvable artifact path
above it, which fails rather than being skipped; and **a `GATES.md` carrying
no pin at all.** **A pin validator that passes over an empty pin set is the
same defect `P7` carried, one level along**, and this programme has now met
that shape twice.

**What V1 does not establish.** It does not establish that the pinned
digests are the *right* ones — only that the artifacts still match whatever
`GATES.md` declares. **A pin that was wrong when it was written passes.**
**Nor does anything currently detect V1 itself going vacuous:** its non-empty
assertion is a guard written by the same hand as the guard it imitates, and
if the pin notation drifted so that the pattern stopped matching, the
non-empty assertion would be the thing that fires — which is why it exists,
and is not a substitute for an independent check that does not exist.

---

## 2. The eighteen rules

**Rule 1 — Contradiction-stop.** `JUDGEMENT`. Deciding that an
instruction contradicts a rule requires reading both for meaning, which
is the same act the rule asks a human to perform.

**Rule 2 — Scope precedence.** `JUDGEMENT`. It resolves a conflict, and
detecting the conflict is the semantic step; a machine that could see the
conflict would already have decided Rule 1.

**Rule 3 — Declared frozen scope is normative.** `PARTIAL` via **P7**.
The necessary condition checked is that no `## P2-` gate section outside
a caller-supplied authorised set changes byte-for-byte and that the
section count is unchanged. **It does not establish that the declared
frozen set was the right one**, nor does it reach any frozen file outside
`GATES.md`.

**Rule 4 — Execution prompts are evidence.** `PARTIAL` via **P8**. That a
specification exists under `specs/` and is the task's first commit is
mechanical; **that the committed prompt is the one that actually governed
the run is not a fact about any repository object.**

**Rule 5 — Minimum mandatory merge discipline.** `PARTIAL` via **P5**.
Parent 1, parent 2 and a freshly recomputed merge-base are checkable
against the merge object. **The rule's substance — that the discipline
was followed rather than reconstructed afterwards — is not**, and P5's
limitation sentence says so.

**Rule 6 — Reporting honesty for merges.** `JUDGEMENT`. It requires a
report to distinguish two states of the world in prose; no repository
object records which distinction the author intended.

**Rule 7 — Evidence precedence.** `JUDGEMENT`. It tells a reader which
source wins when three disagree, and detecting the disagreement is
semantic.

**Rule 8 — Responsibility separation.** `JUDGEMENT`. Whether an executor
made a decision reserved to the specification author is a fact about
authorship of a choice, not about a diff.

**Rule 9 — Outcome-based task specification.** `JUDGEMENT`. Whether a
specification states outcomes rather than procedures requires reading it.

**Rule 10 — Self-correction authority and its limit.** `JUDGEMENT`.
Whether a change was a permitted self-correction depends on what the
specification authorised, which is prose.

**Rule 11 — Task granularity and integration boundary.** `JUDGEMENT`. It
is a `SHOULD` about how much work belongs in one task.

**Rule 12 — Acceptance criteria must be mechanically checkable.**
`PARTIAL` via **P1**. **One recurring instance is decidable** — a scope
manifest's path count against the total the block itself declares in a
`stated:` record — and that instance is the defect shape which recurred
four times in this programme. **No sentence is consulted**; a document
that declares no total is not judged. **Whether every criterion in a
specification has a machine-executable verification is not decidable**;
P1 checks one criterion's internal arithmetic, not the rule.

**P1's decidability is narrow, and it was measured, not assumed.** P1 is
decidable only over specifications written in the declared-total syntax.
**Forty-two fixtures did not establish behaviour over real documents; one
corpus run did.** Over the twenty-nine specifications carrying exactly
one scope block at `1cb5550f`, **the pre-repair pass rate was ten**, and
the nineteen non-passes were not defects in those documents: sixteen
found no count sentence at all, because the backward walk stopped at the
nearest markdown heading, and three took an intermediate dry-run count
for the manifest's. **After the repair those twenty-nine are
`NOT_PARSEABLE`.** **`NOT_PARSEABLE` is not a pass and is not a failure;
P1 has made no determination about those documents at all**, and a corpus
reading `NOT_PARSEABLE` throughout has not been checked. **Adoption of
the syntax by convention is a separate matter this classification does
not record as done.**

**Rule 13 — Execution environment.** `JUDGEMENT`. It governs which
diagnostic order an executor follows on failure, and **it carries two
conflicting orders**, so no machine could decide conformance even in
principle without first resolving that. **This is a known open item and
is recorded in §4 as unenforceable as written.**

**Rule 14 — Validator outcome contract.** `JUDGEMENT`. It is about the
disposition of a process run — started, completed, exit status, nothing
skipped — and **no repository object records that a validator ran, let
alone how it terminated.** The disposition vocabulary (satisfied /
PI-authorized exception / waived) is a reporting obligation.

**Rule 15 — Governing artifacts are committed.** `MECHANICAL` via **P2**
and **P8**. Placement is a path predicate; specification-first and
review-before-work are commit-order predicates over a range. **This is
the only rule in the document that is mechanical without qualification**,
and it is so because its text is entirely about paths and order.

**Rule 16 — Accumulated reading.** `JUDGEMENT`. It requires naming an
inference a reader could draw from a set of artifacts, which is the
definition of reading for meaning.

**Rule 17 — Integrations do not add epistemic or governance
classifications.** `JUDGEMENT`. Deciding that a classification is *new*
requires understanding what the reviewed results already carried.

**Rule 18 — Review supply protocol.** `JUDGEMENT`, and **no check stands
behind it.** **How a review file reached the executor is not recoverable
from repository objects** — a byte-identical blob is consistent with a
file supply, a paste, and a reconstruction. §3 of the specification
states this and forbids inventing a check; none is written.

## 3. The eleven amendments

**Amendment A — mid-task authorizations reproduced verbatim in the
report.** `JUDGEMENT`. Whether the reproduction is verbatim requires the
original, which exists only in a conversation.

**Amendment B — every task report carries a "Stops and clarifications"
section.** `MECHANICAL` via **P9**, for the heading's presence only. **What
the section must contain — each stop, its output, whether it was correct,
its category — is `JUDGEMENT`**, and P9 makes no claim about it.

**Amendment C — digest semantics and binary-safe computation.**
`JUDGEMENT`. Whether a digest was computed binary-safe is a fact about
the command that produced it, not about the value.

**Amendment D — execution location, and the process/harness layer.**
`JUDGEMENT`. Where a command ran is not recorded in any object.

**Amendment E — a failed observation is not a negative result.**
`JUDGEMENT`. It governs how an executor may describe an observation that
failed, which is a claim about prose.

**Amendment F — mutation tests must prove reach.** `JUDGEMENT`. Whether a
mutation test reaches the code it claims to cover requires running it and
reading what it asserts.

**Amendment G — structural changes propagate.** `JUDGEMENT`. **§0 of the
specification uses this as its worked example and is right**: that a
structural change was propagated everywhere it should have been cannot be
decided from a diff, because "should have been" is semantic.

**Amendment H — literals are verified by execution.** `JUDGEMENT`.
Whether a recorded literal was measured or asserted is a fact about the
author's process. **This task found a false `MEASURED` line in its own
commissioning document** (§4), which is exactly the failure no machine
catches.

**Amendment I — mid-task authority changes require reviewer-visible
provenance.** `JUDGEMENT`. **§0's second worked example**: whether a
provenance record is adequate is a judgement about sufficiency.

**Amendment K — re-issuing an executed specification.** `PARTIAL` via
**P4**. **One clause is mechanical** — a superseded branch must not be
integrated, which is an ancestry test against the register. **The rest is
not**: that a re-issue used new task-identity paths, that the superseded
branch was preserved untouched, and that the re-issue mechanism was
supplied rather than derived are not decidable from a commit range.

**Amendment L — consumed conventions must be discoverable through the
conventions index.** `JUDGEMENT`. Whether a convention is discoverable is
a claim about a reader's path through documents.

## 4. Rules unenforceable as written — findings, not licence to change

**This section reports; it changes nothing.** `CONVENTIONS.md` is not
modified by this task.

**Rule 13 carries two conflicting diagnostic orders.** No conformance
check is possible until one is chosen, and this is a long-standing open
item that every report in this line has had to note rather than resolve.

**P6 enforces no rule at all.** **`CONVENTIONS.md` contains zero
occurrences of "Co-Authored-By", "session identifier", "tool attribution"
or "trailer".** Commit-message hygiene has been an acceptance criterion
in every recent specification and **is nowhere a standing rule**. The
check is implemented because the criterion recurs, but the classification
must not pretend it enforces a convention. **Two of the four forbidden
categories have no delimited vocabulary anywhere in the repository**,
which is why P6 is PARTIAL rather than MECHANICAL.

**Rule 15's "Prospective only" has no stated boundary commit.** The rule
says records created before it are not retrospectively non-conforming,
but nothing in the repository states *which commit* that is. **The
checker therefore takes the boundary as a parameter and refuses to assume
one**, and runs both the INCLUSIVE and EXCLUSIVE readings so the
difference is measured rather than chosen.

**Amendment B's requirement is stronger than any check.** It demands the
lines that establish a stop be reproduced. **P9 checks a heading**, and
saying otherwise would be the proxy substitution this task exists to
detect.

## 5. The count that matters

    MECHANICAL   Rule 15                                          1 rule
                 Amendment B (heading presence only)              1 amendment
    PARTIAL      Rules 3, 4, 5, 12                                4 rules
                 Amendment K                                      1 amendment
    JUDGEMENT    Rules 1, 2, 6, 7, 8, 9, 10, 11, 13, 14, 16,
                 17, 18                                          13 rules
                 Amendments A, C, D, E, F, G, H, I, L             9 amendments
    -----------------------------------------------------------------------
                 18 rules + 11 amendments                        29 objects

**Two of twenty-nine objects are mechanical, and one of those only in
part.** **Five more have a necessary condition behind them.** **Twenty-two
have no machine behind them at all.**

**A suite that claimed to enforce eighteen rules while enforcing one and
a half would be worse than one that enforces what it enforces and says
so.** That is the whole of this document's purpose.
