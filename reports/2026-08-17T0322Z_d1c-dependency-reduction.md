# Report — `D-1c`: non-mathematical dependency reduction of the reflection-positivity gaps

    branch      science/d1c-dependency-reduction
    base        ec85f66b05b3ed92cd924bc75273b74a73eee23b   (authoritative main)
    measured at commit 3, 5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76
    main        NOT TOUCHED. No merge. Integration is a separate task.

**25 `UNFROZEN DATUM` occurrences → 5 `RULING` nodes.**
**8 `INCOMPATIBLE HYPOTHESIS` occurrences → 2 `ESTABLISHED FACT` nodes.**
**21 bridges and 9 undetermined entries untouched.**

**No node is sized, no candidate preferred, no ruling recommended, no
bridge judged.**

---

## 1. `A3` — environment conformance, run FIRST

**The normative execution order, and the order followed:**

    A3  environment conformance                     ran first
    A1  repository identity, refs, branch availability   ran second
    A2  review binding                              ran third
    A4  onward

**Criterion numbering is not execution order.**

    (0) execution location    /home/user/2-emergent-gravity; work in the
                              science/d1c-dependency-reduction worktree cut
                              from ec85f66b… by explicit SHA. MEASURED: six
                              worktrees present. SAME CONTAINER as the five
                              preceding tasks.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 447 commits on the
                              authoritative line. NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content
was touched by this criterion.**

**Rule 13 carries two diagnostic orders, a known open item. NO ENVIRONMENT
FAILURE OCCURRED**, and **neither order was exercised** — I am not naming
one as having applied.

## 2. `A1` — repository, refs, branch availability

**MEASURED, VERBATIM and NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix. `A1` accepts either form, and it identifies
`zetacheng/2-emergent-gravity`.**

