# P2-SESSION-RULINGS-02 — Extract candidate sources for the unrecorded adjudications

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              EXTRACTION. No landing. No merge. No confirmation.

---

## 0. Binding SHA

    Evidence base (main at authorship)   caf5111dacad21da9e204b79b4b7add1f648107c

If `main` has advanced when execution begins, execution does not proceed.

---

## 0a. What this task is, and what it deliberately is not

The landed census placed a set of distinct adjudications in `S_missing`: cited
by landed artifacts, with no landed record of the adjudication itself.

**The route to a record is fixed and this task performs only its first step:**

    candidate source  ->  PI confirmation  ->  canonical provenance record
    ^^^^^^^^^^^^^^^^      this task does not      this task does not
    this task              perform this            perform this

**This task lands nothing.** The PI has not confirmed these adjudications, and
**a specification that assumed confirmation would be the defect this line has
been repairing** — an adjudication described as settled before it was.

Its product is material for the PI to confirm or reject, per adjudication.

## 0b. What the landed ruling makes possible, and what it does not

The landed ruling holds that a specification transcribing an adjudication's
words is **evidence of that adjudication's content**, but is not that
adjudication's canonical record.

**The first limb is what makes this task possible**: the transcriptions may be
read as candidate sources.

**The second limb is what makes the confirmation step necessary**: a
transcription is single-source, unverified, and one has already been measured
to diverge from what it claimed to reproduce.

## 0c. Non-objectives

This task does **not**:

1. confirm, ratify, adopt or land any adjudication;
2. **reconstruct any adjudication's wording from more than one citation.**
   A candidate source is a single quoted block in a single artifact.
   Assembling one from several is forbidden by `A4`;
3. paraphrase, summarise, normalise, translate or tidy any candidate source;
4. resolve any divergence it finds between citations — **it records both**;
5. decide which of several candidate sources is authoritative;
6. re-open, re-scope or recompute the census, or add to `S_missing`;
7. answer `R-13`, `R-14` or `R-15`. **Each has a landed home and is a separate
   governance question**; touching them here would undo the scope the census
   integration established;
8. merge anything, move `main`, or modify any file under `scripts/`.

## 0d. Authorised path manifest — defined once

    P1   the extraction artifact this task produces
    P2   any new script created solely for this extraction, under a diagnostic
         or analysis path, **each named in the report**. **No existing script
         may be modified.**
    P3   this task's own spec, review and report artifacts, wherever their
         authorised paths lie, including under specs/

`A6` and `C11` both refer to this manifest and neither restates it.

**Self-check on this specification**, against the defect classes this line has
produced: no asserted count — **the subject set's size is read under `M1`, not
stated**; no unmeasured universal; no dangling `M`/`A`/`C`/`§` reference; no
predeclared set; no acceptance criterion covering a case an abort condition
covers; self-referential counts checked against this document's content.

---

## 1. Measurements

Nothing is carried, including from the census execution report and from any
summary of it.

    M1   **The subject set.** From the landed census artifact, read the
         distinct adjudications it places in `S_missing`, and for each, its
         identifier and every citing passage the census records for it.
         **Read; do not carry, and do not add or remove a member.**

    M2   **Candidate sources.** For each member of `M1`, examine each of its
         citing passages and determine whether that passage contains a block
         presenting the adjudication's own words — a quotation, a block
         labelled as reproducing what was ruled, or equivalent.

         Record per passage: `QUOTED BLOCK`, `REFERENCE ONLY` (the passage
         names or relies on the adjudication without giving its words), or
         `INDETERMINATE` with the reason.

    M3   **Divergence between citations.** For each member with more than one
         `QUOTED BLOCK`, compare the blocks. Record `AGREE`, or `DIVERGE` with
         **both texts in full** and what differs.

         **This is expected to be informative rather than empty**: a
         divergence of exactly this kind, between a landed block and its
         source, has already been measured in this repository. Whether any
         occurs here is what `M3` establishes.

    M4   **Per-adjudication disposition.** For each member, record one of:

             CANDIDATE AVAILABLE      at least one `QUOTED BLOCK` exists.
                                      Record each, verbatim, with its path
                                      and line span.
             SOURCE UNAVAILABLE       no `QUOTED BLOCK` exists among its
                                      citing passages. **Record this as the
                                      result. Do not reconstruct.**
             INDETERMINATE            the passages do not settle it. Record
                                      what would.

    M5   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm this
         task alters neither.

