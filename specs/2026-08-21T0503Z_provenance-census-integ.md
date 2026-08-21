# P2-PROVENANCE-CENSUS-INTEG — Land the census, and ratify the criterion it turned on

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              INTEGRATION, plus one PI decision landed alongside.

---

## 0. Binding SHAs

    Integration base (main at authorship)   d9f676a4b7d0a851c82177f8e14cba1af467b06f
    Source                                  science/provenance-census-01
                                            f69c1a1d (abbreviated)

`M1` reads the full source ref value from the remote. If it does not begin
with the abbreviation above, that is an `A1` return. **No merge proceeds
against an abbreviation.**

---

## 0a. Two parts, two authorities — read before executing

    §4   TRANSPORT of the reviewed census. Rule 17 governs: nothing is
         reclassified, recomputed, or re-scoped.

    §5   A PI RULING issued in session after the census executed, and landed
         here retrospectively. It **ratifies the criterion the executor
         applied** and changes no census value.

**§5 is not rule 17 territory, and the record must say why.** The executor
applied the criterion, stated it in the artifact for rejection, and computed
the result under it. The PI has now ruled it correct. **A ratification of an
applied criterion reclassifies nothing**; had the PI ruled the other way, the
census would require recomputation and this task would not be the vehicle.

## 0b. Non-objectives

This task does **not**:

1. recompute, re-scope, or re-classify any census member;
2. reconstruct, draft, or land any adjudication the census found unrecorded —
   **that is a later task and it needs PI confirmation per adjudication**;
3. place, register, or file any of those adjudications anywhere;
4. resolve the provenance-tier question the census surfaced;
5. amend any citation the census enumerates;
6. modify any file under `scripts/` other than by the merge itself;
7. state any census figure. **Every count in the landing record is read from
   the artifact under `M8`**, not carried from any report.

## 0c. Authorised path manifest — defined once

    P1   every path arriving from the source by the merge
    P2   the decision file created under §5, and any review artifact supplied
         for it
    P3   every register selected under M5 for the §6 records. **These may
         differ, more than one may be written, and none may be created.**
    P4   this task's own spec, review, landing-record and report artifacts,
         wherever their authorised paths lie, including under specs/

`A6` and `C13` both refer to this manifest and neither restates it.

**Self-check on this specification**, against the defect classes this line has
produced: no asserted count; no unmeasured universal; no dangling `M`/`A`/`C`
reference; **no predeclared set** — the census members are the artifact's, read
under `M8`; no acceptance criterion covering a case an abort condition covers;
self-referential counts checked against this document's own content.

---

## 1. Measurements

Nothing is carried, including from the census execution report.

    M1   Read the full source ref value from the remote. Record it.
    M2   Test suite on the merge product and at `d9f676a4`, in real worktrees.
         **Unshallow before running.** A shallow clone was measured to
         produce governance-test failures that are not defects; record the
         clone depth used.
    M3   Dry-run merge: conflict-free or not; conflicting paths if any.
    M4   **The revert hazard.** For every path present on both `d9f676a4` and
         the source at differing blobs, record the blob at the fork point, on
         the source, on `main`, and on the merge product, and record HOW any
         emptiness was established.
    M5   Read the registers' stated scopes and record, PER RECORD in §6,
         which admits it. Record the answer either way; none may be created.
    M6   Locate the `science/*` integration clause; record its line span and
         the merge mode, allowed-ref scope and main-advance rule.
    M7   `git diff --name-only d9f676a4..<merge product>`, and separately the
         source's contribution against its own fork point. Record both and
         whether they differ.
    M8   **From the landed census artifact**, read and record: the cardinality
         of each set; the number of distinct adjudications the census
         identifies and how many fall in each provenance state it distinguishes;
         and the criterion the executor applied under `S-6`, in its own words.
         **Read, do not carry.**
    M9   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm
         unchanged and neither file modified.
    M10  **Append-only verification.** For every file the merge product
         modifies that declares itself append-only, record whether the base
         blob's bytes are a prefix of the merge product's, and the byte counts
         compared. This is the measurement `C12` evaluates.

---

## 2. Abort conditions

    A1   the base or source SHA observed differs from §0, or `M1` returns a
         value not beginning with §0's abbreviation
    A2   `M3` reports conflicts
    A3   `M2` shows a failure not also present at `d9f676a4` **on an
         unshallowed clone**
    A4   `M6` finds no governing clause, or one contradicting §4
    A5   `M4` finds the merge product carrying a source blob where `main` had
         advanced
    A6   a path outside the §0c manifest appears in `M7`
    A7   `M8` finds the criterion recorded in the artifact differs in substance
         from the one §5 ratifies. **Stop before any merge and any landing**,
         and return both texts. A ratification of a criterion the executor did
         not apply would silently change the census result.

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

