# Report — `D-1b`: classifying the reflection-positivity gaps

    branch      science/d1b-rp-gap-classification
    base        822cd4fbfe9bff6e43867caed95c5635344683d0   (authoritative main)
    measured at commit 3, 45f7b54a48a4395180c3e07e41b3c402829c3c4b
    main        NOT TOUCHED. No merge. Integration is a separate task.

**Fifty-two `FAIL` entries classified. Nine `UNDETERMINED`. Zero shared
closures established.**

**No gap is sized, no candidate is chosen, no proof route is designed.**

---

## 1. `A3` — environment conformance, before any measurement

**Run first, in Rule 13's diagnostic order extended by Amendment D's step
0.**

    (0) execution location    /home/user/2-emergent-gravity; work in the
                              science/d1b-rp-gap-classification worktree cut
                              from 822cd4fb… by explicit SHA. MEASURED: four
                              worktrees present. SAME CONTAINER as the three
                              preceding tasks.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 439 commits on the
                              authoritative line. NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content
was touched by this criterion.**

**Rule 13 carries two diagnostic orders, a known open item. NO ENVIRONMENT
FAILURE OCCURRED**, and **neither order was exercised** — I am not naming
one as having applied. The order above was run as `A3`'s conformance check,
not in response to a failure.

## 2. `A1` — repository, refs, and branch availability

**MEASURED, VERBATIM and NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix. `A1` accepts either form, and it identifies
`zetacheng/2-emergent-gravity`.**

**Refs, MEASURED after fetching:**

    refs/remotes/origin/main    822cd4fbfe9bff6e43867caed95c5635344683d0
    refs/heads/main             1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/remotes/origin/main` is `822cd4fb…`, as the evidence base requires.
No stop.** **`refs/heads/main` lags, and `A1` says a lagging local ref is
not a stop.** Every measurement here reads the remote-tracking ref or an
explicit SHA.

**Branch availability, MEASURED BEFORE the branch was created:**

    git ls-remote origin 'refs/heads/science/d1b-rp-gap-classification'   0 hits
    git branch --list 'science/d1b-rp-gap-classification'                 0 hits

**`science/d1b-rp-gap-classification` did NOT already exist, locally or on
the remote. No stop.** **A1 makes prior existence a stop because a second
name is not this specification's to choose**, and the check was made before
anything was created rather than discovered by a collision — which is how
the `D-1` line met this hazard as its preflight `3a`.

**The pinned inputs, MEASURED at the evidence base:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md   b9109c87ee8aa52ec96c9e095e6de85d2f1d8779
    derivations/P2-LATTICE-ONTOLOGY-01.md                           6544fb1a72eff49b4af4a1767d63405ddb87e4b8
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md               0be773f6a52c759abd23438c66da6b43bca44930
    derivations/P2-LATTICE-ROUTE-01.md                              42be438ff1a4eb1994545cbadabe85cb1f448ad8

**All four match the specification's pre-issue record to the digit.**

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       4b37e09bed455c116e1ad449d7715fbe0a0835c38c9fa7286af19a429feab406
    SHA-256 of the committed specification bytes      4b37e09bed455c116e1ad449d7715fbe0a0835c38c9fa7286af19a429feab406
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared.**

## 4. `A4` — the `FAIL` inventory, re-derived

**Re-derived, not carried.** The landed figures were not consulted while
counting; they were compared afterwards.

**My counting rule, stated so it is reproducible.** An entry is one
occurrence of the literal token `` `FAIL` `` inside a `§2.2` basis block of
the arriving artifact. **The legend paragraph defining `FAIL` is excluded** —
it sits above the first `#### ` heading and is skipped structurally, not by
a string filter. **`UNKNOWN AT ABSTRACT DEPTH` is a different token and is
counted separately, never as a `FAIL`.** Axis-table rows and
theorem-hypothesis prose are counted separately and then summed.

**This is the rule the previous executor stated, and I reproduced it rather
than substituting my own** — `§0` of the specification offers that choice
explicitly.

**MEASURED, per basis:**

    basis                                        rows   FAIL table   FAIL prose   UNKNOWN AT ABSTRACT DEPTH
    MP87 → Wilson                                   7            6            5                           0
    MP87 → naive                                    7            6            3                           0
    OS78 → Wilson (abstract-depth cross-check)      7            2            0                           6
    FG26 → naive                                    7            5            6                           0
    FG26 → staggered                                7            5            5                           0
    KU10 → overlap                                  7            5            4                           0

**MEASURED, per candidate, against the landed figures:**

    candidate     re-derived   landed   agree?
    naive                 20       20    yes
    Wilson                13       13    yes    (plus 6 UNKNOWN AT ABSTRACT DEPTH, counted separately, in both)
    staggered             10       10    yes
    overlap                9        9    yes

    total                 52

**All four agree, and the `UNKNOWN AT ABSTRACT DEPTH` figure agrees too.
No difference to report.**

### 4.1 One thing the token count does not capture

