# Task specification — `RECON-01a`: build the curved-background Proca operators and validate them against the flat limit

Specification evidence base: `f21198cd25ae285b789b706f7c4ac0730f9fff69`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/recon-01a-construction
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

**THIS TASK BUILDS AND VALIDATES. IT DOES NOT SCAN `k`.** §1 says why.

**ANCHOR-ISOLATION DISCIPLINE APPLIES.** §2 states it and makes it
checkable. **It is not a claim that you are ignorant of the anchor.**

---

## 0. What the gate asks for, and what this stage delivers

**`P2-BETAV-RECON-01` at `GATES.md:725-764`, `Status: PROPOSED`.** Its
`Scope` names:

    Δ⁽¹⁾[g,h]   1-form operator on a weak-field background
    Δ⁽⁰⁾[g,h]   compensating scalar
    Γ_k = ½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾
    method      numerical h-derivatives at the determinant/eigenvalue
                level; fixed axis-TT projection
    vary        only k ∈ {0,1,2,3,½}

**Its `Required computations` says: a substantial implementation, NOT
RUN this sweep.**

**`RECON-B0` measured ten components: two with usable implementation and
specification, seven specification-only, one neither.**

**This stage delivers the operators and their flat-limit validation.**
**It does not compute `Γ_k`, does not vary `k`, and does not compare
against any anchor.**

## 1. Why the split, and it is the kill criterion's own requirement

**The gate's kill criterion has two clauses**: one says a particular
constant value across all `k` means the pipeline is degenerate — a bug;
the other says a particular drift at heavy mass means a longitudinal
artefact. **The values are in the gate and this specification does not
repeat them, because `RECON-01b` is where they are applied.**

**Both readings PRESUPPOSE A VALIDATED PIPELINE.** **A `k`-scan run on
an unvalidated construction returns numbers whose meaning is
undecidable**: a wrong operator can produce values that vary plausibly
with `k` and mean nothing, and the kill criterion catches neither.

**So the pipeline must be shown correct against a target that does NOT
involve the anchor, BEFORE the anchor is ever approached.**

**The flat limit is that target.** `P2-BETAV-CIRC-01` names the flat
Proca eigenvalue structure `{+m²(×3), m²}` — **it says nothing about the ratio
anchor**, so validating against it leaks nothing.

**A single task that built and scanned would find a construction error
by way of a wrong scan result**, and **the distinction between "bug" and
"result" would then be drawn after seeing the number** — the same defect
`SIGN-01` was written to close on the sign.

## 2. Blind discipline, and it is checkable

**This specification does not pretend you are ignorant of the anchor.**
**An earlier draft claimed to establish a blind while itself stating the
anchor's values** — **the claim was false the moment it was written, and
"do not read `SIGN-01`" cannot restore what a specification has already
disclosed.**

**What is enforceable is ISOLATION, and that is what is required:**

> **Anchor information must not enter the construction source, the
> tests, the validation logic, or ANY DECISION used to choose or tune
> the construction.**

**Concretely:**

- **no anchor value appears in `proca_curved.py`, `flat_validation.py`,
  or the test** — not in code, not in a comment, not in a docstring, not
  in a constant, not in an assertion;
- **no design choice is made because it moves a result toward an
  expected value.** **You do not compute a result that could be compared
  to the anchor in this task at all** — §5 forbids `Γ_k` and `k`;
- **the derivation artifact and the report state findings, not
  comparisons to the anchor.**

**The contamination scan is MECHANICAL and uses externally supplied
patterns.** **`A9` reports HIT COUNTS AND PATHS, not the patterns.**
**A report that reproduces the forbidden literals in order to say it
searched for them has defeated the purpose of not writing them.**

**Do not read `P2-HK-01`, `betav_discriminating_power.md`,
`P2-BETAV-SIGN-01_anchor-reconciliation.md`, or the `RECON-01` gate's
`Analytic anchors` line.** **Not because they would tell you something
this specification withheld — they would not — but because reading them
during construction makes the isolation claim unverifiable.** **Report
whether you read any.**