**Refs, MEASURED after fetching:**

    refs/remotes/origin/main    ec85f66b05b3ed92cd924bc75273b74a73eee23b
    refs/heads/main             1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/remotes/origin/main` is `ec85f66b…`, as the evidence base requires.
No stop.** **`refs/heads/main` lags, and `A1` says a lagging local ref is
not a stop.**

**Branch availability, MEASURED BEFORE the branch was created:**

    git ls-remote origin 'refs/heads/science/d1c-dependency-reduction'   0 hits
    git branch --list 'science/d1c-dependency-reduction'                 0 hits

**It did NOT already exist, locally or remotely. No stop.**

**The pinned inputs, MEASURED at the evidence base — all five match the
pre-issue record to the digit:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md      66d5087ae6b064acf590a50c9a68d08c26607e7e
    derivations/P2-LATTICE-ONTOLOGY-01.md                             6544fb1a72eff49b4af4a1767d63405ddb87e4b8
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 0be773f6a52c759abd23438c66da6b43bca44930
    derivations/P2-LATTICE-ROUTE-01.md                                42be438ff1a4eb1994545cbadabe85cb1f448ad8
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   0b227206f3561144b4d5ea869390341aeefddc29

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       cadbe6d886e990f13ce26ee5e469c4b760850e39b2817927401a02f20abefe1d
    SHA-256 of the committed specification bytes      cadbe6d886e990f13ce26ee5e469c4b760850e39b2817927401a02f20abefe1d
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared.**

## 4. `A4` — the input inventory, re-derived

**Counted from `D-1b`'s per-entry tables, parsing the tag column of the six
`§3.x` tables. NOT by whole-file grep.**

    entries      52
    UD           25
    IH            8
    UB           21
    UNDETERMINED  9
    multi-tag    11
    occurrences  54

    per candidate     entries   UD   IH   UB   UNDET
    naive                  20    9    4    7       4
    Wilson                 13    5    0    7       3
    staggered              10    6    3    3       1
    overlap                 9    5    1    4       1

**Every figure matches the expected values.**

**I ran the whole-file grep as well, to confirm the criterion's warning
rather than take it on trust. MEASURED:**

    grep figure   UNFROZEN DATUM 6   INCOMPATIBLE HYPOTHESIS 6   UNESTABLISHED APPLICABILITY BRIDGE 6   UNDETERMINED 13
    true figure                  25                          8                                     21                9

**THE PER-ENTRY TABLE FIGURES GOVERN.** The grep counts definitions,
junction discussion and denials, because the artifact defines its own
vocabulary. **This is the third occurrence of that shape in this line** —
`D-pre-B0`'s `REFUTED` at five occurrences and zero cells, `D-1`'s `FAIL`
legend, and now the tag names.

## 5. `A5` — the `UNFROZEN DATUM` reduction

**Five `RULING` nodes, each with all six fields of `§3`. The full records
are in the ledger's `§3`; the summary:**

    node   datum                                          anchor (primary)             controls                     candidates            status
    R1     the canonical kinetic operator and its         ONTOLOGY:189                 W8 W9 n8 k7 s9          5    all four              OPEN
           parameters                                     ROUTE:189-190
                                                          dossier:169-170, 232-233, 274-275
    R2     the admissible lattice extent and              ONTOLOGY:192                 W3 n3 f3 f8 s3 s8 k3 k8 8    all four              OPEN
           finite-volume rules                            ROUTE:192-193
    R3     boundary conditions, temporal in particular    ROUTE:193, :202              W4 n4 f4 s4 k4          5    all four              OPEN
                                                          ONTOLOGY:27
    R4     the microscopic Euclidean variables,           ONTOLOGY:185                 W5 n5 f5 s5 k5          5    all four              OPEN
           state space and measure                        ROUTE:189
    R5     the internal multiplicity N                    CHANNEL-FREEZE:43            f7 s7                   2    naive, staggered      OPEN
                                                          ONTOLOGY:27

**THE THREE-WAY DECOMPOSITION OF ALL 25 OCCURRENCES:**

    N_mapped                   25      assigned to a VERIFIED-OPEN RULING node
    N_frozen_finding            0      CLASSIFICATION FINDING — ALREADY FROZEN
    N_undetermined_finding      0      CLASSIFICATION FINDING — STATUS NOT DETERMINABLE
                               --
                               25

    25 = 25 + 0 + 0

**Both finding counts are zero, so the decomposition reduces to `25 → 5`,
and I say so.**

    RATIO, over category 1 only:   25 occurrences  →  5 RULING nodes

**Every occurrence is dispositioned exactly once.** **No occurrence
appears under two nodes**, and the arithmetic 5 + 8 + 5 + 5 + 2 = 25 is
the check.

**One occurrence names two data and is dispositioned once.** `k8` reads
*"finite even extent and boundary data"*. **Its leading datum is the
extent and it is assigned to `R2`, once.** **Its text also touches `R3`'s
datum, which the ledger records as a note and NOT as a second
disposition** — counting it twice would break the exactly-once rule and
overstate `R3`'s reach. **Closing `R2` alone would not fully retire
`k8`**, and that is on the record.

## 6. `A6` — the `INCOMPATIBLE HYPOTHESIS` reduction

**Two `ESTABLISHED FACT` nodes, controlling all 8 occurrences.**

    node   fact                                                    anchor                                 controls              candidates
    F1     the H(4) lattice is four-dimensional, four axes         ONTOLOGY:62-64, 94-95                  f3 f6 s3 s6      4     naive, staggered
           equivalent, isotropy on the freeze list
    F2     the frozen U(N)_L × U(N)_R generator-sum interaction    CHANNEL-FREEZE:31-32, 36-37,           f1 f10 s1 k1     4     naive, staggered,
           with G > 0                                              40-41, 45                                                    overlap

    THE FULL 8-TO-2 MAPPING:

        F1   f3  f6  s3  s6     4
        F2   f1  f10 s1  k1     4
                               --
                                8

    8 occurrences  →  2 ESTABLISHED FACT nodes

**`f3` and `s3` appear in both the `UD` and the `IH` mapping, and that is
correct rather than double counting.** Each is a multi-tag entry: its `UD`
occurrence goes to `R2`, its `IH` occurrence to `F1`. **Two tag
occurrences of one entry, each dispositioned once in its own class**, and
`A5`'s 25 and `A6`'s 8 partition different sets.

## 7. `A7` — every `RULING` node verified against the repository

### 7.1 The four mandatory documents

**ALL FOUR WERE CHECKED FOR EVERY ONE OF THE FIVE NODES, without
exception:**

    derivations/P2-LATTICE-ONTOLOGY-01.md                             R1 R2 R3 R4 R5
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 R1 R2 R3 R4 R5
    derivations/P2-LATTICE-ROUTE-01.md                                R1 R2 R3 R4 R5
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   R1 R2 R3 R4 R5

### 7.2 The additional authoritative sources searched

**`§3` of the specification makes the four a minimum, not the authority
set, and `A7` requires `GATES.md`, `DECISION_LOG.md` and any registered or
frozen specification those documents reference to be searched for a LATER
ruling.** **All were, for every node.**

    GATES.md            kinetic operator, Wilson parameter, domain wall, overlap,
                        staggered, finite volume, infinite volume, thermodynamic,
                        lattice extent, lattice size, boundary condition,
                        microscopic measure, Grassmann measure, internal
                        multiplicity, large-N
    DECISION_LOG.md     kinetic operator, boundary condition, finite volume,
                        thermodynamic, microscopic measure, internal multiplicity,
                        reflection type, Wilson parameter
    referenced derivations, extracted from the four documents rather than guessed —
                        CANONICAL_INTERACTION.md, P2-GENERATOR-SUM-CRITICALITY_01.md,
                        P2-PHASE-01_C-CHECK_OPEN-ITEMS.md,
                        P2-PHASE-01_C3_curvature_asymmetry.md, u3-fierz/u3_fierz.md
    repository-wide phrase sweep —
                        "kinetic operator is frozen", "boundary condition(s) (are|is)
                        frozen", "extent is frozen", "volume is frozen", "measure is
                        frozen", "N is fixed", "canonical kinetic operator"

**MEASURED: NO LATER AUTHORITATIVE RULING EXISTS FOR ANY OF THE FIVE
DATA.**

**`DECISION_LOG.md` returns ZERO occurrences of every term searched.**

**Two hits needed reading rather than counting, and neither is a ruling:**

**`derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md:80` carries
`| Canonical kinetic operator and species accounting | DELEGATED: D-pre
(§4 obligation binds it) |`** — **the ontology's row quoted verbatim in a
second artifact.** It corroborates `R1` and supersedes nothing. **This is
exactly the case `§3` warns about — a ruling recorded elsewhere than the
derivation it governs — and here the elsewhere agrees.**

**`GATES.md` hits on "finite-volume" and "thermodynamic"** are a
Brillouin-zone tadpole fit at `:156`, a note on finite-volume grid
artifacts at `:694`, and thermodynamic dominance conditions at
`:1032`–`:1047`. **None rules on the admissible extent.**

**No node's status was settled by a source outside the four.** The four
supply every anchor; the additional search returned nothing that changes a
status.

### 7.3 The two levels of count, reported separately

**DATUM LEVEL — counting proposed dependencies:**

    N_ruling                  5      R1 R2 R3 R4 R5, all verified open
    N_proposed_frozen         0
    N_proposed_undetermined   0

**OCCURRENCE LEVEL — counting `UD` occurrences, per `A5`:**

    N_mapped                 25
    N_frozen_finding          0
    N_undetermined_finding    0

**These are different quantities and are not equated.** **5 ≠ 25 is not a
discrepancy**; one datum controls several occurrences, and `R2` alone
controls eight.

**THE MAPPING BETWEEN THEM, accounting for every occurrence exactly
once:**

    R1  →  W8 W9 n8 k7 s9                  5      \
    R2  →  W3 n3 f3 f8 s3 s8 k3 k8         8       |
    R3  →  W4 n4 f4 s4 k4                  5       |  25 occurrences,
    R4  →  W5 n5 f5 s5 k5                  5       |  each exactly once
    R5  →  f7 s7                           2      /
                                          --
                                          25   =  N_mapped

**This reproduces `A5`'s decomposition of 25 exactly.** **Reconciliation
means the mapping accounts for every occurrence once — not that the totals
match.**

**No node's datum turned out already frozen. Zero is an answer, not an
absence:** each of the five was searched across four mandatory documents,
two registers, five referenced derivations and a phrase sweep. **No
finding about `D-1b`'s classification arises**, and `D-1b`'s artifact is
not modified.

## 8. `A8` — the grouping rule, demonstrated not asserted

**All seven nodes control more than one occurrence. The shared datum or
fact, by name:**

    R1   the canonical kinetic operator is undelivered — ONE delegated row,
         ONTOLOGY:189. r, the mass/hopping domain, M_0 and the staggered
         phases are parameters OF that undelivered choice, and the dossier
         says so in its own words: M_0 is "part of the choice this dossier
         does not make", :274-275.
    R2   there is no frozen lattice extent — ONTOLOGY:192 delegates the
         admissible limits; ROUTE:192-193 lists finite-volume rules among
         what must still be frozen.
    R3   there is no frozen boundary condition — ROUTE:193 and :202.
    R4   there is no frozen microscopic measure — ONTOLOGY:185.
    R5   N is not fixed — CHANNEL-FREEZE:43 keeps it symbolic.
    F1   the lattice is four-dimensional — ONTOLOGY:62-64, 94-95.
    F2   the interaction is the frozen generator sum with G > 0 —
         CHANNEL-FREEZE:31-32, 36-37, 40-41, 45.

**NONE rests on wording, on a source paper, or on apparent similarity.
Every one rests on a line of a freeze document that identifies the datum
or the fact.**

**The test that shows this is not circular, and it is a measurement:**
`R2`, `R3` and `R4` each group occurrences drawn from **three different
papers** — `MP87`, `FG26` and `KU10`. **The grouping cannot be an artefact
of shared source text, because the sources are not shared.**

### 8.1 Pairs considered and NOT grouped

**Four, and the first is the sharpest.**

**`R2` and `R3` — named in the SAME SENTENCE and kept apart.**
`P2-LATTICE-ROUTE-01.md:192-193` reads *"…finite-volume and thermodynamic
rules; boundary conditions."* **One `*Freeze:*` sentence, one semicolon
between them.** **NOT GROUPED**: a ruling on the admissible volume fixes no
boundary condition, and a boundary-condition ruling fixes no extent.
**This is the rule in its purest form — shared wording, shared sentence,
shared delegation, and still two data.** **Grouping them would have turned
five nodes into four on the strength of a semicolon.**

**`R1` and `R4` — adjacent delegated rows, kept apart.** `ONTOLOGY:185`
and `:189` are two rows of one table, and `ROUTE:189` names *"microscopic
variables and measure; the canonical lattice Dirac operator"* in one
sentence. **NOT GROUPED**: the ontology delegates them as separate items to
different addressees, and freezing an operator does not deliver a measure.

**`R5` and `F1` — both arise inside `FG26`'s hypothesis list, kept
apart.** `FG26` requires even `N` and works in two dimensions, and both
mismatches appear in one sentence of `D-1`'s table. **NOT GROUPED**: one is
a programme datum awaiting a ruling and the other a programme fact already
settled — **different kinds, not merely different data.**

### 8.2 `MP87`'s two entries — the case named in advance

**`W6` and `n6` ended in NEITHER one node NOR two. They are
`UNESTABLISHED APPLICABILITY BRIDGE` occurrences and are OUT OF SCOPE
entirely**, per `§1` of the specification. **The reduction never reached
them.**

**The rule they motivated still did its work**, in the `R2`/`R3` rejection
at `§8.1`.

**And the positive half of the `MP87` story is worth stating.** `MP87`
contributes eight `UD` occurrences — `W3 W4 W5 W9` and `n3 n4 n5 n8` —
**and every one is grouped with `FG26` and `KU10` occurrences rather than
with its `MP87` sibling.** **The grouping cuts across papers, not along
them**, which is what a datum-based rule should do.

### 8.3 The grouping this ledger's ratio is most sensitive to

**`R1` groups four quantities — `r`, the mass/hopping domain, `M_0`, the
staggered phases — under one datum**, on `ONTOLOGY:189`'s single delegated
row and the dossier's own framing of `M_0` as *part of the choice*.

**The alternative is defensible and is recorded rather than omitted.** If
each operator parameter is taken as its own datum, `R1` splits into four
and the total becomes **eight nodes rather than five**, over the same 25
occurrences.

**The ledger takes the five-node reading and states the eight-node
reading beside it**, because the difference is a grouping judgement and
not a measurement. **A reader who disagrees with the call can see exactly
what it costs.**

## 9. `A9` — the out-of-scope tags

    UNESTABLISHED APPLICABILITY BRIDGE   21 occurrences
    UNDETERMINED                          9 entries

**Neither was grouped, classified, or judged.** **No node controls a `UB`
occurrence or an `UNDETERMINED` entry**, and none is mentioned in any
`CONTROLS` list.

**Why the bridges are excluded, in my own words.** A `RULING` node can be
settled by reading: either a document freezes the datum or it does not,
and that is a question about the repository. **A bridge is not that kind of
question.** Asking whether two bridges are one problem is asking whether
the same mathematics closes both — **and no amount of reading tables
answers it.** Doing it anyway would mean guessing at a mathematical
identity and recording the guess as a reduction, which would make the
ledger's central number partly fictional.

**And what the bridges' status actually is: `NOT ESTABLISHED IN THE
PRESENT EVIDENCE BASIS`.** `D-1`'s literature search was bounded and
`D-1b` re-read nothing. **Absence from the evidence is not absence from
mathematics**, and nothing here says the bridges do not exist.

**Why the undetermined entries are excluded.** They carry no
classification at all. **Putting one in a node would decide what it is** —
the determination `D-1b` declined to make on the evidence — **and would
decide it silently, as a by-product of grouping rather than as a finding.**

## 10. `A10` — no sizing, no selection, no closure judgement

**MEASURED. Searched the ledger, this report and all four commit
messages** for effort vocabulary — `cheap`, `expensive`, `easy`, `hard`,
`small`, `large`, `trivial`, `effort`, `cost`, `weeks`, `months`, `quick`,
`workload` — selection vocabulary — `select`, `prefer`, `rank`, `better`,
`best`, `favour`, `eliminate`, `recommend` — and closure/route phrasings —
*same mathematical problem*, *same bridge*, *shared closure*, *the ruling
should*, *one bridge would close*.

    ledger            effort vocabulary        6 hits, ALL denials or quotations
                      selection vocabulary     4 hits, ALL denials
                      closure / route          1 hit, and it is a denial
    this report       hits occur only in this criterion's statement of the search,
                      in denials, and in quotations of the ledger
    commit messages   0 hits of any kind

**The six effort hits itemised, so "all denials" is checkable:** *"A node
is not a cost. Five nodes are not five easy decisions"*; **two occurrences
of `large-N`, which is a quoted repository phrase and not an effort word**;
*"A NODE COUNT IS NOT A WORKLOAD"*; *"five distinct questions, not five
easy ones"*; *"does not make the ruling easier"*.

**The single closure hit is** *"whether two such bridges are the same
problem would take mathematical judgement this file does not make"* — a
statement that the judgement was not made.

**No sentence estimates effort, ranks candidates, prefers one, judges two
bridges the same, or describes how a ruling would be made.**

**Treatment length per candidate, MEASURED.** The ledger is organised by
NODE rather than by candidate, so length is reported as the material each
candidate attracts:

    candidate    in-scope occurrences   entry-id mentions in the ledger   candidate-name mentions
    naive                12                      32                             10
    Wilson                5                      14                             10
    staggered             8                      20                             11
    overlap               6                      15                              7

**THE LENGTHS DIFFER, and the reason is arithmetic rather than
judgement.** In-scope occurrences differ by more than a factor of two —
naive 12, Wilson 5 — because naive has two load-bearing bases and carries
both `UD` and `IH` occurrences, while Wilson has no `IH` occurrence at all.
**Mentions track occurrences almost exactly.**

**Levelling them would have required padding Wilson or compressing
naive**, and either would have misrepresented how much of `D-1b`'s
classified material bears on each. **Unequal length here is a fact about
the input, not a judgement about the candidates** — and Wilson's low
figure in particular follows from its zero `IH` count, which `§13.2` shows
is an artefact of the fetched theorem set.

## 11. `A11` — scope

**MEASURED, base to commit 3:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
    A   reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md
    A   specs/2026-08-17T0322Z_d1c-dependency-reduction.md

    3 additions, 0 modifications

**INTENDED, base to commit 4: 4 additions and 0 modifications**, the fourth
being this report. **INTENDED and not MEASURED: this report is written
before the commit containing it.**

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.** **None of the forbidden operations occurs.**

**On `append_only: DECISION_LOG.md`, and no conflict arose.** It is a
checker-configuration declaration, not an authorisation to write that
file, and `§8` limits executor-writable paths to this specification, its
review, its report and the ledger. **MEASURED: `DECISION_LOG.md` is
blob-identical at the head**, `§12`. **The two never appeared to conflict,
so no stop was required** — and had they, `§8` would have governed.

**The `{HHMM}Z` token, MEASURED against the clock this time:**

    date -u at branch creation      2026-08-17T0322Z
    commit 1 author date, UTC       2026-08-17T0322Z      MATCH
    token used in all four paths    2026-08-17T0322Z

**I measured the time and used the value I measured.** The preceding
task's token was forty-four minutes early; **this one agrees to the
minute**, and the token was fixed once by commit 1 and reused. **I chose
no path.**

## 12. `A12` — nothing existing changed

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      453
    compared                        453
    blob-identical                  453
    differing                         0
    missing at head                   0

**ZERO differing.**

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                                                          IDENTICAL
    CONVENTIONS.md                                                    IDENTICAL
    DECISION_LOG.md                                                   IDENTICAL
    docs/GOVERNANCE-DEBT.md                     (governance register) IDENTICAL
    docs/BRANCHING_POLICY.md                    (superseded register) IDENTICAL

    the four mandatory documents of §11:
    derivations/P2-LATTICE-ONTOLOGY-01.md                             IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 IDENTICAL
    derivations/P2-LATTICE-ROUTE-01.md                                IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   IDENTICAL

    all six microspec artifacts:
    …_kinetic-operator-dossier.md                                     IDENTICAL
    …_selection-discriminants.md                                      IDENTICAL
    …_plaquette-provenance.md                                         IDENTICAL
    …_tm-rp-scope.md                                                  IDENTICAL
    …_rp-literature-coverage.md                                       IDENTICAL
    …_rp-gap-classification.md                                        IDENTICAL

    scripts/    60 paths,  0 changed
    tests/      21 paths,  0 changed
    results/    69 paths,  0 changed

**`D-1b`'s classification and `D-1`'s tables are both unchanged**, and so
are the four documents every `RULING` node was verified against. **A task
that verified a node against a file and then altered that file would have
moved its own evidence.**

**No register entry was added anywhere.**

## 13. `A13` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**THE STATUS LINE WAS READ SCOPED TO ITS GATE SECTION**: the heading is at
`GATES.md:971` and the status line was taken as the offset `971 + 2`. **A
bare first-hit grep returns line 209, a different gate.**

**The pins were verified by RECOMPUTING the target digests:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md    identical

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md    identical

## 14. `A14` — the checker, MEASURED at commit 3

    base   ec85f66b05b3ed92cd924bc75273b74a73eee23b
    head   5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   sha256 10c171d3b453a69f0db2c28b0cdce7705ec278fffa64f9301be696c5889a3d61
    run 1 EXCLUSIVE   exit 0   PASS   sha256 af7c149485a6477e069135cbc78c0cf956e7ec65f5e70d7554b934e8e437381a
    run 2 INCLUSIVE   exit 0   PASS   sha256 10c171d3b453a69f0db2c28b0cdce7705ec278fffa64f9301be696c5889a3d61
    run 2 EXCLUSIVE   exit 0   PASS   sha256 af7c149485a6477e069135cbc78c0cf956e7ec65f5e70d7554b934e8e437381a

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four.   commits_in_range 3

### 14.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly one
specification** — this task's own, the only one in range:

    specs/2026-08-17T0322Z_d1c-dependency-reduction.md
    stated 4 additions / 0 modifications    counted 4 / 0    parse OK

**`RUN 1` and `RUN 2` produced BYTE-IDENTICAL output at each prospectivity
reading**, because the range contains one specification. **That is not
evidence the two runs are the same check**: `RUN 2` names the subject and
`RUN 1` discovers it.

**The `C3` multi-specification residual did not arise, and the reason is
that there is one declaring specification, not that declarations agreed.**
**The two preceding integrations exercised the other half** — two
specifications in range, agreeing, no conflict — **so both halves are on
the record: the trigger is a DIFFERENCE between declarations, not their
number.** The residual is unchanged and remains unregistered.

### 14.2 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP,
and it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed
without exercising the append property — **which is the outcome `A11`'s
warning anticipates: the path is declared to the checker and never
written.**

### 14.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "head": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 14.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "head": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
      "specification_paths": ["specs/2026-08-17T0322Z_d1c-dependency-reduction.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass** —
`§8` forbids both. **`RUN 2` passed on its first invocation at both
readings.**

### 14.5 The output, verbatim, `INCLUSIVE` reading

**`RUN 1` and `RUN 2` are byte-identical here, verified by `diff`, so the
four invocations produce exactly TWO distinct byte strings. Both are
below.**

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md",
                "reports/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md",
                "specs/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "050323ab144175ee54b03fab3043e9f5dabd3702",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md"
                ]
              }
            ],
            "first_review_commit": "6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6",
            "first_work_commit": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "050323ab144175ee54b03fab3043e9f5dabd3702",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "050323ab144175ee54b03fab3043e9f5dabd3702",
            "first_commit_paths": [
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 14.6 The `EXCLUSIVE` reading

**MEASURED by `diff`, and this is the whole of the difference:**

    line 252 of 256:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line, and nothing else.** No property status, evidence field or scope
figure differs, and `commits_out_of_scope` is empty in all four.

## 15. `A15`, `A16` — validators and hygiene

**`A15`, MEASURED at commit 3, exit status 0:**

    324 passed, 2 deselected      in 43.26 s

**Expected 324 and 2; measured 324 and 2.**

**`A16`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   050323ab   spec: reduce the reflection-positivity gaps to their programme dependencies
               trailer hits 0      not amended
    commit 2   6f7fe5ff   review: pre-execution review for the dependency reduction
               trailer hits 0      not amended
    commit 3   5d2f3c2b   derivation: reduce the reflection-positivity gaps to five rulings and two facts
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`,
`claude.ai/code`, `Generated with`, `Claude-Session` and
`noreply@anthropic` returns ZERO.** **`P6` independently reports
`matches: []` for all three commits.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind.**

