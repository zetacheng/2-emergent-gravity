# P2-SESSION-RULINGS-01 — Land the adjudications that exist only in session

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              GOVERNANCE. Transcription of PI adjudications.

---

## 0. Binding SHA

    Integration base (main at authorship)   46a9c28697fd5b918c6b3d346bd76f8b68ae6d82

If `main` has advanced when execution begins, execution does not proceed.

---

## 0a. Why this task exists

`P2-GAPB-INTEG`'s `S-3` established, by reading authoritative state, that
phrases describing adjudications as made appear in no landed record. **How
many, and what the landed authority on those questions says, are read here
under `M1` and `M2` rather than carried from that report** — a report's count
is evidence about the report.

**The adjudications were made. They were made in session and never landed.**
Under the rule landed by `P2-GAPB-HOUSEKEEP-02` — PI decisions take effect
when issued, their reviews mandatory but non-gating — they are in force. What
is missing is provenance, and a task that relies on an unlanded ruling cannot
show its authority.

**This is the same defect class the `S-2` characterisation finding named**, in
a different medium: a fact that is true, correctly relied upon, and never
established against the record.

## 0b. Two roles, and the record must not merge them

    RATIFIED DISPOSITION
        The Researcher proposed a disposition; the PI agreed. Authority is the
        PI's; origin is the Researcher's. Reversible as a PI matter.

    PI RULING
        A question was returned to the PI and the PI decided it.

**These are recorded distinctly per item.** Collapsing them would misdescribe
who originated what, and the register's value is exactly that attribution.

## 0c. Non-objectives

This task does **not**:

1. act on any adjudication it lands — no re-specification, no re-scoping, no
   claim-reach work, no measurement;
2. adjudicate anything the PI did not decide, or extend a decision beyond its
   stated words;
3. edit `DECISION_LOG.md`'s existing `R-1`–`R-4` entry, which is append-only
   and records those items as open **as of when it was written**;
4. correct the register-census claim that `P2-GAPB-INTEG` measured false —
   that is `R-3`'s subject and its own act;
5. modify any file under `scripts/`.

## 0d. Authorised path manifest — defined once

    P1   the decision file(s) created under §5, and any review artifact
         supplied for them
    P2   every register selected under M3 for the §6 records. **These may
         differ, more than one may be written, and none may be created.**
    P3   this task's own spec, review, landing-record and report artifacts,
         wherever their authorised paths lie, including under specs/

`A6` and `C11` both refer to this manifest and neither restates it.

**Self-check on this specification.** No manifest entry assumes a count; none
says "the register" where more than one may apply; **no number in the prose is
asserted rather than measured** — in particular the number of unlanded
adjudications is measured under `M2`, not stated; and no universal term is
asserted rather than measured.

---

## 1. Measurements

Nothing is carried.

    M1   Read `DECISION_LOG.md`'s existing entry covering `R-1`–`R-4`. Record
         verbatim what it says about their status, with line span.
    M2   **Enumerate, by reading, every adjudication this session's landed
         artifacts describe or rely on that has no entry in `decisions/`.**
         Do not carry a count and do not assume the set equals §5's items.
         If `M2` finds an adjudication §5 does not cover, **`A8` fires**: the
         finding is recorded in the report and returned, and nothing is
         landed. `M2` does not authorise landing a reduced set.
    M3   Read the registers' stated scopes and record, PER RECORD in §6,
         which admits it. Record the answer either way; none may be created.
    M4   **The revert hazard.** For every path present on both `46a9c286` and
         the source at differing blobs, record the blob at the fork point, on
         the source, on `main`, and on the merge product, and record HOW any
         emptiness was established. `M4` intercepted a deletion of four open
         records one landing ago; it is not a formality.
    M5   Locate the `science/*` integration clause; record its line span and
         the merge mode, allowed-ref scope and main-advance rule.
    M6   Test suite on the merge product and at `46a9c286`, in real worktrees.
    M7   `git diff --name-only 46a9c286..<merge product>`, and separately the
         source's contribution against its own fork point. Record both and
         whether they differ.
    M8   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm
         unchanged and neither file modified.
    M9   **Dry-run merge.** Record conflict-free or not, and the conflicting
         paths if any. This is the measurement `A2` evaluates.

