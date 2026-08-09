# DRAFT amendment — observation failure, mutation coverage, structural propagation, and literal verification (PROPOSED)

Status: **PROPOSED**, for reviewer consideration. Not an executor
prompt. If approved, a separate specification lands it.

Target: refinements attached to existing rules in `CONVENTIONS.md`, plus
new rules. **Do not renumber existing rules.** Headings are lettered or
given new numbers, never reusing an existing rule's number for an
amendment to a different rule.

**The common principle, stated once so the amendments are not read as a
checklist of accidents.** Across all of them:

> **Evidence must establish the property claimed, not merely a
> correlated proxy for it.**

An exit code is not an observation. A stop is not proof that a mutation
was reached. A numerical reproduction is not an algebraic proof. A
string that nearly matches does not match. A path count is not blob
integrity. A citation is not computational consumption. **Each amendment
below is that principle applied to one place where the proxy was
mistaken for the property.**

**Every item is derived from a specific incident in the last two days,
and each records that incident.**

**Each incident is marked as CAUGHT PRE-ISSUE or as REACHED
EXECUTION.** The distinction matters for the same reason Amendment I
exists: a later reader must be able to reconstruct what was actually in
force. **Amendments G and J are drawn from defects caught in draft and
corrected before issue** — the issued specifications do not contain
them. **The rules are not weakened by that; the mechanism that caught
both was ad hoc, and these rules institutionalise it.** A rule whose origin
is stated is one a later reader can evaluate; a rule without one becomes
folklore.

---

## Amendment E (attached to Rule 14) — a failed observation is not a negative result

> **A failure to observe MUST NOT be recorded, mapped, or acted upon as
> an observed negative result.**
>
> Where a check can fail to produce an observation, its outcome model
> MUST distinguish — **whether by explicit states or by equivalent
> evidence** — at least: **observed positive**, **observed negative**,
> and **not observed**.
>
> **This does not require every tool to expose a three-valued enum.**
> The requirement is that the distinction be recoverable, not that it be
> encoded in a particular form. A tool exit status, acceptance criterion, or
> state machine that maps "could not determine" onto the same value as
> "determined to be false" is a defect.
>
> **The two require opposite responses:** a failed observation calls for
> repairing the measurement; an observed negative calls for stopping and
> investigating.

*Incidents — all four REACHED EXECUTION.*

**(i)** `git merge-base --is-ancestor` returns `0` for merged, `1` for
not merged, and `>= 2` for execution failure. A specification that
treated any non-zero status as "not merged" would have moved a branch
into a terminal `NOT_AUTHORIZED` state on the strength of a command that
did not run.

**(ii)** `merge_guard.py` returns exit `2` both for a governance failure
and for an argparse rejection. When `--mode` was passed on the command
line instead of in the config, the tool refused to run and returned the
same code it uses for a failed check. **Exit `2` alone cannot
distinguish "the tool refused to run" from "the check failed".**

**(iii)** The branch-deletion authorization machine had no state for
"listed but absent from the remote". The executor **conservatively used
`NOT_AUTHORIZED` because no absence state existed; this prevented
deletion but misclassified the observation** — producing a record in
which `not_merged_count` was `0` while one entry was `NOT_AUTHORIZED`.
The fix added `ABSENT_FROM_REMOTE` as a distinct terminal state.

**A conservative effect does not make an incorrect observation label
acceptable.** "It caused no harm" is the reason this class of defect
survives.

**(iv)** A specification stated that if a numerical reproduction
disagreed across three prefactors, "the invariance argument is wrong".
**It would more likely mean the three cases had not in fact shared one
regulated integral.** A numerical disagreement is evidence that stated
conditions were not reproduced; it does not overturn an exact algebraic
identity.

## Amendment F (attached to Rule 12) — mutation tests must prove reach

