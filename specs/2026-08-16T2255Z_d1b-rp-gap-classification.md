# Task specification — `D-1b`: classifying the reflection-positivity gaps

Specification evidence base: `822cd4fbfe9bff6e43867caed95c5635344683d0`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/d1b-rp-gap-classification
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**It classifies gaps. It does not close them, size them, or use them to
choose a candidate.**

---

## 0. What `D-1` left, and why this is a separate task

**`D-1` landed four `PARTIAL` verdicts, zero `COVERED`, and a burden
accounting of nought replaced and four open.** **Its tables record, per
candidate and per load-bearing theorem, which hypotheses are unmatched.**

**The classification was deliberately NOT performed in `D-1`'s
integration.** That task's `A7` counted `FAIL` entries and assigned no
tags, and its executor reported the reason plainly:

> the taxonomy assigns itself on a first read … `FG26`'s `H1/H2/H3` and
> `KU10`'s auxiliary-field bridge read like either of the other two
> depending on which sentence you weight

**The easy cases classify themselves. The cases that matter do not.**
**This task exists so the hard ones are classified under a reviewed
method rather than on a first read.**

**Raw counts, as landed, for orientation only:**

    naive       20    11 table + 9 prose
    Wilson      13    8 + 5, plus 6 UNKNOWN AT ABSTRACT DEPTH
    staggered   10    5 + 5
    overlap      9    5 + 4

**Re-derive these. Do not carry them.** **The counting rule the previous
executor used — `UNKNOWN AT ABSTRACT DEPTH` counted separately, legend
line excluded, table rows separated from hypothesis prose — is stated
here so you can reproduce it or say why you did not.**

## 1. The three categories

**A `FAIL` may carry MORE THAN ONE tag, and may be layered.** **Do not
force a mutually exclusive assignment.** **Report every tag each entry
carries, and where a tag applies only under a further condition, say
which.**

    UNFROZEN DATUM
        the theorem constrains a quantity the programme has not frozen.

        REQUIRES AFFIRMATIVE REPOSITORY EVIDENCE OF NON-FREEZING.
        Absence of a located freeze is NOT evidence of non-freezing; a
        search that finds nothing yields UNDETERMINED, not this tag.

        Candidates that MAY qualify if §2's verification confirms them:
        reflection type, lattice extent, temporal boundary condition,
        the Wilson parameter r, the hopping or mass domain.

        A source-table phrase such as "not mapped", "not
        convention-mapped", or "not frozen/mapped" is NOT by itself
        sufficient for this tag. Measured in the landed tables: 24
        occurrences of "unfrozen", 7 of "not mapped", 2 of "not
        convention-mapped", 1 of "not frozen/mapped" — DELIBERATELY
        MIXED WORDING, because D-1 only had to decide applicability and
        did not need to separate them. Separating them is this task.

        The MP87 → Wilson row is the clearest case: `r` is FAIL
        "(programme value unfrozen)" while operator normalization is
        FAIL "(not convention-mapped)" IN THE SAME SENTENCE. An earlier
        draft of this specification listed operator normalisation as an
        UNFROZEN DATUM example, collapsing a distinction the artifact
        itself makes. Two further rows record "operator normalization is
        FAIL" with no qualifier at all, which is neither.

    INCOMPATIBLE HYPOTHESIS
        a KNOWN programme fact genuinely conflicts with the hypothesis.
        Example: a theorem proved in two dimensions against a
        four-dimensional target.

    UNESTABLISHED APPLICABILITY BRIDGE
        possibly compatible, but the mapping, specialization,
        factorization or measure junction has not been shown. Examples
        named by the previous executor: FG26's H1, H2, H3; MP87's
        non-gauge specialization; KU10's auxiliary-field junction.

**These close by different means, and that is the whole point of
separating them:**

    UNFROZEN DATUM        may close when D-pre freezes the datum — work
                          the programme intends anyway
    INCOMPATIBLE          that basis cannot cover; other mathematics is
                          needed
    UNESTABLISHED BRIDGE  may need only a targeted applicability lemma
                          rather than a full construction

**None of that is a size estimate.** §4 governs.

## 2. An `UNFROZEN DATUM` claim must be checked against the repository

**This is the criterion most easily satisfied in appearance, and the one
this task is most likely to get wrong.**

**A table entry saying "the programme reflection type is unfrozen" is
`D-1`'s ASSERTION about the repository.** **It is not a repository
fact until it is checked.**

**For every entry you tag `UNFROZEN DATUM`, verify against the
repository that the quantity is in fact unfrozen**, and **report where
you looked.** The places to look, at the evidence base:

    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    derivations/P2-LATTICE-ROUTE-01.md

**If a quantity turns out to BE frozen, the tag is wrong and the entry
belongs elsewhere.** **Report every such case as a finding about `D-1`'s
tables**, not as a correction to them — **you do not modify the arriving
artifact.**

**Report the count verified frozen, the count verified unfrozen, and the
count you could not determine.**

**This matters beyond the tags.** **The `D-1` line has already carried
one chain of assertions that had no independent anchor** — execution 2's
branch and commit were described in successive specifications from an
executor report and are not resolvable in the repository. **A
classification built on `D-1`'s description of the repository, rather
than on the repository, would repeat that shape.**

