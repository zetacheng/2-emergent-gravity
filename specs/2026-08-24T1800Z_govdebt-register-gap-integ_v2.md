# SPECIFICATION — P2-GOVDEBT-REGISTER-GAP-INTEG: transport of the governance-debt entry to main

    Task ID        P2-GOVDEBT-REGISTER-GAP-INTEG
    Version        v2 — revises v1 (sha256 e39346427201179a5bbf0f8034
                   b6471454073b21420e8ea204262a21c5182cf3) per Reviewer
                   verdict REVISE BEFORE EXECUTION. Three corrections,
                   all to M3b(d) and §0a; no architecture change:
                   (i) "exactly one heading is added" had no stated
                   comparison basis, which a stale-source integration
                   may not leave to the Executor — v2 formalises it as
                   an ordered-sequence identity against the Base;
                   (ii) v1 asserted the counts table could be checked
                   against headings, but a heading carries an entry
                   identifier and not a disposition, so the criterion
                   named no measurement that could produce the
                   per-disposition lists — v2 requires the buckets to
                   be reconstructed from each entry's own landed
                   Disposition field;
                   (iii) §0a's "fourteen paths" is demoted to a
                   Researcher expectation, with M3b's measurement
                   named authoritative.
    Spec file      specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    Author         Researcher (Claude)
    Date           2026-08-24
    Base           main @ 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    Source         science/govdebt-register-gap-01 @
                   e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    Branch         science/integrate-govdebt-register-gap, cut from
                   the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Protocol       Instantiates the closed STALE-SOURCE transport
                   protocol approved and executed as
                   P2-XI-LEDGER-01-INTEG v1 (sha256
                   83884d351133e28ee0581b1ead3ee026f1150b48359528d4be
                   0729fa6988ae9d). The source predates the Base: it
                   forked at 9af94a4a… and main has since advanced by
                   the clarification landing and its integration, so
                   M3b's main-side sweep is NON-VACUOUS and is this
                   task's load-bearing protection. The one MODIFIED
                   path is handled as in P2-XI-RULINGS-02-INTEG v1.

---

## 0. What this task is and is not

**This task transports one executed, reviewed result to `main` and
does nothing else.** Under Rule 17 it adds no classification the
reviewed result did not carry.

The arriving result is the `G-18` governance-debt entry — *no landed
index of the repository's registers and their stated scopes* —
disposition `OPEN`, together with its specification, its
pre-execution review, and its execution report.

- **The entry arrives with disposition `OPEN` and no other.** The
  Reviewer's determination was `OPEN` CONCUR, `SPECIFIABLE` NOT
  ESTABLISHED. This task does not restate, upgrade, downgrade or
  gloss the disposition, and does not mark the entry closed —
  the register's own text provides that no entry is closed by being
  written down.
- **The entry registers no open item and proposes no register.** It
  records a mechanism gap. This task does not read it as, or
  represent it as, a resolution of where future XI-line open items
  are registered — which the PI's 2026-08-24 ruling expressly left
  undecided.
- It does not begin, schedule, constrain or prioritise the Q-M3
  check, the Q-M2 scope assessment, or the registered
  representation-stability inquiry.
- It does not move the source branch or any ref beyond the two this
  spec authorizes (the integration branch and main).

## 0a. Two stale-source facts, recorded because they are load-bearing

Measured by the Researcher on a clean clone, 2026-08-24, and
re-measured by the Executor at M1 and M3b:

1. The source forked at `9af94a4a…`. Main has since advanced to
   `0c01fc7f…` by the clarification landing and its integration —
   including the issued clarification, the register-routing decision
   record, `DECISION_LOG.md` carrying the open-item registration, and
   the preceding tasks' artifacts. The Researcher measured fourteen
   main-side changed paths and expects none of them in the source's
   contributed set, so that each falls to the main-preservation
   sweep. **The Executor re-measures the authoritative set at M3b;
   the number here is an expectation, not a precondition, and a
   different count is not by itself an abort — the manifest, union
   and sweep relations of M3b are what bind.**
2. `docs/GOVERNANCE-DEBT.md`, the source's one modified path, is
   **unchanged on main since the fork**. That is a measurement, not
   an assumption: if it were changed on both sides the union
   classification would place it in the both-changed class and A5
   would fire.

