# `P2-SRC-01a` — is the halo configuration derived, fitted, or both?

    STATUS      PROVENANCE ASSESSMENT. NOTHING IS COMPUTED AND NOTHING IS IMPORTED.
    BASE        de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    SUBJECT     paper/emergent_gr_paper_v2_15.tex, 1833 lines, unmodified
    VERDICT     FORM DERIVED / SCALE FITTED

**This artifact reads one manuscript already in this repository and reports what
that manuscript establishes about the origin of the halo configuration and its
parameters.** It computes no profile, fits no data, evaluates no phenomenology,
and reads nothing outside this repository. **Paper 1 is not here and was not
read**; every statement below about Paper 1 is THIS MANUSCRIPT'S CLAIM about it,
marked as such.

**It does not revise `SRC-B0`'s verdict.** A configuration usable for
computation is still absent; nothing here supplies one.

## 1. The manuscript, measured

    paper/emergent_gr_paper_v2_15.tex        1833 lines
    wc -l and grep -c "" agree at 1833; the file ends with a newline

**The specification's pre-issue record gives 1834.** The difference is the
standard one between counting newline characters and counting a final
unterminated line; **there is no unterminated final line here, so 1833 is the
line count under both conventions.** Nothing turns on it, and every line number
quoted below was read at the head.

## 2. The two-pass inventory

**PASS 1 — the seed terms. Lines matched, case-insensitive substring:**

    sparc              15        fit                 7
    halo                2        derive              5
    rotation curve      0        profile             1
    r_c                 2        Yukawa              4
    m_theta             0        m_\theta            7

    PASS 1 distinct lines: 36

**`m_theta` RETURNS ZERO AND `m_\theta` RETURNS SEVEN**, exactly as the
specification warned: the manuscript writes the LaTeX macro. **`rotation curve`
returns zero** — the phrase does not occur.

**PASS 2 — the identification terms:**

    chi                72        dark matter         3
    \theta             29        Green               2
    \tilde\theta        3        cutoff             14
    ultralight         11        identif            14
    scalar sector       2

    PASS 2 distinct lines: 137

**UNION AND ACCOUNTING:**

    PASS 1 only     24
    BOTH            12
    PASS 2 only    125
    UNION          161

**PASS 2 CONTRIBUTES 125 LINES THAT PASS 1 DOES NOT REACH — more than three
times PASS 1's entire yield.** Among them is `:80`:

> `This mode is identified with the ultralight scalar responsible for`

**That is the carrier identification, and the seed list does not reach it.** An
inventory built on PASS 1 alone would have supported a provenance verdict about
a subset of the argument — specifically, about the parameters, with the step
that makes the parameters relevant missing.

**The specification's author measured 136 lines found only by PASS 2; I measure
125.** Both are correct under their own matching convention — the figure depends
on how `fit`, `derive` and `m_\theta` are matched in PASS 1, and a wider PASS 1
lowers the PASS-2-only count by moving lines into the intersection. **The
substantive claim reproduces exactly: `:80` is reached only by PASS 2, and PASS
2 supplies the large majority of the union.**

### 2.1 Which `chi` hits are substantive

**`chi` returns 72 lines and 71 of them are about something else.**

    lines containing the LaTeX macro \chi         15
    lines with "chi" but no \chi macro            57
      of which: chiral 36, chirally 8, machinery 7, machine 3,
                matching 2, chiralmass 1

**And of the fifteen `\chi` lines, FOURTEEN denote objects that are not the
ultralight scalar:**

    :260              G_\chi        a coupling in the chiral sector
    :938 :944 :983-:986 :994  c_\chi^2   the collective-mode speed
    :953 :955        \xi_\chi      a non-minimal coupling coefficient
    :1198-:1200 :1203  \tilde\chi  the RADIAL (amplitude) fluctuation

**EXACTLY ONE OF SEVENTY-TWO `chi` HITS IS THE IDENTIFICATION:**

    :616   We identify $\tilde\theta$ with the ultralight scalar $\chi$ whose

**A count of 72 that is really 1 is the clearest measurement-quality fact in
this task.** The same symbol carries four different physical meanings in this
manuscript, and `\tilde\chi` at `:1198` is the mode the identification passage
at `:628-631` explicitly EXCLUDES from low-energy relevance.

### 2.2 Vocabulary added beyond both lists

**I added `varepsilon` and read every one of its eleven lines**, because PASS 2
established that `m_θ` is fixed through `m_θ² ~ εΛ²` and neither list reaches
the breaking parameter itself. **That addition is what produced §5.3's finding**,
and without it the parameter chain would have terminated one step early.

