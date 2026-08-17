# Task specification — integrate the reflection-positivity gap classification, and land it

Specification evidence base: `822cd4fbfe9bff6e43867caed95c5635344683d0`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-d1b-classification
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/d1b-rp-gap-classification
                       242b2f35…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§7 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`822cd4fb…`, **6 additions and 0 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**Nothing is modified.** No gate, no pin, no register, no script, no
test, and **not `D-1`'s tables.**

---

## 0. The arriving paths carry an inaccurate timestamp token, and it stays

**Measured, the four arriving paths:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
    reports/2026-08-16T2255Z_d1b-rp-gap-classification.md
    reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
    specs/2026-08-16T2255Z_d1b-rp-gap-classification.md

**The `{HHMM}Z` token reads `2255Z`. Commit 1's UTC timestamp is
`2339:43Z` — forty-four minutes later.** **The source executor measured
the time and then typed a different value, found it, and reported it
rather than repairing it.**

**Do not rewrite it.** **Renaming three committed paths means rewriting
commits 1–3, and Rule 20 permits amending only a message with the tree
unchanged.** **`2339Z` is not the time the content was produced either
— it is a commit timestamp — so the rewrite would exchange one
unreliable proxy for another across four layers of pushed history.**

**Treat `2255Z` as the AUTHORITATIVE arriving paths.** **Record in your
report: the token is inaccurate historical metadata; the measured
commit-1 UTC was `2339Z`; no scientific content depends on it; no
criterion checks a token against a clock; and this integration preserves
the source history rather than rewriting provenance retrospectively.**

**An error that happened, was found by its author, and is on the record
is better provenance than one that was erased.**

## 1. What lands

**Fifty-two entries classified. Fifty-four tag occurrences. Eleven
multi-tag. Nine `UNDETERMINED`.**

    UNFROZEN DATUM                       25
    INCOMPATIBLE HYPOTHESIS               8
    UNESTABLISHED APPLICABILITY BRIDGE   21

    naive     20 entries    UD 9  IH 4  UB 7  UNDET 4
    Wilson    13            UD 5  IH 0  UB 7  UNDET 3
    staggered 10            UD 6  IH 3  UB 3  UNDET 1
    overlap    9            UD 5  IH 1  UB 4  UNDET 1

**The `FAIL` inventory was re-derived independently under the previous
executor's stated counting rule and agrees at every position.**

## 2. The finding that justified the task

**`§2` of the source specification required every `UNFROZEN DATUM` tag
verified against the repository rather than accepted from `D-1`'s
wording.** **That requirement caught six entries.**

**The source executor reported that its first pass was about to take
`D-1`'s wording as the evidence** — **twenty-four occurrences of
"unfrozen" in the tables make the assignment feel already done.**
**Searching the repository first instead produced six entries a
wording-based pass would have tagged `UNFROZEN DATUM` without
justification: five reflection type, one observable algebra.**

**Measured, and re-verified by the Researcher: `site reflection`, `link
reflection`, `reflection type` and `reflection plane` occur ZERO times
across all three named freeze documents.** **The ontology freezes
reflection positivity as an OBLIGATION and names no reflection type.**

> **`RP obligation frozen` ≠ `reflection type frozen`.**

**Re-derive the six interceptions and the zero-occurrence measurement.**
**`A6` requires it.**

**And report the source executor's own observation that "could not
determine = 0" is true BY CONSTRUCTION rather than by luck** — anything
unverifiable became `UNDETERMINED` and never received the tag.

## 3. Two entries where `D-1`'s tables and the repository disagree

**`W6` and `n6` record "non-gauge specialization is not frozen".**
**`P2-LATTICE-ONTOLOGY-01.md` line 26 places gauge bosons on the
emergent side**, so **the microscopic action being non-gauge is settled,
not open.**

**Both readings were reported**: as a claim about the theorem the
entries are right; as a claim about programme status the repository
contradicts them. **They were tagged `UB`, and `D-1`'s tables were not
modified.**