The arriving report also records that its own specification's §0
described the clarification landing branch as standing where it
stopped, which by then it did not. That is a recorded defect of the
arriving task and travels with it unaltered; **this task does not
correct, annotate, or re-litigate it.**

## 1a. The contributed manifest, and the one modified path

The arriving change set contains three added paths and one modified
path. The modified path is `docs/GOVERNANCE-DEBT.md`, whose
modification is the `G-18` append plus its counts-table update, and
whose character is re-verified here by M3b(d) — **not by prefix
alone**, because the counts table sits above the append point and two
of its lines legitimately change. No other modified path is
authorized: any second `M`, or any `D`/`R` status, is A5.

## 2. Measurements

    M1  Pre-merge ref audit, before any write.
        Record the full SHAs of: origin/main; the source branch tip;
        origin/science/xi-clar-01-landing, origin/science/xi-ledger-01
        and origin/science/integrate-xi-clar-01 (refs this task must
        not move). Verify origin/main equals the Base and the source
        tip equals the Source field, both as full-string matches.
        Verify `git merge-base main <source>` equals
        9af94a4a11cd06e90ef2d24183565412b4043c6a — the source does
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
          docs/GOVERNANCE-DEBT.md
              expected b7ff84e929e7f333b122d51fa3083d3ad73e2c44396b2ff84f1dbcdef817206b
          specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
              expected 815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c
          reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
              expected 76bffe973bd9d2cabfe63d7f03e135d93ca9ed61ad509cba7d7317c956935fe5
          reports/2026-08-29T1715Z_govdebt-register-gap.md
              expected b50be869554b781e84d4a23c463fc78030444558f54be76afe9bed452ef61e7c
        (Digests measured by the Researcher from the source tip on a
        clean clone, 2026-08-24; M3 re-measures them from the merge
        product.)

    M3b Fork-aware merge-hazard audit, from the merge product.
        Let FORK = the merge-base measured at M1 (expected
        9af94a4a…).
        (a) Contributed path set. Measure
            `git diff --name-status FORK..<source>`. Record verbatim.
            Pre-registered expectation: the three added M3 paths with
            status A, plus docs/GOVERNANCE-DEBT.md with status M —
            four entries, nothing else. Any other path, or any status
            outside {A for the three, M for GOVERNANCE-DEBT}, is A5 —
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
            P_overlap is empty — recorded as a measured comparison
            over the classified union, not inferred from fork
            distance. **docs/GOVERNANCE-DEBT.md must classify (1,0):
            if it classifies (1,1) the counts table has been changed
            on both sides and A5 fires.**
        (c) Main-preservation sweep, NON-VACUOUS here. For each path
            in P_main not in P_source, compare the merge product's
            blob id against the Base's, pairwise; record each pair.
            Any inequality is A5. This is what protects the landed
            clarification, the register-routing decision record,
            `DECISION_LOG.md` with the open-item registration, and
            the preceding tasks' artifacts from being walked back by
            a source that forked before them.
        (d) Structure verification of the one modified path.
            Prefix alone is NOT the test here, because the counts
            table sits above the append point and legitimately
            changes. Verify instead, from the merge product:

              (d1) BYTE GOVERNANCE. The file's byte content equals
                   the source's byte content for that path (covered
                   by M3; restated here as the governing check for
                   this limb).

              (d2) HEADING SEQUENCE, against the Base. Extract the
                   ordered sequence of `## \`G-` headings from the
                   Base, call it H_B, and from the merge product,
                   call it H_P, each as a list of heading lines in
                   file order. Require exactly

                       H_P = H_B ++ [the `G-18` heading]

                   i.e. H_B is an ordered prefix of H_P and H_P has
                   exactly one further element, the `G-18` heading.
                   This establishes in one comparison that no Base
                   heading is removed, renamed, reordered or
                   duplicated and that exactly one is added. Record
                   both sequences' lengths and the differing element.

              (d3) COUNTS TABLE, reconstructed from entry fields.
                   A heading carries an identifier and NOT a
                   disposition, so the table is not checkable against
                   headings. For each `G-*` entry in the product,
                   read that entry's own landed `Disposition:` field
                   from its body. Reconstruct the per-disposition
                   identifier lists and the entry total independently
                   from those entry-level fields. Then compare the
                   reconstruction with the counts table as landed:
                   each disposition's identifier list must match as
                   an exact set AND in the table's stated order, each
                   per-disposition count must equal its list length,
                   and the entry total must equal the number of
                   entries measured. Record the reconstruction and
                   the table side by side. An entry whose
                   `Disposition:` field cannot be read is A5, not a
                   default assignment.

              (d4) NO OTHER BASE LINE CHANGED. Outside the counts
                   table and the appended `G-18` entry, no Base line
                   is changed; measured by diff and reported as the
                   set of changed line ranges with their content.

            Any failure of d1–d4 is A5.

    M3c Arrival-state verification of the entry.
        From the merge product, verify and quote verbatim:
        (i)   `G-18` carries `Disposition: OPEN` and no other
              disposition;
        (ii)  the entry's two disclaimer sentences are present — that
              it registers no open item and proposes no register, and
              that it is not closed by being written down;
        (iii) the entry does not state that no register admits the
              representation-stability item, and does not state that
              the item's routing is unresolved.
        Any failure is A5. State the normalization used for each
        quotation, or state that none was applied.

    M4  Suite, on a full (non-shallow) tree, after M2.
        Run the suite at the base and at the post-merge integration
        tree. Record both results verbatim and the tested tree's SHA,
        T.

    M4b Report commit and final tip.
        Write reports/<UTC>_govdebt-register-gap-integ.md recording
        M1 through M4 and nothing later. The report does not state
        its own commit SHA: it names T and records that it is itself
        the next commit on T. Commit it; the tip after this commit is
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
        9af94a4a… as a full-string match; the source tip equals the
        Source field.
    C2  (M1b, M2) M_merge has exactly two parents: the M1b tip and
        the source tip; the M1b tip descends from the base by exactly
        two commits (the spec, then its review); the spec's sha256
        equals the digest the review declares, as recorded at M1b.
    C3  (M3) Every digest equals its expected value, as full-string
        matches recorded in the report.
    C3b (M3b) The contributed set equals the four-entry manifest with
        its stated statuses; the union classification assigns each
        P_union path to exactly one class with its blob rule
        satisfied, with GOVERNANCE-DEBT in (1,0); the measured
        P_overlap is empty; the main-preservation sweep records
        product blob equal to Base blob for each swept path,
        pairwise; and d1–d4 each pass with their measured values
        recorded — d2 with both heading sequences and the differing
        element, d3 with the reconstruction and the landed table side
        by side, d4 with the changed line ranges and their content.
    C3c (M3c) All three arrival-state checks pass, each with its
        quoted text and its stated normalization.
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
        from it; would restate, upgrade, downgrade or gloss the
        entry's disposition; would mark the entry closed; would read
        the entry as resolving where future XI-line open items are
        registered; would correct or annotate the arriving report's
        recorded defect; or would begin, schedule, constrain or
        prioritise any authorized or registered inquiry. STOP;
        report.
    A5  M3b finds a contributed path or status outside §1a's
        manifest, a both-changed path, a source-unchanged path whose
        product blob differs from the Base's, a main-unchanged
        contributed path whose product blob differs from the
        source's, or any failure of M3b(d); or M3c finds any failure.
        STOP; report the path and all applicable blob ids — for a
        both-changed path: fork, source, Base, AND product. Do not
        repair the merge inside this task.

## 5. Deliverables

    The integration branch: the M1b spec and review commits,
        M_merge, the report (through M4), and the post-push M5
        addendum (branch-only)
    specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md and its
        SHA-bound review, landed at M1b
    main advanced by fast-forward to H_integ
    reports/<UTC>_govdebt-register-gap-integ.md — M1 through M4
        outputs as matched text, every digest in full, the M3b path
        sets, blob-id pairs and the d1–d4 limb results including both
        heading sequences and the counts reconstruction, and the M3c
        quotations verbatim; M5 ref values in the branch-only
        addendum; any A that fired recorded wherever the stop
        occurred

END OF SPECIFICATION
