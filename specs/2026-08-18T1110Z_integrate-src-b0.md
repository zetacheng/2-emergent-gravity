# Task specification — integrate the source-side scope assessment, and land it

Specification evidence base: `0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-src-b0
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/src-b0-source-side-scope
                       cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`0a7a988c…`.

    source contributes          4 additions, 0 modifications
    this task authors           3 — spec, review, report
    cumulative at merge (3)     6 additions
    cumulative at final (4)     7 additions

**`6` is CUMULATIVE, not the merge's contribution.** **Any conflict is
an immediate STOP.** **Nothing is modified.**

---

## 0. The source branch tip, and a reporting defect that has now happened twice

**THE SOURCE TIP IS `cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56`.**

**The `SRC-B0` execution report gave `8f5e3c4c…`, which is not
resolvable in this repository.** **The `DET-01` integration report gave
`55c2e4a4…` for a landing whose authoritative head is `0a7a988c…`, also
not resolvable.**

**Two consecutive tasks reported a final commit id that does not
exist.** **In both cases the work itself was sound**: commit messages,
structure, scope and content all matched, and the discrepancy was only
in the reported identifier.

**Resolve every SHA in your report with `git rev-parse` at the moment of
reporting.** **Do not transcribe an id from earlier in your own session,
and do not carry one from a prior report.** **`A4` and `A9` both require
this.**

**Report the two prior discrepancies as a finding.** **Do not repair
either report** — both are pushed, and Rule 20 permits only a message
repair with the tree unchanged.

## 1. What lands

**Verdict: `NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`.** **The
source-side calculation cannot presently be executed from repository
materials.**

**And a second finding that was not in the specification's expectations
and is the more consequential of the two.**

### 1a. The `DET-01` rider does NOT survive a metric variation

**`DET-01` established that the measure ambiguity `Σₓ F(g(x))` is
ultralocal and mass-independent, and therefore does not touch `β_V`.**

**`T_μν = (2/√g) δΓ/δg^{μν}` is a VARIATION with respect to `g`.**
**Differentiating an ultralocal functional does not give zero** — it
gives an ultralocal SOURCE contribution.

**So the ambiguity that is harmless for the Einstein–Hilbert coefficient
REACHES the stress tensor.** **`d = 4` does not help**: it is what makes
`det[√g g⁻¹] = det g`, and that identity is about the determinant's
form, not about the variation vanishing.

**Report this as a landed finding — AND REPORT THAT IT IS
CONDITIONAL.**

**The measure prerequisite attaches to a `Γ`-DEFINED stress tensor.**
**The same execution located a CLASSICAL-ACTION definition in the
manuscript, `T_μν^{(S)} ~ δS/δg^{μν}`, WHICH DOES NOT INHERIT IT.**

**So the correct statement is ONE UNCONDITIONAL prerequisite and ONE
CONDITIONAL one:**

    UNCONDITIONAL   a usable source configuration
    CONDITIONAL     IF the source observable is defined through the full
                    quantum effective action Γ, then the functional
                    measure or an admissible source-side subtraction
                    prescription. A classical-action-defined stress
                    tensor does not inherit this.

**Which source definition the programme requires REMAINS UNRESOLVED**
until the source construction is specified. **Do not settle it here.**

**An earlier draft of this section wrote two unconditional
prerequisites**, which is stronger than the source established and would
have landed a conditional result as an unconditional one.

**On the subtraction, state the repository's actual state and not its
absence:**

> **No repository prescription AUTHORIZES the required SOURCE-side
> subtraction. The existing frozen subtraction is scoped to RESPONSE
> observables and is explicitly scoped away from cosmological source
> energy, and whether it commutes with metric variation remains open.**

**"Exists but is not authorized for this use" and "does not exist" are
different programme states**, and an earlier draft wrote the second.

### 1b. Absence of a usable configuration, distinguished from absence of hits

**Measured by the Researcher over the whole tree: `sparc` 3 files,
`halo` 3, `yukawa` 7, `domain wall` 2, `profile` 6, `r_c` 53, `soliton`
0, `rotation curve` 0.**

**None is a usable configuration.** The `sparc` and `halo` hits are in
`paper/emergent_gr_paper_v2_15.tex` and
`results/recovered-2026/`; the `yukawa` hits are `D-1`'s chiral Yukawa
literature and unrelated; `domain wall` is `D-1c` ledger prose.

**The source executor reported AVAILABILITY, not literal counts, and was
right to.** **The `SRC-B0` specification asked for eight term counts and
did not require the distinction** — **the executor drew it anyway, and
that is the Researcher's specification gap.**

**Report both: the literal counts AND the availability finding**, and
**say which is the verdict.**

**Do NOT infer from these hits whether any external profile is derived
or fitted.** **`NOT PRESENT` and `FITTED` are different findings and the
second cannot be reached from here.**

## 2. What this does NOT establish

- **`NOT PRESENT` does not mean the physics is wrong.** **It means the
  calculation cannot be posed from what is in this repository.**
- **Nothing here characterises Paper 1's profile.** **Whether it is
  derived from field equations or fitted to rotation curves is
  undetermined and was deliberately not pursued.**
- **A homogeneous Lorentz-invariant vacuum contributes a
  cosmological-constant-type stress tensor.** **It does not provide the
  localized clustering source the proposed test needs** — **and that is
  NOT the same as having no gravitational effect**, which would be
  false.
- **The proposed calculation probes the condensate's INHOMOGENEOUS
  sector.** **A null result there would say nothing about the vacuum
  sector, which `DET-01` left unfixed.**
- **No tolerance, quantity or direction was chosen for a failure
  criterion**, and **this task does not choose them either.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file.**
- **Do not import, reconstruct or characterise Paper 1's profile.**
- **Do not choose a tolerance or failure criterion.**
- **Do not settle the measure, define a background subtraction, or
  compute any `T_μν`.**
- **Do not repair either prior SHA report.**
- **Do not touch `R1`–`R5`, `RECON-01b`, or the `r = 1` conflict.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 4. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` and confirm it is
`0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`. **Report `refs/heads/main`
for contrast.**

