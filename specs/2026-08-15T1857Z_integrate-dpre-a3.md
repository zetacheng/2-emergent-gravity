# Task specification — integrate the plaquette-provenance result, and land it

Specification evidence base: `773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`

    Branch to create   science/integrate-dpre-a3
    Cut from           authoritative main @ 773dd2cb…
    Source             science/dpre-a3-plaquette-provenance
                       4b27009fbc7692f1e22bd68a137dfbb3a1e8deab

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `773dd2cb…`, **6 additions and 0 modifications at
the merge commit.** **Any conflict is an immediate STOP.**

**Nothing is modified.** No gate, no pin, no register, no script, no
existing artifact.

**The source cites no branch SHA** — measured: the only bare hex-like
token in its artifact is a random seed, `20260815`. **The previous
integration in this line had to merge two branches because one cited the
other; this one does not.**

---

## 0. What lands

**A closed derivation, and the closure of a route.**

    P_μν(x) · 1₄ = Γ(x)† [γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹] Γ(x) = Γ(x)† C_μν Γ(x)

**`C_μν = −1·1₄` is a scalar, so the conjugation drops out and
`P_μν = −1` everywhere.** **Verdict: `REPRESENTATION-EQUIVALENT`.**

**It is not a coincidence of value: it is the same Clifford structure
represented differently** — through gamma matrices in `naive`, `Wilson`
and `overlap`, and through link phases after staggered spin
diagonalisation.

**How real that structure is under the substrate ontology is not
something `A3` established**, and this specification does not say. **An
earlier draft of this paragraph said the structure is "as real in
staggered as the gamma matrices are in the other three" — an ontology
claim the derivation does not carry, written two lines above a passage
forbidding the report from amplifying the artifact.**

**That last clause is the artifact's own wording and this specification
does not strengthen it.** **Measured: the arriving artifact says at line
380 that the verdict "is a statement that the four candidates carry the
same structure at the level tested", and the phrase "as real in staggered
as in the other three" appears NOWHERE in it** — it is in the execution
summary only.

**Do not carry the summary's phrasing into the report.** **How real the
Clifford structure is under the substrate ontology is not something `A3`
established**, and **an artifact that avoided the claim should not have
it added by the task that integrates it.**

**This is the third time in this line that an execution summary has
stated something stronger than its artifact** — after *violate outright*
and *physical difference between candidates*. **The first two required
specification repairs; this one does not, because the artifact is
correct.** **`A6a` requires it verified rather than taken from here.**

**Three previously separate facts become consequences of one identity:**
the value; the site-independence, because the commutator is scalar so the
only `x`-dependence cancels; and the redefinition-invariance, because a
scalar is invariant under conjugation. **The last two share a cause, and
no argument from matching numbers could have shown that.**

**The companion question has the same answer.** The translation defect is
pure gauge on all four axes — 96 mismatches re-measured and split
`48 / 32 / 16 / 0`, the zero because `η_μ` depends only on lower-indexed
coordinates — **so the translated configuration carries the same
plaquettes and contributes no invariant of its own.** **The two questions
are one question.**

## 1. What this does NOT establish

- **No candidate is eliminated, preferred or ranked.** **All four carry
  the same invariant and differ only in representation** — gammas for
  `naive`, `Wilson` and `overlap`, link phases for `staggered`.
- **This is not corroboration of the dossier.** The derivation and the
  dossier's staggered ledger **rest on the same reconstruction**, so
  agreement between them is not independent support.
- **The comparison is at one level.** **A negative result at the
  plaquette and translation level is not a negative result at every
  level**, and nothing here shows the space of redefinition-invariant
  structures is exhausted.
- **Reflection positivity is the outstanding requirement among those
  ALREADY IDENTIFIED. It is not established to be the only one that
  could exist.** **Do not write it as the only one.**
- **`C-iii` and `D0` are not unblocked.**

## 2. The route this closes, and what it costs

**Three cheap discriminants have now been tried and none discriminates on
grounds the programme has already committed to:**

    isotropy reading      elimination is of a PRESENTATION, and only
                          under the stronger reading
    finite-range case     elimination costs a NEW ontology commitment
                          that line 115 does not require
    plaquette phase       no difference — all four carry the same
                          invariant

**Under the weaker reading of each question, all four candidates
survive.**

**Report that as the state after this lands**, and **report that THE
THREE CHEAP ROUTES IDENTIFIED AND TESTED SO FAR are exhausted — not that
cheap routes in general are, and not that the selection problem is nearly
solved.**

**The distinction matters because it is the one §7's third junction
turns on**, and because a summary that shortens *three tested routes* to
*cheap discriminators exhausted* is one step from *only reflection
positivity remains*, which nothing establishes.

## 3. One specification defect in the source task, carried and not repaired

**The source specification's pre-issue record named "81 base sites" for
the plaquette measurement and did not state the shift convention.**

