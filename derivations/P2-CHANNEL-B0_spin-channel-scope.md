# `P2-CHANNEL-B0` — which channel is gravity, and which is a fifth force?

    STATUS      CHANNEL CLASSIFICATION SCOPE ASSESSMENT. NOTHING IS DERIVED.
    BASE        af145d5a3e36e6bca62f038092748ada3abdcec1
    SUBJECT     paper/emergent_gr_paper_v2_15.tex, 1833 lines, unmodified
    VERDICT     CHANNELS SEPARATED
                the universality claim is scoped to the SPIN-2 TT channel

**This artifact reports what the repository SAYS about two mediation channels of
the same condensate.** It derives nothing, computes no coupling, suppression
factor or mixing angle, and takes no position on whether the equivalence
principle holds or whether a scalar force would be a problem. **Paper 1, Paper 4
and Paper 5 are not in this repository and were not read.**

## 1. The two channels, as the manuscript names them

**The manuscript states the two-channel structure in its own words at
`:574-576`:**

    :574  The light degrees of freedom of the theory are exclusively the
    :575  collective bosonic modes: the angular condensate mode below, and
    :576  the induced graviton of Section~\ref{sec:induced}.

**TWO LIGHT MODES, NAMED SEPARATELY, IN ONE SENTENCE.** Everything below is
whether the repository keeps them apart thereafter.

## 2. `Z`'s channel and `Z`'s source

### 2.1 The kinetic coefficient

`CONVENTIONS.md:20` defines `Z` as *"The induced axis/transverse-traceless (TT)
graviton kinetic coefficient, i.e. the coefficient of the induced
Einstein–Hilbert term `∫√g R`"*. **`Z` is a SPIN-2 KINETIC COEFFICIENT.**

**IT STATES NO COUPLING, AND I DID NOT READ ONE FROM IT.** A kinetic coefficient
says how a field propagates. It is silent about what excites it. **The source
below is taken from different lines entirely, and if those lines did not exist
this section would report that the repository says nothing.**

### 2.2 What the repository says the TT channel's source is

**IT SAYS `T^{μν}`, AND IT SAYS SO TWICE.**

    :669  S[\psi, h] = S[\psi, \eta]
    :670  + \frac{\kappa}{2}\int d^4x\; h_{\mu\nu}\,T^{\mu\nu}
    :671  + \mathcal{O}(h^2),
    :673  T^{\mu\nu} = \frac{i}{4}\,\bar{\psi}\gamma^{(\mu}
    :674  \!\overleftrightarrow{\partial}{}^{\nu)}\psi + \mathrm{h.c.}
    :675  - \eta^{\mu\nu}\mathcal{L},
    :678  where $T^{\mu\nu}$ is the symmetric energy-momentum tensor of the
    :679  fermions.

**And `:680`: *"Note that the source of gravity is the derivative bilinear …"***

**Restated as a universal statement at `:830-831`:** *"Hence all matter couples as
`$\kappa\int d^4x\,h_{\mu\nu}T^{\mu\nu}$` with a common `$\kappa$`"*.

**SO THE REPOSITORY DOES STATE THE TT CHANNEL'S SOURCE: the fermionic
energy-momentum tensor, coupled linearly to `h_{μν}` with a common `κ`.**

**AND THAT IS A STRUCTURAL STATEMENT, NOT A COMPUTED SOURCE.** `SRC-B0` already
established that no configuration usable for computation is present in this
repository. **The programme has computed one side of the TT channel — the kinetic
coefficient — and not the other.**

## 3. `θ̃`'s coupling, and universality — two separate findings

### 3.1 What the manuscript states, quoted

    :633  One element of this identification remains open: the effective
    :634  coupling of the angular mode to visible (baryonic) matter with the
    :635  scalar (monopole) structure used phenomenologically in
    :636  Ref.~\cite{Cheng:2025sparc}.
    :637  A pure Goldstone couples derivatively; a monopole coupling must be
    :638  induced by the explicit breaking and/or by mixing with the heavy
    :639  radial mode, and is therefore suppressed by powers of
    :640  $\varepsilon$ and the mixing angle.

### 3.2 The suppression — a statement about MAGNITUDE

