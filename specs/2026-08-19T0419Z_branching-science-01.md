# P2-BRANCHING-SCIENCE-01 — Policy amendment specification

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Origin            PI ruling of this session, on items A and D of the
                      P2-POLE-B0-INTEG-01 A4 abort

---

## 0. Binding SHA and provenance

    Integration base (main at authorship)   11af14a792c5858b368180d99ab9ee4692a7f698

If `main` has advanced when execution begins, execution does not proceed and
the specification returns to the Researcher for re-issue (stale-base stop).

**This specification transcribes a PI ruling. It does not adjudicate.** The
ruling text is reproduced in §5 and is to be landed as ruled. Where the
executor finds the ruling text cannot be applied as written, that is an abort
and a return to the PI — not an executor edit.

## 0a. Self-contained mechanics — bootstrap note

This task's own merge mode and push scope are stated in §4 of this document
and are **not** delegated to `docs/BRANCHING_POLICY.md`. The policy clause
that would govern them is the clause this task introduces; delegating would be
circular. Every integration specification preceding P2-POLE-B0-INTEG-01 stated
its mechanics this way, and P2-POLE-B0-INTEG-01's delegation is what surfaced
the policy gap.

---

## 1. Objective

Amend `docs/BRANCHING_POLICY.md` to recognise `science/*` as a branch class
and to fix its integration merge mode and allowed-ref scope; add a
cross-reference in `CONVENTIONS.md`; register the retroactive governance gap.

## 1a. Non-objectives

This task does **not**:

1. merge `science/pole-b0-milestone-scope`, which is the object of a separate
   re-issued specification;
2. modify, re-merge, re-verify, or retrospectively authorise any historical
   `science/*` branch already an ancestor of `main`;
3. amend `AGENTS.md` — the PI ruled that ref-level mechanics do not belong in
   the role model;
4. touch `docs/local/execution_environment.md` — item C of the ruling is a
   separate task;
5. touch `scripts/recon2026/proca_curved.py` — see §12;
6. create the POLE construction register entry — ruled to the open register,
   actioned by the re-issued POLE integration specification.

---

## 1b. Authorised path manifest — defined once

    P1   docs/BRANCHING_POLICY.md
    P2   CONVENTIONS.md
    P3   the register file selected for G-1 under §6
    P4   this task's own spec, review, and report artifacts, at their
         authorised paths

`A5` and `C8` both refer to this manifest and neither restates it. Any future
change to the authorised set is made here and nowhere else.

Note that P4 is necessarily present in `M3`: this task's spec and review are
committed before execution under Rule 15, so a diff of the merge product
against the base will list them. An abort condition that omitted P4 would fire
on correct execution.

---

## 2. Pre-execution measurements

Every value is measured at execution time. No value is carried from any report
or prior specification.

    M1   Count of remote `science/*` refs that are ancestors of `main`
         at 11af14a7. Record the observed integer and the command used.

         A figure appeared in the P2-POLE-B0-INTEG-01 stop report. It is a
         historical observation and is NOT a target. If the measured value
         differs, the measured value is what §6 records; the difference is an
         observation, not a discrepancy to reconcile.

    M2   Test suite result on the merge product. Record passed / failed /
         deselected as observed, with the invocation used, alongside the same
         run at 11af14a7.

    M3   `git diff --name-only 11af14a7..<merge product>` — record the full list.

    M4   Dry-run merge: conflict-free or not; if not, the conflicting paths.

    M5   Read the current branch-name taxonomy block of
         `docs/BRANCHING_POLICY.md` and record its line span as observed. The
         span `:5-11` is quoted from a prior read for orientation only and is
         not a target.

---

## 3. Abort conditions

Execution stops, with no partial landing, and returns to the Researcher if:

    A1   the base SHA observed differs from §0
    A2   M4 reports conflicts
    A3   M2 shows a failure not also present at 11af14a7 for the same test
    A4   the ruling text of §5 cannot be applied as written — for example if
         the taxonomy block's structure does not admit the new entry in the
         form given. Return to the PI; the executor does not reword the ruling.
    A5   a path outside the §1b manifest appears in M3

---

## 4. Merge mechanics for this task

    Branch            a new task branch for this specification
    Integration       `git merge --no-ff` of the pinned task-branch tip into a
                      dedicated integration branch
    Prohibited        squash integration; rebase integration; force-push;
                      `--force-with-lease`; branch deletion; history rewrite
    Landing           `main` advances by FAST-FORWARD only, from 11af14a7 to
                      the completed integration head. If a fast-forward is not
                      available, STOP.
    Push scope        push only this task's branch, the integration branch,
                      and `refs/heads/main`. No session branch. No other ref.
                      The source branch must not move.

The push exit status is recorded as a measurement. Remote `main` is read back
after the push and its SHA recorded.

---

## 5. Policy amendment — text as ruled

### 5.1 Taxonomy

Add `science/<scientific-task>` to the branch-name block located under M5,
in the form the block already uses for the five existing prefixes.