## 3. The boundary cases are the deliverable

**Report, separately and prominently, every `FAIL` whose tag was not
obvious.** **For each:**

- **the tags it could carry, and the reading that supports each**;
- **which sentence in the source you weighted, and why**;
- **whether you assigned one tag, several, or left it undetermined.**

**`FG26`'s `H1`, `H2`, `H3` and `KU10`'s auxiliary-field junction are
named in advance because the previous executor named them.** **Do not
treat that as the complete list**, and **do not treat it as a
prediction of how they classify.**

**An entry you cannot classify is `UNDETERMINED`, and that is a
permitted outcome.** **Report the count.** **A classification with zero
undetermined entries and zero boundary cases has almost certainly
assigned tags on a first read**, which is exactly what this task was
split off to prevent.

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not estimate how large any remaining work is.** **A tag is not a
  cost.** **`UNESTABLISHED APPLICABILITY BRIDGE` does not mean small**,
  and **`INCOMPATIBLE HYPOTHESIS` does not mean large.**
- **Do not revise `B0`'s seven-to-eleven estimate**, and do not
  re-derive it.
- **Do not select, eliminate, rank or prefer a candidate.** **A candidate
  with more `UNFROZEN DATUM` tags is not closer to admissible** — it is
  a candidate whose gaps happen to depend on decisions not yet made.
- **Do not design a proof route, a lemma, or a construction**, and **do
  not state what would be required to close any gap** beyond naming the
  category.
- **Do not conclude that any missing mathematics does not exist.**
  **`D-1` established that the fetched literature does not supply it**,
  and its search was bounded.
- **Do not modify any existing file**, including `D-1`'s tables.
- **Do not add a register entry anywhere.**
- **Do not claim this unblocks `C-iii` or `D0`.**

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**, and **confirm it identifies
`zetacheng/2-emergent-gravity`** — accept either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`822cd4fbfe9bff6e43867caed95c5635344683d0`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.**

**Report whether `science/d1b-rp-gap-classification` already exists.**
**If it does, STOP** — a second name is not this specification's to
choose.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, BEFORE any measurement.** **Run Rule
13's diagnostic order including Amendment D's step 0**, and report
location, workspace depth, and package availability. **Report whether
the clone is shallow and its commit count.** **If a restoration is
needed, report it in one line each and confirm no repository content was
touched.**

**A4 — The `FAIL` inventory, re-derived.** Report the count per
candidate, **your counting rule stated so it is reproducible**, and
**whether your figures match the landed ones** — `naive` 20,
`Wilson` 13, `staggered` 10, `overlap` 9, with `Wilson` carrying 6
`UNKNOWN AT ABSTRACT DEPTH` counted separately. **A difference is a
finding, not an error to reconcile silently.**

**A5 — Every `FAIL` classified, with tags.** Report the full
assignment: per candidate, per load-bearing theorem, per entry, the tags
carried. **Report the count per tag, the count carrying more than one
tag, and the count `UNDETERMINED`.**

**A6 — `UNFROZEN DATUM` verification, per §2.** For every entry so
tagged, **report the repository check, the file and lines consulted, and
the outcome.** **Report the three counts: verified unfrozen, verified
frozen, could not determine.** **An `UNFROZEN DATUM` tag reported
without its check fails this criterion.**

**Report any entry where `D-1`'s table asserts a quantity is unfrozen
and the repository shows otherwise.** **Zero is an acceptable answer.**

**A7 — The boundary cases, per §3.** Report each with its competing
readings, the sentence weighted, and the disposition. **Report the
count.** **If the count is zero, say so and explain how you satisfied
yourself that no entry was ambiguous** — the previous executor reported
the pull toward first-read assignment as real.

**A8 — Shared or distinct, in TWO LAYERS that must not be conflated.**

    SHARED SUBJECT    the same programme datum, or the same named
                      hypothesis or junction, occurs for more than one
                      candidate
    SHARED CLOSURE    repository or D-1 evidence establishes that the
                      SAME ruling, or the SAME mathematical bridge,
                      would resolve those entries for more than one
                      candidate

**Report both, per tag category, for each of the three tags.**

**DO NOT INFER SHARED CLOSURE FROM SHARED WORDING.** **Where only
shared subject is established, report `SHARED SUBJECT / CLOSURE NOT
ESTABLISHED`.**

**`naive` and `staggered` may both carry `FG26`'s `H1/H2/H3` as
unestablished** — **that is shared subject.** **Whether one bridge would
close both depends on operator structure, and nothing in `D-1`
establishes it.** **Reporting the first as if it were the second would
produce a shared-construction saving the evidence does not support**, and
that saving would go straight into the next task's cost estimate.

**A9 — No sizing, no selection.** **Search the artifact, the report and
the commit messages for any sentence that estimates effort, ranks
candidates, prefers one, or describes how a gap would be closed.**
**Report the search and the finding.** **Report the treatment length per
candidate**, and **whether the lengths differ and why** — the `FAIL`
counts differ by a factor of two, **so unequal treatment is expected and
must be explained rather than levelled.**

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 822cd4fbfe9bff6e43867caed95c5635344683d0
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
      reports/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md
      specs/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**A11 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, all five microspec artifacts including
