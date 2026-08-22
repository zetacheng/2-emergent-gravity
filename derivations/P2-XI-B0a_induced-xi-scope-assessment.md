# `P2-XI-B0a` — what the repository establishes about the induced ξ ledger

    Kind          SCOPE ASSESSMENT. Documentary reading only.
    Specification specs/2026-08-22T0156Z_xi-b0a.md
    Review        reviews/chatgpt/2026-08-22T0156Z_xi-b0a.md
    Evidence base main at 6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Computed      NOTHING. No ξ, no per-mode coefficient, no channel
                  contribution, no scaling. See §9 and `C9`.

**Every numerical value in this artifact is CITED from a landed statement at
the evidence base, with its path and line, and is NOT computed by this task.**
§8 lists them in one place.

---

## 0. Reading discipline used throughout

**A statement is landed if it is on `main` at the evidence base.** Being on
`main` does not make every statement the same kind of evidence; `M1` records
the kind and **this artifact does not rank the kinds**.

Two passages quoted below are in Cantonese, in a session log. They are
reproduced **verbatim first**; each English rendering is **a working
translation, identified as such**, and is not the landed text.

Every textual criterion was applied with one normalisation on both sides —
blockquote prefixes stripped, code and emphasis delimiters stripped,
whitespace including line breaks collapsed — and every probe reports the text
it matched, not only that it matched.

---

## 1. `M1` — provenance of the induced ξ result

Search forms: `xi_ind`, `ξ_ind`, `ξ_{ind}`, `xi_{ind}`,
`\xi_{\mathrm{ind}}`, over every blob at the evidence base. Every hit is
listed. **The `xi_h` / `ξ_χ` / `ξ_f` / `ξ_eff` quantities are separate objects
and are recorded separately in §1b** — §7 of the specification names `xi` as a
substring hazard and this is the hazard it names.

### 1a. Landed statements of the induced ξ result

    #  path:line                                          carries          kind of artifact
    ------------------------------------------------------------------------------------------------
    1  paper/emergent_gr_paper_v2_15.tex:115-124          value, regime    subject paper under
                                                                           verification (abstract)
    2  paper/emergent_gr_paper_v2_15.tex:1194-1231        value, chain     subject paper (Finding 4
                                                                           body; eq:xichain, eq:xiuniv,
                                                                           eq:xi16)
    3  paper/emergent_gr_paper_v2_15.tex:1237-1249        scaling, regime  subject paper (verdict
                                                                           paragraph)
    4  paper/emergent_gr_paper_v2_15.tex:1408-1409        dependency       subject paper
    5  paper/emergent_gr_paper_v2_15.tex:1427             consequence      subject paper
    6  paper/emergent_gr_paper_v2_15.tex:1600-1611        regime           subject paper (summary)
    7  results/recovered-2026/emergent_gr_paper_v2_7.tex  value, scaling,  archived EARLIER version of
                                                          regime           the subject paper
    8  derivations/P2-NORM-01_normalization_chain.md:26    the chain        repository derivation note
    9  derivations/P2-NORM-01_normalization_chain.md:72    caveat           repository derivation note
    10 derivations/P2-NORM-01_normalization_chain.md:81-86 sign, scaling   repository derivation note
    11 GATES.md:274                                        the chain        gate register (P2-NORM-01)
    12 GATES.md:309                                        sign, scaling    gate register (P2-NORM-01,
                                                                           "Reviewer verdict" field)
    13 GATES.md:1188-1192                                  sign, scaling    gate register (SI-2 gate,
                                                                           "Honest prior" field)
    14 CLAIMS.md:31                                        sign, scaling    claim register (P2-C8,
                                                                           status SUPPORTED)
    15 DECISION_LOG.md:124                                 sign, scaling    decision log (append-only)
    16 results/P2-NORM-01/README.md:11                     sign, scaling    results README
    17 results/P2-NORM-01/raw/normalization_chain.json:33  value at L=5     machine-generated raw
       and :38                                                             result (authoritative
                                                                           output of a script)
    18 scripts/normalization_chain.py:68,100,106,133,136   value, sign      script source and comments
    19 results/recovered-2026/session_log_full.md:153      value, chain     session log (Cantonese)
    20 results/recovered-2026/session_log_full.md:154      scaling, regime  session log (Cantonese)
    21 results/recovered-2026/session_log_full.md:169      scaling, regime  session log (Cantonese)
    22 results/recovered-2026/REPRODUCTION.md:42           sign             reproduction record
    23 scripts/recovered_2026/PROVENANCE.md:12             sign             provenance register
    24 scripts/recovered_2026/PROVENANCE.md:189            value            provenance register
    25 reports/2026-07-20_recovery-merge_report.md:91      sign             task report
    26 derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:220 sign, scaling  repository derivation note
                                                                           (reproducing the SI-2
                                                                           honest prior)
    27 HANDOFF.md:20, :58                                  sign, scaling    status document
    28 MIGRATION.md:11                                     sign             status document
    29 results/comparison/PAPER_COMPARISON.md:51           survival window  comparison table
    30 derivations/P2-FIERZSUM-01.md:111-118               DEFINITION       concept note, explicitly
                                                                           NOT REGISTERED
    31 derivations/P2-FIERZSUM-01.md:231-233, :342, :413,  upstream         concept note, explicitly
       :459-460                                            requirements     NOT REGISTERED
    32 derivations/P2-LATTICE-ROUTE-01.md:43, :115         UV character     repository derivation note
    33 derivations/P2-LATTICE-ONTOLOGY-01.md:349, :404     scope            repository derivation note
    34 scripts/recovered_2026/reproduce_check.py:51        sign             script source

