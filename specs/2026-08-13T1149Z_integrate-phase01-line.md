# Task specification — integrate the science line, and land it

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   science/integrate-phase01-line
    Cut from           authoritative main @ 1cb5550f…

    Sources, merged in THIS ORDER and no other:
      1  science/adopt-parameter-domain-labels    8b79fad4d62be70724b83850c2a8f23ffee1392f
      2  science/adopt-admissibility-contract     f27f868a03449416fbf6eb96e9d5522c33f46806
      3  science/c1-complement-root-provenance    92726596f29e12ec12e7f795bd68b902ac712d50
      4  science/c3-curvature-asymmetry           c6f4f5e35c8591d18c51443678142f52891b7edd

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This is the integration authorization AND the landing authorization.**
§7 carries the landing clause; **no second task is required.**

**Four merges. Two of them conflict, and both conflicts are resolved by
text given verbatim in §4.** **Any other conflict is an immediate STOP.**

**Source 1 carries three commits' worth of parameter-domain work**
(`2e4cc6eb…` adoption, `cd1ebd84…` repair, `8b79fad4…` labels) as its
ancestry. **Merging it merges all three.** **Do not merge `2e4cc6eb…` or
`cd1ebd84…` separately.**

**`governance/p1-declared-total @ 8ff032e7…` is NOT integrated here.** It
carries an undischarged `A10` and waits on the `P7` repair. **It is a
different line and this task does not touch it.**

---

## 0. What lands

**Two adopted prerequisite artifacts, two completed C-checks, one
open-items register, and eighteen task records.**

    derivations/P2-PHASE-01_microscopic_parameter_domain.md
    derivations/P2-PHASE-01_input_admissibility_contract.md
    derivations/P2-PHASE-01_C1_complement_root_provenance.md
    derivations/P2-PHASE-01_C3_curvature_asymmetry.md
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md

**After this lands, `P2-PHASE-01` has both prerequisites `SATISFIED` and
remains `PROPOSED`.** **That combination has never existed on any single
branch**, and §8 requires it stated where a reader meets it.

## 1. What this does NOT establish

**No phase has been found. No candidate has been assessed. Nothing has
been evaluated against the admissibility standard this merge lands.**

- **The gate's `Required computations` section still reads
  `(not started)`.** Landing two prerequisites does not start them.
- **Three evaluation inputs remain open** — `OPEN-AC-1`, `OPEN-AC-3`,
  `OPEN-AC-4` — **one of them not started at all.**
- **`C1` and `C3` removed evidential weight; they added none.** The
  negative-mass branch's stored position and restricted curvature are
  now known to carry no content independent of the ordinary branch.
  **That is not a demonstration that the branch is unphysical**, and the
  landed artifacts say so.
- **Three items in the C-check register are open**, including one that
  qualifies `C1`'s own exactness verdict as resting on a refuted
  argument.

**Do not describe this merge as progress toward a verdict.** It is
progress toward being able to ask the question.

## 2. Merge order, and why it is fixed

**The order determines which conflicts arise, so it is frozen.**

    merge 1  8b79fad4  clean, measured
    merge 2  f27f868a  CONFLICTS in two paths, resolved per §4
    merge 3  92726596  clean, measured
    merge 4  c6f4f5e3  clean, measured

**Sources 3 and 4 add only base-absent paths and touch nothing the
earlier merges touch.** **Sources 1 and 2 both modify `GATES.md` and both
insert a paragraph immediately after the first heading line of
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.**

**The second conflict was NOT predicted by either branch's
specification.** Source 1's task inserted a cross-reference into the
contract draft; source 2's task inserted a supersession pointer into the
same file at the same place. **Each was authorised in isolation and
neither could see the other.** **It was found by dry run, not by
reading.**

## 3. Conflict resolution is normally forbidden; here it is authorised twice

**An integration task must not author content.** **The two resolutions
in §4 are given verbatim so that the executor substitutes rather than
decides**, and so that the resolving text is reviewed before it is
written rather than after.

**Any conflict other than the two named is an immediate STOP.** **Do not
resolve it, do not take one side, do not consult the branches.**

**Report both resolutions in full**, and **report that no third conflict
occurred.**

## 4. The two resolutions

### 4a. `GATES.md` — take the incoming side entire

The conflict region has, on the `HEAD` side, the OLD
`### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT`
block carrying the draft pin `e373efcb…`; and on the `f27f868a…` side,
the new `### Satisfied prerequisite — …` block carrying the adopted
contract's pin `e63f5a7f…`.