**Commits, MEASURED:**

    commit 1   050323ab144175ee54b03fab3043e9f5dabd3702   specs/2026-08-17T0322Z_d1c-dependency-reduction.md
    commit 2   6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6   reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md
    commit 3   5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76   derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md

**Commit 4's message, INTENDED:**

    report: five rulings and two facts control thirty-three of the gap occurrences

## 16. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 16.1 First junction — a node count is not a workload

**Twenty-five occurrences collapsing to five nodes means FIVE DISTINCT
QUESTIONS, NOT FIVE EASY ONES.**

**Each is a decision the PI has not made, on a question the programme has
not framed.** A ruling on the admissible lattice extent is one node and one
sentence in this ledger; **it is not one sentence of work.** **The ledger's
arithmetic says nothing about what any node costs to answer**, and
`B0`'s seven-to-eleven construction estimate is unchanged and not
re-derived.

**A low node count means the questions are fewer, not lighter.**

### 16.2 Second junction — the twenty-one bridges are untouched

**THIS IS THE LARGEST THING THIS TASK DOES NOT DO.**

**Nothing here establishes how many independent bridges the 21
`UNESTABLISHED APPLICABILITY BRIDGE` occurrences represent** — **one,
twenty-one, or anything between.** Establishing it needs mathematics this
task is forbidden.

