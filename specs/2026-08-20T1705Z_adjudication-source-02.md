# P2-ADJUDICATION-SOURCE-02 — Land the adjudication document, with the divergence ruled

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              GOVERNANCE. Retrospective provenance landing.
    Supersedes        P2-ADJUDICATION-SOURCE-01, stopped A8 on the item-2
                      divergence. Its branch is preserved and MUST NOT be
                      integrated.

---

## 0. Binding SHAs

    Integration base (main at authorship)   46a9c28697fd5b918c6b3d346bd76f8b68ae6d82
    Superseded branch, not integrated       science/adjudication-source-01
                                            e3bbc7fb (abbreviated)

If `main` has advanced when execution begins, execution does not proceed.

**The source document and its review are supplied to the executor**, as they
were to the predecessor. `A7` still governs their absence.

---

## 0a. What changed, and what did not

The predecessor stopped correctly. Its `A8` found that a landed block labelled
`registered verbatim` differs from the source in what its item decides, and it
refused to choose a side.

**The PI has now determined the questions that stop raised.** They are
recorded in §5 and §6. **Nothing about the predecessor's finding is reversed**:
the divergence is real, the **exact original historical wording** remains
undeterminable, and this task does not decide which side was issued.
**What §5 does decide is which wording governs the record being created**, at
a different level from that question.

**What this task adds is a disposition for a divergence that is now known.**
`A8` continues to fire on any divergence §5 does not cover.

## 0b. Non-objectives

This task does **not**:

1. re-adjudicate any item of the document, or alter its stated words;
2. decide which text of the divergent item was originally issued — **§5
   records that this is not determinable**;
3. rewrite any landed quoted block;
4. act on any item beyond what §5 and §6 direct;
5. re-open items already landed and found faithful;
6. land `R-1`–`R-4`, or perform the provenance census;
7. integrate the superseded branch;
8. modify any file under `scripts/`;
9. edit any append-only file's history.

## 0c. Authorised path manifest — defined once

    P1   the decision record(s) created under §4, and any review artifact
         supplied for them
    P2   the register file carrying the entry §5 corrects, for the ADDITIVE
         correction §5.3 specifies
    P3   every register selected under M4 for the §7 records. **These may
         differ, more than one may be written, and none may be created.**
    P4   this task's own spec, review, landing-record and report artifacts,
         wherever their authorised paths lie, including under specs/

`A6` and `C14` both refer to this manifest and neither restates it.

**Self-check on this specification**, against the defect classes this line has
produced:

    asserted count        no number in the prose is asserted rather than
                          measured; item counts, landed-item counts and
                          citing-artifact counts are all read under §1
    unmeasured universal  no "sole", "only", "every", "no other" is asserted
                          rather than measured
    dangling reference    every `M`, `A`, `C` and `§` reference resolves to
                          something this document defines
    predeclared set       §4 does not enumerate the document's items; `M1`
                          establishes the set
    contested control     no acceptance criterion covers a case an abort
                          condition covers; `A8`'s exclusion is stated in
                          `A8` itself, not in a criterion

---

## 1. Measurements

Nothing is carried — **including from the predecessor's report**, whose `M1`,
`M2` and `M3` results are a prior execution's observations and are not targets.

    M1   **Read the supplied source document** and record: how many items it
         contains, each item's number, and each item's stated words. **Do not
         assume a count.** Record separately any block that is not numbered,
         and **do not classify it as an item or as not an item** — §7
         registers that question.

    M2   For each item `M1` records, determine from landed state whether it
         has been landed, and if so by which task and into which file, with
         line citations. For each landed item, compare its landed words with
         `M1`'s. Record: faithful, divergent, or not determinable.
         **For any divergence, record both texts in full.**

    M3   Enumerate the landed artifacts that cite or rely on any item, by
         reading, with citations. **Do not carry a count.**

    M4   Read the registers' stated scopes and record, PER RECORD in §7,
         which admits it. Record the answer either way; none may be created.

    M5   Read the conventions governing the register file §5.3 corrects, and
         record whether an additive correction beneath an existing entry is
         permitted, and in what form. **If it is not permitted, `A9` fires.**

    M6   **The revert hazard.** For every path present on both `46a9c286` and
         this task's branch at differing blobs, record the blob at the fork
         point, on the branch, on `main`, and on the merge product, and
         record HOW any emptiness was established.

    M7   Locate the `science/*` integration clause; record its line span and
         the merge mode, allowed-ref scope and main-advance rule.

    M8   Test suite on the merge product and at `46a9c286`, in real worktrees.

    M9   `git diff --name-only 46a9c286..<merge product>`, and separately this
         task's contribution against its own fork point. Record both and
         whether they differ.

    M10  **Dry-run merge.** Conflict-free or not; conflicting paths if any.
         This is the measurement `A2` evaluates.

    M11  Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm
         unchanged and neither file modified.