> **A mutation test MUST establish three things, separately:**
>
>     1  the mutation was injected
>     2  the dependency point was REACHED
>     3  the expected downstream consequence was observed — either the
>        dependent quantity changed in the expected causal direction, or
>        the mutation caused the specifically expected failure AT OR
>        AFTER the dependency point
>
> **The expected consequence MUST be one that could not occur under the
> un-mutated input.** Reach plus a consequence is not enough if the
> consequence was available anyway: **a mutation flipping a sign in a
> channel whose coefficient is zero proves reach and nothing else.**
>
> **"The output changed" is too narrow.** Mutating a required convention
> may correctly produce a STOP at the parsing or validation point rather
> than a different final value; that establishes the dependency just as
> well. **What must be excluded is an unrelated earlier STOP being
> counted as coverage.**
>
> **Demonstrating that the program stopped is not sufficient.** A
> program can stop before the mutation is consumed, for an unrelated
> reason, and a test that only asserts a stop will pass while covering
> nothing.
>
> **Stop behaviour is tested separately** from mutation reach.

*Incident — REACHED EXECUTION.* While verifying that two PI rulings were genuine
computational inputs rather than decorative citations, the executor
found that a gate fired before the mutated quantity was measured. The
test would have passed while proving nothing about the dependency it
existed to demonstrate. **The dependency was real; the test was not
evidence of it until the reach was shown.**

*Why this belongs in the rules.* A ruling recorded in `DECISION_LOG.md`
and cited in prose is not thereby consumed by any computation. **The
distinction between "the specification says to use it" and "removing it
breaks the result" is exactly what a mutation test exists to establish**
— and it establishes nothing if the mutation never arrives.

## Amendment G (attached to Rule 9) — structural changes propagate

> **When a specification gains, splits, or re-layers a structure — a
> stage, a layer, a conditional branch, a state, a commit-order
> constraint — every acceptance criterion, invariant, report-contract
> item and objective statement MUST be re-read against the new
> structure before issue.**
>
> For each, ask two questions: **how does this clause read under the new
> structure**, and **does it now require a quantity the new structure
> permits to be undefined?**
>
> **Propagation is TRANSITIVE.** Revising one structural element
> requires checking every clause whose meaning or satisfiability depends
> on it, **not only clauses that name it directly**. A new stage changes
> the sequence, which changes commit ordering, which changes evidence
> layering, which changes scope timing, which changes the report
> contract, which changes what is post-report evidence.
>
> **Residual clauses from the old structure do not lapse. They become
> contradictions**, and a correct executor will stop.
>
> **Layer boundaries must be drawn by what each layer actually requires,
> not by where a statement intuitively belongs.** A statement placed in
> a layer that does not supply its premises invalidates the layering.

*Incidents — six on one specification, all CAUGHT PRE-ISSUE.* Splitting the scope check into
pre- and post-merge left the validator check unsplit. Adding a Stage 0
left the invariants forbidding what Stage 0 required, left the push
unauthorized, and left the source head stale in four criteria. Adding a
partial-stop left the deliverables and scope clauses assuming the
non-stopped case. Splitting a two-layer result into three left the tests
requiring a quantity the third layer permitted to be undefined.

*And one of a different kind — CAUGHT PRE-ISSUE, not reached
execution.* In a draft of the channel-character specification, real
Hubbard–Stratonovich admissibility was placed in the layer described as
requiring no exponent mapping —
**but it is an exponent-level quantity.** The layering was not merely
incomplete; **one boundary was drawn in the wrong place.**

**That clause is dependency-derived, not frequency-derived.** `c` is
interaction-expression level; `g` is exponent level; without the mapping
there is no `g`; so real-HS admissibility cannot belong to a layer
declared free of the mapping. **One demonstrated case in which a layer
lacked a premise required by one of its own outputs is sufficient to
establish the structural rule** — no second incident is needed, because
this is a dependency violation rather than an observed pattern.

## Amendment H (attached to Rule 3) — literals are verified by execution

