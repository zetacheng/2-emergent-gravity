# Report — `P2-XI-QM2-SCOPE-INTEG` v2: transport of the executed `Q-M2` scope assessment

    Task ID     P2-XI-QM2-SCOPE-INTEG
    Version     v2
    Spec        specs/2026-08-25T0600Z_xi-qm2-scope-integ_v2.md
    Review      reviews/chatgpt/2026-08-25T0600Z_xi-qm2-scope-integ_v2.md
    Base        main @ 08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    Source      science/xi-qm2-scope-01 @
                b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    Fork        0c01fc7f26e91dd84b032dccde0feac61f61d8ea  (measured)
    Branch      science/integrate-xi-qm2-scope-01
    Outcome     COMPLETE through M4. Four contributed paths transported,
                all added; the NON-VACUOUS main-preservation sweep passed
                on all fourteen main-side paths. No abort fired.

This report records `M1` through `M4` and nothing later. It names the tested
tree `T` and **is itself the next commit** on it; it does not state its own
commit SHA, and it does not state `H_integ`. `M5`'s measurements are post-commit
and are recorded in the branch-only addendum.

    T = 736286bb3587822dc0bb1e46620e20005f671d23

**MEASUREMENT UNITS.** Every offset, length, prefix and byte-identity comparison
in this task is performed and reported in bytes, and every byte-identity claim
below states the normalization applied or states that none was.

**Rule 17.** This task transports one executed, reviewed result and adds no
classification the reviewed result did not carry.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    host                     vm
    working directory        /home/user/2-emergent-gravity
    worktree top level       /home/user/2-emergent-gravity
    shallow repository       false
    HEAD before the branch   4afadd0e188874c65133679cc5638046b01a3cf5
                             (science/integrate-xi-qm3-dep-01)
    working tree             clean before the branch was cut

    git checkout -b science/integrate-xi-qm2-scope-01 \
        08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0

## 0a. What v1 stopped on, and what v2 changed

**v1 of this specification STOPPED at `A1` before any write.** Its Source field
named `b133e6aa07d6ea7b7c85f6e3e17cbb0f78ed12f0`, which this repository does not
hold; the measured tip was `b133e6aab8a9f03a2c76345d5bd818898c6a1ab3`, agreeing
only on the first 8 hex characters. No branch was cut, no commit made, and the
measured tip was **not** substituted for the reviewed Source field.

**v2 corrects that one field and nothing else.** Under v2 the source pin is
re-measured here from scratch; **v1's measurements are not inherited as execution
evidence**, and every value below was measured in this run.

## 1. `M1` — pre-merge ref audit, before any write

    git ls-remote origin, full SHAs as returned

    refs/heads/main                             08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    refs/heads/science/xi-qm2-scope-01          b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/xi-qm3-dep-01            d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/integrate-xi-qm3-dep-01  4afadd0e188874c65133679cc5638046b01a3cf5
    refs/heads/science/govdebt-register-gap-01  e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/integrate-xi-qm2-scope-01   (no ref; created here)

The last three are the refs this task must not move; their `M1` values are
recorded here for the `M5` comparison.

**Full-string comparisons, not prefix comparisons:**

    origin/main                       08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    spec Base                         08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
                                      EQUAL

    source tip                        b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    spec Source                       b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
                                      EQUAL, all 40 hex characters

    git rev-parse --disambiguate=b133e6aa
      b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
                                      exactly one object carries that
                                      abbreviation, and it is the tip

    git merge-base main <source>      0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    the value the spec requires       0c01fc7f26e91dd84b032dccde0feac61f61d8ea
                                      EQUAL  =>  the source does NOT descend
                                                 from the Base

    git rev-list --count Base..source    4
    git rev-list --count source..Base   16