---

## 2. Abort conditions

    A1   the base SHA observed differs from §0
    A2   `M9` reports conflicts
    A3   `M6` shows a failure not also present at `46a9c286`
    A4   `M5` finds no governing clause, or one contradicting §4
    A5   `M4` finds the merge product carrying a source blob where `main` had
         advanced
    A6   a path outside the §0d manifest appears in `M7`
    A7   an adjudication in §5 cannot be landed as its stated words give it —
         return to the PI; the executor does not reword an adjudication
    A8   `M2` finds any adjudication outside §5's set. **Execution stops
         before any merge and before any landing.** The finding is recorded
         in the task report and returned to the Researcher; **no §5 decision
         record and no §6 register record is landed.** The scope of a
         retrospective provenance task is the set it was written for, and a
         set found to be incomplete is re-scoped rather than partially
         landed.

---

## 3. Merge mechanics

Governed by the clause located at `M5`. `--no-ff` merge of this task's branch
into a dedicated integration branch; `main` advances by fast-forward only;
push scope is the integration branch and `refs/heads/main` and no other ref.
Prohibited: squash, rebase, force-push, `--force-with-lease`, branch deletion,
history rewrite.

---

## 4. What is landed — the adjudications, as given

Each is recorded with its role per §0b, its stated words, and what it does
**not** decide.

### 4.1 `R-1` — `D-2` retired and split

    ROLE   RATIFIED DISPOSITION. Researcher-proposed, PI-agreed.

> `D-2` is retired as a single item. Its mass part becomes part of the primary
> observable extraction. Its volume part stands separately as a systematic,
> with its priority raised rather than lowered.

**Recorded with the ground given for the split**: that the mass extension
ceased to be a robustness check when `P2-OBS-IDENT-01` established the
extraction level, and that the volume part's priority rose because a
finite-volume figure of merit was measured at the light end of the existing
mass window. **The figure itself is transcribed from where it was measured,
not restated from memory.**

**It does not decide** what the primary extraction's protocol is, nor when the
volume systematic runs.

### 4.2 `R-2` — no re-scope now; `GAP-B` landed as it stood

    ROLE   RATIFIED DISPOSITION. Researcher-proposed, PI-agreed.

> `GAP-B`, `MM-1`, `MM-3` and `MM-5` are not re-scoped now. `GAP-B` is
> integrated as it stands, transport only. The consequence of
> `P2-OBS-IDENT-01` for their reach remains open.

**It does not decide** that their reach is unchanged, nor that it is changed.

### 4.3 `R-3` — both steps, with timing at Researcher discretion

    ROLE   PI RULING.

> The claim-reach enumeration is performed, and the narrowing that may follow
> it is also performed. The first step precedes the second; the second may
> begin once the first is complete, with timing at the Researcher's discretion
> in light of execution results.

**It does not decide** what counts as the authoritative layer, nor which
mechanism a narrowing uses.

### 4.4 `R-4` — measure before deciding

    ROLE   PI RULING.

> Whether `A-EXT-01`'s `Z_axis-TT` and the locked-conventions `Z(m²)` are the
> same object is measured first. Whether any clarification, supersession or
> other record follows is decided after that measurement, not before.

**It does not decide** that a clarification is needed, nor its form.

### 4.5 Provenance, recorded with all four

That each was issued in session and is landed retrospectively; that under the
landed rule they took effect when issued and this landing does not change
their effective date; and that `P2-GAPB-INTEG`'s `S-3` is what established
they were unlanded.

---

## 5. The decision record

Created in `decisions/`, following that directory's landed structure:

    PART 1   the four adjudications of §4, each with its role, stated words,
             what it does not decide, and §4.5's provenance.
    PART 2   the review if supplied; `REVIEW PENDING` if not — which under
             the landed rule does not delay effect.

**One entry or several is determined by the directory's own structure as read,
not chosen here.** If its structure does not admit four adjudications of two
different roles in one entry, that is what the executor records and follows.

---

