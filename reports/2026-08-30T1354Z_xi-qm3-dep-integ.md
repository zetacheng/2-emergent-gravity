# Report — `P2-XI-QM3-DEP-INTEG` v2: transport of the executed `Q-M3` dependence check

    Task ID     P2-XI-QM3-DEP-INTEG
    Version     v2
    Spec        specs/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
    Review      reviews/chatgpt/2026-08-25T0000Z_xi-qm3-dep-integ_v2.md
    Base        main @ 1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    Source      science/xi-qm3-dep-01 @
                d55b6350a015d124f723d1fceb75b77cdcc112a9
    Fork        0c01fc7f26e91dd84b032dccde0feac61f61d8ea  (measured)
    Branch      science/integrate-xi-qm3-dep-01
    Outcome     COMPLETE through M4. Four contributed paths transported,
                all added; the NON-VACUOUS main-preservation sweep passed
                on all seven main-side paths. No abort fired.

This report records `M1` through `M4` and nothing later. It names the tested
tree `T` and **is itself the next commit** on it; it does not state its own
commit SHA, and it does not state `H_integ`. `M5`'s measurements are post-commit
and are recorded in the branch-only addendum.

    T = 157e695b068893613ace3fb852354fc1577fce55

**MEASUREMENT UNITS.** Every offset, length, prefix and byte-identity comparison
in this task is performed and reported in bytes, and every byte-identity claim
below states the normalization applied or states that none was.

**Rule 17.** This task transports one executed, reviewed result and adds no
classification the reviewed result did not carry. **No dependence verdict was
returned by the arriving task, and none is stated, implied or summarised here.**

---

## 0. Execution location and worktree identity (Amendment D step 0)

    host                     vm
    working directory        /home/user/2-emergent-gravity
    worktree top level       /home/user/2-emergent-gravity
    shallow repository       false
    HEAD before the branch   963563ad16d6b289a53d8480d420a9aaac6a15a7
                             (science/integrate-govdebt-register-gap)
    working tree             clean before the branch was cut

    git checkout -b science/integrate-xi-qm3-dep-01 \
        1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841

## 1. `M1` — pre-merge ref audit, before any write

    git ls-remote origin, full SHAs as returned

    refs/heads/main                                    1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    refs/heads/science/xi-qm3-dep-01                   d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/xi-qm2-scope-01                 b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/govdebt-register-gap-01         e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/integrate-govdebt-register-gap  963563ad16d6b289a53d8480d420a9aaac6a15a7
    refs/heads/science/integrate-xi-qm3-dep-01         (no ref; created here)

The last three are the refs this task must not move; their `M1` values are
recorded here for the `M5` comparison. **`science/integrate-govdebt-register-gap`
stands at its `M5` addendum commit `963563ad`, not at `main`'s tip** — that is
its state, and it is what the `M5` comparison uses.

**Full-string comparisons, not prefix comparisons:**

    origin/main                       1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    spec Base                         1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
                                      EQUAL

    source tip                        d55b6350a015d124f723d1fceb75b77cdcc112a9
    spec Source                       d55b6350a015d124f723d1fceb75b77cdcc112a9
                                      EQUAL

    git merge-base main <source>      0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    the value the spec requires       0c01fc7f26e91dd84b032dccde0feac61f61d8ea
                                      EQUAL  =>  the source does NOT descend
                                                 from the Base

    git rev-list --count Base..source   4
    git rev-list --count source..Base   8

**`A1` did not fire. `C1` PASS.** The repository is non-shallow, so both suite
runs are on a valid substrate. The source is 8 commits behind the Base and 4
ahead of the fork, so `M3b(c)` is non-vacuous.

## 1b. `M1b` — pre-execution provenance commits, before the merge

**Rule 18 and Amendment N.** The review carries the line
`**Reviewed specification SHA-256:**` — PRESENT — at its lines 4 and 83, and
states the same digest inline at its line 10. That digest,

    f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfbae9f613ab904df0

