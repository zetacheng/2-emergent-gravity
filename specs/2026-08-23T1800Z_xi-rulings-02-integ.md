# SPECIFICATION — P2-XI-RULINGS-02-INTEG: transport of the executed ruling landing to main

    Task ID        P2-XI-RULINGS-02-INTEG
    Version        v1
    Spec file      specs/2026-08-23T1800Z_xi-rulings-02-integ.md
    Author         Researcher (Claude)
    Date           2026-08-23
    Base           main @ 9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Source         science/xi-rulings-02-landing @
                   6c7a1f7238273214f87fe0d9b76111a7e5f45a6c
    Branch         science/integrate-xi-rulings-02, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed transport protocol approved
                   and executed as P2-XI-B0A-INTEG v4 (sha256
                   8feca4de9910fefc7ef0b2fdb40de23023af15fa71bf1b2b5f
                   b7c57c1dc7e5f5). Differences, all measured rather
                   than assumed: the source DESCENDS from the Base
                   here (merge-base = Base), so the fork-aware audit
                   of M3b is retained but its main-side set is
                   expected empty; and the contributed manifest
                   includes one MODIFIED path (DECISION_LOG.md,
                   append-only), which that instance's all-`A` rule
                   would have rejected — §1a states the rule for it.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is `P2-XI-RULINGS-02-LANDING-01`: the issued PI
ruling `P2-XI-RULINGS-02` landed byte-exact, its document review, the
decision-register record, the `DECISION_LOG.md` index append, and the
execution report carrying the full `M2b` correspondence scan.
Researcher verification from a clean clone confirmed every digest,
the commit order, the subject-pin match, the chronology fact's
byte-identity across its two required locations, and the append-only
prefix relation.

- It does not act on either task the arriving ruling authorizes (the
  Q-M3 dependence check; the Q-M2 scope assessment). Landing the
  authority is not exercising it.
- It does not integrate `science/xi-ledger-01`, and does not alter
  the subject pin the arriving register record states.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 1a. The contributed manifest, and the one modified path

The arriving change set contains six added paths and one modified
path. The modified path is `DECISION_LOG.md`, whose modification is
the append the landing task's `M4` performed and whose append-only
character is re-verified here by prefix relation (M3b(d)), not
assumed from the status letter. No other modified path is authorized:
any second `M`, or any `D`/`R` status, is A5.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-ledger-01 (which this task must not move,
        and whose value the arriving record pins). Verify origin/main
        equals the Base; verify `git merge-base main <source>` equals
        the Base as a full-string match (the source descends from
        the Base); verify the source tip equals the Source field in
        full.

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
          decisions/P2-XI-RULINGS-02.issued.md
              expected ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
              and git blob id 72a6b24c9289efde8a096e4e591ff01728323473
          decisions/2026-08-23-xi-rulings-02.md
              expected cf39e8999dd5d8c1c284cd3ef0c37bcc499959f358f02f4ad189e5d5b5b7d758
          reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
              expected d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49
          specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
              expected c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da4750f926a14cc5
          reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
              expected fafca91a0cfdc9a85e888509004958d0427ad537c073faf11b8b3c130fc274df
          reports/2026-08-23T1540Z_xi-rulings-02-landing.md
              expected e7c0cece291f22cc761836f404769c147c2dc6ecdda4b42b762fb814f2a945e3
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-08-23; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected equal to
        the Base).
        (a) Contributed path set. Measure
            `git diff --name-status FORK..<source>`. Record verbatim.
            Pre-registered expectation: the six M3 paths with status
            A, plus DECISION_LOG.md with status M — seven entries,
            nothing else. Any other path, or any status outside
            {A for the six, M for DECISION_LOG.md}, is A5.
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
            Base's, pairwise. Expected vacuous; record it as measured.
        (d) Append-only re-verification of the one modified path.
            Verify the Base's DECISION_LOG.md bytes are an exact
            byte-prefix of the merge product's. Failure is A5.

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim, and the SHA of the tree
        the integration-side run used.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-rulings-02-integ.md recording M1
        through M4 (M5 is post-push and excluded by construction).
        Commit it. The tip after this commit is H_integ; record its
        SHA. No suite re-run is required: H_integ differs from the
        tested tree only by the report artifact. The report states
        this.

    M5  Push, then post-push ref audit.
        Push the integration branch. Advance main by fast-forward to
        H_integ and push. Then record the full SHAs of origin/main,
        the source branch, and origin/science/xi-ledger-01, and
        verify the latter two equal their M1 values. M5's output is
        recorded in an addendum commit on the integration branch
        ONLY; origin/main remains H_integ.

## 3. Acceptance criteria

    C1  (M1) origin/main equals the Base; the merge-base equals the
        Base as a full-string match; the source tip equals the
        Source field.
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
        DECISION_LOG.md prefix relation holds.
    C4  (M4) No test fails on the post-merge integration tree that
        passes at the base; and H_integ differs from that tested
        tree only by the report artifact (M4b), verified by diff.
    C5  (M5) origin/main equals H_integ; the source branch and
        science/xi-ledger-01 are unmoved from their M1 values; the
        M5 addendum commit is on the integration branch only and
        origin/main remains H_integ after it.

## 4. Abort conditions

    A1  Any M1 value disagrees with this spec's Base, Source, or
        stated merge-base relation. STOP before any write; report
        the measured values. (A moved main is stale-base handling
        per BRANCHING_POLICY.md, not an error to repair silently.)
    A2  The merge is not conflict-free, or M3 finds any digest
        mismatch in the merge product. STOP; report; do not resolve
        content inside this task.
    A3  Advancing main would not be a fast-forward at push time.
        STOP; report; stale-base handling applies.
    A4  Any step would modify the source branch, any file arriving
        from it, or begin/schedule/constrain either task the
        arriving ruling authorizes. STOP; report.
    A5  M3b finds: a contributed path or status outside §1a's
        manifest, with no exception; a path in the both-changed
        class; a source-unchanged path whose product blob differs
        from the Base's; a main-unchanged contributed path whose
        product blob differs from the source's; or a failure of the
        DECISION_LOG.md prefix relation. STOP; report the path and
        all applicable blob ids — for a both-changed path: fork,
        source, Base, AND product. Do not repair the merge inside
        this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4), and the post-push M5
        addendum (branch-only)
    specs/2026-08-23T1800Z_xi-rulings-02-integ.md and its SHA-bound
        review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-rulings-02-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets and
        blob-id pairs verbatim; M5 ref values in the branch-only
        addendum; any A that fired recorded wherever the stop
        occurred

END OF SPECIFICATION
