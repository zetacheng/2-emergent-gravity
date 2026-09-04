# `P2-XI-HSPRESC-01` — the decoupling prescription for the assembled chain

Authority: `specs/2026-08-25T1200Z_xi-hspresc-01_v6.md`, approved for
execution by `reviews/chatgpt/2026-08-25T1200Z_xi-hspresc-01_v6.md`.

**This artifact defines. It does not evaluate.** It fixes the decoupling
prescription for the assembled chain in the sense
`derivations/P2-FIERZSUM-01.md:218-220` states, and it identifies the
normalization object the landed criterion names. It computes nothing about
that object.

Every `path:line` in this artifact resolves at the Base
`b01bb18ba51008d09b64b442afad37b800b2d3d1`, and every quotation was extracted
from the file's bytes at that commit — none was transcribed from a rendering,
a truncated display, or memory. Two quotation forms are used and their
normalizations differ:

    fenced block quotation    the cited byte range exactly, verified by
                              containment against the file's bytes.
                              Normalization: NONE.

    inline quotation, in “ ”  the cited byte range with runs of whitespace —
                              including the source's own line breaks and
                              leading indentation — collapsed to single
                              spaces, verified by containment against the
                              identically collapsed bytes of the cited range.
                              Normalization: WHITESPACE COLLAPSE, and nothing
                              else. No character is added, removed or altered.

Both checks are re-run over the artifact's committed bytes and their result is
recorded in the report.

---

## 0. The conditions this artifact carries

    COND-R  Chosen representation, not representation independence. The
            prescription fixes the decoupling THIS chain uses. It is not a
            claim about admissible decouplings generally, and the
            family-wide question remains the registered open item.

    COND-M  Functional-measure status. `DET-01` is landed NOT DETERMINABLE.
            The prescription fixes the MEASURE TREATMENT required by the
            landed construction, to the extent landed authority determines
            it; it does not fix `𝔊`. This wording presupposes nothing about
            the form that treatment takes — in particular it does not
            presuppose a change of variables, invertible or otherwise,
            between the fermionic and auxiliary-field measures. What the
            landed construction does to the measure is identified at `E5`
            from landed text. Where an element depends on the unfixed
            measure, this artifact says so and defines the element as far as
            landed conventions determine it, leaving the remainder
            explicitly measure-inherited.

    COND-J  Definition, not evaluation. Every statement about `N_α[g]` and any
            Jacobian contributing to it in this artifact is definitional. The
            artifact carries this sentence and no sentence inconsistent with
            it.

**Enumeration rule for the conditioned statements, stated before any of them
is written.** A conditioned statement — an element-fixing statement of §3, or
a result-stating statement of §4 or §5 — is a line of this artifact that
satisfies both of:

    (a) it lies OUTSIDE every fenced block. Fenced blocks are delimited by
        lines whose bytes are exactly ``` or ```text, and their contents are
        quoted landed text, not statements of this artifact. Landed text
        quoted here carries its own source's COND markers, and those markers
        are the source's, not this artifact's.

    (b) its bytes END with `| COND-R, COND-M**` or with
        `| COND-R, COND-M, COND-J**`. The two trailing asterisks are part of
        the bytes: every such statement is emphasis-wrapped, and the rule is
        stated against the bytes rather than against the rendering.

Outside fenced blocks the marker occurs at a line's end in every conditioned
statement, and occurs elsewhere only inside backticks in the two passages that
state this rule — this one and §6.3 — where it is being named rather than
used. The set and count are measured over the artifact's own committed bytes
and recorded in the report; the `C3` check runs over exactly that set.

---

## 1. `M0` — precondition and provenance, measured before any write

Execution location, per Amendment D: worktree `/home/user/2-emergent-gravity`,
non-shallow, working tree clean at entry, `HEAD` resolved to
`b01bb18ba51008d09b64b442afad37b800b2d3d1`.

    Base, measured                 b01bb18ba51008d09b64b442afad37b800b2d3d1
    Base, pinned by the spec       b01bb18ba51008d09b64b442afad37b800b2d3d1
    equal, as a full string        yes

`M0(a)` — the R-1 ruling, as a **pre-registered comparison**: the
specification stated both values before the measurement was taken.

    path                    decisions/P2-XI-RULINGS-03.issued.md
    sha256, measured        1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
    sha256, pre-registered  1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
    git blob id, measured   0b331afb6f21f6591a0c3934fc8916bda742d8de
    git blob id, pre-reg.   0b331afb6f21f6591a0c3934fc8916bda742d8de
    both, as full strings   equal
    bytes                   5604

    register record         decisions/2026-08-31-xi-rulings-03.md, present
    decision key            2026-08-31-xi-rulings-03, present at :5 and :39

`M0(b)` — the prior ruling document:

    path                    decisions/P2-XI-RULINGS-02.issued.md
    sha256, measured        ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    sha256, pre-registered  ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    equal, as a full string yes

`M0(c)` — the ledger artifact, `derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md`,
sha256 `aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454`, 23217
bytes. Both rows present, both valueless, both OPEN, quoted from the file's
bytes at `:305-307`:

```text
    condensate scalar's own                 —                            —     OPEN(Q-M2)
      fluctuation loop
    Hubbard–Stratonovich Jacobian /         —                            —     OPEN(Q-M3)
```

The two `—` entries in each row are the value columns. No number, sign, bound
or estimate stands in either.

**`C0` is satisfied. No `A0` condition is met.**

---

## 2. `M1` — provenance extraction, before any definition is written

### 2.1 The R-1 ruling in full

`decisions/P2-XI-RULINGS-03.issued.md:1-105`:

```text
# PI RULING — R-1: THE DECOUPLING OF THE ASSEMBLED CHAIN

    STATUS      ISSUED TEXT. This document is the ruling. Any
                translation, summary, or restatement elsewhere is a
                rendering of it.
    AUTHORITY   PI (Zeta Hoi-Ho Cheng)
    DATE        2026-08-31
    SUPERSEDES  The document of the same identifier bearing SHA-256
                f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8,
                which was reviewed FIT FOR RECORDING but not landed.
                Its RATIONALE named the exponent mapping as the second
                element not fixed by landed text. That was wrong:
                P2-XI-QM3-DEP-01 records the exponent mapping as FIXED
                at g = +2c by DECISION_LOG.md:1258-1262, and names the
                decoupling prescription as the second unfixed element.
                The correction is confined to that RATIONALE; every
                RULING line is unchanged.
    IDENTIFIER  P2-XI-RULINGS-03. A canonical repository decision key
                may be assigned externally at landing. Such filing
                metadata does not modify this ISSUED TEXT.
    SCOPE       R-1 of the resolution path recorded by
                P2-XI-QM3-DEP-01: which decoupling the assembled chain
                of the xi ledger comprises.
    LAYERING    Lines marked RULING are the decision. Lines marked
                RATIONALE are rendering, recorded for context, and are
                not to be cited as the ruling.

---

## RULING 1 — The decoupling of the assembled chain

RULING      The scope of the 2026-08-09 ruling "Mean-field channel for
            P2-PHASE-01: the scalar channel with a real auxiliary
            field" is extended from P2-PHASE-01 mean-field work to the
            assembled chain of the xi ledger. The assembled chain's
            decoupling is the scalar channel with a real auxiliary
            field, on the same terms the 2026-08-09 ruling states.

RULING      This is a choice of route for the chain, not a judgement
            about other channels. It carries forward, unchanged, the
            2026-08-09 ruling's own limits:
              - It does not close OPEN-AC-1. The Fierz ambiguity —
                that channels equivalent as operators are inequivalent
                after truncation — is unaffected by which channel is
                used, and the P/V/A/T mean-field construction remains
                open.
              - It is not a finding that the V and A representations
                are wrong. They remain deferred, not excluded, per
                DEFERRED-01.
              - Specifying the decoupling used is not a claim that
                decouplings are equivalent after truncation. The
                family-wide question remains the open item registered
                on 2026-08-24, whose escalation condition is unchanged
                by this ruling.

## RULING 2 — What this ruling does not supply

RULING      This ruling names the channel and the auxiliary field. It
            does not fix the exponent convention, the g-to-c mapping,
            the constraints or contour, the functional-measure
            treatment, or the mathematical definition of the
            normalization object the landed criterion names. Those are
            the decoupling prescription. Until such a prescription is
            landed, the decoupling of the assembled chain is named but
            not fully specified, and P2-XI-QM3-DEP-01's determination
            stands.

## RULING 3 — Authorization of the prescription task

RULING      A specification is authorized to land the decoupling
            prescription for the assembled chain in the sense
            P2-FIERZSUM-01.md:218-220 states — auxiliary variables,
            constraints, Jacobian, and an explicit statement of what
            is generated dynamically rather than introduced as an
            independent field. That task defines; it does not
            evaluate. It must not compute the curvature dependence of
            the normalization object, which remains the question
            P2-XI-QM3-DEP-01 was scoped to and which a re-run of that
            check, under a separate specification, is to answer. It
            must not resolve DET-01 or choose the functional measure.

RATIONALE   P2-XI-QM3-DEP-01 found two elements not fixed by landed
            text: which channel or set of channels the assembled
            chain's decoupling comprises, and the decoupling
            prescription — auxiliary variables, constraints,
            Jacobian. This ruling fixes the first. The second is a
            prescription question and is not fixed by naming a
            channel. The exponent mapping is NOT among the unfixed
            elements: that same artifact records it as fixed by
            landed text at g = +2c, DECISION_LOG.md:1258-1262. On the
            Researcher's reading, recorded in that artifact's own
            symmetry statement, R-1 and R-2 together would return
            UNIQUELY IDENTIFIED and R-1 alone does not.

## ROUTING

RULING      As established by P2-XI-RULINGS-01: review of this ruling
            document is mandatory as a document-quality and
            consistency review, non-gating as to the PI's substantive
            authority. The specification this ruling authorizes
            remains subject to the repository's normal pre-execution
            review gate. Model-level assumptions arising in that task
            are routed to the PI.

END OF ISSUED TEXT
```

Its authorization of this task is `RULING 3` at `:70-80`; its statement of
what it does not supply is `RULING 2` at `:58-66`.

### 2.2 The 2026-08-09 ruling it extends, in full

`DECISION_LOG.md:1749-1781`:

```text
## 2026-08-09 — Mean-field channel for `P2-PHASE-01`: the scalar channel with a real auxiliary field

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: selects a route for mean-field work; defers an alternative

### Decision

The PI ruling of 2026-08-09, reproduced verbatim:

> **PI ruling, 2026-08-09 — mean-field channel for `P2-PHASE-01`.**
>
> Mean-field work proceeds in the **scalar channel with a real auxiliary
> field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`
> and admits the standard real linear Hubbard–Stratonovich
> representation; the induced V and A singlets have `g < 0` and do not.
>
> **This is a choice of direct route, not a judgement that the V/A
> representation is wrong.** The programme's existing machinery — the
> gap equation, `I_0`, the stationary-branch study — is built on a real
> auxiliary field. **The V/A channel does not admit the standard real
> linear HS contour that machinery uses, and would require a non-real
> contour or an otherwise reformulated bosonisation apparatus.**
>
> **No evidence indicates the V/A representation is unphysical, and the
> PI's position is that it may contain physically relevant information
> and must be returned to. It is deferred, not excluded** — see
> `DEFERRED-01`.
>
> **This does not close `OPEN-AC-1`.** It selects the channel for
> mean-field work; the Fierz ambiguity — that channels equivalent as
> operators are inequivalent after truncation — is unaffected by which
> one is used.
```

Its three limits, as `R-1` carries them forward at
`decisions/P2-XI-RULINGS-03.issued.md:42-54`, are in the quoted bytes above:
the V/A representation is deferred and not excluded (`:1773-1776`);
`OPEN-AC-1` is not closed (`:1778-1781`); and the ruling is a choice of route
and not a judgement (`:1766-1767`).

### 2.3 `P2-FIERZSUM-01.md:218-220` — the four-element prescription requirement

```text
4. **The decoupling prescription**: auxiliary variables, constraints,
   Jacobian, and an explicit statement of what is generated
   dynamically rather than introduced as an independent field.
```

### 2.4 `P2-XI-QM3-DEP-01`'s determination table, in full, both lists

`derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md:302-335`:

```text
### 2d. The determination

**`M0b` returns `NOT UNIQUELY IDENTIFIED`. | COND-R, COND-M**

