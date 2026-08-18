# Task specification — integrate the `ε` tractability assessment, and land it

Specification evidence base: `af145d5a3e36e6bca62f038092748ada3abdcec1`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-eps-b0
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/eps-b0-scope
                       efb8d63f0f2e4a208dc735af0936a40db7ce3fe8

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`af145d5a…`.

    source contributes          4 additions, 0 modifications
    this task authors           3 — spec, review, report
    cumulative at merge (3)     6 additions
    cumulative at final (4)     7 additions

**`6` is CUMULATIVE, not the merge's contribution.** **Any conflict is
an immediate STOP.** **Nothing is modified.**

**THIS IS THE FIRST OF TWO INTEGRATIONS FROM THE SAME BASE.**
**`science/channel-b0-spin-scope @ 8c27a606…` also branches from
`af145d5a`.** **It is NOT integrated here and must not be merged.**
**After this lands, its integration will need a new base.**

---

## 0. The verdict

    BLOCKED PENDING A RULING
    R1 DEPENDENCE ESTABLISHED, and R1 is OPEN

**Rider: even if `R1` were ruled tomorrow, this route would not produce
a NUMBER.**

**`ε` was the candidate route to reversing `SRC-01a`'s chain** — from
`SPARC → r_c → m_θ → ε` to `microscopic theory → ε → m_θ → r_c`.
**That reversal is not available, and it fails twice independently.**

## 1. How the `R1` dependence was established, and why the method matters

**Textually, from two landed documents set side by side — NEITHER
CITING THE OTHER ON THIS POINT.**

    paper:526-528   effects that explicitly break the chiral U(1): the
                    axial anomaly, realized on the lattice through the
                    Wilson term and the surviving doublers, together
                    with the discrete (Z_M) structure of the phase

    ledger:78-79    "the canonical lattice Dirac operator; the species
                    ledger and doubling treatment"
    ledger:89       CONTROLS  W8  the Wilson parameter r
    ledger:96       STATUS OPEN

**`ε`'s stated mechanism is item-for-item `R1`'s subject.**

**And `ε` had never been mapped to any `R`-node before**: the ledger,
`ONTOLOGY-01` and `ROUTE-01` return zero on `varepsilon` and `epsilon`.
**This is a newly established dependency, not a restatement.**

**The executor's own limit, and it must land with the finding:**

> **It did NOT claim `ε`'s VALUE would change under a different ruling
> — that would be physics.** **What is established is that the
> computation AS DESCRIBED cannot be posed without the ruling, because
> its stated ingredients are the ruling's subject.**

**Report that distinction.** **A dependency established textually is
weaker than one established physically, and it is the one that was
established.**

**`R2`, `R3`, `R4`: `NOT ESTABLISHED`, not `INDEPENDENT`.** **The
repository is silent about `ε` there, and silence is not
independence.** **`R5` is established for the `Λ` leg only.**

## 2. The two independent failures downstream of `R1`

**Either alone is sufficient. `R1` is not the only thing blocking this
route.**

### 2a. The coefficient is not closed — and the gap is INSIDE `ε`

    K ~ ε Λ⁴        :533
    m_θ² ~ ε Λ²     :598
    f ~ v           :589

**Three tildes.** **Six of the seven `m_\theta` lines carry `~`; the
single equality is `r_c = 1/m_θ`, which is `SRC-01a`'s relation.**

**And the ambiguity is inside `ε`'s OWN DEFINITION, not downstream of
it.** **`ε` is introduced by a scaling relation, so "computing `ε`" is
not numerically well-posed until a normalisation is fixed — and none
is.**

### 2b. `Λ` loops rather than reverses

**Measured: `CONVENTIONS.md:31` sets `Λ ≡ 1` — a UNIT, not a value.**
`:717` assumes it at the Planck scale.

**The one relation to a measurable, `M_Pl² = c₂NΛ²/(8π²)` at `:714`,
requires an OBSERVED `M_Pl`, plus `c₂` — which `:737-739` calls "a
defining assumption" — plus `N`, which is `R5` and open.**

> **So the chain does not reverse; it loops.**

**The best outcome reachable from a settled `R1` is the SECOND verdict,
`TRACTABLE BUT ONLY A RELATION`.** **The apparent shortcut is not one.**

## 3. Three further repository findings

- **No gate covers this object.** `GATES.md` returns zero on all nine
  terms across its fourteen sections, and the repository's own Goldstone
  artifact returns zero on six of them.
- **`M`, the order of the discrete `Z_M` phase symmetry, is a required
  input that no document fixes and no `R`-node covers.** Without it
  `V_θ ≃ −K cos(Mθ)` is not computable.
- **The anomaly is ONE TERM, not all of `ε`** — `:601` says `ε`
  "collects the explicit-breaking coefficients", plural, and
  `:541-543`'s open computation is about "the anomaly contribution".

## 4. What this does NOT establish, and what this task must not do