**NEITHER LIST IS EXHAUSTIVE.** They are the Researcher's, and they came from a
description of the manuscript rather than from the manuscript. **A derivation
using vocabulary outside both would be missed by this inventory.**

## 3. The passages, verbatim

### 3.1 The introduction's claim, `:206-210`

    :206  In Ref.~\cite{Cheng:2025sparc}, we derived a Yukawa-type dark
    :207  matter halo profile from the scalar sector of the same lattice
    :208  fermion framework and tested it against 175 SPARC galaxies.
    :209  The present paper develops the gravitational sector and the vacuum
    :210  structure that underlies both papers.

**The sentence is in the past tense and its subject is another paper.** `:209`
states what THIS paper does, and it is the gravitational sector and the vacuum
structure — not the halo profile.

### 3.2 The carrier identification, `:76-81`

    :76   while the angular direction of the complex condensate hosts a
    :77   naturally light pseudo--Goldstone mode whose mass is protected by
    :78   the same approximate $U(1)$ symmetry, broken only by the discrete
    :79   lattice structure.
    :80   This mode is identified with the ultralight scalar responsible for
    :81   the dark-matter phenomenology of Ref.~\cite{Cheng:2025sparc}.

**`:76-79` is a result of this manuscript. `:80-81` is an identification with an
object defined elsewhere, and it is asserted, not argued.**

### 3.3 The halo passage, `:612-625`

    :612  \item \textbf{Identification with the dark-matter mode.}
    :613  The static field equation of $\tilde\theta$ is that of a massive
    :614  scalar, with Yukawa Green's function of range
    :615  $r_c = 1/m_\theta$.
    :616  We identify $\tilde\theta$ with the ultralight scalar $\chi$ whose
    :617  galactic-scale phenomenology was tested in
    :618  Ref.~\cite{Cheng:2025sparc}; the SPARC-scale cutoff radii
    :619  $r_c \sim 10\,\mathrm{kpc}$ correspond to
    :620  $m_\theta \sim 10^{-27}\,\mathrm{eV}$, i.e.\
    :621  $\varepsilon \sim m_\theta^2/\Lambda^2$, an extraordinarily good
    :622  approximate symmetry.
    :623  This pseudo--Goldstone origin places the model's ultralight scale
    :624  on the same mechanistic footing as axion-like ultralight
    :625  dark-matter scenarios \cite{Hui:2016ltb}.

### 3.4 The open coupling, `:633-644`

    :633  One element of this identification remains open: the effective
    :634  coupling of the angular mode to visible (baryonic) matter with the
    :635  scalar (monopole) structure used phenomenologically in
    :636  Ref.~\cite{Cheng:2025sparc}.
    :637  A pure Goldstone couples derivatively; a monopole coupling must be
    :638  induced by the explicit breaking and/or by mixing with the heavy
    :639  radial mode, and is therefore suppressed by powers of
    :640  $\varepsilon$ and the mixing angle.
    :641  Establishing this coupling chain quantitatively is deferred to
    :642  future work; in Ref.~\cite{Cheng:2025sparc} the coupling is
    :643  treated as an effective parameter, so the phenomenological results
    :644  there are unaffected.

### 3.5 Does the Researcher's reading survive?

**YES, AND IT UNDERSTATES THE CASE IN ONE DIRECTION AND OVERSTATES IT IN
ANOTHER.**

**IT SURVIVES ON THE FORM.** `:613-615` derives the Yukawa Green's function from
the static field equation of a massive scalar — a step this manuscript performs,
not one it cites.

**IT SURVIVES ON THE SCALE, AND `:618-620` IS MORE EXPLICIT THAN THE READING
SUGGESTED.** The sentence's direction is unambiguous: the SPARC-scale radii
`r_c ~ 10 kpc` "correspond to" `m_θ ~ 10⁻²⁷ eV`. **The observation is the input
and the mass is the output.** `:621` then runs the chain one step further,
inferring `ε ~ m_θ²/Λ²`.

**WHERE IT UNDERSTATES: the manuscript itself says `ε` is not computed.** §5.3.

**WHERE IT OVERSTATES: `:613-615` is not the halo profile.** It is the Green's
function of the mediating field. **A halo profile additionally requires a source
distribution and a coupling to it, and this manuscript supplies neither** — §3.4
records the coupling as open. **The word `halo` occurs on exactly two lines in
1833**: `:207`, the citation sentence, and `:1815`, the bibliography title.

