# Task specification — land the supply protocol integration on main

Specification evidence base: `cc8adaa04ed75f5118ae2c25926a05e51a0056ff`

    Authoritative main   0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
    Reviewed integration governance/integrate-supply-protocol-v3
                         cc8adaa04ed75f5118ae2c25926a05e51a0056ff
    Merge commit within  48268e6c

Classification: **MATERIAL**. **This task advances `refs/heads/main`.**

**This task builds nothing and verifies no science.** The integration
was built, reviewed and verified under
`specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md`. **Its only
outstanding element is that authoritative `main` never moved**, because
that specification carried no clause authorising a ref advance and the
executor correctly declined to infer one from the task's name.

**This is a SPECIFICATION_DEFECT of the integration task, not an
executor defect.** It is repaired here rather than backdated.

**One ref advance, by fast-forward.** No merge, no rebase, no squash, no
force. **Verified available:** `0ab6369a…` is a strict ancestor of
`cc8adaa0…`.

---

## 0. What is and is not true right now

**True.** The integration exists, is complete, and passed every
criterion under independent re-measurement: scope 6 additions and 3
modifications with no other operation; six arriving blobs identical;
`DECISION_LOG.md` append-only on both measures, 82337 → 89541 bytes with
zero deletions; `GATES.md` unchanged at `849a4fbf…` with fourteen `P2-`
sections and `P2-PHASE-01` still `PROPOSED`; eighteen rules; six
register entries; six superseded commits none an ancestor.

**NOT true, and this is the whole point of the task.** **Rule 18 is not
in force on authoritative `main`, and the superseded register does not
exist there.** `main` is at `0ab6369a…`, which carries seventeen rules.
**Until this task completes, "Rule 18 has landed" is false**, and any
document saying otherwise is describing a branch.

**Say it the accurate way until then:** the integration branch is
complete and verified but **not landed**.

## 1. Why main does not land exactly on cc8adaa0

**The reviewer's landing clause said to advance `main` to
`cc8adaa0…` exactly. This specification departs from that, and the
reason is stated rather than glossed.**

This task has its own specification, its own pre-execution review and its
own report, and **Rule 15 requires the review committed before the work
it authorises.** Any commit carrying them descends from `cc8adaa0…` and
therefore moves the tip. **So either `main` lands past `cc8adaa0…`, or
this task's own record never lands at all.**

**The property the reviewer actually wanted is preserved, and A5 checks
it directly:** `cc8adaa0…` and the merge commit `48268e6c…` are both
ancestors of the final `main`, and **the only difference between
`cc8adaa0…` and the final `main` is this task's three artifacts** — no
modification, no deletion, no new merge. **Authoritative `main` will
contain exactly the reviewed integration plus the record of landing it.**

**This is also what every prior integration on this line did.**
`gate/p2-integrate-chirality-census`, `fix/integrate-si1-crossref` and
`governance/land-rules-14-15` each end at their own report commit, and
each is an ancestor of `main`.

## 2. Which rules govern

**Rule 18 is operative at this task's evidence base** — `cc8adaa0…`
carries it — **but not on authoritative `main`**, which is the state
this task exists to change.

**Nothing here turns on resolving that.** §3 requires file supply as a
specification instruction, which is what Rule 18 would require anyway.
**Both readings produce the same executor action**, so do not spend a
stop on the question. **Report which reading you took**, so the next
specification can settle it deliberately.

## 3. How the review arrives

- **Supplied as a FILE.** No delimiters are named; there is nothing to
  extract.
- **If no file is supplied, STOP.** Do not reconstruct a review from a
  conversation and do not author one.
- **The review must identify this specification**, by digest or task
  name. **If it identifies a different one, STOP and say which.**
- **Commit the file's bytes unchanged.** Placeholders inside its text
  stay as written; resolve them in the PATH only.
- **Report how the review arrived, and how this specification arrived.**

## 4. Commit order and evidence layering

Cut `governance/land-supply-protocol-v3` from `cc8adaa04ed75f5118ae2c25926a05e51a0056ff`.

    commit 1  specs/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md
    commit 3  reports/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md
    then      fast-forward refs/heads/main to commit 3, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**There is no merge commit in this task.** If your procedure produces
one, **STOP** — the fast-forward was not available and something moved.

**The ref advance follows the report**, which is the same layering every
integration on this line uses: the report states the intended parameters,
and the outcome is post-report evidence.