- **This is a finding about what the repository says, not about whether
  `ε` is computable in principle.** **A physicist with different methods
  might compute it; nothing here bears on that.**
- **`R1 DEPENDENCE ESTABLISHED` is textual.** **Do not report it as a
  physical necessity.**
- **`R2`/`R3`/`R4` `NOT ESTABLISHED` must not be reported as
  `INDEPENDENT`.**
- **Do not touch `main` until §6's landing.**
- **Do not modify any file.**
- **DO NOT COMPUTE `ε`, `m_θ`, `Λ`, `r_c`, or any suppression factor.**
  **The source executor reported the specific temptation: `:621` gives
  `ε ~ m_θ²/Λ²`, `:620` gives `m_θ`, `:717` puts `Λ` at the Planck scale
  — two numbers and a division.** **That division would run `SRC-01a`'s
  chain and launder an observational input into a microscopic quantity.**
  **It was not performed and must not be here.**
- **Do not merge or reference `science/channel-b0-spin-scope`.**
- **Do not adjudicate `R1`–`R5` or recommend a next task.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` **pasted from `git rev-parse` output** and
confirm it is `af145d5a3e36e6bca62f038092748ada3abdcec1`.

**Report the source tip PASTED FROM COMMAND OUTPUT** and confirm it is
`efb8d63f0f2e4a208dc735af0936a40db7ce3fe8`, **and that it is not an
ancestor of `main`.**

**Also report `science/channel-b0-spin-scope`'s tip and confirm it is
NOT merged here.**

**Every SHA in your report is pasted from command output.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0.

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 the source tip as re-resolved,
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The `R1` dependence, re-derived from both documents at the
head.** **Quote `paper:526-528` and the ledger's `:78-79`, `:89` and
`:96` verbatim with line numbers.** **Confirm neither document cites the
other on this point.**

**Confirm `varepsilon` and `epsilon` return zero in the ledger,
`ONTOLOGY-01` and `ROUTE-01`** — the dependency is newly established.

**Report the executor's own limit verbatim**: the claim is that the
computation as described cannot be posed, NOT that `ε`'s value would
change.

**A7 — `R2`–`R5` states.** **Report each as `INDEPENDENT`, `DEPENDENCE
ESTABLISHED`, or `DEPENDENCE NOT ESTABLISHED`.** **Confirm `R2`, `R3`
and `R4` are reported `NOT ESTABLISHED` and not `INDEPENDENT`.**

**A8 — The coefficient failure**, per §2a. **Quote the three relations
with lines.** **Report the tilde count on `m_\theta` lines**, and
**report that the ambiguity is inside `ε`'s own definition.**

**A9 — The `Λ` failure**, per §2b. **Quote `CONVENTIONS.md:31` and
`:714`, `:717`, `:737-739`.** **Report that `Λ ≡ 1` is a unit and not a
value**, and **that the chain loops.**

**A10 — The three further findings**, per §3, **each verified at the
head.** **Report `GATES.md`'s zero across its fourteen sections**, the
`Z_M` order `M` gap, and **that the anomaly is one term of `ε` and not
all of it, with `:601` quoted.**

**A11 — Nothing computed.** **Search the artifact, the report and the
commit messages for any physical-unit numeral, any suppression factor,
and any quotient of manuscript values.** **Governance measurements, line
numbers, counts and SHAs are excluded.** **Report the search and the
result.** **The source executor reported the artifact contains no
physical-unit numeral at all; verify.**

**A12 — Scope, frozen manifest. Cumulative final: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: af145d5a3e36e6bca62f038092748ada3abdcec1
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-EPS-B0_epsilon-tractability-scope.md
      reports/2026-08-18T2124Z_eps-b0-scope.md
      reports/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
      reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
      specs/2026-08-18T2124Z_eps-b0-scope.md
      specs/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the cumulative figure at each commit AND the source's own
contribution, separately labelled** — expected cumulative 1, 2, 6, 7;
contribution 4.

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **Measure the UTC time and use
the value you measured.**

**A13 — Which merge case.** **The merge-base is the evidence base**, so
no commit on `main` could have touched an arriving path — report that,
**then** the four blob comparisons.

**A14 — Nothing existing changed.** Every path blob-identical at the
head, **`paper/emergent_gr_paper_v2_15.tex` in particular — report its
blob id at both ends.** **Report the count compared**, and confirm for
`GATES.md`, `CONVENTIONS.md`, **every `derivations/P2-*` artifact —
re-measure the count; it was 49 at this base**, the two
`scripts/recon2026/` files and `tests/test_recon2026_flat_limit.py`,
both registers, and everything under `results/`.

**A15 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — The checker over this task's own range**, base `af145d5a…`, head
**commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming only
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

**A17-final, post-report evidence:** re-run RUN 2 at commit 4, before
the landing.

**A18 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.**

**A19 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
    commit 3  --no-ff merge of efb8d63f…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-eps-b0.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A16, A18 and A19 for
commits 1–3; **A17's two runs with both configs verbatim**; commit 1–3
SHAs pasted from `git rev-parse` and stored messages; commit 4's
intended message; **A12's final scope stated as INTENDED, with the
measured cumulative 6 at commit 3.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A17-final; A15 and A16 re-run after the advance; A19
for commit 4; the push; remote `main` read back from command output;
final ancestry confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The
advance is a fast-forward; `af145d5a…` is the base.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch.**

**REPORT COMMIT 4's SHA, PASTED FROM `git rev-parse`.** **The
`CHANNEL-B0` integration will use it as its evidence base**, and it
cannot be written into that specification until this one lands.

## 7. Rule 16 assessment

**Rule 16 is operative.** **Five junctions, all five required.**

**First.** **The `R1` dependence is TEXTUAL.** **Two documents describe
the same objects; neither says `ε` needs `R1`.** **Say that the
inference is the executor's, that it is sound as a reading, and that a
physical demonstration was neither attempted nor required.**

**Second.** **`R1` is not the only blocker and is not the deepest one.**
**The coefficient gap sits inside `ε`'s own definition, and `Λ ≡ 1` is a
unit.** **A reader who takes `BLOCKED PENDING R1` as "unblocked once
`R1` lands" would be wrong.** **Say that the best reachable outcome is a
RELATION.**

**Third.** **This closes a route, not a question.** **Whether `m_θ` is
predictable remains open** — what is established is that THIS
repository's stated path to it does not reach a number. **Say that a
different formulation might.**

**Fourth.** **`SRC-01a`'s verdict is unchanged.** **`FORM DERIVED /
SCALE FITTED` stands, and this landing removes the candidate route for
changing the second half.** **Say that the scale remains observational.**

**Fifth.** **`M`, the `Z_M` order, is a required input covered by no
document and no `R`-node.** **Say that the dependency map is
incomplete** — `D-1c` mapped what `D-1` found, and `D-1` was a
reflection-positivity audit.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
- **Modify nothing. Compute nothing. Merge only the named source.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
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

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**, and **every SHA pasted from command
  output**;
- **A1's verbatim `origin` URL, both pasted SHAs, and the `CHANNEL-B0`
  tip with confirmation it was not merged**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's quoted passages, the zero-check, and the executor's limit**;
- **A7's four `R`-node states**;
- **A8's three relations and the tilde count**;
- **A9's `Λ` quotations and the loop statement**;
- **A10's three findings**;
- **A11's search and result**;
- **A12's cumulative figures and contribution, separately labelled**;
- **A13's merge case, stated BEFORE the blob comparisons**;
- **A14's path count, the manuscript blob id at both ends, and the
  `P2-*` count re-measured**;
- **A15's four invariants**;
- **A16's six exit statuses, before and after**;
- **A17's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A18's counts**;
- **the landing**, including **commit 4's SHA pasted from command
  output** for the next integration's base;
- **§7's five Rule 16 junctions**;
- **whether landing a blocked route made you want to compute `ε`, to
  declare `R1` the only blocker, or to call `R2`–`R4` independent.**
  **Say which and why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories, included even if there were none.

## 10. Pre-issue literal verification record

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from af145d5a with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = af145d5a3e36e6bca62f038092748ada3abdcec1;
                source = efb8d63f0f2e4a208dc735af0936a40db7ce3fe8, NOT
                an ancestor. Merge CLEAN; merge-base = af145d5a.
                CONTRIBUTES 4 additions, 0 modifications. CUMULATIVE 6
                at the merge, 7 with a placeholder report.

    target      the second branch from the same base
    method      git rev-parse; git merge-base --is-ancestor
    MEASURED    science/channel-b0-spin-scope = 8c27a606…, also branched
                from af145d5a, also 4 additions and 0 modifications, and
                its merge from this base is also CLEAN. It is NOT
                integrated by this task. After this lands, its
                integration must be rebased onto commit 4.

    target      the R1 dependence passages
    method      read paper lines 526-528 and the ledger at 78-79, 89, 96
    MEASURED    paper:526-528 "effects that explicitly break the chiral
                U(1): the axial anomaly, realized on the lattice through
                the Wilson term and the surviving doublers, together
                with the discrete (Z_M) structure of the phase".
                ledger:78-79 quotes ROUTE:189-190 "the canonical lattice
                Dirac operator; the species ledger and doubling
                treatment"; ledger:89 "CONTROLS W8 the Wilson parameter
                r"; ledger:96 "STATUS OPEN". Both present. A6 requires
                them re-read.

    target      Λ's status
    method      read CONVENTIONS.md line 31
    MEASURED    "| Cutoff and lattice units | `Λ ≡ 1` (continuum),
                `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |"
                Λ ≡ 1 is a UNIT CONVENTION, not a determined value.

    target      the P2-* artifact count
    method      git ls-tree over derivations/
    MEASURED    49 at this base. A14 requires it re-measured.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
