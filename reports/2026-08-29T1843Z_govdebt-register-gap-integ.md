# Report — `P2-GOVDEBT-REGISTER-GAP-INTEG` v2: transport of the `G-18` governance-debt entry

    Task ID     P2-GOVDEBT-REGISTER-GAP-INTEG
    Version     v2
    Spec        specs/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    Review      reviews/chatgpt/2026-08-24T1800Z_govdebt-register-gap-integ_v2.md
    Base        main @ 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    Source      science/govdebt-register-gap-01 @
                e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    Fork        9af94a4a11cd06e90ef2d24183565412b4043c6a  (measured)
    Branch      science/integrate-govdebt-register-gap
    Outcome     COMPLETE through M4. Four contributed paths transported;
                the NON-VACUOUS main-preservation sweep passed on all
                fourteen main-side paths. No abort fired.

This report records `M1` through `M4` and nothing later. It names the tested
tree `T` and **is itself the next commit** on it; it does not state its own
commit SHA, and it does not state `H_integ`. `M5`'s measurements are post-commit
and are recorded in the branch-only addendum.

    T = 9ef48055ba3b935566dd4ea34476bab1ac3d19b4

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
    HEAD before the branch   b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
                             (science/xi-qm2-scope-01)
    working tree             clean before the branch was cut

    git checkout -b science/integrate-govdebt-register-gap \
        0c01fc7f26e91dd84b032dccde0feac61f61d8ea

## 1. `M1` — pre-merge ref audit, before any write

    git ls-remote origin, full SHAs as returned

    refs/heads/main                             0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    refs/heads/science/govdebt-register-gap-01  e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/xi-clar-01-landing       0b3c85cb158f6aae2dd661054d66bcd1f986878f
    refs/heads/science/xi-ledger-01             0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    refs/heads/science/integrate-xi-clar-01     37a2f411ea1166134b3c153e15aab74af3f79bf6
    refs/heads/science/integrate-govdebt-register-gap   (no ref; created here)

The last three are the refs this task must not move; their `M1` values are
recorded here for the `M5` comparison.

**Full-string comparisons, not prefix comparisons:**

    origin/main                       0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    spec Base                         0c01fc7f26e91dd84b032dccde0feac61f61d8ea
                                      EQUAL

    source tip                        e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    spec Source                       e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
                                      EQUAL

    git merge-base main <source>      9af94a4a11cd06e90ef2d24183565412b4043c6a
    the value the spec requires       9af94a4a11cd06e90ef2d24183565412b4043c6a
                                      EQUAL  =>  the source does NOT descend
                                                 from the Base

    git rev-list --count Base..source   4
    git rev-list --count source..Base  14

**`A1` did not fire. `C1` PASS.** The repository is non-shallow, so both suite
runs are on a valid substrate.

**The stale-source topology is confirmed by measurement, not inherited from
§0a.** The source is 14 commits behind the Base and 4 ahead of the fork, so the
main-side sweep at `M3b(c)` is non-vacuous and is this task's load-bearing
protection.

## 1b. `M1b` — pre-execution provenance commits, before the merge

**Rule 18 and Amendment N.** The review carries the line
`**Reviewed specification SHA-256:**` — PRESENT — at its lines 4 and 168,
identically, and

    78e5ff109ac992adbc25dd5e072c9860dd010a0e9dc14f586a2303620b9fce9b

is the only 64-hex string it contains. Measured **before** the specification
commit, and re-measured over the committed bytes afterwards:

    sha256 of the spec file, before the commit
      78e5ff109ac992adbc25dd5e072c9860dd010a0e9dc14f586a2303620b9fce9b
    the digest the review declares itself bound to
      78e5ff109ac992adbc25dd5e072c9860dd010a0e9dc14f586a2303620b9fce9b
    sha256 of the committed bytes
      78e5ff109ac992adbc25dd5e072c9860dd010a0e9dc14f586a2303620b9fce9b

The review artifact has no pre-committed hash. Its sha256 is recorded at commit
as its first recorded digest,

    21b893f4735662c021c22ce641b9379dc1a5f718adcd25e298ced4198a03fc94

provenance transmitted by the PI in session. Verdict `APPROVE FOR EXECUTION`.

