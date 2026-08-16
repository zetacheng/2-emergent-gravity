# `P2-LATTICE-MICROSPEC-01` — classifying the reflection-positivity gaps

**This file classifies the `FAIL` entries in
`derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md`. It does
not close them, size them, or use them to choose a candidate.**

**A tag is not a cost.** `UNESTABLISHED APPLICABILITY BRIDGE` does not mean
small and `INCOMPATIBLE HYPOTHESIS` does not mean large. **`B0`'s
seven-to-eleven construction estimate is unchanged and is not re-derived
here.**

    source artifact   derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
                      blob b9109c87ee8aa52ec96c9e095e6de85d2f1d8779
    evidence base     822cd4fbfe9bff6e43867caed95c5635344683d0

---

## 1. The vocabulary, and what each tag is allowed to rest on

    UNFROZEN DATUM (UD)
        the theorem constrains a quantity the programme has not frozen.
        REQUIRES AFFIRMATIVE REPOSITORY EVIDENCE OF NON-FREEZING.
        A source phrase such as "not mapped" or "not convention-mapped"
        is NOT sufficient. Where no affirmative evidence was found, the
        entry is UNDETERMINED and NOT tagged UD.

    INCOMPATIBLE HYPOTHESIS (IH)
        a KNOWN, frozen programme fact genuinely conflicts with the
        source hypothesis.

    UNESTABLISHED APPLICABILITY BRIDGE (UB)
        possibly compatible, but the mapping, specialization,
        factorization or measure junction has not been shown.

    UNDETERMINED
        the available evidence does not justify any of the three.

**An entry may carry more than one tag, and eleven do.** **Tags are
recorded, not ranked.**

**These close by different means — that is the only reason to separate
them:** a `UD` entry may close when a `D-pre` task freezes the datum;
`IH` means that basis cannot cover and other mathematics is needed; `UB`
may close through a targeted applicability step. **None of that is a
statement about how much work any of them is.**

## 2. The inventory, re-derived

**Counting rule, stated so it is reproducible.** An entry is one
occurrence of the literal token `` `FAIL` `` inside a `§2.2` basis block
of the source artifact. **The legend paragraph that defines `FAIL` is
excluded** — it lies above the first `#### ` heading and is skipped by
construction. **`UNKNOWN AT ABSTRACT DEPTH` is a different token and is
counted separately, never as a `FAIL`.** Axis-table rows and
theorem-hypothesis prose are counted separately and then summed.

    basis                                        axis rows   FAIL table   FAIL prose   UNKNOWN AT ABSTRACT DEPTH
    MP87 → Wilson                                        7            6            5                           0
    MP87 → naive                                         7            6            3                           0
    OS78 → Wilson (abstract-depth cross-check)           7            2            0                           6
    FG26 → naive                                         7            5            6                           0
    FG26 → staggered                                     7            5            5                           0
    KU10 → overlap                                       7            5            4                           0

    candidate     bases   table   prose   TOTAL   UNKNOWN AT ABSTRACT DEPTH
    naive             2      11       9      20                           0
    Wilson            2       8       5      13                           6
    staggered         1       5       5      10                           0
    overlap           1       5       4       9                           0

                                        52 entries in total

**These agree with the landed figures at every position.**

### 2.1 A token is not always one hypothesis

**Two entries each carry three named hypotheses under a single token.**
`FG26 → naive` reads *"determinant reflection invariance (H1), local
Grassmann representation/factorization (H2), and kinetic cross-term
decomposition (H3) are each `FAIL`"*, and `FG26 → staggered` reads *"H1
…, H2 …, and H3 … are all `FAIL`"*.

**So 52 tokens correspond to 56 named hypotheses.** **The classification
below is at the TOKEN level**, to stay commensurable with the inventory,
**and both multi-hypothesis tokens are flagged where they appear.**

## 3. The classification

**Tags: `UD`, `IH`, `UB`, `UNDET`. Multi-tag entries carry both, joined
by `+`.**

