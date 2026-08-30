# `P2-XI-QM3-DEP-01` — the HS Jacobian curvature-dependence check on the landed decoupling

    KIND        MEASUREMENT. Not a gate. No gate status changes, no
                membership is ruled, P2-PHASE-01 and SI-2 are untouched.
    AUTHORITY   P2-XI-RULINGS-02, Ruling 2, scoped by
                P2-XI-RULINGS-02-CLARIFICATION-01.
    BASE        main @ 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    SPEC        specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    EXECUTION   M0 → M0b → M4 → M6. The early-return path.
                M1, M2, M3 and M5 did not run.
    RESULT      M0b returns NOT UNIQUELY IDENTIFIED.
                Rule 22: INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED.
                **No dependence evaluation was performed.**

---

## 0. The conditions this artifact carries

    COND-R  Landed decoupling only. Anything this artifact returns is
            conditional on the landed HS representation and is not a
            statement about admissible decouplings generally.
    COND-M  Functional-measure status. DET-01 is landed as NOT
            DETERMINABLE. This artifact states that status and does not
            resolve it; no part of any normalization is assigned a value.

`COND-M`'s citation, `derivations/P2-SRC-B0_source-side-scope.md:186-188`,
verbatim:

```text
**`T_μν = (2/√g) δΓ/δg^{μν}` requires `Γ`.** `DET-01` established, and the
landed artifact records, that the functional measure is `NOT DETERMINABLE` from
the frozen conventions: `Γ = ½ log det K − ½ log det 𝔊` with `𝔊` unspecified.
```

**Every verdict sentence below carries both tags.**

## 0a. The question, and what this artifact returns instead

The authorized question, from `derivations/P2-FIERZSUM-01.md:451-460`,
verbatim:

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

The scope the clarification puts on this task,
`decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md:24-30`, verbatim:

```text
CLARIFICATION   The Q-M3 check authorized by P2-XI-RULINGS-02, Ruling 2
                is scoped to the landed decoupling — the
                Hubbard–Stratonovich transformation of the assembled
                chain. The verdict it returns is conditional on that
                representation, and this conditionality is to be
                recorded in the artifact's conditions alongside its
                other stated conditions.
```

**`M0b` asked whether that object — "the landed decoupling α", the HS
transformation of the assembled chain — is uniquely identified by landed text
at the Base. It is not.** The measurement is §2; the determination is §2d.

## 1. `M0` — precondition and provenance

    origin/main                     0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    the Base this specification pins 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
                                    EQUAL, full string

    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
      measured 0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
      required 0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22

    decisions/P2-XI-RULINGS-02.issued.md
      measured ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
      required ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5

    derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
      present; sha256 aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454
      the two OPEN rows present at :305 and :307, both valueless

**`A0` did not fire.** The clarification this specification cites for its scope
is landed at its canonical path on `main` at the stated digest, so the citation
is to landed state and not asserted.

## 2. `M0b` — subject identification

**The subject is the object named "the landed decoupling α".** For it to be
uniquely identified, landed text must fix the channel and the exponent mapping
and state the decoupling as fixed. Each element is measured below from landed
text alone.

### 2a. What the assembled chain is, and what its own provenance names

`derivations/P2-NORM-01_normalization_chain.md:26`, the chain itself:

```text
Z(m²)  ──►  β_s (coeff of m²ln m² in Z)  ──►  4 G_c β_F  ──►  ξ_ind = 4Gβ_F(3−L)
```

`derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md:26-39`, which
defines the assembled chain and states the status of the term this task was
authorized to test:

```text
    COND-1  MEMBERSHIP = LANDED MEMBERSHIP ONLY. The assembled chain is the
            landed chain of P2-NORM-01 (:26):
                Z(m²) → β_s → 4G_c β_F → ξ_ind = 4Gβ_F(3−L).
            **The condensate scalar's own fluctuation loop is NOT included
            and NOT excluded on physical grounds** — it is an OPEN ledger row
            pending the PI's Q-M2 ruling
            (derivations/P2-XI-B0a_induced-xi-scope-assessment.md:615-618).

    COND-2  **The Hubbard–Stratonovich Jacobian/normalization term is NOT
            included and NOT asserted absent** — an OPEN ledger row pending
            the PI's Q-M3 disposition. The landed text requiring its
            inclusion if curvature-dependent is
            derivations/P2-FIERZSUM-01.md:451-460, via Q-M3 at
            derivations/P2-XI-B0a_induced-xi-scope-assessment.md:620-624.
```

**Neither the chain nor its landed definition names a decoupling.** The chain
is a normalization chain over heat-kernel species coefficients; no HS
transformation appears in it, and no landed line attaches one to it.

### 2b. What landed text DOES fix — the exponent mapping

**The exponent mapping is fixed by a landed PI ruling.**
`DECISION_LOG.md:1258-1262`, from the ruling reproduced verbatim in that entry:

```text
> Consequently, for a channel whose coefficient in `X` is written
> `c * J**2`, the Hubbard–Stratonovich coefficient is
>
>     g = +2c
>
```