## 4. Claimed here versus established here

**Every load-bearing statement about the halo, classified.**

    CLAIMED HERE AND DERIVED HERE                                        3
      :76-79   the angular pseudo-Goldstone mode exists and its mass is
               protected by the approximate U(1)
      :598     m_θ² ~ ε Λ², the mass RELATION, with ε undetermined
      :613-615 the static field equation of θ̃ is a massive scalar's, so its
               Green's function is Yukawa with range r_c = 1/m_θ

    CLAIMED HERE, CITED TO PAPER 1                                       6
      :80-81   this mode IS the ultralight scalar of Ref. [Cheng:2025sparc]
      :206-208 "we derived a Yukawa-type dark matter halo profile … and
               tested it against 175 SPARC galaxies"
      :443     the light angular mode is "dark matter [Cheng:2025sparc]"
      :616-618 θ̃ is identified with χ "whose galactic-scale phenomenology
               was tested in Ref."
      :1529-:1534 the framework "produces both gravitational dynamics and
               ultralight dark-matter phenomenology"
      :1555-:1558 summary: the mode is "identified with the ultralight
               dark-matter scalar of Ref."

    NOT ADDRESSED (explicitly open in this manuscript)                   3
      :541-544 the magnitude of ε "is the dedicated computation left open"
      :633-644 the monopole coupling to baryons — "remains open", "deferred
               to future work"
      :1626-1630 the same, in the Limitations list: "the quantitative chain
               is open"

    TOTAL load-bearing statements classified                            12

**THE DISTRIBUTION IS THE FINDING.** Three steps are performed here, six are
asserted and pointed elsewhere, three are stated as open by the manuscript
itself. **A sentence beginning "we derived" is a claim about another paper, and
this manuscript does not contain the derivation it names.**

**NOTHING VERIFIES THE SIX CITED CLAIMS.** They are recorded as this
manuscript's claims. Paper 1 is not in this repository and was not read.

## 5. Provenance, parameter by parameter — the identification first

### 5.1 The identification

    WHICH MODE      the angular (phase) direction of the complex condensate
                    Φ ~ ψ̄_R ψ_L, i.e. the pseudo-Goldstone θ̃
    WITH WHAT       χ, the ultralight scalar of Ref. [Cheng:2025sparc]
    WHERE           :80-81 (introduction) and :616-618 (Section angular),
                    restated at :443, :1531-:1534 and :1555-:1558
    ON WHAT BASIS   ASSERTED. The manuscript states the identification; it
                    does not derive it, and it offers one supporting
                    argument of a different kind — :623-625, that the
                    pseudo-Goldstone origin puts the scale "on the same
                    mechanistic footing as axion-like ultralight dark-matter
                    scenarios". That is a plausibility statement about a
                    class of models, not a derivation that this mode IS that
                    scalar.
    A6 CATEGORY     CLAIMED HERE, CITED TO PAPER 1

**THE IDENTIFICATION IS LOAD-BEARING AND IT IS THE WEAKEST LINK IN THE CHAIN.**
Everything downstream — that `r_c` is a galactic scale at all, that `m_θ` is
ultralight, that `ε` is tiny — follows from it. **If the identification is
withdrawn, the manuscript still has a pseudo-Goldstone mode with an undetermined
mass, and nothing connects it to a galaxy.**

**AND IT IS PARTLY FIXED BY THE PHENOMENOLOGY IT IS MEANT TO EXPLAIN.** The mode
is identified with the dark-matter scalar, and then the dark-matter scalar's
observed scale is used to fix the mode's mass — §5.3. **The manuscript is
explicit about this direction and does not disguise it.**

### 5.2 `r_c`

    WHAT THE MANUSCRIPT SAYS FIXES IT
      the relation r_c = 1/m_θ, derived at :613-615 from the static field
      equation
    WHAT DETERMINES ITS VALUE
      OBSERVATION. :618-619 takes "the SPARC-scale cutoff radii
      r_c ~ 10 kpc" as given.
    PROVENANCE   FITTED — an observational input, quoted from :619

### 5.3 `m_θ`, and this is where the chain terminates

    WHAT THE MANUSCRIPT SAYS FIXES IT
      two relations, both derived here:
        m_θ² ~ ε Λ²        :598
        r_c  = 1/m_θ       :615
    WHAT DETERMINES ITS VALUE
      :619-:620 — "the SPARC-scale cutoff radii r_c ~ 10 kpc correspond to
      m_θ ~ 10⁻²⁷ eV". THE OBSERVED RADIUS IS THE INPUT AND THE MASS IS THE
      OUTPUT.
    PROVENANCE   FITTED, via r_c

