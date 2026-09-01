# Report — `P2-XI-RULINGS-03-INTEG` v2: transport of the R-1 ruling landing

    Task ID     P2-XI-RULINGS-03-INTEG
    Version     v2
    Spec        specs/2026-09-01T0600Z_xi-rulings-03-integ_v2.md
    Review      reviews/chatgpt/2026-09-01T0600Z_xi-rulings-03-integ_v2.md
    Base        main @ 4a99e81ad16322e1152286df0158b648b75d18f3
    Source      science/xi-rulings-03-landing @
                4eca6408dcd64e0066cdeff775de85d5043bdfed
    Fork        4a99e81ad16322e1152286df0158b648b75d18f3  (measured)
    Branch      science/integrate-xi-rulings-03
    Outcome     COMPLETE through M4. Seven contributed paths transported,
                six added and one modified under append-only
                re-verification. No abort fired.

This report records `M1` through `M4` and nothing later. **`M5`'s post-push ref
values do not exist when this is written and are not in it**, per the
specification's separation of the two evidence surfaces. It names the tested tree
`T` and **is itself the next commit** on it; it does not state its own commit SHA
and it does not state `H_integ`.

    T = 1d781ef9af8dbc15a51423e9d506d0538337ea4e

**MEASUREMENT UNITS.** Every offset, length, prefix and byte-identity comparison
is in BYTES, with the normalization stated or stated to be none. **No identifier
is used at a value this task did not measure and print, and no abbreviation is
completed.**

**Rule 17.** This task transports one executed, reviewed result and adds no
classification the reviewed result did not carry.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    host                     vm
    working directory        /home/user/2-emergent-gravity
    worktree top level       /home/user/2-emergent-gravity
    shallow repository       false
    HEAD before the branch   4eca6408dcd64e0066cdeff775de85d5043bdfed
                             (science/xi-rulings-03-landing)
    working tree             clean before the branch was cut

    git checkout -b science/integrate-xi-rulings-03 \
        4a99e81ad16322e1152286df0158b648b75d18f3

## 1. `M1` — pre-merge ref audit, before any write

    git ls-remote origin, full SHAs as returned

    refs/heads/main                              4a99e81ad16322e1152286df0158b648b75d18f3
    refs/heads/science/xi-rulings-03-landing     4eca6408dcd64e0066cdeff775de85d5043bdfed
    refs/heads/science/xi-qm2-scope-01           b133e6aab8a9f03a2c76345d5bd818898c6a1ab3
    refs/heads/science/xi-qm3-dep-01             d55b6350a015d124f723d1fceb75b77cdcc112a9
    refs/heads/science/integrate-xi-qm2-scope-01 17ecc15b2b98718a955611cb334d05d7b8aaff41
    refs/heads/science/integrate-xi-rulings-03   (no ref; created here)

The last three are the refs this task must not move; their `M1` values are
recorded here for the `M5` comparison.

**Full-string comparisons, not prefix comparisons:**

    origin/main                       4a99e81ad16322e1152286df0158b648b75d18f3
    spec Base                         4a99e81ad16322e1152286df0158b648b75d18f3
                                      EQUAL

    source tip                        4eca6408dcd64e0066cdeff775de85d5043bdfed
    spec Source                       4eca6408dcd64e0066cdeff775de85d5043bdfed
                                      EQUAL, all 40 hex characters

    git merge-base main <source>      4a99e81ad16322e1152286df0158b648b75d18f3
    the Base                          4a99e81ad16322e1152286df0158b648b75d18f3
                                      EQUAL  =>  the source DESCENDS from
                                                 the Base

    git rev-list --count Base..source   6
    git rev-list --count source..Base   0

**`A1` did not fire. `C1` PASS.** The repository is non-shallow, so both suite
runs are on a valid substrate.

## 1b. `M1b` — pre-execution provenance commits, before the merge

**Rule 18 and Amendment N.** The review carries the line
`**Reviewed specification SHA-256:**` — PRESENT — at its lines 4 and 230,
identically, and

    f701669a01114e78c73a4121ebdbcca41c3659daf5a3adde19c9349033cb8050

