# Task specification — `D-pre-A3`: the provenance of the staggered plaquette phase

Specification evidence base: `773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`

    Branch to create   science/dpre-a3-plaquette-provenance
    Cut from           authoritative main @ 773dd2cb…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**It asks where a structure comes from. It does not ask what the answer
implies for any candidate.** §4 forbids that, and the prohibition is the
point.

---

## 0. The question, and why it is worth one task

**`D-pre-A2` established, and this task takes as given:** the staggered
phases produce a plaquette product `P_μν = −1` on every plane at every
site, and that product **is invariant under an arbitrary site-sign
redefinition `ε(x)`** — the `ε` factors cancel around a closed loop.

**So it is a structure a redefinition cannot remove.** **That is why it
is worth asking about, and it is also the whole of what is established.**

**The observation that motivates the question, and it is NOT an answer.**
The Clifford group commutator `γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹` **equals `−1` on all
six planes**, measured against an explicit `4×4` Euclidean gamma
representation. **The same value, on the same six planes.**

**COINCIDENCE OF VALUE IS NOT IDENTITY OF STRUCTURE.** **Anyone who
treats the matching numbers as the answer has drawn an equals sign
between two structures not shown to be the same** — **and it is equally
wrong in either direction.** **The integration that landed this question
on `main` carries it explicitly as a question and not an answer.**

**Spin diagonalisation is the step that moves the Dirac structure out of
gamma matrices and into site and link phases.** **That is why the two
might be the same thing in different variables. It is not why they are.**

## 1. What is to be derived

**Whether `P_μν = −1` in the staggered formulation is the
spin-diagonalised representation of the Clifford anticommutation
structure the other formulations carry in their gamma matrices, or
whether it carries content those do not.**

**Work from the reconstruction the dossier already records.** At
`derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md` §3.3,
the identity `Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄` exhibits the naive
operator as four decoupled copies. **That identity is where the gamma
structure becomes a phase.** **Follow it, and report what happens to the
plaquette.**

**Derive, do not assert.** **State every step.** **If the derivation
does not close, say so** — §3's `NOT ESTABLISHED` is a real outcome.

## 2. All four candidates, not one

**Report, for EACH of the four candidates, the redefinition-invariant
structure its formulation carries in the same sense**, and **how it is
represented** — in gamma matrices, in link phases, or otherwise.

**Four rows. `naive`, `Wilson`, `staggered`, `overlap`.**

**Analysing staggered alone would be looking for staggered's problem**,
which is the failure mode `D-pre-A`'s `A10` was written against and
which this task inherits. **A table with one row derived and three
asserted has ranked them.**

**Report the derivation length per candidate**, as `D-pre-A` and
`D-pre-A2` both required.

## 2a. The companion question, same tools, same form

**`D-pre-A2` found that staggered's TRANSLATION invariance holds in
exactly the same "up to a field redefinition" sense as its isotropy** —
96 mismatches over the `2⁴` block, with a restoring redefinition found
for all four axes. **Recorded at lines 224–235 of
`derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md`.**

**So ask the same question of translation that §1 asks of axis
permutation: is there a redefinition-invariant structure on the
translation side, and if so, is it the same structure as `P_μν`?**

**This is not scope creep.** It uses the same tool, takes the same form,
and **asks about provenance rather than consequence.** **If the two
structures turn out to be one, that is a stronger result than either
alone.**

**`NOT ESTABLISHED` is acceptable here and does not affect §1's
verdict.**

## 3. The pre-registered verdicts

**Fixed before the executor derives. Not renegotiated afterwards.**

**`REPRESENTATION-EQUIVALENT`** — `P_μν` is the spin-diagonalised
representation of the Clifford structure the other formulations carry.

**Consequence:** **this cheap discriminator is closed.** The four
candidates do not differ **at the structure tested here**, and **this
task proposes no further representation-level discriminator.**

**Among the formulation-discriminating requirements ALREADY IDENTIFIED,
reflection positivity remains outstanding and requires a transfer matrix
that does not exist.** **State that; do not scope it.**

**THIS TASK DOES NOT ESTABLISH THAT REFLECTION POSITIVITY IS THE ONLY
POSSIBLE REMAINING DISCRIMINATOR.** **An earlier version of this
consequence said it was**, which contradicted §7's fourth junction in the
same document — **that junction correctly states that nothing here shows
the discriminator space is exhausted.** **A consequence and a limitation
that deny each other cannot both be transcribed into an artifact, and
`A7` requires the consequence transcribed verbatim.**

