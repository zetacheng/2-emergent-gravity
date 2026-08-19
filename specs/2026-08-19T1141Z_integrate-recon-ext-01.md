# P2-RECON-EXT-01-INTEG — Integration specification

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes

---

## 0. Binding SHAs

    Integration base (main at authorship)   968e726a5a4322eecf4254ff69b25832f263c155
    Branch to integrate                     science/recon-ext-01-discarded-space
                                            70f0e257b9afcd9f97445c5c2c62530fa742321e

If either has advanced when execution begins, execution does not proceed and
the specification returns to the Researcher for re-issue.

---

## 1. Objective

Land the `EXT-01` measurement; record the execution-layer decisions taken on
its result; and register the definitional convention `A-EXT-01`, the
physical hypothesis `H-EXT-01`, and the assumption review that produced their
present form.

## 1a. Non-objectives

This task does **not**:

1. set any criterion, threshold, or acceptance band on the discarded space;
2. adjudicate the axis-TT projection question — that is `RECON-PROJ-01`;
3. adjudicate component 5 or component 9;
4. modify the frozen blind target, or re-register it;
5. begin `RECON-01b`;
6. modify any file under `scripts/`.

## 1b. Authorised path manifest — defined once

    P1   the register file(s) M6 selects for A-EXT-01 and H-EXT-01, which
         need not be the same file, and the assumption-review artifact
    P2   the register used for the deferred and open items of §6
    P3   this task's own spec, review, landing-record and report artifacts
    P4   every path arriving from science/recon-ext-01-discarded-space by the
         merge itself

`A5` and `C9` both refer to this manifest and neither restates it. `P3` and
`P4` are necessarily present in the diff; an abort condition omitting either
would fire on correct execution.

---

## 2. Pre-execution measurements

Every value is measured at execution time. Nothing is carried from the
execution report, from this specification, or from the handover.

    M1   Test suite on the merge product and at 968e726a. Record
         passed / failed / deselected with the invocation, in real git
         worktrees.
    M2   Ancestry: is 70f0e257 currently an ancestor of main? Record observed.
    M3   Dry-run merge: conflict-free or not.
    M4   `git diff --name-only 968e726a..<merge product>` — full list.
    M5   Locate the `science/*` integration clause in
         `docs/BRANCHING_POLICY.md`; record its line span and the merge mode,
         allowed-ref scope and main-advance rule it states, as read.
    M6   Read the stated scopes of the repository's registers and record
         which admits each entry class of §5, and which admits the
         deferred and open items of §6. Record separately which admits a
         DEFINITIONAL CONVENTION and which admits a PHYSICAL HYPOTHESIS;
         these may differ. If no register's stated scope admits one of the
         classes, record the scopes observed and return to the Researcher.
    M7   Recompute the two robust ratios from the landed measurement's own
         recorded coefficients:
             |sum discarded| / |sum retained|
             max|discarded component| / mean|retained component|
         Record both as recomputed, alongside the values the measurement
         reports. A difference is recorded, not reconciled.

---

## 3. Abort conditions

    A1   the base or branch SHA observed differs from §0
    A2   M3 reports conflicts
    A3   M1 shows a failure not also present at 968e726a for the same test
    A4   M5 finds no clause governing integration of a `science/*` branch, or
         one contradicting §4
    A5   a path outside the §1b manifest appears in M4
    A6   M7's recomputation does not reproduce the landed measurement's
         reported ratios

---

## 4. Merge mechanics

Governed by the clause located under `M5`. Shape:

    Source        science/recon-ext-01-discarded-space @ 70f0e257, pinned,
                  merged --no-ff into a dedicated integration branch so the
                  source tip is preserved as a merge parent. Squash and
                  rebase integration prohibited.
    Landing       main advances by FAST-FORWARD only. Verify before the push
                  and record the exit status. If a fast-forward is not
                  available, STOP.
    Push scope    the integration branch and `refs/heads/main`, and no other
                  ref. The source branch does not move.
    Prohibited    force-push; `--force-with-lease`; branch deletion; history
                  rewrite.

---

## 5. Definitions and hypotheses register — required content

Two entries. **The distinction between them is the point: they are not merged,
abbreviated, or presented as one item, and they are not the same type of
object.**

### 5.0 Schema, adopted here and forward

Each entry carries, as named fields:

    ID / Type / Status / Exact statement / Scope / What depends on it /
    What does NOT depend on it / Evidence / Falsifier or resolution
    condition / Review / Review SHA / Date / Supersedes

`Type` distinguishes at minimum a **definitional convention** from a
**physical hypothesis**. An entry whose `Type` is definitional carries no
falsifier; its resolution condition field records instead what would change
its *scope*.

