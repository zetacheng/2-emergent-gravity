# P2-BETAV-EXTCOMP-INTEG — Land the per-component mass-log measurement

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              INTEGRATION. Transport only.

---

## 0. Binding SHAs

    Integration base (main at authorship)   caf5111dacad21da9e204b79b4b7add1f648107c
    Source                                  science/betav-extcomp-01
                                            7035e0b7 (abbreviated)

`M1` reads the full source ref value from the remote. If it does not begin
with the abbreviation above, that is an `A1` return. **No merge proceeds
against an abbreviation.**

---

## 0a. Rule 17 governs, and this landing is unusually exposed to it

The reviewed result is a measurement that **invites a conclusion**. It bears
on `H-EXT-01`, it bears on `GAP-B`'s mismatches, and it produced a figure that
reads as a correction to a target-bearing quantity.

**None of those readings is drawn here.** The measurement set no criterion,
returned no verdict, and recorded its most consequential observation — a sign
reversal in the retained aggregate between windows — as open. **The landing
transports that state, including its openness.**

`C7` fails on any statement that resolves what the measurement left open.

## 0b. Non-objectives

This task does **not**:

1. interpret the result, or state what it implies for `H-EXT-01`, `Q1`,
   `GAP-A`, `GAP-B`, `MM-1`, `MM-3` or `MM-5`;
2. reclassify any of those, or alter any verdict, subclass or `Resolution
   path`;
3. set a criterion, threshold, or acceptability judgement on any figure it
   transports;
4. explain the sign reversal, or offer a mechanism for it;
5. **open, propose, or scope additional mass windows.** More windows chosen
   after seeing a sign reversal would be estimator selection, and the
   question the reversal raises is prior to any further window;
6. recompute, re-fit or re-aggregate any value;
7. rewrite the record of how many mass windows the pipeline defines;
8. touch the provenance line's candidate sources;
9. modify any file under `scripts/` other than by the merge itself;
10. state any measured figure. **Every number in the landing record is read
    from the artifact under `M8`.**

## 0c. Authorised path manifest — defined once

    P1   every path arriving from the source by the merge
    P2   every register selected under M5 for the §6 records. **These may
         differ, more than one may be written, and none may be created.**
    P3   this task's own spec, review, landing-record and report artifacts,
         wherever their authorised paths lie, including under `specs/`

`A6` and `C13` both refer to this manifest and neither restates it.

**Self-check on this specification**: no asserted count or figure; no
unmeasured universal; every `M`/`A`/`C`/`§` reference resolves, sub-references
to a real subsection; no predeclared set; no acceptance criterion covering a
case an abort condition covers; self-referential counts checked against
content.

---

## 1. Measurements

Nothing is carried, including from the measurement's execution report.

    M1   Read the full source ref value from the remote. Record it.
    M2   Test suite on the merge product and at `caf5111d`, in real worktrees,
         **on an unshallowed clone**. Record the clone depth used.
    M3   Dry-run merge: conflict-free or not; conflicting paths if any.
    M4   **The revert hazard.** For every path present on both `caf5111d` and
         the source at differing blobs, record the blob at the fork point, on
         the source, on `main`, and on the merge product, and record HOW any
         emptiness was established.
    M5   Read the registers' stated scopes and record, PER RECORD in §6,
         which admits it. Record the answer either way; none may be created.
    M6   Locate the `science/*` integration clause; record its line span and
         the merge mode, allowed-ref scope and main-advance rule.
    M7   `git diff --name-only caf5111d..<merge product>`, and separately the
         source's contribution against its own fork point. Record both and
         whether they differ.
    M8   **From the landed artifact**, read and record: the frozen parameters
         including the assembly weights; the per-component coefficients; both
         aggregates and both ratios per variant; the band and the secondary
         spread; the prediction's outcome; and the reproduction check.
         **Read, do not carry.**
    M9   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm
         unchanged and neither file modified. Record every blob id under
         `scripts/recon2026/` and `scripts/recovered_2026/` and confirm
         unchanged.
    M10  **Append-only verification.** For every append-only file this task's
         merge product modifies, record the base byte count, the product byte
         count, and whether the complete base bytes are an exact prefix of the
         product bytes. This is the measurement `C12` evaluates. **If no
         append-only file is modified, record that**, so the criterion has a
         source either way.

---