is the only 64-hex string it contains. Measured **before** the specification
commit, and re-measured over the committed bytes afterwards:

    sha256 of the spec file, before the commit
      f701669a01114e78c73a4121ebdbcca41c3659daf5a3adde19c9349033cb8050
    the digest the review declares itself bound to
      f701669a01114e78c73a4121ebdbcca41c3659daf5a3adde19c9349033cb8050
    sha256 of the committed bytes
      f701669a01114e78c73a4121ebdbcca41c3659daf5a3adde19c9349033cb8050

The review artifact has no pre-committed hash. Its sha256 is recorded at commit
as its first recorded digest,

    5c6400c32a4fe3476d193196fd69b3e372a1587683e0eef4f1d04e9b65ac4d46

provenance transmitted by the PI in session. Verdict `APPROVE FOR EXECUTION`.

**Commit order, spec then review, nothing between them:**

    16cfb7b8d4f456c7966e25a567f491b04ce0cdcd  spec(P2-XI-RULINGS-03-INTEG): v2, ...
    eb9fcd069e88940e3bcd3819e89330084bdb8d02  review(P2-XI-RULINGS-03-INTEG): ...

    M1b tip                            eb9fcd069e88940e3bcd3819e89330084bdb8d02
    git rev-list --count Base..M1b tip 2

**Reviewer determinations, recorded as issued and not restated:**

    v1 evidence-surface defect  RESOLVED
    Base / Source topology      PASS
    Manifest authority          PASS
    Fork-aware audit            PASS
    Append-only verification    PASS
    Supersession verification   PASS
    Corrected-rationale verif.  PASS
    Scientific non-interference PASS
    T -> H_integ topology       PASS
    M5 evidence routing         PASS
    Measurement discipline      PASS

Its §23 records, non-blocking, that the v2 version note calls the change "no
acceptance-architecture change" where it is more precisely an evidence-surface
consistency correction. **That is the reading this execution followed**: the
report below carries `M1`–`M4` and nothing later.

## 2. `M2` — merge construction

    git merge --no-ff <source tip>   on the M1b tip

    M_merge    ae096af18a49f0574545ddf8270256f8e69d6e39
    parent 1   eb9fcd069e88940e3bcd3819e89330084bdb8d02   (the M1b tip)
    parent 2   4eca6408dcd64e0066cdeff775de85d5043bdfed   (the source tip)

    Merge made by the 'ort' strategy.
    7 files changed, 1851 insertions(+)
    git status --porcelain after the merge: empty

**The merge was conflict-free.** `A2` did not fire on this limb. `M_merge` has
exactly two parents, and they are the two the spec names. **`C2` PASS on all
three limbs.**

## 3. `M3` — arriving-blob verification, from the merge product

Every digest re-measured from the merge product, not from the source tip. Seven
of seven match.

    path      DECISION_LOG.md
    expected  d248e849007b0299c8ce92951d27ed500834f1ae49827a49637bf89ef8495d41
    measured  d248e849007b0299c8ce92951d27ed500834f1ae49827a49637bf89ef8495d41

    path      decisions/P2-XI-RULINGS-03.issued.md
    expected  1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
    measured  1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686
    blob id   expected 0b331afb6f21f6591a0c3934fc8916bda742d8de
              measured 0b331afb6f21f6591a0c3934fc8916bda742d8de

    path      decisions/2026-08-31-xi-rulings-03.md
    expected  e1c6bb959c7091f7a5af9d23a41ecdda9da52fc838b7df341c540151ecf6c1aa
    measured  e1c6bb959c7091f7a5af9d23a41ecdda9da52fc838b7df341c540151ecf6c1aa

    path      reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
    expected  dc538e3a69aef2f205a74f7c51bb10345ea4dbe66d292af66b3712aba00e5359
    measured  dc538e3a69aef2f205a74f7c51bb10345ea4dbe66d292af66b3712aba00e5359

    path      specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
    expected  0b6f48d73fdd4a1761f704d9801f338918a00391d18b6ccf472df5b79dd179d5
    measured  0b6f48d73fdd4a1761f704d9801f338918a00391d18b6ccf472df5b79dd179d5

    path      reviews/chatgpt/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
    expected  26ba2ccbe0ad9afd6e5dbdcb49074bfca14a2674a7c556d442caf548148b31ca
    measured  26ba2ccbe0ad9afd6e5dbdcb49074bfca14a2674a7c556d442caf548148b31ca

    path      reports/2026-09-01T0135Z_xi-rulings-03-landing.md
    expected  b934a857cc800891affd0b9a26a6212737d4621af4cddec9e7cf4c6e582c5e8c
    measured  b934a857cc800891affd0b9a26a6212737d4621af4cddec9e7cf4c6e582c5e8c

    mismatches: 0

