# Task specification — `D-1c`: non-mathematical dependency reduction of the reflection-positivity gaps

Specification evidence base: `ec85f66b05b3ed92cd924bc75273b74a73eee23b`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/d1c-dependency-reduction
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity, refs, branch availability
    A2  review binding
    A4  onward

**Criterion numbering is not execution order.**

---

## 0. The question, and the reason it is worth one task

**`D-1b` landed fifty-two entries.** **Fifty-two entries are not
fifty-two problems.**

**Many are repeated manifestations of the same underlying thing.** **If
twenty-five `UNFROZEN DATUM` occurrences rest on three or four
programme decisions, then a handful of `D-pre` rulings would clear most
of the apparent gap — with no mathematics at all.**

**That possibility is worth measuring before anyone commits to `B0`'s
seven-to-eleven constructions.**

**This task builds the dependency ledger and nothing else.**

## 1. What is in scope, and the asymmetry that decides it

    UNFROZEN DATUM         25 occurrences    IN SCOPE
    INCOMPATIBLE HYPOTHESIS 8 occurrences    IN SCOPE
    UNESTABLISHED BRIDGE   21 occurrences    OUT OF SCOPE
    UNDETERMINED            9 entries        OUT OF SCOPE

**The three tags do not reduce alike, and that is why two are excluded
rather than merely deprioritised.**

**`UNFROZEN DATUM` reduces by shared RULING.** Several entries may wait
on one decision the programme has not made. **Establishing that requires
reading the entries and the freeze documents — no mathematics.**

**`INCOMPATIBLE HYPOTHESIS` reduces by shared ESTABLISHED FACT.**
Several entries may rest on one thing the programme has already settled
— a dimension, an interaction form. **Also no mathematics.**

**`UNESTABLISHED APPLICABILITY BRIDGE` does NOT reduce this way.** **A
bridge is not waiting on a programme ruling; it is waiting on a
mathematical applicability bridge NOT ESTABLISHED IN THE PRESENT
REPOSITORY OR IN `D-1`'s FETCHED EVIDENCE BASIS.** **Determining whether
two such bridges are mathematically the same problem is outside this
task.**

**An earlier draft said a bridge waits on "a proof that does not
exist".** **Neither `D-1` nor `D-1b` established that.** **`D-1`'s
literature search was bounded and `D-1b` re-read nothing** — **what is
established is absence from the evidence basis, not absence from
mathematics.**

**`UNDETERMINED` entries are not classified at all.** **Grouping an
unclassified entry would assign it a classification by the back door.**

**Do not reduce `UB`. Do not reduce `UNDETERMINED`.** **Report their
counts and say they are out of scope and why.**

## 2. The grouping rule, and it is a hard boundary

> **A dependency may group entries ONLY when the same
> already-identified programme datum, or the same already-established
> incompatibility fact, controls them.**
>
> **Similar wording, a common source paper, or apparent mathematical
> similarity is INSUFFICIENT.**

**`D-1b` produced the case that shows why.** **`MP87`'s non-gauge
specialization appears for `Wilson` and for `naive` — same paper, same
phrasing — and the `Wilson` entry rests on `MP87`'s own site-reflection
theorem while the `naive` entry rests on its discussion of the earlier
link-reflection proof at `r=0`.** **Shared wording was not even shared
theorem there.**

**Every dependency node you create must name the datum or fact, and
point at where it is identified** — in `D-1b`'s classification, in a
freeze document, or in both. **A node with no anchor is not a node.**

## 3. What each node must carry

    NODE            the programme datum awaiting a ruling, or the
                    established fact
    KIND            RULING or ESTABLISHED FACT
    ANCHOR          where the datum or fact is identified, with file
                    and lines
    CONTROLS        every entry id the node controls, listed
    CANDIDATES      which of naive, Wilson, staggered, overlap are
                    touched
    STATUS          for a RULING node: whether the ruling is open, and
                    where the repository shows it open

**A `RULING` node asserts the programme has not decided something.**
**Verify that against the repository and report where you looked.**

**The four documents in §11 are a MANDATORY MINIMUM, not an exhaustive
authority set.** **All four must be inspected for every `RULING` node.**
**In addition, search `GATES.md`, the relevant entries of
`DECISION_LOG.md`, and any registered or frozen specification those
documents reference, for a LATER authoritative ruling.**