## 6. Records registered, per `M3`

    R-6   That `DECISION_LOG.md`'s `R-1`–`R-4` entry records those items as
          open, that the entry is append-only and is not edited, and that the
          adjudications now landed in `decisions/` are their disposition.
          **A pointer, not a correction.**

    R-7   `M2` found no unlanded adjudication outside §5's set.

**`R-7` exists only on the continuing branch.** If `M2` finds an extra
adjudication, `A8` fires and nothing is landed, so `R-7` is never written —
the abort condition and this record do not contend for the same case.

---

## 7. Acceptance criteria

    C1   The decision record exists in `decisions/` with Part 1 covering all
         four adjudications and a Part 2 that is a supplied review or
         `REVIEW PENDING`.
    C2   Each adjudication carries its role per §0b, and the two roles are not
         collapsed. Verified by reading.
    C3   Each carries its stated words and its "does not decide" clause.
    C4   §4.5's provenance present, including that effect dates are unchanged.
    C5   The `R-1` ground is transcribed from where the figure was measured,
         with citation. **No figure is restated without its source.**
    C6   `M1` recorded verbatim, and `DECISION_LOG.md`'s existing entry is
         unmodified. Append-only verified by byte prefix.
    C7   `R-6` exists as a pointer and contains no correction of the earlier
         entry.
    C8   `R-7` records the negative census — that `M2` found no unlanded
         adjudication outside §5's set. **This criterion is reached only when
         `A8` did not fire**; there is no branch of it that records an
         `A8` case.
    C9   `M4` recorded with the manner of any emptiness; no silent revert.
    C10  `M8`'s two Statement SHAs unchanged and neither file modified.
    C11  `M7`'s base-relative list contains no path outside the §0d manifest.
    C12  Nothing in the landed text acts on any adjudication — no
         re-specification, re-scoping, narrowing or measurement appears.
         Verified by reading; **passes on absence**.
    C13  Refs pushed are exactly the integration branch and `refs/heads/main`.

---

## 8. Substring hazards

    ruling          PI rulings, the rule set, and "ruled" as ordinary past
                    tense — `S-3` arose from exactly this
    decision        `decisions/`, `DECISION_LOG.md`, and "decided"
    open            an open record, an open question, and "open" as a verb
    R-1..R-7        `R-` labels here, `R-1`/`R-2` of the GAP-A integration,
                    and `R_i` recipe labels in the derivations — three
                    unrelated namespaces
    disposition     the execution-layer sense and ordinary usage

A check that cannot state its exclusions is performed by reading.

## 9. Criterion satisfiability

`C8` is reached only when `A8` did not fire, so it is satisfiable by every
execution that reaches it. An execution that finds an extra adjudication does
not fail `C8`; it never reaches it, and `A8` governs instead.

`C12` is negative and satisfiable by reading for absence.

`C5` is satisfiable because §4.1 requires transcription from a measured
source, which exists in landed state before this task runs.

---

## 10. Post-execution verification (Researcher)

1. re-run the ancestry and fast-forward checks;
2. read Part 1 against §4, checking the two roles are distinct per item —
   **the most likely quiet loss here is a ratified disposition recorded as a
   PI ruling**, which would misattribute origin;
3. confirm `C5`'s figure against its cited source;
4. confirm `DECISION_LOG.md` append-only by byte prefix;
5. re-run `M4` independently, including the manner of emptiness;
6. read for anything barred by `C12`;
7. recompute `M8`'s digests;
8. confirm `C13` by `git ls-remote`;
9. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 11. What this task does not establish

It lands adjudications already in force. It produces no scientific result, no
measurement of any physical quantity, moves no gate, and `P2-PHASE-01` is
unchanged. `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01` are untouched.

**What it changes is that the next task can show its authority.**

---

## 12. Next

1. **`R-4`'s measurement** — whether `Z_axis-TT` and `Z(m²)` are the same
   object. Authorised by §4.4 once landed.
2. **`R-3` step one** — the claim-reach enumeration, which now also covers the
   register-census claim `P2-GAPB-INTEG` measured false.
3. **`R-3` step two**, then **`P2-BETAV-EXTCOMP-01`** protocol freeze.