Fixed by landed text, and recorded so:

    the exponent mapping     g = +2c, DECISION_LOG.md:1258-1262

Not fixed by landed text, each with its carrier quoted above:

    which channel or set of channels the assembled chain's decoupling
      comprises
        the landed selection is scoped to P2-PHASE-01 mean-field work
          (DECISION_LOG.md:1761-1766, :1778-1781;
           P2-PHASE-01_input_admissibility_contract.md:122-127;
           P2-PHASE-01_microscopic_parameter_domain.md:347-350)
        the landed freeze keeps every non-redundant HS field in the
          candidate set (P2-CHANNEL-FREEZE-01_phaseA_freeze.md:109)
        the decomposition the ledger is read by is landed open
          (P2-XI-B0a_induced-xi-scope-assessment.md:634-636)
        the manuscript under verification writes the linearization
          channel by channel (paper:281-292)

    the decoupling prescription — auxiliary variables, constraints,
      Jacobian
        landed as a deliverable the gate must freeze, in a note landed
          not registered (P2-FIERZSUM-01.md:218-220; GATES.md:1374-1376)
        the one landed line naming the HS normalization gives it no
          value (P2-CHANNEL-FREEZE-01_phaseA_freeze.md:71-79)

**No channel is selected here, no exponent mapping is fixed here, and no
preference among candidates is expressed here.** The exponent mapping is
reported as already fixed by a landed PI ruling; nothing in this artifact fixes
it. **`M1`, `M2`, `M3` and `M5` did not run, and no `N_α[g]` was constructed.**
```

**The table at the Base reads as the specification records it.** The exponent
mapping stands in the "Fixed by landed text" list at `:308`; the two entries
of the "Not fixed by landed text" list are the channel (`:312-313`) and the
decoupling prescription (`:325-326`). `A1` is not met on this node.

### 2.5 The landed `g = +2c` authority

`DECISION_LOG.md:1244-1281`, the exponent-mapping ruling reproduced verbatim
in the log, of which `:1258-1262` is the mapping itself:

```text
The PI ruling of 2026-08-08, reproduced verbatim:

> **PI ruling, 2026-08-08 — Euclidean exponent mapping.**
>
> The canonical interaction expression
>
>     X = (G/(2N)) * Sum( bilinear(lam(A), Id4)**2
>                       + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )
>
> is written **as it appears in the Boltzmann exponent**. Equivalently,
> it enters the Euclidean action with a minus sign:
>
>     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
>
> Consequently, for a channel whose coefficient in `X` is written
> `c * J**2`, the Hubbard–Stratonovich coefficient is
>
>     g = +2c
>
> **Basis, stated exactly.** This is **NOT derived from the frozen
> material.** The frozen material contains no Euclidean action, no free
> or kinetic part, and no exponent mapping; the derivation that raised
> this question searched for one and found none. The ruling is
> **constrained by executed usage**: `P2-GAP-01` is a PASSed gate whose
> mean-field treatment introduces a **real** scalar auxiliary field `Σ`,
> which is admissible only when the scalar channel has `g > 0`. Under
> the opposite mapping the scalar channel would give `g < 0` and that
> gate's method would not be available.
>
> **This supplies a definition the frozen material never carried. It is
> not a recovery of an original intent.**
>
> **Scope.** This ruling resolves the exponent mapping and nothing else.
> It selects no Hubbard–Stratonovich channel — that remains `OPEN-AC-1`
> and is the PI's. It freezes none of the three diquark-definition gaps
> (`η`, particle–particle Grassmann ordering, diquark normalisation). It
> reaches no conclusion about a composite vector. It does not by itself
> re-run any withheld verdict.
```

### 2.6 The no-channel-selected statement

`derivations/P2-PHASE-01_channel_character.md:7-10`:

```text
**This is a computation, not a ruling.** It registers no gate, changes
no status, and reaches no admissibility verdict. `P2-PHASE-01` remains
`PROPOSED`. **It does not select a Hubbard–Stratonovich channel** —
`OPEN-AC-1` is the PI's.
```

and `:371-377`:

```text
## 3. What this note does not do

It registers no gate and changes no status. It selects no
Hubbard–Stratonovich channel: it reports which channels admit a real
linear auxiliary field **under each of the two possible exponent
mappings**, and reports that the mapping itself is not frozen.
`OPEN-AC-1` is untouched. `P2-PHASE-01` remains `PROPOSED`.
```

### 2.7 The landed assembled chain

`derivations/P2-NORM-01_normalization_chain.md:23-28`:

```text
## The one normalization chain

```
Z(m²)  ──►  β_s (coeff of m²ln m² in Z)  ──►  4 G_c β_F  ──►  ξ_ind = 4Gβ_F(3−L)
```

```

The chain's `G_c` node, `derivations/P2-NORM-01_normalization_chain.md:50-52`:

```text
3. **Gap-equation coupling `G_c`.** `G_c = 8π²/Λ²` from `1 = 2G_c I_0`
   (P2-GAP-01). This is a property of the four-fermion bubble `I_0` and is
   **`Z`-independent** — it does *not* carry `R_Z`.
```

and the landed derivation that node cites,
`derivations/P2-GAP-01_gap_criticality.md:30-54`:

```text
## Derivation of `G_c = 1/(2 I_0)`

Mean-field (Hubbard–Stratonovich) treatment of the attractive scalar-channel
four-fermion interaction. Introducing the scalar auxiliary `Σ` (the dynamical
self-energy), the gap equation is the tadpole self-consistency

```
Σ = 2 G · Σ · B(Σ),      B(Σ) = (untraced scalar bubble) = ∫ d⁴p/(2π)⁴ 1/D(p;Σ),
```

where `D` is the propagator denominator and `G` is the **channel coupling**:
we absorb the Dirac trace (`tr 𝟙₄ = 4`) into the definition of `G`, so that the
combinatorial prefactor of the gap equation is exactly `2`. (In the alternative
"NJL" normalization `L_int = G_N(ψ̄ψ)²`, one has `G = 4 G_N` and the gap
equation reads `1 = 8 G_N B`; the physics — the value of `I_0` and the ratio of
continuum to lattice `G_c` — is normalization-independent.)

A nontrivial solution `Σ ≠ 0` bifurcates from `Σ = 0` when