This measurement corrects a reading the specification's §0c surfaced.
`derivations/P2-PHASE-01_channel_character.md:142-152` does say the mapping is
not fixed:

```text
The Hubbard–Stratonovich identity

    exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J]

converges only for `g > 0`. **`g` is an exponent-level quantity and is
not `2c`.** If the frozen expression is a term of `S_E`, the Boltzmann
weight carries `exp[-S_E] ⊃ exp[-c J^2]` and `g = -2c`; if the
expression already sits in the exponent, `g = +2c`. The two differ by a
sign.

**The frozen material does not fix which.** What it does contain:
```

**That passage is dated before the ruling and is superseded on this point by
it.** It is quoted here because §0c cited it, and because a reader comparing
the two must be able to see that the later landed ruling settles the question
the earlier derivation left open. **The exponent mapping is therefore NOT among
the unfixed elements.**

### 2c. What landed text does NOT fix

**(1) Which channel, or set of channels, the assembled chain's decoupling
comprises.**

A landed PI ruling selects a channel, and states its own scope.
`DECISION_LOG.md:1761-1766`:

```text
> Mean-field work proceeds in the **scalar channel with a real auxiliary
> field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`
> and admits the standard real linear Hubbard–Stratonovich
> representation; the induced V and A singlets have `g < 0` and do not.
>
> **This is a choice of direct route, not a judgement that the V/A
```

Its scope, `DECISION_LOG.md:1778-1781`:

```text
> **This does not close `OPEN-AC-1`.** It selects the channel for
> mean-field work; the Fierz ambiguity — that channels equivalent as
> operators are inequivalent after truncation — is unaffected by which
> one is used.
```

That ruling's title scopes it to `P2-PHASE-01`, and the landed statements that
carry its route forward carry the same scope.
`derivations/P2-PHASE-01_input_admissibility_contract.md:122-127`:

```text
    OPEN-AC-1  P/V/A/T mean-field construction.
               STILL OPEN. An input to C-ii whenever a channel beyond
               the scalar enters the comparison. Not required for a
               scalar-only evaluation, and the PI's route choice is
               scalar. It is the largest of the three and it has not
               been started.
```

`derivations/P2-PHASE-01_microscopic_parameter_domain.md:347-350`:

```text
- **It does not settle the non-scalar channels.** `OPEN-AC-1` — the
  P/V/A/T mean-field construction — remains open and blocks any
  enumeration beyond the scalar route. **It does not block the scalar
  route, which is the PI's chosen route.**
```

**No landed line extends that route choice to the assembled chain of the ξ
ledger.** The ruling names `P2-PHASE-01` mean-field work; the ledger states of
itself that `P2-PHASE-01` and SI-2 are untouched. Reading the ruling as fixing
this subject's channel would be an extension of a landed scope, which this task
does not perform.

**And the landed freeze keeps the candidate set open rather than reducing it to
one.** `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:109`:

```text
> Every non-redundant HS field supported by the canonical interaction remains in the candidate K_ij mixing set unless exclusion is affirmatively proven under the exclusion rule. Absence of an implementation, absence of a known condensate, computational convenience, or failure of one phenomenological role is not evidence for exclusion.
```

**What the manuscript under verification writes is a channel-by-channel
decomposition, not a single channel.** The manuscript is this repository's
SUBJECT, not its authority, and is quoted here as evidence of what is being
verified rather than as a landed convention.
`paper/emergent_gr_paper_v2_15.tex:281-292`:

```text
The four-fermion interaction is linearized by introducing
auxiliary fields $\Phi_A$ channel by channel:
\begin{equation}
\mathcal{L}_{\mathrm{HS}} = \bar{\psi}
\bigl(i\slashed{\partial} - g_A\Gamma^A\Phi_A\bigr)\psi
- \frac{1}{2G_A}\Phi_A^2,
\label{eq:HS}
\end{equation}
where the channel couplings $G_A$ are the independent parameters
of Eq.~\eqref{eq:Lgen}; for the minimal chiral pair used here,
$G_S = G_P = G$ and the remaining sectors enter only if their
couplings are switched on.
```

**And the question of which decomposition the ledger is read by is itself
landed open.** `derivations/P2-XI-B0a_induced-xi-scope-assessment.md:634-636`:

```text
    Q-M6  By what decomposition is the ledger to be read — by HS channel,
          by loop species, or by the `ξ(0)` / `Δξ(G)` / `ξ(G)` split?
          §5b records that these are not the same partition.
```

**(2) The decoupling prescription, including the Jacobian this task was
authorized to test.**

`derivations/P2-FIERZSUM-01.md:218-220`, one of the eight deliverables that
section lists under the heading *"What the gate must freeze (deliverables)"*:

```text
4. **The decoupling prescription**: auxiliary variables, constraints,
   Jacobian, and an explicit statement of what is generated
   dynamically rather than introduced as an independent field.
```

That note's registration status, `GATES.md:1374-1376`:

```text
- `P2-FIERZSUM-01` and the Route D concept note remain in review and are not
  registered here. The effective-discretization reading is non-operative and
  consumed by no gate.
