# Task specification — `C-c`: an authoritative register for governance debt

Specification evidence base: `80595d4cd575d1d024d1415b9b599947bf847677`

    Branch to create   governance/debt-register-cc
    Cut from           authoritative main @ 80595d4c…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**It records. It repairs nothing, builds nothing, and obliges nobody.**
**Every item in it is already known**; what it lacks is a place a reader
meets it. **`D3` in its own list is exactly that failure**, and a
register nobody finds would reproduce it.

---

## 0. Why a register, and why it is not a rule

**Measured at the evidence base: there is no governance-side register.**
Two registers exist and both are science-side —
`derivations/P2-DEFERRED-ITEMS.md`, whose own text says entries are added
by PI decision, and
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, created by `C3` for the
C-check line.

**Governance debt has been carried in task reports.** **A report is a
record of one task**; nothing aggregates them, and **three of the items
below were found only because a later task tripped over them.**

**The register creates no obligation.** Like the consolidation record
`C-a` landed, **it must state that nothing in it binds**, and the PI's
ruling on that record governs here too: **it may record what rules,
amendments and reports already carry, and must not create, modify or
explain any new obligation.**

## 1. The file, and one pointer so it is findable

**Create `docs/GOVERNANCE-DEBT.md`.**

**Modify `CONVENTIONS.md` by adding ONE pointer line** to the
consolidation record `C-a` landed, naming the register's path and saying
what it is. **Nothing else in `CONVENTIONS.md` changes.**

**The pointer is required, and the reason is in the register itself.**
**`D3` records that a correction and the thing it corrects landed
together with nothing linking them.** **A register reachable only by
knowing it exists is the same defect**, and `C-c` must not commit it
while recording it.

**`CONVENTIONS.md` is not pinned by any gate** — verify that rather than
assume it, per Rule 19; **if it were, this task would owe a re-pin.**

## 2. What goes in, and what does not

**Eleven entries. Each records what is known, what is not, and where the
evidence sits.**

    G-01  The executor harness conflicts with P6.
          Generic git guidance adds Co-Authored-By and a session URL;
          P6 forbids both. Recurs on every task. Outside the repository
          and not repairable inside it. Currently caught by a criterion
          each specification must remember to write.

    G-02  scripts/p2_phase01_scalar_exploratory.py line 73 reads
          "for the frozen Wilson D". The canonical lattice Dirac
          operator is NOT frozen; the docstring is the conflation the
          AC-4 determination rejects. REPAIRABLE: one line, blocked
          only by scope — no task has been authorised to touch
          scripts/.

    G-03  Correction discoverability. A false MEASURED line and its
          correction landed in the same merge with no pointer between
          them; the shape recurred. An executor proposed a
          repository-level CORRECTIONS.md keyed by path:line. The
          reservation on record: nothing would keep such a file
          updated.

    G-04  Nothing requires a newly issued SCOPE-BEARING specification
          to carry stated:. P1 refuses a scope block without one, but
          that refusal is exercised only when the specification is
          actually selected as a P1 subject. The classification calls
          this C2. Measured: 13 of 50 specifications carried stated: at
          f179b45e, and the 13 were exactly those issued after the
          grammar landed.

          THIS ENTRY IS ABOUT stated: ALONE. append_only: and
          authorised_gates: are not folded in: C-b established them as
          a declaration mechanism in which DECLARED_EMPTY is a valid
          and meaningful state, so whether a given task needs either
          depends on the task. An earlier draft of this specification
          merged all three under one entry and cited C2 for the whole,
          which is accurate only for stated:.

    G-05  No mechanism compares a review's cited specification digest
          against the specification committed beside it. Amendment N(b)
          states the obligation; nothing checks it. Fully specifiable
          inside the repository.

    G-06  No mechanism performs the auto-merge line-survival check.
          Amendment P(b) states the obligation; it has been measured by
          hand, once, by an executor beyond its criterion. Fully
          specifiable inside the repository.

    G-07  The mechanism-marker vocabulary is defined only in the
          non-binding consolidation record. The binding rules use the
          markers; the one sentence explaining what MECHANISM DEFERRED
          means sits in the record. The PI has ruled this acceptable
          because a marker is an annotation and not a requirement.
          Recorded so a later reader knows it was decided rather than
          overlooked.

    G-08  Acceptance criteria can make unchecked factual assertions
          about the specification artifact itself. A pre-issue
          verification record checks literals against the repository;
          it does not check what a specification asserts about its own
          bytes. Instance: C-b's A13 asserted its own scope block
          declared append_only and authorised_gates; it declared
          neither. A narrower subtype of the classification's C4.

    G-09  Nothing independently validates the shared gate-heading
          grammar against an external or separately maintained
          statement of the accepted heading language. C-b removed the
          divergence: there is now one helper, not two production
          grammars. What remains is common-mode failure — the helper
          and everything asserting it is correct derive from one
          author's reading of what a gate heading is. The residual of
          C1, which is otherwise closed.

          An earlier draft said "nothing detects them drifting
          together", which reads as though two grammars still existed
          and could drift. They do not. The problem is the absence of
          an independent oracle, not divergence.

    G-10  Nothing detects a guard going vacuous. The pin validator
          asserts it found at least one pin; P7 asserts parsed sections
          equal the raw count. Both guards were written by the hand
          that wrote the thing they guard. The classification calls
          this C5. Naming the regress is not solving it.

    G-11  A hand-written probe that contradicts an existing check is
          more likely to be wrong than the check. Instance: a pin probe
          read a field name the collector does not emit and printed
          MISMATCH for two pins that a landed test had already passed
          on. Method note, not a defect in the repository.

