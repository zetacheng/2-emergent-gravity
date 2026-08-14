# Task specification — `C-b`: one gate-heading grammar, and declarations that a reviewer sees

Specification evidence base: `f179b45eee359ef007da5e30833e9aed92069039`

    Branch to create   governance/mechanisms-cb
    Cut from           authoritative main @ f179b45e…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18, **and by
Amendments M–P and Rules 19–21, which landed at the evidence base and
bind this task prospectively.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**Two mechanisms, both with a measured failure behind them.** `C1`, the
two coexisting gate-heading grammars. `C3`, declared sets supplied by a
hand-written config no reviewer sees. **`C2`, `C4` and `C5` are not in
scope** — the PI's scoping ruling put them after these.

---

## 0. `C1` — two grammars, agreeing by coincidence

**Measured at the evidence base.** Two expressions read the same
fourteen gate headings from the same file:

    scripts/governance_tools/task_checker.py:540
      ^## (P2-[A-Z0-9-]+)[ \t]+[—–-][ \t]+\S.*$

    tests/test_repository_structure.py:154
      ^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+)

**Both return fourteen ids and their symmetric difference is empty
today.** **They are not the same language**, and three shapes separate
them — measured, not imagined:

    '## P2-FOO2-01 — Title'    checker ACCEPTS   structure REJECTS
                               (a digit inside an id segment)
    '## P2-BAR-01'             checker REJECTS   structure ACCEPTS
                               (no separator, no title)
    '## P2-BAZ-01 — '          checker REJECTS   structure ACCEPTS
                               (separator, empty title)

**Nothing keeps them agreeing.** **A future heading convention changed on
one side leaves the other reading a different registry**, and the two
would disagree silently — neither is compared against the other by
anything.

## 1. `C1` — what to build, and the canonical language is decided here

**Extract ONE gate-heading grammar into a shared helper, and have both
call sites use it.** **A single source of truth, not two expressions kept
in step by attention.**

**The canonical language is the CONJUNCTION of the two**: a heading is a
gate heading when **the id matches the strict naming shape**
`P2-[A-Z]+(?:-[A-Z]+)*-\d+` **AND the heading carries a separator
followed by a non-empty title.**

**Why the conjunction and not either side.** **It is strictly tighter
than both**, so every heading it accepts, both current expressions
already accept — **the change cannot silently admit something neither
side admits today.** **The structure test's id shape encodes a naming
convention the checker's does not, and dropping it would lose a check;
the checker's title requirement encodes that a registry entry without a
title is not usable, and dropping it would lose another.**

**Anything the conjunction rejects does not disappear.** `P7`'s
completeness invariant — landed — **compares parsed sections against the
raw `^## P2-` count and returns `NOT_PARSEABLE` when they differ.** **A
heading the tightened grammar rejects surfaces there**, which is the
whole reason tightening is safe.

**MEASURE FIRST, and STOP if the measurement contradicts the
decision.** **Apply the conjunction to `GATES.md` at the evidence base
before changing anything.** **Expected: fourteen, the same fourteen
ids.** **If it accepts fewer than fourteen, the decision loses a real
heading and this specification is wrong: STOP and report which heading
and why.**

**`RAW_GATE_HEADING` stays as it is** — `^## P2-` — **and stays separate
from the helper.** **It is the independent signal `P7`'s invariant is
measured against, and routing it through the helper would make the guard
depend on the thing it guards.**

## 2. `C3` — declared sets that a reviewer never sees

**Measured.** `P3` and `P7` take their declared sets from
`config.get("append_only_paths")` and
`config.get("authorised_modified_gates")` — **a JSON object written by
the executor at run time.** **A reviewer approves a specification; the
config is written afterwards and is not part of what was approved.**

**The failure this produced, on `main`.** One landed integration supplied
`append_only_paths: []`. **`check_p3` treats an empty declared set as
`NOT_APPLICABLE` — the check switched off, not passed** — and the run
went green. **The Researcher's independent verification of that task read
the result and not the config, and did not catch it.**

## 3. `C3` — what to build

**(a) The scope block carries the declarations.** Extend the scope
block's key set so a specification declares, in the same machine-readable
record `Amendment O(a)` already requires for `stated:`:

    append_only:        one path per line, or [] with the meaning fixed
                        by (c)
    authorised_gates:   one gate id per line, or []

**(b) The specification's declaration takes precedence over config, and
the precedence is reported, never silent.** **When both are present and
they differ, that is a STOP, not a merge** — a config that quietly
overrides a reviewed declaration would reproduce the defect this
mechanism exists to remove, one layer along. **When only config is
present, the check proceeds and the JSON says the value came from
config.**