**You DO need `CONVENTIONS.md`.** **`P2-BETAV-CIRC-01` is permitted for
the flat-spectrum and propagating-scalar statements ONLY, and §4's
staging governs when its quantitative results may be read.**

## 3. What to build

**Three files under `scripts/recon2026/`, a directory this task
creates.**

**`proca_curved.py` — the operators.** `Δ⁽¹⁾[g,h]` and `Δ⁽⁰⁾[g,h]` on a
weak-field background, metric-coupled, on a finite hypercubic lattice.

**`flat_validation.py` — the validation driver.** Sets `h = 0` and
checks the operators reproduce the flat Proca structure.

**`tests/test_recon2026_flat_limit.py` — the regression anchor.**
**`RECON-01`'s `Regression anchors` field currently reads `None yet
(proposed)`.** **This test is the first one**, and **`RECON-01b` will
depend on it.**

**THE CONSTRUCTION IS FROZEN BEFORE THE QUANTITATIVE VALIDATION TARGET
IS READ.** **Commit 3 is split in two:**

    commit 3a   proca_curved.py, flat_validation.py, the test
                — built knowing ONLY the analytic flat-spectrum
                  requirement and the propagating-scalar distinction
    commit 3b   the derivation artifact
                — written after reading CIRC-01's quantitative results

**After commit 3a, the three code files are FROZEN.** **You may not
modify them in commit 3b or afterwards.** **If the comparison in §4(b)
disagrees, you report a finding — you do not adjust the construction.**

**This is the mechanism that makes §5's "do not tune" enforceable rather
than merely stated.** **An earlier draft named `CIRC-01`'s mixed-`q`
figure in the specification itself**, which would have made it a
construction target before any code existed — **the exact failure the
staging prevents, and this specification does not repeat the figure.**

**Clean-room, and what that means concretely.** **You may READ
`scripts/recovered_2026/proca_loop.py` and the other recovered scripts
to understand what was done.** **You may NOT copy code from them, import
them, or reproduce their structure.** **`RECON-B0` classified two
existing components as usable — `scripts/betav_decomp_check.py` for
flat-limit validation and the `P2-BETAV-CAMPAIGN` harness architecture —
and classified them usable AS CHECKS, not as components.** **Report,
per file you read, whether anything from it entered your implementation
and how.**

## 4. What the validation must establish

**Report each separately.**

**(a) The flat spectrum.** At `h = 0`, `Δ⁽¹⁾ + m²` must reproduce the
Proca eigenvalue structure `P2-BETAV-CIRC-01` records —
`{+m²(×3), m²}` in the appropriate decomposition. **Quote that
document's statement, with lines**, and **report whether it is precise
enough to test against or whether you had to make it precise** — `A7`
of `RECON-B0` asked this and its answer is an input here.

**(b) Transverse and longitudinal separation. STAGED.**

**Before commit 3a**: **build the separation and MEASURE what your
construction gives.** **Do not read `CIRC-01`'s quantitative result for
the mixed `q` term.** **Record your own number.**

**After commit 3a, with the code frozen**: **read `CIRC-01`'s figure and
compare.** **Report both numbers and their relation.**

**A difference is a finding, not an error to tune away** — and **with
the code frozen, tuning is not available to you even if you wanted it.**

**Report the two numbers in that order: yours first, then `CIRC-01`'s.**
**The order is the evidence that yours was not chosen to match.**

**(c) The compensating scalar.** `Δ⁽⁰⁾[g,h]` at `h = 0`. **Report its
spectrum and confirm it is the propagating scalar `Δ + m²` and not the
ultralocal `m²`** — **`CIRC-01`'s `DECOMP-UNAVAILABLE-AS-RECOVERED`
verdict turned on exactly that distinction**, and a reconstruction that
repeated the confusion would be unusable for the same reason.

**(d) Lattice-spacing and volume behaviour.** **Report how the
validation behaves as the lattice is refined and enlarged**, over at
least two extents and two masses. **State what you varied.**

**(e) The `h`-derivative machinery, validated but not applied.**
**Build it, and validate it on a case with a known answer that is not
the anchor** — a free scalar determinant derivative, or any quantity you
can check independently. **Report what you validated against.**
**Richardson extrapolation is named in the gate's `Inputs`; report
whether you implemented it and what it gave.**

## 5. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT COMPUTE `Γ_k`.** **Do not vary `k`.** **Do not evaluate any
  quantity whose value depends on `k`.**
- **Do not compare anything to any anchor**, and **do not write the
  anchor or its values** — §2.
- **Do not read the four documents §2 names.**
- **Do not copy from, import, or reproduce the structure of any
  `scripts/recovered_2026/` file.**
- **Do not modify any existing file.** **Not `GATES.md` — the gate's
  `Regression anchors` field stays `None yet (proposed)` until an
  integration task changes it, and this task does not.**
- **Do not tune a construction to match an expectation.** **If the flat
  limit does not come out, report that it does not** — **a failed
  validation is a result and this task's most valuable possible
  outcome.**
- **Do not adjudicate `r = 1`**, and do not touch `R1`–`R5`.
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 6. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`, accepting either URL form.
Fetch, then report `refs/remotes/origin/main` and confirm it is
`f21198cd25ae285b789b706f7c4ac0730f9fff69`. **Report `refs/heads/main`
for contrast.**

