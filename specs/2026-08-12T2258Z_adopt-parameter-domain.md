# Task specification — adopt the microscopic parameter domain, with evidence corrections

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   science/adopt-parameter-domain
    Cut from           authoritative main @ 1cb5550f…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main`.** It produces a branch. **Integration
and landing are a separate task.**

**This task adopts a domain. It performs no physics.** It does not run
the checks it commissions, does not answer `C1`, `C2` or `C3`, and does
not enumerate a single phase.

**It modifies `GATES.md`.** That is unusual and §3 states exactly which
lines and why. **No gate status changes; `P2-PHASE-01` remains
`PROPOSED`.**

---

## 0. What is being adopted

**A source artifact exists, reviewed and approved for an adoption task:**

    supplied file   DRAFT_P2-PHASE-01_parameter_domain_for_adoption.md
    sha256          096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba

**That digest is the authority for what is adopted.** **If the file you
are supplied has a different digest, STOP** — a review of one version and
adoption of another is a failure mode this programme has already
experienced once, and it is undetectable from the text alone.

**The substantive decisions are adopted UNCHANGED:** the coordinate `G`,
the window `G/Gc ∈ [0.80, 3.00]`, the sixteen pre-registered values,
`mu = 0` as a fixed input, `a` unfixed, the negative-mass branch admitted
as a candidate, and the pre-registration and non-exclusion statements.
**None of §4's corrections touches any of them.**

## 1. Why the adopted text is not byte-identical to the approved file

**An executor's read-only audit of the approved file against the pinned
results artifact found five defects.** Four are evidence-precision or
completeness defects; one is a reading hazard. **None overturns a PI
ruling and none changes a decision.**

**They are corrected here rather than in a new revision of the source
file, deliberately.** Correcting the source would change its digest and
invalidate the approval it carries. **Correcting it inside a specification
that a reviewer reads keeps the change inside the review, instead of
after it.**

**Every correction in §4 is given as exact old text and exact new text.**
**The executor substitutes; the executor decides nothing.** **If any
`OLD` string is not found verbatim, STOP and report which** — do not
locate an approximate match.

## 2. What this task does NOT do

- **It does not answer `C1`, `C2` or `C3`.** All three remain
  commissioned follow-up checks. **The script that would answer `C1` is
  present at the evidence base and its digest matches; reading it is
  still not authorised here.**
- **It enumerates no phase and computes nothing.**
- **It changes no gate status.** `P2-PHASE-01` stays `PROPOSED`,
  because its second prerequisite — PHASE INPUT / ADMISSIBILITY
  CONTRACT — remains `UNSATISFIED` and this task does not touch it.
- **It does not adopt the admissibility contract**, and does not resolve
  `OPEN-AC-1`, `OPEN-AC-3` or `OPEN-AC-4`.
- **It does not delete or rewrite either existing DRAFT.** Both stay,
  each gaining one pointer paragraph.

## 3. The `GATES.md` edit, in full

**`GATES.md` currently carries, under `## P2-PHASE-01`:**

    ### Unsatisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
    Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
    **UNSATISFIED**. ... Draft:
    `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
    (sha256 `d8e15469…`).

**Adoption's operational meaning is that this block changes.** An adopted
artifact sitting beside a gate that still calls its prerequisite
`UNSATISFIED` is a contradiction on `main`.

**The replacement is given verbatim in A6.** It changes the heading, the
artifact state, the prerequisite state, the path and the digest, **and
nothing else in `GATES.md`.**

**One requirement of the gate's own words is arguably not met, and the
reviewer should rule on it rather than the executor.** The gate says the
future artifact *must decide whether cutoff ratios and finite-density
`μ` are FIXED INPUTS or SCAN DIMENSIONS.* The adopted artifact answers
`μ` = FIXED INPUT, but for the lattice spacing `a` it answers **neither**:
`a` is not fixed and not scanned, because no computed quantity at this
gate depends on it. **That is a third answer to a binary question.** A6's
replacement text states it in those terms. **The executor reports the
wording as specified and does not judge whether it satisfies the gate.**

**Whether the third answer discharges the prerequisite is settled by the
PI ruling at §3a**, not by this section, not by A6, and not by the
executor.

## 3a. PI ruling — the third disposition

**Recorded verbatim as issued by the PI. It is a ruling, not a
derivation, and this specification neither weakens nor paraphrases it.**

> **PI RULING.** "Not operative at this gate" is an admissible third
> disposition for a quantity that neither enters the dimensionless
> computation as a fixed numerical input nor defines a scan coordinate.
> Accordingly, leaving the lattice spacing `a` neither fixed nor scanned
> satisfies this prerequisite. This disposition fixes no physical lattice
> scale. It expires immediately if any quantity computed for this gate
> acquires dependence on `a`; at that point `a` must be given a new
> explicit disposition before the affected computation can serve as gate
> evidence.

> **PI RULING — extension of §3a.** For this prerequisite, no independent
> cutoff ratio requires disposition beyond the lattice-scale quantity
> `a`. In the lattice formulation, the regulator is supplied by the
> lattice itself, while `CONVENTIONS.md` fixes the unit conventions
> `Λ ≡ 1` in the continuum notation and `a ≡ 1` in lattice units. These
> are unit conventions, not assignments of a physical cutoff scale.
> Under this convention, `a` is not a parameter of any quantity computed
> for this gate. Any dimensionless combination already used here,
> including `Mhat = aM`, is an output or derived variable, not an
> additional microscopic scan coordinate or fixed cutoff input.
> Accordingly, the §3a ruling exhausts the cutoff-scale part of this
> prerequisite for the quantities presently identified at this gate. If
> any additional independent cutoff ratio is identified later, it is
> outside this ruling and requires its own explicit disposition before
> affected results can serve as gate evidence.

**The extension closes a gap between what the gate asks and what the
first ruling answered.** The gate asks about "cutoff ratios", plural; the
first ruling addressed `a` alone. **The term is defined nowhere in the
repository** — it occurs exactly once in the whole of `GATES.md`, in the
requirement itself — and the Phase-A freeze's machine record enumerates
`G`, `HS_scale` and `Fierz_basis` and no cutoff ratio at all. **Two
existing artifacts supply the substance**:
`derivations/P2-LATTICE-ROUTE-01.md` records that the lattice is the
cutoff, and `CONVENTIONS.md` fixes `Λ ≡ 1` and `a ≡ 1` as unit
conventions.

**The `a ≡ 1` convention had to be addressed, not stepped around.** A
strict reader could take it for a FIXED INPUT and find it in conflict
with a ruling that `a` is neither fixed nor scanned. **The two are
consistent only because `a ≡ 1` chooses units rather than a physical
scale**, and the extension says so in those words rather than leaving the
reconciliation to a reader.

**This ruling is what gives A6's `SATISFIED` its authority.** Without it,
marking a prerequisite satisfied on a third answer to a binary question
would be the executor or the specification author making a governance
decision. **With it, A6 records a ruling rather than reaching one.**

**The expiry clause is load-bearing.** The disposition holds only while
nothing computed at this gate depends on `a`. **It is not a permanent
exemption**, and the condition that voids it is stated so that it can be
noticed rather than remembered.

## 4. The five corrections, verbatim

### C-1 — the `I0` bracket claims a scope it does not have

**OLD:**

    `1 = 2 G I0(Mhat)`. Every `I0` in the results file is positive
    (`0.02845` to `0.10670`). **A negative `G` therefore requires
    `I0(Mhat) < 0` somewhere, which no measurement has tested.**

**NEW:**

    `1 = 2 G I0(Mhat)`. Every `I0` measured in the results file is
    positive. **The brackets, with their scope stated:** the root-level
    `I0` values span `0.0284403` to `0.1067275` over all six grids;
    on the single grid `n = 48`, `shift 0.0` they span `0.0284534` to
    `0.1067006`; across every `I0`-valued field in the file the upper
    bound reaches `0.1439968`. **An earlier version of this artifact
    quoted the single-grid bracket as if it covered the file.**

    **Partial negative-mass evidence already exists and was overlooked.**
    The file's `symmetry.sign_pairs` evaluates `I0` at
    `Mhat = -0.1, -0.5, -1.0`, giving `0.09046`, `0.11173`, `0.14400` —
    **all positive, at negative mass.** **So it is not true that no
    measurement has tested the sign there.** What has not been
    established is **global** non-negativity over the admissible mass
    domain, and a negative `G` requires `I0(Mhat) < 0` somewhere in it.

### C-2 — §5a names no grid

**OLD:**

    **The accounting, because ninety is not six times sixteen:**

**NEW:**

    **The three examples below are from grid `n = 48`, `shift 0.0`; the
    five-decimal figures are not grid-independent.** The accounting that
    follows is over all six grids.

    **The accounting, because ninety is not six times sixteen:**

### C-3 — §5c names no grid

**OLD:**

    **MEASURED.** The ordinary branch shows a textbook transition:

**NEW:**

    **MEASURED**, grid `n = 48`, `shift 0.0`; **the five-decimal figures
    are not grid-independent** — `+0.02134` reads `+0.02133` at
    `n = 32, shift 0.0` and `+0.02135` at `n = 48, shift 0.25`. **The
    qualitative pattern holds on all six.** The ordinary branch shows a
    textbook transition:

### C-4 — §5b's "ordinary branch" column is a reading hazard

**OLD:**

        G/Gc    ordinary branch    complement branch    ratio

**NEW:**

        G/Gc    near-origin root   complement root      ratio

**And immediately after that table, insert:**

    **Below `Gc` the near-origin root lies at NEGATIVE `Mhat`** — at
    `G/Gc = 0.80` the two non-trivial roots are `-0.41025` and
    `-7.58975`. **It is not the positive-mass condensate branch of
    §5c, which does not exist below `Gc`.** The column is named for
    position, not for sign, and §5b and §5c do not conflict.

### C-5 — two open items were missed

**OLD:**

    **`OPEN-AC-1` — the P/V/A/T construction.** Unchanged and untouched.

**NEW:**

    **`OPEN-AC-1` — the P/V/A/T construction.** Unchanged and untouched.

    **`OPEN-AC-4` — exact/remnant symmetry and Goldstone implications.**
    **REMAINS OPEN.** **An earlier version of this artifact omitted it
    entirely.** It bears on stability and therefore on any later upgrade
    of a candidate to a phase; **it is not a peripheral item and it is
    not addressed here.**

    **`OPEN-AC-5` — whether `Mhat = 1` is an admissibility bound.**
    **CLOSED, by the same answer that closes `OPEN-PD-1`: NO.** The two
    are the same question recorded in two artifacts. **An earlier
    version of this one answered `OPEN-PD-1` and was silent on its
    twin**, which is how a reader of the admissibility contract would
    have gone on believing the question undecided.

**The `OPEN-AC` set has FIVE members, not three.** The earlier count came
from reading the head of the contract file rather than all of it.

## 5. The boundary statement

**Insert, as the final paragraph of §7 of the adopted artifact:**

    **Adoption freezes the enumeration window and the treatment of
    inputs. It does not certify root completeness, full-space stability,
    thermodynamic dominance, negative-`G` exclusion, or finite-density
    coverage.**

**This sentence belongs in the artifact and not only in a report**,
because the artifact is what a later reader opens. **It is the shortest
true summary of what adoption does, and it must be reachable without
finding this task.**

## 6. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. The supplied source artifact
digests to
`096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba`.
**Any mismatch → STOP.** Report both.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18: supplied as a file, no delimiters, bytes unchanged. **It must carry
`reviewed artifact SHA-256:` filled in, not left as a placeholder.**
**If it is blank or names a different digest, STOP and say which.**
Report the supplied file's digest and the committed blob's digest and
show them equal.

**A3 — Pinned inputs at the evidence base**, Git blob ids:

    GATES.md
    849a4fbfe62d6478f092a84b0175357a74bbbb06

    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    <measure at 1cb5550f before use>

    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    <measure at 1cb5550f before use>

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    <measure at 1cb5550f before use>

**Measure all four and report them.** The results file is not modified;
it is pinned because every `MEASURED` literal in the adopted text is read
from it.

**A4 — The adopted artifact.** Create
`derivations/P2-PHASE-01_microscopic_parameter_domain.md` as the supplied
file with **exactly** the substitutions of §4 and the insertion of §5
applied, and its status header changed from

    **Status: DRAFT FOR ADOPTION. Not adopted, not committed.**

to

    **Status: ADOPTED.** Adopted by
    `specs/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md`.

**Report the digest before and after the substitutions**, and **the count
of edit operations applied: EIGHT** — six operations implementing the
five corrections, because C-4 has two parts, plus the §5 boundary
insertion and the status-header replacement. **The eight operations act
on eight distinct anchored strings or insertion points.**

    C-1  1     C-2  1     C-3  1     C-4  2     C-5  1
    §5 boundary insertion  1     status header  1        total 8

**If the count does not come out at eight, STOP and report the
discrepancy rather than reconciling it.** **An earlier version of this
specification said six here while its own prose enumerated eight** —
that arithmetic defect is the reason this criterion now carries the
addition.

**A5 — Nothing else in the adopted text changed.** Diff the supplied file
against the adopted file and **report the diff in full.** **Every hunk
must correspond to §4 or §5 or the status header.** **A hunk that does
not is a STOP.**

**A6 — The `GATES.md` edit.** Replace, under `## P2-PHASE-01`, the block
beginning `### Unsatisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN`
and ending at the line before
`### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT`,
with:

    ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
    Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
    per the PI ruling recorded in §3a of
    `specs/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md`.
    Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER DOMAIN**;
    not a gate ID. Adopted artifact:
    `derivations/P2-PHASE-01_microscopic_parameter_domain.md`
    (sha256 `<the digest measured in A4>`).
    Superseded draft:
    `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`.

    The adopted artifact bounds the scan-eligible coupling `G` to
    `G/Gc` in `[0.80, 3.00]` over sixteen pre-registered values, and
    answers finite-density `μ` as a FIXED INPUT at `0`. **For the
    lattice spacing `a` it answers NEITHER fixed input nor scan
    dimension**: `a` is left unfixed because no quantity computed at
    this gate depends on it, and every quantity is dimensionless.
    **That is a third answer to this gate's binary question and is
    recorded as such.** No scan dimension is admitted without a frozen
    range.

    **Adoption freezes where to look. It certifies no phase**, no root
    completeness, no full-space stability, no thermodynamic dominance,
    no exclusion of negative `G`, and no finite-density coverage.