The three components the specification names, as landed:

    value      `ξ_ind = 4Gβ_F(3 − L)`, and `ξ_ind = (1/6)(3 − L)` at
               sharp-cutoff criticality
               — paper:1214-1226; derivations/P2-NORM-01_normalization_chain.md:26,81
    scaling    `ξ_ind ≃ −(1/6)L < 0`, i.e. negative and growing in magnitude
               with `L`
               — paper:1244
    regime     `L ≫ 1`, "the logarithmically induced regime", called the
               qualifier "clean regime" at paper:120 and paper:1610
               — paper:1241-1243

### 1b. Adjacent ξ quantities that are NOT the induced ξ result

Recorded so that no reader takes them for it.

    xi_h       the graviton dim-6 coefficient measured by `seagull_check`,
               landed as converging toward `−1/6`
               — GATES.md:1279; results/recovered-2026/REPRODUCTION.md:24,42
    ξ_χ, ξ_f   dim-6 coefficients from `speed_check`
               — GATES.md:1254; REPRODUCTION.md:19-21
    ξ_eff      the survival-condition variable of the paper
               — paper:1173-1180
    ξ (scalar) the non-minimal coupling parameter of the action
               — CONVENTIONS.md:17

### 1c. Does any carry it as a reviewed derivation with a specification and a review?

**NO.**

Method: the introducing commit of each carrier line was read, and the
repository's complete `specs/` and `reviews/` inventories at the evidence base
were enumerated.

    line                                                introduced   commit
    GATES.md:274, :309;  CLAIMS.md:31                   2026-07-17   43d3fe1f
    derivations/P2-NORM-01_normalization_chain.md:81    2026-07-17   eddda676
    DECISION_LOG.md:124; paper:1244                     2026-07-17   f95f2eb4
    GATES.md:1189                                       2026-07-20   2d46fb73
    results/recovered-2026/REPRODUCTION.md:42           2026-07-20   4b5ed28b
    derivations/P2-FIERZSUM-01.md:111                   2026-08-03   405d269e

    earliest file under specs/    specs/2026-08-06T0456Z_role-model-and-executors.md
    earliest ChatGPT review       reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md

**Every landed statement of the induced ξ result predates the first
specification in the repository.** No file under `specs/` names `NORM-01`.
Two files under `reviews/` name it, both in
`reviews/claude/2026-07-19-paper2-followup.md`, which reviews a *branch state*
(`:3-4`) and carries **no** `Reviewed specification SHA-256` field — verified by
reading the file for that string and finding none.

`derivations/P2-FIERZSUM-01.md`, which carries the definition of `ξ_ind` at
`:111-112`, is landed as **"Concept note v6 (APPROVED FOR REGISTRATION AS
SPECIFIED, not registered)"** (`:1`) with **"Nothing here is registered or
authorized"** (`:3-4`), and `GATES.md:1374` states **"`P2-FIERZSUM-01` and the
Route D concept note remain in review and are not registered here."**

**This is a record of artifact kind, not a ranking of the kinds, and not a
statement that the result is wrong.**

---

## 2. `M2` — claims 1 to 4

Each claim is reproduced **as stated** in the specification's §0b, then
classified. The three admissible values are `ESTABLISHED`, `REFUTED`,
`UNDETERMINED BY READING`. A compound claim is `ESTABLISHED` only if every
substantive limb is established; `REFUTED` if landed state states at least one
required limb otherwise; `UNDETERMINED BY READING` in every other case.
**Silence is recorded as silence.**

### 2.1 `CLAIM 1`

> the −1/6 per mode is the universal conformal-coupling value from the
> heat-kernel a₁ convention

**Classification: `REFUTED`.**