**MEASURED: two entries each carry THREE named hypotheses under a single
token.** `FG26 → naive` reads *"determinant reflection invariance (H1),
local Grassmann representation/factorization (H2), and kinetic cross-term
decomposition (H3) are each `FAIL`"*, and `FG26 → staggered` reads *"H1 …,
H2 …, and H3 … are all `FAIL`"*.

**So 52 tokens correspond to 56 named hypotheses.** **I classified at the
TOKEN level**, to stay commensurable with the inventory `A4` asks for, and
flagged both entries in the artifact. **This is not a difference from the
landed figures** — it is a property of the source that a token count cannot
show, and it is reported because a later task reading "52" as "52
hypotheses" would be wrong by four.

### 4.2 `§0`'s wording census, reconciled

**`§0` states the landed tables contain 24 occurrences of `unfrozen`, 7 of
`not mapped`, 2 of `not convention-mapped`, and 1 of `not frozen/mapped`.**

**MEASURED, whole file: 26, 7, 2, 1. MEASURED, `§2.2` only: 19, 6, 2, 1.
Neither is 24.**

**The figure is reproducible under a third region.** `unfrozen` occurs
twice in `§1`, the verdict-vocabulary section, and 24 times across `§2`
and `§4`–`§7` — the ledger, the mapping tables and the four candidate
sections. **`not mapped` is 7 under that same region, `not
convention-mapped` 2 and `not frozen/mapped` 1.** **All four figures are
correct under "everything except the vocabulary section", and I report the
region rather than a discrepancy.**

## 5. `A5` — every `FAIL` classified

**The full assignment is in the artifact, `§3`, entry by entry, per
candidate and per load-bearing theorem.** The five aggregate figures:

    UNFROZEN DATUM                       25 tag occurrences
    INCOMPATIBLE HYPOTHESIS               8 tag occurrences
    UNESTABLISHED APPLICABILITY BRIDGE   21 tag occurrences
                                         --
                                         54 tag occurrences

    entries carrying MORE THAN ONE tag   11
    entries UNDETERMINED                  9

**Arithmetic check, MEASURED: 52 entries − 9 undetermined = 43 tagged; 43
+ 11 multi-tag extras = 54 occurrences.** The five figures close.

**Per candidate:**

    candidate     entries   UD   IH   UB   UNDET
    naive              20    9    4    7       4
    Wilson             13    5    0    7       3
    staggered          10    6    3    3       1
    overlap             9    5    1    4       1

**Wilson carries ZERO `INCOMPATIBLE HYPOTHESIS` tags and that is not a
result about Wilson.** It follows from which theorems reached it: `MP87` is
a four-dimensional Wilson theorem, so the dimension conflict that produces
three of the eight `IH` tags elsewhere does not arise, and `OS78`
contributes two entries of which one is an access gap. **A zero here is an
artefact of the fetched set, not a property of the candidate**, and `§16.2`
says so where a reader meets the counts.

## 6. `A6` — `UNFROZEN DATUM` verified against the repository

**Every one of the 25 `UD` occurrences rests on an affirmative repository
statement.** **None rests on failure to locate a freeze.** Eight distinct
quantities carry them; the full table with quotations, files and lines is
the artifact's `§4`.

    quantity                              entries                        outcome
    lattice extent / finite volume        W3 n3 f3 f8 s3 s8 k3 k8        VERIFIED UNFROZEN
    temporal boundary condition           W4 n4 f4 s4 k4                 VERIFIED UNFROZEN
    microscopic measure                   W5 n5 f5 s5 k5                 VERIFIED UNFROZEN
    Wilson parameter r                    W8                             VERIFIED UNFROZEN
    mass / hopping domain                 W9 n8                          VERIFIED UNFROZEN (weakest — see below)
    overlap kernel M_0                    k7                             VERIFIED UNFROZEN
    internal multiplicity N               f7 s7                          VERIFIED UNFROZEN (symbolic)
    staggered phases / normalization      s9                             VERIFIED UNFROZEN

**The load-bearing quotations, MEASURED with file and line:**

    P2-LATTICE-ONTOLOGY-01.md:185   "Microscopic Euclidean variables, state space and measure | DELEGATED"
    P2-LATTICE-ONTOLOGY-01.md:189   "Canonical kinetic operator and species accounting | DELEGATED: D-pre"
    P2-LATTICE-ONTOLOGY-01.md:192   "Admissible thermodynamic / infinite-volume limits | DELEGATED"
    P2-LATTICE-ROUTE-01.md:192-193  "*Freeze:* … finite-volume and thermodynamic rules; boundary conditions."
    P2-LATTICE-ROUTE-01.md:202      "finite temporal extent; temporal boundary conditions"
    P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43   "`N` kept symbolic in all algebra"
    kinetic-operator-dossier.md:169-171  "`r = 1` is what the exploratory script uses, not something the repository freezes"
    kinetic-operator-dossier.md:232-233  "`M_0` is a convention this dossier states and does not choose"

**A delegation is affirmative evidence, and that is the load-bearing
reading.** The ontology's table is prefaced *"No known item on this list may
remain implicit"*, and a row reading `DELEGATED` states that the item is
assigned to a future artifact — **not that a freeze could not be found.**

