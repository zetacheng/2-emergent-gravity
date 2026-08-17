# Task specification — integrate the reflection-positivity dependency ledger, and land it

Specification evidence base: `ec85f66b05b3ed92cd924bc75273b74a73eee23b`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-d1c-ledger
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/d1c-dependency-reduction
                       cdbfa6b9…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§7 carries the landing clause; **no second task is required.**

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**Criterion numbering is not execution order.**

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`ec85f66b…`, **6 additions and 0 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**Nothing is modified.**

---

## 0. What lands

    25 UNFROZEN DATUM occurrences  →  5 RULING nodes         25 = 25+0+0
     8 INCOMPATIBLE HYPOTHESIS     →  2 ESTABLISHED FACT       8 =  4+4
    21 bridges + 9 undetermined    →  UNTOUCHED

    R1  canonical kinetic operator and its parameters      controls 5
    R2  admissible lattice extent / finite volume          controls 8
    R3  boundary conditions, temporal                      controls 5
    R4  microscopic variables, state space, measure        controls 5
    R5  internal multiplicity N                            controls 2
    F1  H(4) is four-dimensional                           controls 4
    F2  frozen U(N)_L×U(N)_R generator sum, G>0            controls 4

**Datum level 5 / 0 / 0; occurrence level 25 / 0 / 0** — different
units, not equated, mapping accounts for all 25 exactly once.

## 1. Three things this landing must lock, because each is a reading a
## reader will otherwise take

**These are not caveats appended to a result. They are part of the
result, and the source executor stated all three unprompted.**

### 1a. Five is an ADOPTED GRANULARITY, not a measurement

**The source report's own first sentence about the figure:**

> **the five-node figure is a judgement, not a measurement**

**`R1` groups `r`, the mass and hopping domain, `M_0` and the staggered
phases as constituents of ONE delegated datum**, on `ONTOLOGY:189` and
the dossier's words *part of the choice this dossier does not make*.
**Split them and the total is EIGHT nodes over the same 25
occurrences.** **Both readings are in the landed ledger.**

**Write it as:** *under `D-1c`'s adopted programme-dependency
granularity, the 25 `UD` occurrences reduce to five `RULING` nodes; a
finer constituent-level decomposition, explicitly recorded by `D-1c`,
would yield eight nodes over the same 25 occurrences.*

**Do not write `25 → 5` as a granularity-independent fact.**

### 1b. `CONTROLS` is accounting, NOT intervention effect

**`k8` names two data — "finite even extent and boundary data" — and the
exactly-once rule forces it into `R2`.** **It depends on `R3` as well.**

**So a `CONTROLS` count is not the number of entries that closing that
ruling would retire.** **`D-1c` built a dependency-accounting partition,
not an intervention-effect model.**

    WRONG   freezing R2 would eliminate eight gaps
    RIGHT   eight UD occurrences are borne by R2 as their primary
            dependency node under D-1c's exactly-once accounting

**The source executor reported this as a bias its own bookkeeping
introduces, in `R2`'s favour, without being asked.** **Report it in
those terms.**

### 1c. A node count is not a question count

**"Five open programme questions" is a granularity-dependent
statement**, and §1a is why. **`R1` alone decomposes into four
constituents, and `R5`'s relation to the species ledger is itself
unsettled.**

**Report the node count as a node count.** **Do not restate it as a
number of questions, decisions, or problems.**

## 2. The check that makes the grouping rule non-circular

**§2 of the source specification forbade grouping on shared wording, a
common source paper, or apparent similarity.** **Whether that rule was
followed or merely asserted is testable, and the source executor tested
it:**

**`MP87`'s eight `UD` occurrences all group with `FG26` and `KU10`
entries rather than with each other.** **`R2`, `R3` and `R4` each span
three different papers.** **The grouping cuts ACROSS papers, not along
them.**

