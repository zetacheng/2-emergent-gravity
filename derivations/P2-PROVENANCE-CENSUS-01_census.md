# `P2-PROVENANCE-CENSUS-01` — what is cited, what is landed, and what is neither

    KIND        MEASUREMENT. Nothing is landed, registered, placed or repaired.
    SCOPE       the repository at `d9f676a4b7d0a851c82177f8e14cba1af467b06f`
    PRODUCT     four sets, and a table of the adjudications they refer to

**This artifact recommends nothing and proposes no rule.** Where it records a
question, it records it as open and leaves it there.

---

## 0. The result, in one place

    S_C        263   candidate passages admitted by M1's predicate
    S_A        151   of those, passages referring to a PI ruling or a
                     PI-ratified disposition
    S_P        120   of those, whose adjudication has a landed record
    S_missing   31   of those, whose adjudication has none

    identity   S_missing = S_A - S_P   =>   151 - 120 = 31

**Those 31 passages refer to TEN distinct adjudications.** The adjudications
are the object of interest; the passages are how they were found.

    adjudications identified          33
      with a landed record            23
      with none found in this scope   10

**`S_missing` is not empty, and that is the census's substantive result.** It
was reachable because `S_A` membership was decided on evidence that an
adjudication occurred, and `S_P` separately on evidence that a record of it
landed. Had the two been merged, `S_missing` would have been empty by
construction.

---

## 1. The ten adjudications with no landed record

**For each: what it decided, where it is cited, and the evidence that no landed
record was found.** The search for a landed record covered every register and
governing document in the frozen scope, not `decisions/` alone.

### `ADJ-19` — "Reading 1 governs" — the commit order of the Fierz integration

    citing passages   1
    where it is set out   specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:130

**Cited at:**

    specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:130

### `ADJ-20` — The gamma5 definition governs from the Phase-A freeze; the JSON companion entry is not authoritative, 2026-08-07

    citing passages   3
    where it is set out   specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:802-834

**Cited at:**

    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:783
    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:802
    specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:824

### `ADJ-21` — A registered-gate artifact pin denotes the exact bytes (the re-pin ruling)

    citing passages   1
    where it is set out   specs/2026-08-12T2326Z_adopt-domain-repair.md:68-78

**Cited at:**

    specs/2026-08-12T2326Z_adopt-domain-repair.md:68

### `ADJ-22` — "Not operative at this gate" is an admissible third disposition, and its extension on the cutoff ratio

    citing passages   6
    where it is set out   specs/2026-08-12T2258Z_adopt-parameter-domain.md:106-126

**Cited at:**

    GATES.md:1012
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:103
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:121
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:352
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:395
    specs/2026-08-12T2258Z_adopt-parameter-domain.md:407

### `ADJ-23` — C is split into C-a, C-b and C-c, in that order

    citing passages   5
    where it is set out   specs/2026-08-14T1241Z_conventions-consolidation-ca.md:27-31

**Cited at:**

    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:20
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:27
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:34
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:206
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md:313

### `ADJ-24` — The amendment / new-numbered-rule dichotomy

    citing passages   3
    where it is set out   specs/2026-08-14T2135Z_integrate-conventions-ca.md:64-77

**Cited at:**

    specs/2026-08-14T2135Z_integrate-conventions-ca.md:64
    specs/2026-08-14T2135Z_integrate-conventions-ca.md:79
    specs/2026-08-14T2135Z_integrate-conventions-ca.md:445

### `ADJ-25` — The RECON-01B-B0 ruling set — rulings 1, 2 and 4

    citing passages   7
    where it is set out   specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:43-62

**Cited at:**

    derivations/P2-RECON-EXT-01_discarded-external-space.md:9
    derivations/P2-RECON-EXT-01_discarded-external-space.md:421
    derivations/P2-RECON-EXT-01_discarded-external-space.md:437
    derivations/P2-RECON-EXT-01_discarded-external-space.md:471
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:8
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:43
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:288

### `ADJ-26` — Researcher-Reviewer review exchanges, 2026-08-06

    citing passages   1
    where it is set out   specs/2026-08-06T0456Z_role-model-and-executors.md:141

**Cited at:**

    specs/2026-08-06T0456Z_role-model-and-executors.md:141

### `ADJ-27` — The ruling commissioning P2-OBS-IDENT-01, following P2-GAPB-BRIDGE-01

    citing passages   2
    where it is set out   specs/2026-08-20T1050Z_obs-ident-01.md:8; derivations/P2-OBS-IDENT-01_observable-identity.md:5

**Cited at:**

    derivations/P2-OBS-IDENT-01_observable-identity.md:5
    specs/2026-08-20T1050Z_obs-ident-01.md:8

### `ADJ-28` — The D-pre-A ruling on the canonical kinetic operator, cited as the authority for DEFERRED-04

    citing passages   2
    where it is set out   derivations/P2-DEFERRED-ITEMS.md:199

**Cited at:**

    derivations/P2-DEFERRED-ITEMS.md:77
    specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:41

**How "no landed record" was established, and what it does not mean.** For
each of the ten, a content search was run over `DECISION_LOG.md`, `decisions/`,
`CONVENTIONS.md`, `GATES.md`, `docs/` and `derivations/` for the ruling's own
substance — not for its number and not for its name, since §0b's first finding
makes matching by number unsound. The search returned nothing in every case.

**A specification is not treated as a landed record of the adjudication it
transcribes.** That test is not this census's invention: `P2-ADJUDICATION-SOURCE-02`
landed a `decisions/` record for a document whose items `P2-GOV-HOUSEKEEP-02`'s
specification had already transcribed, on the ground that the transcription was
not itself the record. **All ten below are set out in a specification or a
derivation and in no register.**

---

## 2. The twenty-three adjudications with a landed record

