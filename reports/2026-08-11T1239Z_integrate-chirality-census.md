# Report — integrate the chirality census

Specification: `specs/2026-08-11T1239Z_integrate-chirality-census.md`
Specification sha256:
`7ad4f065e89555526fec02610b437ce1f5918c52adc55d3edf6f974cd13730b7`
Pre-execution review: `reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md`
Evidence base: `8701a97a6bb58550d4300f75c10638b057335731`
Source branch: `gate/p2-chirality-census` @
`e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb`
Branch: `gate/p2-integrate-chirality-census`
Classification: MATERIAL.

---

## 0. Summary

One merge, no conflict, 7 additions and 0 modifications arriving exactly
as the dry run predicted. All seven arriving blobs are identical to A6's
pinned ids and to the source branch. 195 pre-existing protected paths
unchanged. `GATES.md` blob-identical, fourteen `## P2-` sections,
`P2-PHASE-01` still `PROPOSED`, `P2-GAP-01` still `PASS`. Neither
unintegrated diquark branch is an ancestor of the merged head.

**Two things worth the reader's attention before the criteria:**

- **The review supply protocol worked** (§3). After six consecutive
  failures, both delimiters matched as whole lines on the first attempt —
  and the first-occurrence search the specification forbids **would have
  failed here**, because the instruction sentence names both literals.
  This is the first instance in the sequence where the mandated rule was
  both necessary and sufficient.
- **The merge puts a particle–particle coefficient row on `main` for the
  first time** (§8). It arrives inside the source specification's own §0,
  as context, with that same specification's next paragraph declaring it
  non-authoritative. Measured: 0 such rows on `main` before, 1 after.
  This is the Reviewer's non-blocking point made concrete, and it is the
  sharpest available answer to §8's question about how the merged state
  reads.

No STOP condition fired.

---

## 1. A1 — refs

    remote refs/heads/main                     8701a97a6bb58550d4300f75c10638b057335731
    refs/remotes/origin/main                   8701a97a6bb58550d4300f75c10638b057335731
    remote gate/p2-chirality-census            e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb
    local main (stale by design)               0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both `main` refs resolve to the evidence base and the source branch to
`e4bea1c9…`; no mismatch, so no STOP. Local `main` is stale by design and
was neither consulted nor repaired.

---

## 2. Commits 1–3, and A2 — merge parentage

    commit 1  0534be2ceddbcbd63f7754d44b935ebc5384108e
              specs/2026-08-11T1239Z_integrate-chirality-census.md
              "spec: integrate the chirality census"

    commit 2  8ab819ea43c7139a4db13ff3c1e0ea2d92d26853
              reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md
              "review: commit the pre-execution review for the chirality
               census integration"

    commit 3  3d3493aa094da34a5a248143ee52faca9268c05a
              --no-ff merge of the pinned remote ref
              "merge: integrate the chirality census (reviewed; pinned e4bea1c)"

**A2, as distinct values:**

    merge commit        3d3493aa094da34a5a248143ee52faca9268c05a
    parent 1            8ab819ea43c7139a4db13ff3c1e0ea2d92d26853   = commit 2, the review
    parent 2            e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb   = the source branch
    merge-base(p1,p2)   8701a97a6bb58550d4300f75c10638b057335731   = the evidence base

    commit 1 (0534be2c) is an ancestor of parent 1:  yes

Parent 1 is the review commit because §4's order puts the review before
the merge and parent 1 is fixed by which commit one stands on.

**Dry run, before the merge:**

    predicted tree   8fef7b3620194b6845e8413464495a6b034b1919
    conflict output  (none)

    base..source name-status
      A  derivations/P2-PHASE-01_chirality_census.md
      A  reports/2026-08-11T1134Z_chirality-census.md
      A  results/P2-PHASE-01/chirality-census/census.json
      A  reviews/chatgpt/2026-08-11T1134Z_chirality-census.md
      A  scripts/p2_chirality_census.py
      A  specs/2026-08-11T1134Z_chirality-census.md
      A  tests/test_p2_chirality_census.py

    additions 7   modifications 0

Exactly what the specification's header predicted, and the merge-base is
the original base.

---

## 3. A5 — the review, and the protocol working