### 3.1 `MP87 → Wilson` — 11 entries

| # | Entry | Tag |
|---|---|---|
| W1 | axis 1 free/interacting — Wilson gauge/fermion action, not the programme's four-fermion interaction | `UB` |
| W2 | axis 2 reflection type — site reflection proved; programme type stated unfrozen | `UNDET` |
| W3 | axis 3 lattice extent — source setup not mapped to a frozen programme extent | `UD` |
| W4 | axis 4 boundary conditions — programme temporal condition unfrozen | `UD` |
| W5 | axis 6 measure/determinant — source Grassmann/gauge measure not mapped to the programme measure with the NJL term | `UD` + `UB` |
| W6 | axis 7 gauge content — theorem for a gauge theory; non-gauge specialization not demonstrated | `UB` |
| W7 | Wilson operator normalization — `FAIL` (not convention-mapped) | `UB` |
| W8 | `r` — `FAIL` (programme value unfrozen) | `UD` |
| W9 | hopping parameter `K < 1/6` — no programme `K`/mass mapping | `UD` + `UB` |
| W10 | gauge-invariant observables — programme algebra stated unfrozen | `UNDET` |
| W11 | programme coupling `G>0` — interaction absent from the theorem | `UB` |

### 3.2 `MP87 → naive` — 9 entries

| # | Entry | Tag |
|---|---|---|
| n1 | axis 1 free/interacting — the `r=0` passage concerns the kinetic proof, not the programme interaction | `UB` |
| n2 | axis 2 reflection type — programme type stated unfrozen | `UNDET` |
| n3 | axis 3 lattice extent — no programme extent frozen and mapped | `UD` |
| n4 | axis 4 boundary conditions — programme temporal condition unfrozen | `UD` |
| n5 | axis 6 measure/determinant — gauge/Grassmann measure not mapped to the programme NJL measure | `UD` + `UB` |
| n6 | axis 7 gauge content — non-gauge specialization not fixed | `UB` |
| n7 | exact operator normalization — `FAIL`, no qualifier | `UNDET` |
| n8 | mass/hopping domain — `FAIL` (not frozen/mapped) | `UD` + `UB` |
| n9 | exact `G>0` interaction — `FAIL` (absent) | `UB` |

### 3.3 `OS78 → Wilson` — 2 entries

| # | Entry | Tag |
|---|---|---|
| o1 | axis 6 measure/determinant — detailed measure hypotheses not fetched and cannot be mapped | `UNDET` |
| o2 | axis 7 gauge content — non-gauge specialization not established from the abstract | `UB` |

**`o1` is an EVIDENCE gap, not a programme gap.** The three tags classify
a relation between a theorem hypothesis and the programme; **here the
theorem's hypothesis is unread.** Tagging it `UB` would assert that a
bridge is what is missing, and nothing establishes that. **The six
`UNKNOWN AT ABSTRACT DEPTH` rows in this block are not entries and are
not classified.**

### 3.4 `FG26 → naive` — 11 entries

| # | Entry | Tag |
|---|---|---|
| f1 | axis 1 free/interacting — scalar Gross–Neveu, not the frozen generator sum | `IH` |
| f2 | axis 2 reflection type — programme reflection stated unfrozen | `UNDET` |
| f3 | axis 3 lattice extent — finite 2D torus with divisibility; programme extent unfrozen AND target is 4D | `UD` + `IH` |
| f4 | axis 4 boundary conditions — anti-periodic both directions; programme temporal condition unfrozen | `UD` |
| f5 | axis 6 measure/determinant — RP for an effective bosonic measure after Hubbard–Stratonovich; no map supplied | `UD` + `UB` |
| f6 | dimension 2 against 4 | `IH` |
| f7 | even `N` against symbolic unrestricted `N` | `UD` |
| f8 | lattice length divisibility — `FAIL` (unfrozen) | `UD` |
| f9 | operator normalization — `FAIL`, no qualifier | `UNDET` |
| f10 | `λ>0` sign-compatible with `G>0` but the operators differ | `IH` |
| f11 | `H1`, `H2`, `H3` each `FAIL` — none established for the programme action **(three hypotheses, one token)** | `UB` |

