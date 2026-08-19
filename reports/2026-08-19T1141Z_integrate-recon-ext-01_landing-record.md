# Landing record — `EXT-01`, the discarded external space

    SOURCE      science/recon-ext-01-discarded-space @ 70f0e257b9afcd9f97445c5c2c62530fa742321e
    BASE        968e726a5a4322eecf4254ff69b25832f263c155
    MERGE       45e7b9042cadda338ba371ca942b538e7007603d, --no-ff,
                source tip preserved as parent 2

**What lands is a measurement, a definition, and a hypothesis — three
different kinds of object, and the record keeps them apart.**

---

## 1. The measurement, as landed

**At one pre-registered parameter point, the external space the axis-TT
projection discards is not a small correction.**

    sum over the five retained         +1.098831929e-01
    sum over the five discarded        -3.266825703e-02
    mean over the five retained        +2.197663858e-02
    largest single discarded, |D1|      2.215669317e-02

**The two robust ratios, recomputed at this landing from the landed
coefficients rather than carried:**

    |sum discarded| / |sum retained|        0.297300
    max|discarded| / mean|retained|         1.008193

**Both reproduce the values the measurement reports, to every printed digit.**

**`D1` alone is 1.008 times the mean retained component** — larger than the
average component the projection keeps.

**The signed shares are not the robust quantities and are not repeated here as
if they were.** The retained group's share is `+142%` and the discarded
group's `−42%`, because the two carry opposite signs and the denominator is
their sum. **A threshold on a signed, unbounded, cancelling share would fix an
arbitrary choice of normaliser**, which is why `D-1` sets none.

**Every component scales as `q²`** — observed exponents in `[1.9887, 1.9982]`
— so the coefficient is a meaningful extraction for all ten, retained and
discarded alike.

---

## 2. `A-EXT-01` — a definitional convention

**Registered in `CONVENTIONS.md`, the repository's Convention Registry**, in a
new definitional-conventions section carrying the full field schema. **The
locked-conventions table is unchanged**; no row of it is added to, altered, or
superseded.

    Type     DEFINITIONAL CONVENTION — working definition.
             NOT a physical assumption.
    Status   ADOPTED for the RECON line.

> For `RECON-01b`, `Z_axis-TT` is defined as the coefficient extracted after
> the repository's axis-TT projection. This is a definition of the observable
> used by the reconstruction pipeline, not a derived statement that the
> discarded external complement is physically negligible. All `RECON-01b`
> results must therefore be stated relative to `Z_axis-TT`, and must not be
> identified with the full gravitational response unless that equivalence is
> independently established.

**It carries no falsifier**, because a definition is not a falsifiable
proposition. Its resolution-condition field records instead what would change
its *scope*.

---

## 3. `H-EXT-01` — a physical hypothesis

**Registered in `DECISION_LOG.md`**, which is where this repository already
records open items as `UNESTABLISHED`. **A hypothesis is not a convention, so
it is not in the Convention Registry.**

    Type     PHYSICAL HYPOTHESIS — directional, falsifiable.
    Status   UNESTABLISHED — **NOT ASSUMED BY `RECON-01b`.**

> The discarded external complement makes no contribution to the physically
> relevant gravitational observable, so that `Z_axis-TT = Z_physical`.

**The `Status` line is load-bearing and lands with the entry.** `RECON-01b`
requires only the definition `A-EXT-01`; **it does not require `H-EXT-01` to be
true, and does not assume it.** A reader who takes `RECON-01b` to presuppose
`H-EXT-01` has read the design backwards.

---

## 4. The distinction, and why the two are separate entries

**A definition is not a falsifiable proposition.** `A-EXT-01` cannot be refuted
by a future calculation; `Z_axis-TT` remains well-defined whatever is later
established.

**`H-EXT-01` is the falsifiable proposition.** If the complement is later
derived to make no contribution to the target observable, what is upgraded to a
theorem is *the physical completeness of the projection for this observable*.
If the complement is shown to contribute irreducibly, **`H-EXT-01` is refuted,
and the outcome is not that `A-EXT-01` was wrong but that `Z_axis-TT` is not
the full physical `Z`.**

