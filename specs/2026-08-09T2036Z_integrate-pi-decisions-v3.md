# Task specification — integrate the PI decisions v3 replay

Specification evidence base: `7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`

    Branch  fix/pi-decisions-v3
            93de3218095cafdabcd0fda92abc31af33109879

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**Rules 1–17 are in force at this evidence base**, so this task is
governed by Rule 15: its pre-execution review is a committed artifact —
see §5 commit 2 and A5.

**One merge.** Dry run: **4 additions, 1 modification**, **no conflict**,
merge-base is the original base. **If a conflict occurs, STOP.**

---

## 0. What is being integrated

Three PI decisions of 2026-08-09 and the deferred-items register,
replayed on the current authoritative base after the earlier execution
lost conflict-free integrability.

    Decision 1   mean-field work proceeds in the SCALAR channel with a
                 real auxiliary field — a choice of direct route, NOT a
                 judgement that the V/A representation is wrong
    Decision 2   η is NOT selected; both signs are computed
    Decision 3   the negative-mass branch is DEFERRED, neither admitted
                 nor excluded

**`derivations/P2-DEFERRED-ITEMS.md`** records `DEFERRED-01` (the V/A
representation), `DEFERRED-02` (the negative-mass branch), and
`DEFERRED-03` (a PI hypothesis relating them, `UNTESTED`,
`Evidence: none`).

**The register holds work examined and consciously postponed**, not work
nobody has reached. Open questions live elsewhere.

## 1. A4's comparison scope, settled here rather than left to inference

**The replay's substantive equivalence check passed, and one aspect of
how it was reported needs pinning down before it becomes precedent.**

A4 defined a task-identity canonicalisation function for
`P2-DEFERRED-ITEMS.md`, and for the three `DECISION_LOG.md` rulings
specified only: strip blockquote prefixes, strip `**` and backticks,
collapse whitespace, keep en dashes. **It did not authorise
branch-name canonicalisation.**

**The executor found the entries differing in seven line pairs, all
inside `### Related branch and files`, and reported that adding a
branch-name canonicalisation would make them identical.** That phrasing
reads as though an acceptance criterion had been extended at execution
time. **It was not, and no extension was needed.**

**Verified directly:** `### Related branch and files` is a top-level
`###` section of each entry, **entirely outside the `> ` blockquote that
carries the ruling.** The ruling text lives in `### Decision`.

**So the correct reading is:**

    A4's ruling comparison covers   the ruling substantive text, i.e.
                                    the blockquote under ### Decision
    outside that comparison         entry-level metadata sections,
                                    including ### Related branch and
                                    files, which legitimately name this
                                    execution's branch

**The substantive ruling blockquotes are identical under A4's specified
normalisation.** The observed differences occur only in entry-level
metadata and are therefore outside the ruling-text comparison. **No
extra normalisation rule was adopted by the executor.**

**A9a below checks the metadata separately** — that it names the v3
branch and files correctly — rather than folding it into the
substantive comparison.

## 2. What the replay established, verified independently

**The task-identity canonicalisation of A4 was executed against both
registers before this specification was written:**

    differing lines before normalisation   exactly one
                                           Authority: specs/…v2.md
                                           Authority: specs/…v3.md
    after normalisation                    byte-identical, 8344 = 8344
    residual v2 references in the v3 file  zero

**Append-only held on both measures**, and more strongly than required:
**the base's `DECISION_LOG.md` is an exact byte PREFIX of the branch
head's.** Entries went 29 → 32; the three PI rulings are appended after
the two governance rulings; **no ordering judgement occurred anywhere.**

**That is the point of the replay.** The ordering is a consequence of
lineage, not of a merge resolver's choice, and **the rulings remain
dated 2026-08-09 — entry order records when each reached the
authoritative lineage, not when it was decided.**

## 3. What this integration does NOT establish

- **Decision 1 does not close `OPEN-AC-1`**; Decision 2 declines to
  select; Decision 3 declines to classify. **None is a physics result.**
- **`DEFERRED-03` has no evidence** and must not be read as carrying
  support comparable to the two evidence-backed entries.
- **It does not resolve `DEFERRED-02`'s consequence**: the SI-1 kill
  criterion's quantifier range remains undetermined, and `GATES.md`
  still does not reference the register. **That cross-reference is an
  agreed separate task and `GATES.md` is protected here.**