**THE THREE COUNTS:**

    verified unfrozen        8 quantities, 25 tag occurrences
    verified frozen          0
    could not determine      0 among entries tagged UNFROZEN DATUM

**The third is zero BY CONSTRUCTION, not by luck.** An entry whose quantity
I could not verify was left `UNDETERMINED` and never received the tag.
**The nine `UNDETERMINED` entries are where that discipline landed**, and
reporting "0 could not determine" without saying so would misrepresent a
design choice as a finding.

**Where I looked.** `§2` names three files; **they were searched first and
are the basis for six of the eight quantities.** **Two — `r` and `M_0` —
are settled by a fourth**, `P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md`,
which names them where the three do not. **Reported rather than passed off
as coming from the named three.**

**The weakest of the eight, stated as such.** `mass / hopping domain` rests
on the kinetic-operator delegation, from which the absence of a frozen mass
parameter follows. **No repository text names a hopping parameter or a mass
domain at all.** That is an inference from an explicit delegation, not a
quotation about the quantity, and it is weaker than the `r` and `M_0`
evidence.

### 6.1 Where `D-1`'s table and the repository disagree

**Two entries, `W6` and `n6`, on one reading; zero on the other. Both are
reported.**

`MP87 → Wilson` axis 7 says the non-gauge specialization *"is **not
frozen** and demonstrated in the programme action"*; `MP87 → naive` axis 7
says it *"is **not fixed** in the programme"*.

**READ AS A CLAIM ABOUT PROGRAMME STATUS, the repository contradicts
them.** MEASURED, `P2-LATTICE-ONTOLOGY-01.md:26`: *"gauge bosons and
composite particles"* sit in the EMERGENT column, while the FUNDAMENTAL
column carries the fermionic variables, the Euclidean lattice action and
the lattice Dirac operator. **That the microscopic action is non-gauge is
settled, not open.**

**READ AS A CLAIM ABOUT THE THEOREM, they are correct**: what is not
established is that `MP87`'s gauge-theory result specializes to the
non-gauge case. **Both entries are tagged `UB` and neither is tagged
`UD`.**

    entries where D-1 asserts unfrozen and the repository shows frozen
        programme-status reading      2   (W6, n6)
        theorem reading               0

**Reported as a finding about `D-1`'s tables. The arriving artifact was NOT
modified**, and the classification artifact does not correct it.

**No other entry was found where `D-1`'s assertion about the repository
fails against the repository.**

### 6.2 Two quantities the repository does not settle either way

**`reflection type`, five entries.** MEASURED: the strings `site
reflection`, `link reflection`, `reflection type` and `reflection plane`
occur **ZERO** times across all three named files.
`P2-LATTICE-ONTOLOGY-01.md:181` freezes *"Reflection positivity of the
action"* as an OBLIGATION and `:70-79` requires it *"proved per declared
kinetic operator"* — **neither names a reflection type.**

**`observable algebra`, one entry.** MEASURED: one occurrence in the three
named files, `P2-LATTICE-ONTOLOGY-01.md:326`, inside a list of properties a
reconstructed continuum theory should have. **Not a freeze and not a
delegation.**

**`D-1` asserts both are unfrozen. The repository neither freezes them nor
affirmatively records them as open.** **Absence of a located freeze is not
evidence of non-freezing**, so these six entries are `UNDETERMINED`.

## 7. `A7` — the boundary cases

**ELEVEN, and they are the deliverable.** Each is set out in the artifact's
`§5` with its competing readings, the sentence weighted, and the
disposition. In brief:

    B1   W1, n1        MP87 axis 1, the missing interaction        UB   (IH refused: silence is not conflict)
    B2   W6, n6, o2    axis 7 gauge content                        UB   (UD refused: §6.1; IH refused: "plausible")
    B3   W7, k6        "not convention-mapped" normalization       UB   (UD available and not taken)
    B4   n7, f9        bare "operator normalization is FAIL"       UNDETERMINED
    B5   W2 n2 f2 s2 k2   reflection type                          UNDETERMINED  (largest group)
    B6   W10           observable algebra                          UNDETERMINED
    B7   f7, s7        even N against symbolic N                   UD   (IH refused: deferral, not constraint)
    B8   f11, s10      FG26's H1/H2/H3                             UB   (named in advance)
    B9   k1            KU10 axis 1                                 IH + UB, genuinely layered
    B10  o1            OS78 measure at abstract depth              UNDETERMINED  (evidence gap, not programme gap)
    B11  f3, s3        axis 3 carrying extent AND dimension        UD + IH

**Six of the eleven turned on a specific word in the source** — *added*,
*plausible*, *convention*, *symbolic*, *established*, *versus* — **and each
is quoted in the artifact.** **None was resolved by preference.**

**`B5` is the one I am least comfortable with and I say so in the
artifact.** `D-1` asserts non-freezing of the reflection type five times
and the assertion may well be right; it is simply not verifiable from the
repository, and `§2` of this specification is explicit that a search
finding nothing yields `UNDETERMINED`.

