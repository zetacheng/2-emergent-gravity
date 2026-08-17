# Task specification — integrate the clean-room Proca reconstruction scope assessment, and land it

Specification evidence base: `ece34f7bacbbee00efa0fecf0be644d593eed72f`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-recon-b0
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/recon-b0-scope
                       e219ae0e5e2a740c9212795599bb37460ba8d5bf

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
`ece34f7b…`, **6 additions and 0 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**Nothing is modified.**

---

## 0. What lands, and why it changes what the PI is choosing between

**`A8a` returned NO DEPENDENCE.**

    A8a   the RATIO β_V/β_B = (k+2)          depends on NONE of R1–R5
    A8b   absolute / assembled β_V, induced-G  depends on R5 and on R1
    hence                                      TWO PARALLEL LINES

**Before this, the programme had one blocked line.** **After it, the
clean-room `β_V/β_B` RATIO reconstruction line may proceed while
`R1`–`R5` remain open.**

**It is the RATIO line that `A8a` unlocks.** **Absolute and assembled
`β_V`, and `G_ind`, remain constrained by `A8b`.** **Do not write "the
`βV` reconstruction" unqualified** — a later reader would take it for
the absolute quantity.

**The mechanism matters and must land with the verdict.** **`N` DOES
appear in `CONVENTIONS.md:20` and `:29` — in the NORMALISATION of `Z`,
identically for both species — so it CANCELS in the ratio.**

**The source assessment states the trap it avoided:**

> **an assessment that answered `A8a` "yes, via `R5`" would have found
> `N` in the right document and drawn the wrong conclusion**

**Transcribe that.** **A later reader who finds `N` in `CONVENTIONS.md`
and concludes the ratio is ruling-dependent would reverse a correct
result using correct evidence.**

**Size: ten components, two usable.**

## 1. Three unresolved items arriving with it

**All three are in the source report's `§19` and none is adjudicated
here.**

**1a. A sign discrepancy** between the gate and the `RECON-B0`
specification on the `β_V/β_B` anchor.

**Measured by the Researcher at the evidence base, bytes preserved:**

    GATES.md      β_V/β_B = −(k+2)   kill values −3 and −5
    P2-HK-01      β_V/β_B = −3       at k=1
    RECON-B0 spec (k+2), 3, 5        UNSIGNED

**The repository is consistent at MINUS in both places. The unsigned
form is the Researcher's, carried into the `RECON-B0` specification
without checking it against the gate.**

**THIS DISCREPANCY BLOCKS `RECON-01`'s PRE-REGISTRATION.** **A blind
comparison whose target sign is undecided is not a blind comparison**:
a pipeline returning `+3` could be read as a sign-convention artefact or
as a failure, and that reading would be made AFTER seeing the number.
**Both kill criteria are also sign-specific — "stuck at `−3`" and "stuck
at `3`" are different tests.**

**Report it and say it blocks.** **Do not resolve it** — the reconciliation
is its own task and this one does not scope it.

**1b. `CONVENTIONS.md:24` freezes the Wilson parameter `r = 1`, while
`D-1c`'s `R1` treats `r` as an unfrozen constituent.**

**Measured by the Researcher: `CONVENTIONS.md:24` reads
`… Wilson term W(p) = r Σ_μ (1 − cos p_μ) with Wilson parameter r = 1`.**

**This is a genuine conflict between two landed artifacts.** **The source
executor reported it and said it was not its to adjudicate. It is not
this task's either.** **Report it, with both anchors, and leave it
open.**

**Note what it would imply if resolved toward `CONVENTIONS.md`**: `R1`'s
constituent count would change, and `D-1c`'s five-node figure rests on
`R1` grouping `r` with three other constituents. **Say that this is a
consequence to be checked by whoever adjudicates it, NOT a conclusion of
this task.**

**1c. `A8b`'s verdict is a LOWER BOUND.** **`R5` and `R1` are
established as dependencies; `R2`, `R3` and `R4` are neither established
nor excluded.** **Do not report `A8b` as "depends on two of five".**

## 2. What this does NOT establish

- **No reconstruction exists.** **Ten components, two usable — a count
  of what would have to be built, not a start on building it.**
- **A component count is not a difficulty.** **Two usable out of ten is
  not "eighty percent remaining" in any meaningful unit.**
- **`P2-BETAV-CIRC-01` remains `RUN`, neither passed nor failed.** **A
  future reconstruction returning `(k+2)` would show the reconstruction
  is correct and would NOT show the historical pipeline was
  non-circular** — the gate says so itself.
- **`P2-BETAV-01` remains `PROPOSED (deferred)`.**
- **The assessment is bounded by the repository.** **A component
  existing outside it is not counted.**
