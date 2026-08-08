# Execution report — integrate the exponent-mapping ruling

Authority: `specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md`
Evidence base: `481f4ad77cb4ec92ef9d58471530784087e67a43`
Branch: `fix/integrate-exponent-mapping-ruling`
Classification: MATERIAL.

**One merge, clean, no conflict.** Written at the pre-report head
`d56335b5281ecdf062ce1d615ead0b7b76a8e692`, before the push; it contains
neither its own commit SHA nor the final branch head.

**A pure integration.** It merges reviewed content and authors nothing
but its own specification and report. **Neither deferred item of §0 was
performed** — see §8.

---

## 1. A1 — refs, read from the remote

    $ git fetch --prune origin                                exit 0
    $ git ls-remote origin …

    481f4ad77cb4ec92ef9d58471530784087e67a43  refs/heads/main
    79399dfd26eacb69a0ef0cba8432ec46e2366eea  refs/heads/fix/exponent-mapping-ruling
    10c260b96882ac12610f78840aeeabd07be2d7cb  refs/heads/review/role-model-and-executors

Remote-tracking refs after the fetch, reported separately:

    refs/remotes/origin/main                         481f4ad77cb4ec92ef9d58471530784087e67a43
    refs/remotes/origin/fix/exponent-mapping-ruling  79399dfd26eacb69a0ef0cba8432ec46e2366eea

Local `main`, reported separately and **not repaired**:

    refs/heads/main                                  0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**Every A1 value matched. No STOP.** The merge was performed against
`refs/remotes/origin/fix/exponent-mapping-ruling` immediately after the
fetch, never against a local branch ref.

## 2. The dry-run claims, verified independently

Re-derived before merging rather than inherited.

    merge-base(base, source) = 481f4ad77cb4ec92ef9d58471530784087e67a43   the ORIGINAL base

    source changed paths:
      M	DECISION_LOG.md
      A	reports/2026-08-08T1634Z_exponent-mapping-ruling.md
      A	specs/2026-08-08T1634Z_exponent-mapping-ruling.md
      additions: 2   modifications: 1

    the one modification, on the source branch:
      157	0	DECISION_LOG.md        (added  deleted  path)
      deleted lines: 0
      hunk header: @@ -1232,3 +1232,160 @@

    both new entries present, as separate top-level headings:
      1236:## 2026-08-08 — Euclidean exponent mapping: …
      1326:## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED
      '##' headings from the first to EOF: 2

**All four claims hold as stated.**

## 3. A2 — merge parentage, as distinct values

**Merge commit** — `d56335b5281ecdf062ce1d615ead0b7b76a8e692`

    parent 1    471a7a7b913a38cee106d12fe2cc51f567ddad5e   the integration spec commit (commit 1)
    parent 2    79399dfd26eacb69a0ef0cba8432ec46e2366eea   the source branch tip
    merge-base  481f4ad77cb4ec92ef9d58471530784087e67a43   the ORIGINAL base

Parent 1 was fixed by the commit being stood on, not selected. The merge
used `--no-ff` and produced a real merge commit with exactly two parents.
No conflict:

    Merge made by the 'ort' strategy.
     3 files changed, 1144 insertions(+)

    $ git status --porcelain=v1
    (empty)

**Every arriving line is an insertion** — `1144 insertions(+)`, no
deletions.

## 4. A5 — `DECISION_LOG.md` arrived intact and append-only

### 4.1 Blob-identical to the source branch

    base    0bc14ab020464c8dad56cdd6785914a8fa445992
    source  345688919786874b8837af150d2ec38976eb6bb2
    merged  345688919786874b8837af150d2ec38976eb6bb2
    merged == source : YES

**The merge changed nothing about the file.** The reviewed content
arrived byte-for-byte.

### 4.2 Zero deleted lines, proved two ways

    $ git diff --numstat 481f4ad7… HEAD -- DECISION_LOG.md
    157	0	DECISION_LOG.md          (added  deleted  path)

    lines beginning with a single '-':  0
    hunk header:  @@ -1232,3 +1232,160 @@