### 5.2 New integration section

Landed verbatim as ruled:

> `science/*` is a recognized scientific-task branch class.
> Approved science branches integrate by `--no-ff` into a dedicated
> integration branch.
> Squash/rebase integration prohibited.
> During landing, only the integration branch and `refs/heads/main` may be
> pushed.
> Source branch, session branches and unrelated refs must not move.
> `main` advances only by fast-forward from its reviewed evidence base to the
> completed integration head.

### 5.3 Retroactive note

Landed verbatim as ruled, with one substitution: the placeholder for the
ruling commit is replaced by a phrase naming the pre-amendment state, because
a commit cannot cite its own identifier. The base SHA is named as the
pre-amendment tip and **not** as the date from which the policy takes effect —
the policy takes effect with this amendment, which is strictly later.

> Through pre-amendment `main` `11af14a7`, `science/*` was used operationally
> but absent from the formal branch taxonomy and had no policy-level
> merge-mode rule. Historical landed science branches remain accepted; no
> retrospective rewrite or re-merge is authorized.

### 5.4 CONVENTIONS.md cross-reference

Landed verbatim as ruled:

> Branch-specific merge mode and allowed-ref policy are defined in
> `docs/BRANCHING_POLICY.md`.

`CONVENTIONS.md` receives the cross-reference only. No merge-mode or ref rule
is duplicated there — single source of truth is the policy file.

---

## 6. Register entry

    G-1   Retroactive governance gap — ONE entry, not one per branch.
          Records: the pre-amendment absence of `science/` from the taxonomy;
          the absence of any policy-level merge-mode rule for the class; the
          M1-measured count of historical `science/*` ancestors of `main`; and
          the ruling that these remain accepted with no retrospective rewrite
          or re-merge authorised.

          The register this belongs in is determined by reading the registers'
          own stated scopes. If none admits it, record the scopes observed and
          return to the Researcher rather than coining a location.

---

## 7. Acceptance criteria

    C1   `docs/BRANCHING_POLICY.md` contains `science/` in the taxonomy block
         identified by M5.
    C2   The §5.2 section is present, containing all six ruled statements.
    C3   The §5.3 retroactive note is present, names `11af14a7` as the
         pre-amendment tip, and does not present that SHA as the point from
         which the policy takes effect. Verified by reading.
    C4   `CONVENTIONS.md` contains the §5.4 cross-reference and does NOT
         restate any merge mode or ref rule. Verified by reading.
    C5   G-1 exists, carrying the M1-measured integer.
    C6   M1–M5 recorded with observed values and the commands or reads used.
    C7   `main` has the integration head as its tip and reached it by
         fast-forward. Record `git merge-base --is-ancestor` and the push
         read-back.
    C8   M3 lists no path outside the §1b manifest. Any other path is an
         A5 abort.
    C9   `scripts/recon2026/proca_curved.py` blob id is unchanged. Record the
         observed id.

---

## 8. Substring hazards

Any check performed by search must state its exclusions in the report.

    science         matches "scientific", "scientific-task", and the prose of
                    §5.2 itself; a taxonomy check must read the block, not
                    count file-wide hits
    merge           matches "merge parent", "merge-base", "merged"
    push            matches "force-push"

A check that cannot state its exclusions is performed by reading, and the
reading recorded.

## 9. Criterion satisfiability

No criterion requires the report to contain a term in order to locate it.
C1 is a read of a block located by M5, not a file-wide count. C2 is a presence
check on ruled text whose wording is fixed by §5.2 and therefore known before
execution. C9 is a measurement whose expected value is not asserted here: the
executor records the observed id, and the Researcher compares it under §11.

---

## 10. Post-execution verification (Researcher)

From a clean clone of the remote, no writes:

1. re-run C1 through C5 and C7 by reading;
2. compare C9's recorded blob id against the three landed records that pin it
   (the RECON-01a integration report's three-point identity, the SRC-B0
   report's UNCHANGED line, and the RECON-01a specification's MEASURED line);
3. any check that cannot be evaluated is recorded **INCONCLUSIVE**, not PASS.

---

## 11. What this task does not establish

This is a governance amendment. It produces no physical number, moves no
gate, and adds no support to the programme. `P2-PHASE-01` does not move. What
it removes is a rule-lookup failure that blocked an integration.

---

## 12. Held pending a separate PI ruling

Item C of the session's rulings proposed rewording the sentence in
`scripts/recon2026/proca_curved.py` that states scipy is not a declared
package. That file's blob `03f46905e5798fb7f6880dfae9ed5a1931be895b` is pinned
in three landed records as part of the frozen clean-room construction. Any
edit breaks that identity.

The ruling as given did not address the freeze, and a confirmation that does
not mention it is not read here as authorising an unfreeze. The rewording is
therefore **not actioned by this task and not by the execution-environment
task**. It proceeds only on an explicit unfreeze ruling naming the blob.

The `docs/local/execution_environment.md` clarification carries no such
constraint and is a separate task.