**Location is determined by `M6`, not by the identifier.** The prefix `A-` is
retained for `A-EXT-01` because its provenance is already formed in the
session record, but the prefix does not place it: if the repository has a
conventions or definitions register, a definitional entry belongs there and
not in an assumption register. If no register's stated scope admits a
definitional convention, record the scopes observed and return to the
Researcher.

### 5.1 `A-EXT-01` — Definitional axis-TT observable

    Type     DEFINITIONAL CONVENTION — working definition.
             NOT a physical assumption.
    Status   ADOPTED for the RECON line.

Exact statement, landed verbatim:

> For `RECON-01b`, `Z_axis-TT` is defined as the coefficient extracted after
> the repository's axis-TT projection. This is a definition of the observable
> used by the reconstruction pipeline, not a derived statement that the
> discarded external complement is physically negligible. All `RECON-01b`
> results must therefore be stated relative to `Z_axis-TT`, and must not be
> identified with the full gravitational response unless that equivalence is
> independently established.

### 5.2 `H-EXT-01` — Physical completeness hypothesis

    Type     PHYSICAL HYPOTHESIS — directional, falsifiable.
    Status   UNESTABLISHED — **NOT ASSUMED BY `RECON-01b`.**

Exact statement, landed verbatim:

> The discarded external complement makes no contribution to the physically
> relevant gravitational observable, so that `Z_axis-TT = Z_physical`.

The `Status` line is load-bearing and is landed with the entry: **`RECON-01b`
requires only the definition `A-EXT-01`; it does not require `H-EXT-01` to be
true, and does not assume it.** A reader who takes `RECON-01b` to presuppose
`H-EXT-01` has read the design backwards.

### 5.3 The distinction, recorded as the reason the two are separate

The record states, in its own words:

- **A definition is not a falsifiable proposition.** `A-EXT-01` cannot be
  refuted by a future calculation; `Z_axis-TT` remains well-defined whatever
  is later established.
- **`H-EXT-01` is the falsifiable proposition.** If the complement is later
  derived to make no contribution to the target observable, what is upgraded
  to a theorem is *the physical completeness of the projection for this
  observable*. If the complement is shown to contribute irreducibly,
  `H-EXT-01` is refuted and the outcome is not that `A-EXT-01` was wrong but
  that `Z_axis-TT` is not the full physical `Z`.

**Provenance.** The record states that the Researcher drafted a single entry
that treated the definition as itself falsifiable — a type error — and that
the present two-entry form, the directional wording of `H-EXT-01`, and the
`NOT ASSUMED` status all follow an assumption review. **The correction is
recorded, not silently absorbed.**

### 5.4 The assumption review, landed as an independent artifact

The review is landed as its own file, not summarised into the register entry.
Each register entry pins the review by SHA in its `Review SHA` field.

    entry     under the register M6 selects
    review    under a reviews path for assumption reviews, distinct from
              the specification-review path

**Binding rule, landed with the schema:** a register entry's `Review SHA` binds
to the exact bytes reviewed. **If an entry's statement is later edited, the
pinned review no longer applies and a new review is required.** A review must
never be carried across a wording change — this is the same exact-byte
principle the specification reviews already use.

### 5.5 Consequence for how `RECON-01b` may be claimed

Recorded with the entries, not deferred to a later task:

> `RECON-01b` tests whether, on the axis-TT-defined observable, the clean-room
> reconstruction recovers the pre-registered structure. It is a **conditional
> spin-2-sector reconstruction test**. It may not be stated as having
> reconstructed the full gravitational `Z`, and it may not be cited as
> evidence for vanishing spin-1/0 residues.

---

## 6. Execution-layer dispositions and open findings

`D-1` to `D-3` are **execution-layer dispositions, adopted for this task and
reversible by PI adjudication.** They are not PI rulings, and they carry no
PI-level scientific authority. They are recorded so that they can be inspected
and reversed rather than inherited silently.

`O-1` and `O-2` are **open findings, not decisions.** Nothing is settled by
recording them.

    D-1   NO CRITERION IS SET on the discarded space.
          Ground: the shares are signed, unbounded, and subject to
          cancellation, so a threshold on them would fix an arbitrary choice
          of normaliser. The robust quantities are the two ratios of M7.
          Status: MEASURED, NO CRITERION SET, with the reason recorded.
          This is not "awaiting a PI ruling"; it is a disposition open to
          reversal.

    D-2   EXTENSION IN MASS AND VOLUME IS DEFERRED, with reason.
          The measurement stands at one pre-registered point. Robustness of
          the ratios in mass and in volume is unmeasured. Deferred to the
          RECON-01b construction, where the same machinery is already
          required, rather than opened as a separate task now.
          Recorded so that it attaches to that work and is not lost.

    D-3   THE PROJECTION QUESTION IS ROUTED TO RECON-PROJ-01, not settled
          here, and not settled by the magnitude. Whether the complement
          matters is a question for derivation, not for 0.2973 or 1.008.

    O-1   EVIDENCE-ARCHITECTURE SEPARATION. Open finding.
          The βV/RECON line is a TT-conditioned reconstruction test. A test of
          the manuscript's decisive claim — a spin-2 pole with vanishing
          spin-1/0 residues — requires a calculation that does not project the
          other channels away before measuring. Whether any current numerical
          pipeline performs the latter is recorded as an open question.
          **This does not alter POLE-B0's verdict.** It records that the
          construction POLE-B0 found unscoped may be the pipeline the
          decisive claim requires. Priority is a PI matter and is not set here.

    O-2   MAGNITUDE IS NOT CHANNEL STRUCTURE. Open finding.
          The measurement establishes that the discarded directions cannot be
          neglected on grounds of magnitude. It establishes nothing about
          whether those directions carry physical poles, where any pole lies,
          or whether a residue vanishes. Recorded so that the magnitude
          result is not read as a channel-structure result.

