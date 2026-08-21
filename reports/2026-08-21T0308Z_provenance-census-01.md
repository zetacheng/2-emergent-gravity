# Execution report — `P2-PROVENANCE-CENSUS-01`

    OUTCOME     COMPLETE. No abort fired. No landing, no merge, no register
                written. `main` does not move.

                S_C 263, S_A 151, S_P 120, S_missing 31.

                S_MISSING IS NOT EMPTY. Its 31 passages refer to TEN distinct
                adjudications for which no landed record was found anywhere
                governance admits. Each of the ten is set out in a
                specification or a derivation and in no register.

                THE CITATION FORM IS WORSE THAN §0b RECORDED. `PI ruling N`
                resolves to two different numbered sets; `PI ruling of this
                session` resolves to three different referents; and one
                citation names an authority the searched scope does not
                contain at all.

                THE SET WAS DISCOVERED, NOT PREDECLARED. The specification
                names no adjudication and states no count, and neither does
                this report carry one from anywhere.

**Specification:** `specs/2026-08-21T0308Z_provenance-census-01.md`
**Review:** `reviews/chatgpt/2026-08-21T0308Z_provenance-census-01.md`
**Census artifact:** `derivations/P2-PROVENANCE-CENSUS-01_census.md`
**Script added:** `scripts/diagnostics/provenance_census_01.py`
**Base:** `d9f676a4b7d0a851c82177f8e14cba1af467b06f`

**Measurement head: `0f46d2e`,** the census commit. This report is the commit
after it. `C11`'s push clause is INTENDED and measured in the post-report
layer.

---

## §0 — Binding SHA (MEASURED, no `A1` abort)

    observed origin/main    d9f676a4b7d0a851c82177f8e14cba1af467b06f
    §0 evidence base        d9f676a4b7d0a851c82177f8e14cba1af467b06f

**Equal**, measured after `git fetch origin main` at execution start and again
after the census commit. `A1` does not fire; `A4` does not fire.

### Review binding (Rule 18, Amendment N) — presence checked before value

`Reviewed specification SHA-256:` is **present**, populated, at
`reviews/chatgpt/2026-08-21T0308Z_provenance-census-01.md:4`, restated at
`:61`.

    sha256 of the specification bytes as committed
      7cc1f91ab3054402473733a40f8ab7dcfcf1706891d9b7d86359d16ac91acf22
    the review's bound SHA
      7cc1f91ab3054402473733a40f8ab7dcfcf1706891d9b7d86359d16ac91acf22

**Equal**, measured against `git cat-file blob` on the committed blob, so the
binding is verified over committed bytes rather than over the supplied file.
Both artifacts arrived AS FILES; neither was pasted.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity
    worktree identity    a real git worktree, branch
                         science/provenance-census-01
    resolved HEAD        0f46d2e at measurement

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.16.3
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**Thirty-seventh consecutive task without `scipy`.** The census imports
`json`, `re`, `subprocess`, `argparse` and `pathlib` only.

**Validators: 332 passed, 2 deselected, exit 0.** Not a criterion here — this
task adds no test and changes no existing code — and recorded as evidence that
nothing was broken.

**Lint.** `ruff check .` reports 13 errors at the task head, in
`scripts/euclidean_reconstruction.py` (8), `tests/test_task_checker.py` (3),
`scripts/governance_tools/task_checker.py` (1) and
`tests/test_repository_structure.py` (1). **All thirteen are the base's**, and
the attribution was measured rather than assumed: `ruff check` on the added
script alone returns `All checks passed!`, and the script does not exist at
`d9f676a4`.

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised.

---

## §2 — Measurements

Nothing was carried, including the three findings §0b states as context. Each
was re-established here or not used.

### `M1` — `S_C`, discovered on five search forms (MEASURED)

    files in the frozen scope     184
    raw hits                      369 lines
    grouped into passages         270
    admitted to S_C by M1         263
    excluded at M1 on reading       7

**Grouping rule, stated because it changes the count:** hits in the same file
within 6 lines of one another form one passage. The forms and their exclusions
are recorded in the census artifact §5 and in the script itself, so the search
is reproducible.