**A ruling made after an early derivation was written, and recorded
elsewhere, would otherwise read as open.** **The node count is exactly
what that error would inflate**, and this programme has repeatedly
recorded rulings in gates and decision entries rather than back into the
derivations they govern.

**`D-1b` established that `RP obligation frozen ≠ reflection type
frozen`, and that distinction cost six wrong tags when it was nearly
missed.**

**If a datum turns out to be already frozen, the node is not a `RULING`
node.** **Report it as a finding about `D-1b`'s classification** — **and
do not modify `D-1b`'s artifact.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not group `UB` entries**, and **do not judge whether any two
  bridges are the same mathematical problem.**
- **Do not group `UNDETERMINED` entries**, and do not classify them.
- **Do not reopen `W6` or `n6`.** **`D-1b` settled their programme-side
  status from `P2-LATTICE-ONTOLOGY-01.md` line 26 and retagged them
  `UB`.** **Re-deciding a completed determination would produce two
  inconsistent records of one question.**
- **Do not judge shared closure**, for any pair, in any tag.
- **Do not re-fetch any source**, and do not read any work `D-1` cited.
- **Do not design a lemma, a proof, or a construction.**
- **Do not estimate effort.** **A node is not a cost, and four nodes are
  not "four easy decisions".**
- **Do not select, eliminate, rank or prefer a candidate.** **A
  candidate whose entries collapse into fewer nodes is not better
  supported.**
- **Do not revise `B0`'s seven-to-eleven estimate**, and do not
  re-derive it.
- **Do not modify any existing file**, including `D-1b`'s classification
  and `D-1`'s tables.
- **Do not add a register entry anywhere.**

## 5. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**, and confirm it
identifies `zetacheng/2-emergent-gravity` — accept either URL form.
Fetch, then report `refs/remotes/origin/main` and confirm it is
`ec85f66b05b3ed92cd924bc75273b74a73eee23b`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.**

**Report whether `science/d1c-dependency-reduction` already exists.**
**If it does, STOP** — a second name is not this specification's to
choose.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** **Rule 13's diagnostic
order including Amendment D's step 0**: location, workspace depth,
package availability. **Report whether the clone is shallow and its
commit count.** **If a restoration is needed, report it in one line each
and confirm no repository content was touched.**

**A4 — The input inventory, re-derived from `D-1b`'s artifact.** Report
the per-tag totals and the per-candidate breakdown. **Expected: `UD` 25,
`IH` 8, `UB` 21, `UNDETERMINED` 9; 52 entries, 54 occurrences, 11
multi-tag.**

**Count from the per-entry tables, NOT by whole-file grep.** **Measured
in the previous task: a whole-file grep returns 6, 6, 6 and 13 against
the true 25, 8, 21 and 9**, because the artifact defines its own
vocabulary and the grep counts definitions and denials. **This is the
third occurrence of that shape in this line.** **Report both figures if
you run both, and say which governs.**

**A5 — The `UD` reduction.** Report every `RULING` node with all six
fields of §3.

**Every one of the 25 `UD` occurrences is DISPOSITIONED EXACTLY ONCE, as
one of three:**

    1  assigned to a VERIFIED-OPEN RULING node — including a node it
       alone controls, where nothing shared controls it
    2  CLASSIFICATION FINDING — ALREADY FROZEN
    3  CLASSIFICATION FINDING — PROGRAMME STATUS NOT DETERMINABLE

**ONLY category 1 enters the reduction ratio.**

**Report the decomposition:**

    25 = N_mapped + N_frozen_finding + N_undetermined_finding

**and then the ratio: `N_mapped` occurrences to `N_ruling` nodes.**

**If the two finding counts are zero, the decomposition reduces to `25 →
N` and you say so.**

**An earlier draft required every occurrence assigned to a `RULING`
node, which contradicted §3 and `A7`**: those permit an occurrence's
datum to turn out already frozen, and forbid such a node from being a
`RULING` node. **A specification with no legal path through an outcome
it expressly permits is defective, and this is the repair.**

**A6 — The `IH` reduction.** The same, for all 8 `IH` occurrences, with
`KIND` = `ESTABLISHED FACT`. **Report the node count and the mapping.**

