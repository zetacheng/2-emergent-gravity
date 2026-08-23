# SPECIFICATION — P2-XI-LEDGER-01-INTEG: transport of the executed conditional ledger, with its count addendum, to main

    Task ID        P2-XI-LEDGER-01-INTEG
    Version        v1
    Spec file      specs/2026-08-23T2100Z_xi-ledger-01-integ.md
    Author         Researcher (Claude)
    Date           2026-08-23
    Base           main @ 6c1af3cace259663a288354b1725bdd923d3b1fc
    Source         science/xi-ledger-01 @
                   0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    Branch         science/integrate-xi-ledger-01, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed stale-source transport
                   protocol approved and executed as P2-XI-B0A-INTEG
                   v4 (sha256 8feca4de9910fefc7ef0b2fdb40de23023af15f
                   a71bf1b2b5fb7c57c1dc7e5f5). The source predates the
                   Base here, so the full fork-aware audit applies and
                   its main-side sweep is non-vacuous.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is `P2-XI-LEDGER-01` — the conditional analytic
ξ ledger, Phase 1 — together with the branch-only count addendum
executed as `P2-XI-LEDGER-01-COUNT-ADDENDUM v2`.

- **The two OPEN ledger rows arrive OPEN.** `Q-M2` (the condensate
  scalar's own fluctuation loop) and `Q-M3` (the HS Jacobian /
  normalization term) carry no value and no membership disposition.
  `P2-XI-RULINGS-02`, already landed on the Base, defers membership
  and authorizes two tasks; this integration does not perform,
  schedule, or constrain either, and does not mark either row
  disposed.
- **No verdict travels.** The arriving artifact is a conditional
  assembly labelled `ξ(G) | COND-1..4` throughout. Nothing here
  relabels it, strips a condition, or draws a survival conclusion
  from it.
- No gate moves; `P2-PHASE-01` and `SI-2` are untouched.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 0a. Pin versus source — the obligation this task inherits

`P2-XI-RULINGS-02` was issued on the ledger state pinned as
`science/xi-ledger-01 @ 8f9edfead214b5bb3337924c18c5d241274e97c3`,
and that pin is quoted in the landed register record
`decisions/2026-08-23-xi-rulings-02.md`. The count addendum
subsequently advanced the branch. Therefore, stated here and to be
carried verbatim into this task's report and integration commit
message:

> The source of this integration is the pin plus the count addendum:
> `8f9edfead214b5bb3337924c18c5d241274e97c3` is the ledger state
> `P2-XI-RULINGS-02` was issued on;
> `0101d65ea581b0f6b08f1b0ca62969a51a7a16d1` is that state plus the
> branch-only addendum and its provenance commits. The
> addendum-bearing tip is NOT the state the ruling was issued on.

The obligation originates in the addendum task's `§10a` and in this
specification's own Base state; this task discharges it by recording,
not by editing anything. `M3c` measures that the pin's substantive
content survives to the merge product unchanged.

## 1. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/integrate-xi-rulings-02 (the preceding task's
        branch, which this task must not move). Verify origin/main
        equals the Base and the source tip equals the Source field,
        both as full-string matches. Verify
        `git merge-base main <source>` equals
        9eefe4c85c646b96ce334426598bc0e405f6e3d5 — the source does
        NOT descend from the Base — recording the output.
        Verify the pin 8f9edfead214b5bb3337924c18c5d241274e97c3 is
        an ancestor of the source tip
        (`git merge-base --is-ancestor`), recording the exit status.

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
          derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
              expected aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454
          scripts/xi_ledger.py
              expected 97571fa0ef7bee8dbcdf06cb7117fa04eda0d6b2606322af08f0fe73879a695c
          tests/test_p2_xi_ledger.py
              expected c0c6a6d26f3138191487564505043eeb0d4b02a45aae4ea241ee4e66a472a31b
          specs/2026-08-23T0600Z_xi-ledger-01_v3.md
              expected b1120556eaf6d5c9e77048efbd84ba113b58ad0d932991ba54c8d9b64f6dbe17
          reviews/chatgpt/2026-08-23T0600Z_xi-ledger-01_v3.md
              expected de3556a97a51c92e9e77e4561ba4ce9d3933d8d439ee7831ce56997e265b13a2
          reports/2026-08-23T0434Z_xi-ledger-01.md
              expected 1b234b5e14b137406ba336c5ba97427d562ecdb074f49c1d7d778f5e2676b049
          specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
              expected 7a924f143c82dfaac8a971e6f4ead5ca94c2313cdd8f449510c746a4ead32416
          reviews/chatgpt/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
              expected 6c9648a7f01e89d00cc429eb6c9ae5baf38cf6360d386ce4415a019d877f67ee
          reports/2026-08-23T1909Z_xi-ledger-01-count-addendum.md
              expected 481ce13a46697ef72ab111cc17977fb9e7e4cd81296df155bdb90e9be83456fd
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-08-23; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected
        9eefe4c8…).
        (a) Contributed path set. Measure
            `git diff --name-status FORK..<source>`. Record verbatim.
            Pre-registered expectation: exactly the nine M3 paths,
            each with status A. Any path outside the nine, or any
            status other than A, is A5 — no exception; a manifest
            change requires a revised, re-reviewed specification.
        (b) Union classification. Measure P_source (FORK..source) and
            P_main (FORK..Base); record both verbatim. Classify each
            path of P_union = P_source ∪ P_main into exactly one of
            (1,0) source-only → product blob equals the source's;
            (0,1) main-only → product blob equals the Base's;
            (1,1) both-changed → A5;
            (0,0) does not occur within P_union.
            P_overlap ≡ the (1,1) class. Pre-registered expectation:
            P_overlap is empty, recorded as a measured comparison
            over the classified union, not inferred from fork
            distance.
        (c) Main-preservation sweep. For each path in P_main not in
            P_source, compare the merge product's blob id against the
            Base's, pairwise; record each pair. Any inequality is A5.
            This is the silent-revert check, and it is non-vacuous
            here: the source predates the landing and integration of
            `P2-XI-RULINGS-02`, so the sweep is what protects the
            landed ruling, its register record, its document review,
            `DECISION_LOG.md`, and the preceding task artifacts from
            being walked back by a pre-ruling source.

    M3c Pin-content survival, from the merge product.
        Verify that the ledger artifact and the ledger execution
        report arrive with the pin's substantive content intact:
        (i)  derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
             in the merge product is byte-identical to the same path
             at the pin (`git show <pin>:<path>`), recording both
             digests — the addendum touched only the execution
             report, so the ledger artifact must be unchanged;
        (ii) the ledger execution report at the pin (sha256
             93ed8caf14d23ddc35d224d4bcc9bcf7b1a3b7c082535be78a6fd4c4841e8959)
             is an exact byte-prefix of the same path in the merge
             product, evidencing that the addendum appended and
             rewrote nothing;
        (iii) the two OPEN rows are present in the merge product's
             ledger artifact with statuses OPEN(Q-M2) and
             OPEN(Q-M3) and em-dash value cells, quoted verbatim.
        Any failure is A5.

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim, and the SHA of the tree
        the integration-side run used. The arriving tests are
        expected to raise the count; the criterion is regression,
        not a count.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-ledger-01-integ.md recording M1
        through M4 (M5 is post-push and excluded by construction),
        including §0a's pin-versus-source paragraph verbatim. The
        report does not state its own commit SHA; it names the tip
        it is committed onto and records that it is itself the next
        commit. Commit it; the tip after this commit is H_integ;
        record its SHA. No suite re-run is required: H_integ differs
        from the tested tree only by the report artifact, verified
        by diff. The report states this.

    M5  Push, then post-push ref audit.
        Push the integration branch. Advance main by fast-forward to
        H_integ and push. Then record the full SHAs of origin/main,
        the source branch, and origin/science/integrate-xi-rulings-02,
        and verify the latter two equal their M1 values. M5's output
        is recorded in an addendum commit on the integration branch
        ONLY; origin/main remains H_integ.

