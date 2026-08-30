# SPECIFICATION — P2-XI-QM3-DEP-INTEG: transport of the executed Q-M3 dependence check to main

    Task ID        P2-XI-QM3-DEP-INTEG
    Version        v2 — revises v1 (sha256 cb3ecba04b5f0878e1f83f37a4
                   a9b6b941bb802b6672a214ee17f9e25650fbcc) per Reviewer
                   verdict REVISE BEFORE EXECUTION. Both corrections
                   are to M3c's measurement domain; no scope or
                   architecture change:
                   (i) v1's (i) tested for the ABSENCE of the bare
                   tokens `DEPENDENT` and `INDEPENDENT` anywhere in
                   the artifact. That test is unsound twice over —
                   `INDEPENDENT` contains `DEPENDENT` as a substring,
                   and a token occurrence is not a verdict assertion,
                   the artifact legitimately naming both words in
                   vocabulary, counterfactual and not-run text. v2
                   restricts the test to the artifact's own
                   verdict-assertion domain and directs that
                   occurrences outside it be reported, not failed.
                   (ii) v1's (iv) said "every verdict sentence"
                   without defining which sentences those are. v2
                   requires the enumeration rule and the enumerated
                   set to be stated and counted BEFORE the tags are
                   tested.
    Spec file      specs/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
    Author         Researcher (Claude)
    Date           2026-08-25
    Base           main @ 1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    Source         science/xi-qm3-dep-01 @
                   d55b6350a015d124f723d1fceb75b77cdcc112a9
    Branch         science/integrate-xi-qm3-dep-01, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed STALE-SOURCE transport
                   protocol approved and executed as
                   P2-GOVDEBT-REGISTER-GAP-INTEG v2 (sha256
                   78e5ff109ac992adbc25dd5e072c9860dd010a0e9dc14f586a
                   2303620b9fce9b). The source forked at 0c01fc7f…
                   and main has since advanced by the governance-debt
                   entry and its integration, so M3b's main-side sweep
                   is NON-VACUOUS. Unlike that instance, the
                   contributed set here is all-`A`: there is no
                   modified path, so its M3b(d) structural limb does
                   not apply and is absent rather than carried over
                   empty.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is `P2-XI-QM3-DEP-01`, executed on its
early-return path: `M0b` returned `NOT UNIQUELY IDENTIFIED`, the task
recorded `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED` under Rule 22
with a symmetric resolution path it defined and did not walk, and
`M1`–`M3` and `M5` did not run.

**What must survive transport unaltered, and what this task therefore
must not do:**

- **The finding is a gap in landed state, not an answer about the
  Jacobian.** No dependence verdict was returned. This task does not
  restate the finding as `DEPENDENT`, `INDEPENDENT`, or as evidence
  bearing either way, and does not summarise it in any words that
  imply the question was answered.
- **`Q-M3` remains an OPEN ledger row.** Membership is deferred by
  `P2-XI-RULINGS-02` Ruling 1 until evidence returns; a
  constructive-gap finding is not that evidence and this task does
  not dispose the row.
- **The criterion is not discharged, in full or in part.** The
  arriving artifact says so in those terms; this task preserves the
  statement and adds no gloss.
- **The resolution path arrives defined and unwalked.** This task
  does not walk it, order it, prioritise it, or begin either
  determination it names.
- It does not touch `OPEN-AC-1`, the exponent-mapping question, or
  the registered representation-stability inquiry.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 0a. The stale-source fact, recorded because it is load-bearing

Measured by the Researcher on a clean clone, 2026-08-25, and
re-measured by the Executor at M1 and M3b: the source forked at
`0c01fc7f…`, and main has since advanced to `1852d17c…` by the
governance-debt entry and its integration. The Researcher measured
seven main-side changed paths, among them `docs/GOVERNANCE-DEBT.md`
carrying the `G-18` entry, and expects none of them in the source's
contributed set, so that each falls to the main-preservation sweep.
**The Executor re-measures the authoritative set at M3b; the number
here is an expectation, not a precondition, and a different count is
not by itself an abort — the manifest, union and sweep relations of
M3b are what bind.**

## 1a. The contributed manifest

