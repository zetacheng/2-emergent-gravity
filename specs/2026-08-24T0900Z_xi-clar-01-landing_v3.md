# SPECIFICATION — P2-XI-CLAR-01-LANDING v3: resumption from the M4 stop, with the PI register ruling

    Task ID        P2-XI-CLAR-01-LANDING
    Version        v3 — resumes the execution that stopped at M4 under
                   A3. v2 (sha256 2a30601952c0cdf48d000f0a46f39241c0c6
                   315e590c766c40b1c3d8be620ca6, APPROVE FOR EXECUTION)
                   executed M1, M2, M2b and M3 successfully; its M4
                   could not proceed because no register's stated scope
                   had been shown to admit the directed open item. The
                   PI has since ruled the applicable mechanism. v3
                   changes: the Base is the stopped branch tip, not
                   main (§0a); the completed measurements are carried
                   forward as measured rather than re-run (§0b); a
                   canonical decision record for the PI ruling is
                   added (M3b); M4 is rewritten to the ruled mechanism
                   and its landed format precedent. M5, M6a, M6b, M6c
                   are unchanged in structure.
    Spec file      specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
    Author         Researcher (Claude)
    Date           2026-08-24
    Base           science/xi-clar-01-landing @
                   2936e967f7fb893e455547e348243bf49b56aff4
                   (the stopped branch tip, NOT main; main stands at
                   9af94a4a11cd06e90ef2d24183565412b4043c6a)
    Branch         science/xi-clar-01-landing — this task appends
                   commits to the existing stopped branch. No new
                   branch is cut.
    Executor       The executor designated by the PI at execution time.
    Review         SHA-bound pre-execution review by the Reviewer
                   (ChatGPT) required before execution, bound to the
                   exact bytes of this file.

    Commit points, named for the measurements below:
        Base        2936e967…
        B_task      Base + this spec + its review
        H_land      B_task + the M3b, M4 and M5 commits
        T           the tree M6a tests (= H_land)
        H_final     T + the M6a report commit

---

## 0. What this task is

**A resumption, not a re-execution.** The stopped branch already
carries, landed and verified: the issued clarification byte-exact,
its document review, the register record, and the stop report. This
task adds the canonical record of the PI ruling that unblocks M4,
performs M4 and M5, and closes the task.

It remains a transport with one directed registration. It does not
adjudicate, does not begin or constrain any authorized task, and does
not integrate.

## 0a. Why the Base is the branch and not main

v2's measurements were taken against main @ 9af94a4a and its results
are commits on this branch. Restarting from main would discard four
landed commits and re-run measurements that stand. The Base is
therefore the branch tip. **Integration to main remains a separate
later task**, and this specification performs no merge and no
fast-forward.

## 0b. Measurements carried forward, and what M0 does about them

The following are NOT re-run. They are carried forward as executed
under v2 and re-verified only by identity at M0:

    M1   issued-document byte identity — sha256
         0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22,
         blob 1786124bbe3bfa02809d83c2890d0800e0d3edd8
    M2   review-artifact identity, recorded under v2
    M2b  the three-item correspondence scan, all RESOLVE, including
         the scope relation between the landed criterion's "For every
         admissible decoupling α" and the clarification's
         landed-decoupling scope
    M3   the landing commits: clarification, document review, register
         record

    M0  Resumption audit, before any write.
        Verify: origin/science/xi-clar-01-landing equals the Base as a
        full-string match; main equals 9af94a4a… and does not contain
        the clarification; the clarification at
        decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md on the
        Base has the sha256 and blob id above; DECISION_LOG.md at the
        Base is byte-identical to DECISION_LOG.md at main (the v2 run
        wrote nothing to it); and the register record's §4 statement
        that the directed open item is not yet registered is present,
        quoted verbatim. Any mismatch is A0.

## 0c. The PI ruling this task lands, quoted verbatim

