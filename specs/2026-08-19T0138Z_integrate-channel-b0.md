# Task specification — integrate the spin-channel scope assessment, and land it

    Specification evidence base: 7ae371994a8bb940e6f6d6b9c9868c96adcfaca9

**THE EVIDENCE BASE IS NOW SUBSTITUTED AND MEASURED.**
`7ae371994a8bb940e6f6d6b9c9868c96adcfaca9` is the `EPS-B0` integration's
commit 4, landed and read back from the remote.

**An earlier draft of this specification carried a placeholder in four
places, including the scope block's `base:` field.** **The Researcher
performed the substitution and RE-MEASURED against the new base rather
than carrying the old figures.**

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-channel-b0
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/channel-b0-spin-scope
                       8c27a606643ef315d11e1a1dad8875aa2f1029b1

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**Re-measured against THIS base, `7ae37199…`:** merge **CLEAN**, source
contributes **4 additions, 0 modifications**, cumulative **6** at the
merge and **7** at the report. **The figures are unchanged from the
source's own base, but they were measured again rather than assumed.**

**THE MERGE-BASE IS `af145d5a`, NOT THIS TASK'S EVIDENCE BASE.**
**Measured: they are NOT equal.** **This is the first integration in
this line where they differ, and `A13` requires both reported
separately.**

**`A5` still requires the merge measured fresh and `A12` the scope
figures measured.** **A conflict is an immediate STOP.**

---

## 0. The verdict

    CHANNELS SEPARATED
    the universality claim is scoped to the SPIN-2 TT channel

**And it rests on reading the argument, not on a word list.** **`spin-0`
returns zero and `fifth force` returns zero, and NEITHER ABSENCE WAS
USED AS EVIDENCE.**

**The separation is stated in the manuscript's own vocabulary, in six
places:**

    :96         "both the scalar channel and the graviton (stress-tensor)
                channel"
    :574-576    the two light modes named separately in one sentence
    :810-814    the decisive test is a single p²=0 pole in the spin-2
                sector "with vanishing spin-1/0 residues", named as the
                programme's key numerical milestone
    :787-788    "the only possible massless pole resides in the TT
                spin-2 channel"
    :1531-1534  both phenomenologies attributed to their channels
    :816-833    the universality subsection scopes itself to eq:PiTT in
                its first sentence and never mentions θ̃

**The specification's word list was wrong and the specification said so
in advance.** **`§3` of `CHANNEL-B0` stated that a separation expressed
in other terms would be `CHANNELS SEPARATED` and the word list the
defect.** **The executor added `spin-1/0`, which returns one line — and
that line is the separation, stated as a test criterion.**

**Report that the verdict was reached by reading and that the added term
decided it.**

## 1. Three findings that must land uncompressed

### 1a. `θ̃`'s universality is `UNSTATED`, not `NON-UNIVERSAL`

**Suppression by `ε` and a mixing angle is a statement about MAGNITUDE,
not about whether the scalar charge varies across bodies.**

**The executor searched every form of object dependence** —
`composition-dependent`, `baryon number`, `charge-to-mass`, `Eötvös`,
`test body`, `torsion balance` — **all zero.** **The Researcher
independently re-ran those six and confirms zero for each.**

**And the near-miss that must land with it:** **`composition` returns
five lines and ALL FIVE ARE `decomposition`.** **Counting them would
have returned `NON-UNIVERSAL` on a substring** — the most consequential
false positive available in that task.

**`:634` says the coupling is to "visible (baryonic) matter", which
names a TARGET, not a charge law.**

### 1b. The equivalence principle is `DERIVED HERE`, with four limits

**For the SPIN-2 channel, at the level of the linear coupling.**

**Not merely `CLAIMED`** — `:825-831` gives premises and a *Hence*.
**Not `DERIVED ELSEWHERE`** — the only citation is Fierz, for the
action's form. **Not `TESTED`.**

