# Integration report — the attraction/repulsion ruling and the Layer 1b / Layer 2 recomputation

Specification: `specs/2026-08-09T0346Z_integrate-attraction-and-layers.md`
Specification evidence base: `3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`
Source branch: `gate/p2-attraction-ruling-and-layers` @ `878b632ced8caa5ef2c6255022a44291d50ccfe2`
Integration branch: `gate/p2-integrate-attraction-and-layers`
Pre-report head: `10f14f01cc2bf8bb18308cd1b12bace28e471d73` (the merge commit)

**Outcome.** One `--no-ff` merge, no conflict, correct parentage,
merge-base the original base. Every arriving blob is byte-identical to
its reviewed value. `DECISION_LOG.md` arrives intact and append-only,
and all three 2026-08-08 entries are present and top-level. All thirteen
protected paths are blob-identical between base and merged head. Nine
validators pass.

**The finding the Reviewer should read is §9**, which answers the
specification's question about whether the merged state now reads as
though the composite-vector question were settled. **No single artifact
overstates anything. One junction does not carry its own disclaimer**,
and the chain a reader could assemble across it is named precisely
there. It is reported, not fixed — fixing it would mean editing content
this task may not touch.

---

## 1. A1 — refs, read from the remote

    refs/remotes/origin/main                            3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    remote refs/heads/main                              3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    local  refs/heads/main                              0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote refs/heads/gate/p2-attraction-ruling-and-layers
                                                        878b632ced8caa5ef2c6255022a44291d50ccfe2
    local  refs/heads/gate/p2-attraction-ruling-and-layers
                                                        878b632ced8caa5ef2c6255022a44291d50ccfe2

Both remote `main` refs resolve to the specification's base and the
source branch to `878b632c…`. **Local `main` is stale by design and was
not repaired.** No `main` ref was moved.

**The merge took the pinned remote ref**, not a local copy:
`refs/remotes/origin/gate/p2-attraction-ruling-and-layers` was fetched
immediately before the merge and confirmed to resolve to
`878b632ced8caa5ef2c6255022a44291d50ccfe2`.

**`{HHMM}Z` was fixed once as `0346`** by commit 1 and reused for the
report path.

## 2. A2 — merge parentage

    merge commit   10f14f01cc2bf8bb18308cd1b12bace28e471d73
    parent 1       c881b3e550afb326e6ef95aece46cf1684415c4f   (commit 1, the specification)
    parent 2       878b632ced8caa5ef2c6255022a44291d50ccfe2   (the reviewed source branch)
    merge-base     3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b   (the original base)

Read as three distinct values: `git rev-parse <merge>^1`,
`git rev-parse <merge>^2`, `git merge-base <merge>^1 <merge>^2`. The
full parent list `<merge>^@` contains exactly those two, in that order.

**Parent 1 is fixed by which commit the merge was made from**, not
selected: the integration branch stood on the specification commit.

**No conflict.** `git merge --no-ff --no-commit` reported
`Automatic merge went well; stopped before committing as requested`, and
`git diff --name-only --diff-filter=U` returned nothing. `--no-ff` was
mandatory and used; the source descends from the base, so an ordinary
merge would have fast-forwarded.

## 3. A3 — `PRE_MERGE` guard, verbatim