---

## 7. Acceptance criteria

    C1   `git merge-base --is-ancestor 70f0e257 <main tip>` succeeds.
    C2   `A-EXT-01` and `H-EXT-01` exist as two separate entries, each
         carrying its §5.1 / §5.2 text and the full §5.0 field set, with
         `Type` distinguishing DEFINITIONAL CONVENTION from PHYSICAL
         HYPOTHESIS, and `H-EXT-01` carrying the `NOT ASSUMED BY RECON-01b`
         status. Verified by reading.
    C3   §5.3's distinction is present, including the statement that a
         definition is not falsifiable and the identification of `H-EXT-01`
         as the falsifiable proposition.
    C4   The provenance statement of §5.3 is present, recording the
         Researcher's weaker draft and the review that corrected it.
    C5   The assumption review is landed as its own artifact, identified as
         an assumption review and not as a specification review, and each
         entry's `Review SHA` field pins it by the bytes reviewed. The §5.4
         binding rule — that an edit to an entry's statement voids the pinned
         review — is landed with the schema.
    C6   §5.5's claim restriction is present, including both prohibitions.
    C7   `D-1`, `D-2`, `D-3`, `O-1`, `O-2` exist, each identified as a
         execution-layer disposition or an open finding, with identifiers
         drawn from the selected register's own sequence.
    C8   `M7`'s recomputed ratios are recorded beside the reported ones.
    C9   `M4` lists no path outside the §1b manifest.
    C10  Refs pushed are exactly the integration branch and `refs/heads/main`.
    C11  Every blob under `scripts/` is unchanged from 968e726a except those
         arriving with the merge. Record the observed ids for
         `scripts/recon2026/`.

---

## 8. Substring hazards

    TT              matches tt_check and TT_RECIPES
    trace           matches traceless; the spatial trace and the traceless
                    combinations are different components, and conflating
                    them would move a component between the retained and
                    discarded sets
    projection      does not match projector
    assumption      matches "locked assumptions" in gate text, which is a
                    different register
    A-EXT-01 / H-EXT-01   share a suffix; a search for one matches neither
                    reliably. Read.

A check that cannot state its exclusions is performed by reading.

## 9. Criterion satisfiability

`C2` requires two entries to exist and is established by reading both; it does
not search for a token that only one of them would carry.

`C4` is satisfiable because the provenance statement is required content under
§5.3, not something the executor must discover.

`A6` compares a recomputation against a landed number; both exist before the
check runs.

---

## 10. Post-execution verification (Researcher)

1. re-run `C1`;
2. read `A-EXT-01` and `H-EXT-01` against §5.1–5.3, confirming they are two
   entries and that neither states the other's content;
3. recompute `M7`'s two ratios independently from the landed coefficients;
4. confirm `C7`'s five items and their identifiers;
5. confirm `C10` by `git ls-remote` and `C11` by blob id;
6. anything unevaluable is recorded **INCONCLUSIVE**, not PASS.

---

## 11. What this task does not establish

It lands a measurement, a definition and a hypothesis. It produces no `β_V`,
moves no gate,
and does not advance `P2-PHASE-01`. It does not make the axis-TT projection
correct or incorrect; it records that the choice is presently definitional and
that its physical completeness is an open question.

---

## 12. Next, and deliberately not actioned here

1. **`RECON-PROJ-01`** — the projection adjudication, with branches
   distinguishing a *derivational* ground for axis-TT from a *definitional*
   one. The distinction matters because existing repository evidence already
   supplies the definitional kind, and a branch structure that does not
   separate them could be satisfied without answering the question.
2. **Component 9** — deferred until the projection / completeness
   adjudication is settled. **Not** "until the observable definition is
   settled": `A-EXT-01` settles the observable definition operationally as of
   this landing. What remains open is `H-EXT-01`.
3. **Component 5** — the `TT_RECIPES` question, unadjudicated.