A single hunk starting at line 1232 of a 1234-line file, adding only.
And the stronger check:

    $ git cat-file blob 481f4ad7…:DECISION_LOG.md > base.txt
    $ head -c $(stat -c%s base.txt) DECISION_LOG.md | cmp - base.txt
    (no output)

**The base file is a byte-exact prefix of the merged file.** Nothing
above the append point was reordered, reflowed or rewritten. 1234 lines
→ 1391 lines.

### 4.3 Both entries still separate top-level entries

    1236:## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent
    1326:## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED

    '##' headings from the first new entry to EOF: 2

**Exactly two**, so nothing between them is a `##`; every heading inside
either entry is `###`. **The second did not become a subsection of the
first through the merge** — which was the specific risk A5 names, and it
did not occur.

### 4.4 Entry one, as it stands on the merged head

    ## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent
    
    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: supplies a convention absent from the frozen material
    
    ### Decision
    
    The PI ruling of 2026-08-08, reproduced verbatim:
    
    > **PI ruling, 2026-08-08 — Euclidean exponent mapping.**
    >
    > The canonical interaction expression
    >
    >     X = (G/(2N)) * Sum( bilinear(lam(A), Id4)**2
    >                       + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )
    >
    > is written **as it appears in the Boltzmann exponent**. Equivalently,
    > it enters the Euclidean action with a minus sign:
    >
    >     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
    >
    > Consequently, for a channel whose coefficient in `X` is written
    > `c * J**2`, the Hubbard–Stratonovich coefficient is
    >
    >     g = +2c
    >
    > **Basis, stated exactly.** This is **NOT derived from the frozen
    > material.** The frozen material contains no Euclidean action, no free
    > or kinetic part, and no exponent mapping; the derivation that raised
    > this question searched for one and found none. The ruling is
    > **constrained by executed usage**: `P2-GAP-01` is a PASSed gate whose
    > mean-field treatment introduces a **real** scalar auxiliary field `Σ`,
    > which is admissible only when the scalar channel has `g > 0`. Under
    > the opposite mapping the scalar channel would give `g < 0` and that
    > gate's method would not be available.
    >
    > **This supplies a definition the frozen material never carried. It is
    > not a recovery of an original intent.**
    >
    > **Scope.** This ruling resolves the exponent mapping and nothing else.
    > It selects no Hubbard–Stratonovich channel — that remains `OPEN-AC-1`
    > and is the PI's. It freezes none of the three diquark-definition gaps
    > (`η`, particle–particle Grassmann ordering, diquark normalisation). It
    > reaches no conclusion about a composite vector. It does not by itself
    > re-run any withheld verdict.
    
    ### Reason
    
    The exponent mapping was identified as missing by the channel-character
    derivation, which searched the frozen material for it and found none,
    and therefore withheld two verdicts: `REAL-HS ADMISSIBILITY NOT DEFINED
    BY THE FROZEN MATERIAL` and `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE
    FROZEN MATERIAL`. Both remain withheld until separately recomputed; this
    entry does not re-run them.
    
    The ruling is **constrained by executed usage** rather than derived.
    `P2-GAP-01` is a PASSed gate whose method requires the scalar channel to
    admit a real linear auxiliary field.
    
    **Not a recovery of an original intent** — no document ever stated the
    mapping, and the constraint fixes which of two conventions the programme
    has in fact been using, not which one was once intended.
    
    ### Consequences
    
    For any channel whose coefficient in `X` is `c`, the exponent-level
    Hubbard–Stratonovich coefficient is `g = +2c`. The withheld Layer-1b and
    Layer-2 verdicts of the channel-character derivation become computable;
    computing them is a separate authorized task and is not performed here.
    
    This ruling **selects no Hubbard-Stratonovich channel**. `OPEN-AC-1`
    remains open and is the PI's. The three diquark-definition gaps — `η`,
    the particle–particle Grassmann ordering, and the diquark normalisation
    — are untouched and remain unfrozen.
    
    No gate status changes. `P2-GAP-01` remains `PASS` and `P2-PHASE-01`
    remains `PROPOSED`.
    
    ### Related gate
    
    None. This ruling supplies a convention; it registers no gate and
    changes no gate status.
    
    ### Related branch and files
    
    `fix/exponent-mapping-ruling`;
    `DECISION_LOG.md`,
    `specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

### 4.5 Entry two, as it stands on the merged head

    ## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED
    
    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: opens an unperformed derivation item
    
    ### Decision
    
    The open item, reproduced verbatim:
    
    > **Open derivation item — generator-sum criticality.**
    >
    > `P2-GAP-01` obtained `G_c = 1/(2·I_0)` working from the singlet-only
    > form `L_int = G_N (ψ̄ψ)²`, with `G = 4·G_N`. **The mean-field
    > combinatorics of the full U(N) generator-sum canonical interaction
    > have never been performed**, in that gate or since.
    >
    > **Status: UNESTABLISHED.** Whether `G_c = 1/(2·I_0)` transfers to the
    > canonical generator-sum interaction is not known. **`P2-GAP-01`'s PASS
    > stands for the form it computed**; this item concerns whether that
    > result may be lifted to the canonical form, and it may not be assumed.
    >
    > **Not implied by the exponent ruling.** That `P2-GAP-01`'s real-`Σ`
    > usage constrains the exponent mapping says nothing about whether its
    > `G_c` applies to the generator-sum form. **Treating HS contour
    > consistency as evidence for a gap equation would conflate a convention
    > with a derivation.**
    
    ### Reason
    
    The canonical interaction designated by `CANONICAL_INTERACTION.md` §2 is
    the U(N) generator-sum form `(G/2N) Σ_A [S^A² + P^A²]`. `P2-GAP-01`
    computed its critical coupling from the singlet-only NJL form
    `L_int = G_N(ψ̄ψ)²`. Those are different interactions: the generator sum
    carries `N²` internal channels where the singlet-only form carries one,
    and the mean-field combinatorics that produce the gap equation's
    prefactor have never been carried out for it.
    
    The question this item opens is narrow and dynamical: **does
    `G_c = 1/(2·I_0)` survive the change of interaction?** It is a
    derivation, not a convention, and no ruling can settle it.
    
    ### Consequences
    
    `G_c = 1/(2·I_0)` may not be quoted for the canonical generator-sum
    interaction until the derivation is performed. It remains quotable for
    the form `P2-GAP-01` actually computed.
    
    **`P2-GAP-01`'s gate entry is not edited and its `PASS` is not
    qualified.** The gate passed for the interaction it computed, and that
    remains true; this item records a question about lifting the result, not
    a doubt about it.
    
    Stated once without markup, so the record carries the sentence plainly:
    P2-GAP-01's PASS stands for the form it computed.
    
    ### Related gate
    
    `P2-GAP-01`, whose status is unchanged at `PASS`. This entry registers no
    gate and changes no gate status.
    
    ### Related branch and files
    
    `fix/exponent-mapping-ruling`;
    `DECISION_LOG.md`,
    `specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