**Resolution, stated in SEMANTIC BLOCKS and not in conflict markers:**

    PRESERVE  the already-landed MICROSCOPIC PARAMETER DOMAIN block
              from HEAD, byte for byte
    REPLACE   only the PHASE INPUT / ADMISSIBILITY CONTRACT block, with
              the adopted block from f27f868a…
    PRESERVE  the separating blank line
    AUTHOR    nothing. No other line in GATES.md is changed by the
              resolution.

**The result is exactly `source 1's parameter-domain block` plus
`source 2's admissibility block`, and it does not depend on where `git`
chooses to draw its markers.**

**Why the resolution is stated this way.** An earlier version said *take
the incoming side entire and discard the HEAD side entire*, and asserted
that the parameter-domain block *is not touched by either side of this
hunk*. **In the author's dry run that assertion held** — the markers fell
at lines 1035 and 1072, twenty-five lines below the parameter-domain
heading at 1010, which sat outside them. **But a marker-relative
instruction is only as safe as the marker placement**, and a conflict
hunk may legitimately carry unconflicted context. **Executed literally
under different marker placement, "take the incoming side entire" could
revert the already-landed parameter-domain block to the version source 2
was cut against.** **The semantic form cannot do that.**

**The two branches make substantively disjoint edits.** The
parameter-domain block may appear inside the textual conflict hunk as
context; **if it does, the resolution still preserves HEAD's version of
it byte for byte.**

### 4b. The contract draft — both paragraphs, reconciled

**Both sides are pure insertions after line 1. Concatenating them
verbatim would contradict**: source 2's pointer says *its `OPEN-AC`
entries are unchanged and remain OPEN*, while source 1's says `OPEN-AC-2`
is `RESOLVED FOR ENUMERATION` and `OPEN-AC-5` is `CLOSED`. **Source 2 was
written on `main`, where both were still open, and could not know.**

**Replace the entire conflict region — both sides and all three markers —
with exactly this text:**

    **SUPERSEDED.** Adopted as
    `derivations/P2-PHASE-01_input_admissibility_contract.md`. This file is
    retained as historical evidence and is not operative.

    **Cross-reference.** `OPEN-AC-2` is **RESOLVED FOR ENUMERATION**: the
    negative-mass branch is included as a candidate, and is NOT certified as
    admissible or stable, by the PI ruling recorded in
    `derivations/P2-PHASE-01_microscopic_parameter_domain.md`. `OPEN-AC-5`
    is **CLOSED** — `Mhat = 1` is NOT an admissibility bound — by the same
    answer that closes `OPEN-PD-1` in that artifact. `OPEN-AC-1`,
    `OPEN-AC-3` and `OPEN-AC-4` **remain OPEN**, and the adopted contract
    reclassifies those three as evaluation-input gaps without resolving any
    of them.

    **`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the difference is the
    point.** `OPEN-AC-2` asks whether the branch is physical; the ruling
    answers only where it may appear in an enumeration.

**Nothing else in that file changes.** **No `OPEN-AC` body text is
edited.** **The three-`OPEN-AC` claim now reads "those three", which is
correct once `AC-2` and `AC-5` are accounted for above it.**

## 5. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`, and the four sources to the
SHAs in the header. **Any mismatch → STOP.** **Also confirm
`2e4cc6eb…` and `cd1ebd84…` are ancestors of `8b79fad4…`**, and report
the two exit statuses.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — Merge parentage, per merge, each value derived separately.** For
each of the four merges report parent 1, parent 2 and the merge-base as
three independent measurements with the method for each. **Parent 1 of
merge 1 is this task's review commit; parent 1 of merges 2, 3 and 4 is
the preceding merge commit.** **That is the legitimate merge-as-parent-1
case, not a defect.**

**A4 — Exactly two conflicts, in the two named paths.** Report the
conflicting paths for each merge. **A conflict in any third path, or in
either named path during merges 1, 3 or 4, is a STOP.**

**A5 — The two resolutions applied verbatim**, per §4. **Report the
resolved region of each file in full.** **Report that no conflict marker
(`<<<<<<<`, `=======`, `>>>>>>>`) survives anywhere in the tree** —
search all files, not only the two.

**AND: after resolving `GATES.md`, confirm the MICROSCOPIC PARAMETER
DOMAIN block is byte-identical to source 1's version.** **Report that
comparison.** **A resolution that reverted it — even by taking a
conflict side literally — is a STOP**, and this criterion exists so that
it cannot pass unnoticed.