### 3.5 `FG26 → staggered` — 10 entries

| # | Entry | Tag |
|---|---|---|
| s1 | axis 1 free/interacting — scalar Gross–Neveu, not the programme generator sum | `IH` |
| s2 | axis 2 reflection type — source bond/link reflection not mapped to a frozen programme reflection | `UNDET` |
| s3 | axis 3 lattice extent — finite 2D torus and size restrictions versus a 4D target with unfrozen extent | `UD` + `IH` |
| s4 | axis 4 boundary conditions — anti-periodic both directions; programme temporal condition unfrozen | `UD` |
| s5 | axis 6 measure/determinant — effective bosonic determinant measure not mapped to the programme measure | `UD` + `UB` |
| s6 | dimension 2 | `IH` |
| s7 | even `N` | `UD` |
| s8 | lattice length conditions | `UD` |
| s9 | exact staggered phases / operator normalization and flavour-to-taste map | `UD` + `UB` |
| s10 | `H1`, `H2`, `H3` all `FAIL` for lack of a programme-action verification **(three hypotheses, one token)** | `UB` |

### 3.6 `KU10 → overlap` — 9 entries

| # | Entry | Tag |
|---|---|---|
| k1 | axis 1 free/interacting — free overlap RP proved and a different chiral Yukawa interaction treated; the programme interaction is not | `IH` + `UB` |
| k2 | axis 2 reflection type — link reflection proved; programme type stated unfrozen | `UNDET` |
| k3 | axis 3 lattice extent — finite `[-L+1,L]^4`; programme extent unfrozen | `UD` |
| k4 | axis 4 boundary conditions — anti-periodic time, periodic space; programme temporal condition unfrozen | `UD` |
| k5 | axis 6 measure/determinant — source positivity cone and Yukawa measure not mapped to an auxiliary-field representation of the programme NJL determinant | `UD` + `UB` |
| k6 | source overlap normalization — `FAIL` (not convention-mapped) | `UB` |
| k7 | kernel parameter `0 < m ≤ 1` — programme `M_0` unfrozen | `UD` |
| k8 | finite even extent and boundary data | `UD` |
| k9 | strict locality — `FAIL` **as a compositional bridge**, the programme four-fermion/auxiliary-field measure being different | `UB` |

### 3.7 The five aggregate figures

    UNFROZEN DATUM                       25 tag occurrences
    INCOMPATIBLE HYPOTHESIS               8 tag occurrences
    UNESTABLISHED APPLICABILITY BRIDGE   21 tag occurrences
                                         --
                                         54 tag occurrences

    entries carrying MORE THAN ONE tag   11
    entries UNDETERMINED                  9

    arithmetic check: 52 entries − 9 undetermined = 43 tagged;
                      43 + 11 multi-tag extras = 54 occurrences.

**Per candidate, tag occurrences:**

    candidate     entries   UD   IH   UB   UNDET
    naive              20    9    4    7       4
    Wilson             13    5    0    7       3
    staggered          10    6    3    3       1
    overlap             9    5    1    4       1

## 4. `UNFROZEN DATUM` verified against the repository

**Every `UD` tag rests on an affirmative repository statement, quoted
below with its file and line.** **No `UD` tag rests on failure to locate
a freeze.**

**Eight distinct quantities carry the 25 `UD` occurrences.**