**The manuscript states that a monopole coupling must be INDUCED — by the
explicit breaking and/or by mixing with the heavy radial mode — and is therefore
SUPPRESSED by powers of `ε` and the mixing angle.**

**THAT IS A STATEMENT ABOUT HOW LARGE THE COUPLING IS.** `:641-643` adds that
establishing the chain quantitatively is deferred to future work and that the
cited work treats the coupling as an effective parameter.

**THIS ARTIFACT REPORTS THE STRUCTURE AND NOT THE MAGNITUDE.** The magnitude is
`ε`-dependent, and **no value of `ε`, of the mixing angle, or of the coupling is
stated, computed, or treated here as frozen or derived.**

### 3.3 Universality — a separate question, separately answered

> ## `UNSTATED`

**NOT `NON-UNIVERSAL`. The suppression does not establish it, and nothing else
does.**

**SUPPRESSION AND UNIVERSALITY ARE DIFFERENT PROPERTIES.** Suppression concerns
the coupling's magnitude; universality concerns whether the scalar charge is the
same, in the relevant sense, across matter species or test bodies. **A coupling
`g ~ ε·α` with `α` common to all matter is weak AND universal.**

**SEARCHED FOR ANY STATEMENT OF OBJECT DEPENDENCE, AND FOUND NONE:**

    composition-dependent    0        charge-to-mass      0
    composition dependence   0        Eötvös              0
    baryon number            0        test body           0
    per baryon               0        torsion balance     0

**`composition` returns five lines and ALL FIVE ARE `decomposition`** — `:105`,
`:278`, `:380`, `:392`, `:1093`, every one about momentum-structure or
Hubbard–Stratonovich decomposition. **Not one is a composition dependence.**

**`species-dependent` returns two lines, `:196` and `:870`, and both are about
species-dependent LIMITING SPEEDS on the lattice** — the Lorentz-violation
analysis, not matter species.

**THE ONE ADJACENT FACT, REPORTED BECAUSE IT IS ADJACENT AND NOT BECAUSE IT
SETTLES ANYTHING.** `:634` says the coupling is to *"visible (baryonic)
matter"*. **That names what the mode couples to. It does not give a charge
law.** A coupling to baryonic matter could be proportional to mass — universal
among ordinary bodies — or to some other baryonic quantity that is not. **The
manuscript does not say which**, and `:633` calls the whole coupling "open".

**SO THE ANSWER IS `UNSTATED`, and it is unstated because the manuscript defers
the question, not because it is silent by oversight** — `:641-642` says
explicitly that establishing the coupling chain quantitatively is deferred.

## 4. The conflation search

> **COUNT: ZERO.**

**Searched for every place a halo, an attraction, or a gravitational effect is
attributed without naming the channel.** Terms: `halo`, `attract`,
`gravitational effect`, `gravitational force`, `gravitational attraction`.

**EVERY HIT NAMES ITS CHANNEL:**

    :207        "matter halo profile from THE SCALAR SECTOR of the same
                 lattice fermion framework"                    — scalar, named
    :126        "Two corrections to THE VECTOR ROUTE … its attractive
                 branch"                                       — vector, named
    :407, :417  "an additional attractive pairing operator"; "its induced
                 VECTOR COUPLING is repulsive rather than attractive"
                                                               — vector, named
    :1270       "Which VECTOR CHANNEL this is matters … The attractive
                 channel"                                      — vector, named
    :1612, :1677 "the attractive VECTOR CHANNEL"               — vector, named

**AND THE `attract` HITS ARE NOT ABOUT GRAVITY VERSUS THE SCALAR AT ALL.** They
belong to the Hubbard–Stratonovich channel analysis — which HS channel supports a
bound state — a different question from the one this artifact asks. **Counting
them as conflation would have been a false positive from a shared English word.**

**THE CLEAREST SEPARATION STATEMENT IN THE MANUSCRIPT IS `:1529-1534`:**

    :1531  Ref.~\cite{Cheng:2025sparc}, the lattice fermion framework
    :1532  produces both gravitational dynamics (induced sector) and
    :1533  ultralight dark-matter phenomenology (angular condensate mode)
    :1534  from the same microscopic Lagrangian~\eqref{eq:L0}.

