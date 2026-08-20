# Landing record — `P2-GAPB-INTEG`

**Transport only, plus the §6 re-measurement.** Every statement about the
finding below is one the reviewed result already made. **Nothing is added,
reclassified or re-read.**

    Source   science/gapb-bridge-01   46b4791152fd87ced7e718df5ec3d91d394883ac
    Base     55deaec9ef49f197307e5e41f712a484473a4964
    Fork     f23a0e1e1a24398d082a9597444ff9f750ed38e1

---

## 1. The outcome, and the subclass question

    OUTCOME   INDETERMINATE — UNDETERMINED BY READING

**The reviewed result assigns NO rule 22 subclass to its own outcome, and none
is supplied here.**

**Recorded as observed.** `INDETERMINATE — UNDETERMINED BY READING` is one of
the four outcomes `P2-GAPB-BRIDGE-01`'s own §5 pre-registered; it is not a rule
22 subclass. Measured across the reviewed artifact, every occurrence of
`INCONCLUSIVE` refers to **`Q1`**, at `:232`, `:233` and `:492` — never to
`GAP-B`'s own result. `:233` carries `Q1`'s subclass
`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`, which is `Q1`'s and is transported
as `Q1`'s.

**A subclass added at integration is the defect `P2-PROJ-01-CLASS-01` was
created to avoid**, and none is added.

---

## 2. Every mismatch, with its classification AND its reasoning

**Five mismatches.** Classifications alone would not be checkable; each
reasoning below is the reviewed result's own.

### `MM-1` — SPECIES. `L-1`, `L-2`, `L-3`. **(iv) not determinable here**

`L2`'s object is the kernel obtained by integrating out **fermions**, and its
Ward premise is the diffeomorphism invariance of the **fermion** measure and
action. `EXT-01`'s object is a **massive vector** loop, a boson determinant.

**Not (i)** — the repository states the difference. **Not (ii)** — the
manuscript extends its machinery to one other species and for one other
purpose, a lattice **scalar** and **Finding 2's degeneracy**, not `eq:Ward` or
`eq:PiTT`. **Not (iii)** — a controlling relation would be a Ward identity for
this lattice Proca discretisation with its Symanzik counting, which the
repository does not contain and the reviewed result did not supply.

**What would settle it: a derivation, not a measurement.**

### `MM-2` — REGIME. `L-8`, `L-9`. **(i) the condition is met**

`Λ ~ 1/a`, and `a = 1` for this object — established by reading the action, not
by inheriting a description. `(q·a)²` runs across the pre-registered grid from
`0.0100` to `0.0784`, so `q ≪ Λ` holds.

**One ratio recorded and set aside**: `q/m` runs `0.333` to `0.933`, so the
measurement is not at `q ≪ m` — **but `L2` states no such condition.** Its
"infrared" is the external kernel's regime relative to `Λ`; the manuscript's
"infrared (k ~ m) region of the loop" is about **loop** momentum in a different
argument. **The two are not conflated, and the q/m observation is not promoted
into a condition on the argument.**

### `MM-3` — IMPROVEMENT. `L-6`. **(iv), and a measurement would bear on it**

`L-6` invokes the trace identity **for the improved stress tensor**. The
repository states nothing about improvement for this object; the reviewed
result settled it by reading the action, which is a minimal forward-difference
discretisation with **no Symanzik improvement term of any kind**.

**Not (ii), and the reason is specific**: the trace identity's function in `L2`
is to remove the **propagating scalar block**, and the discarded set contains
exactly the components that block governs — the spatial trace and `h00`, which
`GAP-A` identified as the `P0s` and `P0w` blocks. **A mismatch in the identity
that removes the scalar block cannot be irrelevant to two of the five
components at issue.**

**Not (iii)** — an analytic relation between improved and unimproved trace
identities at `O(q²)` for this discretisation is not in the repository.

### `MM-4` — CONTACT TERMS. `L-5`, and `L-6`'s "up to contact terms". **(ii) present and provably irrelevant to the `q²` conclusion**