**(c) `[]` means different things for `P3` and `P7`, and that is the
defect, not the design.** Today `P7` reads `[]` as *no gate may change* —
truthful and useful — while `P3` reads it as *nothing to check*. **Two
identical notations, opposite meanings, and the difference lives in the
code rather than in the notation.**

**Decided here. `append_only: []` is a DECLARATION that the applicable
set is empty. It is not an exemption, and it is not a pass.**

**`P3` evaluates the task against the declared set and MUST NOT return
`NOT_APPLICABLE` merely because that set is empty.** **An empty declared
set is something the specification said; absence is something it did not
say, and the two must not share an outcome.**

**Three states, each distinguishable in the JSON:**

    NOT_DECLARED       the specification says nothing. Unchanged: the
                       run is INCOMPLETE and exits non-zero.
    DECLARED_EMPTY     the specification declares an empty set. The run
                       continues. THE STATUS IS NOT `PASS`, and the JSON
                       carries a sentence saying nothing was checked
                       because nothing was declared applicable.
    declared non-empty the named paths are checked as now.

**Why `DECLARED_EMPTY` and not `PASS`.** The Reviewer is right that `[]`
must stop meaning *off*. **But an empty declared set leaves nothing to
check, and `PASS` over nothing is the vacuous green this programme has
now met three times** — `P7` over two empty maps, a pin validator that
would have passed on zero pins, and `P3` itself. **`P7`'s `[]` is
genuinely different**: an empty authorised-gate set inverts into a
checkable assertion, *no gate changed*. **An empty append-only set
inverts into nothing.** **So it gets a state of its own rather than
borrowing either neighbour's.**

**`P3` does NOT independently verify that the declaration is complete**,
and this task does not make it. **Whether a specification declares
truthfully is the discovery gap `P3` is `PARTIAL` for**, and §5 keeps it
`PARTIAL` for that reason. **An earlier version of this section required
`P3` to check the declaration against a repository-wide list of
append-only paths that does not exist**, which would have driven this
task into a STOP over a problem `C-b` is not solving. **The Reviewer
identified that and the requirement is withdrawn.**

**Do not invent a repository-wide append-only list.** Registering the
need for one is `C-c`'s.

## 4. Fixtures

**Every change gets a passing AND a failing fixture, and each new failure
mode gets at least one fixture the pre-change code cannot get right.**
At minimum:

    the real GATES.md through the helper            → 14 ids
    a heading with a digit inside an id segment     → rejected, and
                                                      surfaced by P7's
                                                      completeness
                                                      invariant
    a heading with no separator or empty title      → rejected, surfaced
                                                      the same way
    both call sites return the SAME id set          → the invariant that
                                                      replaces coincidence
    append_only declared in the scope block         → P3 uses it
    append_only in BOTH spec and config, differing  → STOP
    append_only: [] in the scope block              → DECLARED_EMPTY,
                                                      not PASS and not
                                                      NOT_APPLICABLE
    no declaration anywhere                         → NOT_DECLARED

**The pre-existing tests must continue to pass, or any that should not
must be reported with the reason.** **Do not delete a test to make the
suite green.**

## 5. The classification, updated

**Update `derivations/GOVERNANCE-ENFORCEMENT_classification.md` for `P3`
and `P7` only.** State what each now checks and where its declared set
comes from. **`P3` and `P7` both stay `PARTIAL`** — **the discovery
problem narrows but does not vanish: a specification still declares its
own sets, and a specification can declare wrongly.** **What changes is
that the declaration is now inside the artifact a reviewer reads.**

**Do not change any verdict. Do not add or remove a property. The nine
stay nine.**

## 6. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not modify `GATES.md`.** Every mechanism here reads it.
- **Do not change `P1`, `P2`, `P4`, `P5`, `P6`, `P8` or `P9`.**
- **Do not route `RAW_GATE_HEADING` through the helper.**
- **Do not build `C2`, `C4` or `C5`**, and **do not register anything** —
  `C-c` holds the register and its list has grown to seven.
- **Do not create a repository-wide append-only path list.**
- **Do not fix `F1` or `F2`.**
- **Do not weaken an existing check to make the suite green.**

## 7. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`f179b45eee359ef007da5e30833e9aed92069039`. Report the Git blob ids of
`scripts/governance_tools/task_checker.py`,
`tests/test_task_checker.py`, `tests/test_repository_structure.py`,
`derivations/GOVERNANCE-ENFORCEMENT_classification.md` and `GATES.md`.
**Any ref mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank or naming a different digest, STOP and say
which.** Report both digests equal. **Amendment `N` binds this task; say
so.**

