# `P2-EPS-B0` — can `ε` be computed, and would it produce a number?

    STATUS      TRACTABILITY AND DEPENDENCY ASSESSMENT. NOTHING IS COMPUTED.
    BASE        af145d5a3e36e6bca62f038092748ada3abdcec1
    SUBJECT     paper/emergent_gr_paper_v2_15.tex, 1833 lines, unmodified
    VERDICT     BLOCKED PENDING A RULING
                R1 DEPENDENCE ESTABLISHED. R1 is OPEN.
    RIDER       Even with R1 ruled, this route would not produce a NUMBER.

**This artifact reads the manuscript and the landed dependency ledger and reports
what they establish about whether `ε` can be computed.** It computes no `ε`, no
`m_θ`, no `Λ`, no `r_c` and no instanton action, and it offers no estimate, no
order of magnitude and no bound. **It does not adjudicate `R1`–`R5`, does not
choose between routes, and does not say whether the route is worth taking.**

## 1. What `ε` is

### 1.1 Which symmetry it breaks

**The approximate chiral `U(1)` phase symmetry of the condensate**,
`:521-523`:

    :521  loop the \emph{angular} direction is exactly flat: it is a
    :522  pseudo-flat direction, the perturbative reflection of the
    :523  approximate $U(1)$ chiral phase symmetry $\Phi \to e^{i\alpha}\Phi$.

### 1.2 What breaks it — and it is NOT one thing

    :525  The phase is therefore fixed not at one loop but by the subleading
    :526  effects that explicitly break the chiral $U(1)$: the axial anomaly,
    :527  realized on the lattice through the Wilson term and the surviving
    :528  doublers, together with the discrete ($Z_M$) structure of the phase
    :529  landscape.

**Restated at `:592-595`:**

    :592  On the lattice this symmetry is not exact: the discrete substrate
    :593  breaks it explicitly---through Wilson-type terms and the discrete
    :594  ($Z_M$) structure of the phase landscape---by a dimensionless
    :595  amount $\varepsilon \ll 1$.

### 1.3 Is the anomaly the whole of `ε`, or one term?

**ONE TERM. The manuscript is explicit three times over.**

**First, `:601`:** *"where `$\varepsilon$` collects the explicit-breaking
coefficients"* — **plural.**

**Second, `:526-529` names two sources joined by "together with":**

    (a)  the axial anomaly — itself realized through TWO lattice mechanisms,
         the Wilson term and the surviving doublers
    (b)  the discrete (Z_M) structure of the phase landscape

**Third, `:541-543` singles out one of them for the open computation:**

    :541  ... (The magnitude of $\varepsilon$ on the $H(4)$
    :542  substrate---in particular whether the ANOMALY CONTRIBUTION is
    :543  exponentially instanton-suppressed---is the dedicated computation
    :544  left open in Section~\ref{sec:angular}.)

**"THE ANOMALY CONTRIBUTION" IS THE MANUSCRIPT'S OWN PHRASE FOR ONE PART OF
`ε`.** A computation that settled only whether the anomaly term is
instanton-suppressed would not have computed `ε`; it would have computed one of
at least two contributions.

### 1.4 How `ε` is defined dimensionally — and this matters for §4

**`ε` is the dimensionless coefficient of the periodic angular potential,
`:531-533`:**

    :531  \begin{equation}
    :532  V_\theta(\theta) \simeq -K\cos(M\theta),
    :533  \qquad K \sim \varepsilon\,\Lambda^4,\quad \varepsilon \ll 1,

**NOTE THE `\simeq` AND THE `\sim`.** `ε` is not introduced by an equation. It
is introduced by a scaling relation, and `:538-540` then ties the same `K` to the
mass: *"the same small coefficient `K` sets the pseudo-Goldstone mass … the flat
one-loop direction and the ultralight angular mode share a single origin."*

**SO `ε` IS ITSELF DEFINED ONLY UP TO A COEFFICIENT.** That is not a remark about
the mass formula in §4; it is a property of the definition. **"Computing `ε`" is
not a numerically well-posed instruction until a normalisation convention for
`ε` is fixed, and no repository document fixes one** — §3.

