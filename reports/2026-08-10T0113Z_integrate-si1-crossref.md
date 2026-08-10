# Report — integrate the SI-1 / `DEFERRED-02` cross-reference

Specification: `specs/2026-08-10T0113Z_integrate-si1-crossref.md`
Specification sha256:
`d0c0ec7be6de8ae45464139582990435d02587c7fe201ca35cee0a1acf503434`
Pre-execution review: `reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md`
Evidence base: `898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`
Source branch: `fix/si1-deferred-02-crossref` @ `3830214126387663365aa7671d25d01d57e25d10`
Integration branch: `fix/integrate-si1-crossref`
Classification: MATERIAL.

---

## 0. Summary

One merge, no conflict. The reference arrived exactly as reviewed:
`GATES.md` is blob-identical to its source-branch value, fourteen `## P2-`
gate sections before and after, `P2-PHASE-01` the only section whose body
differs, the other thirteen byte-identical. `P2-DEFERRED-ITEMS`
occurrences in `GATES.md`: **0 → 1**.

Three things a reader of this report should not miss:

- **A guard failed once, by my construction error, and I report it in
  full** (§4). `PRE_MERGE` evaluates `pinned_artifacts` at the *reviewed
  branch head*, not at the base; I had pinned `GATES.md` to its base
  value. Nothing was modified — a guard run is read-only — and the
  corrected pin then asserted something worth asserting.
- **The delimiter literals removed the boundary judgement almost
  entirely, but not quite** (§3). One residual normalisation remained: a
  single leading blank line. I quantify it to the byte and say what I
  chose.
- **The mutation evidence is now stronger than §0(b) states** (§9).
  Deleting `P2-PHASE-01`'s whole entry leaves **all four** validators
  green — not just the two named — and so does deleting *only the added
  reference*, which returns the occurrence count to 0.

No STOP condition fired.

---

## 1. A1 — refs, read from the remote

    remote refs/heads/main                            898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    refs/remotes/origin/main                          898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    remote refs/heads/fix/si1-deferred-02-crossref    3830214126387663365aa7671d25d01d57e25d10
    refs/remotes/origin/fix/si1-deferred-02-crossref  3830214126387663365aa7671d25d01d57e25d10
    local main (stale by design)                      0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both `main` refs resolve to the evidence base and the source branch to
`38302141…`; no mismatch, so no STOP. Local `main` is stale by design and
was neither consulted nor repaired.

---

## 2. Commits 1–3

    commit 1  abef7d2bff281662051c5f6f1d00153d672457b5
              specs/2026-08-10T0113Z_integrate-si1-crossref.md
              "spec: integrate the SI-1 / DEFERRED-02 cross-reference"

    commit 2  025c88b1073f177f8435da0fe3e515962364989a
              reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md
              "review: commit the pre-execution review for the SI-1
               cross-reference integration"

    commit 3  65ace0389df7bad4cf8cd73a21e30d8b842ecdfe
              --no-ff merge of the pinned remote ref
              "merge: integrate the SI-1 / DEFERRED-02 cross-reference
               (reviewed; pinned 3830214)"

Full stored messages are reproduced in §12 alongside the hygiene scans.

**A2 — merge parentage**, as distinct values:

    merge commit        65ace0389df7bad4cf8cd73a21e30d8b842ecdfe
    parent 1            025c88b1073f177f8435da0fe3e515962364989a   = commit 2, the review
    parent 2            3830214126387663365aa7671d25d01d57e25d10   = the source branch
    merge-base(p1,p2)   898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7   = the evidence base

    commit 1 (abef7d2b) is an ancestor of parent 1:  yes

Parent 1 is the review commit because §4's order puts the review before
the merge and parent 1 is fixed by which commit one is standing on. This
is Rule 15's structure showing up in the object graph.

**Dry run before the merge**, `git merge-tree --write-tree --name-only`:

    predicted tree   02e4795433f2556c7814e274bef6963b52b7da83
    conflict output  (none)

    base..source, name-status:
      M  GATES.md
      A  reports/2026-08-09T2153Z_si1-deferred-02-crossref.md
      A  reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
      A  specs/2026-08-09T2153Z_si1-deferred-02-crossref.md

Three additions and one modification, no conflict, merge-base equal to
the original base — as the specification's header predicted. The
predicted merged tree differs from the source tree only by this
integration's own two artifacts, confirming the merge introduces nothing
else.

---

## 3. A5 — the pre-execution review, and whether the delimiter literals worked

Committed at `reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md`
in commit 2, before the merge, per Rule 15.

    committed blob sha256  ba9aed51c343c31e1af9e2f7a54b1f948511eb9a185e8fe3389fd12dffa865cd
    git blob id            b2b5d639cbaa4b46e0c7c4510528c0c8b9da25ba
    size                   8101 bytes, 8073 characters, 68 lines
    identical to the extracted text:  True