**`A1` did not fire. `C1` PASS on all three limbs.** The equality of the source
tip and the Source field was established by comparing full 40-character strings;
**no abbreviation-based substitution was made.** The repository is non-shallow,
so both suite runs are on a valid substrate. The source is 16 commits behind the
Base and 4 ahead of the fork, so `M3b(c)` is non-vacuous.

## 1b. `M1b` — pre-execution provenance commits, before the merge

**Rule 18 and Amendment N.** The review carries the line
`**Reviewed specification SHA-256:**` — PRESENT — at its lines 4 and 182,
identically, and

    043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6

is the only 64-hex string it contains. **This review is the v2 authority; the v1
review artifact does not authorize v2**, and the v1 binding digest
`3eb76e9e…` appears nowhere in it. Measured **before** the specification commit,
and re-measured over the committed bytes afterwards:

    sha256 of the spec file, before the commit
      043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6
    the digest the review declares itself bound to
      043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6
    sha256 of the committed bytes
      043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6

The review artifact has no pre-committed hash. Its sha256 is recorded at commit
as its first recorded digest,

    438165c849bf97cb443b3d1e211a5eb107a67ed52f32464807feaf4650a0a6a1

provenance transmitted by the PI in session. Verdict `APPROVE FOR EXECUTION`.

**Commit order, spec then review, nothing between them:**

    86db217f2e18af1f097c388b0ea8681d81f4041c  spec(P2-XI-QM2-SCOPE-INTEG): v2, ...
    634aed0520a50f0ef1f840fe93b0270fad5e8ca6  review(P2-XI-QM2-SCOPE-INTEG): ...

    M1b tip                            634aed0520a50f0ef1f840fe93b0270fad5e8ca6
    git rev-list --count Base..M1b tip 2

**Reviewer determinations, recorded as issued and not restated:**

    Source pin defect         RESOLVED
    Base / fork topology      CONSISTENT
    M3 manifest / digests     PRESERVED
    M3c classification audit  PRESERVED
    Q-M2 authority boundary   PRESERVED
    Protocol closure          PASS

## 2. `M2` — merge construction

    git merge --no-ff <source tip>   on the M1b tip

    M_merge    424cd41212c47017132efd886cc64d76e4a02728
    parent 1   634aed0520a50f0ef1f840fe93b0270fad5e8ca6   (the M1b tip)
    parent 2   b133e6aab8a9f03a2c76345d5bd818898c6a1ab3   (the source tip)

    Merge made by the 'ort' strategy.
    4 files changed, 1475 insertions(+)
    git status --porcelain after the merge: empty

**The merge was conflict-free.** `A2` did not fire on this limb. `M_merge` has
exactly two parents, and they are the two the spec names. **`C2` PASS on all
three limbs.**

## 3. `M3` — arriving-blob verification, from the merge product

Every digest re-measured from the merge product, not from the source tip and not
inherited from v1's pre-write measurements. Four of four match.

    path      derivations/P2-XI-QM2-SCOPE-01_condensate-loop-input-scope.md
    expected  3ce0215db7ed61103b3074ae23567ca77760f07af586c052aef2e3d2095110ae
    measured  3ce0215db7ed61103b3074ae23567ca77760f07af586c052aef2e3d2095110ae

    path      specs/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
    expected  680248e8deada3e1d77df13ee1f5f8899ddb3084e76db71f4c052ce7ff07fb87
    measured  680248e8deada3e1d77df13ee1f5f8899ddb3084e76db71f4c052ce7ff07fb87

    path      reviews/chatgpt/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
    expected  f22397a0d5d52fdca3ff828e113e66b107f64c245f2af772b3d3bb849bf566cb
    measured  f22397a0d5d52fdca3ff828e113e66b107f64c245f2af772b3d3bb849bf566cb

    path      reports/2026-08-29T1825Z_xi-qm2-scope-01.md
    expected  98d6bbc9a8b7c4b83b15836b1c114a8a24afae2e8c1802f6c45b8d5ddaa49830
    measured  98d6bbc9a8b7c4b83b15836b1c114a8a24afae2e8c1802f6c45b8d5ddaa49830

    mismatches: 0

