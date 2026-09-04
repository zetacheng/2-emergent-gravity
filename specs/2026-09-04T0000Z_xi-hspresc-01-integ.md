# SPECIFICATION — P2-XI-HSPRESC-01-INTEG: transport of the executed decoupling prescription to main

    Task ID        P2-XI-HSPRESC-01-INTEG
    Version        v1
    Spec file      specs/2026-09-04T0000Z_xi-hspresc-01-integ.md
    Author         Researcher (Claude)
    Date           2026-09-04
    Base           main @ b01bb18ba51008d09b64b442afad37b800b2d3d1
    Source         science/xi-hspresc-01 @
                   5771ebd082ec53dfcb37b1ddc076aaef3329844f
    Branch         science/integrate-xi-hspresc-01, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed transport protocol approved
                   and executed as P2-XI-QM3-DEP-INTEG v2 (sha256
                   f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfba
                   e9f613ab904df0), the all-`A` variant: the
                   contributed set here has no modified path, so that
                   protocol's modified-path structural limb is absent
                   rather than carried over empty. The source DESCENDS
                   from the Base (merge-base = Base, measured), so
                   M3b's main-side set is expected empty; it is
                   measured regardless.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is `P2-XI-HSPRESC-01`, executed on its
`INCONCLUSIVE` path: `E1` through `E6` fixed `LANDED-DERIVED`, the
auxiliary functional measure's normalization routed under `A3` within
`E5`, `E7` routed, and `M4` returning
`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED` with a symmetric
resolution path defined and not walked.

**What must survive transport unaltered, and what this task therefore
must not do:**

- **The prescription is NOT complete.** `M4`'s two returns are
  mutually exclusive and the arriving one is `INCONCLUSIVE`. This
  task does not describe the prescription as complete, as complete in
  part, or as uniquely defining `N_α[g]`. "Uniquely defined to the
  extent reached" was not an available return to that task and is not
  an available description here. (A4)
- **`N_α[g]` was IDENTIFIED, not DEFINED.** The arriving artifact
  records what kind of object it is — the normalization the adjoined
  auxiliary integration carries, not the Jacobian of an invertible
  change of variables — and records that writing its defining
  expression needs authority landed text does not carry. **This task
  does not collapse identification into definition.** (A4)
- **The refused reading stays refused.** The artifact records that
  reading the landed identity literally as a functional statement
  would make `N_α[g]` the identity and thereby settle what Q-M3 asks,
  and records the refusal. This task does not adopt, endorse,
  weaken, or characterise that reading as available. (A4)
- **`Q-M3`'s subject remains not uniquely identified.** The
  constructive gap is narrowed, not discharged. No step describes
  the Q-M3 re-run as unblocked, ready, due, or nearer. (A4)
- **The two routed items arrive unanswered and unranked.** They are
  the PI's. This task does not answer, recommend on, order,
  prioritise, or schedule work on either. (A4)
- **`DET-01` is not resolved and `𝔊` is not chosen.** The arriving
  artifact routed rather than choose; this task preserves that by
  transporting it unaltered. (A4)
- Both OPEN ledger rows remain OPEN; no membership is ruled.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 1a. The contributed manifest