**Delimiter location, by whole-line match:**

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: line 4    ENDS: line 75
    lines strictly between  70

I matched whole lines as instructed, and record for the next task that on
*this* message a first-occurrence search would also have succeeded — the
specification file was supplied as an attachment rather than inlined, so
its §head literals were not in the message text. The whole-line
requirement cost nothing and is still the right rule; it simply was not
load-bearing this time. Reporting it because the opposite would be worth
knowing and only a count distinguishes the two.

**Correspondence check** before committing, against A5's STOP clause. The
supplied text is present, has delimiters, and corresponds — it names this
integration by title, both SHAs (`38302141…`, `898aecd1…`), criterion
`A6a`, Rule 15 and Rule 16. None of A5's three STOP conditions was met.

### The report contract's question: did the literals remove the boundary judgement?

**Almost entirely — one residual decision remained, and it is one byte.**

The specification's §0(a) describes an executor deciding *where the
artifact starts and ends*. That judgement is gone: two whole-line matches,
one occurrence each, no inference. Had the delimiters been stated this
way last time, §0(a) would not have been written.

What remains is not a boundary question but a trailing-whitespace one.
The text strictly between the two delimiter lines is:

    literal slice   8102 bytes
                    leading newlines: 1     trailing newlines: 1

because each delimiter sits on its own line with a blank line of
separation. Committing that literally would have produced a file
beginning with a blank line. I removed the single leading newline and
kept exactly one trailing newline:

    committed       8101 bytes
    difference from the literal slice: one leading blank line
    identical after stripping leading/trailing newlines:  True

That choice was made on evidence rather than taste: every prior artifact
in `reviews/chatgpt/` begins at its own first content line, none with a
blank first line.

**For the next specification.** The remaining gap is that A5 says
"byte-identical to the text between the delimiter literals" while the
delimiters are line-oriented, so "the text between" is ambiguous by
exactly the newlines adjacent to them. One sentence fixes it — e.g. *the
committed artifact is the delimited lines exclusive, joined by newlines,
with leading and trailing blank lines removed and a single trailing
newline*. Until that sentence exists, **the supply protocol is still
under-specified, though by one byte rather than by a whole boundary.**

**The review's non-blocking observation, recorded and not acted on.** The
Reviewer observed that an integration specification is not the durable
home for a requirement binding all future SI-1 tasks. §1 of this
specification already frames that sentence as an observation rather than a
rule, and explicitly leaves the gate-versus-`CONVENTIONS.md` question to a
separate governance decision. Nothing in this integration acts on it, and
this report does not convert it into one.

---

## 4. A3 — guards, including the one that failed

### `PRE_MERGE`, first attempt: FAIL, my construction error

    "condition": "pinned_artifacts", "status": "FAIL"
      GATES.md
        expected  dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f
        actual    8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526   FAIL
      derivations/P2-DEFERRED-ITEMS.md   PASS
      CONVENTIONS.md                     PASS
    overall FAIL, EXIT=2

**Diagnosed before changing anything.** The working tree's `GATES.md` was
`dbe797ab…` and so was `HEAD:GATES.md` and `898aecd1:GATES.md` — the
integration worktree was exactly at base content. Reading the tool:

    scripts/governance_tools/merge_guard.py:76
        pins = _pins(repo, branch_head, config)

`PRE_MERGE` evaluates `pinned_artifacts` at the **reviewed branch head**,
not at the base or the worktree. `8ce38b8a…` is `GATES.md` at
`38302141…` — the arriving value, reported correctly. **My config was
wrong, not the tool and not the specification.** I had pinned the file to
the value it holds *before* the change, on a criterion whose purpose is to
assert what *arrives*.

Corrected pin: `GATES.md` → `8ce38b8a…`, which is the same object A6
requires by blob id. The other two pins were already right and meaningful
for the same reason inverted: `derivations/P2-DEFERRED-ITEMS.md` and
`CONVENTIONS.md` are pinned to their base values *and* pass at the branch
head, which asserts the branch does not touch them.

**Nothing was modified by the failed run.** The guard performs
`git status` and read-only object reads; the worktree was verified clean
and at `025c88b1…` immediately afterward.