**A6 — Scope, frozen manifest. Final base-to-head scope: 26 additions
and 3 modifications.**

    stated: 26 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <the report commit>
    mode: exact
    add:
      derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
      derivations/P2-PHASE-01_C1_complement_root_provenance.md
      derivations/P2-PHASE-01_C3_curvature_asymmetry.md
      derivations/P2-PHASE-01_input_admissibility_contract.md
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
      reports/2026-08-12T2258Z_adopt-parameter-domain.md
      reports/2026-08-12T2326Z_adopt-domain-repair.md
      reports/2026-08-13T0034Z_adopt-domain-labels.md
      reports/2026-08-13T0150Z_c1-complement-provenance.md
      reports/2026-08-13T0307Z_c3-curvature-asymmetry.md
      reports/2026-08-13T0740Z_adopt-admissibility-contract.md
      reports/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
      reviews/chatgpt/2026-08-12T2258Z_adopt-parameter-domain.md
      reviews/chatgpt/2026-08-12T2326Z_adopt-domain-repair.md
      reviews/chatgpt/2026-08-13T0034Z_adopt-domain-labels.md
      reviews/chatgpt/2026-08-13T0150Z_c1-complement-provenance.md
      reviews/chatgpt/2026-08-13T0307Z_c3-curvature-asymmetry.md
      reviews/chatgpt/2026-08-13T0740Z_adopt-admissibility-contract.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
      specs/2026-08-12T2258Z_adopt-parameter-domain.md
      specs/2026-08-12T2326Z_adopt-domain-repair.md
      specs/2026-08-13T0034Z_adopt-domain-labels.md
      specs/2026-08-13T0150Z_c1-complement-provenance.md
      specs/2026-08-13T0307Z_c3-curvature-asymmetry.md
      specs/2026-08-13T0740Z_adopt-admissibility-contract.md
      specs/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Twenty-three arrive from the four sources — five under `derivations/`
and six each under `specs/`, `reviews/chatgpt/` and `reports/` — and
three are authored here.** **Report the manifest against what the merges
actually produced, path by path.**

**At the final merge commit, before the report exists, the count is 25
additions and 3 modifications.** **Report which head each figure was
measured at.**

**A7 — Every pin matches at the head.** For each occurrence of
`` (sha256 `<64 hex>`) `` in `GATES.md`, identify the artifact path named
immediately above it, measure that path's SHA-256 at the head, and report
the pair. **Expected: two pins, both matching** —
`4a3bd821…` for the adopted parameter domain and `e63f5a7f…` for the
adopted contract. **Assert the count is at least one**, and **report the
count found.**

**The contract DRAFT is no longer pinned by anything after this merge**,
because §4a's resolution replaces the block that pinned it. **Confirm
that explicitly** — a draft that changed in the merge and is pinned
nowhere is the correct outcome here, and a reader should not have to
infer it.

**A8 — Gate invariants.** At the final merge commit: `^## P2-` count
**14**; `P2-PHASE-01` reads `Status: PROPOSED`; **both prerequisites read
`SATISFIED` and none reads `UNSATISFIED`**; every other gate's `Status:`
line textually identical to the evidence base. **Report all four.**

**A9 — Arriving artifacts, and the two modified drafts, compared
SEPARATELY.**

**(i) The twenty-three ADDED paths** — five `derivations/` artifacts and
eighteen task records — **arrive blob-identical to the source commit that
contributes each.** **Report all twenty-three comparisons.**

**(ii) The two pre-existing DRAFT files, which are MODIFICATIONS and are
not among the twenty-three.** Compare each separately:

    P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
      must match source 1's version exactly. It is modified by source 1
      alone, was not in conflict, and §4 authored nothing for it.

    P2-PHASE-01_input_admissibility_contract_DRAFT.md
      is the SOLE path expected to match NEITHER source 1 NOR source 2,
      because §4b supplies reviewed reconciliation text that exists on
      neither branch. Report both comparisons and confirm both differ.

**An earlier version of this criterion folded the two sets together and
produced three incompatible counts at once** — twenty-three arriving
additions, two modified drafts, and one path differing from both
sources. **They are three different universes and the criterion now keeps
them apart.**

**A10 — Protected paths.** Every path existing at the evidence base other
than the three in A6's `modify:` list is blob-identical at the head. **In
particular everything under `results/`, `scripts/` and `tests/`, and
`CONVENTIONS.md`, `DECISION_LOG.md` and `docs/BRANCHING_POLICY.md`.**
Compare path by path and report the count.

**A11 — Superseded branches not merged, all six.** No commit in the
register is an ancestor of the head:

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A12 — The checker over this task's own range**, base `1cb5550f…`, head
**the final merge commit** — not the report commit, which must carry this
output. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-phase01-line.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  ["P2-PHASE-01"]
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.**