**Those bridges are `NOT ESTABLISHED IN THE PRESENT EVIDENCE BASIS`.**
`D-1`'s search was bounded and `D-1b` re-read nothing. **They are not
said to not exist.**

**The count beside the reduction, so no reader takes a reduced `UD` figure
for a reduced total:**

    reduced here      25 UD  +  8 IH   =  33 of 54 tag occurrences
    not reduced       21 UB            =  21 of 54
    not classified     9 UNDETERMINED entries

**The reduction covers 33 of 54. It does not touch the other 21.**

### 16.3 Third junction — three bounded layers, and the bounds compose

**This ledger rests on `D-1b`'s classification, which rests on `D-1`'s
tables, whose literature search was bounded** — ten works fetched, one
encountered and not fetched, and its own artifact stating that absence of
`COVERED` is not an exhaustive non-existence claim.

**A GAP ABSENT FROM `D-1`'s TABLES IS ABSENT FROM THIS LEDGER.** A
programme datum that no fetched theorem happened to constrain has no
occurrence, and therefore no node — **and its absence here is not evidence
that the programme has frozen it.**

**Three layers, each bounded, and the bounds compose.** Nothing recovers
at layer three what was not visible at layer one.

### 16.4 Fourth junction — a node says nothing about what the ruling should be

