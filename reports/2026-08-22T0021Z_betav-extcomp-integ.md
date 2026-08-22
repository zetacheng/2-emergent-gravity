# Execution report — `P2-BETAV-EXTCOMP-INTEG`

    OUTCOME     COMPLETE. No abort fired. Transport only: nothing was
                interpreted, reclassified, explained or recomputed.

                THE SIGN REVERSAL IS TRANSPORTED OPEN. The landing record
                states it, states that its spread exceeds either endpoint,
                and offers no explanation. C7 verified by reading every
                H-EXT-01 sentence in the record.

                THE §4.4 STATEMENT LANDS WITH ITS SCOPE ATTACHED, once, with
                both denials in the same block. C7a verified per occurrence.

                A PROVENANCE POINT THE REVIEW RAISED IS HONOURED IN THE
                RECORD: the scoped wording is this integration's requirement,
                and the record says so rather than implying the measurement
                artifact already carried it.

                C11 MEASURED, NOT ASSERTED: 47 numeric literals in the landing
                record, every one of them the artifact's own; zero drift.

**Specification:** `specs/2026-08-22T0021Z_betav-extcomp-integ.md`
**Review:** `reviews/chatgpt/2026-08-22T0021Z_betav-extcomp-integ.md`
**Landing record:** `reports/2026-08-22T0021Z_betav-extcomp-integ_landing-record.md`
**Source:** `science/betav-extcomp-01` @ `7035e0b7b4a6eaeefb91900eefc0a74e78f78fa0`
**Base:** `caf5111dacad21da9e204b79b4b7add1f648107c`

**Measurement head: `1987834`,** the landing commit. This report is the commit
after it. `C2` and `C15` are INTENDED and measured in the post-report layer.

---

## §0 — Binding SHAs (MEASURED, no `A1` abort)

    observed origin/main                  caf5111dacad21da9e204b79b4b7add1f648107c
    §0 integration base                   caf5111dacad21da9e204b79b4b7add1f648107c

    observed source ref, from the remote  7035e0b7b4a6eaeefb91900eefc0a74e78f78fa0
    §0 abbreviation                       7035e0b7

**`M1` read the FULL ref value from `git ls-remote` before anything else**, and
it begins with §0's abbreviation. No merge was attempted against the
abbreviation, and the merge was performed against
`refs/remotes/origin/science/betav-extcomp-01` — **the remote ref, not the
local branch**, per Rule 5 point 2.

### Review binding (Rule 18, Amendment N) — presence checked before value

`Reviewed specification SHA-256:` is **present**, populated, at
`reviews/chatgpt/2026-08-22T0021Z_betav-extcomp-integ.md:4`, restated at `:124`.

    sha256 of the specification bytes as committed
      bbbb495f63597acbc612af826bdf5c2aebb637341bd770c42f42f6834283c176
    the review's bound SHA
      bbbb495f63597acbc612af826bdf5c2aebb637341bd770c42f42f6834283c176

**Equal**, measured against the committed blob. Both arrived AS FILES.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity
    worktree identity    a real git worktree, branch
                         science/integrate-betav-extcomp-01
    resolved HEAD        1987834 at measurement
    extra worktrees      two detached worktrees for M2, at the base and at
                         the merge product, outside the repository

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.16.3
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**Clone depth, recorded because `M2` requires it.** No `.git/shallow`; **679
commits reachable from all refs.** The shallow-clone condition that once
produced six governance-test failures did not recur, and its absence was
measured rather than assumed.

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised. **This task computes nothing** — the measurement it lands was made
and reproduced on the source branch.

---

## §1 — Measurements

Nothing was carried, including from the measurement's execution report.
**Every figure in the landing record was read from the landed artifact under
`M8`.**

    M1   source ref read from the remote            7035e0b7… ✓
    M2   validators both sides, unshallowed          332/332 ✓
    M3   dry-run merge                               conflict-free ✓
    M4   revert hazard                               subject set EMPTY ✓
    M5   registers' stated scopes, per record        recorded ✓
    M6   the governing clause                        :25-40 ✓
    M7   two diffs                                   they DIFFER ✓
    M8   the artifact's own figures, read            recorded ✓
    M9   pins and frozen script blobs                unchanged ✓
    M10  append-only byte prefix                     verified ✓

**`M2`–`M4`, `M6`, `M7`, `M9`, `M10` are recorded in full in the landing record
with their raw values and are not restated here.**

### `M8` — what was read, and the two items that most needed reading

The four-variant table, the ten per-component coefficients, both aggregates,
both ratios, the band, the secondary spread, the prediction's outcome and the
reproduction check — all read from
`derivations/P2-BETAV-EXTCOMP-01_external-component-mass-log.md` at the source
ref.

**The assembly weight**, `w_i = 1/5` at `proca_loop.py:130`, established by the
artifact both structurally and numerically to `2.531e-15`, and **`v_i = 1/5` as
the measurement task's own choice** rather than a landed definition. Both are
transported with that distinction intact.

