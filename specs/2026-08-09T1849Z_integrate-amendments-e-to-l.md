# Task specification — integrate amendments E–L and Rules 16 and 17

Specification evidence base: `a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed`

    Branch  governance/land-amendments-e-to-l
            c58f1b9148828b8b37e775c6c499848bb63fd781

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**One merge.** Dry run: **4 additions, 2 modifications**, no conflict,
merge-base is the original base. **If a conflict occurs, STOP.**

**Rules 1–15 are in force at this evidence base**, so **this task is
governed by Rule 15**: its pre-execution review is a committed artifact
— see §5 commit 2 and A5. **Rules 16 and 17 do NOT exist at the evidence
base; they arrive with this merge.**

---

## 0. What is being integrated

`CONVENTIONS.md` goes from **1–15 to 1–17**, and six rules gain seven
refinements:

    Amendment E  -> Rule 14   a failed observation is not a negative result
    Amendment F  -> Rule 12   mutation tests must prove reach
    Amendment G  -> Rule 9    structural changes propagate
    Amendment H  -> Rule 3    literals are verified by execution
    Amendment I  -> Rule 8    mid-task authority needs reviewer-visible
                              provenance
    Amendment K  -> Rule 5    re-issuing an executed specification
    Amendment L  -> Rule 9    consumed conventions must be discoverable

    New Rule 16               Accumulated reading
    New Rule 17               Integrations do not add epistemic or
                              governance classifications

**Rule 9 takes two, G and L, landed as distinct blocks and not merged.**

**Verified independently before this specification was written**, by
extracting each rule section from both revisions: **rules 1–15 keep
their titles, and exactly six rule bodies changed — 3, 5, 8, 9, 12 and
14.** Rule 15's extracted block differs by one trailing newline, an
artifact of it no longer being the file's last section; **its content is
identical after `rstrip`.** No rule was silently reworded.

**The amendments' justification is committed**, not left in
conversation: `docs/amendments/2026-08-09_observation-and-propagation.md`
is byte-identical to the reviewed draft, digest
`6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4`.

**Rule 15's lifecycle ran for the first time** on the source branch —
specification, then review, then work, then report, with the review
commit an ancestor of the work commit. **This integration follows the
same lifecycle.**

## 1. Three findings the source task reported, carried forward

**These are recorded because this specification requires it — Rule 16
does not yet govern — and because none is closed by this merge.**

**(a) Amendment I's first live instance exposed a process weakness.**
The specification did not resolve an ambiguity in A4a — whether a
`{HHMM}` placeholder inside the supplied review text should be resolved,
or only in the filename — and **the instruction that resolved it was
given in a chat message.** Amendment I, which the task was landing at
that moment, names exactly that as what it exists to prevent.

**The durable authority chain nevertheless remained complete**, because
**the committed Reviewer artifact independently stated the same rule**:
*「其中 `{XX}`、`{HHMM}` 應由 Executor 按 A0 與 commit 1 已固定的 token
解析;不要把本段中的 placeholder 當成 literal filename。」*

**So the weakness is in the specification, not in the authority chain.**
A clause in A4a would have put the resolution where Amendment I
requires, instead of leaving it to be supplied twice. **Later
specifications should state the scope of placeholder resolution —
filename versus body — explicitly**, and A5 of this one does.

**(b) Amendment L lands with a known unsatisfied instance already on
`main`.** `scripts/p2_channel_character_layers.py` locates two PI
rulings by exact `DECISION_LOG.md` heading text, and neither is
referenced from `CONVENTIONS.md`. **L is prospective, so this is not a
breach** — but the item now has a rule behind it and an identified
instance. **Raised ten times as an observation; this is the first time
as a rule.**

**(c) Rule 13 carries two diagnostic orders**, with
`docs/local/execution_environment.md` still pointing at the ambiguous
rule. **Amendment E lands in Rule 14, immediately after it.**

**None of (a), (b) or (c) is addressed here.** They are follow-ups, and
recording them is what Rule 16 will require of a task adding to an
evidentiary chain **once it is operative** — this specification asks for
it now.

## 2. What this integration does NOT establish