**A `RULING` node asserts only that the programme has not decided
something.** **It says nothing about what the decision should be**, which
way it should go, or whether the question is ripe.

**The node's existence does not make the ruling easier.** Naming a
question is not progress toward answering it, and **`R2` is not closer to
settled for having eight occurrences depend on it than `R5` is with two.**

**THE LEDGER MUST NOT READ AS A TO-DO LIST**, and it does not: no node is
ordered, prioritised, recommended, or described as ready. **Nothing in it
suggests which ruling should be made first, or at all.**

## 17. Did reducing make me want to group a `UB` pair, size a node, or say which ruling should be made?

**All three. The first was the strongest, and it is the one the exclusion
in `§1` exists to stop.**

**Grouping a `UB` pair: strongest, and it presents itself as obvious.**
Reading the 21 bridges, the same phrases recur — `FG26`'s `H1`/`H2`/`H3`
for naive and staggered, `KU10`'s auxiliary-field junction, the
interaction-preservation step across all four. **After grouping 25
occurrences into five nodes by anchor, the hand wants to keep going**, and
the bridges look like they would collapse the same way. **They would not
collapse the same way, because the collapse would rest on nothing.** A
`RULING` node has an anchor line in a freeze document; **a `UB` grouping
would have only my impression that two unestablished bridges are the same
mathematics** — and `D-1b` already recorded that `MP87`'s two
same-sounding entries rest on two different proofs. **I grouped none of
them.**

