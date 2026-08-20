# PI adjudication on the returned items — the source, retrospectively recorded

    Status           RETROSPECTIVELY RECORDED AND PI-CONFIRMED AT LANDING
                     — ORIGINAL ISSUANCE NOT ESTABLISHED

    Decision owner   PI
    Recorded by      Executor, under
                     `specs/2026-08-20T1705Z_adjudication-source-02.md`
    Recorded         2026-08-20

---

## PART 1 — THE DECISION

### 1. What this record is

**This record lands a document that was acted on before any record of it
existed.** Items of it were transcribed into `decisions/README.md` and
`docs/GOVERNANCE-DEBT.md`, acted on by `P2-REGISTRY-SPLIT-01` and
`P2-RECON-PROJ-01`, and cited by number in a landed specification — while the
document itself sat nowhere in the repository. This record is the source those
citations lacked.

**Its original issuance is NOT ESTABLISHED by the surviving record.** No stored
transcript of the original exists. What exists is a transcription made by the
Researcher from the adjudication as it appeared in session, and the PI's
confirmation of its substantive content. That confirmation is of *meaning*;
byte-identity with the original, and the original's interface formatting,
emphasis and mathematical rendering, are not asserted by it and are not
established here.

**The PI confirms the substantive content of this document at this landing.**

### 2. What this record does NOT do, in either direction

**This record alters no item's effective date, and makes no finding about what
any effective date was.**

**Two errors are barred, and this record is shaped to commit neither:**

    FORWARD    recording the document as adjudicated by the PI at issuance
    BACKWARD   recording that items not previously landed had no authority
               until now, or take effect only now

**Neither proposition is asserted anywhere in this record.** The first would
manufacture a provenance the evidence does not carry; the second would strip an
authority the evidence does not deny. The evidence settles the question in
neither direction, and this record leaves it where the evidence leaves it.

**Absence of surviving provenance is not evidence of absence of historical
authorisation**, and this task has measured only the former.

**Items already landed from this document were in force on a citation whose
source was unlanded.** That is a statement about the state of the record, not
about the authority of the items.

---

### 3. The document, item by item

**The item set below is the set measured from the source, item for item, in its
stated words.** No count is asserted here; the set is what the reading returned.

**Reading method.** Every bold heading in the source's PART B was enumerated,
and those beginning with a digit and a full stop were taken as the numbered
items. The numbers returned were consecutive from 1, and one bold heading —
`Priority / sequencing` — carries no number. It is recorded at §4 below and is
**not classified** as an item or as not an item.

#### 1. PI-decision effective time — RULED

**Stated words:**

> **1. PI-decision effective time — RULED**
>
> Adopt the proposed rule, effective now:
>
> PI decisions take effect when issued. Their reviews are mandatory but
> non-gating. A review may identify defects and recommend revision or
> supersession, but does not suspend or delay the decision unless the PI
> explicitly so rules.
>
> Please replace the current PROVISIONAL treatment in `decisions/README.md`
> with the formal rule, preserving provenance of the earlier provisional state
> and this adjudication.

**Landed.** By `P2-GOV-HOUSEKEEP-02`, into `decisions/README.md:29-34`, under
the label `PI RULING, adopted verbatim:`. The landed ruling text and the stated
words above are equal under a normalisation that strips blockquote prefixes and
code delimiters and collapses whitespace, applied to both sides.

**Its effective date is unchanged by this record.**

---

#### 2. `CONVENTIONS.md` protection — record an OPEN finding

**Stated words:**

> **2. `CONVENTIONS.md` protection — record an OPEN finding**
>
> Agreed. Record that `CONVENTIONS.md` contains programme-level definitional
> records, including review-bound statements, but the repository does not
> presently specify the protection model for such reviewed entries.
>
> Do not infer append-only status and do not settle the protection model in
> this task.
>
> The open question is whether a reviewed definitional statement may be edited
> in place or instead requires supersession, a new `Statement SHA`, and a new
> review.

**Landed, and divergent.** By `P2-GOV-HOUSEKEEP-02`, into
`docs/GOVERNANCE-DEBT.md:305-312` as `G-13`, under the label
`PI RULING, registered verbatim:`. **The landed block differs from the stated
words above in what the item decides.** Both texts are recorded in full, and the
divergence is disposed of, in the additive correction landed beneath `G-13` by
this task. **The landed block is not rewritten.**

**Its effective date is unchanged by this record.**

---

#### 3. `assumptions/` and definitions — RULED

**Stated words:**

> **3. `assumptions/` and definitions — RULED**
>
> Definitions do not belong in `assumptions/`.
>
> Preserve the taxonomy now landed:
>
> `CONVENTIONS.md` → definitions / definitional conventions
> `assumptions/` → physical assumptions and physical hypotheses
> `decisions/` → PI decisions
> `reviews/` → specification reviews
>
> `A-EXT-01` therefore remains canonical in `CONVENTIONS.md`. Do not create an
> assumption copy or stub for it.