```
1 = 2 G_c B(0)  ≡  2 G_c I_0,     I_0 ≡ B(0).      (★)
```

Hence **`G_c = 1/(2 I_0)`**, with `I_0` the untraced scalar bubble evaluated at
the chiral point.
```

The ledger's own statement of what the assembled chain is,
`derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md:26-32`:

```text
    COND-1  MEMBERSHIP = LANDED MEMBERSHIP ONLY. The assembled chain is the
            landed chain of P2-NORM-01 (:26):
                Z(m²) → β_s → 4G_c β_F → ξ_ind = 4Gβ_F(3−L).
            **The condensate scalar's own fluctuation loop is NOT included
            and NOT excluded on physical grounds** — it is an OPEN ledger row
            pending the PI's Q-M2 ruling
            (derivations/P2-XI-B0a_induced-xi-scope-assessment.md:615-618).
```

### 2.8 `DET-01`'s status statement — `COND-M`'s citation

`derivations/P2-SRC-B0_source-side-scope.md:186-188`:

```text
**`T_μν = (2/√g) δΓ/δg^{μν}` requires `Γ`.** `DET-01` established, and the
landed artifact records, that the functional measure is `NOT DETERMINABLE` from
the frozen conventions: `Γ = ½ log det K − ½ log det 𝔊` with `𝔊` unspecified.
```

and the adjudication it records, `derivations/P2-BETAV-DET-01_measure-adjudication.md:226-245`:

```text
## 6. The verdict, and the missing convention named precisely

> **`NOT DETERMINABLE`**

**By `§4`, the verdict is entirely determined by `𝔊`. By `§5.1`, the repository
fixes no property of `𝔊` whatsoever.** Not its existence, not its form, not
whether it is ultralocal, not its power of `√g`.

### 6.1 The missing convention, stated exactly

**What is missing is one line of `CONVENTIONS.md` of this form:**

> *The functional integration measure for a 1-form field `A_μ` is defined by the
> field-space metric `‖δA‖² = ∫d⁴x √g g^{μν} δA_μ δA_ν`, with
> `DA = (det 𝔊)^{1/2} ∏ dA_μ(x)`; equivalently the lattice measure is
> `∏_x (det g(x))^{1/2} ∏_{x,μ} dA_μ(x)`.*

**— or an explicit statement of a different `𝔊`, or an explicit statement that
the measure is Cartesian in the components `A_μ(x)`.** **Any one of the three
would settle it. The repository contains none of the three.**
```

with the null result that verdict rests on, `:167-169`:

```text
**MEASURED: NO LINE OF `CONVENTIONS.md` ADDRESSES THE PATH-INTEGRAL MEASURE, THE
FIELD-SPACE METRIC, OR A CHANGE-OF-VARIABLES JACOBIAN.** The null result is the
finding.
```

### 2.9 Supporting landed lines the elements of §3 rest on

These are not `M1` nodes. They are quoted here so that every basis cited in
§3 is present in this artifact as measured bytes.

(a) The landed Hubbard–Stratonovich identity and its convergence condition,
`derivations/P2-PHASE-01_channel_character.md:142-150`:

```text
The Hubbard–Stratonovich identity

    exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J]

converges only for `g > 0`. **`g` is an exponent-level quantity and is
not `2c`.** If the frozen expression is a term of `S_E`, the Boltzmann
weight carries `exp[-S_E] ⊃ exp[-c J^2]` and `g = -2c`; if the
expression already sits in the exponent, `g = +2c`. The two differ by a
sign.
```

(b) The two landed normalisations of the coefficient, and the landed
coefficient table, `derivations/P2-PHASE-01_channel_character.md:52-73`:

```text
**Normalisation is the whole difficulty here**, so it is stated before
any number. A coefficient is meaningless without the operator it
multiplies, and this note uses **two explicit normalisations
throughout**, never mixing them:

    normalisation L :  coefficient of  (psibar lam(0) Gamma psi)^2
    normalisation P :  coefficient of  (psibar Gamma psi)^2

They are related by the frozen singlet definition alone:

    (psibar lam(0) Gamma psi)^2 = (2/N) (psibar Gamma psi)^2
    so   c_P = (2/N) * c_L

**The scalar coefficient is read from the frozen material**, not
assumed. The freeze's `interaction_decomposition` (line 116 of the
Phase-A freeze) carries, for both supported families,

    family S: coefficient "G/(2*N)", operator Sum(bilinear(lam(A),Id4)**2, (A,0,N**2-1))
    family P: coefficient "G/(2*N)", operator Sum(bilinear(lam(A),I*gamma5)**2, (A,0,N**2-1))

so `c_can = G/(2N)` in normalisation L, with `G > 0` frozen by
`CANONICAL_INTERACTION.md` §2 and §3.
```

and `:92-103`:

```text
The resulting Layer-1a table, with `G > 0` and `N > 0`:

    channel                         normalisation L      normalisation P
    scalar singlet (direct)            +G/(2N)              +G/N^2
    induced V singlet (operator)       -G/4                 -G/(2N)
    induced A singlet (operator)       -G/4                 -G/(2N)
    induced S, P, T                     0                     0

**Signs: the scalar coefficient is positive; the induced V and A
coefficients are negative. This is unconditional** — it needs no
knowledge of how the expression enters the Euclidean exponent, and it is
the deliverable that stands whatever the later layers do.
```

(c) The two exponent branches as landed text reports them,
`derivations/P2-PHASE-01_channel_character.md:175-196`:

```text
**Both branches are nonetheless reported, because one of them is
inconsistent with what the repository has already executed.** Writing
`c J^2 = (g/2) J^2` at exponent level:

    branch (i)   the expression enters the exponent with a + sign, g = +2c
                 scalar   g = +2G/N^2  > 0   real HS field admissible
                 V and A  g = -G/N     < 0   no real linear HS field
    branch (ii)  the expression is a term of S_E,      g = -2c
                 scalar   g = -2G/N^2  < 0   no real linear HS field
                 V and A  g = +G/N     > 0   real HS field admissible

**Branch (ii) contradicts `P2-GAP-01`'s executed calculation**, which
introduces a **real** scalar auxiliary `Sigma` for the attractive scalar
channel and obtains a physical critical coupling `G_c = 1/(2 I_0)`. A
scalar channel with `g < 0` admits no real linear HS field, so branch
(ii) cannot be the convention `P2-GAP-01` operated under.

