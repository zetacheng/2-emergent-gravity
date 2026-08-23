# SPECIFICATION — P2-XI-RULINGS-02-LANDING-01: verbatim landing of the issued Q-M2/Q-M3 disposition ruling and its document review

    Task ID        P2-XI-RULINGS-02-LANDING-01
    Version        v3 — revises v2 (sha256 9ae86eb9e9a5af1ac94112851f
                   59a0973ab9aee145c4fcfb1ec9cc4061ee5749) per Reviewer
                   verdict REVISE BEFORE EXECUTION on v2: M2b(5) read
                   the ruling's subject artifact from a movable branch
                   name with no frozen commit identity. v3 pins the
                   subject at science/xi-ledger-01 @
                   8f9edfead214b5bb3337924c18c5d241274e97c3 (full
                   SHA), splits item (5) into a main-side absence
                   measurement and a source-side pinned-commit
                   extraction with a remote-equality check, and adds
                   A5 for a moved subject ref. v2 had revised v1
                   (sha256 e122dd095a07c50df841acfd8df1cea054a86e09ee
                   7b6061a7f9a91a5a77c06a) per Reviewer
                   verdict REVISE BEFORE EXECUTION: (i) A2 was an
                   abort with no measurement feeding it; v2 adds M2b,
                   a mandatory pre-write correspondence scan resolving
                   each authoritative reference the issued document
                   makes against landed state, so landing proceeds
                   only over a measured no-conflict record — including
                   the explicit chronology fact that P2-XI-LEDGER-01
                   is a completed reviewed measurement on
                   science/xi-ledger-01 and not on main at this Base;
                   (ii) v2 adds M6, closing report/final-tip/push
                   sequencing to match the programme's other tasks.
    Spec file      specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
    Subject pin    The ruling's SCOPE names the two OPEN rows of
                   P2-XI-LEDGER-01. That artifact's authoritative
                   commit for this task is FROZEN here:
                   science/xi-ledger-01 @
                   8f9edfead214b5bb3337924c18c5d241274e97c3
                   (the executed, reviewed, Researcher-verified
                   ledger tip presented to the PI). The branch name
                   is not the referent; the SHA is.
    Author         Researcher (Claude)
    Date           2026-08-23
    Base           main @ 9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Branch         science/xi-rulings-02-landing, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Template       This specification instantiates the landing
                   structure of P2-XI-RULINGS-LANDING-01 v2 (sha256
                   23973a59cba041590f8f461b542ef48348d11212313a28ff9e
                   6c24e2e59c4eee, APPROVE FOR EXECUTION, executed and
                   integrated to main), with the two-file decision
                   layout the Reviewer selected there and the
                   Reviewer-directed guards (A3's transport-fidelity
                   clause) carried over. Differences: the issued
                   document registers no hypothesis and names no
                   carrier, so that template's M3 (carrier extraction)
                   and M4 (Statement SHA) are absent and steps are
                   renumbered; expected digests are this task's own.

---

## 0. What this task is and is not

**This task transports.** It lands the issued PI ruling document
`P2-XI-RULINGS-02`, byte-exact, with its document-review artifact and
register entries, and adjudicates nothing:

- No gate moves; no claim status changes; the two OPEN ledger rows of
  `P2-XI-LEDGER-01` remain OPEN — the issued document itself defers
  membership (its Ruling 1), and this landing adds no disposition.
- The two tasks the issued document authorizes (the Q-M3
  curvature-dependence check, Ruling 2; the Q-M2 scope assessment,
  Ruling 3) are NOT specified, scheduled, or begun by this task. They
  are separate specifications, each subject to the normal
  pre-execution review gate, and each will cite the ruling at its
  landed path.
- Nothing in `science/xi-ledger-01` is touched or integrated here.

## 0a. Provenance of the bytes this task lands

    Issued document      P2-XI-RULINGS-02, issued by the PI in
                         session, 2026-08-23, with review-declared
                         identity SHA-256
                         ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5.
    Recovery             The session upload did not materialize on
                         disk. The Researcher reconstructed a
                         candidate byte sequence from the session
                         rendering and verified it: its sha256 equals
                         the review-declared identity. THE HASH MATCH
                         IS THE VERIFICATION; a non-match would have
                         been a STOP. Recorded so the recovery route
                         is on the record and is not mistaken for
                         reconstruction-from-review, which remains
                         prohibited.
    Derived git blob id  72a6b24c9289efde8a096e4e591ff01728323473
                         (SHA-1, `git hash-object` over the same
                         bytes), pre-registered as a secondary check.
                         A blob id is a different hash function and
                         cannot literally equal a SHA-256; byte
                         identity is discharged by C1.
    Review artifact      2026-08-23_review_P2-XI-RULINGS-02.md,
                         ChatGPT, verdict "FIT FOR RECORDING",
                         self-bound to the issuance SHA-256 above. No
                         independent pre-committed hash of the review
                         artifact exists; its sha256 is computed and
                         recorded at landing (M2), provenance
                         transmitted-in-session. The PI supplies the
                         review file's original bytes with this
                         specification.