**`B9` is the clearest genuinely layered entry.** `KU10`'s main theorem
assumes a FREE theory, which conflicts with the frozen non-zero
interaction — `IH`. `KU10` also treats a chiral Yukawa interaction, where
what is missing is the auxiliary-field junction — `UB`. **Two source
results in one entry; forcing one tag would lose whichever was dropped.**

**The count is not zero, and `A7` explains why that matters:** a
classification with zero boundary cases and zero undetermined entries would
have assigned tags on a first read, which is what this task was split off
to prevent.

## 8. `A8` — shared subject and shared closure, in two layers

**ELEVEN `SHARED SUBJECT` relationships identified. ZERO `SHARED CLOSURE`
established.**

**`UNFROZEN DATUM` — 5 shared subjects:**

    temporal boundary condition       naive, Wilson, staggered, overlap    SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    lattice extent / finite volume    naive, Wilson, staggered, overlap    SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    microscopic measure               naive, Wilson, staggered, overlap    SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    internal multiplicity N           naive, staggered                     SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    mass / hopping domain             naive, Wilson                        SHARED SUBJECT / CLOSURE NOT ESTABLISHED

    r, M_0, staggered phases          candidate-specific                   NOT SHARED

**`INCOMPATIBLE HYPOTHESIS` — 2 shared subjects:**

    dimension 2 against the frozen 4       naive, staggered                SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    interaction differs from generator sum naive, staggered, overlap       SHARED SUBJECT / CLOSURE NOT ESTABLISHED

**`UNESTABLISHED APPLICABILITY BRIDGE` — 4 shared subjects:**

    FG26's H1/H2/H3                   naive, staggered                     SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    MP87's non-gauge specialization   naive, Wilson                        SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    interaction-preservation step     all four                             SHARED SUBJECT / CLOSURE NOT ESTABLISHED
    measure / auxiliary-field junction all four                            SHARED SUBJECT / CLOSURE NOT ESTABLISHED

**Why closure fails even for the boundary condition, which looks like the
strongest case.** One PI ruling fixes one temporal boundary condition —
**but the four theorems assume DIFFERENT boundary data**: `FG26`
anti-periodic in both directions, `KU10` anti-periodic time with periodic
space, `MP87` a finite-lattice setup with arbitrary reflection-plane
separation. **A single ruling would match some and exclude others**, and
`D-1`'s own entries say so: *"a different future ruling would exclude the
theorem"*, *"an incompatible ruling would exclude the theorem"*.

**`MP87`'s non-gauge specialization is the sharpest case and it surprised
me.** Both entries come from the same paper — **but from different results
inside it.** The Wilson entry rests on `MP87`'s own site-reflection
theorem; the naive entry rests on `MP87`'s DISCUSSION of the earlier
link-reflection proof at `r=0`. **Same paper, same-sounding gap, two
different proofs.** **Shared wording is not even shared theorem here**,
let alone shared closure.

**NO SHARED CLOSURE IS REPORTED ANYWHERE, and none may be read into the
table.** `A8` exists because a shared-subject finding presented as shared
closure would produce a construction saving the evidence does not support,
and **that saving would go straight into the next task's cost estimate.**

## 9. `A9` — no sizing, no selection

**MEASURED. Searched the artifact, this report and all four commit
messages** for effort vocabulary — `cheap`, `expensive`, `easy`, `hard`,
`small`, `large`, `trivial`, `effort`, `cost`, `weeks`, `months`,
`man-hours`, `quick` — for selection vocabulary — `select`, `prefer`,
`rank`, `better`, `best`, `favour`, `eliminate`, `recommend` — and for
route-design phrasings — *would be required*, *one would prove*, *the proof
would*, *to close this gap*, *constructing a lemma*.

    artifact          effort vocabulary        7 hits, ALL denials or quotations
                      selection vocabulary     3 hits, ALL denials
                      route-design phrasings   0 hits
    this report       hits occur only in this criterion's own statement of the
                      search, in denials, and in quotations of the artifact
    commit messages   0 hits of any kind

**The seven effort hits, itemised so "all denials" is checkable:** two are
the artifact's opening *"A tag is not a cost … does not mean small … does
not mean large"*; two are the same denial repeated in `§7`; one is
*"cheaper to close"* inside *"Nothing here establishes that …"*; one is
*"not made easier by being counted"*; **and one is `large-N limit` inside a
quoted repository line, which is not an effort word at all.** **A further
match, `trivial`, occurs in "a trivial gauge group" — a technical term for
the group, not a size claim.**

**No sentence anywhere estimates effort, ranks candidates, prefers one, or
describes how a gap would be closed.**

**Treatment length per candidate, MEASURED in words of the artifact's
per-basis classification blocks:**

    naive        355 words   (2 bases: MP87 → naive 159, FG26 → naive 196)
    Wilson       317 words   (2 bases: MP87 → Wilson 203, OS78 → Wilson 114)
    staggered    183 words   (1 basis)
    overlap      188 words   (1 basis)