**One item is NOT entered, and the omission is deliberate.** The
classification's `D4` — the unresolved mechanism behind the bit-exact
mirroring — **is already registered as `OPEN-CC-3` in
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`.** **Cross-reference it;
do not duplicate it.** **A second entry would create a second place for
its status to drift.**

**`C1` and `C3` are not entered as open debt.** They landed. **Their
residuals are `G-09` and `G-04`** and are entered as those.

## 3. Each entry carries a disposition

**One of:**

    REPAIRABLE            a repair is known and blocked only by scope;
                          name what blocks it
    SPECIFIABLE           the mechanism is fully specifiable inside the
                          repository and none exists; name the
                          obligation it would enforce
    NOT REPAIRABLE HERE   the cause lies outside the repository
    RULED                 a PI ruling settled it; name the ruling
    METHOD NOTE           a practice, not a defect
    OPEN                  none of the above

**Do not mark anything CLOSED.** **Nothing in this register is closed by
being written down**, and an entry that reads as resolved would be the
false green this whole line of work exists to prevent.

**`SPECIFIABLE` requires a mechanism SHAPE, not merely a belief that one
could exist.** `G-05` and `G-06` have one: compare a cited digest against
a committed blob; measure line survival across a merge. **`G-09` and
`G-10` do not** — an independent oracle for a grammar, and a detector for
a vacuous guard, are both problems whose shape is not yet defined.
**`OPEN` is the expected disposition for those two**, and **if you assign
`SPECIFIABLE` to either, state the mechanism shape you have in mind**
and expect it to be challenged. **`C5`'s own record says naming the
regress is not solving it.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not repair any item.** Not `G-02`, which is one line and
  tempting.
- **Do not build `G-05` or `G-06`.** They are `SPECIFIABLE`, which
  means specifiable, not specified.
- **Do not create a `CORRECTIONS.md`**, and do not decide `G-03`.
- **Do not modify `GATES.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md`, or anything under `scripts/`, `tests/`,
  `results/` or `derivations/`** — including the two existing registers.
- **Do not add a numbered rule or an amendment.** The register binds
  nobody and `CONVENTIONS.md` gains one pointer line and nothing else.
- **Do not enter `D4`.** Cross-reference `OPEN-CC-3`.
- **Do not describe the governance gap as closed or as measured.**
  §7 governs.

## 5. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`80595d4cd575d1d024d1415b9b599947bf847677`. Report the Git blob ids of
`CONVENTIONS.md`, `derivations/P2-DEFERRED-ITEMS.md` and
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`. **Any ref mismatch →
STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank or naming a different digest, STOP and say
which.** Report both digests equal.