Committed at
`reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md` in
commit 2, before the merge.

    committed blob sha256  9d3c1d63c6c2b919866c796f2663fad1aa6d378b70a8723fe8b88f0ac444e81b
    size                   5712 bytes, 5641 characters, 68 lines
    identical to the extracted text:  True

**The whole-line rule succeeded on the first attempt.**

    substring occurrences   BEGINS: 2    ENDS: 2
    WHOLE-LINE matches      BEGINS: [line 3]    ENDS: [line 74]

**Both counts matter.** The delimiters occupy their own lines, so the
mandated procedure worked with no derived rule and no executor judgement
about where the artifact starts. And the substring count of **2** is the
reason the rule exists: the accompanying instruction sentence names both
literals, so a first-occurrence search would have located the delimiter
inside the instruction and produced a fragment. **The rule the
specification mandates was both necessary and sufficient here** — the
first time in this sequence that is true.

The three preamble lines before BEGIN (the attachment marker plus the
instruction, then two blank lines) were excluded, as A5 requires.

**A5's three STOP conditions** — missing, no delimiters, does not
correspond — **none applies.** The text is present, both delimiters are
whole lines, and it corresponds: it names this task by title, both SHAs,
`A6`, and the bar-flip correction.

**One residual normalisation, unchanged and still one byte.** The literal
slice between the delimiter lines is 5713 bytes with one leading and one
trailing newline; the committed artifact drops the leading blank line and
keeps a single trailing newline, matching every prior artifact in
`reviews/chatgpt/`.

**What this means for the standing recommendation.** The previous three
reports proposed a `CONVENTIONS.md` paragraph covering the shared-line
case. This task's supply did not need it. **That is not evidence the
recommendation is unnecessary** — it is evidence that the outcome depends
on how the message happens to be composed, which is precisely the
argument for writing the rule down once rather than rediscovering it. The
one-byte normalisation clause is still unwritten and was still applied by
me.

**The review's non-blocking finding is addressed in §8**, which is where
the evidence for it is.

---