Both files are handed to the Executor with this specification. The
Executor verifies both against this section before any write (M1, M2)
and does not retype, reflow, or re-encode either.

## 1. Landing structure

Per the Reviewer-selected two-file decision layout, landed precedent
`decisions/P2-XI-RULINGS-01.issued.md` + `decisions/2026-08-22-xi-rulings-01.md`:

    decisions/P2-XI-RULINGS-02.issued.md
        The issued bytes, byte-exact. This file is the ruling.

    decisions/2026-08-23-xi-rulings-02.md
        The decision-register record, in the two parts
        decisions/README.md requires. PART 1 states: decision owner,
        date, effect, scope; that the ruling's canonical text is the
        issued file above, identified by its SHA-256 and git blob id;
        and the canonical decision key (below). PART 1 does not
        paraphrase the rulings; where it must refer to their content
        it does so by section name ("RULING 1" through "RULING 4",
        "ROUTING") and by quotation. PART 2 reproduces the
        document-review artifact verbatim and records its SHA-256 as
        computed in M2.

    Canonical decision key: 2026-08-23-xi-rulings-02
        Assigned here as filing metadata under the issued document's
        IDENTIFIER clause, which provides that such assignment "does
        not modify this ISSUED TEXT".

    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
        The document-review artifact as a standalone landed original,
        byte-identical to the bytes handed over (M2).