| Quantity | Entries | Repository evidence | Outcome |
|---|---|---|---|
| lattice extent / finite volume | W3, n3, f3, f8, s3, s8, k3, k8 | `P2-LATTICE-ONTOLOGY-01.md:192` — *"Admissible thermodynamic / infinite-volume limits \| DELEGATED: the gate that first needs them, with preregistration"*; `P2-LATTICE-ROUTE-01.md:192-193` lists *"finite-volume and thermodynamic rules"* among what `D-pre` must **freeze** | VERIFIED UNFROZEN |
| temporal boundary condition | W4, n4, f4, s4, k4 | `P2-LATTICE-ROUTE-01.md:193` — *"boundary conditions"* in the same **Freeze:** list; `:202` — *"finite temporal extent; temporal boundary conditions"* named as blocking-deliverable content; `P2-LATTICE-ONTOLOGY-01.md:27` places *"boundary conditions"* on the FUNDAMENTAL side, i.e. to be declared | VERIFIED UNFROZEN |
| microscopic measure | W5, n5, f5, s5, k5 | `P2-LATTICE-ONTOLOGY-01.md:185` — *"Microscopic Euclidean variables, state space and measure \| DELEGATED: a subordinate `P2-LATTICE-MICROSPEC-01` artifact"* | VERIFIED UNFROZEN |
| Wilson parameter `r` | W8 | `P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md:169-171` — *"the value of `r` as a canonical choice — `r = 1` is what the exploratory script uses, not something the repository freezes"* | VERIFIED UNFROZEN |
| mass / hopping domain | W9, n8 | `P2-LATTICE-ONTOLOGY-01.md:189` — *"Canonical kinetic operator and species accounting \| DELEGATED: D-pre"*; the operator and therefore its mass parameter are undelivered | VERIFIED UNFROZEN — see the caveat below |
| overlap kernel `M_0` | k7 | dossier `:232-233` — *"`M_0` is a convention this dossier states and does not choose"*; `:274-275` — *"NOT ESTABLISHED for this candidate: which `M_0` the programme would adopt"* | VERIFIED UNFROZEN |
| internal multiplicity `N` | f7, s7 | `P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43` — *"the `1/N` prefactor defining the large-N limit; `N` kept symbolic in all algebra"* | VERIFIED UNFROZEN (symbolic, not fixed) |
| staggered phases / operator normalization | s9 | `P2-LATTICE-ONTOLOGY-01.md:189`, as above — the canonical kinetic operator is delegated | VERIFIED UNFROZEN |

    verified unfrozen        8 quantities, 25 tag occurrences
    verified frozen          0
    could not determine      0 among entries tagged UD

**The three counts are as stated, and the third is zero BY
CONSTRUCTION**, not by luck: **an entry whose quantity I could not verify
was left `UNDETERMINED` and never received the tag.** The nine
`UNDETERMINED` entries in `§3` are where that discipline landed.

**Caveat on `mass / hopping domain`, stated because it is the weakest of
the eight.** No repository text names a hopping parameter or a mass
domain at all. The evidence is that the canonical kinetic operator is
delegated, from which the absence of a frozen mass parameter follows.
**That is an inference from an explicit delegation, not a quotation about
the mass**, and it is weaker than the `r` and `M_0` evidence, which quote
the quantity by name.

**A note on where I looked.** `§2` of the specification names three
files. **Two of the eight quantities — `r` and `M_0` — are settled by a
fourth**, `P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md`, which
states them by name where the three named files do not. **The three named
files were searched first and are the basis for the other six.**

### 4.1 Where `D-1`'s table and the repository disagree

**Two entries, `W6` and `n6`, on ONE reading.**

`MP87 → Wilson` axis 7 reads *"non-gauge specialization is plausible but
is **not frozen** and demonstrated in the programme action"*, and
`MP87 → naive` axis 7 reads *"its non-gauge specialization is **not
fixed** in the programme"*.

**READ AS A CLAIM ABOUT PROGRAMME STATUS, the repository contradicts
them.** `P2-LATTICE-ONTOLOGY-01.md:26` places *"gauge bosons and
composite particles"* on the EMERGENT side of the
fundamental/emergent table, and the FUNDAMENTAL column carries the
fermionic variables, the Euclidean lattice action, and the lattice Dirac
operator — **no gauge field.** **That the microscopic action is
non-gauge is settled, not open.**

