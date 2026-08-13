# Task specification — C1: is the complement root recovered or constructed?

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   science/c1-complement-root-provenance
    Cut from           authoritative main @ 1cb5550f…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task reads. It modifies nothing that already exists**, runs no
script, and produces no new numerical result. **Its entire output is one
findings artifact, and the answer to one question.**

**It touches no pinned artifact**, so it requires no re-pin — the first
task in this line for which that is true.

**It is independent of the adoption line.** `science/adopt-parameter-domain-labels`
and its predecessors are not referenced, not merged, and not required.
**Nothing here waits on them.**

> ## PRE-REGISTRATION IS COMPROMISED, AND THIS SECTION SAYS HOW
>
> **This task was designed so that nobody who fixed the consequences knew
> the answer.** **That property no longer holds.** The Reviewer read the
> script during review and named a verdict — `RECOVERED` — with
> supporting line-level claims. **The review is committed as commit 2 and
> the executor will read it before writing commit 3.**
>
> **This is not a fault of the review.** Checking a specification's
> premises against the repository is what the Reviewer should do, and it
> has already caught a real defect here. **But it changes what this task
> can establish.**
>
> **So the task is restructured rather than pretended intact.** §2's
> verdicts and consequences remain fixed. **§2a now records the
> Reviewer's stated claims as falsifiable predictions**, and the
> executor's job is to verify each one against the code rather than to
> form an unanchored judgement. **A verification that names its
> anchor is worth more than a judgement that hides one.**
>
> **The executor must report whether their reading was reached
> independently, agreed after anchoring, or cannot be separated from the
> review's.** **All three are acceptable answers. Silence is not.**

---

## 0. The question, and why it is worth a task

**`derivations/P2-PHASE-01_microscopic_parameter_domain.md`, in the
adoption line, records this as `C1` and defers it.** The adopted text
says of the complement root:

    The reported complement-root position satisfies
    Mhat_comp = −8 − Mhat_ord exactly in the stored results. Whether
    that is an independently recovered root or a constructed companion
    is NOT established here and is deferred to C1.

**The measurement that raises it.** Across all six grids and all sixteen
couplings, ninety pairs of non-trivial roots satisfy
`|Mhat_ord + Mhat_comp + 8| = 0.00e+00`. **Exactly zero, ninety times.**

**A residual of exactly zero is a property of a method, not of physics.**
Three things produce it, and they carry different evidential weight:

    RECOVERED    a search found both roots independently, and they
                 agree to the last bit because the underlying relation
                 I0(Mhat) = I0(-8-Mhat) is exact in the frozen integral
    CONSTRUCTED  the second root was computed as -8 minus the first and
                 never independently sought
    GRID-INDUCED both were found by search, but over a mass grid
                 symmetric about Mhat = -4, so mirrored grid points
                 coincide exactly by construction of the grid

**The consequence differs, and it is pre-registered in §2 so that it
cannot be chosen after the answer is known.**

**This matters to a PI ruling already recorded.** The negative-mass
branch is admitted as a candidate in the SI-1 enumeration. **If its
position carries no independent numerical evidence, the branch's entire
positional content is a restatement of the ordinary branch**, and what
remains distinctive is the curvature asymmetry alone.

## 1. What is read

    scripts/p2_phase01_scalar_exploratory.py
    sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
    blob    b44bc63d115f4e88a706d046e60488c51d8a06a0
    462 lines

**That digest is recorded in the results file's own `script_sha256`
field and matches the file byte for byte.** **Verify that before reading;
if it does not match, STOP** — the study's outputs would not be
attributable to this script.

**The regions that bear on the question**, named so the reading is
scoped rather than open-ended:

    line 138  bisect_root
    line 162  algebraic_roots
    line 172  root_record
    line 190  grid_result
    line 294  symmetry_check

**Read whatever else is needed to answer honestly.** The list is a
starting point, not a boundary; **if the answer turns on a line outside
it, say which.**

**Also read**, in the results file at the same revision, the
`symmetry` object's `complement_pairs` and `wilson_complement_relation`
fields, and **say whether either is computed from the relation rather
than measured against it.**