- **No gate, no science, no result changes.**

**One accumulated-reading risk, carried forward because it is the
strongest this programme has identified.** `DEFERRED-01` records the V/A
representation as deferred; the scalar channel was selected; and
`layers.json` labels V and A `REPULSIVE` with no real HS contour.
**Together these make available the inference that the V/A sector was
examined and set aside on physical grounds.** **It was not.** The
deferral is about which machinery exists — the programme's apparatus is
built for a real auxiliary field — **and `DEFERRED-01`'s PI position
says the opposite: that the V/A representation may contain physically
relevant information and must be returned to.**

**This integration does not resolve that risk**; it records it so a
later reader of the merged state does not assemble the stronger
conclusion.

## 4. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`; the source
branch to `93de3218…`. Any mismatch → STOP. **Local `main` is stale by
design.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §5's commit order, the merge is executed **after the
pre-execution review has been committed**, so parent 1 is the review
commit, not the specification commit.

    parent 1 = the integration pre-execution review commit (commit 2)
    parent 2 = 93de3218095cafdabcd0fda92abc31af33109879
    merge-base(parent 1, parent 2)
             = 7c5cba5df76de6ef8f52af390ca92100dcdf0d8b

**Commit 1, the integration specification, MUST be an ancestor of
parent 1.** Verify and report that too — it is still part of the chain
even though it is no longer the merge's first parent.

**An earlier version of this criterion named commit 1.** Rule 15 added
the review commit between the specification and the merge, and **A2 was
not re-read against that change** — the structural propagation
Amendment G requires.

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push. **The final guard carries TWO DISTINCT SHAs**: the merge
object under verification is the merge commit; remote agreement is
checked against the final report-commit head. **If the guard cannot
represent both roles separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-DEFERRED-ITEMS.md
      reports/2026-08-09T1958Z_pi-decisions-v3.md
      reports/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md
      reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
      reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md
      specs/2026-08-09T1958Z_pi-decisions-v3.md
      specs/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 7 additions and 1 modification.** Four
additions arrive from the branch; three are authored here. **A ninth
path is a defect.**

**A5 — This task's pre-execution review committed, unedited.** The
Reviewer's approval of THIS specification is supplied with it. Place it
at `reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md`,
**byte-identical to the text supplied between the supplied delimiters,
excluding the delimiter lines and any instruction accompanying them.**

**Locate the delimiters as WHOLE LINES**, not as first occurrences of
the delimiter string: **an instruction that names a delimiter contains
it, and searching for the first occurrence finds the instruction rather
than the boundary.** This has been met twice.

**You do not write, edit, summarise or reformat the review. If a
placeholder appears inside its text, it stays as written** — resolve
placeholders in the path only. **If the supplied text is missing or does
not correspond to this specification, STOP.**

**A6 — `DECISION_LOG.md` arrives intact and append-only.**
Blob-identical to its source-branch value
`04539f26a6bc39367d32f5cd6c6a887a1d05e491`, with **zero deleted lines
measured base-to-head AND, for the merge commit, against BOTH parents.**
Against parent 1 this shows the integration deleted none of the base's
log; against parent 2, that the merge dropped none of the branch's
entries. **They establish different things.**

**Additionally: the base's `DECISION_LOG.md` must be an exact byte
prefix of the merged head's.** That is stronger than a zero-deletion
diff and it held on the source branch; **it should survive the merge.**

**A7 — Arriving artifacts intact.** The four additions arriving from the
source branch are blob-identical to:

    derivations/P2-DEFERRED-ITEMS.md
    33b3a664e0578ded484e31ad7f96f3a2908bcbb1

    reports/2026-08-09T1958Z_pi-decisions-v3.md
    885399c243902f46ffa55291e075e029acf789d9

    reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
    eb77adfb19f288df2a64cdf76cb3b4f5a8185fd9

    specs/2026-08-09T1958Z_pi-decisions-v3.md
    706cc00f7ce09433ca975af1d943cb08592a6dc4

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**A8 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`pyproject.toml`, and **every path under `scripts/`, `results/`,
`tests/`, `derivations/`, `docs/` and `reviews/` that exists at the
evidence base**: blob-identical between base and merged head. **Compare
path by path, not as tree objects** — `reviews/` gains **two
base-absent authorised paths, one arriving from the source branch and
one authored by this integration task**, and
`derivations/P2-DEFERRED-ITEMS.md` does not exist at the base either.
**A8 does not compare any of the three.**