> **A specification that requires a literal or normalised-text match
> MUST have had the specified match executed against the target text by
> its author before issue.** Asserting a literal is not verifying it.
>
> **The specification MUST distinguish two kinds of check:**
>
>     byte- or character-exact    no representation-changing
>                                 normalisation is permitted
>     normalised substantive      one explicitly defined normalisation
>                                 function, applied to BOTH the
>                                 requirement and the target
>
> **Once blockquote prefixes are stripped or whitespace collapsed, the
> check is no longer an exact string match** — and some literals cannot
> tolerate that: a SHA, a JSON key, a Markdown heading a script locates
> by. **Say which kind each check is.**
>
> **The specification MUST state which representation features are
> SEMANTIC for that check and which are normalised away.** Do not write
> that representation is ignored in general — for some literals the
> representation IS the substance:
>
>     normally normalisable   blockquote prefixes, line wrapping
>     depends on the target   Markdown emphasis, code delimiters
>     usually SEMANTIC        Unicode dashes, exact SHAs and blob ids,
>                             JSON field names, Markdown headings a
>                             script locates by, code identifiers,
>                             regex tokens
>
> **The normalisation MUST be a single function applied to BOTH the
> requirement and the target**, specified as a function rather than as a
> list of removals. **Stripping can manufacture a match the raw text does
> not contain as easily as it can repair one it does**; applying one
> function to both sides is the property that makes the check auditable.
>
> **The specification MUST record the target, the normalisation, the
> verification method, and that the check PASSED before issue** — for
> example: *"Pre-issue literal verification: PASS after stripping
> blockquote prefixes and collapsing whitespace; code delimiters
> stripped; en dashes preserved."* **Raw authoring output may be
> retained in the review record rather than embedded in the
> specification**, so that a specification does not fill with tool
> transcripts.
>
> Where the literal is itself sensitive — **especially a hash, an object
> id, a machine-consumed heading, or an identifier** — the expected
> value and the executable verification method MUST be written out.
> **This is not required of every exact heading**: a specification with
> ten of them should not carry ten shell commands. It applies where the
> literal is consumed by machine or where a near-match would pass
> unnoticed.

*Incidents — the first REACHED EXECUTION, the rest CAUGHT PRE-ISSUE.* A specification supplied a `GATES.md` blob id that was
fabricated; the author caught it only by reading the object. A required
phrase spanned a line break inside a blockquote, so no literal `grep`
could find it. The normalisation was then corrected for quote markers
and wrapping — **and still failed, because backticks remained.** The
same trap was met three times in one specification, each fix addressing
only the layer then visible.

*Why execution and not care.* Each of those was written carefully.
**Care does not distinguish a string that matches from one that nearly
matches; running the check does.**

## Amendment I (attached to Rule 8) — mid-task authority changes require reviewer-visible provenance

> **A specification author who amends a task mid-execution MUST record
> the amendment where the reviewers read.**
>
> **Narrative explanation does not itself create execution authority or
> governance status.** An account of why a change is reasonable is not
> the change's authorization.
>
> **The amendment MUST exist in a durable reviewer-visible record that
> is part of the task's issued authority** — at minimum an amended or
> re-issued specification, or another repository-defined amendment
> record cited by it. **Not a chat message the reviewer happens to see**,
> which is the thing this amendment exists to stop.
>
> **`DECISION_LOG.md` is additionally required only where the amendment
> itself creates or changes a programme-level decision or governance
> state.** A path typo, a manifest count, a corrected command syntax or
> a clarified acceptance criterion needs reviewer-visible authority
> **without entering the decision log** — and requiring it would both
> dilute that log and collide with any task whose scope does not
> authorize modifying it.
>
> **The record MUST identify what prior instruction is superseded, the
> replacement instruction, and the scope of that replacement.** Without
> those three, a reviewer can follow the reasoning and still not know
> which line of authority changed.