**The seven exclusions are not absences.** Each matched a search form and, on
reading, neither cites, describes, nor relies on an adjudication — four are
`PI RULING` appearing as a **label token** in a vocabulary list, a label census
and a grep pattern; the others concern a review approval, pre-registration
statements, and a question the PI asked rather than a decision the PI made.
**They are recorded individually with their reasons**, not summarised as a
count.

### `M2` — classification of every `S_C` member (MEASURED)

     151  PI RULING
      56  DEPENDENCY DESCRIPTION
      50  OPEN FINDING
       6  EXECUTOR DISPOSITION
       0  RATIFIED DISPOSITION, RECOMMENDATION, INDETERMINATE
     ----
     263

**Every member carries one of six reason codes**, defined once in the artifact
and printed on every row. `S_A` = `PI RULING` + `RATIFIED DISPOSITION` = **151**.

**On `INDETERMINATE` being unused — see `S-2`.** It was available throughout
and no member required it. That is an outcome, and it is one worth stating
plainly rather than presenting as tidiness.

### `M3` — `S_P`, landed provenance per adjudication (MEASURED)

**The 151 `S_A` passages refer to 33 distinct adjudications.** Provenance was
determined per adjudication and then applied to its citing passages.

    adjudications                     33
      landed, FULL                    19
      landed, SUMMARY only             4
      no landed record found          10

    S_P        120 passages
    S_missing   31 passages

**Matching was on content, never on number or name**, per §0b. For each of the
ten, a content search for the ruling's own substance was run over
`DECISION_LOG.md`, `decisions/`, `CONVENTIONS.md`, `GATES.md`, `docs/` and
`derivations/`, and returned nothing.

**The criterion that decides `S_missing`'s size, stated because it is a
judgement — see `S-6`.** A specification transcribing a ruling is **not**
treated as a landed record of it.

### `M4` — `S_missing`, with its citing passages (MEASURED)

     1  ADJ-19  "Reading 1 governs" — the Fierz integration's commit order
     3  ADJ-20  the gamma5 definition governs from the Phase-A freeze
     1  ADJ-21  a registered-gate artifact pin denotes the exact bytes
     6  ADJ-22  "not operative at this gate" as a third disposition
     5  ADJ-23  C is split into C-a, C-b and C-c
     3  ADJ-24  the amendment / new-numbered-rule dichotomy
     7  ADJ-25  the RECON-01B-B0 ruling set — rulings 1, 2 and 4
     1  ADJ-26  Researcher-Reviewer review exchanges, 2026-08-06
     2  ADJ-27  the ruling commissioning P2-OBS-IDENT-01
     2  ADJ-28  the D-pre-A ruling on the canonical kinetic operator

### `M5` — the label question (MEASURED)

**Six blocks had a source to compare against; five are faithful and one
diverges.** One normalisation was applied to both sides — strip blockquote
prefixes, strip code and emphasis delimiters, collapse whitespace including
line breaks — and the comparison is a **normalised substantive** check, not a
byte-exact one.

The single divergence is `docs/GOVERNANCE-DEBT.md:307-312` against the
PI-confirmed source's item 2, already measured and already disposed of
additively beneath `G-13`. Both texts are landed there and are not restated.

**Every block of the ten in `M4` claims to reproduce a ruling and NONE can be
tested**, the repository holding no independent source for any of them. That is
`M5`'s third outcome — *no source available for comparison* — recorded as such,
and it is neither a finding of faithfulness nor one of divergence.

### `M6` — the citation form (MEASURED)

**Three distinct numbered adjudication sets are cited.** `ruling 2` and
`ruling 4` each resolve to two of them, distinguished by nothing in the
citation. **One citation resolves to none**: `derivations/P2-DEFERRED-ITEMS.md:199`
names "the `D-pre-A` ruling on the canonical kinetic operator" as the authority
for `DEFERRED-04`, and no such ruling is landed in the frozen scope — the
`D-pre-A` dossier itself carries no ruling text.

**A named form has the same defect.** `PI ruling of this session` occurs four
times with three referents, and resolves only through the artifact's own date
and subject.

**§0b said the numbered form was found not to be unique. It is worse than
that:** the named form is not unique either, and a citation exists that
resolves to nothing.