**Provenance, recorded and not silently absorbed.** The Researcher drafted a
single entry that treated the definition as itself falsifiable — **a type
error**. The present two-entry form, the directional wording of `H-EXT-01`,
and its `NOT ASSUMED` status all follow an assumption review.

---

## 5. The assumption review

**Landed as its own artifact**,
`reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md`,
identified in its header as an **assumption review** and carrying
`Function: Reviewer`. **It is not summarised into either register entry.**

**Each entry pins it by the digest of the exact statement bytes**, so that an
edit to a statement breaks the pin visibly:

    A-EXT-01 statement   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01 statement   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
    review artifact      e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953

**Both statement digests were verified against the landed bytes after landing**
and both match.

**Binding rule, landed with the schema in `CONVENTIONS.md`:** a `Review SHA`
binds to the exact bytes reviewed. **If an entry's statement is later edited,
the pinned review no longer applies and a new review is required.** A review is
never carried across a wording change.

**One thing the review record states about itself, because it is true and a
reader should not have to infer it:** the executor received no free-standing
assumption-review document. The Reviewer's assessment of these two statements
was delivered inside the pre-execution review of this integration
specification, and the artifact quotes that review verbatim with its section
numbers, attributing nothing to the Reviewer that the Reviewer did not write.

---

## 6. Consequence for how `RECON-01b` may be claimed

> `RECON-01b` tests whether, on the axis-TT-defined observable, the clean-room
> reconstruction recovers the pre-registered structure. It is a **conditional
> spin-2-sector reconstruction test**. It may not be stated as having
> reconstructed the full gravitational `Z`, and it may not be cited as
> evidence for vanishing spin-1/0 residues.

**The second prohibition is the one with teeth.** A calculation defined inside
the axis-TT subspace cannot independently establish a channel separation that
its own projection already imposes.

---

## 7. Execution-layer dispositions and open findings

**Registered in `DECISION_LOG.md` as a separate dated entry.**

**`D-1` to `D-3` are execution-layer dispositions, adopted for the EXT-01
integration and reversible by PI adjudication. They are not PI rulings and
carry no PI-level scientific authority.** **`O-1` and `O-2` are open findings,
not decisions.**

    D-1   NO CRITERION IS SET on the discarded space, with the reason
          recorded. Not "awaiting a ruling" — a disposition open to reversal.
    D-2   EXTENSION IN MASS AND VOLUME IS DEFERRED to the RECON-01b
          construction, where the same machinery is already required.
    D-3   THE PROJECTION QUESTION IS ROUTED TO RECON-PROJ-01, not settled
          here and not settled by the magnitude.
    O-1   EVIDENCE-ARCHITECTURE SEPARATION. The βV/RECON line is a
          TT-conditioned reconstruction test; the manuscript's decisive claim
          needs a calculation that does not project the other channels away
          before measuring. Does not alter POLE-B0's verdict.
    O-2   MAGNITUDE IS NOT CHANNEL STRUCTURE. The measurement says the
          discarded directions cannot be neglected on grounds of magnitude,
          and says nothing about poles or residues.

---

## 8. What this landing does not establish

**It does not make the axis-TT projection correct or incorrect.** It records
that the choice is presently definitional and that its physical completeness is
open.

**It does not claim `EXT-01` disproves the axis-TT observable**, and does not
claim the large discarded components are physical spin-0/1 poles. **What
`EXT-01` establishes is that numerical smallness cannot presently justify
discarding the complement.** Pole content and physical relevance are separate
questions, and `O-2` exists to keep them separate.

**No criterion is created from the observed result.** The measure-first ruling
stands: any future criterion must arise from a physical or structural
adjudication, not from a number selected after seeing the magnitude.

**It produces no `β_V`, moves no gate, and does not advance `P2-PHASE-01`**,
which remains `Status: PROPOSED`. **It does not begin `RECON-01b`**, adjudicate
the projection question, or touch components 5 or 9.
