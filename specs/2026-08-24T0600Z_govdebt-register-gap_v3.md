# SPECIFICATION — P2-GOVDEBT-REGISTER-GAP-01: record the XI-line open-item register gap as governance debt

    Task ID        P2-GOVDEBT-REGISTER-GAP-01
    Version        v3 — revises v2 (sha256 6e7bc64c51546948523cc98d5b
                   e5c3c90d8580cc525ea6f90e6992c57ff25afe) per Reviewer
                   verdict REVISE BEFORE EXECUTION: v2 restated the
                   disposition as OPEN in §0a but left three v1
                   strings standing — M3's executable "Disposition:
                   SPECIFIABLE", and two passages describing the
                   item's routing as an outstanding PI ruling after
                   §0b recorded that it had been ruled. All three are
                   corrected here; no architecture changes. The
                   Reviewer's concurrence with OPEN and with the
                   restated debt framing is recorded; A5 does not
                   fire. v2 had revised v1 (sha256 8519b71b2d3f8685bb
                   64c565725ecf42ede453376029d73a825ba6b2437630e9)
                   with two changes, from two sources:
                   (i) REVIEWER, v1 review: v1 inferred SPECIFIABLE
                   partly from "the repository's own register-creation
                   practice shows the shape is specifiable inside it".
                   That inference is unsupported and is REMOVED.
                   (ii) EVIDENCE FOUND AFTER THE v1 REVIEW WAS
                   WRITTEN, changing that review's premise: see §0b.
                   The recorded debt is restated accordingly, and the
                   disposition is set to OPEN with the choice
                   re-flagged for the Reviewer on the new evidence.
    Spec file      specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
    Author         Researcher (Claude)
    Date           2026-08-24
    Base           main @ 9af94a4a11cd06e90ef2d24183565412b4043c6a
    Branch         science/govdebt-register-gap-01, cut from the base
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.
    Kind           Recording. Nothing binds; no gate moves; no open
                   item is registered and no register is created.

---

## 0. What this task is and is not

`docs/GOVERNANCE-DEBT.md` states of itself: **nothing in it binds; it
records what the rules, amendments and task reports already carry, and
it creates, modifies and explains no obligation.** This task adds one
entry on that basis.

**The debt recorded is a mechanism gap, not the scientific
question, and not a claim that no register admits the item — see
§0b.** What is recorded is that the repository holds no landed index
of its registers and their stated scopes, with the measured
consequence that the same candidate-register reasoning has been
performed twice by different agents, months apart, and that the
second performance omitted a candidate the first had used.

Accordingly, and each of these is an abort if attempted:

- **This task does not register the representation-stability
  inquiry.** That item's routing was settled by the PI on 2026-08-24
  for that item only, and its registration is performed by the
  resumed landing task, not here. This entry records a different
  thing: the indexing gap that the ruling leaves untouched. (A2)
- **This task creates no register**, proposes no register, and states
  no preference among the candidate resolutions. The disposition
  carried is `OPEN` — *none of the above* — which asserts neither
  that a repair exists nor that one is specifiable; the entry must
  not read as a specification. (A3)
- It does not resume, unblock, or modify `P2-XI-CLAR-01-LANDING`,
  whose branch stands where it stopped. (A4)
- It does not begin, schedule, constrain, or prioritise the Q-M3
  check, the Q-M2 scope assessment, or the representation-stability
  inquiry. (A4)

## 0b. The evidence that changed the v1 framing

Two landed records, to be extracted at M1 and set side by side in
the entry:

    2026-08-19   DECISION_LOG.md:2147-2215 files an open item as
                 UNESTABLISHED and states in its Reason that this log
                 is the register whose stated scope covers an item so
                 opened, having read and excluded P2-DEFERRED-ITEMS,
                 P2-PHASE-01_C-CHECK_OPEN-ITEMS, OPEN-AC-*, OPEN-PD-*
                 and GOVERNANCE-DEBT.
    2026-08-24   reports/2026-08-24T0043Z_xi-clar-01-landing.md, on
                 branch science/xi-clar-01-landing @ 2936e967…,
                 performs the same candidate-register reasoning for a
                 different item, tests three registers, and does not
                 test DECISION_LOG.

