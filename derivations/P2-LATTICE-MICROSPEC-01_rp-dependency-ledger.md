# `P2-LATTICE-MICROSPEC-01` — the reflection-positivity dependency ledger

**This file reduces `D-1b`'s `UNFROZEN DATUM` and `INCOMPATIBLE
HYPOTHESIS` occurrences to the programme data and established facts that
control them. It does nothing else.**

**A node is not a cost. Five nodes are not "five easy decisions".** **No
gap is sized, no candidate is preferred, no ruling is recommended, and no
mathematical bridge is judged.**

    source artifact   derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
                      blob 66d5087ae6b064acf590a50c9a68d08c26607e7e
    evidence base     ec85f66b05b3ed92cd924bc75273b74a73eee23b

---

## 1. What is reduced here, and what is not

    UNFROZEN DATUM                       25 occurrences   REDUCED HERE
    INCOMPATIBLE HYPOTHESIS               8 occurrences   REDUCED HERE
    UNESTABLISHED APPLICABILITY BRIDGE   21 occurrences   OUT OF SCOPE
    UNDETERMINED                          9 entries       OUT OF SCOPE

**The three tags do not reduce alike.**

**`UNFROZEN DATUM` reduces by shared RULING** — several occurrences may
wait on one decision the programme has not made, and establishing that
needs only the entries and the freeze documents.

**`INCOMPATIBLE HYPOTHESIS` reduces by shared ESTABLISHED FACT** —
several occurrences may rest on one thing the programme has already
settled. Also no mathematics.

**`UNESTABLISHED APPLICABILITY BRIDGE` does not reduce either way.** A
bridge is not waiting on a programme ruling. It is waiting on a
mathematical applicability step **NOT ESTABLISHED IN THE PRESENT
REPOSITORY OR IN `D-1`'s FETCHED EVIDENCE BASIS** — which is a statement
about the evidence, not about mathematics. **Deciding whether two such
bridges are the same problem would take mathematical judgement this file
does not make.**

**`UNDETERMINED` entries carry no classification at all.** Grouping one
would assign it a classification by the back door.

**Neither out-of-scope class is grouped, classified or judged here.**

## 2. The grouping rule this ledger is held to

> **A dependency may group occurrences ONLY when the same
> already-identified programme datum, or the same already-established
> incompatibility fact, controls them. Similar wording, a common source
> paper, or apparent mathematical similarity is INSUFFICIENT.**

**Every node below names its datum or fact and points at where the
repository identifies it, with file and lines.** **A node with no anchor
is not a node.**

**`D-1b` produced the case that forces the rule.** `MP87`'s non-gauge
specialization appears for `Wilson` and for `naive` — same paper, same
phrasing — and the `Wilson` entry rests on `MP87`'s own site-reflection
theorem while the `naive` entry rests on its discussion of the earlier
link-reflection proof at `r=0`. **Shared wording was not even shared
theorem there.**

## 3. `RULING` nodes — the `UNFROZEN DATUM` reduction

**Five nodes. Every one verified open against the repository, `§5`.**

### R1 — the canonical kinetic operator and its parameters

    NODE        which lattice Dirac operator is canonical, and the
                parameter values that come with the choice
    KIND        RULING
    ANCHOR      P2-LATTICE-ONTOLOGY-01.md:189
                  "| Canonical kinetic operator and species accounting |
                   DELEGATED: D-pre (§4 obligation binds it) |"
                P2-LATTICE-ROUTE-01.md:189-190
                  "*Freeze:* … the canonical lattice Dirac operator; the
                   species ledger and doubling treatment"
                P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md:169-170
                  "the value of `r` as a canonical choice — `r = 1` is what
                   the exploratory script uses, not something the repository
                   freezes"
                same:232-233   "`M_0` is a convention this dossier states
                                and does not choose"
                same:274-275   "which `M_0` the programme would adopt, that
                                being part of the choice this dossier does
                                not make"
    CONTROLS    W8  the Wilson parameter r
                W9  the hopping/mass domain, Wilson
                n8  the mass/hopping domain, naive
                k7  the overlap kernel parameter M_0
                s9  the staggered phases and operator normalization
                    — 5 occurrences
    CANDIDATES  naive, Wilson, staggered, overlap
    STATUS      OPEN. §5 records the search.

### R2 — the admissible lattice extent and finite-volume rules

    NODE        what lattice extent and finite-volume regime the programme
                admits
    KIND        RULING
    ANCHOR      P2-LATTICE-ONTOLOGY-01.md:192
                  "| Admissible thermodynamic / infinite-volume limits |
                   DELEGATED: the gate that first needs them, with
                   preregistration |"
                P2-LATTICE-ROUTE-01.md:192-193
                  "*Freeze:* … finite-volume and thermodynamic rules"
    CONTROLS    W3 n3 f3 f8 s3 s8 k3 k8   — 8 occurrences
    CANDIDATES  naive, Wilson, staggered, overlap
    STATUS      OPEN. §5 records the search.

**`f8` and `s8` are divisibility conditions on the torus size and `k8`
names a finite even extent** — all three are constraints ON the extent,
and there is no frozen extent for them to be checked against. **Same
datum, not similar wording.**

### R3 — boundary conditions, the temporal one in particular

    NODE        which boundary conditions the programme adopts, temporal
                above all
    KIND        RULING
    ANCHOR      P2-LATTICE-ROUTE-01.md:193
                  "*Freeze:* … boundary conditions."
                P2-LATTICE-ROUTE-01.md:202
                  "finite temporal extent; temporal boundary conditions"
                  — named among the blocking deliverable's content
                P2-LATTICE-ONTOLOGY-01.md:27
                  "| boundary conditions, internal multiplicity `N` |
                   Lorentz symmetry, the light cone |"
                  — the FUNDAMENTAL column, i.e. to be declared
    CONTROLS    W4 n4 f4 s4 k4   — 5 occurrences
    CANDIDATES  naive, Wilson, staggered, overlap
    STATUS      OPEN. §5 records the search.

### R4 — the microscopic Euclidean variables, state space and measure

    NODE        what the microscopic measure is
    KIND        RULING
    ANCHOR      P2-LATTICE-ONTOLOGY-01.md:185
                  "| Microscopic Euclidean variables, state space and
                   measure | DELEGATED: a subordinate
                   `P2-LATTICE-MICROSPEC-01` artifact … |"
                P2-LATTICE-ROUTE-01.md:189
                  "*Freeze:* microscopic variables and measure"
    CONTROLS    W5 n5 f5 s5 k5   — 5 occurrences
    CANDIDATES  naive, Wilson, staggered, overlap
    STATUS      OPEN. §5 records the search.

### R5 — the internal multiplicity `N`

    NODE        what value, or what restriction, the programme fixes for N
    KIND        RULING
    ANCHOR      P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43
                  "the `1/N` prefactor defining the large-N limit; `N` kept
                   symbolic in all algebra"
                P2-LATTICE-ONTOLOGY-01.md:27
                  "| boundary conditions, internal multiplicity `N` | … |"
                  — the FUNDAMENTAL column
    CONTROLS    f7 s7   — 2 occurrences
    CANDIDATES  naive, staggered
    STATUS      OPEN. §5 records the search.
                Note: "kept symbolic" is a deferral, not a commitment that
                N is unrestricted. The ruling that fixes N — or restricts
                it — has not been made.

### 3.1 The decomposition of all 25 occurrences

**Every `UNFROZEN DATUM` occurrence is dispositioned EXACTLY ONCE.**

    R1   W8 W9 n8 k7 s9                    5
    R2   W3 n3 f3 f8 s3 s8 k3 k8           8
    R3   W4 n4 f4 s4 k4                    5
    R4   W5 n5 f5 s5 k5                    5
    R5   f7 s7                             2
                                          --
    N_mapped                              25
    N_frozen_finding                       0
    N_undetermined_finding                 0
                                          --
                                          25

    25 = 25 + 0 + 0

**The decomposition reduces to `25 → 5`, and it is stated that way
because both finding counts are zero.**

    RATIO, over category 1 only:   25 occurrences  →  5 RULING nodes

### 3.2 One occurrence names two data, and is dispositioned once

**`k8` reads *"finite even extent and boundary data"*.** Its leading
datum is the extent, and it is assigned to `R2` **once**.

**Its text also touches `R3`'s datum.** **That is recorded here and is
NOT a second disposition** — counting it twice would break the
exactly-once rule and would inflate both the mapping and the apparent
reach of `R3`. **A reader should know that closing `R2` alone would not
fully retire `k8`.**

## 4. `ESTABLISHED FACT` nodes — the `INCOMPATIBLE HYPOTHESIS` reduction

**Two nodes, controlling all 8 occurrences.**

### F1 — the lattice is four-dimensional, and its four axes are equivalent

    NODE        the H(4) lattice is four-dimensional; isotropy of the four
                axes is on the freeze list
    KIND        ESTABLISHED FACT
    ANCHOR      P2-LATTICE-ONTOLOGY-01.md:62-64
                  "The fundamental formulation is EUCLIDEAN: the H(4)
                   lattice is a four-dimensional configuration-and-weight
                   statistical system with all four axes equivalent."
                P2-LATTICE-ONTOLOGY-01.md:94-95
                  "H(4) isotropy (equal couplings on all four axes) joins
                   the freeze list."
    CONTROLS    f3 f6 s3 s6   — 4 occurrences
    CANDIDATES  naive, staggered

### F2 — the frozen `U(N)_L × U(N)_R` generator-sum interaction with `G > 0`

    NODE        the interaction is frozen as the generator sum
                (G/2N) Σ_A [ (S^A)² + (P^A)² ], with G > 0 and continuous
                U(N)_L × U(N)_R symmetry
    KIND        ESTABLISHED FACT
    ANCHOR      P2-CHANNEL-FREEZE-01_phaseA_freeze.md:31-32
                  S^A and P^A defined
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md:36-37
                  the canonical action, with the (G/2N) generator sum
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md:40-41
                  "`G > 0` — the single independent coupling of the
                   operative canonical four-fermion interaction"
                P2-CHANNEL-FREEZE-01_phaseA_freeze.md:45
                  "classical symmetry `U(N)_L × U(N)_R`"
    CONTROLS    f1 f10 s1 k1   — 4 occurrences
    CANDIDATES  naive, staggered, overlap

### 4.1 The mapping

    F1   f3 f6 s3 s6     4
    F2   f1 f10 s1 k1    4
                        --
                         8

    8 occurrences  →  2 ESTABLISHED FACT nodes

**`f3` and `s3` appear in both `§3.1` and here, and that is correct, not
double counting.** Each is a multi-tag entry carrying `UD` + `IH`: its
`UD` occurrence is dispositioned to `R2`, its `IH` occurrence to `F1`.
**Two tag occurrences of one entry, each dispositioned once in its own
class.**

## 5. Every `RULING` node verified against the repository

**All four mandatory documents were inspected for every one of the five
nodes**, and in addition `GATES.md`, `DECISION_LOG.md`, and the
derivations those four documents reference were searched for a LATER
authoritative ruling.

**Mandatory minimum, checked for R1–R5 without exception:**

    derivations/P2-LATTICE-ONTOLOGY-01.md                             blob 6544fb1a72…
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 blob 0be773f6a5…
    derivations/P2-LATTICE-ROUTE-01.md                                blob 42be438ff1…
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   blob 0b227206f3…

**Additional authoritative sources searched, for every node:**

    GATES.md            searched for kinetic operator, Wilson parameter,
                        domain wall, overlap, staggered, finite volume,
                        infinite volume, thermodynamic, lattice extent,
                        lattice size, boundary condition, microscopic
                        measure, Grassmann measure, internal multiplicity,
                        large-N
    DECISION_LOG.md     searched for kinetic operator, boundary condition,
                        finite volume, thermodynamic, microscopic measure,
                        internal multiplicity, reflection type, Wilson
                        parameter
    the derivations referenced by the four documents —
                        CANONICAL_INTERACTION.md,
                        P2-GENERATOR-SUM-CRITICALITY_01.md,
                        P2-PHASE-01_C-CHECK_OPEN-ITEMS.md,
                        P2-PHASE-01_C3_curvature_asymmetry.md,
                        u3-fierz/u3_fierz.md
    a repository-wide sweep for freeze phrasings —
                        "kinetic operator is frozen", "boundary condition(s)
                        (are|is) frozen", "extent is frozen", "volume is
                        frozen", "measure is frozen", "N is fixed",
                        "canonical kinetic operator"

**MEASURED: NO LATER AUTHORITATIVE RULING WAS FOUND FOR ANY OF THE FIVE
DATA.**

**Two hits needed reading rather than counting, and neither is a
ruling:**

**`derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md:80` carries
`| Canonical kinetic operator and species accounting | DELEGATED: D-pre
(§4 obligation binds it) |`** — **the ontology's row quoted verbatim in
another artifact.** It corroborates `R1` and supersedes nothing.

**`GATES.md` hits on "finite-volume" and "thermodynamic"** are a
Brillouin-zone tadpole fit at `:156`, a note on finite-volume grid
artifacts at `:694`, and thermodynamic dominance conditions at
`:1032`–`:1047`. **None rules on the admissible extent.**

**`DECISION_LOG.md` returns ZERO occurrences of every term searched.**

**Datum-level counts:**

    N_ruling                  5     R1 R2 R3 R4 R5, all verified open
    N_proposed_frozen         0
    N_proposed_undetermined   0

**Occurrence-level counts, per `§3.1`:**

    N_mapped                 25
    N_frozen_finding          0
    N_undetermined_finding    0

**These are different quantities and are not equated.** **The mapping in
`§3.1` accounts for every one of the 25 occurrences exactly once**, which
is what reconciliation means here — **not that 5 and 25 should match.**

**No node's datum turned out already frozen. Zero is the answer, and it
is an answer rather than an absence:** each of the five was searched
across four mandatory documents, two registers, five referenced
derivations and a phrase sweep, and none returned a ruling.

**No finding about `D-1b`'s classification arises from this criterion**,
and `D-1b`'s artifact is not modified.

## 6. The grouping rule, demonstrated

**All seven nodes control more than one occurrence. For each, the shared
datum or fact by name:**

    R1   the canonical kinetic operator is undelivered — one delegated
         row, ONTOLOGY:189. r, the mass/hopping domain, M_0 and the
         staggered phases are parameters OF that undelivered choice, and
         the dossier says so in its own words: M_0 is "part of the choice
         this dossier does not make".
    R2   there is no frozen lattice extent — ONTOLOGY:192 delegates the
         admissible limits; ROUTE:192-193 lists finite-volume rules among
         what must still be frozen.
    R3   there is no frozen boundary condition — ROUTE:193 and :202.
    R4   there is no frozen microscopic measure — ONTOLOGY:185.
    R5   N is not fixed — CHANNEL-FREEZE:43 keeps it symbolic.
    F1   the lattice is four-dimensional — ONTOLOGY:62-64, 94-95.
    F2   the interaction is the frozen generator sum with G > 0 —
         CHANNEL-FREEZE:31-32, 36-37, 40-41, 45.

**None of the seven rests on wording, on a source paper, or on apparent
similarity.** **Every one rests on a line of a freeze document that
identifies the datum or the fact.**

**The test that shows this is not circular:** `R2`, `R3` and `R4` each
group entries drawn from THREE DIFFERENT PAPERS — `MP87`, `FG26` and
`KU10`. **The grouping cannot be an artefact of shared source text
because the sources are not shared.**

### 6.1 Pairs considered and NOT grouped

**Four, and the first is the sharpest.**

**`R2` and `R3` — named in the SAME SENTENCE and kept apart.**
`P2-LATTICE-ROUTE-01.md:192-193` reads *"…finite-volume and thermodynamic
rules; boundary conditions."* **One `*Freeze:*` sentence, one semicolon
between them.** **NOT GROUPED**: a ruling on the admissible volume does
not fix a boundary condition, and a boundary-condition ruling fixes no
extent. **This is the purest form of the rule — shared wording, shared
sentence, shared delegation, and still two data.**

**`R1` and `R4` — adjacent delegated rows, kept apart.**
`ONTOLOGY:185` and `:189` are two rows of one table, and `ROUTE:189`
names *"microscopic variables and measure; the canonical lattice Dirac
operator"* in one sentence. **NOT GROUPED**: the ontology delegates them
as separate items to different addressees, and freezing an operator does
not deliver a measure.

**`R5` and `F1` — both arise inside `FG26`'s hypothesis list, kept
apart.** `FG26` requires even `N` and works in two dimensions, and both
mismatches appear in the same sentence of `D-1`'s table. **NOT GROUPED**:
one is a programme datum awaiting a ruling and the other is a programme
fact already settled — **different kinds, not merely different data.**

**`MP87`'s `W6` and `n6` — the case named in advance — are in NEITHER a
node nor two nodes.** **They are `UNESTABLISHED APPLICABILITY BRIDGE`
occurrences and therefore out of scope entirely**, `§1`. **The rule they
motivated still did its work here**, in the `R2`/`R3` rejection above.

**And the positive half of the `MP87` story is worth stating.** `MP87`
does contribute eight `UD` occurrences — `W3 W4 W5 W9` and `n3 n4 n5 n8`
— **and every one of them is grouped with `FG26` and `KU10` occurrences,
not with its `MP87` sibling.** **The grouping is by datum, and it cuts
across papers rather than along them.**

### 6.2 The one grouping this ledger's ratio is most sensitive to

**`R1` groups four different quantities — `r`, the mass/hopping domain,
`M_0`, and the staggered phases — under one datum.** The evidence for
that is `ONTOLOGY:189`'s single delegated row and the dossier's own
framing of `M_0` as *"part of the choice this dossier does not make"*.

**The alternative is defensible and is stated so a reader can see the
sensitivity.** If each operator parameter is taken as its own datum,
`R1` splits into four and the total becomes **eight nodes rather than
five**, with the same 25 occurrences.

**This ledger takes the five-node reading**, on the ground that the
repository identifies ONE delegated item and the dossier treats the
parameters as constituents of it. **The eight-node reading is recorded
here rather than omitted, because the difference is a grouping judgement
and not a measurement.**

## 7. Out of scope, reported and not reduced

    UNESTABLISHED APPLICABILITY BRIDGE   21 occurrences
    UNDETERMINED                          9 entries

**Neither was grouped, classified, or judged.**

**Why the bridges are excluded, and it is not a matter of priority.** A
`RULING` node can be verified by reading the repository: either a
document freezes the datum or it does not. **A bridge is not like that.**
Asking whether two bridges are one problem means asking whether the same
mathematics closes both — **a mathematical question, answerable only by
doing mathematics**, which this file is forbidden to do and could not do
honestly by reading tables.

**And the bridges are `NOT ESTABLISHED IN THE PRESENT EVIDENCE BASIS`.**
`D-1`'s literature search was bounded and `D-1b` re-read nothing. **That
they are absent from the evidence is not that they are absent from
mathematics**, and nothing here says otherwise.

**Why the undetermined entries are excluded.** They carry no
classification. **Placing one in a node would decide what it is** — the
very determination `D-1b` declined to make on the evidence — **and would
do it silently, as a by-product of grouping.**

## 8. What this ledger does not establish

**A NODE COUNT IS NOT A WORKLOAD.** Twenty-five occurrences resting on
five nodes means **five distinct questions, not five easy ones.** **Each
is a decision the PI has not made, on a question the programme has not
framed**, and the ledger's arithmetic says nothing about what any of them
costs to answer.

**THE TWENTY-ONE BRIDGES ARE UNTOUCHED.** **Nothing here establishes how
many independent bridges they represent — one, twenty-one, or anything
between.** **A reader must not take a reduced `UD` figure for a reduced
total**: the reduction covers 33 of the 54 tag occurrences, and the
remaining 21 are not reduced at all.

**THE BOUNDS COMPOSE.** This rests on `D-1b`'s classification, which
rests on `D-1`'s tables, whose literature search was bounded. **A gap
absent from `D-1`'s tables is absent from this ledger.** Three layers,
each bounded.

**A `RULING` NODE SAYS THE PROGRAMME HAS NOT DECIDED SOMETHING. IT SAYS
NOTHING ABOUT WHAT THE DECISION SHOULD BE.** **The node's existence does
not make the ruling easier**, and **this ledger is not a to-do list.**
Nothing here recommends a ruling, orders the nodes, or suggests that any
of them is ready to be made.

**`B0`'s seven-to-eleven construction estimate is unchanged and is not
re-derived here. No candidate is selected, eliminated, ranked or
preferred**, and a candidate whose occurrences collapse into fewer nodes
is not better supported — **it is a candidate whose gaps happen to depend
on decisions not yet made.**