## 2. The pre-registered verdicts and their consequences

**Fixed before reading. The consequences are not renegotiated
afterwards.**

**Two independent classifications, and the executor selects one from
each:**

    ROOT PROVENANCE       how the production root table's values were
                          obtained
                          RECOVERED / CONSTRUCTED / INCONCLUSIVE

    EXACTNESS PROVENANCE  why |sum + 8| is exactly zero
                          SEARCH-STRUCTURE-INDUCED /
                          NOT-STRUCTURE-INDUCED / INCONCLUSIVE

**`NOT-STRUCTURE-INDUCED` has no pre-registered consequence**, because
the author cannot state one without knowing what the mechanism turns out
to be. **Selecting it is therefore a STOP under A4**, and that is
deliberate: **a verdict with no consequence attached is a verdict whose
meaning would be written after the fact.**

**`RECOVERED`** — both roots are located by separate bracketed searches
that do not use the complement relation, and no discrete mass-search grid
forces their positions.

**Consequence:** the complement root is **independently recovered
numerically, rather than constructed** from the ordinary root. This
discharges the adopted artifact's caution about numerical provenance.
**It does NOT make the complement position algebraically independent:**
under the exact Wilson-complement identity, its position remains
determined by `Mhat_comp = -8 - Mhat_ord`. The independent recovery
therefore **validates the solver and the realised symmetry, but does not
by itself add independent positional physics.** The branch's potentially
distinctive content remains in quantities not fixed by that positional
identity, including the curvature asymmetry, whose interpretation remains
deferred to `C3`.

**`RECOVERED` and "carries independent positional information" are
different claims, and an earlier version of this specification conflated
them.** **Recovering a value independently says something about the
solver. It says nothing about whether the value was free to be
otherwise.**

**`CONSTRUCTED`** — the second root is computed from the first.
**Consequence:** the complement root's position is not numerical evidence
at all. `results/.../scalar_stationary.json`'s ninety zero residuals are
ninety restatements of one identity. **The adopted artifact's §5a
becomes an understatement**, and the negative-mass branch's remaining
distinctive content is the curvature asymmetry alone — which `C3` has
not yet shown to be physical.

**`SEARCH-STRUCTURE-INDUCED`** — both are searched for, but the SEARCH
STRUCTURE forces the exactness: a discrete mass grid symmetric about
`Mhat = -4`, **or a pair of brackets that are mirror images under
`m -> -8-m`**, or any other arrangement in which the two searches are
reflections of one another rather than independent.

**Consequence:** the roots are independent as searches but **the
exactness is not evidence of anything.** `max |sum + 8| = 0.00e+00`
must not be quoted as numerical agreement, because a reflected search of
a function with an exact reflection symmetry cannot produce anything
else.

**This verdict was narrowed to discrete grids in an earlier version.**
**That was too narrow**: the mechanism is reflection in the search
structure, and a bracket pair is a search structure.

**`INCONCLUSIVE`** — the code does not settle it. **Consequence:** say
what would. **Name the specific computation** — for example a re-run over
a deliberately asymmetric mass grid — **and do not perform it.** That is
a separate task with its own pre-registration.

**Report the verdict, the lines that establish it, and the consequence
as written above.** **If you find yourself wanting a consequence other
than the one attached to your verdict, that is a finding about this
specification: report it, and do not substitute.**

## 2a. The Reviewer's stated claims, as predictions to verify

**Each was stated in the pre-execution review after reading the script at
the pinned digest. Each is falsifiable against named lines.** **Verify
every one and report PER CLAIM: CONFIRMED, REFUTED, or CANNOT DETERMINE.**

    R1  algebraic_roots() calls bisect_root() separately on the two
        brackets (-12,-4) and (-4,4)
    R2  bisect_root() uses only divided_gap(); no root is computed as
        -8 - mhat
    R3  grid_result() writes each root returned by algebraic_roots()
        straight into the results, without post-processing the pair
    R4  symmetry_check() DOES construct complement = -8.0 - mhat, and
        compares bubble(mhat) against bubble(-8-mhat) — so the
        complement_pairs field is a constructed diagnostic, while the
        production root table is not
    R5  therefore the code-provenance verdict is RECOVERED