**Commit order, spec then review, nothing between them:**

    768c0cefc83fa83cf69352b613ddb41a54eb5848  spec(P2-GOVDEBT-REGISTER-GAP-INTEG): v2, ...
    94d5f17c8ea81ec2e1eedb9aed56ed36981581a6  review(P2-GOVDEBT-REGISTER-GAP-INTEG): ...

    M1b tip                            94d5f17c8ea81ec2e1eedb9aed56ed36981581a6
    git rev-list --count Base..M1b tip 2

**Reviewer determinations, recorded as issued and not restated:**

    Stale-source protocol            CONCUR
    M3b union audit                  CLOSED
    M3b(d) structural verification   CLOSED
    Main preservation                PASS
    Arrival semantics                PRESERVED
    Scope / authority boundary       PRESERVED

## 2. `M2` — merge construction

    git merge --no-ff <source tip>   on the M1b tip

    M_merge    5301097f9c2c1815bbbc8e584f786b9563c2e6fa
    parent 1   94d5f17c8ea81ec2e1eedb9aed56ed36981581a6   (the M1b tip)
    parent 2   e242a178bebb3ce8bbc8fce66d21a7f4a0257e13   (the source tip)

    Merge made by the 'ort' strategy.
    4 files changed, 1085 insertions(+), 2 deletions(-)
    git status --porcelain after the merge: empty

**The merge was conflict-free.** `A2` did not fire on this limb. `M_merge` has
exactly two parents, and they are the two the spec names. **`C2` PASS on all
three limbs.**

## 3. `M3` — arriving-blob verification, from the merge product

Every digest re-measured from the merge product, not from the source tip, and
recorded in full. Four of four match.

    path      docs/GOVERNANCE-DEBT.md
    expected  b7ff84e929e7f333b122d51fa3083d3ad73e2c44396b2ff84f1dbcdef817206b
    measured  b7ff84e929e7f333b122d51fa3083d3ad73e2c44396b2ff84f1dbcdef817206b

    path      specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
    expected  815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c
    measured  815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c

    path      reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
    expected  76bffe973bd9d2cabfe63d7f03e135d93ca9ed61ad509cba7d7317c956935fe5
    measured  76bffe973bd9d2cabfe63d7f03e135d93ca9ed61ad509cba7d7317c956935fe5

    path      reports/2026-08-29T1715Z_govdebt-register-gap.md
    expected  b50be869554b781e84d4a23c463fc78030444558f54be76afe9bed452ef61e7c
    measured  b50be869554b781e84d4a23c463fc78030444558f54be76afe9bed452ef61e7c

    mismatches: 0

`A2` did not fire on its second limb. **`C3` PASS.**

## 3b. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK = the merge-base measured at M1 = 9af94a4a11cd06e90ef2d24183565412b4043c6a
    BASE                                 = 0c01fc7f26e91dd84b032dccde0feac61f61d8ea
    SRC                                  = e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    PROD = M_merge                       = 5301097f9c2c1815bbbc8e584f786b9563c2e6fa

### `M3b(a)` — the contributed path set

`git diff --name-status FORK..<source>`, verbatim:

    M	docs/GOVERNANCE-DEBT.md
    A	reports/2026-08-29T1715Z_govdebt-register-gap.md
    A	reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
    A	specs/2026-08-24T0600Z_govdebt-register-gap_v3.md

    entries 4    A 3    M 1    other 0
    the A set equals the three-path manifest of M3      true
    the M set is exactly {docs/GOVERNANCE-DEBT.md}      true
    no D, R, C or T status appears                      true

**`A5` does not fire on `(a)`.** The set is §1a's four-entry manifest exactly.

### `M3b(b)` — union classification