**The executor recorded four explicit limits on the derivation.**
**Report them.** **`DERIVED HERE` is not the same as established**, and
a landing that carries the label without the limits misrepresents it.

### 1c. Channel separation does not establish parameter independence

**Carry this verbatim:**

> **Channel separation does not establish parameter independence.** The
> spin-0 and spin-2 observables may be conceptually distinct while the
> scalar channel's strength remains dependent on unresolved microscopic
> data through `ε`.

**`EPS-B0` has now landed and IS on this task's evidence base.** **The
`CHANNEL-B0` executor could not cite it — it was absent from that base
— and correctly did not.** **You can.** **Report the relation: the
channels are separated, and the scalar channel's strength waits on an
open node.**

## 2. What this does NOT establish

- **A `CHANNELS SEPARATED` verdict means the DOCUMENTS are clear, not
  that the separation is correct.**
- **`Z` is a kinetic coefficient.** **The TT channel's source side
  remains absent** — `SRC-B0` established that and this does not change
  it.
- **`UNSTATED` universality is not universality.** **It is silence.**
- **The manuscript's own decisive test — `:810-814`'s spin-1/0 residue
  measurement — HAS NOT BEEN PERFORMED.** **Report that the milestone is
  named and unexecuted.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file.**
- **Do not report `θ̃`'s universality as anything but `UNSTATED`.**
- **Do not report the equivalence principle as established.**
- **Do not derive any coupling, magnitude, or charge law.**
- **Do not perform, design, or scope the `:810-814` milestone test.**
- **Do not adjudicate `R1`–`R5`.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 4. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured, **verbatim and not
normalised**. Fetch, then report `refs/remotes/origin/main` **pasted
from `git rev-parse` output** and confirm it equals this specification's
declared base. **If `main` has advanced beyond it, STOP** — do not
rebase.

**Report the source tip pasted from command output** and confirm it is
`8c27a606643ef315d11e1a1dad8875aa2f1029b1`, **and that it is not an
ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0.

**A4 — Merge parentage, three separately derived measurements.**
**Commit 1 must be an ancestor of parent 1.**

**A5 — No conflict, measured fresh at THIS base.** **Report the conflict
list.** **It must be empty.** **The dry run recorded in §0's header was
against `af145d5a`, a different base; do not carry its result.**

**A6 — The six separation passages, re-read at the head.** **Quote each
verbatim with line numbers.** **Confirm the verdict rests on these and
not on the absence of `spin-0` or `fifth force`.**

**Report that `spin-1/0` returns one line and that it decided the
verdict**, and **report that the specification anticipated its own word
list being wrong.**

**A7 — §1a, with the near-miss.** **Report the six object-dependence
terms and their counts** — expected zero for each. **Report that
`composition` returns five lines and all five are `decomposition`.**
**Confirm the verdict is `UNSTATED` and not `NON-UNIVERSAL`.**

**A8 — §1b, with the four limits.** **Report the equivalence principle's
status as one of `CLAIMED` / `DERIVED HERE` / `DERIVED ELSEWHERE AND
CITED` / `TESTED`**, and **report all four limits the source recorded.**
**Quote `:825-831`.**

**A9 — §1c, carried verbatim**, and **the `EPS-B0` relation now that it
is on the base.** **Confirm `EPS-B0` is an ancestor of your base** — it
is, if the substitution was performed correctly — **and report its
verdict as landed evidence rather than as a constraint.**

**A10 — The unexecuted milestone.** **Report that `:810-814` names a
decisive test and that no artifact in the repository performs it.**
**Search and report.** **Do not scope it.**

**A11 — Nothing derived.** **Search the artifact, the report and the
commit messages for any statement about what a channel should couple to,
any computed magnitude, and any claim that the equivalence principle
holds.** **Report the search and the result.**

**A12 — Scope, frozen manifest. Measure, do not carry.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 7ae371994a8bb940e6f6d6b9c9868c96adcfaca9
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-CHANNEL-B0_spin-channel-scope.md
      reports/2026-08-18T2219Z_channel-b0-spin-scope.md
      reports/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
      reviews/chatgpt/2026-08-18T2219Z_channel-b0-spin-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
      specs/2026-08-18T2219Z_channel-b0-spin-scope.md
      specs/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Report the cumulative figure at each commit AND the