---

## 2. Abort conditions

    A1   the base SHA observed differs from §0
    A2   `M10` reports conflicts
    A3   `M8` shows a failure not also present at `46a9c286`
    A4   `M7` finds no governing clause, or one contradicting §3
    A5   `M6` finds the merge product carrying a branch blob where `main` had
         advanced
    A6   a path outside the §0c manifest appears in `M9`
    A7   the source document is not supplied. **Stop before any merge and any
         landing.** A retrospective provenance record is not built from the
         citations that lack it.
    A8   `M2` finds a divergence between a landed item's words and `M1`'s,
         **other than the divergence §5 identifies**. Stop before any merge
         and any landing, and return both texts.

         **The §5 divergence is excluded because the PI has ruled on it**, and
         the exclusion is stated here rather than in a criterion so that no
         criterion contends with this condition. If `M2` finds the §5
         divergence but its texts differ from those §5 records, **that is a
         different divergence and `A8` fires**.
    A9   `M5` finds an additive correction is not permitted in the register
         file §5.3 names. Stop and return; the executor does not select an
         alternative mechanism.

**Every condition here stops execution.** No acceptance criterion covers a
case any of them covers.

---

## 3. Merge mechanics

Governed by the clause located at `M7`. `--no-ff` merge of this task's branch
into a dedicated integration branch; `main` advances by fast-forward only;
push scope is the integration branch and `refs/heads/main` and no other ref.
Prohibited: squash, rebase, force-push, `--force-with-lease`, branch deletion,
history rewrite. **The superseded branch does not move and is not merged.**

---

## 4. The decision record for the source

Created in `decisions/`, following that directory's landed structure.

### 4.1 Part 1 — the document

Every item `M1` records, **reproduced in its stated words**, with its number
as the document gives it, and any unnumbered block recorded as `M1` recorded
it. **This specification lists no items**; `C2` checks Part 1's set equals
`M1`'s.

### 4.2 Part 1 — status and grounds

    RETROSPECTIVELY RECORDED AND PI-CONFIRMED AT LANDING
    — ORIGINAL ISSUANCE NOT ESTABLISHED

with, in the record itself: that the document was acted on before any record
of it existed; that its original issuance is **not established by the
surviving record**; that the PI confirms its substantive content at landing;
that this record **alters no item's effective date and makes no finding about
what any effective date was**; and that items already landed from it were in
force on a citation whose source was unlanded.

**Both errors are barred, and the record says so:**

    FORWARD    recording the document as adjudicated by the PI at issuance
    BACKWARD   recording that items not previously landed had no authority
               until now, or take effect only now

**Absence of surviving provenance is not evidence of absence of historical
authorisation**, and this task has measured only the former.

### 4.3 Part 1 — what is already in force, per `M2`

For each landed item: which task landed it, into which file, and that **its
effective date is unchanged by this record**.

For each unlanded item: that its content is confirmed by the PI at this
landing, and that **the record makes no finding about its effective date in
either direction**.

### 4.4 Part 1 — the points the PI addressed at landing

Recorded with the item they belong to, not as separate items:

- The bounded re-scope of components 5 and 9 is **ratified retrospectively**.
  The record states the ordering explicitly — **executed, then reviewed, then
  independently verified, then retrospectively ratified** — and states that
  the historical timing and provenance of the original authorisation are **not
  established by the surviving record**. It represents neither that this
  record existed before landing nor that no earlier authorisation existed.
- The statement tying that re-scope to the changed status of the projection
  question is recorded **as part of that item's own reasoning**, not as a
  separate adjudication.

### 4.5 Part 2 — the review

The review if supplied; `REVIEW PENDING` if not, which under the landed rule
does not delay effect. **The executor does not author it.**

---

## 5. The item-2 divergence — PI determination

### 5.1 Three determinations, at three different levels