**`STAGGERED-SPECIFIC`** — `P_μν` carries content the Clifford structure
does not.

**Consequence:** **this is the first structural difference between
candidates visible without a new ontology commitment and without a
transfer matrix.** **It does NOT follow that any candidate is eliminated
or preferred.** **A uniform `π` flux on a physically real substrate may
be a defect or a feature, and deciding which is a PI ruling this task
does not prepare and must not anticipate.** **Report the difference and
stop.**

**`NOT ESTABLISHED`** — the derivation does not close.
**Consequence:** name what would close it, **and do not perform it.**
**Say whether what is missing is the same transfer matrix reflection
positivity waits on**, or something else.

**If the derivation establishes something none of these represents, STOP
and report a `SPECIFICATION_DEFECT`.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT ELIMINATE, PREFER, RANK OR RECOMMEND ANY CANDIDATE**, and
  **do not state that any result favours or disfavours one.** **A
  `STAGGERED-SPECIFIC` verdict is a statement about structure, not about
  admissibility.**
- **Do not rule on either `D-pre-A2` question**, and do not indicate
  which reading or case you would adopt.
- **Do not add an ontology requirement**, and do not propose one.
- **Do not construct a transfer matrix**, and do not attempt reflection
  positivity.
- **Do not treat the matching `−1` values as the answer.** §0 governs.
- **Do not modify any existing file.** **Not `GATES.md`, not the
  ontology, not the dossier, not the discriminants artifact, not either
  register.**
- **Do not run any script**, and do not compute anything about the
  exploratory kernel.
- **Do not claim this task unblocks `C-iii` or `D0`.**

## 5. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`. Report the Git blob ids of
`derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md`,
`derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md` and
`derivations/P2-LATTICE-ONTOLOGY-01.md`. **Any ref mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank, absent, or naming a different digest, STOP and
say which.** Report both digests equal.

**This criterion stopped the previous task.** **The review that arrived
carried no digest at all** — zero occurrences of the field, zero 64-hex
strings — **and nothing in the repository would have caught it.**
**`G-05` records that gap.** **Check the field is present before
checking it matches.**

**A3 — The two structures, each established independently before the
derivation begins.**

**(i) The staggered plaquette product on all six planes**, computed and
reported.

**(ii) Its invariance under site-sign redefinition, PROVED for arbitrary
`ε(x)`, not sampled.** Under `η_μ(x) → ε(x) η_μ(x) ε(x+μ̂)`, **each site
sign appears twice around a closed plaquette and cancels**, so
`P'_μν(x) = P_μν(x)` **for every `ε`.** **Give the proof.** **A single
random draw does not establish a statement about all `ε`**, and an
earlier version of this criterion asked only for one.

**(iii) A numerical sanity check of (ii) with a STATED FIXED SEED**, so
the measurement reproduces. **Report the seed and the result.** **This
supplements the proof; it does not replace it.**

**(iv) The Clifford group commutator on all six planes**, against an
explicit gamma representation **you state and verify satisfies
`{γ_μ, γ_ν} = 2δ_μν`.**

**Report all four, and state in the same breath that the agreement
between (i) and (iv) is not the verdict.**

**A4 — The derivation, step by step.** From §3.3's identity
`Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄` **to the plaquette.** **Report every
step.** **A step asserted rather than derived is a STOP.**

**A5 — Four candidates, four rows.** Per candidate: the
redefinition-invariant structure it carries and how it is represented.
**Report the derivation length per candidate**, and **report whether the
table is symmetric in depth.**

**A6 — §2a's companion question.** Report the redefinition-invariant
structure on the translation side, if any, **and whether it is the same
structure as `P_μν`.** **`NOT ESTABLISHED` is acceptable.** **Report the
lines of the discriminants artifact you relied on**, and **verify the 96
mismatches independently rather than quoting them.**

**A7 — The verdict**, one of the three of §3, **in the artifact's first
line**, with its consequence **transcribed verbatim** from §3. **A
rewritten consequence is a STOP.**

**A8 — No elimination, no preference.** **Search the artifact, the
report and the commit messages for any sentence that eliminates, favours,
ranks or recommends a candidate, or that draws an admissibility
conclusion from a structural finding.** **Report the search and the
finding.**

**This criterion is the one most easily satisfied in appearance.** **A
`STAGGERED-SPECIFIC` verdict written in language that treats the
difference as a burden has taken a position without stating one.**
**Report how the difference is characterised**, and **confirm the
characterisation is neutral as to admissibility.**