---

## 2. How a candidate source is extracted

    E1   **Verbatim, by extraction, not by transcription.** Each quoted block
         is taken from the file programmatically — located by its bounds and
         copied — not retyped. Record the method and the byte count.

    E2   **A candidate source is one block in one artifact.** Where a member
         has several, each is recorded separately, as a separate candidate.
         **They are not merged, reconciled, or ranked.**

    E3   **Surrounding prose is not the source.** A sentence describing what
         was ruled is `REFERENCE ONLY` under `M2`, however confident it
         sounds. **The distinction is between the adjudication's words and a
         report of them**, and `C4` checks it was applied.

    E4   **Nothing is supplied that the block does not contain.** No ellipsis
         filled, no bracket expanded, no obvious omission repaired. If a block
         is incomplete on its face, that is recorded as a property of the
         candidate.

    E5   **If no single passage contains a sufficient candidate block, the
         passages are not combined.** The member is classified
         `SOURCE UNAVAILABLE` under `M4`, and the record names which passages
         would have had to be combined and what each contributes.

         **This is a result, not a failure.** `A4` covers the different case
         where a combined candidate has actually been produced.

---

## 3. Abort conditions

    A1   the base SHA observed differs from §0
    A2   the landed census artifact cannot be read, or `M1`'s set cannot be
         derived from it
    A3   a member of `M1` cannot be located in the artifact's own records
    A4   a candidate has been produced by combining more than one passage,
         or by supplying words absent from a single source block. **Stop
         before commit and discard the reconstructed candidate.**

         **This is the procedural case, not the evidential one.** A member for
         which no single sufficient block exists is `SOURCE UNAVAILABLE` under
         `E5` and `M4`, and execution continues; `A4` fires only if a
         reconstruction has been written.
    A5   `main` moves during execution
    A6   a path outside the §0d manifest is modified

**Every condition here stops execution.** No acceptance criterion covers a
case any of them covers: `SOURCE UNAVAILABLE` is an `M4` disposition under
`E5`, not an `A4` case, and the two describe different situations — the
absence of a single source, and the production of a combined one.

---

## 4. Branch mechanics

    Branch       a new science/<scientific-task> branch
    Merge        NONE. `main` MUST NOT MOVE from `caf5111d`.
    Push scope   this task's branch only.
    Prohibited   force-push; `--force-with-lease`; branch deletion; history
                 rewrite.

**Integration, and any landing of a confirmed record, are separate
specifications and follow PI confirmation.**

---

## 5. Required content of the extraction artifact

1. `M1`'s subject set, each member with its identifier and citing passages.
2. `M2`'s per-passage classification with the reason.
3. `M3`'s comparison for every member with more than one quoted block,
   including both texts where they diverge.
4. `M4`'s disposition per member, with every candidate recorded verbatim, its
   path, its line span, and `E1`'s method and byte count.
5. A statement of what the extraction does **not** establish, naming at
   minimum: that a candidate source is evidence of content and not a record;
   that no member is confirmed; that `SOURCE UNAVAILABLE` means no single
   block was found among the citing passages, **not that the adjudication was
   never made**; and that no effective date is determined.
6. Any question raised and not settled, recorded as open.

**The artifact recommends nothing and confirms nothing.** `C6` fails on a
recommendation, an adoption, or a statement that a candidate is correct.

---