**`RUN 1` uses default subject selection.** The range contains **the six
specifications arriving from the four sources AND this task's own
specification, added at commit 1** — **seven**, not six. **An earlier
version of this clause said six and forgot the one this task writes.**

**Report the subject set the checker ACTUALLY selected, and its results,
as measured.** **Do not infer the selected set from this specification**
— the author has not run the checker over the merged range, and `RUN 1`
governs nothing either way.

**`P7` will return `PASS` and it is evidence of nothing.**
`GATE_HEADING` matches zero of the fourteen real gate headings. **This
task modifies `GATES.md` and flips a prerequisite, so the vacuous green
sits beside the strongest gate declaration in the merge.** **A5, A7 and
A8 are what establish the edit's confinement.**

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.**

**A12-final, post-report evidence:** re-run RUN 2 at the report commit,
**before the landing.** **If it fails, STOP before advancing `main`.**

**A13 — Validators, exit status 0**, run as the repository defines them.
Report pass and deselect counts before and after. **Expected: unchanged
at 280 passed, 2 deselected** — this merge adds no test and changes none.

**A14 — Commit-message hygiene** on all seven commits including the four
merges. **Commits 1–6 go in the report; the report commit is post-report
evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
    commit 3  --no-ff merge of 8b79fad4…
    commit 4  --no-ff merge of f27f868a…, with §4's two resolutions
    commit 5  --no-ff merge of 92726596…
    commit 6  --no-ff merge of c6f4f5e3…
    commit 7  reports/2026-08-XXT{HHMM}Z_integrate-phase01-line.md
    then      fast-forward refs/heads/main to commit 7, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes every
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 6:** A1–A11, A13 and A14 for
commits 1–6; **A12's two runs with both configs verbatim**; commit 1–6
SHAs and stored messages; commit 7's intended message; **A6's final scope
stated as INTENDED, with the measured 25/3 figure at commit 6.**

**Post-report evidence, NOT written back:** A6's final scope measured
base-to-commit-7; A12-final; A7 and A11 re-run after the advance; A14 for
commit 7; validators at the pushed `main`; the push; remote `main` read
back; final ancestry confirmation.

**Nothing in the committed report may claim to measure commit 7.**

## 7. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 7**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward.** `1cb5550f…` is the base of this
branch, so the branch descends from it. **Verify `--is-ancestor` before
the push and report the exit status as a measurement.** **If a
fast-forward is not available, STOP** — do not convert the landing into a
merge.

**Push without `--force` and without `--force-with-lease`.**

**None of the four source branches is deleted, and none moves.** Verify
and report all four tips after the advance.

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** `GATES.md` will read `SATISFIED` for both prerequisites of a
gate that remains `PROPOSED`. **A reader may take that for a gate ready
to run.** It is not: `Required computations` reads `(not started)`, and
three evaluation inputs are open. **Say where a reader meets that.**

**Second.** **Until this merge, neither branch showed the state the
programme was in** — each showed one prerequisite satisfied and the other
not, in opposite senses. **Anyone who checked out either branch saw a
state that did not exist.** **That is now repaired, and the repair is
worth stating**, because the same shape will recur whenever two branches
edit adjacent prerequisite blocks.

**Third.** `P7` returns `PASS` over two empty maps while this merge
carries the strongest gate declaration made so far. **Say that a vacuous
check is most dangerous exactly where the change is largest.**

**One landed inaccuracy arrives with this merge and is NOT repaired
here.** `specs/2026-08-13T0740Z_adopt-admissibility-contract.md`, at
line 150, instructs whoever integrates to *verify afterwards that all
four pins in the merged file match their targets*. **There are two pins
in the merged file, not four** — A7 measures them and §11 confirms it.
The sentence conflated how many times a pin was moved across the two
branches with how many pins the file ends up carrying.

**It is arriving content and this task does not edit it.** **Report it,
name the line, and record that A7's measured two is the correct figure**,
so that a later reader following that instruction is not left counting
to four.

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed**,
  except the two conflict regions of §4, **whose resolutions are given
  verbatim and are not the executor's.**
- **Do not resolve any conflict not named in §4.**
- **Do not edit `CONVENTIONS.md`, `DECISION_LOG.md`,
  `docs/BRANCHING_POLICY.md`, or anything under `results/`, `scripts/`
  or `tests/`.**
- **Do not change any gate `Status:` line.**
- **Do not evaluate any candidate against the admissibility standard
  this merge lands**, and do not name any candidate as passing or
  failing any of its conditions.