**Landed, as the act it directs.** The taxonomy this item directs be preserved
was landed by `P2-REGISTRY-SPLIT-01` and stands at `decisions/README.md:11-16`
and `assumptions/README.md:21-26`. `A-EXT-01` remains canonical in
`CONVENTIONS.md`, and `assumptions/README.md:14-15` records that it has no entry
or stub there.

**No landed block claims to reproduce this item's words**, and none is compared
against them. The item directs that an existing taxonomy be preserved; what is
landed is that taxonomy, which the item's own words describe rather than quote.

**Its effective date is unchanged by this record.**

---

#### 4. Historical `reviews/pi/` records — retrospective review required

**Stated words:**

> **4. Historical `reviews/pi/` records — retrospective review required**
>
> The three historical PI records should receive retrospective reviews.
>
> Each review must be explicitly labelled:
>
> RETROSPECTIVE REVIEW — non-gating; does not alter the historical effective
> date of the PI decision.
>
> Review the exact historical decision bytes actually in force. Do not rewrite
> the historical decisions merely to make them conform to the new registry
> structure.

**Landed.** By `P2-GOV-HOUSEKEEP-02`, into `decisions/README.md:87-104` and
into `docs/GOVERNANCE-DEBT.md:346-370` as `G-14`, whose disposition is `RULED`
and whose status is `REVIEW PENDING` for all three records.

**One measured difference, recorded rather than passed over.** The required
label is landed in both places without the stated words' trailing full stop —
`...does not alter the historical effective date of the PI decision` against
`...of the PI decision.` **Nothing else differs.** A trailing stop on a label is
a difference of punctuation and not a difference in what the item decides, and
it is recorded here so that a later reader meets it rather than rediscovers it.

**Its effective date is unchanged by this record.**

---

#### 5. Component 5 and Component 9 — re-scope before RECON-01b

**Stated words:**

> **5. Component 5 and Component 9 — re-scope before RECON-01b**
>
> Perform a bounded reassessment because `A-EXT-01`/`H-EXT-01` changed the
> epistemic status of the projection question.
>
> For Component 5, distinguish the implementation/specification of
> `TT_RECIPES` from the separate physical-completeness question. `A-EXT-01`
> now permits axis-TT to be used definitionally by `RECON-01b`. Failure to
> establish that the discarded complement is physically irrelevant belongs
> under `H-EXT-01` and must not automatically block an axis-TT-defined
> reconstruction.
>
> For Component 9, determine exactly whether the missing requirement concerns:
>
> (a) specification of the observable, or
> (b) physical completeness of the projection.
>
> The former may now be satisfied by `A-EXT-01`; the latter remains
> UNESTABLISHED under `H-EXT-01`. Reclassify only from repository evidence.
>
> This should be a short scope reassessment, not execution of `RECON-01b`.

**Landed, as the act it directs.** By `P2-RECON-PROJ-01`, into
`derivations/P2-RECON-PROJ-01_projection-adjudication.md`, whose specification
cites this item by number at `specs/2026-08-19T2214Z_recon-proj-01.md:8`
(`Origin: PI adjudication item 5`). The bounded reassessment was performed;
components 5 and 9 were each reclassified from repository evidence and each
returned `SPECIFICATION ONLY`, unchanged.

**The PI ratifies that bounded re-scope retrospectively, at this landing.** The
ordering is stated explicitly, and in sequence:

    1  executed
    2  then reviewed
    3  then independently verified
    4  then retrospectively ratified

**The historical timing and provenance of the original authorisation are not
established by the surviving record.** This ratification represents neither that
this record existed before that landing, nor that no earlier authorisation
existed.

**The statement tying the re-scope to the changed status of the projection
question is part of this item's own reasoning**, recorded here with the item and
**not as a separate adjudication.** The item's stated words give that tie as the
reason for the reassessment — that `A-EXT-01`/`H-EXT-01` changed the epistemic
status of the projection question — and it is read as reasoning for this item,
not as an eighth ruling.

**Its effective date is unchanged by this record.**

---

#### 6. D-2 extension — measure, do not set a post-hoc criterion

**Stated words:**

> **6. D-2 extension — measure, do not set a post-hoc criterion**
>
> Extend the discarded-external-space diagnostic across the relevant
> `RECON-01b` k/parameter domain so we can determine whether the `EXT-01`
> result is local to the preregistered point or structurally persistent.
>
> This is a measurement task. Do not derive or introduce a kill threshold from
> the observed values after the fact, and do not make this measurement a new
> prerequisite for the axis-TT-defined `RECON-01b` unless separate evidence
> establishes that requirement.

**Not landed.** No landed artifact records this item, and the work it directs
has not been performed: there is no results directory for the extension, and it
is named as an outstanding follow-on at `specs/2026-08-19T2214Z_recon-proj-01.md:313`
and `specs/2026-08-19T2324Z_gov-housekeep-02.md:489`.

**`D-2` as recorded at `DECISION_LOG.md:2369` is not this item's landing.** That
entry is `P2-RECON-EXT-01`'s own execution-layer disposition, recorded for that
task, and it defers the extension rather than recording this item.