**Had the grouping run along papers, that would have been evidence the
rule was being satisfied in name only.** **Re-derive this and report
it** — **it is the only empirical confirmation that the hard boundary
held.**

**`MP87`'s `W6` and `n6`, named in advance as the motivating case, are
in neither one node nor two: they are `UB` and out of scope entirely.**
**Report that.**

## 3. What this does NOT establish

- **The 21 `UNESTABLISHED APPLICABILITY BRIDGE` occurrences are
  untouched.** **Nothing establishes whether they are one bridge or
  twenty-one.** **The reduction covers 33 of 54 tag occurrences.**
  **Report the 21 beside the reduction so no reader takes a reduced `UD`
  figure for a reduced total.**
- **The 9 `UNDETERMINED` entries are not classified and were not
  grouped.**
- **`B0`'s seven-to-eleven construction estimate is unchanged** and is
  not re-derived here.
- **No candidate is selected, eliminated, ranked or preferred.**
- **No ruling is made, ordered, or recommended.** §4 governs.

## 4. What this task must not do

- **Do not touch `main` until §7's landing.**
- **Do not modify any file**, including `D-1`'s tables, `D-1b`'s
  classification, and `D-1c`'s ledger.
- **DO NOT ORDER `R1`–`R5`.** **Do not say which could be decided
  first, which depends on which, or which is independent.** **That is
  the next task and this one does not scope it.**
- **Do not make, recommend, or indicate a preference for any ruling.**
- **Do not group any `UB` pair**, and do not judge whether two bridges
  are the same problem.
- **Do not classify any `UNDETERMINED` entry.**
- **Do not estimate effort**, and **do not state how many gaps a ruling
  would retire** — §1b forbids it.
- **Do not select a candidate.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`, accepting either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`ec85f66b05b3ed92cd924bc75273b74a73eee23b`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.** Report the source at
`cdbfa6b9…` and **that it is not an ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0: location, workspace depth, package
availability. **Report whether the clone is shallow and its commit
count.** **Any restoration reported in one line each, with confirmation
that no repository content was touched.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 `cdbfa6b9…`, merge-base the
evidence base. **Commit 1 must be an ancestor of parent 1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The seven nodes, re-derived from the arriving ledger.** Report
each node's datum or fact, its anchor, its controlled entries, and its
status. **Report the two decompositions — datum level and occurrence
level — as separate figures**, and **confirm the mapping accounts for
all 25 `UD` and all 8 `IH` occurrences exactly once.**

**A7 — The anchors verified against the repository, not the ledger, and
LEXICAL HITS DISTINGUISHED FROM RULINGS.**

**For every search you run, report the LEXICAL HIT COUNT and, for every
non-zero count, the DISPOSITION AFTER READING each hit.** **These are
different figures and both are reported.**

**Do not report a lexical-hit count of zero unless you measured zero.**
**Measured by the Researcher: `DECISION_LOG.md` returns three lexical
hits for `measure`, none of which is a ruling.** **The source's "zero on
every term" is correct as a statement about rulings and imprecise as a
statement about hits.** **Report both, and do not collapse them.**

**The core assertion of `D-1c` is that no later ruling exists for
`R1`–`R5`.** **That assertion survives only if lexical absence and
ruling absence are kept apart.**
For each of `R1`–`R5`, **open the anchor lines and confirm they say what
the ledger reports.** **Report the file, the lines, and what you read.**

**Two are stated here as the Researcher measured them, and both must be
re-read rather than accepted:** `ONTOLOGY:189` reads
`| Canonical kinetic operator and species accounting | DELEGATED: D-pre …|`;
`ROUTE:192-193` reads *the subtraction / reference-equivalence class;
finite-volume and thermodynamic rules; boundary conditions.*

**Report that `R2` and `R3` are named in that one semicolon-separated
sentence and were kept as two nodes.** **Grouping them would have made
five nodes four on the strength of punctuation.**

**A8 — §1a, §1b and §1c transcribed.** Report all three, **in the form
§1 gives**, and **confirm the report contains no sentence writing
`25 → 5` as granularity-independent, no sentence stating how many gaps
closing a node would retire, and no sentence calling the node count a
number of questions.** **Search for each and report the search.**

**A9 — §2's cross-paper check, re-derived.** Report **which papers each
of `R2`, `R3`, `R4` spans**, and **that `MP87`'s eight `UD` occurrences
group with `FG26` and `KU10` entries rather than with each other.**
**Report that `W6` and `n6` are `UB` and out of scope.**

**A10 — The `k8` double dependency, transcribed.** Report **that `k8`
names two data, that exactly-once accounting placed it in `R2`, that it
depends on `R3` as well**, and **that the source executor reported this
bias in `R2`'s favour unprompted.**

**A11 — Out-of-scope counts.** **21 `UB`, 9 `UNDETERMINED`, 33 of 54 tag
occurrences covered.** **Confirm none was grouped, classified or
judged.**

**A12 — Scope, frozen manifest. Final base-to-head: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: ec85f66b05b3ed92cd924bc75273b74a73eee23b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
      reports/2026-08-17T0322Z_d1c-dependency-reduction.md
      reports/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
      reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
      specs/2026-08-17T0322Z_d1c-dependency-reduction.md
      specs/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately, and state whether they coincide** — **they do, at four.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **`modify:` is empty and §8
limits writable paths.** **If they appear to conflict, §8 governs; stop
and report.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Report which head each figure was measured at.**

**Measure the UTC time and use the value you measured.** **The `D-1b`
token was forty-four minutes early; `D-1c`'s matched its commit to the
minute.**

**A13 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A14 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `DECISION_LOG.md`, all six microspec
artifacts, the four freeze documents, both registers, and everything
under `scripts/`, `tests/` and `results/`.

**A15 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four.** **Read the status line SCOPED to
its gate section** — a bare grep's first hit is a different gate.

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — The checker over this task's own range**, base `ec85f66b…`, head
**commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming only
this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` has two specifications in range**;
report what it did. **`P7` must report fourteen sections.** **`PASS` at
zero is a STOP.** **RUN 2 is stop-governing.** **Both configs and both
JSON outputs verbatim.**

