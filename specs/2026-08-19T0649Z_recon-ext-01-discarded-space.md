# P2-RECON-EXT-01 — Discarded external space, measured

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              MEASUREMENT + DOCUMENTARY. No landing.
    Origin            PI rulings 2 and 4 following P2-RECON-01B-B0

---

## 0. Binding SHA

    Evidence base (main at authorship)   968e726a5a4322eecf4254ff69b25832f263c155

If `main` has advanced when execution begins, execution does not proceed and
the specification returns to the Researcher for re-issue.

---

## 1. Objective

`P2-RECON-01B-B0` established that all four sectors `CIRC-01` reports fall
inside the axis-TT projected object, and recorded as open what the projection
discards, because **no repository measurement reports a magnitude there.**

This task measures it, and separately gathers the documentary provenance of
the projection choice.

    Q1   What does the axis-TT projection discard, stated as a decomposition
         of the external index space?

    Q2   What is the magnitude in the discarded space, relative to the
         retained one, at a single pre-registered k?

    Q3   By what authority, recorded where, did this particular external
         projection become the definition of the observable the βV line
         measures?

**Q3 is documentary.** It asks what the repository records, not what the
answer should be.

## 1a. The PI rulings this task implements, and their limits

    Ruling 2   measure first; DO NOT set a physics kill criterion.
               This task therefore states NO threshold, NO pass band, and NO
               criterion of the form "if the discarded magnitude exceeds X".
               Setting one before the magnitude is known would either be
               unfalsifiable or post-hoc.

    Ruling 4   the TT_RECIPES governance question is NOT adjudicated.
               This task does not decide whether a clean-room re-expression of
               a symmetry-fixed constant counts as reuse. It records the
               question's current documentary state under Q3.

    Ruling 1   the previously frozen blind target is retained unchanged.
               Nothing in this task modifies, re-registers, or evaluates it,
               and §3 constrains what may be computed so that it is not
               approached. **This specification does not reproduce the target
               expression**; it is recorded in the gate, and this task has no
               occasion to restate it.

## 1b. Non-objectives

This task does **not**:

1. compute `β_V`, `β_B`, their ratio, or any quantity the frozen anchor
   ranges over;
2. run a `k`-scan, or measure `k`-dependence of anything;
3. begin, scope, or contribute to the `RECON-01b` clean-room reconstruction —
   it is a diagnostic on the existing object;
4. adjudicate the component 5 or component 9 questions;
5. set any kill criterion, threshold, or acceptance band on a physical
   quantity;
6. merge anything, or move `main`.

## 1c. Authorised path manifest — defined once

    P1   the measurement artifact this task produces
    P2   any new script this task requires, under a path that makes its
         diagnostic status explicit and OUTSIDE scripts/recon2026/
    P3   this task's own spec, review and report artifacts

`A5` and `C9` both refer to this manifest and neither restates it.

**No existing file under `scripts/` is modified.** `scripts/recon2026/` is
neither modified nor added to: the clean-room construction is frozen and this
task is a diagnostic, not part of it.

---

## 2. Measurements

Every value is measured at `968e726a`. Nothing is carried.

    M1   Read the axis-TT projection's definition and record the external
         index space it spans, as a list of independent tensor components,
         with the file and line evidence.

    M2   Record the full external index space of the object before
         projection, on the same basis and by the same convention, with
         evidence. Record the decomposition
             full space = retained (M1) + discarded
         and enumerate the discarded components explicitly.

    M3   Record what the discarded components of M2 correspond to in the
         spin decomposition of the external perturbation, IF the repository
         states a correspondence. If it does not, record that no
         correspondence is stated, and do not supply one.

    M4   PRE-REGISTERED BEFORE RUNNING: fix a single value of `k` and record
         it, together with the lattice size, mass, and every other parameter
         the computation takes, in the artifact, BEFORE any number is
         produced. The pre-registration commit precedes the result commit.

    M5   At the M4 parameters, compute the contribution of each discarded
         component of M2, and of the retained space, to the same object
         `CIRC-01` decomposes. Report each as a magnitude and as a fraction
         of the total.

         **Reported as measured, in whatever direction it falls.** A large
         discarded fraction and a negligible one are equally reportable
         results and neither is a failure.

    M6   Record which code produced M5: every module imported, its path, and
         whether it lies under `scripts/recovered_2026/` or elsewhere. If any
         module carrying an analytic target is imported, record that fact and
         the target it carries.

    M7   DOCUMENTARY, for Q3. Record every repository location that fixes,
         selects, or justifies the axis-TT projection as the observable's
         definition — gate text, conventions, derivations, specifications,
         landed reports. For each: what it states, and whether it states a
         GROUND for the choice or only the choice itself.

         Record the earliest location by commit date, and whether any
         location records who or what selected it.

---

## 3. Computation constraints

    K1   No target-bearing `β` quantity, no ratio of two such quantities, and
         no quantity over which the frozen anchor ranges is computed,
         printed, logged, or stored.
    K2   No `k`-scan. `k` is fixed at M4's pre-registered value for the whole
         task.
    K3   The blind target is not read from `GATES.md` into any script, test,
         or output of this task.
    K4   If a computation the executor believes necessary would violate K1-K3,
         it is not performed; the item is recorded as UNMEASURED with the
         reason, and returned to the Researcher.