**Report whether `science/recon-01a-construction` already exists.**
**If it does, STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count**, and **the versions of every package the
construction uses.** **Any restoration in one line each, with
confirmation that no repository content was touched.**

**A4 — The construction.** Report, for each of `Δ⁽¹⁾` and `Δ⁽⁰⁾`: **the
lattice discretisation used, the metric coupling, the boundary
conditions, and the free parameters and their values.** **State every
convention you fixed that `CONVENTIONS.md` does not fix**, and **report
it as a choice made here, not as a repository fact.**

**A5 — The five validations of §4**, each reported separately with its
numbers.

**A6 — The flat-limit target's precision.** Per §4(a). **Quote
`P2-BETAV-CIRC-01`'s statement with lines**, and **report whether you
had to make it precise and how.**

**A7 — Clean-room provenance.** **List every file you read.** **Per
file, state whether anything from it entered the implementation and
how.** **Confirm no code was copied, imported, or structurally
reproduced from `scripts/recovered_2026/`.**

**A8 — The new test.** Report the node id, what it asserts, and its
result. **Report the validator count before and after: 324 passed and 2
deselected at the base, and the count you measure at the head.** **An
increase equal to the number of tests you added is expected; any other
change is a finding and must be explained.**

**A9 — The contamination scan, mechanical, patterns not reproduced.**

**Scan every file this task creates against the forbidden-token pattern
set.** **Report HIT COUNTS AND PATHS ONLY.** **Do not reproduce the
patterns in the artifact or the report** — **a report that writes the
forbidden literals in order to say it searched for them has defeated the
purpose.**

**Expected: zero hits in all seven paths.** **A non-zero hit in any of
the three code files is a STOP.**

**Report separately whether you read `P2-HK-01`,
`betav_discriminating_power.md`,
`P2-BETAV-SIGN-01_anchor-reconciliation.md`, or the gate's
`Analytic anchors` line.** **If you did, say which and when** — **a
disclosed reading is recoverable; an undisclosed one makes the isolation
claim unverifiable for `RECON-01b`.**

**And report the staging**: that the three code files at commit 3a are
BLOB-IDENTICAL at commit 3b and at the head. **That identity is the
evidence that the quantitative target did not reach the
construction.**

**Use the character-immediately-preceding test for sign classification**
if any sign question arises. **Measured across this line: a
strip-non-ASCII filter loses `U+2212`; accepting only `U+2212` misreads
ASCII-hyphen files; accepting any hyphen on the line misreads
word-joiners such as `clean-room` and `flat-limit`.** **Only the
immediately-preceding test gets all three right.**

