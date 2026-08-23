# SPECIFICATION — P2-XI-LEDGER-01-COUNT-ADDENDUM: branch-only correction of a self-referential count in the ledger execution report

    Task ID        P2-XI-LEDGER-01-COUNT-ADDENDUM
    Version        v2 — revises v1 (sha256 0ac5597f09dcf7ba32a64a4a67
                   08b2d174f80a8fb861b17dac951a769d369110) per Reviewer
                   verdict REVISE BEFORE EXECUTION: v1's C3 required
                   exactly one commit changing one path from the Base,
                   while its own Deliverables required the spec and
                   review to be committed on the same branch first —
                   an accounting contradiction. v2 names four commit
                   points (Base, B_task, H_addendum, H_final) and
                   measures each interval separately. The Reviewer's
                   concurrence with §0a's execution-layer category is
                   recorded; A2 is discharged.
    Spec file      specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
    Author         Researcher (Claude)
    Date           2026-08-23
    Base           science/xi-ledger-01 @
                   8f9edfead214b5bb3337924c18c5d241274e97c3
                   (the executed, reviewed, Researcher-verified ledger
                   tip; NOT main)
    Branch         science/xi-ledger-01 — this task appends commits to
                   the existing unintegrated source branch. No new
                   branch is cut. Commit points, named for the
                   measurements below:
                     Base        8f9edfea… (above)
                     B_task      Base + spec commit + review commit
                     H_addendum  B_task + the addendum commit
                     H_final     H_addendum + the execution report
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.

---

## 0. What this task is and why it is separate

`P2-XI-LEDGER-01`'s execution report states, at
`reports/2026-08-23T0434Z_xi-ledger-01.md:376-377`:

> **This task modifies no pre-existing path.** `git diff --name-status` against
> the Base shows five entries, all `A`.

The claim's substance — that the task modifies no pre-existing path —
is TRUE at both relevant times and is not being corrected. The count
is the defect: five was correct for the tree at the moment the
sentence was written, and six for the landed branch tip, because the
report's own commit added the sixth entry. This is the
SELF-REFERENTIAL COUNT class of the landed defect register, in its
temporal variant.

**This is a correction, not a transport and not a re-execution.** It
is separate from the integration task because a transport task adds
no classification the reviewed result did not carry, and rewording a
landed report inside a merge would be exactly that.

## 0a. Authority and the pin consequence

    PI direction, in session 2026-08-23, on the disposition offered
    at Researcher verification: the executor adds a branch-only
    clarification of the count's temporal scope before integration.
    This is an execution-layer disposition — the correction is to the
    executor's own report, on an unintegrated branch, and changes no
    model-level content, no measurement, and no verdict. It is
    recorded here rather than in decisions/ on that basis. DISPOSITION
    FLAGGED FOR THE REVIEWER: if the Reviewer judges this to require a
    canonical decision record instead, A2 fires and the question
    returns to the PI.

    PIN CONSEQUENCE, recorded because it is load-bearing: the Base of
    this task, 8f9edfead214b5bb3337924c18c5d241274e97c3, is the
    subject pin quoted in the landed register record
    decisions/2026-08-23-xi-rulings-02.md and in the landing report,
    identifying the ledger state on which P2-XI-RULINGS-02 was issued.
    This task moves the BRANCH TIP off that commit; it does not and
    cannot alter the commit. The pin remains valid and continues to
    denote the ruling's subject. The later ledger integration
    specification must therefore state its source as "the pin plus
    this addendum" and must not describe the addendum-bearing tip as
    the state the ruling was issued on. Nothing in this task edits,
    reinterprets, or annotates the landed pin.

