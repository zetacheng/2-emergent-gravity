# Execution report — integrate the channel-character derivation and the normalisation audit

Authority: `specs/2026-08-08T1427Z_integrate-channel-character-and-audit.md`
Evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`
Branch: `gate/p2-integrate-channel-character-and-audit`
Classification: MATERIAL.

**Two merges, both clean, no conflict. Zero files modified.** Written at
the pre-report head `258c98c0584c8b4b9c75901be56292e582b0a1b1`, before
the push; it contains neither its own commit SHA nor the final branch
head.

**Nothing is frozen, decided or upgraded by this integration.** §9 states
what remains open.

---

## 1. A1 — refs, read from the remote

    $ git fetch --prune origin                                   exit 0
    $ git ls-remote origin …

    eb88a2c9174cfda746c266924e741a6f88134234  refs/heads/main
    cb604a4e3a96f9120787a685120f205d8e4c7c88  refs/heads/gate/p2-channel-character
    9c6ff5b3ed8c0071abed058c4567f4b50c974d76  refs/heads/fix/normalisation-audit-g-omega
    10c260b96882ac12610f78840aeeabd07be2d7cb  refs/heads/review/role-model-and-executors

Remote-tracking refs after the fetch, reported separately:

    refs/remotes/origin/main                              eb88a2c9174cfda746c266924e741a6f88134234
    refs/remotes/origin/gate/p2-channel-character         cb604a4e3a96f9120787a685120f205d8e4c7c88
    refs/remotes/origin/fix/normalisation-audit-g-omega   9c6ff5b3ed8c0071abed058c4567f4b50c974d76

Local `main`, reported separately and **not repaired**:

    refs/heads/main                                       0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**Every A1 value matched. No STOP.** Both merges were performed against
`refs/remotes/origin/*` immediately after the fetch, never against a
local branch ref.

## 2. The specification's structural claims, verified independently

Re-derived before merging rather than inherited.

**Neither source contains the other.**

    $ git merge-base --is-ancestor cb604a4e… 9c6ff5b3…      exit 1
    $ git merge-base --is-ancestor 9c6ff5b3… cb604a4e…      exit 1

**All three merge-bases are the original base.**

    merge-base(base, A) = eb88a2c9174cfda746c266924e741a6f88134234
    merge-base(base, B) = eb88a2c9174cfda746c266924e741a6f88134234
    merge-base(A,    B) = eb88a2c9174cfda746c266924e741a6f88134234

**Disjoint path sets, and both branches additive only.**

    Branch A (6 paths, all A)          Branch B (5 paths, all A)
    A derivations/P2-PHASE-01_channel_character.md
                                       A derivations/P2-NORMALISATION-AUDIT_g_omega.md
    A reports/…1321Z_channel-character.md
                                       A reports/…1354Z_normalisation-audit.md
    A results/…/channel-character/channel_character.json
                                       A results/…/normalisation-audit/g_omega_audit.json
    A scripts/p2_channel_character.py  A scripts/p2_normalisation_audit.py
    A specs/…1321Z_channel-character.md
                                       A specs/…1354Z_normalisation-audit.md
    A tests/test_p2_channel_character.py

    overlap count: 0
    6 + 5 = 11 arriving operations: 11 additions, 0 modifications

A grep for any status other than `A` on either branch returned nothing:
**neither branch changes an existing file**, exactly as the authority
states.

## 3. A2 — merge parentage, as distinct values

**Merge A** — `46b2915d1fe04f137fff5cbf5002adb22066f0cb`

    parent 1    ead58b640b8fe6a97c2dc61ece19d912d9c98dbb   the integration spec commit (commit 1)
    parent 2    cb604a4e3a96f9120787a685120f205d8e4c7c88   Branch A tip
    merge-base  eb88a2c9174cfda746c266924e741a6f88134234   the ORIGINAL base

**Merge B** — `258c98c0584c8b4b9c75901be56292e582b0a1b1`

    parent 1    46b2915d1fe04f137fff5cbf5002adb22066f0cb   the Merge-A commit
    parent 2    9c6ff5b3ed8c0071abed058c4567f4b50c974d76   Branch B tip
    merge-base  eb88a2c9174cfda746c266924e741a6f88134234   the ORIGINAL base

The two merge commits are distinct objects. Parent 1 in each case was
fixed by the commit being stood on, not selected. Merge B's merge-base is
the original base and **not** the Merge-A commit, because Branch B was
cut from the same base and does not contain Merge A.

Both merges used `--no-ff`; both produced a real merge commit with
exactly two parents; neither reported a conflict:

    Merge made by the 'ort' strategy.
     …6 files changed, 2783 insertions(+)      [Merge A]
     …5 files changed, 1646 insertions(+)      [Merge B]

    $ git status --porcelain=v1     (after each merge)
    (empty)

**Every arriving line is an insertion.** The two merge diffstats show
`2783 insertions(+)` and `1646 insertions(+)` with no deletions.

## 4. A3 — guards

### 4.1 `PRE_MERGE(A)`, at the spec commit, before Merge A

    {
      "checks": [
        {
          "condition": "worktree_clean",
          "entries": [],
          "status": "PASS"
        },
        {
          "attachment": "gate/p2-integrate-channel-character-and-audit",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "ead58b640b8fe6a97c2dc61ece19d912d9c98dbb",
          "status": "PASS",
          "worktree_head": "ead58b640b8fe6a97c2dc61ece19d912d9c98dbb"
        },
        {
          "actual": "eb88a2c9174cfda746c266924e741a6f88134234",
          "condition": "merge_base",
          "expected": "eb88a2c9174cfda746c266924e741a6f88134234",
          "status": "PASS"
        },
        {
          "condition": "scope",
          "evidence": {
            "base": "eb88a2c9174cfda746c266924e741a6f88134234",
            "failures": [],
            "head": "cb604a4e3a96f9120787a685120f205d8e4c7c88",
            "mode": "exact",
            "observed_operations": [
              {"operation": "add", "path": "derivations/P2-PHASE-01_channel_character.md"},
              {"operation": "add", "path": "reports/2026-08-08T1321Z_channel-character.md"},
              {"operation": "add", "path": "results/P2-PHASE-01/channel-character/channel_character.json"},
              {"operation": "add", "path": "scripts/p2_channel_character.py"},
              {"operation": "add", "path": "specs/2026-08-08T1321Z_channel-character.md"},
              {"operation": "add", "path": "tests/test_p2_channel_character.py"}
            ],
            "overall": "PASS",
            "tool": "scope_checker"
          },
          "status": "PASS"
        },
        {
          "condition": "pinned_artifacts",
          "evidence": [
            {"actual": "27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81",
             "expected": "27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81",
             "path": "derivations/CANONICAL_INTERACTION.md", "status": "PASS"},
            {"actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS"},
            {"actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json", "status": "PASS"},
            {"actual": "40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606",
             "expected": "40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606",
             "path": "scripts/P2-CHANNEL-FREEZE/vocab_parser.py", "status": "PASS"}
          ],
          "status": "PASS"
        }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }
    === exit 0 ===

`derivations/CANONICAL_INTERACTION.md` is pinned in **both** guards, not
only in A5's post-merge check — Branch B produces evidence about that
file and must not have touched it.

### 4.2 `PRE_MERGE(B)`, at the Merge-A commit, before Merge B

Same four pinned artifacts, all `PASS`:

    overall: PASS
      worktree_clean                    -> PASS
      worktree_matches_declared_target  -> PASS   (head 46b2915d…, the Merge-A commit)
      merge_base                        -> PASS   (eb88a2c9…, the ORIGINAL base)
      scope                             -> PASS   (base eb88a2c9… head 9c6ff5b3…)
      pinned_artifacts                  -> PASS
    === exit 0 ===

    observed_operations:
      add  derivations/P2-NORMALISATION-AUDIT_g_omega.md
      add  reports/2026-08-08T1354Z_normalisation-audit.md
      add  results/P2-PHASE-01/normalisation-audit/g_omega_audit.json
      add  scripts/p2_normalisation_audit.py
      add  specs/2026-08-08T1354Z_normalisation-audit.md

### 4.3 The final `POST_MERGE` — intended parameters

**The two roles are representable separately, so no stop arose.**
`merge_guard.post_merge` takes `merge_commit` and `expected_remote_sha`
as independent config keys.

    mode                  POST_MERGE
    merge_commit          258c98c0584c8b4b9c75901be56292e582b0a1b1   <- the MERGE OBJECT (Merge B)
    expected_parent_1     46b2915d1fe04f137fff5cbf5002adb22066f0cb
    expected_parent_2     9c6ff5b3ed8c0071abed058c4567f4b50c974d76
    expected_merge_base   eb88a2c9174cfda746c266924e741a6f88134234
    remote_check_policy   REQUIRED
    expected_remote_ref   refs/remotes/origin/main
    expected_remote_sha   <the final REPORT-commit head>              <- a DIFFERENT SHA
    scope_manifest        the A4 manifest below, head = final head
    pinned_artifacts      the same four as the PRE_MERGE guards

`merge_commit` is a merge object; `expected_remote_sha` is the report
commit that will be `main`'s tip. Different commits, different keys. The
executed guard is post-report evidence.

## 5. A5 — protected paths

Read from the objects, base vs merged head:

    GATES.md                                            bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                      2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    DECISION_LOG.md                                     0bc14ab020464c8dad56cdd6785914a8fa445992   IDENTICAL
    pyproject.toml                                      9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/CANONICAL_INTERACTION.md                6e5d9e1bb7dffe67e7b9ada026b366ef0e10a2a9   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md   0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json         5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf   IDENTICAL
    scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py     8be4f5de8a3b08230835c55a24ff3b95dfc5196b   IDENTICAL
    scripts/P2-CHANNEL-FREEZE/vocab_parser.py           20800bc649924fd0629b3232615dae4c4fac36a7   IDENTICAL

**`CANONICAL_INTERACTION.md` is unchanged and its banner is intact**, read
from the merged tree:

    # CANONICAL_INTERACTION.md — DRAFT v0.5 (ratification candidate)

    **Status: DRAFT v0.5 — ratification candidate under the Discriminator's

Branch B produced evidence *about* that document and altered nothing *in*
it — which is the whole point of the check, and it holds.

## 6. A6 — arriving content intact

Blob-compared against the source branch tips.

From Branch A @ `cb604a4e…`:

    derivations/P2-PHASE-01_channel_character.md                  4b9e1902997a944bb17f7f3b419fe45c5920bb17   IDENTICAL
    reports/2026-08-08T1321Z_channel-character.md                 9bac625752680f2a8051df497df27768844f0362   IDENTICAL
    results/P2-PHASE-01/channel-character/channel_character.json  e0fcdbb784e951176fd40ca11252435f20a53df1   IDENTICAL
    scripts/p2_channel_character.py                               569543ee0b6aae7cc2a873fbee0a3516eb6106bd   IDENTICAL
    specs/2026-08-08T1321Z_channel-character.md                   7bbb1fd5138193d999b6a2617d9f26d934a75a83   IDENTICAL
    tests/test_p2_channel_character.py                            d7f18814f0e8983cf0a13e2048ff813d5e1da95c   IDENTICAL

From Branch B @ `9c6ff5b3…`:

    derivations/P2-NORMALISATION-AUDIT_g_omega.md                 065201c0c82a1c9dae52581cb2fd4742acf1be79   IDENTICAL
    reports/2026-08-08T1354Z_normalisation-audit.md               315c18fe41b315149983d7b33d1647f9790175a5   IDENTICAL
    results/P2-PHASE-01/normalisation-audit/g_omega_audit.json    52aad469fad522207b0d5985c504f7f343e84518   IDENTICAL
    scripts/p2_normalisation_audit.py                             c7a409f325cae22905132e7f4c5b345e3e8f2ad4   IDENTICAL
    specs/2026-08-08T1354Z_normalisation-audit.md                 ab559d142821ba176a68dc3055058e92bb937bbd   IDENTICAL

All eleven arriving additions present and byte-identical to their source.
**Nothing arriving by merge was edited**, including the two withheld
verdicts and the diquark determination.

## 7. A7 — no gate changed

    GATES.md base vs merged head                        IDENTICAL (bd482051…)
    '^## P2-' count at base                             14
    '^## P2-' count at merged head                      14
    P2-PHASE-01                                         Status: PROPOSED

**No gate, gate status, verdict, digest or hash-pinned artifact was
modified.**

## 8. A8 — nothing outside the manifest, and zero modifications

    $ git diff --name-status eb88a2c9… HEAD
    A	derivations/P2-NORMALISATION-AUDIT_g_omega.md
    A	derivations/P2-PHASE-01_channel_character.md
    A	reports/2026-08-08T1321Z_channel-character.md
    A	reports/2026-08-08T1354Z_normalisation-audit.md
    A	results/P2-PHASE-01/channel-character/channel_character.json
    A	results/P2-PHASE-01/normalisation-audit/g_omega_audit.json
    A	scripts/p2_channel_character.py
    A	scripts/p2_normalisation_audit.py
    A	specs/2026-08-08T1321Z_channel-character.md
    A	specs/2026-08-08T1354Z_normalisation-audit.md
    A	specs/2026-08-08T1427Z_integrate-channel-character-and-audit.md
    A	tests/test_p2_channel_character.py

    additions:     12       (11 arriving + the integration specification)
    modifications:  0
    anything not an addition:  NONE

### **Zero files were modified. This integration is additive only.**

The authority asks for this to be stated explicitly, and a single
modification would be a finding. There is none — no `M`, no `D`, no `R`,
no `C`, no `T`, no `U` in the entire base-to-head range. The twelve
additions above plus the report commit give the thirteen of A4; **there
is no fourteenth path.**

## 9. A9-pre — ten validators, at head `258c98c0`

    $ python -m pytest tests/test_repository_structure.py            ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py                  -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py                    -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py                ->  8 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_scalar_exploratory.py   ->  5 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py     -> 14 passed              exit 0
    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py      -> 19 passed              exit 0
    $ python -m pytest tests/test_p2_channel_character.py            -> 23 passed              exit 0
    $ python -m pytest tests/test_channel_freeze_phase_a.py          ->  3 passed              exit 0
    $ python -m pytest tests/test_channel_freeze_mutations.py        -> 18 passed              exit 0

All ten exit 0. Exit statuses were captured from `python -m pytest`
itself, not from the tail of a pipeline.

`tests/test_p2_channel_character.py` is the file arriving from Branch A;
its 23 tests pass in the merged tree, which is the regression evidence
that the arriving test file works against the integrated repository and
not only against its own branch.

## 10. A4 — scope manifest

Held with a `{PUSHED_HEAD}` placeholder so the digest does not depend on
the report commit. SHA-256:
`2b65142418ede6db00d8ac0b7d69935275c9909272ae74ffb085cdcd9c5f496c`.

    {
      "base": "eb88a2c9174cfda746c266924e741a6f88134234",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "derivations/P2-NORMALISATION-AUDIT_g_omega.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_channel_character.md"},
        {"operation": "add", "path": "reports/2026-08-08T1321Z_channel-character.md"},
        {"operation": "add", "path": "reports/2026-08-08T1354Z_normalisation-audit.md"},
        {"operation": "add", "path": "reports/2026-08-08T1427Z_integrate-channel-character-and-audit.md"},
        {"operation": "add", "path": "results/P2-PHASE-01/channel-character/channel_character.json"},
        {"operation": "add", "path": "results/P2-PHASE-01/normalisation-audit/g_omega_audit.json"},
        {"operation": "add", "path": "scripts/p2_channel_character.py"},
        {"operation": "add", "path": "scripts/p2_normalisation_audit.py"},
        {"operation": "add", "path": "specs/2026-08-08T1321Z_channel-character.md"},
        {"operation": "add", "path": "specs/2026-08-08T1354Z_normalisation-audit.md"},
        {"operation": "add", "path": "specs/2026-08-08T1427Z_integrate-channel-character-and-audit.md"},
        {"operation": "add", "path": "tests/test_p2_channel_character.py"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**13 additions, 0 modifications**, matching A4. The `{HHMM}` token
resolved to `1427` at commit 1 and is reused. `modify` is empty, as the
authority requires — the manifest itself asserts the additive-only
property, so a modification would fail the scope check rather than merely
be noticed in prose. The resolved manifest, its SHA-256 and the checker
JSON at the pushed head are post-report evidence.

## 11. Worktree states, stated separately

**The merge worktree** — `…/scratchpad/integ4`, attached to
`gate/p2-integrate-channel-character-and-audit`, at
`258c98c0584c8b4b9c75901be56292e582b0a1b1`.
`git status --porcelain=v1` empty after both merges. All merging and all
checks in this report were performed here.

**The main worktree** — `/home/user/2-emergent-gravity`, attached to
`gate/p2-grassmann-crossing-sign` at `cf4c789`. **It was not touched by
this task** beyond read-only `fetch` and `ls-remote`; it reported 0 dirty
entries before the work began and its attachment is unchanged. Local
`main` was not checked out, fast-forwarded or repaired.

**Seven other registered worktrees**, none altered, cleaned or stashed,
all reporting 0 dirty entries at the start of this task:

    …/scratchpad/chan     cb604a4  [gate/p2-channel-character]
    …/scratchpad/fixA     0ab0ca9  [fix/freeze-checker-sign-repair]
    …/scratchpad/fixB     f2da41a  [fix/branch-deletion-policy]
    …/scratchpad/fixC     1c10637  [fix/branch-deletion-policy-amendment]
    …/scratchpad/integ    9609677  [integration/role-model-clean]
    …/scratchpad/integ2   236f71c  [gate/p2-integrate-fierz-and-sign-ruling]
    …/scratchpad/integ3   eb88a2c  [fix/integrate-freeze-repair-and-deletion-policy]
    …/scratchpad/norm     9c6ff5b  [fix/normalisation-audit-g-omega]

## 12. What remains open — nothing here closes it

Restated because an integration is where scope creep is easiest.

**Two withheld verdicts stand exactly as reviewed.** Layer 1b remains
`REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL` and Layer 2
remains `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`. **No
withheld verdict was upgraded**; the arriving files are byte-identical
(§6), so this is verified rather than asserted.

**Four conventions are now known to be missing, and this integration
freezes none of them:**

1. the Euclidean exponent mapping — whether the canonical four-fermion
   expression is a term of `S_E` or already sits in the exponent;
2. `η` in `ψ̄^c = η ψ^T C⁻¹`;
3. the particle–particle Grassmann ordering;
4. the diquark operator normalisation.

**The three diquark-definition gaps are unresolved inputs, and this
integration assigns them to no governance item.** The authority is
explicit that their governance placement is not settled here, and I have
not placed them.

**`OPEN-AC-1` is narrowed, not answered.** No Hubbard–Stratonovich
channel is selected. The exponent mapping bears on it directly, and
naming that mapping as the missing piece is the narrowing — it is a
smaller decision than choosing a channel, but it is still the PI's.

**`CANONICAL_INTERACTION.md` keeps its DRAFT v0.5 banner.** One row of
its §5 evidence table now exists; the others do not. Landing that row
does not ratify the document, and §5 above verifies the file itself is
untouched.

**`P2-PHASE-01` remains `PROPOSED`** (§7).

## 13. Stops and clarifications

**Stops: none.** No A1 ref mismatched, no merge conflicted, no guard
returned `FAIL`, no modification appeared where the manifest allows
none, and the `POST_MERGE` guard proved able to carry the merge object
and the remote head as distinct values — so A3's stop condition did not
arise.

**Findings: none of my own in this task.** No tool-invocation error, no
observation-method error, and no repository defect surfaced during the
integration itself.

**Finding 1 — secondary, carried forward, not this task's to fix.** The
channel-character report records two pre-existing defects in
`CANONICAL_INTERACTION.md`: §2 states the canonical interaction with a
Minkowski kinetic operator while all algebra is Euclidean with no
Wick-rotation rule recorded, and the document carries both a
"no governing force" DRAFT banner and a completed ratification record at
its foot. **Both arrive on `main` with this integration as recorded
findings**, and the file is on A5's protected list, so neither is
repaired here. They are the substantive reason Layer 1b could not
resolve.

**Clarification 1 — where commit 1 sits in §2's sequence.** §2 lists ten
steps and does not name the specification commit; §4 requires it as
commit 1 and A2 requires it to be parent 1 of Merge A. I took it as part
of step 1 — create the branch, land the spec — which is the only
placement satisfying both. **This is the same unlisted step I flagged in
the previous integration report**, and it recurred verbatim; see §14(b).

**Clarification 2 — which ref was merged.** §5 requires merging the
pinned remote refs rather than local copies. I merged
`refs/remotes/origin/<branch>` immediately after `git fetch --prune`,
having confirmed each equals both its `git ls-remote` value and its
pinned SHA.

**Clarification 3 — the `modify: []` line in A4.** The manifest declares
an empty modify list rather than omitting the key. The scope checker
treats absent and empty identically, so this changes no behaviour, but it
makes the additive-only property explicit in the frozen artifact rather
than only in prose. Noted as a small improvement worth keeping.

## 14. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A11 were met as written, and every
structural claim held on independent re-derivation.

**(a) A4's `modify: []` and the "zero modifications" report line are the
right pattern and I would generalise them.** Most integration
specifications in this programme state the expected operation counts in
prose; this one puts the additive-only property into the manifest, where
the checker enforces it. **An integration that expects no modification
should say so in the manifest, not only in the report contract.**

**(b) §2's step list and §4's commit order should be one list.**
Clarification 1. I raised this on the previous integration and it is
unchanged here — two orderings that must be interleaved to be executed,
with the specification commit appearing only in one of them. It is
self-consistent both times, but the interleaving is still left to the
reader, and this is exactly the shape of the parent-1 defect an earlier
integration specification in this programme actually contained.

**(c) A8 and A4 overlap almost completely.** A4 freezes thirteen paths
with `mode: exact`, which already means "nothing outside the manifest";
A8 then says it again as a separate criterion. No harm, but the reader
has to check whether A8 adds a condition A4 lacks — it does not. I would
fold A8 into A4 as a sentence.

One thing I would keep exactly as written: **§0's insistence that
"withheld verdicts are results", together with the §5 prohibition on
upgrading them.** An integration is precisely where a `NOT DEFINED`
verdict is most likely to be quietly softened into a "pending" or a
"probably", and naming that risk in the authority is what makes §12
checkable rather than rhetorical.

## 15. Commits, and commit-message hygiene

Commits 1–3, at the pre-report head. The report commit's SHA is
necessarily absent from the report it commits; its intended message is
below and its stored message is read back as post-report evidence.

**Commit 1** — `ead58b640b8fe6a97c2dc61ece19d912d9c98dbb`

    spec: integrate the channel-character derivation and the normalisation audit

    Records the PI integration authorization, evidence base
    eb88a2c9174cfda746c266924e741a6f88134234, transcribed verbatim.

    Eleven additions arrive from two branches with disjoint path sets and no
    modification to any existing file. Branch A delivers the channel
    character in three layers, two of them withheld as NOT DEFINED BY THE
    FROZEN MATERIAL, and locates the diquark obstruction away from the
    charge-conjugation matrix. Branch B produces one row of the
    CANONICAL_INTERACTION.md evidence table, ruling the apparent G_omega
    factor of two a normalisation mapping rather than a defect.

    The specification is explicit that the withheld verdicts are results and
    that four conventions are now known to be missing. This integration
    freezes none of them, selects no Hubbard-Stratonovich channel, assigns
    the three diquark-definition gaps to no governance item, upgrades no
    withheld verdict, and leaves the CANONICAL_INTERACTION.md banner in
    place.

**Commit 2 (Merge A)** — `46b2915d1fe04f137fff5cbf5002adb22066f0cb`

    merge: integrate the channel-character derivation (reviewed; pinned cb604a4)

    Integrates gate/p2-channel-character at
    cb604a4e3a96f9120787a685120f205d8e4c7c88 into the integration branch.

    Six additions, all reviewed: the task specification, the derivation
    note, the script, the results artifact, a new test file with 23 tests,
    and the execution report.

    The derivation reports the channel character of the Fierz-induced
    interaction in three layers that are kept apart. Layer 1a is
    unconditional: the scalar singlet coefficient is positive and the
    induced V and A singlet coefficients are negative, in both of the
    normalisations the note declares, with S, P and T exactly zero. Layer 1b
    is withheld as REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL,
    because no frozen statement maps the canonical interaction expression
    into the Boltzmann exponent; both branches of that mapping are computed.
    Layer 2 is withheld in consequence.

    For the diquark channel the derivation reaches step 4 of the authority's
    ordering. The charge-conjugation matrix is unique up to a scalar that
    cancels between the paired conjugate factors, so C is not the
    obstruction; the obstruction is the unfrozen charge-conjugated field
    convention, the particle-particle Grassmann ordering, and the diquark
    normalisation.

    Nothing pre-existing is touched: the branch is additive only.

**Commit 3 (Merge B)** — `258c98c0584c8b4b9c75901be56292e582b0a1b1`

    merge: integrate the G_omega normalisation audit (reviewed; pinned 9c6ff5b)

    Integrates fix/normalisation-audit-g-omega at
    9c6ff5b3ed8c0071abed058c4567f4b50c974d76 into the integration branch.

    Five additions, all reviewed: the task specification, the derivation
    note, the script, the results artifact, and the execution report.

    The audit produces one row of the evidence table CANONICAL_INTERACTION.md
    requires for its own ratification. Verdict NORMALISATION MAPPING: Paper 3
    defines G_omega by L_V = (G_V/2) J_mu J^mu, so G_omega is twice the
    coefficient of J_mu J^mu, and line 189 of the pinned Paper-3 note writes
    that coefficient explicitly as -(G/2N) before naming G_omega. That is the
    value this repository derives for the same operator, so the apparent
    factor of two is definitional and neither value was adjusted. Agreement
    holds at every intermediate level, not only the endpoint.

    The Paper-3 note was read from a read-only clone of a pinned external
    revision with its digest verified. No Paper-3 file is copied into this
    repository and nothing in Paper 3 was modified.

    CANONICAL_INTERACTION.md is untouched and retains its DRAFT v0.5
    ratification-candidate banner; the other rows of its evidence table
    remain unproduced.

    Branch B was cut from the same base as Branch A and does not contain
    merge A, so the merge-base of this merge is the original base and not
    the merge-A commit.

**Intended report commit message** (commit 4):

    docs: report the integration of the channel character and the audit

    Records A1-A3, A5-A8, A9-pre and A10 for the two merges, with both merge
    commits' parents and merge-bases as distinct values, both PRE_MERGE
    guard results, and the intended final manifest and POST_MERGE
    parameters.

    Zero files were modified: the base-to-head range contains additions
    only, and the manifest declares an empty modify list so the scope
    checker enforces it rather than the report merely observing it.
    CANONICAL_INTERACTION.md is byte-identical with its DRAFT banner
    intact, GATES.md is unchanged at 14 P2 gates, and the arriving test
    file's 23 tests pass in the merged tree.

    Both withheld verdicts stand unaltered, none of the four missing
    conventions is frozen, the three diquark-definition gaps are assigned
    to no governance item, and no Hubbard-Stratonovich channel is selected.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this
branch — **including both merge commits** — by composing each message in
a file and passing it with `-F`, never `-m`, and never through a path
that would append them.

    commit 1  ead58b64   spec       suppressed: Co-Authored-By, Claude-Session
    commit 2  46b2915d   MERGE A    suppressed: Co-Authored-By, Claude-Session
    commit 3  258c98c0   MERGE B    suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)              suppression applied identically; stored
                                    message read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` returned no match on either form, for all three
commits. **No trailer appeared despite inspection, so A10's pre-push STOP
did not trigger.**

**Suppression is a fact disclosed here, not an absence.** The merge
commits in particular — where a generated message would ordinarily be
accepted with `--no-edit` — were given authored messages by file for
exactly this reason.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