*Incident — REACHED EXECUTION.* Several specification corrections during this period were
communicated to the executor as narrative in the task conversation
rather than as amendments to the issued specification — most visibly
when a specification's stated scope count and its manifest disagreed and
the correction was explained rather than reissued. **The distinction
between explaining a correction and authorizing it had to be made
explicit so that a later reviewer could reconstruct which authority was
actually in force at execution time.**

## Amendment J (new) — integrations do not add epistemic or governance classifications

> **An integration, derivation, or any task that carries reviewed
> results forward MUST NOT add a governance or epistemic classification
> the reviewed results did not carry.**
>
> Recording what a result did not establish is required. **Assigning it
> to an open item, a gate, a status, or a category it was never assigned
> to is not.**

*Incident — CAUGHT PRE-ISSUE, not reached execution.* A draft
integration specification assigned three unresolved derivation inputs to
a governance item they had never been assigned to.
**That is the same act specifications forbid executors from performing**
— supplying a classification the evidence does not support — and **the
specification author, rather than the executor, introduced it.**
("Introduced", not "committed": the defect was corrected in draft and
never entered the repository.)

*Why these are separate rules.* The incident touches both, but a later
reader searching for "an integration may not classify" will not find it
under a heading about mid-task authority.

## Amendment K (attached to Rule 5) — re-issuing an executed specification

> **TASK-IDENTITY PATHS are paths whose names identify a particular
> execution instance** — ordinarily its specification and its report,
> plus any other path the specification explicitly designates as
> execution-specific. **Canonical target files are NOT task-identity
> paths.**
>
> **A specification that has already been executed and pushed MUST NOT
> be re-issued against the same branch while reusing the same
> task-identity paths.** A re-issue proceeds on a NEW branch cut from
> the evidence base, under a NEW task name and NEW specification and
> report `{HHMM}` paths.
>
> **Canonical target paths the task exists to populate or modify may
> remain the same** — an append-only log, a registry, a named
> derivation — **provided the new branch starts from the original
> evidence base and the re-issue specification explicitly authorizes
> them.** Only the paths that identify the task are required to change.
>
> **The original branch is preserved UNTOUCHED and is identified as
> superseded in the re-issue specification and report**; it is not
> rewritten, reset, force-pushed, or carried forward. **A Git branch ref
> carries no such marker, so the identification lives in the documents,
> not in the ref.**
>
> **A superseded branch MUST NOT be integrated.** `docs/BRANCHING_POLICY.md`'s
> authorization machine has `PENDING_DELETE`, `NOT_AUTHORIZED` and
> `ABSENT_FROM_REMOTE` and **no state for superseded, never to be
> integrated** — so a later integrator reading the branch list would see
> two branches claiming to land the same entries. **Either that state is
> added or this prohibition is stated where an integrator will meet it.**
> This is Amendment E(iii) again: a missing state forcing a
> conservative-but-wrong label.
>
> **Append-only and forbidden-delete are evaluated against the LAST
> PUSHED STATE OF THAT BRANCH, as well as against the evidence base.**
> A re-issue on a new branch starts from the original evidence base and
> **does not inherit the superseded branch's append-only history.** A record already
> pushed and then removed or replaced by a later commit is not
> append-only for the branch's operative content, **even though the old
> commit survives in Git history.** Evaluating only against a distant
> base would let any append-only file be rewritten by rebuilding it from
> that base.
>
> **Local iteration before a push is unaffected.** Committing a log
> entry and correcting a typo in it two commits later, before anything
> is pushed, is ordinary work and is not a violation. **An earlier draft
> said "immediate parent-to-child", which would have forbidden that.**
>
> **The re-issue mechanism is supplied by the specification, not derived
> by the executor.** A re-issued specification that does not say how the
> second execution is to be represented **is a specification defect**,
> and the executor's correct response is: **stop before the first
> irreversible or authority-expanding step; complete only those
> remaining observations or local checks that are independently
> authorised and do not alter protected or remote state; then report the
> unresolved construction for authorization.**
>
> **"Authorised" is the operative test, not "reversible".** Some
> read-only observations have no meaningful notion of reversibility, and
> some local commits are technically reversible while not being
> authorised at all.
>
> **A bare stop would have delivered nothing** — no entries, no
> register, no analysis of the collision. **What serves the PI is the
> full work, the conflict laid out, and the choice.** A rule that reads
> as "produce nothing when uncertain" teaches silence, which is the
> opposite of what this discipline is for.
>
> **This describes required behaviour; it does not create a named
> state.** If a formal `PARTIAL_STOP` state is wanted — with its own
> semantics for what may be committed, pushed and reported — **it should
> be defined deliberately elsewhere, not created in passing here.**