**A17-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A18 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A19 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
    commit 3  --no-ff merge of cdbfa6b9…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A16, A18 and A19 for
commits 1–3; **A17's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A12's final
scope stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A17-final; A15 and A16 re-run after the advance; A19
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 7. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `ec85f66b…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no `D-1`,
`D-1b` or `D-1c` branch.** **The source branch is not deleted and does
not move**; verify and report its tip.

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First, and it is this landing's characteristic risk.** **A ledger of
five named nodes reads as a to-do list.** **It is not one.**

**Each node is an ADOPTED DEPENDENCY-ACCOUNTING UNIT — not a to-do item,
not a question, not a decision, not a problem.** **A low node count
means only that more `UD` occurrences have been grouped under fewer
accounting nodes AT THE ADOPTED GRANULARITY.** **It does not establish
fewer underlying questions, and it does not establish easier work.**

**An earlier draft of this junction said each node "is a question the
programme has not framed" and that a low count means "fewer distinct
questions".** **Both contradict §1c and `A8` in this same
specification**, which forbid restating the node count as a number of
questions. **§1c is also the correct version: `R1` alone decomposes into
four constituents.**

**`R1` is the sharpest case.** **It contains the canonical
kinetic-operator choice and its delegated constituents — the choice this
programme has repeatedly declined to make for want of independent
physical grounds.** **Its representation as ONE node must not make that
ontological ruling look like one atomic task or question.** **Say so**,
and **say that nothing in this line has produced a ground for making
it.**

**Second.** **Reflection-positivity applicability is not a ground for
choosing the operator.** **If a ruling on `R1` were made because it
would close `UD` occurrences, the programme would be deriving its
microscopic content from what the fetched literature happens to prove.**
**Say that this is the inversion the whole `D-pre` line exists to
avoid.**

**Third.** **The 21 bridges are untouched and unmeasured.** **A reduced
`UD` figure beside an unreduced `UB` figure invites reading the total as
reduced.** **Report 33 of 54 covered.**

**Fourth.** **This rests on `D-1c`, on `D-1b`, on `D-1`, each bounded.**
**`D-1`'s literature search was bounded; `D-1b` re-read nothing; `D-1c`
did no mathematics.** **Four layers, and the bounds compose.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing**, and do not rename any arriving path.
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not order the rulings, make one, or say which is independent.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's seven nodes and the two decompositions, reported separately**;
- **A7's anchor verification with files, lines and what you read**, and
  the `R2`/`R3` punctuation finding;
- **A8's three transcriptions and the three searches**;
- **A9's cross-paper check with the papers each node spans**;
- **A10's `k8` double dependency**;
- **A11's out-of-scope counts**;
- **A12's two scope figures and the arriving-path statement**;
- **A13's merge case, stated BEFORE the blob comparisons**;
- **A14's path count**;
- **A15's four invariants, with the scoped read stated**;
- **A16's six exit statuses, before and after**;
- **A17's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **A18's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§8's four Rule 16 junctions**;
- **whether landing a five-node ledger made you want to order the
  rulings, say which is easiest, or say what `R1` should be.** **Say
  which and why, and confirm you did not** — **the source executor
  reported that after grouping 25 occurrences by anchor, the bridges
  look like they would collapse the same way, and they would not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from ec85f66b with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = ec85f66b05b3ed92cd924bc75273b74a73eee23b;
                source = cdbfa6b9…, NOT an ancestor of main. Merge
                CLEAN; merge-base = ec85f66b; 6 additions and 0
                modifications at the merge commit; 7 and 0 with a
                placeholder report; the landing fast-forward is
                available. Four arriving paths, all additions, carrying
                the token 0322Z.

    target      two of the five anchors
    method      read ONTOLOGY line 189 and ROUTE lines 192-193 at the
                evidence base
    MEASURED    ONTOLOGY:189 reads "| Canonical kinetic operator and
                species accounting | DELEGATED: D-pre (4 obligation
                binds it) |". ROUTE:192-193 reads "the subtraction /
                reference-equivalence class; finite-volume and
                thermodynamic rules; boundary conditions." R2 and R3 are
                indeed named in one semicolon-separated sentence, and
                the source kept them apart. A7 requires all five
                re-read.

    target      the DECISION_LOG sweep the source reported
    method      grep -ci for five node terms in DECISION_LOG.md, then
                READ the non-zero hits
    MEASURED    LEXICAL HIT COUNTS: kinetic operator 0, lattice extent
                0, boundary condition 0, multiplicity 0, MEASURE 3.
                The three "measure" hits, read: line 416 "longitudinal
                mixing measured in the wrong basis"; line 1728
                "Amendment K's append-only measure"; line 1963 "the
                quantity measured is the ...". All three are the
                ordinary verb or an unrelated governance metric. NONE
                concerns the microscopic integration measure, and none
                is a later authoritative ruling.
    NOTE        the source's wording "zero on every term" is IMPRECISE
                if read as a literal grep count: the literal count for
                "measure" is three, not zero. Read as "zero later
                authoritative rulings", it is correct and this author's
                reading confirms it.
    RETRACTED   an earlier draft of this record observed the discrepancy
                and wrote that the hits "are consistent with" the
                source's claim WITHOUT READING THEM. That is supplying
                a reason for a source rather than verifying it. A7 now
                requires the executor to read every non-zero hit and
                report both figures.

    target      the node figures
    method      NOT MEASURED by this author. 5 RULING nodes, 2
                ESTABLISHED FACT nodes, the controls counts and the two
                decompositions are the source executor's. A6 requires
                them re-derived from the arriving ledger.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