`P_source` (`FORK..source`) is the four-entry set above.
`P_main` (`FORK..Base`), verbatim:

    M	DECISION_LOG.md
    A	decisions/2026-08-24-xi-open-item-register-routing.md
    A	decisions/2026-08-24-xi-rulings-02-clarification-01.md
    A	decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
    A	reports/2026-08-24T0043Z_xi-clar-01-landing.md
    A	reports/2026-08-29T1648Z_xi-clar-01-landing-resumed.md
    A	reports/2026-08-29T1729Z_xi-clar-01-integ.md
    A	reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
    A	reviews/chatgpt/2026-08-24T0000Z_xi-clar-01-landing_v2.md
    A	reviews/chatgpt/2026-08-24T0900Z_xi-clar-01-landing_v3.md
    A	reviews/chatgpt/2026-08-24T1200Z_xi-clar-01-integ.md
    A	specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md
    A	specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
    A	specs/2026-08-24T1200Z_xi-clar-01-integ.md

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

    docs/GOVERNANCE-DEBT.md
      product f6a813ee84f1b166b3fbbf73d48a2c7c03965f85   source f6a813ee84f1b166b3fbbf73d48a2c7c03965f85
    reports/2026-08-29T1715Z_govdebt-register-gap.md
      product d7a35c0df0cf729df918f45737f9afaa420b5566   source d7a35c0df0cf729df918f45737f9afaa420b5566
    reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product b03ce1f48a7904b7416775deeefd13b87524a0e4   source b03ce1f48a7904b7416775deeefd13b87524a0e4
    specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
      product 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e   source 029d07112bc9d2e24d3809aedc32ed3e2a39fd1e

    all four equal — PASS

**`docs/GOVERNANCE-DEBT.md` classifies `(1,0)`** — it is changed on the source
side and unchanged on main since the fork. **That is measured, not assumed**: had
it classified `(1,1)`, the counts table would have been changed on both sides
and `A5` would have fired.

**`(0,1)`: the product blob must equal the Base's.** All fourteen measured
pairwise and equal; the pairs are reproduced in full at `M3b(c)` below, which
sweeps the same set.

    (1,1) P_overlap : EMPTY, measured over the classified union and not
                      inferred from fork distance
    (0,0)           : 0

**`A5` does not fire on `(b)`.**

### `M3b(c)` — main-preservation sweep, NON-VACUOUS

    paths in P_main \ P_source : 14

**This is the sweep that protects the landed clarification, the
register-routing decision record, `DECISION_LOG.md` with the open-item
registration, and the preceding tasks' artifacts from being walked back by a
source that forked before them.** Every pair measured; blob ids in full:

    DECISION_LOG.md
      product d6ac0ecdba2c9d91d0fc840e2e5e80f20474c90b   base d6ac0ecdba2c9d91d0fc840e2e5e80f20474c90b
    decisions/2026-08-24-xi-open-item-register-routing.md
      product 70ea2b80297bab1d22b6af9e30348fa04d809b63   base 70ea2b80297bab1d22b6af9e30348fa04d809b63
    decisions/2026-08-24-xi-rulings-02-clarification-01.md
      product 5599f4cbd6a82e61b18e568e0cc43d6d926066ea   base 5599f4cbd6a82e61b18e568e0cc43d6d926066ea
    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
      product 1786124bbe3bfa02809d83c2890d0800e0d3edd8   base 1786124bbe3bfa02809d83c2890d0800e0d3edd8
    reports/2026-08-24T0043Z_xi-clar-01-landing.md
      product 6c5ae294bb541ba71382dc7ef2b378a9b14da5ff   base 6c5ae294bb541ba71382dc7ef2b378a9b14da5ff
    reports/2026-08-29T1648Z_xi-clar-01-landing-resumed.md
      product 2729d6c2c14cbe3889cf000f014999c3a6635006   base 2729d6c2c14cbe3889cf000f014999c3a6635006
    reports/2026-08-29T1729Z_xi-clar-01-integ.md
      product 1431c5114673203c951a1e874cfa148271de4cf1   base 1431c5114673203c951a1e874cfa148271de4cf1
    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
      product 062145c6d0923e7a05166acdde0de1bfdf7aeb78   base 062145c6d0923e7a05166acdde0de1bfdf7aeb78
    reviews/chatgpt/2026-08-24T0000Z_xi-clar-01-landing_v2.md
      product 4f5a8adb1788e7ccc7a92aa63f92ba7d53659d52   base 4f5a8adb1788e7ccc7a92aa63f92ba7d53659d52
    reviews/chatgpt/2026-08-24T0900Z_xi-clar-01-landing_v3.md
      product 2e8db209dcf9334c09ed14d856bb6e9a9fe185fe   base 2e8db209dcf9334c09ed14d856bb6e9a9fe185fe
    reviews/chatgpt/2026-08-24T1200Z_xi-clar-01-integ.md
      product 1912f73e3d1570295a4114cd3f4fab78e44c2ae1   base 1912f73e3d1570295a4114cd3f4fab78e44c2ae1
    specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md
      product 9542cf614d5ea29539e2d7f22ecb68021a145cc2   base 9542cf614d5ea29539e2d7f22ecb68021a145cc2
    specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
      product 7175c0fda5876d99e19b7a2524ed5e21789440c2   base 7175c0fda5876d99e19b7a2524ed5e21789440c2
    specs/2026-08-24T1200Z_xi-clar-01-integ.md
      product e5737a0967b567055a49f202e0fb78a44fe05ca1   base e5737a0967b567055a49f202e0fb78a44fe05ca1

    fourteen of fourteen equal — PASS. No inequality; A5 does not fire.