Limbs and their separate evidence:

    L1a  "−1/6 per mode" is a landed object
         NOT SUPPORTED. Search forms `per mode`, `per-mode` return four
         landed occurrences, none about any 1/6 quantity:
           derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md:237
           reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:463
           scripts/recon2026/proca_curved.py:209
           specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md:267
         Search forms `-1/6`, `−1/6` return landed occurrences of three
         other objects only: `xi_h` (GATES.md:1279,1295;
         REPRODUCTION.md:24,42,45; reports/2026-07-20_gravity-engine-
         recovery_report.md:43,55,96), the Proca naive determinant sum
         (results/P2-HK-01/raw/hk_species.json:23, which
         results/P2-HK-01/README.md:33-37 states `β_V` is NOT assembled
         from), and `ξ_ind ≃ −(1/6)L` (paper:1244).

    L1b  the conformal-coupling value, in the landed a₁ convention
         CONTRADICTED. CONVENTIONS.md:17 states "The conformal value in
         `d=4` is `ξ = 1/6`." derivations/P2-HK-01_heat_kernel_species.md:71
         states "Conformal value `ξ=1/6`." CLAIMS.md:27 records
         P2-C4 as "conformal null at `ξ=1/6`".
         **The landed conformal-coupling value is `+1/6`.**
         The repository has additionally examined and rejected the
         convention under which it would sit at `−1/6`:
         derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md:320-322
         states that under the flipped `E`-sign convention `β_B(ξ)` "would
         read `−(1/2)K(1/6 + ξ)`, which has no zero at `ξ = +1/6`, and the
         conformal cross-check would fail", and `:544-546` records that
         the conformal cross-check "fails under the alternative".
         **This limb is carried by a derivation that does have a
         specification and a review** — specs/2026-08-17T1250Z_sign-01-
         anchor-reconciliation.md and reviews/chatgpt/2026-08-17T1250Z_
         sign-01-anchor-reconciliation.md.

    L1c  "universal" across species
         NOT SUPPORTED AS STATED. CONVENTIONS.md:16 gives
         `a_1 = tr[(1/6)R·𝟙 − E]`; the `(1/6)R·𝟙` term is common to every
         bundle, but the landed per-species `tr a_1/R` values are
         `1/6` (real scalar), `1/6 − ξ` (non-minimal scalar), `−1/3`
         (Dirac), `−1/3` (Proca vector part), `1/6` (Proca scalar part)
         — derivations/P2-HK-01_heat_kernel_species.md:62-68. The common
         term is the `1/6` multiplying the identity, not a per-species
         `1/6`, and its landed sign is `+`.

At least one required limb — `L1b` — is stated otherwise by landed state, so
the compound resolves to `REFUTED`. **What is refuted is the sign and the
"per mode" attribution, not the existence of a conformal value: the landed
conformal value is `+1/6` and is cross-checked.**

### 2.2 `CLAIM 2`

> a fermion monoculture provides no sign cancellation

**Classification: `UNDETERMINED BY READING`.**

**`A4` fired on this submeasurement.** A model-level question must be answered
to classify it, the executor does not decide it, the question is recorded in
`M6` as `Q-M8`, and the remaining claims continued.

Limbs and their separate evidence:

    L2a  "fermion monoculture" describes the content in question
         PARTIALLY SUPPORTED, IN ONE SENSE AND NOT THE OTHER.
         The ξ_ind computation's loop content is the fermion determinant
         alone: paper:1196-1206 states the fluctuation χ̃ "enters the
         fermion determinant only through the mass, `m = y(v + χ̃)`", and
         paper:1211-1212 inserts `Z ⊃ β_F m² ln m²`, the Dirac coefficient.
         The MODEL content is not a monoculture: paper:1427 calls it "the
         minimal fermion-plus-scalar content", and
         session_log_full.md:154 names it "minimal model(fermion +
         condensate scalar)".
         The term "monoculture" itself does not occur anywhere at the
         evidence base — search form `monocultur`, zero hits.

    L2b  "provides no sign cancellation"
         NOT SETTLED BY READING. No landed statement asserts or denies it
         for a fermion-only content. What landed state does state, and
         which bears on it:
           paper:1161-1167 — "minimal matter contributes negatively to
             `M_Pl²` at the scheme-independent level",
             `ΔM_Pl²|_log = −4 Σ_s β_s m_s² ln(Λ²/m_s²) < 0
             (minimal coupling)` — a sum over species in which every
             minimal-coupling species carries the same sign, so no
             cancellation arises among them;
           derivations/P2-HK-01_heat_kernel_species.md:84-87 — `β_B` and
             `β_F` share a sign, `β_V` does not;
           paper:1169-1172 — the landed sign-reversing lever is the
             non-minimal coupling, "which flips sign for `ξ > 1/6`",
             not the addition of a further species.
         **Landed state therefore attributes the absence of cancellation
         to minimal COUPLING rather than to fermion-ness**, which neither
         establishes nor refutes the claim as worded.