**That handling is correct and this task does not revisit it.**
**Report it**, and **report that the arriving artifact lands BESIDE
`D-1`'s tables, not over them.**

## 4. The result that must not be overstated

**Eleven shared subjects. ZERO shared closures ESTABLISHED.**

**`CLOSURE NOT ESTABLISHED` is not `CLOSURE REFUTED`.** **`D-1b` did not
re-read any source and did no mathematics.** **What it established is
that, on the repository and `D-1` evidence available, nothing supports
shared closure** — **not that shared closure does not exist.**

**Transcribe that distinction and do not compress it.** **A report
saying the cheap shared-lemma case is "ruled out" would close a question
that is open**, and the next task would not ask it.

**Report the strongest cases as the source found them:**

- **the temporal boundary condition looks strongest and is not** — the
  four theorems assume different boundary data, so **one ruling matches
  some and excludes others**;
- **`MP87`'s non-gauge specialization appears for `Wilson` and `naive`,
  same paper, same-sounding gap** — but **the `Wilson` entry rests on
  `MP87`'s own site-reflection theorem and the `naive` entry on its
  discussion of the earlier link-reflection proof at `r=0`.** **Shared
  wording is not even shared theorem there.**

**That second case is one instance.** **Do not generalise it to the
other ten**, and **do not conclude that shared closure is unlikely
because one case dissolved.**

## 5. What this does NOT establish, and what comes next

- **No candidate is selected, eliminated, ranked or preferred.**
  **`Wilson` carries zero `INCOMPATIBLE HYPOTHESIS` occurrences.**
  **THAT IS NOT A REASON TO CHOOSE IT.** **A tag distribution is not
  candidate evidence**, and a candidate whose gaps depend on rulings not
  yet made is not better supported.
- **A tag is not a cost.** **`UNESTABLISHED APPLICABILITY BRIDGE` does
  not mean small; `INCOMPATIBLE HYPOTHESIS` does not mean large.**
  **`B0`'s seven-to-eleven estimate is unchanged and is not re-derived
  here.**
- **The classification rests on `D-1`'s tables, whose search was
  bounded.** **A gap absent from the tables is not classified.**
- **Fifty-two entries are not fifty-two independent problems.** **Many
  are repeated manifestations of the same underlying programme datum or
  theorem junction** — **and reducing them is a SEPARATE task this one
  does not perform and does not scope.**

  **That reduction asks a different question from §4's**: not *does one
  bridge close several gaps*, but *does one programme DECISION control
  several entries*. **A temporal-boundary freeze involves no
  mathematics at all.** **Report that the two are distinct.**

## 6. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**, and confirm it identifies
`zetacheng/2-emergent-gravity` — accept either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`822cd4fbfe9bff6e43867caed95c5635344683d0`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.** Report the source at
`242b2f35…` and **that it is not an ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, and it RUNS FIRST.**

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**Criterion numbering is not execution order, and this specification
says so rather than leaving it to be inferred.** **An earlier draft said
`A3` runs "BEFORE any measurement", which `A1` and `A2` contradict —
both require measurements of their own.** **Three tasks in this line
have already stopped on execution-order or repository-identity
ambiguity; a fourth ordering statement disagreeing with the others is
the shape that produced them.**

**Run Rule 13's diagnostic order including Amendment D's step 0**, and
report location, workspace depth, and package availability. **If a
restoration is needed, report it in one line each and confirm no
repository content was touched.**

**The diagnostic needs the workspace location, which `A1` also
measures.** **That overlap is intended: `A3` establishes the environment
is conformant, `A1` establishes it is the RIGHT repository.** **A
conformant environment pointing at `0-programme` passes `A3` and fails
`A1`, and both have happened in this line.**

**A4 — Merge parentage, three separately derived measurements**, with
parent 1 this task's review commit, parent 2 `242b2f35…`, and the
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — §2's interceptions, re-derived.** Report:

- **the count of entries a wording-based pass would have tagged
  `UNFROZEN DATUM` without repository justification** — expected six,
  five reflection type and one observable algebra;
