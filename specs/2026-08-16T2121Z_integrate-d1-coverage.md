# Task specification — integrate the reflection-positivity literature coverage audit, and land it

Specification evidence base: `b27926aad0d3a1ef39f5e7e886f8571657c5687c`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-d1-coverage
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/d1-literature-coverage-audit-3
                       f8fdcf64e4106fff3958ae726237e4aec453af04

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`b27926aa…`, **6 additions and 0 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**Nothing is modified.** No gate, no pin, no register, no script, no
test.

---

## 0. What lands, and what it cost to get here

**`D-1` produced a scientific result on its third execution.** **The two
preceding executions and three preflights are records, not failures**,
and the arriving artifact is the first `D-1` output that reaches `A4`–`A8`
at all.

    execution 1    …-audit @ 8267bd40      STOP at §1, sandbox egress
    preflight 2a   stale local refs/heads/main
    preflight 2b   wrong repository, 0-programme
    execution 2    …-audit-2 @ a537e036    STOP at A14, pin test
    preflight 3a   branch-name occupancy
    execution 3    …-audit-3 @ f8fdcf64    COMPLETE

**Eight specification revisions preceded it and NONE concerned the
literature audit itself** — repository identity, ref semantics, branch
naming, execution order, provenance vocabulary, environment
preconditions. **Report that where the Rule 16 assessment discusses what
this cost.**

## 1. The result

**Four candidates, four `PARTIAL` verdicts, zero `COVERED`.**

    burden accounting    0 replaced, 4 remain open

**No construction unit is removed from `B0`'s seven-to-eleven
estimate.** **Every load-bearing work fails on at least one material
hypothesis**, and the failures are not the same failure.

**TEN works were fetched — eight at full text, two at abstract depth —
and one further work was encountered and not fetched.**

**`B0`'s named seed set is five works: `OS73`, `OS75`, `OS78`, `N97`,
`HJL98`.** **FIVE fetched works were outside it: `MP87`, `KU10`, `GK22`,
`FG26`, `STW81`.** Of those five, **three became load-bearing
applicability bases — `MP87`, `KU10`, `FG26` — one supplied `ROUTE
EVIDENCE` (`GK22`), and one supplied abstract-only formulation context
(`STW81`).** **`L77` is a sixth outside-seed work, encountered and not
fetched.**

**An earlier draft of this section said seven fetched and three outside
the seed set.** **Ten and five are the measured figures**; the three was
the count of outside-seed works that became load-bearing bases, **a
different quantity reported as if it were the same one.**

**The audit's `§6` treats `B0`'s claims as SEARCH SEEDS rather than a
boundary, and that decision is what produced all five.** **Report the
counts and say plainly that a boundary-scoped audit would have missed
them.**

**`OS78` was reachable only at abstract depth.** **Report that the
access limitation is factual AND that the refusal to let it support
`COVERED` is the evidential criterion operating correctly.** **Both are
true and an earlier draft named only the second.**

## 2. A distinction this integration RECORDS and does NOT perform

**`B0`'s remaining question was whether the four gaps are one gap or
four.** **The artifact answers something more useful and the answer must
not be flattened.**

**The `FAIL` entries fall into THREE kinds, and a two-way split
misclassifies the most interesting ones:**

    UNFROZEN DATUM                     the programme has not frozen the
                                       quantity the source hypothesis
                                       constrains — reflection type,
                                       lattice extent, temporal boundary
                                       condition, operator
                                       normalisation, r, the hopping
                                       domain
    INCOMPATIBLE HYPOTHESIS            a KNOWN programme fact genuinely
                                       conflicts with the hypothesis —
                                       two dimensions against four, a
                                       different operator class
    UNESTABLISHED APPLICABILITY BRIDGE possibly compatible, but the
                                       mapping, specialization,
                                       factorization or measure junction
                                       has not been shown — a non-gauge
                                       specialization not established, a
                                       determinant-reflection or
                                       Grassmann-factorization step
                                       unproved for the programme action

**A `FAIL` may carry more than one tag.** **Report every tag it carries.**