**A7 — Every `RULING` node verified against the repository**, per §3.
Report, per node: **the datum; the four mandatory documents checked; ANY
ADDITIONAL AUTHORITATIVE SOURCE found and searched — `GATES.md`,
`DECISION_LOG.md`, a registered specification; the files and lines
consulted; and whether the repository shows the datum open.**

**Report explicitly, per node, that all four mandatory documents were
checked**, and **report any node whose status was settled by a source
outside the four.**

**Report status counts at TWO LEVELS, which are different quantities and
must not be equated.**

**Dependency/datum level — counting proposed dependencies:**

    N_ruling                  verified open, and therefore RULING nodes
    N_proposed_frozen         proposed dependencies found already frozen
    N_proposed_undetermined   proposed dependencies whose programme
                              status could not be determined

**Occurrence level — counting `UD` occurrences, per `A5`:**

    N_mapped   N_frozen_finding   N_undetermined_finding

**Report both sets, and report the MAPPING between them** — which
proposed dependency accounts for which occurrences. **Confirm the
occurrence-level figures reproduce `A5`'s decomposition of 25.**

**DO NOT require the two sets to be numerically equal.** **One rejected
datum may control several occurrences**: three entries resting on one
datum that turns out already frozen give `N_proposed_frozen = 1` and
`N_frozen_finding = 3`. **An earlier draft asked for the datum-level
counts to "reconcile with" `A5`'s occurrence-level decomposition without
saying which unit each counted**, which is unsatisfiable whenever a
rejected datum controls more than one entry.

**Reconciliation means the mapping accounts for every occurrence exactly
once, not that the totals match.**

**Report any node whose datum turns out already frozen**, as a finding
about `D-1b`'s classification. **Zero is an acceptable answer.**

**A8 — The grouping rule honoured, demonstrated not asserted.** For
**every node controlling more than one entry**, report **the shared
datum or fact by name**, and **confirm the grouping does not rest on
wording, source paper, or apparent similarity.**

**Report any pair of entries you considered grouping and did not**, with
the reason. **`MP87`'s two entries are named in advance as the case that
motivated the rule** — **report whether they ended up in one node or
two, and why.**

**A9 — Out-of-scope tags reported and not reduced.** **Report the `UB`
count and the `UNDETERMINED` count**, and **confirm neither was grouped,
classified, or judged.** **State §1's reason in your own words.**

**A10 — No sizing, no selection, no closure judgement.** **Search the
artifact, the report and the commit messages for any sentence that
estimates effort, ranks candidates, prefers one, judges two bridges the
same, or describes how a ruling would be made.** **Report the search and
the finding.**

**Report the per-candidate treatment length**, and **whether it differs
and why** — entry counts differ by a factor of two, **so unequal
treatment is expected and must be explained rather than levelled.**

**A11 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: ec85f66b05b3ed92cd924bc75273b74a73eee23b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
      reports/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md
      specs/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **`modify:` is empty and §8
limits executor-writable paths to this specification, its review, its
report, and the ledger.** **`DECISION_LOG.md` is not among them.** **If
the two ever appear to conflict, §8 governs and you stop and report.**

**Measure the UTC time and use the value you measured.** **The previous
task's token was forty-four minutes early, found by its own author, and
preserved because rewriting pushed history to fix a filename costs more
than it returns.**

**A12 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, all six microspec artifacts, the four
documents named in §11, both registers, and everything under `scripts/`,
`tests/` and `results/`.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.** **Read the status
line SCOPED to its gate section** — a bare grep's first hit is a
different gate.

**A14 — The checker over this task's own range**, base `ec85f66b…`,
head **commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming
only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4.

**A15 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A16 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
    commit 4  reports/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A13, A15 and A16;
**A14's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A11's final scope stated
as INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **A node count is not a workload.** **If twenty-five
occurrences collapse to four nodes, four rulings are still four
decisions the PI has not made, on questions the programme has not
framed.** **Say that a low node count means fewer distinct questions,
not easier ones.**

**Second, and it is the largest thing this task does not do.** **The
twenty-one `UNESTABLISHED APPLICABILITY BRIDGE` occurrences are
untouched.** **Nothing here establishes how many independent bridges
they represent** — **one, twenty-one, or anything between** — **and
establishing it needs mathematics this task is forbidden.**