Both agents reasoned correctly from what they had. The first
recorded its conclusion inside one entry's Reason; nothing indexed
it, so the second could not reach it.

**The PI has since ruled** (2026-08-24, quoted at M1 and recorded in
the resumed landing task, not here) that the applicable registration
mechanism for the representation-stability item is the
`DECISION_LOG.md` `UNESTABLISHED` mechanism, for that item only, with
no register's scope extended and no general decision made for future
XI-line items. **That ruling settles the routing of one item and
leaves the indexing gap exactly where it is** — which is why this
entry is still worth landing, and why it must not be written as
though the routing question were unresolved.

## 0a. Authority for the disposition

The disposition is `OPEN`, defined by the register's own text as
*none of the above*, quoted verbatim at M1 and used as written.

`SPECIFIABLE` is NOT claimed: its definition requires that the
mechanism be fully specifiable inside this repository, and no
measurement here establishes that limb. The v1 inference from
register-creation practice is withdrawn.

**DISPOSITION RE-FLAGGED FOR THE REVIEWER, on changed premises.** The
v1 review determined `OPEN` on the reading that no existing register
has demonstrated jurisdiction. §0b's evidence shows one has, and the
PI has ruled for this item. The Reviewer is therefore asked to make
the determination again on the present evidence and the present entry
content. `OPEN` is carried here as the conservative default and as
the v1 determination; if the Reviewer now judges `SPECIFIABLE`
warranted — the missing mechanism being an index of registers and
their stated scopes — that substitution is within this spec's scope
and the Reviewer's concurrence selects between them. If the Reviewer
judges the choice to require a PI ruling, A5 fires.

## 1. Measurements

    M1  Provenance extraction, before any write.
        Extract VERBATIM, with path:line, from the Base and from the
        stopped branch as stated:
          (a) the register's disposition definitions in full,
              including the OPEN definition used by M3 and the
              SPECIFIABLE definition together with the sentence
              "SPECIFIABLE means specifiable, not specified", the
              latter pair extracted so the entry can show what is
              NOT being claimed (docs/GOVERNANCE-DEBT.md);
          (b) the register's self-description that nothing in it
              binds (same file);
          (c) the clarification's registration direction, from the
              landed issued bytes on the stopped branch
              science/xi-clar-01-landing @ 2936e967…
              (full SHA resolved and recorded at M1), file
              decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md,
              whose sha256 must equal
              0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22;
          (d) the stop report's register-by-register findings, from
              reports/2026-08-24T0043Z_xi-clar-01-landing.md on that
              same branch, quoted as the report's own measurement and
              attributed to it;
          (e) the two candidate registers' own scope statements
              (derivations/P2-DEFERRED-ITEMS.md and
              derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md), quoted
              from the Base.
        A node that cannot be located is A1. Every downstream
        sentence uses these bytes, not memory.

    M2  Entry identifier.
        Measure the existing entry identifiers and disposition
        counts in the register at the Base, recording the measured
        list. The new entry takes the next unused identifier in the
        register's own sequence, as measured — not as assumed from
        the counts table, which is itself part of the file and is
        updated by M3.

    M3  The entry.
        Append one entry to docs/GOVERNANCE-DEBT.md in the file's
        existing format, containing:
          - the identifier from M2 and a title naming the gap;
          - **Disposition: OPEN**, with the register's own
            definition — *none of the above* — quoted verbatim from
            the file;
          - a statement of the gap, in these terms and no stronger:
            the repository holds no landed index of its registers and
            their stated scopes; the same candidate-register
            reasoning was performed on 2026-08-19 and again on
            2026-08-24 by different agents; the second omitted
            DECISION_LOG, which the first had identified and used;
            and the routing of the item that triggered the second
            performance has since been ruled by the PI for that item
            only, leaving the indexing gap unaddressed;
          - the two records of §0b set side by side, each quoted and
            attributed, so a reader can see the repetition and the
            omission without reconstructing them;
          - **Evidence**: M1's quotations with their path:line and
            the branch SHA for those read from the stopped branch,
            and the stop report attributed as the measurement's
            source;
          - an explicit sentence that this entry records a missing
            mechanism and does NOT register the open item, propose a
            register, or express a preference among resolutions;
          - an explicit sentence that the entry is not closed by
            being written down, per the register's own rule.
        Update the file's disposition counts table to the values
        measured after the append. The Base bytes preceding the
        counts table and the entry insertion point are otherwise
        unchanged.

    M4  Post-write verification.
        Verify: the entry exists with its identifier and disposition;
        the counts table's arithmetic is consistent with the entry
        list as measured from the file itself; every quotation in the
        entry is byte-identical to its M1 extraction; and
        `git diff --name-status Base..tip` shows exactly the paths
        this task declares.

    M5  Suite.
        Run the suite at the Base and at the post-M3 tree on a full
        (non-shallow) tree. Record both verbatim and the tested
        tree's SHA, T.

    M6a Report.
        Write reports/<UTC>_govdebt-register-gap.md recording M1
        through M5 and nothing later. The report does not state its
        own commit SHA: it names T and records that it is itself the
        next commit on T. Commit it.

    M6b Push and post-commit evidence, branch-only.
        Verify by diff that the final tip differs from T only by the
        report artifact. Push the branch. Record the final tip SHA,
        the diff result and the push result in a branch-only addendum
        or in the execution summary; neither is required to exist
        inside the M6a report. Integration is a separate task.