is the only 64-hex string it contains. Measured **before** the specification
commit, and re-measured over the committed bytes afterwards:

    sha256 of the spec file, before the commit
      f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfbae9f613ab904df0
    the digest the review declares itself bound to
      f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfbae9f613ab904df0
    sha256 of the committed bytes
      f354716a4a90b237f3a0246cdb1ebd6870b3e0730c457fcfbae9f613ab904df0

The review artifact has no pre-committed hash. Its sha256 is recorded at commit
as its first recorded digest,

    1d1036dd9542d285b9860ca2c3d3264a46d04ad87ecbd44cec9af3109ed032b4

provenance transmitted by the PI in session. Verdict `APPROVE FOR EXECUTION`.

**Commit order, spec then review, nothing between them:**

    aa7c6720a84560d452afb3365734ffe764fd6424  spec(P2-XI-QM3-DEP-INTEG): v2, ...
    c9a7f467e112941bffdb35a5ddaffa844f28e125  review(P2-XI-QM3-DEP-INTEG): ...

    M1b tip                            c9a7f467e112941bffdb35a5ddaffa844f28e125
    git rev-list --count Base..M1b tip 2

**Reviewer determinations, recorded as issued and not restated:**

    Transport scope           PRESERVED
    Early-return semantics    PRESERVED
    Q-M3 OPEN status          PRESERVED
    Stale-source protocol     CONCUR
    M3c assertion domain      CLOSED
    M3c verdict enumeration   CLOSED
    Negative-check discipline PASS

## 2. `M2` — merge construction

    git merge --no-ff <source tip>   on the M1b tip

    M_merge    3e5ab10f0b122dda21e4085e35b5f412d24e1afd
    parent 1   c9a7f467e112941bffdb35a5ddaffa844f28e125   (the M1b tip)
    parent 2   d55b6350a015d124f723d1fceb75b77cdcc112a9   (the source tip)

    Merge made by the 'ort' strategy.
    4 files changed, 1386 insertions(+)
    git status --porcelain after the merge: empty

**The merge was conflict-free.** `A2` did not fire on this limb. `M_merge` has
exactly two parents, and they are the two the spec names. **`C2` PASS on all
three limbs.**

## 3. `M3` — arriving-blob verification, from the merge product

Every digest re-measured from the merge product, not from the source tip, and
recorded in full. Four of four match.

    path      derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
    expected  1729136c9579198e118adff74246f42f9cdb1ed164e1dd37030893e6297049ea
    measured  1729136c9579198e118adff74246f42f9cdb1ed164e1dd37030893e6297049ea

    path      specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    expected  0fab1fdc58612bfd44971b2d7fef842ce4db4a9ca1ec86fdc926767ce31ebfaa
    measured  0fab1fdc58612bfd44971b2d7fef842ce4db4a9ca1ec86fdc926767ce31ebfaa

    path      reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    expected  a2c462b9cc465252934d2bfb2288c50dc628ccc11854bf44099c05fc72d46837
    measured  a2c462b9cc465252934d2bfb2288c50dc628ccc11854bf44099c05fc72d46837

    path      reports/2026-08-29T1811Z_xi-qm3-dep-01.md
    expected  e5770d21b15efcfb040bf8fbc3254167a1e8bbb814967b4da2371cbb92e8da3e
    measured  e5770d21b15efcfb040bf8fbc3254167a1e8bbb814967b4da2371cbb92e8da3e

    mismatches: 0

`A2` did not fire on its second limb. **`C3` PASS.**

## 3b. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK = the merge-base measured at M1 = 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    BASE                                 = 1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    SRC                                  = d55b6350a015d124f723d1fceb75b77cdcc112a9
    PROD = M_merge                       = 3e5ab10f0b122dda21e4085e35b5f412d24e1afd

### `M3b(a)` — the contributed path set

`git diff --name-status FORK..<source>`, verbatim:

    A	derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
    A	reports/2026-08-29T1811Z_xi-qm3-dep-01.md
    A	reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
    A	specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md

    exactly four entries                                true
    every status is A — no M, D or R appears            true
    the path set equals the four-path manifest of §1a   true

