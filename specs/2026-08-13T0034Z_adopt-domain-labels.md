# Task specification — repair the adopted domain's operative status label, and sweep the rest

Specification evidence base: `cd1ebd84ca588a8ec946fc89e692f9e34760713d`

    Branch to create   science/adopt-parameter-domain-labels
    Cut from           science/adopt-parameter-domain-repair @ cd1ebd84…
    Authoritative main 1cb5550f… — NOT touched by this task

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main` and does not merge.** It is the last
correction the adoption line needs before it is integrable.

**It is the third task to edit this one artifact.** §0 says why, and the
sweep in A5 exists so that there is not a fourth.

---

## 0. One defect, and the reason it was not caught with the other three

**`derivations/P2-PHASE-01_microscopic_parameter_domain.md` at
`cd1ebd84…` carries, at line 85, immediately under `## 3. The domain`:**

    **RECOMMENDATION, for PI adoption.**

**Line 28 of the same file defines that word:** *`RECOMMENDATION` is the
Researcher's and binds nobody.*

**So the adopted artifact labels its own operative content — the domain
itself — as a non-binding Researcher suggestion awaiting adoption.** The
title says ADOPTED, the status line says ADOPTED, and the section that
carries the coordinate, the window, the sixteen values, the treatment of
`mu` and the treatment of `a` says it binds nobody.

**This is worse than the three defects already repaired.** Those were
framing sentences; **this one labels the content.**

**Why it survived two rounds.** The previous specification anchored the
three strings an executor had reported. **It repaired exactly what it
anchored and swept nothing.** **That is the same failure shape as the
adoption task itself**, which anchored the status line and left three
neighbours, and it is why A5 below enumerates rather than anchors.

**The three other `RECOMMENDATION` labels are correct and must stay.**
Lines 131, 252 and 357 mark, respectively, advice on how to record a
ruling, a deliberately weakened reading of an observation, and three
proposed follow-up checks. **All three genuinely bind nobody.** **Only
line 85 is stale.**

## 1. Editing the artifact stales its gate pin — again

    GATES.md:1017  pins  a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
                   for   derivations/P2-PHASE-01_microscopic_parameter_domain.md

**That pin matches at the evidence base and will not match after A4.**
**This is the third consecutive task in which editing a pinned artifact
requires a re-pin in the same task**, and the third time it must be
written into the specification because nothing detects it.

**Authority.** The PI ruling recorded in
`specs/2026-08-12T2326Z_adopt-domain-repair.md` §1 states that a
registered-gate pin denotes the exact operative bytes of the referenced
artifact, and that an authorised modification must not leave a knowingly
stale pin. **This task is an authorised modification under that ruling
and re-pins on the same basis.** **No new ruling is sought and none is
needed.**

**The contract-draft pin at `GATES.md:1040` is NOT touched.** That file
is not modified here; its pin already matches and must still match at the
head.

## 2. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not change any gate `Status:` line**, prerequisite state, heading,
  path, or any digest other than the one at `GATES.md:1017`.
- **Do not edit either DRAFT file.**
- **Do not change the three correct `RECOMMENDATION` labels** at lines
  131, 252 and 357, **nor any `MEASURED`, `PI RULING`, `DERIVED` or
  `CAUTION` label**, nor the vocabulary definition at lines 25–28.
- **Do not change any content of `## 3. The domain`** — not the range,
  not the sixteen values, not the treatment of `mu` or `a`. **Only the
  label above it changes.**
- **Do not answer `C1`, `C2` or `C3`.**
- **Do not repair anything A5's sweep turns up.** **Report it and leave
  it.** If the sweep finds a further stale label, that is a finding for
  the next specification, and **this task's scope does not grow to meet
  it.**
- **Do not write a superseded-register entry.**

## 3. The one anchored edit

**OLD**, occurring exactly once:

    **RECOMMENDATION, for PI adoption.**

**NEW:**

    **ADOPTED.** The domain below was proposed by the Researcher and
    **adopted by the PI**; it is the operative content of this artifact
    and it binds. **An earlier version of this line read
    `RECOMMENDATION, for PI adoption`, which line 28 defines as binding
    nobody** — a label left behind when the artifact's status changed,
    and the last of four such labels to be corrected.

**One anchored edit.** **If the OLD string is not found verbatim exactly
once, STOP and report the count.**

## 4. The re-pin

`GATES.md`, the pin under the MICROSCOPIC PARAMETER DOMAIN block:

    OLD  (sha256 `a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8`).
    NEW  (sha256 `<the digest of the artifact measured from the COMMITTED
          BLOB at commit 3>`).

**One anchored edit, on the digest string only.** **Verify the OLD 64-hex
string occurs exactly once in `GATES.md` before substituting.**
**Measure the new value from the committed blob, not from a working-tree
file.**

## 5. The sweep, which is the point of this task