**READ AS A CLAIM ABOUT THE THEOREM, they are correct**: what is not
established is that `MP87`'s gauge-theory result specializes to the
non-gauge case. **That is why both entries are tagged `UB` and neither
is tagged `UD`.**

**Reported as a finding about `D-1`'s tables. The arriving artifact is
NOT modified**, and this file does not correct it.

    entries where D-1 asserts unfrozen and the repository shows frozen
        under the programme-status reading      2   (W6, n6)
        under the theorem reading               0

**No other entry was found where `D-1`'s assertion about the repository
fails against the repository.**

### 4.2 Two quantities the repository does not settle either way

**`reflection type` — `W2`, `n2`, `f2`, `s2`, `k2`.** MEASURED: the
strings `site reflection`, `link reflection`, `reflection type` and
`reflection plane` occur ZERO times in all three named files.
`P2-LATTICE-ONTOLOGY-01.md:181` freezes *"Reflection positivity of the
action"* as an OBLIGATION, and `:70-79` requires it *"proved per declared
kinetic operator"* — **neither names a reflection type.**

**`D-1` asserts the programme reflection type is unfrozen. The repository
neither freezes it nor affirmatively records it as an open datum.**
**Absence of a located freeze is not evidence of non-freezing**, so these
five entries are `UNDETERMINED` rather than `UD`.

**`observable algebra` — `W10`.** MEASURED: `observable algebra` occurs
once in the three named files, at `P2-LATTICE-ONTOLOGY-01.md:326`, in a
list of properties a reconstructed continuum theory should have. **That
is not a freeze and not a delegation.** `UNDETERMINED`.

## 5. The boundary cases

**Eleven, and they are the deliverable.** Each is an entry whose tag was
not obvious from a first read.

**B1 — `W1`, `n1`: `MP87` axis 1, the missing interaction.** `UB` or
`IH`? **`UB` assigned.** The reading that supports `IH`: the programme's
interaction is frozen and `MP87`'s action does not contain it, so a
frozen programme fact differs from the source's. The reading that
supports `UB`, **which I weighted**: `MP87` is SILENT about a
four-fermion term rather than assuming its absence, and **silence is not
conflict** — an interaction-preservation step would be a bridge, not a
replacement. **Sentence weighted:** *"Wilson gauge/fermion action, not
the programme's added four-fermion interaction"* — *added* implies
composition, not contradiction.

**B2 — `W6`, `n6`, `o2`: axis 7, gauge content.** `UB`, `IH` or `UD`?
**`UB` assigned to all three.** `UD` is refused because the repository
settles the programme side (`§4.1`). `IH` is refused because a
gauge-theory theorem may specialize to a trivial gauge group; nothing
establishes it cannot. **Sentence weighted:** *"non-gauge specialization
is **plausible** but is not … demonstrated"* — the source's own word
`plausible` rules out `IH`.

**B3 — `W7`, `k6`: normalization "not convention-mapped".** `UB` or
`UD`? **`UB` assigned.** `§1` of the specification expressly excludes
`not convention-mapped` from sufficing for `UD`, and the entry is about a
mapping between conventions rather than about a quantity the programme
has failed to fix. **A `UD` reading is available** through the delegated
kinetic operator, **and I did not take it**, because the entry's own
subject is the mapping.

**B4 — `n7`, `f9`: bare "operator normalization is `FAIL`".**
`UNDETERMINED` assigned. **These two carry no qualifier at all** — no
"unfrozen", no "not mapped". **Nothing in the entry says which of the
three failures it is**, and assigning `UD` by analogy with `W7`'s
neighbour would be inventing the reason. **The specification flags these
two in advance as "neither", and they are.**