**`A5` does not fire on `(a)`.** The set is §1a's four-path all-`A` manifest
exactly. **There is no modified path in this change set**, so the modified-path
structural limb of the protocol this task instantiates does not apply here and
is absent rather than carried over empty.

### `M3b(b)` — union classification

`P_source` (`FORK..source`) is the four-entry set above.
`P_main` (`FORK..Base`), verbatim:

    M	docs/GOVERNANCE-DEBT.md
    A	reports/2026-08-29T1715Z_govdebt-register-gap.md
    A	reports/2026-08-29T1843Z_govdebt-register-gap-integ.md
    A	reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
    A	reviews/chatgpt/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    A	specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
    A	specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md

    |P_source| 4    |P_main| 7    |P_union| 11

**Seven main-side changed paths, as §0a expected. The expectation is recorded as
met; the measurement above is what binds.**

Each path of `P_union` classified into exactly one class:

    (1,0) source-only    4
    (0,1) main-only      7
    (1,1) both-changed   0     = P_overlap
    (0,0)                0     (does not occur within P_union)

**`(1,0)`: the product blob must equal the source's.** Measured pairwise, blob
ids in full:

    derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md
      product bb438a909bd8ba855a3524a2caf73e3cf52f6f86   source bb438a909bd8ba855a3524a2caf73e3cf52f6f86
    reports/2026-08-29T1811Z_xi-qm3-dep-01.md
      product c9c184f05e48ffb3e6b4027f7703da485f606eee   source c9c184f05e48ffb3e6b4027f7703da485f606eee
    reviews/chatgpt/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
      product ebee1bcfd59802fb00e0f914d4d8cbd5ec1f42b7   source ebee1bcfd59802fb00e0f914d4d8cbd5ec1f42b7
    specs/2026-08-24T0000Z_xi-qm3-dep-01_v3.md
      product 6aee5b2882a7a021bce17454985553c3e6fc8b8f   source 6aee5b2882a7a021bce17454985553c3e6fc8b8f

    all four equal — PASS

**`(0,1)`: the product blob must equal the Base's.** All seven measured pairwise
and equal; the pairs are reproduced in full at `M3b(c)`, which sweeps the same
set.

    (1,1) P_overlap : EMPTY, measured over the classified union and not
                      inferred from fork distance
    (0,0)           : 0

**`A5` does not fire on `(b)`.**

### `M3b(c)` — main-preservation sweep, NON-VACUOUS

    paths in P_main \ P_source : 7

**This is the sweep that protects the `G-18` governance-debt entry and the
governance-debt task's artifacts — all landed on main after the source forked —
from being walked back.** Every pair measured; blob ids in full:

    docs/GOVERNANCE-DEBT.md
      product f6a813ee84f1b166b3fbbf73d48a2c7c03965f85   base f6a813ee84f1b166b3fbbf73d48a2c7c03965f85
    reports/2026-08-29T1715Z_govdebt-register-gap.md
      product d7a35c0df0cf729df918f45737f9afaa420b5566   base d7a35c0df0cf729df918f45737f9afaa420b5566
    reports/2026-08-29T1843Z_govdebt-register-gap-integ.md
      product dba8ced709f95cb8da5097047477c5fb26a556c3   base dba8ced709f95cb8da5097047477c5fb26a556c3
    reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product b03ce1f48a7904b7416775deeefd13b87524a0e4   base b03ce1f48a7904b7416775deeefd13b87524a0e4
    reviews/chatgpt/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
      product 85413004e371a54428e2802bf9727f489609dfc6   base 85413004e371a54428e2802bf9727f489609dfc6
    specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e   base 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e
    specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
      product 8d1e9d83f359c990021e9c5f963b38ccb259f258   base 8d1e9d83f359c990021e9c5f963b38ccb259f258

    seven of seven equal — PASS. No inequality; A5 does not fire.

**`C3b` PASS on every limb.**

## 3c. `M3c` — arrival-state verification of the finding

