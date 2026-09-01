# SPECIFICATION — P2-XI-RULINGS-03-INTEG: transport of the executed R-1 ruling landing to main

    Task ID        P2-XI-RULINGS-03-INTEG
    Version        v2 — revises v1 (sha256 27ca169de59477228d7d951d05
                   a070fdf54b2f23b856e136d9eca4a3c9f6a167) per Reviewer
                   verdict REVISE BEFORE EXECUTION. v1's M4b required
                   the report to record "M1 through M4 and nothing
                   later", while its Deliverables required the same
                   report to carry M5's post-push ref values — which
                   exist only after the report is committed. Under
                   either M5 route the two demands are unsatisfiable
                   together. v2 separates the two evidence surfaces:
                   the report carries M1–M4, and M5's evidence lives
                   in the execution summary or the optional
                   branch-only addendum. No scope, manifest, merge
                   protocol or acceptance-architecture change.
    Spec file      specs/2026-09-01T0600Z_xi-rulings-03-integ_v2.md
    Author         Researcher (Claude)
    Date           2026-09-01
    Base           main @ 4a99e81ad16322e1152286df0158b648b75d18f3
    Source         science/xi-rulings-03-landing @
                   4eca6408dcd64e0066cdeff775de85d5043bdfed
    Branch         science/integrate-xi-rulings-03, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed transport protocol approved
                   and executed as P2-XI-RULINGS-02-INTEG v1 (sha256
                   3672a9126e3bba40817d186f04346ddb2111301d69f186638f0
                   745c016d6f69c), the variant carrying one MODIFIED
                   path under append-only re-verification. The source
                   DESCENDS from the Base here (merge-base = Base,
                   measured), so M3b's main-side set is expected empty;
                   it is measured regardless.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is the landing of `P2-XI-RULINGS-03`, the R-1
ruling extending the scalar-channel route to the assembled chain: the
re-issued bytes, its document review, the decision-register record,
the `DECISION_LOG.md` index append, both the specification and its
pre-execution review, and the execution report carrying the full
eight-item `M2b` scan.

**What must survive transport unaltered, and what this task therefore
must not do:**

- **Landing an authorization is not exercising it.** `RULING 3`
  authorizes a prescription-definition specification. Such a
  specification exists and has been reviewed. This task does not
  begin, schedule, constrain, sequence, or represent as ready any
  such task. (A4)
- **`P2-XI-QM3-DEP-01`'s determination stands.** `RULING 2` says so
  in its own words. No step describes the Q-M3 subject as now
  uniquely identified, or the constructive gap as closed or narrowed.
  (A4)
- **The exponent mapping is not this ruling's to fix.** The arriving
  `RATIONALE` records that landed authority fixes it at `g = +2c`;
  `RULING 2` records that this ruling does not supply it. **The two
  are compatible and this task flattens neither into the other.**
  (A4)
- **`OPEN-AC-1` stays open, the V/A representations stay deferred
  rather than excluded, and the registered representation-stability
  item is untouched.** (A4)
- The two OPEN ledger rows remain OPEN; no membership is ruled.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 0a. The supersession, and what does NOT travel

The arriving issued bytes are a re-issuance. The superseded document
at sha256
`f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8`
**was never landed**, and the executing task measured that: no commit
in the repository mentions that digest and the canonical path was
absent at its Base. Nothing in the repository is superseded by this
transport. The only trace of the superseded bytes reaching `main` is
the `SUPERSEDES` field inside the re-issued text itself, which
travels as part of those bytes. **This task lands one document and
engages no erratum, clarification, or supersession mechanism.**

## 1a. The contributed manifest, and the one modified path