Some limbs are unsupported and none is contradicted, so the compound resolves
to `UNDETERMINED BY READING`. **This is not refutation.**

### 2.3 `CLAIM 3`

> boson-loop contributions enter with opposite sign at O(L)

**Classification: `REFUTED`.**

Limbs and their separate evidence:

    L3a  boson-loop contributions enter with opposite sign
         CONTRADICTED FOR THE MINIMAL SCALAR, SUPPORTED FOR THE PROCA
         VECTOR — and the claim as worded is unqualified, so the
         contradicted case controls.
         Contradicting: derivations/P2-HK-01_heat_kernel_species.md:84-86
         gives `β_B = −1/(192π²)` and `β_F = −1/(96π²)`, the same sign;
         paper:1161-1166 states "minimal matter contributes negatively",
         with the species sum covering scalars; and
         results/recovered-2026/session_log_full.md:101 states it
         directly. Verbatim:

         > Continuum **預期**:minimal coupling **嘅** scalar **同**
         > fermion **同號**(**都負**),**救命嘅係** non-minimal ξφ²R

         *A working translation, identified as such: "Continuum
         expectation: a minimal-coupling scalar and the fermion have the
         same sign (both negative); what saves it is the non-minimal
         ξφ²R." The Cantonese text above is the landed text.*

         Supporting, for a different boson: P2-HK-01:87 gives
         `β_V = +1/(64π²)`, and session_log_full.md:186 and :191 record a
         massive composite vector as "**同** scalar/fermion **相反符號、
         三倍強度**" — *a working translation, identified as such: "opposite
         in sign to scalar/fermion, three times the strength."*
         **So landed state states that whether a boson loop carries the
         opposite sign depends on its curvature-coupling and spin
         structure, not on its being a boson.**

    L3b  "at O(L)"
         SILENT. Search forms `O(L)`, `\mathcal{O}(L)`, `order L`,
         `linear in L`, `leading log` return no landed statement of the
         `L`-order of any boson-loop contribution to the induced ξ. The
         landed ordering of the boson fluctuation loop is in the loop
         counting, not in `L`: session_log_full.md:101 records it as
         "**boson fluctuation loop**(O(1) **對** fermion **嘅** O(N)…)"
         — *a working translation, identified as such: "the boson
         fluctuation loop (O(1) against the fermion's O(N))."*
         **Recorded as silence, which is `UNDETERMINED BY READING` at limb
         level, not `REFUTED`.**

At least one required limb — `L3a` — is stated otherwise by landed state, so
the compound resolves to `REFUTED`.

### 2.4 `CLAIM 4`

> "clean regime" as landed means precisely that boson fluctuation feedback is
> excluded from the ξ ledger

**Classification: `REFUTED`.**

Limbs and their separate evidence:

    L4a  the term "clean regime" appears in landed state
         ESTABLISHED. paper/emergent_gr_paper_v2_15.tex:120 and :1610;
         and in the archived earlier version at
         results/recovered-2026/emergent_gr_paper_v2_7.tex. See `M3`.

    L4b  its landed meaning is "boson fluctuation feedback is excluded
         from the ξ ledger"
         CONTRADICTED. The landed text glosses the term itself, and the
         gloss is about the mass hierarchy, not about which loops are in
         the ledger. paper:1241-1243, verbatim:

         > In the logarithmically induced regime $L \gg 1$, which is
         > precisely where the scheme-independent analysis is clean and
         > where the near-critical condensate naturally lives,

         The same sense is landed in the session log at
         session_log_full.md:154: "**而喺乾淨** regime(L ≫ 1,
         near-critical condensate **自然住嘅地方**),ξ_ind ≈ −L/6"
         — *a working translation, identified as such: "and in the clean
         regime (L ≫ 1, where a near-critical condensate naturally
         lives), ξ_ind ≈ −L/6."*
         **Landed state defines the term by `L ≫ 1` and by
         scheme-independence. No landed statement gives it the meaning the
         claim asserts.**

Landed state states the required limb `L4b` otherwise, so the compound
resolves to `REFUTED`.

**Recorded separately, because it is a different proposition and is not what
`CLAIM 4` asserts:** landed state does say that the boson fluctuation loop is
not in the computed object. `session_log_full.md:101` states

> fermion loop **喺** condensate background **嘅貢獻**(**即** ξ_ind v²R
> **嗰類**)**其實已經包含喺我哋計咗嘅** Z_cov(m=gv) **入面**——**所以真正新
> 嘅嘢係** **boson fluctuation loop**