`A2` did not fire on its second limb. **`C3` PASS.**

## 3b. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK = the merge-base measured at M1 = 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    BASE                                 = 08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    SRC                                  = b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    PROD = M_merge                       = 424cd41212c47017132efd886cc64d76e4a02728

### `M3b(a)` — the contributed path set

`git diff --name-status FORK..<source>`, verbatim:

    A	derivations/P2-XI-QM2-SCOPE-01_condensate-loop-input-scope.md
    A	reports/2026-08-29T1825Z_xi-qm2-scope-01.md
    A	reviews/chatgpt/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
    A	specs/2026-08-24T1500Z_xi-qm2-scope-01_v2.md

    exactly four entries                                true
    every status is A — no M, D or R appears            true
    the path set equals the four-path manifest of §1a   true

**`A5` does not fire on `(a)`.** The set is §1a's four-path all-`A` manifest
exactly. **There is no modified path in this change set**, so the protocol's
modified-path structural limb is absent rather than carried over empty.

### `M3b(b)` — union classification

`P_source` (`FORK..source`) is the four-entry set above.
`P_main` (`FORK..Base`), verbatim:

    A	derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
    M	docs/GOVERNANCE-DEBT.md
    A	reports/2026-08-29T1715Z_govdebt-register-gap.md
    A	reports/2026-08-29T1811Z_xi-qm3-dep-01.md
    A	reports/2026-08-29T1843Z_govdebt-register-gap-integ.md
    A	reports/2026-08-30T1354Z_xi-qm3-dep-integ.md
    A	reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    A	reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
    A	reviews/chatgpt/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    A	reviews/chatgpt/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
    A	specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    A	specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
    A	specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    A	specs/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md

    |P_source| 4    |P_main| 14    |P_union| 18

**Fourteen main-side changed paths, as §0a expected. The expectation is recorded
as met; the measurement above is what binds.**

Each path of `P_union` classified into exactly one class:

    (1,0) source-only    4
    (0,1) main-only     14
    (1,1) both-changed   0     = P_overlap
    (0,0)                0     (does not occur within P_union)

**`(1,0)`: the product blob must equal the source's.** Measured pairwise, blob
ids in full:

    derivations/P2-XI-QM2-SCOPE-01_condensate-loop-input-scope.md
      product 177468e88f21851d6c15676f60480791af647f26   source 177468e88f21851d6c15676f60480791af647f26
    reports/2026-08-29T1825Z_xi-qm2-scope-01.md
      product 55371786a3dc0aa0eaba6b7b59ed4356aaf9d7b3   source 55371786a3dc0aa0eaba6b7b59ed4356aaf9d7b3
    reviews/chatgpt/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
      product 9589ef12d904dce3b7f0aaaf2ddd30524e8297cb   source 9589ef12d904dce3b7f0aaaf2ddd30524e8297cb
    specs/2026-08-24T1500Z_xi-qm2-scope-01_v2.md
      product 211f6851a4c187732dfa1f12dd48906fc1a1c61b   source 211f6851a4c187732dfa1f12dd48906fc1a1c61b

    all four equal — PASS

**`(0,1)`: the product blob must equal the Base's.** All fourteen measured
pairwise and equal; the pairs are reproduced in full at `M3b(c)`, which sweeps
the same set.

    (1,1) P_overlap : EMPTY, measured over the classified union and not
                      inferred from fork distance
    (0,0)           : 0

**`A5` does not fire on `(b)`.**

### `M3b(c)` — main-preservation sweep, NON-VACUOUS

    paths in P_main \ P_source : 14