The arriving change set contains six added paths and one modified
path. The modified path is `DECISION_LOG.md`, whose modification is
the index append the landing performed at its `M4`, and whose
append-only character is re-verified here by prefix relation
(M3b(d)), not assumed from the status letter. No other modified path
is authorized: any second `M`, or any `D`/`R` status, is A5.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-qm2-scope-01,
        origin/science/xi-qm3-dep-01 and
        origin/science/integrate-xi-qm2-scope-01 (refs this task must
        not move). Verify origin/main equals the Base and the source
        tip equals the Source field, both as full-string matches.
        Verify `git merge-base main <source>` equals the Base as a
        full-string match.

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
          DECISION_LOG.md
              expected d248e849007b0299c8ce92951d27ed500834f1ae49827a49637bf89ef8495d41
          decisions/P2-XI-RULINGS-03.issued.md
              expected 1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
              and git blob id 0b331afb6f21f6591a0c3934fc8916bda742d8de
          decisions/2026-08-31-xi-rulings-03.md
              expected e1c6bb959c7091f7a5af9d23a41ecdda9da52fc838b7df341c540151ecf6c1aa
          reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
              expected dc538e3a69aef2f205a74f7c51bb10345ea4dbe66d292af66b3712aba00e5359
          specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
              expected 0b6f48d73fdd4a1761f704d9801f338918a00391d18b6ccf472df5b79dd179d5
          reviews/chatgpt/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
              expected 26ba2ccbe0ad9afd6e5dbdcb49074bfca14a2674a7c556d442caf548148b31ca
          reports/2026-09-01T0135Z_xi-rulings-03-landing.md
              expected b934a857cc800891affd0b9a26a6212737d4621af4cddec9e7cf4c6e582c5e8c
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-09-01; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected equal to
        the Base).
        (a) Contributed path set. Measure
            `git diff --name-status FORK..<source>`. Record verbatim.
            Pre-registered expectation: the six added M3 paths with
            status A, plus DECISION_LOG.md with status M — seven
            entries, nothing else. Any other path, or any status
            outside {A for the six, M for DECISION_LOG.md}, is A5 —
            no exception; a manifest change requires a revised,
            re-reviewed specification.
        (b) Union classification. Measure P_source (FORK..source) and
            P_main (FORK..Base); record both verbatim. Classify each
            path of P_union = P_source ∪ P_main into exactly one of
            (1,0) source-only → product blob equals the source's;
            (0,1) main-only → product blob equals the Base's;
            (1,1) both-changed → A5;
            (0,0) does not occur within P_union.
            P_overlap ≡ the (1,1) class. Pre-registered expectation:
            P_main is empty because FORK = Base, hence P_overlap is
            empty — recorded as a measured comparison over the
            classified union, not inferred from the equality.
        (c) Main-preservation sweep. For each path in P_main not in
            P_source, compare the merge product's blob id against the
            Base's, pairwise. Expected vacuous; record it as
            measured, not skipped.
        (d) Append-only re-verification of the one modified path.
            Verify the Base's DECISION_LOG.md bytes are an exact
            byte-prefix of the merge product's, and record the two
            lengths in bytes. Failure is A5.

    M3c Arrival-state verification of the ruling.
        From the merge product, verify and quote verbatim, stating
        for each the normalization applied or that none was:
        (i)   the issued file's `SUPERSEDES` field is present and
              names the superseded digest, and the repository
              contains no other landed occurrence of that digest
              outside this arriving change set — reported with the
              patterns searched and a live positive control, so a
              null result is distinguishable from a dead probe;
        (ii)  the arriving `RATIONALE` names the channel and the
              decoupling prescription as the two elements not fixed
              by landed text, states that the exponent mapping is not
              among them, and cites `g = +2c` at
              `DECISION_LOG.md:1258-1262`; and this agrees with
              `P2-XI-QM3-DEP-01`'s determination table in the merge
              product;
        (iii) `RULING 2`'s sentence that the determination stands is
              present, and `RULING 3`'s authorization is present with
              its define-not-evaluate limits;
        (iv)  the register record's quotations of the issued file are
              byte-identical to the corresponding spans of the issued
              file as it stands in the merge product.
        Any failure is A5.

        MEASUREMENT SUBSTRATE, applying to all of M3c: probes are
        constructed from the file's bytes, not from remembered or
        rendered markup, and operate on bytes. Every structural scan
        states its assumptions about fenced blocks, blockquote
        prefixes and emphasis wrapping. A probe that fails against
        its own assumption is a defect of the probe: re-measure and
        record the correction; do not declare A5 on a false failure.

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim and the tested tree's SHA,
        T.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-rulings-03-integ.md recording M1
        through M4 and nothing later. The report does not state its
        own commit SHA: it names T and records that it is itself the
        next commit on T. Commit it; the tip after this commit is
        H_integ, measured externally. Verify by diff that H_integ
        differs from T ONLY by the report artifact.

    M5  Push, and post-push evidence.
        Push the integration branch at H_integ. Advance main by
        fast-forward to H_integ and push. Then record the full SHAs
        of origin/main, the source branch, and the three refs of M1,
        and verify all but main equal their M1 values. Two routes are
        available for this evidence and the Executor states which was
        taken: EXECUTION SUMMARY ONLY, leaving the branch tip at
        H_integ; or BRANCH-ONLY ADDENDUM, one further commit on the
        integration branch changing exactly one path, the addendum
        record, touching nothing that arrived from M2 or M4b.
        **origin/main remains H_integ under either route**, and
        M4b's report-only diff is bound to H_integ and unaffected.

    MEASUREMENT UNITS, applying throughout: every offset, length,
    prefix and byte-identity comparison is performed and reported in
    BYTES, with the normalization stated or stated to be none. An
    identifier — a commit SHA, a digest, a line number — is used only
    at a value this task has measured and printed; an abbreviation is
    never completed.

