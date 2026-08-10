# Task specification — integrate the SI-1 / `DEFERRED-02` cross-reference

Specification evidence base: `898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`

    Branch  fix/si1-deferred-02-crossref
            3830214126387663365aa7671d25d01d57e25d10

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see §4 commit 2 and A5.

**One merge.** Dry run: **3 additions, 1 modification**, no conflict,
merge-base is the original base. **If a conflict occurs, STOP.**

**Review artifact delimiters, stated as literals.** The supplied review
is bounded by these two lines, each occupying a whole line on its own:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

**Match them as complete lines**, and commit only what lies strictly
between them. **§0(a) records why this is now stated as a literal.**

---

## 0. What is being integrated, and two findings carried forward

One reference at the end of `P2-PHASE-01`'s `### Scope`:

> `derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a
> stationary branch that is neither admitted nor excluded; whether it
> falls within the existential quantifier of this gate's scientific
> question is therefore undetermined.

**`P2-DEFERRED-ITEMS` occurrences in `GATES.md`: 0 → 1.**

**Verified independently before this specification was written**, by
extracting each `## P2-` section from both revisions: **fourteen gates
before and after; `P2-PHASE-01` is the only section whose body differs;
the other thirteen are byte-identical.** Four lines were added, and they
are the reference. `P2-PHASE-01` remains `PROPOSED`; `P2-GAP-01` remains
`PASS`; `derivations/P2-DEFERRED-ITEMS.md` is unchanged — **the pointer
is one-directional.**

**The wording is more precise than the specification asked for**, and
the improvement should not be lost: *"the existential quantifier of this
gate's scientific question"* rather than *"this gate's existential
quantifier"*. **The entry contains two quantifiers** — the existential
one in the question, and a universal one in the kill criterion — **and
the shorter phrasing would have been ambiguous between them.**

### (a) The review artifact had no delimiters — a specification defect

A2 required delimiters to be matched **as whole lines**, but **this
specification's predecessor never stated what the delimiters were**, and
the supplied review text contained none. **The executor had to decide
the boundary itself**, taking the artifact from its title to the end of
the message.

**The result was correct. The procedure was not specified.** This is the
third distinct delimiter failure: first a delimiter string found inside
the instruction naming it; then the same again; **now no delimiter at
all.** **The pattern is that the supply protocol was never written
down**, and each task rediscovered it.

**This specification states the literals**, above. **A future
specification should not require the executor to infer a boundary.**

### (b) The cross-reference is not protected by any test

The executor mutation-tested it: **deleting `P2-PHASE-01`'s entire
103-line gate entry left `test_gate_anchors.py` and
`test_si1_governance.py` both green.**

**Two distinct findings, which should not be merged.** If a
specification claims those validators cover that section, that claim is
an **`OBSERVATION_METHOD_ERROR`** — a proxy mistaken for the property.
Separately, **the absence of any persistent check is a
`REPOSITORY_DEFECT`**: this task's A4 protected the section
mechanically *during this execution*, but **nothing prevents a later
silent deletion.**

**Neither is fixed here.** Adding a test would widen a reviewed scope,
and `tests/` is protected in this specification. **A separate task
should decide which governance-critical cross-references require
persistent test coverage** — and it is the same task the programme
already needs for the wider enforcement gap: **no test checks any of the
seventeen `CONVENTIONS.md` rules, and every recent specification
protects `tests/`.**

## 1. What this integration does NOT establish

- **It does not resolve SI-1's quantifier range.** The reference records
  that the question exists. **Nobody is assigned to answer it**, and
  answering it requires a PI decision on whether the negative-mass
  branch is an admissible phase.
- **It does not state that the branch is admissible or inadmissible**,
  and does not qualify the kill criterion.
- **It does not make SI-1 unable to proceed.** A specification that
  eventually runs SI-1 will need to state which reading of the
  quantifier it uses — **an observation about what the reference makes
  visible, not a governance requirement this specification imposes on
  future tasks.** An integration specification is the wrong permanent
  home for such a requirement; **whether it belongs in the gate or in
  `CONVENTIONS.md` is a separate governance decision.**
- **It does not add test coverage** for the reference or for anything
  else.
- **No gate status, no science, no result changes.**

## 2. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`; the source
branch to `38302141…`. Any mismatch → STOP. **Local `main` is stale by
design.** Report all refs, read from the remote.

**A2 — Merge parentage.** **Parent 1 is fixed by which commit you are
standing on.** With §4's commit order, the merge is executed **after the
pre-execution review has been committed**, so parent 1 is the review
commit.

    parent 1 = the integration pre-execution review commit (commit 2)
    parent 2 = 3830214126387663365aa7671d25d01d57e25d10
    merge-base(parent 1, parent 2)
             = 898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7

**Commit 1, the integration specification, MUST be an ancestor of
parent 1.** Verify and report that too.

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push. **The final guard carries TWO DISTINCT SHAs**: the merge
object under verification is the merge commit; remote agreement is
checked against the final report-commit head. **If the guard cannot
represent both roles separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    head: <computed final head>
    mode: exact
    add:
      reports/2026-08-09T2153Z_si1-deferred-02-crossref.md
      reports/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md
      reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md
      specs/2026-08-09T2153Z_si1-deferred-02-crossref.md
      specs/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md
    modify:
      GATES.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 6 additions and 1 modification.** Three
