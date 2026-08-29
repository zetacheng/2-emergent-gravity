# SPECIFICATION — P2-XI-CLAR-01-LANDING: verbatim landing of the issued Ruling-2 scope clarification and its document review

    Task ID        P2-XI-CLAR-01-LANDING
    Version        v2 — revises v1 (sha256 277848701e5d49ad652e47612f
                   a1a61f09bb4556f980a4c674a41deabe2978f1) per Reviewer
                   verdict REVISE BEFORE EXECUTION: v1's M6 folded
                   suite, report, commit and push into one step and
                   then required the report to record "M1–M6", which
                   includes evidence that exists only after the report
                   is committed. v2 splits it into M6a (suite), M6b
                   (report, recording M1–M6a only), and M6c (push and
                   post-commit evidence, branch-only), and restates
                   C6. The Reviewer's concurrence with §1's filing
                   structure is recorded; A2 is discharged.
    Spec file      specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md
    Author         Researcher (Claude)
    Date           2026-08-24
    Base           main @ 9af94a4a11cd06e90ef2d24183565412b4043c6a
    Branch         science/xi-clar-01-landing, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Template       Instantiates the landing structure approved and
                   executed as P2-XI-RULINGS-02-LANDING-01 v3 (sha256
                   c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da
                   4750f926a14cc5), including its mandatory pre-write
                   correspondence scan (M2b) and its report/final-tip
                   sequencing (M6). Differences: this document is a
                   CLARIFICATION, not a ruling — §1 states how that is
                   filed; the subject-pin limb is absent because this
                   document's subject is a landed ruling, not an
                   unlanded artifact; expected digests are this task's
                   own.

---

## 0. What this task is and is not

**This task transports.** It lands the issued
`P2-XI-RULINGS-02-CLARIFICATION-01` byte-exact with its
document-review artifact and register entries, and adjudicates
nothing.

- The clarification changes no ruling of `P2-XI-RULINGS-02`, issues
  no membership ruling, and authorizes no task beyond those already
  authorized — its own words. This landing adds nothing to that.
- The two OPEN ledger rows remain OPEN.
- **The named open item the clarification requires** — the
  family-wide representation-stability inquiry, linked to
  `P2-FIERZSUM-01 §8`, with the clarification's escalation
  condition — **is registered by M4 of this task**, because the
  clarification directs its registration. Registration is not
  authorization: nothing here commissions that inquiry, assigns it
  priority beyond the clarification's own words, or begins it.
- No step begins, schedules, or constrains the Q-M3 check or the
  Q-M2 scope assessment.

## 0a. Provenance of the bytes this task lands

    Issued document      P2-XI-RULINGS-02-CLARIFICATION-01, issued by
                         the PI in session, 2026-08-23, with
                         review-declared identity SHA-256
                         0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22.
    Recovery             The session upload did not materialize on
                         disk. The Researcher reconstructed a
                         candidate byte sequence from the session
                         rendering and verified it: its sha256 equals
                         the review-declared identity. THE HASH MATCH
                         IS THE VERIFICATION; a non-match would have
                         been a STOP.
    Derived git blob id  1786124bbe3bfa02809d83c2890d0800e0d3edd8,
                         pre-registered as a secondary check.
    Review artifact      2026-08-23_review_P2-XI-RULINGS-02-CLARIFICATION-01.md,
                         ChatGPT, verdict "FIT FOR RECORDING",
                         self-bound to the digest above. No
                         pre-committed hash of the review artifact
                         exists; its sha256 is recorded at landing
                         (M2), provenance transmitted-in-session. The
                         PI supplies its original bytes.

## 1. Landing structure

    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
        The issued bytes, byte-exact. This file is the clarification.

    decisions/2026-08-24-xi-rulings-02-clarification-01.md
        The register record in the two parts decisions/README.md
        requires. PART 1: owner, date, effect, scope; the canonical
        text's location with its SHA-256 and blob id; the canonical
        decision key; and an explicit statement that this document is
        a CLARIFICATION of P2-XI-RULINGS-02 Ruling 2's scope and not
        an independent ruling. PART 1 does not paraphrase; where it
        refers to content it does so by section name and quotation.
        PART 2 reproduces the document review verbatim with its
        sha256 from M2.

    Canonical decision key: 2026-08-24-xi-rulings-02-clarification-01

    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
        The review artifact as a standalone landed original.

    STRUCTURE DISPOSITION, flagged for the Reviewer: a clarification
    is filed in decisions/ under the same two-file layout as a
    ruling, with its clarification status stated in PART 1 rather
    than by a separate directory. If the Reviewer judges a
    clarification to require a distinct filing location, A2 fires and
    the question returns to the PI.