`_rp-literature-coverage.md`, the three freeze documents named in §2,
both registers, and everything under `scripts/`, `tests/` and
`results/`.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.** **Read the status
line SCOPED to its gate section** — a bare grep's first hit is a
different gate seven hundred lines above.

**A13 — The checker over this task's own range**, base `822cd4fb…`,
head **commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming
only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A14 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A15 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
    commit 4  reports/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A10's final scope stated
as INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A13-final; A14 at commit 4; A15 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **A classification is not a cost estimate.** **Nothing here
establishes that an `UNESTABLISHED APPLICABILITY BRIDGE` gap is cheaper
to close than an `INCOMPATIBLE HYPOTHESIS` one**, only that they close by
different means. **Say that where a reader meets the tag counts**, and
**say that `B0`'s seven-to-eleven estimate is unchanged.**

**Second.** **A tag distribution is not candidate evidence.** **A
candidate whose gaps are mostly `UNFROZEN DATUM` is not better supported;
its gaps depend on rulings the programme has not made.** **Those rulings
are the PI's and are not made easier by being counted.**

**Third.** **This classification rests on `D-1`'s tables, and `D-1`'s
search was bounded.** **A gap that does not appear in the tables is not
classified here**, and **nothing establishes the tables are complete.**

**Fourth.** **`UNFROZEN DATUM` tags are verified against the repository
and the other two are not verified against anything outside `D-1`.**
**An `INCOMPATIBLE HYPOTHESIS` or `UNESTABLISHED BRIDGE` tag rests on
`D-1`'s reading of a fetched source**, which this task does not
re-fetch.

**Report, per tag, whether it was independently verified in this task.**
**Where the source was not re-fetched, state that whether direct source
re-reading would change the tag is `NOT DETERMINABLE BY THIS TASK`.**

**An earlier draft asked whether such a tag "would change if the source
were read directly", which the same junction forbids you from finding
out.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  classification artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified**, including
  `D-1`'s tables.
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not size, select, rank, or design.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- **Push only this task's branch.** **No session branch, no `D-1`
  branch, no `main`.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run and reported rather than assumed.** **Rule 13
  carries two such orders, a known open item; if no environment failure
  occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order**;
- **A4's re-derived counts with the counting rule stated**, and any
  difference from the landed figures;
- **A5's full assignment with the THREE per-tag counts, the multi-tag
  count, and the `UNDETERMINED` count** — five aggregate figures, not
  four;
- **A6's repository checks with files and lines, and the three
  counts**, plus any entry where `D-1`'s assertion and the repository
  disagree;
- **A7's boundary cases with competing readings and dispositions**;
- **A8's SHARED SUBJECT and SHARED CLOSURE findings, reported
  separately, per tag**, with any `CLOSURE NOT ESTABLISHED` stated as
  such;
- **A9's search, finding, and per-candidate treatment lengths with the
  reason for any inequality**;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **§7's four Rule 16 junctions**;
- **whether classifying made you want to size a gap, choose a candidate,
  or sketch a lemma.** **Say which and why, and confirm you did not** —
  **the previous executor reported the pull toward first-read assignment
  as real, and this task's equivalent is the pull toward saying which
  gaps are easy**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the evidence base and the artifact this task reads
    method      git fetch; git rev-parse origin/main; git rev-parse
                <rev>:<path>
    MEASURED    origin/main = 822cd4fbfe9bff6e43867caed95c5635344683d0.
                derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
                is present at blob b9109c87ee8a.

    target      the documents an UNFROZEN DATUM tag must be checked
                against
    method      git rev-parse <rev>:<path> for each
    MEASURED    P2-LATTICE-ONTOLOGY-01.md at 6544fb1a72;
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md at 0be773f6a5;
                P2-LATTICE-ROUTE-01.md at 42be438ff1. All three present
                at the evidence base.

    target      the raw FAIL counts
    method      NOT MEASURED by this author. The figures in 0 —
                naive 20, Wilson 13, staggered 10, overlap 9 — are the
                D-1 integration executor's, reported with a stated
                counting rule. A4 requires them RE-DERIVED, not carried.

    target      the named boundary cases
    method      NOT MEASURED by this author. FG26's H1/H2/H3, MP87's
                non-gauge specialization and KU10's auxiliary-field
                junction are named by the previous executor as entries
                whose tag is not obvious. 3 forbids treating that
                list as complete or as a prediction.

    target      execution 2's branch and commit
    method      git ls-remote --heads origin; git cat-file -t a537e036
    MEASURED    science/d1-literature-coverage-audit-2 is ABSENT from
                the remote, and a537e036 is not a valid object in the
                Researcher's clone. Every earlier description of it in
                this line derives from an executor report and has no
                independent anchor.
    CONSEQUENCE 2 requires UNFROZEN DATUM tags checked against the
                repository rather than accepted from D-1's tables,
                because a chain of unanchored assertions has already
                occurred once in this line.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
