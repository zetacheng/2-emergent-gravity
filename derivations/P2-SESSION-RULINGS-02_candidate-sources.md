# `P2-SESSION-RULINGS-02` — candidate sources for the unrecorded adjudications

    KIND        EXTRACTION. Nothing is confirmed, adopted, ranked or landed.
    SUBJECT     the distinct adjudications the landed census places in
                `S_missing`, read under `M1`
    BASE        caf5111dacad21da9e204b79b4b7add1f648107c
    PRODUCT     candidate source material, for the PI to confirm or reject,
                per adjudication

**This artifact confirms nothing and recommends nothing.** No candidate below
is stated to be correct, authoritative, or preferred over another.

---

## 0. The result, in one place

    members read from the census        10
      CANDIDATE AVAILABLE                5
      SOURCE UNAVAILABLE                 4
      INDETERMINATE                      1

    citing passages examined            31
      QUOTED BLOCK                       6
      REFERENCE ONLY                    19
      INDETERMINATE                      6

    distinct candidate blocks extracted  6

**Five of the ten members have a candidate; five do not.** The five without one
are not a failure of the search: for four, no citing passage contains a
delimited block at all, and for the fifth the passages do not settle whether a
nearby block is this member's ruling.

---

## 1. How a candidate was located and extracted

**A passage carries a `QUOTED BLOCK` only where the adjudication's own words
are delimited.** A confident sentence reporting what was ruled is
`REFERENCE ONLY`, per `E3`, however precisely it states the outcome. **Three
members turn entirely on this distinction**, and it is where this task is most
exposed to error.

**The bounds rule, stated so it can be checked.** A block is admitted for a
member where a citing passage LIES WITHIN it, or IMMEDIATELY INTRODUCES it —
the block beginning within eight lines of the passage's recorded line, with
only a heading, a label, or blank lines between. **The window is a stated
parameter of the method, not a result**; one member's outcome turns on it and
that is recorded at `ADJ-28`.

**Extraction, not transcription.** Every block below was located by its own
delimiters and copied byte for byte out of the blob by
`scripts/diagnostics/session_rulings_02_extract.py`:

    git cat-file blob <rev>:<path>, split on newline, slice [lo-1:hi] by the
    block's own delimiter bounds, joined on newline; no line retyped, nothing
    normalised

**No line was retyped, no ellipsis filled, no bracket expanded.** Byte counts
are recorded per candidate so the claim is checkable.

---

## 2. The subject set, member by member

### `ADJ-19` — "Reading 1 governs" — the commit order of the Fierz integration

    disposition   SOURCE UNAVAILABLE
    passages      1

**Per-passage classification, with the reason each carries:**

    specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:130
      REFERENCE ONLY
        bolded inline prose, `**PI ruling: Reading 1 governs.**`, with no 
        quotation delimiter and no verbatim label. Where the ruling ends a
        nd the specification's own reasoning begins is not marked, so no b
        lock bounds exist to extract by

**`E5` — what would have had to be combined, and what each passage contributes.**

Only ONE citing passage exists, so no combination was available to make 
and none was attempted. The passage contributes a bolded assertion of th
e outcome ("Reading 1 governs") together with the specification's reason
ing, undelimited. Nothing else in the searched scope was offered by the 
census for this member.

**No reconstructed text appears above and none was written.**

---

### `ADJ-20` — The gamma5 definition governs from the Phase-A freeze; the JSON companion entry is not authoritative, 2026-08-07

    disposition   CANDIDATE AVAILABLE
    passages      3

**Per-passage classification, with the reason each carries:**

    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:783
      REFERENCE ONLY
        a section heading and the narrative that introduces the disagreeme
        nt; it reports that a ruling was delivered and does not give its w
        ords
    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:802
      QUOTED BLOCK
        labelled `**PI ruling, delivered 2026-08-07, reproduced verbatim:*
        *` and followed by a delimited blockquote
    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:824
      QUOTED BLOCK
        lies INSIDE the same blockquote the passage at :802 introduces. It
         resolves to one block, not a second

**Candidate `C-20`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
    line span   804-842
    bytes       1749
    reached by  the passage at :802 introduces it; the passage at :824 lies inside it

**Verbatim, as extracted:**

