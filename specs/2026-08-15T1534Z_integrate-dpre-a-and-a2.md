# Task specification — integrate `D-pre-A` and `D-pre-A2` together, and land them

Specification evidence base: `ae3604def317667b44ea59458569ba105463fd6b`

    Branch to create   science/integrate-dpre-a-and-a2
    Cut from           authoritative main @ ae3604de…

    Sources, merged in THIS ORDER and no other:
      1  science/dpre-a-kinetic-operator-dossier
         27fabe17…
      2  science/dpre-a2-selection-discriminants
         4749961a486c796f560bef94160c1e397d3e8a90

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**Two merges, both measured clean.** Dry run from the evidence base:
merge 1 gives **6 additions and 1 modification**; merge 2 gives **10 and
1**; with this task's report, **11 additions and 1 modification.**
**Any conflict is an immediate STOP.**

---

## 0. Why both together, and why not `D-pre-A2` alone

**`D-pre-A2`'s artifact cites the `D-pre-A` dossier by branch SHA, twice.**
**Measured: `27fabe17…` is an ancestor of neither `main` nor the
`D-pre-A2` branch.**

**So integrating `D-pre-A2` alone would put on `main` an artifact whose
two load-bearing citations resolve to a branch that is not there.**

**That is the shape the governance debt register already carries as
`G-08`'s neighbour and as the classification provenance gap** — an
identifier cited on `main` whose authoritative source is absent from
`main`. **This line found that failure; it should not commit it.**

**Hence one task, two merges, dossier first.**

## 1. What lands

**A candidate dossier for the canonical kinetic operator, and a test of
two cheap discriminants.**

    D-pre-A    four species ledgers, each derived by its own
               formulation's method; reflection positivity NOT
               ESTABLISHED for all four; compatibility 6 COMPATIBLE,
               0 INCONSISTENT, 10 NOT ESTABLISHED; species-to-N mapping
               NOT ESTABLISHED for all four, so no revised G_c;
               DEFERRED-04 recording option (b) as a downstream
               hypothesis

    D-pre-A2   question one DISCRIMINATING — INTERPRETIVE: Reading A
               eliminates staggered as standardly presented, Reading B
               eliminates none;
               question two DISCRIMINATING — ADDITIVE: Case A
               eliminates overlap, Case B eliminates none, and the
               ontology is silent on finite range

**No operator is selected. No ontology question is ruled.** **Both
remain the PI's.**

## 2. What this does NOT establish

- **`C-iii` is not unblocked, and `D0` is not unblocked.** A dossier and
  a discriminant test are neither a freeze nor an Euclidean–spectral
  equivalence.
- **Reflection positivity remains NOT ESTABLISHED for all four
  candidates**, and the species-to-`N` mapping likewise. **Two resolved
  readings are not a resolved selection problem.**
- **Question one's elimination is of a PRESENTATION.** Whether another
  staggered convention is manifestly axis-symmetric while preserving the
  plaquette orientation condition is `NOT ESTABLISHED`. **Any statement
  that Reading A eliminates staggered must carry that qualifier.**
- **Question two's elimination costs a new physical commitment.** **The
  emergence mechanism at ontology line 115 does not require finite
  range** — it requires a convergent derivative expansion, which
  exponential localisation supplies. **Adding finite range would protect
  a claim about the substrate the ontology has not made.**
- **The adopted parameter domain is unaffected.** No revised `G_c`
  follows, because no species-to-`N` mapping was established.

## 3. One finding carried forward, and not registered

**The staggered plaquette phase is redefinition-invariant and uniform.**

`D-pre-A2` reports the plaquette product as `−1`. **Independently
computed by the Researcher: the product is `−1` on ALL SIX planes at
every site, and it is unchanged under an arbitrary sign redefinition
`ε(x)`, because the `ε` factors cancel around a closed loop.**

**It does not threaten isotropy.** A flux taking the same value on all
six planes is invariant under axis permutation. **The one structure a
redefinition cannot remove is the one that is isotropic**, and the
structure that is not manifestly symmetric — the single-link sign
pattern — is exactly the one a redefinition does remove. **This
strengthens Reading B rather than weakening it.**

**Its PROVENANCE is NOT ESTABLISHED, and an earlier draft of this
section overstated it.**