**Enumerate EVERY kind-label occurrence in the adopted artifact at the
head**, over the whole file, **with no `head`, no `tail`, and no
sampling.** The vocabulary the artifact defines at lines 25–28 is
`MEASURED`, `PI RULING`, `DERIVED`, `RECOMMENDATION`; the file also uses
`CAUTION`, and carries a `Status:` line.

**For each occurrence report: line number, the label, and whether it is
CURRENT or STALE**, where STALE means **the label asserts a state the
artifact is no longer in** — for example a label saying something awaits
adoption in a document that has been adopted.

**The expected census, from the author's own sweep at the evidence base,
given so that a disagreement is visible rather than absorbed:**

    3    Status: ADOPTED                        CURRENT
    25-28 the vocabulary definition             CURRENT (a definition,
                                                not a claim about state)
    52   MEASURED                               CURRENT
    64   MEASURED                               CURRENT
    85   RECOMMENDATION, for PI adoption        STALE — repaired by A4
    129  PI RULING (2026-08-12)                 CURRENT
    131  RECOMMENDATION on how to record        CURRENT
    162  DERIVED, not chosen                    CURRENT
    180  MEASURED                               CURRENT
    219  CAUTION                                CURRENT
    231  MEASURED                               CURRENT
    252  RECOMMENDATION, deliberately weaker    CURRENT
    278  MEASURED                               CURRENT
    357  RECOMMENDATION                         CURRENT

**Fourteen entries — and the counting rule matters, because a naive grep
returns seventeen.** The vocabulary definition spans four lines, each
carrying one label word, and **the census counts LABELLED STATEMENTS, not
matching lines**: those four lines are one entry, because together they
define the vocabulary rather than making four claims about state.

    17  lines matching the label words
    -4  the four definition lines at 25-28
    +1  counted once, as the definition
    ------
    14  labelled statements

**Report both numbers.** **If your count differs from fourteen under this
rule, report yours and do not reconcile it to this one.** **If you find a STALE label other than line
85, report it and leave it** — §2 forbids repairing it here, and a
specification that grows to absorb its own findings stops being a frozen
scope.

**This census is the deliverable that makes a fourth round unnecessary.**
Three tasks have now each repaired the labels reported to them and swept
nothing; **the sweep is what breaks that.**

## 6. Commit order and evidence layering

Cut `science/adopt-parameter-domain-labels` from
`cd1ebd84ca588a8ec946fc89e692f9e34760713d`.

    commit 1  specs/2026-08-XXT{HHMM}Z_adopt-domain-labels.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-domain-labels.md
    commit 3  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  GATES.md
    commit 5  reports/2026-08-XXT{HHMM}Z_adopt-domain-labels.md

    stated: 3 additions, 2 modifications
    base: cd1ebd84ca588a8ec946fc89e692f9e34760713d
    head: <commit 5>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_adopt-domain-labels.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-domain-labels.md
      specs/2026-08-XXT{HHMM}Z_adopt-domain-labels.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Commit 3 precedes commit 4 because the re-pin embeds commit 3's blob
digest.**

**Committed report — measured at commit 4:** A1–A8 and A10–A11 for
commits 1–4; **A9's two checker runs with both configs verbatim**;
commit 1–4 SHAs and stored messages; commit 5's intended message; **the
final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-5; A9-final at commit 5; A6 re-run at commit 5; A11 for
commit 5; validators at commit 5; the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 7. Acceptance criteria

**A1 — Refs.** `science/adopt-parameter-domain-repair` resolves to
`cd1ebd84ca588a8ec946fc89e692f9e34760713d`; `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18. **It must carry `reviewed specification SHA-256:` filled in.** **If
it is blank or names a different digest, STOP and say which.** Report the
supplied file's digest and the committed blob's digest and show them
equal.

**A3 — Pinned inputs at the evidence base.** Measure and report the
SHA-256 of `derivations/P2-PHASE-01_microscopic_parameter_domain.md`.
**It must equal
`a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8`; if
it does not, STOP.** Also report the Git blob ids of `GATES.md` and both
DRAFT files.

**A4 — The one anchored edit**, per §3. **Report the artifact's digest
before and after, and the diff under `--unified=0`.** **Exactly one
region changed.** **Report the changed-line accounting as well as the
hunk count**, and **state the context setting used** — a hunk count
without its context setting is not a measurement.

**A5 — The sweep**, per §5. **Report the full census.** **The count, and
every entry, including the CURRENT ones.**

**A6 — Both pins match at the head.** For each occurrence of
`` (sha256 `<64 hex>`) `` in `GATES.md`, identify the artifact path named
immediately above it, measure that path's SHA-256 at the head, and report
the pair.

**Expected: two pins, both matching.** **Report the count found and every
pair.** **Assert that the count is at least one** — a sweep that finds no
pins and reports success would be the same vacuous green this programme
has now met twice.

**A7 — `GATES.md` changes in exactly one place.** Diff base to commit 4
under `--unified=0`: **one region, one digest string.** **A change to a
heading, path, prerequisite state or `Status:` line is a STOP.** At
commit 4: `^## P2-` count **14**; every `Status:` line textually
identical to the evidence base; `P2-PHASE-01` reads `Status: PROPOSED`;
MICROSCOPIC PARAMETER DOMAIN reads `SATISFIED`; PHASE INPUT /
ADMISSIBILITY CONTRACT reads `UNSATISFIED`. **Report all five.**