**Report the source tip AS RESOLVED BY `git rev-parse` at the moment of
reporting** and confirm it is
`cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56`, **and that it is not an
ancestor of `main`.** **Report that the source's own report gave a
different id** — §0.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 the source tip **as re-resolved**,
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — §1a re-derived, not transcribed.** **Confirm that `δ/δg^{μν}` of
an ultralocal `Σₓ F(g(x))` does not vanish**, and **that it therefore
contributes to `T_μν`.** **State the derivation.**

**Report separately that `d = 4` does not rescue it**, and **why**:
`d = 4` is what makes `det[√g g⁻¹] = det g` — **measured generally as
`(det g)^{d/2−1}`, equal to `det g` only at `d = 4` and equal to `1` at
`d = 2`** — **and that identity concerns the determinant's form, not the
vanishing of its variation.**

**This is the finding that changed what the proposed calculation would
require.** **A landing that carried `NOT PRESENT` without it would leave
the programme unaware that a `Γ`-defined source observable carries a
second, CONDITIONAL prerequisite** — **and a landing that stated it
unconditionally would overstate it.** **Report the condition, per §1a.**

**A7 — §1b's two-level report.** **Report the eight literal term counts
over the whole tree**, **where the non-zero hits live**, and **the
availability verdict.** **State which is the verdict and confirm the
literal counts are not it.**

**Confirm no inference was drawn about any external profile's
provenance.**

**A8 — The prerequisites, enumerated AND CORRECTLY QUANTIFIED.**

**Report ONE UNCONDITIONAL prerequisite and ONE CONDITIONAL one**, per
§1a. **Report the condition explicitly: the measure prerequisite
attaches to a `Γ`-defined `T_μν` and NOT to a classical-action-defined
one.** **Report that which definition the programme requires is
unresolved.**