### `PRE_MERGE`, corrected: PASS

    $ python -m scripts.governance_tools.merge_guard --repo . --config i11_pre_cfg.json
    EXIT=0
    {
      "checks": [
        { "condition": "worktree_clean", "entries": [], "status": "PASS" },
        { "attachment": "fix/integrate-si1-crossref",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "025c88b1073f177f8435da0fe3e515962364989a",
          "status": "PASS",
          "worktree_head": "025c88b1073f177f8435da0fe3e515962364989a" },
        { "actual": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
          "condition": "merge_base",
          "expected": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
          "status": "PASS" },
        { "condition": "scope",
          "evidence": {
            "base": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
            "failures": [],
            "head": "025c88b1073f177f8435da0fe3e515962364989a",
            "mode": "exact",
            "observed_operations": [
              { "operation": "add",
                "path": "reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md" },
              { "operation": "add",
                "path": "specs/2026-08-10T0113Z_integrate-si1-crossref.md" }
            ],
            "overall": "PASS",
            "tool": "scope_checker" },
          "status": "PASS" },
        { "condition": "pinned_artifacts",
          "evidence": [
            { "actual": "8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526",
              "expected": "8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526",
              "path": "GATES.md", "status": "PASS" },
            { "actual": "47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd",
              "expected": "47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd",
              "path": "derivations/P2-DEFERRED-ITEMS.md", "status": "PASS" },
            { "actual": "e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451",
              "expected": "e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451",
              "path": "CONVENTIONS.md", "status": "PASS" }
          ],
          "status": "PASS" }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }

(`other_registered_worktrees` is omitted from the quotation only; it
listed 25 worktrees and no failure depends on it.)

### `POST_MERGE`, intended parameters

A3 requires the final guard to carry **two distinct SHAs** in **two
distinct roles**. The tool supports this: `merge_commit` names the object
under verification and `expected_remote_sha` names the ref agreement
target, and they are separate keys. **The guard can represent both roles
separately, so no STOP.** Intended configuration:

    mode                    POST_MERGE
    merge_commit            65ace0389df7bad4cf8cd73a21e30d8b842ecdfe   <- the merge object
    expected_parent_1       025c88b1073f177f8435da0fe3e515962364989a
    expected_parent_2       3830214126387663365aa7671d25d01d57e25d10
    expected_merge_base     898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    scope_manifest          the final manifest of §7
    pinned_artifacts        GATES.md                          8ce38b8a…072e526
                            derivations/P2-DEFERRED-ITEMS.md  47b22bbb…0658cd
                            CONVENTIONS.md                    e3afa521…f94a451
    remote_check_policy     REQUIRED
    expected_remote_ref     refs/remotes/origin/main
    expected_remote_sha     <the final report-commit head>    <- ref agreement

The two roles hold different values by construction: the merge object is
`65ace038…` and the remote target is the report commit that sits above
it. The `GATES.md` pin is the merged value here, for the same reason the
`PRE_MERGE` pin had to be the arriving one.

---

## 5. A6 — `GATES.md` arrives intact

    merged head blob id     849a4fbfe62d6478f092a84b0175357a74bbbb06
    source branch blob id   849a4fbfe62d6478f092a84b0175357a74bbbb06
    A6 expects              849a4fbfe62d6478f092a84b0175357a74bbbb06   MATCH

    sha256 at the merged head
      8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526

Blob-identical: the merge did not rewrite, re-encode or reflow the file.

---

## 6. A6a — exactly one gate section differs

Each `## P2-` section extracted from base and merged head, heading line to
the line before the next `## P2-` heading, compared **body to body**.
Digests are sha256 of the section text, first 8 hex characters.

    gate count                base: 14    merged head: 14
    headings identical        True   (this is the proxy)

    SECTION                                                        BASE      HEAD
    ## P2-HK-01 — Heat-kernel species coefficients                 6be205b8  6be205b8  identical
    ## P2-GAP-01 — Gap-equation criticality (continuum + lattice)  d3d35fe2  d3d35fe2  identical
    ## P2-BETA-01 — Lattice mass-scan extraction of `β_B`          9655d3b7  9655d3b7  identical
    ## P2-BETAV-01 — Lattice `β_V/β_B` (Proca / Stueckelberg)      5c2b98b8  5c2b98b8  identical
    ## P2-NORM-01 — Locate the `β`/`G` normalization factor 2      afaed93c  afaed93c  identical
    ## P2-BETAV-CIRC-01 — Does the lattice `β_V` test discriminate f9c7fbb0  f9c7fbb0  identical
    ## P2-BETAV-NUMREPRO-01 — Numerical reproduction of `β_V/β_B`  d44e7373  d44e7373  identical
    ## P2-BETAV-RECON-01 — Clean-room curved-background Proca reco f520f45f  f520f45f  identical
    ## P2-BETAV-ASSEMBLY-01 — Determinant-bookkeeping regression ( 6656473b  6656473b  identical
    ## P2-CHANNEL-FREEZE-01 — Freeze the HS/Fierz channel basis +  81a57766  81a57766  identical
    ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)   c1fb257d  dc86eff9  *** DIFFERS ***
    ## P2-MULTIPHASE-GRAV-01 — Programme-death: does any phase giv 18c94ae3  18c94ae3  identical
    ## P2-GRAV-ENGINE-RECOVERED-01 — Recovered historical gravity  7d92c83a  7d92c83a  identical
    ## P2-LATTICE-ONTOLOGY-01 — Physical H(4) lattice substrate sp e08a5419  e08a5419  identical

    sections that differ:  1  ->  {P2-PHASE-01}
    the other thirteen byte-identical:  True