The arriving change set contains four added paths and no modified
path. Any `M`, `D` or `R` status, or any path outside the four, is
A5 — no exception; a manifest change requires a revised,
re-reviewed specification.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-rulings-03-landing,
        origin/science/xi-qm3-dep-01 and
        origin/science/xi-qm2-scope-01 (refs this task must not
        move). Verify origin/main equals the Base and the source tip
        equals the Source field, both as full-string matches. Verify
        `git merge-base main <source>` equals the Base as a
        full-string match. **Resolve `origin/main` explicitly: a
        local `refs/heads/main` may be stale and is not the canonical
        tip; the arriving report records that condition.**

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
          derivations/P2-XI-HSPRESC-01_assembled-chain-decoupling-prescription.md
              expected a478154dbaf266cfd389a808f82d5cabe1533a0868b0775ccb137a7ef20a4e41
          specs/2026-08-25T1200Z_xi-hspresc-01_v6.md
              expected 940d8d7820d6fd58ad728637808cf8aee7f17ff1cc38f38639a3a01508fdc497
          reviews/chatgpt/2026-08-25T1200Z_xi-hspresc-01_v6.md
              expected 4aa3713c76fb8332da27c96c3e92aedcbca75a4305868fe9f6d3a53fb53e5e23
          reports/2026-09-03T1919Z_xi-hspresc-01.md
              expected 82e50c35de0c351dacb20e53370882627c90399e296e1e4593b785c7a671546f
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-09-04; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected equal to
        the Base).
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
            P_main is empty because FORK = Base, hence P_overlap is
            empty — recorded as a measured comparison over the
            classified union, not inferred from the equality.
        (c) Main-preservation sweep. For each path in P_main not in
            P_source, compare the merge product's blob id against the
            Base's, pairwise. Expected vacuous; record it as
            measured, not skipped.

    M3c Arrival-state verification of the finding.
        Perform (i) FIRST and derive the domain of (ii) from it.
        (i)   ENUMERATION. State the rule by which a passage counts
              as an element's outcome mark, taking it from the
              artifact's own landed structure rather than from
              judgement — the artifact carries per-element sections
              and explicit mark statements. Record the rule, the
              enumerated set and its count BEFORE testing any mark.
              **Token counting is not enumeration:** the vocabulary
              words appear in the artifact's own explanatory prose,
              and a count of occurrences is not a count of
              assignments. If the rule cannot be stated from the
              artifact's structure, that is A5.
        (ii)  MARKS AND ROUTINGS. Within the enumerated set, verify
              that each of E1–E7 carries its mark as executed, and
              that the routed items — the auxiliary functional
              measure's normalization within E5, and E7 — are each
              recorded as routed under `A3` with the choice at issue
              stated and not taken.
        (iii) THE RETURN. `M4`'s return in the merge product reads
              `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`, with its
              blocking elements named, the fixed elements recorded as
              gap characterization, and the resolution path present
              and marked defined-not-walked. Verify that
              `PRESCRIPTION COMPLETE` is not asserted as this task's
              return anywhere. **Confine that check to the enumerated
              return-stating passages, not the artifact's full text:
              the phrase occurs legitimately where the vocabulary is
              defined and where a future re-run is contemplated.**
        (iv)  THE REFUSAL. The artifact's record of the refused
              reading — that the landed identity read literally as a
              functional statement would make `N_α[g]` the identity —
              is present, together with its reason for refusal.
        Any failure is A5. State for each check the normalization
        applied or that none was.

        MEASUREMENT SUBSTRATE, applying to all of M3c: probes are
        constructed from the file's bytes, not from remembered or
        rendered markup, and operate on bytes. Every structural scan
        states its assumptions about fenced blocks, blockquote
        prefixes, emphasis wrapping and line wrapping. Vocabulary
        probes match whole words, case-sensitively, against a bounded
        vocabulary — a bare substring search is invalid here, as the
        arriving task's own second probe defect demonstrates. A
        negative result is reported only alongside a live positive
        control. A probe that fails against its own assumption is a
        defect of the probe: re-measure and record the correction; do
        not declare A5 on a false failure.

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim and the tested tree's SHA,
        T. The arriving task added no tests; the criterion is
        regression, not a count.

    M4b Report commit and final tip.
        Write reports/<UTC>_xi-hspresc-01-integ.md recording M1
        through M4 and nothing later — M5's evidence does not exist
        when it is written. The report does not state its own commit
        SHA: it names T and records that it is itself the next commit
        on T. Commit it; the tip after this commit is H_integ,
        measured externally. Verify by diff that H_integ differs from
        T ONLY by the report artifact.

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
        field; and origin/main was resolved explicitly rather than
        from a local ref.
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
        is recorded as measured.
    C3c (M3c) (i)'s enumeration rule, enumerated set and count are
        recorded before any mark is tested; (ii)'s per-element marks
        and both routings are verified as executed; (iii)'s return is
        verified with its check confined to the enumerated
        return-stating passages, and out-of-domain occurrences
        recorded as context rather than as failures; (iv)'s refusal
        record is present; and each check states its normalization.
    C4  (M4) No test fails on T that passes at the base.
    C5  (M4b, M5) H_integ differs from T only by the report artifact,
        verified by diff; the report records nothing later than M4
        and does not assert its own SHA; origin/main equals H_integ;
        the source branch and the three M1 refs are unmoved; the
        route taken at M5 is stated, and under either route
        origin/main remains H_integ.

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
        from it; would describe the prescription as complete or
        partially complete, or `N_α[g]` as defined rather than
        identified; would adopt, endorse or weaken the refused
        reading; would describe the Q-M3 subject as uniquely
        identified, its gap as discharged, or its re-run as
        unblocked, ready or due; would answer, recommend on, order or
        prioritise either routed item; would resolve `DET-01` or
        choose `𝔊`; or would dispose either OPEN ledger row. STOP;
        report.
    A5  M3b finds a contributed path or status outside §1a's
        manifest, a both-changed path, a source-unchanged path whose
        product blob differs from the Base's, or a main-unchanged
        contributed path whose product blob differs from the
        source's; or M3c finds any failure, including an enumeration
        rule that cannot be stated from the artifact's structure, or
        a negative result reported without a live positive control.
        STOP; report the path and all applicable blob ids — for a
        both-changed path: fork, source, Base, AND product. Do not
        repair the merge inside this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4, yielding H_integ), and — on
        the BRANCH-ONLY ADDENDUM route only — the M5 addendum commit
    specs/2026-09-04T0000Z_xi-hspresc-01-integ.md and its SHA-bound
        review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-hspresc-01-integ.md — M1 through M4 outputs as
        matched text, every digest in full, the M3b path sets and
        blob-id pairs, and M3c's enumeration rule, per-element marks,
        routings, return and refusal record with their
        normalizations. **It records nothing later than M4.**
    M5's post-push ref values and the route taken — recorded in the
        execution summary, or in the optional branch-only addendum
        commit, according to M5. Not in the M4b report.
    Any A that fired — recorded wherever the stop occurred

END OF SPECIFICATION