**The PI confirms this item's content at this landing.** **This record makes no
finding about its effective date in either direction.**

**The substantive question this item frames has since moved**, and that is
registered — not decided — as `R-9`.

---

#### 7. Two wording corrections

**Stated words:**

> **7. Two wording corrections**
>
> Apply the already identified non-substantive wording corrections as
> maintenance, with exact before/after text recorded. Do not use them to alter
> scientific meaning or reopen settled findings.

**Landed, as a departure from what it directs.** By `P2-GOV-HOUSEKEEP-02`, into
`docs/GOVERNANCE-DEBT.md:391-442` as `G-15`, disposition `REPAIRABLE`. The
departure is ratified at §5 below.

**Its effective date is unchanged by this record.**

---

### 4. The unnumbered block

The source carries one bold block that carries no number:

> **Priority / sequencing**
>
> First land the governance rulings and provenance housekeeping above. Then
> perform the bounded Component 5/9 reassessment. D-2 may follow as a
> measurement task.
>
> None of the governance housekeeping should by itself block `RECON-01b`.
>
> The controlling scientific distinction remains:
>
> `A-EXT-01`: `Z_axis-TT` is the defined RECON observable
>
> while
>
> `H-EXT-01`: `Z_axis-TT = Z_physical`
>
> remains UNESTABLISHED and is NOT ASSUMED by `RECON-01b`.
>
> Accordingly, `RECON-01b` may test the frozen prediction within the
> axis-TT-defined sector, but its result must not be presented as establishing
> full gravitational completeness or vanishing spin-1/0 residues.

**It is recorded here as the reading returned it, and it is NOT classified.**
Whether it is an item of this document is registered as open at `R-11`. It is
not counted among the numbered items above and it is not excluded from the
document; the question is left where the evidence leaves it.

---

### 5. Item 7 — the departure, ratified

**What the item directed.** That the already identified non-substantive wording
corrections be applied as maintenance, with exact before/after text recorded.

**What was done instead.** The corrections were recorded as errata at `G-15` and
**were not applied to the landed bytes.** The departure was stated in
`specs/2026-08-19T2324Z_gov-housekeep-02.md` §7.2, with three reasons: that a
landed specification's bytes are the evidence of what was executed and reviewed;
that editing a review-bound landed record would settle `G-13` by practice while
the PI has ruled it open; and that an errata record delivers the same benefit to
a reader at no provenance cost.

**The departure was reviewed but was not PI-confirmed at the time.** The
Researcher flagged it to the Reviewer, and the Reviewer approved the
specification carrying it. **Reviewer approval is not PI ratification**, and the
surviving record carries no PI confirmation of the departure at that time.

**The PI ratifies the errata treatment at this landing**, **with no
representation that it was authorised earlier.**

---

### 6. Provenance of the text recorded here

    Source artifact      the adjudication-source transcription
    sha256               8c730eacc673153c2cd3b27fa9537186d2151f9c99d42a782cbb2219fb87daf1
    Origin               conversation, not a pre-existing file
    Transcribed by       the Researcher, from the adjudication as it
                         appeared in session
    Verification         PI VERIFIED — substantive adjudication content
                         confirmed; exact historical formatting NOT
                         established

    Review of that       ChatGPT, 2026-08-20,
    artifact             verdict APPROVE AS PI-CONFIRMED ADJUDICATION SOURCE
    sha256               c07a173e21fed8eb193b6683e60f82c693c350738985fc7ed372c96aa561c31a
    bound to             the source artifact's bytes, by digest

**The ground on which the words above are the ones recorded.** For this
retrospective provenance record, the PI-confirmed source wording governs the
substantive adjudication content, including for the item whose landed
transcription diverges from it. **This is a determination about which text is
authoritative for a record being made now.** It asserts nothing about historical
bytes or formatting, and it does not license editing any landed quotation. The
determination and the two levels it must not be confused with are recorded in
full beneath `G-13` in `docs/GOVERNANCE-DEBT.md`.

**Known limits of the transcription, stated rather than hidden.** The original
contained expressions rendered as mathematics in the interface, which appear in
the source as plain text; whether that conversion altered anything is not
established. Formatting — headings, emphasis, list markers — is reconstructed,
not preserved from a stored original.

---

## PART 2 — THE REVIEW

**`REVIEW PENDING`.**

**No review of Part 1 as constructed was supplied**, and the executor does not
author one. Under the rule at `decisions/README.md:29-34`, a decision takes
effect when issued and a pending review does not delay it.

**What was supplied is a review of the SOURCE ARTIFACT, not of this record.** It
is identified at §6 above by digest and verdict. Its own §9 states that it
"does not itself perform that landing, alter any register, or adjudicate later
scientific consequences", and it saw none of Part 1's construction — not the
status at the head of this file, not §2's barred propositions, not §3's landed
findings, and not §5's ratification. **It is recorded as what it is and is not
presented as Part 2.**