## 2. Acceptance criteria

    C1  (M1) Every extracted node appears in the entry as a verbatim
        quotation with a path:line that resolves at the Base, or at
        the named branch SHA for the two read from it.
    C2  (M2, M3) The entry's identifier is the next unused one in the
        measured sequence; its disposition is the one this spec
        carries as reviewed, with the register's own definition
        quoted verbatim.
    C3  (M3, M4) The entry contains both explicit disclaimer
        sentences — that it registers no open item and proposes no
        register, and that it is not closed by being written down —
        and states the gap in §0b's terms without asserting that no
        register admits the item.
    C4  (M4) The counts table is consistent with the entry list as
        measured from the file; all quotations are byte-identical to
        M1; the diff shows only this task's declared paths.
    C5  (M5) No test fails on T that passes at the Base.
    C6  (M6a, M6b) The final tip differs from T only by the report,
        verified by diff; the report does not assert its own SHA.

## 3. Abort conditions

    A1  A node named in M1 cannot be located, or the clarification's
        sha256 on the stopped branch does not match. STOP before any
        write; report the measured value.
    A2  Any step would register the representation-stability inquiry,
        or would read as registering it. STOP; that registration
        belongs to the resumed landing task under the PI's 2026-08-24
        ruling, not to this one.
    A3  Any step would create a register, create an index, name a
        register as the general answer for future items, or express a
        preference among candidate resolutions of the indexing gap.
        STOP. Recording a gap is not specifying its repair, and OPEN
        does not assert that a repair is specifiable.
    A3b Any step would state or imply that no register admits the
        representation-stability item, or that its routing is
        unresolved. STOP: the PI ruled it on 2026-08-24 for that
        item, and §0b's evidence contradicts the stronger claim.
    A4  Any step would modify science/xi-clar-01-landing, resume that
        task, or begin/schedule/constrain/prioritise any authorized
        or registered inquiry. STOP.
    A5  The Reviewer judges the disposition choice to require a PI
        ruling. STOP before execution; the question returns to the
        PI.

## 4. Deliverables

    docs/GOVERNANCE-DEBT.md — one appended entry and the updated
        counts table
    specs/2026-08-24T0600Z_govdebt-register-gap_v3.md and its SHA-bound
        review, committed before the entry commit in spec → review
        order
    reports/<UTC>_govdebt-register-gap.md (M6a)
    Branch pushed per BRANCHING_POLICY.md science/* scope (M6b);
        integration is a separate task.

END OF SPECIFICATION