**This is the sweep that protects the `G-18` governance-debt entry, the `Q-M3`
check's artifact and its constructive-gap finding, and both preceding
integrations' records — all landed on main after the source forked.** Every pair
measured; blob ids in full:

    derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
      product bb438a909bd8ba855a3524a2caf73e3cf52f6f86   base bb438a909bd8ba855a3524a2caf73e3cf52f6f86
    docs/GOVERNANCE-DEBT.md
      product f6a813ee84f1b166b3fbbf73d48a2c7c03965f85   base f6a813ee84f1b166b3fbbf73d48a2c7c03965f85
    reports/2026-08-29T1715Z_govdebt-register-gap.md
      product d7a35c0df0cf729df918f45737f9afaa420b5566   base d7a35c0df0cf729df918f45737f9afaa420b5566
    reports/2026-08-29T1811Z_xi-qm3-dep-01.md
      product c9c184f05e48ffb3e6b4027f7703da485f606eee   base c9c184f05e48ffb3e6b4027f7703da485f606eee
    reports/2026-08-29T1843Z_govdebt-register-gap-integ.md
      product dba8ced709f95cb8da5097047477c5fb26a556c3   base dba8ced709f95cb8da5097047477c5fb26a556c3
    reports/2026-08-30T1354Z_xi-qm3-dep-integ.md
      product 7b4ba2f8f3403b22658c1b94baaeccb174ee9755   base 7b4ba2f8f3403b22658c1b94baaeccb174ee9755
    reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
      product ebee1bcfd59802fb00e0f914d4d8cbd5ec1f42b7   base ebee1bcfd59802fb00e0f914d4d8cbd5ec1f42b7
    reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product b03ce1f48a7904b7416775deeefd13b87524a0e4   base b03ce1f48a7904b7416775deeefd13b87524a0e4
    reviews/chatgpt/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
      product 85413004e371a54428e2802bf9727f489609dfc6   base 85413004e371a54428e2802bf9727f489609dfc6
    reviews/chatgpt/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
      product 979d757c3e9f4975366e7f4a118366b058f235df   base 979d757c3e9f4975366e7f4a118366b058f235df
    specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
      product 6aee5b2882a7a021bce17454985553c3e6fc8b8f   base 6aee5b2882a7a021bce17454985553c3e6fc8b8f
    specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e   base 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e
    specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
      product 8d1e9d83f359c990021e9c5f963b38ccb259f258   base 8d1e9d83f359c990021e9c5f963b38ccb259f258
    specs/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
      product bd40f5e96f797b10af0849aa4d2eaceb742b29ce   base bd40f5e96f797b10af0849aa4d2eaceb742b29ce

    fourteen of fourteen equal — PASS. No inequality; A5 does not fire.

**`C3b` PASS on every limb.**

## 3c. `M3c` — arrival-state verification of the classification