## 3. Acceptance criteria

    C1  (M1) origin/main equals the Base; the merge-base equals the
        Base as a full-string match; the source tip equals the Source
        field.
    C2  (M1b, M2) M_merge has exactly two parents: the M1b tip and
        the source tip; the M1b tip descends from the base by exactly
        two commits (the spec, then its review); the spec's sha256
        equals the digest the review declares, as recorded at M1b.
    C3  (M3) Every digest equals its expected value, as full-string
        matches recorded in the report.
    C3b (M3b) The contributed set equals the seven-entry manifest
        with its stated statuses; the union classification assigns
        each P_union path to exactly one class with its blob rule
        satisfied; the measured P_overlap is empty; the
        main-preservation sweep is recorded as measured; and the
        DECISION_LOG.md prefix relation holds with both lengths
        recorded in bytes.
    C3c (M3c) All four arrival-state checks pass, each with its
        quoted text and its stated normalization; (i)'s null result
        is reported with its patterns and its positive control.
    C4  (M4) No test fails on T that passes at the base.
    C5  (M4b, M5) H_integ differs from T only by the report artifact,
        verified by diff; the report does not assert its own SHA;
        origin/main equals H_integ; the source branch and the three
        M1 refs are unmoved; the route taken at M5 is stated, and
        under either route origin/main remains H_integ.

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
        from it; would begin, schedule, constrain, sequence or
        represent as ready the prescription-definition task RULING 3
        authorizes; would describe the Q-M3 subject as uniquely
        identified or its constructive gap as closed or narrowed;
        would flatten "not fixed by this ruling" into "unfixed in the
        repository" or the converse; would close `OPEN-AC-1`, exclude
        the V/A representations, or touch the registered
        representation-stability item; or would dispose either OPEN
        ledger row. STOP; report.
    A5  M3b finds a contributed path or status outside §1a's
        manifest, a both-changed path, a source-unchanged path whose
        product blob differs from the Base's, a main-unchanged
        contributed path whose product blob differs from the
        source's, or a failure of the DECISION_LOG.md prefix
        relation; or M3c finds any failure, including a null result
        reported without a live positive control. STOP; report the
        path and all applicable blob ids — for a both-changed path:
        fork, source, Base, AND product. Do not repair the merge
        inside this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4, yielding H_integ), and — on
        the BRANCH-ONLY ADDENDUM route only — the M5 addendum commit
    specs/2026-09-01T0600Z_xi-rulings-03-integ_v2.md and its
        SHA-bound review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-rulings-03-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets,
        blob-id pairs and byte lengths, and the M3c quotations with
        their normalizations, patterns and positive control. **It
        records nothing later than M4**, M5's evidence not existing
        when it is written.
    M5's post-push ref values and the route taken — recorded in the
        execution summary, or in the optional branch-only addendum
        commit, according to M5. Not in the M4b report.
    Any A that fired — recorded wherever the stop occurred

END OF SPECIFICATION