**A9 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
      reports/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md
      specs/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**A10 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, the ontology, both microspec artifacts, both
registers, and everything under `scripts/`, `tests/` and `results/`.

**A11 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A12 — The checker over this task's own range**, base `773dd2cb…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.**

**`RUN 1` selects one specification in this range — this task's — so it
should not hit the multi-specification declaration conflict the previous
task met.** **Report what it actually did.** **If it raises, report that
as a finding and note that `RUN 2` governs.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.**

**A12-final, post-report evidence:** re-run RUN 2 at commit 4.

**A13 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected.** **A change is a finding.**

**A14 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
    commit 4  reports/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

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

**Four junctions, all four required in the report.**

**First.** **A structural finding is not an admissibility finding.**
**If `P_μν` proves staggered-specific, nothing follows about whether
staggered may be canonical.** **Say that**, and **say that deciding
whether a uniform `π` flux on a physically real substrate is a defect or
a feature is a PI ruling this task does not prepare.**

**Second.** **A `REPRESENTATION-EQUIVALENT` verdict closes this route and
opens none.** **Of the formulation-discriminating requirements already
identified, reflection positivity would then be the outstanding one**,
and it waits on a transfer matrix that does not exist and that overlaps
`D-pre-B`. **Say so, and do not scope it.**

**Do not say it is the only one that could exist.** **The fourth
junction below is why**, and the two must agree.

**Third.** **This task derives from an identity the dossier records.**
**It does not re-derive the dossier's species ledgers, and it does not
check them.** **A result consistent with the dossier is not
corroboration of the dossier**, because both rest on the same
reconstruction.

**Fourth.** **The four candidates' redefinition-invariant structures are
compared at one level only** — the plaquette, and if §2a closes, the
translation sector. **Nothing here establishes that no other
redefinition-invariant structure distinguishes them.** **Say that**, and
**say that a negative result at this level is not a negative result at
every level.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  provenance artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not conclude admissibility from structure**, in the artifact, the
  report, or a commit message.
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's four items** — the plaquette product, the arbitrary-`ε` proof,
  the fixed-seed sanity check with its seed, and the Clifford commutator
  with its verified representation — and **the statement that the
  agreement is not the verdict**;
- **A4's derivation, every step**;
- **A5's four rows with per-candidate derivation lengths**, and whether
  the table is symmetric in depth;
- **A6's companion result**, with the 96 mismatches independently
  verified;
- **A7's verdict and transcribed consequence**;
- **A8's search, the finding, and how the difference is characterised**;
- **A12's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and what `RUN 1` did;
- **§7's four Rule 16 junctions**;
- **whether the derivation made you want to draw an admissibility
  conclusion.** **Say which and why, and confirm you did not**;
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

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    773dd2cb2ad8fb457e23150f0cb19ab80dd614a5, the head
                landed by the combined D-pre-A and D-pre-A2
                integration. Both microspec artifacts are present on
                main and the discriminants artifact's two dossier
                citations resolve.

    target      the staggered plaquette product
    method      compute the plaquette phase from the standard staggered
                phases on all six planes over 81 base sites, then
                recompute under a random site-sign redefinition
    MEASURED    -1 on all six planes at every site tested, and UNCHANGED
                under the redefinition.

    target      the Clifford group commutator
    method      an explicit 4x4 Euclidean gamma representation built as
                Kronecker products of Pauli matrices, verified to
                satisfy {g_mu, g_nu} = 2 delta, then the commutator on
                all six planes
    MEASURED    -1 on all six planes, a scalar multiple of the identity
                in each case.
    NOT DERIVED whether the two structures are the same. THE MATCHING
                VALUES ARE THE REASON TO ASK, NOT THE ANSWER, and §0
                forbids treating them as one.

    target      the reconstruction identity the derivation starts from
    method      read §3.3 of the dossier on main
    MEASURED    the identity Gamma(x)^dagger gamma_mu Gamma(x+mu) =
                eta_mu(x) . 1_4 is recorded there, exhibiting naive as
                four decoupled copies.

    target      the companion translation result
    method      read lines 224-235 of the discriminants artifact on main
    MEASURED    line 115 conjoins local, translation-invariant and
                axis-isotropic; staggered's translation invariance holds
                in the same up-to-redefinition sense; 96 mismatches over
                the 2^4 block, with a restoring redefinition found for
                each of the four axes. A6 requires the 96 re-measured
                rather than quoted.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path, one per line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                773dd2cb and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                the manifest lists four and 'modify: []' contributes
                none; parse OK, counted equals stated per category.