**THE LENGTHS DIFFER, by roughly a factor of two, and the reason is
structural.** naive and Wilson each have TWO load-bearing bases; staggered
and overlap have one each. **The `FAIL` counts differ by the same factor —
20, 13, 10, 9 — and length tracks entry count, not importance.**

**Levelling them would have required either padding the one-basis
candidates or compressing the two-basis ones**, and either would have
misrepresented how much fetched material bears on each. **Unequal length
here is a fact about the literature, not a judgement about the
candidates.**

## 10. `A10` — scope

**MEASURED, base to commit 3:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
    A   reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
    A   specs/2026-08-16T2255Z_d1b-rp-gap-classification.md

    3 additions, 0 modifications

**INTENDED, base to commit 4: 4 additions and 0 modifications**, the fourth
being this report. **INTENDED and not MEASURED: this report is written
before the commit containing it.**

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.** **None of the forbidden operations occurs.**

**On the `{HHMM}Z` token, and it is wrong — see `§17.3`.** The token is
`2255Z`; **commit 1's UTC timestamp is `2339Z`.** The paths are internally
consistent and reused unchanged across all four commits, and the token does
not match the clock.

## 11. `A11` — nothing existing changed

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      446
    compared                        446
    blob-identical                  446
    differing                         0
    missing at head                   0

**ZERO differing. This range adds only.**

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                                                          IDENTICAL
    CONVENTIONS.md                                                    IDENTICAL
    docs/GOVERNANCE-DEBT.md                     (governance register) IDENTICAL
    docs/BRANCHING_POLICY.md                    (superseded register) IDENTICAL
    derivations/P2-LATTICE-ONTOLOGY-01.md                             IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 IDENTICAL
    derivations/P2-LATTICE-ROUTE-01.md                                IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md    IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md       IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md                IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md     IDENTICAL

    scripts/    60 paths,  0 changed
    tests/      21 paths,  0 changed
    results/    69 paths,  0 changed

**All five microspec artifacts are unchanged, and so are the three freeze
documents `§2` sends this task to read.** **A task that read the freeze
documents to verify a tag and then altered one of them would have moved its
own evidence**; none moved. **`D-1`'s tables are unmodified**, including
the two entries `§6.1` finds at odds with the repository.

**No register entry was added anywhere.**

## 12. `A12` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**THE STATUS LINE WAS READ SCOPED TO ITS GATE SECTION**, as `A12` requires:
the `P2-PHASE-01` heading is at `GATES.md:971` and the status line was taken
as the offset `971 + 2`. **A bare `grep 'Status: PROPOSED' | head -1`
returns line 209** — a different gate seven hundred lines above, reading
`Status: PROPOSED (deferred — not computed this sweep)` — **and would have
produced the right word from the wrong place.**

**The pins were verified by RECOMPUTING the target digests:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md    (identical)

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md    (identical)

## 13. `A13` — the checker, MEASURED at commit 3

    base   822cd4fbfe9bff6e43867caed95c5635344683d0
    head   45f7b54a48a4395180c3e07e41b3c402829c3c4b   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   sha256 306a4e968c23e44c54d950494bd03497b55523c29b2d560dbba378f7f0ea963a
    run 1 EXCLUSIVE   exit 0   PASS   sha256 763305e703a8d8cfdb87bcd7624cc24bcb7fe656b9ccd343551fe6b6893429a1
    run 2 INCLUSIVE   exit 0   PASS   sha256 306a4e968c23e44c54d950494bd03497b55523c29b2d560dbba378f7f0ea963a
    run 2 EXCLUSIVE   exit 0   PASS   sha256 763305e703a8d8cfdb87bcd7624cc24bcb7fe656b9ccd343551fe6b6893429a1

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four invocations.   commits_in_range 3

### 13.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly one
specification** — this task's own, the only one in range:

    specs/2026-08-16T2255Z_d1b-rp-gap-classification.md
    stated 4 additions / 0 modifications    counted 4 / 0    parse OK

**`RUN 1` and `RUN 2` produced BYTE-IDENTICAL output at each prospectivity
reading.** That is expected here and does not mean the two runs are the
same check: `RUN 2` names the subject and `RUN 1` discovers it, and they
coincide only because the range contains one specification.

**The `C3` multi-specification residual did not arise**, and the reason is
that there is one declaring specification, not that declarations agreed.
**The preceding two integrations exercised the other half** — two
specifications in range, agreeing, no conflict — **so both halves of the
diagnosis are now on the record: the trigger is a DIFFERENCE between
declarations, not their number.** The residual is unchanged and remains
unregistered.

### 13.2 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP,
and it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property.

### 13.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "head": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "head": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
      "specification_paths": ["specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"],
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

### 13.5 The output, verbatim, `INCLUSIVE` reading