**They close by different means.** **`UNFROZEN DATUM` may close when
`D-pre` freezes the datum — work the programme intends anyway.**
**`INCOMPATIBLE HYPOTHESIS` means that basis cannot cover, and other
mathematics is needed.** **`UNESTABLISHED APPLICABILITY BRIDGE` may need
only a targeted applicability lemma rather than a full construction** —
**and that is the distinction most likely to change what the next task
costs.**

**An earlier draft offered only the first two and said an
`INCOMPATIBLE HYPOTHESIS` gap "needs mathematics that does not exist".**
**`D-1` established that the FETCHED literature does not supply it.**
**It established nothing about what exists**, and asserting otherwise
would break the bounded-search discipline `D-1` was written to keep.

**THIS TASK DOES NOT PERFORM THE CLASSIFICATION.**

**Classifying every `FAIL` across four candidates and ten works is
load-bearing scientific analysis that would be invented, executed and
relied upon inside a landing report, with no specification of its own and
no pre-execution review of its method.** **Every other integration in
this line re-derived conclusions ALREADY PRESENT in the arriving
artifact; this would author a new one.**

**An earlier draft required it here and called it "the criterion that
determines what the next task can be" — which is precisely why it does
not belong in an integration.**

**It is deferred to a separate small task, `D-1b — RP gap
classification`, which this specification does not write.** **The
three-way taxonomy above is recorded so that task starts from a stated
one rather than inventing it under time pressure**, and **the examples
are the Researcher's reading of two bases, not an exhaustive survey.**

## 3. What this does NOT establish

- **No candidate is eliminated, preferred, or ranked.** **Four uniform
  `PARTIAL` verdicts carry no discriminating information**, exactly as
  four uniform `NOT ESTABLISHED` results did in `B0`.
- **`PARTIAL` is not "nearly covered".** **It means a relevant theorem
  exists and at least one material hypothesis is unmatched.** **Whether
  the remaining extension is small or large is NOT established by a
  `PARTIAL` verdict**, and §2's classification is the nearest thing to an
  answer.
- **`NO COVERAGE FOUND` did not occur, and its absence is not
  evidence.** Ten works were fetched; **nothing establishes that no
  further applicable work exists.**
- **The audit is bounded by what was fetched.** **Report the fetch-depth
  counts.**
- **`C-iii` and `D0` are not unblocked**, and **the operator remains
  unfrozen.**

## 4. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file.** There are no authorised modifications.
- **Do not select, eliminate, rank or prefer a candidate**, and **do not
  present a candidate with more literature behind it as better
  supported.** **Coverage is a fact about what others studied.**
- **Do not design a proof route**, **do not estimate how large any
  remaining extension is**, and **do not perform §2's classification.**
- **Do not revise `B0`'s seven-to-eleven estimate.** **Zero units were
  replaced; the estimate stands unchanged and this task does not
  re-derive it.**
- **Do not repair the thirteen pre-existing Ruff findings**, and **do not
  add a lint configuration.** **Report them as arriving and untouched.**
- **Do not add a register entry anywhere.**
- **Do not delete, reset, or reuse any earlier `D-1` branch.**

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**, and **confirm it identifies
`zetacheng/2-emergent-gravity`** — accept either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`b27926aad0d3a1ef39f5e7e886f8571657c5687c`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.** Report the source at
`f8fdcf64…` and **that it is not an ancestor of `main`.**

**Also report that `science/d1-literature-coverage-audit` and
`…-audit-2` still exist and are unchanged**, and **confirm you did not
touch them.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, BEFORE any measurement.** **Run Rule
13's diagnostic order including Amendment D's step 0**, and report
location, workspace depth, and package availability. **Report whether
the clone is shallow and its commit count.** **If any restoration is
needed, report it in one line each and confirm no repository content was
touched.**

**A4 — Merge parentage, three separately derived measurements**, with
parent 1 this task's review commit, parent 2 `f8fdcf64…`, and the
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The four verdicts and the burden accounting, re-derived from the
artifact.** Report each candidate's verdict and **the closing accounting
sentence**. **Expected: four `PARTIAL`, zero `COVERED`, zero replaced,
four open.** **Report what you actually measured.**

**A7 — The gap classification is DEFERRED, and that is what you report.**

**Do not classify the `FAIL` entries.** **Report that §2's three-way
taxonomy is recorded and not performed, and that it is deferred to
`D-1b — RP gap classification`.**

