# SPECIFICATION — P2-XI-QM2-SCOPE-INTEG: transport of the executed Q-M2 scope assessment to main

    Task ID        P2-XI-QM2-SCOPE-INTEG
    Version        v2 — revises v1 (sha256 3eb76e9e27fc313eb219e533d2
                   c257620b74d4f85fd398e64607302374251464), which
                   STOPPED at A1 before any write. v1's Source field
                   named b133e6aa07d6ea7b7c85f6e3e17cbb0f78ed12f0, an
                   object this repository does not hold: the Researcher
                   had measured the source tip only through the
                   abbreviation b133e6aa and completed the remaining
                   32 hex characters without measuring them. The
                   Executor measured the tip, found the disagreement,
                   and correctly declined to substitute the measured
                   value and proceed — a Source field is the reviewed
                   authority for which commit is transported, and
                   replacing it at execution time would execute an
                   unreviewed specification.
                   THE ONLY CHANGE IN v2 is the Source field, now
                   b133e6aab8a9f03a2c76345d5bd818898c6a1ab3, measured
                   by `git rev-parse origin/science/xi-qm2-scope-01`
                   and confirmed the unique object carrying that
                   abbreviation by `git rev-parse --disambiguate`.
                   Everything else is unchanged, and v1's own
                   measurements at the actual tip — merge-base
                   0c01fc7f…, the four-path all-`A` manifest, and all
                   four M3 digests — verified before the stop and are
                   re-measured here as before, not inherited.
    Spec file      specs/2026-08-25T0600Z_xi-qm2-scope-integ_v2.md
    Author         Researcher (Claude)
    Date           2026-08-25
    Base           main @ 08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    Source         science/xi-qm2-scope-01 @
                   b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    Branch         science/integrate-xi-qm2-scope-01, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed STALE-SOURCE transport
                   protocol approved and executed as
                   P2-XI-QM3-DEP-INTEG v2 (sha256
                   f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfba
                   e9f613ab904df0), the all-`A` variant: the
                   contributed set here has no modified path either,
                   so that protocol's modified-path structural limb is
                   absent rather than carried over empty. The source
                   forked at 0c01fc7f… and main has since advanced by
                   the governance-debt entry, the Q-M3 check, and both
                   of their integrations, so M3b's main-side sweep is
                   NON-VACUOUS.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is `P2-XI-QM2-SCOPE-01`: nine inputs enumerated
for a bounding computation of the condensate scalar's own fluctuation
loop, each carrying exactly one of the four outcomes, with five
inputs returned to the PI.

**What must survive transport unaltered, and what this task therefore
must not do:**

- **Scope is not evidence about membership.** The artifact answers
  what a bounding computation would require, not whether the loop
  enters the ledger. `Q-M2` remains an OPEN ledger row; this task
  does not dispose it, and does not present the assessment as the
  evidence `P2-XI-RULINGS-02` Ruling 1 awaits.