- **Do not merge `governance/p1-declared-total`.**
- **Do not write a superseded-register entry.** Nothing is superseded by
  this task; the four sources are integrated, not replaced.
- **Do not describe `P7` as having checked gate integrity.**
- Merge commits only for the four integrations: no fast-forward there,
  no squash, no rebase. **The landing is a fast-forward or a stop.**
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
- **A3's twelve values**, three per merge, each separately derived;
- **A4's per-merge conflict list**, and confirmation that exactly two
  occurred;
- **A5's two resolved regions in full**, the tree-wide marker search,
  and **the byte comparison of the MICROSCOPIC PARAMETER DOMAIN block
  against source 1**;
- **A6's twenty-six additions enumerated**, and both scope figures with
  the head each was measured at;
- **A7's pin table**, the count found, and the explicit statement about
  the now-unpinned contract draft;
- **A8's four invariants**;
- **A9(i)'s twenty-three comparisons**, and **A9(ii)'s two draft
  comparisons reported separately**, with the contract draft confirmed
  to match neither source and the parameter-domain draft confirmed to
  match source 1;
- **A11's six exit statuses, before and after the advance**;
- **A12's two runs**, both configs verbatim, and the `P7` statement;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the four source tips
  unchanged;
- **§8's three Rule 16 junctions**, including the landed four-pins
  inaccuracy, named by file and line, with A7's measured count beside
  it;
- **whether `main` now reads as though a phase had been found.** It has
  not;
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
clone.** **No measurement was taken through a truncated view, and no
figure below was carried over from an earlier task's record.**

    target      the four source refs and the ancestry of source 1
    method      git fetch; git rev-parse; git merge-base --is-ancestor
    MEASURED    all four resolve as stated in the header. 2e4cc6eb and
                cd1ebd84 are both ancestors of 8b79fad4. None of the
                four is an ancestor of main.

    target      the four merges, in the specified order
    method      dry run from 1cb5550f with two placeholder commits,
                then git merge --no-ff of each source in turn
    MEASURED    merge 1 clean; merge 2 CONFLICTS in exactly two paths,
                GATES.md and
                derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md;
                merges 3 and 4 clean.
    MEASURED    the second conflict was not anticipated by either
                branch's specification. Source 1's task inserted a
                cross-reference after line 1 of the contract draft;
                source 2's task inserted a supersession pointer at the
                same position.

    target      the contradiction inside the second conflict
    method      read both sides of the conflict region
    MEASURED    source 2's pointer says the draft's OPEN-AC entries
                "remain OPEN"; source 1's says OPEN-AC-2 is RESOLVED FOR
                ENUMERATION and OPEN-AC-5 is CLOSED. Concatenation would
                contradict. §4b's text reconciles them by scoping
                "those three" to AC-1, AC-3 and AC-4.

    target      the integrated result
    method      apply §4's two resolutions in the dry run, complete all
                four merges, then measure
    MEASURED    scope from 1cb5550f: 25 additions and 3 modifications
                with two placeholders standing in for this task's spec
                and review, and no report. With the three real task
                records that is 26 additions and 3 modifications.
    MEASURED    no conflict marker survives in any file.
    MEASURED    GATES.md carries exactly TWO pins, at the adopted
                parameter domain (4a3bd821…) and the adopted contract
                (e63f5a7f…). BOTH MATCH their targets.
    MEASURED    14 gate sections; P2-PHASE-01 Status: PROPOSED; two
                prerequisites read Satisfied and none reads Unsatisfied.
    MEASURED    four merge commits in the range.

    target      the block separation that produced the GATES conflict
    method      read GATES.md at 1cb5550f, lines 1008-1030
    MEASURED    the MICROSCOPIC PARAMETER DOMAIN block spans 1010-1019;
                line 1020 is blank; the PHASE INPUT / ADMISSIBILITY
                CONTRACT block spans 1021-1027. ONE BLANK LINE separates
                them.
    RETRACTED   the admissibility specification's §11 said "ten lines
                separate the end of one from the start of the other".
                Ten is the length of the first block's body, not the
                separation. Its executor measured this correctly and
                reported it; the corrected figure is recorded here so
                the error does not survive into this task.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 26 additions, 3 modifications;
                the manifest enumerates twenty-six add: paths and three
                modify: paths; parse OK, counted equals stated.
    RETRACTED   an earlier draft of this specification stated the
                additions in prose and left the add: list absent, which
                P1 would have counted as zero. The author's own
                pre-issue run caught it before issue.
