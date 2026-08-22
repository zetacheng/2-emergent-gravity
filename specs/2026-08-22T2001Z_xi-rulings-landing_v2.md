# SPECIFICATION — P2-XI-RULINGS-LANDING-01: verbatim landing of the issued PI ruling document, its document review, and the Ruling-2 hypothesis registration

    Task ID        P2-XI-RULINGS-LANDING-01
    Version        v2 — revises v1 (sha256 5eeba556b17678e94a954e423c
                   f56eb07c465e089361773696a0d9787a1a0e2a) per Reviewer
                   verdict REVISE BEFORE EXECUTION, 2026-08-22. The v1
                   defect: the H-XI-SIGN-01 statement and falsifier
                   added "spin structure" beyond the issued ruling's
                   words — a transport-fidelity failure of the class
                   §0 itself prohibits. v2 changes: §2 statement, §2
                   falsifier, A4 guard. Reviewer concurrence on the §1
                   structure disposition is recorded; A2 is discharged.
    Spec file      specs/2026-08-22T2001Z_xi-rulings-landing_v2.md
    Author         Researcher (Claude)
    Date           2026-08-22
    Base           main @ 6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Branch         science/xi-rulings-landing-01, cut from the base above
    Review         SHA-bound pre-execution review by the Reviewer (ChatGPT)
                   is required before execution. The review binds to the
                   exact bytes of this file.
    Execution      Executor (Codex) only. The Researcher holds no write
                   access and this specification grants none.

---

## 0. What this task is and is not

**This task transports.** It lands three things and adjudicates nothing:

1. the issued PI ruling document `P2-XI-RULINGS-01`, byte-exact;
2. the document-review artifact bound to those bytes;
3. the H-type hypothesis registration that Ruling 2 of the issued
   document itself directs.

**No gate moves. No claim status changes. No physical quantity is
computed.** Item 3 is not an addition by this specification: the issued
text at its Ruling 2 states the proposition "is to be registered as an
H-type hypothesis, status UNESTABLISHED"; this specification arranges
that registration and nothing beyond it. Under Rule 17 the authority for
item 3 is the issued ruling, cited at the point of use below.

**Ruling 2's forward-terminology effect is out of scope.** No existing
repository text is reworded by this task. Any future rewording proceeds
under the repository's clarification, erratum, or supersession
mechanism, per the issued text.

## 0a. Provenance of the bytes this task lands

    Issued document      P2-XI-RULINGS-01, issued by the PI in session,
                         2026-08-22, with issuance statement:
                         "Issued bytes: SHA-256 1f39b0f9c5cf2cd54fd5a2a0
                         b38fa05ae454bb47a8fd81160f34485a7a2f6941."
    Recovery             The session upload did not materialize on disk.
                         The Researcher reconstructed a candidate byte
                         sequence from the session rendering and verified
                         it: sha256 of the candidate equals the issuance
                         hash. THE HASH MATCH IS THE VERIFICATION — a
                         candidate matching a pre-committed SHA-256 is
                         the issued bytes; a non-match would have been a
                         STOP. This is recorded so that the recovery
                         route is on the record and is not mistaken for
                         reconstruction-from-review, which remains
                         prohibited.
    Derived git blob id  f793f9fd866f563480fbec6168553a2b967aea8f
                         (SHA-1, `git hash-object` over the same bytes),
                         pre-registered here as a secondary check. NOTE:
                         a git blob id is a different hash function and
                         cannot literally equal a SHA-256; the issuance
                         instruction's byte-identity requirement is
                         discharged by C1 below, and the blob id is the
                         repository-native fingerprint of the same bytes.
    Review artifact      2026-08-22_review_P2-XI-RULINGS-01.md, ChatGPT,
                         verdict "FIT FOR RECORDING", self-bound to the
                         issuance SHA-256. No independent pre-committed
                         hash of the review artifact itself exists; its
                         SHA-256 is computed and recorded at landing
                         (M2), with provenance "transmitted by the PI in
                         session, 2026-08-22".

The issued bytes and the review bytes are handed to the Executor with
this specification. The Executor verifies both against this section
before any write (M1, M2) and does not retype, reflow, or re-encode
either.

## 1. Landing structure