**Report the raw material only**: the count of `FAIL` entries in the
arriving tables, per candidate. **A count is not a classification.**

**If you find yourself assigning tags while counting, stop and report
that you did** — the temptation is the reason this criterion exists.

**A8 — Works fetched, with depth and provenance.** Report **the count
fetched and the depth of each — expected ten, eight full text and two
abstract**; **the work encountered and not fetched**; **which works were
outside `B0`'s five-work named seed set — expected five**; and **which
of those five became load-bearing applicability bases — expected
three.**

**Report `OS78`'s abstract-only limitation as a FACT ABOUT ACCESS**, and
**separately** that **refusing it as a `COVERED` basis is the evidential
criterion operating correctly.** **Both, not one.**

**A9 — Scope, frozen manifest. Final base-to-head scope: 7 additions and
0 modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: b27926aad0d3a1ef39f5e7e886f8571657c5687c
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
      reports/2026-08-16T1952Z_d1-literature-coverage-audit.md
      reports/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
      reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
      specs/2026-08-16T1952Z_d1-literature-coverage-audit.md
      specs/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive from the source, all additions; three are
authored here.** **Report the ARRIVING PATH count and the ARRIVING
ADDITION count separately, and state whether they coincide** — **they do,
at four, and a guard should stay visible when it does nothing.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Report which head each figure was measured at.**

**A10 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A11 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, all four earlier microspec
artifacts, both registers, `docs/GOVERNANCE-DEBT.md`, and everything
under `scripts/`, `tests/` and `results/`.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match their targets. **Report all four.**
**Read the status line scoped to its gate section, not by a bare grep**
— a preceding gate also reads `Status: PROPOSED`, and a first-hit grep
returns the wrong one.

**A13 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A14 — The checker over this task's own range**, base `b27926aa…`, head
**commit 3, the merge commit**. Two runs, `RUN 1` observational and
`RUN 2` naming only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` has two specifications in range**;
report what it actually did. **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A15 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.** **A change is a finding.**

**A16 — The thirteen Ruff findings, reported and untouched.** **Report
the count and the files**, and **confirm none was introduced or modified
by the source task or by this one.** **Do not repair them.**

**A17 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
    commit 3  --no-ff merge of f8fdcf64…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A13 and A15–A17 for
commits 1–3; **A14's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A9's final scope
stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A9's final scope measured
base-to-commit-4; A14-final; A12 and A13 re-run after the advance; A17
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The advance
is a fast-forward; `b27926aa…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no earlier
`D-1` branch.** **The source branch is not deleted and does not move**;
verify and report its tip.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **Four uniform `PARTIAL` verdicts provide ZERO
VERDICT-LEVEL discrimination for operator selection, just as the earlier
uniform `NOT ESTABLISHED` statuses did.** **They nevertheless add
candidate-specific literature and mismatch information**, and **an
earlier draft said they discriminate "exactly as little", which erased
what `D-1` did produce.**

**The audit removed zero construction units.** **A reader may take a
completed audit for progress toward selecting an operator.**

**Say what it actually delivered: ten fetched works at recorded
evidential depths, candidate-specific unmatched hypotheses and raw
`FAIL` material, four `PARTIAL` verdicts, and no reduction in
construction burden.** **The three-way gap classification is NOT
performed here and is deferred to `D-1b`.**

**An earlier draft of this junction said "seven identified works, a
classification of what is missing".** **Both were wrong**: the count was
retracted in §10 of this same specification, and the classification is
the thing §2 and `A7` expressly decline to do.

**Second.** **`PARTIAL` does not mean nearly covered.** **Nothing here
establishes that any remaining extension is small.** **§2's taxonomy is
recorded and not applied**, so **this landing carries no statement about
which gaps are cheap.** **Say that, and say that `D-1b` is where the
question is asked.**

**And nothing here establishes that any missing mathematics does not
exist.** **`D-1` established that the FETCHED literature does not supply
it** — a bounded search, and its bound is part of its result.

**Third.** **FIVE of the TEN fetched works were outside `B0`'s
five-work named seed set**, and **three of those five became load-bearing
applicability bases.** **A boundary-scoped audit would have missed them**,
and `B0`'s claims were recall.