**The executor's first probe used periodic identification at odd extent
`L = 3` and returned mixed `{+1, −1}`** — **apparently contradicting the
specification.** **`η_μ` is periodic only under even shifts**, so `x+3 ≡
x` flips signs that are not part of the local structure. **Recomputed
with integer shifts it is uniformly `−1` at `3⁴`, `4⁴` and `5⁴`.**

**The executor diagnosed rather than reported, and recorded the
convention in the artifact itself** — **because a reader reproducing the
derivation on a periodic odd lattice would disagree with a correct
result.**

**The defect is the Researcher's**: `81` is exactly the extent at which
the artefact bites, and the criterion should have stated the convention.
**Report it. Do not repair the source, and do not register it** — the
governance register is frozen and this is a science-side specification
error, already corrected inside the artifact that lands.

**Independently verified for this specification:** the reconstruction
identity `Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄` holds in `324` of `324` cases
over a `3⁴` block, and the plaquette is uniformly `−1` under integer
shifts at `L = 3, 4, 5`.

## 4. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any arriving file**, and **do not modify anything
  else** — this task has no authorised modifications.
- **Do not eliminate, prefer or rank any candidate.**
- **Do not rule on either `D-pre-A2` question.**
- **Do not write that reflection positivity is the only possible
  remaining discriminator.**
- **Do not scope the transfer matrix or `D-pre-B`.**
- **Do not add a register entry anywhere**, including for §3's defect
  and for the `C3` multi-specification residual the source task
  re-confirmed.
- **Do not claim `C-iii` or `D0` is unblocked.**

## 5. Acceptance criteria

**A1 — Refs.** `refs/heads/main` resolves to
`773dd2cb2ad8fb457e23150f0cb19ab80dd614a5` and
`science/dpre-a3-plaquette-provenance` to
`4b27009fbc7692f1e22bd68a137dfbb3a1e8deab`. **Any mismatch → STOP.**
**Report the exit status of `--is-ancestor` for the source against
`main`** — expected non-zero.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**
**If absent, blank, or naming a different digest, STOP and say which.**
Report both digests equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 4b27009fbc7692f1e22bd68a137dfbb3a1e8deab
    merge-base(parent 1, parent 2)
             = 773dd2cb2ad8fb457e23150f0cb19ab80dd614a5

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.

**A4 — No conflict.** Report the conflict list. **It must be empty.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 7 additions and
0 modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
      reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
      reports/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
      reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
      specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
      specs/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive from the source, all additions; three are
authored here, all additions.** **`modify:` is `[]` and must remain
so.**

**At the merge commit, before the report exists, the count is 6
additions and 0 modifications.** **Report which head each figure was
measured at.**

**A6 — Source-branch paths, derived from the SOURCE and not from A5.**
**Expected four additions, zero modifications.** **Report any
disagreement with A5.** **Report the count of ARRIVING PATHS and the
count of ARRIVING ADDITIONS separately** — the previous integration's
specification conflated them, and here they happen to coincide at four,
**which is the case in which a conflation is least likely to be
noticed.**

**A6a — The summary's phrasing is not in the artifact, verified.**
**Search the arriving artifact for "as real" and for "not merely a
representation", and report the search.** **Expected: zero hits.**
**Then quote the artifact's own statement of what the verdict means**,
with its line number. **If the phrase IS present, report it as a finding
and do not repeat it in the report** — the artifact is integrated as
written either way, but the report must not amplify it.

**A7 — Which merge case.** **The merge-base is the evidence base, so no
commit exists on `main` that could have touched an arriving path** —
report that, **then** the blob comparisons. **All four arriving paths
blob-identical to the source tip.**

**A8 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, the ontology, both earlier
microspec artifacts, both registers, `docs/GOVERNANCE-DEBT.md`, and
everything under `scripts/`, `tests/` and `results/`.

**A9 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A10 — The derivation reproduces at the merged head.** Independently
recompute, from the artifact at the head:

- **the reconstruction identity** `Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄`,
  over a stated block, **with the gamma representation stated and
  verified to satisfy `{γ_μ, γ_ν} = 2δ_μν`**;
- **the plaquette product under INTEGER SHIFTS at `L = 3, 4, 5`** —
  **state the convention explicitly**, per §3;
- **the Clifford commutator on all six planes.**

**Report all three.** **Expected: the identity holds everywhere, the
plaquette is uniformly `−1`, and the commutator is `−1·1₄`.**

**This criterion exists because §3 records a convention under which a
correct result reads as wrong.** **Report the convention you used, not
only the numbers.**

**A11 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A12 — The checker over this task's own range**, base `773dd2cb…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.**

**`RUN 1` has TWO specifications in range** — the arriving one and this
task's — **and both declare `append_only: DECISION_LOG.md` alone.**
**They agree, so the multi-specification conflict the earlier integration
met should not arise.** **Report what `RUN 1` actually did**, and **if it
raises, report that as a finding and note that `RUN 2` governs.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.**