That draft said the flux is *a physical difference between candidates*
and that *`naive`, `Wilson` and `overlap` carry no background flux*.
**Neither is established.** **The Clifford group commutator
`γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹` equals `−1` on every one of the six planes** —
measured by the Researcher against an explicit `4×4` representation —
**which is the same value the staggered plaquette carries on every
plane.** **Spin diagonalisation is precisely the step that moves the
Dirac structure into site and link phases**, so the staggered flux may be
the representation of an anticommutation structure the other three
formulations already carry in their gamma matrices.

**The accurate statement, and the one to carry:**

> **The staggered formulation carries a uniform, redefinition-invariant
> plaquette phase `P_μν = −1`. Whether this is a staggered-specific
> microscopic structure, or the spin-diagonalised representation of the
> Clifford anticommutation structure already present in the other
> formulations, is NOT ESTABLISHED. This task does not weigh it.**

**IDENTIFIED, PROVENANCE NOT ESTABLISHED, NOT REGISTERED, NOT WEIGHED.**
**Report it in those terms.** **Do not treat it as a discriminator, do
not eliminate or favour any candidate with it, and do not add a register
entry.**

**This integration carries the QUESTION to `main`, not an answer to
it.**

## 4. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any arriving file.** **In particular the dossier is
  correct as written and needs no change** — the loose claim was in the
  `D-pre-A` execution summary, not in the artifact.
- **Do not select a candidate**, rank, recommend, or prefer.
- **Do not rule on either ontology question.**
- **Do not weigh the plaquette flux.**
- **Do not modify `GATES.md`** or any gate state, and **do not modify
  `derivations/P2-LATTICE-ONTOLOGY-01.md`.**
- **Do not add a register entry anywhere.**
- **Do not claim `C-iii` or `D0` is unblocked.**

## 5. Acceptance criteria

**A1 — Refs.** `refs/heads/main` resolves to
`ae3604def317667b44ea59458569ba105463fd6b`;
`science/dpre-a-kinetic-operator-dossier` to `27fabe17…`;
`science/dpre-a2-selection-discriminants` to
`4749961a486c796f560bef94160c1e397d3e8a90`. **Any mismatch → STOP.**
**Also report TWO ancestry exit statuses**, from these two commands and
no others:

    git merge-base --is-ancestor 27fabe17… ae3604de…      expect 1
    git merge-base --is-ancestor 27fabe17… 4749961a…      expect 1

**Both non-zero, meaning the dossier is an ancestor of neither** —
**which is why §0 merges both.** **An earlier draft said "three exit
statuses" without naming a third measurement.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** Report both digests equal.

**A3 — Merge parentage, per merge, each value derived separately.** For
each of the two merges report parent 1, parent 2 and the merge-base as
three independent measurements. **Parent 1 of merge 1 is this task's
review commit; parent 1 of merge 2 is the first merge commit.** **Both
merge-bases are the evidence base** — **verify and report both.**

**A4 — No conflict in either merge.** Report each merge's conflict list.
**Both must be empty.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 11 additions
and 1 modification.**

    stated: 11 additions, 1 modification
    append_only:
      DECISION_LOG.md
      derivations/P2-DEFERRED-ITEMS.md
    authorised_gates: []
    base: ae3604def317667b44ea59458569ba105463fd6b
    head: <commit 5>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
      derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
      reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
      reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
      reports/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
      reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
      reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
      specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
      specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
      specs/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
    modify:
      derivations/P2-DEFERRED-ITEMS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Twelve paths.** **Eight arrive from the two sources — four additions
and one modification from `D-pre-A`, four additions from `D-pre-A2` —
and three are authored here.**

    D-pre-A     4 additions + 1 modification = 5
    D-pre-A2    4 additions                  = 4
    this task   3 additions                  = 3
    total      11 additions + 1 modification = 12

**Report the intermediate figures too: 6 additions and 1 modification at
merge 1, 10 and 1 at merge 2.** **Say which head each figure was
measured at.**

**A6 — Source-branch paths, derived from EACH SOURCE and not from A5.**
Report the path set each source changes relative to the evidence base.
**Report any disagreement with A5's arithmetic.**

**A7 — Which merge case, established BEFORE any blob comparison is
interpreted.** **Both merge-bases are the evidence base, so no commit
exists on `main` that could have touched an arriving path.** **Report
that, then the blob comparisons.**