> For this task, the Phase-A freeze governs the definition of gamma5:
>
> gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)
>
> under the frozen Euclidean signature (1,1,1,1), with gamma5 Hermitian
> and gamma5^2 = Id4.
>
> The vocabulary.gamma5 entry in derivations/CANONICAL_INTERACTION.json,
> which inserts an additional factor of I, is an erroneous
> companion-artifact entry for this point. It is not authoritative for
> interpretation of the canonical interaction in this task. This ruling
> is supported by the Phase-A freeze, CONVENTIONS.md, the governing
> CANONICAL_INTERACTION.md, and the Phase-A checker assertions.
>
> Accordingly, Deliverable 4 uses:
>
> (bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2
>
> with gamma5 understood in the Phase-A-freeze sense.
>
> Record this PI ruling in commit 1's specification authority artifact so
> that the branch remains self-contained and reproducible. Then execute
> derivations (a) and (b) as originally scoped.
>
> Do not modify CANONICAL_INTERACTION.json or any other frozen/
> pre-existing artifact in this task. Record the inconsistent JSON
> vocabulary entry as a REPOSITORY_DEFECT finding. Its correction is a
> separate governance task.
>
> Also record a secondary process finding for later follow-up: the
> existing ratification process allowed a machine-readable companion to
> disagree semantically with its governing Markdown/convention sources.
> A future governance task should consider a machine check for
> duplicated normative fields across governing .md / companion .json
> pairs.
>
> This ruling resolves only the identified gamma5 source disagreement. It
> does not authorize any other reconciliation, convention choice, physics
> decision, or scope expansion.

---

### `ADJ-21` — A registered-gate artifact pin denotes the exact bytes (the re-pin ruling)

    disposition   CANDIDATE AVAILABLE
    passages      1

**Per-passage classification, with the reason each carries:**

    specs/2026-08-12T2326Z_adopt-domain-repair.md:68
      QUOTED BLOCK
        the section is headed `## 1. The PI ruling that authorises the re-
        pin` and labelled `**Recorded verbatim as issued. It is a ruling, 
        not a derivation.**`, followed by a delimited blockquote

**Candidate `C-21`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-12T2326Z_adopt-domain-repair.md
    line span   72-83
    bytes       796
    reached by  the passage lies in the section that introduces it

**Verbatim, as extracted:**

> **PI RULING.** A registered-gate artifact pin denotes the exact
> operative bytes of the referenced artifact. Where an authorised task
> intentionally modifies that artifact, retaining the old digest would
> create a false correspondence and is not an acceptable landed state.
> The prohibition on an executor re-pinning a gate without authority
> prevents unilateral repair; it does not require an authorised
> modification to leave a knowingly stale pin. Accordingly, before
> integration of `science/adopt-parameter-domain`, a separately reviewed
> corrective task must update the `P2-PHASE-01` admissibility-contract
> draft pin from `a3ec0cb6…` to the digest of the exact bytes intended to
> land. No prerequisite state, gate status, or admissibility verdict is
> changed by that re-pin.

---

### `ADJ-22` — "Not operative at this gate" is an admissible third disposition, and its extension on the cutoff ratio

    disposition   CANDIDATE AVAILABLE
    passages      6

**Per-passage classification, with the reason each carries:**

    GATES.md:1012
      REFERENCE ONLY
        a `GATES.md` prerequisite entry citing the ruling by location — "p
        er the PI ruling recorded in §3a of ..." — and giving none of its 
        words
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:103
      REFERENCE ONLY
        a pointer sentence: the question is "settled by the PI ruling at §
        3a". It describes the ruling's effect and gives no text. The block
         it points to was located separately and is recorded as a candidat
        e
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:121
      QUOTED BLOCK
        the passage lies within a delimited blockquote opening `> **PI RUL
        ING — extension of §3a.**`
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:352
      REFERENCE ONLY
        a template of the `GATES.md` entry the task is to write, carrying 
        an unresolved path placeholder; it cites the ruling by location
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:395
      INDETERMINATE
        the passage cites "the PI ruling recorded in `derivations/P2-PHASE
        -01_microscopic_parameter_domain.md`" — the negative-mass enumerat
        ion ruling, which the census records as landed and as a different 
        member. Whether it bears on this member at all is not settled by t
        he passage
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:407
      REFERENCE ONLY
        "the adopted PI rulings" in the plural, describing their consequen
        ce for a cross-reference; no text is given

**Candidate `C-22a`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-12T2258Z_adopt-parameter-domain.md
    line span   111-119
    bytes       578
    reached by  the passage points to §3a and the block opens 8 lines later, with only the section heading and the verbatim label between

**Verbatim, as extracted:**

> **PI RULING.** "Not operative at this gate" is an admissible third
> disposition for a quantity that neither enters the dimensionless
> computation as a fixed numerical input nor defines a scan coordinate.
> Accordingly, leaving the lattice spacing `a` neither fixed nor scanned
> satisfies this prerequisite. This disposition fixes no physical lattice
> scale. It expires immediately if any quantity computed for this gate
> acquires dependence on `a`; at that point `a` must be given a new
> explicit disposition before the affected computation can serve as gate
> evidence.

**Candidate `C-22b`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-12T2258Z_adopt-parameter-domain.md
    line span   121-135
    bytes       1025
    reached by  the passage lies within it

**Verbatim, as extracted:**

> **PI RULING — extension of §3a.** For this prerequisite, no independent
> cutoff ratio requires disposition beyond the lattice-scale quantity
> `a`. In the lattice formulation, the regulator is supplied by the
> lattice itself, while `CONVENTIONS.md` fixes the unit conventions
> `Λ ≡ 1` in the continuum notation and `a ≡ 1` in lattice units. These
> are unit conventions, not assignments of a physical cutoff scale.
> Under this convention, `a` is not a parameter of any quantity computed
> for this gate. Any dimensionless combination already used here,
> including `Mhat = aM`, is an output or derived variable, not an
> additional microscopic scan coordinate or fixed cutoff input.
> Accordingly, the §3a ruling exhausts the cutoff-scale part of this
> prerequisite for the quantities presently identified at this gate. If
> any additional independent cutoff ratio is identified later, it is
> outside this ruling and requires its own explicit disposition before
> affected results can serve as gate evidence.

---

### `ADJ-23` — C is split into C-a, C-b and C-c, in that order

    disposition   CANDIDATE AVAILABLE
    passages      5

**Per-passage classification, with the reason each carries:**

    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:20
      REFERENCE ONLY
        a section heading naming that a ruling scoped the task
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:27
      QUOTED BLOCK
        labelled `**PI RULING, recorded verbatim, scoping `C`:**` and foll
        owed by a delimited blockquote
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:34
      REFERENCE ONLY
        the specification stating what it itself covers, in its own voice
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:206
      INDETERMINATE
        the passage introduces a delimited blockquote, but the block prese
        nts the words of the ARTIFACT-STATE / STATEMENT-KIND namespace rul
        ing — a different adjudication, which the census records as landed
        . Whether it bears on this member is not settled by the passage
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:313
      INDETERMINATE
        an acceptance criterion about that same namespace ruling's adopted
         sentence, not about this member

**Candidate `C-23`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-14T1241Z_conventions-consolidation-ca.md
    line span   29-30
    bytes       111
    reached by  the passage introduces it

**Verbatim, as extracted:**

> **`C` is not made into a single twelve-rule task. It is split into
> `C-a`, `C-b` and `C-c`, in that order.**

---

### `ADJ-24` — The amendment / new-numbered-rule dichotomy

    disposition   CANDIDATE AVAILABLE
    passages      3

**Per-passage classification, with the reason each carries:**

    specs/2026-08-14T2135Z_integrate-conventions-ca.md:64
      QUOTED BLOCK
        the section is headed `## 2. Two PI rulings this integration rests
         on` and labelled `**Recorded verbatim.**`; the passage introduces
         a delimited blockquote whose text is this member's
    specs/2026-08-14T2135Z_integrate-conventions-ca.md:79
      INDETERMINATE
        the passage lies within a delimited blockquote, but the block pres
        ents the words of the MECHANISM-marker ruling — a different adjudi
        cation, which the census records as landed. Whether it bears on th
        is member is not settled by the passage
    specs/2026-08-14T2135Z_integrate-conventions-ca.md:445
      INDETERMINATE
        a measurement record describing that same MECHANISM-marker ruling,
         not this member

**Candidate `C-24`** — one block, one artifact, not merged with any other.

    path        specs/2026-08-14T2135Z_integrate-conventions-ca.md
    line span   70-75
    bytes       418
    reached by  the passage introduces it

**Verbatim, as extracted:**

> **PI RULING.** §4's amendment / new-numbered-rule dichotomy applies to
> binding governance principles, and does not apply to material expressly
> marked non-binding — traceability, provenance or consolidation records.
> **`## Consolidation record — C-a` may remain, provided that section
> creates, modifies or explains no new obligation and only records what
> the formal rules and amendments already carry.**

---

### `ADJ-25` — The RECON-01B-B0 ruling set — rulings 1, 2 and 4

    disposition   SOURCE UNAVAILABLE
    passages      7

**Per-passage classification, with the reason each carries:**

    derivations/P2-RECON-EXT-01_discarded-external-space.md:9
      REFERENCE ONLY
        the artifact stating what it does not do, citing "PI ruling 2" and
         "PI ruling 4" by number for their effect; no text of either is gi
        ven
    derivations/P2-RECON-EXT-01_discarded-external-space.md:421
      REFERENCE ONLY
        "PI ruling 4 reserves it" — the ruling's effect, not its words
    derivations/P2-RECON-EXT-01_discarded-external-space.md:437
      REFERENCE ONLY
        "PI ruling 4 reserves the related `TT_RECIPES` governance question
        " — effect only
    derivations/P2-RECON-EXT-01_discarded-external-space.md:471
      REFERENCE ONLY
        "PI ruling 2 defers that until the magnitude is known" — effect on
        ly
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:8
      REFERENCE ONLY
        an `Origin` field value naming the rulings the task implements
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:43
      REFERENCE ONLY
        an indented summary headed `## 1a. The PI rulings this task implem
        ents, and their limits`. Each entry states the ruling's substance 
        AND the specification's own consequence in the same breath — "This
         task therefore states NO threshold..." — so it is a report of the
         rulings woven together with the task's response to them, not a de
        limited reproduction of their words. `E3` governs
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:288
      REFERENCE ONLY
        "the PI has ruled it is not upgraded" and "Ruling 2 defers it" — e
        ffects, in a non-objectives list

**`E5` — what would have had to be combined, and what each passage contributes.**

SEVEN citing passages, none delimited. Combining them would have require
d taking the substance of ruling 2 from `specs/2026-08-19T0649Z_recon-ex
t-01-discarded-space.md:43` ("measure first; DO NOT set a physics kill c
riterion"), the substance of ruling 4 from the same summary ("the TT_REC
IPES governance question is NOT adjudicated"), the substance of ruling 1
 from the same summary ("the previously frozen blind target is retained 
unchanged"), and their effects from the four derivation passages at :9, 
:421, :437 and :471 — each of which gives a consequence rather than a te
xt. **No combination was performed.**

**No reconstructed text appears above and none was written.**

---

### `ADJ-26` — Researcher-Reviewer review exchanges, 2026-08-06

    disposition   SOURCE UNAVAILABLE
    passages      1

**Per-passage classification, with the reason each carries:**

    specs/2026-08-06T0456Z_role-model-and-executors.md:141
      REFERENCE ONLY
        `**PI decision, 2026-08-06:**` followed by prose that continues in
        to the specification's own justification — "so that every report h
        as a corresponding instruction in the repository" — with no delimi
        ter marking where the decision's words end

**`E5` — what would have had to be combined, and what each passage contributes.**

Only ONE citing passage exists, so no combination was available. It cont
ributes the decision's substance ("Researcher-Reviewer review exchanges 
are NOT committed") run together with the specification's own justificat
ion, with no boundary between them.

**No reconstructed text appears above and none was written.**

---

### `ADJ-27` — The ruling commissioning P2-OBS-IDENT-01, following P2-GAPB-BRIDGE-01

    disposition   SOURCE UNAVAILABLE
    passages      2

**Per-passage classification, with the reason each carries:**

    derivations/P2-OBS-IDENT-01_observable-identity.md:5
      REFERENCE ONLY
        an `ORIGIN` field value: "PI ruling of this session, following P2-
        GAPB-BRIDGE-01". It names the ruling and gives none of its words
    specs/2026-08-20T1050Z_obs-ident-01.md:8
      REFERENCE ONLY
        the same `Origin` field value in the governing specification

**`E5` — what would have had to be combined, and what each passage contributes.**

TWO citing passages, both `Origin`/`ORIGIN` field values naming the ruli
ng. Combining them would have yielded the same field value twice and no 
text of the ruling at all; neither contributes any of its words.

**No reconstructed text appears above and none was written.**

---

### `ADJ-28` — The D-pre-A ruling on the canonical kinetic operator, cited as the authority for DEFERRED-04

    disposition   INDETERMINATE
    passages      2

**Per-passage classification, with the reason each carries:**

    derivations/P2-DEFERRED-ITEMS.md:77
      INDETERMINATE
        the passage is about "the two PI rulings of 2026-08-08 — the Eucli
        dean exponent mapping and the attraction/repulsion labels", which 
        the census records as landed and as different members. Whether it 
        bears on this member is not settled by the passage
    specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:41
      REFERENCE ONLY
        "The PI ruling it informs will, together with the freeze task that
         follows it" — a reference to a ruling not yet made at the time of
         writing

---

## 3. `M3` — comparison where a member has more than one block

**`ADJ-20` — two passages, ONE block.** The passages at `:802` and `:824`
resolve to the same blockquote at `:804-842`; the second lies inside the block
the first introduces. **There is one candidate, not two**, and the
`AGREE`/`DIVERGE` axis does not arise. Recorded because two passages carrying
the same classification could otherwise be read as two competing sources.

**`ADJ-22` — two blocks, and they are NOT competing versions of one text.**

    C-22a   :111-119   labelled `**PI RULING.**`
    C-22b   :121-135   labelled `**PI RULING — extension of §3a.**`

**The second is expressly an extension of the first, not a variant of it.**
Recording `DIVERGE` would misdescribe them, and recording `AGREE` would assert
a correspondence that does not exist: they say different things about
different questions. **Both are recorded in full above and neither is ranked.**
The census's own title for this member — "and its extension on the cutoff
ratio" — treats both as one member, consistently with what is measured here.

**No other member has more than one block.** For the three members whose
passages located a block belonging to a DIFFERENT adjudication, that block is
not a candidate for the member it was filed under and is not compared as one.

---

## 4. What was found and is not this task's to repair

**Six of the thirty-one citing passages point at a block, or describe a
ruling, that is NOT the member's own.** They are at `ADJ-22:395`,
`ADJ-23:206`, `ADJ-23:313`, `ADJ-24:79`, `ADJ-24:445` and `ADJ-28:77`, and
each is classified `INDETERMINATE` with that reason above.

**In every case the other adjudication is one the census records as LANDED.**

**This is the pattern the census itself registered** in its §9 as
`THE SHADOWING RISK` — that a per-file attribution can file a passage under
the adjudication its file is mostly about, and that whether other files carry
more than one ruling was unmeasured.

**Nothing is repaired here.** The subject set is not expanded, contracted or
corrected, no census value is recomputed, and no member is re-attributed.
**This is recorded as a finding for the applicable reviewed process**, and it
is a finding about the census's passage attribution, not about whether any
adjudication occurred.

---

## 5. What this extraction does NOT establish

**A candidate source is evidence of content and is not a record.** Every block
above sits in a specification, and the landed ruling of 2026-08-21 holds that a
specification transcribing an adjudication's words is evidence of that
adjudication's content but is not its canonical landed provenance record.

**No member is confirmed.** The PI has confirmed none of these adjudications,
and nothing above may be read as confirmation. A candidate becomes a record
only by PI confirmation and a separate landing, in that order.

**`SOURCE UNAVAILABLE` means no single sufficient block was found among the
citing passages. IT DOES NOT MEAN THE ADJUDICATION WAS NEVER MADE.** It is a
finding about the repository, not about the ruling. Four members carry it, and
for each, `E5` above records what would have had to be combined.

**No effective date is determined here**, for any member, in either direction.

**Two further limits, stated because the natural reading would otherwise
exceed them.** The passage classifications are readings, and a different
reader may classify a borderline passage differently — `ADJ-19` and `ADJ-26`
are the two that turn most finely on `E3`. And the bounds rule of §1 has a
stated window; `ADJ-28`'s disposition would change if the window changed, which
is why the parameter is recorded rather than buried.

---

## 6. Open, and recorded rather than settled

    THE SHADOWING PATTERN     Six passages are filed under a member whose
                              words they do not carry. Whether the census's
                              attribution should be revised is NOT decided
                              here and is not this task's.

    ADJ-28's IDENTITY         A delimited block labelled `**Recorded verbatim
                              as issued.**` sits at
                              `specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:51-60`,
                              701 bytes, TEN lines past this member's recorded
                              citing line and so outside §1's window. Its
                              subject is whether an a priori target species
                              count may be imposed. The citation this member
                              rests on, `derivations/P2-DEFERRED-ITEMS.md:199`,
                              names "the `D-pre-A` ruling on the canonical
                              kinetic operator" as the authority for
                              `DEFERRED-04`. **Whether these are the same
                              ruling is NOT established by the citing
                              passages.** What would settle it is PI
                              confirmation that the block is the ruling
                              `DEFERRED-04` relies on. **The block is named
                              here, and is not recorded as a candidate.**

    ADJ-25's FORM             This member is a numbered SET — rulings 1, 2 and
                              4 — and its only structured presentation is a
                              summary that states each ruling's substance and
                              the specification's response to it in one breath.
                              Whether a set of this kind should be confirmed as
                              one member or three is NOT decided here.