**A3 — Eleven entries, each with exactly one disposition.** **Report the
list with its disposition**, and **the count of each disposition.**
**An entry with none, or with two, is a STOP.** **No entry may read
`CLOSED`.**

**A4 — Each entry's evidence located.** For every entry, **name the task
report, specification or repository path where its evidence sits**, and
**verify that reference resolves at the evidence base.** **Report any
that does not.** **An entry whose evidence cannot be located is a
finding: record it as such rather than dropping it.**

**A5 — `G-04`'s figure re-measured, not quoted.** §2 states 13 of 50 at
`f179b45e`, **for `stated:` alone.** **Measure it again at THIS evidence
base and report both numbers**, and **confirm you measured `stated:` and
not the three keys together.** **They will differ, because
specifications have landed since** — **report the current figure and say
which revision each belongs to.**

**Also report, separately and without entering it in the register, how
many specifications at this base carry `append_only:` and
`authorised_gates:`.** **Whether their absence is debt is undecided**,
and §2 says why it is not folded into `G-04`. **Report the numbers as a
finding; the register stays at eleven entries.**

**A6 — `D4` is cross-referenced and not duplicated.** Report that
`OPEN-CC-3` exists in
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` at the evidence base,
**that the register points at it**, and **that
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` is byte-identical at base
and head.**

**A7 — The register states that nothing in it binds.** Report the
sentence. **Report the count of lines in the new file containing `MUST`,
`SHALL` or `binds`** — **and if that count exceeds the one sentence
saying nothing binds, name each and justify it**, per the PI's ruling on
the consolidation record.

**A8 — The pointer, and `CONVENTIONS.md` changes in no other way.**
Diff `CONVENTIONS.md` base to head and **report it in full.** **Exactly
one region added.** **Zero deleted lines**, and **the base file is an
exact in-order subsequence of the head file** — report the matched count
against the base line count. **These are two independent measurements of
one property, and neither substitutes for the other.**

**Report the rule and amendment counts at the head: twenty-one rules,
fifteen amendment letters A–P, no `J`** — unchanged, because this task
adds neither.

**A9 — Scope, frozen manifest.**

    stated: 4 additions, 1 modification
    append_only: DECISION_LOG.md
    authorised_gates: []
    base: 80595d4cd575d1d024d1415b9b599947bf847677
    head: <commit 4>
    mode: exact
    add:
      docs/GOVERNANCE-DEBT.md
      reports/2026-08-XXT{HHMM}Z_debt-register-cc.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_debt-register-cc.md
      specs/2026-08-XXT{HHMM}Z_debt-register-cc.md
    modify:
      CONVENTIONS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Five paths.**

**A10 — Protected paths.** Every path existing at the evidence base other
than `CONVENTIONS.md` is blob-identical at the head. **In particular
`GATES.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`, both existing
registers, and everything under `scripts/`, `tests/` and `results/`.**
Compare path by path and report the count.

**A11 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets**, and **`CONVENTIONS.md` is
named by neither.** **Report all five.**

**A12 — The checker over this task's own range**, base `80595d4c…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_debt-register-cc.md

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**This specification's scope block declares the same two sets, and they
are written to agree.** **Report `declared_source` for each** and
**confirm no `DECLARATION_CONFLICT` arose.**

**`register_path` names `docs/BRANCHING_POLICY.md` and NOT the new
file.** **`P4` checks the superseded-branch register; `docs/GOVERNANCE-DEBT.md`
is not that register and this task does not make it one.** **Say so in
the report** — two files with `register` in their description is exactly
the kind of adjacency that produces a wrong reading later.

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A12-final, post-report evidence:** re-run RUN 2 at commit 4.

**A13 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected: unchanged at 324 passed, 2 deselected** — this task adds no
test. **A change is a finding and must be explained.**

**A14 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Report what happened per commit.** **Commits 1–3 go in the
report; commit 4 is post-report evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_debt-register-cc.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_debt-register-cc.md
    commit 3  docs/GOVERNANCE-DEBT.md
              CONVENTIONS.md
    commit 4  reports/2026-08-XXT{HHMM}Z_debt-register-cc.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **The register and its pointer