**B5 — `W2`, `n2`, `f2`, `s2`, `k2`: reflection type.** `UD` or
`UNDETERMINED`? **`UNDETERMINED` assigned to all five**, per `§4.2`.
**This is the largest single group and the one I am least comfortable
with**: `D-1` asserts non-freezing five times, and the assertion may well
be right. **It is not verifiable from the repository**, and `§2` of the
specification is explicit that a search finding nothing yields
`UNDETERMINED`.

**B6 — `W10`: observable algebra.** Same shape as `B5`, one entry.
`UNDETERMINED`.

**B7 — `f7`, `s7`: even `N`.** `UD` or `IH`? **`UD` assigned.** The `IH`
reading: the programme keeps `N` symbolic and unrestricted, `FG26`
requires it even, so a programme commitment conflicts. The reading I
weighted: **"kept symbolic" is a statement that no value is fixed, not a
commitment that `N` is odd or unrestricted forever.** A later ruling
could make `N` even. **Sentence weighted:** `P2-CHANNEL-FREEZE-01`'s
*"`N` kept symbolic in all algebra"* — a deferral, not a constraint.

**B8 — `f11`, `s10`: `FG26`'s `H1`, `H2`, `H3`.** Named in advance by
the previous executor. `UB` or `IH`? **`UB` assigned to both.** The
entries say *"none is established for the programme action"* and *"for
lack of a programme-action verification"* — **both are statements about
what has not been shown, not about what has been shown false.**
**Each token covers three named hypotheses**, and **the tag is the same
for all three in each case**; I did not find a reading on which `H1`,
`H2` and `H3` classify differently from one another.

**B9 — `k1`: `KU10` axis 1.** **BOTH `IH` and `UB` assigned**, and this
is the clearest genuinely layered entry. `IH`: `KU10`'s main theorem
assumes a FREE theory, and the programme's interaction is frozen and
non-zero — that is a conflict with a frozen fact. `UB`: `KU10` also
treats a chiral Yukawa interaction, and what is missing there is the
auxiliary-field junction to the programme's four-fermion term — a
bridge. **Two source results in one entry, and forcing one tag would
lose whichever was dropped.**

**B10 — `o1`: `OS78`'s measure row at abstract depth.**
`UNDETERMINED` assigned, per `§3.3`. The `UB` reading would say a
mapping is missing; **what is actually missing is the source text.**

**B11 — `f3`, `s3`: axis 3 carrying two subjects.** Both entries name
the programme extent (unfrozen) AND the 2D/4D difference in one
sentence. **`UD` + `IH` assigned to each.** A single tag would have
hidden one of two distinct failures recorded in one row.

**None of the eleven was resolved by preference.** **Six turned on a
specific word in the source** — *added*, *plausible*, *convention*,
*symbolic*, *established*, *versus* — and those words are quoted above.

## 6. Shared subject and shared closure

**Two layers, and they are not the same.** `SHARED SUBJECT` means the
same programme datum, hypothesis or junction appears for more than one
candidate. `SHARED CLOSURE` means evidence establishes that the SAME
ruling or the SAME bridge would resolve those entries for more than one
candidate.

### 6.1 `UNFROZEN DATUM`

| Subject | Candidates | Layer |
|---|---|---|
| temporal boundary condition | naive, Wilson, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| lattice extent / finite volume | naive, Wilson, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| microscopic measure | naive, Wilson, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| internal multiplicity `N` | naive, staggered | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| `r` | Wilson only | not shared |
| `M_0` | overlap only | not shared |
| staggered phases | staggered only | not shared |
| mass / hopping domain | naive, Wilson | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |

**Why closure is not established even for the boundary condition, which
looks like the strongest case.** One PI ruling would fix one temporal
boundary condition. **But the four theorems assume DIFFERENT boundary
data** — `FG26` anti-periodic in both directions, `KU10` anti-periodic
time with periodic space, `MP87` a finite-lattice setup with arbitrary
reflection-plane separation. **A single ruling would match some and
exclude others**, and `D-1`'s own entries say so: *"a different future
ruling would exclude the theorem"*, *"an incompatible ruling would
exclude the theorem"*. **The subject is shared; the outcome is not
jointly determined.**