**`GATES.md` changes in that block and nowhere else.** **The
`^## P2-` section count stays 14** and **`P2-PHASE-01`'s `Status:` line
stays `PROPOSED`** — verify both and report them. **The PHASE INPUT /
ADMISSIBILITY CONTRACT block is untouched and still reads
`UNSATISFIED`.**

**A7 — Two pointer insertions, one per draft.** Each is a paragraph, not
a single line; **no line count is implied.** Insert immediately after the
first heading line of each:

In `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`:

    **SUPERSEDED.** Adopted as
    `derivations/P2-PHASE-01_microscopic_parameter_domain.md`. This file
    is retained as historical evidence and is not operative.

In `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`:

    **Cross-reference.** `OPEN-AC-2` is **RESOLVED FOR ENUMERATION**:
    the negative-mass branch is included as a candidate, and is NOT
    certified as admissible or stable, by the PI ruling recorded in
    `derivations/P2-PHASE-01_microscopic_parameter_domain.md`.
    `OPEN-AC-5` is **CLOSED** — `Mhat = 1` is NOT an admissibility
    bound — by the same answer that closes `OPEN-PD-1` in that artifact.
    `OPEN-AC-1`, `OPEN-AC-3` and `OPEN-AC-4` **remain OPEN**.

    **`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the difference is
    the point.** `OPEN-AC-2` asks whether the branch is physical; the
    ruling answers only where it may appear in an enumeration.

**Nothing else in either file changes.** **No pre-existing `OPEN-AC` body
text and no pre-existing verdict is edited or replaced.** The inserted
cross-reference **records the consequences of the adopted PI rulings
without rewriting the original contract entries.**

**The distinction is the whole point of inserting rather than editing.**
The original entries stay as the state they recorded at the time; the new
paragraph is a later authoritative cross-reference. **It does not pretend
the old text was never `OPEN`.** Report both diffs in full.

**A8 — Scope, frozen manifest.**

    stated: 4 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5>
    mode: exact
    add:
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
      reports/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md
      specs/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths. Nothing under `results/`, `scripts/`, `tests/` is
touched.**

**A9 — The checker over this task's own range**, base `1cb5550f…`, head
**commit 4** — not commit 5, which is the report that carries this
output. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md

**The config for BOTH runs carries these declared sets, and they are
stated here so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  ["P2-PHASE-01"]
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.** An empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE`, which is the check switched off
rather than passed. `DECISION_LOG.md` is untouched by this range, so
`P3` passes truthfully.