- **Nothing here opens, orders, or decides any of `R1`–`R5`.**

## 3. What this task must not do

- **Do not touch `main` until §7's landing.**
- **Do not modify any file.**
- **Do not adjudicate `1b`'s `r = 1` conflict**, and do not revise
  `D-1c`'s node count on the strength of it.
- **Do not resolve `1a`'s sign discrepancy.**
- **Do not build, run, or prototype anything**, and **do not execute any
  script named in the arriving assessment.**
- **Do not compute any `β` value or ratio** beyond quoting the anchor as
  an anchor.
- **Do not judge whether the historical pipeline is circular.**
- **Do not write the `RECON-01` specification.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 4. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`, accepting either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`ece34f7bacbbee00efa0fecf0be644d593eed72f`. **Report `refs/heads/main`
for contrast.** Report the source at `e219ae0e…` and **that it is not an
ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.** **Any restoration in one line each, with
confirmation that no repository content was touched.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 `e219ae0e…`, merge-base the
evidence base. **Commit 1 must be an ancestor of parent 1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — `A8a` and `A8b`, re-derived from the arriving assessment.**
Report both verdicts, **the lines each rests on**, and **which one the
parallel-or-serial conclusion rests on.**

**Report the cancellation mechanism**: that `N` appears in
`CONVENTIONS.md:20` and `:29`, in the normalisation of `Z`, identically
for both species, and therefore cancels in the ratio. **Verify those two
lines against the repository, not against the assessment.**

**Transcribe the trap sentence** from §0. **A landing that carries the
verdict without the mechanism leaves the next reader able to reverse it
from correct evidence.**

**A7 — The three unresolved items**, per §1, **reported and not
resolved.** **For `1a`, report the three anchors as measured with their
signs preserved, and report that it BLOCKS `RECON-01`'s
pre-registration.** **Read the bytes; a display filter that strips
non-ASCII will remove the very character in dispute, and did so once for
the Researcher.** For `1b`, **quote `CONVENTIONS.md:24` and `D-1c`'s `R1`
anchor as measured**, and **confirm you did not adjudicate.** For `1c`,
**confirm the report does not state `A8b` as a count out of five.**

**A8 — The component inventory, re-derived.** Report **the four mutually
exclusive counts and their sum**, and **the two usable components
named.** **Confirm the classification is reported separately from the
clean-room reuse classification.**

**A9 — Nothing built, nothing run.** **Search the artifact, the report
and the commit messages for any numerical value claimed as newly
computed reconstruction physics output** — determinant or eigenvalue
results, numerical `h`-derivatives, `β` values, `β` ratios beyond
quotation of the anchor, `k`-scan outputs. **Governance and checker
measurements, inventory counts, line numbers, SHAs and timestamps are
expressly excluded from this search.** **Report the search and the
finding.**

**A10 — Scope, frozen manifest. Final base-to-head: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: ece34f7bacbbee00efa0fecf0be644d593eed72f
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-RECON-01_scope-assessment.md
      reports/2026-08-17T1105Z_recon-b0-scope.md
      reports/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
      reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
      specs/2026-08-17T1105Z_recon-b0-scope.md
      specs/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately, and state whether they coincide** — **they do, at four.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **If they appear to conflict,
§8 governs; stop and report.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Report which head each figure was measured at.**

**Measure the UTC time and use the value you measured.**

**A11 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A12 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, all `derivations/P2-BETAV-*`
artifacts, all six microspec artifacts, both registers, and everything
under `scripts/`, `tests/` and `results/`.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four.** **Read the status line SCOPED to
its gate section.**

**Also report, scoped:** `P2-BETAV-RECON-01` is `PROPOSED`,
`P2-BETAV-CIRC-01` is `RUN`, `P2-BETAV-01` is `PROPOSED (deferred)`.
**Confirm none changed.**

**A14 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A15 — The checker over this task's own range**, base `ece34f7b…`, head
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

**A15-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **Expect `P5` to change state** — the merge gives it a
subject where the source task's range had none.

**A16 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A17 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
    commit 3  --no-ff merge of e219ae0e…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-recon-b0.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A14, A16 and A17 for
commits 1–3; **A15's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A10's final
scope stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A15-final; A13 and A14 re-run after the advance; A17
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 7. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `ece34f7b…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no
`science/recon-b0-scope`, no `D-1` branch.** **The source branch is not
deleted and does not move**; verify and report its tip.

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First, and it is the reason this landing matters.** **`A8a`'s NO
DEPENDENCE means the clean-room `β_V/β_B` RATIO reconstruction line may
proceed while `R1`–`R5` remain open.** **It does NOT mean the
reconstruction will succeed, or that the `RECON-01` gate will pass.**