**This is an inference from usage, not a frozen definition, and it is
labelled as such.** It is reported as evidence bearing on which mapping
the programme is in fact using; it does not turn Layer 1b into a
resolved layer, and the verdict above stands. **Fixing the mapping is a
PI decision this note informs and does not take.**
```

(d) The landed curved-background fermionic path integral and the status of
auxiliary-field representations, `derivations/P2-FIERZSUM-01.md:106-118`:

```text
The unambiguous starting point is the curved-background fermionic path
integral

    Z[g] = ∫ Dψ̄ Dψ  exp( − S_free[ψ̄,ψ;g] − S_int[ψ̄,ψ] )

with `S_int` the frozen generator-sum interaction. `ξ_ind` is defined
from the `R`-linear part of `−log Z[g]`. **The prescription required to define
and eventually match that coefficient as a unique physical number is
frozen as a deliverable of this gate (§4.2). Until the microscopic
matching dependencies are discharged, only the continuum-side
renormalized coefficient and its transformation law are available.** Auxiliary fields, channels,
composite propagators, and channel determinants are *representations*,
and each must be shown to approximate this object.
```

(e) The landed criterion that names `N_α[g]`,
`derivations/P2-FIERZSUM-01.md:451-460`:

```text
- **HS-normalization / Jacobian curvature test.** For every admissible
  decoupling `α`, verify not only recovery of the frozen quartic
  interaction but the full identity
  `Z_HS^(α)[g] = N_α[g] · Z_fermionic[g]`, and determine whether
  `δ log N_α[g] / δR` vanishes. A field-independent normalization is
  harmless in flat-space scattering, but here the observable IS
  `−log Z[g]`: any metric-, regulator- or curvature-dependent
  normalization, contour phase, or Jacobian contributes to the
  cosmological and `R` terms and **must be included in `ξ_ind`, not
  discarded as an irrelevant constant**.
```

(f) The one landed line naming the HS normalization,
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:69-79`:

```text
> A parameter counts as a genuinely free microscopic coordinate only if varying it changes the canonical action itself. Changing HS normalization, field rescaling, basis choice, Fierz representation, or a redundant parametrization does not create a new scan coordinate.

| genuine microscopic coordinate | exact expression | scan eligible |
| --- | --- | --- |
| `G` | `G` | yes |

| auxiliary representation parameter | reason | scan eligible |
| --- | --- | --- |
| `HS_scale` | HS normalization / field rescaling | no |
| `Fierz_basis` | basis choice / crossing representation | no |
| `g_c` per channel | rejected T1 multi-coupling extension | no |
```

(g) `Q-M3` as the ledger carries it,
`derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md:327-335`:

```text
`derivations/P2-XI-B0a_induced-xi-scope-assessment.md:620-624` — `Q-M3`:

```text
    Q-M3  Does the Hubbard–Stratonovich decoupling's Jacobian or
          normalization contribute? derivations/P2-FIERZSUM-01.md:451-460
          states that any metric-, regulator- or curvature-dependent
          normalization "must be included in `ξ_ind`, not discarded as an
          irrelevant constant", and records the check as undone.
```
```

**Every node named in `M1` is above, as a verbatim quotation with a
`path:line` resolving at the Base. `C1` is satisfied. No node was missing and
no `A1` condition is met.**

---

## 3. `M2` — the prescription, element by element

Each element below is either FIXED, with the landed material it rests on
quoted in §2 and cited here and with the mark `LANDED-DERIVED` or
`PRESCRIBED-HERE`, or ROUTED under `A3` with the choice stated. **No element
is fixed by default, by elimination, or by a judgement of what is likely.**

### `E1` — the HS channel and the auxiliary-field content

**Fixed: the scalar channel, decoupled by one real auxiliary field. LANDED-DERIVED. | COND-R, COND-M**

Basis. `R-1`, `RULING 1`, `decisions/P2-XI-RULINGS-03.issued.md:35-37`:
“The assembled chain's decoupling is the scalar channel with a real auxiliary field, on the same terms the 2026-08-09 ruling states.” `R-1`, `RULING 2`,
`:58-59`, states of itself: “This ruling names the channel and the auxiliary field.” The
2026-08-09 ruling it extends, `DECISION_LOG.md:1761-1762`:
“Mean-field work proceeds in the **scalar channel with a real auxiliary > field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`” The landed
execution that introduces it, `derivations/P2-GAP-01_gap_criticality.md:33-34`:
“Introducing the scalar auxiliary `Σ` (the dynamical self-energy)” The auxiliary field is one
real scalar, singular in every one of those carriers.

Scope of the element, recorded so that §4's comparison can be read. The
frozen quartic carries an `S` family and a `P` family, each summed over
`A = 0..N**2-1` (`DECISION_LOG.md:1250-1251`). The landed treatment this
element fixes is of “the attractive scalar-channel four-fermion interaction”
(`derivations/P2-GAP-01_gap_criticality.md:32-33`), the channel `R-1` names.
This element decouples that channel and no other. Nothing here asserts that
the remaining families need no decoupling, and nothing here decouples them.

### `E2` — the exact exponent convention

**Fixed: the canonical interaction is written as it appears in the Boltzmann exponent. LANDED-DERIVED. | COND-R, COND-M**

Basis. `DECISION_LOG.md:1248-1256`, within the PI ruling of 2026-08-08
reproduced verbatim in the log:

```text
> The canonical interaction expression
>
>     X = (G/(2N)) * Sum( bilinear(lam(A), Id4)**2
>                       + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )
>
> is written **as it appears in the Boltzmann exponent**. Equivalently,
> it enters the Euclidean action with a minus sign:
>
>     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
```

The convention is therefore: the canonical interaction expression `X` sits in
the exponent with a `+` sign, equivalently `S_E = S_E,0 - X`. This is a
landed convention, not one chosen here.

### `E3` — the `g`↔`c` mapping

**Fixed: `g = +2c`. LANDED-DERIVED, and not this task's to choose. | COND-R, COND-M**

Basis, `DECISION_LOG.md:1258-1262`:

```text
> Consequently, for a channel whose coefficient in `X` is written
> `c * J**2`, the Hubbard–Stratonovich coefficient is
>
>     g = +2c
>
```

The specification records this element as landed at this Base and excludes it
from routing. **This artifact does not re-adjudicate it**, and no sign choice
is made here. The landed value for the channel `E1` fixes, in the
normalisation the landed branch table uses, is
`derivations/P2-PHASE-01_channel_character.md:179-180`:

```text
    branch (i)   the expression enters the exponent with a + sign, g = +2c
                 scalar   g = +2G/N^2  > 0   real HS field admissible
