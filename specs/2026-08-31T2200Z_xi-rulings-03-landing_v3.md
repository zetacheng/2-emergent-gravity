# SPECIFICATION — P2-XI-RULINGS-03-LANDING-01: verbatim landing of the issued R-1 ruling and its document review

    Task ID        P2-XI-RULINGS-03-LANDING-01
    Version        v3 — revises v2 (sha256 ebae08b843270e166f056462d8
                   dec428b257b6e5146aad75456c19d46e3c6182), which
                   STOPPED at M2b under A3 before any write. The scan
                   found the issued document's RATIONALE naming the
                   exponent mapping as the second element not fixed by
                   landed text, where P2-XI-QM3-DEP-01 records it as
                   FIXED at g = +2c and names the decoupling
                   prescription instead. The PI re-issued the ruling
                   with that RATIONALE corrected; every RULING line is
                   unchanged. v3 rebinds to the re-issued bytes and
                   adds M2b item (8), which makes the check that
                   caught this a standing one rather than an accident
                   of item (6). v2 had revised v1 (sha256
                   a63a36207ea29b576b3ce633f3
                   9c506616731500ed58d82e63ea5346c99e3938) per Reviewer
                   verdict REVISE BEFORE EXECUTION. v1's M6b offered
                   two lawful routes for post-push evidence — a
                   branch-only addendum commit, or the execution
                   summary — while C6 required the final tip to differ
                   from T only by the report. Taking the addendum
                   route would have made C6 fail by construction. v2
                   names three states, binds the report-only diff to
                   the report commit rather than to whatever the
                   branch tip ends as, and gives the addendum its own
                   criterion. No scope or content change.
    Spec file      specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md

    Commit points, named for the measurements below:
        Base        4a99e81a… (above)
        T           the tested post-M4 tip (M5)
        H_report    T + the report commit (M6a)
        H_addendum  H_report + the post-push addendum, if taken (M6b)
    Author         Researcher (Claude)
    Date           2026-08-31
    Base           main @ 4a99e81ad16322e1152286df0158b648b75d18f3,
                   pinned here and MEASURED at M0, not assumed.
    Branch         science/xi-rulings-03-landing, cut from the Base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Template       Instantiates the landing structure approved and
                   executed as P2-XI-CLAR-01-LANDING v2 (sha256
                   2a30601952c0cdf48d000f0a46f39241c0c6315e590c766c40
                   b1c3d8be620ca6), including its mandatory pre-write
                   correspondence scan and its M6a/M6b/M6c
                   report-sequencing. One improvement on every prior
                   instance: the review artifact carries a
                   PRE-COMMITTED digest this time, so M2 verifies
                   against a pre-registered value rather than
                   recording one for the first time.

---

## 0. What this task is and is not

**This task transports.** It lands the issued PI ruling
`P2-XI-RULINGS-03` byte-exact, with its document-review artifact and
register entries, and adjudicates nothing.

- **It does not exercise the ruling's Ruling 3 authorization.** That
  ruling authorizes a prescription-definition specification. A
  specification answering to it exists and has been reviewed, but
  **this landing does not begin, schedule, constrain, sequence, or
  represent as ready any such task.** Landing an authorization is not
  exercising it. (A5)
- **It does not disturb `P2-XI-QM3-DEP-01`'s determination.** That
  check returned `NOT UNIQUELY IDENTIFIED`, and the issued text's
  Ruling 2 states in its own words that the determination stands
  until a prescription is landed. No step here describes the subject
  as now uniquely identified, or the constructive gap as closed or
  narrowed. (A5)
- **It does not close `OPEN-AC-1`, exclude the V/A representations,
  or touch the registered representation-stability item.** The issued
  text preserves all three; this landing preserves them by
  transporting the text unaltered. (A5)
- The two OPEN ledger rows remain OPEN; no membership is ruled.