**The specification author independently read lines 134–170 and confirms
R1 and R2 there.** **R3, R4 and R5 are not confirmed by the author and
are for the executor.**

### The fact that none of the claims explains

**`R5` being true does not account for the observation that motivated
this task.** Ninety pairs have `|sum + 8| = 0.00e+00` — **exactly zero,
in floating point, ninety times.**

**The author simulated the described structure and did not reproduce
it.** Bisecting a toy function with the same exact reflection symmetry
about `Mhat = -4`, over the same two brackets, for the same 17
iterations, gave a residual of `-6.103515625e-05` — **one bisection step,
not zero.** The reason it need not be zero: `m -> -8-m` maps the first
bracket onto the second **reversed**, and the tie-break in the bisection
is written in terms of `left` and `right`, which reflection exchanges.

**On the real data the mirroring is nonetheless exact to the last bit** —
verified in hex: `-0x1.e5cd800000000p+2` and `-0x1.a328000000000p-2` sum
to exactly `-8.0`, and `-8.0 - first == second` returns `True`.

**So a fact remains unexplained, and answering `C1` means explaining it.**
**Add to the findings artifact a section stating WHY the residual is
exactly zero**, or **stating that the code does not determine it.**

**Do not compute anything new to answer this.** **Read, or say you
cannot.** If the answer requires running a variant of the solver, that is
`INCONCLUSIVE` and a separate task.

**If the mechanism turns out to be reflection in the search structure,
the verdict is `SEARCH-STRUCTURE-INDUCED` on the exactness even though it
is `RECOVERED` on the provenance.** **Those are two questions and the
findings artifact answers both separately.**

## 3. What this task must not do

- **Do not modify any existing file.** Not the script, not the results,
  not the adopted artifact, not `GATES.md`.
- **Do not run the script**, and do not run anything that writes under
  `results/`.
- **Do not compute a new numerical result of any kind.** **Quoting a
  number already in the results file is reading; producing one is not.**
- **Do not answer `C2` or `C3`.** If the reading bears on either, **say
  so in one sentence and stop there.**
- **Do not change any gate, gate status, prerequisite state or verdict.**
- **Do not touch `main`**, do not merge.
- **Do not soften or strengthen the adopted artifact's §5a.** That text
  is on a branch, not on `main`, and amending it is a later task with
  the verdict in hand.
- **Do not write a superseded-register entry.**

## 4. The findings artifact

Create `derivations/P2-PHASE-01_C1_complement_root_provenance.md`
containing, in this order:

1. **the question**, in one paragraph, and the pinned script digest;
2. **TWO verdicts, each in the first line of its own section**, so a
   reader meets them before any reasoning:
   **(a) ROOT PROVENANCE** — `RECOVERED`, `CONSTRUCTED` or
   `INCONCLUSIVE`, for how the production root table's values were
   obtained;
   **(b) EXACTNESS PROVENANCE** — why `|sum + 8|` is exactly zero, or a
   statement that the code does not determine it.
   **Separating them prevents the reading that a `RECOVERED` root table
   makes its exact mirroring meaningful.**
   **Also state, separately, that `symmetry_check()`'s
   `complement_pairs` is CONSTRUCTED FOR CHECKING**, so that a later
   reader meeting `complement = -8.0 - mhat` in the script does not
   conclude the root table was built the same way;
3. **the evidence** — the specific lines, quoted minimally and
   attributed by line number, that establish it;
4. **the consequence**, transcribed from §2 for the selected verdict,
   **not paraphrased**;
5. **what this does not establish**, per §6;
6. **whether the reading bore on `C2` or `C3`**, in at most one sentence
   each, with no conclusion drawn.