```

`g` there is the Hubbard–Stratonovich coefficient of the channel. It is not
`N_α[g]`, and nothing in this element states a sign, magnitude, bound or
scaling for `N_α[g]` or for any Jacobian or normalization contributing to it.

### `E4` — the constraints and the integration contour

**Fixed: no constraint is imposed, and the contour is the standard real linear one. LANDED-DERIVED. | COND-R, COND-M**

Basis. The landed identity, `derivations/P2-PHASE-01_channel_character.md:142-146`:

```text
The Hubbard–Stratonovich identity

    exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J]

converges only for `g > 0`. **`g` is an exponent-level quantity and is
```

Two things are read from those bytes and nothing else is. First, the identity
as landed carries **no constraint**: no delta function, no Lagrange
multiplier and no auxiliary condition relating `Phi` to `J` appears in it; the
auxiliary variable is integrated freely. Second, its stated convergence
condition is `g > 0`, which is a condition on a **real** integration
variable — a contour condition, and the one the landed rulings speak in.
`DECISION_LOG.md:1769-1771` names it for the channels that lack it:
“**The V/A channel does not admit the standard real > linear HS contour that machinery uses, and would require a non-real > contour or an otherwise reformulated bosonisation apparatus.**” With `E3` landed and
the channel of `E1`, the landed branch table records this channel on the
admitting side (`derivations/P2-PHASE-01_channel_character.md:180`). The
contour this prescription fixes is therefore the standard real linear one
that landed text names, and no other.

### `E5` — the functional-measure treatment

**Fixed, to the extent landed authority determines it: the landed construction adjoins an auxiliary integration to a fermionic integration it does not remove. LANDED-DERIVED. | COND-R, COND-M**

**Routed under `A3`: the normalization of the auxiliary functional measure. | COND-R, COND-M**

The fixed part, and the landed text it is read from. In the landed identity
`derivations/P2-PHASE-01_channel_character.md:144`, the right-hand side still
carries `J` — the fermion bilinear — under the auxiliary integration. The
fermionic object itself is landed at `derivations/P2-FIERZSUM-01.md:109`:

```text
    Z[g] = ∫ Dψ̄ Dψ  exp( − S_free[ψ̄,ψ;g] − S_int[ψ̄,ψ] )