> **The general trigger, of which re-issue is one instance.** **If
> resolving an apparent inconsistency requires a construction the
> specification does not describe, that is a stop-before-push and a
> request for authorization — not a resolution.** Re-issue is the worked
> example below; the next instance will not be a re-issue.

*Incident — REACHED EXECUTION.* A specification was corrected and re-issued after its first
execution had been pushed. It named the same branch, the same task, and
the same paths, and it still said *create the branch from that commit* —
an instruction unexecutable against a branch that already existed. The
executor identified four mutually inconsistent requirements and, having
no guidance, **resolved them by adopting a new execution semantics:
base-to-head tree scope governs, so the same paths may be overwritten
and superseded records removed from the final tree.**

The two diffs on the resulting branch:

    evidence base -> head     256/0   193/0   972/0   357/0    no deletions
    first -> second issue      35/13   31/18  422/344   57/14    deletions

**Both describe the same tree.** The first satisfied every stated
criterion; the second is what happened.

*Where the fault lies.* **The executor should have stopped** — the
specification says so explicitly. **But it had nothing to follow,
because the re-issued specification did not say how a second execution
should be represented.** The defect originated with the specification
author.

*Why this is the umbrella principle again.* **Final-state scope
compliance is not a proxy for history-preservation or append-only
compliance.** This is the cleanest instance the programme has produced:
one tree, two diffs, one showing conformance and one showing violation.

## Amendment L (attached to Rule 9) — consumed conventions must be discoverable through the conventions index

> **A convention or decision that a computation CONSUMES MUST be
> discoverable from the governing conventions index, not only from a
> chronological decision log.**
>
> **The index may point to the authoritative ruling rather than
> duplicate it.** This requirement governs discoverability and
> provenance; **it does not prescribe the machine-readable storage
> format**, which remains an open design question.
>
> **Index discoverability does not by itself make prose a stable machine
> interface.** A computation that parses a convention must consume a
> representation **whose machine-facing identifier or lookup contract is
> explicitly governed.** The storage format and the synchronisation
> mechanism remain separate design questions.
>
> **The incident below has two layers. This amendment closes the
> governance obligation for BOTH, while leaving the machine-readable
> implementation of the second open**: a human should find the ruling
> from the conventions index; **and a script should not depend on
> mutable prose headings as a semantic API.** **Adding an index pointer
> does not by itself discharge the second obligation** — the lookup
> contract must still be governed, and how it is represented is the
> deferred design question.

*Incident — REACHED EXECUTION.* A script merged to `main` locates two PI
rulings by **exact `DECISION_LOG.md` heading text**. **A heading rename
would break a computation while changing no meaning.** The rulings are
genuine computational inputs — the script parses them, and mutation
tests confirm that removing or reversing either changes or halts the
result — **so the fragility is load-bearing, not cosmetic.**

*Why it is a rule and not a design note.* The finding was raised seven
times as a tidiness observation before a computation came to depend on
it. **The obligation — that a consumed convention be findable from the
index — holds whatever format the index eventually takes**, so deferring
it with the format would have deferred the part that is already
settled.

## New Rule 16 — accumulated reading