**A3 — The conjunction measured BEFORE the change.** Apply the canonical
language of §1 to `GATES.md` at the evidence base and **report the count
and the full id list.** **Expected fourteen.** **Fewer is a STOP under
§1.** **Also report the count each of the two existing expressions
returns on the same file, from the same measurement session** — expected
fourteen and fourteen.

**A4 — One helper, two call sites.** Report **the helper's location and
signature**, and **that both `task_checker.py` and
`tests/test_repository_structure.py` call it** rather than carrying their
own expression. **Report that no gate-heading expression remains outside
the helper**, other than `RAW_GATE_HEADING`. **Search for it and report
the search**, not only the conclusion.

**A5 — The agreement invariant.** Report the test that asserts both call
sites return the same id set for `GATES.md`, **and what it does if the
set is empty.** **An empty set must not pass** — the same shape `P7`
already guards against, and a test that agrees on nothing agrees.

**A6 — Per-fixture demonstration against the OLD code, with each
fixture's PURPOSE stated first.** Classify each fixture in §4 as one of:

    CHANGE-DISCRIMINATING   the old code gets it wrong; the fixture
                            exists to show the change works
    REGRESSION              the old code gets it right; the fixture
                            exists to show the change did not break it

**Run every fixture against the code at the evidence base and report
what happens, per fixture, not in aggregate.**

**A `CHANGE-DISCRIMINATING` fixture the old code already handles is
mislabelled** — reclassify or replace it. **A `REGRESSION` fixture the
old code handles correctly is doing its job**, and old-code failure is
not the default purpose of every fixture. **The real `GATES.md`
returning fourteen ids is a regression fixture, and an earlier version of
this criterion implied it should fail against the old code.**

**A7 — Precedence, demonstrated.** Report three runs: **declaration in
the specification only**; **config only**; **both, differing.** **The
third must STOP.** **Report the JSON's statement of where the value came
from in each of the first two.**

**A8 — the three states of `append_only`, demonstrated separately.**
Report one run for each: **no declaration**, **`[]`**, and **a non-empty
set.** **Report the status and the JSON message for each.**

**`[]` must yield `DECLARED_EMPTY`** — **not `NOT_APPLICABLE`, and not
`PASS`.** **Report the sentence the JSON carries**, and **confirm a
reader of the JSON alone can tell `DECLARED_EMPTY` from `PASS`.**

**Report whether `DECLARED_EMPTY` affects the run's exit status**, and
**say why that is the right answer** — it is a valid declaration, unlike
`NOT_DECLARED`, and this specification's position is that the run
continues.

**A9 — `P3` and `P7` still `PARTIAL`.** Diff the classification and
report it in full. **Confirm every verdict unchanged, no property added
or removed, and that only `P3`'s and `P7`'s entries changed.**

**A10 — Scope, frozen manifest.**

    stated: 3 additions, 4 modifications
    base: f179b45eee359ef007da5e30833e9aed92069039
    head: <commit 5>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_mechanisms-cb.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_mechanisms-cb.md
      specs/2026-08-XXT{HHMM}Z_mechanisms-cb.md
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_repository_structure.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths. `GATES.md` is not among them.**

**A11 — Protected paths.** Every path existing at the evidence base other
than the four in A10's `modify:` list is blob-identical at the head. **In
particular `GATES.md`, `CONVENTIONS.md`, `DECISION_LOG.md`,
`docs/BRANCHING_POLICY.md`, `tests/test_gate_pins.py`, and everything
under `results/`.** Compare path by path and report the count.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets.** **Report all four.**

**A13 — The checker over this task's own range**, base `f179b45e…`, head
**commit 4**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_mechanisms-cb.md

**Config for both runs. Note what this task changes about it:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**This specification's own scope block also declares `append_only` and
`authorised_gates`, per §3(a).** **So the precedence rule of §3(b)
applies to this task's own run: if the two differ, RUN 2 STOPS.**
**Make them agree, and report that you did.** **This task is the first
subject of the mechanism it builds.**

**`P7` must report fourteen sections through the new helper.** **`PASS`
at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 5.

**A14 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**The count MUST rise from 310** — new fixtures land. **Report the delta
and what accounts for it.** **A count that did not move means the new
tests are not being collected.**

**A15 — Commit-message hygiene** on all five commits. **`F1` says your
harness will try; report what happened per commit.** **Rule 20 landed at
the evidence base and binds this task: if an unpushed commit carries a
mechanically detected hygiene violation, the amend is permitted and
EVERY affected check is re-run, not only the failing one.** **Report both
commit ids if that happens.**

## 8. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_mechanisms-cb.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_mechanisms-cb.md
    commit 3  scripts/governance_tools/task_checker.py
              tests/test_task_checker.py
              tests/test_repository_structure.py
    commit 4  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    commit 5  reports/2026-08-XXT{HHMM}Z_mechanisms-cb.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Code and both test files move