**These are distinct questions and all three answers hold together.** An
earlier draft of this specification collapsed the first into a claim that
neither text has authority over the other; **that was not ruled**, and it left
§4.1 without a ground for using the source's wording at all.

    LEVEL 1 — HISTORICAL EXACT TEXT
    NOT DETERMINED   The exact byte-level wording of the original session
                     cannot be established. No stored transcript exists, the
                     transcription asserts no byte-identity, and the landed
                     block's own label cannot be taken as evidence of the
                     source it claims to reproduce.

    LEVEL 2 — RETROSPECTIVE SOURCE OF RECORD
    DETERMINED       For the retrospective provenance record this task
                     creates, **the PI-confirmed source wording governs the
                     substantive adjudication content of the divergent item.**
                     This is what gives §4.1 its ground.
                     **It asserts nothing about historical bytes or
                     formatting**, which Level 1 leaves open.

    LEVEL 3 — FORWARD OPERATIVE SCOPE
    DETERMINED       The open protection question applies to review-bound
                     statements generally, not only to those carrying a
                     particular field.

**Level 2 is a determination about which text is authoritative for a record
being made now. Level 1 is a question about what happened. Neither answers the
other**, and the record must not let one be read as the other.

### 5.2 The ground for the scope determination, which is forward not archaeological

**The scope determination does not rest on which text was issued.** It rests
on measurement made since: landed specifications under `specs/` were found to
carry live review bindings, and a single specification's digest was found
pinned by several documents. `M3` of `P2-GOV-HOUSEKEEP-02` and `M6` of
`P2-GAPA-INTEG` are the measurements; **their values are read at execution,
not restated here**.

The landed entry's own evidence section already concedes the point, in a
sentence the qualifier is what makes necessary. **The determination removes
the need for that workaround rather than adding to it.**

### 5.3 How the correction is made

**Additively, beneath the existing entry, per `M5`.** The quoted block is
**not rewritten**: neither text is a **byte-level** authority over the other,
and rewriting the landed quotation would assert that one reproduces the
original bytes. **Level 2 settles which wording governs the record being made;
it does not license editing a landed quotation.**

The correction records:

1. both texts in full, as `M2` measured them;
2. that the exact original historical wording is undeterminable, and why;
3. **that for this retrospective record the PI-confirmed source wording
   governs the substantive adjudication content of the item, and that this
   asserts neither that the source reproduces the original bytes nor that it
   reproduces the original formatting**;
4. that the label on the existing block — asserting the quotation reproduces
   what was ruled — **is not supported by the evidence**, and that the block
   is retained as landed rather than relabelled in place;
5. the forward operative scope determination of §5.1, with §5.2's ground;
6. that the entry's disposition is otherwise unchanged.

**No landed quoted text is altered.** `C7` verifies by diff.

---

## 6. Item 7 — the departure, ratified

The item directed that certain wording corrections be applied. The Researcher
instead recorded them as errata and did not apply them, stated the departure
in the specification, and the Reviewer approved that specification.

**The PI had not confirmed the departure.** The Researcher flagged it to the
Reviewer and not to the PI, and Reviewer approval is not PI ratification.

**The PI now ratifies the errata treatment.** The record states: what the item
directed; what was done instead; that the departure was reviewed but not
PI-confirmed at the time; and that it is ratified at this landing, **with no
representation that it was authorised earlier**.

---

## 7. Records registered, per `M4`

    R-8   `M3`'s enumeration of citing artifacts. A finding. **No citation is
          edited**, and whether any needs amendment is not decided here.

    R-9   That one item's substantive question has since changed — the item
          concerning whether a deferred extension is a measurement or a
          prerequisite was framed before the observable-identity finding.
          **The item is landed in its stated words regardless**, and that the
          question has moved is recorded beside it, undecided.

    R-10  Whether any item's effective date should be fixed, and to what.
          **Open.** §4.2 records that the surviving evidence settles it in
          neither direction.

    R-11  Whether the unnumbered block `M1` records is an item of the
          document. **Open**, and not assumed either way.

    R-12  The labelling practice: that a block asserting it reproduces what
          was ruled was found not to. **Whether other such labels hold is a
          question for the provenance census**, and is not answered here.

**A record restating an existing obligation is recorded as such and no count
is incremented.** If `M4` finds no register admits a record, that is recorded
with the scopes read. `C11` accepts both branches.