## 2. Measurements

    M1  Byte identity of the issued document, before any write.
        sha256sum over the handed-over issued file; record the
        digest. git hash-object over the same file; record the blob
        id. Both recorded as matched text (the full digest), not as
        a boolean. Disagreement with §0a is A1.

    M2  Byte identity of the review artifact.
        sha256sum over the handed-over review file; record the
        digest (its first recorded hash — provenance per §0a).
        Extract from inside the review artifact the SHA-256 it
        declares itself bound to; record the extracted string
        verbatim.

    M2b Landed-authority correspondence scan, before any write.
        Resolve, at the Base, each authoritative reference the
        issued document makes, recording for each the reference, the
        landed text located (path:line, quoted), and a per-item
        finding RESOLVES / DOES NOT RESOLVE:
          (1) P2-XI-RULINGS-01 (the ROUTING clause the issued
              document extends): decisions/P2-XI-RULINGS-01.issued.md
              present with its recorded identity;
          (2) P2-FIERZSUM-01.md:451-460 (Ruling 2's named criterion):
              the passage exists and states the
              curvature-dependence inclusion criterion;
          (3) DET-01 (Ruling 3's stated-not-resolved item): the
              landed adjudication NOT DETERMINABLE is locatable;
          (4) the O(1)-versus-O(N) counting reference (Ruling 3):
              its landed carrier via Q-M2
              (P2-XI-B0a_induced-xi-scope-assessment.md:615-618);
          (5a) Main-side chronology: measure that the Base does not
              contain the P2-XI-LEDGER-01 artifact
              (derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
              absent at the Base), recording the command and output.
          (5b) Source-side subject identity: resolve
              refs/heads/science/xi-ledger-01 by `git ls-remote` and
              verify it equals the Subject pin
              8f9edfead214b5bb3337924c18c5d241274e97c3 as a
              full-string match; inequality is A5. Then extract the
              two OPEN rows DIRECTLY from the pinned commit
              (`git show <pin>:<path>`), quoting them verbatim with
              their OPEN(Q-M2)/OPEN(Q-M3) statuses and em-dash
              cells.
          (5c) The chronology fact, recorded verbatim in the
              register record and the report, now with its unique
              referent: P2-XI-LEDGER-01 exists as a completed
              reviewed measurement at science/xi-ledger-01 @
              8f9edfead214b5bb3337924c18c5d241274e97c3 and is NOT
              landed on main at this task's Base; this landing does
              not integrate it. This is factual chronology, not a
              conflict and not a reinterpretation of the ruling.
        Any substantive conflict found is A2, before any write. An
        item that does not resolve is likewise A2. The scan's output
        is the measured record that A2 evaluates; landing without
        the scan is not a permitted execution path.

    M3  Landing.
        Cut the branch; commit this specification, then its
        SHA-bound pre-execution review (spec → review, binding
        verified before the spec commit); then land the §1 files.
        Record every commit SHA.

    M4  Register append.
        Append one entry to DECISION_LOG.md recording: decision key,
        issued-file path, issuance SHA-256, review verdict string
        "FIT FOR RECORDING". Append-only; verify the base's
        DECISION_LOG.md bytes are an exact byte-prefix of the
        product.

    M5  Suite, on a full (non-shallow) tree.
        Run the suite at the base and at the post-M4 branch tip.
        Record both results verbatim, and the SHA of the tree the
        branch-side run used.

    M6  Report, final tip, push.
        Write reports/<UTC>_xi-rulings-02-landing.md only after
        M1–M5, recording every M output (including the full M2b
        scan). Commit it; the branch tip after this commit is the
        task's final tip; record its SHA; the tip differs from the
        M5-tested tree only by the report artifact, verified by
        diff. Then push the branch per BRANCHING_POLICY.md science/*
        scope. Integration is a separate task.

## 3. Acceptance criteria

    C1  (M1) The recorded sha256 digest equals
        ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
        and the recorded blob id equals
        72a6b24c9289efde8a096e4e591ff01728323473, and the landed
        file decisions/P2-XI-RULINGS-02.issued.md reproduces both
        under re-measurement from the branch tip.
    C2  (M2) The SHA-256 the review artifact declares equals the
        issuance SHA-256 in C1, as an exact string match on the
        digest, and the review file lands byte-identical to the
        handed-over bytes under re-measurement from the branch tip.
    C2b (M2b) Each scan item carries a finding with its quoted
        landed text; (5a)'s absence measurement and (5b)'s
        remote-equality match and pinned-commit extraction are
        recorded; (5c)'s chronology fact appears verbatim, with the
        full-SHA referent, in both the register record and the
        report; no item is left unresolved and no substantive
        conflict is recorded.
    C3  (M3) The branch's commit sequence is: spec, its review, then
        the landing commits, nothing interleaved; the register
        record's quotations of ruling text are byte-identical to the
        issued file's corresponding passages.
    C4  (M4) The DECISION_LOG.md diff is append-only: the base bytes
        are an exact byte-prefix of the product.
    C5  (M5) No test fails on the M5-tested tree that passes at the
        base.
    C6  (M6) The final tip differs from the M5-tested tree only by
        the report artifact, verified by diff; the report contains
        the full M2b scan.

## 4. Abort conditions

    A1  Any digest measured in M1 or M2 disagrees with §0a before
        any write occurs. STOP; no branch is created; report the
        measured digest.
    A2  The M2b scan records a substantive conflict or an
        unresolved item, or any later step surfaces a conflict
        between the issued ruling and landed repository text. STOP;
        report the conflict verbatim; do not reconcile inside this
        task. The scan is mandatory: absence of a completed M2b
        record is itself this abort.
    A3  Transport fidelity: any register-record passage that would
        state the rulings materially more narrowly, more broadly, or
        more specifically than the issued text, without independent
        landed authority. STOP; report the divergent wording
        verbatim.
    A4  Any step would begin, schedule, or constrain either task the
        ruling authorizes. STOP; those are separate specifications.
    A5  refs/heads/science/xi-ledger-01 does not resolve to the
        Subject pin at M2b(5b). STOP before any write; report the
        measured SHA; the subject-identity question returns to the
        PI. Do not read the moved tip and do not substitute it for
        the pin.

## 5. Deliverables

    decisions/P2-XI-RULINGS-02.issued.md          (byte-exact)
    decisions/2026-08-23-xi-rulings-02.md         (register record)
    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
    DECISION_LOG.md                               (append)
    specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md and its
        SHA-bound review, committed at M3 in spec → review order
    reports/<UTC>_xi-rulings-02-landing.md — every M output as
        matched text, every digest in full, the full M2b scan, any A
        that fired (M6)
    Branch pushed per BRANCHING_POLICY.md science/* scope (M6);
        integration is a separate task and is not performed here.

END OF SPECIFICATION