**A10 — Scope, frozen manifest.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: f21198cd25ae285b789b706f7c4ac0730f9fff69
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md
      reports/2026-08-XXT{HHMM}Z_recon-01a-construction.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_recon-01a-construction.md
      scripts/recon2026/flat_validation.py
      scripts/recon2026/proca_curved.py
      specs/2026-08-XXT{HHMM}Z_recon-01a-construction.md
      tests/test_recon2026_flat_limit.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths, three of them code.** **This is the first task in this
line that adds executable content**, and **`modify:` is still `[]`.**

**If your construction needs a file this manifest does not name, STOP
and report** — **do not add it.** **The manifest is frozen and a
construction that outgrows it is a specification defect, not an
executor decision.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.**

**Measure the UTC time and use the value you measured.**

**A11 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, all five
`derivations/P2-BETAV-*` artifacts, all seven microspec artifacts, both
registers, everything under `scripts/recovered_2026/`, and everything
under `results/`.

**`GATES.md` in particular**: **the `Regression anchors` field still
reads `None yet (proposed)` at the head.** **Confirm it.**

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.** **Also report:**
`P2-BETAV-RECON-01` `PROPOSED`, `P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01`
`PROPOSED (deferred)`. **Confirm none changed.**

**A13 — The checker over this task's own range**, base `f21198cd…`, head
**commit 3b**. Two runs, `RUN 1` observational and `RUN 2` naming only
this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.** **PARSE the output; do not grep it.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A14 — Validators, exit status 0**, per `A8`.

**A15 — Commit-message hygiene** on all FIVE commits. **Rule 20 binds
this task.**

## 7. Commit order and evidence layering

    commit 1   specs/2026-08-XXT{HHMM}Z_recon-01a-construction.md
    commit 2   reviews/chatgpt/2026-08-XXT{HHMM}Z_recon-01a-construction.md
    commit 3a  scripts/recon2026/proca_curved.py
               scripts/recon2026/flat_validation.py
               tests/test_recon2026_flat_limit.py
                 — the CONSTRUCTION FREEZE. Built and measured knowing
                   only the analytic flat-spectrum requirement and the
                   propagating-scalar distinction.
    commit 3b  derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md
                 — written AFTER reading CIRC-01's quantitative results.
                   The three code files are NOT touched.
    commit 4   reports/2026-08-XXT{HHMM}Z_recon-01a-construction.md

**FIVE commits, not four.** **The split is the enforcement mechanism**:
after `3a` the construction cannot be adjusted, so a disagreement in
§4(b) can only be reported.

**Report the three code blobs' object ids at `3a`, at `3b`, and at the
head, and confirm all three sets are identical.**

**Committed report — measured at commit 3b:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1, 2, 3a and 3b
SHAs and stored messages; commit 4's intended message; **A10's final
scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A13-final; A14 at commit 4; A15 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **A validated flat limit does not establish that the curved
construction is correct.** **`h = 0` tests the operators where the
metric coupling is switched off** — **the very thing the reconstruction
exists to exercise.** **Say that explicitly**, and **say what a
curved-background validation would require that this stage does not
provide.**

**Second.** **This stage produces no number that bears on the anchor**,
and **that is by design.** **A reader may take a completed construction
for progress toward the result.** **`RECON-01b` is where a result
becomes possible, and it can still fail there.**

**Third.** **Every convention this construction fixes that
`CONVENTIONS.md` does not fix is a choice made here.** **Report how
many.** **A later reader must be able to tell which of the
reconstruction's inputs are repository facts and which are this task's
decisions** — **and if `RECON-01b` returns a wrong number, that list is
where the search starts.**

**Fourth.** **Clean-room is a claim about provenance, not about
correctness.** **A clean-room construction can be wrong in the same way
the historical one was**, and **nothing here establishes it is not.**
**`A7`'s file list is the evidence for the provenance claim and it is
the only evidence there is.**

## 9. Invariants and prohibitions