**Ten components are inventoried; TWO have potentially applicable
implementation plus specification, while EIGHT lack a potentially
applicable implementation — seven specification-only and one neither.**

**An earlier draft said "eight are neither implemented nor specified",
which contradicts the arriving inventory**: `neither` is ONE. **The
eight is `7 + 1`, and it counts components lacking a usable
implementation, not components lacking both.**

**Say that a parallel line is an available line, not a completed
one.**

**Second.** **The `N`-cancellation mechanism must land with the
verdict.** **`N` is in `CONVENTIONS.md` and a reader who finds it there
can reverse `A8a` from correct evidence.** **Say that the mechanism is
what makes the verdict checkable.**

**Third.** **`1b`'s `r = 1` conflict is between two LANDED artifacts.**
**`CONVENTIONS.md` freezes it; `D-1c`'s `R1` treats it as unfrozen.**
**Both are on `main` and this task adjudicates neither.** **Say that the
repository now carries a contradiction it did not carry before this line
began**, and **say that resolving it may change `D-1c`'s node count.**

**Fourth.** **`A8b` is a lower bound.** **`R2`, `R3` and `R4` are
neither established nor excluded as dependencies of the assembled
quantity.** **Do not let "depends on `R5` and `R1`" read as "depends on
exactly two".**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing**, and do not rename any arriving path.
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not adjudicate, build, run, or compute.**
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

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's two verdicts, the lines each rests on, the cancellation
  mechanism verified against `CONVENTIONS.md`, and the trap sentence**;
- **A7's three unresolved items**, with the three sign anchors quoted as
  measured, the blocking statement for `1a`, and both `r = 1` anchors
  quoted;
- **A8's four counts, their sum, and the two usable components named**;
- **A9's search and finding**;
- **A10's two scope figures and the arriving-path statement**;
- **A11's merge case, stated BEFORE the blob comparisons**;
- **A12's path count**;
- **A13's four invariants plus the three `BETAV` gate statuses**;
- **A14's six exit statuses, before and after**;
- **A15's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and **`P5`'s state at commit 3 versus commit 4**;
- **A16's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§8's four Rule 16 junctions**;
- **whether landing a parallel line made you want to start building it,
  adjudicate the `r = 1` conflict, or revise `D-1c`'s node count.**
  **Say which and why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from ece34f7b with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = ece34f7bacbbee00efa0fecf0be644d593eed72f;
                source = e219ae0e5e2a740c9212795599bb37460ba8d5bf, NOT
                an ancestor of main. Merge CLEAN; merge-base =
                ece34f7b; 6 additions and 0 modifications at the merge
                commit; 7 and 0 with a placeholder report; the landing
                fast-forward is available. Four arriving paths, all
                additions, carrying the token 1105Z.

    target      the sign of the β_V/β_B anchor
    method      read GATES.md's RECON-01 section and P2-HK-01 WITHOUT
                a non-ASCII display filter
    MEASURED    GATES.md: "β_V/β_B = −(k+2)", kill values "−3" and
                "−5". P2-HK-01: "β_V/β_B = (K/4)/(−K/12) = −3". The
                repository is consistent at MINUS.
    RETRACTED   the RECON-B0 specification stated the anchor unsigned as
                (k+2), 3, 5. That was the Researcher's, taken from
                CIRC-01 without checking the gate.
    NOTE        the Researcher's first attempt to read this stripped the
                Unicode minus (U+2212) through tr -cd '[:print:]' and
                displayed "= (k+2)", nearly reporting the gate as
                unsigned too. A7 requires the bytes read.

    target      the r = 1 conflict
    method      read CONVENTIONS.md line 24 at the evidence base
    MEASURED    it reads "... Wilson term W(p) = r Σ_μ (1 − cos p_μ)
                with Wilson parameter r = 1." The freeze is explicit.
                D-1c's R1 treats r as an unfrozen constituent. Both
                artifacts are on main. §1b requires this reported and
                NOT adjudicated.

    target      A8a's verdict and its mechanism
    method      read the arriving assessment at the source tip
    MEASURED    A8a: IT DEPENDS ON NONE OF THEM. A8b: YES — on R5, and
                on R1. The conclusion rests on A8a alone. The mechanism
                recorded is that N appears in CONVENTIONS.md:20 and :29
                in the normalisation of Z, identically for both species,
                and cancels in the ratio.
    NOT VERIFIED by this author: lines 20 and 29 of CONVENTIONS.md were
                not read here. A6 requires them checked against the
                repository rather than against the assessment.

    target      the component inventory
    method      NOT MEASURED by this author. "Ten components, two
                usable" is the source executor's figure, taken from
                commit 4's message. A8 requires it re-derived.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