**Sizing a node: moderate, and it arrives through the word "only".** `R5`
controls two occurrences and `R2` eight, and the sentence that forms
itself is *"`R5` is a small one"*. **It is a smaller number of
occurrences, and that is all it is.** Deciding what `N` the programme fixes
is not made easy by only two theorems having tripped over it. **No node is
described as small, large, cheap or ready anywhere.**

**Saying which ruling should be made: weakest, and the most specific.**
`R3`, the temporal boundary condition, is the node whose absence blocks the
most theorems from even being tested, **and it is very tempting to write
that the programme should rule on it first.** That is a recommendation, it
is outside this task, and **the previous executor's warning applies exactly
— the easiest boundary to cross is writing a figure or an ordering while
believing you are only describing someone else's task.** **Not written.**

**One further pull, specific to this task: to let `§8.3`'s alternative
decomposition become an argument for one reading.** I recorded that `R1`
could split into four, making eight nodes rather than five. **It would have
been easy to add "and five is the better reading because it makes the
reduction stronger", which is reasoning from the conclusion.** **The ledger
gives the evidence for the five-node call and records the alternative
without arguing for either on the strength of its ratio.**

**I confirm: I grouped no `UB` occurrence and no `UNDETERMINED` entry;
judged no two bridges the same problem and judged no shared closure;
estimated no effort and sized no node; recommended no ruling and ordered
none; re-fetched no source and read no work `D-1` cited; designed no lemma,
proof or construction; did not reopen `W6` or `n6`; selected, eliminated,
ranked and preferred no candidate; did not revise or re-derive `B0`'s
estimate; modified no file, including `D-1b`'s classification and `D-1`'s
tables; added no register entry; did not touch `main`; and pushed no ref
but this task's branch.**