**A8 — Protected paths.** Every path existing at the evidence base other
than the two in §6's `modify:` list is blob-identical at commit 5. **In
particular both DRAFT files and everything under `results/`, `scripts/`
and `tests/`.** Compare path by path.

**A9 — The checker over this task's own range**, base `cd1ebd84…`, head
**commit 4**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_adopt-domain-labels.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  ["P2-PHASE-01"]
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.**

**`P7` will return `PASS` and it is evidence of nothing** — at this
evidence base `GATE_HEADING` matches zero of the fourteen real gate
headings. **This task modifies `GATES.md`, so the vacuous green is again
exactly where it is most dangerous.** **A7's diff is what establishes the
edit's confinement, not `P7`.**

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.**

**A9-final, post-report evidence:** re-run RUN 2 at commit 5. **If it
fails, STOP.**

**A10 — Validators, exit status 0.** Report pass and deselect counts
before and after. **Expected: unchanged.** **State plainly that the suite
cannot distinguish a matching pin from a stale one**, which was measured
in the previous task at three revisions.

**A11 — Commit-message hygiene** on all five commits. **Commits 1–4 go in
the report; commit 5 is post-report evidence.**

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task the adopted artifact will be labelled consistently and both pins
will match. **A reader may infer that the adoption line is now
self-consistent by construction.** It is not: **it is self-consistent
because three tasks in sequence found and repaired what the previous one
left**, and **the only reason a fourth is not needed is A5's census,
which was performed once by a person.**

**Say that plainly.** **Neither the label consistency nor the pin
correspondence is checked by anything that runs.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  two paths in §6's `modify:` list. **Nothing else.**
- **Do not change any digest string other than the one at
  `GATES.md:1017`**, and do not add or remove a pin.
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A4's before and after digests, the diff, and the context setting**;
- **A5's full census**, every entry, with the count;
- **A6's pin table**, with the count found and the at-least-one
  assertion;
- **A7's five gate invariants and the one-region diff**;
- **A9's two runs, both configs verbatim**, and the `P7` statement;
- **whether any further STALE label was found**, and confirmation it was
  left unrepaired;
- **§8's Rule 16 assessment**;
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
clone.** **No measurement was taken through a truncated view, and the
census below was taken over the whole 425-line file.**

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    science/adopt-parameter-domain-repair = cd1ebd84…;
                main = 1cb5550f…; the branch head is NOT an ancestor
                of main; it descends from 2e4cc6eb…

    target      the stale label
    method      read the committed blob at cd1ebd84
    MEASURED    line 85 reads "**RECOMMENDATION, for PI adoption.**",
                directly under "## 3. The domain" at line 84.
                Line 28 defines RECOMMENDATION as "the Researcher's and
                binds nobody". The string occurs exactly once.

    target      the other RECOMMENDATION labels
    method      grep -n over the whole file
    MEASURED    lines 131, 252, 357. Each was read in place: advice on
                recording a ruling; a deliberately weakened reading of
                an observation; three proposed follow-up checks. ALL
                THREE ARE CURRENT and none is touched.

    target      the full kind-label census
    method      grep -nE over MEASURED, PI RULING, DERIVED,
                RECOMMENDATION, CAUTION, Status: — whole file, 425
                lines, no head, no tail
    MEASURED    fourteen entries, as tabulated in §5. One STALE.

    target      the pin this task will stale
    method      read GATES.md at cd1ebd84; sha256sum the target
    MEASURED    GATES.md:1017 pins a481955b…, which equals the
                artifact's current bytes. Editing the artifact breaks
                it. GATES.md:1040 pins e373efcb… for the contract
                draft, which is not modified here and must still match
                at the head.

    target      pin count
    method      grep -c 'sha256 `[0-9a-f]{64}`' over the whole file
    MEASURED    exactly TWO

    target      gate invariants at the evidence base
    method      grep -c '^## P2-'; read the P2-PHASE-01 block; compare
                all Status: lines against 2e4cc6eb
    MEASURED    14 sections; 15 Status: lines, textually identical to
                the previous revision; P2-PHASE-01 PROPOSED;
                MICROSCOPIC PARAMETER DOMAIN SATISFIED; PHASE INPUT /
                ADMISSIBILITY CONTRACT UNSATISFIED

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 3 additions, 2 modifications;
                manifest lists three and two; parse OK, counted equals
                stated.