*A working translation, identified as such: "the fermion loop's contribution
in the condensate background (the ξ_ind v²R kind) is in fact already contained
in the Z_cov(m=gv) we computed — so the genuinely new thing is the boson
fluctuation loop."*

**That is a statement about what the computation contains. It is not a
definition of "clean regime", and this artifact does not treat it as one.**

### 2.5 `CLAIM 5`

Reproduced as stated, because §0b states it and `C2` requires every claim of
§0b to appear as stated:

> no free parameter exists that could tune the combined total, which is what
> would make the question a two-sided test

**It carries no `M2` classification, and this task assigns it none.** The
specification's §0c removes it from `M2`: it is a universal negative, "**This
task therefore does not attempt to verify Claim 5**", and what is determined
instead is `Q5`. **`Q5`'s answer is in §4, and it is `NOT ANSWERABLE`.**

Recording no classification here is not evidence about `CLAIM 5` either way.

---

---

## 3. `M3` — the regime term

**Finding: the term is landed, and its landed sense is `L ≫ 1`.** It is
carried only by the subject paper and by a session log; **no repository-authored
derivation, gate, or register defines it.**

Forms searched, with what each excluded:

    FORM 1  `clean regime`, case-insensitive, line breaks collapsed, over
            every blob at the evidence base.
            HITS: paper/emergent_gr_paper_v2_15.tex ×2 (:120, :1610);
                  results/recovered-2026/emergent_gr_paper_v2_7.tex ×2.
            Matched text reported, not only the hit: at :120
            "fails in the clean regime, so the minimal model cannot";
            at :1610 "the survival condition ... in the clean   regime"
            (the double space is a line-break join).

    FORM 2  `clean` and `regime` within 80 characters, EITHER ORDER, line
            breaks collapsed.
            HITS: FORM 1's, plus one per paper file —
            "regime $L \gg 1$, which is precisely where the
            scheme-independent analysis is clean" (v2.15 at :1241-1242).
            **This is the form that located the definition**; FORM 1 alone
            would have found the term and missed its gloss.

    FORM 3  Cantonese `乾淨`.
            HITS: results/recovered-2026/session_log_full.md ×8, of which
            TWO are the regime sense (:154 "喺乾淨 regime(L ≫ 1…)" and
            :169 "機制乾淨嘅地方", *a working translation, identified as
            such: "where the mechanism is clean"*), and SIX are ordinary
            usage — :12, :80, :108, :113, :115, :202.

    FORM 4  `clean-regime`, hyphenated. Zero hits.

Exclusions, recorded as counts over the whole evidence base. The
case-insensitive string `clean` occurs **741** times; the regime sense accounts
for five Latin-script occurrences and two Cantonese ones. The excluded senses:

    clean-room / cleanroom      188   the βV reconstruction methodology
    clean clone                  63   the verifier's working procedure
    clean-rebuild / clean rebuild 31  a governance task name
    cleanup                       9   ordinary usage
    CLEAN-PASS / CLEAN PASS      12   the SI-2 verdict tier (GATES.md:1171)
    chirally clean                2   paper:1373, :1433 — a different
                                      property of an extraction

**`CLEAN-PASS` and "clean regime" are unrelated**, as the specification's §7
warns: `CLEAN-PASS` is a pre-registered SI-2 verdict tier (`GATES.md:1171-1174`),
not a regime in `L`.

**Does any landed statement define what the regime EXCLUDES?** No. The landed
gloss (paper:1241-1243) states what the regime IS — `L ≫ 1`, where the
scheme-independent analysis is clean and the near-critical condensate lives —
and states nothing about exclusion from a ledger. **Recorded as silence.**

**On "ledger":** the request's term "ξ ledger" is not landed. The string
`ledger` occurs at the evidence base overwhelmingly as "species ledger" (the
lattice species and doubling accounting) and as dependency ledgers. The one
landed use of "ledger" for a ξ decomposition is
`derivations/P2-FIERZSUM-01.md:552-558`, inside the concept note that
`GATES.md:1374` records as not registered.

---

## 4. `M4` and `Q5` — the boundary of the ξ ledger's upstream

**`Q5` = `NOT ANSWERABLE`.**

**`A4` fired on `M4`.** A model-level question must be answered before the
upstream can be delimited, the executor does not decide it, and per the
specification's §0c and `A4` the answer is `NOT ANSWERABLE` with the question
given as the reason.

**The question, which is itself landed as open** —
`derivations/P2-FIERZSUM-01.md:559-562`:

> Retained for the record: is the baseline-subtraction deliverable
> (§4.1) correctly identified as the primary one — i.e. does the programme
> intend SI-2 to measure `ξ(G)`, `Δξ(G) = ξ(G) − ξ(0)`, or the
> composite-sector piece?

Delimiting the upstream of "the ξ ledger" presupposes knowing which ξ the
ledger is of. `derivations/P2-FIERZSUM-01.md:152-156` states that without this
"'which term dominates' comparisons are comparisons of different observables".
**The executor does not choose the observable.**

### What was searched, and the candidate delimiting statements found

Recorded so the negative answer is auditable rather than asserted.

    CANDIDATE A   derivations/P2-NORM-01_normalization_chain.md:26 and
                  GATES.md:274 — the chain
                  `Z(m²) → β_s → 4 G_c β_F → ξ_ind = 4Gβ_F(3−L)`.
                  WHAT IT DELIMITS: the computational chain of the landed
                  Finding-4 result.
                  WHY IT DOES NOT SETTLE Q5: it delimits how one already-
                  chosen quantity was computed, not the set of choice
                  points upstream of a ledger. It is silent on whether
                  further contributions belong in `ξ_ind`.

    CANDIDATE B   derivations/P2-FIERZSUM-01.md:150-236 — eight enumerated
                  deliverables the gate "must freeze", including the target
                  observable and baseline (§4.1), the renormalization /
                  matching / normalization prescription in three layers
                  (§4.2), the exact functional and truncation, the
                  decoupling prescription, and the diagrammatic ledger.
                  WHAT IT DELIMITS: an enumeration of the choice points
                  for the CONTINUUM pipeline.
                  WHY IT DOES NOT SETTLE Q5: (i) the note is landed as
                  "Nothing here is registered or authorized" (`:3-4`) and
                  `GATES.md:1374` records it as "not registered"; (ii) its
                  own first deliverable is the undecided question quoted
                  above; (iii) `:193-204` records that the objects that
                  would close it — "the microscopic measure, kinetic
                  operator, species ledger, geometry map, curvature
                  estimator, the actual definition of the reference
                  equivalence class, or the continuum–lattice matching
                  map" — are not frozen, and that Test II is "recorded as
                  an UNRESOLVED UPSTREAM DEPENDENCY"; (iv) it covers the
                  continuum pipeline only, `:9-14` recording a parallel
                  lattice-native pipeline with its own concept note.

    CANDIDATE C   derivations/P2-FIERZSUM-01.md:552-558 — the decomposition
                  `ξ_matched(G) = ξ_matched(0) + Δξ_matched(G)`, "with all
                  three recorded separately as a mandatory decomposition
                  ledger".
                  WHAT IT DELIMITS: the shape of the eventual verdict
                  object.
                  WHY IT DOES NOT SETTLE Q5: it is inside the same
                  unregistered note, and it names the components of a
                  result rather than the choice points upstream of it.

    ALSO SEARCHED, NOTHING FOUND: `ledger` in a ξ sense outside
    CANDIDATE C (see `M3`); `free parameter` in connection with `ξ_ind`;
    any register entry (`GATES.md`, `CLAIMS.md`, `DECISION_LOG.md`,
    `derivations/P2-DEFERRED-ITEMS.md`, `docs/GOVERNANCE-DEBT.md`)
    delimiting the ξ upstream.

**`Q5`'s dependency on `CLAIM 4` also holds, and independently points the same
way.** The specification's §0c states that the ledger's boundary is what "clean
regime" would fix. `CLAIM 4` is `REFUTED` (§2.4): the landed sense of the term
is a regime in `L` and fixes no boundary on the ledger's contents. **That is a
finding, not a failure.**

**What `NOT ANSWERABLE` means here, stated so it is not over-read:** it means
no landed statement delimits the ξ ledger's upstream into a bounded set over
which a census could run. **It does not mean the upstream is unbounded, and it
does not mean `CLAIM 5` is false.** `CLAIM 5` cannot be given a bounded form
until something else fixes the boundary.

---

## 5. `M5` — `SI-2` scope and the overlap determination

### 5a. The landed `SI-2` scope statement, verbatim

`SI-2` is the Sea–Ice alias of the gate `P2-MULTIPHASE-GRAV-01`
(`GATES.md:1113-1114`). Its scope statement is `GATES.md:1120-1123`,
reproduced verbatim:

```
### Scope
Every phase from `P2-PHASE-01`; the full `K_ij(p)` including all
frozen-channel mixing; Paper 3 vector input. Verdict is one of three
pre-registered tiers (below).
```

`A3` does not fire.

### 5b. Determination: PARTLY WITHIN

**The request's question about per-channel contributions falls PARTLY WITHIN
`SI-2`'s scope.**