- **No outcome is restated, upgraded, or resolved.** In particular
  `LANDED — NOT DETERMINABLE` is a landed STATUS and not a value in
  hand (the artifact's own `COND-S`), and
  `ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE` is a
  classification and not an absence of one. This task repeats
  neither in other words.
- **The five returns arrive unanswered and unranked.** This task does
  not answer, recommend on, order, or prioritise `I-1`, `I-3`,
  `I-5`, `I-8`, or the routed `I-7`.
- **The bounding computation is not authorized by anything here.**
  Ruling 3 reserves it to a separate later task; this transport does
  not begin, design, scope, or schedule it.
- It does not touch `DET-01`, `OPEN-AC-2`, `Q-M1`, the truncation
  order that `I-7` turns on, or the registered
  representation-stability inquiry.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 0a. The stale-source fact, recorded because it is load-bearing

Measured by the Researcher on a clean clone, 2026-08-25, and
re-measured by the Executor at M1 and M3b: the source forked at
`0c01fc7f…` and main has since advanced to `08b46fb4…`. The
Researcher measured fourteen main-side changed paths — the
governance-debt entry `G-18` and its task's artifacts, and the Q-M3
check's artifacts and its integration's report — and expects none of
them in the source's contributed set, so that each falls to the
main-preservation sweep. **The Executor re-measures the authoritative
set at M3b; the number here is an expectation, not a precondition,
and a different count is not by itself an abort — the manifest, union
and sweep relations of M3b are what bind.**

## 1a. The contributed manifest

The arriving change set contains four added paths and no modified
path. Any `M`, `D` or `R` status, or any path outside the four, is
A5 — no exception; a manifest change requires a revised,
re-reviewed specification.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-qm3-dep-01,
        origin/science/integrate-xi-qm3-dep-01 and
        origin/science/govdebt-register-gap-01 (refs this task must
        not move). Verify origin/main equals the Base and the source
        tip equals the Source field, both as full-string matches.
        Verify `git merge-base main <source>` equals
        0c01fc7f26e91dd84b032dccde0feac61f61d8ea — the source does
        NOT descend from the Base — recording the output.

    M1b Pre-execution provenance commits, before the merge.
        Cut the integration branch from the base. Commit the exact
        reviewed specification, then its SHA-bound pre-execution
        review, in that order (spec → review). Before the spec
        commit, verify the spec file's sha256 equals the digest the
        review declares itself bound to, recording both strings. The
        review file has no pre-committed hash; record its sha256 at
        commit as its first recorded digest, provenance
        transmitted-in-session. Record the M1b tip SHA. Nothing else
        is committed between them.

    M2  Merge construction.
        On the integration branch at the M1b tip, merge the source
        tip with `--no-ff`. Record the merge commit SHA (M_merge) and
        its two parent SHAs. A conflict is A2.

    M3  Arriving-blob verification, from the merge product.
        sha256sum over each of, recording every digest in full:
          derivations/P2-XI-QM2-SCOPE-01_condensate-loop-input-scope.md
              expected 3ce0215db7ed61103b3074ae23567ca77760f07af586c052aef2e3d2095110ae
          specs/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
              expected 680248e8deada3e1d77df13ee1f5f8899ddb3084e76db71f4c052ce7ff07fb87
          reviews/chatgpt/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
              expected f22397a0d5d52fdca3ff828e113e66b107f64c245f2af772b3d3bb849bf566cb
          reports/2026-08-29T1825Z_xi-qm2-scope-01.md
              expected 98d6bbc9a8b7c4b83b15836b1c114a8a24afae2e8c1802f6c45b8d5ddaa49830
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-08-25; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected
        0c01fc7f…).
        (a) Contributed path set. Measure
            `git diff --name-status FORK..<source>`. Record verbatim.
            Pre-registered expectation: exactly the four M3 paths,
            each with status A, nothing else. Any other path or any
            other status is A5 per §1a.
        (b) Union classification. Measure P_source (FORK..source) and
            P_main (FORK..Base); record both verbatim. Classify each
            path of P_union = P_source ∪ P_main into exactly one of
            (1,0) source-only → product blob equals the source's;
            (0,1) main-only → product blob equals the Base's;
            (1,1) both-changed → A5;
            (0,0) does not occur within P_union.
            P_overlap ≡ the (1,1) class. Pre-registered expectation:
            P_overlap is empty — recorded as a measured comparison
            over the classified union, not inferred from fork
            distance.
        (c) Main-preservation sweep, NON-VACUOUS here. For each path
            in P_main not in P_source, compare the merge product's
            blob id against the Base's, pairwise; record each pair.
            Any inequality is A5. This protects the `G-18` entry, the
            Q-M3 check's artifact and its constructive-gap finding,
            and both preceding integrations' records, all landed on
            main after the source forked.

    M3c Arrival-state verification of the classification.
        Perform (i) FIRST, and derive the domains of (ii) and (iii)
        from it.
        (i)   ENUMERATION. State the rule by which a passage counts
              as an input's outcome declaration, taking it from the
              artifact's own landed structure rather than from
              judgement — the artifact carries an explicit outcome
              marker on each. Record the rule, the enumerated set,
              and its count, BEFORE testing anything about the
              outcomes. If the rule cannot be stated from the
              artifact's own structure, that is A5 — do not
              enumerate by judgement.
        (ii)  ONE OUTCOME EACH. Within the enumerated set, verify
              that every input carries exactly one outcome, and that
              every outcome value is drawn from the four-outcome
              vocabulary the arriving specification fixes. Record the
              per-input assignment as a table. An input with none, or
              with two, is A5.
        (iii) THE PI-FACING RETURNS. Verify the artifact's own list
              of PI-facing returns is present and contains every
              input whose enumerated outcome is
              `REQUIRING A PI RULING` or
              `ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE`,
              measured from (i)'s enumeration rather than from the
              list itself, and that the two outcomes remain
              distinguishable in it.
        (iv)  DISCIPLINE STATEMENTS. Verify the artifact's five
              discipline statements are present: that it proposes
              nothing; that a question being listed is not evidence
              about its answer; `COND-D`; `COND-E`; and `COND-S`.
              Quote each.
        Any failure is A5. State for each check the normalization
        applied or that none was.

        MEASUREMENT SUBSTRATE, applying to all of M3c: probes are
        constructed from the file's bytes, not from remembered or
        rendered markup, and operate on bytes. Every structural scan
        states its assumptions about fenced blocks, blockquote
        prefixes and emphasis wrapping. A negative result is reported
        only alongside a live positive control. **A probe that fails
        against its own assumption is a defect of the probe: re-measure
        and record the correction; do not declare A5 on a false
        failure.**

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim and the tested tree's SHA,
        T. The arriving task added no tests; the criterion is
        regression, not a count.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-qm2-scope-integ.md recording M1
        through M4 and nothing later. The report does not state its
        own commit SHA: it names T and records that it is itself the
        next commit on T. Commit it; the tip after this commit is
        H_integ, measured externally.

    M5  Push, then post-push ref audit.
        Verify by diff that H_integ differs from T only by the report
        artifact. Push the integration branch. Advance main by
        fast-forward to H_integ and push. Then record the full SHAs
        of origin/main, the source branch, and the three refs of M1,
        and verify all but main equal their M1 values. M5's output is
        recorded in an addendum commit on the integration branch
        ONLY; origin/main remains H_integ.

    MEASUREMENT UNITS, applying throughout: every offset, length,
    prefix and byte-identity comparison is performed and reported in
    BYTES, and every byte-identity claim states the normalization
    applied or states that none was.