**A6a warns that a heading count is a proxy.** The heading row above is
that proxy, reported and set aside; the body digests are what the verdict
rests on.

The one differing body, in full:

    ---- body diff: ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    --- base
    +++ merged head
    @@ -15,2 +15,7 @@
     the pre-registered microscopic parameter domain (policy §2, §4).
    +
    +`derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a stationary
    +branch that is neither admitted nor excluded; whether it falls within the
    +existential quantifier of this gate's scientific question is therefore
    +undetermined.

    added lines: 5   removed lines: 0
    added content, excluding the blank separator:
        `derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a stationary
        branch that is neither admitted nor excluded; whether it falls within the
        existential quantifier of this gate's scientific question is therefore
        undetermined.

**The four-line reference and nothing else**, as A6a requires: five added
lines of which one is the blank separator, zero removed, zero modified.

Statuses, read by the same method the repository's own validator uses:

    P2-PHASE-01   base 'PROPOSED'
                  head 'PROPOSED'                                     unchanged
    P2-GAP-01     base 'PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)'
                  head 'PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)'
                                                                      unchanged

Text before the first `## P2-` heading, which the section extraction would
otherwise not cover: identical.

    P2-DEFERRED-ITEMS occurrences   base: 0    merged head: 1

**The reference as it stands at the merged head**, `GATES.md` lines
982–990, quoted from the committed blob:

      982  ### Scope
      983  Stationary solutions `δΓ/δΦ_i = 0` of the full effective action, with all
      984  condensates drawn from the frozen channels, at finite density / `μ`, within
      985  the pre-registered microscopic parameter domain (policy §2, §4).
      986
      987  `derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a stationary
      988  branch that is neither admitted nor excluded; whether it falls within the
      989  existential quantifier of this gate's scientific question is therefore
      990  undetermined.

(Extracted by locating `P2-PHASE-01`'s section first and then its `### Scope`
within it. `### Scope` occurs 14 times in the file — once per gate — so
the section name alone is not an anchor. My first attempt used a
file-wide range match and returned three different gates' Scope sections;
it was discarded and re-done as above.)

---

## 7. A4 — scope, and A8 — protected paths

**A8, compared path by path**, as individual blob object IDs from
`git ls-tree -r`, so that a `reviews/` addition cannot mask a `reviews/`
modification:

    protected paths present at base:      192
    protected paths differing at head:      0

    CONVENTIONS.md                     base 0db56c39d44e  head 0db56c39d44e  identical
    AGENTS.md                          base 5e60b5fcd6e9  head 5e60b5fcd6e9  identical
    DECISION_LOG.md                    base 04539f26a6bc  head 04539f26a6bc  identical
    pyproject.toml                     base 9fc6fdd196dd  head 9fc6fdd196dd  identical
    derivations/P2-DEFERRED-ITEMS.md   base 33b3a664e057  head 33b3a664e057  identical

    per-prefix counts of base-present paths, all blob-identical:
      scripts/        56
      results/        66
      tests/          16
      derivations/    30
      docs/            7
      reviews/        13

    tests/ specifically: 16 paths, all blob-identical: True

The two paths A8 singles out are both confirmed unchanged. The pointer is
one-directional — `DEFERRED-02` was read and quoted, never edited — and
`tests/` is untouched, so §0(b)'s enforcement gap is left exactly as
found.

Base-absent paths present at the merged head:

    reports/2026-08-09T2153Z_si1-deferred-02-crossref.md              (arriving)
    reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md      (arriving)
    specs/2026-08-09T2153Z_si1-deferred-02-crossref.md                (arriving)
    reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md        (authored here)
    specs/2026-08-10T0113Z_integrate-si1-crossref.md                  (authored here)

Base-present paths absent at the merged head: none. `reviews/` gains the
two base-absent authorised paths A8 anticipates, one from each side.

