# Landing record — `POLE-B0`, the manuscript's decisive pole milestone

    SOURCE      science/pole-b0-milestone-scope @ 3f78acfebd7e994460eb30ac54ffd31a5cf3c21f
    BASE        4b30e7855a657674aecf46d4cc76d68244f385a9
    MERGE       4102344bc405eb99c8786a2a8bacfd6e337bd4ab, --no-ff,
                source tip preserved as parent 2
    TASK        P2-POLE-B0-INTEG-02, re-issued after INTEG-01's A4 abort

**This is the landed record of a NEGATIVE RESULT, and it is written at the
prominence a positive result would receive.** The programme's own decisive
test is not executable, and the reason is not one reason but two of different
kinds, which the two layers below keep apart.

---

## The verdict as landed

    PRIMARY       REQUIRES A CONSTRUCTION NOT YET SCOPED

    PARTIAL       TRACTABLE BUT BLOCKED PENDING A RULING
                  — applying to PART of the scope only, and explicitly
                    NOT the primary verdict.

**The partial classification does not replace the primary one and must not be
read as softening it.** A ruling is a decision someone can take. A
construction that has not been scoped is work nobody has defined. The verdict
is primary on the second because the second survives every disposition of the
first.

---

## The load-bearing finding

    N_both = 0

**No milestone component holds both an applicable implementation and a
specification.**

**The consequence, which is why the primary verdict is a construction verdict
and not a ruling verdict:** the construction layer itself is not established.
There is no component of this test that is simultaneously specified and built.
Three components are built and unspecified; three are specified and unbuilt;
six are neither. **A test with nothing in the `BOTH` column is not a test that
is nearly ready, and no ruling changes the column.**

---

## Component accounting, transcribed

    12 = 0 both + 3 impl + 3 spec + 6 neither

**Transcribed from the branch's own execution report at `3f78acfe`. Not
recomputed, not re-derived, not re-partitioned.** The frozen text reads

    N_total = N_both + N_impl + N_spec + N_neither
       12   =    0   +   3    +   3    +    6

and the numerals and category labels above match it.

---

## LAYER 1 — RULING BLOCKERS

**Components blocked pending an `R1`–`R4` ruling.**

The source assessment classified each node, with `INDEPENDENT`,
`DEPENDENCE ESTABLISHED` and `DEPENDENCE NOT ESTABLISHED` as the three
available states, and recorded that silence is not independence:

    R1  the canonical kinetic operator and its parameters    DEPENDENCE ESTABLISHED
    R2  the admissible lattice extent, finite-volume rules   DEPENDENCE ESTABLISHED
    R3  boundary conditions, the temporal one in particular  DEPENDENCE ESTABLISHED
    R4  the microscopic variables, state space and measure   DEPENDENCE ESTABLISHED
    R5  the internal multiplicity N                          DEPENDENCE NOT ESTABLISHED

**All five nodes carry `STATUS OPEN` in the dependency ledger. This landing
rules none of them.**

**What a ruling would unblock.** `C1`'s lattice stress-tensor operator waits on
`R1`, which fixes the canonical Dirac operator and the Wilson parameter the
vertex prescription carries. `C6`'s Osterwalder–Schrader reflection positivity
waits on `R1` too, because the obligation must be discharged per declared
kinetic operator. `C10`'s finite-volume rules wait on `R2`. The temporal
boundary condition a spectral decomposition needs waits on `R3`. `C7`'s
definition of `⟨·⟩` waits on `R4`.

**These are removable by decision.** That is what makes them Layer 1.

---

## LAYER 2 — CONSTRUCTION BLOCKERS

**Components for which no applicable implementation exists and none is
scoped. These are not cleared by any ruling.**

    C7   a definition of ⟨·⟩ — the microscopic measure and state
    C8   an evaluation of ⟨TT⟩ beyond one loop
    C9   a preregistered operator basis for the tensor sector
    C10  finite-volume rules and the massless limit
    C11  the numerical meaning of "vanishing"
    C12  an artefact-versus-physics discriminator

**Six components. Neither implemented nor specified.**

### Ruling `R1`–`R4` in full would not clear Layer 2

**This is the statement the record exists to carry, and it is stated
plainly.** Suppose every one of `R1`, `R2`, `R3` and `R4` were ruled tomorrow,
in whatever way the PI chose. **All six components above would remain exactly
where they are.**

Ruling `R4` says what the microscopic measure is. **It does not supply a
method for evaluating a correlator against that measure** — `C8` is untouched.
Ruling `R2` says which lattice extents are admissible. **It does not supply a
finite-volume pole extraction** — the procedure in `C10` is still unwritten.
No ruling writes a preregistered tensor-sector operator basis (`C9`), decides
what "vanishing" means numerically (`C11`), or supplies a discriminator
separating a lattice artefact from a physical non-vanishing residue (`C12`).