## 2. Abort conditions

    A1   the base or source SHA observed differs from §0, or `M1` returns a
         value not beginning with §0's abbreviation
    A2   `M3` reports conflicts
    A3   `M2` shows a failure not also present at `caf5111d` on an unshallowed
         clone
    A4   `M6` finds no governing clause, or one contradicting §3
    A5   `M4` finds the merge product carrying a source blob where `main` had
         advanced
    A6   a path outside the §0c manifest appears in `M7`
    A7   any figure the landing record states differs from `M8`'s reading of
         the artifact. **Stop and return both.** A transported number that
         drifts is worse than one that is absent.

**Every condition here stops execution.** No acceptance criterion covers a
case any of them covers.

---

## 3. Merge mechanics

Governed by the clause located at `M6`. `--no-ff` merge of the source into a
dedicated integration branch, preserving the source tip as a merge parent;
`main` advances by fast-forward only; push scope is the integration branch and
`refs/heads/main` and no other ref; the source branch does not move.
Prohibited: squash, rebase, force-push, `--force-with-lease`, branch deletion,
history rewrite.

---

## 4. Landing record — required content

### 4.1 The measurement, as measured

`M8`'s figures, per variant, with both aggregations always shown together.
**Neither aggregation is presented as the result**, and the variant whose two
aggregations diverge is identified with the component whose sign accounts for
it, as the artifact records.

### 4.2 The assembly weights, and why they mattered

That the landed assembly's weight was established from the pipeline rather
than assumed, by both a structural and a numerical route, and **what a wrong
weight would have done to every aggregate**. Recorded as the artifact records
it.

### 4.3 The sign reversal, transported open

That the retained aggregate changes sign between windows, that its spread
exceeds either endpoint's magnitude, and that **no explanation is offered and
none is landed here**. Recorded together with the secondary quantity that
makes it visible.

**`C7` fails if the landing record explains it, attributes it, or treats it as
resolved.**

### 4.4 The pre-registered consequence, marked as not a verdict

`§0b` of the measurement's specification stated, before any number existed,
what each outcome would and would not mean. **That text is transported as the
measurement transported it — labelled as a pre-registered consequence and not
as a verdict of the measurement or of this landing.**

In particular the record states, **with its scope attached and not
detachable from it**:

> Under the repository's presently locked operational definition, the
> target-bearing coefficient is the retained-space coefficient. The
> discarded-space measurement therefore does not numerically redefine that
> repository quantity. **This is a statement about the scope of the registered
> observable — not a conclusion that the discarded components are physically
> irrelevant, and not a conclusion that the retained-space quantity is the
> unique covariant coefficient.**

**The second sentence is why the first is safe to land.** Without it the first
reads as a physical result, and whether the retained-space coefficient is the
physically relevant one is exactly what `H-EXT-01` leaves open and what the
identifiability mismatch of `GAP-B` has not settled.

`C7a` verifies the qualification is present wherever the statement appears.

### 4.5 The prediction

That the pre-registered methodological prediction held, **and that holding is
consistent with the stated cause without establishing it.** The artifact draws
this distinction; the landing record does not weaken it.

### 4.6 Window count, preserved

That the pipeline defines more mass windows than the measurement used, which
those are, and the ground on which the unused one was excluded. **This is not
rewritten as a repository with fewer windows**, and `C8` verifies by reading.

### 4.7 What the measurement does not establish

As the artifact states it, at minimum: one lattice extent; one frozen variant
set; no criterion; and `H-EXT-01` unresolved in either direction.

---

## 5. What this landing does not decide, stated in the record

The record states plainly that the following are **not decided by it**:

- what the result implies for `H-EXT-01`;
- whether `GAP-B`'s mismatches change status;
- whether any correction to the target-bearing coefficient follows;
- why the retained aggregate reverses sign.

**Each is registered under §6 or named under §8. None is answered.**

---

## 6. Records registered, per `M5`

    R-16  **Interpretation is owed.** The measurement bears on `H-EXT-01` and
          on `GAP-B`'s mismatches, and no task has read it against them.
          **Open**; the reading is a separate task and is not performed at
          integration.

    R-17  **The sign reversal, as a question about the extraction.** Why the
          retained aggregate reverses sign between windows is unexplained.
          **Open.** Recorded with the constraint that additional windows are
          not the way to approach it: a window chosen after seeing a reversal
          is an estimator chosen on the evidence it is meant to test.

    R-18  **A method finding.** Two acceptance checks reported false negatives
          because a search term spanned a line break and because backticks
          survived whitespace normalisation. **The line-break case is a
          recorded lesson recurring; the backtick case is new.** Recorded for
          adoption, **not adopted here.**