**A7 — arriving artifacts intact**, compared as git blob ids with
`git rev-parse <rev>:<path>`, not as content digests:

    reports/2026-08-09T2153Z_si1-deferred-02-crossref.md
      merged head  cad180e4bca3334d15bc4efb0aaaaf0556a821b0
      source       cad180e4bca3334d15bc4efb0aaaaf0556a821b0
      A7 expects   cad180e4bca3334d15bc4efb0aaaaf0556a821b0   MATCH

    reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
      merged head  ed5eb0dbaf830c68082d35be98e6789a4050482a
      source       ed5eb0dbaf830c68082d35be98e6789a4050482a
      A7 expects   ed5eb0dbaf830c68082d35be98e6789a4050482a   MATCH

    specs/2026-08-09T2153Z_si1-deferred-02-crossref.md
      merged head  2524c366a5f56f38d883bd3ec97e1ae39fc72833
      source       2524c366a5f56f38d883bd3ec97e1ae39fc72833
      A7 expects   2524c366a5f56f38d883bd3ec97e1ae39fc72833   MATCH

Everything arriving by merge is integrated exactly as reviewed; none of it
was edited.

**A4 — intended final manifest**, with this report as the sixth addition:

    {
      "mode": "exact",
      "base": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
      "head": "<the final report-commit head>",
      "required": [
        {"operation": "add",    "path": "reports/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "reports/2026-08-10T0113Z_integrate-si1-crossref.md"},
        {"operation": "add",    "path": "reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md"},
        {"operation": "add",    "path": "specs/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "specs/2026-08-10T0113Z_integrate-si1-crossref.md"},
        {"operation": "modify", "path": "GATES.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Six additions and one modification: three arriving from the branch, three
authored here. The final scope check is post-report evidence per §4.

---

## 8. A11 — branches preserved

    fix/si1-deferred-02-crossref     remote  3830214126387663365aa7671d25d01d57e25d10
                                     local   3830214126387663365aa7671d25d01d57e25d10
    review/role-model-and-executors  remote  10c260b96882ac12610f78840aeeabd07be2d7cb
                                     local   10c260b96882ac12610f78840aeeabd07be2d7cb

    total remote branches: 41   (40 before this task, plus fix/integrate-si1-crossref)

The source branch still resolves to its recorded commit, the protected
review branch is untouched at `10c260b9…`, and this task deleted no
branch.

**Worktree states, stated separately** as the report contract requires:

    merge worktree   <scratch>/integ11
                     branch  fix/integrate-si1-crossref
                     head    65ace0389df7bad4cf8cd73a21e30d8b842ecdfe
                     dirty   0 entries

    main worktree    /home/user/2-emergent-gravity
                     branch  gate/p2-grassmann-crossing-sign
                     head    cf4c78959c0caf6bfed7c80f9451b6a3337972fe
                     dirty   0 entries

The main worktree is on an unrelated historical branch and was not moved,
checked out, or written to by this task.

---

## 9. A9-pre — validators, and what they actually assert

Run individually with `python -m pytest <path>` at the pre-report head
`65ace038…`:

    tests/test_repository_structure.py    4 passed in 0.02s                     EXIT=0
    tests/test_si1_governance.py         14 passed in 0.04s                     EXIT=0
    tests/test_gate_anchors.py           18 passed, 2 deselected in 8.47s       EXIT=0
    tests/test_governance_tools.py        8 passed in 1.30s                     EXIT=0

All four exit 0.

### They do not cover the cross-reference

**Stated plainly, as A9 requires: none of these four validators covers the
cross-referenced section, and their passing is not evidence that the
reference is correct or protected.** What they assert:

    tests/test_gate_anchors.py            (20 tests)
      Reads no repository file. Zero occurrences of the string "GATES".
      Numerical regression and mutation tests over heat-kernel coefficients,
      gap-equation criticality, the lattice β_B mass scan, the β_V ratio and
      the assembly bookkeeping. Despite its name it constrains derivation
      code and results, not the gate ledger.

    tests/test_si1_governance.py          (14 tests, 7 of which read GATES.md)
      Substring-presence checks only, over the P2-BETAV-* family and
      P2-CHANNEL-FREEZE-01:
        _gate_status(gate_id) — first "Status:" line after "## <gate_id> ",
          called for P2-BETAV-CIRC-01, P2-BETAV-RECON-01,
          P2-BETAV-NUMREPRO-01, P2-BETAV-ASSEMBLY-01.  Never for P2-PHASE-01.
        presence of "recovered", "DECOMP-UNAVAILABLE-AS-RECOVERED",
          "Previous additive k-scan design: WITHDRAWN",
          "alone does not verify or promote",
          "does not by itself promote `P2-C9`",
          "P2-BETAV-CIRC-01 = PASS", "P2-BETAV-NUMREPRO-01 = PASS",
          "A PASS does **not** verify or promote",
          the pinned Paper-3 commit 8c363ef0…,
          "no longer requires" together with "P2-BETAV-CIRC-01".
      No assertion mentions P2-PHASE-01. No assertion in tests/ mentions
      DEFERRED at all.

    tests/test_repository_structure.py    (4 tests)
      Existence of required top-level files, directories and nested paths;
      and test_every_cited_gate_id_has_a_gates_heading, which reads
      "## <ID>" headings from GATES.md and requires every gate ID cited in
      CLAIMS.md's table to have one. P2-PHASE-01 appears 0 times in
      CLAIMS.md, so this test does not reach it even at heading level.

    tests/test_governance_tools.py        (8 tests)
      Self-tests of the four governance tools against synthetic tmp_path
      repositories: the operation taxonomy, content-checker match modes,
      merge-guard parentage and scope rejection, the consistency checker,
      and a self-application pass. Reads no repository content file.

### Mutation evidence, extended beyond §0(b)

§0(b) records that deleting `P2-PHASE-01`'s entry left the two named
validators green. I re-ran that at the merged head against **all four**,
and added a second, sharper mutation.

    MUTATION 1 — delete P2-PHASE-01's entire entry (103 lines)
      tests/test_repository_structure.py    4 passed    EXIT=0
      tests/test_si1_governance.py         14 passed    EXIT=0
      tests/test_gate_anchors.py           18 passed    EXIT=0
      tests/test_governance_tools.py        8 passed    EXIT=0

    MUTATION 2 — delete only the added reference paragraph
      P2-DEFERRED-ITEMS occurrences returns to 0
      tests/test_repository_structure.py    4 passed    EXIT=0
      tests/test_si1_governance.py         14 passed    EXIT=0
      tests/test_gate_anchors.py           18 passed    EXIT=0
      tests/test_governance_tools.py        8 passed    EXIT=0

    Working tree restored and verified: git status clean,
    HEAD:GATES.md = 849a4fbfe62d6478f092a84b0175357a74bbbb06

Mutation 2 is the one that matters for this integration: **the exact
change being integrated can be reverted and the entire validator set stays
green.** The only mechanical protection this change has ever had is the
section-by-section comparison in §6, which is a report artifact and will
not run again.

---

## 10. §3 — Rule 16 assessment

Rule 16 is operative. Assembled set: `GATES.md` with the reference,
`derivations/P2-DEFERRED-ITEMS.md` with `DEFERRED-02`, the exploratory
scalar study the branch comes from, and four passing validators.

**§3's candidate is confirmed.** `GATES.md` points at `DEFERRED-02`,
`DEFERRED-02` names SI-1's quantifier range, and four validators pass. A
reader could conclude the quantifier question is tracked and the reference
protected. **Neither holds.** Nobody is assigned to the question;
answering it requires a PI decision on whether the negative-mass branch is
an admissible phase. And §9's mutation 2 establishes by execution that no
validator protects the reference.

**Two sharpenings, offered as additions rather than replacements.**

*The passing validators are now co-located with the change in a way they
were not before.* Before this merge, the four suites and the
cross-reference lived on different refs. After it, one commit contains
both, and this report — which reproduces four green results a few sections
above the reference itself — is the strongest single source of the false
inference §3 names. That is a property of putting evidence next to a
claim it does not support, and the only defence is that §9 says so
explicitly and in the same document.

*A second junction, which §3 does not name.* The set now co-locates the
exploratory scalar study (a stationary branch at `M̂ ≈ −7.59`, `mu = 0`
slice, no admissibility verdict), `DEFERRED-01`'s recorded PI position
that the V/A representation "may contain physically relevant information"
with "no evidence indicates it is unphysical", and a `### Scope` paragraph
that now carries a deferral notice. Read together, the available inference
is that **the gate's scope has been narrowed to what has been examined,
with the remainder parked.** It has not. `### Scope` still says "all
condensates drawn from the frozen channels"; the added paragraph subtracts
nothing from that set. What is parked is one branch's *classification*,
not any part of the gate's *range*.

**Search.** I checked for anything mechanical that resists either
inference: no test mentions `DEFERRED`; no test mentions `P2-PHASE-01` in
any of the four suites; `P2-PHASE-01` is cited 0 times in `CLAIMS.md`, so
even the dangling-gate-ID guard does not reach it; and the added reference
carries no status or ownership field, by design. **There is no artifact in
the repository that would register an objection if the quantifier question
stayed open indefinitely, or if the reference were silently deleted.**

---

## 11. What this integration does not establish

Restating §1's list against what was actually executed, so the record
shows each discharged:

- **SI-1's quantifier range is not resolved.** The reference records that
  the question exists. Nobody is assigned; answering it needs a PI
  decision on the negative-mass branch.
- **The branch is neither admitted nor excluded here**, and the kill
  criterion is not qualified — §6 shows it byte-unchanged.
- **SI-1 is not made unable to proceed.** Nothing in the merged text says
  so. The observation that a future SI-1 specification will need to state
  which reading it uses remains an observation; this integration imposes
  no rule on future tasks, and the Reviewer's non-blocking note that such
  a rule would need a durable home is recorded in §3 and not acted on.
- **No test coverage was added**, for the reference or anything else;
  `tests/` is blob-identical across all 16 paths.
- **No gate status, no science, no result changed.** `P2-PHASE-01` stays
  `PROPOSED`, `P2-GAP-01` stays `PASS`, thirteen gate bodies are
  byte-identical, and 192 protected paths are unchanged.

---

## 12. A10 — commit-message hygiene

Each message was inspected before writing (proposed file) and after
(`git log -1 --format='%B'`, read from the object). Scan pattern, case
insensitive: `co-authored-by|claude|session|https?://|generated with|
anthropic`.

    commit 1  abef7d2bff281662051c5f6f1d00153d672457b5
      "spec: integrate the SI-1 / DEFERRED-02 cross-reference"
      proposed: no match    stored: no match
      trailers suppressed: yes — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither appears in the object.

    commit 2  025c88b1073f177f8435da0fe3e515962364989a
      "review: commit the pre-execution review for the SI-1 cross-reference
       integration"
      proposed: no match    stored: no match
      trailers suppressed: yes — same two.

    commit 3  65ace0389df7bad4cf8cd73a21e30d8b842ecdfe   (the merge)
      "merge: integrate the SI-1 / DEFERRED-02 cross-reference
       (reviewed; pinned 3830214)"
      proposed: no match    stored: no match
      trailers suppressed: yes — same two.

The merge commit's stored message, in full, since A10 names the merge
explicitly:

    merge: integrate the SI-1 / DEFERRED-02 cross-reference (reviewed; pinned 3830214)

    Brings one reference into P2-PHASE-01's ### Scope in GATES.md:
    derivations/P2-DEFERRED-ITEMS.md records, as DEFERRED-02, a stationary
    branch that is neither admitted nor excluded, so whether it falls within
    the existential quantifier of this gate's scientific question is
    undetermined. P2-DEFERRED-ITEMS occurrences in GATES.md: 0 -> 1.

    Fourteen P2- gate sections before and after; P2-PHASE-01 is the only
    section whose body differs; the other thirteen are byte-identical.
    P2-PHASE-01 remains PROPOSED, P2-GAP-01 remains PASS, and
    derivations/P2-DEFERRED-ITEMS.md is unchanged -- the pointer is
    one-directional.

    This resolves nothing. SI-1's quantifier range stays open, nobody is
    assigned to it, and answering it needs a PI decision on whether the
    negative-mass branch is an admissible phase. No test protects the
    cross-referenced section: deleting P2-PHASE-01's entire entry leaves the
    four validators green. Neither gap is closed here.

    Merged --no-ff from the pinned remote ref after the pre-execution review
    was committed, per Rule 15.

**A note on the raw object.** `git cat-file commit` shows
`author`/`committer Claude <noreply@anthropic.com>`. That is repository
identity configuration, not a message trailer, and it is identical on the
five preceding `main` commits; A10 constrains the message, and the message
scans are clean.

The report commit's message is below; its authoring-time suppression is
post-report evidence per §4.

---

## 13. Intended final state

**Pre-report head:** `65ace0389df7bad4cf8cd73a21e30d8b842ecdfe`

**Intended report commit message:**

    docs: report the integration of the SI-1 DEFERRED-02 cross-reference

    Records A1-A3, A5-A8, A9-pre, A10 and A11 for the one merge of
    fix/si1-deferred-02-crossref @ 38302141 onto 898aecd1. Fourteen P2-
    gate sections before and after, P2-PHASE-01 the only differing body,
    the other thirteen byte-identical, GATES.md blob-identical to its
    source-branch value, 192 protected paths unchanged.

    Three findings. PRE_MERGE failed once on my construction error --
    it evaluates pinned_artifacts at the reviewed branch head, not at the
    base -- and the corrected pin is reported alongside the failure. The
    stated delimiter literals removed the boundary judgement; one residual
    normalisation remained, a single leading blank line, quantified to the
    byte. Mutation evidence is extended past what the specification
    carried forward: deleting only the added reference, not just the whole
    gate entry, leaves all four validators green.

    Nothing is resolved. SI-1's quantifier range stays open with nobody
    assigned, and no test protects the cross-reference.

**Blob digests at the pre-report head:**

    GATES.md
      blob 849a4fbfe62d6478f092a84b0175357a74bbbb06
      sha256 8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526
    specs/2026-08-10T0113Z_integrate-si1-crossref.md
      sha256 d0c0ec7be6de8ae45464139582990435d02587c7fe201ca35cee0a1acf503434
    reviews/chatgpt/2026-08-10T0113Z_integrate-si1-crossref.md
      blob b2b5d639cbaa4b46e0c7c4510528c0c8b9da25ba
      sha256 ba9aed51c343c31e1af9e2f7a54b1f948511eb9a185e8fe3389fd12dffa865cd

---

## 14. Environment

    Python              3.11.15
    python -m pytest    9.1.1      (the version the specifications mandate)
    pytest on PATH      9.0.2      (not used)
    ruff                0.15.8

Nothing was installed. All validators were run as `python -m pytest`.

`CONVENTIONS.md` Rule 13 carries two diagnostic orders, a known open item.
**No environment failure occurred, so neither order was exercised.** The
`PRE_MERGE` failure in §4 was a configuration error of mine, not an
environment failure, and did not engage Rule 13.

---

## 15. Stops and clarifications

No stop occurred. All findings below are secondary.

**`OBSERVATION_METHOD_ERROR` — two, both mine, both caught before they
could mislead.**

*The `PRE_MERGE` `GATES.md` pin was set to the wrong revision's value*
(§4). I pinned the file to its base value on a criterion the tool
evaluates at the reviewed branch head. The guard reported the mismatch
correctly and I read the tool source before changing anything. The
corrected pin asserts what the criterion is for — that the branch delivers
the reviewed `GATES.md` — and is the same object A6 requires. Recorded
because a pin that cannot fail asserts nothing, and one aimed at the wrong
revision fails for the wrong reason; had I "fixed" it by deleting the pin,
the guard would have passed while checking less.

*My first extraction of the reference for §6 used a file-wide range match
on `### Scope`* and returned three different gates' Scope sections,
because `### Scope` occurs 14 times. Discarded and re-done by locating
`P2-PHASE-01`'s section first. This is the same shape as the delimiter
failures §0(a) catalogues — a marker that is not unique being treated as
though it were — and it is worth noting that the shape recurs in reporting
code as well as in supply protocols.

**`SPECIFICATION_DEFECT` — one, residual and small.**

*A5's phrase "the text between the delimiter literals" is ambiguous by the
newlines adjacent to line-oriented delimiters* (§3). The specification
fixed the boundary problem §0(a) describes; what remains is a
one-byte normalisation the executor still decides. A single clause
specifying leading/trailing blank-line handling and the trailing newline
would close it. I record this as a defect rather than a clarification
because A5 says "byte-identical", and byte-identity to an ambiguous
referent is not decidable.

**`REPOSITORY_DEFECT` — one, unchanged and now better evidenced.**

*Nothing in `tests/` protects the cross-reference or the gate section it
sits in* (§9). Deleting only the added paragraph leaves all four
validators green and returns the `P2-DEFERRED-ITEMS` count to 0. Deleting
the entire 103-line gate entry also leaves all four green. `P2-PHASE-01`
is cited 0 times in `CLAIMS.md`, so even the dangling-gate-ID guard does
not reach it. This is §0(b)'s finding, extended from two validators to
four and from whole-entry deletion to reference-only deletion. **This
integration does not close it**, per §5, and the separate task §0(b) calls
for should decide which governance-critical cross-references need
persistent coverage — together with the wider gap that no test checks any
of the seventeen `CONVENTIONS.md` rules while every recent specification
protects `tests/`.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one, carried forward.**

*`P2-PHASE-01`'s entry now describes its quantifier two ways* —
"existential quantifier" in `### Scope`, "universal quantifier" in
`### Quantifier note`. These are duals and both correct about their own
statements, but nothing in the entry says so, and only one of them is
cross-referenced. Recorded in the source task's report and unchanged here;
this integration is not authorised to edit gate text.

**`ENVIRONMENT` — none.** No environment failure occurred; neither of Rule
13's two diagnostic orders was exercised (§14).

**Things I would have specified differently.**

*The specification could pin `GATES.md` for `PRE_MERGE` explicitly, with
its revision named.* A6 states the source-branch blob id and §7 states
base digests; a guard config author has to know which of those
`PRE_MERGE` wants. Naming the revision beside the digest — "at the
reviewed branch head" — would have prevented §4 outright. This generalises:
a pinned digest without a named revision is under-specified whenever the
file legitimately differs between the two.

*A9's instruction "say what they actually assert" is the right shape and
should be the default for validator criteria.* It is the clause that
turned four green lines into §9, and it is what stops a report from
offering passing tests as coverage. Contrast the predecessor task's A8,
which asserted that two validators "constrain this file" — one does not.
Naming the expected property rather than asserting it makes the absence
detectable.

*§0(a) is right that the pattern is a supply protocol that was never
written down.* This specification wrote most of it down and the
improvement is measurable — the boundary decision went from "infer the
whole extent" to "one leading newline". The remaining sentence is small
enough to add to `CONVENTIONS.md` rather than to each specification, which
would also end the per-task rediscovery §0(a) describes.