**The window count**, three defined and two used, with the ground for excluding
the third. Transported so the repository is not rewritten as having fewer.

### `M5` — which register admits each §6 record

`DECISION_LOG.md` admits all three, on its stated scope and the precedent of
the entries at `:2506`, `:2593`, `:2655` and `:2770`.
`derivations/P2-DEFERRED-ITEMS.md` and
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` admit none.
**`docs/GOVERNANCE-DEBT.md` admits `R-18` and does NOT admit `R-16` or
`R-17`** — those two are scientific questions about a measurement, not
governance debt. **The answer is recorded both ways and no register was
created.** All three are entered once, in `DECISION_LOG.md`.

---

## §2 — Abort conditions, each evaluated

    A1   base or source SHA differs; M1 not matching §0    DOES NOT FIRE
    A2   M3 reports conflicts                              DOES NOT FIRE
    A3   M2 failure not present at the base, unshallowed   DOES NOT FIRE
    A4   M6 finds no clause, or one contradicting §3       DOES NOT FIRE
    A5   product carries a source blob where main advanced DOES NOT FIRE
    A6   a path outside the §0c manifest in M7             DOES NOT FIRE
    A7   a landing figure differs from M8's reading        DOES NOT FIRE

**`A7` is the one this task is exposed to**, and it was measured rather than
asserted — see `C11` below.

---

## §7 — Acceptance criteria

    C1   source tip an ancestor of main, and a merge parent   SATISFIED
    C2   main reached its tip by fast-forward from caf5111d   INTENDED — post-report
    C3   arriving blobs byte-identical, per path              SATISFIED
    C4   §4.1 with both aggregations, neither as the result   SATISFIED
    C5   §4.2, §4.5, §4.7 as the artifact records them        SATISFIED
    C6   §4.3 with the reversal and the secondary quantity    SATISFIED
    C7   no explanation, no interpretation, no criterion      SATISFIED
    C7a  the §4.4 scope qualification, every occurrence       SATISFIED
    C8   §4.6 window count, not rewritten                     SATISFIED
    C9   §5's four items present as not decided               SATISFIED
    C10  R-16..R-18 recorded, discharged per M5               SATISFIED
    C11  every landing figure equals M8's reading             SATISFIED
    C12  M9's pins and blobs; M10's byte-prefix result        SATISFIED
    C13  M7's base-relative list within the §0c manifest      SATISFIED
    C14  M4 with the manner of any emptiness                  SATISFIED
    C15  refs pushed exactly two                              INTENDED — post-report

**`C11`, by comparison and not by assertion.** Every numeric literal in the
landing record was extracted by pattern and set-differenced against the same
extraction over the artifact:

    distinct numeric literals in the artifact   79
    distinct numeric literals in the landing    47
    in the landing but NOT in the artifact       0

**Zero drift. Every transported figure is the artifact's own.**

**`C7`, verified by reading rather than by pattern alone.** Every sentence in
the landing record containing `H-EXT-01` was read in full — five of them. One
states what `H-EXT-01` leaves open, one is the artifact's non-establishment
statement, one is §8's explicit *not decided*, one is the status-preservation
line, and one is the pin record. **None interprets the result.** A probe for an
explanation of the reversal returned nothing, and a probe for an acceptability
judgement returned nothing.

**`C7a`, per occurrence.** The §4.4 statement appears **once**. Measured on
that occurrence: the scope clause precedes it, and **both denials — physical
irrelevance and unique covariance — appear in the same block.** A search for an
unqualified variant elsewhere in the record returned none.

**`C13`.** Eight paths: six arriving from the source (`P1`), `DECISION_LOG.md`
(`P2`, the register `M5` selected), and this task's own specification, review
and landing record (`P3`).

---

## §9 — Substring hazards, and how each was handled

    band          the variant spread throughout. The other sense — the
                  longitudinal mode's flat band — appears in the source's
                  imported docstrings and is not reproduced here.
    window        mass windows throughout; §4.6 turns on counting them, and
                  no fit window arises since the q grid is fixed.
    reversal      the sign reversal throughout; ordinary usage avoided so the
                  term stays single-sensed where C7 reads for it.
    aggregate     the two aggregates as nouns. "Re-aggregate" appears only in
                  the specification's non-objective forbidding it.
    prediction    **the methodological prediction, never the frozen physical
                  anchor.** The landing record transports the first; the
                  second appears nowhere in it, and the measurement's own
                  disclosure of where an anchor sits in an imported docstring
                  was not reproduced.
    verdict       the measurement's absence of one, and task verdicts. Both
                  senses appear; neither asserts a verdict on the result.

---

## §0b — Non-objectives, all honoured

The result was not interpreted and nothing was stated about what it implies for
`H-EXT-01`, `Q1`, `GAP-A`, `GAP-B`, `MM-1`, `MM-3` or `MM-5`. **None was
reclassified**; no verdict, subclass or `Resolution path` was altered. No
criterion or acceptability judgement was set on any transported figure. **The
sign reversal was not explained and no mechanism was offered.** **No additional
mass window was opened, proposed or scoped** — and `R-17` records why one would
be the wrong instrument. Nothing was recomputed, re-fitted or re-aggregated:
every figure was read. The record of how many windows the pipeline defines was
preserved, not rewritten. The provenance line's candidate sources were not
touched. No file under `scripts/` was modified other than by the merge, which
added one and modified none.

---

## Stops and clarifications

**No stop occurred.**

### `S-1` — `C7a`'s check reported zero occurrences, and the check was wrong

**Not a stop; my verification, caught immediately, and it is the third variant
of one defect class in two days.**

The first `C7a` run reported **zero occurrences** of the §4.4 statement. The
statement is in the landing record inside a blockquote, and the probe collapsed
whitespace without stripping the `>` prefixes — so the normalised text read
`…redefine that > repository quantity…` and no phrase matched.

    before   0 occurrences found; the criterion would have read as unmet
    after    1 occurrence, scope-before Y, both denials Y

**Category: `OBSERVATION_METHOD_ERROR`.**

**This is `R-18` recurring while `R-18` was being registered.** The measurement
task recorded two variants — a search term spanning a line break, and backticks
surviving whitespace normalisation. **This is a third: blockquote prefixes.**
The common cause is the same one `R-18` names: **collapsing whitespace is not
sufficient normalisation over marked-up text.** The correct normalisation, used
for every textual criterion in this task, strips blockquote prefixes and code
and emphasis delimiters *and* collapses whitespace, applied to both sides.

**It is recorded here and not adopted as a rule**, consistent with `R-18` being
registered for adoption rather than adopted.

### `S-2` — a `C7` probe returned an empty capture group, which is not a hit

**Not a stop.** The `C7` interpretation probe printed `['']`, which reads as a
match. It was an alternation whose capture group was empty on the branch that
matched. Re-run with `finditer` reporting matched text: the single match is
`"implies for H-EXT-01"`, from §8's line **"what the result implies for
`H-EXT-01` — not decided; registered `R-16`"** — a required non-decision
statement, not an interpretation.

**Category: `OBSERVATION_METHOD_ERROR`.** Recorded because a probe that reports
a match without reporting *what* matched cannot distinguish a defect from the
statement that denies it.

### `S-3` — the §4.4 qualification is this integration's, and the record says so

**Not a stop. A provenance point the Reviewer raised at its §12, honoured
explicitly.**

The scoped sentence the landing record carries is **required by this
integration's specification**. Checked against the source artifact: the
measurement carries the pre-registered `§0b` text and the reach-not-correctness
distinction, **but not this exact scoped sentence.**

**So the landing record states that the scoped wording is this integration's
requirement** rather than presenting it as wording the measurement already had.
The Reviewer's §12 asks precisely that the two not be blurred, and the
distinction is written into the record at §4 rather than left to this report.

### `S-4` — `R-16` and `R-17` are not governance debt, and `M5` says so

**Not a stop; an `M5` reading worth stating.** Previous integrations in this
line found `docs/GOVERNANCE-DEBT.md`'s stated scope admitting their records
alongside `DECISION_LOG.md`'s. **Here it admits only one of the three.**

`R-18` is a method finding and would sit under that register's `METHOD NOTE`
disposition. **`R-16` and `R-17` are scientific questions about a
measurement** — what it implies for a hypothesis, and why an extraction is
unstable — and that register's stated scope is governance debt, which they are
not. **Recorded both ways per `M5`, and all three entered once, in
`DECISION_LOG.md`.**

---

## Rule 16 — the accumulated reading

**The junction is named.** `main` now carries, together: a measurement showing
the discarded external space is not empty of mass-log content; `A-EXT-01`
defining the retained-space observable; `H-EXT-01` `UNESTABLISHED`; and
`GAP-B`'s identifiability mismatch unresolved.

**The inference their combination makes available, and which none of them
states, is that the axis-TT observable has now been shown to be incomplete —
or, read the other way, that the discarded content has been shown not to
matter.** **Neither follows, and the landing record bars both**: §4's scoped
statement denies the second in terms, and §7 and §8 deny the first by recording
that `H-EXT-01` is unresolved in either direction and that the reading is owed
and unperformed.

**A third over-reading is available and is the one the sign reversal invites:
that the measurement is unreliable and can be set aside.** That does not follow
either. Every component produced a finite, full-rank coefficient under every
frozen variant, and the reproduction check is exact at printed precision.
**What is unstable is the aggregate across windows, and that instability is the
recorded finding — `R-17` — not a reason to discount the components.**

---

## Layering

This report is measured at `1987834`, the landing commit, which is commit N−1.
**`C2`'s fast-forward and `C15`'s push clause are measured in the post-report
layer**; that evidence is returned to the Reviewer in chat and is not written
back into this file.