### `M7` — the two statement pins (MEASURED)

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Unchanged. Neither `CONVENTIONS.md` nor `assumptions/H-EXT-01.md` appears in
this task's changed-file set.

---

## §4 — Abort conditions, each evaluated

    A1   base SHA differs from §0                       DOES NOT FIRE
    A2   the searched scope cannot be read              DOES NOT FIRE
    A3   (not an abort, by its own terms)               n/a
    A4   main moves during execution                    DOES NOT FIRE
    A5   a path outside the §0d manifest is modified    DOES NOT FIRE

`A2`: all 184 files in the frozen scope were read from committed blobs at the
base; no read failed.

`A3` records that an unclassifiable item is recorded `INDETERMINATE` and
execution continues. **No item reached that case.**

---

## §8 — Acceptance criteria

    C1   four sets as explicit lists, each with evidence      SATISFIED
    C2   every S_C member classified, with its reason         SATISFIED
    C3   the three set relations, member by member            SATISFIED
    C4   no S_A membership on a verb; M3 not a condition      SATISFIED
    C5   M5 and M6 in the required forms                      SATISFIED
    C6   no recommendation and no proposed rule               SATISFIED
    C7   §6.6's three named non-establishments                SATISFIED
    C8   INDETERMINATE recorded, not dropped or forced        SATISFIED
    C9   forms searched and exclusions recorded               SATISFIED
    C10  M7's two Statement SHAs unchanged                    SATISFIED
    C11  manifest, main unmoved, branch-only push             INTENDED — post-report

**`C3`, re-derived from the artifact's own printed table rather than from the
working data**, so the check tests what a reader can see:

    |S_C| 263   |S_A| 151   |S_P| 120   |S_missing| 31
    S_A ⊆ S_C                     True
    S_P ⊆ S_A                     True
    S_missing == S_A − S_P        True
    S_P ∩ S_missing == ∅          True
    S_A == S_P ∪ S_missing        True
    arithmetic  151 − 120 = 31 = |S_missing|   HOLDS

**`C4`, in both directions.** All 151 `S_A` rows carry `r1` or `r2`, and
**neither code mentions a landed record**: `r1` is "a landed block reproducing
a ruling, or its immediate preamble identifying one", `r2` is "cites a
specific, identified adjudication as authority for something". Membership rests
on contextual evidence, never on the presence of a verb — the 50 `OPEN FINDING`
members are exactly the passages that use adjudicative words about a decision
**not yet made**, and they are excluded from `S_A` on that ground.
**No member was excluded from `S_A` for lacking a landed record**; that is what
makes `S_missing` non-empty.

**`C6`.** No sentence recommends anything or proposes a rule. Both occurrences
of "should" in the artifact are explicit non-decisions —
"Whether either form should change is not decided here" and its §9 restatement.

**`C8`.** `INDETERMINATE` is defined, available and used zero times. See `S-2`
for why that is a reading result rather than a forced one.

**`C11`.** Four paths, each mapped to the manifest entry admitting it:
`P1` the census artifact, `P2` the new script, `P3` the spec and the review.

---

## §9 — Substring hazards, and how each was handled

    ruling        `PI ruling N` in two distinct namespaces is M6's subject and
                  was measured, not assumed. "Ruled" as ordinary past tense was
                  separated by reading: the 50 OPEN FINDING members are largely
                  that case.
    decision      `decisions/`, `DECISION_LOG.md`, "decided" and "decision
                  owner" were kept apart; the last two produced DEPENDENCY
                  DESCRIPTION members, not S_A members.
    adjudication  the act, the document, and the phrase inside unrelated
                  clauses. `reversible by PI adjudication` is the recurring
                  unrelated clause and produced the 6 EXECUTOR DISPOSITION
                  members, which expressly say they are NOT PI rulings.
    agreed        no member entered S_A on "agreed" alone.
    item          numbered items of a document, register items and list items
                  are distinguished per member by the referent column.
    verbatim      the label under examination against ordinary usage. Four
                  members were EXCLUDED at M1 precisely here, `PI RULING`
                  appearing as a label token rather than as a citation.

---

## §0c — Non-objectives, all honoured