**Two independent stated grounds, and the observable isolates it.** The
manuscript states the seagull tadpole "is *exactly* q-independent: contact terms
shift the momentum-independent part of the kernel but not its q² slope";
`mlog_coeff.py:10-11` states the same for this family of objects. **The reported
quantity is the `q²` coefficient of `Π(q) = A + Bq² + Cq⁴`, so a
`q`-independent term lands in `A`.**

**The mismatch is an intercept and the observable is a slope.** **This ground is
for the `q²`-coefficient observable and is not generalised beyond it.**

### `MM-5` — COVARIANCE STATE. `L-4`, `L-8`. **(iv) not determinable here**

`eq:PiTT` is stated for the **infrared** kernel, and the manuscript states that
covariance of the infrared effective action "must be restored by local
counterterms" including non-covariant `O(q²)` structures. `EXT-01`'s object is
the **bare finite-spacing kernel**, before any restoration.

**Why this is not `TRANSFER FAILS`.** Finding 2 establishes an **exact null
space** making the covariant coefficient **not identifiable from TT data**.
**That is an obstruction to DETERMINING the coefficient, not a demonstration
that `L2`'s conclusion is false of the restored kernel**, and turning the first
into the second is the invalid conversion the reviewed result's §5 forbids.

### And one condition met by prior work

`L-7`, the Barnes–Rivers basis, **MET by `GAP-A`, for `q ∥ e₀` and not beyond.**
The momentum condition travels with it and it is not promoted to a covariant
identity.

---

## 3. Why the outcome is not the measurement-required one

**Transported because it is the finding's most easily lost part** — a reader
seeing `INDETERMINATE` will look for the missing experiment.

The reviewed result's own reason: `MEASUREMENT REQUIRED` is reserved for a
mismatch whose status cannot be settled without a lattice measurement, and
**`MM-1` and `MM-5` are logically prior to `MM-3` and are not measurement
questions.** Until the species bridge exists, **a continuum-limit study of the
Proca object would report the continuum behaviour of the Proca object — it
would not establish whether `L2`'s fermion-sector conclusion transfers to it.**

**The measurement is specified in the reviewed result and was not run**:
evaluate the same ten-component decomposition at two or more lattice spacings
at fixed physical `m` and `q`, and observe whether the discarded group's `q²`
coefficients approach zero relative to the retained group as `a → 0`. A ratio
falling like `a²` shows a lattice artefact the continuum limit removes; a ratio
approaching a non-zero constant shows it does not.

**Stated plainly by the reviewed result, and transported: the measurement a
reader would reach for first would not, on its own, settle `GAP-B`.**

---

## 4. What this landing does and does not do to the finding's reach

**The finding is landed as it stands.**

**`P2-OBS-IDENT-01` has since established a relation bearing on the object the
mismatches concern.** `R-2` of the `DECISION_LOG.md` entry dated 2026-08-20
registers that **the consequence for reach is undecided.**

**This is a cross-reference to an open record and no consequence is drawn.** No
mismatch above is narrowed, widened, or re-read in its light, and the outcome
is neither upgraded nor downgraded.

---

## 5. The pre-registration characterisation finding

**Two properties named in `GAP-B`'s pre-registered wording appear nowhere in
the artifact they characterise.** The pre-registered question describes
`EXT-01`'s object as at `a = 1` and **unimproved**. Measured: a
repository-wide search for `unimproved` returns **zero** occurrences in
`EXT-01`'s artifact, its report, its diagnostic script, or `proca_loop.py`, and
no lattice spacing is stated in `EXT-01`'s artifact or report. Every occurrence
of the characterisation is in `PROJ-01`'s adjudication and downstream of it.

**What established them, transported because the finding is about method and is
not checkable without it: the reviewed result read the action.**
`proca_loop.py:5` defines `D_μ f(x) = f(x+μ) − f(x)` with unit shift and the
Brillouin zone runs `[−π, π)`, so lengths are in units of the spacing; and the
action carries no Symanzik improvement term of any kind.

**Both properties hold.** The finding is that they entered a frozen
pre-registration on a prior artifact's word and were established against the
object only when this task read it. **The historical pre-registration is not
rewritten.**

---

## 6. `M10` — the register census, re-measured

**`DECISION_LOG.md`'s stated scope**, quoted from its `:3-4`:

> This log is append-only. New decisions must use the entry template below and
> must not erase superseded decisions.

**And its own precedent for records of this shape**, `:2346-2349` and
`:2359-2360`:

> ## 2026-08-19 — EXT-01 execution-layer dispositions and open findings
>
> Decision owner: Executor, adopted for the EXT-01 integration

> **`O-1` and `O-2` are open findings, not decisions. Nothing is settled by
> recording them.**

**Every obligation recorded as having no admissible register, enumerated by
reading the three landing records that recorded them:**

    O-1   Register consequences of PROJ-01's component determinations.
          PROJ-01-INTEG landing record :198-203, "REGISTER: none".
          Re-grounded by RECON-01B-B0-INTEG to include the newly landed
          baseline.
          STATUS: OUTSTANDING.
          AGAINST DECISION_LOG.md's STATED SCOPE: ADMITTED. It is an open
          record adopted by an executor for an integration, with nothing
          settled by recording it — the precedent's own shape.

    O-2   The bridge tasks, GAP-A and GAP-B, one bounded task each.
          PROJ-01-INTEG landing record :205-208, "REGISTER: none".
          GAPA-INTEG's R-2 narrowed THIS OBLIGATION to GAP-B's half after
          GAP-A closed. (An obligation, not a mismatch — no mismatch above
          is narrowed by anything.)
          STATUS: DISCHARGED BY EXECUTION. Both bridge tasks were opened and
          executed; GAP-B's result is the artifact this task lands.
          AGAINST THE STATED SCOPE: ADMITTED, on the same ground. The
          precedent's D-2 is a deferral "Recorded so that it attaches to that
          work and is not lost", which is this shape.

    O-3   P2-RECON-01B-B0 integration.
          PROJ-01-INTEG landing record :210-211, "REGISTER: none".
          STATUS: DISCHARGED. P2-RECON-01B-B0-INTEG performed it.
          AGAINST THE STATED SCOPE: ADMITTED, on the same ground.

    R-2   GAPA-INTEG's R-2, "REGISTER: none — see below" at :196.
          STATUS: RESTATES O-2 and is not a separate obligation; that landing
          record says so at :198-202.
          AGAINST THE STATED SCOPE: ADMITTED, with O-2.

**All four are ADMITTED. None is "not admitted" and none is "not determinable
from the stated scope".**

**The standing claim is therefore false as measured.** Three landing records
state that no register's stated scope admits these records. **`DECISION_LOG.md`
admits every one of them**, and it was not among the registers those tasks
enumerated.

**A second measurement, recorded because it was reached by the same reading.**
The figure those records carry alongside the claim does not survive
enumeration either: `O-3` was discharged by the same task that restated the
figure, and `O-2` is discharged by this landing. **Measured now, ONE of the four
is outstanding — `O-1`.**

**THIS TASK PLACES NONE OF THEM.** Placement is a separate action with its own
authority question. `M10` establishes whether the standing claim is true; it is
not.

---

## 7. `R-5`, registered

    R-5   The homeless-obligation enumeration. §6's per-obligation result:
          all four admitted by DECISION_LOG.md's stated scope; one of the four
          outstanding; the standing claim that none is admitted is false as
          measured. **Whether any obligation is now placed, and by what
          authority, is undecided.**

**Registered in `DECISION_LOG.md`**, which admits it on the same stated scope
and the same precedent — an open record adopted by an executor for an
integration, settling nothing.

**`R-5` does not restate an existing obligation.** It is a finding about the
enumeration, not one of the obligations enumerated. **No count is incremented
by it.**

---

## 8. What this landing does not establish

It lands a finding already made, reviewed and verified, and measures one
standing claim about registers. **It produces no scientific result, no `β_V`,
moves no gate, and `P2-PHASE-01` is unchanged.**

`Q1` remains `INCONCLUSIVE` with its subclass and `Resolution path`. `GAP-A`
remains closed with its momentum condition. **`GAP-B` remains as the reviewed
result left it.** `H-EXT-01` remains `UNESTABLISHED — NOT ASSUMED BY
RECON-01b`. `A-EXT-01` is unchanged.