**On subtraction, report the repository's ACTUAL state**: whether a
prescription exists, what its frozen scope is, whether that scope
authorizes source-side use, whether it is scoped away from cosmological
source energy, and whether commutation with metric variation is settled.

**Do NOT report that no prescription exists.** **Verify each of those
five points against the repository and report what you measure.**

**A9 — Scope, frozen manifest. Cumulative final: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-SRC-B0_source-side-scope.md
      reports/2026-08-18T0507Z_src-b0-source-side-scope.md
      reports/2026-08-XXT{HHMM}Z_integrate-src-b0.md
      reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-b0.md
      specs/2026-08-18T0507Z_src-b0-source-side-scope.md
      specs/2026-08-XXT{HHMM}Z_integrate-src-b0.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately** — they coincide, at four.

**Report the cumulative figure at each commit AND the source's own
contribution, separately labelled.** **Expected cumulative 1, 2, 6, 7;
source contribution 4.**

**Every commit SHA in the report resolved by `git rev-parse` at
reporting time** — §0.

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **Measure the UTC time and use
the value you measured.**

**A10 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A11 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, **every
`derivations/P2-BETAV-*` artifact — re-measure the count and report what
you measure**, all seven microspec artifacts, the two
`scripts/recon2026/` files and `tests/test_recon2026_flat_limit.py`,
both registers, `paper/`, and everything under `results/`.

**The `P2-BETAV-*` count was seven at the previous base and the `DET-01`
landing added one.** **Re-measure; do not carry a number.**

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.** **Also report:**
`P2-BETAV-RECON-01` `PROPOSED`, `P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01`
`PROPOSED (deferred)`, and **`Regression anchors` still `None yet
(proposed)`.**

**A13 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A14 — The checker over this task's own range**, base `0a7a988c…`, head
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

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A15 — Validators, exit status 0.** **Expected 332 passed, 2
deselected** — the arriving task adds no code.

**A16 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-src-b0.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-b0.md
    commit 3  --no-ff merge of cb07f3a9…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-src-b0.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A13, A15 and A16 for
commits 1–3; **A14's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A9's final scope
stated as INTENDED, with the measured cumulative 6 at commit 3.**