Nothing was landed, registered, placed or recorded in any register. No citation,
label or record was decided to need amendment. **Every discrepancy is reported
with both sides and none is resolved** — the divergent block, the two-set
citation form, the citation resolving to nothing. Whether the citation form
should change is not adjudicated and no rule is proposed. Nothing was merged and
`main` did not move. No file under `scripts/` was modified — one was **added**,
which `P2` authorises and which is named here and in the artifact. **No figure
was carried from a prior task's report**; the three §0b findings were
re-established from the repository, and two of them turned out to understate
what is there.

---

## Stops and clarifications

**No stop occurred.** The entries below are clarifications and method errors,
recorded because three of them nearly changed a reported number.

### `S-1` — the specification's own §0b was understated, and that is a result

Not a defect. §0b states three findings as context and requires each to be
re-established or not used. Two came back stronger: the citation form is
non-unique in its **named** variant as well as its numbered one, and one
citation resolves to **no** ruling at all. **Recorded as a measurement, not as
a correction to the specification**, which asked for exactly this.

### `S-2` — the rule set left 61 members `INDETERMINATE`; reading resolved all of them

**Not a stop.** The first classification pass, driven by ordered regular
expressions, returned 61 `INDETERMINATE` members. Each was then read in its
file. All 61 resolved: 6 were landed ruling blocks whose preamble the rules did
not recognise, 24 were citations of an identified adjudication, 13 reserved a
decision **not yet made**, 4 stated a register's scope, 7 were not adjudication
mentions at all and were excluded at `M1`, and 7 more resolved on a second
reading of their surrounding lines.

**Category: `OBSERVATION_METHOD_ERROR`** — the repository state was correct and
the first inspecting method was too coarse.

**Why this is recorded rather than presented as a clean result.** A census
reporting zero `INDETERMINATE` invites the suspicion that the class was
avoided. It was not: it is defined in the artifact, printed in the reason-code
list, and available on every row. **The honest statement is that every passage
proved classifiable on reading, and that the machine pass alone did not
establish that.** The hardest cases were the three bare fragments — a line
reading only `PI decision.`, and two `The open item, reproduced verbatim:`
preambles — and each was settled by reading its surrounding block, which showed
the first to reserve a future decision and the other two to introduce an open
item rather than a ruling.

### `S-3` — two path-level referent rules shadowed a distinct ruling in the same file

**Not a stop. Caught by an arithmetic cross-check, not by inspection.**

Referents were assigned partly by a file-level rule: every passage in a given
specification maps to the adjudication that specification is about. **Two files
each contain a SECOND, different ruling**, and the rule swallowed both:

    specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:130
      "PI ruling: Reading 1 governs" — the commit order. Mapped to the Fierz
      sign-convention ruling, which is landed; it is ADJ-19, which is not.

    specs/2026-08-06T0456Z_role-model-and-executors.md:141
      "PI decision, 2026-08-06: Researcher-Reviewer review exchanges are ..."
      Mapped to the role-model ruling, which is landed; it is ADJ-26, which
      is not.

**How it surfaced.** The adjudication table held ten adjudications with no
landed record, and `S_missing` grouped into only eight. **Ten and eight do not
agree, and that disagreement is what exposed it** — not a re-reading. Both
passages moved from `S_P` to `S_missing`; `S_P` went 122 → 120 and `S_missing`
29 → 31.

**Category: `OBSERVATION_METHOD_ERROR`.** **It is also the census's own
finding, and is carried in the artifact's §9 as `THE SHADOWING RISK`**: whether
other files carry more than one ruling is unmeasured, and a per-file
attribution would miss every such case.

### `S-4` — the `C3` verification regex silently dropped every `S_P` row

**Not a stop.** The first run of the independent `C3` check, reading the
artifact's printed table, reported `|S_C| 143, |S_A| 31, |S_P| 0`. The set
relations all evaluated `True` against those numbers.

The cause was the character class `[A-M-]{3}` matching the per-row set marks.
**`P` is not in the range `A`–`M`**, so every row marked as a member of `S_P`
failed to match and was dropped from the parse entirely.

    before   |S_C| 143   |S_A| 31   |S_P| 0    |S_missing| 31
    after    |S_C| 263   |S_A| 151  |S_P| 120  |S_missing| 31

**Category: `OBSERVATION_METHOD_ERROR`.**