## 1. Measurements

    M1  Pre-write audit.
        Record the full SHAs of origin/science/xi-ledger-01 and
        origin/main. Verify the branch tip equals the Base above as a
        full-string match; a moved tip is A1. Verify main does not
        contain the ledger artifact (the branch remains
        unintegrated); if it does, A1.

    M2  Extract the subject text.
        From the Base, extract byte-exact
        `reports/2026-08-23T0434Z_xi-ledger-01.md` lines 376-377 and
        record them. If the extracted bytes do not contain the token
        `five entries`, A3; do not search for another location.

    M2b Provenance commits, before the addendum.
        Commit this specification, then its SHA-bound pre-execution
        review, in that order (spec → review), on
        science/xi-ledger-01. Before the spec commit, verify the spec
        file's sha256 equals the digest the review declares itself
        bound to, recording both strings; record the review file's
        sha256 at commit as its first recorded digest, provenance
        transmitted-in-session. Record the resulting tip as B_task.
        Nothing else is committed between them.

    M3  The correction, as an appended clarification.
        Append to that report a dated addendum section — appended at
        the end of the file, leaving lines 376-377 as they stand —
        stating, at minimum: that the count sentence was written
        before the report's own commit and is correct for the tree at
        writing; that the landed branch tip carries six entries, the
        sixth being the report itself; that the substantive claim (no
        pre-existing path modified) holds at both times; and the
        measured `git diff --name-status` output against the Base as
        of this addendum. The original lines are NOT edited: the
        historical record is preserved and clarified, not rewritten.
        Commit as a single commit on science/xi-ledger-01.

    M4  Post-write verification, by interval.
        (a) Base..B_task: exactly two commits, the spec then its
            review, changing exactly those two paths.
        (b) B_task..H_addendum: exactly one commit, changing exactly
            one path, `M` on
            reports/2026-08-23T0434Z_xi-ledger-01.md, nothing else.
        (c) Content: at H_addendum, lines 376-377 are byte-identical
            to M2's extraction, and the report file's bytes AS THEY
            STAND AT THE BASE are an exact byte-prefix of the file at
            H_addendum.
        Record each interval's `git diff --name-status` output and
        each commit SHA.

    M5  Suite, on a full (non-shallow) tree.
        Run the suite at the Base and at H_addendum. Record both
        verbatim, and the SHA of the tree the branch-side run used.

    M6  Execution report, final tip, push.
        Write reports/<UTC>_xi-ledger-01-count-addendum.md only after
        M1–M5, recording every M output. Commit it; the tip after
        this commit is H_final; record its SHA. H_final differs from
        the M5-tested tree (H_addendum) only by the execution-report
        artifact, verified by diff; no suite re-run is required and
        the report states this. Then push the branch.

## 2. Acceptance criteria

    C1  (M1) The branch tip equals the Base; main does not contain
        the ledger artifact.
    C2  (M2, M4c) Lines 376-377 at H_addendum are byte-identical to
        the M2 extraction, and the report file's Base bytes are an
        exact prefix of its bytes at H_addendum.
    C3  (M2b, M3, M4a, M4b) Base..B_task is exactly two commits, spec
        then review, on exactly those two paths; B_task..H_addendum
        is exactly one commit modifying exactly the report path.
    C4  (M3) The addendum states the temporal scope of the count and
        the measured diff output, and asserts no change to any
        measurement, verdict, or membership status.
    C5  (M5) No test fails at H_addendum that passes at the Base.
    C6  (M6) H_final differs from H_addendum only by the
        execution-report artifact, verified by diff.

## 3. Abort conditions

    A1  The branch tip does not equal the Base, or main already
        contains the ledger artifact. STOP before any write; report
        the measured values.
    A2  DISCHARGED for v2: the Reviewer concurs that §0a's
        execution-layer category is correct and that no canonical
        decision record is required (review of 2026-08-23). The
        condition remains only against regression: if the disposition
        as executed departs from §0a, STOP; the question returns to
        the PI.
    A3  M2's extraction does not contain `five entries`, or the
        report path or line numbers do not resolve at the Base.
        STOP; report the extracted or missing text.
    A4  Any step would edit lines 376-377, any other landed line of
        the report, or any content of the ledger derivation, script,
        or tests; or would change any path outside the four this
        task creates or modifies (the spec, its review, the ledger
        report, the execution report). STOP; report.
    A5  Any step would touch main or any branch other than
        science/xi-ledger-01. STOP; report.

## 4. Deliverables

    reports/2026-08-23T0434Z_xi-ledger-01.md — one appended addendum
        section, original lines untouched
    specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md and its
        SHA-bound review, committed on the same branch before the
        addendum commit, in spec → review order (M2b, yielding
        B_task)
    reports/<UTC>_xi-ledger-01-count-addendum.md — every M output as
        matched text, each interval's diff output and commit SHA; any
        A that fired (M6, yielding H_final)
    Branch pushed per BRANCHING_POLICY.md science/* scope;
        integration remains a separate task and is not performed here.

END OF SPECIFICATION