**Committed report:** raw output for A1–A6 and A8 as measured on the
branch before the advance; commit 1–3 SHAs and messages; the intended
`main` target SHA; the intended fast-forward parameters; the pre-advance
head.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the push; A7's post-advance verification; remote `main` read back; the
report commit's stored message read back from the object; final ancestry
confirmation; A9 and A10 as re-verified after the advance.

## 5. Acceptance criteria

**A1 — Refs before anything.** Read from the remote:

    refs/heads/main                             0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
    governance/integrate-supply-protocol-v3     cc8adaa04ed75f5118ae2c25926a05e51a0056ff
    governance/supply-protocol-v3               aa531aeab3a98b51b2b55b1f79f9e21c139e7dde

**Any mismatch → STOP.** In particular, **if `main` has moved, this
task's fast-forward premise is void** — do not attempt a merge instead.

**A2 — The advance is a fast-forward, verified BEFORE it is attempted.**
`git merge-base --is-ancestor <current main> <commit 3>` exits 0.
**Report the exit status as a measurement, not as an expectation.**
**Push without `--force` and without `--force-with-lease`**; if the push
requires either, **STOP** — a plain push refusing means the premise is
already false.

**A3 — No tree object of the integration is touched.** Between
`cc8adaa0…` and commit 3 the diff is **exactly three additions and
nothing else**:

    A  reports/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md
    A  reviews/chatgpt/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md
    A  specs/2026-08-XXT{HHMM}Z_land-supply-protocol-v3.md

**Zero modifications, zero deletions, zero renames, no other operation.**
`CONVENTIONS.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`,
`GATES.md`, `AGENTS.md`, `pyproject.toml` and every path under
`scripts/`, `results/`, `tests/`, `derivations/`, `docs/` and `reviews/`
existing at `cc8adaa0…` are blob-identical at commit 3. **This task
appends nothing to `DECISION_LOG.md`.**

**A4 — Scope from the old main.** Base `0ab6369a…`, head commit 3:
**9 additions and 3 modifications**, `mode: exact`, forbidden operations
`delete, rename, copy, type_change, unmerged, unknown`. Six additions and
all three modifications arrive from the integration; **three are authored
here.**

**A5 — The reviewed integration is contained, not re-derived.** Both
`cc8adaa04ed75f5118ae2c25926a05e51a0056ff` and the merge commit
`48268e6c…` are ancestors of commit 3, **verified by
`git merge-base --is-ancestor` and reported as two exit statuses.**
**`48268e6c…` remains the only merge commit in `0ab6369a…..main`**;
report the count of merge commits in that range.

**A6 — The integration's own criteria still hold at commit 3**, since a
fast-forward can carry only what the branch carries. Re-verify and
report, at commit 3:

    CONVENTIONS.md          18 numbered rules
    BRANCHING_POLICY.md     6 register entries, counted by entry record
                            inside the fenced block, WITH the six
                            branch names read back
    GATES.md                blob 849a4fbfe62d6478f092a84b0175357a74bbbb06
                            14 sections matching '^## P2-'
                            P2-PHASE-01 still PROPOSED
    DECISION_LOG.md         blob-identical to cc8adaa0…
    tests/                  tree object IDENTICAL to the tree at
                            0ab6369a… — compare the tree object, do not
                            count files

**The `tests/` check is stated as tree identity deliberately.** The
integration specification wrote it as a file count and the count did not
match the predicate; **a tree comparison is exact and has no count to
disagree with.**

**A7 — After the advance.** Remote `refs/heads/main` resolves to
commit 3; `0ab6369a…`, `cc8adaa0…` and `48268e6c…` are all ancestors of
it; **no history was rewritten** — `0ab6369a…` is still reachable and
still has the same commit object.

**A8 — Branches preserved, all nine.** After the task these still
resolve to the recorded commits, and **none is deleted:**

    governance/integrate-supply-protocol-v3  cc8adaa0…
    governance/supply-protocol-v3            aa531aea…
    fix/pi-decisions-and-deferred            52f65117…
    fix/pi-decisions-v2                      ebd531ab…
    governance/supply-protocol-v2            40168469…
    governance/supply-protocol-and-superseded 7146a093…
    review/role-model-and-executors          10c260b9…
    gate/p2-land-diquark-line                d64cd912…
    gate/p2-land-diquark-line-v2             <read and report>

**`governance/integrate-supply-protocol-v3` must still point at
`cc8adaa0…`, not at commit 3.** The reviewed head keeps its own ref.

**A9 — Superseded branches still not merged.** After the advance, none
of the six register commits is an ancestor of `main`. **Six separate exit
statuses.** **This is re-checked after the advance and not inherited from
the integration report**, because `main` is a different ref from the one
that was checked there.

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`, at commit 3 before the advance and again at
the pushed `main`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`.