```

Putting only those two landed statements together: the auxiliary integration
is **adjoined** to the fermionic one. The fermionic integration variables are
not removed, not traded, and not re-expressed.

**Accordingly this artifact assumes no change of variables between the
fermionic and auxiliary-field measures, invertible or otherwise, and asserts
none.** `derivations/P2-BETAV-DET-01_measure-adjudication.md:167-168` records
the measured null result that bears directly on this:
“**MEASURED: NO LINE OF `CONVENTIONS.md` ADDRESSES THE PATH-INTEGRAL MEASURE, THE FIELD-SPACE METRIC, OR A CHANGE-OF-VARIABLES JACOBIAN.**”

The routed part, and why it is routed. What landed authority does **not**
determine is the normalization of the auxiliary functional measure — what
`Dσ` is, as against the single-variable `dPhi` the landed identity writes.
Three landed carriers bear on it and none supplies a value:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:77
        names `HS_scale` as “HS normalization / field rescaling”, scan
        eligible “no” — the one landed line naming the object, and it gives
        the object no value

    derivations/P2-BETAV-DET-01_measure-adjudication.md:167-169
        the measured null result quoted above

    derivations/P2-SRC-B0_source-side-scope.md:186-188
        `DET-01` landed NOT DETERMINABLE, `Γ = ½ log det K − ½ log det 𝔊`
        with `𝔊` unspecified

Fixing this remainder would require choosing `𝔊`. That is `A3`, and `A3` alone:
it is recorded, routed to the PI, and the measurement continues. It is
**explicitly measure-inherited** in the sense `COND-M` requires, and it is not
resolved here.

### `E6` — which fields are independent and which are generated dynamically

**Fixed: the fermion fields remain independent integration variables; the auxiliary field is introduced as an integration variable and its dynamics is generated, not posited. LANDED-DERIVED. | COND-R, COND-M**

Basis. That the fermion fields remain independent is the same reading of
`derivations/P2-PHASE-01_channel_character.md:144` and
`derivations/P2-FIERZSUM-01.md:109` recorded at `E5`. That the auxiliary field
is introduced rather than posited as an independent field is
`derivations/P2-GAP-01_gap_criticality.md:33-34`, quoted at `E1`: it is
introduced in the course of the treatment, and it is identified there as
“(the dynamical self-energy)” — a generated object, not an
input. That its dynamics is generated is
`derivations/P2-GAP-01_gap_criticality.md:15-16`:

```text
the point at which the mean-field effective potential `V(Σ)` for the scalar
self-energy `Σ` first develops a nontrivial stationary point, equivalently
```

— the potential `V(Σ)` is a **mean-field effective** potential, produced by
the treatment; no landed line gives the auxiliary field a kinetic term or an
independent action of its own. The programme's own classification of such
objects is landed at `derivations/P2-FIERZSUM-01.md:116-118`:
“Auxiliary fields, channels, composite propagators, and channel determinants are *representations*, and each must be shown to approximate this object.”

This is the explicit statement `derivations/P2-FIERZSUM-01.md:218-220`
requires of a decoupling prescription.

### `E7` — the mathematical definition of `N_α[g]`

**Routed under `A3`: the landed construction does not determine the object's form far enough for a defining expression to be written. | COND-R, COND-M, COND-J**

**The identification comes first, and is recorded whether or not the element
is routed.**

What the landed construction produces, read from the landed text of `E5`: an
auxiliary Gaussian integration **adjoined** to an unchanged fermionic
integration. The object relating `Z_HS^(α)[g]` to `Z_fermionic[g]` in the
landed criterion's identity is therefore whatever normalization that adjoined
integration carries, together with whatever the promotion of the identity
from a single variable to a field carries. **It is not the Jacobian of an
invertible change of variables**, because the landed construction establishes
no such change of variables — the fermionic measure is untouched. The landed
criterion's own wording is consistent with that identification and with no
narrower one: `derivations/P2-FIERZSUM-01.md:457-459` speaks of
“any metric-, regulator- or curvature-dependent normalization, contour phase, or Jacobian” — three contributors in
the alternative, not one object named in advance.

Why the element is nevertheless routed. Writing a **defining** expression for
`N_α[g]` requires two things that landed text does not supply:

    (i)   the auxiliary functional measure, with its normalization — the
          remainder E5 routes. Landed authority fixes no property of the
          functional measure (P2-BETAV-DET-01_measure-adjudication.md:230-232)
          and CONVENTIONS.md carries no functional measure at all (:167-169).

    (ii)  the promotion of the landed identity at
          P2-PHASE-01_channel_character.md:144 from a single-variable
          algebraic identity to a functional integral over the field in a
          curved background — the mode decomposition, and the definition by
          which the product of the per-mode identities is taken. No landed
          line states it. The landed criterion is written for `Z_HS^(α)[g]`
          and `Z_fermionic[g]`, functionals of the background; the landed
          identity available to build them from is written for one variable.

Either would be a choice the landed text does not fix and the `R-1` ruling
does not authorize, and (i) would additionally require choosing `𝔊`. Both are
`A3`. The choice is recorded, routed to the PI, and not taken here.

**One reading is available and is refused, and the refusal is recorded.** The
landed identity at `:144` is written with no normalization prefactor. Read
literally as a functional statement it would make `N_α[g]` the identity, which
would settle the question `Q-M3` puts. That reading is not taken: the absence
of a prefactor in a single-variable identity is a **statement about the
normalization convention chosen for `dPhi`**, and adopting it as the
functional measure's normalization would be choosing `𝔊` — `A3`, and outside
this task — while stating its consequence for the curvature question would be
a `Q-M3` verdict, which is `A2`. Neither is done here.

---

## 4. `M3` — consistency with the landed chain, conditional on what `M2` fixed

**This is a consistency check on definitions.** No chain node is re-derived
and no coefficient is computed. Both sides are shown. The two sides are
summarized below; each summary's verbatim carrier is quoted in §2 at the
`path:line` given.

### 4.1 The comparison

    SIDE A — the landed chain
      the chain              P2-NORM-01_normalization_chain.md:26, quoted §2.7
      the node at which the
        decoupling enters    P2-NORM-01_normalization_chain.md:50-52, quoted §2.7
      the landed derivation
        of that node         P2-GAP-01_gap_criticality.md:30-54, quoted §2.7

    SIDE B — what M2 fixed
      E1  the scalar channel, one real auxiliary field
      E4  no constraint; the standard real linear contour
      E6  fermion fields independent; the auxiliary field's dynamics generated
      E2  the interaction sits in the Boltzmann exponent
      E3  g = +2c

Side A's derivation, in its own bytes, is
`derivations/P2-GAP-01_gap_criticality.md:32-34`:
“Mean-field (Hubbard–Stratonovich) treatment of the attractive scalar-channel four-fermion interaction. Introducing the scalar auxiliary `Σ` (the dynamical self-energy)”

**The construction M2 fixes and the construction the chain's `G_c` node was derived by are the same construction. | COND-R, COND-M**

The channel the chain's `G_c` node was derived in and the channel `E1` fixes are the same
channel. The auxiliary-field character in that derivation — one real scalar,
introduced, identified as the self-energy — and the character `E1` and `E6`
fix are the same. The admissibility condition the landed identity states,
`g > 0` at `derivations/P2-PHASE-01_channel_character.md:146`, is met under
`E2` and `E3` for this channel by the landed branch table at `:180`, which is
the condition the 2026-08-09 ruling's own reasoning turns on at
`DECISION_LOG.md:1785-1791`. The construction `M2` fixes is the construction
the chain's `G_c` node was produced by. **They agree, and no adjustment to
either side was made.**

### 4.2 The exponent convention

`E3` arrives `LANDED-DERIVED` at this Base and is not routable. `E2` is fixed.

**`E2` together with the landed `E3` determines one exponent convention and leaves no `±` open. | COND-R, COND-M**

The interaction sits in the exponent (`E2`), so `g = +2c` (`E3`) and not
`g = -2c`. The landed branch table names those as the only two
(`derivations/P2-PHASE-01_channel_character.md:179-184`), and one of them is
landed. No unresolved sign remains.

`E3` is not routed and is not recorded as unfixed anywhere in this artifact.

### 4.3 What the comparison does not cover, recorded rather than passed over

The frozen quartic `X` carries an `S` family and a `P` family, each summed
over `A = 0..N**2-1` (`DECISION_LOG.md:1250-1251`). The chain reaches that
quartic only through `G_c`, and landed text derives `G_c` from the
scalar-channel treatment alone
(`derivations/P2-GAP-01_gap_criticality.md:32-33`). The prescription
decouples that channel. **The comparison is therefore between the
prescription and the chain node as landed text actually constructs it, and it
is not a statement that this construction decouples the whole of `X`.** No
landed line requires that it does, and none is contradicted by observing that
it does not.

**No inconsistency between a fixed definition and landed text was found. `A5`
is not met.** `E5`'s remainder and `E7` are elements unresolved for want of
authority. They are recorded as routed at §3 and carried to §5, and this
section does not report either as a contradiction.

---

## 5. `M4` — the binary determination

**Result: `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`. | COND-R, COND-M**

The determination is binary because the gate it feeds is binary. A
`uniquely defined to the extent reached` return is not available under this
task's specification and is not used anywhere in this artifact.

### 5.1 The blocking routed elements, each with what its routing blocks

    E7   the mathematical definition of `N_α[g]`
         BLOCKS  the uniqueness of the normalization object itself. Without
                 a defining expression there is no unique `N_α[g]`, and the
                 subject the later Q-M3 question would be put to does not
                 exist.

    E5   the normalization of the auxiliary functional measure
         BLOCKS  E7. The object E7 must define is a normalization, and the
                 measure whose normalization is unfixed is the measure that
                 carries it. E5's routed remainder is not separable from
                 E7's: it is the first of E7's two named requirements.

Both bear on the uniqueness of `N_α[g]`. Under `A3` that forces this return,
however many elements were fixed.

### 5.2 The elements that WERE fixed, recorded as gap characterization

    E1  the scalar channel, decoupled by one real auxiliary field   LANDED-DERIVED
    E2  the interaction is written in the Boltzmann exponent        LANDED-DERIVED
    E3  g = +2c                                                     LANDED-DERIVED
    E4  no constraint; the standard real linear contour             LANDED-DERIVED
    E5  the auxiliary integration is adjoined to a fermionic
          integration the construction does not remove              LANDED-DERIVED
          (the measure's normalization is the routed remainder)
    E6  fermion fields independent; the auxiliary field introduced
          as an integration variable, its dynamics generated        LANDED-DERIVED

Five elements and part of a sixth are fixed, every one of them
`LANDED-DERIVED`. **No element of this prescription is `PRESCRIBED-HERE`.**
That is itself the shape of the gap: what landed text determines, it
determines completely; where it stops, it stops at the measure and at the
promotion of an algebraic identity to a functional one, and this task is not
authorized to carry either further.

The identification recorded at `E7` — that the object is the normalization
carried by an adjoined auxiliary integration, and **not** the Jacobian of an
invertible change of variables — is part of this characterization. It narrows
what a later prescription must define without defining it.

### 5.3 What this return does and does not license

**This artifact does not supply `Q-M3`'s subject. | COND-R, COND-M**

`Q-M3` asks whether the Hubbard–Stratonovich decoupling's Jacobian or
normalization contributes
(`derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md:330-334`, quoted
at §2.9(g)). A question about `N_α[g]` presupposes a unique `N_α[g]`. This
task was to define that object and returns without having defined it.
`Q-M3` therefore remains exactly as it stood: an OPEN ledger row, valueless,
its subject not yet constructed.

No prescription is claimed complete. No curvature dependence is evaluated,
in whole or in part. No sign, magnitude, bound or `L`-scaling is stated for
`N_α[g]`, for any Jacobian, or for any normalization contributing to either.
No membership implication is carried for `Q-M2` or `Q-M3`.

---

## 6. Rule 22 — the classification and its resolution path

    Classification    INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
    Subclass          CONSTRUCTIVE GAP: two named landed conventions are
                      absent, and each is suppliable by a bounded act of
                      authority. This is not an unbounded inquiry and not a
                      measurement this task could have taken.

### 6.1 The resolution path, defined here and NOT walked

    R-1'  A landed statement fixing the functional measure for the real
          scalar auxiliary field. P2-BETAV-DET-01_measure-adjudication.md:236-245
          states exactly what such a statement would have to be, in three
          alternatives, and records that the repository contains none of the
          three:

              **— or an explicit statement of a different `𝔊`, or an explicit statement that
              the measure is Cartesian in the components `A_μ(x)`.** **Any one of the three
              would settle it. The repository contains none of the three.**

          The path names all three and prefers none. They are different
          measures and the prescription that follows differs accordingly.
          Which one, if any, is the PI's.

    R-2'  A landed statement promoting the single-variable Hubbard–Stratonovich
          identity at P2-PHASE-01_channel_character.md:144 to a functional
          integral over the auxiliary field in a curved background — the mode
          decomposition and the definition by which the product of the
          per-mode identities is taken. The path does not say what that
          statement should be, and does not prefer a promotion that makes the
          normalization background-independent over one that does not.

### 6.2 The symmetry statement

**On the Researcher's reading**, `R-1'` and `R-2'` together would let `E7` be
written and would let a re-run of this task return `PRESCRIPTION COMPLETE`;
`R-1'` alone would not, because `E7`'s second requirement would remain, and
`R-2'` alone would not, because `E7`'s first would. The path is symmetric in
that it is stated for either outcome: nothing in `R-1'` or `R-2'` is written
so as to make one answer to the later `Q-M3` question easier to reach than
another, and this artifact takes no position on what either supplied
convention would yield.