**Two tiers are distinguished, because they are not the same thing.**

    FULL      the adjudication's words are landed in a register or a
              governing document
    SUMMARY   a register records that it occurred and what it decided,
              without its words, and points elsewhere for them

    ADJ-01        FULL     Fierz matrix sign convention, 2026-08-07
                           DECISION_LOG.md:1013-1088, ruling block :1021-1032
    ADJ-02        FULL     Euclidean exponent mapping, 2026-08-08
                           DECISION_LOG.md:1236-1325, ruling block :1244-1258
    ADJ-03        FULL     Attraction/repulsion sign convention, 2026-08-08
                           DECISION_LOG.md:1393-1392..1518, ruling block :1401-1412
    ADJ-04        FULL     Mean-field channel for P2-PHASE-01, 2026-08-09
                           DECISION_LOG.md:1749-1826, ruling block :1757-1770
    ADJ-05        FULL     The charge-conjugation phase eta is not selected, 2026-08-09
                           DECISION_LOG.md:1827-1906, ruling block :1835-1848
    ADJ-06        FULL     The negative-mass branch is DEFERRED, not excluded, 2026-08-09
                           DECISION_LOG.md:1907-2004, ruling block :1915-1928
    ADJ-07        FULL     Function-based role model and the dual-executor arrangement, 2026-08-06
                           DECISION_LOG.md:948-1012
    ADJ-08        FULL     Registry split: assumptions and PI decisions get their own directories, 2026-08-19
                           DECISION_LOG.md:2425-2505, ruling block :2433-2451
    ADJ-09        FULL     Artifact-state and statement-kind namespaces (E2)
                           CONVENTIONS.md:1452-1487, ruling block :1456-1460
    ADJ-10        FULL     Disposition of INCONCLUSIVE results
                           CONVENTIONS.md:1488-1561 block :1492-1496; decisions/2026-08-19-inconclusive-disposition.md:11-13
    ADJ-11        FULL     The seven-item adjudication on the returned items
                           decisions/2026-08-20-adjudication-source.md, items at :60-320
    ADJ-12        FULL     "operational" is read in the first sense (admissibility contract)
                           derivations/P2-PHASE-01_input_admissibility_contract.md:37-45
    ADJ-13        FULL     A candidate in the parameter-domain enumeration, 2026-08-12
                           derivations/P2-PHASE-01_microscopic_parameter_domain.md:134
    ADJ-14        SUMMARY  science/* is a recognized branch class; historical landings remain accepted
                           docs/GOVERNANCE-DEBT.md:258-300 (G-12), esp. :283; the resulting policy at docs/BRANCHING_POLICY.md:25-46
    ADJ-15        FULL     The pre-push commit-hygiene amend is ratified
                           CONVENTIONS.md:1402-1451 (Rule 20)
    ADJ-16        SUMMARY  The mechanism-marker vocabulary sitting only in a record is acceptable
                           docs/GOVERNANCE-DEBT.md:160-176 (G-07), esp. :169
    ADJ-17        SUMMARY  C-b's A13 continuation accepted, A13 recorded as a specification defect
                           docs/GOVERNANCE-DEBT.md:182-198 (G-08), esp. :186
    ADJ-18        SUMMARY  The pinned-artifact re-pin obligation, ratified once for a single instance
                           CONVENTIONS.md:1370-1401 (Rule 19), esp. :1386
    ADJ-29        FULL     CONVENTIONS.md amendments A-D adopted; Rules 14 and 15 added, 2026-08-09
                           DECISION_LOG.md:1519-1624
    ADJ-30        FULL     CONVENTIONS.md amendments E-L adopted; Rules 16 and 17 added, 2026-08-09
                           DECISION_LOG.md:1625-1748
    ADJ-31        FULL     derivations/CANONICAL_INTERACTION.md is the ratified governing source
                           DECISION_LOG.md:667-707, esp. :678 and :685
    ADJ-32        SUMMARY  R-1 files to the OPEN side, not the deferred side
                           DECISION_LOG.md:2147-2240
    ADJ-SET-0809  FULL     The three PI rulings of 2026-08-09, cited as a set (ADJ-04, ADJ-05, ADJ-06)
                           DECISION_LOG.md:1749-1826, :1827-1906, :1907-2004

**Four of the twenty-three are `SUMMARY` only.** `ADJ-14`, `ADJ-16`, `ADJ-17`
and `ADJ-18` are known to a register, which states what was ruled but does not
carry the ruling's words. **`G-08`'s evidence line points at a specification as
the place the ruling is recorded** — the same arrangement the ten in §1 are in,
differing only in that a register notices it. **Whether a summary record is
sufficient provenance is not decided here.**

---

## 3. `M5` — every block claiming to reproduce a ruling, compared

**A label asserting faithfulness is not evidence of it**, so each block was
compared against the source the repository holds, under one normalisation
applied to both sides: strip blockquote prefixes, strip code and emphasis
delimiters, collapse whitespace including line breaks.

    BLOCK                                              SOURCE COMPARED AGAINST            RESULT
    decisions/README.md:31-34                          decisions/2026-08-20-adjudication   FAITHFUL
      "PI RULING, adopted verbatim:"                     -source.md:78-81
    docs/GOVERNANCE-DEBT.md:307-312                    the same source, item 2            DIVERGENT
      "PI RULING, registered verbatim:"                  (:106-113)
    CONVENTIONS.md:1494-1496                           decisions/2026-08-19-inconclusive  FAITHFUL
      "PI RULING, adopted verbatim:" (Rule 22)           -disposition.md:11-13
    DECISION_LOG.md:1246-1258                          specs/2026-08-08T1634Z_exponent-   FAITHFUL
      "reproduced verbatim:"                             mapping-ruling.md:20-32
    DECISION_LOG.md:1403-1412                          specs/2026-08-09T0300Z_attraction  FAITHFUL
      "reproduced verbatim:"                             -ruling-and-layers.md:20-29
    DECISION_LOG.md:1023-1032                          specs/2026-08-07T1320Z_integrate-  FAITHFUL
      "reproduced verbatim:"                             fierz-and-sign-ruling.md:23-32

**The one divergence is the item-2 case**, already measured and already
disposed of additively beneath `G-13`. Both texts are landed there and are not
restated here.

**Blocks for which NO SOURCE IS AVAILABLE FOR COMPARISON.** Every block set out
in §1 claims to reproduce a ruling — `recorded verbatim as issued`,
`reproduced verbatim`, `recorded verbatim` — and **the repository holds no
independent source for any of them.** The claim cannot be tested either way.
That is recorded as the third of `M5`'s outcomes, not as a finding of
faithfulness and not as a finding of divergence.

**`CONVENTIONS.md:1456` (Rule 21) was not compared**: the repository holds no
separate source for the namespace ruling, its earliest record being the
specification that adopted it. Same outcome, same reason.

---

## 4. `M6` — the citation form

**Three distinct numbered adjudication sets are cited in the frozen scope, and
the form `PI ruling N` does not distinguish them.**

    SET 1   the seven-item adjudication on the returned items
            identified by      item number, 1 to 7
            landed at          decisions/2026-08-20-adjudication-source.md
            cited as           "PI rulings 1/2/4/7", "ruling 2", "ruling 4",
                               "ruling 7", "PI adjudication item 5"

    SET 2   the rulings following P2-RECON-01B-B0
            identified by      ruling number, 1, 2 and 4
            landed at          NOWHERE — this is ADJ-25 of §1
            cited as           "PI rulings 2 and 4", "PI ruling 4",
                               "PI ruling 2"

    SET 3   the numbered points of the registry-split ruling
            identified by      point number, 1 to 5
            landed at          DECISION_LOG.md:2433-2451
            cited as           not cited by number from outside the entry

**`ruling 2` and `ruling 4` each resolve to TWO of these sets**, and nothing in
the citation distinguishes them:

    resolves to SET 1   decisions/README.md:70, :71, :87
                        docs/GOVERNANCE-DEBT.md:582
                        specs/2026-08-19T2324Z_gov-housekeep-02.md:74, :247, :254
                        specs/2026-08-20T0042Z_proj-01-class-01.md:50

    resolves to SET 2   derivations/P2-RECON-EXT-01_discarded-external-space.md:14,
                        :421, :437, :471
                        specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:8, :43-62

**A citation resolving to NONE.** `derivations/P2-DEFERRED-ITEMS.md:199` cites
"the `D-pre-A` ruling on the canonical kinetic operator" as the authority for
`DEFERRED-04`. **No such ruling is landed anywhere in the frozen scope**, and
the `D-pre-A` dossier itself carries no ruling text. The citation names an
authority the searched scope does not contain. That is `ADJ-28`.

**A named form with the same defect.** `PI ruling of this session` occurs four
times with three different referents:

    specs/2026-08-19T1723Z_registry-split-01.md:7          the registry split
    specs/2026-08-19T0419Z_branching-science-01.md:7       items A and D
    specs/2026-08-20T1050Z_obs-ident-01.md:8               the OBS-IDENT ruling
    derivations/P2-OBS-IDENT-01_observable-identity.md:5   the OBS-IDENT ruling

**It resolves only through the artifact's own date and subject**, never through
the phrase. **Whether either form should change is not decided here**, and no
change is proposed.

---

## 5. The forms searched, and the exclusions stated for each

The search ran over committed blobs at the evidence base, by
`scripts/diagnostics/provenance_census_01.py`, which discovers and classifies
nothing.

    A_NUMBERED   a citation identifying an adjudication by number
                 EXCLUDED: a following four-digit year, so "decision
                 2026-08-06" is a date reference; "Rule N" and "Amendment X",
                 which name governance rules rather than adjudications

    B_LABELLED   a block labelled as carrying or reproducing a ruling
                 EXCLUDED: "verbatim" unqualified by adopted / registered /
                 recorded / reproduced, which in this repository is ordinary
                 usage about preserved text

    C_PI_ACT     prose asserting the PI performed an adjudicative act
                 EXCLUDED: "PI" inside a longer token, by the word boundary

    D_INDIRECT   an indirect or passive assertion that an adjudication
                 occurred, including the act named as a noun
                 EXCLUDED: "ruled" with no adjudicative subject; "ruler" and
                 "ruled out", by the word boundary and the verb list

    E_REGISTER   a pointer to a register where adjudications are filed
                 EXCLUDED: nothing at match time. A bare directory mention
                 citing no particular adjudication is excluded by reading

    raw hits                     369 lines
    grouped into passages        270   (hits within 6 lines of one another in
                                        the same file form one passage)
    admitted to S_C by M1          263
    excluded at M1 on reading        7

**The seven excluded at `M1`, each with its reason** — these matched a form but
neither cite, describe, nor rely on an adjudication:

    derivations/P2-BETAV-CAMPAIGN_prereg.md:471
      concerns pre-registration statements recorded verbatim, not an adjudication
    derivations/P2-FIERZSUM-01.md:40
      concerns the scope of a REVIEW approval, which is not a PI adjudication
    specs/2026-08-13T0034Z_adopt-domain-labels.md:79
      `PI RULING` appears as a LABEL TOKEN in a label census, not as a citation
    specs/2026-08-13T0034Z_adopt-domain-labels.md:127
      `PI RULING` appears as a LABEL TOKEN in a vocabulary list
    specs/2026-08-13T0034Z_adopt-domain-labels.md:386
      `PI RULING` appears inside a grep pattern describing a search method
    specs/2026-08-18T0507Z_src-b0-source-side-scope.md:458
      describes a question the PI has asked, not a decision the PI made
    specs/2026-08-20T0042Z_proj-01-class-01.md:203
      an acceptance criterion about measurements recorded verbatim, not a ruling

---

## 6. `S_C` — every member, with its classification and reason

**Reason codes, defined once and carried by every member:**

    r1   PI RULING
         the passage is a landed block reproducing a ruling, or its immediate preamble identifying one
    r2   PI RULING
         the passage cites a specific, identified adjudication as authority for something
    r3   OPEN FINDING
         the passage records that a question is reserved for a PI decision NOT YET MADE; it decides nothing
    r4   DEPENDENCY DESCRIPTION
         the passage defines vocabulary, states a register's scope, or describes where adjudications are filed
    r5   DEPENDENCY DESCRIPTION
         the passage is a path or cross-reference naming no particular adjudication
    r6   EXECUTOR DISPOSITION
         the passage records a disposition the executor adopted, expressly NOT a PI ruling
    r7   RECOMMENDATION
         a Reviewer or Researcher proposed it and no PI agreement is evidenced
    r8   RATIFIED DISPOSITION
         a Researcher or executor acted and the PI agreed afterwards; the agreement is evidenced
    r9   INDETERMINATE
         the passage does not permit classification from the searched scope

**Set membership per row:** `A` marks a member of `S_A`; `P` marks a member of
`S_P`; `M` marks a member of `S_missing`. A row with no mark is in `S_C` only.

    ID    SETS  CLASS / reason        REFERENT      PATH:LINES

    C001  AP-   r1 PI RULING            ADJ-29        CONVENTIONS.md:473-476
    C002  ---   r4 DEPENDENCY DESCRIPTI               CONVENTIONS.md:1088
    C003  ---   r4 DEPENDENCY DESCRIPTI               CONVENTIONS.md:1169
    C004  AP-   r2 PI RULING            ADJ-18        CONVENTIONS.md:1386
    C005  AP-   r1 PI RULING            ADJ-09        CONVENTIONS.md:1456
    C006  AP-   r1 PI RULING            ADJ-10        CONVENTIONS.md:1492
    C007  ---   r5 DEPENDENCY DESCRIPTI               CONVENTIONS.md:1560
    C008  ---   r4 DEPENDENCY DESCRIPTI               DECISION_LOG.md:737
    C009  ---   r5 DEPENDENCY DESCRIPTI               DECISION_LOG.md:837
    C010  AP-   r1 PI RULING            ADJ-01        DECISION_LOG.md:1021-1023
    C011  AP-   r1 PI RULING            ADJ-02        DECISION_LOG.md:1244-1246
    C012  ---   r3 OPEN FINDING                       DECISION_LOG.md:1334
    C013  AP-   r1 PI RULING            ADJ-03        DECISION_LOG.md:1401-1403
    C014  AP-   r1 PI RULING            ADJ-04        DECISION_LOG.md:1757-1759
    C015  AP-   r1 PI RULING            ADJ-05        DECISION_LOG.md:1835-1837
    C016  AP-   r1 PI RULING            ADJ-06        DECISION_LOG.md:1915-1917
    C017  ---   r3 OPEN FINDING                       DECISION_LOG.md:2090
    C018  ---   r3 OPEN FINDING                       DECISION_LOG.md:2155
    C019  ---   r4 DEPENDENCY DESCRIPTI               DECISION_LOG.md:2204
    C020  ---   r3 OPEN FINDING                       DECISION_LOG.md:2249
    C021  ---   r6 EXECUTOR DISPOSITION               DECISION_LOG.md:2355
    C022  ---   r6 EXECUTOR DISPOSITION               DECISION_LOG.md:2367
    C023  AP-   r1 PI RULING            ADJ-08        DECISION_LOG.md:2425
    C024  ---   r4 DEPENDENCY DESCRIPTI               DECISION_LOG.md:2433-2451
    C025  ---   r3 OPEN FINDING                       DECISION_LOG.md:2478-2482
    C026  ---   r5 DEPENDENCY DESCRIPTI               DECISION_LOG.md:2503
    C027  AP-   r2 PI RULING            ADJ-11        DECISION_LOG.md:2673-2684
    C028  AP-   r1 PI RULING            ADJ-11        DECISION_LOG.md:2708-2709
    C029  ---   r4 DEPENDENCY DESCRIPTI               DECISION_LOG.md:2725
    C030  ---   r5 DEPENDENCY DESCRIPTI               DECISION_LOG.md:2765
    C031  A-M   r2 PI RULING            ADJ-22        GATES.md:1012
    C032  AP-   r2 PI RULING            ADJ-12        GATES.md:1049
    C033  AP-   r1 PI RULING            ADJ-10        decisions/2026-08-19-inconclusive-disposition.md:1-3
    C034  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-19-inconclusive-disposition.md:45
    C035  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-19-inconclusive-disposition.md:99
    C036  AP-   r1 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:1
    C037  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-20-adjudication-source.md:18
    C038  AP-   r1 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:78-88
    C039  AP-   r1 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:115
    C040  AP-   r1 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:136
    C041  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-20-adjudication-source.md:143
    C042  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-20-adjudication-source.md:156-160
    C043  AP-   r1 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:167-180
    C044  AP-   r2 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:217
    C045  AP-   r2 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:338-341
    C046  AP-   r2 PI RULING            ADJ-11        decisions/2026-08-20-adjudication-source.md:368
    C047  ---   r5 DEPENDENCY DESCRIPTI               decisions/2026-08-20-adjudication-source.md:389
    C048  ---   r4 DEPENDENCY DESCRIPTI               decisions/README.md:3
    C049  ---   r4 DEPENDENCY DESCRIPTI               decisions/README.md:15
    C050  AP-   r1 PI RULING            ADJ-11        decisions/README.md:27-31
    C051  AP-   r2 PI RULING            ADJ-11        decisions/README.md:42-62
    C052  AP-   r2 PI RULING            ADJ-11        decisions/README.md:70-92
    C053  AP-   r2 PI RULING            ADJ-31        derivations/CANONICAL_INTERACTION.json:2
    C054  ---   r4 DEPENDENCY DESCRIPTI               derivations/GOVERNANCE-ENFORCEMENT_classification.md:287
    C055  AP-   r1 PI RULING            ADJ-29        derivations/GOVERNANCE-ENFORCEMENT_classification.md:311
    C057  ---   r3 OPEN FINDING                       derivations/P2-BETAV-DET-01_measure-adjudication.md:291
    C058  AP-   r2 PI RULING            ADJ-01        derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md:83
    C059  AP-   r2 PI RULING            ADJ-01        derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md:22
    C060  A-M   r2 PI RULING            ADJ-28        derivations/P2-DEFERRED-ITEMS.md:77
    C061  ---   r4 DEPENDENCY DESCRIPTI               derivations/P2-DEFERRED-ITEMS.md:191
    C062  ---   r4 DEPENDENCY DESCRIPTI               derivations/P2-DEFERRED-ITEMS.md:199
    C064  ---   r3 OPEN FINDING                       derivations/P2-GAPB-BRIDGE-01_regime-transfer.md:476
    C065  AP-   r2 PI RULING            ADJ-02        derivations/P2-GENERATOR-SUM-CRITICALITY_01.md:32
    C066  ---   r3 OPEN FINDING                       derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md:387
    C067  ---   r3 OPEN FINDING                       derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md:445
    C068  ---   r3 OPEN FINDING                       derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md:407
    C069  ---   r3 OPEN FINDING                       derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md:513
    C070  A-M   r2 PI RULING            ADJ-27        derivations/P2-OBS-IDENT-01_observable-identity.md:5
    C071  ---   r3 OPEN FINDING                       derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md:108
    C072  ---   r4 DEPENDENCY DESCRIPTI               derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md:7-10
    C073  AP-   r2 PI RULING            ADJ-06        derivations/P2-PHASE-01_C3_curvature_asymmetry.md:170
    C074  ---   r3 OPEN FINDING                       derivations/P2-PHASE-01_channel_character.md:196
    C075  ---   r3 OPEN FINDING                       derivations/P2-PHASE-01_channel_character.md:368
    C076  AP-   r2 PI RULING            ADJ-01        derivations/P2-PHASE-01_channel_character_layers.md:5
    C077  AP-   r2 PI RULING            ADJ-05        derivations/P2-PHASE-01_diquark_both_eta.md:8
    C078  ---   r3 OPEN FINDING                       derivations/P2-PHASE-01_diquark_both_eta.md:365
    C079  ---   r3 OPEN FINDING                       derivations/P2-PHASE-01_diquark_sensitivity_addendum.md:187
    C080  AP-   r1 PI RULING            ADJ-01        derivations/P2-PHASE-01_fierz_sign_addendum.md:18
    C081  AP-   r2 PI RULING            ADJ-01        derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md:33
    C082  ---   r4 DEPENDENCY DESCRIPTI               derivations/P2-PHASE-01_input_admissibility_contract.md:21
    C083  AP-   r1 PI RULING            ADJ-12        derivations/P2-PHASE-01_input_admissibility_contract.md:37-41
    C084  AP-   r2 PI RULING            ADJ-06        derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md:9
    C085  ---   r4 DEPENDENCY DESCRIPTI               derivations/P2-PHASE-01_microscopic_parameter_domain.md:26
    C086  AP-   r1 PI RULING            ADJ-13        derivations/P2-PHASE-01_microscopic_parameter_domain.md:134
    C087  ---   r3 OPEN FINDING                       derivations/P2-POLE-B0_milestone-scope.md:678
    C088  ---   r3 OPEN FINDING                       derivations/P2-RECON-01B-B0_scope-assessment.md:532
    C089  A-M   r2 PI RULING            ADJ-25        derivations/P2-RECON-EXT-01_discarded-external-space.md:9-14
    C090  A-M   r2 PI RULING            ADJ-25        derivations/P2-RECON-EXT-01_discarded-external-space.md:421
    C091  A-M   r2 PI RULING            ADJ-25        derivations/P2-RECON-EXT-01_discarded-external-space.md:437
    C092  A-M   r2 PI RULING            ADJ-25        derivations/P2-RECON-EXT-01_discarded-external-space.md:471
    C093  ---   r3 OPEN FINDING                       derivations/P2-SRC-B0_source-side-scope.md:383
    C094  ---   r4 DEPENDENCY DESCRIPTI               docs/BRANCHING_POLICY.md:60
    C095  ---   r3 OPEN FINDING                       docs/BRANCHING_POLICY.md:252
    C096  ---   r4 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:29
    C097  AP-   r2 PI RULING            ADJ-16        docs/GOVERNANCE-DEBT.md:169
    C098  AP-   r2 PI RULING            ADJ-17        docs/GOVERNANCE-DEBT.md:186
    C099  AP-   r2 PI RULING            ADJ-17        docs/GOVERNANCE-DEBT.md:196
    C100  AP-   r2 PI RULING            ADJ-14        docs/GOVERNANCE-DEBT.md:283
    C101  AP-   r2 PI RULING            ADJ-14        docs/GOVERNANCE-DEBT.md:297
    C102  AP-   r1 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:305
    C103  AP-   r2 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:314
    C104  AP-   r1 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:352-353
    C105  AP-   r2 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:408
    C106  AP-   r1 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:453-456
    C107  AP-   r2 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:471-475
    C108  ---   r5 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:486-490
    C109  ---   r5 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:497
    C110  ---   r5 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:508
    C111  ---   r5 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:527
    C112  AP-   r2 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:547
    C113  AP-   r2 PI RULING            ADJ-11        docs/GOVERNANCE-DEBT.md:582
    C114  ---   r5 DEPENDENCY DESCRIPTI               docs/GOVERNANCE-DEBT.md:600
    C115  AP-   r2 PI RULING            ADJ-SET-0809  docs/amendments/2026-08-09_observation-and-propagation.md:120
    C116  AP-   r2 PI RULING            ADJ-SET-0809  docs/amendments/2026-08-09_observation-and-propagation.md:496
    C117  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T0456Z_role-model-and-executors.md:9
    C118  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T0456Z_role-model-and-executors.md:91-99
    C119  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-06T0456Z_role-model-and-executors.md:122
    C120  A-M   r2 PI RULING            ADJ-26        specs/2026-08-06T0456Z_role-model-and-executors.md:141
    C121  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T0456Z_role-model-and-executors.md:246
    C122  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T0456Z_role-model-and-executors.md:467
    C123  AP-   r1 PI RULING            ADJ-07        specs/2026-08-06T0456Z_role-model-and-executors.md:516-520
    C124  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T1218Z_role-model-clean-rebuild.md:40
    C125  AP-   r2 PI RULING            ADJ-07        specs/2026-08-06T1218Z_role-model-clean-rebuild.md:175
    C126  A-M   r2 PI RULING            ADJ-20        specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:783
    C127  A-M   r1 PI RULING            ADJ-20        specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:802
    C128  A-M   r2 PI RULING            ADJ-20        specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:824
    C129  ---   r3 OPEN FINDING                       specs/2026-08-07T1159Z_grassmann-crossing-sign.md:65
    C130  AP-   r2 PI RULING            ADJ-01        specs/2026-08-07T1159Z_grassmann-crossing-sign.md:146
    C131  ---   r3 OPEN FINDING                       specs/2026-08-07T1159Z_grassmann-crossing-sign.md:306
    C132  AP-   r2 PI RULING            ADJ-01        specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:6
    C133  AP-   r1 PI RULING            ADJ-01        specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:21-23
    C134  A-M   r1 PI RULING            ADJ-19        specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md:130
    C135  AP-   r2 PI RULING            ADJ-01        specs/2026-08-07T1424Z_freeze-checker-sign-repair.md:40
    C136  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-07T1437Z_branch-deletion-policy.md:68
    C137  ---   r3 OPEN FINDING                       specs/2026-08-08T1321Z_channel-character.md:196
    C138  AP-   r1 PI RULING            ADJ-02        specs/2026-08-08T1634Z_exponent-mapping-ruling.md:20
    C139  AP-   r2 PI RULING            ADJ-02        specs/2026-08-08T1634Z_exponent-mapping-ruling.md:116
    C140  AP-   r1 PI RULING            ADJ-02        specs/2026-08-08T1634Z_exponent-mapping-ruling.md:123
    C141  AP-   r2 PI RULING            ADJ-02        specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md:24
    C142  AP-   r2 PI RULING            ADJ-02        specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md:45
    C143  AP-   r2 PI RULING            ADJ-03        specs/2026-08-09T0300Z_attraction-ruling-and-layers.md:8
    C144  AP-   r1 PI RULING            ADJ-03        specs/2026-08-09T0300Z_attraction-ruling-and-layers.md:20
    C145  AP-   r2 PI RULING            ADJ-03        specs/2026-08-09T0300Z_attraction-ruling-and-layers.md:86
    C146  AP-   r2 PI RULING            ADJ-03        specs/2026-08-09T0346Z_integrate-attraction-and-layers.md:20
    C147  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-09T1711Z_integrate-rules-14-15.md:57
    C148  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T1958Z_pi-decisions-v3.md:1
    C149  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T1958Z_pi-decisions-v3.md:24
    C150  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T1958Z_pi-decisions-v3.md:47-53
    C151  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T1958Z_pi-decisions-v3.md:241
    C152  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md:1
    C153  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md:22
    C154  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md:93
    C155  AP-   r2 PI RULING            ADJ-SET-0809  specs/2026-08-09T2153Z_si1-deferred-02-crossref.md:26-32
    C156  ---   r3 OPEN FINDING                       specs/2026-08-09T2153Z_si1-deferred-02-crossref.md:183
    C157  ---   r3 OPEN FINDING                       specs/2026-08-09T2153Z_si1-deferred-02-crossref.md:206
    C158  ---   r3 OPEN FINDING                       specs/2026-08-10T0113Z_integrate-si1-crossref.md:97
    C159  AP-   r2 PI RULING            ADJ-05        specs/2026-08-10T0245Z_diquark-both-eta.md:26
    C160  AP-   r2 PI RULING            ADJ-05        specs/2026-08-10T0245Z_diquark-both-eta.md:56
    C161  ---   r3 OPEN FINDING                       specs/2026-08-12T1122Z_land-supply-protocol-v3.md:250
    C162  A-M   r1 PI RULING            ADJ-22        specs/2026-08-12T2258Z_adopt-parameter-domain.md:103-111
    C163  A-M   r1 PI RULING            ADJ-22        specs/2026-08-12T2258Z_adopt-parameter-domain.md:121
    C164  A-M   r2 PI RULING            ADJ-22        specs/2026-08-12T2258Z_adopt-parameter-domain.md:352
    C165  A-M   r2 PI RULING            ADJ-22        specs/2026-08-12T2258Z_adopt-parameter-domain.md:395
    C166  A-M   r2 PI RULING            ADJ-22        specs/2026-08-12T2258Z_adopt-parameter-domain.md:407
    C167  A-M   r1 PI RULING            ADJ-21        specs/2026-08-12T2326Z_adopt-domain-repair.md:68-72
    C168  AP-   r2 PI RULING            ADJ-13        specs/2026-08-13T0034Z_adopt-domain-labels.md:60
    C171  AP-   r1 PI RULING            ADJ-13        specs/2026-08-13T0034Z_adopt-domain-labels.md:144
    C173  AP-   r2 PI RULING            ADJ-06        specs/2026-08-13T0150Z_c1-complement-provenance.md:77
    C174  AP-   r2 PI RULING            ADJ-06        specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:177
    C175  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:280-283
    C176  AP-   r2 PI RULING            ADJ-06        specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:297
    C177  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:354
    C178  AP-   r2 PI RULING            ADJ-06        specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:464
    C179  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-13T0307Z_c3-curvature-asymmetry.md:553
    C180  AP-   r1 PI RULING            ADJ-12        specs/2026-08-13T0740Z_adopt-admissibility-contract.md:46-52
    C181  AP-   r2 PI RULING            ADJ-12        specs/2026-08-13T0740Z_adopt-admissibility-contract.md:228
    C182  AP-   r2 PI RULING            ADJ-12        specs/2026-08-13T0740Z_adopt-admissibility-contract.md:295
    C183  AP-   r2 PI RULING            ADJ-06        specs/2026-08-13T1149Z_integrate-phase01-line.md:161
    C184  ---   r3 OPEN FINDING                       specs/2026-08-13T1239Z_ac4-symmetry-goldstone.md:240
    C185  AP-   r1 PI RULING            ADJ-15        specs/2026-08-13T1424Z_integrate-ac4.md:74
    C186  A-M   r2 PI RULING            ADJ-23        specs/2026-08-14T1241Z_conventions-consolidation-ca.md:20
    C187  A-M   r1 PI RULING            ADJ-23        specs/2026-08-14T1241Z_conventions-consolidation-ca.md:27
    C188  A-M   r2 PI RULING            ADJ-23        specs/2026-08-14T1241Z_conventions-consolidation-ca.md:34
    C189  A-M   r1 PI RULING            ADJ-23        specs/2026-08-14T1241Z_conventions-consolidation-ca.md:206
    C190  A-M   r2 PI RULING            ADJ-23        specs/2026-08-14T1241Z_conventions-consolidation-ca.md:313
    C191  A-M   r1 PI RULING            ADJ-24        specs/2026-08-14T2135Z_integrate-conventions-ca.md:64-70
    C192  A-M   r1 PI RULING            ADJ-24        specs/2026-08-14T2135Z_integrate-conventions-ca.md:79
    C193  A-M   r2 PI RULING            ADJ-24        specs/2026-08-14T2135Z_integrate-conventions-ca.md:445
    C194  AP-   r1 PI RULING            ADJ-17        specs/2026-08-14T2307Z_integrate-mechanisms-cb.md:68
    C195  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-15T0008Z_debt-register-cc.md:26
    C196  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-15T0008Z_debt-register-cc.md:170
    C197  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-15T0008Z_debt-register-cc.md:449
    C198  ---   r3 OPEN FINDING                       specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:15
    C199  A-M   r2 PI RULING            ADJ-28        specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:41-47
    C200  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:227
    C201  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:590
    C202  ---   r3 OPEN FINDING                       specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md:18
    C203  ---   r3 OPEN FINDING                       specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md:63
    C204  ---   r3 OPEN FINDING                       specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md:128
    C205  ---   r3 OPEN FINDING                       specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md:332
    C206  ---   r3 OPEN FINDING                       specs/2026-08-17T0322Z_d1c-dependency-reduction.md:386
    C207  ---   r3 OPEN FINDING                       specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md:68
    C208  ---   r3 OPEN FINDING                       specs/2026-08-18T0142Z_det-01-measure-adjudication.md:76
    C209  ---   r3 OPEN FINDING                       specs/2026-08-18T0507Z_src-b0-source-side-scope.md:140
    C211  ---   r3 OPEN FINDING                       specs/2026-08-18T2124Z_eps-b0-scope.md:90
    C212  ---   r3 OPEN FINDING                       specs/2026-08-18T2325Z_integrate-eps-b0.md:47
    C213  ---   r3 OPEN FINDING                       specs/2026-08-19T0223Z_pole-b0-milestone-scope.md:68
    C214  ---   r3 OPEN FINDING                       specs/2026-08-19T0223Z_pole-b0-milestone-scope.md:146
    C215  AP-   r2 PI RULING            ADJ-14        specs/2026-08-19T0419Z_branching-science-01.md:7
    C216  AP-   r2 PI RULING            ADJ-14        specs/2026-08-19T0419Z_branching-science-01.md:19
    C217  AP-   r2 PI RULING            ADJ-14        specs/2026-08-19T0419Z_branching-science-01.md:49
    C218  ---   r3 OPEN FINDING                       specs/2026-08-19T0419Z_branching-science-01.md:264
    C219  AP-   r2 PI RULING            ADJ-32        specs/2026-08-19T0448Z_pole-b0-integ-02.md:276
    C220  ---   r3 OPEN FINDING                       specs/2026-08-19T0448Z_pole-b0-integ-02.md:391
    C221  ---   r3 OPEN FINDING                       specs/2026-08-19T0511Z_recon-01b-b0-scope.md:22
    C222  ---   r3 OPEN FINDING                       specs/2026-08-19T0511Z_recon-01b-b0-scope.md:34
    C223  ---   r3 OPEN FINDING                       specs/2026-08-19T0511Z_recon-01b-b0-scope.md:195
    C224  ---   r3 OPEN FINDING                       specs/2026-08-19T0511Z_recon-01b-b0-scope.md:286-291
    C225  A-M   r2 PI RULING            ADJ-25        specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:8
    C226  A-M   r2 PI RULING            ADJ-25        specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:43
    C227  A-M   r2 PI RULING            ADJ-25        specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:288
    C228  ---   r6 EXECUTOR DISPOSITION               specs/2026-08-19T1141Z_integrate-recon-ext-01.md:222-223
    C229  ---   r6 EXECUTOR DISPOSITION               specs/2026-08-19T1141Z_integrate-recon-ext-01.md:234
    C230  AP-   r2 PI RULING            ADJ-08        specs/2026-08-19T1723Z_registry-split-01.md:7
    C231  AP-   r2 PI RULING            ADJ-08        specs/2026-08-19T1723Z_registry-split-01.md:18
    C232  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:28-31
    C233  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:63
    C234  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:119
    C235  ---   r6 EXECUTOR DISPOSITION               specs/2026-08-19T1723Z_registry-split-01.md:164-195
    C236  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:236-245
    C237  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:257
    C238  ---   r6 EXECUTOR DISPOSITION               specs/2026-08-19T1723Z_registry-split-01.md:274-276
    C239  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:292
    C240  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T1723Z_registry-split-01.md:316
    C241  ---   r3 OPEN FINDING                       specs/2026-08-19T1723Z_registry-split-01.md:339-348
    C242  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2214Z_recon-proj-01.md:8
    C243  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2214Z_recon-proj-01.md:318-319
    C244  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:1
    C245  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:49
    C246  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:65-66
    C247  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:74
    C248  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T2324Z_gov-housekeep-02.md:84-90
    C249  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T2324Z_gov-housekeep-02.md:105-107
    C250  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T2324Z_gov-housekeep-02.md:138
    C251  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:152-173
    C252  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:199-204
    C253  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:311-313
    C254  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:354
    C255  AP-   r2 PI RULING            ADJ-11        specs/2026-08-19T2324Z_gov-housekeep-02.md:379-390
    C256  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-19T2324Z_gov-housekeep-02.md:447-448
    C257  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T0042Z_proj-01-class-01.md:50
    C259  ---   r3 OPEN FINDING                       specs/2026-08-20T0408Z_gapb-bridge-01.md:68
    C260  ---   r3 OPEN FINDING                       specs/2026-08-20T0408Z_gapb-bridge-01.md:235
    C261  A-M   r2 PI RULING            ADJ-27        specs/2026-08-20T1050Z_obs-ident-01.md:8
    C262  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:30
    C263  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:154
    C264  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-20T1705Z_adjudication-source-02.md:180
    C265  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:258
    C266  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:298-303
    C267  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:323
    C268  AP-   r2 PI RULING            ADJ-11        specs/2026-08-20T1705Z_adjudication-source-02.md:347
    C269  ---   r5 DEPENDENCY DESCRIPTI               specs/2026-08-20T1705Z_adjudication-source-02.md:358
    C270  ---   r4 DEPENDENCY DESCRIPTI               specs/2026-08-20T1705Z_adjudication-source-02.md:398

---

## 7. `M7` — the two statement pins, unchanged

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

This task modifies neither `CONVENTIONS.md` nor `assumptions/H-EXT-01.md`.

---

## 8. What this census does NOT establish

**`S_missing` is a measurement over the SEARCHED SCOPE, not over the
repository.** `reviews/` and `reports/` were not searched. That exclusion is a
scope decision recorded in the governing specification, not a finding that
nothing relevant sits there — and `reviews/pi/` in particular holds three
historical PI records, named at `docs/GOVERNANCE-DEBT.md:486-490`, which this
census could not read. **An adjudication landed only there would appear in
`S_missing` here and would not be missing.**

**A member of `S_missing` may have had authority whose record did not
survive.** Absence of surviving provenance is not evidence of absence of
historical authorisation. Nothing in §1 is a finding that a ruling was not
issued, or was issued without authority.

**No member's effective date is determined here.** The census records where
each adjudication is cited and whether a landed record was found. It fixes no
date, in either direction, for any of the thirty-three.

**Three further limits, stated because the natural reading of §0's table would
otherwise exceed them.** The counts are of PASSAGES, not of adjudications, and
the two differ by more than an order of magnitude in places. The classification
of a passage is a reading, and a different reader may classify differently at
the margin. And the `FULL`/`SUMMARY` distinction of §2 is this census's, not
governance's — **no rule in the repository says which of the two counts as
provenance.**

---

## 9. Open, and carried here rather than registered

**This task registers nothing.** It merges nothing, so it writes to no
register. The following are recorded in this artifact for a later task.

    THE SCOPE EXCLUSION      What a search including `reviews/` and `reports/`
                             would add is UNMEASURED. `reviews/pi/`'s three
                             historical records are the specific known case.

    THE CITATION FORM        `PI ruling N` resolves to two sets and
                             `PI ruling of this session` to three referents.
                             Whether either form should change is NOT DECIDED.

    THE LABEL PRACTICE       One block claiming to reproduce a ruling was found
                             not to. For the ten of §1 the claim cannot be
                             tested at all, no source being held. Whether the
                             untestable claims hold is UNDETERMINED.

    THE TWO TIERS            Whether a `SUMMARY` register record is sufficient
                             provenance is UNSETTLED, and four adjudications
                             turn on the answer.

    THE SHADOWING RISK       Two distinct rulings sit inside files whose other
                             passages cite a different ruling — `ADJ-19` inside
                             the Fierz integration specification and `ADJ-26`
                             inside the role-model specification. A per-file
                             attribution would have missed both. Whether other
                             files carry more than one ruling is UNMEASURED.