## 2. The two-pass inventory

    PASS 1                          PASS 2
      varepsilon           11         U(1)               10
      \Lambda              60         axial              13
      instanton             2         theta              34
      anomaly               4         topological         0
      pseudo-Goldstone      2         suppress           11
      angular mode          9         cutoff             14
      explicit breaking     1         substrate          28
      m_\theta              7         H(4)               14
                                      spurion             0
                                      soft breaking       0

      PASS 1 union         89         PASS 2 union      117

    PASS 1 only    70
    BOTH           19
    PASS 2 only    98
    UNION         187      of 1833 lines

**THE RESEARCHER'S TWO COUNTS REPRODUCE EXACTLY: `varepsilon` 11, `\Lambda` 60.**

**PASS 2 CONTRIBUTES 98 LINES PASS 1 DOES NOT REACH.** They are mostly the
substrate and `H(4)` material — the context in which `ε` would have to be
computed — and the `U(1)`/`axial` lines that carry the symmetry statement `ε`
measures the breaking of.

**THREE PASS-2 TERMS RETURN ZERO AND THE ZEROS ARE INFORMATIVE:**

    topological     0    the manuscript's instanton language at :530 is
                         "instanton/lattice origin"; it never uses the word
                         "topological", so a search built on it would find
                         nothing and conclude wrongly
    spurion         0    no spurion analysis is present
    soft breaking   0    the breaking is called "explicit", never "soft"

### 2.1 Vocabulary added, and why

**I added `Z_M`, `M_{\mathrm{Pl}}`, `decay constant` and `c_2`**, and the
additions were not decorative:

- **`Z_M`** — because `:528` and `:594` make the discrete phase structure one of
  the two named sources of `ε`, and neither pass reaches it. **It appears on
  three manuscript lines and nowhere else in the repository in this sense** —
  §5.2 records the collision.
- **`M_{\mathrm{Pl}}`, `c_2`** — because §4's `Λ` question cannot be answered
  without the one relation that connects `Λ` to a measurable quantity, `:714`.
- **`decay constant`** — because `:589` gives `f ~ v`, a third tilde in the
  chain, which §3 needs.

**NEITHER SUPPLIED LIST IS EXHAUSTIVE**, and mine is not either. The terms came
from a description of the manuscript rather than from its own index, and I read
the union plus the surrounding argument at each cluster rather than the whole
file.

## 3. The coefficient — would `ε` alone fix `m_θ`?

**NO. NOTHING IN THIS MANUSCRIPT FIXES THE COEFFICIENT.**

**The relation, quoted with its surroundings, `:596-601`:**

    :596  The angular mode is then a pseudo--Goldstone boson with
    :597  \begin{equation}
    :598  m_\theta^2 \;\sim\; \varepsilon\,\Lambda^2 ,
    :599  \label{eq:mtheta}
    :600  \end{equation}
    :601  where $\varepsilon$ collects the explicit-breaking coefficients.

**EVERY RELATION IN THE CHAIN CARRIES A TILDE, AND THERE ARE THREE OF THEM:**

    :533   K ~ ε Λ⁴          the definition of ε
    :598   m_θ² ~ ε Λ²       the mass relation
    :589   f ~ v             the decay constant, which any careful
                             pseudo-Goldstone mass formula would need

**MEASURED: `m_\theta` occurs on seven lines** — `:598`, `:605`, `:609`, `:615`,
`:620`, `:621`, `:1556`. **Six of the seven carry `~`.** The single exact
equality is `:615`, `r_c = 1/m_θ` — which is `SRC-01a`'s derived RELATION, not a
coefficient.

**Searched for anything that would fix it — a matching condition, a
normalisation, a convention:** `f^2`, `f_\theta`, `decay constant`,
`normalis`/`normaliz`. **The only kinetic normalisation the manuscript states for
this mode is `:589-590`, `f ~ v` with
`L_θ = ½ f²(∂θ̃)²` — itself a tilde.** Every other `normalization` hit belongs
to the gravitational sector.