**Scan assumptions, stated.** The scan operates on the artifact's **bytes**,
decoded as UTF-8 and split on newlines; it tracks fenced-block state, so a line
inside a ``` fence is quoted text and not structure. The artifact carries no
blockquote prefixes on its own assertions and none is stripped anywhere. **No
character-offset arithmetic is used.** The artifact is 18811 bytes, 421 lines,
read from the merge product.

### `(iv)` FIRST — the enumeration rule, the enumerated set, and its count

**The rule is taken from the artifact's own landed structure, not from
judgement.** The artifact declares its own tagging rule at
`derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md:35`:

```text
**Every verdict sentence below carries both tags.**
```

and carries an inline tag marker on each such sentence.

**THE ENUMERATION RULE: a sentence is a verdict-assertion sentence if and only
if it carries the artifact's landed inline tag marker `| COND-R, COND-M`,
outside any fenced block.**

**THE ENUMERATED SET — 5 sentences.** Each is quoted verbatim; **normalization
applied: NONE.**

    [1]  :304

```text
**`M0b` returns `NOT UNIQUELY IDENTIFIED`. | COND-R, COND-M**
```

    [2]  :339

```text
**Result: `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`. | COND-R, COND-M**
```

    [3]  :370

```text
**This result is evidence, not a disposition. | COND-R, COND-M** The membership
```

    [4]  :384-388

```text
**This task was SCOPED to the landed `α` only**, by
`P2-XI-RULINGS-02-CLARIFICATION-01` as quoted at §0a — **but landed state did
not uniquely identify that object, so NO dependence evaluation was performed.**
`α` was not evaluated. No `N_α[g]` was constructed, no variation was taken, and
no verdict from `M3`'s pre-registered vocabulary is returned. | COND-R, COND-M
```

    [5]  :399-401

```text
**The criterion is therefore NOT discharged in full by this task.** It is not
discharged in part either: on this path no decoupling was evaluated at all.
| COND-R, COND-M
```

    COUNT: 5

**THEN the tag test, performed after the enumeration above:**

    [1] :304      carries both COND-R and COND-M            PASS
    [2] :339      carries both COND-R and COND-M            PASS
    [3] :370      carries both COND-R and COND-M            PASS
    [4] :384-388  carries both COND-R and COND-M            PASS
    [5] :399-401  carries both COND-R and COND-M            PASS
    no marker occurrence lies inside a fenced block         PASS
    marked-sentence count equals enumerated-sentence count  PASS

**The enumeration rule was stateable from the artifact's own structure, so the
`A5` case for an unstateable rule did not arise and nothing was enumerated by
judgement.**

### `(i)` `M0b`'s return, and no dependence verdict asserted as this task's result

The result-stating header field, `:11-13`, verbatim; **normalization: NONE**:

```text
    RESULT      M0b returns NOT UNIQUELY IDENTIFIED.
                Rule 22: INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED.
                **No dependence evaluation was performed.**