together in commit 3** — a commit where the helper existed and one call
site still carried its own expression would be a green that means
nothing.

**Committed report — measured at commit 4:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1–4 SHAs and stored
messages; commit 5's intended message; **A10's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-5; A13-final; A14 at commit 5; A15 for commit 5; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 9. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** After this, one grammar reads the gate registry and
declarations live in the reviewed artifact. **A reader may take that for
the declared-set problem being solved.** **A specification still declares
its own sets and can declare them wrongly.** **What changed is that a
reviewer now sees the declaration.** **`P3` and `P7` stay `PARTIAL` and
the classification says why.**

**Second.** **The agreement invariant replaces a coincidence with a
check, and the check is written by the same hand as the helper.**
**Say what would detect the helper and its test drifting together** —
and **do not build it here.** This is the third time this programme has
met that regress and naming it is not solving it.

**Third.** **`C2` remains open**: nothing requires a newly issued
specification to carry `stated:`, `append_only:` or `authorised_gates:`.
**This task makes the declarations possible and readable. It does not
make them mandatory.** **Say that, and say that compliance therefore
still rests on an authoring habit.**

## 10. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  four paths in A10's `modify:` list. **Nothing else.**
- **Do not modify `GATES.md`, for any reason.**
- **Do not adjust the config to make RUN 2 pass**, and **do not adjust
  this specification's own declarations to make the precedence check
  pass** — make them agree by making them correct.
- **Do not describe `P3` or `P7` as no longer `PARTIAL`.**
- No force-push, no history rewrite, no branch deletion **except as Rule
  20 permits**, and then per its terms.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 11. Report contract

- everything in §8 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's three counts from one measurement session**, with the id list;
- **A4's helper location and the search for stray expressions**;
- **A5's invariant and its empty-set behaviour**;
- **A6's per-fixture old-code results**;
- **A7's three precedence runs**, including the STOP;
- **A8's `[]` behaviour**, or the authorised STOP and its reason;
- **A9's classification diff**, verdicts confirmed unchanged;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  and **confirmation that this task's own declarations agree with its
  config**;
- **A14's delta and what accounts for it**;
- **§9's three Rule 16 junctions**;
- **whether building these mechanisms made you want to build `C2`.**
  **Say so, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 12. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.** **Every line was produced by running the stated method in
a clean clone.** **No measurement was taken through a truncated view, and
no statement below is clone-dependent.**

    target      the two grammars and what separates them
    method      read both expressions at f179b45e; apply each to
                GATES.md; then apply each to three constructed headings
    MEASURED    checker at task_checker.py:540, structure test at
                tests/test_repository_structure.py:154. Both return
                FOURTEEN ids from GATES.md; symmetric difference EMPTY.
    MEASURED    '## P2-FOO2-01 — Title' checker ACCEPTS, structure
                REJECTS. '## P2-BAR-01' checker REJECTS, structure
                ACCEPTS. '## P2-BAZ-01 — ' checker REJECTS, structure
                ACCEPTS. Three shapes, both directions.

    target      how P3 and P7 receive declared sets
    method      grep for the config keys in task_checker.py
    MEASURED    check_p1 takes config['specification_paths'] or
                _added_specs; check_p3 takes
                config['append_only_paths']; check_p7 takes
                config['authorised_modified_gates']. All three come
                from the run-time config, which is written after review.

    target      what an empty declared set does today
    method      read check_p3's and check_p7's guards
    MEASURED    P3: an empty set yields NOT_APPLICABLE, "no
                append_only_paths supplied; the set is not inferred" —
                the check is off. P7: an empty set is an empty
                authorised set and the check proceeds. IDENTICAL
                NOTATION, OPPOSITE MEANING.

    target      what Amendment O already requires
    method      read Amendment O at f179b45e
    MEASURED    O(a) requires a machine-readable 'stated:' key and says
                the missing enforcement is C2; O(b) requires reading
                lists to name evidence-write sites and records that
                there is no mechanism at all and registering it is
                C-c's. NEITHER covers append_only or authorised_gates,
                which is why §3(a) extends the key set rather than
                relying on O.

    target      the rules binding this task
    method      read CONVENTIONS.md at f179b45e
    MEASURED    21 numbered rules; 15 amendments A-P, no J. Amendments
                M-P and Rules 19-21 landed at this evidence base and
                bind this task prospectively, unlike the task that wrote
                them.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                f179b45e and executed — not re-implemented
    MEASURED    one scope block; stated 3 additions, 4 modifications;
                the manifest lists three and four; parse OK, counted
                equals stated per category.
