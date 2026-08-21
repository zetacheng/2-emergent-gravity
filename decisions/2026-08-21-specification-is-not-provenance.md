# PI decision — a specification that transcribes an adjudication is not that adjudication's provenance record

**Function:** a PI decision, in the two parts `decisions/README.md` requires.

    Decision owner   PI
    Issued           2026-08-21, in session
    Recorded by      Executor, under
                     `specs/2026-08-21T0503Z_provenance-census-integ.md`
    Effect           ratifies a criterion already applied; changes no
                     measured value

---

## PART 1 — THE DECISION

### 1. The ruling, as issued

**Landed verbatim, in the language it was issued in. This is the ruling:**

> 我裁定：一份 specification 轉錄一條裁決嘅文字，係該裁決內容嘅證據，但本身唔構成
> 該裁決嘅 canonical landed provenance record。

**A working translation, identified as such:**

> A specification that transcribes the words of an adjudication is evidence of
> that adjudication's content, but does not itself constitute that
> adjudication's canonical landed provenance record.

**THE ISSUED TEXT GOVERNS.** The translation is recorded because this
repository's records are otherwise in English. **It is not the ruling and is
not to be cited as it.** A translation cited as the ruling would be the same
substitution this ruling is about.

### 2. The two layers, which are not to be collapsed

    FACT LAYER          The specification DOES carry the adjudication's words.
                        The content is in the repository and is NOT lost.

    GOVERNANCE LAYER    That text is NOT the canonical provenance record of
                        the adjudication.

**Collapsing these misstates the ruling in one of two directions** — as a claim
that the content is missing, which it is not, or as a claim that a
transcription suffices, which the ruling denies. **Both layers hold at once.**

### 3. The measured ground

**The ruling rests on measurement, not on convention.** Three grounds, each
cited as read at the landing head rather than asserted.

**(a) A landed block labelled as reproducing what was ruled was measured and
found to diverge from its source.** `docs/GOVERNANCE-DEBT.md:305` carries the
label `PI RULING, registered verbatim:`; the correction added beneath that
entry at `:346-466` records at `:352-353` that the quoted block "differs from
the PI-confirmed adjudication source in what the item decides", and at `:379`
that two of the differences are substantive — a restrictive qualifier inserted,
and a directive sentence absent. **The label asserted faithfulness and the
measurement refuted it.**

**(b) That transcription was single-source and unverified against any other at
the time it was made.** `decisions/2026-08-20-adjudication-source.md:351-360`
records the source artifact's origin as "conversation, not a pre-existing
file", transcribed by the Researcher from the adjudication as it appeared in
session, with byte-identity to the original expressly not established.

**(c) A later task built a separate record for a document whose items an
earlier specification had already transcribed.**
`specs/2026-08-19T2324Z_gov-housekeep-02.md:152` heads a section
`## 5. TRANSCRIPTION — PI rulings 1, 2, 4`, and that specification is landed.
`P2-ADJUDICATION-SOURCE-02` nonetheless created
`decisions/2026-08-20-adjudication-source.md`, whose `:15-22` states that the
document "was acted on before any record of it existed" and "sat nowhere in the
repository" — **while, in the same passage, listing the transcriptions that did
exist.**

> **What (c) does and does not establish, measured rather than assumed.**
> The behaviour is consistent with the distinction and operationally
> demonstrates it: a specification transcription existed, and it was not
> treated as sufficient. **But no artifact of that earlier line STATES the
> distinction as its motive.** A search of the landed scope for such a
> statement returns only `derivations/P2-PROVENANCE-CENSUS-01_census.md:160`
> and `:164` and `reports/2026-08-21T0308Z_provenance-census-01.md:429` — **the
> census's own artifact and report, which are the very work this ruling
> ratifies.** They therefore cannot serve as independent historical ground for
> it, and are not offered as such. **(c) is recorded as operational
> demonstration, not as stated motive**, and the ruling rests on (a) and (b)
> together with the PI's own authority.

### 4. Effect and scope

**This ruling ratifies the criterion the executor of `P2-PROVENANCE-CENSUS-01`
applied, and CHANGES NO CENSUS VALUE.** The executor stated the criterion in
the census artifact for rejection and computed the result under it. The
criterion applied and the criterion ruled agree in their operative limb; the
comparison is recorded in that task's integration report.

**Had the ruling gone the other way, the census would require recomputation
rather than ratification**, and this landing would not have been the vehicle
for it.

**It takes effect when issued**, per the rule at `decisions/README.md:29-34`.
**This landing does not alter that effective date.**

**What it does not decide.** It does not establish that any unrecorded
adjudication lacked authority. It does not resolve whether a register record
that states an adjudication occurred without carrying its words is sufficient
provenance — that question is registered open as `R-13`. It settles no
citation convention.

### 5. Issuance provenance, recorded rather than smoothed

The ruling was **issued in session on 2026-08-21**, in response to a request
that named the consequence of each possible answer, and is landed here
**retrospectively**.

**An earlier draft of the governing specification described this ruling as
having been issued before it had been.** That draft was caught in review. **The
description is corrected here rather than dropped**, because a record that
quietly acquired a correct issuance date would be the same manufactured
provenance this line of work exists to repair.

---

## PART 2 — THE REVIEW

**`REVIEW PENDING`.**

**No review of Part 1 was supplied**, and the executor does not author one.
Under the rule at `decisions/README.md:29-34`, a PI decision takes effect when
issued and a pending review does not delay it.

**What was supplied is a review of the SPECIFICATION that landed this record**,
`reviews/chatgpt/2026-08-21T0503Z_provenance-census-integ.md`, which reviewed
the specification's treatment of the ruling and not the ruling itself. **It is
not Part 2 and is not presented as it.**