**MEASUREMENT SUBSTRATE, stated.** Probes are built from the artifact's bytes —
27093 bytes, 573 lines, read from the merge product — decoded as UTF-8 and split
on newlines. The scan tracks fenced-block state, so a line inside a ``` fence is
quoted text and not structure. The artifact carries no blockquote prefixes on its
own declarations and none is stripped. **Emphasis wrapping is not assumed
anywhere**: every marker is matched against the line's actual leading bytes. **No
character-offset arithmetic is used.**

### `(i)` ENUMERATION — performed FIRST, before any outcome was tested

**The rule is taken from the artifact's own landed structure, not from
judgement.** The artifact declares at `:211`:

```text
**Each input carries exactly one of four mutually exclusive outcomes.** No
```

and carries two explicit structural markers: an input heading and an outcome
declaration line.

**THE ENUMERATION RULE.** An INPUT is a line matching ``^### `I-<n>` — ``
outside any fenced block; its OUTCOME DECLARATION is the first line matching
``^**Outcome: `...`.**`` after that heading and before the next input heading,
also outside any fenced block.

**THE ENUMERATED SET — 9 inputs**, with the line each heading resolves at:

    :216  ### `I-1` — the condensate scalar's own curvature coupling `ξ_χ`
    :249  ### `I-2` — the functional-measure inheritance
    :265  ### `I-3` — how the `O(1)`-versus-`O(N)` counting enters the normalization chain
    :291  ### `I-4` — the scalar species' heat-kernel data and the `β_s` prefactor rule
    :320  ### `I-5` — the mass at which the scalar species enters, and the `L` treatment
    :365  ### `I-6` — the `Z` convention the result is stated in
    :400  ### `I-7` — non-overlap with what the landed chain already contains
    :451  ### `I-8` — which ξ observable the result would be a contribution to
    :471  ### `I-9` — the scalar species' `β_s` as a function of its ξ

    COUNT: 9

    every input identifier is distinct                      PASS
    the identifiers run I-1..I-9 with no gap                PASS

**The enumeration rule was stateable from the artifact's own structure, so the
`A5` case for an unstateable rule did not arise and nothing was enumerated by
judgement.**

### `(ii)` ONE OUTCOME EACH — tested only after the enumeration above

The per-input assignment, measured; **normalization applied: NONE.**

    input   line   outcome, verbatim from the declaration
    --------------------------------------------------------------------------
    I-1     :225   REQUIRING A PI RULING
    I-2     :257   LANDED — NOT DETERMINABLE
    I-3     :274   REQUIRING A PI RULING
    I-4     :299   LANDED
    I-5     :329   REQUIRING A PI RULING
    I-6     :374   LANDED
    I-7     :408   ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE
    I-8     :458   REQUIRING A PI RULING
    I-9     :479   DERIVABLE

    every input has exactly one outcome declaration, and it parses    PASS
    every outcome is drawn from the fixed vocabulary                  PASS
    the outcome count equals the input count                          PASS

**The vocabulary used as the test set is the landed one the arriving
specification fixes**, not a taxonomy inferred here:

    LANDED
    LANDED — NOT DETERMINABLE      the landed-status specialization of LANDED
    DERIVABLE
    REQUIRING A PI RULING
    ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE

**Note on the label count, per the Reviewer's §20.** Five labels appear because
`LANDED — NOT DETERMINABLE` is the landed-status specialization the arriving
specification's `COND-S` defines, not a fifth category. **The architecture is not
reinterpreted here from the natural-language numeral**: the test was against the
landed vocabulary, and no consolidation or re-derivation of the categories was
performed.

Distribution, measured from the table above:

    LANDED — NOT DETERMINABLE                       1   I-2
    LANDED                                          2   I-4, I-6
    DERIVABLE                                       1   I-9
    REQUIRING A PI RULING                           4   I-1, I-3, I-5, I-8
    ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE  1   I-7

### `(iii)` THE PI-FACING RETURNS

**Reconstructed from `(i)`'s enumeration, not read off the artifact's list:**

    REQUIRING A PI RULING                           I-1, I-3, I-5, I-8
    ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE  I-7

The artifact's own list is present at `:510`, with the two outcomes in separate
subsections:

```text
## 4. `M4` — the routed list, this artifact's return to the PI
```

```text
### 4a. `REQUIRING A PI RULING`
```

```text
### 4b. `ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE`
```

    the artifact's own 4a list   I-1, I-3, I-5, I-8
    the artifact's own 4b list   I-7

    4a equals the enumeration's REQUIRING A PI RULING set        PASS
    4b equals the enumeration's ROUTED TO PI set                 PASS
    the two lists are disjoint                                   PASS
    together they are the five PI-facing returns                 PASS

**The two outcomes remain distinguishable in the list**, in separate subsections
with their outcome names as headings. **Transport does not collapse them into a
generic needs-PI bucket**, and this task does not answer, recommend on, order or
prioritise any of the five.

### `(iv)` DISCIPLINE STATEMENTS — five, each quoted

Each matched as a byte substring; **normalization applied: NONE.**

`:17`

```text
**This artifact proposes nothing.**
```

`:24`

```text
**Every routed question below is recorded, none is answered here, and a
question being listed is not evidence about its answer.**
```

`:33`

```text
    COND-D  FUNCTIONAL-MEASURE STATUS.