```

**The one landed line that names the HS normalization names it as a redundant
representation parameter and assigns it no value.**
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:71-79`:

```text
| genuine microscopic coordinate | exact expression | scan eligible |
| --- | --- | --- |
| `G` | `G` | yes |

| auxiliary representation parameter | reason | scan eligible |
| --- | --- | --- |
| `HS_scale` | HS normalization / field rescaling | no |
| `Fierz_basis` | basis choice / crossing representation | no |
| `g_c` per channel | rejected T1 multi-coupling extension | no |
```

**"Not scan eligible" is a statement that changing it creates no new scan
coordinate. It is not a statement of its value**, and no landed line supplies
one.

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

## 3. Rule 22 — the classification and its resolution path

**Result: `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`. | COND-R, COND-M**

**Subclass.** `CONSTRUCTIVE GAP IDENTIFIED`, not `EVIDENCE INSUFFICIENT`. The
gap is not that the evidence was too thin to read: the landed statements are
explicit, and they say the object is not fixed. **The reason the dependence
question is returned unasked is a property of landed state, not of the check.**

**Resolution path, symmetric, defined here and NOT walked.** Either of the two
determinations below would close the gap; nothing in this artifact prefers one,
and this task performs neither.

    R-1  A landed determination of which channel, or set of channels, the
         assembled chain's decoupling comprises — either by extending the
         2026-08-09 route ruling's scope from P2-PHASE-01 mean-field work
         to the assembled chain, or by a separate determination naming the
         decoupling for the chain. Authority: the PI. Neither extension nor
         determination is proposed here.

    R-2  A landed decoupling prescription in the sense
         P2-FIERZSUM-01.md:218-220 states — auxiliary variables,
         constraints, Jacobian, and what is generated dynamically rather
         than introduced as an independent field. That note is landed not
         registered; by what route it or an equivalent becomes landed is
         the PI's.

**Symmetry.** The path is stated in both directions: `R-1` and `R-2` together
would return `UNIQUELY IDENTIFIED` and let `M1`–`M3` run; the absence of either
returns this same determination. **Nothing here asserts which outcome the
dependence question would then have**, and no sign, bound, magnitude or
structure is offered for `N_α[g]`.

**This result is evidence, not a disposition. | COND-R, COND-M** The membership
consequence of a dependence finding belongs to the PI under `P2-XI-RULINGS-02`,
Ruling 1, and no dependence finding was produced.

## 4. `M4` — scope statement (early-return wording)

**The landed criterion is written for every admissible decoupling.**
`derivations/P2-FIERZSUM-01.md:451-452`, verbatim:

```text
- **HS-normalization / Jacobian curvature test.** For every admissible
  decoupling `α`, verify not only recovery of the frozen quartic
```

**This task was SCOPED to the landed `α` only**, by
`P2-XI-RULINGS-02-CLARIFICATION-01` as quoted at §0a — **but landed state did
not uniquely identify that object, so NO dependence evaluation was performed.**
`α` was not evaluated. No `N_α[g]` was constructed, no variation was taken, and
no verdict from `M3`'s pre-registered vocabulary is returned. | COND-R, COND-M

**The family-wide residue is the registered open item.** It is registered in
`DECISION_LOG.md` under the PI's 2026-08-24 routing ruling, with status
`UNESTABLISHED. REGISTERED, NOT AUTHORIZED.` and its escalation condition
recorded and untriggered. **Nothing in this artifact begins, schedules,
constrains, prioritises or triggers it**, and executing this task does not
trigger its escalation condition, which requires both that the check return
`DEPENDENT` and that the term be subsequently found to grow with `L` — this
task returned no `DEPENDENT` and measured no `L`-scaling.

**The criterion is therefore NOT discharged in full by this task.** It is not
discharged in part either: on this path no decoupling was evaluated at all.
| COND-R, COND-M

## 5. What this artifact does not establish

1. **No dependence verdict.** `DEPENDENT`, `INDEPENDENT` and the `M3`
   `INCONCLUSIVE` vocabulary are all absent; `M3` did not run.
2. **No channel selection, no exponent-mapping choice, no preference among
   candidate decouplings.** `A2`'s prohibition holds throughout.
3. **No resolution of `DET-01`, and no choice of `𝔊`.**
4. **No membership disposition and no ledger edit.** The two OPEN rows are
   untouched, valueless, and left as they stand; `OPEN(Q-M3)` remains OPEN
   because this task returned no evidence that would dispose it.
5. **No L-scaling measurement, no magnitude estimate, no second decoupling.**
6. **No gate movement and no `PASS`/`FAIL`.** `P2-PHASE-01`, SI-2 and
   `P2-FIERZSUM-01`'s registration status are exactly where they were.
7. **No claim that the object does not exist.** The determination is about what
   landed state fixes, not about the physics: a decoupling that landed text
   does not uniquely identify may still be perfectly well defined once the PI
   supplies `R-1` or `R-2`.

END OF ARTIFACT