**`C7` and `C10` appear in both layers, and that is not an error.** Each has a
ruling dependency AND is unbuilt and unspecified. Clearing the ruling leaves
the construction; the two blockages are independent and both must lift.

**The blockage would lift and the construction would still be absent.**

---

## Dependency transfer — two kinds, kept distinct

**POLE milestone — inherits `R4` UNCONDITIONALLY.**

> Its object is `⟨T_{μν}(x) T_{ρσ}(y)⟩`. The expectation-value bracket enters
> the DEFINITION of the correlator, not only the operator; without an
> ensemble / state space / functional measure the correlator is not yet
> defined.

**`SRC-B0` — inherits CONDITIONALLY.**

> A `Γ`-defined stress tensor inherits; an `S`-defined one does not; which the
> programme needs is unresolved.

**These are two statements and they are not one statement.** `SRC-B0`'s
conditional turns on which stress tensor a calculation uses, and the
manuscript's `T^{μν}` at `:673-675` is `S`-defined, so the operator itself
needs no measure. **The milestone does not ask for an operator. It asks for a
correlation function of two of them, and the correlation is where the measure
enters.** Merging the two into one dependency claim would lose precisely the
distinction that makes the milestone's inheritance unconditional.

---

## Negative delimitation of existing machinery

**Three delimitations. Each says what an existing component is NOT.**

**1. Barnes–Rivers projector machinery provides channel decomposition.** It is
**not** an interacting correlator, **not** pole extraction, and **not**
residue analysis. A projector sorts a rank-4 object into spin sectors; it says
nothing about where that object is singular.

**2. `tt_check.py` computes four channels and the caller retains the first.**
`project()` returns `g2, g1, g0s, g0w`; the caller takes `[0]`, and the spin-1
and both spin-0 channels are computed on every call and discarded. **Recorded
as evidence that building blocks present is not milestone implementation
present** — the three channels the manuscript's criterion is about are exactly
the three this code throws away.

**3. `RECON-01a` establishes a curved bosonic determinant / operator
construction.** Metric variations of `logdet` yield an effective-action
response, a `Γ⁽²⁾`-class object. **It is NOT an interacting stress-tensor
correlator and is not to be renamed as one.** `Γ⁽²⁾` is the 1PI kernel for an
external field — which is what the manuscript's `:807-808` sets aside by name
when it distinguishes a genuine pole from "merely an induced kinetic term for
an external field".

---

## Correction to the branch's own report

**The POLE-B0 report at `3f78acfe` states, of `scipy`, that the manifest
declares it and the code says it is not declared, and treats this as a
repository contradiction. It is not one, and the report's line citation is
also wrong.**

    location         the statement is at proca_curved.py:42-43, not :43-44
    subjects differ  pyproject.toml declares a PROJECT dependency;
                     proca_curved.py speaks of THIS ENVIRONMENT, whose
                     declared packages are listed in
                     docs/local/execution_environment.md and do not include
                     scipy. Both statements are true.

**The branch content at `3f78acfe` is unchanged by this correction.** The
source was merged as it stands; nothing was written back into it, and the
report on the branch still carries the erroneous sentence. **This record is
where the correction lives.**

**The correction does not affect the POLE-B0 verdict.** The `scipy` remark was
an execution-environment note. It sits outside the twelve-component accounting
above and outside every dependency finding — no component's classification,
no `R`-node state, and neither layer changes by one word.

**A separate relationship question remains OPEN.** Whether
`docs/local/execution_environment.md` is intended to mirror the full project
dependency set, or to state only the minimum validated execution environment,
has not been adjudicated. **If the latter, `scipy`'s absence from it is not an
inconsistency at all.** This record does not adjudicate it and **does not
assert that an inconsistency exists.**

    the original scipy contradiction                      NOT REPRODUCED
    pyproject.toml ↔ execution_environment.md relationship  OPEN

**A pre-registered conditional entry did not fire.** `INTEG-01` proposed a
`scipy` repository-consistency debt entry, conditional on a measurement
reproducing the contradiction. The measurement did not reproduce it. **No such
entry is created, and the conditional is recorded as having been pre-registered
and not fired** — an unfired condition is evidence the check worked, not a gap.

---

## What this landing does not establish

**Landing a negative result adds no support to the programme. This merge
closes a task.**

It does not establish that a massless spin-2 pole exists, or that it does not.
The manuscript calls that question nonperturbative and unresolved at
`:808-809`, and this landing leaves it there. It does not advance
`P2-PHASE-01`, which remains `Status: PROPOSED` with `Required computations:
(not started)`. It rules no `R`-node. It does not scope, design or begin the
construction layer — that item is registered as open, and registering an item
is not scoping it.

**What the programme gains is a map of what is missing**, and the map's
governing feature is that six of its twelve entries are blank in both columns.