**No recommendation, no proposal for the next task, no physics beyond
the question asked.** **This artifact answers `C1` and stops.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_c1-complement-provenance.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_c1-complement-provenance.md
    commit 3  derivations/P2-PHASE-01_C1_complement_root_provenance.md
    commit 4  reports/2026-08-XXT{HHMM}Z_c1-complement-provenance.md

    stated: 4 additions, 0 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-PHASE-01_C1_complement_root_provenance.md
      reports/2026-08-XXT{HHMM}Z_c1-complement-provenance.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_c1-complement-provenance.md
      specs/2026-08-XXT{HHMM}Z_c1-complement-provenance.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Four commits, not five** —
there is no separate content commit because commit 3 is the content.

**Committed report — measured at commit 3:** A1–A7 and A9; **A8's two
checker runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **the final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-4; A8-final at commit 4; A9 for commit 4; validators at
commit 4; the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** Whatever the
verdict, **this task establishes something about the SCRIPT, not about
the physics.** A `CONSTRUCTED` verdict does not show the complement root
is unphysical; **it shows that the stored numbers are not evidence for
it.** A `RECOVERED` verdict does not show the branch is a phase; **the
full-space Hessian and the admissibility assessment remain absent, and
`OPEN-AC-3` still blocks the depth comparison.**

**Say plainly that C1 changes the weight of existing evidence and adds
none.**

## 7. Acceptance criteria

**A1 — Refs and the script.** `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.
`scripts/p2_phase01_scalar_exploratory.py` measures
`3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0`, and
that value equals the `script_sha256` field in
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`.
**Any mismatch → STOP.** Report all three.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18. **It must carry `reviewed specification SHA-256:` filled in.** **If
blank or naming a different digest, STOP and say which.** Report the
supplied file's digest and the committed blob's digest and show them
equal.

**A3 — The TWO verdicts**, each stated in the first line of its own
findings section:

    ROOT PROVENANCE       RECOVERED, CONSTRUCTED, or INCONCLUSIVE
    EXACTNESS PROVENANCE  SEARCH-STRUCTURE-INDUCED, NOT-STRUCTURE-INDUCED,
                          or INCONCLUSIVE

**Report both separately, with the line numbers establishing each.**

**`RECOVERED` for root provenance does not determine exactness
provenance.** They are answers to different questions and the
combination `RECOVERED` + `SEARCH-STRUCTURE-INDUCED` is coherent — **it
is the combination this specification's author considers most likely, and
saying so here is a prediction, not an instruction.**

**An earlier version of this criterion asked for "the verdict, one of the
four", which contradicted §4's requirement of two.** **That was a
structural defect**: §4 was rewritten and A3 was not.

**A4 — Consequences remain pre-registered, both of them.**

**For ROOT PROVENANCE**: transcribe the §2 consequence corresponding to
the verdict, **without paraphrase.**

**For EXACTNESS PROVENANCE**: if `SEARCH-STRUCTURE-INDUCED`, transcribe
that consequence without paraphrase; if `INCONCLUSIVE`, transcribe the
`INCONCLUSIVE` consequence.

**If the static reading establishes a mechanism that none of the
pre-registered consequences represents — including
`NOT-STRUCTURE-INDUCED` — STOP and report a SPECIFICATION_DEFECT.** **Do
not invent a consequence.** **A consequence written after the evidence is
seen is not a pre-registered consequence, whatever it says.**

**Diff each transcribed paragraph against its §2 source and report that
they correspond.** **A rewritten consequence is a STOP.**

**A5 — Scope, per §5. Final base-to-head scope: 4 additions and 0
modifications.** **`modify:` is `[]` and must remain so.** **A single
modification anywhere is a STOP**, including a whitespace change to the
script.

**A6 — Nothing existing changed.** Every path existing at the evidence
base is blob-identical at commit 4. **Compare path by path**, and
**report the count of paths compared.** **In particular
`scripts/p2_phase01_scalar_exploratory.py`,
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`,
`GATES.md` and both DRAFT files.**

**A7 — Gate invariants untouched.** `GATES.md` blob-identical to the
evidence base; `^## P2-` count 14; `P2-PHASE-01` reads
`Status: PROPOSED`. **Report all three.** **This task changes no gate,
and A6 already proves it; A7 states it because a reader of a science
task will look for it.**