`A2` did not fire on its second limb. **`C3` PASS.**

## 3b. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK = the merge-base measured at M1 = 4a99e81ad16322e1152286df0158b648b75d18f3
    BASE                                 = 4a99e81ad16322e1152286df0158b648b75d18f3
    SRC                                  = 4eca6408dcd64e0066cdeff775de85d5043bdfed
    PROD = M_merge                       = ae096af18a49f0574545ddf8270256f8e69d6e39

### `M3b(a)` — the contributed path set

`git diff --name-status FORK..<source>`, verbatim:

    M	DECISION_LOG.md
    A	decisions/2026-08-31-xi-rulings-03.md
    A	decisions/P2-XI-RULINGS-03.issued.md
    A	reports/2026-09-01T0135Z_xi-rulings-03-landing.md
    A	reviews/chatgpt/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
    A	reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
    A	specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md

    seven entries                                       true
    the A set equals the six-path manifest              true
    the M set is exactly {DECISION_LOG.md}              true
    no D, R, C or T status appears                      true

**`A5` does not fire on `(a)`.**

### `M3b(b)` — union classification

`P_source` (`FORK..source`) is the seven-entry set above.
`P_main` (`FORK..Base`), verbatim:

    (empty)

    |P_source| 7    |P_main| 0    |P_union| 7

    (1,0) source-only    7
    (0,1) main-only      0
    (1,1) both-changed   0     = P_overlap
    (0,0)                0     (does not occur within P_union)

**`(1,0)`: the product blob must equal the source's.** Measured pairwise, blob
ids in full:

    DECISION_LOG.md
      product 5fa2adf2e48b8d2e188c00950be54472b58c960c   source 5fa2adf2e48b8d2e188c00950be54472b58c960c
    decisions/2026-08-31-xi-rulings-03.md
      product 78b484282f3b3df5f9bba9dd6cbff6278713d0d3   source 78b484282f3b3df5f9bba9dd6cbff6278713d0d3
    decisions/P2-XI-RULINGS-03.issued.md
      product 0b331afb6f21f6591a0c3934fc8916bda742d8de   source 0b331afb6f21f6591a0c3934fc8916bda742d8de
    reports/2026-09-01T0135Z_xi-rulings-03-landing.md
      product 9e6195442b5eb1f8e7ed5a51b302335b4a7e5f31   source 9e6195442b5eb1f8e7ed5a51b302335b4a7e5f31
    reviews/chatgpt/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
      product 2d2248a0ccb984d7293e5ed586ed7c977c13bf74   source 2d2248a0ccb984d7293e5ed586ed7c977c13bf74
    reviews/chatgpt/2026-08-31_document-review_p2-xi-rulings-03.md
      product b1a3352fd8a1959737b7aa6c2b320ab4d231ed9b   source b1a3352fd8a1959737b7aa6c2b320ab4d231ed9b
    specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md
      product 7167ecfaa736f1179f0fbd9916020b553efc567d   source 7167ecfaa736f1179f0fbd9916020b553efc567d

    all seven equal — PASS

    (0,1) main-only  : class empty, nothing to compare
    (1,1) P_overlap  : EMPTY, measured over the classified union and not
                       inferred from the FORK = Base equality
    (0,0)            : 0

**`A5` does not fire on `(b)`.**

### `M3b(c)` — main-preservation sweep

    paths in P_main \ P_source : 0

**Recorded as measured, not skipped.** The sweep is vacuous here because
`P_main` is empty — `FORK = Base`, so no main-side path exists whose Base blob
the merge could displace. **The emptiness is the measured result of the
classification above, not a substitute for performing it.**