## 6. Acceptance criteria

    C1   `M1`'s set matches the landed census artifact member for member —
         **neither more nor fewer**. Verified by comparison against the
         artifact, not by assertion.
    C2   Every citing passage of every member carries an `M2` classification
         with its reason.
    C3   `M3` present for every member with more than one quoted block, with
         both texts where divergent.
    C4   No block classified `QUOTED BLOCK` is a description of a ruling
         rather than the ruling's words, per `E3`. Verified by reading a
         sample and by the recorded reasons.
    C5   Every candidate is recorded verbatim with `E1`'s method and byte
         count, and no candidate combines text from more than one passage.
    C6   The artifact contains no confirmation, adoption, recommendation, or
         statement that a candidate is correct. Verified by reading;
         **passes on absence**.
    C7   §5 item 5's statement of non-establishment is present in the
         artifact with each of its named items, and §10's statement is not
         substituted for it — **§5 item 5 is a required content of the
         artifact; §10 is a statement about this specification.**
    C8   `SOURCE UNAVAILABLE` members carry no reconstructed text, and each
         records under `E5` which passages would have had to be combined.
    C9   `R-13`, `R-14` and `R-15` are untouched — no answer, no partial
         answer, no proposed rule. Verified by reading.
    C10  `M5`'s two Statement SHAs unchanged.
    C11  No path outside the §0d manifest is modified; `main` unmoved at
         `caf5111d`; only this task's branch pushed.

---

## 7. Substring hazards

    ruling          PI rulings, the rule set, "ruled" as past tense
    source          candidate source, source branch, source of record
    verbatim        the label on a block, and the extraction method — `E1`
                    performs it, a label only claims it
    record          a canonical record, a census row, "record" as a verb
    quoted          a quotation, and "quoted" describing a citation
    block           a text block, and a blocked task

A check that cannot state its exclusions is performed by reading.

## 8. Criterion satisfiability

`C1` compares against an artifact that exists before the check runs.

`C4`, `C6`, `C8` and `C9` have negative limbs satisfiable by reading for
absence; none requires the artifact to declare an absence.

`M4`'s three dispositions are all admissible outcomes, so a correct execution
passes whichever each member takes.

**No criterion is reachable in a case an abort condition covers.** In
particular `C8` and `A4` describe different situations: `C8` reports a member
for which no single source exists, `A4` fires when a combined candidate has
been written. **The absence of a source and the manufacture of one are not the
same event**, and an earlier draft of this specification conflated them.

---

## 9. Post-execution verification (Researcher)

1. compare `M1`'s set against the landed census independently;
2. **re-extract a sample of candidates by a different method** and compare
   byte for byte — `E1` claims extraction rather than transcription, and the
   claim is checkable;
3. read `C4`'s sample myself — **a confident description of a ruling is the
   easiest thing to admit as the ruling**, and it is the failure this task is
   most exposed to;
3a. read every `SOURCE UNAVAILABLE` member for `E5`'s record of what would
   have had to be combined — **a member marked unavailable without that record
   cannot be distinguished from one that was not looked at**;
4. read every `M3 DIVERGE` case for whether both texts are present;
5. read for anything barred by `C6`;
6. confirm `C9` by reading the three records;
7. recompute `M5`'s digests;
8. confirm `C11` by `git ls-remote`;
9. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 10. What this task does not establish

It produces no scientific result, no `β_V`, moves no gate, and `P2-PHASE-01`
is unchanged.

**It does not establish as authoritative** whether any adjudication was made,
what its confirmed content was, or when it took effect. **What it does produce
is candidate evidence of content, for PI confirmation** — which is what the
landed ruling's first limb permits and its second limb requires be confirmed
before it becomes a record.

**It produces material for the PI to confirm or reject**, and a member marked
`SOURCE UNAVAILABLE` is a finding about the repository, not about the
adjudication.

---

## 11. Next

1. **PI confirmation, per adjudication**, over what this task extracts. A
   member the PI does not confirm does not become a record.
2. **A landing specification**, over the confirmed subset only.
3. **`R-4`'s measurement**, then **`R-3`**, then the extraction protocol
   freeze, whose contested elements go to the PI item by item.