Reasoning, stated rather than asserted:

1. **Within, on the decomposition object.** `SI-2`'s eventual verdict object is
   landed as the total matched coefficient decomposed into three separately
   recorded parts — `ξ(0)`, `Δξ(G)`, `ξ(G)`
   (`derivations/P2-FIERZSUM-01.md:552-558`). A question asking what the
   induced ξ contains when the contributions are separated is a question about
   the components of that same decomposition. The same passage states that "A
   composite-sector contribution alone is diagnostic and may NOT serve as the
   death-verdict object" — a scope boundary drawn around exactly this kind of
   per-part reading.

2. **Within, on the input.** `SI-2`'s "Honest prior" already consumes the
   induced ξ result: `GATES.md:1188-1192` states "The minimal single-channel
   induced-gravity result gives `ξ_ind < 0` for `L ≫ 1`". A change in what
   that result contains is a change in `SI-2`'s stated prior.

3. **Outside, on the sense of "channel".** `SI-2`'s scope text says "the full
   `K_ij(p)` including all frozen-channel mixing", and the frozen channels are
   the Hubbard–Stratonovich / Fierz channel basis frozen by
   `P2-CHANNEL-FREEZE-01` (`GATES.md:1126-1127`, `GATES.md:874`). A
   decomposition of the induced ξ **by loop species** — fermion loop versus
   boson fluctuation loop — is not the HS channel basis, and the scope text
   does not name it. §7 of the specification names `channel` as a substring
   hazard, and this is the hazard.

4. **Outside, on the verdict.** `SI-2`'s scope text ends "Verdict is one of
   three pre-registered tiers", and the tiers at `GATES.md:1171-1180` are
   phase-space statements about a healthy phase. A per-species reading of ξ
   produces no such verdict.

**Consequence, recorded and acted on: `A5` fired.** The remaining measurements
were completed and this assessment is produced; **what stopped is the proposal
of any ordering or follow-on work.** The overlap is returned for a PI ruling.
This artifact proposes nothing.

---

## 6. `M6` — model-level questions, listed and unanswered

**Every question below is recorded. None is answered here, and the fact that a
question is listed is not evidence about its answer.**

    Q-M1  Which ξ observable is the ledger's subject — `ξ(G)`,
          `Δξ(G) = ξ(G) − ξ(0)`, or the composite-sector contribution?
          Landed as open at derivations/P2-FIERZSUM-01.md:559-562.
          This is the question `A4` fired on for `M4`.

    Q-M2  Does the condensate scalar's own fluctuation loop enter the ξ
          ledger, and at what order? session_log_full.md:101 identifies it
          as the genuinely new object and counts it O(1) against the
          fermion's O(N); no landed statement settles whether it enters.

    Q-M3  Does the Hubbard–Stratonovich decoupling's Jacobian or
          normalization contribute? derivations/P2-FIERZSUM-01.md:451-460
          states that any metric-, regulator- or curvature-dependent
          normalization "must be included in `ξ_ind`, not discarded as an
          irrelevant constant", and records the check as undone.

    Q-M4  Which masses enter, and over what window? session_log_full.md:186
          and :191 record an untested scenario with `m_f ≪ m_V ≪ Λ`;
          CONVENTIONS.md:22 fixes `L ≡ ln(Λ²/m²)` for a single `m`.

    Q-M5  Which determinant structure defines a composite vector's
          contribution? CONVENTIONS.md:19 records the Proca structure as
          "taken as an input from the paper".

    Q-M6  By what decomposition is the ledger to be read — by HS channel,
          by loop species, or by the `ξ(0)` / `Δξ(G)` / `ξ(G)` split?
          §5b records that these are not the same partition.

    Q-M7  Is the sign-carrying feature the species or the curvature-coupling
          and spin structure? session_log_full.md:177 and :197 state the
          latter; no registered artifact adjudicates it.

    Q-M8  At what level is "sign cancellation" to be assessed — within one
          loop species, across minimal-coupling species, or across the full
          matched coefficient? This is the question `A4` fired on for
          `M2.2`, and it depends on `Q-M1`.

---

## 7. `M7` — the two Statement SHAs

    A-EXT-01  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
              CONVENTIONS.md:129
    H-EXT-01  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
              assumptions/H-EXT-01.md:53

**This task alters neither, and modifies neither file.**

---

## 8. Numerical values appearing above — all CITED, none computed here