**Say that those bridges are NOT ESTABLISHED IN THE PRESENT EVIDENCE
BASIS**, and **do not say they do not exist.** **Report the count beside
the reduction so no reader takes a reduced `UD` figure for a reduced
total.**

**Third.** **This rests on `D-1b`'s classification, which rests on
`D-1`'s tables, whose literature search was bounded.** **A gap absent
from `D-1`'s tables is absent from this ledger.** **Three layers, each
bounded, and the bounds compose.**

**Fourth.** **A `RULING` node says the programme has not decided
something. It says nothing about what the decision should be.** **The
node's existence does not make the ruling easier, and the ledger must
not read as a to-do list.** **Say so.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  dependency ledger. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not group, judge, size, select, or design.**
- **Push only this task's branch.** **No session branch, no `D-1`,
  `D-1b` or other branch, and not `main`.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's re-derived inventory**, with the grep figures if you ran them
  and which governs;
- **A5's `RULING` nodes with all six fields, the three-way decomposition
  of all 25 occurrences, and the ratio over category 1 only**;
- **A6's `ESTABLISHED FACT` nodes and the full 8-to-N mapping**;
- **A7's per-node verification**: the four mandatory documents checked,
  any additional authoritative source searched, files and lines, **the
  THREE DATUM-LEVEL counts and the THREE OCCURRENCE-LEVEL counts
  reported separately**, and **the mapping between them accounting for
  every occurrence exactly once**;
- **A8's shared datum or fact per multi-entry node, and the pairs
  considered and rejected including `MP87`'s two entries**;
- **A9's out-of-scope counts and the reason in your own words**;
- **A10's search, finding, and per-candidate treatment lengths**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **§7's four Rule 16 junctions**;
- **whether reducing made you want to group a `UB` pair, size a node, or
  say which ruling should be made.** **Say which and why, and confirm
  you did not** — **the previous executor reported that the easiest
  boundary to cross is writing a figure while believing you are only
  describing someone else's task**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the evidence base and the artifact this task reads
    method      git fetch; git rev-parse origin/main; git rev-parse
                <rev>:<path>
    MEASURED    origin/main = ec85f66b05b3ed92cd924bc75273b74a73eee23b.
                derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
                is present at blob 66d5087ae6b0.

    target      the documents a RULING node must be anchored in
    method      git rev-parse <rev>:<path> for each
    MEASURED    P2-LATTICE-ONTOLOGY-01.md 6544fb1a72;
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md 0be773f6a5;
                P2-LATTICE-ROUTE-01.md 42be438ff1;
                P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
                0b227206f3. All four present. The fourth is included
                because the previous executor reported that r and M_0
                are settled only there, not in the three usually named.

    target      the tag totals
    method      NOT MEASURED by this author. 25 / 8 / 21 / 9, 52
                entries, 54 occurrences and 11 multi-tag are the
                previous executor's figures, re-derived by it from the
                per-entry tables and verified against the relation
                (52 - 9) + 11 = 54. A4 requires them re-derived again.

    target      whether a whole-file grep can be used for A4
    method      grep -oE for the four tag names over the classification
                artifact
    MEASURED    it CANNOT. The previous task reported 6, 6, 6 and 13
                against the true 25, 8, 21 and 9, because the artifact
                defines its own vocabulary. A4 states this so the
                obvious method is not attempted as if it were valid.

    target      W6 and n6
    method      D-1b's landed finding and P2-LATTICE-ONTOLOGY-01.md
                line 26
    MEASURED    the line places gauge bosons among emergent objects, so
                the microscopic action's non-gauge status is settled.
                D-1b retagged both entries UB on that basis. 4 forbids
                reopening them.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.

## 11. The four mandatory freeze documents

    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    derivations/P2-LATTICE-ROUTE-01.md
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md

**The fourth is named because the previous executor found that `r` and
`M_0` are settled only there.**

**These four are a MANDATORY MINIMUM. They are not the complete set of
places a ruling may live.** **`A7` additionally requires `GATES.md`, the
relevant `DECISION_LOG.md` entries, and any registered or frozen
specification referenced by these documents to be searched for a later
authoritative ruling**, and **requires the files consulted reported per
node.**