Run at the specification commit, before the merge. `overall: PASS`,
exit status 0, empty stderr.

    {
      "checks": [
        {
          "condition": "worktree_clean",
          "entries": [],
          "status": "PASS"
        },
        {
          "attachment": "gate/p2-integrate-attraction-and-layers",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "c881b3e550afb326e6ef95aece46cf1684415c4f",
          "status": "PASS",
          "worktree_head": "c881b3e550afb326e6ef95aece46cf1684415c4f"
        },
        {
          "actual": "3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b",
          "condition": "merge_base",
          "expected": "3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b",
          "status": "PASS"
        },
        {
          "condition": "scope",
          "evidence": {
            "base": "3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b",
            "failures": [],
            "head": "878b632ced8caa5ef2c6255022a44291d50ccfe2",
            "mode": "exact",
            "observed_operations": [
              {"operation": "modify", "path": "DECISION_LOG.md"},
              {"operation": "add", "path": "derivations/P2-PHASE-01_channel_character_layers.md"},
              {"operation": "add", "path": "reports/2026-08-09T0300Z_attraction-ruling-and-layers.md"},
              {"operation": "add", "path": "results/P2-PHASE-01/channel-character-layers/layers.json"},
              {"operation": "add", "path": "scripts/p2_channel_character_layers.py"},
              {"operation": "add", "path": "specs/2026-08-09T0300Z_attraction-ruling-and-layers.md"},
              {"operation": "add", "path": "tests/test_p2_channel_character_layers.py"}
            ],
            "overall": "PASS",
            "tool": "scope_checker"
          },
          "status": "PASS"
        },
        {
          "condition": "pinned_artifacts",
          "evidence": [
            {"actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS"},
            {"actual": "380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f",
             "expected": "380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f",
             "path": "derivations/P2-PHASE-01_channel_character.md", "status": "PASS"},
            {"actual": "093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f",
             "expected": "093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f",
             "path": "results/P2-PHASE-01/channel-character/channel_character.json", "status": "PASS"},
            {"actual": "521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126",
             "expected": "521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126",
             "path": "scripts/p2_channel_character.py", "status": "PASS"}
          ],
          "status": "PASS"
        }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }

The guard's `other_registered_worktrees` block is omitted above only for
length; it listed fifteen worktrees, all as expected, with the primary
worktree on `gate/p2-grassmann-crossing-sign` at `cf4c789` and the
source-branch worktree on `878b632`.

**A3's two-SHA requirement is satisfiable.** The `POST_MERGE` config
schema carries `merge_commit` and `expected_remote_sha` as separate
fields, so the merge object under verification and the ref the remote is
checked against are represented distinctly. **No stop was required.**
The intended parameters are in §7.

## 4. A5 — `DECISION_LOG.md` arrives intact and append-only

    blob on the source branch    3261b1f5c8b53f5dffed83fe96ffa323f6ce2d74
    blob at the merged head      3261b1f5c8b53f5dffed83fe96ffa323f6ce2d74   IDENTICAL
    blob at the base             345688919786874b8837af150d2ec38976eb6bb2

    git diff --numstat 3b3d3b2e… 10f14f01… -- DECISION_LOG.md
      126     0       DECISION_LOG.md

    deleted lines across the ENTIRE base-to-head diff (^-[^-]):  0

**Append-only, and stronger than the diff shows:** the merged blob has
the base blob as an exact byte prefix, with 5924 characters appended and
nothing before them touched.

### 4.1 The three 2026-08-08 entries, all present and all top-level

    1236  ## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent
    1326  ## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED
    1393  ## 2026-08-08 — Attraction/repulsion sign convention: the label is assigned to the sign of g

All three are `## ` headings. **None became a subsection of another
through the merge.**

**The two earlier entries are unaltered**, compared as byte slices
between base and merged head:

    Euclidean exponent mapping                  identical=True   3618 bytes
    Open derivation item: generator-sum         identical=True   2607 bytes

## 5. A6 — protected paths, blob-identical base to merged head

Read from the Git objects with `git rev-parse <rev>:<path>`:

    GATES.md                                                  bd48205…  IDENTICAL
    CONVENTIONS.md                                            2d4f735…  IDENTICAL
    AGENTS.md                                                 5e60b5f…  IDENTICAL
    pyproject.toml                                            9fc6fdd…  IDENTICAL
    derivations/P2-GAP-01_gap_criticality.md                  70b4383…  IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md         0be773f…  IDENTICAL
    derivations/P2-PHASE-01_channel_character.md              4b9e190…  IDENTICAL
    results/P2-PHASE-01/channel-character/channel_character.json
                                                              e0fcdbb…  IDENTICAL
    scripts/p2_channel_character.py                           569543e…  IDENTICAL
    derivations/P2-GENERATOR-SUM-CRITICALITY_01.md            47c28e2…  IDENTICAL
    derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md   e2bf581…  IDENTICAL
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
                                                              158ab18…  IDENTICAL
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
                                                              5f020f3…  IDENTICAL

**The channel-character artifacts were not edited to record that their
withheld verdicts are now resolved.** Their `layer_1b.verdict` still
reads `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL` and
their `layer_2.verdict` still reads `ATTRACTIVE/REPULSIVE NOT DEFINED BY
THE FROZEN MATERIAL`. **That is correct and deliberate.** Those verdicts
were true of the frozen material at the time they were written, and they
remain true of the frozen material now — what changed is that two
conventions were supplied by ruling, which is later evidence, not a
correction of the earlier record.

## 6. A6a — arriving artifacts intact

Git blob ids at the merged head, compared both to the specification's
declared ids and to the source branch:

    derivations/P2-PHASE-01_channel_character_layers.md
      55e60b2f072edab7504920ae9fbb8cdf16f0fea1   MATCH
    reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
      5c22cee6355bdde3798697ede98b06249a04dcc4   MATCH
    results/P2-PHASE-01/channel-character-layers/layers.json
      73ae5a522a37c310dcee797d24035a5cbc7f6443   MATCH
    scripts/p2_channel_character_layers.py
      68ba9bb87a6600c8ae0b34972b26c1eafba8007f   MATCH
    specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
      3a18acd22bfded37c13f6968090e143ebb4fc86f   MATCH
    tests/test_p2_channel_character_layers.py
      9d863215731f98fb4fe0a87e5b37dfc1930fa231   MATCH

**All six agree with the specification and with the source branch.
Nothing arriving was edited.**

**This criterion earns its place.** A4's path set and the `add`
operation type would both have been satisfied by an edited arriving
file, and no validator in A8 reads the derivation note or the two
reports at all. Before A6a existed, §5's "may not be edited" had no
independent check. It now does.

## 7. A4 — scope, and the intended final `POST_MERGE`

### Intended final manifest

    base: 3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    head: <the report commit, computed after this file is committed>
    mode: exact
    required:
      add     derivations/P2-PHASE-01_channel_character_layers.md
      add     reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
      add     reports/2026-08-09T0346Z_integrate-attraction-and-layers.md
      add     results/P2-PHASE-01/channel-character-layers/layers.json
      add     scripts/p2_channel_character_layers.py
      add     specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
      add     specs/2026-08-09T0346Z_integrate-attraction-and-layers.md
      add     tests/test_p2_channel_character_layers.py
      modify  DECISION_LOG.md
    optional: []
    forbidden_operations: [delete, rename, copy, type_change, unmerged, unknown]

**8 additions and 1 modification.** Six additions arrive from the
branch; two — this report and the integration specification — are
authored here. **A tenth path would be a defect.**

### Observed at the pre-report head

`git diff --name-status 3b3d3b2e… 10f14f01…`, eight paths, this report
not yet existing:

    M   DECISION_LOG.md
    A   derivations/P2-PHASE-01_channel_character_layers.md
    A   reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
    A   results/P2-PHASE-01/channel-character-layers/layers.json
    A   scripts/p2_channel_character_layers.py
    A   specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
    A   specs/2026-08-09T0346Z_integrate-attraction-and-layers.md
    A   tests/test_p2_channel_character_layers.py

Line counts, all additions, no deletions anywhere:

    126   DECISION_LOG.md
    275   derivations/P2-PHASE-01_channel_character_layers.md
    764   reports/2026-08-09T0300Z_attraction-ruling-and-layers.md
    195   results/P2-PHASE-01/channel-character-layers/layers.json
    477   scripts/p2_channel_character_layers.py
    339   specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
    278   specs/2026-08-09T0346Z_integrate-attraction-and-layers.md
    311   tests/test_p2_channel_character_layers.py

### Intended final `POST_MERGE` parameters

    mode                   POST_MERGE
    merge_commit           10f14f01cc2bf8bb18308cd1b12bace28e471d73
    expected_parent_1      c881b3e550afb326e6ef95aece46cf1684415c4f
    expected_parent_2      878b632ced8caa5ef2c6255022a44291d50ccfe2
    expected_merge_base    3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    scope_manifest         the final manifest above
    pinned_artifacts       the same four as PRE_MERGE
    remote_check_policy    REQUIRED
    expected_remote_ref    refs/remotes/origin/main
    expected_remote_sha    <the report commit head>

**Two distinct SHAs, in two distinct fields.** `merge_commit` is the
merge object under verification; `expected_remote_sha` is the final
report-commit head the remote must agree with. **The final guard result
is post-report evidence** and is returned to the Reviewer, not written
back here.

## 8. A7 — no gate changed

    GATES.md   base bd48205…   merged bd48205…   IDENTICAL
    ^## P2- anchor count:   14 before,  14 after

    P2-GAP-01     Status: PASS (continuum exact; lattice `I_0` agrees
                  with paper at matched mass)          — unchanged, no caveat added
    P2-PHASE-01   Status: PROPOSED                     — unchanged

No gate, gate status, verdict, digest or hash-pinned artifact was
modified. The programme registry was not updated: the
`Sign convention for attraction and repulsion` row still reads
`NOT DEFINED`, which is a `0-programme` task and follows this one.

## 9. Does the merged state now read as though anything were settled?

**The specification asks this because the risk is no longer a wrong
number.** Three rulings and four derivations have landed on this topic
in two days. I looked for the assembled conclusion, not for a wrong
statement, and the answer has two parts.

### 9.1 No single artifact overstates anything

Every artifact that touches the question carries its own limit, and I
checked each at the merged head:

- **the ruling** (`DECISION_LOG.md`): "REPULSIVE in a `ψ̄ψ` channel does
  NOT imply that a composite vector is absent"; "A channel-character
  label is not a pole calculation"; "It is not a derivation";
- **the new derivation note**, §6: a repulsive label "does not settle
  whether a composite vector exists", and an attractive label does not
  establish condensation, which depends on `Γ⁽²⁾(0) = 1/g − Π(0)`, the
  determinant, stability and `G_c`;
- **the new results artifact**: the `composite_vector` field says no
  statement is made, and `layer_2.scope_limit` repeats the condensation
  and bound-state limits;
- **the new derivation note**, §7, and the artifact's `diquark` block:
  the particle–particle channel is untouched, three conventions remain
  unfrozen, and `channel_picture_is_not_complete` is `true`;
- **the older channel-character artifacts**, unaltered, still recording
  their withheld verdicts and their own composite-vector scope note.

**Nothing was found that asserts a composite vector is absent, that
condensation occurs, or that the diquark channel is computable.**

### 9.2 One junction does not carry its own disclaimer

**This is the finding.** The merged state contains, in different
documents, every link of a chain that a reader could close without
noticing they had:

1. `results/P2-PHASE-01/channel-character-layers/layers.json` now states
   the induced V singlet has `g_P = -G/N` and is `REPULSIVE`.
2. `results/P2-PHASE-01/normalisation-audit/g_omega_audit.json` records
   Paper 3's coupling as `G_omega = -G/N`, reached by `G_ω = 2·c_J` from
   the same derived `c_J = -G/(2N)`. **The number and the sign are
   identical to link 1**, and this is not a coincidence: Paper 3's
   `L_V = (G_V/2) J_μ J^μ` defines `G_V` as the coefficient of `½J²`,
   which is exactly what `g` is in `exp[(g/2)J²]`. **`g` and `G_V` are
   the same kind of object**, which is why the audit's factor `2` and
   the exponent mapping ruling's factor `2` agree.
3. The same audit artifact quotes Paper 3's classification verbatim:
   `G_V < 0 repulsive (omega survives) / G_V > 0 attractive (fails)`,
   and `derivations/CANONICAL_INTERACTION.md` §7(b) repeats it as
   `classification G_V < 0 repulsive/ω survives`.

**Closing 1 → 2 → 3 yields "the ω survives", which is a statement about
whether a composite vector exists.** That is precisely the inference the
ruling forbids. Nothing in the chain is false; the fallacy is that
Paper 3's parenthetical "(omega survives)" is a label from a framework
in which an ω is already posited, not a consequence of the sign.

**The disclaimers that block this exist**, in the ruling, in both
derivation notes and in both results artifacts. **They are not at the
junction.** A reader arriving at `g_omega_audit.json` or at
`CANONICAL_INTERACTION.md` §7(b) is one step from the conclusion and two
documents away from the warning.

**A second, weaker version of the same shape** concerns condensation:
the scalar singlet is now labelled `ATTRACTIVE`, and `P2-GAP-01` is a
`PASS`ed gate that computes a critical coupling for an attractive scalar
channel. A reader could take the label as evidence that the condensate
forms. **The new note blocks it explicitly** — the label is a channel
statement and condensation needs the full kernel — but `GATES.md`, where
`P2-GAP-01`'s `PASS` lives, does not mention the distinction. This one is
weaker because `P2-GAP-01` already carried the criticality condition.

### 9.3 What I did about it, and did not

**Nothing, deliberately.** `CANONICAL_INTERACTION.md`, `GATES.md` and
the normalisation-audit artifact are all protected paths under A6, and
the arriving artifacts may not be edited under §5 and A6a. **Annotating
the junction inside an integration would break exactly the discipline
those criteria exist to enforce**, and the annotation would have had no
review of its own.

**Recorded as a follow-up recommendation, not performed:** a short note
at the junction — in `CANONICAL_INTERACTION.md` §7(b), or as a field in
the normalisation-audit artifact, or as the `CONVENTIONS.md` index entry
that is already deferred — saying that Paper 3's "(omega survives)"
parenthetical is internal to Paper 3's framework and that the
repository's own channel labels settle no existence question. **It is a
`0-programme` or documentation task, and it should be reviewed on its
own.**

## 10. A8-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py             exit=0    4 passed
    tests/test_si1_governance.py                   exit=0   14 passed
    tests/test_gate_anchors.py                     exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py                 exit=0    8 passed
    tests/test_p2_phase01_scalar_exploratory.py    exit=0    5 passed
    tests/test_p2_phase01_fierz_and_depths.py      exit=0   14 passed
    tests/test_p2_channel_character.py             exit=0   23 passed
    tests/test_p2_generator_sum_criticality.py     exit=0    7 passed
    tests/test_p2_channel_character_layers.py      exit=0   26 passed

`pytest 9.1.1`, Python 3.11.15. **A8-final at the pushed head is
post-report evidence** and carries the verdict.

**Note for the Reviewer.** `test_p2_channel_character.py` and
`test_p2_channel_character_layers.py` both pass at the same head while
asserting apparently opposite things — the former that Layer 2 is
correctly withheld, the latter that Layer 2 is `ATTRACTIVE / REPULSIVE /
REPULSIVE`. **They are not in conflict.** The first asserts what the
*frozen material* determines; the second asserts what the *rulings*
determine. Both are true simultaneously, and their coexistence is the
mechanical form of "later evidence supersedes without rewriting".

## 11. A9 — commit-message hygiene

Every message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` **before**
committing, committed with `git commit -F <file>` and never `-m`, and
the stored message read back from the object afterwards with
`git log -1 --format=%B`.

    commit 1   c881b3e…   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   10f14f0…   trailers suppressed: Co-Authored-By, Claude-Session
               (the merge; committed with --no-commit then -F, so the
                message was authored under the same discipline as the
                others rather than by `git merge -m`)

**Suppression is a fact to disclose, not an absence.** This harness
appends both trailers by default; `-F` prevents it, and the read-back
confirmed neither reached any stored message. No session identifier,
URL, or tool attribution appears in any message.

### Commit 1

    c881b3e550afb326e6ef95aece46cf1684415c4f

    spec: integrate the attraction/repulsion ruling and the recomputed layers

    Verbatim transcription of the PI specification authorizing the
    integration of gate/p2-attraction-ruling-and-layers at 878b632.

### Commit 2 — the merge

    10f14f01cc2bf8bb18308cd1b12bace28e471d73

    merge: integrate the attraction/repulsion ruling and the layers (reviewed; pinned 878b632)

    Merges gate/p2-attraction-ruling-and-layers at
    878b632ced8caa5ef2c6255022a44291d50ccfe2, reviewed and unmodified.

    Brings the PI ruling assigning ATTRACTIVE to g > 0 and REPULSIVE to
    g < 0, and the recomputation it unblocks: the scalar singlet is
    ATTRACTIVE and admits a real linear auxiliary field; the induced V and
    A singlets are REPULSIVE and do not. The Layer-1a control reproduced
    every pinned coefficient with exact symbolic difference zero and the
    scalar control returned ATTRACTIVE consistent with P2-GAP-01.

    This closes two verdicts the channel-character derivation deliberately
    withheld. Withholding them was correct at the time; both blockers have
    since been ruled on. The earlier artifacts are not edited to say so.

    Nothing here establishes that a composite vector is absent, that
    condensation occurs, or that the particle-particle channel is
    computable. No Hubbard-Stratonovich channel is selected, no diquark
    convention is frozen, no gate status changes, and the programme
    registry is untouched.

### Intended report commit message

Prepared the same way, with the same two trailers suppressed:

    docs: report the integration of the attraction/repulsion ruling and the layers

    Records one --no-ff merge of gate/p2-attraction-ruling-and-layers at
    878b632, with correct parentage and the original base as merge-base.
    DECISION_LOG.md arrives blob-identical and append-only, all three
    2026-08-08 entries present and top-level, and every arriving blob
    byte-identical to its reviewed value.

    Reports that no single artifact overstates what has been established,
    and names one junction that does not carry its own disclaimer: the
    induced V singlet's g = -G/N and REPULSIVE label sit beside Paper 3's
    G_omega = -G/N and its "(omega survives)" classification, and the
    warnings that block the inference live in other documents. Reported
    as a follow-up recommendation and deliberately not fixed here.

## 12. A10 — branches preserved

    gate/p2-attraction-ruling-and-layers    878b632ced8caa5ef2c6255022a44291d50ccfe2
    review/role-model-and-executors         10c260b96882ac12610f78840aeeabd07be2d7cb

Both unchanged. **This task deleted no branch.**

## 13. Worktree states, stated separately

**The merge worktree**, `<scratch>/integ7`: created from
`3b3d3b2e…` for this task, attached to
`gate/p2-integrate-attraction-and-layers`, clean at the pre-report head
`10f14f01…`. The `PRE_MERGE` guard's `worktree_clean` check confirmed it
independently before the merge.

**The primary worktree**, `/home/user/2-emergent-gravity`: on
`gate/p2-grassmann-crossing-sign` at `cf4c789`, **zero modified or
untracked entries, and not touched by this task.**

No other worktree was altered. Nothing was cleaned, stashed or
discarded anywhere.

## 14. Stops and clarifications

**No stop occurred.** No conflict arose, every check passed, and no
instruction proved inconsistent with a repository rule or with another
instruction.

### `SPECIFICATION_DEFECT`

None.

### `ENVIRONMENT`

None. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

None.

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

None that blocked execution. §9.2 is a finding of this class in
substance — an assembled conclusion available across artifacts that no
artifact states — but it obstructed nothing and is recorded as a
recommendation rather than a stop.

## 15. Secondary findings, and what I would have specified differently

**1. A6a is the right criterion and should become standard.** Before
it, "everything arriving by merge may not be edited" was an instruction
with no verification: an edited arriving file is still an `A` operation,
still satisfies the path set, and — for a derivation note or a report —
is read by no test at all. **I would put A6a, or its equivalent, in
every integration specification**, and I flagged the same gap
implicitly on earlier integrations without naming it this clearly.

**2. The exponent mapping ruling has now been independently
corroborated, and nobody asked for it.** The normalisation audit,
already on `main`, found `G_ω = 2·c_J` for Paper 3's vector coupling.
The exponent mapping ruling independently gives `g = 2c`. **These are
the same relation**, because Paper 3's `L_V = (G_V/2)J²` defines `G_V`
as the coefficient of `½J²` — the same slot `g` occupies in
`exp[(g/2)J²]`. The ruling's own basis cites only `P2-GAP-01`'s real
auxiliary field. **This is a second, structurally different consistency
check, and it agrees.** It is not a derivation and does not upgrade the
ruling's status, but it is stronger corroboration than the one the
ruling cites, and it deserves to be recorded where the ruling is.

**3. Paper 3's sign-to-label direction already agreed with the new
ruling.** Paper 3 classifies `G_V < 0` as repulsive and `G_V > 0` as
attractive. The ruling assigns `g < 0` REPULSIVE and `g > 0`
ATTRACTIVE. **Same object, same direction** — a third consistency
anchor, also not cited by the ruling. Recorded because it makes the
ruling less arbitrary than its own text suggests, and because a reader
should know the convention was not chosen freely.

**4. Recurring, and raised for the fifth time.** The
`CONVENTIONS.md` index entry deferred by
`specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md` §0(b) is
still not written, and there are now **three** conventions living only
as dated `DECISION_LOG.md` entries — the exponent mapping, the
attraction/repulsion labels, and by implication the relation between
them. The merged script `scripts/p2_channel_character_layers.py`
locates two of them by exact heading text, so **renaming either heading
now breaks executable code on `main`.** That coupling is deliberate and
good, but it means the index task is no longer only tidiness.

**5. What I would have specified differently.** §2's step list and §4's
commit order are still two lists describing one sequence, and the
specification commit appears only in §4. This is the fifth consecutive
integration on which I have said so. It has never caused an error
because §4 is unambiguous, but a reader following §2 alone would merge
before writing the specification and get parent 1 wrong.