The `decisions/` register requires one file per decision in two parts
(`decisions/README.md`). The issuance requires the issued text to land
byte-exact, which excludes wrapping it inside another document. These
are jointly satisfied by:

    decisions/P2-XI-RULINGS-01.issued.md
        The issued bytes, byte-exact. This file is the ruling.

    decisions/2026-08-22-xi-rulings-01.md
        The decision-register record, in the two parts
        decisions/README.md requires. PART 1 states: decision owner,
        date, effect, scope; that the ruling's canonical text is the
        issued file above, identified by its SHA-256 and git blob id;
        and the canonical decision key (below). PART 2 reproduces the
        document-review artifact verbatim and records its SHA-256 as
        computed in M2. PART 1 does not paraphrase the rulings; where
        it must refer to their content it does so by section name
        ("RULING 1", "RULING 2", "RULING 3", "CROSS-RULING
        CONSISTENCY", "ROUTING") and by quotation.

    Canonical decision key: 2026-08-22-xi-rulings-01
        Assigned here as filing metadata under the issued document's
        IDENTIFIER clause, which provides that such assignment "does
        not modify this ISSUED TEXT". The key is the register file's
        basename, matching the register's existing date-keyed naming.

    reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md
        The document-review artifact as a standalone landed original,
        byte-identical to the bytes handed over (M2). Precedent for a
        non-specification review under reviews/chatgpt/:
        reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md.

    STRUCTURE DISPOSITION, flagged for the Reviewer: the two-file
    decision layout (issued file + register record) is an
    execution-layer structure choice by the Researcher. Under the
    landed rule that Researcher–Reviewer agreement may stand as PI
    agreement for spec structure, Reviewer concurrence suffices; if the
    Reviewer judges it to conflict with decisions/README.md, A2 fires.

## 2. The hypothesis registration (Ruling 2, second RULING block)

    File     assumptions/H-XI-SIGN-01.md, following the structure of
             assumptions/H-EXT-01.md (PART 1 entry; PART 2 review, which
             at landing is marked REVIEW PENDING — the assumption review
             is a follow-on, per the precedent that H-EXT-01's review
             was a distinct artifact).

    ID       H-XI-SIGN-01
    Type     PHYSICAL HYPOTHESIS — directional, falsifiable.
    Status   UNESTABLISHED — NOT ADJUDICATED BY P2-XI-RULINGS-01, which
             fixes ledger language only (its own words).

**Exact statement to be registered (drafted here for review; the landed
bytes of this block are pinned by Statement SHA at M4):**

> In the induced ξ ledger, the sign is driven by coupling structure
> rather than species.

    The statement tracks the issued ruling's own words ("the physical
    proposition that sign is driven by coupling structure rather than
    species"), scoped to the ledger the ruling governs, and adds
    nothing. The carrier lines (M3) themselves speak of spin and
    curvature-coupling structure; that sharper wording is the
    carrier's, is quoted verbatim in the entry as carrier, and does
    NOT enter the hypothesis statement. Any operationalization of
    "coupling structure" — including whether it comprises spin
    structure — is for the later reviewed specification that
    adjudicates the hypothesis, not for this registration.

    Carrier  results/recovered-2026/session_log_full.md:177 and :197,
             quoted VERBATIM in the entry in the language they are
             written in, each followed by an English working
             translation identified as a translation and not the
             carrier. The Executor extracts the carrier lines from the
             repository at the base SHA (M3); this specification does
             not transcribe them, so that the landed quotation cannot
             inherit a transcription error from spec prose.

    What depends on it
             Nothing landed. The ledger's decomposition axis (Ruling 2,
             first RULING block) is a language choice and does not
             depend on this hypothesis being true — the issued text
             states the separation explicitly.

    Falsifier or resolution condition
             ESTABLISHED or REFUTED only by a later reviewed
             specification that operationally defines "coupling
             structure" and pre-registers the corresponding
             discriminating test, proceeding through the normal
             reviewed specification and evidence path (the issued
             text's own routing). No falsification criterion narrower
             or more specific than the statement above is defined
             here; defining one is part of the adjudicating task, not
             of this registration.

    Provenance note
             The carrier is a session log, in Cantonese, never
             adjudicated (P2-XI-B0a §6, Q-M7, on branch science/xi-b0a
             @ 012bdff3; the same finding is in the session handover).
             Registration here is directed by RULING 2 of the issued
             document and is registration only.

## 3. Measurements

    M1  Byte identity of the issued document.
        sha256sum over the handed-over issued file; record the digest.
        git hash-object over the same file; record the blob id.
        Both are recorded as matched text (the full digest), not as a
        boolean.

    M2  Byte identity of the review artifact.
        sha256sum over the handed-over review file; record the digest
        (this is its first recorded hash — provenance per §0a).
        Extract from inside the review artifact the SHA-256 it declares
        itself bound to; record the extracted string verbatim.

    M3  Carrier extraction.
        From a clean checkout of the base SHA, extract
        results/recovered-2026/session_log_full.md lines 177 and 197,
        byte-exact. Record the extracted bytes in the execution report
        and place them in H-XI-SIGN-01.md per §2. If either line number
        does not carry a statement about sign structure — i.e. the
        extraction yields text that does not mention sign, coupling, or
        species in any language — record the extracted text and fire
        A3; do not search for a better line.

    M4  Statement SHA.
        sha256 over the exact-statement bytes of §2's blockquote as
        landed in H-XI-SIGN-01.md (the statement text only, per the
        H-EXT-01 pin convention). Record in the entry's Statement SHA
        field.

    M5  Register append.
        Append one entry to DECISION_LOG.md recording: decision key,
        issued-file path, issuance SHA-256, review verdict string
        "FIT FOR RECORDING", and the H-XI-SIGN-01 registration with its
        Statement SHA. Append-only; no existing line is modified.

    M6  Suite.
        Run the test suite from the branch tip. Record pass/fail counts
        as reported by the runner, verbatim.

## 4. Acceptance criteria

Each criterion names the measurement it evaluates.

    C1  (evaluates M1)  The recorded sha256 digest equals
        1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
        and the recorded blob id equals
        f793f9fd866f563480fbec6168553a2b967aea8f, and the landed file
        decisions/P2-XI-RULINGS-01.issued.md reproduces these under
        re-measurement from the branch tip.

    C2  (evaluates M2)  The SHA-256 the review artifact declares equals
        the issuance SHA-256 in C1, as an exact string match on the
        digest, and the review file lands byte-identical to the
        handed-over bytes under re-measurement from the branch tip.

    C3  (evaluates M3)  The carrier lines land in H-XI-SIGN-01.md
        byte-identical to the M3 extraction.

    C4  (evaluates M4)  The Statement SHA field holds the digest M4
        measured, and re-measurement from the branch tip reproduces it.

    C5  (evaluates M5)  The DECISION_LOG.md diff is append-only: the
        diff contains no deletion or modification of any pre-existing
        line.

    C6  (evaluates M6)  The suite result from the branch tip shows no
        test failing that passes at the base SHA. (The base's own
        counts are whatever M6 measures at base; this criterion asserts
        no regression, not a count.)

## 5. Abort conditions

No abort condition below shares a case with any acceptance criterion:
each names a circumstance under which the corresponding measurement is
not evaluated against its criterion at all, and the task stops.

    A1  Any digest measured in M1 disagrees with §0a before any write
        occurs. STOP; no branch is created; report the measured digest.

    A2  DISCHARGED for v2: the Reviewer's concurrence with the §1
        structure disposition is on record (review of 2026-08-22).
        The condition remains only against regression: if the
        structure actually executed departs from §1, STOP; the
        structure question returns to the PI.

    A3  M3's extraction yields text outside the description in M3, or
        the file or line numbers do not resolve at the base SHA. STOP;
        report the extracted or missing text; the carrier
        identification returns to the PI. Do not substitute another
        location.

    A4  Any step surfaces a conflict between the issued rulings and
        landed repository text, or an internal contradiction among the
        rulings' requirements as they bear on this landing. A proposed
        registration statement or falsifier materially narrower,
        broader, or more specific than the hypothesis directed by the
        issued ruling is also a STOP unless that additional content
        has independent landed authority. STOP; report the conflict or
        the divergent wording verbatim per the issued document's
        CROSS-RULING CONSISTENCY clause; do not reconcile.

    A5  The branch cannot integrate into main by the landed science/*
        path (--no-ff into a dedicated integration branch, main by
        fast-forward only) without content conflict. STOP; report;
        stale-base handling per BRANCHING_POLICY.md.

## 6. Deliverables

    decisions/P2-XI-RULINGS-01.issued.md          (byte-exact)
    decisions/2026-08-22-xi-rulings-01.md         (register record)
    reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md
    assumptions/H-XI-SIGN-01.md
    DECISION_LOG.md                               (append)
    reports/<UTC>_xi-rulings-landing.md           (execution report,
        recording every M output as matched text, every digest in
        full, and any A that fired)

## 7. Non-goals, restated as prohibitions

- Do not reword any existing repository text under Ruling 2.
- Do not open, modify, or classify anything in the XI ledger itself;
  the ledger specification is a separate task under Ruling 3.
- Do not integrate science/xi-b0a; that integration is a separate task.
- Do not push beyond the branch scope fixed in BRANCHING_POLICY.md.

END OF SPECIFICATION