**BOTH EFFECTS NAMED, EACH WITH ITS CHANNEL IN PARENTHESES, IN THE SAME
SENTENCE.** Same origin, two channels, attributed separately.

## 5. The universality claim's scope

### 5.1 It is scoped to the spin-2 TT channel, and the scope is STATED

    :816  \subsection{Emergent gauge redundancy and universal coupling}
    :818  Up to $\mathcal{O}(p^2/\Lambda^2)$ corrections, the quadratic
    :819  action defined by Eq.~\eqref{eq:PiTT} is the Fierz--Pauli action,
    :820  invariant under linearized diffeomorphisms
    :821  $h_{\mu\nu} \to h_{\mu\nu} + \partial_\mu\xi_\nu
    :822  + \partial_\nu\xi_\mu$ \cite{Fierz:1939ix}.
    :823  This gauge redundancy is not imposed; it emerges from the infrared
    :824  Ward identity.
    :825  Gauge invariance of the linear matter coupling
    :826  $\int h_{\mu\nu}X^{\mu\nu}$ requires
    :827  $\partial_\mu X^{\mu\nu} = 0$, and in a local infrared effective
    :828  theory the unique conserved symmetric tensor (up to improvements)
    :829  is the energy-momentum tensor.
    :830  Hence all matter couples as
    :831  $\kappa\int d^4x\,h_{\mu\nu}T^{\mu\nu}$ with a common $\kappa$:
    :832  the equivalence principle is an emergent consequence of the
    :833  infrared gauge structure.

**THE SCOPE IS NOT INFERRED — THE SECTION DECLARES IT IN ITS FIRST SENTENCE.**
`:818-819` opens by naming *"the quadratic action defined by
Eq.~\eqref{eq:PiTT}"*, and `eq:PiTT` is the TT kernel at `:780-785`,
`Γ^{(2)} = Z_h p² P^{TT} + O(p⁴/Λ²)×(non-TT)`.

**EVERY OBJECT IN THE ARGUMENT IS THE SPIN-2 FIELD.** `h_{μν}` at `:821`, `:826`
and `:831`; linearized diffeomorphisms at `:820-822`; the linear matter coupling
`∫h_{μν}X^{μν}` at `:826`.

**`θ̃` DOES NOT APPEAR IN THIS SUBSECTION AT ALL.** The claim is about which
tensor can couple to `h_{μν}`, and the answer — the unique conserved symmetric
tensor — is a statement about the spin-2 channel's source.

**WHAT THAT MEANS FOR THE OTHER CHANNEL, STATED CAREFULLY:** the argument
constrains what may couple to `h_{μν}`. **It says nothing about whether an
additional scalar exchange exists, or how that scalar couples.** A `θ̃` exchange
would be an interaction beyond `κ∫h_{μν}T^{μν}`, and this subsection neither
permits nor forbids it. **The universality claim's silence about `θ̃` is a
consequence of its scope, not a claim about `θ̃`.**

### 5.2 The equivalence principle's status — one of four

> ## `DERIVED HERE` — for the spin-2 channel, at the level of the linear coupling

**NOT merely `CLAIMED`:** `:825-831` gives an argument with premises and a
conclusion — gauge invariance of the linear coupling requires `∂_μ X^{μν} = 0`;
the unique conserved symmetric tensor is the energy-momentum tensor; **"Hence"**
all matter couples with a common `κ`. **The word "consequence" at `:832` is
backed by the two sentences preceding it.**

**NOT `DERIVED ELSEWHERE AND CITED`:** the only citation in the passage is
Fierz for the Fierz–Pauli action's form, not for the universality conclusion.

**NOT `TESTED`:** `Eötvös` 0, `test body` 0, `torsion balance` 0, and no
composition-dependence analysis anywhere. **Nothing in this repository tests it.**

**AND THE DERIVATION'S OWN LIMITS, RECORDED RATHER THAN GLOSSED:** it is four
lines long; it holds *"up to `O(p²/Λ²)` corrections"* per `:818`; its uniqueness
premise is asserted *"in a local infrared effective theory … (up to
improvements)"* at `:827-829` rather than proved here; and it is a statement at
the level of the LINEAR coupling. **`DERIVED HERE` is the correct state of the
four, and it is not the same as established.**

## 6. The inventory