## 18. Stops and clarifications

**NO STOP occurred.** All four checker invocations exited 0, `RUN 2` passed
at both prospectivity readings, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 18.1 `OBSERVATION_METHOD_ERROR` — one finding, and it is the specification's warning confirmed

**`A4` predicted the whole-file grep fails, and I ran it to check rather
than take it on trust. MEASURED: 6, 6, 6 and 13 against 25, 8, 21 and 9.**

**The prediction is exactly right, and it is now confirmed twice by
independent executions.** **I report it as a finding rather than a
near-miss of mine**: the warning is what prevented the error, and a later
task counting tags in these artifacts will meet the same trap.

**This is the third instance of the shape in this line** — `D-pre-B0`'s
`REFUTED` at five occurrences and zero cells, `D-1`'s `FAIL` legend line,
and now the tag names. **A whole-file grep over an artifact that DEFINES
its own vocabulary counts the definitions.** **Three occurrences is a
pattern, not a coincidence**, and every artifact in this line defines a
vocabulary.

### 18.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**`R1`'s grouping is a judgement, not a measurement**, `§8.3`. The
five-node figure depends on treating `r`, the mass/hopping domain, `M_0`
and the staggered phases as constituents of one delegated datum. **The
evidence for that is `ONTOLOGY:189` and the dossier's phrase *"part of the
choice this dossier does not make"* — good evidence, and not a
measurement.**