**`authorised_modified_gates` names `P2-PHASE-01` because A6 modifies
it.** **Report what `P7` returns and treat it as evidence of nothing:**
`GATE_HEADING` at this evidence base is
`^## (P2-[A-Z0-9-]+)\s*$` and matches **zero** of the fourteen real gate
headings, so `P7` compares two empty maps and returns `PASS` regardless.
**That defect is known, is scheduled for repair in a separate task, and
must not be described here as gate integrity having been checked.**

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.**

**A9-final, post-report evidence:** re-run RUN 2 at commit 5. **If it
fails, STOP.**

**A10 — Protected paths.** Every path existing at the evidence base other
than the three in A8's `modify:` list is blob-identical at commit 5. **In
particular the results file and every file under `results/`,
`scripts/` and `tests/`.** Compare path by path.

**A11 — Commit-message hygiene** on all five commits: proposed message
inspected before, stored message after; no `Co-Authored-By`, no session
identifier or URL, no tool attribution. **Commits 1–4 go in the report;
commit 5 is post-report evidence.**

## 7. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md
    commit 3  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  GATES.md
              derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
              derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    commit 5  reports/2026-08-XXT{HHMM}Z_adopt-parameter-domain.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Commit 3 precedes commit 4 for a reason: A6's replacement text embeds