- **the occurrence count of `site reflection`, `link reflection`,
  `reflection type` and `reflection plane` across the three freeze
  documents** — expected zero for each, **reported per term per file**;
- **that the ontology freezes reflection positivity as an obligation and
  names no reflection type**, with the lines.

**This is the finding that justified splitting `D-1b` from the `D-1`
integration.** **A re-derivation that quotes the source report rather
than the repository fails this criterion.**

**A7 — The tag totals and the per-candidate breakdown**, re-derived from
the arriving artifact. **Report the three per-tag counts, the multi-tag
count, the `UNDETERMINED` count, and the per-candidate table.**
**Expected as §1.** **Report what you measured.**

**Re-derive the consistency relation explicitly:**

    52 entries − 9 UNDETERMINED = 43 tagged entries
    43 tagged + 11 multi-tag    = 54 tag occurrences

**This holds only if EVERY multi-tag entry carries exactly two tags and
none carries three.** **Verify that from the artifact and report it.**

**If any entry carries three tags, or if any `UNDETERMINED` entry also
carries a tag, the relation fails and the figures need restating** —
**report the discrepancy, do not reconcile it.**

**The Researcher could not verify this relation.** **A whole-file grep
for the tag names returns prose occurrences, not per-entry assignments**
— 6, 6, 6 and 13 against expected 25, 8, 21 and 9. **The count must come
from the per-entry table, and this criterion exists because the obvious
method does not work.**

**A8 — §4's distinction, transcribed and not compressed.** Report
**eleven shared subjects, zero shared closures ESTABLISHED**, and
**the sentence distinguishing `NOT ESTABLISHED` from `REFUTED`.**
**Report both named cases** — the temporal boundary condition and
`MP87`'s two different theorems — **and confirm neither is generalised
to the remaining nine.**

**A9 — §3's two disagreeing entries.** Report `W6` and `n6`, **both
readings**, the ontology line, and **that `D-1`'s tables are
blob-identical at the head.**

**A10 — The `2255Z` token, per §0.** Report **the four arriving paths
verbatim**, **commit 1's UTC timestamp as measured**, **the
discrepancy**, and **the four statements §0 requires.** **Confirm no
path was renamed and no commit rewritten.**

**A11 — Scope, frozen manifest. Final base-to-head scope: 7 additions
and 0 modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 822cd4fbfe9bff6e43867caed95c5635344683d0
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
      reports/2026-08-16T2255Z_d1b-rp-gap-classification.md
      reports/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
      reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
      specs/2026-08-16T2255Z_d1b-rp-gap-classification.md
      specs/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive from the source, all additions; three are
authored here.** **Report the ARRIVING PATH count and the ARRIVING
ADDITION count separately, and state whether they coincide** — **they
do, at four.**

**The arriving paths are stated here VERBATIM including `2255Z`**, per
§0. **Confirm the manifest matches the committed bytes exactly, with no
token substitution.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Report which head each figure was measured at.**

**A12 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A13 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, all five earlier microspec
artifacts **including `_rp-literature-coverage.md`**, the three freeze
documents, both registers, and everything under `scripts/`, `tests/` and
`results/`.

**A14 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.** **Read the status
line SCOPED to its gate section** — a bare grep's first hit is a
different gate.

**A15 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A16 — The checker over this task's own range**, base `822cd4fb…`, head
**commit 3, the merge commit**. Two runs, `RUN 1` observational and
`RUN 2` naming only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` has two specifications in range**;
report what it actually did. **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A16-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A17 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A18 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 7. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
    commit 3  --no-ff merge of 242b2f35…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.** **Measure the time and use the value you measured** — §0
records what happens otherwise.

**Committed report — measured at commit 3:** A1–A15, A17 and A18 for
commits 1–3; **A16's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A11's final
scope stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A16-final; A14 and A15 re-run after the advance; A18
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The advance
is a fast-forward; `822cd4fb…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no
`D-1` or `D-1b` branch.** **The source branch is not deleted and does
not move**; verify and report its tip.

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **Zero shared closures established is not zero shared
closures.** **`D-1b` re-read no source and did no mathematics.** **Say
that**, and **say that the cheap shared-lemma case is UNRESOLVED rather
than ruled out.**