- Executor-writable: the seven paths of `A10`. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not compute `Γ_k`, vary `k`, or write the anchor.**
- **Do not copy from `scripts/recovered_2026/`.**
- **Do not tune to match an expectation.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Push only this task's branch.** **No session branch, no other
  branch, and not `main`.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §7 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**, with
  package versions;
- **A4's construction description with every convention fixed here
  listed as a choice**;
- **A5's five validations with their numbers**, with §4(b)'s two
  figures reported in the required order — yours first, `CIRC-01`'s
  second;
- **A6's quoted flat-limit target and whether you made it precise**;
- **A7's file list with per-file provenance statements**;
- **A8's node id, assertion, result, and the before-and-after validator
  counts**;
- **A9's contamination scan — hit counts and paths, patterns NOT
  reproduced** — the four-document reading statement, and the three code
  blobs identical at `3a`, `3b` and the head;
- **A10's scope**;
- **A11's path count and the `Regression anchors` confirmation**;
- **A12's four invariants plus the three `BETAV` statuses**;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **§8's four Rule 16 junctions**;
- **whether building made you want to compute `Γ_k`, look up the anchor,
  or reuse recovered code.** **Say which and why, and confirm you did
  not** — **this is the first task in this line where the forbidden
  action would produce the interesting number**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the evidence base and the gate
    method      git fetch; git rev-parse; read GATES.md:725-764 with
                UTF-8 decoding
    MEASURED    origin/main = f21198cd25ae285b789b706f7c4ac0730f9fff69.
                The gate is PROPOSED. Its Scope names Δ⁽¹⁾[g,h],
                Δ⁽⁰⁾[g,h], Γ_k = ½logdetΔ⁽¹⁾ − (k/2)logdetΔ⁽⁰⁾,
                numerical h-derivatives, fixed axis-TT projection, and
                k ∈ {0,1,2,3,½}. Regression anchors: None yet
                (proposed). Required computations: "a substantial
                implementation, not run this sweep".

    target      whether a k-scan can be interpreted without prior
                validation
    method      read the gate's Kill criterion
    MEASURED    it has two clauses — a constant value across all k
                meaning a degenerate pipeline, and a drift at heavy mass
                meaning a longitudinal artefact. The values are not
                reproduced here.
    DERIVED     both readings presuppose a pipeline already known to be
                correct. §1 is the author's argument for splitting on
                that basis; it is not stated in the gate.

    target      the flat-limit target and the scalar distinction
    method      the CIRC-01 findings as landed
    MEASURED    the flat Proca eigenvalue structure {+m²(×3), m²}; the
                transverse/longitudinal split only approximately
                invariant with a small non-zero mixed q term whose
                value is deliberately not reproduced here; and
                DECOMP-UNAVAILABLE-AS-RECOVERED turning on the recovered
                scalar being Δ+m² (propagating) rather than m²
                (ultralocal).
    NOT VERIFIED by this author at line level. A6 requires the statement
                quoted with lines and its precision assessed.

    target      whether this specification can establish a blind
    method      inspection of an earlier draft of this specification
    MEASURED    it stated the anchor's values in its own A9 search list
                while claiming "the anchor must not appear anywhere in
                this task's output" and forbidding the executor from
                reading SIGN-01.
    RETRACTED   that claim was false when written. A specification that
                discloses the anchor cannot make its executor blind to
                it, and no prohibition on later reading restores what
                was already disclosed. §2 now requires ISOLATION —
                anchor information not entering the construction, the
                tests, the validation logic, or any tuning decision —
                which is enforceable and checkable. A9's scan uses
                externally supplied patterns and reports counts and
                paths only.

    target      whether CIRC-01's mixed-q figure could become a
                construction target
    method      inspection of an earlier draft of §4(b)
    MEASURED    it named the figure in the specification, before any
                code existed.
    RETRACTED   naming an expected diagnostic in the specification makes
                it a construction target no matter what §5 says about
                tuning. §3 and §7 now freeze the code at commit 3a and
                permit the comparison only at 3b, so the construction
                cannot be adjusted after the target is known.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