### 6.2 `INCOMPATIBLE HYPOTHESIS`

| Subject | Candidates | Layer |
|---|---|---|
| dimension 2 against the frozen 4 | naive, staggered | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| interaction differs from the frozen generator sum | naive, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |

**Both arise from `FG26` for naive and staggered, and the temptation is
to read one shared remedy.** **Nothing in `D-1` establishes that a
single piece of mathematics would settle the dimension question for both
models**, and `FG26` treats them as two models with different kinetic
structure and a flavour-to-taste map that `s9` records as unmapped.

### 6.3 `UNESTABLISHED APPLICABILITY BRIDGE`

| Subject | Candidates | Layer |
|---|---|---|
| `FG26`'s `H1`/`H2`/`H3` | naive, staggered | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| `MP87`'s non-gauge specialization | naive, Wilson | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| interaction-preservation step | naive, Wilson, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |
| measure / auxiliary-field junction | naive, Wilson, staggered, overlap | `SHARED SUBJECT / CLOSURE NOT ESTABLISHED` |

**`H1`/`H2`/`H3` is the case named in advance, and the answer is the one
the specification anticipated:** whether one bridge closes both **depends
on operator structure, and nothing in `D-1` establishes it.**

**`MP87`'s non-gauge specialization is the sharper case, and it is
sharper than it looks.** Both entries come from the same paper —
**but from different results inside it.** The Wilson entry rests on
`MP87`'s own site-reflection theorem; the naive entry rests on `MP87`'s
DISCUSSION of the earlier link-reflection proof at `r=0`. **Same paper,
same-sounding gap, two different proofs.** **Shared wording is not even
shared theorem here.**

### 6.4 The count

    SHARED SUBJECT relationships identified        11
    SHARED CLOSURE established                      0

**Zero.** **Every shared subject in this artifact is reported as
`SHARED SUBJECT / CLOSURE NOT ESTABLISHED`**, and none of them may be
read as a construction that would serve more than one candidate.

## 7. What this classification does not establish

**A tag is not a cost.** Nothing here establishes that an
`UNESTABLISHED APPLICABILITY BRIDGE` gap is cheaper to close than an
`INCOMPATIBLE HYPOTHESIS` one — only that they close by different means.
**`B0`'s seven-to-eleven construction estimate is unchanged.**

**A tag distribution is not candidate evidence.** naive carries nine `UD`
occurrences and Wilson five; **that does not make either better
supported.** A candidate whose gaps are mostly `UNFROZEN DATUM` is one
whose gaps depend on rulings the programme has not made, **and those
rulings are the PI's and are not made easier by being counted.**

**This rests on `D-1`'s tables, and `D-1`'s search was bounded.** **A gap
that does not appear in those tables is not classified here**, and
nothing establishes the tables are complete.

**Only `UNFROZEN DATUM` was independently verified in this task**, against
the repository, as `§4` records. **`INCOMPATIBLE HYPOTHESIS` and
`UNESTABLISHED APPLICABILITY BRIDGE` tags rest on `D-1`'s reading of a
fetched source**, and **this task did not re-fetch any source.** Whether
reading `MP87`, `FG26`, `KU10` or `OS78` directly would change those
tags is **`NOT DETERMINABLE BY THIS TASK`**.

**Partial exception, stated so the verification claim is not
overstated:** the `IH` tags that turn on a PROGRAMME fact — the frozen
four dimensions, the frozen generator-sum interaction — had that half
checked against the repository. **The other half, what the source
assumes, was not.**

**No candidate is selected, eliminated, ranked or preferred here. No
proof route, lemma or construction is designed. Nothing here concludes
that any missing mathematics does not exist** — `D-1` established that
the fetched literature does not supply it, over a bounded search.
