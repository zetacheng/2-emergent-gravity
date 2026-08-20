# Landing record — `P2-PROJ-01-INTEG`

**Transport only.** Every statement below is one a reviewed result already
concluded. **Nothing here is a new finding, and nothing here is a
classification this integration made.**

    Source 1   science/recon-proj-01      e333b8a025c39fe66931a9763fe740d71209dc0a
    Source 2   science/proj-01-class-01   a6241239b9d52a1a6348052f6c8deb3fbafffb0d
    Base       15796ed3f1e68d6e91b90f9e404d55b25cee9f80

---

## 1. `Q1` and its subclass, kept in their two documents

    Q1 verdict     INCONCLUSIVE, unchanged
                   derivations/P2-RECON-PROJ-01_projection-adjudication.md:5-7
                   reports/2026-08-19T2214Z_recon-proj-01.md:4
                   reason: UNDETERMINED BY READING

    Subclass       INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
                   derivations/P2-PROJ-01-CLASS-01_q1-classification.md:12
                   carrying its label:
                   RETROSPECTIVE CLASSIFICATION — assigned after rule 22 was
                   landed; does not alter the finding, its verdict, or the
                   date it was recorded.

**The subclass was not present in the adjudication and has not been written
into it.** It was produced by a separate reviewed task, `P2-PROJ-01-CLASS-01`,
and it remains in that task's artifact. This integration transports both and
merges them into no single document.

**The reason is rule 17**, `CONVENTIONS.md:1280-1288`:

> **An integration, derivation, or any task that carries reviewed
> results forward MUST NOT add a governance or epistemic classification
> the reviewed results did not carry.**

Transporting a reviewed classification is permitted. Relocating it into a
document that did not carry it is not, and would additionally edit an executed
artifact.

**Measured on the merge product:** the four files arriving from Source 1
contain zero occurrences of `CONSTRUCTIVE GAP`, `EVIDENCE INSUFFICIENT`,
`subclass`, or `Resolution path`.

---

## 2. The two gaps, with both signs

As the classification states them. Neither direction is omitted or abbreviated.

### `GAP-A` — the basis identification

    WHAT WOULD ESTABLISH IT
        A reviewed derivation stating that, for q along an axis, the
        Barnes–Rivers TT block and the span of TT_RECIPES are the same
        five-dimensional space, and that the Barnes–Rivers non-TT blocks are
        the five components EXT-01 enumerates as discarded. The kind of work
        is named: a structural identification of two projector bases.

    ... AND WHAT THAT WOULD THEN PERMIT
        L2 would satisfy Part 2 of Q1's test as well as Part 1. Q1 could then
        be re-run against its own pre-registered outcomes and could return
        FOUND. NOT AUTOMATICALLY: Q1's outcome is set by a task executing
        Q1's test, and GAP-B would remain open.

    WHAT WOULD REFUTE IT
        A reviewed derivation stating that the two sets are NOT the same —
        the sign the adjudication itself admits, "or that they are not".

    ... AND WHAT THAT WOULD THEN MEAN
        L2 would fail Part 2 and cease to be a candidate ground. Q1's
        pre-registered NOT FOUND IN REPOSITORY outcome would be supported on
        this location, and the three repository locations that instruct a
        reader to DISTINGUISH the two decompositions would be shown to have
        been right to.

    WHAT IT WOULD SETTLE ON ITS OWN
        GAP-A only.

### `GAP-B` — the regime transfer

    WHAT WOULD ESTABLISH IT
        A reviewed derivation stating that L2's O(p⁴/Λ²) suppression —
        derived for the infrared effective kernel Γ⁽²⁾, under Symanzik power
        counting, for the improved stress tensor up to contact terms —
        transfers to the object EXT-01 measured: a lattice Proca bubble at
        a = 1, m = 0.3, finite n, unimproved.

    ... AND WHAT THAT WOULD THEN PERMIT
        The conclusion L2 carries would be about the object the repository
        actually measures. NOT ON ITS OWN: without GAP-A, L2's conclusion is
        about a set not shown to be the discarded complement.

    WHAT WOULD REFUTE IT
        A reviewed derivation stating that the suppression does NOT transfer.

    ... AND WHAT THAT WOULD THEN MEAN
        L2's conclusion would not bear on the measured object even with GAP-A
        closed. EXT-01's measurement would stand as a measurement of a regime
        L2's derivation does not reach, and Q1 would need a derivational
        ground other than L2, or none exists.

    WHAT IT WOULD SETTLE ON ITS OWN
        GAP-B only.

**Establishing one bridge does not by itself change `Q1`'s verdict while the
other is open. A bridge may be refuted, and a refutation is a resolution, not
a failure of the task that pursued it.**

---

## 3. What `Q1` did not establish