### 6.1 Two passes over the manuscript

    PASS 1, lines                    PASS 2, lines
      transverse-traceless   10        tensor              33
      TT                    147        scalar mode          0
      spin-2                 13        angular mode         9
      spin-0                  0        mixing angle         1
      graviton               21        composition          5
      equivalence principle   1        Eötvös               0
      universal              26        test body            0
      fifth force             0        geodesic             0
      Yukawa                  4        source               3
      monopole                3        charge               0
      derivative coupling     0        gauge redundancy     2

      PASS 1 union          212        PASS 2 union        53

    PASS 1 only   203
    BOTH            9
    PASS 2 only    44
    UNION         256      of 1833 lines

**THE RESEARCHER'S SIX FILE COUNTS OVER `derivations/` AND `paper/` REPRODUCE
EXACTLY:** `spin-2` 1 file, `spin-0` 0, `fifth force` 0,
`transverse-traceless` 2, `equivalence principle` 1, `universal coupl` 1.

### 6.2 `TT` is 147 lines of noise and 10 lines of signal

**`TT` matched case-insensitively as a substring returns 147 manuscript lines.
As an uppercase token `\bTT\b` it returns TEN.**

**What the other 137 are:**

    lattice   68        splitting   7
    matter    21        ttcheck     6
    witten     8        lett        6   (bibliography)
                        attractive  6

**A count of 147 would have suggested the TT channel saturates the manuscript.
The signal is ten lines.**

### 6.3 Terms I added, and why

**`spin-1/0`, `spin-1`, `scalar channel`, `scalar sector`, `scalar block`,
`species-dependent`, `baryon number`, `charge-to-mass`, `torsion balance`.**

**THE ADDITION THAT MATTERED IS `spin-1/0`.** §3 of the specification warned that
the repository might separate the channels in vocabulary the supplied list does
not contain, and it does — see §7.1. **`spin-0` returns zero; `spin-1/0` returns
one line, and that line is a separation statement of the sharpest kind.**

**`scalar channel` (5 lines) and `scalar sector` (2) carry the contrast that
`scalar mode` (0) misses.**

**NEITHER SUPPLIED LIST IS EXHAUSTIVE AND NEITHER IS MINE**, and I read the union
plus the surrounding argument at each cluster rather than the whole file.

## 7. The verdict

> ## `CHANNELS SEPARATED`
>
> **The repository distinguishes spin-2 from spin-0 mediation, and the
> universality claim is scoped to the SPIN-2 TT CHANNEL.**

### 7.1 The evidence, and it does not rest on vocabulary counts

**FIRST — the manuscript contrasts the two channels explicitly, `:96`:**
*"we verify this by explicit one-loop lattice computations in both **the scalar
channel** and **the graviton (stress-tensor) channel**."*

**SECOND — it names both light modes separately, `:574-576`** — the angular
condensate mode and the induced graviton.

**THIRD, AND SHARPEST — `:810-814` makes the separation a TEST CRITERION:**

    :810  A lattice measurement of the Barnes--Rivers--projected
    :811  stress-tensor correlator, checking for a single $p^2 = 0$ pole in
    :812  the spin-2 sector with vanishing spin-1/0 residues, is the decisive
    :813  test; we identify it as the key numerical milestone for this
    :814  programme.

**REQUIRING THE SPIN-1/0 RESIDUES TO VANISH IN THE TT CORRELATOR IS AN EXPLICIT
DEMAND THAT THE CHANNELS BE SEPARATE.** It is stated as the programme's key
numerical milestone.

**FOURTH — `:787-788`:** *"the only possible massless pole resides in the TT
spin-2 channel."*

**FIFTH — `:1529-1534` attributes the two phenomenologies to the two channels by
name**, in parentheses, in one sentence.

**SIXTH — the universality subsection scopes itself to `eq:PiTT` in its opening
sentence** and never mentions `θ̃` — §5.1.

