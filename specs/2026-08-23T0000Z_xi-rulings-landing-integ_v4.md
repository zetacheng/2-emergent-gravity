# SPECIFICATION — P2-XI-RULINGS-LANDING-INTEG: transport of the executed landing to main

    Task ID        P2-XI-RULINGS-LANDING-INTEG
    Version        v4 — revises v3 (sha256 d0a30ff4bdeacecc957e73bba2
                   e63f90a68588cc082b6b99829caae5be2529c1) per Reviewer
                   verdict REVISE BEFORE EXECUTION on v3, two items:
                   (i) v3's Spec file field still named the v2 path —
                   corrected to the v4 path below, so filename,
                   content, and review binding agree; (ii) the
                   pre-execution spec and review commits are now an
                   explicit step (M1b) preceding the merge, so that
                   C5's "H_integ differs from the tested tree only by
                   the report" is made true by construction. A
                   consequence the Researcher repairs with it: C2's
                   parent condition is restated, since with M1b the
                   merge's first parent is the M1b tip, not the base.
                   Version chain: v3 revised v2 (sha256 ff6a7f6a48bbb1
                   bb31d12f91abd93ebbd34caa78a5aa137734692f3c443ae8b0,
                   sequencing M4→M5→M5b→M6, C5 tested-tree wording);
                   v2 revised v1 (sha256 046806bdddfdcd7b1cbf2d8338fa
                   da26aaf43d246952def977f8384ff75cca2e) with three
                   changes, all retained:
                   (1) the executor-identity ruling's canonical home is
                   a decisions/ record, per the Reviewer's selection of
                   that limb of v1's flagged structure disposition;
                   DECISION_LOG.md carries an index entry pointing to
                   it, not the ruling's sole record. (2) v1's forward
                   executor-field convention is REMOVED from landed
                   content: it was Researcher-proposed, not PI-issued,
                   and an integration task does not land it. (3) the
                   merge commit and the final integration tip are now
                   distinct named objects; main advances to the final
                   tip, and the report/post-push sequencing is closed.
    Spec file      specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md
    Author         Researcher (Claude)
    Date           2026-08-23
    Base           main @ 6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Source         science/xi-rulings-landing-01 @
                   190f61c4 (full SHA recorded by the Executor at M1;
                   the abbreviated form here is the handover reference
                   and M1 records the full form before any write)
    Branch         science/integrate-xi-rulings-landing-01, cut from
                   the base above
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

Prohibitions, restated from the Reviewer's disposition of the
execution report:

- It does not re-adjudicate any ruling in
  `decisions/P2-XI-RULINGS-01.issued.md`.
- It does not reconstruct, reword, or re-derive `H-XI-SIGN-01`.
- It does not exercise Ruling 2's forward-terminology effect; no
  existing repository text is reworded.
- It does not integrate `science/xi-b0a` or touch any other branch.
- It does not move the source branch
  (`BRANCHING_POLICY.md:34-37`).

## 0a. Provenance carried by this integration

### The executed result

`P2-XI-RULINGS-LANDING-01` executed under
`specs/2026-08-22T2001Z_xi-rulings-landing_v2.md` (sha256
`23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee`),
pre-execution review APPROVE FOR EXECUTION (sha256
`e252589cb010db0009e6382a85e6621253a6a8200a3c5628390433e6fca8477b`).
The execution report is on the source branch. C1–C6 PASS; A1–A5 none
fired. Independent verification from a clean clone by the Researcher
confirmed every digest, the Statement-SHA convention re-derivation,
carrier byte-identity, append-only preservation, and identical
base/tip failure sets under the known shallow-clone artifact.
The Reviewer's disposition of the execution report:
EXECUTION COMPLETE — NOT YET INTEGRATED.

### PI ruling on executor identity, issued in session 2026-08-23,
### quoted verbatim

> I confirm. Claude Code was the designated executor for
> P2-XI-RULINGS-LANDING-01 under AGENTS.md:86. The specification's
> "Codex only" label is superseded for executor identity only by that
> runtime PI designation. No scientific, measurement, scope, or
> acceptance criterion is changed, and no re-execution is required.

This ruling's canonical provenance record is created by M4 below as
`decisions/2026-08-23-xi-landing-executor-identity.md`, per the
four-way separation and per the landed rule that a specification
transcribing a ruling is evidence of its content and not its
canonical provenance record. The Reviewer selected this form from
v1's flagged disposition; the selection is on record in the v1 review.
`DECISION_LOG.md` receives an append-only index entry pointing to the
canonical record; the log entry is a pointer, not the ruling's home.

### What this task does NOT land about executor identity

