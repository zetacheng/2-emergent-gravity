# Task specification — cross-reference SI-1's gate entry to `DEFERRED-02`

Specification evidence base: `898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see A0 commit 2 and A2.

**This task adds one pointer. It changes no gate status, no verdict, no
science, and no decision.**

---

## 0. Why a pointer, and why it is not a caveat

`derivations/P2-DEFERRED-ITEMS.md` records, under `DEFERRED-02`:

    Blocks:  the quantifier range of the SI-1 kill criterion, which
             must state whether this branch falls inside it

**`GATES.md` does not reference that register anywhere.** Someone
designing SI-1 from its gate entry — which is where anyone would start —
**would not encounter the constraint at all.** Both reviewers identified
this independently when the PI decisions were reviewed, and both said it
should not be fixed inside that task.

**What the constraint is.** SI-1 asks whether the frozen theory
possesses **at least one** physically admissible stable condensed phase.
**The negative-mass stationary branch at `M̂ ≈ −7.59` is neither admitted
nor excluded** — a PI decision of 2026-08-09 — so **whether it falls
inside that existential quantifier is undetermined.** With it inside,
SI-1 may be unable to fail; with it outside, the quantifier ranges over
less.

**This is a pointer, not a caveat on the gate.** The gate's status,
question, scope, assumptions and criteria are unchanged. **What is added
is a reference telling a reader where an unresolved input to its
quantifier range is recorded.** **Do not qualify, weaken, or annotate
the kill criterion itself.**

## 1. What to add

**One reference inside `P2-PHASE-01`'s entry in `GATES.md`.** Place it
where a reader designing the gate will meet it before writing criteria —
**the `### Scope` section is the natural home**, since the quantifier
range is a scope question. **If the entry's structure makes another
section clearly better, use it and say why.**

The reference must state three things and no more:

    1  that DEFERRED-02 records a stationary branch neither admitted
       nor excluded
    2  that whether it falls within this gate's existential quantifier
       is therefore undetermined
    3  where it is recorded: derivations/P2-DEFERRED-ITEMS.md

**It must not:**

- **assert or deny that the branch is admissible** — that is the PI's
  and is deferred;
- **qualify the gate's status, question or criteria**;
- **suggest the gate cannot proceed.** It can; the specification that
  eventually runs SI-1 must simply state which reading of the quantifier
  it uses.

**Nothing else in `GATES.md` changes.** No other gate is touched, no
status moves, no anchor is added or removed.

## 2. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md
    commit 3  GATES.md
    commit 4  reports/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the work**,
per Rule 15.

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP.
Method for each: `git cat-file blob <rev>:<path> | sha256sum`.

    GATES.md
    dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f

    derivations/P2-DEFERRED-ITEMS.md
    47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599

**A2 — This task's pre-execution review committed, unedited**, at
`reviews/chatgpt/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md`,
**byte-identical to the text supplied between the supplied delimiters,
excluding the delimiter lines and any accompanying instruction.**

**Locate the delimiters as WHOLE LINES**, not as first occurrences of
the delimiter string — an instruction naming a delimiter contains it.
**If a placeholder appears inside the review's text it stays as
written**; resolve placeholders in the path only. **If the supplied text
is missing or does not correspond to this specification, STOP.**

**A3 — `DEFERRED-02`'s `Blocks:` line quoted** from the pinned register,
and the added reference shown to correspond to it. **If the register
does not say what §0 quotes, STOP** — this task's premise is that
constraint.

**A4 — The reference added, and nothing else in `GATES.md` changed.**

    ^## P2- count          14 before and after
    every other gate       byte-identical, section by section
    P2-PHASE-01's status   PROPOSED, unchanged
    P2-GAP-01's status     PASS, unchanged

**Extract each `## P2-` section from base and head and compare.**
Exactly one section differs, and its difference is the added reference.
**Heading equality is a proxy; report the section-body comparison.**

**A5 — The reference says three things and no more**, per §1. Quote it
in full and **state, for each of the three prohibitions, that it does
not do that.**

**A6 — Nothing else touched.** `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`, and **every path under `scripts/`,
`results/`, `tests/`, `derivations/`, `docs/` and `reviews/` that exists
at the evidence base**: blob-identical. **Compare path by path, not as
tree objects** — `reviews/` gains one base-absent authorised path.

**`derivations/P2-DEFERRED-ITEMS.md` is on that list.** The pointer goes
one way, from the gate to the register; **the register is not edited.**

**A7 — Scope**, three additions and one modification:

    add:
      specs/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md
      reports/2026-08-XXT{HHMM}Z_si1-deferred-02-crossref.md
    modify:
      GATES.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 3 additions and 1 modification.**

**A8 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A8-pre** at the pre-report head goes
in the report; **A8-final** at the pushed head is post-report evidence.

**`test_gate_anchors.py` and `test_si1_governance.py` both constrain
this file. Report exactly what they assert about `GATES.md`** — a
governance test that examines the file this task edits is worth knowing
about, and **if either fails, do not adjust the reference to satisfy it
without saying so.**

**A9 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

**A10 — Commit-message hygiene** on every commit: inspect the proposed
message before, the stored message after; permit no `Co-Authored-By`, no
session identifier or URL, no tool attribution. **Report per commit
whether any trailer was suppressed and which.**

## 3. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task, `GATES.md` will point at `DEFERRED-02`, and `DEFERRED-02` names
SI-1's quantifier range. **A reader could conclude the quantifier
question is now resolved, or that it is being tracked toward
resolution.** **It is neither.** The pointer records that the question
exists; **nobody is assigned to answer it, and answering it requires a
PI decision on whether the negative-mass branch is an admissible phase.**

## 4. Evidence layering

**Committed report:** A1–A7, A8-pre, A10, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A8-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the four paths of A7 only.
- **Do not edit `derivations/P2-DEFERRED-ITEMS.md`.** The reference is
  one-directional.
- **Do not change any gate status, verdict, question, scope statement,
  locked assumption or criterion** beyond adding the reference.
- **Do not state or imply that the negative-mass branch is admissible or
  inadmissible**, or that SI-1 cannot proceed.
- **Do not resolve the quantifier range.** That is a PI decision this
  task exists to make visible, not to make.
- No digest or hash-pinned artifact may be modified.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/si1-deferred-02-crossref`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A8, scope-checker JSON verbatim including
  `observed_operations`;
- `DEFERRED-02`'s `Blocks:` line quoted from the pinned register;
- the added reference quoted in full, with the three prohibitions
  addressed one by one;
- **A4's section-by-section comparison**, showing exactly one gate
  section differs;
- what `test_gate_anchors.py` and `test_si1_governance.py` assert about
  `GATES.md`;
- **§3's Rule 16 assessment**, junction named or search described;
- **whether the added reference would change how you would write an SI-1
  execution specification.** If it would not — if a reader could still
  design the gate without meeting the constraint — **the pointer is in
  the wrong place and this task has not achieved its purpose**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 7. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      derivations/P2-DEFERRED-ITEMS.md at 898aecd1…
    digest      47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd
    method      Python substring containment against the raw text
    check type  EXACT LITERAL SUBSTRING — no normalisation

    PASS   the quantifier range of the SI-1 kill criterion

    target      GATES.md at 898aecd1…
    digest      dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f

    PASS   ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    PASS   ### Scope
    CONFIRMED  count of "P2-DEFERRED-ITEMS" occurrences in GATES.md: 0

**That last count is the finding this task exists to change.**