**No new physics quantity is computed by this task.** Each value below is
reproduced from a landed statement, with the statement's location.

    value                            cited from
    ξ_ind = 4Gβ_F(3 − L)             paper:1214-1216; M1 row 2
    ξ_ind = (1/6)(3 − L)             paper:1224; M1 row 2
    ξ_ind ≃ −(1/6)L < 0              paper:1244; M1 row 3
    ξ_ind at L=5: −0.6666…, −0.3333… results/P2-NORM-01/raw/
                                     normalization_chain.json:33,38; M1 row 17
    4G_cβ_F = 1/6                    paper:1222; M1 row 2
    m > 0.37Λ, m > 0.287Λ, m>0.368Λ  paper:1239; results/comparison/
                                     PAPER_COMPARISON.md:51; M1 row 29
    xi_h → −1/6 (n=8:−0.109,         GATES.md:1279; REPRODUCTION.md:24
      n=16:−0.142)                   — §1b, NOT the induced ξ result
    ξ_χ = −0.078, ξ_f = −0.250,      GATES.md:1254; REPRODUCTION.md:19-21
      Δξ = +0.17                     — §1b, NOT the induced ξ result
    conformal value ξ = 1/6          CONVENTIONS.md:17; P2-HK-01:71
    β_B = −1/(192π²)                 P2-HK-01:84
    β_F = −1/(96π²)                  P2-HK-01:86
    β_V = +1/(64π²)                  P2-HK-01:87
    β_B(ξ) flips sign for ξ > 1/6    paper:1171-1172
    tr a_1/R per species             P2-HK-01:62-68
    G_c = 8π²/Λ², G_c = 5.93         paper:1221, :1229
    741 'clean' occurrences and the  measured by this task over the evidence
      per-sense exclusion counts     base — a count of landed text, not a
                                     physics quantity

**The last row is the only number this task produced, and it is a count of
occurrences of a string in landed files, not a physics quantity.**

---

## 9. What this assessment does NOT establish

1. **No claim of §0b is established by this task's failure to find contrary
   evidence.** Where a claim is `UNDETERMINED BY READING`, no search was
   treated as exhaustive and no absence was converted into support.
2. **`UNDETERMINED BY READING` is not refutation.** `CLAIM 2` is undetermined.
   That means the repository does not settle it — not that it is false, and
   not that it is true.
3. **Nothing is computed.** No ξ, no per-mode coefficient, no channel
   contribution, no scaling was computed here. Every number is cited (§8).
4. **The ξ result's provenance kind is recorded and NOT ranked.** §1 records
   that no landed statement of the induced ξ result is carried by a reviewed
   derivation with a specification and a review. **That is a record of kind. It
   is not a statement that the result is wrong, not a statement that a session
   log is worth less than a derivation, and not a demotion of any register
   entry.** What weight each kind bears is not decided here.
5. It does not establish that the induced ξ result is right or wrong, that any
   species contributes with any sign, or that any total falls anywhere.
6. `Q5 = NOT ANSWERABLE` does not establish that the ξ ledger's upstream is
   unbounded, and does not bear on `CLAIM 5`'s truth.
7. The `SI-2` overlap determination is a reading of the landed scope text. **It
   makes no programme-priority decision and proposes no ordering.**

---

## 10. Open questions raised and not settled

    O-1  All eight questions of `M6`, none answered.
    O-2  Whether the artifact kind that carries the induced ξ result, as §1
         records it, is the kind the programme intends it to have. Raised by
         `M1`'s finding; not decided here, and not a defect finding.
    O-3  Whether "clean regime", landed only in the subject paper and a
         session log, needs a repository-side definition before it is used
         as a qualifier in any specification. Raised by `M3`; not decided.
    O-4  The `SI-2` overlap of §5b, returned for a PI ruling per `A5`.
    O-5  Whether a boson-loop contribution's `L`-order is a well-posed
         question before `Q-M1` is answered. Raised by `L3b`'s silence.

---

## 11. Abort conditions — what fired and what did not

    A1  base SHA differs from §0                     DID NOT FIRE
                                                     observed origin/main
                                                     6da1f7cb8ea1d28d7dead
                                                     b8a938c67365b28384c,
                                                     equal to §0
    A2  main moves during execution                  DID NOT FIRE
    A3  SI-2 scope statement cannot be located       DID NOT FIRE
                                                     located at GATES.md:1120-1123
    A4  model-level question needed                  FIRED TWICE, NARROWLY
                                                     M2.2 → CLAIM 2 classified
                                                     UNDETERMINED BY READING,
                                                     question recorded as Q-M8,
                                                     remaining claims continued;
                                                     M4 → Q5 = NOT ANSWERABLE,
                                                     question recorded as Q-M1
    A5  SI-2 overlap established                     FIRED
                                                     remaining measurements
                                                     completed, this assessment
                                                     produced, and the proposal of
                                                     any ordering or follow-on work
                                                     stopped
    A6  path outside the §0e manifest modified       DID NOT FIRE