> **A task that adds a MATERIAL artifact bearing on a question already
> addressed by other authoritative or reviewable artifacts MUST state
> what the assembled set does NOT establish.**
>
> **"Material artifact, same question" is the trigger**, not "any
> artifact in any chain" — otherwise every report gains a boilerplate
> paragraph.
>
> **An integration task that brings previously separate artifacts into
> one authoritative branch MUST perform that assessment again against
> the MERGED state.**
>
> Individual artifacts may each be scrupulous while their accumulation
> reads as a stronger conclusion than any of them states. **The
> responsibility is two-layered**: the producing task assesses the local
> accumulated reading; **the integration task assesses the authoritative
> one**, because the strongest misleading inference sometimes becomes
> available only once separate branches sit on one `main`.
>
> **This does not require repeating every earlier limitation.** **At
> each required assessment, the responsible task must identify only the
> limitations whose omission would materially change the natural reading
> of the assembled evidence** — not reproduce every earlier caveat.
>
> **The assessment MUST name the junction or report a search.** Either
> name the artifact pair and the specific inference their combination
> makes available, **or state that a search was performed, describe it,
> and report that none was found.** Without this, "the accumulation was
> assessed" is unfalsifiable and every report gains a paragraph saying
> so. **The one finding this rule has actually produced came from
> hunting a junction — three artifacts, one named inference — not from a
> general assurance.**
>
> **"The responsible task", not "the latest artifact"**: an integration
> may produce only its own report, yet it is the task that owes the
> assembled-state assessment.

*Incident — REACHED EXECUTION.* Over two days, three PI rulings and four derivations landed
on the character of one interaction channel. Each withheld what it could
not establish. **The risk that emerged was not a wrong number but a
reader assembling "the vector channel is settled" from artifacts none of
which says it** — while the particle–particle channel, which is what the
downstream paper actually needs, had not been computed at all.

## Two things this amendment does NOT do

**It does not decide the machine-readable convention format or the
registry synchronisation mechanism.** The discoverability obligation
itself is Amendment L below; only the format is deferred.

**It does not address the harness-trailer conflict.** The executor's
tooling appends `Co-Authored-By` and a session URL by default, and every
task has suppressed them by hand. **Depending on each task remembering
is fragile**; the fix belongs to the execution environment, not to a
rule.

## Reviewer questions, and how this revision answers them

**Was one incident enough for Amendment G's layer-boundary clause?**
Yes, and the revision says why: the clause is **dependency-derived, not
frequency-derived**. A single demonstrated case in which a layer lacked
a premise required by its own output establishes a structural
violation; no second occurrence is needed.

**Should Rule 16's obligation sit with the newest task or the
integrator?** **Both**, and the revision splits them: the producing task
assesses the local accumulated reading, the integration task assesses
the authoritative merged one. **The strongest misleading inference is
sometimes available only after separate branches sit on one `main`**,
which no producing task can see.

**Should Amendment H require the executed check to appear in the
specification?** **Evidence, yes; raw output, not necessarily.** The
specification records the target, the normalisation, the method, and the
pre-issue PASS; raw authoring output may live in the review record.
**Where the literal is itself sensitive — a hash, a blob id, a
machine-consumed heading, or another identifier whose near-match could
pass unnoticed — the expected value and the executable verification
method are written out.**

## Why E and F remain separate rules

**They share the umbrella principle and address different defects, and
a later reader reaches them by different routes.**

**Amendment E is observation semantics** — *what did I actually
observe?* The error is mapping "not observed" onto "observed negative".
It constrains state vocabularies, exit-code interpretation, state
machines and measurement-failure handling. Someone meets it as
`--is-ancestor` returned 128 and something recorded "not merged".

**Amendment F is causal test adequacy** — *did this test verify the
dependency I claim?* The observation can be perfectly correct and the
test still worthless, because it never reached its target. Someone meets
it as *the mutation test passed, but the program exited before the
mutated value was read*.

**That second case is not an E problem at all.** The test successfully
observed that the program stopped; **it observed the wrong property.**
Merging the two would put it under a rule about observation states,
where nobody would look for it.

**The umbrella principle at the head of this document is what unifies
them.** They do not also need to be one rule.