```

`:39`

```text
    COND-S  STATUS, NOT VALUE.
```

`:48`

```text
    COND-E  ENUMERATION IS NOT EXHAUSTION.
```

**POSITIVE CONTROL for the substring method used above**, so the results are
distinguishable from a dead probe: by the same method, a string known present is
FOUND (`## 4. `M4` — the routed list`) and a string known absent is NOT FOUND
(`THIS STRING IS NOT IN THE ARTIFACT`).

**`M3c` PASS on all four checks. `C3c` PASS.**

## 4. `M4` — suite

Run on a full, non-shallow tree. **The arriving task added no tests; the
criterion is regression, not a count.**

**At the base**, tree `0127f491f9f5fd332f7c34a180fc8851ce2df21d`:

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 49.69s

**At the post-merge integration tree**, which is the tested tree:

    T = 736286bb3587822dc0bb1e46620e20005f671d23   (the tree of M_merge)

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 41.79s

Identical outcomes. **No test fails on `T` that passes at the base. `C4` PASS.**

**This report is the next commit on the tested tree above.**

---

## 5. Acceptance criteria

    C1  PASS  origin/main equals the Base; the merge-base equals 0c01fc7f… as a
              full-string match; the source tip equals the Source field as a
              full 40-character string.
    C2  PASS  M_merge has exactly two parents, the M1b tip and the source tip;
              the M1b tip descends from the base by exactly two commits, spec
              then review; the spec's sha256 equals the digest the review
              declares, recorded at M1b.
    C3  PASS  Four of four digests equal their expected values, as full-string
              matches, re-measured from the merge product.
    C3b PASS  The contributed set is the four-path all-A manifest; the union
              classification assigns each of the eighteen P_union paths to
              exactly one class with its blob rule satisfied; P_overlap is empty
              as measured over the classified union; the main-preservation sweep
              records product blob equal to Base blob for all fourteen swept
              paths, pairwise.
    C3c PASS  (i)'s enumeration rule, enumerated set and count are recorded
              BEFORE any outcome is tested; (ii)'s per-input table shows exactly
              one outcome per input, each from the landed vocabulary; (iii)'s
              PI-facing list matches the enumeration and keeps the two outcomes
              distinguishable; (iv)'s five statements are quoted; and each check
              states its normalization.
    C4  PASS  344 passed and 2 deselected at the base and at T.
    C5  NOT YET REACHED at this commit. Its limbs are post-commit and post-push
              and are recorded in the branch-only M5 addendum.

## 6. Abort conditions

    A1  DID NOT FIRE.  Every M1 value agrees with the spec's Base, Source and
        stated merge-base relation, as full-string matches. Under v1 this
        condition DID fire and execution stopped before any write; v2's
        corrected Source field is what passes here, and the tip was re-measured
        rather than assumed from that stop.
    A2  DID NOT FIRE.  The merge was conflict-free and M3 found no digest
        mismatch in the merge product.
    A3  EVALUATED AT PUSH TIME.  main stands at the Base, which is the first
        parent's ancestor and H_integ's ancestor, so the advance is expected to
        be a fast-forward; the measurement is made at push and recorded in the
        M5 addendum.
    A4  DID NOT FIRE.  No file arriving from the source was modified and no ref
        of the source branch moved. No outcome is restated, upgraded, resolved
        or glossed — §3c quotes each declaration and adds nothing;
        LANDED — NOT DETERMINABLE is not treated as a value obtained, and
        ROUTED TO PI is not treated as an unclassified input; none of the five
        PI-facing returns is answered, recommended on, ordered or prioritised;
        the Q-M2 row and the ledger are untouched and are in neither P_source
        nor P_main; the assessment is not presented as membership evidence; and
        the bounding computation is not begun, designed, scoped or scheduled.
        DET-01, OPEN-AC-2, Q-M1, the truncation order I-7 turns on, and the
        registered representation-stability inquiry are all untouched.
    A5  DID NOT FIRE.  No contributed path or status outside §1a's manifest, no
        both-changed path, no source-unchanged path whose product blob differs
        from the Base's, no main-unchanged contributed path whose product blob
        differs from the source's, and no M3c failure: the enumeration rule was
        stateable from the artifact's structure, no input carried none or two
        outcomes, and every negative result in §3c carries a live positive
        control.