**These constrain a measurement; they are not abort conditions and §4 does not
list them.**

---

## 4. Abort conditions

Execution stops, with no partial artifact, and returns to the Researcher if:

    A1   the base SHA observed differs from §0
    A2   the axis-TT projection's definition cannot be located
    A3   the object CIRC-01 decomposes cannot be computed without modifying
         an existing file under scripts/
    A4   the M4 pre-registration cannot be committed before the result
    A5   a path outside the §1c manifest is modified

---

## 5. Required content of the artifact

1. `M1` and `M2` with the explicit decomposition and the enumerated discarded
   components.
2. `M3`, in whichever of its two forms the evidence supports.
3. `M4`'s pre-registration, visibly earlier in the commit sequence than `M5`.
4. `M5`'s table: every component, magnitude, and fraction.
5. `M6`'s provenance of the computation, including any target-bearing import.
6. `M7`'s documentary record for Q3, distinguishing locations that state a
   ground from locations that state only the choice.
7. A statement of what the measurement does not establish, naming at minimum:
   that it measures one `k` and says nothing about `k`-dependence; that it
   sets no criterion; and that a magnitude is not by itself a judgement of
   physical relevance.
8. Any question raised and not settled, recorded as open.

**The artifact must not recommend what to do about the discarded space, and
must not state whether the measured fraction is acceptable.**

---

## 6. Acceptance criteria

    C1   M1 and M2 present, with the decomposition arithmetic shown: the
         retained and discarded component counts sum to the full space.
    C2   M3 present in one of its two forms.
    C3   M4's pre-registration commit precedes M5's result commit. Verified
         by commit order, not by assertion.
    C4   M5 reports every discarded component enumerated in M2, with no
         component omitted.
    C5   M6 lists the imports with their paths and target status.
    C6   M7 records at least the gate location, and classifies each location
         as stating a ground or stating only the choice.
    C7   Neither the measurement artifact nor any diagnostic script or output
         this task produces contains a `β_V` value, a `β_B` value, their
         ratio, or the frozen target literal.

         **Search extent, stated explicitly.** The check covers the
         measurement artifact, every script this task adds, and every output
         those scripts emit. It does **not** cover this specification or its
         bound review: those are governance inputs authored before any
         measurement, not numerical outputs, and including them would make
         the criterion unsatisfiable for any specification that has to name
         what it forbids.
    C8   The §5.7 statement of non-establishment is present, and the artifact
         contains no recommendation and no acceptability judgement.
    C9   No path outside the §1c manifest is modified; `main` is unmoved;
         only this task's branch is pushed.
    C10  Every blob under `scripts/recon2026/` has its id unchanged. Record
         the observed ids.

---

## 7. Substring hazards

    TT              matches tt_check and TT_RECIPES; these are different
                    objects and the artifact must not use one token for both
    trace           matches traceless; the spatial trace and the traceless
                    combinations are different components
    projection      does not match projector
    k               the scan variable, the ratio's k, and lattice momentum
                    indices are written alike; state which is meant at each use
    external        the external index space and an external digest are
                    unrelated uses in this repository

A check that cannot state its exclusions is performed by reading.

## 8. Criterion satisfiability

`C7` is negative and satisfiable by reading for absence; it does not require
the artifact to declare the absence.

`C3` is checked by commit order, which is observable independently of what
either commit claims about itself.

`M3`'s second form — no stated correspondence — is a completed measurement.
`C2` accepts it.

---

## 9. Branch mechanics

    Branch       a new science/<scientific-task> branch
    Merge        NONE. main MUST NOT MOVE from 968e726a.
    Push scope   this task's branch only.
    Prohibited   force-push; --force-with-lease; branch deletion; history
                 rewrite

---

## 10. Post-execution verification (Researcher)

1. re-derive `C1`'s decomposition arithmetic;
2. confirm `C3` by reading the commit sequence;
3. read `M5` against `M2` for completeness;
4. grep the measurement artifact and any added script or emitted output for
   the frozen target literal and for `β_V`/`β_B` values, stating exclusions,
   and over the extent `C7` defines — not over the specification or review;
5. confirm `C9` and `C10` by `git ls-remote` and blob id;
6. anything unevaluable is recorded **INCONCLUSIVE**, not PASS.

---

## 11. What this task does not establish

It produces no `β_V`, moves no gate, and does not advance `P2-PHASE-01`. It
measures the discarded/retained decomposition at one pre-registered `k` and
records where a choice came from. Whether what it measures matters is a PI
judgement this task is written to inform and not to make.

---

## 12. Open, and deliberately not actioned here

1. **Component 5 — the `TT_RECIPES` clean-room question.** Not adjudicated.
2. **Component 9 — whether a specification exists or has only been named.**
   Not adjudicated; the PI has ruled it is not upgraded.
3. **`k`-dependence of anything measured here.** Out of scope by `K2`.
4. **Whether the discarded space warrants a criterion.** Ruling 2 defers it
   until the magnitude is known, which is what this task produces.