additions arrive from the branch; three are authored here. **An eighth
path is a defect.**

**A5 — This task's pre-execution review committed, unedited**, at
`reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md`,
**byte-identical to the text between the delimiter literals stated at
the head of this specification, excluding the delimiter lines
themselves and any instruction accompanying them.**

**You do not write, edit, summarise or reformat it. If a placeholder
appears inside its text, it stays as written** — resolve placeholders in
the path only. **If the supplied text is missing, has no delimiters, or
does not correspond to this specification, STOP and say which** —
**§0(a) is why that last clause is explicit.**

**A6 — `GATES.md` arrives intact.** Blob-identical to its source-branch
value `849a4fbfe62d6478f092a84b0175357a74bbbb06`.

**A6a — Exactly one gate section differs.** Extract each `## P2-`
section from base and merged head and verify:

    gate count             14 before, 14 after
    sections that differ   exactly {P2-PHASE-01}
    the other thirteen     byte-identical
    P2-PHASE-01 status     PROPOSED, unchanged
    P2-GAP-01 status       PASS, unchanged
    added content          the four-line reference, and nothing else

**A heading count is a proxy.** Report the section-body comparison.

**A7 — Arriving artifacts intact.** The three additions arriving from
the source branch are blob-identical to:

    reports/2026-08-09T2153Z_si1-deferred-02-crossref.md
    cad180e4bca3334d15bc4efb0aaaaf0556a821b0

    reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
    ed5eb0dbaf830c68082d35be98e6789a4050482a

    specs/2026-08-09T2153Z_si1-deferred-02-crossref.md
    2524c366a5f56f38d883bd3ec97e1ae39fc72833

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**A8 — Protected paths.** `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`, and **every path under `scripts/`,
`results/`, `tests/`, `derivations/`, `docs/` and `reviews/` that exists
at the evidence base**: blob-identical between base and merged head.
**Compare path by path, not as tree objects** — `reviews/` gains two
base-absent authorised paths, one arriving from the source branch and
one authored here.

**`derivations/P2-DEFERRED-ITEMS.md` and `tests/` are on that list
deliberately.** The pointer is one-directional, and §0(b)'s enforcement
gap is not closed here.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A9-pre** at the pre-report head goes
in the report; **A9-final** at the pushed head is post-report evidence.

**Do not report these as covering the cross-reference.** §0(b)
established by mutation that they do not. **Report them as passing, and
say what they actually assert.**

**A10 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

**A11 — Branch preserved.** `fix/si1-deferred-02-crossref` still
resolves to `38302141…`. **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 3. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
merge, `GATES.md` points at `DEFERRED-02`, `DEFERRED-02` names SI-1's
quantifier range, and four validators pass. **A reader could conclude
the quantifier question is tracked and the reference protected.**
**Neither holds:** nobody is assigned to the question, and §0(b)
established by mutation that no test protects the reference.

## 4. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md
    commit 3  --no-ff merge of the source branch
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-si1-crossref.md

**Commit 2 precedes the merge**, per Rule 15's timing clause.

**Committed report:** raw output for A1, A2, A6–A8, A9-pre, A10 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A9-final, the push,
the report commit's stored message read back from the object, and
ancestry confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the integration specification, its pre-execution
  review, and the integration report. **Everything arriving by merge is
  integrated exactly as reviewed and may not be edited.**
- **Do not add any test**, and do not modify `tests/`. §0(b)'s gap is a
  separate task.
- **Do not edit `derivations/P2-DEFERRED-ITEMS.md`.**
- **Do not resolve SI-1's quantifier range**, classify the negative-mass
  branch, or qualify any gate.
- **Do not claim that any validator covers the cross-reference.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref.**
- Any merge conflict is an immediate stop.
- Branch naming: use `fix/integrate-si1-crossref`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- everything listed in §4 under its correct layer;
- the merge commit SHA, its parents and merge-base, as distinct values;
- **A6a's section-by-section comparison**, showing exactly one gate
  section differs and the other thirteen byte-identical;
- the reference quoted as it stands at the merged head;
- **what the four validators actually assert**, and explicitly that they
  do not cover the cross-referenced section;
- confirmation that the source branch and the protected review branch
  remain at their recorded commits;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **§3's Rule 16 assessment**, junction named or search described;
- **whether the delimiter literals stated at the head of this
  specification removed the boundary judgement §0(a) describes.** If any
  judgement remained, **the supply protocol is still under-specified and
  the next task should know**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 7. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      GATES.md at fix/si1-deferred-02-crossref @ 38302141…
    method      section extraction on ^## P2- and body comparison
    check type  STRUCTURAL, then byte-equality per section

    CONFIRMED   14 gate sections before and after
    CONFIRMED   P2-PHASE-01 is the only section whose body differs
    CONFIRMED   the other thirteen are byte-identical
    CONFIRMED   four lines added, and they are the reference
    CONFIRMED   P2-DEFERRED-ITEMS occurrences: 0 at base, 1 at branch
    CONFIRMED   derivations/P2-DEFERRED-ITEMS.md unchanged between them