### 4.1 The result, as measured

`M8`'s cardinalities and the distinct-adjudication figure, **with the
distinction between passages and adjudications stated in the same place**.

**A passage count is not an adjudication count.** The record states which
figure is the action set for any later task, and that acting per passage would
record one adjudication several times.

### 4.2 The provenance states the census distinguishes

As the artifact records them, **including the state the census surfaced that
no rule covers** — adjudications a register knows to have been ruled without
carrying their words. **Recorded as the artifact records it, in its own
terms**; whether the model should be revised is §6's, not this record's.

### 4.3 What `S_missing` means, and what it does not

Recorded verbatim in the landing record, because the misreading is the one
that would do damage:

> `S_missing` means **no landed provenance record was found in the searched
> scope**. It does **not** mean the content is unknown. Where a specification
> transcribes an adjudication's words, those words are **evidence of the
> content and may serve as candidate source material** — but they are a single
> source, unverified against any other, and a transcription of this kind has
> already been measured to diverge from its source. **They therefore require
> PI confirmation before becoming a record**, by the same route the
> adjudication-source document took.

**Any later task that reconstructs an adjudication from citations instead of
confirming a candidate source is doing what `A7` of that route forbids.**

### 4.4 The method findings, transported

The census's own recorded method errors, **including the set-relation check
that passed while wrong**. Transported because the failure is reusable: a
parser that silently dropped one set left every set identity trivially true.

### 4.5 What the census does not establish

As the artifact states it, at minimum: that the result is a measurement over
the searched scope and not over the repository; that a member of `S_missing`
may have had authority whose record did not survive; and that no effective
date is determined.

---

## 5. The PI decision, landed alongside

Created in `decisions/`, following that directory's landed structure.

### 5.1 Part 1 — the ruling, as issued

Landed verbatim, in the language it was issued in:

> 我裁定：一份 specification 轉錄一條裁決嘅文字，係該裁決內容嘅證據，但本身唔構成
> 該裁決嘅 canonical landed provenance record。

Recorded alongside it, as a working translation and **identified as such**,
not as the ruling:

> A specification that transcribes the words of an adjudication is evidence of
> that adjudication's content, but does not itself constitute that
> adjudication's canonical landed provenance record.

**The issued text governs.** The translation is provided because the
repository's records are otherwise in English; **it is not the ruling and is
not to be cited as it.**

### 5.2 Part 1 — the two layers, kept apart

**The ruling is about records, not about content.** The record states both:

    FACT LAYER          the specification does carry the adjudication's
                        words. The content is in the repository and is not
                        lost.

    GOVERNANCE LAYER    that text is not the canonical provenance record of
                        the adjudication.

**Collapsing these would misstate the ruling in either direction** — as a
claim that the content is missing, or as a claim that a transcription
suffices.

### 5.3 Part 1 — the measured ground

The ruling rests on measurement, not on convention, and the record says so:

- a landed block labelled as reproducing what was ruled **was measured and
  found to diverge from its source** — a qualifier inserted, a directive
  sentence absent;
- that transcription was single-source and unverified against any other at the
  time it was made;
- a later task built a separate record for a document whose items an earlier
  specification had already transcribed. **This is consistent with, and
  operationally demonstrates, the distinction** — the transcription was not
  treated as sufficient canonical provenance. **Whether that was its stated
  motive is established by citation at execution, not asserted here.**

**The citations for each are read at execution and recorded**; this
specification names no line numbers, having produced citation defects by doing
so before.

### 5.4 Part 1 — effect and scope

That the ruling ratifies the criterion the census executor applied and
**changes no census value**; that it takes effect when issued, per the landed
rule, and that this landing does not alter that effective date; and that had
it gone the other way, the census would require recomputation rather than
ratification.

**Issuance provenance, recorded rather than smoothed:** the ruling was issued
in session, in response to a request that named the consequence of each
possible answer, and is landed here retrospectively. An earlier draft of this
specification described it as issued **before it had been**; that draft was
caught in review and the description is corrected here rather than dropped.

### 5.5 Part 2 — the review

The review if supplied; `REVIEW PENDING` if not, which does not delay effect.
**The executor does not author it.**