the adopted artifact's digest, which cannot be measured until commit 3
exists.** Measure it from the committed blob, not from a working-tree
file.

**Committed report — measured at commit 4:** A1–A8, A10, A11 for commits
1–4; **A9's two runs with both configs verbatim**; commit 1–4 SHAs and
stored messages; commit 5's intended message; **the final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-5; A9-final at commit 5; A11 for commit 5; the push; the
branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  four paths in A8. **Nothing else.**
- **Do not edit `CONVENTIONS.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md`, or anything under `results/`, `scripts/`
  or `tests/`.**
- **Do not change any gate `Status:` line**, including
  `P2-PHASE-01`'s.
- **Do not answer `C1`, `C2` or `C3`, and do not read
  `scripts/p2_phase01_scalar_exploratory.py` to answer `C1`.**
- **Do not correct anything in the adopted text beyond §4 and §5.** If
  you find a sixth defect, **report it and leave it**; adoption of a
  reviewed artifact is not the place to repair what the review did not
  see.
- **Do not supply `[]` for `append_only_paths`.**
- **Do not describe `P7` as having checked gate integrity.**
- **Do not touch `main`, and do not merge.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task, `GATES.md` will read `SATISFIED` for one prerequisite of a gate
that remains `PROPOSED` and whose other prerequisite is still
`UNSATISFIED`. **A reader may take "domain adopted" for "the gate is
ready to run".** It is not. **Say where a reader meets that, and say
what the second prerequisite still needs.**