**`derivations/P2-DEFERRED-ITEMS.md` is modified by `D-pre-A` and by
nothing else** — **verify it, and confirm the merged blob equals the
`D-pre-A` side.** **In a two-sided merge that equality would mean a side
was lost; here it is correct, and A7 exists so the difference is stated
rather than assumed.**

**A8 — The deferred register, append-only, verified two ways.** **Zero
deleted lines**, and **the base file is an exact BYTE PREFIX of the head
file** — **not merely an in-order subsequence.** **`check_p3` enforces
`after.startswith(before)`**, and a subsequence check would pass content
inserted in the middle that `P3` rejects. **Report both measurements and
the byte lengths.** **Confirm four entries, `DEFERRED-01` through
`-04`, and that `-01` to `-03` are byte-identical.**

**A9 — The dossier's citations now resolve.** **Report that
`derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md` cites
`27fabe17…`, the count of citations, and that the cited dossier is
present at the head.** **This is the reason the two merges are one
task.**

**A10 — Arriving artifacts intact.** All eight arriving paths
blob-identical to their contributing source. **Report all eight
comparisons.**

**A11 — Protected paths.** Every path at the evidence base other than
`derivations/P2-DEFERRED-ITEMS.md` is blob-identical at the head. **In
particular `GATES.md`, `CONVENTIONS.md`, `P2-LATTICE-ONTOLOGY-01.md`,
`docs/GOVERNANCE-DEBT.md`, and everything under `scripts/`, `tests/` and
`results/`.** Compare path by path and report the count.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.** **Neither pin names
`P2-DEFERRED-ITEMS.md`** — verify and report it.

**A13 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A14 — The checker over this task's own range**, base `ae3604de…`, head
**commit 4, the second merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md",
                                "derivations/P2-DEFERRED-ITEMS.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each, `P3`'s result for EACH of the two
declared paths, and confirm no `DECLARATION_CONFLICT`.** **One of the two
declared paths is modified by this range and the other is not** — **report
what `P3` returned for each and why they differ.**

**`RUN 1` will select three specifications** — the two arriving and this
task's. **Report the set it actually selected, as measured.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 5, **before
the landing.**

**A15 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected** — neither source adds a test. **A change is a finding.**

**A16 — Commit-message hygiene** on all five commits including both
merges. **Rule 20 binds this task.** **Commits 1–4 go in the report;
commit 5 is post-report evidence.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
    commit 3  --no-ff merge of 27fabe17…       the dossier
    commit 4  --no-ff merge of 4749961a…       the discriminants
    commit 5  reports/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md
    then      fast-forward refs/heads/main to commit 5, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes both
merges**, per Rule 15's timing clause. **The dossier merges first so that
the discriminants' citations resolve at every commit from commit 4
onward.**