**Read cold, the two still stand apart.** Entry two names its subject in
its own heading, states what `P2-GAP-01` computed before saying what is
unknown, and explains the physics gap without invoking the exponent
mapping; its only reference to the ruling is the sentence saying the
ruling does **not** imply it. Entry one ends at its own provenance block
and implies no outstanding qualification.

## 5. A3 — guards

### 5.1 `PRE_MERGE`, at the spec commit, before the merge

    {
      "checks": [
        {
          "condition": "worktree_clean",
          "entries": [],
          "status": "PASS"
        },
        {
          "attachment": "fix/integrate-exponent-mapping-ruling",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "471a7a7b913a38cee106d12fe2cc51f567ddad5e",
          "status": "PASS",
          "worktree_head": "471a7a7b913a38cee106d12fe2cc51f567ddad5e"
        },
        {
          "actual": "481f4ad77cb4ec92ef9d58471530784087e67a43",
          "condition": "merge_base",
          "expected": "481f4ad77cb4ec92ef9d58471530784087e67a43",
          "status": "PASS"
        },
        {
          "condition": "scope",
          "evidence": {
            "base": "481f4ad77cb4ec92ef9d58471530784087e67a43",
            "failures": [],
            "head": "79399dfd26eacb69a0ef0cba8432ec46e2366eea",
            "mode": "exact",
            "observed_operations": [
              {"operation": "modify", "path": "DECISION_LOG.md"},
              {"operation": "add", "path": "reports/2026-08-08T1634Z_exponent-mapping-ruling.md"},
              {"operation": "add", "path": "specs/2026-08-08T1634Z_exponent-mapping-ruling.md"}
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
            {"actual": "17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00",
             "expected": "17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00",
             "path": "derivations/P2-GAP-01_gap_criticality.md", "status": "PASS"},
            {"actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS"},
            {"actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json", "status": "PASS"}
          ],
          "status": "PASS"
        }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }
    === exit 0 ===

`derivations/P2-GAP-01_gap_criticality.md` is pinned in the guard as well
as protected in A6 — the ruling it constrains must not have moved
underneath the merge, and it did not.

### 5.2 The final `POST_MERGE` — intended parameters

**The two roles are representable separately, so no stop arose.**
`merge_guard.post_merge` takes `merge_commit` and `expected_remote_sha`
as independent config keys.

    mode                  POST_MERGE
    merge_commit          d56335b5281ecdf062ce1d615ead0b7b76a8e692   <- the MERGE OBJECT
    expected_parent_1     471a7a7b913a38cee106d12fe2cc51f567ddad5e
    expected_parent_2     79399dfd26eacb69a0ef0cba8432ec46e2366eea
    expected_merge_base   481f4ad77cb4ec92ef9d58471530784087e67a43
    remote_check_policy   REQUIRED
    expected_remote_ref   refs/remotes/origin/main
    expected_remote_sha   <the final REPORT-commit head>              <- a DIFFERENT SHA
    scope_manifest        the A4 manifest below, head = final head
    pinned_artifacts      the same four as the PRE_MERGE guard

`merge_commit` is the merge object; `expected_remote_sha` is the report
commit that will be `main`'s tip. Different commits, different keys. The
executed guard is post-report evidence.

## 6. A6 — protected paths

Read from the objects, base vs merged head:

    GATES.md                                            bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                      2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml                                      9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/CANONICAL_INTERACTION.md                6e5d9e1bb7dffe67e7b9ada026b366ef0e10a2a9   IDENTICAL
    derivations/P2-GAP-01_gap_criticality.md            70b43834873aac435aaed24af70201a9a16b79b7   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md   0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json         5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf   IDENTICAL

Tree OIDs, which cover every path beneath:

    scripts/   4e56b73ecba4f40688bfe1338d77c1641a6b1b5c   IDENTICAL
    results/   70d75be5b5dd18fc1fec0b8435ad425669466333   IDENTICAL
    tests/     f5eb78aaa6a4413a41dab445869800fab4ec6d38   IDENTICAL

**`CONVENTIONS.md` is byte-identical, and the deferred §0(b) index entry
was not anticipated**, checked positively rather than only by blob:

    'exponent' occurrences in CONVENTIONS.md at the merged head:  0
    'S_E = S_E,0' occurrences:                                    0

## 7. A7 — no gate changed

    GATES.md base vs merged head                        IDENTICAL (bd482051…)
    '^## P2-' count at base                             14
    '^## P2-' count at merged head                      14

    ## P2-GAP-01 — Gap-equation criticality (continuum + lattice)
    Status: PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)

    ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    Status: PROPOSED

**`P2-GAP-01` still reads `PASS` with no caveat added.** The open item
that questions lifting its `G_c` to the generator-sum form lives in
`DECISION_LOG.md`, where it belongs; the gate text is untouched. **No
gate, gate status, verdict, digest or hash-pinned artifact was
modified.**

## 8. What was deferred, and stayed deferred

The authority names two follow-up items and forbids performing them
here. **Neither was performed**, and both are restated so the merge does
not bury them:

**(a) The ruling's provenance should be stated more precisely** —
promoting the positive-`G_c` evidence (`1 = 2·G_c·I_0` with `I_0 > 0`
giving `G_c > 0`, against `P2-GAP-01`'s attractive `G > 0` convention) to
the primary constraint, and demoting the real-`Σ` usage to supporting
evidence. **The ruling's epistemic status does not change**: it remains
a PI-supplied convention constrained for consistency by an executed
calculation, not something `P2-GAP-01` proves. No restatement was made
here; entry one stands exactly as reviewed.

**(b) The ruling should be indexed into `CONVENTIONS.md`**, so that a
future executor consulting the convention registry and the freeze files
does not conclude a second time that the exponent mapping is undefined.
**No index entry was added** — §6 verifies `CONVENTIONS.md` unchanged and
free of both `exponent` and `S_E = S_E,0`.

**Also not done, per §5 of the authority:** Layer 1b and Layer 2 were not
re-run and their results are not anticipated anywhere in this report; no
Hubbard–Stratonovich channel was selected; `η`, the particle–particle
Grassmann ordering and the diquark normalisation remain unfrozen.

## 9. A8-pre — seven validators, at head `d56335b5`

    $ python -m pytest tests/test_repository_structure.py        ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py              -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py                -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py            ->  8 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py -> 14 passed              exit 0
    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py  -> 19 passed              exit 0
    $ python -m pytest tests/test_p2_channel_character.py        -> 23 passed              exit 0

All seven exit 0. Exit statuses were captured from `python -m pytest`
itself, not from the tail of a pipeline.

## 10. A4 — scope manifest

`{PUSHED_HEAD}` placeholder so the digest does not depend on the report
commit. SHA-256:
`a1e416f1c602d2fea135ee3f150122db8ed03c924750fc59be50fbab12effdee`.

    {
      "base": "481f4ad77cb4ec92ef9d58471530784087e67a43",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "reports/2026-08-08T1634Z_exponent-mapping-ruling.md"},
        {"operation": "add", "path": "reports/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md"},
        {"operation": "add", "path": "specs/2026-08-08T1634Z_exponent-mapping-ruling.md"},
        {"operation": "add", "path": "specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**4 additions and 1 modification**, matching A4. The `{HHMM}` token
resolved to `1702` at commit 1 and is reused. **There is no sixth path.**

At the pre-report head the report commit does not yet exist, so three
additions appear rather than four:

    M	DECISION_LOG.md
    A	reports/2026-08-08T1634Z_exponent-mapping-ruling.md
    A	specs/2026-08-08T1634Z_exponent-mapping-ruling.md
    A	specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md

    additions: 3   modifications: 1

The authoritative five-operation check at the pushed head is post-report
evidence.

## 11. Worktree states, stated separately

**The merge worktree** — `…/scratchpad/integ5`, attached to
`fix/integrate-exponent-mapping-ruling`, at
`d56335b5281ecdf062ce1d615ead0b7b76a8e692`.
`git status --porcelain=v1` empty after the merge. All merging and all
checks in this report were performed here.

**The main worktree** — `/home/user/2-emergent-gravity`, attached to
`gate/p2-grassmann-crossing-sign` at `cf4c789`. **It was not touched by
this task** beyond read-only `fetch` and `ls-remote`; it reported 0 dirty
entries before the work began and its attachment is unchanged. Local
`main` was not checked out, fast-forwarded or repaired.

**Nine other registered worktrees**, none altered, cleaned or stashed,
all reporting 0 dirty entries at the start of this task:

    …/scratchpad/chan     cb604a4  [gate/p2-channel-character]
    …/scratchpad/expmap   79399df  [fix/exponent-mapping-ruling]
    …/scratchpad/fixA     0ab0ca9  [fix/freeze-checker-sign-repair]
    …/scratchpad/fixB     f2da41a  [fix/branch-deletion-policy]
    …/scratchpad/fixC     1c10637  [fix/branch-deletion-policy-amendment]
    …/scratchpad/integ    9609677  [integration/role-model-clean]
    …/scratchpad/integ2   236f71c  [gate/p2-integrate-fierz-and-sign-ruling]
    …/scratchpad/integ3   eb88a2c  [fix/integrate-freeze-repair-and-deletion-policy]
    …/scratchpad/integ4   481f4ad  [gate/p2-integrate-channel-character-and-audit]

## 12. Stops and clarifications

**Stops: none.** No A1 ref mismatched, the merge did not conflict — in
`DECISION_LOG.md` or anywhere else — the guard did not return `FAIL`, the
append carried zero deletions, and the `POST_MERGE` guard proved able to
carry the merge object and the remote head as distinct values, so A3's
stop condition did not arise.

**Findings: none of my own in this task.** No tool-invocation error, no
observation-method error, and no repository defect surfaced during the
integration.

**Finding 1 — secondary, carried forward by design.** The soft joint in
the ruling's provenance — that `P2-GAP-01` never uses the word "real" of
`Σ`, and never writes the exponent or action sign chain — arrives on
`main` inside the reviewed report, unaltered. It is deferred item (a),
not a defect in what was merged.

**Finding 2 — secondary, carried forward by design.** The exponent
mapping is now a load-bearing input convention that exists only as a
dated log entry. That is deferred item (b). **It is worth noting that
the risk it names is live from the moment this merge lands**: any
derivation started against `main` before (b) is done will search
`CONVENTIONS.md` and the freeze, find nothing, and be right to withhold.
The authority is aware of this and chose the ordering deliberately; I
record it so the window is visible rather than implicit.

**Clarification 1 — where commit 1 sits in §2's sequence.** §2 lists
eight steps and does not name the specification commit; §4 requires it as
commit 1 and A2 requires it to be parent 1. I took it as part of step 1
— create the branch, land the spec — which is the only placement
satisfying both. **I have flagged this on the two previous integrations;
it recurs unchanged.** See §13(b).

**Clarification 2 — which ref was merged.** §5 requires merging the
pinned remote ref rather than a local copy. I merged
`refs/remotes/origin/fix/exponent-mapping-ruling` immediately after
`git fetch --prune`, having confirmed it equals both its `git ls-remote`
value and its pinned SHA.

## 13. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A10 were met as written, and every
dry-run claim held on independent re-derivation.

**(a) A5 is the best-specified criterion in this family of tasks, and I
would reuse it.** It asks for three distinct things about one file —
blob-identical to source, zero deleted lines, entries still separate —
and each is independently checkable. The third in particular targets a
failure a merge could actually cause and a blob comparison alone would
not localise. Most integration specifications check that arriving content
is intact; this one also checks that it is intact *in the right shape*.

**(b) §2's step list and §4's commit order should be one list.**
Clarification 1. Third integration running, unchanged: the specification
commit appears only in §4, so the two orderings must be interleaved by
the reader to be executed. Self-consistent each time, but this is exactly
the shape of the parent-1 defect an earlier integration specification in
this programme actually contained, and the fix is to merge the two lists.

**(c) A4's manifest could assert the append-only property the way the
previous integration's did.** That one wrote `modify: []` so the scope
checker enforced additive-only rather than the report merely observing
it. Here `DECISION_LOG.md` is legitimately modified, so the same trick
does not apply — but nothing in the frozen manifest expresses "and that
modification adds only". A5 carries it in prose and I verified it two
ways, so nothing was lost; it is simply the one property of this merge
that no machine check in the manifest covers.

One thing I would keep exactly as written: **naming the two deferred
items in §0 rather than leaving them to the next specification.** They
are the kind of follow-up that goes missing between tasks, and putting
them in the integration's own specification means they land on `main`
inside a document that is itself merged — which is a more durable place
for them than a report that only the Reviewer reads.

## 14. Commits, and commit-message hygiene

Commits 1–2, at the pre-report head. The report commit's SHA is
necessarily absent from the report it commits; its intended message is
below and its stored message is read back as post-report evidence.

**Commit 1** — `471a7a7b913a38cee106d12fe2cc51f567ddad5e`

    spec: integrate the exponent-mapping ruling

    Records the PI integration authorization, evidence base
    481f4ad77cb4ec92ef9d58471530784087e67a43, transcribed verbatim.

    One merge: two additions and one modification, the modification an
    append to DECISION_LOG.md with zero deleted lines, merge-base the
    original base.

    The specification defers two follow-up items rather than folding them
    into the merge, and names them so they are not lost: restating the
    ruling's provenance to promote the positive-G_c evidence over the
    real-Sigma usage, and indexing the ruling into CONVENTIONS.md so a
    future executor does not conclude again that the exponent mapping is
    undefined. Neither is performed here; CONVENTIONS.md is a protected
    path.

    Layer 1b and Layer 2 are not re-run and their results are not
    anticipated. No Hubbard-Stratonovich channel is selected, no diquark
    convention is frozen, and P2-GAP-01's PASS is not qualified.

**Commit 2 (the merge)** — `d56335b5281ecdf062ce1d615ead0b7b76a8e692`

    merge: integrate the exponent-mapping ruling (reviewed; pinned 79399df)

    Integrates fix/exponent-mapping-ruling at
    79399dfd26eacb69a0ef0cba8432ec46e2366eea into the integration branch.

    Three operations, all reviewed: the task specification, the execution
    report, and an append to DECISION_LOG.md carrying two entries.

    The first entry records the PI ruling that the canonical interaction
    expression is written as it appears in the Boltzmann exponent, so
    S_E = S_E,0 - X and g = +2c. It is recorded as supplying a convention
    the frozen material never carried, constrained for consistency by an
    executed calculation rather than derived from a frozen definition.

    The second entry, separate and top-level rather than a caveat on the
    first, opens the generator-sum criticality item as UNESTABLISHED:
    P2-GAP-01 computed G_c = 1/(2 I_0) from the singlet-only form, and
    whether that lifts to the full U(N) generator sum has never been
    derived. P2-GAP-01's gate entry is untouched and its PASS is not
    qualified.

    The append carries zero deleted lines and the previous file remains a
    byte-exact prefix. Nothing pre-existing is otherwise touched.

    Two follow-up items are deferred by the integration specification and
    not performed here: restating the ruling's provenance around the
    positive-G_c evidence, and indexing the ruling into CONVENTIONS.md.

**Intended report commit message** (commit 3):

    docs: report the integration of the exponent-mapping ruling

    Records A1-A3, A5-A7, A8-pre and A9 for the single merge, with the
    merge commit's parents and merge-base as distinct values, the
    PRE_MERGE guard result, and the intended final manifest and
    POST_MERGE parameters.

    DECISION_LOG.md arrived blob-identical to the source branch, the
    append carries zero deleted lines with the base file a byte-exact
    prefix, and both entries remain separate top-level entries rather
    than one becoming a subsection of the other. CONVENTIONS.md is
    byte-identical and contains neither 'exponent' nor 'S_E = S_E,0', so
    the deferred index entry was not anticipated. GATES.md is unchanged
    at 14 P2 gates and P2-GAP-01 still reads PASS with no caveat.

    Both deferred items are restated so the merge does not bury them.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this
branch — **including the merge commit** — by composing each message in a
file and passing it with `-F`, never `-m`, and never through a path that
would append them.

    commit 1  471a7a7b   spec     suppressed: Co-Authored-By, Claude-Session
    commit 2  d56335b5   MERGE    suppressed: Co-Authored-By, Claude-Session
    commit 3  (report)            suppression applied identically; stored
                                  message read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` returned no match on either form, for both commits.
**No trailer appeared despite inspection, so A9's pre-push STOP did not
trigger.**

**Suppression is a fact disclosed here, not an absence.** The merge
commit in particular — where a generated message would ordinarily be
accepted with `--no-edit` — was given an authored message by file for
exactly this reason.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