## 0a. Provenance of the bytes this task lands

    Issued document      P2-XI-RULINGS-03, RE-ISSUED by the PI in
                         session, 2026-08-31, with issuance statement
                         declaring: SHA-256
                         1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686.
    Supersession         The re-issuance supersedes the document of
                         the same identifier at SHA-256
                         f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8.
                         **That document was never landed.** Nothing
                         in the repository is superseded by this
                         landing, and no erratum, clarification or
                         supersession mechanism is engaged: the
                         correction happened before landing, and the
                         only trace of the superseded bytes that
                         reaches the repository is the SUPERSEDES
                         field inside the re-issued text itself. This
                         landing lands one document.
    Derived git blob id  0b331afb6f21f6591a0c3934fc8916bda742d8de,
                         measured by the Researcher over the same
                         bytes and pre-registered as a secondary
                         check. A blob id is a different hash function
                         and cannot equal a SHA-256; byte identity is
                         discharged by C1.
    Review artifact      2026-08-31_review_P2-XI-RULINGS-03-issued-v2.md,
                         ChatGPT, verdict "FIT FOR RECORDING",
                         self-bound to the re-issued digest above. Its
                         own digest is NOT pre-registered: the
                         issuance statement provides that it "is
                         recorded at landing". M2 therefore records it
                         for the first time, provenance
                         transmitted-in-session, as in the
                         P2-XI-RULINGS-01, -02 and clarification
                         landings. The review artifact bound to the
                         superseded bytes
                         (eda7a4c6eff5f088b94d67a89dd85fbe74576b11f03ee8ced6af822480ca296a)
                         is NOT the artifact this task lands and must
                         not be supplied in its place; supplying it is
                         A1, since the digest it declares would not
                         equal M1's.

Both files are supplied by the PI with this specification. The
Executor verifies both against this section before any write (M1, M2)
and does not retype, reflow, or re-encode either.

## 1. Landing structure

Per the landed two-file decision layout
(`decisions/P2-XI-RULINGS-02.issued.md` +
`decisions/2026-08-23-xi-rulings-02.md`):

    decisions/P2-XI-RULINGS-03.issued.md
        The issued bytes, byte-exact. This file is the ruling.

    decisions/2026-08-31-xi-rulings-03.md
        The register record in the two parts decisions/README.md
        requires. PART 1: owner, date, effect, scope; the canonical
        text's location with its SHA-256 and blob id; and the
        canonical decision key. PART 1 does not paraphrase the
        ruling; where it refers to content it does so by section name
        ("RULING 1" through "RULING 3", "ROUTING") and by quotation.
        PART 2 reproduces the document review verbatim and records
        its SHA-256 as verified at M2.

    Canonical decision key: 2026-08-31-xi-rulings-03

    reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
        The review artifact as a standalone landed original,
        byte-identical to the bytes supplied.