**The path is defined here and is NOT walked.** No part of `R-1'` or `R-2'` is
supplied, proposed, or preferred by this artifact.

### 6.3 The `C3` enumeration and check

**The enumeration rule was stated at §0 before any conditioned statement was
written**: a line outside every fenced block whose bytes end with
`| COND-R, COND-M**` or `| COND-R, COND-M, COND-J**`. The rule is fence-aware
because the landed text quoted in §2 carries its own source's `COND` markers —
`derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md:304` is one,
inside the block quoted at §2.4 — and those are that artifact's statements,
not this one's. The set and count are measured over this artifact's own bytes
and recorded in the report.

The `C3` check runs over exactly that set and asks whether any of its members
evaluates `N_α[g]`, states its curvature dependence, its sign, its magnitude,
its `L`-scaling, or a `Q-M3` verdict. Occurrences of those terms elsewhere in
this artifact — in quoted landed text, in the prohibitions of §5.3 and §7, and
in statements that something was NOT done — are context, not failures, and are
recorded as such.

---

## 7. What this artifact does not establish

- It does not evaluate `N_α[g]`, any Jacobian or normalization contributing to
  it, or any coefficient.
- It does not resolve `DET-01` and does not choose the functional measure.
- It does not answer `Q-M3` and does not bear on what an answer would be.
  Both ledger rows remain OPEN and valueless.
- It does not close `OPEN-AC-1`. Naming the decoupling this chain uses is not
  a claim that decouplings are equivalent after truncation, and the
  family-wide representation-stability question is untouched.
- It does not find the V or A representations wrong. They remain deferred and
  not excluded, per `DEFERRED-01`.
- It does not extend the `R-1` ruling beyond the assembled chain.
- It does not assert an invertible change of variables between the fermionic
  and auxiliary-field measures. It records that landed text establishes none.
- It does not scope, order, or design the re-run of `P2-XI-QM3-DEP-01` that
  the `R-1` ruling's own terms reserve.
- It does not state that the decoupling it fixes decouples the whole of the
  frozen quartic `X`, and it does not state that the remaining families
  require no decoupling.

END OF ARTIFACT