**`scripts/p2_channel_character_layers.py` and `GATES.md` are on that
list deliberately** — §3 names both as subjects of separate open items.

**A9 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; `P2-PHASE-01` still `PROPOSED`; `P2-GAP-01` still
`PASS`.

**A9a — Entry metadata checked separately from the ruling text**, per
§1. For each of the three PI-decision entries at the merged head,
confirm that `### Related branch and files` names `fix/pi-decisions-v3`
and this execution's paths. **Report it as a metadata check, not as part
of any ruling-text equivalence** — and **do not apply branch-name
canonicalisation to any comparison.**

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A10-pre** at the pre-report head
goes in the report; **A10-final** at the pushed head is post-report
evidence.

**A11 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

**A12 — Branches preserved.** `fix/pi-decisions-v3` still resolves to
`93de3218…`; `fix/pi-decisions-v2` to `ebd531ab…`; and
`fix/pi-decisions-and-deferred` to `52f651174dc1fef03b4fb9276078fa1f08d94bd7`.
**`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md
    commit 2  reviews/chatgpt/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md
    commit 3  --no-ff merge of the source branch
    commit 4  reports/2026-08-09T{HHMM}Z_integrate-pi-decisions-v3.md

**Commit 2 precedes the merge**, per Rule 15's timing clause.

**Committed report:** raw output for A1, A2, A6–A9a, A10-pre, A11 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A10-final, the
push, the report commit's stored message read back from the object, and
ancestry confirmation.

## 6. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**§3's V/A junction is offered as the leading candidate**, and it is the
strongest this programme has found. **If you identify a stronger one,
report that instead** — and **note that four executions of this task now
exist in the repository, each preserved**, which is itself a candidate:
a reader could take four executions for four substantive revisions. **It
was revised once on substance.**

## 7. Invariants and prohibitions

- Executor-writable: the integration specification, its pre-execution
  review, and the integration report. **Everything arriving by merge is
  integrated exactly as reviewed and may not be edited.**
- **Do not adopt any normalisation rule not stated in this
  specification**, and do not apply branch-name canonicalisation.
- **Do not add the SI-1 cross-reference**, and do not touch `GATES.md`
  or `scripts/p2_channel_character_layers.py`.
- **Do not classify the negative-mass branch, select `η`, or select a
  Hubbard–Stratonovich channel** beyond the scalar one Decision 1
  already selected.
- **Do not perform the diquark computation.** Decision 2 authorizes it;
  a separate specification issues it.
- **Do not state or imply that the V/A representation was set aside on
  physical grounds.** §3 records why that inference is available and
  wrong.
- **Do not back-fill or modify any existing review record.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref.**
- Any merge conflict is an immediate stop.
- Branch naming: use `fix/integrate-pi-decisions-v3`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 8. Report contract

- everything listed in §5 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **the three append-only measures of A6**, plus the byte-prefix check;
- **A9a's metadata check, reported separately from any equivalence
  comparison**;
- confirmation that **the three PI-decision branches and the protected
  `review/role-model-and-executors` branch** remain at their recorded
  commits;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **§6's Rule 16 assessment**, junction named or search described;
- **whether the merged state now reads as though any of the three
  decisions were a physics result**, or as though the V/A sector had
  been physically excluded;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 9. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      DECISION_LOG.md at fix/pi-decisions-v3 @ 93de3218…
    method      structural inspection of one PI-decision entry
    check type  STRUCTURAL — section nesting, not a string match

    CONFIRMED   `### Related branch and files` is a top-level ### section
                of the entry, outside the `> ` blockquote
    CONFIRMED   the ruling text sits in `### Decision` as a blockquote

**This is what settles §1**: the differing lines the executor reported
are outside the ruling-text comparison A4 defines, **so no additional
normalisation was needed and none is authorised.**

    target      derivations/P2-DEFERRED-ITEMS.md, v2 vs v3
    method      A4's task-identity canonicalisation, executed
    check type  BYTE-EQUALITY after the defined substitutions

    CONFIRMED   one differing line before normalisation (the Authority
                path); byte-identical after; 8344 = 8344; zero residual
                v2 references in the v3 file