source's contribution, separately labelled.** **Expected contribution 4 and
cumulative 1, 2, 6, 7 — MEASURED BY THE RESEARCHER AGAINST THIS BASE.**
**Measure them again anyway**, and report what you measure.

**If the measured figures differ from the stated manifest, STOP and
report.** **Do not adjust the manifest.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **Measure the UTC time and use
the value you measured.**

**A13 — Which merge case.** **Report whether the merge-base equals this
task's evidence base**, and whether any commit between the source's own
base and yours touched an arriving path. **Then** the four blob
comparisons.

**This differs from the previous integrations**: the source branched
from `af145d5a`, and your base is later. **The merge-base will be
`af145d5a`, NOT your base.** **Report both and do not conflate them.**

**A14 — Nothing existing changed.** Every path at your evidence base
blob-identical at the head, **`paper/emergent_gr_paper_v2_15.tex` in
particular — report its blob id at both ends.** **Report the count
compared**, and confirm for `GATES.md`, `CONVENTIONS.md`, **every
`derivations/P2-*` artifact — re-measure the count**, the `EPS-B0`
artifact, the two `scripts/recon2026/` files and
`tests/test_recon2026_flat_limit.py`, both registers, and everything
under `results/`.

**A15 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — The checker over this task's own range**, base as declared, head
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

**A17-final, post-report evidence:** re-run RUN 2 at commit 4.

**A18 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.**

**A19 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
    commit 3  --no-ff merge of 8c27a606…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-channel-b0.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A16, A18 and A19 for
commits 1–3; **A17's two runs with both configs verbatim**; commit SHAs
pasted from `git rev-parse`; commit 4's intended message; **A12's final
scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A17-final; A15 and A16 re-run after the advance; A19
for commit 4; the push; remote `main` read back; final ancestry.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**. **The advance is a fast-forward from
this specification's declared base.** **Verify `--is-ancestor` before
the push and report the exit status as a measurement.** **If a
fast-forward is not available, STOP.** **Push without `--force` and
without `--force-with-lease`.** **Push only `refs/heads/main` and this
task's branch.** **The source branch is not deleted and does not move.**

## 7. Rule 16 assessment

**Rule 16 is operative.** **Five junctions, all five required.**

**First.** **`CHANNELS SEPARATED` is a finding about the documents.**
**It does not establish that the separation is physically correct, and
it does not establish that either channel behaves as claimed.**

**Second, and it is the one a reader will compress.** **`UNSTATED` is
not `UNIVERSAL`.** **The manuscript does not say `θ̃` couples
universally; it does not say it couples non-universally either.** **Say
that the silence is the finding**, and **say that a substring search on
`composition` would have produced the opposite answer from five
instances of `decomposition`.**

**Third.** **`DERIVED HERE` carries four recorded limits and applies to
the spin-2 channel at linear order.** **It is not a demonstration that
the equivalence principle holds in this theory.** **Say so, and list the
limits.**

**Fourth.** **The manuscript names its own decisive test at `:810-814`
and no artifact performs it.** **Say that the programme's key numerical
milestone, by its own designation, is unexecuted.**

**Fifth.** **Channel separation does not establish parameter
independence**, per §1c. **`EPS-B0` is now on the base and establishes
that `ε` is blocked pending an open node** — **so the scalar channel is
conceptually distinct and parametrically dependent at the same time.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
- **Modify nothing. Derive nothing. Merge only the named source.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration. **The landing is a fast-forward
  or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**, and **every SHA pasted from command
  output**;
- **A1's verbatim `origin` URL and both pasted SHAs**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A5's fresh conflict measurement, with a note that §0's figures came
  from a different base**;