**A8 — The checker over this task's own range**, base `1cb5550f…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_c1-complement-provenance.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`** — an empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE`, the check switched off rather than
passed.

**`authorised_modified_gates` IS `[]`, and here that is the truthful
value**: no gate may change in this task. **The two empty lists mean
opposite things and the difference is in the checker's code, not in the
notation** — `P3` treats `[]` as "nothing to check", `P7` treats it as
"nothing may change".

**`P7` will return `PASS` and it is evidence of nothing** —
`GATE_HEADING` matches zero of the fourteen real gate headings. **This
task changes no gate, so nothing rests on it either way**; A6 is what
establishes that.

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.**

**A8-final, post-report evidence:** re-run RUN 2 at commit 4. **If it
fails, STOP.**

**A9 — Commit-message hygiene** on all four commits. **Commits 1–3 go in
the report; commit 4 is post-report evidence.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  findings artifact. **Nothing else, at all.**
- **No file that exists at the evidence base may be modified**, for any
  reason, including a formatting or lint fix.
- **Do not run the exploratory script.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **both verdicts and the lines establishing each**;
- **R1–R5 each marked CONFIRMED, REFUTED or CANNOT DETERMINE**;
- **whether your reading was independent, anchored-then-agreed, or
  inseparable from the review's** — per the disclosure block;
- **confirmation that the consequence was transcribed, not
  paraphrased**;
- **A6's path count**, and confirmation that the script and the results
  file are byte-identical;
- **A8's two runs, both configs verbatim**, and the statement about the
  two empty lists meaning opposite things;
- **whether the reading bore on `C2` or `C3`**, one sentence each, no
  conclusion;
- **whether answering `C1` made you want to change anything outside this
  task's scope.** **Say what, and confirm you did not**;
- **§6's Rule 16 assessment**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.**

    target      the script and its recorded digest
    method      git rev-parse and sha256sum at 1cb5550f; read
                script_sha256 from the results JSON
    MEASURED    scripts/p2_phase01_scalar_exploratory.py
                blob b44bc63d115f4e88a706d046e60488c51d8a06a0
                sha256 3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
                462 lines. The results file's script_sha256 field
                carries the SAME value. The script is attributable.

    target      the regions named in §1
    method      grep -nE '^def |^class |^[A-Z_]+ *=' over the whole
                file — DEFINITION LINES ONLY
    MEASURED    bisect_root at 138, algebraic_roots at 162,
                root_record at 172, grid_result at 190,
                symmetry_check at 294.
    NOT READ    the author read the definition map and did NOT read the
                bodies of those functions. The answer to C1 is not
                known to the author and is not implied anywhere in this
                specification. **A specification that already knew the
                answer would be pre-registering nothing.**

    target      the ninety zero residuals
    method      over all six grids and all sixteen couplings, sum the
                two non-trivial roots and take |sum + 8|
    MEASURED    90 pairs; max |sum + 8| = 0.00e+00; the six G/Gc = 1.00
                points return a single non-trivial root and are not
                pairs

    target      the symmetry object's fields
    method      read the results JSON's symmetry keys
    MEASURED    Mhat_to_negative_Mhat, sign_pairs,
                wilson_complement_relation, complement_pairs. The last
                two are named in §1 because a field named for the
                relation may be computed FROM it.

    target      whether this task touches anything pinned
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md at 1cb5550f
    MEASURED    TWO pins at that revision:
                line 1015  d8e15469…  for
                  derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
                line 1026  a3ec0cb6…  for
                  derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
                This task modifies neither file, and modifies no file
                named by any pin, so no re-pin is required and none is
                authorised.
    RETRACTED   an earlier draft of this record said ONE pin. The
                author had measured two at this revision in a previous
                task and wrote one here from memory rather than from
                the run. The count was corrected by the author's own
                pre-issue check before issue.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                manifest lists four paths and 'modify: []' contributes
                none; parse OK, counted equals stated.