> 就 P2-XI-RULINGS-02-CLARIFICATION-01 指令註冊嘅
> representation-stability inquiry:適用登記處為 DECISION_LOG.md 嘅
> UNESTABLISHED 條目機制,即 derivations/P2-DEFERRED-ITEMS.md 自身文本為
> open questions 指名嘅路由。呢項裁決只就本 item 而言,唔擴大或修改任何
> register 嘅 scope,唔建立新 register,亦唔就日後 XI-line open items 嘅
> 登記處作一般性決定 — 後者留待需要時另裁。條目按 clarification 原文登記,
> 狀態 REGISTERED, NOT AUTHORIZED,escalation condition 逐字引錄。
> — Zeta, PI, 2026-08-24

Issued in session, 2026-08-23/24, in Cantonese. The landed record
carries these bytes as the ruling; any English rendering is marked a
translation and is not the ruling.

## 1. Measurements

    M2c Provenance extraction for the ruled mechanism, before M4.
        Extract VERBATIM with path:line, from the Base:
          (a) the landed UNESTABLISHED precedent at
              DECISION_LOG.md:2147-2215 — its entry structure (Date,
              Decision owner, Effect, Decision with the item quoted
              verbatim, Reason, Consequences) and its Reason's
              statement that this log is the register whose stated
              scope covers an item opened as UNESTABLISHED. This is
              the FORMAT PRECEDENT M4 follows.
          (b) the clarification's registration direction and its
              escalation condition, from the landed issued bytes.
        A node that cannot be located is A1.

    M3b Canonical record of the PI ruling.
        Create decisions/2026-08-24-xi-open-item-register-routing.md
        in the two parts decisions/README.md requires. PART 1: owner,
        date 2026-08-24, effect, scope; §0c's ruling quoted
        byte-identical, in the language issued, with an English
        rendering marked as a translation and not the ruling; and the
        explicit scope limits the ruling itself states — this item
        only, no register's scope extended, no register created, no
        general decision for future XI-line items. PART 2 is marked
        REVIEW PENDING per decisions/README.md.
        Canonical decision key: 2026-08-24-xi-open-item-register-routing.

    M4  Registration of the directed open item, per the ruling.
        Append to DECISION_LOG.md one entry in the M2c(a) format,
        containing at minimum:
          - a heading dated 2026-08-24 naming the open item;
          - Decision owner: Principal Investigator; Effect: opens the
            representation-stability inquiry as an open item;
          - the item quoted from the clarification: the question, no
            broader and no narrower than the clarification states it;
            the link to P2-FIERZSUM-01 §8; the escalation condition
            BYTE-IDENTICAL to the clarification's; and the note that
            its decoupling-family membership is an unlanded
            model-level choice;
          - **Status: UNESTABLISHED. REGISTERED, NOT AUTHORIZED.**
            with an explicit sentence that registration is not
            authorization and that nothing here begins, schedules,
            constrains or prioritises the inquiry;
          - a Reason section citing the PI ruling's canonical record
            (M3b's path and key) as the authority for using this
            mechanism, and stating the ruling's own scope limit — for
            this item only.
        Append-only: the Base's DECISION_LOG.md bytes must be an
        exact byte-prefix of the product.

    M5  Landing index append.
        Append to DECISION_LOG.md the clarification landing's index
        entry, as v2's M5 required: decision key
        2026-08-24-xi-rulings-02-clarification-01, issued-file path,
        issuance SHA-256, review verdict "FIT FOR RECORDING", and the
        identifier of the open item registered at M4. The M4 entry
        precedes it; both appends preserve the byte-prefix relation.
        The resulting tip is H_land.

    M5b Register-record correction.
        The register record landed at v2's M3 states in its §4 that
        the directed open item is not yet registered. That statement
        was true when written and is false at H_land. Correct it by
        APPENDING a dated note to that file recording: the original
        statement's temporal scope, that the item was registered at
        M4 under the PI ruling, and the M4 entry's identifier. The
        original sentence is NOT edited. Verify the file's Base bytes
        are an exact byte-prefix of the result.

    M6a Suite.
        Run the suite at main (9af94a4a…) and at the post-M5b tree on
        a full (non-shallow) tree. Record both verbatim and the
        tested tree's SHA, T.

    M6b Report.
        Write reports/<UTC>_xi-clar-01-landing-resumed.md recording
        M0 through M6a and nothing later, and carrying forward v2's
        M1/M2/M2b/M3 results by reference to the stop report with its
        path, not by re-assertion. The report does not state its own
        commit SHA: it names T and records that it is itself the next
        commit on T. Commit it.

    M6c Push and post-commit evidence, branch-only.
        Verify by diff that H_final differs from T only by the report
        artifact. Push the branch. Record H_final, the diff and the
        push result in a branch-only addendum or in the execution
        summary. Integration is a separate task.

## 2. Acceptance criteria

    C0  (M0) Every resumption-audit value matches: branch tip, main,
        clarification sha256 and blob id, DECISION_LOG identity with
        main, and the register record's §4 statement present.
    C1  (M2c) Both extracted nodes appear in the deliverables as
        verbatim quotations with path:line resolving at the Base.
    C2  (M3b) The canonical record exists at its stated path with
        §0c's ruling byte-identical, in the language issued, its
        English rendering marked as a translation, and the ruling's
        own scope limits stated.
    C3  (M4) The entry exists in the M2c(a) format with Status
        UNESTABLISHED and REGISTERED, NOT AUTHORIZED; the escalation
        condition is byte-identical to the clarification's; the
        registration-is-not-authorization sentence is present; the
        Reason cites M3b's canonical record.
    C4  (M4, M5, M5b) The Base's DECISION_LOG.md bytes are an exact
        byte-prefix of the product; the M4 entry precedes the M5
        index entry; the register record's Base bytes are an exact
        byte-prefix of its M5b result and its original §4 sentence is
        unedited.
    C5  (M6a) No test fails on T that passes at main.
    C6  (M6b, M6c) The report records M0–M6a and no later
        measurement, names T, does not assert its own SHA or H_final,
        and carries v2's results by reference to the stop report;
        H_final differs from T only by the report, verified by diff.

## 3. Abort conditions

    A0  Any M0 value mismatches. STOP before any write; report the
        measured value. In particular, a DECISION_LOG.md at the Base
        that differs from main's means the v2 run wrote to it after
        all, and the append-only reasoning of M4/M5 must be re-made
        by the PI.
    A1  A node named in M2c cannot be located at the Base. STOP;
        report what is missing.
    A2  Transport fidelity: any passage in the canonical record, the
        M4 entry, or the M5b note that would state the ruling or the
        clarification materially more narrowly, more broadly, or more
        specifically than the issued text, without independent landed
        authority. STOP; report the divergent wording verbatim.
    A3  Any step would extend or modify any register's scope, create
        a register, or state a general rule for future XI-line open
        items. The ruling settles this item only. STOP.
    A4  Any step would begin, schedule, constrain or prioritise the
        Q-M3 check, the Q-M2 scope assessment, or the registered
        representation-stability inquiry. STOP; registration is not
        authorization.
    A5  Any step would edit the original §4 sentence of the register
        record, any landed byte of the stop report, or any file
        arriving from v2's M3. STOP.
    A6  Any step would merge, fast-forward, or otherwise move main.
        STOP; integration is a separate task.

## 4. Deliverables

    decisions/2026-08-24-xi-open-item-register-routing.md (M3b)
    DECISION_LOG.md — the M4 open-item entry, then the M5 index
        entry, both appended
    the register record's appended M5b note
    specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md and its SHA-bound
        review, committed first in spec → review order (B_task)
    reports/<UTC>_xi-clar-01-landing-resumed.md (M6b)
    Branch pushed per BRANCHING_POLICY.md science/* scope (M6c);
        integration is a separate task and is not performed here.

END OF SPECIFICATION