```

    M0b's return reads NOT UNIQUELY IDENTIFIED, in the header field   PASS
    and in enumerated sentence [1]                                    PASS

**THE TEST DOMAIN is the five enumerated sentences plus that header field, 948
bytes in total — and NOT the artifact's full text.**

**Bounded verdict forms searched inside the domain.** A bare `DEPENDENT` search
would be invalid because `INDEPENDENT` contains it; the first pattern carries a
negative lookbehind that excludes that case.

    pattern                                                        matches
    ------------------------------------------------------------------------
    (?<!IN)(?<!In)(?<!in)\bDEPENDENT\b                                 0
    \bINDEPENDENT\b                                                    0
    (?:returns?|verdict is|Result:\s*)\s*`?(?:IN)?DEPENDENT`?          0

**POSITIVE CONTROL — the same method, on the same domain, finds strings known
present**, so the null results above are distinguishable from a dead probe:

    'NOT UNIQUELY IDENTIFIED'                                       FOUND
    'INCONCLUSIVE'                                                  FOUND
    "no verdict from `M3`'s pre-registered vocabulary is returned"   FOUND

**OUT-OF-DOMAIN occurrences, RECORDED AS CONTEXT and NOT as findings**, per the
specification's direction:

    :396  `DEPENDENT` and that the term be subsequently found to grow with `L` — this
    :397  task returned no `DEPENDENT` and measured no `L`-scaling.
    :405  1. **No dependence verdict.** `DEPENDENT`, `INDEPENDENT` and the `M3`

Three lines. `:396-397` is the registered item's escalation condition, quoted as
a counterfactual and immediately negated; `:405` is the artifact's own
prohibition list, naming the vocabulary in order to say it is absent. **None is
a verdict assertion and none is a failure.**

### `(ii)` the Rule 22 classification

The classification, enumerated sentence `[2]`, reads
`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`. **PASS**

Its subclass reasoning, `:341-344`, verbatim; **normalization: NONE**:

```text
**Subclass.** `CONSTRUCTIVE GAP IDENTIFIED`, not `EVIDENCE INSUFFICIENT`. The
gap is not that the evidence was too thin to read: the landed statements are
explicit, and they say the object is not fixed. **The reason the dependence
question is returned unasked is a property of landed state, not of the check.**
```

Its resolution path, `:346-348`, marked defined-not-walked in the artifact's own
words; verbatim, **normalization: NONE**:

```text
**Resolution path, symmetric, defined here and NOT walked.** Either of the two
determinations below would close the gap; nothing in this artifact prefers one,
and this task performs neither.
```

and the two determinations it names, `:350-355` and `:357-362`:

```text
    R-1  A landed determination of which channel, or set of channels, the
         assembled chain's decoupling comprises — either by extending the
         2026-08-09 route ruling's scope from P2-PHASE-01 mean-field work
         to the assembled chain, or by a separate determination naming the
         decoupling for the chain. Authority: the PI. Neither extension nor
         determination is proposed here.
```

```text
    R-2  A landed decoupling prescription in the sense
         P2-FIERZSUM-01.md:218-220 states — auxiliary variables,
         constraints, Jacobian, and what is generated dynamically rather
         than introduced as an independent field. That note is landed not
         registered; by what route it or an equivalent becomes landed is
         the PI's.