move together in commit 3** — a commit carrying one without the other
would land either an unreachable register or a pointer to nothing.

**Committed report — measured at commit 3:** A1–A11, A13 and A14;
**A12's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A9's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A9's final scope measured
base-to-commit-4; A12-final; A13 at commit 4; A14 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** After this lands, governance debt has a home. **A reader may
take a register for progress on the debt.** **Nothing in it is repaired
by being written down.** **Report the disposition counts**, and **say
that `SPECIFIABLE` means specifiable and not specified.**

**Second.** **This register is a list of what was noticed.** Three of its
entries were found only because a later task tripped over them. **The
absence of an entry is not evidence that the corresponding debt does not
exist.** **A list assembled by noticing is not a survey**, and **this
task does not perform one.**

**Third.** **The register itself has no mechanism.** Nothing requires an
entry to be added when debt is found, nothing checks that entries stay
current, and **`G-03`'s reservation applies to this file as much as to
the `CORRECTIONS.md` it describes.** **Say that plainly**, and **do not
build the mechanism here.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report,
  `docs/GOVERNANCE-DEBT.md`, and one pointer region in `CONVENTIONS.md`.
  **Nothing else.**
- **No deletion from `CONVENTIONS.md`, for any reason.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not mark any entry CLOSED**, and **do not add a twelfth entry**
  without reporting it as a finding first — **if you find debt this
  specification missed, report it and leave it**, because a register that
  grows during its own creation has no frozen scope.
- No force-push, no history rewrite, no branch deletion **except as Rule
  20 permits**.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's eleven entries with dispositions and the count of each**;
- **A4's evidence location per entry**, and any that failed to resolve;
- **A5's two figures for `G-04`**, each with its revision;
- **A6's cross-reference confirmation and the byte-identity of the
  C-check register**;
- **A7's sentence and the binding-vocabulary line count**;
- **A8's full `CONVENTIONS.md` diff**, the zero-deletion count, the
  subsequence match, and the unchanged rule and amendment counts;
- **A10's path count**;
- **A11's five checks**;
- **A12's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and **the statement distinguishing
  `docs/GOVERNANCE-DEBT.md` from the superseded-branch register**;
- **A13's counts**;
- **whether writing the register made you want to repair `G-02`.**
  **Say so, and confirm you did not**;
- **§7's three Rule 16 junctions**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.** **This record covers facts about the repository AND facts
this specification asserts about itself.** **The second kind is here
because `C-b`'s `A13` asserted something false about its own scope block
that no verification record checked.**

    target      existing registers
    method      git ls-tree over derivations/ and the whole tree at
                80595d4c, filtered for register-like names
    MEASURED    TWO, both science-side:
                derivations/P2-DEFERRED-ITEMS.md, whose own text says
                entries are added by PI decision; and
                derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md, 97
                lines, carrying OPEN-CC-1, OPEN-CC-2 and OPEN-CC-3.
                THERE IS NO GOVERNANCE-SIDE REGISTER.

    target      whether D4 is already registered
    method      read the C-check register's headings
    MEASURED    OPEN-CC-3 is "the mechanism of the bit-exact mirroring
                is unresolved" — the classification's D4. §2 therefore
                cross-references rather than duplicating, and an earlier
                plan that listed D4 for entry would have created a
                second place for one status to drift.

    target      whether CONVENTIONS.md is pinned
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md and read the
                path above each
    MEASURED    TWO pins, naming the adopted parameter-domain artifact
                and the adopted admissibility contract. NEITHER names
                CONVENTIONS.md. No re-pin is owed, and A11 requires that
                verified rather than assumed.

    target      G-04's figure
    method      count .md files under specs/ and those carrying a
                'stated:' record, at f179b45e
    MEASURED    13 of 50 at f179b45e. NOT RE-MEASURED at 80595d4c by
                this author; A5 requires the executor to do so, because
                specifications have landed since and the figure will
                have moved.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. Both declarations are
                present, and A12 checks them against the committed bytes
                rather than trusting this line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                80595d4c and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 1 modification;
                the manifest lists four and one; parse OK, counted
                equals stated per category.