- **No derivational ground satisfying both parts of `Q1`'s test was found.**
- **`NOT FOUND IN REPOSITORY` was not the outcome either.** The outcome is
  `INCONCLUSIVE`, and the distinction is the point: `NOT FOUND IN REPOSITORY`
  would assert that no location satisfies both parts, while `INCONCLUSIVE`
  records that one location's status could not be settled by reading.
- **The classification does not make either bridge more or less likely to
  hold**, and states nothing about which sign either would take.
- **`H-EXT-01` is unchanged:** `UNESTABLISHED`, `NOT ASSUMED BY RECON-01b`.
- **Neither result blocks `RECON-01b`**, per the constraint carried in
  `PROJ-01`'s own specification: no outcome of `Q1` may be recorded as a
  blocker on `RECON-01b`.

---

## 4. Components 5 and 9, as the reviewed result states them

**Transcribed. Not recomputed, not reclassified.**

### Component 5 — `SPECIFICATION ONLY`

**Unchanged in state from the last landed assessment.** The implementation is
not potentially applicable — recovered provenance, and no pre-registration — so
it does not count; the specification exists.

**What changed is the ground, not the state.** The landed assessment gave two
reasons. **One does not hold as measured:** the ground said the recipes "live
inside target-bearing recovered modules", and the module that DEFINES them was
measured to carry no target. **What survives, and is decisive:** provenance —
`GATES.md:376` names the recovered module regardless of whether it carries a
target — and the absent pre-registration, `GATES.md:748` requiring a
*pre-registered* projection, of which the reviewed result records **none
exists**.

### Component 9 — `SPECIFICATION ONLY`

**Unchanged in state from the last landed assessment.** No implementation
exists; the form of the ratio-error tolerance is specified and the value is
not.

**The determination and its qualification, as the reviewed result attaches
them.** The unmet requirement is a **SPECIFICATION gap** and is **decisively
NOT physical completeness of the projection** — no location connects component
9 to the projection at all. **The qualification:** the gap is in the
*acceptance criterion* rather than in the observable's definition, which is a
third thing the two-way question does not name. `A-EXT-01` did not change
component 9's readiness state, because the gap was never the observable's
definition.

**Neither component is reclassified by this integration**, and what a readiness
register should record from either is registered as an obligation, not decided.

---

## 5. The baseline caveat, re-measured at execution

The reviewed result records that the landed component baseline is the earlier
assessment, `derivations/P2-BETAV-RECON-01_scope-assessment.md:479` and `:483`,
`P2-RECON-01B-B0`'s re-measurement being unintegrated at the time.

**MEASURED AT THIS EXECUTION, not carried:**

    git merge-base --is-ancestor 1093fc04c85e54c3b9fc0dbcca1a2ebc98c69e23 origin/main
        -> NOT an ancestor

`science/recon-01b-b0-scope` is still not an ancestor of `main`. **The caveat
still holds as observed**, and the landed baseline remains the earlier
assessment. The reviewed result also records that the unlanded re-measurement
classified both components `SPECIFICATION ONLY`, so the comparison is
unaffected either way; the fact is recorded so the baseline is not mistaken.

**This is an observation of repository state, not a claim about the
re-measurement's content.** Its integration is registered as `O-3`.

---

## 6. Obligations registered, not discharged

**The integration performs none of these.** They are recorded so that they
carry an owner rather than depending on recall — the failure `P2-RECON-01B-B0`
already demonstrated.

**Each is an obligation and not a finding.**

    O-1   Register consequences of PROJ-01's component determinations.
          What, if anything, a readiness register should record from
          components 5 and 9 is NOT decided here, because deciding it would
          be a classification this integration is forbidden to add.
          REGISTER: none. No register's stated scope admits it. Returned to
          the Researcher; see the report's M5.

    O-2   The bridge tasks. GAP-A and GAP-B, one bounded task each, opened
          only on PI direction. EACH MAY RETURN A REFUTATION, WHICH COMPLETES
          IT.
          REGISTER: none. Returned to the Researcher; see the report's M5.

    O-3   P2-RECON-01B-B0 integration. Measured above as still unlanded.
          REGISTER: none. Returned to the Researcher; see the report's M5.

    O-4   The rule 22 retrospective audit, and with it the unsettled question
          of who may assign a subclass to a result predating the rule.
          REGISTER: docs/GOVERNANCE-DEBT.md, as `G-16`, disposition OPEN.

**`O-4` carries a governance interpretation and `O-1` to `O-3` do not.** Their
registers were selected independently, per obligation, and three of the four
found none. **The executor did not create a location and did not place a
science or workflow obligation in the governance register for convenience.**

---

## 7. What this landing does not establish

It lands two findings and adds nothing to either. No `β_V`, no gate moved,
`P2-PHASE-01` unchanged. `Q1` remains `INCONCLUSIVE`; `H-EXT-01` remains
`UNESTABLISHED`.

**What changes is that the finding, its subclass, and its two `Resolution
path` entries are on `main` together**, where the next task can act on them
without resolving a branch that is not an ancestor.
