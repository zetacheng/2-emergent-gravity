# P2-OBS-IDENT-INTEG — Land the observable identity audit

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              INTEGRATION. Transport only.

---

## 0. Binding SHAs

    Integration base (main at authorship)   f23a0e1e1a24398d082a9597444ff9f750ed38e1
    Source                                  science/obs-ident-01
                                            612817cb (abbreviated)

`M1` reads the full source ref value from the remote and records it. If it
does not begin with the abbreviation above, that is an `A1` return. **No merge
proceeds against an abbreviation.**

If either has advanced when execution begins, execution does not proceed.

---

## 1. Objective

Land the audit. **Add nothing.**

## 1a. Rule 17 governs, and this landing is unusually exposed to it

The reviewed result establishes a relation between two quantities. **A
relation invites consequences**, and several follow — for how an earlier
measurement should be described, for what three open tasks are about, and for
the purpose of a deferred one.

**None of those consequences is drawn here.** They are registered under §6 as
obligations. Rule 17 forbids this task adding an epistemic classification the
reviewed result does not carry, and a consequence drawn from a result is not
the result.

## 1b. §12 of the source specification, and how the landing must read it

The source specification's §12 says the task produces "no physical result".
**That means no new physical measurement.** It does not mean the outcome is
without consequence, and the landing record must not describe it that way.
`C8` checks this.

## 1c. Non-objectives

This task does **not**:

1. draw any consequence for `GAP-B`, `MM-1`, `MM-3`, `MM-5` or `D-2`;
2. amend, narrow, annotate or reword any landed description of `EXT-01`'s
   measurement, in `EXT-01`'s own artifact or in any later one. **Those are
   landed reviewed records**; whether any needs narrowing is an obligation,
   not an edit;
3. resolve the ambiguity `M5` found in `A-EXT-01`. Resolving it would require
   a new exact statement, which would break its `Statement SHA` and void its
   pinned review;
4. integrate `science/gapb-bridge-01`, which is separate and outstanding;
5. perform any measurement, or specify one beyond what the reviewed result
   already specifies;
6. modify any file under `scripts/`;
7. modify any file arriving from the source.

## 1d. Authorised path manifest — defined once

    P1   every path arriving from the source by the merge
    P2   every register selected under M5 for the §6 records. **These may
         differ between records, more than one may be written, and none may
         be created.**
    P3   this task's own spec, review, landing-record and report artifacts,
         wherever their authorised paths lie, including under specs/

`A6` and `C12` both refer to this manifest and neither restates it.

**Self-check on this specification.** No manifest entry assumes a count; none
says "the register" where more than one may apply; no number in the prose is
asserted rather than measured; no universal term — sole, only, every, no
other — is asserted rather than measured. Both classes have produced defects
in this line.

---

## 2. Measurements

Nothing is carried, including from the source's execution report and from the
Researcher's verification of it.

    M1   Read the full source ref value from the remote. Record it.
    M2   Test suite on the merge product and at `f23a0e1e`, in real worktrees.
    M3   Dry-run merge: conflict-free or not; conflicting paths if any.
    M4   **The revert hazard.** For every path present on both `f23a0e1e` and
         the source at differing blobs, record the blob at the fork point, on
         the source, on `main`, and on the merge product. **Measure the set
         even if it is expected to be empty**; an empty set established by
         comparison is evidence, one inferred from a short fork distance is
         not. A merge product carrying a source blob where `main` had advanced
         fires `A5`.
    M5   Read the registers' stated scopes and record, PER RECORD in §6,
         which admits it. Record the answer either way; **none may be
         created**.
    M6   Locate the `science/*` integration clause; record its line span and
         the merge mode, allowed-ref scope and main-advance rule.
    M7   `git diff --name-only f23a0e1e..<merge product>`, and separately the
         source's contribution measured against its own fork point. Record
         both and whether they differ.
    M8   Transcribe from the reviewed result: the outcome; the definitional
         location it establishes for the observable; the two extraction steps
         with their code citations; which step `EXT-01` performed; and its
         `D3` statement of what differs.
    M9   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm
         unchanged and neither file modified.

---

## 3. Abort conditions

    A1   a SHA observed differs from §0, or `M1` returns a value not
         beginning with the abbreviation §0 records
    A2   `M3` reports conflicts
    A3   `M2` shows a failure not also present at `f23a0e1e`
    A4   `M6` finds no governing clause, or one contradicting §4
    A5   `M4` finds the merge product carrying a source blob where `main` had
         advanced
    A6   a path outside the §1d manifest appears in `M7`
    A7   landing any item would require editing `A-EXT-01`, `H-EXT-01`, any
         file arriving from the source, or any landed artifact describing
         `EXT-01`'s measurement

---

## 4. Merge mechanics

Governed by the clause located at `M6`. `--no-ff` merge of the source into a
dedicated integration branch, preserving the source tip as a merge parent;
`main` advances by fast-forward only; push scope is the integration branch and
`refs/heads/main` and no other ref; the source branch does not move.
Prohibited: squash, rebase, force-push, `--force-with-lease`, branch deletion,
history rewrite.

---

## 5. Landing record — required content

### 5.1 The outcome and the relation

`PROXY ONLY`, with `M8`'s definitional location and both extraction steps.
**The relation is stated as the reviewed result states it** — that the
difference is the mass treatment, with what is common recorded alongside what
differs.

### 5.2 What `EXT-01` measured, and what it did not

That `EXT-01` performed the first extraction step at one mass, and that this
is the input to the fit producing the target coefficient rather than the
coefficient itself. **Established against the code by the reviewed result**,
and transported as such.

### 5.3 What this does not establish — required