### `M3b(d)` — append-only re-verification of the one modified path

    DECISION_LOG.md
      Base bytes     146709
      product bytes  147675        appended 966
      the Base's bytes are an EXACT BYTE-PREFIX of the product's       PASS
      byte-for-byte equality re-tested over the whole prefix           PASS
      normalization applied to either side:  NONE

**The append-only character is re-verified by prefix relation, not assumed from
the status letter.** `A5` does not fire on `(d)`. **`C3b` PASS on every limb.**

## 3c. `M3c` — arrival-state verification of the ruling

**MEASUREMENT SUBSTRATE, stated.** Every probe is built from the merge product's
bytes via `git cat-file` / `git grep`, decoded UTF-8 and split on newlines. The
issued file carries **0 fenced blocks and 0 blockquote-prefixed lines**, measured
before any scan, so no fence or quote handling is applied. Emphasis wrapping is
not assumed: markers are matched against actual leading bytes. No character-offset
arithmetic is used. **Two probes failed against their own assumptions and were
re-measured; see §8a. No product byte was changed by either correction, and `A5`
was not declared on either false failure.**

### `(i)` the `SUPERSEDES` field, and no other landed occurrence

Present at `decisions/P2-XI-RULINGS-03.issued.md:8`; verbatim, **normalization
applied: NONE**:

```text
    SUPERSEDES  The document of the same identifier bearing SHA-256
                f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8,
                which was reviewed FIT FOR RECORDING but not landed.
                Its RATIONALE named the exponent mapping as the second
                element not fixed by landed text. That was wrong:
                P2-XI-QM3-DEP-01 records the exponent mapping as FIXED
                at g = +2c by DECISION_LOG.md:1258-1262, and names the
                decoupling prescription as the second unfixed element.
                The correction is confined to that RATIONALE; every
                RULING line is unchanged.
```

**THE ABSENCE CHECK, on the question it is actually asking: was the superseded
document ever landed before this transport?** Measured against the pre-existing
landed state at the Base:

    git grep -l 'f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8' <Base>
      0 hits
    git grep -l 'f59511b5' <Base>
      0 hits

    git log --all -S <the superseded digest>   ->  5 commits, and for each,
    git merge-base --is-ancestor <commit> <Base>:

      16cfb7b8…  NOT an ancestor of the Base   this task's own spec commit
      4eca6408…  NOT an ancestor of the Base   the source tip
      4e1378b1…  NOT an ancestor of the Base   the landing's register record
      1a8f9831…  NOT an ancestor of the Base   the landing's issued-bytes commit
      dc721410…  NOT an ancestor of the Base   the landing's spec commit

**No commit introducing that digest is an ancestor of the Base.**