## 2. Measurements

    M0  Base check, before any write.
        Record the Base SHA and verify it equals the pinned value.
        A mismatch is A1 (stale-base handling per
        BRANCHING_POLICY.md, not an error to repair silently).

    M1  Byte identity of the issued document.
        sha256sum and git hash-object over the supplied issued file;
        record both in full. Disagreement with §0a is A1.

    M2  Byte identity of the review artifact.
        sha256sum over the supplied review file; record it in full as
        its first recorded digest, provenance
        transmitted-in-session. Then extract from inside the review
        artifact the SHA-256 it declares itself bound to, and compare
        that string against M1's digest as a full-string match. A
        disagreement is A1 — and is the condition that catches the
        superseded artifact being supplied by mistake.

    M2b Landed-authority correspondence scan, before any write.
        Resolve at the Base, recording for each the reference, the
        landed text located (path:line, quoted), and a finding
        RESOLVES / DOES NOT RESOLVE:
          (1) the 2026-08-09 ruling the issued text extends —
              DECISION_LOG.md, heading "2026-08-09 — Mean-field
              channel for P2-PHASE-01: the scalar channel with a real
              auxiliary field" — including its three own limits: that
              it is a choice of route and not a judgement, that it
              does not close OPEN-AC-1, and the DEFERRED-01 deferral
              of the V/A representation;
          (2) OPEN-AC-1's landed status in
              derivations/P2-PHASE-01_input_admissibility_contract.md;
          (3) DEFERRED-01 in derivations/P2-DEFERRED-ITEMS.md;
          (4) the representation-stability open item registered
              2026-08-24 in DECISION_LOG.md, with its escalation
              condition;
          (5) P2-FIERZSUM-01.md:218-220, the four-element
              prescription requirement Ruling 3 names;
          (6) P2-XI-QM3-DEP-01's determination and its R-1/R-2
              symmetry statement. **Record a scope relation, not a
              conflict:** the issued text's RATIONALE cites that
              artifact's reading that R-1 alone does not return
              UNIQUELY IDENTIFIED, and attributes it as the
              Researcher's reading rather than as a landed finding.
              Both wordings are preserved verbatim; neither is
              reworded and they are not reconciled.
          (7) That the landing leaves that determination standing:
              quote Ruling 2's own sentence to that effect from the
              issued bytes.
          (8) FIXED-VERSUS-UNFIXED CONSISTENCY, a standing check.
              For every statement in the issued bytes — in RULING or
              RATIONALE alike — that an element IS or IS NOT fixed by
              landed text, verify it against
              P2-XI-QM3-DEP-01's determination table
              (derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md,
              its "Fixed by landed text" and "Not fixed by landed
              text" lists). Enumerate the issued text's such
              statements by a rule stated from the document's own
              structure before checking any of them, and record the
              enumeration and its count. Each statement must agree
              with the table, or rest on landed authority the table
              does not cover, quoted. **A disagreement is A3.**
              Note the distinction this check must respect and must
              not flatten: "not fixed BY THIS RULING" is a statement
              about the ruling's own supply and is NOT a claim that
              the element is unfixed in the repository. Only the
              latter kind of statement is compared against the table.
        Any substantive conflict, or an item that does not resolve,
        is A3. **Landing without a completed scan is not a permitted
        execution path.**

    M3  Landing.
        Cut the branch; commit this specification, then its SHA-bound
        review (spec → review, binding verified before the spec
        commit); then land the §1 files. Record every commit SHA.

    M4  Register append.
        Append to DECISION_LOG.md an index entry: date, decision key
        2026-08-31-xi-rulings-03, one-line subject, the path of the
        canonical record, the issuance SHA-256, and the review
        verdict string "FIT FOR RECORDING". Append-only; verify the
        Base's DECISION_LOG.md bytes are an exact byte-prefix of the
        product.

    M5  Suite, on a full (non-shallow) tree.
        Run the suite at the Base and at the post-M4 tree. Record
        both verbatim and the tested tree's SHA, T.

    M6a Report, and the report commit.
        Write reports/<UTC>_xi-rulings-03-landing.md recording M0
        through M5 and nothing later, including the full M2b scan.
        The report does not state its own commit SHA: it names T and
        records that it is itself the next commit on T. Commit it.
        The resulting tip is H_report, measured externally after the
        commit exists. Verify by diff that H_report differs from T
        ONLY by the report artifact.

    M6b Push, and post-push evidence.
        Push the branch at H_report. Then record H_report's SHA, the
        M6a diff result, and the push result. Two routes are
        available and the Executor states which was taken:
          EXECUTION SUMMARY ONLY — the evidence is returned to the PI
                      and nothing further is committed. The branch
                      tip remains H_report.
          BRANCH-ONLY ADDENDUM — the evidence is committed as one
                      further commit, H_addendum, and the branch is
                      pushed again. That commit changes exactly one
                      path, the addendum record, and NOTHING that
                      arrived from M3 or M4. **H_addendum is
                      post-push evidence and is not part of the
                      tested product**; the report-only diff of M6a
                      is bound to H_report and is unaffected by it.
        Integration is a separate task and is not performed here.

    MEASUREMENT SUBSTRATE, applying throughout: probes are constructed
    from the file's bytes, not from remembered or rendered markup, and
    operate on bytes. Every structural scan states its assumptions
    about fenced blocks, blockquote prefixes and emphasis wrapping. A
    negative result is reported only alongside a live positive
    control. A probe that fails against its own assumption is a defect
    of the probe: re-measure and record the correction; do not declare
    an abort on a false failure. Every offset, length, prefix and
    byte-identity comparison is performed and reported in BYTES, with
    the normalization stated or stated to be none. An identifier — a
    commit SHA, a digest, a line number — is used only at a value this
    task has measured and printed; an abbreviation is never completed.

## 3. Acceptance criteria

    C0  (M0) The Base equals the pinned SHA as a full-string match.
    C1  (M1) The recorded sha256 equals
        1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
        and the blob id equals
        0b331afb6f21f6591a0c3934fc8916bda742d8de, reproduced under
        re-measurement from H_report.
    C2  (M2) The review artifact's sha256 is recorded in full; the
        SHA-256 it declares equals C1's digest as an exact string
        match; and it lands byte-identical to the bytes supplied.
    C2b (M2b) Each of the eight scan items carries a finding with its
        quoted landed text; item (8)'s enumeration rule and count are
        recorded before any of its statements is checked, and its
        "not fixed by this ruling" versus "unfixed in the repository"
        distinction is respected; item (6)'s scope relation is recorded
        with both wordings verbatim and their attributions
        distinguished; item (7) quotes Ruling 2 from the issued
        bytes; no item is unresolved and no substantive conflict is
        recorded.
    C3  (M3) Commit order is spec, its review, then the landing
        commits, nothing interleaved; the register record's
        quotations are byte-identical to the issued file's
        corresponding passages, under a stated normalization.
    C4  (M4) The Base's DECISION_LOG.md bytes are an exact
        byte-prefix of the product.
    C5  (M5) No test fails on T that passes at the Base.
    C6  (M6a) The report records M0–M5 and no later measurement,
        names T, and does not assert its own SHA; and H_report
        differs from T ONLY by the report artifact, verified by diff.
    C6b (M6b) The route taken is stated. On EXECUTION SUMMARY ONLY
        the branch tip equals H_report. On BRANCH-ONLY ADDENDUM the
        range H_report..H_addendum is exactly one commit changing
        exactly one path, the addendum record, and no path arriving
        from M3 or M4 is touched. Under either route the C6 diff
        remains bound to H_report.

## 4. Abort conditions

    A1  The Base is not the pinned SHA, or any digest measured at M1
        or M2 disagrees with §0a, before any write. STOP; no branch
        is created; report the measured values.
    A2  Reserved: not used. No condition in this task depends on a
        merge, which this task does not perform.
    A3  The M2b scan records a substantive conflict or an unresolved
        item, or any later step surfaces a conflict between the
        issued ruling and landed text. STOP; report verbatim; do not
        reconcile. Absence of a completed M2b record is itself this
        abort.
    A4  Transport fidelity: any register-record passage that would
        state the ruling materially more narrowly, more broadly, or
        more specifically than the issued text, without independent
        landed authority. STOP; report the divergent wording
        verbatim.
    A5  Any step would: read the RATIONALE's statement that landed
        authority fixes the exponent mapping at g = +2c as this
        ruling having fixed it — RULING 2 says the opposite of its
        own supply, and the two are compatible; begin, schedule,
        constrain, sequence, or represent as ready the
        prescription-definition task Ruling 3 authorizes; describe the Q-M3 subject as now uniquely
        identified, or its constructive gap as closed or narrowed;
        close OPEN-AC-1; exclude the V/A representations; touch the
        registered representation-stability item; or dispose either
        OPEN ledger row. STOP; report.

## 5. Deliverables

    decisions/P2-XI-RULINGS-03.issued.md          (byte-exact)
    decisions/2026-08-31-xi-rulings-03.md         (register record)
    reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
    DECISION_LOG.md                               (append)
    specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md and its
        SHA-bound review, committed at M3 in spec → review order
    reports/<UTC>_xi-rulings-03-landing.md (M6a, yielding H_report)
    the M6b post-push evidence, by the route taken: the execution
        summary, or a branch-only addendum commit (H_addendum)
    Branch pushed per BRANCHING_POLICY.md science/* scope (M6b);
        integration is a separate task and is not performed here.

END OF SPECIFICATION