---

## 8. Acceptance criteria

    C1   The decision record exists in `decisions/` with Part 1 and a Part 2
         that is a supplied review or `REVIEW PENDING`.
    C2   Part 1's item set equals `M1`'s, item for item, in stated words.
    C3   §4.2's status appears with each of its statements, and the record
         asserts NEITHER of §4.2's two barred propositions. **Both negative
         limbs pass on absence.**
    C4   §4.3 present for every item in whichever of its two forms `M2`
         assigns.
    C5   §4.4's two entries present, the first stating the ordering
         explicitly as four steps in sequence.
    C6   The §5.3 correction exists with all six of its recorded elements.
    C7   No landed quoted block is altered. Verified by diff over the register
         file and over every artifact `M3` enumerates.
    C8   §5.1's three levels appear, each labelled, with Level 1 recorded as
         `NOT DETERMINED` and not resolved, and Level 2 recorded as the ground
         for §4.1's use of the source wording. **The record must not state
         that neither text has authority over the other** — that is a Level 1
         answer given to a Level 2 question, and the negative limb passes on
         absence.
    C9   §5.2's ground is recorded as forward-looking, with the measurements
         cited and their values read at execution.
    C10  §6's ratification present with all four of its statements.
    C11  `R-8` through `R-12` recorded, and discharged per `M4` in one of its
         branches.
    C12  `M6` recorded with the manner of any emptiness; no silent revert.
    C13  `M11`'s two Statement SHAs unchanged and neither file modified;
         append-only files byte-prefix verified.
    C14  `M9`'s base-relative list contains no path outside the §0c manifest.
    C15  Refs pushed are exactly the integration branch and `refs/heads/main`;
         the superseded branch is unmoved.

---

## 9. Substring hazards

    verbatim        the label under examination, and ordinary usage
    item            the document's numbered items, register items, ordinary
                    usage
    scope           the open question's scope, a register's stated scope, a
                    task's scope
    ruling          PI rulings, the rule set, "ruled" as past tense
    qualifier       the inserted phrase, and grammatical usage
    divergence      the item-2 case and any other `M2` finds

A check that cannot state its exclusions is performed by reading.

## 10. Criterion satisfiability

`C2` is checkable because both sides exist before it runs.

`C3`, `C7` and `C8` have negative limbs satisfiable by reading or diffing for
absence.

`C11` accepts both branches of `M4`.

**No criterion is reachable in a case an abort condition covers.** `A7`, `A8`
and `A9` stop before any landing, so no criterion reports on those cases, and
`A8`'s exclusion of the §5 divergence is stated in `A8`.

---

## 11. Post-execution verification (Researcher)

1. compare Part 1's items against the supplied source, word for word;
2. read for an assertion in either direction barred by §4.2 — **the most
   likely quiet defect is a record that resolves, one way or the other, a
   history the evidence leaves open**;
3. check §5.3's six elements, and confirm by diff that no quoted block moved;
4. read §5.2 for whether the ground is stated as forward-looking or slips into
   an archaeological claim;
4a. **read §5.1's three levels for cross-contamination** — specifically for a
   Level 1 answer given to a Level 2 question, which is the defect the
   Reviewer caught in the draft: "neither text has authority over the other"
   is true of bytes and false of the record being made;
5. confirm §6 states that Reviewer approval was not PI ratification;
6. re-run `M6` independently, including the manner of emptiness;
7. recompute `M11`'s digests; verify append-only by byte prefix;
8. confirm `C15` by `git ls-remote`, including the superseded branch;
9. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 12. What this task does not establish

It lands a source that was acted on without one, and disposes of one known
divergence. It produces no scientific result, no measurement of any physical
quantity, moves no gate, and `P2-PHASE-01` is unchanged. `Q1`, `GAP-A`,
`GAP-B`, `A-EXT-01` and `H-EXT-01` are untouched.

**It does not make the earlier citations correct**, and it does not establish
what the original document said where the evidence does not.

---

## 13. Next

1. **`P2-PROVENANCE-CENSUS-01`** — the four-set census, over the scope the PI
   fixed, and now also carrying `R-12`'s labelling question.
2. **`P2-SESSION-RULINGS-02`** — over the set the census freezes.
3. **`R-4`'s measurement**, then **`R-3`**, then the extraction protocol
   freeze.