> **A COMPUTED `ε` WITH THIS COEFFICIENT STRUCTURE GIVES A SCALING LAW, NOT A
> MASS.**

**And the deeper form of the same point, from §1.4: because `ε` is DEFINED by a
tilde, the coefficient ambiguity is not downstream of `ε` — it is inside it.**
Fixing the coefficient in `m_θ² ~ εΛ²` and fixing the normalisation of `ε` are
the same act, and neither is done.

## 4. `Λ` — what it is and what fixes its value

### 4.1 What it is

**The lattice cutoff, the inverse lattice spacing.** `:74-75`: *"the substrate
fermions acquire masses of order the lattice cutoff `$\Lambda \sim 1/a$`"*.
Restated at `:497` and `:717`.

### 4.2 What determines its value — three answers, none of them internal

**FIRST, IN `CONVENTIONS.md` IT IS A UNIT, NOT A VALUE.**

    CONVENTIONS.md:31   "| Cutoff and lattice units | `Λ ≡ 1` (continuum),
                         `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |"
    CONVENTIONS.md:22   "The mass `m` is measured **in units of the cutoff `Λ`**
                         (i.e. `Λ ≡ 1` unless a gate states otherwise)"

**`Λ ≡ 1` IS A CHOICE OF UNITS. A quantity set to one by convention cannot supply
a physical scale to anything.**

**SECOND, IN THE MANUSCRIPT IT IS ASSUMED, NOT DERIVED.** `:717-720`: *"For
`$\Lambda \sim 1/a$` at the Planck scale and `$N \sim \mathcal{O}(10)$`, this is
self-consistent"*. **"At the Planck scale" is an input to a consistency check,
not an output of one.**

**THIRD, THE ONE RELATION CONNECTING `Λ` TO A MEASURABLE QUANTITY RUNS THE WRONG
WAY AND IS DISCLAIMED BY THE MANUSCRIPT ITSELF.** `:713-715`:

    M_Pl² = c₂ N Λ² / (8π²)

**To obtain `Λ` from it one needs `M_Pl` — an OBSERVATIONAL input — and `c₂`, and
`N`.** And `:733-739` says of `c₂`:

    :737  cutoff, $c_2$ is part of the definition of the model rather than a
    :738  derived quantity, and Eq.~\eqref{eq:Mpl} with $c_2 > 0$ is at
    :739  present a defining assumption.

**And `:123-124` and `:1620` both list `"M_Pl² as a defining input"` among the
programme's fallback routes** — i.e. the manuscript contemplates taking the
Planck mass as given rather than deriving it.

**`N` is `R5`, verified OPEN** — §5.1.

### 4.3 The consequence

> **`Λ`'s VALUE IS NOT DETERMINED INTERNALLY. IT IS EITHER A UNIT CONVENTION
> (`Λ ≡ 1`), AN ASSUMPTION ("at the Planck scale"), OR AN INVERSION OF A
> RELATION WHOSE OTHER INPUTS ARE AN OBSERVATION (`M_Pl`), A DEFINING ASSUMPTION
> (`c₂`) AND AN OPEN RULING (`N`, `R5`).**
>
> **SO THE CHAIN DOES NOT REVERSE. IT LOOPS.** A prediction of `r_c` in
> kiloparsecs would need `Λ` in physical units, and the only route to `Λ` in
> physical units passes through an observed `M_Pl`. **A prediction whose
> dimensional scale is an observational input is not a prediction of that
> scale.**

## 5. The input inventory, and the `R1` finding

### 5.1 Per input

    INPUT                                   STATUS
    the canonical lattice Dirac operator    R1 — OPEN
      (whether there is a Wilson term at
      all, and its parameter r)
    the species / doubling treatment        R1 — OPEN
      (which doublers "survive")
    the microscopic measure                 R4 — OPEN, but see §5.3: the
                                            repository states a general freeze
                                            requirement, not one about ε
    the internal multiplicity N             R5 — OPEN. Enters ε's route only
                                            through Λ, via :714.
    Λ's numerical value                     NOT FROZEN ANYWHERE. A unit
                                            convention in CONVENTIONS.md:31.
    the coefficient in m_θ² ~ ε Λ²          NOT FIXED — §3
    the normalisation of ε itself           NOT FIXED — §1.4
    M, the order of the discrete Z_M        NOT FIXED, AND NOT COVERED BY ANY
      phase symmetry                        R-NODE — §5.4
    the H(4) instanton / topological         NO REPOSITORY TREATMENT — §5.5
      sector on the substrate

    COUNTS
      frozen in CONVENTIONS.md               0
      fixed by the manuscript                0
      falling in R1–R5                       4  (R1 twice, R4 conditionally, R5)
      unfrozen and outside R1–R5             5

**NOT ONE INPUT IS FROZEN.**

### 5.2 A measurement-quality warning on `Z_M`

**`Z_M` returns hits in more than sixty files across the repository, and ALL of
them outside the manuscript are a DIFFERENT OBJECT** — the Fierz / channel-freeze
normalisation constant of the `P2-CHANNEL-FREEZE` and `P2-PHASE-01` line, which
appears in scripts, results JSON, specs and reports throughout.

**The discrete phase symmetry `Z_M` of `:528`, `:532` and `:594` occurs on
exactly THREE lines, all of them in the manuscript, and nowhere else.** A count
of `Z_M` hits would suggest the object is treated throughout the repository. **It
is treated nowhere.**

### 5.3 The `R1` finding, stated as one of the three states

> ## `R1 DEPENDENCE ESTABLISHED`

**NOT `R1 INDEPENDENT`, AND NOT `R1 DEPENDENCE NOT ESTABLISHED`.** The evidence
is textual on both sides, and I set the two documents beside each other rather
than reasoning about the physics.

**SIDE ONE — the manuscript names the mechanism that generates `ε`:**

    :526-528   "the axial anomaly, realized on the lattice through THE WILSON
                TERM AND THE SURVIVING DOUBLERS"
    :592-594   "the discrete substrate breaks it explicitly---through
                WILSON-TYPE TERMS and the discrete (Z_M) structure"

**SIDE TWO — the landed `D-1c` ledger names those same objects as what `R1`
rules on, and records `R1` as open:**

    P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md:71-72
      "NODE  which lattice Dirac operator is canonical, and the parameter
             values that come with the choice"
    same:89     "CONTROLS  W8  the Wilson parameter r"
    same:95     "CANDIDATES  naive, Wilson, staggered, overlap"
    same:96     "STATUS  OPEN. §5 records the search."
    same:78-79  quoting P2-LATTICE-ROUTE-01.md:189-190 —
      "*Freeze:* … the canonical lattice Dirac operator; THE SPECIES LEDGER
       AND DOUBLING TREATMENT"
    same:311    "N_ruling  5  R1 R2 R3 R4 R5, all verified open"

**AND `P2-LATTICE-ONTOLOGY-01.md:346` makes the doubler half explicit:**

> *"doublers, IF present in the spectrum of **the declared kinetic operator**,
> are candidate physical species"*

**THE INFERENCE IS A READING, NOT A PHYSICS ARGUMENT.** The manuscript states
`ε`'s mechanism in terms of the Wilson term and the surviving doublers; the
ledger states that which operator is canonical, its parameter `r`, and the
doubling treatment are exactly what `R1` must rule and has not. **The inputs of
the stated computation are the subject of the unmade ruling.**

**I do NOT claim that `ε`'s VALUE would change under a different ruling. That
would be a physics claim and I did not make it.** What is established is that the
computation as the manuscript describes it cannot be posed without the ruling,
because its stated ingredients are the ruling's subject.

**NO PRIOR ARTIFACT MAPPED `ε` TO ANY `R`-NODE.** Searched: the `D-1c` ledger,
`P2-LATTICE-ONTOLOGY-01` and `P2-LATTICE-ROUTE-01` return zero occurrences of
`varepsilon` or `epsilon`. **This mapping is made here for the first time, from
two documents neither of which cites the other on this point.**

**AND THE `r = 1` TENSION IS REPORTED, NOT ADJUDICATED.** `CONVENTIONS.md:24`
states a Wilson term with `r = 1`; the kinetic-operator dossier says at
`:169-171` that *"the value of `r` as a canonical choice — `r = 1` is what the
exploratory script uses, not something the repository freezes"*. **Those pull in
different directions and this artifact does not resolve them.**

### 5.4 `R2`–`R5`, honestly separated

    R1  DEPENDENCE ESTABLISHED   §5.3
    R2  NOT ESTABLISHED          the ledger's R2 controls are divisibility and
                                 extent conditions; no repository line connects
                                 ε to lattice extent
    R3  NOT ESTABLISHED          no repository line connects ε to boundary
                                 conditions
    R4  NOT ESTABLISHED FOR ε    ROUTE:189 requires "microscopic variables and
                                 measure" to be frozen as a general matter, and
                                 R4 is open — but no line ties ε's computation
                                 to the measure specifically. Reporting this as
                                 established would be my physics, not the
                                 repository's text.
    R5  ESTABLISHED FOR THE Λ    :714's M_Pl² = c₂NΛ²/(8π²) contains N; R5 is N;
        LEG ONLY                 R5 is open. It does not enter ε itself.

**`NOT ESTABLISHED` IS WEAKER THAN `INDEPENDENT` AND IS NOT REPORTED AS IT.** For
`R2`, `R3` and `R4` the repository is silent about `ε`, and silence is not
independence.

### 5.5 An input no ruling node covers

**`M`, the order of the discrete `Z_M` phase symmetry, is never given a value or
a determination anywhere in the repository.** It appears on three manuscript
lines and in no derivation, script, convention or gate. **Without `M` the
potential `V_θ(θ) ≃ −K cos(Mθ)` is not a computable object**, and **no `R`-node
covers it** — `R1`–`R5` are about the Dirac operator, the extent, the boundary
conditions, the measure and `N`.

**THE SAME HOLDS FOR THE `H(4)` INSTANTON SECTOR.** `instanton` occurs on two
manuscript lines and in no derivation or script; `topological` occurs zero times
in the manuscript.

### 5.6 No gate covers this object

**MEASURED IN `GATES.md`, ALL FOURTEEN SECTIONS:**

    varepsilon  0    angular      0    instanton    0
    epsilon     0    Goldstone    0    anomaly      0
    ε           0    dark matter  0    m_theta      0

**ZERO ON EVERY TERM.** The gate register contains no gate for `ε`, the angular
mode, the pseudo-Goldstone, or the dark-matter scalar. **The object this
assessment is about has no gate.**

**AND NO REPOSITORY DERIVATION TREATS IT.** Whole-tree, `varepsilon`,
`instanton`, `pseudo-Goldstone` and `m_\theta` occur only in: the manuscript, its
recovered twin `results/recovered-2026/emergent_gr_paper_v2_7.tex`, the recovered
chat log, and this line's own `SRC-01a` and `EPS-B0` documents. **The repository's
own Goldstone artifact, `P2-PHASE-01_AC4_symmetry_and_goldstone.md`, returns ZERO
on `varepsilon`, `epsilon`, `instanton`, `anomaly`, `Z_M` and `m_theta`.**

## 6. Three and four together — would this route produce a number?

**NO, AND IT WOULD FAIL TWICE INDEPENDENTLY.**

    THE COEFFICIENT   unfixed — and the ambiguity is inside ε's own definition,
                      not merely downstream of it (§1.4, §3)
    Λ                 no internally determined value; a unit convention, an
                      assumption, or an inversion through an observed M_Pl (§4)

**Either alone would reduce the outcome to a scaling law. Both hold.**

> ## VERDICT: `BLOCKED PENDING A RULING`
>
> **The repository establishes that computing `ε` requires `R1`, and `R1` is
> OPEN.** `R5` is additionally required for the `Λ` leg, and `R5` is OPEN.
>
> **THESE NODES ARE OPEN. NO RULING HAS BLOCKED ANYTHING.** Nothing has been
> ruled; the block is a WAIT, not a consequence. `D-1c` records all five nodes as
> *"all verified open"* at its `:311`.

**AND THE RIDER, WHICH IS THE PART A READER MOST NEEDS:**

> **EVEN IF `R1` WERE RULED TOMORROW, THIS ROUTE WOULD NOT PRODUCE A NUMBER.**
> The coefficient and `Λ` are unfixed independently of `R1`, and neither is an
> `R`-node's subject. **The best outcome reachable from a settled `R1` is §3's
> SECOND verdict — `TRACTABLE BUT ONLY A RELATION` — not its first.**

**THE APPARENT SHORTCUT IS NOT ONE.** `ε` looked like a way around the
microscopic line's open rulings — a small dedicated computation that would turn a
fitted scale into a predicted one. **It waits on the same node the whole
microscopic line waits on**, and clearing that node would still leave it short of
a number by two further steps that no node covers.

## 7. What this does NOT establish

**A TRACTABLE COMPUTATION IS NOT A NUMBER.** `SRC-01a` established that
`r_c = 1/m_θ` is a derived RELATION and not a derived VALUE. **`m_θ² ~ εΛ²` has
the same shape**, and a computed `ε` with an open coefficient and an
observational `Λ` would reproduce exactly the situation `SRC-01a` diagnosed, one
link further up the chain.

**THIS READS THE MANUSCRIPT, NOT THE PHYSICS.** Whether `ε` is computable in
principle is a question about the theory. Whether this repository says how is a
question about a document. **Only the second is answered here**, and a
`NOT DETERMINABLE` finding anywhere in this artifact means the document is
silent, not that a computation is impossible.

**EVEN A FULLY SUCCESSFUL `ε` COMPUTATION WOULD MOVE ONE LINK.** `SRC-01a`
established that the identification `θ̃ ≡ χ` is fixed by the phenomenology and
rests on no internal dynamical reason, the coupling that might have grounded it
being deferred at `:641-643`. **A derived `m_θ` for a mode identified with the
dark-matter scalar on phenomenological grounds is a derived length scale FOR THAT
MODE. It is not yet a prediction OF the dark-matter scale.**

**THE SEARCH VOCABULARY IS NOT EXHAUSTIVE.** Two supplied passes plus four terms
of my own; 187 of 1833 lines read plus the surrounding argument at each cluster.
**A step using vocabulary outside all of them would have been missed.**

**AND THIS ARTIFACT DOES NOT SAY WHETHER THE ROUTE IS WORTH TAKING**, does not
compare it with `RECON-01b`, and does not adjudicate `R1`–`R5` or the `r = 1`
tension.

## 8. Stops and clarifications

**No stop was declared.**

**`REPOSITORY_DEFECT` — no gate covers `ε`, the angular mode, or the
dark-matter scalar.** `GATES.md` returns zero on all nine searched terms across
its fourteen sections, and no derivation, script or test treats the object. §5.6.

**`REPOSITORY_DEFECT` — `M`, the order of the discrete `Z_M` phase symmetry, is a
required input that no `R`-node covers and no document fixes.** §5.5.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `Z_M` collides with
the Fierz/channel-freeze normalisation constant of the same name.** Sixty-plus
files, three of the relevant lines, all in the manuscript. §5.2.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `topological`
returns zero because the manuscript writes "instanton/lattice origin".** A search
built on the expected word would have concluded the sector is absent. §2.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the `r = 1` tension.**
`CONVENTIONS.md:24` states `r = 1`; the kinetic-operator dossier at `:169-171`
says the repository does not freeze it. Reported, not adjudicated. §5.3.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — `ε` had never been mapped to
any `R`-node before this artifact.** The mapping is made here from two documents
neither of which cites the other on this point. §5.3.