**Committed report — measured at commit 4:** A1–A13, A15 and A16 for
commits 1–4; **A14's two runs with both configs verbatim**; commit 1–4
SHAs and stored messages; commit 5's intended message; **A5's final scope
stated as INTENDED, with the measured intermediate figures.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-5; A14-final; A12 and A13 re-run after the advance; A16
for commit 5; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 5.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 5**, not as a SHA. **The advance
is a fast-forward; `ae3604de…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Neither source
branch is deleted and neither moves** — verify and report both tips after
the advance.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** After this lands, `main` carries a dossier and a discriminant
analysis for the canonical kinetic operator. **A reader may take that for
the operator being nearly chosen.** **No candidate is eliminated on
grounds the programme has already committed to.** **Reading B and Case B
eliminate none, and they are the readings that require no new
commitment.** **Say that, and report which candidates survive under the
weaker reading of each question: all four.**

**Second.** **Question two's elimination would cost a new physical
commitment about the substrate**, and **ontology line 115 does not
require it.** **Say that adopting Case A would protect a claim the
ontology has not made**, and **say that this is what makes it a decision
rather than a correction.**

**Third.** **The plaquette flux of §3 is an invariant structure in the
staggered representation whose provenance relative to the other
formulations' Clifford structure is NOT ESTABLISHED.** **Report it in
those words**, and **do not report it as a physical difference between
candidates** — the Clifford commutator carries the same value on the same
six planes, and whether the two are the same structure in different
variables has not been shown.

**Do not let its presence in this report read as a finding for or against
`staggered`, in either direction.**

**Fourth.** **The cheap discriminants are now exhausted.** **What remains
is reflection positivity, which needs a transfer matrix that does not
exist, and which overlaps `D-pre-B`'s Euclidean–spectral equivalence.**
**Say that scoping those together is the open question**, and **do not
scope them here.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify no arriving file, and modify `GATES.md` for no reason.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not select, rank, rule, or weigh.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commits only for the two integrations: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's two ancestry exit statuses, with the commands**;
- **A3's six values**, three per merge, separately derived;
- **A5's three scope figures**, with the head each was measured at;
- **A6's two source-derived path sets**;
- **A7's merge case, stated BEFORE the blob comparisons**, and the
  statement about `P2-DEFERRED-ITEMS.md`;
- **A8's two append-only measurements and the byte lengths**, with the
  **byte-prefix** named as the property `P3` actually enforces;
- **A9's citation count and resolution**;
- **A10's eight blob comparisons**;
- **A11's path count**;
- **A12's four invariants plus the not-pinned verification**;
- **A14's two runs**, both configs verbatim, `declared_source` for each,
  **`P3`'s result per declared path and why they differ**, the section
  count `P7` saw, and the measured RUN 1 subject set;
- **A15's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and both source tips unchanged;
- **§7's four Rule 16 junctions**;
- **whether landing these made you want to select an operator or rule on
  a question.** **Say which and why, and confirm you did not**;
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
this specification asserts about itself.**

    target      the three refs and their ancestry
    method      git fetch; git rev-parse; git merge-base --is-ancestor
    MEASURED    main = ae3604de…; dossier = 27fabe17…; discriminants =
                4749961a486c796f560bef94160c1e397d3e8a90.
                27fabe17 is an ancestor of NEITHER main NOR the
                discriminants branch. That is why §0 merges both.

    target      the discriminants artifact's citations
    method      grep for the dossier SHA in the arriving artifact
    MEASURED    TWO citations of 27fabe17. Integrating the discriminants
                alone would leave both unresolvable from main.

    target      the two merges
    method      dry run from ae3604de with two placeholder commits, then
                git merge --no-ff of each source in order
    MEASURED    both CLEAN. Merge 1: 6 additions, 1 modification.
                Merge 2: 10 additions, 1 modification. With a
                placeholder report: 11 and 1. ae3604de is an ancestor of
                that head, so the landing fast-forward is available.

    target      the deferred register at the combined head
    method      count headings; test byte-prefix against the base blob
    MEASURED    FOUR entries, DEFERRED-01 to -04. The base file is an
                exact byte prefix of the head file.
    NOTE        byte prefix is what check_p3 enforces —
                after.startswith(before) — and is strictly stronger than
                the in-order subsequence test used for CONVENTIONS.md in
                earlier tasks. A8 requires the stronger one here.

    target      the staggered plaquette flux of §3
    method      compute the plaquette phase from the standard staggered
                phases on all six planes over 81 base sites, then
                recompute under a random sign redefinition ε(x)
    MEASURED    the phase is −1 on ALL SIX planes at every site tested,
                and is UNCHANGED under the redefinition — the ε factors
                cancel around the closed loop.
    DERIVED     a flux equal on all six planes is invariant under axis
                permutation, so it does not threaten isotropy.

    target      whether the flux distinguishes staggered from the others
    method      compute the Clifford group commutator
                g_mu g_nu g_mu^-1 g_nu^-1 against an explicit 4x4
                Euclidean gamma representation, on all six planes
    MEASURED    it equals -1 on every plane, the same value the
                staggered plaquette carries on every plane.
    RETRACTED   an earlier draft of §3 said the flux is a physical
                difference between candidates and that the other three
                carry no background flux. NEITHER IS ESTABLISHED. Spin
                diagonalisation moves the Dirac structure into site and
                link phases, so the staggered flux may be that same
                anticommutation structure in different variables.
                Coincidence of value is not identity of structure, and
                the identity has not been shown either way. §3 now
                carries the question and not an answer.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys and values
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                TWO paths, one per line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                ae3604de and executed — not re-implemented
    MEASURED    one scope block; stated 11 additions, 1 modification;
                the manifest lists eleven and one; parse OK, counted
                equals stated per category.