**Second.** **A tag distribution is not candidate evidence.**
**`Wilson`'s zero `INCOMPATIBLE HYPOTHESIS` count is a fact about which
theorems were fetched and how their hypotheses read, not about which
microscopic theory is right.** **Say so where a reader meets the table.**

**Third.** **Fifty-two entries are not fifty-two problems.** **The
reduction from entries to independent unresolved dependencies has not
been performed**, and **until it is, the tag totals overstate how many
distinct things are open.** **Say that, and say the reduction is a
separate task not scoped here.**

**Fourth.** **`UNFROZEN DATUM` tags were verified against the
repository; the other two rest on `D-1`'s reading of sources this line
has not re-fetched since.** **Whether re-reading a source would change
an `IH` or `UB` tag is `NOT DETERMINABLE` from what has landed.** **Say
that.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing**, and **do not rename any arriving path.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Do not select, rank, size, or perform the dependency reduction.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run and reported rather than assumed.** **Rule 13
  carries two such orders, a known open item; if no environment failure
  occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §7 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**, with
  the execution order stated;
- **A4's three values, separately derived**;
- **A6's six interceptions and the per-term per-file zero counts**;
- **A7's tag totals, per-candidate table, and the consistency relation
  `(52 − 9) + 11 = 54` re-derived**, with confirmation that every
  multi-tag entry carries exactly two tags;
- **A8's shared-subject and shared-closure figures with the
  `NOT ESTABLISHED` ≠ `REFUTED` sentence, and both named cases**;
- **A9's two disagreeing entries with both readings**;
- **A10's four arriving paths verbatim, the measured commit-1 UTC, and
  the discrepancy**;
- **A11's two scope figures and the arriving-path versus
  arriving-addition statement**;
- **A12's merge case, stated BEFORE the blob comparisons**;
- **A13's path count**;
- **A14's four invariants, with the scoped read stated**;
- **A15's six exit statuses, before and after**;
- **A16's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **A17's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§8's four Rule 16 junctions**;
- **whether landing this made you want to choose a candidate, size a
  gap, or start the dependency reduction.** **Say which and why, and
  confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from 822cd4fb with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = 822cd4fbfe9bff6e43867caed95c5635344683d0;
                source = 242b2f35…, NOT an ancestor of main. Merge
                CLEAN; merge-base = 822cd4fb; 6 additions and 0
                modifications at the merge commit; 7 and 0 with a
                placeholder report; the landing fast-forward is
                available.

    target      the arriving paths
    method      git diff --name-only
    MEASURED    four additions, zero modifications. The three task
                records carry the token 2255Z.

    target      the token against the clock
    method      git log on commit 1 of the source branch
    MEASURED    commit 1 = 7063a2a1…, committed 2026-08-16T23:39:43+00:00.
                The filenames read 2255Z. Discrepancy 44 minutes. §0
                rules that it stays.

    target      the reflection vocabulary in the freeze documents
    method      grep -ci for four terms across P2-LATTICE-ONTOLOGY-01.md,
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md and
                P2-LATTICE-ROUTE-01.md at the evidence base
    MEASURED    site reflection 0, link reflection 0, reflection type 0,
                reflection plane 0. The source executor's interception
                is independently confirmed. A6 requires it re-derived
                per term per file rather than taken from here.

    target      the ontology's gauge statement
    method      read line 26 of P2-LATTICE-ONTOLOGY-01.md
    MEASURED    the line places gauge bosons among emergent objects,
                which is the basis for §3's finding that the
                microscopic action's non-gauge status is settled.

    target      the tag totals
    method      NOT MEASURED by this author. 25 / 8 / 21, 52 entries,
                54 occurrences, 11 multi-tag, 9 UNDETERMINED and the
                per-candidate table are the source executor's figures.
                A7 requires them re-derived from the arriving artifact.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