**`RUN 1` and `RUN 2` are byte-identical here**, verified by `diff`, so the
four invocations produce exactly TWO distinct byte strings. **Both are
below, with no bytes omitted and none duplicated.**

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md",
                "reports/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md",
                "specs/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
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
                "commit": "7063a2a12326c029796ba241dd1d46cf2c35ce04",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "9e9f429f11dfcb72dd87798e22f236bd2ad37741",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md"
                ]
              }
            ],
            "first_review_commit": "9e9f429f11dfcb72dd87798e22f236bd2ad37741",
            "first_work_commit": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
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
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
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
              "commit": "7063a2a12326c029796ba241dd1d46cf2c35ce04",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "9e9f429f11dfcb72dd87798e22f236bd2ad37741",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
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
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
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
            "first_commit": "7063a2a12326c029796ba241dd1d46cf2c35ce04",
            "first_commit_paths": [
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
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

### 13.6 The `EXCLUSIVE` reading

**MEASURED by `diff`, and this is the whole of the difference:**

    line 252 of 256:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line, and nothing else.** No property status, evidence field or scope
figure differs between the readings, and `commits_out_of_scope` is empty in
all four.

## 14. `A14`, `A15` — validators and hygiene

**`A14`, MEASURED at commit 3, `python -m pytest` from the repository root,
exit status 0:**

    324 passed, 2 deselected      in 36.69 s

**Expected 324 and 2; measured 324 and 2.**

**`A15`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   7063a2a1   spec: classify the reflection-positivity gaps left by the literature audit
               trailer hits 0      not amended
    commit 2   9e9f429f   review: pre-execution review for the gap classification
               trailer hits 0      not amended
    commit 3   45f7b54a   derivation: classify the reflection-positivity gaps by how they close
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`,
`claude.ai/code`, `Generated with`, `Claude-Session` and
`noreply@anthropic` returns ZERO.** **`P6` independently reports
`matches: []` for all three commits.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind** — including for the token
error at `§17.3`, which Rule 20 does not cover.

**Commits, MEASURED:**

    commit 1   7063a2a12326c029796ba241dd1d46cf2c35ce04   specs/2026-08-16T2255Z_d1b-rp-gap-classification.md
    commit 2   9e9f429f11dfcb72dd87798e22f236bd2ad37741   reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
    commit 3   45f7b54a48a4395180c3e07e41b3c402829c3c4b   derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md

**Commit 4's message, INTENDED:**

    report: the reflection-positivity gaps are classified and none is sized

## 15. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 15.1 First junction — a classification is not a cost estimate

**NOTHING HERE ESTABLISHES THAT AN `UNESTABLISHED APPLICABILITY BRIDGE`
GAP IS CHEAPER TO CLOSE THAN AN `INCOMPATIBLE HYPOTHESIS` ONE** — only that
they close by different means. **A `UD` gap may close when a `D-pre` task
freezes the datum; an `IH` gap means that basis cannot cover; a `UB` gap
may close through a targeted applicability step.** **"May close through"
is not "is small".**

**`B0`'s seven-to-eleven construction estimate is UNCHANGED**, is not
re-derived here, and no tag count bears on it. **`D-1` replaced zero
construction units and this task replaces none either** — it describes the
four open burdens, it does not reduce them.

**This is said in the artifact at `§7`, where a reader meets the tag
counts**, and not only here.

### 15.2 Second junction — a tag distribution is not candidate evidence

**naive carries nine `UNFROZEN DATUM` occurrences and Wilson five. That
does not make either better supported.**

**A candidate whose gaps are mostly `UNFROZEN DATUM` is not closer to
admissible** — it is a candidate whose gaps depend on rulings the programme
has not made, **and those rulings are the PI's and are not made easier by
being counted.**

**The sharpest case is Wilson's zero `INCOMPATIBLE HYPOTHESIS` count**, and
it is exactly the shape a reader could misread. It follows from which
theorems reached Wilson — `MP87` is four-dimensional, so the 2D/4D conflict
never arises — **not from anything about the Wilson operator.** **A zero
produced by the fetched set is not a property of the candidate**, and
`§5` of this report says so where the counts appear.

### 15.3 Third junction — bounded by `D-1`'s tables

**This classification rests entirely on `D-1`'s tables, and `D-1`'s search
was bounded**: ten works fetched, one encountered and not fetched, and its
own artifact states that absence of `COVERED` "is not an exhaustive
non-existence claim."

**A GAP THAT DOES NOT APPEAR IN THOSE TABLES IS NOT CLASSIFIED HERE**, and
**nothing establishes the tables are complete.** A hypothesis `D-1` did not
record — because no fetched theorem raised it — has no entry and therefore
no tag, and its absence from this file is not evidence that it does not
exist.

**Nor does anything here conclude that missing mathematics does not
exist.** `D-1` established that the FETCHED literature does not supply it.

### 15.4 Fourth junction — which tags were independently verified

**Per tag, and the answer differs sharply:**

    UNFROZEN DATUM                       INDEPENDENTLY VERIFIED in this task,
                                         against the repository, quotation by
                                         quotation — §6.
    INCOMPATIBLE HYPOTHESIS              PARTIALLY verified. The PROGRAMME half —
                                         the frozen four dimensions, the frozen
                                         generator-sum interaction — was checked
                                         against the repository. The SOURCE half,
                                         what the theorem assumes, was not.
    UNESTABLISHED APPLICABILITY BRIDGE   NOT verified against anything outside
                                         D-1. It rests on D-1's reading of a
                                         fetched source.

**THIS TASK RE-FETCHED NO SOURCE.** No literature was retrieved, and none
was consulted beyond `D-1`'s tables.

**Whether reading `MP87`, `FG26`, `KU10` or `OS78` directly would change an
`IH` or `UB` tag is `NOT DETERMINABLE BY THIS TASK`.**

**The partial exception is stated so the verification claim is not
overstated**, and it matters: eight `IH` tags rest on a programme fact I
checked and a source claim I did not. **Reporting `IH` as "verified"
without that split would have overstated half of it.**

## 16. Did classifying make me want to size a gap, choose a candidate, or sketch a lemma?

**All three, in that order of strength. None acted on.**

**Sizing: the strongest by a wide margin, and the specification predicted
it.** The three categories are DEFINED by how they close — a ruling, other
mathematics, a targeted step — and **a definition in terms of closure
mechanism sits one word away from a claim about closure cost.** Having
tagged twenty-five entries `UNFROZEN DATUM`, the sentence that forms itself
is *"a quarter of the gaps close when the PI rules"*, which is **already a
size claim wearing a count's clothing.** It is also wrong in a way worth
naming: `§8` establishes that **no ruling closes any two entries jointly**,
so twenty-five `UD` occurrences are not twenty-five things one ruling
resolves.

**The pull was sharpest at `UNESTABLISHED APPLICABILITY BRIDGE`**, whose
own definition contains *"may need only a targeted applicability lemma
rather than a full construction"* — **the word `only` is a size word, and
it is in the category's definition.** I used the phrase in the artifact
because the specification's `§1` uses it, **and I did not attach it to any
particular entry.**

**Choosing a candidate: moderate, and it arrived through the table.**
Wilson's zero `IH` count is visually striking, and *"Wilson is the only
candidate with no incompatible basis"* is a true sentence about the table
and a false suggestion about the physics. **I wrote the count and then
wrote why the count is an artefact of the fetched set** — `§15.2` — rather
than leaving the reader to draw the inference.

**Sketching a lemma: real but weak, and localised to one place.** `FG26`'s
`H1`, `H2`, `H3` recur for naive and staggered, and `KU10`'s
auxiliary-field junction is the same shape again — **it is very tempting to
observe that one determinant-reflection argument might serve several.**
**`§8` is the discipline that stopped it: that observation IS a shared
closure claim**, it is exactly what `A8` forbids inferring from shared
wording, and **the `MP87` case shows why** — two entries from the same
paper turn out to rest on two different proofs inside it.

**I confirm: I estimated no effort and sized no gap; selected, eliminated,
ranked and preferred no candidate; designed no proof route, lemma or
construction and stated nothing about what would be required to close any
gap beyond naming its category; did not revise or re-derive `B0`'s
seven-to-eleven estimate; concluded nothing about whether missing
mathematics exists; modified no file, including `D-1`'s tables; added no
register entry; claimed nothing about `C-iii` or `D0`; did not touch
`main`; and pushed no ref but this task's branch.**

## 17. Stops and clarifications

**NO STOP occurred.** All four checker invocations exited 0, `RUN 2` passed
at both prospectivity readings, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 2 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 17.1 `OBSERVATION_METHOD_ERROR` — first finding, mine, caught within the task

**My first pass at `A6` was about to accept `D-1`'s "unfrozen" wording as
the evidence for the tag.** Twenty-four occurrences of the word `unfrozen`
in the tables make the `UD` assignment feel already done, **and `§2` of the
specification exists precisely because it is not.**

**Corrected by searching the repository for each quantity BEFORE assigning
any `UD` tag**, which is what produced the five `reflection type` entries
and the one `observable algebra` entry as `UNDETERMINED` — **six entries
that a wording-based pass would have tagged `UD` without justification** —
and the two entries at `§6.1` where the repository contradicts the table on
one reading.

**Recorded because the near-miss is the informative part**: had I taken the
wording, the report would have shown 31 `UD` occurrences and zero
undetermined, and would have looked more complete while resting on `D-1`'s
description of the repository rather than on the repository.

### 17.2 `OBSERVATION_METHOD_ERROR` — second finding, mine, caught within the task

**My first `FAIL` count treated the token as the unit of hypothesis.** It
is not: `§4.1` shows two tokens each covering three named hypotheses, so 52
tokens are 56 hypotheses. **The token count is still the right basis for
`A4`, because it is what the landed inventory counts**, and reporting it
without the discrepancy would have let a later task read "52" as a count of
scientific gaps.

**Corrected by reading each prose sentence rather than counting its
tokens**, and both multi-hypothesis entries are flagged in the artifact.

### 17.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding, and it is my error

**THE `{HHMM}Z` TOKEN IS WRONG. It reads `2255Z`. Commit 1's UTC timestamp
is `2339Z`.**

    date -u at branch creation           2026-08-16T2339Z
    commit 1 author date, UTC            2026-08-16T2339Z
    token used in all four filenames     2255Z
    discrepancy                          44 minutes early

**I measured the time and then typed a different value into the paths.**
The token is internally consistent — fixed once by commit 1 and reused
unchanged by commits 2, 3 and 4 — **and it does not match the clock it is
supposed to record.**

**I did NOT repair it, and the reason is the prohibition rather than the
cost.** Repair means renaming three committed paths, which requires
rewriting commits 1–3. **Rule 20 permits amending an unpushed commit ONLY
to remove a mechanically detected commit-message hygiene violation, with
the tree unchanged**, and this is a tree change. **`§8` of this
specification forbids any other history rewrite.** **A branch reset would
also be a rewrite, and branch deletion is separately forbidden.**

**So the honest disposition is to leave it and report it**, which is what I
have done. **Nothing scientific depends on it**, no criterion checks the
token against a clock, and the manifest's `2026-08-XXT{HHMM}Z` pattern is
satisfied. **A future integration specification naming these paths should
take them from this report, where they are stated exactly, and not from the
clock.**

**I am flagging this rather than minimising it because the programme's
provenance discipline rests on artifacts saying true things about
themselves**, and a filename that claims a time the work did not happen at
is a small instance of exactly that failure. **The PI may prefer a rewrite;
that ruling is not mine to make.**

### 17.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**Two entries of `D-1`'s tables assert a programme status the repository
contradicts on one reading and supports on another**, `§6.1`. `W6` and
`n6` say the non-gauge specialization "is not frozen" / "is not fixed in
the programme", while `P2-LATTICE-ONTOLOGY-01.md:26` settles that the
microscopic action carries no gauge field.

**Which reading was intended is not determinable from the table**, and the
two have different consequences: on one the entry is an `UNFROZEN DATUM`,
on the other an `UNESTABLISHED APPLICABILITY BRIDGE`. **I tagged `UB` and
reported both readings rather than choosing silently.**

**Reported, NOT registered** — `§4` forbids adding a register entry and the
governance debt register is frozen at eleven. **`D-1`'s tables are not
modified.**

### 17.5 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked at four points —
the evidence base, the coverage artifact's blob, the three freeze
documents' blobs, and its own scope block — **and MEASURED agrees at every
one.**

**Its `§0` orientation figures are correct**, and its warning that they are
the previous executor's and must be re-derived was followed. **Its wording
census of 24 / 7 / 2 / 1 is reproducible under a stated region**, `§4.2`,
and I report the region rather than a discrepancy.

**Its `§1` caution about `operator normalization` is well founded**:
MEASURED, the phrase `operator normalization` occurs five times in the
artifact, and the `FAIL` verdicts attached to a normalization carry
**two different qualifiers and none at all** — twice *(not
convention-mapped)*, twice bare, and once bundled with the
flavour-to-taste map. **They do not classify alike**: the qualified ones
are `UB`, the bare ones `UNDETERMINED`, the bundled one `UD` + `UB`.

### 17.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred**, `§1`; **neither of Rule 13's two
diagnostic orders was exercised**, and nothing was installed.

**No defect in the repository was found by this task.** Every path at the
evidence base is blob-identical at the head; the gate invariants hold; both
pins recompute; the checker passes at both readings; the validators are
unchanged at 324 passed, 2 deselected.

### 17.7 What I would have specified differently

**`A5` asks for "every `FAIL` classified" without saying what an entry
is.** I used the token, because that is what `A4`'s inventory counts, **and
`§4.1` shows the two units differ by four.** **I would have had `A5` name
the unit and require the token-versus-hypothesis discrepancy reported** —
otherwise two careful executors classify 52 and 56 entries respectively and
both satisfy the criterion.

**And `§2` names three files to check `UNFROZEN DATUM` against, but two of
the eight quantities are settled only by a fourth.** **I would have had
`§2` say the three are a starting point and require the executor to report
any further file consulted**, which is what I did, rather than leaving it
to be inferred that the list was exhaustive.

## 18. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A12`, `A14` and
`A15` for commits 1–3; `A13`'s four invocations with both configs and the
output verbatim; `A10`'s scope base-to-commit-3 at 3 additions and 0
modifications; commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; `A10`'s final
base-to-commit-4 scope of 4 additions and 0 modifications.

**Stated as `NOT DETERMINABLE BY THIS TASK`:** whether direct re-reading of
any fetched source would change an `INCOMPATIBLE HYPOTHESIS` or
`UNESTABLISHED APPLICABILITY BRIDGE` tag, `§15.4`.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A10`'s final scope measured base-to-commit-4; `A13-final`, being `RUN 2`
re-run at commit 4; `A14` at commit 4; `A15` for commit 4; the exact push
command; the branch tip read back from the remote; confirmation that
`refs/heads/main` is unchanged at `822cd4fb…`.

**Nothing in this report claims to measure commit 4.**