```

    the classification reads INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED   PASS
    its subclass reasoning is present                                     PASS
    a symmetric resolution path is present                                PASS
    it is marked defined-not-walked, in the artifact's own words          PASS
    the path names R-1 and R-2                                            PASS
    the artifact states it performs neither determination                 PASS

**This task does not walk that path, order it, prioritise it, or begin either
determination it names.**

### `(iii)` the early-return scope wording, and the criterion

From enumerated sentence `[4]`:

    the scope statement is in its early-return wording —
      "SCOPED to the landed `α` only"                                     PASS
    and states "NO dependence evaluation was performed"                   PASS

From enumerated sentence `[5]`:

    the criterion is stated NOT discharged in full by this task           PASS
    and not discharged in part either                                     PASS

**Normalization applied to these substring tests: NONE.**

**`M3c` PASS on all four checks. `C3c` PASS.** See §8a for a probe defect found
and corrected inside `(ii)`.

## 4. `M4` — suite

Run on a full, non-shallow tree. **The arriving task added no tests; the
criterion is regression, not a count.**

**At the base**, tree `09937703df9bdd447046467e19b4335ed4c2cb02`:

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 52.93s

**At the post-merge integration tree**, which is the tested tree:

    T = 157e695b068893613ace3fb852354fc1577fce55   (the tree of M_merge)

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 44.67s

Identical outcomes. **No test fails on `T` that passes at the base. `C4` PASS.**

**This report is the next commit on the tested tree above.**

---

## 5. Acceptance criteria

    C1  PASS  origin/main equals the Base; the merge-base equals 0c01fc7f… as a
              full-string match; the source tip equals the Source field.
    C2  PASS  M_merge has exactly two parents, the M1b tip and the source tip;
              the M1b tip descends from the base by exactly two commits, spec
              then review; the spec's sha256 equals the digest the review
              declares, recorded at M1b.
    C3  PASS  Four of four digests equal their expected values, as full-string
              matches.
    C3b PASS  The contributed set is the four-path all-A manifest; the union
              classification assigns each of the eleven P_union paths to exactly
              one class with its blob rule satisfied; P_overlap is empty as
              measured over the classified union; the main-preservation sweep
              records product blob equal to Base blob for all seven swept paths,
              pairwise.
    C3c PASS  All four arrival-state checks pass, each with its quoted text and
              its stated normalization; (iv)'s enumeration rule, enumerated set
              and count are recorded BEFORE its tag test; (i)'s test is confined
              to that enumerated domain plus the result-stating header field,
              its negative result reported with its patterns and its live
              positive control, and all three out-of-domain occurrences recorded
              as context rather than as failures.
    C4  PASS  344 passed and 2 deselected at the base and at T.
    C5  NOT YET REACHED at this commit. Its limbs are post-commit and post-push
              and are recorded in the branch-only M5 addendum.

## 6. Abort conditions

    A1  DID NOT FIRE.  Every M1 value agrees with the spec's Base, Source and
        stated merge-base relation, as full-string matches.
    A2  DID NOT FIRE.  The merge was conflict-free and M3 found no digest
        mismatch in the merge product.
    A3  EVALUATED AT PUSH TIME.  main stands at the Base, which is the first
        parent's ancestor and H_integ's ancestor, so the advance is expected to
        be a fast-forward; the measurement is made at push and recorded in the
        M5 addendum.
    A4  DID NOT FIRE.  No file arriving from the source was modified and no ref
        of the source branch moved. The finding is not restated as a dependence
        verdict or as evidence bearing on one — §3c(i) confines the test to the
        artifact's own assertion domain and this report asserts nothing further;
        the Q-M3 row and the ledger are untouched and are not among this task's
        changed paths; the criterion is not described as discharged in whole or
        in part; the resolution path is transported, not walked, ordered or
        prioritised; and OPEN-AC-1, the exponent-mapping question and the
        registered representation-stability inquiry are untouched.
    A5  DID NOT FIRE.  No contributed path or status outside §1a's manifest, no
        both-changed path, no source-unchanged path whose product blob differs
        from the Base's, no main-unchanged contributed path whose product blob
        differs from the source's, and no M3c failure. Every negative result in
        §3c(i) is reported with a live positive control.

## 7. What arrives, stated as the arriving bytes state it

**`M0b` returned `NOT UNIQUELY IDENTIFIED`**, classified under Rule 22 as
`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`. Both strings are quoted at §3c
from the merge product; neither is paraphrased here.

**No dependence verdict was returned.** The arriving artifact says so in its own
words, quoted at §3c(i) and (iii). **This report states no verdict, and states
nothing about what a verdict would have been.**

**`Q-M3` remains an OPEN ledger row.** The ledger artifact is not in this task's
contributed set, is not in `P_main` either, and is therefore untouched by this
transport; membership stays deferred under `P2-XI-RULINGS-02` Ruling 1, and a
constructive-gap finding is not the evidence that ruling contemplates.

**The criterion is not discharged, in full or in part**, in the arriving
artifact's own terms.

**The resolution path arrives defined and unwalked**, with its two
determinations `R-1` and `R-2` named and neither begun.

## 8. Stops and clarifications (Amendment B)

Nothing stopped execution. One observation is recorded.

### 8a. A probe in `M3c(ii)` assumed the wrong emphasis span and reported a false failure

**Category: `OBSERVATION_METHOD_ERROR`, found and corrected inside this task,
before any conclusion was drawn.** The first pass at `M3c(ii)`'s
defined-not-walked limb searched for

    defined here and \*\*NOT walked\*\*

which assumes the emphasis markers wrap only the words `NOT walked`. In the
landed bytes the emphasis wraps the whole lead phrase —
`**Resolution path, symmetric, defined here and NOT walked.**` — so the pattern
could not match, and the limb reported FAIL.

**The probe was the defect, not the artifact.** The limb was re-measured as a
byte-exact substring test with no normalization on either side, and the marking
is present at `:346`; §3c(ii) records the corrected measurement, and the
surrounding evidence — the two named determinations and the artifact's own
sentence that it "performs neither" — was quoted rather than inferred.

**`A5` was not declared on the false failure**, and nothing but the measurement
changed: no arriving file was touched and the merge was not repaired. It is
recorded because the general fault is worth carrying forward — **a probe written
against remembered markup rather than against the file's bytes will fail against
its own assumption**, and the correction is the same one this programme has
already had to make twice: read the bytes, then test.

## 9. Rule 22

No result in this task is `INCONCLUSIVE`. The arriving task's
`INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED` is transported unaltered, with its
subclass and its symmetric resolution path, all three verified present at §3c.
**This task issues no verdict of its own and therefore owes no subclass or
resolution path.**

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

    to be pushed   refs/heads/science/integrate-xi-qm3-dep-01
                   refs/heads/main, fast-forward to H_integ
    must not move  refs/heads/science/xi-qm3-dep-01
                   refs/heads/science/xi-qm2-scope-01
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

**This section exists only on `science/integrate-xi-qm3-dep-01`. It is not on
`main`, and `origin/main` remains `H_integ`.** Everything below was measured
after the report commit above, so it could not have been inside it.

    H_integ   08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0

## `C5` first limb — `H_integ` against the tested tree

    git diff --name-status 157e695b068893613ace3fb852354fc1577fce55 H_integ
    A	reports/2026-08-30T1354Z_xi-qm3-dep-integ.md

**Exactly one path, the report artifact.** Measured, not asserted; re-measured
after the push against `origin/main` with the same single-path result.

## `A3` and the push order

`A3` was evaluated before the main push, as a measurement:

    git merge-base --is-ancestor origin/main H_integ   ->  0
    origin/main at that moment  1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841

`origin/main` was an ancestor of `H_integ`, so the advance is a fast-forward and
**`A3` did not fire.**

Push order executed, integration branch first, then `main`:

    git push -u origin science/integrate-xi-qm3-dep-01
      * [new branch]      science/integrate-xi-qm3-dep-01 -> science/integrate-xi-qm3-dep-01

    git push origin 08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0:refs/heads/main
      1852d17..08b46fb  08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0 -> main

`main` was advanced to **`H_integ`**, not to `M_merge` (`3e5ab10f…`).

## Post-push ref audit

    refs/heads/main                                    08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    refs/heads/science/integrate-xi-qm3-dep-01         08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0
    refs/heads/science/xi-qm3-dep-01                   d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/xi-qm2-scope-01                 b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/govdebt-register-gap-01         e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/integrate-govdebt-register-gap  963563ad16d6b289a53d8480d420a9aaac6a15a7
    refs/heads/science/xi-clar-01-landing              0b3c85cb158f6aae2dd661054d66bcd1f986878f
    refs/heads/science/xi-ledger-01                    0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    refs/heads/science/integrate-xi-clar-01            37a2f411ea1166134b3c153e15aab74af3f79bf6

    origin/main equals H_integ                                       PASS
    origin/main is NOT M_merge                                       PASS
    the integration branch equals H_integ                            PASS
    science/xi-qm3-dep-01 unmoved from its M1 value                  PASS
    science/xi-qm2-scope-01 unmoved from its M1 value                PASS
    science/govdebt-register-gap-01 unmoved from its M1 value        PASS
    science/integrate-govdebt-register-gap unmoved from its M1 value PASS
    science/xi-clar-01-landing unmoved                               PASS
    science/xi-ledger-01 unmoved                                     PASS
    science/integrate-xi-clar-01 unmoved                             PASS

**`C5` PASS on every limb.** The source branch did not move; no session, harness
or unrelated ref moved. The only two refs this task moved are the two the
specification authorizes.

**This addendum commit is pushed to `science/integrate-xi-qm3-dep-01` only.**
`origin/main` stays at `H_integ`; the addendum's own SHA is measured after this
commit and is returned outside the repository, not written back into it.

END OF ADDENDUM