### `M3b(d)` — structure verification of the one modified path

    docs/GOVERNANCE-DEBT.md
      base bytes    32677
      source bytes  42698
      product bytes 42698

**`(d1)` BYTE GOVERNANCE.**

    sha256 source   b7ff84e929e7f333b122d51fa3083d3ad73e2c44396b2ff84f1dbcdef817206b
    sha256 product  b7ff84e929e7f333b122d51fa3083d3ad73e2c44396b2ff84f1dbcdef817206b
    the product's byte content equals the source's, byte for byte      PASS
    normalization applied to either side of this comparison:  NONE

**`(d2)` HEADING SEQUENCE, against the Base.** `H_B` and `H_P` are the ordered
lists of `## \`G-` heading lines in file order.

    |H_B| = 17        |H_P| = 18
    H_B is an ordered PREFIX of H_P                                    PASS
    H_P has exactly one further element                                PASS
    no duplicate heading in H_P                                        PASS

`H_B`, in file order:

    ## `G-01` — the executor harness conflicts with `P6`
    ## `G-02` — a docstring asserts a freeze the determination rejects
    ## `G-03` — corrections are not discoverable from what they correct
    ## `G-04` — nothing requires a newly issued specification to carry `stated:`
    ## `G-05` — nothing compares a review's cited digest against the specification
    ## `G-06` — nothing performs the auto-merge line-survival check
    ## `G-07` — the mechanism-marker vocabulary is defined only in a record
    ## `G-08` — a criterion can assert something false about its own specification
    ## `G-09` — nothing independently validates the shared gate-heading grammar
    ## `G-10` — nothing detects a guard going vacuous
    ## `G-11` — a probe contradicting an existing check is likelier to be wrong
    ## `G-12` — `science/` was an operational branch class the policy did not name
    ## `G-13` — the protection model for review-bound records is unspecified
    ## `G-14` — three historical PI records are each owed a retrospective review
    ## `G-15` — errata: two wording corrections not applied to the landed bytes
    ## `G-16` — rule 22's retrospective reach is unsettled, and the audit is owed
    ## `G-17` — no rule says a scoped result must be cited with its scope

The differing element, verbatim, and the whole of the difference:

    ## `G-18` — no landed index of the repository's registers and their stated scopes

**`H_P = H_B ++ [the G-18 heading]` holds exactly.** In one comparison this
establishes that no Base heading was removed, renamed, reordered or duplicated
and that exactly one was added.

**`(d3)` COUNTS TABLE, reconstructed from entry fields.** A heading carries an
identifier and not a disposition, so the buckets were rebuilt from each `G-*`
entry's own landed `Disposition:` line in the product:

    G-01  NOT REPAIRABLE HERE      G-10  OPEN
    G-02  REPAIRABLE               G-11  METHOD NOTE
    G-03  OPEN                     G-12  RULED
    G-04  SPECIFIABLE              G-13  OPEN
    G-05  SPECIFIABLE              G-14  RULED
    G-06  SPECIFIABLE              G-15  REPAIRABLE
    G-07  RULED                    G-16  OPEN
    G-08  OPEN                     G-17  OPEN
    G-09  OPEN                     G-18  OPEN

    18 entries measured; every one had a readable Disposition field, so the A5
    case for an unreadable field did not arise and no default was assigned.

The counts table as landed in the product, verbatim:

    REPAIRABLE            2     G-02  G-15
    SPECIFIABLE           3     G-04  G-05  G-06
    NOT REPAIRABLE HERE   1     G-01
    RULED                 3     G-07  G-12  G-14
    METHOD NOTE           1     G-11
    OPEN                  8     G-03  G-08  G-09  G-10  G-13  G-16  G-17  G-18
    ------------------------------------------------
    entries              18