**A record restating an existing obligation is recorded as such and no count
is incremented.** If `M5` finds no register admits a record, that is recorded
with the scopes read. `C10` accepts both branches.

---

## 7. Acceptance criteria

    C1   The source tip is an ancestor of the new `main` and is a merge parent.
    C2   `main` reached its tip by fast-forward from `caf5111d`.
    C3   Every arriving path's blob is byte-identical to its source blob,
         reported per path.
    C4   §4.1 present with both aggregations shown together for every variant,
         and neither presented as the result.
    C5   §4.2, §4.5 and §4.7 present as the artifact records them.
    C6   §4.3 present, with the sign reversal and the secondary quantity.
    C7   The landing record contains no explanation of the sign reversal, no
         interpretation of the result for `H-EXT-01`, `Q1`, `GAP-A`, `GAP-B`
         or any mismatch, and no criterion or acceptability judgement.
         Verified by reading; **passes on absence**.
    C7a  Wherever the §4.4 statement about the target-bearing coefficient
         appears, its scope qualification appears with it. **A statement that
         the discarded contribution does not change that coefficient, standing
         without its "under the repository's operational definition" scope,
         fails this criterion.** Verified by reading every occurrence.
    C8   §4.6 present; the record does not state that the pipeline defines
         only the windows the measurement used.
    C9   §5's four items present as not decided.
    C10  `R-16` to `R-18` recorded, and discharged per `M5` in one of its
         branches.
    C11  Every figure in the landing record equals `M8`'s reading. Verified by
         comparison, not by assertion.
    C12  `M9`'s Statement SHAs and script blobs unchanged, and `M10` records
         a byte-prefix result for every append-only file the merge product
         modifies, or records that none is modified.
    C13  `M7`'s base-relative list contains no path outside the §0c manifest.
    C14  `M4` recorded with the manner of any emptiness; no silent revert.
    C15  Refs pushed are exactly the integration branch and `refs/heads/main`.

---

## 8. Named, not performed here

1. **The interpretation task** — reading the measurement against `H-EXT-01`
   and `GAP-B`. `R-16`.
2. **The fit-stability question** — a pre-registered task asking why the
   retained aggregate reverses sign, **before any further window is added**.
   `R-17`.
3. **The provenance line** — candidate sources awaiting PI confirmation,
   untouched by this task.

---

## 9. Substring hazards

    band            the variant spread, and a flat band in the operator
                    spectrum
    window          mass windows, and a fit window
    reversal        the sign reversal, and ordinary usage
    aggregate       the two aggregates, and "aggregate" as a verb
    prediction      the methodological prediction, and the frozen physical
                    anchor — **this task transports the first and never the
                    second**
    verdict         the measurement's absence of one, and task verdicts

A check that cannot state its exclusions is performed by reading.

## 10. Criterion satisfiability

`C7` and `C8` have negative limbs satisfiable by reading for absence.

`C10` accepts both branches of `M5`.

`C11` compares two readings of the same artifact and is satisfiable whatever
the values are.

**No criterion is reachable in a case an abort condition covers**, per §2.

---

## 11. Post-execution verification (Researcher)

1. re-run `C1` and confirm the merge parent by id;
2. compare arriving blobs against source blobs;
3. **re-derive both aggregates and both ratios from the per-component
   coefficients independently**, and compare against the landing record —
   `C11` is the check a transported number needs;
4. read for anything barred by `C7` — **the likeliest defect here is a
   sentence that explains the sign reversal in passing**, since it is the most
   conspicuous feature of the result and the record is required to leave it
   open;
4a. read every occurrence of the §4.4 statement for `C7a` — **a scope
   qualification is the first thing lost when a sentence is quoted onward**,
   and the unqualified form reads as a physical result the measurement did not
   produce;
5. confirm `C8` by reading the window count;
6. re-run `M4` independently, including the manner of emptiness;
7. recompute `M9`'s digests;
8. confirm `C15` by `git ls-remote`;
9. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 12. What this task does not establish

It lands a measurement already made, reviewed and independently reproduced. It
produces no new result, moves no gate, and `P2-PHASE-01` is unchanged.

`Q1` remains `INCONCLUSIVE`. `GAP-A` remains closed with its momentum
condition. `GAP-B` remains as its reviewed result left it. `H-EXT-01` remains
`UNESTABLISHED` and `NOT ASSUMED BY RECON-01b`.

**What changes is that a measurement of the target observable's per-component
mass-log content is on `main`, with its instability recorded rather than
resolved.**