## 4. A3 — the `PRE_MERGE` guard

    $ python -m scripts.governance_tools.merge_guard --repo . --config i12_pre_cfg.json
    EXIT=0
    {
      "checks": [
        { "condition": "worktree_clean", "entries": [], "status": "PASS" },
        { "attachment": "gate/p2-integrate-chirality-census",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "8ab819ea43c7139a4db13ff3c1e0ea2d92d26853",
          "status": "PASS",
          "worktree_head": "8ab819ea43c7139a4db13ff3c1e0ea2d92d26853" },
        { "actual": "8701a97a6bb58550d4300f75c10638b057335731",
          "condition": "merge_base",
          "expected": "8701a97a6bb58550d4300f75c10638b057335731",
          "status": "PASS" },
        { "condition": "scope",
          "evidence": {
            "base": "8701a97a6bb58550d4300f75c10638b057335731",
            "failures": [],
            "head": "8ab819ea43c7139a4db13ff3c1e0ea2d92d26853",
            "mode": "exact",
            "observed_operations": [
              { "operation": "add",
                "path": "reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md" },
              { "operation": "add",
                "path": "specs/2026-08-11T1239Z_integrate-chirality-census.md" }
            ],
            "overall": "PASS",
            "tool": "scope_checker" },
          "status": "PASS" },
        { "condition": "pinned_artifacts",
          "evidence": [
            { "actual": "8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526",
              "expected": "8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526",
              "path": "GATES.md", "status": "PASS" },
            { "actual": "e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451",
              "expected": "e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451",
              "path": "CONVENTIONS.md", "status": "PASS" },
            { "actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
              "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
              "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS" }
          ],
          "status": "PASS" }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }

(`other_registered_worktrees` omitted from the quotation only; no check
depends on it.)

**The pins are set to the values these files hold at the reviewed branch
head**, because `PRE_MERGE` evaluates `pinned_artifacts` there. All three
are files the source branch does not touch, so pinning them asserts the
branch leaves them alone — which is the assertion worth making, and the
reason a previous integration's guard failed when the pin was aimed at
the base instead.

**`POST_MERGE`, intended parameters.** A3 requires the final guard to
carry **two distinct SHAs in two distinct roles**. The tool supports it:
`merge_commit` names the object under verification, `expected_remote_sha`
names the ref-agreement target, and they are separate keys. **Both roles
can be represented separately, so no STOP.**

    mode                    POST_MERGE
    merge_commit            3d3493aa094da34a5a248143ee52faca9268c05a   <- the merge object
    expected_parent_1       8ab819ea43c7139a4db13ff3c1e0ea2d92d26853
    expected_parent_2       e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb
    expected_merge_base     8701a97a6bb58550d4300f75c10638b057335731
    scope_manifest          the final manifest of §7
    pinned_artifacts        GATES.md                                    8ce38b8a…072e526
                            CONVENTIONS.md                              e3afa521…f94a451
                            derivations/P2-CHANNEL-FREEZE-01_phaseA…    fe68b9c6…12a4e67a
    remote_check_policy     REQUIRED
    expected_remote_ref     refs/remotes/origin/main
    expected_remote_sha     <the final report-commit head>              <- ref agreement

The two roles hold different values by construction: the merge object is
`3d3493aa…` and the remote target is the report commit above it.

---

## 5. A6 — arriving artifacts intact

Compared as git blob ids with `git rev-parse <rev>:<path>` — **not**
content SHA-256 digests — at the merged head and at the source, against
A6's pinned values:

    derivations/P2-PHASE-01_chirality_census.md
      A6 / source / merged head   b8a403aecb86e0aca6d029454b63e099d3f98145   MATCH
    reports/2026-08-11T1134Z_chirality-census.md
      A6 / source / merged head   b7c521d3d5d2f0b0b66977435d7956d235098973   MATCH
    results/P2-PHASE-01/chirality-census/census.json
      A6 / source / merged head   31c8d7012938438b13f16b26f98c41be842b5da0   MATCH
    reviews/chatgpt/2026-08-11T1134Z_chirality-census.md
      A6 / source / merged head   9b331993bdcecd69a915da88b191275f507e7f93   MATCH
    scripts/p2_chirality_census.py
      A6 / source / merged head   eb02aebc3a53f905d37f224423a5c07e700aa47b   MATCH
    specs/2026-08-11T1134Z_chirality-census.md
      A6 / source / merged head   b6529e4b86917b0f94db3ed95086e89ccc73ec02   MATCH
    tests/test_p2_chirality_census.py
      A6 / source / merged head   17513abecb0f8f55e5a98ae63c68b8e6680799de   MATCH

**All seven identical on both comparisons.** Everything arriving by merge
is integrated exactly as reviewed; none of it was edited.

---

## 6. A7 — protected paths; A8 — no gate changed; A9 — the diquark branches

**A7**, compared as individual blob object ids from `git ls-tree -r`, path
by path rather than as tree objects:

    pre-existing protected paths checked          195
    differing at the merged head                    0

    GATES.md, CONVENTIONS.md, AGENTS.md,
    DECISION_LOG.md, pyproject.toml               all identical

    per-prefix counts of base-present paths, all blob-identical:
      scripts/ 56   results/ 66   tests/ 16   derivations/ 30
      docs/ 7       reviews/ 15

**`tests/` gains exactly one arriving file and no existing test is
modified** — 16 at base, all identical, 17 at head.

Base-absent paths at the merged head, nine, all authorised:

    derivations/P2-PHASE-01_chirality_census.md                 (arriving)
    reports/2026-08-11T1134Z_chirality-census.md                (arriving)
    results/P2-PHASE-01/chirality-census/census.json            (arriving)
    reviews/chatgpt/2026-08-11T1134Z_chirality-census.md        (arriving)
    scripts/p2_chirality_census.py                              (arriving)
    specs/2026-08-11T1134Z_chirality-census.md                  (arriving)
    tests/test_p2_chirality_census.py                           (arriving)
    reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md  (authored here)
    specs/2026-08-11T1239Z_integrate-chirality-census.md            (authored here)

Base-present paths absent at head: none.

**A8 — no gate changed:**

    GATES.md blob   base 849a4fbfe62d6478f092a84b0175357a74bbbb06
                    head 849a4fbfe62d6478f092a84b0175357a74bbbb06   identical
    ^## P2- count   base 14   head 14
    P2-PHASE-01     PROPOSED
    P2-GAP-01       PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)

**A9 — the unintegrated diquark branches:**

    gate/p2-diquark-both-eta        remote  bc1e5c743aada004c52dc7ab7ce2af61de439955
    gate/p2-diquark-adjudication    remote  3767973bf57c52f4dd2be1fddcf62916ec409c72

    bc1e5c74 is an ancestor of the merged head:   no
    3767973b is an ancestor of the merged head:   no