**In the merge product**, every occurrence lies inside the arriving change set or
inside this task's own `M1b` provenance:

    decisions/2026-08-31-xi-rulings-03.md                  [arriving change set]
    decisions/P2-XI-RULINGS-03.issued.md                   [arriving change set]
    reports/2026-09-01T0135Z_xi-rulings-03-landing.md      [arriving change set]
    specs/2026-08-31T2200Z_xi-rulings-03-landing_v3.md     [arriving change set]
    specs/2026-09-01T0600Z_xi-rulings-03-integ_v2.md       [this task's M1b provenance]

**POSITIVE CONTROL**, same method and same tree, so the null results above are
distinguishable from a dead probe:

    '1a982547f6c4a25ab29ec2d02e8ba54fa3e89c68…'   6 hits    (expected present)
    'ZZZZNOTAREALDIGESTZZZZ'                      0 hits    (expected absent)

**The superseded document is not landed anywhere except as the `SUPERSEDES`
field inside the re-issued text and the records that quote it. No erratum,
clarification or supersession mechanism is engaged.**

### `(ii)` the corrected `RATIONALE`, against the landed determination table

`decisions/P2-XI-RULINGS-03.issued.md:82-93`, verbatim, **normalization applied:
NONE**:

```text
RATIONALE   P2-XI-QM3-DEP-01 found two elements not fixed by landed
            text: which channel or set of channels the assembled
            chain's decoupling comprises, and the decoupling
            prescription — auxiliary variables, constraints,
            Jacobian. This ruling fixes the first. The second is a
            prescription question and is not fixed by naming a
            channel. The exponent mapping is NOT among the unfixed
            elements: that same artifact records it as fixed by
            landed text at g = +2c, DECISION_LOG.md:1258-1262. On the
            Researcher's reading, recorded in that artifact's own
            symmetry statement, R-1 and R-2 together would return
            UNIQUELY IDENTIFIED and R-1 alone does not.
```

**The four content checks**, measured under a stated normalization: runs of
whitespace, **including line breaks and the continuation indent**, collapsed to a
single space, applied to the issued bytes alone so a phrase split across a line
cannot evade the probe. **That collapse is the only normalization applied.**

    names the channel as not fixed by landed text                     PASS
      matched "which channel or set of channels the assembled chain's
               decoupling comprises"
    names the decoupling prescription as the other                    PASS
      matched "the decoupling prescription — auxiliary variables,
               constraints, Jacobian"
    states the exponent mapping is NOT among them                     PASS
      matched "The exponent mapping is NOT among the unfixed elements"
    cites g = +2c at DECISION_LOG.md:1258-1262                        PASS
      matched "g = +2c, DECISION_LOG.md:1258-1262"

    POSITIVE CONTROL on the same flattened text:
      'This ruling fixes the first.'      found      (expected present)
      'NOT A PHRASE IN THIS DOCUMENT'     not found  (expected absent)

**The landed determination table in the merge product**,
`derivations/P2-XI-QM3-DEP-01_hs-jacobian-curvature-dependence.md:306-327`:

```text
Fixed by landed text, and recorded so:

    the exponent mapping     g = +2c, DECISION_LOG.md:1258-1262

Not fixed by landed text, each with its carrier quoted above:

    which channel or set of channels the assembled chain's decoupling
      comprises
```

with its second not-fixed entry:

```text
    the decoupling prescription — auxiliary variables, constraints,
      Jacobian
```

    the FIXED list carries the exponent mapping                       PASS
    the NOT-FIXED list does NOT carry the exponent mapping            PASS
    the NOT-FIXED list carries the channel                            PASS
    the NOT-FIXED list carries the decoupling prescription            PASS

**The arriving `RATIONALE` and the landed table agree on all three elements.**
This is the check whose failure stopped the v2 landing attempt under `A3`; on the
re-issued bytes it passes.

### `(iii)` `RULING 2` and `RULING 3`

`decisions/P2-XI-RULINGS-03.issued.md:56-66`, verbatim, **normalization: NONE**:

```text
## RULING 2 — What this ruling does not supply

RULING      This ruling names the channel and the auxiliary field. It
            does not fix the exponent convention, the g-to-c mapping,
            the constraints or contour, the functional-measure
            treatment, or the mathematical definition of the
            normalization object the landed criterion names. Those are
            the decoupling prescription. Until such a prescription is
            landed, the decoupling of the assembled chain is named but
            not fully specified, and P2-XI-QM3-DEP-01's determination
            stands.
```

**The determination-stands sentence is present.** And **"It does not fix"
predicates non-supply of this ruling** — it is not a claim that the named
elements are unfixed in the repository, and the `RATIONALE` records that landed
authority already fixes one of them. **The two are compatible and this task
flattens neither into the other.**

`decisions/P2-XI-RULINGS-03.issued.md:68-80`, verbatim, **normalization: NONE**:

```text
## RULING 3 — Authorization of the prescription task

RULING      A specification is authorized to land the decoupling
            prescription for the assembled chain in the sense
            P2-FIERZSUM-01.md:218-220 states — auxiliary variables,
            constraints, Jacobian, and an explicit statement of what
            is generated dynamically rather than introduced as an
            independent field. That task defines; it does not
            evaluate. It must not compute the curvature dependence of
            the normalization object, which remains the question
            P2-XI-QM3-DEP-01 was scoped to and which a re-run of that
            check, under a separate specification, is to answer. It
            must not resolve DET-01 or choose the functional measure.
```

    RULING 3 authorizes a prescription specification                  PASS
    its define-not-evaluate limit is present                          PASS
    its no-curvature-dependence limit is present                      PASS
    its DET-01 / functional-measure limit is present                  PASS

### `(iv)` the register record's quotations, against the issued file in the product

Each tested as a byte substring of the register record against the exact span of
the issued file **as it stands in the merge product**; **normalization applied to
either side: NONE.**

    issued span   what it is                    bytes   result
    ---------------------------------------------------------------
    :8-17         SUPERSEDES                      679   PASS
    :24-26        LAYERING                        185   PASS
    :39-54        RULING 1's three limits         955   PASS
    :58-66        RULING 2                        566   PASS
    :82-93        RATIONALE                       776   PASS
    PART 2        the review artifact, verbatim  6030   PASS

**`M3c` PASS on all four checks. `C3c` PASS.**

## 4. `M4` — suite

Run on a full, non-shallow tree.

**At the base**, tree `b429a1a3d92da9febecb8ae2b0eaaa945f56c92a`:

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 54.98s

**At the post-merge integration tree**, which is the tested tree:

    T = 1d781ef9af8dbc15a51423e9d506d0538337ea4e   (the tree of M_merge)

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 50.14s

Identical outcomes. **No test fails on `T` that passes at the base. `C4` PASS.**

**This report is the next commit on the tested tree above.**

---

## 5. Acceptance criteria

    C1  PASS  origin/main equals the Base; the merge-base equals the Base as a
              full-string match; the source tip equals the Source field, all 40
              hex characters.
    C2  PASS  M_merge has exactly two parents, the M1b tip and the source tip;
              the M1b tip descends from the base by exactly two commits, spec
              then review; the spec's sha256 equals the digest the review
              declares, recorded at M1b.
    C3  PASS  Seven of seven digests equal their expected values, plus the one
              expected blob id, all as full-string matches.
    C3b PASS  The contributed set is the seven-entry manifest with its stated
              statuses; the union classification assigns each of the seven
              P_union paths to exactly one class with its blob rule satisfied;
              P_overlap is empty as measured over the classified union; the
              main-preservation sweep is recorded as measured and vacuous; and
              the DECISION_LOG.md prefix relation holds with both lengths
              recorded in bytes.
    C3c PASS  All four arrival-state checks pass, each with its quoted text and
              its stated normalization; (i)'s null results are reported with
              their patterns and a live positive control.
    C4  PASS  344 passed and 2 deselected at the base and at T.
    C5  NOT YET REACHED at this commit. Its limbs are post-commit and post-push
              and are recorded on the M5 surface, not here.

## 6. Abort conditions

    A1  DID NOT FIRE.  Every M1 value agrees with the spec's Base, Source and
        stated merge-base relation, as full-string matches.
    A2  DID NOT FIRE.  The merge was conflict-free and M3 found no digest
        mismatch in the merge product.
    A3  EVALUATED AT PUSH TIME.  main stands at the Base, which is the first
        parent's ancestor and H_integ's ancestor, so the advance is expected to
        be a fast-forward; the measurement is made at push and recorded on the
        M5 surface.
    A4  DID NOT FIRE.  No file arriving from the source was modified and no ref
        of the source branch moved. The prescription-definition task RULING 3
        authorizes is not begun, scheduled, constrained, sequenced or
        represented as ready — §3c(iii) quotes the authorization and adds
        nothing about any task answering to it. The Q-M3 subject is not
        described as uniquely identified and its constructive gap is not
        described as closed or narrowed. "Not fixed by this ruling" is not
        flattened into "unfixed in the repository" or the converse; §3c(iii)
        records the two as compatible and keeps them apart. OPEN-AC-1 is not
        closed, the V/A representations are not excluded, the registered
        representation-stability item is untouched, and neither OPEN ledger row
        is disposed — none of those paths is in this task's change set.
    A5  DID NOT FIRE.  No contributed path or status outside §1a's manifest, no
        both-changed path, no source-unchanged path whose product blob differs
        from the Base's, no main-unchanged contributed path whose product blob
        differs from the source's, no failure of the DECISION_LOG.md prefix
        relation, and no M3c failure. Every null result in §3c(i) carries a live
        positive control. **The two probe failures recorded at §8a were defects
        of the probes, not of the product; per the specification's MEASUREMENT
        SUBSTRATE clause they were re-measured and recorded, and A5 was not
        declared on either.**

## 7. What arrives, stated as the arriving bytes state it

**The ruling is `decisions/P2-XI-RULINGS-03.issued.md`**, at
`1a982547f6c4a25ab29ec2d02e8ba54fa3e89c6871a80df395ac0d8b07418686`. The register
record and the `DECISION_LOG` index are filing infrastructure; the document
review is its own artifact. All arrive byte-exact.

**Landing an authorization is not exercising it.** `RULING 3` reaches `main` as
canonical authority. Nothing here begins, schedules, constrains, sequences or
represents as ready any task answering to it.

**`P2-XI-QM3-DEP-01`'s determination stands**, in `RULING 2`'s own words, quoted
at §3c(iii).

**The exponent mapping is not this ruling's to fix, and is already fixed
elsewhere.** Both facts are in the arriving bytes and both are recorded here
without collapsing either into the other.

**`OPEN-AC-1`, the deferred V/A representations, the registered
representation-stability item, and the two OPEN ledger rows are all untouched.**
None of their paths is in this task's change set.

## 8. Stops and clarifications (Amendment B)

Nothing stopped execution. One observation is recorded.

### 8a. Two `M3c` probes failed against their own assumptions and were re-measured

**Category: `OBSERVATION_METHOD_ERROR`, found and corrected inside this task,
before any conclusion was drawn.** Both are recorded because the specification
requires the correction to be recorded, and because each is a distinct way for a
probe to lie.

**Probe 1 — an exclusion set that omitted this task's own provenance.** The
absence check's first pass defined the permitted occurrences of the superseded
digest as the *source's* contributed paths alone. It therefore flagged
`specs/2026-09-01T0600Z_xi-rulings-03-integ_v2.md` as an occurrence "outside the
arriving change set". **That file is this task's own specification**, committed at
`M1b` one commit before the merge, whose §0a quotes the superseded digest by
design. It is not pre-existing landed state. **The probe's exclusion set was the
defect, not the product.** Re-measured on the question the check actually asks —
whether the superseded document was ever landed *before* this transport — the
Base returns 0 hits on both patterns, and no commit introducing the digest is an
ancestor of the Base. §3c(i) records the corrected measurement.

**Probe 2 — a contiguous-string search across a line wrap.** The `RATIONALE`
check's first pass searched for `'decoupling prescription — auxiliary variables'`
as a contiguous byte string and found none. The issued file wraps that phrase
across a line break with the continuation indented, so no such contiguous string
exists:

```text
            chain's decoupling comprises, and the decoupling
            prescription — auxiliary variables, constraints,
```

**The probe assumed no line wrap.** Re-measured with runs of whitespace including
line breaks collapsed to a single space — that collapse stated as the only
normalization — all four content checks pass, with a positive and a negative
control on the same flattened text. §3c(ii) records the corrected measurement.

**Neither correction changed a product byte**, and `A5` was declared on neither.
The general fault is the one this programme has now recorded four times running:
**a probe written against remembered structure rather than the bytes in front of
it fails against its own assumption, not against the evidence.** Probe 1 adds a
second face of it — an exclusion set drawn from memory of what "the change set"
means, rather than from what this task actually committed.

## 9. Rule 22

No result in this task is `INCONCLUSIVE`. The arriving `Q-M3` determination and
its classification are transported untouched; **this task issues no verdict of
its own and owes no subclass or resolution path.**

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

    to be pushed   refs/heads/science/integrate-xi-rulings-03
                   refs/heads/main, fast-forward to H_integ
    must not move  refs/heads/science/xi-rulings-03-landing
                   refs/heads/science/xi-qm2-scope-01
                   refs/heads/science/xi-qm3-dep-01
                   refs/heads/science/integrate-xi-qm2-scope-01
                   any other science, session or harness branch

**`M5`'s post-push evidence is not in this report and could not be**: `H_integ`,
the report-only diff against `T`, the push results and the post-push ref audit
all come into existence after this commit. They are recorded on the `M5` surface,
by the route the executor states there.

END OF REPORT