**A11 — Commit-message hygiene** on all three commits: inspect the
proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** Once `main`
carries Rule 18 and the register, **a reader may take a written rule for
an enforced one.** **Nothing checks either.** No test asserts any of the
eighteen rules, and the register stops a superseded branch from being
integrated only by being read. **The enforcement gap is unchanged by this
task**; landing a rule is not enforcing it, and the specification that
addresses the gap is still unissued.

## 7. Invariants and prohibitions

- Executor-writable: this specification, its pre-execution review, and
  its report. **Nothing else, at all.**
- **No merge, no rebase, no squash, no cherry-pick, no revert, no
  force-push, no history rewrite, no tag.** **A fast-forward or a stop.**
- **Do not edit any file arriving from the integration**, including
  `CONVENTIONS.md` and `docs/BRANCHING_POLICY.md`.
- **Do not append to `DECISION_LOG.md`.** If a PI ruling should be
  recorded for this landing, that is a separate task.
- **Do not delete any branch**, including the two of the register that
  name this line's own predecessors.
- **Do not state that any rule is now enforced, tested or checked.** §6
  governs.
- **If `main` has moved from `0ab6369a…`, STOP and report.** Do not
  convert this task into a merge.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 8. Report contract

- everything listed in §4 under its correct layer;
- **A2's is-ancestor exit status, measured before the push**, and the
  exact push command used;
- **A3's diff, in full**, with the operation counts;
- **A5's two exit statuses and the merge-commit count** in
  `0ab6369a…..main`;
- **A6's six re-verifications**, the register's six names included;
- **A8's nine branch tips read back**, with
  `governance/integrate-supply-protocol-v3` shown still at `cc8adaa0…`;
- **A9's six exit statuses, taken after the advance**;
- **which reading of §2 you took**, and whether it changed anything;
- **§6's Rule 16 assessment**, junction named or search described;
- **whether authoritative `main` now reads as though the eighteen rules
  were enforced.** They are not;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently. **In particular: whether §1's departure from the
  reviewer's literal landing clause is sound**, and whether an
  integration specification should carry its landing clause inline
  instead of needing a task like this one.

## 9. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** Nothing here is asserted.

    target      current refs
    method      git fetch, then git rev-parse against origin
    CONFIRMED   origin/main = 0ab6369a…, UNCHANGED;
                governance/integrate-supply-protocol-v3 = cc8adaa0…,
                pushed and visible

    target      fast-forward availability
    method      git merge-base --is-ancestor 0ab6369a cc8adaa0
    CONFIRMED   exit 0. The advance requires no new object.

    target      the branch shape this specification asks for
    method      dry run — branch cut from cc8adaa0, three placeholder
                commits, then diff against both bases
    CONFIRMED   cc8adaa0 -> tip: exactly 3 additions, no other
                operation
    CONFIRMED   0ab6369a -> tip: 9 additions, 3 modifications
    CONFIRMED   merge commits introduced in cc8adaa0..tip: ZERO
    CONFIRMED   cc8adaa0 and 48268e6c are both ancestors of the tip
    CONFIRMED   0ab6369a is a strict ancestor of the tip, so the final
                advance is also a fast-forward

    target      the integration head, re-verified independently of the
                executor's report
    method      clean clone read at cc8adaa0
    CONFIRMED   scope from 0ab6369a: 6 additions, 3 modifications, no
                other operation
    CONFIRMED   the six arriving blob ids, all matching the values
                pinned in the integration specification's A6
    CONFIRMED   DECISION_LOG.md 82337 -> 89541 bytes, exact byte
                prefix, numstat 142/0
    CONFIRMED   GATES.md 849a4fbf…, 14 P2- sections,
                P2-PHASE-01 PROPOSED
    CONFIRMED   18 rules; 6 register entries with all six names
    CONFIRMED   the six register commits, none an ancestor of cc8adaa0
    CONFIRMED   tests/ tree object identical at 0ab6369a and cc8adaa0
    CONFIRMED   no Co-Authored-By, tool attribution or URL in any of
                the four commit messages on the branch

    target      the house pattern this specification follows
    method      git merge-base --is-ancestor for prior integration
                branch tips against origin/main
    CONFIRMED   gate/p2-integrate-chirality-census @ 57c5a6e,
                fix/integrate-si1-crossref @ 8701a97 and
                governance/land-rules-14-15 @ e045ee0 are each their
                own report commit and each an ancestor of main.
                Landing past the reviewed head is what this line has
                always done.