---

## 6. Records registered, per `M5`

    R-13  The provenance-tier question. The census distinguishes more states
          than the binary the measurement used. **The binary result is not
          revised**, and whether the model should be is open.

    R-14  The citation-form finding: that numbered and named citation forms
          were each measured non-unique, and that at least one citation
          resolves to nothing. **Open**; no citation is amended and no rule
          is proposed here.

    R-15  A method rule, from §4.4: **set identities all evaluating true does
          not establish that the parser is correct.** A verifier that drops a
          set makes its identities trivially true. Census-class verification
          requires cardinality sanity, an independent parser, or sentinel
          cases — **recorded as a finding for adoption, not adopted here.**

**A record restating an existing obligation is recorded as such and no count
is incremented.** If `M5` finds no register admits a record, that is recorded
with the scopes read. `C10` accepts both branches.

---

## 7. Acceptance criteria

    C1   The source tip is an ancestor of the new `main` and is a merge parent.
    C2   `main` reached its tip by fast-forward from `d9f676a4`.
    C3   Every arriving path's blob is byte-identical to its source blob,
         reported per path.
    C4   §4.1 present, with the passage-versus-adjudication distinction and
         the statement of which is the action set.
    C5   §4.2 and §4.4 present, the latter including the check that passed
         while wrong.
    C6   §4.3 present **verbatim**, including the sentence that a
         reconstruction from citations is forbidden.
    C7   §4.5 present with each of its named items.
    C8   The §5 decision record exists with Part 1 and a Part 2 that is a
         supplied review or `REVIEW PENDING`.
    C9   §5.2's two layers appear and are not collapsed; §5.3's grounds appear
         with citations read at execution; §5.4's effect statement appears.
    C10  `R-13` to `R-15` recorded, and discharged per `M5` in one of its
         branches.
    C11  No census value in the landing record differs from `M8`'s reading.
         Verified by comparison, not by assertion.
    C12  `M9`'s two Statement SHAs unchanged, and `M10` records a byte-prefix
         result for every append-only file the merge product modifies.
    C13  `M7`'s base-relative list contains no path outside the §0c manifest.
    C14  `M4` recorded with the manner of any emptiness; no silent revert.
    C15  Refs pushed are exactly the integration branch and `refs/heads/main`.

---

## 8. Substring hazards

    record          the provenance record, a census row, and "record" as a verb
    passage         census passages and prose passages
    adjudication    the act, the document, the census class
    transcription   the source transcription, and a specification's
                    transcription of a ruling — §5 turns on the second
    landed          landed on main, and "landed record" as the census's term
    criterion       the `S-6` criterion, and acceptance criteria

A check that cannot state its exclusions is performed by reading.

## 9. Criterion satisfiability

`C6` requires a verbatim block this specification supplies, so both sides
exist before the check runs.

`C10` accepts both branches of `M5`.

`C11` compares two readings of the same artifact and is satisfiable whatever
the values are.

**No criterion is reachable in a case an abort condition covers**, and `A7`'s
stop is stated in `A7`.

---

## 10. Post-execution verification (Researcher)

1. re-run `C1` and confirm the merge parent by id;
2. compare arriving blobs against source blobs;
3. **re-derive the set relations with an independently written parser** —
   §4.4's finding is that the executor's own check passed while wrong, and
   repeating its method would repeat its blind spot;
4. **spot-check for omission using a search form the census did not use**, and
   record the form;
5. read §4.3 for verbatim reproduction, `§5.2` for the two layers, and
   `§5.1` for whether the translation is anywhere presented as the ruling —
   **a translation cited as the ruling would be the same substitution this
   ruling is about**;
6. re-run `M4` independently, including the manner of emptiness;
7. recompute `M9`'s digests;
8. confirm `C15` by `git ls-remote`;
9. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 11. What this task does not establish

It lands a measurement and ratifies the criterion under which it was made. It
produces no scientific result, no `β_V`, moves no gate, and `P2-PHASE-01` is
unchanged.

**It does not establish that any unrecorded adjudication lacked authority** —
only that no landed record of it was found in the searched scope.

---

## 12. Next

1. **`P2-SESSION-RULINGS-02`** — over the distinct adjudications the census
   froze, **not over the passages**, each taking the candidate-source route
   with PI confirmation.
2. **`R-4`'s measurement**, then **`R-3`**, then the extraction protocol
   freeze, whose four contested elements go to the PI item by item.