**Say that the seeds-not-boundary decision is what allowed those
outside-seed works to enter the audit**, and **say that nothing
establishes the resulting search was exhaustive.**

**An earlier draft said "three of the seven", carrying a count this
specification retracted in §10.**

**Fourth, and it is about the process rather than the result.** **`D-1`
took three executions, three preflight stops, and eight specification
revisions, none of which concerned the literature audit.** **Every
revision fixed a real defect and every one was caught.** **Say that the
defects were the specification's assumptions about the execution
environment**, and **say that nothing establishes the remaining
assumptions have been found.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not select, rank, design a proof route, or revise `B0`'s
  estimate.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run and reported rather than assumed.** **Rule 13
  carries two such orders, a known open item; if no environment failure
  occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL** and the two earlier `D-1` branches
  confirmed untouched;
- **A3's environment diagnosis in Rule 13's order**;
- **A4's three values, separately derived**;
- **A6's four verdicts and the accounting sentence**;
- **A7's deferral statement and the raw `FAIL` counts per candidate**,
  with confirmation that no tags were assigned;
- **A8's ten fetched works with depths, the five outside the seed set
  and which three became load-bearing, `L77` as encountered-not-fetched,
  and the `OS78` access limitation stated alongside the criterion
  operating**;
- **A9's two scope figures and the arriving-path versus arriving-addition
  statement, including that they coincide**;
- **A10's merge case, stated BEFORE the blob comparisons**;
- **A11's path count**;
- **A12's four invariants, with the scoped read stated**;
- **A13's six exit statuses, before and after**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **A15's counts**;
- **A16's thirteen findings, untouched**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§7's four Rule 16 junctions**;
- **whether landing a completed audit made you want to select a
  candidate, design a route, or repair the Ruff findings.** **Say which
  and why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from b27926aa with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = b27926aad0d3a1ef39f5e7e886f8571657c5687c;
                source = f8fdcf64e4106fff3958ae726237e4aec453af04, NOT
                an ancestor of main. Merge CLEAN; merge-base =
                b27926aa; 6 additions and 0 modifications at the merge
                commit; 7 and 0 with a placeholder report; the landing
                fast-forward is available.

    target      the source's scope
    method      git diff --name-status
    MEASURED    FOUR additions, ZERO modifications: the coverage
                artifact, and the task's spec, review and report.

    target      the verdicts
    method      read the arriving coverage artifact
    MEASURED    four PARTIAL, zero COVERED; burden accounting 0
                replaced, 4 open.
    MEASURED    the ledger records TEN fetched works — 8 FULL TEXT, 2
                ABSTRACT — plus one NOT FETCHED. Ids present: OS73,
                OS75, OS78, N97, HJL98, MP87, KU10, GK22, FG26, STW81,
                L77. B0's named seed set is five (OS73, OS75, OS78, N97,
                HJL98), so FIVE fetched works were outside it, of which
                three became load-bearing bases. OS78 was reachable only
                at ABSTRACT depth and was refused as a coverage basis.
    RETRACTED   an earlier draft of this record said "seven works with
                identifiers", and 1 and A8 said seven fetched and
                three outside the seed set. Ten and five are the
                measured figures; three is the count of outside-seed
                works that became load-bearing bases — a different
                quantity, reported as if it were the same one. The
                author inferred the counts from a partial view of the
                artifact instead of counting the ledger.

    target      the two kinds of FAIL, for A7
    method      read the mismatch tables for the Wilson and naive
                bases at f8fdcf64
    MEASURED    the FAIL entries include both "the programme datum is
                unfrozen" and "the source proves something about a
                different object". Examples of the first: reflection
                type, lattice extent, temporal boundary condition,
                operator normalisation, r, the hopping domain. Examples
                of the second: gauge theory, free theory, two
                dimensions, different operator class.
    NOT EXHAUSTIVE. The author read two of the bases, not all ten
                fetched works across all four candidates. A7 requires the
                classification derived from the tables rather than taken
                from here.

    target      the P2-PHASE-01 status line
    method      bare grep for 'Status: PROPOSED' versus a read scoped to
                the gate section
    MEASURED    the bare grep's first hit is a DIFFERENT gate, seven
                hundred lines above P2-PHASE-01. A12 requires the
                scoped read.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