- **It does not close (a), (b) or (c).**
- **It does not make the two conventions in
  `p2_channel_character_layers.py` discoverable**, and does not touch
  that script.
- **It does not resolve Rule 13's ambiguity** or update
  `docs/local/execution_environment.md`.
- **It does not back-fill any review record.** Rule 15 is prospective;
  the only review artifact arriving is the source task's own.
- **No gate, no science, no result changes.**

## 3. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed`; the source
branch to `c58f1b91…`. Any mismatch → STOP. **Local `main` is stale by
design.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §5's commit order it is the specification commit.

    parent 1 = the integration specification commit (commit 1)
    parent 2 = c58f1b9148828b8b37e775c6c499848bb63fd781
    merge-base(parent 1, parent 2)
             = a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push. **The final guard carries TWO DISTINCT SHAs**: the merge
object under verification is the merge commit; remote agreement is
checked against the final report-commit head. **If the guard cannot
represent both roles separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
    head: <computed final head>
    mode: exact
    add:
      docs/amendments/2026-08-09_observation-and-propagation.md
      reports/2026-08-09T1801Z_land-amendments-e-to-l.md
      reports/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md
      reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
      reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md
      specs/2026-08-09T1801Z_land-amendments-e-to-l.md
      specs/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md
    modify:
      CONVENTIONS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 7 additions and 2 modifications.** Four
additions arrive from the branch; three are authored here — this
specification, its pre-execution review, and this task's report.
**A tenth path is a defect.**

**A5 — This task's pre-execution review committed, unedited.** The
Reviewer's approval of THIS specification is supplied with it. Place it
at `reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md`,
**byte-identical to the text supplied between the supplied delimiters,
excluding the delimiter lines themselves and any instruction
accompanying them.** Report its committed blob digest.

**You do not write it, edit it, summarise it, or reformat it.** **If a
placeholder appears inside the review's text, it stays as written** —
resolve placeholders only in the path. **If the supplied text is missing
or does not correspond to this specification, STOP.**

**A6 — `CONVENTIONS.md` arrives intact.** Blob-identical to its
source-branch value `0db56c39d44e19126b1035b13ebcf357259c482f`.

**A6a — Rules 1–15 unchanged apart from the seven authorised
insertions.** Extract each `### <n>. <title>` section from base and
merged head and verify:

    rules present            base 1-15, head 1-17
    titles 1-15              identical
    rule bodies that differ  exactly {3, 5, 8, 9, 12, 14}
    Rule 15                  identical after rstrip; its extracted block
                             gains one trailing newline because it is no
                             longer the file's last section
    the other eight bodies   byte-identical

**Heading equality alone is a proxy.** Report the body comparison.

**A7 — `DECISION_LOG.md` arrives intact and append-only.**
Blob-identical to `bdb9dac59cc84416b51e626c7b26a0a7c956d68e`, with
**zero deleted lines measured base-to-head AND, for the merge commit,
against BOTH parents.** Against parent 1 this shows the integration
deleted none of the base's log; against parent 2, that the merge dropped
none of the source branch's entries. **They establish different things.**

**A8 — Arriving artifacts intact.** The four additions arriving from the
source branch are blob-identical to:

    docs/amendments/2026-08-09_observation-and-propagation.md
    642b2541571dcb6fa91edb36bbc75dc93df33f6b

    reports/2026-08-09T1801Z_land-amendments-e-to-l.md
    4e9f40e2b8e2a30948bd8df3b2e5c80376adc4ec

    reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
    10a95fca0b56638f0115963e1d14ad99fe95dcb3

    specs/2026-08-09T1801Z_land-amendments-e-to-l.md
    fb4dbf2094453ec891265fb3d3bd32f4f5090dbf

**These are Git blob ids, not content SHA-256 digests.**

**Separately, confirm the committed amendment draft's CONTENT digest is
`6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4`** —
the blob id proves it arrived unaltered; the SHA-256 proves it is the
reviewed draft.