The arriving change set contains four added paths and no modified
path. Any `M`, `D` or `R` status, or any path outside the four, is
A5 — no exception; a manifest change requires a revised,
re-reviewed specification.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-qm2-scope-01,
        origin/science/govdebt-register-gap-01 and
        origin/science/integrate-govdebt-register-gap (refs this task
        must not move). Verify origin/main equals the Base and the
        source tip equals the Source field, both as full-string
        matches. Verify `git merge-base main <source>` equals
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
          derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
              expected 1729136c9579198e118adff74246f42f9cdb1ed164e1dd37030893e6297049ea
          specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
              expected 0fab1fdc58612bfd44971b2d7fef842ce4db4a9ca1ec86fdc926767ce31ebfaa
          reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
              expected a2c462b9cc465252934d2bfb2288c50dc628ccc11854bf44099c05fc72d46837
          reports/2026-08-29T1811Z_xi-qm3-dep-01.md
              expected e5770d21b15efcfb040bf8fbc3254167a1e8bbb814967b4da2371cbb92e8da3e
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
            Any inequality is A5. This protects the `G-18`
            governance-debt entry and the governance-debt task's
            artifacts, all landed on main after the source forked,
            from being walked back.

    M3c Arrival-state verification of the finding.
        From the merge product's arriving artifact, verify and quote
        verbatim, stating for each the normalization applied or that
        none was:
        (i)   `M0b`'s return reads `NOT UNIQUELY IDENTIFIED`; and no
              M3 dependence verdict is ASSERTED AS THIS TASK'S
              RESULT. The test domain is the artifact's own
              verdict-assertion sentences as enumerated at (iv), plus
              any header field that states a result, and NOT the
              artifact's full text. Within that domain, verify that
              no sentence assigns `DEPENDENT` or `INDEPENDENT` to
              this task. **Occurrences outside that domain — in
              vocabulary definitions, counterfactuals, scope text,
              prohibitions, or statements that a verdict was NOT
              returned — are NOT failures.** Record every occurrence
              found outside the domain, with its line and its
              surrounding sentence, as reported context rather than
              as a finding against the artifact. Where a byte-pattern
              search is used it must match a bounded verdict form,
              not the bare token: a bare `DEPENDENT` search is
              invalid here because `INDEPENDENT` contains it.
        (ii)  the Rule 22 classification reads
              `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`, with its
              subclass reasoning and its symmetric resolution path
              present and marked as defined-not-walked;
        (iii) the scope statement is in its early-return wording —
              the task was SCOPED to the landed α and no dependence
              evaluation was performed — and the artifact's statement
              that the criterion is NOT discharged is present;
        (iv)  BEFORE testing any tag: state the enumeration rule by
              which a sentence counts as a verdict-assertion
              sentence, taking it from the artifact's own landed
              structure rather than from judgement — the artifact
              carries an explicit tag marker on such sentences, and
              the rule should be stated in terms of that marker.
              Record the enumeration rule, the enumerated set, and
              its count. THEN verify that each enumerated sentence
              carries both `COND-R` and `COND-M`. If the enumeration
              rule cannot be stated from the artifact's own
              structure, that is A5 — do not enumerate by judgement.
        Any failure is A5.

        NEGATIVE-CHECK DISCIPLINE, applying to (i) within its stated
        domain: an absence is reported only from a probe shown to be
        alive. State the
        patterns searched, and include at least one positive control
        — a string known present in the artifact, found by the same
        method — so that a null result is distinguishable from a dead
        probe. **Structural scans of the artifact must state their
        assumptions about fenced blocks and blockquote prefixes, and
        must operate on bytes; a fence-blind or character-offset scan
        is not a valid substrate.**

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim and the tested tree's SHA,
        T. The arriving task added no tests; the criterion is
        regression, not a count.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-qm3-dep-integ.md recording M1 through
        M4 and nothing later. The report does not state its own
        commit SHA: it names T and records that it is itself the next
        commit on T. Commit it; the tip after this commit is
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
    C3c (M3c) All four arrival-state checks pass, each with its
        quoted text and its stated normalization; (iv)'s enumeration
        rule, enumerated set and count are recorded before its tag
        test; (i)'s test is confined to that enumerated domain plus
        result-stating header fields, its negative result reported
        with its patterns and its positive control, and every
        out-of-domain occurrence recorded as context rather than as
        a failure.
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
        from it; would restate the finding as a dependence verdict or
        as evidence bearing on one; would dispose or annotate the
        `Q-M3` row or the ledger; would describe the criterion as
        discharged in whole or in part; would walk, order or
        prioritise the arriving resolution path; or would touch
        `OPEN-AC-1`, the exponent-mapping question, or the registered
        representation-stability inquiry. STOP; report.
    A5  M3b finds a contributed path or status outside §1a's
        manifest, a both-changed path, a source-unchanged path whose
        product blob differs from the Base's, or a main-unchanged
        contributed path whose product blob differs from the
        source's; or M3c finds any failure, including a negative
        result reported without a live positive control. STOP; report
        the path and all applicable blob ids — for a both-changed
        path: fork, source, Base, AND product. Do not repair the
        merge inside this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4), and the post-push M5
        addendum (branch-only)
    specs/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md and its SHA-bound
        review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-qm3-dep-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets and
        blob-id pairs, and the M3c quotations with their
        normalizations, patterns and positive control; M5 ref values
        in the branch-only addendum; any A that fired recorded
        wherever the stop occurred

END OF SPECIFICATION