- **A6's six quoted passages and the `spin-1/0` finding**;
- **A7's six zero-counts and the `decomposition` near-miss**;
- **A8's four-state status and the four limits**;
- **A9's verbatim statement and the `EPS-B0` ancestry confirmation**;
- **A10's milestone search**;
- **A11's search and result**;
- **A12's measured figures, with a STOP if they differ from the
  manifest**;
- **A13's merge-base and evidence-base reported SEPARATELY**;
- **A14's path count, the manuscript blob id at both ends, and the
  `P2-*` count re-measured**;
- **A15's four invariants**;
- **A16's six exit statuses, before and after**;
- **A17's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A18's counts**;
- **the landing**;
- **§7's five Rule 16 junctions**;
- **whether landing a favourable verdict made you scrutinise it less.**
  **The source executor raised this about its own work and answered it
  by producing six independent passages instead of two.** **Say what you
  did**;
- a **Stops and clarifications** section using the five primary
  categories, included even if there were none.

## 10. Pre-issue literal verification record

    target      the source branch and its merge from ITS OWN base
    method      git rev-parse; dry run from af145d5a with two
                placeholder commits, then git merge --no-ff
    MEASURED    science/channel-b0-spin-scope =
                8c27a606643ef315d11e1a1dad8875aa2f1029b1. From af145d5a
                the merge is CLEAN, contributing 4 additions and 0
                modifications, cumulative 6 at the merge and 7 with a
                placeholder report.
    LIMIT       THIS TASK'S BASE IS LATER. Those figures were measured
                against af145d5a and A5 and A12 require them measured
                again. The merge-base will remain af145d5a while the
                evidence base is the EPS-B0 landing head; A13 requires
                both reported separately.

    target      this specification's own base, after substitution
    method      git rev-parse origin/main; dry run from 7ae37199 with
                two placeholder commits, then git merge --no-ff
    MEASURED    origin/main = 7ae371994a8bb940e6f6d6b9c9868c96adcfaca9,
                the EPS-B0 integration's commit 4. Merge CLEAN.
                MERGE-BASE = af145d5a, which is NOT the evidence base —
                measured unequal. Source contributes 4 additions, 0
                modifications; cumulative 6 at the merge, 7 with a
                placeholder report. Unchanged from the source's own
                base, but re-measured rather than carried.
                derivations/P2-* = 50 at this base, up from 49.
    NOTE        an earlier draft carried a placeholder because the
                EPS-B0 integration had not landed. Writing "origin/main"
                instead would have made the base whatever main happened
                to be, which is not a frozen base.

    target      the six object-dependence terms
    method      count lines in paper/emergent_gr_paper_v2_15.tex
    MEASURED    composition-dependent 0, charge-to-mass 0, Eotvos 0,
                torsion balance 0, test body 0, baryon number 0. The
                Researcher confirms the source executor's zero-check
                independently. A7 requires it re-run.

    target      the separation passages
    method      read paper lines 787-788 and 810-814
    MEASURED    :787-788 "so that the only possible massless pole
                resides in the TT spin-2 channel." :810-814 "A lattice
                measurement of the Barnes--Rivers--projected
                stress-tensor correlator, checking for a single p^2 = 0
                pole in the spin-2 sector with vanishing spin-1/0
                residues, is the decisive test; we identify it as the
                key numerical milestone for this programme." Both
                confirmed. A6 requires all six re-read.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. The base field
                contains the fully substituted evidence-base SHA
                7ae371994a8bb940e6f6d6b9c9868c96adcfaca9.
    MEASURED    placeholder token count = 0, measured with an
                externally supplied pattern. The token is NOT
                reproduced here: a record that writes the string in
                order to report its absence makes its own count wrong,
                which is the self-referential search hazard this line
                has hit four times.
    RETRACTED   an earlier draft of this record said "the base field
                holds a placeholder by design". That was true of the
                pre-substitution draft and false of this one. The
                substitution updated four occurrences and did not update
                the sentence describing them — the same
                structural-propagation failure this line has recorded
                repeatedly.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