**`r_c = 1/m_θ` IS A RELATION, NOT A DETERMINATION.** It converts one unknown
into another. **The determination enters at `:619` and it is observational.**

**AND `ε` DOES NOT RESCUE IT, BECAUSE THE MANUSCRIPT SAYS `ε` IS NOT COMPUTED.**
`:621` runs the inference in the same direction — `ε ~ m_θ²/Λ²`, i.e. `ε` is
inferred FROM `m_θ`, which was inferred from `r_c`, which came from SPARC. And
`:541-544` states plainly:

> `(The magnitude of $\varepsilon$ on the $H(4)$ substrate---in particular
> whether the anomaly contribution is exponentially instanton-suppressed---is
> the dedicated computation left open in Section~\ref{sec:angular}.)`

**SO THE SCALE CHAIN RUNS OBSERVATION → `r_c` → `m_θ` → `ε`, IN THAT DIRECTION,
AND NO STEP OF IT RUNS THE OTHER WAY.** `:1681-1683` lists the reverse direction
as future work: "the explicit-breaking chain fixing the angular-mode coupling to
baryons, **connecting `ε` to the SPARC-scale phenomenology**".

**THIS IS THE PLAIN STATEMENT `A7` ASKS FOR: `r_c ~ 10 kpc` is taken from SPARC
and `m_θ` is inferred from it.**

### 5.4 The coupling and the amplitude

    WHAT THE MANUSCRIPT SAYS FIXES IT
      NOTHING. :633-644 records the monopole coupling of the angular mode to
      baryonic matter as open, states the mechanism that would have to
      produce it (explicit breaking and/or radial-mode mixing), and defers
      the quantitative chain to future work. :1626-1630 repeats it under
      Limitations.
    WHAT PAPER 1 DOES WITH IT, ACCORDING TO THIS MANUSCRIPT
      ":642-644  in Ref.~\cite{Cheng:2025sparc} the coupling is treated as
      an effective parameter, so the phenomenological results there are
      unaffected."
    PROVENANCE   NEITHER DERIVED NOR FITTED HERE — explicitly open, and
                 carried in the cited work as a free effective parameter

**THE AMPLITUDE OF THE PROFILE IS NOT ADDRESSED AT ALL IN THIS MANUSCRIPT.**
There is no normalisation, no source distribution, and no profile function.

## 6. The verdict

> ## `FORM DERIVED / SCALE FITTED`

**WHICH PARAMETERS FALL ON WHICH SIDE:**

    DERIVED HERE
      the FUNCTIONAL FORM — Yukawa, i.e. the Green's function of a massive
      scalar, from θ̃'s static field equation at :613-615
      the RELATION r_c = 1/m_θ, same lines
      the RELATION m_θ² ~ ε Λ² at :598

    FITTED — set from observation
      r_c        taken as the SPARC-scale radius at :619
      m_θ        inferred from r_c at :619-620
      ε          inferred from m_θ at :621

    NEITHER — explicitly open in this manuscript
      the coupling of the mode to baryonic matter  :633-644, :1626-1630
      the amplitude / normalisation of any profile  not addressed
      the magnitude of ε from first principles      :541-544

**WHY NOT `DERIVED`.** Nothing in this manuscript predicts `m_θ`, `r_c` or `ε`.
Every numerical scale in the chain enters at `:619` from observation.

**WHY NOT `FITTED`.** The Yukawa form is not chosen to match anything. It
follows from the mode being a massive scalar, which follows from the
pseudo-Goldstone structure this manuscript derives. **A fitted profile would be
one selected for its agreement; this form is forced by the field equation and
then given a scale.**

**WHY NOT `NOT DETERMINABLE FROM THIS MANUSCRIPT`, AND THE SCOPE THAT MAKES THE
DIFFERENCE.** The verdict above is about the object this manuscript actually
treats: **the Yukawa Green's function of the identified mode, with range `r_c`.**
For that object the manuscript is explicit on both halves and settles it.

**FOR A DIFFERENT AND BROADER OBJECT — Paper 1's dark-matter halo profile fitted
to 175 galaxies — THE ANSWER IS `NOT DETERMINABLE FROM THIS MANUSCRIPT`**, and
the two must not be conflated. `:206-208` claims that profile was derived and
tested; **this manuscript performs neither step, mentions `halo` on two lines
out of 1833, contains no profile function, no source distribution and no data,
and leaves the coupling that would connect the mode to baryons explicitly
open.** **What would settle it is Paper 1 itself, which is not in this
repository.**