**Neither is merged by this task**, both remain at their recorded
commits, and neither was read.

---

## 7. A4 — the intended final manifest

    {
      "mode": "exact",
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "head": "<the final report-commit head>",
      "required": [
        {"operation": "add", "path": "derivations/P2-PHASE-01_chirality_census.md"},
        {"operation": "add", "path": "reports/2026-08-11T1134Z_chirality-census.md"},
        {"operation": "add", "path": "reports/2026-08-11T1239Z_integrate-chirality-census.md"},
        {"operation": "add", "path": "results/P2-PHASE-01/chirality-census/census.json"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-11T1134Z_chirality-census.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-11T1239Z_integrate-chirality-census.md"},
        {"operation": "add", "path": "scripts/p2_chirality_census.py"},
        {"operation": "add", "path": "specs/2026-08-11T1134Z_chirality-census.md"},
        {"operation": "add", "path": "specs/2026-08-11T1239Z_integrate-chirality-census.md"},
        {"operation": "add", "path": "tests/test_p2_chirality_census.py"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Ten additions and zero modifications**: seven arriving from the branch,
three authored here. The final scope check is post-report evidence per §4.

---

## 8. How the merged state reads — the report contract's question

§8 asks two things directly: **does the merged state read as though the
census explains coefficient signs, and as though the particle–particle
side were numerically tested?** **Neither is true**, and the answer needs
evidence rather than assertion.

### Measured: what the merge puts on `main`

I searched every file at both revisions for a particle–particle
coefficient row:

    main before the merge (8701a97a)    such rows: 0
    merged head                         such rows: 1

      specs/2026-08-11T1134Z_chirality-census.md:28
      particle-particle      0    0    0    +c      -c

**This merge places a particle–particle coefficient row on `main` for the
first time.** It is the source specification's own §0 context table,
arriving verbatim inside a committed specification, and it is the only
one.

### Its immediate context, quoted from the merged blob

Lines 30–38 of that same file, ten lines below the table:

> **S, P and T vanish in both. That parallel has never been explained**,
> and the programme currently holds it as two separate numerical facts.
>
> **Their status differs, and this task must not blur it.** The
> particle–hole coefficients are on `main` and pinned at A1. **The
> particle–particle coefficients were produced and adjudicated on an
> UNINTEGRATED branch; they are NOT authoritative main-line input to this
> task**, and A1 forbids reading them. **They are context for why the
> question is worth asking, not evidence this task may rest on.**

**So the values arrive with their own disclaimer attached, ten lines
away, in the same file.** That is the strongest form the protection could
take for text that arrives unedited: the specification that quotes the
numbers is the same document that declares them non-authoritative.

### The two questions, answered

**Does the merged state read as though the census explains coefficient
signs?** No. The merged artifacts state the opposite repeatedly and in
their own words: the derivation note's Step E lists the inter-channel
sign and the magnitudes as things the argument does not explain; the
results artifact carries them as structured fields; the branch report
devotes a section to it. The census's output is a statement about which
families can form, and every artifact says so.

**Does it read as though the particle–particle side were numerically
tested?** No, and this is stated more insistently than anything else in
the arriving material. The asymmetry — particle–hole structural *and*
numerical, particle–particle structural *only* — appears in the
derivation note, the results artifact, the script's own docstring, the
branch report and the merge message. The results artifact carries
`no_pp_coefficient_decomposition_performed` and `no_slot_map_chosen` as
fields a test asserts.

**The residual risk, named precisely.** A reader who sees `+c` and `−c`
on `main` for the first time, in a document that also carries a surviving
structural argument about the particle–particle channel, could take the
two together as a settled pp result. **They are not.** The values are
context inside a specification, not a result; the structural argument
covers *support only*; and the coefficients that would settle anything
are on two unintegrated branches under three unfrozen conventions. **This
report does not restate those values as established**, and §9 records the
junction.

---

## 9. §6 — Rule 16 assessment

Rule 16 is operative. **§6's candidate is confirmed, and I would sharpen
it with the measurement above.**

After this merge `main` carries a chirality selection rule, a
particle–hole coefficient table, and a structural particle–particle
classification. **A reader could conclude the diquark channel's character
is determined. It is not** — §2's Layer 3 lists what the census does not
explain, and the coefficients that would settle it are on two
unintegrated branches under `η`, the particle–particle Grassmann ordering
and the diquark normalisation.

**The sharpening.** §6 describes the junction as three main-line
artifacts read together. The measurement in §8 makes it concrete and
narrower: **the specific new thing this merge contributes to that
inference is a pp coefficient row appearing on `main` for the first
time**, `0 → 1`. Before the merge a reader could not have formed a view
about pp coefficient *values* from `main` at all, because no value was
there. After it, one is — quoted, disclaimed, and inside a specification
rather than a result artifact, but present.

The previous task's report predicted this junction in the abstract, and
its Rule 16 search noted that "**there is no artifact on `main` that
states the pp coefficients are unintegrated**, because there is no
artifact on `main` that mentions them at all." **That has now changed on
both counts simultaneously**, which is the least bad way for it to change:
the first mention and the first disclaimer arrive in the same paragraph
of the same file.

**Search.** I checked what would resist the inference: `GATES.md` is
byte-identical and records `P2-PHASE-01` as `PROPOSED` with no pp result;
no test in `tests/` mentions either diquark branch; neither branch is an
ancestor of the merged head; and the merged artifacts' own text states the
asymmetry in five places. **What does not exist is any main-line artifact
that names the two branches and their status** — the disclaimer is prose
inside a specification, not a register entry, and nothing mechanical
enforces it. That is the same shape as the `DEFERRED-02` discoverability
problem the SI-1 cross-reference task addressed, and it may deserve the
same remedy; **deciding that is a PI matter and is not this task's.**

---

## 10. A10-pre — validators

Run individually with `python -m pytest <path>` at the pre-report head
`3d3493aa…`:

    tests/test_repository_structure.py         4 passed in 0.02s                EXIT=0
    tests/test_si1_governance.py              14 passed in 0.04s                EXIT=0
    tests/test_gate_anchors.py                18 passed, 2 deselected in 8.84s  EXIT=0
    tests/test_governance_tools.py             8 passed in 1.52s                EXIT=0
    tests/test_p2_channel_character.py        23 passed in 1.12s                EXIT=0
    tests/test_p2_chirality_census.py         21 passed in 0.58s                EXIT=0

All six exit 0. The arriving test file passes against the merged tree,
which is the check that matters: it was written on the branch and had not
previously run in the presence of `main`'s other content.

**Environment.**

    Python 3.11.15   |   python -m pytest 9.1.1 (mandated)   |   ruff 0.15.8

Nothing was installed. No environment failure occurred, so **neither of
Rule 13's two diagnostic orders was exercised.**

---

## 11. A12 — branches preserved; worktree states

    gate/p2-chirality-census        remote  e4bea1c9a6b685da6139f5a7fa37d5667df7e1eb
    gate/p2-diquark-both-eta        remote  bc1e5c743aada004c52dc7ab7ce2af61de439955
    gate/p2-diquark-adjudication    remote  3767973bf57c52f4dd2be1fddcf62916ec409c72
    review/role-model-and-executors remote  10c260b96882ac12610f78840aeeabd07be2d7cb

The source branch is at its recorded commit, the protected review branch
is untouched, and **this task deleted no branch.**

**Worktree states, stated separately:**

    merge worktree   <scratch>/integ12
                     branch  gate/p2-integrate-chirality-census
                     head    3d3493aa094da34a5a248143ee52faca9268c05a
                     dirty   0 entries

    main worktree    /home/user/2-emergent-gravity
                     branch  gate/p2-grassmann-crossing-sign
                     head    cf4c78959c0caf6bfed7c80f9451b6a3337972fe
                     dirty   0 entries

The main worktree is on an unrelated historical branch and was not moved,
checked out, or written to by this task.

---

## 12. A11 — commit-message hygiene, and intended final state

Each message inspected before writing (proposed file) and after
(`git log -1 --format='%B'`, read from the object). Scan pattern, case
insensitive: `co-authored-by|claude|session|https?://|generated with|
anthropic`.

    commit 1  0534be2ceddbcbd63f7754d44b935ebc5384108e
      "spec: integrate the chirality census"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  8ab819ea43c7139a4db13ff3c1e0ea2d92d26853
      "review: commit the pre-execution review for the chirality census
       integration"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 3  3d3493aa094da34a5a248143ee52faca9268c05a   (the merge)
      "merge: integrate the chirality census (reviewed; pinned e4bea1c)"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

**Pre-report head:** `3d3493aa094da34a5a248143ee52faca9268c05a`

**Intended report commit message:**

    docs: report the integration of the chirality census

    Records A1, A2, A5-A9, A10-pre and A11. One merge, no conflict, 7
    additions and 0 modifications arriving exactly as the dry run
    predicted. All seven arriving blobs identical to A6's pinned ids and
    to the source; 195 pre-existing protected paths unchanged; GATES.md
    blob-identical with fourteen P2- sections, P2-PHASE-01 PROPOSED and
    P2-GAP-01 PASS. Neither diquark branch is an ancestor of the merged
    head.

    Two findings. The review supply protocol worked for the first time in
    seven attempts: both delimiters matched as whole lines, and the
    first-occurrence search the specification forbids would have failed
    here because the instruction sentence names both literals. And the
    merge puts a particle-particle coefficient row on main for the first
    time -- measured 0 before, 1 after -- inside the source
    specification's own context table, ten lines above that same
    specification's statement that the values are not authoritative
    main-line input.

    The merged state does not read as though the census explains
    coefficient signs, or as though the particle-particle side were
    numerically tested; the report gives the evidence for both. Nothing
    frozen, no gate status changed, no new programme coefficient.

---

## 13. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — none this task.**

The delimiter defect that has run through the previous six tasks **did not
recur**, because the supply put both delimiters on their own lines (§3).
The standing recommendation is unchanged and still unwritten: the outcome
turned on how the message happened to be composed, not on anything the
specification did differently, and **the one-byte leading-blank-line
normalisation is still an executor decision with no rule behind it.**

**`OBSERVATION_METHOD_ERROR` — none.**

One secondary observation about method, to the specification's credit:
**A6 pinning git blob ids rather than content digests, and saying so
explicitly**, made the arriving-artifact check a two-sided comparison —
source and merged head against the same pinned value — with no conversion
step where an error could hide. Content digests would have required
recomputing both sides.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

One secondary observation, and it is the substantive one: **no main-line
artifact names the two unintegrated diquark branches or their status.**
The disclaimer that protects the pp coefficient row now on `main` is prose
inside a specification (§8), not a register entry, and nothing mechanical
enforces it — no test mentions either branch, and `GATES.md` does not.
This is structurally the same problem the SI-1 cross-reference task
addressed for `DEFERRED-02`, where a constraint existed, was recorded, and
was unreachable from the document a reader would start from. **It is not
repaired here** — this integration may write only three paths and may not
touch `GATES.md` or add a register — and whether it deserves the same
remedy is a PI decision.

Also unchanged: `CONVENTIONS.md`'s seventeen rules still have no
structural validator.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one, carried forward
deliberately.**

**The `P`-sign difference recorded in §3 of the specification remains
unresolved**, and this task did not resolve it, per §7. Both computations
agree on the proposition the third test case turns on — all five families
non-zero — so the difference does not bear on that verdict. It is recorded
as unresolved, not as agreement, and resolving it is a separate task if it
is ever worth one.

**`ENVIRONMENT` — none.** No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised. Nothing was installed.

**Things I would have specified differently.**

*§8's report contract asks the right question and should ask for the
measurement.* "Whether the merged state reads as though the census
explains coefficient signs" is exactly the question worth asking, and the
honest way to answer it is to count what the merge actually puts on
`main` rather than to characterise the prose. The `0 → 1` measurement in
§8 is what turned the Reviewer's non-blocking wording point into
something checkable, and an acceptance criterion could have required it
directly.

*A7's protected-path list should say how many paths it expects.* It names
five files and six directory prefixes; the executor discovers the count
(195) by running the check. A stated expectation would make a silently
shrinking protected set detectable — the same argument A6 already applies
to the arriving artifacts by pinning their ids.

*The specification's §1 is the best part of it, and the pattern is worth
generalising.* It records two claims the previous specification made and
got wrong, attributes the corrections to the branch, and requires them to
survive integration. Most integration specifications carry forward what a
branch *produced*; this one carries forward what the branch *corrected in
its own instructions*, which is the harder thing to preserve and the
easier thing to lose.