**THE VERDICT RESTS ON READING THE ARGUMENT.** `spin-0` returns zero and `fifth
force` returns zero, **and neither absence was used as evidence for anything.**
The separation is stated in the manuscript's own vocabulary — `spin-1/0`, `the
scalar channel`, `the graviton (stress-tensor) channel`, `the angular condensate
mode`, `the induced graviton` — and **the specification's word list was the thing
that was wrong, exactly as its §3 anticipated.**

### 7.2 The manuscript's own classification of the scalar channel

**REPORTED AS THE MANUSCRIPT'S CLASSIFICATION AND NOT DERIVED FROM THE MEDIATOR'S
SPIN.**

**The manuscript calls the angular mode a DARK-MATTER mechanism**, at `:81`,
`:443` (*"Condensate; light angular mode (dark matter [cite])"*), `:612`
(*"Identification with the dark-matter mode"*), `:1533` and `:1557`.

**THIS ARTIFACT DOES NOT ENDORSE OR DISPUTE THAT CLASSIFICATION**, and it does not
derive it from the fact that `θ̃` is spin-0. **A spin-0 mediator is a
scalar-mediated additional force; whether that force belongs to a dark sector, to
scalar–tensor modified gravity, or elsewhere depends on the coupling structure —
which §3.3 found `UNSTATED`.**

### 7.3 The parameter-independence statement, as `A9` requires verbatim

> **Channel separation does not establish parameter independence.** The spin-0
> and spin-2 observables may be conceptually distinct while the scalar channel's
> strength remains dependent on unresolved microscopic data through `ε`.

## 8. What this does NOT establish

**IT REPORTS WHAT THE REPOSITORY SAYS ABOUT TWO CHANNELS. IT DOES NOT ESTABLISH
WHICH CHANNEL IS PHYSICALLY RESPONSIBLE FOR ANYTHING.** `CHANNELS SEPARATED`
means the documents are clear, **not that the separation is correct.**

**UNIVERSALITY AND STRENGTH ARE SEPARABLE AND ONLY THE FIRST WAS ASSESSED.** The
scalar coupling's magnitude is `ε`-dependent and is not reported here as frozen,
derived, or independently determined.

**THE CLASSIFICATION FOLLOWS NEITHER FROM THE MEDIATOR'S SPIN NOR FROM THE
COUPLING'S SUPPRESSION.** Both are non-inferences and both were declined — §3.3,
§7.2.

**A NON-UNIVERSAL SCALAR FORCE WOULD NOT BE A DEFECT, AND NEITHER WOULD A
UNIVERSAL ONE.** Scalar-mediated dark matter is a legitimate mechanism; so is a
universally coupled scalar in the gravitational sector. **This is a
classification, not a criticism**, and §3.3's answer is `UNSTATED` in any case.

**`Z` BEING A KINETIC COEFFICIENT TELLS NOTHING ABOUT ITS SOURCE.** The
programme has computed one side of the TT channel and not the other, and `SRC-B0`
already established the source side is absent from this repository.

**THE EQUIVALENCE PRINCIPLE IS `DERIVED HERE` FOR THE SPIN-2 CHANNEL — NOT
CLAIMED, NOT DERIVED ELSEWHERE, NOT TESTED.** Those four are not
interchangeable, and the derivation's own limits are recorded at §5.2.

**THE VOCABULARY WAS THE RESEARCHER'S AND BOTH PASSES MISSED THE SEPARATION'S
ACTUAL WORDING.** An absence of `spin-0` and `fifth force` is not evidence that
the channels are conflated — **and in this case it was evidence of nothing at
all**, since the separation is stated in other terms.

## 9. Stops and clarifications

**No stop was declared.**

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `TT` returns 147
manuscript lines as a substring and 10 as an uppercase token.** 68 of the
remainder are `lattice`. §6.2.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `composition`
returns five lines and all five are `decomposition`.** Had they been counted as
composition dependence, `A6` would have returned `NON-UNIVERSAL` on a substring.
§3.3.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — the `attract` hits
belong to the Hubbard–Stratonovich vector-channel analysis, not to gravity versus
the scalar.** Counting them as conflation would have been a false positive from a
shared English word. §4.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — `θ̃`'s universality is
`UNSTATED` and the manuscript defers the question explicitly.** `:641-642` says
establishing the coupling chain quantitatively is deferred to future work. **The
question cannot be answered from this repository.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the specification's channel
vocabulary did not match the manuscript's.** `spin-0` returns zero while
`spin-1/0` at `:812` carries the separation. **Recorded because a verdict built
on the supplied word list alone would have been wrong.** §6.3, §7.1.