**Post-report evidence, NOT written back:** A9's final scope measured
base-to-commit-4; A14-final; A12 and A13 re-run after the advance; A16
for commit 4; the push; remote `main` read back; **final ancestry
confirmation, with every SHA re-resolved at reporting time.**

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `0a7a988c…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch.** **The source branch is not
deleted and does not move**; verify and report its tip **as re-resolved,
not as previously reported.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **`NOT PRESENT` is a finding about this repository and
nothing else.** **It does not bear on whether the physics works, and it
does not characterise Paper 1's profile.** **Say both.**

**Second, and it is the landing's real content.** **The measure
ambiguity that `DET-01` showed harmless for `β_V` REACHES a `Γ`-DEFINED
`T_μν`.**

**Say that this gives ONE unconditional prerequisite — a configuration —
and ONE CONDITIONAL prerequisite that attaches only if the source
observable is defined through `Γ`.** **A classical-action-defined stress
tensor does not inherit it**, and **which definition the programme
requires is unresolved.**

**Say that the conditional prerequisite was discovered by asking a
question the previous task's rider did not cover**, and **say that
reporting it as unconditional would overstate what was established.**

**And say that the existing subtraction rule EXISTS but is scoped to
response observables, scoped away from cosmological source energy, and
of unsettled commutation with metric variation** — **not that none
exists.**

**Third.** **A homogeneous vacuum gravitates; it does not cluster.**
**The proposed test probes the inhomogeneous sector only**, and **a null
result there says nothing about the vacuum sector.** **Say both, and do
not let "no localized source" be read as "no gravitational effect".**

**Fourth.** **No failure criterion has been fixed.** **Until the
compared quantity, the tolerance and the direction are pre-registered,
the proposed calculation is not a test** — **a factor-of-three
disagreement would be adjudicated after the number is seen.** **Say
that.**

**Fifth.** **Two consecutive execution reports gave unresolvable commit
ids.** **Neither affected the work, and both were caught by
integration.** **Say that the repository's evidence chain depends on
reported identifiers being re-resolved rather than transcribed**, and
**say that nothing in the repository checks a reported SHA against the
ref it names.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.**
- **Do not characterise Paper 1's profile, choose a tolerance, define a
  subtraction, or compute a `T_μν`.**
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

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**, and **every SHA re-resolved at
  reporting time**;
- **A1's verbatim `origin` URL, the re-resolved source tip, and the
  discrepancy with the source's own report**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's derivation, and the `d = 4` explanation with the general
  `(det g)^{d/2−1}` relation**;
- **A7's eight literal counts, where the hits live, and the availability
  verdict stated as the verdict**;
- **A8's ONE unconditional and ONE conditional prerequisite, with the
  condition stated**, and **the subtraction rule's actual state across
  all five points — existence, frozen scope, source-side authorization,
  cosmological-source-energy scoping, and commutation**;
- **A9's cumulative figures and the source's contribution, separately
  labelled**;
- **A10's merge case, stated BEFORE the blob comparisons**;
- **A11's path count with the `P2-BETAV-*` count re-measured**;
- **A12's four invariants, the three `BETAV` statuses, and the
  `Regression anchors` value**;
- **A13's six exit statuses, before and after**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A15's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§7's five Rule 16 junctions**;
- **whether landing a `NOT PRESENT` verdict made you want to
  characterise the external profile, choose a tolerance, or define a
  subtraction.** **Say which and why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from 0a7a988c with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d;
                source tip = cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56,
                NOT an ancestor of main. Merge CLEAN; merge-base =
                0a7a988c. SOURCE CONTRIBUTES 4 additions, 0
                modifications. CUMULATIVE: 6 at the merge commit, 7 with
                a placeholder report. The landing fast-forward is
                available.

    target      the two reported-SHA discrepancies
    method      git cat-file -t on each reported id
    MEASURED    8f5e3c4c NOT RESOLVABLE; the SRC-B0 branch tip is
                cb07f3a9. 55c2e4a4 NOT RESOLVABLE; the DET-01 landing
                head is 0a7a988c. Both branches' commit messages,
                structure and scope match their reports exactly. The
                defect is in the reported identifiers only.

    target      the configuration search
    method      git grep -cil over the whole tree at the evidence base
    MEASURED    sparc 3, halo 3, yukawa 7, domain wall 2, profile 6,
                r_c 53, soliton 0, rotation curve 0. The sparc and halo
                hits are in paper/emergent_gr_paper_v2_15.tex and
                results/recovered-2026/; yukawa is D-1's chiral Yukawa
                literature; domain wall is D-1c ledger prose. NONE is a
                usable configuration.
    NOTE        the SRC-B0 specification asked for term counts and did
                not require the literal/available distinction. The
                executor drew it anyway. A7 now requires both.

    target      the dimensional relation
    method      form √(det g)·g⁻¹ for random symmetric positive-definite
                g in d = 2, 3, 4, 5
    MEASURED    det[√g g⁻¹] = (det g)^{d/2−1} in every case; equal to
                det g ONLY at d = 4; equal to 1 at d = 2.

    target      whether δ/δg of an ultralocal term vanishes
    method      NOT DERIVED by this author. The source's finding that it
                does not, and that the rider therefore fails for T_μν,
                is A6's subject and must be re-derived there.

    target      the P2-BETAV-* count
    method      git ls-tree over derivations/ at the evidence base
    MEASURED    EIGHT. A11 requires it re-measured, not carried.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