## 7. What arrives, stated as the arriving bytes state it

**Nine inputs, each carrying exactly one outcome**, quoted at §3c(ii) from the
merge product and not paraphrased.

**Five inputs are returned to the PI, in two distinct categories** — four
`REQUIRING A PI RULING` and one `ROUTED TO PI — CLASSIFICATION NOT
DETERMINABLE`. **They arrive unanswered and unranked.**

**`Q-M2` remains an OPEN ledger row.** The ledger artifact is in neither this
task's contributed set nor `P_main`, so it is untouched by this transport. **The
scope assessment is not the evidence `P2-XI-RULINGS-02` Ruling 1 awaits**, and
this task does not present it as such.

**The bounding computation remains unauthorized.** Ruling 3 reserves it to a
separate later task, and nothing here begins, designs, scopes or schedules it.

**`COND-D`, `COND-E` and `COND-S` arrive intact**, quoted at §3c(iv), together
with the artifact's statements that it proposes nothing and that listing a
question is not evidence about its answer.

## 8. Stops and clarifications (Amendment B)

Nothing stopped execution in this run. One observation is carried forward.

### 8a. The v1 stop, and what it cost

**Category: `SPECIFICATION_DEFECT`, already resolved by the PI in v2 and
recorded here for the chain's record.** v1's Source field was a full SHA
completed from an abbreviation without being measured. It named no object this
repository holds, and `A1` fired before any write.

**The cost was one re-review cycle and nothing else.** No branch was cut, no
commit made, no ref moved, and the measured tip was not substituted for the
reviewed field — a Source field is the reviewed authority for *which commit* is
transported, so replacing it at execution time would have executed an unreviewed
specification. v2 corrected the one field, and this run re-measured the pin from
scratch rather than inheriting v1's pre-write measurements.

**The general fault is worth carrying forward:** an abbreviated SHA in a report
or an execution summary is a *display* of a measurement, not the measurement. A
downstream document that needs the full value must re-measure it, never complete
it. This is the same discipline the three preceding tasks recorded for probes —
read the bytes, then write — applied to object names rather than file contents.

## 9. Rule 22

No result in this task is `INCONCLUSIVE`. The arriving artifact's
`ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE` is a classification, not an
inconclusive result — the arriving specification says so, and §3c(ii) verifies it
as one of the fixed vocabulary's values. **This task issues no verdict of its own
and owes no subclass or resolution path.**

## 10. Environment

    python      3.11.15
    pytest      9.1.1
    numpy       2.4.6
    sympy       1.14.0
    ruff        0.15.8
    scipy       ABSENT
    repository  non-shallow, verified before each suite run

No environment repair was needed and none was performed.

## 11. Push scope

`docs/BRANCHING_POLICY.md` `science/*` scope, integration case: during landing
**only the integration branch and `refs/heads/main` may be pushed**, main
advances by fast-forward only, and the source branch, session branches and
unrelated refs must not move.

    to be pushed   refs/heads/science/integrate-xi-qm2-scope-01
                   refs/heads/main, fast-forward to H_integ
    must not move  refs/heads/science/xi-qm2-scope-01
                   refs/heads/science/xi-qm3-dep-01
                   refs/heads/science/integrate-xi-qm3-dep-01
                   refs/heads/science/govdebt-register-gap-01
                   refs/heads/science/integrate-govdebt-register-gap
                   refs/heads/science/xi-clar-01-landing
                   refs/heads/science/xi-ledger-01
                   refs/heads/science/integrate-xi-clar-01
                   any session or harness branch