Reconstruction and landed table, side by side:

    disposition           table n / list                 reconstruction n / list
    -----------------------------------------------------------------------------
    REPAIRABLE            2  G-02 G-15                   2  G-02 G-15
    SPECIFIABLE           3  G-04 G-05 G-06              3  G-04 G-05 G-06
    NOT REPAIRABLE HERE   1  G-01                        1  G-01
    RULED                 3  G-07 G-12 G-14              3  G-07 G-12 G-14
    METHOD NOTE           1  G-11                        1  G-11
    OPEN                  8  G-03 G-08 G-09 G-10 G-13    8  G-03 G-08 G-09 G-10 G-13
                             G-16 G-17 G-18                 G-16 G-17 G-18
    entries              18                             18

    every identifier list matches as an exact SET                      PASS
    every identifier list matches IN THE TABLE'S STATED ORDER          PASS
    every per-disposition count equals its list length                 PASS
    every reconstructed disposition appears as a table row             PASS
    the entry total equals the number of entries measured              PASS
    the row counts sum to the total                                    PASS

**`(d4)` NO OTHER BASE LINE CHANGED.** Measured by diff against the Base; the
changed line ranges with their content:

    replace  Base 42 -> product 42
      -     OPEN                  7     G-03  G-08  G-09  G-10  G-13  G-16  G-17
      +     OPEN                  8     G-03  G-08  G-09  G-10  G-13  G-16  G-17  G-18
    replace  Base 44 -> product 44
      -     entries              17
      +     entries              18
    insert   after Base 644 -> product 645-876
      + the 232-line G-18 entry, containing exactly one `## `G-` heading

    every CHANGED Base line lies inside the counts table               PASS
    all inserted lines form a single trailing block                    PASS
    the inserted block contains the G-18 heading and no other          PASS
    the insertion point is after the last Base entry                   PASS

**Exactly two pre-existing lines change, both in the counts table, and the only
other difference is the appended entry.** `A5` does not fire on `(d)`.
**`C3b` PASS on every limb.**

## 3c. `M3c` — arrival-state verification of the entry

**Entry boundary, measured fence-aware.** The `G-18` entry quotes landed text
that itself contains `## ` heading lines inside fenced blocks; a heading inside a
fence is quoted text and not structure. The boundary scan therefore tracks fence
state, and on that basis the entry spans `docs/GOVERNANCE-DEBT.md:645-876`,
10014 bytes, ending at the next structural heading
`## Not entered here — \`D4\``. See §8a.

**`(i)` `Disposition: OPEN` and no other.** Exactly one `**Disposition:`
declaration in the entry, at `docs/GOVERNANCE-DEBT.md:647`:

```text
**Disposition: OPEN.** The register's disposition definitions in full,
```

    exactly one Disposition declaration in the entry                   PASS
    it declares OPEN                                                   PASS
    no other disposition is declared for this entry                    PASS

**Normalization applied to that quotation: NONE.** The entry does discuss
`SPECIFIABLE` in prose — quoting the register's own definition in order to state
that it is NOT claimed — and the test above is on the declaration form
`**Disposition: X`, not on the word's appearance.

**`(ii)` the two disclaimer sentences.** Both present, matched as byte
substrings of the entry with **no normalization applied**:

```text
**This entry records a missing mechanism. It does not register the open item,
does not propose a register, does not create one, and does not express a
preference among the resolutions of the indexing gap.**
```

```text
**This entry is not closed by being written down**
```

and the register's own rule, quoted inside the entry:

```text
**No entry is marked CLOSED.** Nothing here is closed by being written down.
```

**`(iii)` the two claims that must be ABSENT.**

**Probe method, stated.** The entry's text is searched for each pattern below,
case-insensitively, with runs of whitespace collapsed to a single space.
**That collapse is the only normalization applied**, and it is applied so that a
claim split across a line break cannot evade the probe. Any match would be
printed with its surrounding text; none was found.

    pattern                                              matches
    ---------------------------------------------------------------
    no register admits                                   0
    no register'?s stated scope (?:explicitly )?admits   0
    no register .{0,40}admits                            0
    routing (?:is|remains) unresolved                    0
    routing (?:is|remains) (?:not |un)settled            0
    routing .{0,30}(unresolved|unsettled|not settled|open)  0
    is not yet registered                                0

**Positive control, so the absences are not an artifact of a probe that finds
nothing:** the same probe, on the same flattened text, finds
`has since been ruled by the PI` and `for that item only`. What the entry says
instead, verbatim from the product:

```text
identified and used. **The routing of the item that triggered the second
performance has since been ruled by the PI, on 2026-08-24, for that item
only** — no register's scope was extended and no general rule was made — and
that ruling leaves the indexing gap exactly where it was.
```

**`M3c` PASS on all three checks. `C3c` PASS.**

## 4. `M4` — suite

Run on a full, non-shallow tree.

**At the base**, tree `b113df9eb19becb467fad9be349241c7495d1b62`:

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 39.50s

**At the post-merge integration tree**, which is the tested tree:

    T = 9ef48055ba3b935566dd4ea34476bab1ac3d19b4   (the tree of M_merge)

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 37.65s

Identical outcomes. **No test fails on `T` that passes at the base. `C4` PASS.**

**This report is the next commit on the tested tree above.**

---

## 5. Acceptance criteria

    C1  PASS  origin/main equals the Base; the merge-base equals 9af94a4a… as a
              full-string match; the source tip equals the Source field.
    C2  PASS  M_merge has exactly two parents, the M1b tip and the source tip;
              the M1b tip descends from the base by exactly two commits, spec
              then review; the spec's sha256 equals the digest the review
              declares, recorded at M1b.
    C3  PASS  Four of four digests equal their expected values, as full-string
              matches.
    C3b PASS  The contributed set is the four-entry manifest with its stated
              statuses; the union classification assigns each of the eighteen
              P_union paths to exactly one class with its blob rule satisfied,
              GOVERNANCE-DEBT in (1,0); P_overlap is empty as measured over the
              classified union; the main-preservation sweep records product blob
              equal to Base blob for all fourteen swept paths, pairwise; and
              d1–d4 each pass with their measured values recorded — d2 with both
              heading sequences and the differing element, d3 with the
              reconstruction and the landed table side by side, d4 with the
              changed line ranges and their content.
    C3c PASS  All three arrival-state checks pass, each with its quoted text and
              its stated normalization.
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
        of the source branch moved. The entry's disposition is not restated,
        upgraded, downgraded or glossed — it is quoted; the entry is not marked
        closed; the entry is not read as resolving where future XI-line open
        items are registered; the arriving report's recorded defect is not
        corrected or annotated — see §7; and no authorized or registered inquiry
        is begun, scheduled, constrained or prioritised.
    A5  DID NOT FIRE.  No contributed path or status outside §1a's manifest, no
        both-changed path, no source-unchanged path whose product blob differs
        from the Base's, no main-unchanged contributed path whose product blob
        differs from the source's, no failure of M3b(d), and no M3c failure.

## 7. The arriving report's recorded defect, transported unaltered

The arriving report records that its own specification's §0 described the
clarification landing branch as standing where it stopped, which by then it did
not. **That record travels with the result unaltered.** Its bytes are covered by
`M3`'s digest for `reports/2026-08-29T1715Z_govdebt-register-gap.md`, which
matched, and by the `(1,0)` blob comparison, which matched. **This task does not
correct it, does not annotate it, and does not re-litigate it**, per `A4`.

## 8. Stops and clarifications (Amendment B)

Nothing stopped execution. One observation is recorded.

### 8a. A first pass at `M3c` used a fence-blind entry boundary and reported a false failure

**Category: `OBSERVATION_METHOD_ERROR`, found and corrected inside this task,
before any conclusion was drawn.** The first `M3c` run located the end of the
`G-18` entry as the next line beginning `## `. The entry quotes landed text
inside fenced blocks, and one of those quotations is the `DECISION_LOG.md`
heading `## 2026-08-19 — Open construction item: …`. The scan stopped there, at
`:701`, and measured an entry of 2335 bytes instead of 10014 — so `M3c(ii)`
reported both disclaimer sentences ABSENT.

**They are present.** The boundary was the defect, not the entry. The scan was
redone tracking fence state, so that a `## ` line inside a fenced block is read
as quoted text and not as structure; on that basis the entry spans `:645-876`
and both sentences match as byte substrings with no normalization. §3c records
the corrected measurement.

**`A5` was not declared on the false failure**, and no repair was made to the
merge or to any arriving file: the error was in the measurement, and only the
measurement changed. It is recorded rather than dropped because a governance
register whose entries quote other files' headings will defeat a fence-blind
scan every time, and the next task to audit this file needs to know that.