**Both statements are reported because the question admits both objects and
compressing them into one verdict would lose the distinction.** The primary
verdict is the first, because §1's question names "the halo profile" and the
manuscript's own treatment of it is the Yukawa form with a fitted scale.

## 7. What would remain testable — an implication, not a recommendation

**Under `FORM DERIVED / SCALE FITTED`, the following is what the classification
implies. This artifact does not say whether the source-side test should be
done.**

**NOT TESTABLE AGAINST THE SAME DATA:**

- **any statement whose content is the value of `r_c`, `m_θ` or `ε`.** These
  were set from the SPARC-scale radius. A calculation that recovered
  `r_c ~ 10 kpc` would be recovering its own input.
- **the overall normalisation of any potential**, since the coupling is a free
  effective parameter in the cited work and open here.

**POTENTIALLY TESTABLE, BECAUSE NOT FIXED BY THE FITTED SCALE:**

- **the SHAPE at fixed `r_c`.** Yukawa is a one-parameter family once the range
  is given; whether real systems follow that shape after the range is fitted is
  not guaranteed by having fitted the range.
- **CROSS-SYSTEM behaviour.** One fitted scale cannot absorb a scaling relation
  across many systems. **Whether the framework predicts such a relation is not
  determinable here** — this manuscript contains no scaling relation, and
  `SRC-B0` measured that `r_c ∝ V_max^{0.82}` occurs nowhere in the repository.
- **the coupling chain itself**, `:1681-1683`'s future-work item (iii): deriving
  `ε` and the monopole coupling from the explicit-breaking structure, and then
  checking whether the resulting `m_θ` agrees with `10⁻²⁷ eV`. **That would run
  the chain in the opposite direction from `:619-621` and would be a genuine
  prediction** — and it is exactly the computation `:541-544` records as open.

**THE CIRCULARITY RISK IS REAL BUT BOUNDED, AND THE BOUND IS WHAT MATTERS.** A
test that compared a computed potential's scale to the SPARC scale would be
circular. A test of shape or of cross-system behaviour at fixed range would not
be, **provided the range is declared as an input rather than a result.** **This
artifact does not judge whether such a test is worth doing.**

## 8. What this assessment does NOT establish

**IT READS PAPER 2'S DESCRIPTION OF PAPER 1'S WORK. IT DOES NOT READ PAPER 1.**
Every statement here about what Paper 1 derived, fitted or tested is THIS
MANUSCRIPT'S CLAIM, and **nothing here verifies any of it.** **The `FORM DERIVED`
half of the verdict is a verdict about what this manuscript performs; the
statements about Paper 1's profile are verdicts about what is CLAIMED.**

**A PROVENANCE VERDICT SUPPLIES NO CONFIGURATION.** `SRC-B0`'s finding stands
unchanged: nothing usable for computation is in this repository. **This task
moves the question, not the blocker.**

**IT DOES NOT EVALUATE WHETHER THE HALO PHENOMENOLOGY IS CORRECT.** Provenance
and validity are different questions and only the first was asked.

**IT DOES NOT SETTLE THE `Γ`-VERSUS-`S` SOURCE DEFINITION**, touch `R1`–`R5`, or
choose any tolerance.

**AND THE INVENTORY IS NOT EXHAUSTIVE.** The search terms came from a
description of the manuscript rather than from the manuscript itself, and I
added one term of my own (`varepsilon`) after PASS 2 showed the chain ran
through it. **A derivation using vocabulary outside all three would be missed.**

## 9. Stops and clarifications

**No stop was declared.**

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `chi` returns 72
lines of which exactly one is the subject.** Seventy-one are `chiral`,
`machinery`, or three other physical objects sharing the symbol. §2.1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `m_theta` returns
zero and `m_\theta` returns seven.** A seed list written from a description
rather than from the file misses the notation the file uses.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the taxonomy needed
repairing.** `SRC-B0`'s two-way `DERIVED`/`FITTED` split cannot express this
manuscript's actual position, which is that the form is derived and the scale is
observational. **A taxonomy that cannot express the answer is a defect in the
question, not in the material.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the identification is asserted
and is load-bearing.** Nothing in this repository can establish or refute it,
because the object it identifies the mode WITH is defined in a manuscript that is
not here.