- **`EXT-01` is not invalidated.** Its execution, pre-registration and
  independent reproduction stand. The question was what its numbers bear on.
- **Nothing is concluded about whether the discarded external space matters
  for the target coefficient.** The reviewed result specifies what measuring
  that would require and does not perform it.
- **`A-EXT-01` is unchanged** and its recorded silence is not read either way.
- `Q1`, `GAP-A`, `GAP-B` and `H-EXT-01` are unchanged in status.

### 5.4 The `A-EXT-01` finding, transported not resolved

That its exact statement does not disambiguate between the two extractions,
recorded as the reviewed result records it, **with the statement unaltered**
and no reading supplied.

### 5.5 The negative existence finding

That no per-component instance of the target coefficient was found, with the
reviewed result's own exclusion stated. **A negative existence finding is
transported with its search extent or not at all**, since without the extent
it is not checkable.

### 5.6 The compliance self-correction

That the reviewed result's own first draft of a compliance paragraph placed
the values it was checking for into the document the check covers, and that
this was corrected before commit. **Transported because a compliance check
that becomes a violation source is a reusable finding**, not because it
reflects on the executor.

---

## 6. Records registered, per `M5`

Registered as open items. **None is answered here.**

    R-1   `D-2`'s purpose. The source specification made re-specification
          conditional on the audit's outcome; the condition is now met by
          measurement. Whether `D-2` is re-specified, and as what, is
          undecided.

    R-2   The scope of `GAP-B`, `MM-1`, `MM-3` and `MM-5`, each of which
          reasons about the object the audit has now related to the target
          observable. Undecided.

    R-3   Whether any landed description of `EXT-01`'s measurement requires
          narrowing, and if so by what mechanism, given that landed reviewed
          records are not edited in place. Undecided.

    R-4   The ambiguity in `A-EXT-01`, and whether a definitional convention
          silent at its own load-bearing point requires supersession — which
          would need a new statement and a new review.

**If a record restates an existing obligation, it is recorded as such and the
homeless-obligation count is not incremented.** If `M5` finds no register
whose stated scope admits a record, that is recorded with the scopes read.
`C9` accepts both branches.

---

## 7. Acceptance criteria

    C1   The source tip is an ancestor of the new `main` and is a merge
         parent.
    C2   `main` reached its tip by fast-forward from `f23a0e1e`.
    C3   Every arriving path's blob is byte-identical to its source blob,
         reported per path.
    C4   `M4` recorded, with the set's emptiness or contents established by
         comparison; no silent revert.
    C5   `§5.1` and `§5.2` present, with `M8`'s citations.
    C6   All four items of `§5.3` present.
    C7   `§5.4`, `§5.5` and `§5.6` present, `§5.5` with its search extent.
    C8   The landing record contains no statement that the outcome is without
         consequence, immaterial, or merely procedural, and no statement
         drawing a consequence for `GAP-B`, `MM-1`, `MM-3`, `MM-5` or `D-2`
         beyond registering it under §6. Verified by reading; **passes on
         absence**.
    C9   `R-1` to `R-4` discharged per `M5`, in one of its branches.
    C10  No landed artifact describing `EXT-01`'s measurement is modified.
         Verified by diff.
    C11  `M9`'s two Statement SHAs unchanged and neither file modified.
    C12  `M7`'s base-relative list contains no path outside the §1d manifest.
    C13  `M7` records both measurements and whether they differ.
    C14  Refs pushed are exactly the integration branch and `refs/heads/main`.

---

## 8. Substring hazards

    observable      this task's sense, the manuscript's channel sense, and
                    ordinary prose
    coefficient     the q² coefficient, the mass-log coefficient, a
                    projector's trace coefficient, and recipe coefficients —
                    the distinction between the first two is the finding
    proxy           matches "proxy" in unrelated governance prose
    extraction      matches "extract" in code prose
    step            matches the two extraction steps and ordinary usage
    D-2 / D3        a deferred item and a determination step, unrelated

A check that cannot state its exclusions is performed by reading.

## 9. Criterion satisfiability

`C8` is negative and satisfiable by reading for absence; it does not require
the landing record to declare an absence.

`C9` accepts both branches of `M5`, so a correct execution passes whether or
not a register admits a record.

`C3` and `C11` compare values that exist before the merge.

---

## 10. Post-execution verification (Researcher)

1. re-run `C1`, confirm the merge parent by id;
2. compare arriving blobs against source blobs — the check that the
   integration added nothing;
3. re-run `M4` independently, including confirming an empty set by
   comparison;
4. read for statements barred by `C8` — **this landing's most likely defect
   is a consequence drawn in passing**, not a wrong measurement;
5. confirm `C10` by diffing the artifacts that describe `EXT-01`;
6. recompute `M9`'s digests;
7. confirm `C14` by `git ls-remote`;
8. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 11. What this task does not establish

It lands an audit already performed, reviewed and verified. It produces no new
result and no measurement. No gate moves; `P2-PHASE-01` is unchanged.

**It is not without consequence** — §6 registers four — but every consequence
is registered as open, and none is drawn.

---

## 12. Outstanding after this task

1. **`science/gapb-bridge-01`** — unintegrated. Its findings concern the
   object this audit has related to the target observable; **that relation is
   not written into them**, and how they are read is `R-2`.
2. **The per-component extraction the reviewed result specifies** — the
   measurement that would answer what `EXT-01`'s numbers could not. Not
   opened here.
3. **`O-1`, `O-2`, `R-2` of earlier tasks**, and the obligations register that
   would hold them.
4. **The `S-2` characterisation rule**, not yet landed.
5. **`CONVENTIONS.md`'s hard-coded register tally**, stale and reported
   repeatedly without an owner.