**Under the alternative the total is eight nodes.** **Both are in the
ledger.** **Which is right is a question for the PI, and this report does
not argue it on the strength of which ratio looks better.**

**Reported, NOT registered** — `§4` forbids adding a register entry.

### 18.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**`k8` names two data in one occurrence** — *"finite even extent and
boundary data"* — **and the exactly-once rule forces it into one node**,
`§5`. It is assigned to `R2`; its `R3` component is recorded as a note.

**The residual: the ledger's `CONTROLS` lists are therefore not a complete
statement of what closing a node would retire.** **Closing `R2` alone
would not fully retire `k8`.** **A later task computing "occurrences
retired per ruling" from the `CONTROLS` lists would be wrong by one, in
`R2`'s favour.** **Reported, NOT registered.**

### 18.4 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked at five points —
the evidence base, the classification artifact's blob, the four mandatory
documents' blobs, the whole-file-grep figures, and its own scope block —
**and MEASURED agrees at every one.**

**Its `A5` repair is the one to note approvingly.** An earlier draft
required every occurrence assigned to a `RULING` node, which contradicted
`§3` and `A7` — both of which permit a datum to turn out already frozen and
forbid such a node from being a `RULING` node. **A specification with no
legal path through an outcome it expressly permits is defective**, and the
three-way decomposition is the repair. **It was not exercised here — both
finding counts are zero — but a specification whose legal paths depend on
the answer would have been a stop if either had been non-zero.**

**Its `A7` two-level counting is likewise correct and load-bearing.** **5
and 25 are different units**, and an earlier draft asking them to
"reconcile" would have been unsatisfiable the moment one datum controlled
more than one occurrence — which `R2` does, eight times over.

### 18.5 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred**, `§1`; **neither of Rule 13's two
diagnostic orders was exercised**, and nothing was installed.

**No defect in the repository was found.** Every path at the evidence base
is blob-identical at the head; the gate invariants hold; both pins
recompute; the checker passes at both readings; the validators are
unchanged at 324 passed, 2 deselected.

### 18.6 What I would have specified differently

**`§3` requires a `RULING` node's status verified against the repository,
and `A7` names where to look, but nothing says what to do when one
occurrence names two data.** `k8` does, and the exactly-once rule and the
`CONTROLS` field pull in opposite directions on it. **I would have had `§3`
say that an occurrence naming a second datum is dispositioned once and
annotated**, which is what I did, **rather than leaving each executor to
invent the convention.**

**And `A8` asks for pairs considered and not grouped, which is the right
question, but not for groupings MADE that a reader might dispute.** `R1` is
the one that matters here and I reported it under `§8.3` on my own
initiative. **I would have had `A8` require the most disputable grouping
made, with its alternative**, because the rejected pairs show the rule was
applied and the disputable acceptance shows where the number is soft.

## 19. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A13`, `A15` and
`A16` for commits 1–3; `A14`'s four invocations with both configs and the
output verbatim; `A11`'s scope base-to-commit-3 at 3 additions and 0
modifications; commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; `A11`'s final
base-to-commit-4 scope of 4 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A11`'s final scope measured base-to-commit-4; `A14-final`, being `RUN 2`
re-run at commit 4; `A15` at commit 4; `A16` for commit 4; the exact push
command; the branch tip read back from the remote; confirmation that
`refs/heads/main` is unchanged at `ec85f66b…`.

**Nothing in this report claims to measure commit 4.**