## 3. Acceptance criteria

    C1  (M1) origin/main equals the Base; the merge-base equals
        0c01fc7f… as a full-string match; the source tip equals the
        Source field.
    C2  (M1b, M2) M_merge has exactly two parents: the M1b tip and
        the source tip; the M1b tip descends from the base by exactly
        two commits (the spec, then its review); the spec's sha256
        equals the digest the review declares, as recorded at M1b.
    C3  (M3) Every digest equals its expected value, as full-string
        matches recorded in the report.
    C3b (M3b) The contributed set equals the four-path all-`A`
        manifest; the union classification assigns each P_union path
        to exactly one class with its blob rule satisfied; the
        measured P_overlap is empty; and the main-preservation sweep
        records product blob equal to Base blob for each swept path,
        pairwise.
    C3c (M3c) (i)'s enumeration rule, enumerated set and count are
        recorded before any outcome is tested; (ii)'s per-input table
        shows exactly one outcome per input, each from the fixed
        vocabulary; (iii)'s PI-facing list matches the enumeration
        and keeps the two outcomes distinguishable; (iv)'s five
        statements are quoted; and each check states its
        normalization.
    C4  (M4) No test fails on T that passes at the base.
    C5  (M4b, M5) H_integ differs from T only by the report artifact,
        verified by diff; the report does not assert its own SHA;
        origin/main equals H_integ; the source branch and the three
        M1 refs are unmoved; the M5 addendum is on the integration
        branch only and origin/main remains H_integ.

## 4. Abort conditions

    A1  Any M1 value disagrees with this spec's Base, Source, or
        stated merge-base relation. STOP before any write; report the
        measured values. (A moved main is stale-base handling per
        BRANCHING_POLICY.md, not an error to repair silently.)
    A2  The merge is not conflict-free, or M3 finds any digest
        mismatch in the merge product. STOP; report; do not resolve
        content inside this task.
    A3  Advancing main would not be a fast-forward at push time.
        STOP; report; stale-base handling applies.
    A4  Any step would modify the source branch or any file arriving
        from it; would restate, upgrade, resolve, or gloss any
        outcome; would treat `LANDED — NOT DETERMINABLE` as a value
        obtained or `ROUTED TO PI` as an unclassified input; would
        answer, recommend on, order or prioritise any PI-facing
        return; would dispose or annotate the `Q-M2` row or the
        ledger; would present the assessment as membership evidence;
        or would begin, design, scope or schedule the bounding
        computation. STOP; report.
    A5  M3b finds a contributed path or status outside §1a's
        manifest, a both-changed path, a source-unchanged path whose
        product blob differs from the Base's, or a main-unchanged
        contributed path whose product blob differs from the
        source's; or M3c finds any failure, including an enumeration
        rule that cannot be stated from the artifact's structure, an
        input with none or two outcomes, or a negative result
        reported without a live positive control. STOP; report the
        path and all applicable blob ids — for a both-changed path:
        fork, source, Base, AND product. Do not repair the merge
        inside this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4), and the post-push M5
        addendum (branch-only)
    specs/2026-08-25T0600Z_xi-qm2-scope-integ_v2.md and its SHA-bound
        review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-qm2-scope-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets and
        blob-id pairs, and M3c's enumeration rule, per-input table,
        PI-facing list and quoted statements with their
        normalizations; M5 ref values in the branch-only addendum;
        any A that fired recorded wherever the stop occurred

END OF SPECIFICATION