**A9 — Protected paths.** `AGENTS.md`, `GATES.md`, `pyproject.toml`, and
**every path under `scripts/`, `results/`, `tests/`, `derivations/`,
`reviews/` and `docs/` that exists at the evidence base**:
blob-identical between base and merged head. **Compare path by path, not
as tree objects** — `reviews/` and `docs/` both gain paths this task
authorises.

**`scripts/p2_channel_character_layers.py` is on that list.** §1(b)
identifies it as Amendment L's known unsatisfied instance; **this
integration does not touch it.**

**A10 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; `P2-PHASE-01` still `PROPOSED`; `P2-GAP-01` still
`PASS`.

**A11 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A11-pre** at the pre-report head
goes in the report; **A11-final** at the pushed head is post-report
evidence. **If any validator asserts a rule count, report what it
asserts** — the file just gained two more rules.

**A12 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

**A13 — Branch preserved.** `governance/land-amendments-e-to-l` still
resolves to `c58f1b91…`. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 4. Accumulated-reading assessment, in Rule 16's form

**Rule 16 is NOT governing authority for this task.** It does not exist
at the evidence base and becomes operative only when this merge lands;
the execution-discipline rules bind prospectively, and a rule appearing
in a merge commit does not retroactively govern the task that merged it.

**This specification nevertheless REQUIRES a Rule-16-form
accumulated-reading assessment**, as an acceptance and reporting
requirement of its own — **both to exercise the rule prospectively and
because the assembled merged state should be read before the push, not
after.** State what the assembled governance set does NOT establish,
**naming the junction or reporting a search.**

**A candidate junction, offered so you can confirm or replace it.**
`CONVENTIONS.md` will carry seventeen rules, `DECISION_LOG.md` six
recent rulings, and `docs/amendments/` one justification document.
**A reader assembling those could conclude that the programme's
execution discipline is now complete and self-consistent.** It is not:
§1 records three open items, and **the rules have never been read
together against each other.**

**If you find a stronger junction, report that instead.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md
    commit 2  reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md
    commit 3  --no-ff merge of the source branch
    commit 4  reports/2026-08-09T{HHMM}Z_integrate-amendments-e-to-l.md

**Commit 2 precedes the merge**, per Rule 15's timing clause.

**Committed report:** raw output for A1, A2, A5–A10, A11-pre, A12 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A11-final, the
push, the report commit's stored message read back from the object, and
ancestry confirmation.

## 6. Invariants and prohibitions

- Executor-writable: the integration specification, its pre-execution
  review, and the integration report. **Everything arriving by merge is
  integrated exactly as reviewed and may not be edited.**
- **Do not address §1's findings (a), (b) or (c).**
- **Do not touch `scripts/p2_channel_character_layers.py`**, and do not
  add any conventions-index entry.
- **Do not back-fill or modify any existing review record.**
- **Do not modify `AGENTS.md`**, and do not renumber anything.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref.**
- Any merge conflict is an immediate stop, including in
  `CONVENTIONS.md` and `DECISION_LOG.md`.
- Branch naming: use `governance/integrate-amendments-e-to-l`.
- Environment: rule 13's diagnostic order applies. **Rule 13 carries two
  such orders — §1(c). If they differ for what you need, report which
  you followed and why.** **Do not install anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- everything listed in §5 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **the A6a extraction**, showing which rule bodies changed, the Rule 15
  newline artifact, and that the rest are byte-identical;
- the rule heading list at the merged head, 1–17;
- Rules 16 and 17 quoted in full as they now stand;
- the committed draft's blob id and content digest, both;
- the `DECISION_LOG.md` diff with **all three** append-only measures;
- **§4's accumulated-reading assessment**, with the junction named or
  the search described;
- **whether any of the seventeen rules now reads as contradicted by
  another.** This is the first time all seventeen sit together;
- **two separate questions, not one.** First: **whether this task
  complied with the rules actually in force at its evidence base**,
  especially Rule 15. Second, and separately: **whether its execution
  would ALSO satisfy Amendments H, I and K and Rule 17 as landed by this
  merge** — a prospective self-application check, **not a retrospective
  authority claim.** **If the second finds a violation, that is worth
  more than a clean report**, even though those rules did not govern
  this task;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