`M5`'s measurements — `H_integ`, the diff of `H_integ` against `T`, the push
results and the post-push ref audit — are post-commit and go into the addendum
commit on the integration branch only. `origin/main` remains at `H_integ`.

END OF REPORT

---

# ADDENDUM — `M5`, post-push. BRANCH-ONLY.

**This section exists only on `science/integrate-xi-qm2-scope-01`. It is not on
`main`, and `origin/main` remains `H_integ`.** Everything below was measured
after the report commit above, so it could not have been inside it.

    H_integ   4a99e81ad16322e1152286df0158b648b75d18f3

## `C5` first limb — `H_integ` against the tested tree

    git diff --name-status 736286bb3587822dc0bb1e46620e20005f671d23 H_integ
    A	reports/2026-08-30T1647Z_xi-qm2-scope-integ.md

**Exactly one path, the report artifact.** Measured, not asserted; re-measured
after the push against `origin/main` with the same single-path result.

## `A3` and the push order

`A3` was evaluated before the main push, as a measurement:

    git merge-base --is-ancestor origin/main H_integ   ->  0
    origin/main at that moment  08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0

`origin/main` was an ancestor of `H_integ`, so the advance is a fast-forward and
**`A3` did not fire.**

Push order executed, integration branch first, then `main`:

    git push -u origin science/integrate-xi-qm2-scope-01
      * [new branch]      science/integrate-xi-qm2-scope-01 -> science/integrate-xi-qm2-scope-01

    git push origin 4a99e81ad16322e1152286df0158b648b75d18f3:refs/heads/main
      08b46fb..4a99e81  4a99e81ad16322e1152286df0158b648b75d18f3 -> main

`main` was advanced to **`H_integ`**, not to `M_merge` (`424cd412…`).

## Post-push ref audit

    refs/heads/main                                    4a99e81ad16322e1152286df0158b648b75d18f3
    refs/heads/science/integrate-xi-qm2-scope-01       4a99e81ad16322e1152286df0158b648b75d18f3
    refs/heads/science/xi-qm2-scope-01                 b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/xi-qm3-dep-01                   d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/integrate-xi-qm3-dep-01         4afadd0e188874c65133679cc5638046b01a3cf5
    refs/heads/science/govdebt-register-gap-01         e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/integrate-govdebt-register-gap  963563ad16d6b289a53d8480d420a9aaac6a15a7
    refs/heads/science/xi-clar-01-landing              0b3c85cb158f6aae2dd661054d66bcd1f986878f
    refs/heads/science/xi-ledger-01                    0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    refs/heads/science/integrate-xi-clar-01            37a2f411ea1166134b3c153e15aab74af3f79bf6

    origin/main equals H_integ                                       PASS
    origin/main is NOT M_merge                                       PASS
    the integration branch equals H_integ                            PASS
    science/xi-qm2-scope-01 unmoved from its M1 value                PASS
    science/xi-qm3-dep-01 unmoved from its M1 value                  PASS
    science/integrate-xi-qm3-dep-01 unmoved from its M1 value        PASS
    science/govdebt-register-gap-01 unmoved from its M1 value        PASS
    science/integrate-govdebt-register-gap unmoved                   PASS
    science/xi-clar-01-landing unmoved                               PASS
    science/xi-ledger-01 unmoved                                     PASS
    science/integrate-xi-clar-01 unmoved                             PASS

**`C5` PASS on every limb.** The source branch did not move; no session, harness
or unrelated ref moved. The only two refs this task moved are the two the
specification authorizes.

**This addendum commit is pushed to `science/integrate-xi-qm2-scope-01` only.**
`origin/main` stays at `H_integ`; the addendum's own SHA is measured after this
commit and is returned outside the repository, not written back into it.

END OF ADDENDUM