## 2. Measurements

    M1  Byte identity of the issued document, before any write.
        sha256sum and git hash-object over the handed-over file;
        record both in full. Disagreement with §0a is A1.

    M2  Byte identity of the review artifact.
        sha256sum over the handed-over review file; record it.
        Extract the SHA-256 the review declares itself bound to;
        record the string verbatim.

    M2b Landed-authority correspondence scan, before any write.
        Resolve at the Base, recording reference, landed text
        (path:line, quoted), and RESOLVES / DOES NOT RESOLVE:
          (1) P2-XI-RULINGS-02, Ruling 2 — the parent whose scope is
              clarified: decisions/P2-XI-RULINGS-02.issued.md;
          (2) P2-FIERZSUM-01 §8's representation-stability
              disclosure, to which the open item is to be linked;
          (3) P2-FIERZSUM-01.md:451-460, the membership criterion the
              Q-M3 check feeds. **Record verbatim that the landed
              criterion is written "For every admissible decoupling
              α", and that the clarification scopes the authorized
              task to the landed decoupling, leaving the family-wide
              residue to the registered open item. This is a recorded
              scope relation, not a conflict and not a reconciliation
              — do not reword either text.**
        Any substantive conflict, or an item that does not resolve,
        is A3. Landing without a completed scan is not a permitted
        execution path.

    M3  Landing.
        Cut the branch; commit this specification, then its SHA-bound
        review (spec → review, binding verified before the spec
        commit); then land the §1 files. Record every commit SHA.

    M4  Open-item registration, as the clarification directs.
        Register the family-wide representation-stability inquiry as
        a named open item in the repository's open-item register, at
        minimum: an identifier; the question, stated no more broadly
        or narrowly than the clarification states it; the link to
        P2-FIERZSUM-01 §8; the escalation condition quoted verbatim
        from the clarification; status REGISTERED, NOT AUTHORIZED;
        and the note that its family membership is an unlanded
        model-level choice. Record the register path used and why it
        is the applicable register.

    M5  Register append.
        Append to DECISION_LOG.md: decision key, issued-file path,
        issuance SHA-256, review verdict "FIT FOR RECORDING", and the
        open item's identifier. Append-only; verify the base's bytes
        are an exact byte-prefix of the product.

    M6a Suite, on a full (non-shallow) tree.
        Run the suite at the base and at the post-M5 tree. Record
        both results verbatim and the SHA of the tested tree, T.

    M6b Report and final tip.
        Write reports/<UTC>_xi-clar-01-landing.md recording M1
        through M6a — and nothing later, since nothing later has
        occurred. The report does not state its own commit SHA: it
        names T, the tip it is committed onto, and records that it
        is itself the next commit on T. Commit it. The resulting tip
        is H_final, measured externally after the commit exists;
        H_final is not named inside the report.

    M6c Push and post-commit evidence, branch-only.
        Verify by diff that H_final differs from T only by the
        report artifact. Push the branch per BRANCHING_POLICY.md
        science/* scope. Record H_final's SHA, the diff result, and
        the push result in an addendum commit on this branch ONLY,
        or in the execution summary returned to the PI; neither is
        required to exist inside the M6b report. Integration is a
        separate task and is not performed here.

## 3. Acceptance criteria

    C1  (M1) The digest equals
        0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
        and the blob id equals
        1786124bbe3bfa02809d83c2890d0800e0d3edd8, reproduced under
        re-measurement from the final tip.
    C2  (M2) The SHA-256 the review declares equals C1's digest as an
        exact string match; the review lands byte-identical.
    C2b (M2b) Each scan item carries a finding with quoted landed
        text; item (3)'s scope relation is recorded verbatim; no item
        unresolved; no substantive conflict.
    C3  (M3) Commit order is spec, its review, then the landing
        commits, nothing interleaved; the register record's
        quotations are byte-identical to the issued file's
        corresponding passages.
    C4  (M4) The open item exists with every element listed, its
        escalation condition byte-identical to the clarification's,
        and status REGISTERED, NOT AUTHORIZED.
    C5  (M5) The DECISION_LOG.md base bytes are an exact byte-prefix
        of the product.
    C6  (M6a, M6b, M6c) No test fails on T that passes at the base;
        the M6b report records M1 through M6a and no later
        measurement, names T, and does not assert its own SHA or
        H_final; and H_final differs from T only by the report
        artifact, verified by diff at M6c.

## 4. Abort conditions

    A1  Any digest measured in M1 or M2 disagrees with §0a, before
        any write. STOP; no branch is created; report the measured
        digest.
    A2  DISCHARGED for v2: the Reviewer concurs that a clarification
        may use the decisions/ two-file layout with its clarification
        status stated in PART 1 (review of 2026-08-23). The condition
        remains only against regression: if the structure as executed
        departs from §1, STOP; the question returns to the PI.
    A3  The M2b scan records a substantive conflict or an unresolved
        item, or any later step surfaces a conflict between the
        issued clarification and landed text. STOP; report verbatim;
        do not reconcile. Absence of a completed M2b record is
        itself this abort.
    A4  Transport fidelity: any register-record or open-item passage
        that would state the clarification materially more narrowly,
        more broadly, or more specifically than the issued text,
        without independent landed authority. STOP; report the
        divergent wording verbatim.
    A5  Any step would begin, schedule, constrain, or prioritise the
        Q-M3 check, the Q-M2 scope assessment, or the registered
        representation-stability inquiry. STOP; registration is not
        authorization.

## 5. Deliverables

    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md (byte-exact)
    decisions/2026-08-24-xi-rulings-02-clarification-01.md
    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
    the registered open item (M4), at the register path M4 records
    DECISION_LOG.md (append)
    specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md and its SHA-bound
        review, committed at M3 in spec → review order
    reports/<UTC>_xi-clar-01-landing.md (M6b), recording M1–M6a
    the M6c post-commit evidence, branch-only or in the execution
        summary
    Branch pushed per BRANCHING_POLICY.md science/* scope (M6c);
        integration is a separate task.

END OF SPECIFICATION