## 2. Acceptance criteria

    C1  (M1) origin/main equals the Base; the merge-base equals
        9eefe4c8… as a full-string match; the source tip equals the
        Source field; the pin is an ancestor of the source tip.
    C2  (M1b, M2) M_merge has exactly two parents: the M1b tip and
        the source tip; the M1b tip descends from the base by exactly
        two commits (the spec, then its review); the spec's sha256
        equals the digest the review declares, as recorded at M1b.
    C3  (M3) Every digest equals its expected value, as full-string
        matches recorded in the report.
    C3b (M3b) The contributed set equals the nine-path manifest with
        status A throughout; the union classification assigns each
        P_union path to exactly one class with its blob rule
        satisfied; the measured P_overlap is empty; and the
        main-preservation sweep records product blob equal to Base
        blob for each swept path, pairwise.
    C3c (M3c) The ledger artifact is byte-identical to the pin's;
        the pin's report bytes are an exact prefix of the product's;
        both OPEN rows are present, valueless, and quoted.
    C4  (M4) No test fails on the post-merge integration tree that
        passes at the base; and H_integ differs from that tested
        tree only by the report artifact (M4b), verified by diff.
    C5  (M5) origin/main equals H_integ; the source branch and
        science/integrate-xi-rulings-02 are unmoved from their M1
        values; the M5 addendum commit is on the integration branch
        only and origin/main remains H_integ after it.
    C6  (M4b) The report carries §0a's pin-versus-source paragraph
        verbatim and does not assert its own commit SHA.

## 3. Abort conditions

    A1  Any M1 value disagrees with this spec's Base, Source, stated
        merge-base, or pin-ancestry relation. STOP before any write;
        report the measured values. (A moved main is stale-base
        handling per BRANCHING_POLICY.md, not an error to repair
        silently.)
    A2  The merge is not conflict-free, or M3 finds any digest
        mismatch in the merge product. STOP; report; do not resolve
        content inside this task.
    A3  Advancing main would not be a fast-forward at push time.
        STOP; report; stale-base handling applies.
    A4  Any step would modify the source branch or any file arriving
        from it; would dispose, value, annotate, or cross-reference
        either OPEN row; would begin, schedule, or constrain either
        task `P2-XI-RULINGS-02` authorizes; or would relabel,
        summarise, or condition-strip the arriving `ξ(G) | COND-1..4`
        assembly. STOP; report.
    A5  M3b finds a contributed path or status outside the manifest,
        a both-changed path, a source-unchanged path whose product
        blob differs from the Base's, or a main-unchanged
        contributed path whose product blob differs from the
        source's; or M3c finds any failure. STOP; report the path
        and all applicable blob ids — for a both-changed path: fork,
        source, Base, AND product. Do not repair the merge inside
        this task.

## 4. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4), and the post-push M5
        addendum (branch-only)
    specs/2026-08-23T2100Z_xi-ledger-01-integ.md and its SHA-bound
        review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-ledger-01-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets and
        blob-id pairs verbatim, the M3c comparisons, and §0a's
        pin-versus-source paragraph; M5 ref values in the
        branch-only addendum; any A that fired recorded wherever the
        stop occurred

END OF SPECIFICATION