**What makes it worth recording is that the check PASSED while wrong.** Every
relation held over the truncated parse — `S_P` empty is trivially a subset of
`S_A`, and `S_missing == S_A − ∅` is trivially true. **The check would have
reported a green `C3` over a set it had never read.** It was caught because
`|S_P| = 0` is implausible on its face, not because any relation failed. A
criterion that can pass over a subject it silently failed to read is the shape
`P7`'s vacuous-green history in this repository already records.

### `S-5` — an `M5` comparison used the wrong line range and reported a false divergence

**Not a stop.** The first run of `M5-3` compared `CONVENTIONS.md:1494-1496`
against `decisions/2026-08-19-inconclusive-disposition.md:14-16` and returned
`DIVERGENT`. The second range was wrong: the decision file's ruling text sits
at `:11-13`, and `:14-16` is the sentence after it. Re-run against the located
block, the comparison returns **FAITHFUL**, and that is what the artifact
records.

**Category: `OBSERVATION_METHOD_ERROR`.** The line numbers were assumed from
the file's shape instead of being located first. **A false divergence in an
`M5` row would have been reported as a governance defect in a landed rule.**

### `S-6` — "a specification is not a landed record" is a criterion this task had to supply

**Not a stop, and recorded because it determines `S_missing`'s size.**

`M3` asks whether "a landed record of the adjudication itself exists anywhere
governance admits". Specifications are landed artifacts and are governing
artifacts under Rule 15. **If a specification transcribing a ruling counted as
that ruling's landed record, all ten members of §1 would be in `S_P` and
`S_missing` would be empty.**

The criterion applied is that it does not count, and the ground is landed
precedent rather than the executor's preference: `P2-ADJUDICATION-SOURCE-02`
created a `decisions/` record for a document whose items
`P2-GOV-HOUSEKEEP-02`'s specification had already transcribed, on the stated
ground that the transcription was not itself the record.

**The criterion is stated in the artifact at §1 so a reader can reject it and
recompute.** **If it is rejected, `S_missing` is empty and the census's
substantive result disappears** — which is why it is reported here as a
judgement rather than buried as a method note.

### `S-7` — a second tier of provenance exists and no rule says whether it counts

**Not a stop.** Four adjudications are known to a register that records **that**
they were ruled and **what** was decided, without carrying the ruling's words:
`ADJ-14`, `ADJ-16`, `ADJ-17`, `ADJ-18`. They are counted in `S_P` and marked
`SUMMARY`.

**`G-08`'s evidence line points at a specification as the place its ruling is
recorded** — the same arrangement as the ten of §1, differing only in that a
register notices it.

**The executor did not decide whether a summary record is sufficient
provenance.** Both tiers are recorded, per adjudication, and the question is
carried in the artifact's §9 as open.

### `S-8` — the scope exclusion has a specific, named cost

**Not a stop; the exclusion is the PI's and is not questioned here.**
`reviews/` and `reports/` were not searched. **`reviews/pi/` holds three
historical PI records**, named by path and blob id at
`docs/GOVERNANCE-DEBT.md:486-490`. An adjudication landed only there would
appear in `S_missing` and would not in fact be missing.

**No member of `S_missing` is known to be in that position** — none of the ten
is cited as living in `reviews/pi/` — but **this census cannot exclude it**,
and the artifact's §8 says so rather than presenting `S_missing` as a
repository-wide result.

---

## Rule 16 — the accumulated reading

**The junction is named, not asserted away.** This artifact now sits alongside
`decisions/2026-08-20-adjudication-source.md` and `DECISION_LOG.md`'s `R-8`,
which recorded the citation-form ambiguity for the first time.

**The inference their combination makes available, and which none of them
states, is that the provenance problem is now MEASURED AND BOUNDED** — that
ten adjudications lack records, and that the rest are accounted for. **It does
not follow.** The census covers one scope, on five search forms, and its own §8
records that a form nobody ran would find what the five did not. **A list
assembled by searching is not a survey**, and the absence of an eleventh is not
evidence that there is none.

---

## Layering

This report is measured at `0f46d2e`, the census commit, which is commit N−1.
**`C11`'s push clause is measured in the post-report layer**; that evidence is
returned to the Reviewer in chat and is not written back into this file.