**Second junction.** `P7` will report `PASS` in this task's own checker
output while checking nothing. **The report must not present that as
evidence**, and **must say plainly that a `PASS` from a vacuous check is
the most dangerous kind of green this programme has named.**

## 10. Report contract

- everything in §7 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A4's before and after digests**, and the substitution count;
- **A5's full diff of the adopted artifact against the supplied file**;
- **A6's and A7's diffs in full**;
- **A9's two runs, both configs verbatim**, and the explicit statement
  about `P7`;
- **confirmation that `P2-PHASE-01`'s `Status:` still reads `PROPOSED`**
  and that the ADMISSIBILITY CONTRACT prerequisite still reads
  `UNSATISFIED`;
- **confirmation that `C1`, `C2` and `C3` were not answered**, and that
  the exploratory script was not read;
- **§9's Rule 16 assessment**, both junctions;
- **whether the adopted text now reads as though a phase had been
  found.** It has not;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.** Three of
this author's errors this session came from reading a `head` or `tail`
of a file and treating the visible part as the whole; **the `OPEN-AC`
undercount corrected in §4 C-5 was one of them.** Counts below were taken
over whole files.

    target      the source artifact's digest
    method      sha256sum of the supplied file
    MEASURED    096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba

    target      the OPEN-AC set, counted over the WHOLE file
    method      grep -n 'OPEN-AC-' on
                derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
                at 1cb5550f, no head, no tail
    MEASURED    FIVE items: AC-1 P/V/A/T; AC-2 negative-mass branch;
                AC-3 cross-family comparison; AC-4 exact/remnant
                symmetry and Goldstone; AC-5 whether Mhat = 1 is an
                admissibility bound.

    target      the I0 brackets of C-1
    method      walk every I0-valued field in the results file at
                1cb5550f; and separately the root-level I0 values
    MEASURED    root-level, all six grids: 0.0284403 .. 0.1067275
                root-level, n=48 shift 0.0 only: 0.0284534 .. 0.1067006
                every I0-valued field: upper bound 0.1439968
                All strictly positive.

    target      negative-mass I0 samples
    method      read symmetry.sign_pairs from the results file
    MEASURED    Mhat = -0.1, -0.5, -1.0 give I0 = 0.09046, 0.11173,
                0.14400 — all positive. The claim "no measurement has
                tested" was false.

    target      the sub-critical root signs of C-4
    method      read the root table at G/Gc = 0.80
    MEASURED    both non-trivial roots negative: -0.41025 and -7.58975

    target      the GATES.md block A6 replaces
    method      read GATES.md at 1cb5550f
    MEASURED    the block exists verbatim as quoted in §3, pins the
                draft at sha256 d8e15469…, and is followed by the
                PHASE INPUT / ADMISSIBILITY CONTRACT block. GATES.md
                blob 849a4fbf…, 14 sections matching ^## P2-,
                P2-PHASE-01 Status: PROPOSED.

    target      P7's vacuity, restated as a measurement
    method      apply ^## (P2-[A-Z0-9-]+)\s*$ to GATES.md at 1cb5550f
    MEASURED    14 real '## P2-' headings; 0 matched. P7 compares two
                empty maps.

    target      P3's treatment of an empty declared set
    method      read check_p3 in task_checker.py at 1cb5550f
    MEASURED    declared is None -> NOT_DECLARED; declared == [] ->
                NOT_APPLICABLE, "caller declared an empty append-only
                set". An empty set switches the check off. A9 therefore
                names DECISION_LOG.md.

    target      this specification under its own P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented; a re-implementation of
                this parser produced a wrong result earlier in this
                session
    MEASURED    one scope block; stated 4 additions, 3 modifications;
                manifest lists four and three. They agree.