The forward executor-field convention ("the executor designated by
the PI at execution time" as a programme-wide spec-authoring rule) is
NOT landed by this task. It is a Researcher authoring practice unless
and until the PI issues it as a ruling; if issued, it lands as its
own limb through the normal path, distinct from the retrospective
ruling above. This spec's own Executor field uses the phrasing as
authoring practice, which binds this spec only.

## 1. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-b0a. Verify origin/main equals the Base
        above and is a strict ancestor of the source tip
        (`git merge-base --is-ancestor`), recording the command
        output. Verify the source tip's abbreviated form equals the
        Source field above.

    M1b Pre-execution provenance commits, before the merge.
        Cut the integration branch from the base. Commit the exact
        reviewed v4 specification, then its SHA-bound pre-execution
        review, in that order (spec → review). Before the spec
        commit, verify the spec file's sha256 equals the digest the
        review declares itself bound to, recording both strings. The
        review file has no pre-committed hash; record its sha256 at
        commit as its first recorded digest, provenance
        transmitted-in-session. Record the M1b tip SHA. These commits
        are part of the post-M4 tree that M5 tests; nothing else is
        committed between them.

    M2  Merge construction.
        On the integration branch at the M1b tip, merge the source
        tip with `--no-ff`. Record the merge commit SHA (M_merge) and
        its two parent SHAs. M_merge is the source-transport object;
        it is not the final tip.

    M3  Arriving-blob verification, from the merge product.
        sha256sum over each of, recording every digest in full:
          decisions/P2-XI-RULINGS-01.issued.md
              expected 1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
              and git blob id f793f9fd866f563480fbec6168553a2b967aea8f
          reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md
              expected c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364
          specs/2026-08-22T2001Z_xi-rulings-landing_v2.md
              expected 23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee
          reviews/chatgpt/2026-08-22T2001Z_xi-rulings-landing_v2.md
              expected e252589cb010db0009e6382a85e6621253a6a8200a3c5628390433e6fca8477b
        Re-derive the Statement SHA of H-XI-SIGN-01's exact statement
        under the pin convention the landing task measured
        (blockquote prefix stripped, newline-joined, one trailing
        newline); expected
        8731037c16e485fd40d279cef827421cd733bc438ff828f1408dbdbd15488e90.

    M4  Canonical decision record, then index.
        On the integration branch, after M_merge:
        (a) Create decisions/2026-08-23-xi-landing-executor-identity.md
            containing, at minimum: the task affected
            (P2-XI-RULINGS-LANDING-01); issuance (PI, in session,
            2026-08-23); the PI ruling of Section 0a quoted verbatim,
            byte-identical; scope (executor identity only; no
            scientific, measurement, scope, or acceptance change; no
            re-execution); and the historical fact that the reviewed
            specification's Execution field read "Executor (Codex)
            only" and was superseded for executor identity only, for
            that execution only, by the runtime PI designation under
            AGENTS.md:86. PART 2 is marked REVIEW PENDING per
            decisions/README.md.
        (b) Append to DECISION_LOG.md an index entry: date, decision
            key 2026-08-23-xi-landing-executor-identity, one-line
            subject, and the path of the canonical record. Verify the
            base's DECISION_LOG.md bytes are an exact byte-prefix of
            the product.

    M5  Suite, on a full (non-shallow) tree, after M4.
        Run the suite at the base and at the integration branch tip
        as it stands after M4 (the post-M4 integration tree). Record
        both results verbatim, and record the SHA of the tree the
        integration-side run used. The shallow-clone governance-test
        artifact is on record; a shallow tree is not a valid
        substrate for this measurement.

    M5b Report commit and final tip.
        Write reports/<UTC>_xi-rulings-landing-integ.md on the
        integration branch, recording M1 through M5 outputs (M6 is
        post-push and is excluded from this file by construction).
        Commit it. The integration branch tip after this commit is
        H_integ, the final integration tip. Record H_integ's SHA.
        No suite re-run at H_integ is required: the suite was
        measured on the post-M4 tree, and H_integ differs from that
        tested tree only by the report artifact. The report states
        this.

    M6  Push, then post-push ref audit.
        Push the integration branch. Advance main by fast-forward to
        H_integ and push. Then record the full SHAs of origin/main,
        the source branch, and origin/science/xi-b0a, and verify the
        latter two equal their M1 values. M6's output is recorded in
        an addendum commit on the integration branch ONLY, pushed to
        the integration branch and not to main; origin/main remains
        H_integ. This closes the report/push cycle: everything landed
        on main is measured before push, and the post-push audit
        lives on the preserved integration branch.

## 2. Acceptance criteria

    C1  (M1) origin/main equals the Base; the ancestor check passes;
        the source tip matches the Source field.
    C2  (M1b, M2) M_merge has exactly two parents: the M1b tip and
        the source tip; the M1b tip descends from the base by exactly
        two commits (the spec, then its review); the spec's sha256
        equals the digest the review declares, as recorded at M1b.
    C3  (M3) Every digest equals its expected value, as full-string
        matches recorded in the report.
    C4  (M4) The canonical record exists at its stated path with the
        ruling quoted byte-identical to Section 0a; the DECISION_LOG
        append is byte-prefix-preserving and points to that path.
    C5  (M5) No test fails on the post-M4 integration tree that
        passes at the base; and H_integ differs from that tested
        tree only by the report artifact (M5b), verified by diff.
    C6  (M6) origin/main equals H_integ; the source branch and
        science/xi-b0a are unmoved from their M1 values; the M6
        addendum commit is on the integration branch only and
        origin/main remains H_integ after it.

## 3. Abort conditions

    A1  Any M1 value disagrees with this spec's Base or Source, or
        the ancestor check fails. STOP before any write; report the
        measured values. (A moved main is stale-base handling per
        BRANCHING_POLICY.md, not an error to repair silently.)
    A2  The merge is not conflict-free, or M3 finds any digest
        mismatch in the merge product. STOP; report the conflict or
        the measured digest; do not resolve content inside this task.
    A3  Advancing main would not be a fast-forward at push time. STOP;
        report; stale-base handling applies.
    A4  Any step would require modifying the source branch, any file
        arriving from it, or any pre-existing DECISION_LOG.md byte.
        STOP; report.

## 4. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the canonical decision record, the DECISION_LOG
        index append, the report (through M5), and the post-push M6
        addendum (branch-only)
    specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md and its
        SHA-bound review, landed at M1b
    decisions/2026-08-23-xi-landing-executor-identity.md
    main advanced by fast-forward to H_integ
    reports/<UTC>_xi-rulings-landing-integ.md — M1 through M5 outputs
        as matched text, every digest in full; M6 ref values in the
        branch-only addendum; any A that fired recorded wherever the
        stop occurred

END OF SPECIFICATION