## 9. Rule 22

No result in this task is `INCONCLUSIVE`. The arriving entry's disposition
`OPEN` is a register disposition, defined by that register as *none of the
above*; it is not an `INCONCLUSIVE` verdict, it is transported unaltered, and
this task issues no verdict of its own and owes no subclass or resolution path.

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

    to be pushed   refs/heads/science/integrate-govdebt-register-gap
                   refs/heads/main, fast-forward to H_integ
    must not move  refs/heads/science/govdebt-register-gap-01
                   refs/heads/science/xi-clar-01-landing
                   refs/heads/science/xi-ledger-01
                   refs/heads/science/integrate-xi-clar-01
                   refs/heads/science/xi-qm3-dep-01
                   refs/heads/science/xi-qm2-scope-01
                   any session or harness branch

`M5`'s measurements — `H_integ`, the diff of `H_integ` against `T`, the push
results and the post-push ref audit — are post-commit and go into the addendum
commit on the integration branch only. `origin/main` remains at `H_integ`.

END OF REPORT

---

# ADDENDUM — `M5`, post-push. BRANCH-ONLY.

**This section exists only on `science/integrate-govdebt-register-gap`. It is
not on `main`, and `origin/main` remains `H_integ`.** Everything below was
measured after the report commit above, so it could not have been inside it.

    H_integ   1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841

## `C5` first limb — `H_integ` against the tested tree

    git diff --name-status 9ef48055ba3b935566dd4ea34476bab1ac3d19b4 H_integ
    A	reports/2026-08-29T1843Z_govdebt-register-gap-integ.md

**Exactly one path, the report artifact.** Measured, not asserted; re-measured
after the push against `origin/main` with the same single-path result.

## `A3` and the push order

`A3` was evaluated before the main push, as a measurement:

    git merge-base --is-ancestor origin/main H_integ   ->  0
    origin/main at that moment  0c01fc7f26e91dd84b032dccde0feac61f61d8ea

`origin/main` was an ancestor of `H_integ`, so the advance is a fast-forward and
**`A3` did not fire.**

Push order executed, integration branch first, then `main`:

    git push -u origin science/integrate-govdebt-register-gap
      * [new branch]      science/integrate-govdebt-register-gap -> science/integrate-govdebt-register-gap

    git push origin 1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841:refs/heads/main
      0c01fc7..1852d17  1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841 -> main

`main` was advanced to **`H_integ`**, not to `M_merge` (`5301097f…`). The
two-dot form in the push output is git's own abbreviation of the fast-forward it
performed.

## Post-push ref audit

    refs/heads/main                                    1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    refs/heads/science/integrate-govdebt-register-gap  1852d17c6d2c8a0f7973c0316f5f59f7c4ce0841
    refs/heads/science/govdebt-register-gap-01         e242a178bebb3ce8bbc8fce66d21a7f4a0257e13
    refs/heads/science/xi-clar-01-landing              0b3c85cb158f6aae2dd661054d66bcd1f986878f
    refs/heads/science/xi-ledger-01                    0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    refs/heads/science/integrate-xi-clar-01            37a2f411ea1166134b3c153e15aab74af3f79bf6
    refs/heads/science/xi-qm3-dep-01                   d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/xi-qm2-scope-01                 b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/integrate-xi-rulings-02         fd3a112df30eb43a58f4c264169104c6b847225b

    origin/main equals H_integ                                       PASS
    origin/main is NOT M_merge                                       PASS
    the integration branch equals H_integ                            PASS
    science/govdebt-register-gap-01 unmoved from its M1 value        PASS
    science/xi-clar-01-landing unmoved from its M1 value             PASS
    science/xi-ledger-01 unmoved from its M1 value                   PASS
    science/integrate-xi-clar-01 unmoved from its M1 value           PASS
    science/xi-qm3-dep-01 unmoved                                    PASS
    science/xi-qm2-scope-01 unmoved                                  PASS
    science/integrate-xi-rulings-02 unmoved                          PASS

**`C5` PASS on every limb.** The source branch did not move; no session, harness
or unrelated ref moved. The only two refs this task moved are the two the
specification authorizes.

**This addendum commit is pushed to `science/integrate-govdebt-register-gap`
only.** `origin/main` stays at `H_integ`; the addendum's own SHA is measured
after this commit and is returned outside the repository, not written back into
it.

END OF ADDENDUM