**A12-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A13 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected.** **A change is a finding.**

**A14 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
    commit 3  --no-ff merge of 4b27009f…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A11, A13 and A14 for
commits 1–3; **A12's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A5's final scope
stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A12-final; A9 and A11 re-run after the advance; A14 for
commit 4; the push; remote `main` read back; final ancestry confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The advance
is a fast-forward; `773dd2cb…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **The source branch
is not deleted and does not move** — verify and report its tip after the
advance.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **A closed derivation looks like progress toward selecting an
operator. It is the opposite.** **This result removes a candidate
discriminator rather than a candidate.** **Report that all four survive,
and report the three cheap routes now tried**, per §2.

**Second.** **This is not corroboration of the dossier**, because both
rest on the same reconstruction. **Say so.**

**Third.** **Reflection positivity is the outstanding requirement among
those already identified.** **Do not write that it is the only one that
could exist** — nothing establishes that the space of
redefinition-invariant structures is exhausted, and the source
specification had to be revised once for exactly that overreach.

**Fourth.** **A specification defect of the Researcher's is landing
inside the artifact that corrects it.** **The convention error of §3 is
recorded in the arriving artifact, and the specification that caused it
is landing beside it uncorrected.** **Say that a reader meets the
correction and the cause in the same merge**, and **say that nothing in
the repository links them** — which is `G-03` in the debt register,
unrepaired.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.** There are no authorised modifications.
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not eliminate, prefer, rank, or scope the transfer matrix.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
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
- **A3's three values, separately derived**;
- **A5's two scope figures**, with the head each was measured at;
- **A6's source-derived path set**, and **the arriving-path and
  arriving-addition counts stated separately**;
- **A6a's search and the artifact's own wording with its line number**;
- **A7's merge case, stated BEFORE the blob comparisons**;
- **A8's path count**;
- **A9's four invariants**;
- **A10's three recomputations, with the shift convention and the gamma
  representation stated**;
- **A11's six exit statuses, before and after the advance**;
- **A12's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and what `RUN 1` did;
- **A13's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§7's four Rule 16 junctions**;
- **whether landing a closed derivation made you want to select an
  operator or scope the transfer matrix.** **Say so, and confirm you did
  not**;
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

    target      refs
    method      git fetch; git rev-parse; git merge-base --is-ancestor
    MEASURED    main = 773dd2cb…; source =
                4b27009fbc7692f1e22bd68a137dfbb3a1e8deab; the source is
                NOT an ancestor of main.

    target      the merge
    method      dry run from 773dd2cb with two placeholder commits, then
                git merge --no-ff of the pinned ref
    MEASURED    CLEAN; merge-base = 773dd2cb; 6 additions and 0
                modifications at the merge commit; 7 and 0 with a
                placeholder report; 773dd2cb is an ancestor of that
                head, so the landing fast-forward is available.

    target      the append-only declarations of the two specifications
                RUN 1 will select
    method      parse both scope blocks with the declaration parser
                extracted VERBATIM from the checker at 773dd2cb
    MEASURED    the arriving A3 specification declares exactly
                ['DECISION_LOG.md']; this specification declares exactly
                ['DECISION_LOG.md']. They agree, so no declaration
                difference is predicted and the C3 multi-specification
                conflict should not arise. A12 requires the outcome
                measured rather than taken from here.

    target      whether the summary's stronger phrasing is in the
                artifact
    method      grep the arriving artifact for "as real" and for
                "not merely a representation"
    MEASURED    ZERO hits. The artifact states at line 380 that the
                verdict "is a statement that the four candidates carry
                the same structure at the level tested". The stronger
                phrasing exists only in the execution summary, and the
                Reviewer's objection was raised against the summary.

    target      whether the arriving artifact cites an unintegrated
                branch, as the previous source did
    method      extract every bare 8-hex token from the arriving
                artifact
    MEASURED    ONE token, 20260815 — the random seed A3(iii) required
                stated. NO branch SHA is cited. One merge suffices.

    target      the reconstruction identity
    method      build an explicit 4x4 Euclidean gamma representation as
                Kronecker products of Pauli matrices, verify
                {g_mu,g_nu} = 2 delta, form Gamma(x) as the ordered
                product of g_mu^{x_mu}, and test the identity over a
                3^4 block
    MEASURED    324 of 324 cases hold.

    target      the plaquette under the convention §3 records
    method      compute the plaquette from eta with INTEGER SHIFTS at
                L = 3, 4, 5
    MEASURED    uniformly -1 at all three extents.
    NOTE        the source specification's "81 base sites" is a 3^4
                block, exactly the extent at which periodic
                identification produces mixed signs. The convention, not
                the extent, is what the criterion should have stated.
                §3 records this as the Researcher's defect.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path, one per line, matching A12's config.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                773dd2cb and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                the manifest lists seven and 'modify: []' contributes
                none; parse OK, counted equals stated per category.
