# Report — `P2-XI-LEDGER-01-INTEG` v1: transport of the executed conditional ledger, with its count addendum, to `main`

    Specification   specs/2026-08-23T2100Z_xi-ledger-01-integ.md
    Review          reviews/chatgpt/2026-08-23T2100Z_xi-ledger-01-integ.md
    Branch          science/integrate-xi-ledger-01
    Base            main @ 6c1af3cace259663a288354b1725bdd923d3b1fc
    Source          science/xi-ledger-01 @
                    0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    Fork            9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Ruling pin      8f9edfead214b5bb3337924c18c5d241274e97c3
    Scope of file   `M1` through `M4`. **`M5` is post-push and is excluded by
                    construction**, recorded in the branch-only addendum.

**This report does not state its own commit SHA.** It is committed onto the
merge product `2e36e3153518681a5fc6c9c42205daec4339f384`, and **this report is
itself the next commit**; the tip after it is `H_integ`, whose value is recorded
in the addendum written after that commit exists.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/xi-ledger-01 @ 0101d65e
    repository is shallow   false
    UTC at report           2026-08-23T1925Z

## 0a. Pin versus source — the obligation this task inherits, carried verbatim

> The source of this integration is the pin plus the count addendum:
> `8f9edfead214b5bb3337924c18c5d241274e97c3` is the ledger state
> `P2-XI-RULINGS-02` was issued on;
> `0101d65ea581b0f6b08f1b0ca62969a51a7a16d1` is that state plus the
> branch-only addendum and its provenance commits. The
> addendum-bearing tip is NOT the state the ruling was issued on.

**The obligation originates in the addendum task's §10a and in this
specification's own Base state. This task discharges it by recording, not by
editing anything.** The same paragraph is carried verbatim in this task's merge
commit message. `M3c` measures that the pin's substantive content survives to
the merge product unchanged.

---

## 1. Bindings verified before any write

    ARTIFACT                     SHA-256                                                            BYTES
    integration specification    83884d351133e28ee0581b1ead3ee026f1150b48359528d4be0729fa6988ae9d   14673
    its pre-execution review     9472849418f4eb428efb9040e2795dcfe309f1efb38e4d83a4b773cc56ce91b8    5357

The review carries `Reviewed specification SHA-256` twice, at lines 4 and 127,
and `83884d351133e28ee0581b1ead3ee026f1150b48359528d4be0729fa6988ae9d` is the
only 64-hex string in it. It equals the specification's sha256 and the sha256 of
the committed spec blob at `3ee16d3`. Verdict `APPROVE FOR EXECUTION`. The
review has no pre-committed hash; the digest above is its first recorded one,
provenance transmitted by the PI in session.

---

## 2. `M1` — pre-merge ref audit, before any write

**From `git ls-remote origin`, full SHAs.**

    refs/heads/main                             6c1af3cace259663a288354b1725bdd923d3b1fc
    refs/heads/science/xi-ledger-01             0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    refs/heads/science/integrate-xi-rulings-02  fd3a112df30eb43a58f4c264169104c6b847225b

    origin/main vs Base    measured 6c1af3ca…  Base 6c1af3ca…      EQUAL
    source tip vs Source   measured 0101d65e…  Source 0101d65e…    EQUAL (full string)

**The fork, measured rather than assumed.** The source does NOT descend from the
Base:

    command   git merge-base 6c1af3cace259663a288354b1725bdd923d3b1fc \
                             0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    output    9eefe4c85c646b96ce334426598bc0e405f6e3d5
    stated    9eefe4c85c646b96ce334426598bc0e405f6e3d5
    EQUAL — FORK confirmed as a full-string match

    git merge-base --is-ancestor <Base> <source>   exits non-zero
      -> the Base is NOT an ancestor of the source, as the specification states
    commits Base..source   9
    commits source..Base   8

**The pin must be an ancestor of the source tip** — the check that makes "the
pin plus the addendum" a measured statement rather than a claim:

    command   git merge-base --is-ancestor \
                8f9edfead214b5bb3337924c18c5d241274e97c3 \
                0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    exit status  0  -> the pin IS an ancestor of the source tip
    commits pin..source   5

**`A1` did not fire.** The branch was cut only after every value above was
measured.

---

## 3. `M1b` — pre-execution provenance commits, before the merge

    1  branch cut     science/integrate-xi-ledger-01 at 6c1af3ca
    2  binding measured BEFORE the spec commit
                      spec file sha256  83884d35…6988ae9d
                      review declares   83884d35…6988ae9d    EQUAL
    3  spec commit    3ee16d3
    4  review commit  798edb2082a3adbe976968afdbc409f6574cee15

    M1b tip                 798edb2082a3adbe976968afdbc409f6574cee15
    commits base..M1b tip   2

    3ee16d3  spec(P2-XI-LEDGER-01-INTEG): transport of the executed conditional ledger, with its count addendum, to main
    798edb2  review(P2-XI-LEDGER-01-INTEG): ChatGPT pre-execution review, APPROVE FOR EXECUTION

**Nothing was committed between them.**

---

## 4. `M2` — merge construction

    M_merge      2e36e3153518681a5fc6c9c42205daec4339f384
    parent 1     798edb2082a3adbe976968afdbc409f6574cee15   (the M1b tip)
    parent 2     0101d65ea581b0f6b08f1b0ca62969a51a7a16d1   (the source tip)
    parent count 2
    merge-base of the two parents
                 9eefe4c85c646b96ce334426598bc0e405f6e3d5   (the FORK, re-measured
                                                             in the act of merging)

`--no-ff` per `BRANCHING_POLICY.md:29-30`. The merge added nine files and
changed nothing else.

**`A2`, first limb — conflict-free.** Unmerged paths: 0; working tree clean.
**No content was authored or resolved inside the merge.**

**The §0a paragraph is carried verbatim in the merge commit message**, as the
specification requires.

---

## 5. `M3` — arriving-blob verification, from the merge product

**Measured from `2e36e315`. Every digest in full, measured then expected.**

    derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
      measured  aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454
      expected  aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454   MATCH
    scripts/xi_ledger.py
      measured  97571fa0ef7bee8dbcdf06cb7117fa04eda0d6b2606322af08f0fe73879a695c
      expected  97571fa0ef7bee8dbcdf06cb7117fa04eda0d6b2606322af08f0fe73879a695c   MATCH
    tests/test_p2_xi_ledger.py
      measured  c0c6a6d26f3138191487564505043eeb0d4b02a45aae4ea241ee4e66a472a31b
      expected  c0c6a6d26f3138191487564505043eeb0d4b02a45aae4ea241ee4e66a472a31b   MATCH
    specs/2026-08-23T0600Z_xi-ledger-01_v3.md
      measured  b1120556eaf6d5c9e77048efbd84ba113b58ad0d932991ba54c8d9b64f6dbe17
      expected  b1120556eaf6d5c9e77048efbd84ba113b58ad0d932991ba54c8d9b64f6dbe17   MATCH
    reviews/chatgpt/2026-08-23T0600Z_xi-ledger-01_v3.md
      measured  de3556a97a51c92e9e77e4561ba4ce9d3933d8d439ee7831ce56997e265b13a2
      expected  de3556a97a51c92e9e77e4561ba4ce9d3933d8d439ee7831ce56997e265b13a2   MATCH
    reports/2026-08-23T0434Z_xi-ledger-01.md
      measured  1b234b5e14b137406ba336c5ba97427d562ecdb074f49c1d7d778f5e2676b049
      expected  1b234b5e14b137406ba336c5ba97427d562ecdb074f49c1d7d778f5e2676b049   MATCH
    specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
      measured  7a924f143c82dfaac8a971e6f4ead5ca94c2313cdd8f449510c746a4ead32416
      expected  7a924f143c82dfaac8a971e6f4ead5ca94c2313cdd8f449510c746a4ead32416   MATCH
    reviews/chatgpt/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
      measured  6c9648a7f01e89d00cc429eb6c9ae5baf38cf6360d386ce4415a019d877f67ee
      expected  6c9648a7f01e89d00cc429eb6c9ae5baf38cf6360d386ce4415a019d877f67ee   MATCH
    reports/2026-08-23T1909Z_xi-ledger-01-count-addendum.md
      measured  481ce13a46697ef72ab111cc17977fb9e7e4cd81296df155bdb90e9be83456fd
      expected  481ce13a46697ef72ab111cc17977fb9e7e4cd81296df155bdb90e9be83456fd   MATCH

**`A2`, second limb — no digest mismatch.** The two arriving specifications'
digests are also the digests their own bound reviews declare, so those bindings
re-verify as a by-product.

---

## 6. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK     9eefe4c85c646b96ce334426598bc0e405f6e3d5  (the M1 merge-base)
    SOURCE   0101d65ea581b0f6b08f1b0ca62969a51a7a16d1
    BASE     6c1af3cace259663a288354b1725bdd923d3b1fc
    PRODUCT  2e36e3153518681a5fc6c9c42205daec4339f384

### 6a. `M3b(a)` — contributed path set

`git diff --name-status FORK..SOURCE`, verbatim:

```
A	derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
A	reports/2026-08-23T0434Z_xi-ledger-01.md
A	reports/2026-08-23T1909Z_xi-ledger-01-count-addendum.md
A	reviews/chatgpt/2026-08-23T0600Z_xi-ledger-01_v3.md
A	reviews/chatgpt/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
A	scripts/xi_ledger.py
A	specs/2026-08-23T0600Z_xi-ledger-01_v3.md
A	specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
A	tests/test_p2_xi_ledger.py
```

    entries                                  9
    status A                                 9
    statuses other than A                    0
    paths outside the nine-path manifest     none

**The contributed set equals the manifest exactly.** Note the addendum's edit to
`reports/2026-08-23T0434Z_xi-ledger-01.md` shows as `A` here and not `M`,
because the path did not exist at the FORK — it is contributed whole,
addendum included. **No `M`, `D`, or `R` status appears**, so the all-`A` rule
holds without exception.

### 6b. `M3b(b)` — union classification

`P_source` (`FORK..SOURCE`) — the nine paths above, `|P_source| = 9`.

`P_main` (`FORK..BASE`), verbatim:

```
DECISION_LOG.md
decisions/2026-08-23-xi-rulings-02.md
decisions/P2-XI-RULINGS-02.issued.md
reports/2026-08-23T1540Z_xi-rulings-02-landing.md
reports/2026-08-23T1903Z_xi-rulings-02-integ.md
reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
reviews/chatgpt/2026-08-23T1800Z_xi-rulings-02-integ.md
reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
specs/2026-08-23T1800Z_xi-rulings-02-integ.md
```

    |P_main| = 10

    |P_union| = 19
    (1,0) source-only       9
    (0,1) main-only        10
    (1,1) both-changed      0     <- P_overlap
    (0,0)                   0
    9 + 10 + 0 + 0 = 19 = |P_union| — exclusive and exhaustive

**`(1,0)` source-only — product blob equals the SOURCE blob, pairwise:**

    derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md   e37ca94cbf10a1dc4f80dc6eb0b40dfab7d44839  EQUAL
    reports/2026-08-23T0434Z_xi-ledger-01.md                     5011628343b80428b0b4e957d3209afdb2c0f07e  EQUAL
    reports/2026-08-23T1909Z_xi-ledger-01-count-addendum.md      c20ea4762b169a96a575d8488f8fafe041ed62f1  EQUAL
    reviews/chatgpt/2026-08-23T0600Z_xi-ledger-01_v3.md          7f3e551cfdb6e8b338ca652605b05c5b49a635dd  EQUAL
    reviews/chatgpt/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md
                                                                 f5a2fa4c274b66fc9416e20ceaba58aadc309fc2  EQUAL
    scripts/xi_ledger.py                                         47a8381ab4ac9b1d50650321feca331697acc644  EQUAL
    specs/2026-08-23T0600Z_xi-ledger-01_v3.md                    9284c05d933b23a7a548396ad9a9b117499e2438  EQUAL
    specs/2026-08-23T1800Z_xi-ledger-01-count-addendum_v2.md     5da5bb66d8d606e4ca56ae2f16b054259c708874  EQUAL
    tests/test_p2_xi_ledger.py                                   46a9f0f58dcd2b733114e29a60dd999f474b5ae7  EQUAL

**`(0,1)` main-only — product blob equals the BASE blob, pairwise:**

    DECISION_LOG.md                                              5879d746b8b1530e4370fd6b5ed8f0be9f47bcd0  EQUAL
    decisions/2026-08-23-xi-rulings-02.md                        9c16433e150ed81d13232521a0923db643f3db25  EQUAL
    decisions/P2-XI-RULINGS-02.issued.md                         72a6b24c9289efde8a096e4e591ff01728323473  EQUAL
    reports/2026-08-23T1540Z_xi-rulings-02-landing.md            d49292a8e5e799ac7335f8468a1cdb6ded06fadf  EQUAL
    reports/2026-08-23T1903Z_xi-rulings-02-integ.md              97079c736a38c33b8bf36a6e8d4e8577f8f77151  EQUAL
    reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md 0584d6b9f7338c9326cba58b29339b23d9b098a1  EQUAL
    reviews/chatgpt/2026-08-23T1800Z_xi-rulings-02-integ.md      15809fccd5d6eb1a6f8f7d33b8494e8f58edf1b2  EQUAL
    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
                                                                 7bc4bdc4551540d7d6c50c73457aef717271c9a0  EQUAL
    specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md           0daee554749c5a87ca92483332016f38842445ba  EQUAL
    specs/2026-08-23T1800Z_xi-rulings-02-integ.md                9a475064c867811c8e329f46199812b7d538f20b  EQUAL

**`(1,1)` both-changed — `P_overlap` = `[]`, `|P_overlap| = 0`, EMPTY as
pre-registered.** Measured by testing each of the 19 classified union paths for
membership in both changed-sets; none returned `(1,1)`. **Not inferred from fork
distance.**

### 6c. `M3b(c)` — main-preservation sweep, NON-VACUOUS

    swept paths (P_main \ P_source)   10

**Every one of the ten main-changed paths retains the Base blob in the merge
product** — the pairs are the `(0,1)` block above, each `EQUAL`, and are not
repeated.

**This is the check that matters here, and it is not a formality.** The source
branch forked at `9eefe4c8`, **before `P2-XI-RULINGS-02` was landed and before
that landing was integrated.** A stale source merged carelessly could have
reverted the issued PI ruling, its register record, its document review, the
`DECISION_LOG.md` append, and both preceding tasks' artifacts. **None was walked
back.** The issued ruling's blob id in the product is
`72a6b24c9289efde8a096e4e591ff01728323473` — the same object whose sha256 the
landing verified against the PI's issuance identity.

**`A5` did not fire on any `M3b` limb.**

---

## 7. `M3c` — pin-content survival

### 7a. `M3c(i)` — the ledger artifact is byte-identical to the pin's

    derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md
      sha256 at the pin       aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454
      sha256 in the product   aa0c79e21568b09d6efed64ec538c1ee9b4892ebc65653cb76deecfbd25f1454
      blob id at the pin      e37ca94cbf10a1dc4f80dc6eb0b40dfab7d44839
      blob id in the product  e37ca94cbf10a1dc4f80dc6eb0b40dfab7d44839
      BYTE-IDENTICAL

**The addendum touched only the execution report, and this measurement confirms
it from the other side:** the ledger artifact the ruling was issued on arrives
on `main` unchanged, to the byte.

### 7b. `M3c(ii)` — the pin's report bytes are an exact prefix of the product's

    reports/2026-08-23T0434Z_xi-ledger-01.md
      at the pin        21830 bytes
      sha256 at the pin 93ed8caf14d23ddc35d224d4bcc9bcf7b1a3b7c082535be78a6fd4c4841e8959
      the specification expects
                        93ed8caf14d23ddc35d224d4bcc9bcf7b1a3b7c082535be78a6fd4c4841e8959   MATCH
      in the product    24498 bytes
      sha256            1b234b5e14b137406ba336c5ba97427d562ecdb074f49c1d7d778f5e2676b049
      the pin's bytes are an exact byte-prefix of the product's:   True
      appended          2668 bytes

**The addendum appended and rewrote nothing.** Every byte the report had at the
pin survives unchanged and in place.

### 7c. `M3c(iii)` — the two OPEN rows, present and valueless

Quoted verbatim from the merge product's ledger artifact, lines 304–309:

```text
    ------------------------------------------------------------------------------------------------
    condensate scalar's own                 —                            —     OPEN(Q-M2)
      fluctuation loop
    Hubbard–Stratonovich Jacobian /         —                            —     OPEN(Q-M3)
      normalization term
    ------------------------------------------------------------------------------------------------
```

    OPEN(Q-M2) occurrences in the product's ledger artifact   1
    OPEN(Q-M3) occurrences                                    1
    numeric cells on both rows                                em-dash, both columns

**Both rows arrive OPEN, valueless, and unannotated.** `P2-XI-RULINGS-02` is
already canonical on `main` and **defers** membership; nothing in this
integration marks either row disposed, and no retrospective cross-reference was
inserted into the historical ledger artifact — which `M3c(i)`'s byte-identity
proves could not have happened.

---

## 8. `M4` — suite, on a full tree, at both ends

    BASE
      commit     6c1af3cace259663a288354b1725bdd923d3b1fc
      tree SHA   c08a25ef7234377a39d5d3dc9f2b3675dcb328ee
      shallow    false
      result, verbatim   332 passed, 2 deselected in 48.31s

    POST-MERGE INTEGRATION TREE
      commit     2e36e3153518681a5fc6c9c42205daec4339f384
      tree SHA   4ac5b819fea15ecf021dc92b6c8492e4928aaba6
      shallow    false
      result, verbatim   344 passed, 2 deselected in 48.35s

**No test fails on the post-merge tree that passes at the base.** Both failure
sets are empty. **The count rose by 12** — the arriving
`tests/test_p2_xi_ledger.py` — and **the criterion is regression, not a count**:
tests contributed by the source do not by themselves constitute one.

---

## 9. `M4b` — report commit and the final tip

This file is the report. **It is committed onto `2e36e315`, and it is itself the
next commit; the tip after it is `H_integ`.** Per the specification this report
**does not state its own commit SHA** — that value is recorded in the addendum,
written after the commit exists.

**No suite re-run is required and none was made:** `H_integ` differs from the
tested tree only by this report artifact. **That difference is measured, not
asserted** — the `git diff --stat` is in the addendum.

---

## 10. Acceptance criteria

`C5` is post-push and is evaluated in the branch-only addendum.

    C1  (M1)      PASS   origin/main equals the Base; the merge-base equals
                         9eefe4c8… as a full-string match; the source tip
                         equals the Source field; and the pin is an ancestor of
                         the source tip (exit 0, 5 commits pin..source).
    C2  (M1b, M2) PASS   M_merge 2e36e315 has exactly two parents, the M1b tip
                         798edb20 first and the source tip 0101d65e second; the
                         M1b tip descends from the base by exactly two commits,
                         spec then review; the spec's sha256 equals the digest
                         the review declares, measured at M1b before the spec
                         commit.
    C3  (M3)      PASS   All nine digests equal their expected values as full
                         64-character string matches.
    C3b (M3b)     PASS   The contributed set equals the nine-path manifest with
                         status A throughout (§6a); the union classification
                         assigns each of the 19 P_union paths to exactly one
                         class with its blob rule satisfied (§6b); the measured
                         P_overlap is empty; and the main-preservation sweep
                         records product blob equal to Base blob for each of
                         the 10 swept paths, pairwise (§6c).
    C3c (M3c)     PASS   The ledger artifact is byte-identical to the pin's
                         (§7a); the pin's report bytes are an exact prefix of
                         the product's (§7b); both OPEN rows are present,
                         valueless, and quoted (§7c).
    C4  (M4)      PASS   on its first limb: no test fails on the post-merge
                         tree that passes at the base. **Its second limb — that
                         H_integ differs from the tested tree only by the
                         report — is measured in the addendum.**
    C6  (M4b)     PASS   §0a's pin-versus-source paragraph appears verbatim in
                         this report, and the report does not assert its own
                         commit SHA — §9 names the tip it is committed onto and
                         records that it is itself the next commit.

---

## 11. Abort conditions

    A1  DID NOT FIRE   Every M1 value agrees with the Base, the Source, the
                       stated merge-base, and the pin-ancestry relation. All
                       measured before the branch existed.
    A2  DID NOT FIRE   Conflict-free merge (0 unmerged paths, clean tree) and
                       no digest mismatch among the nine.
    A3  NOT YET REACHED at this commit; evaluated at push time, recorded in the
                       addendum.
    A4  DID NOT FIRE   No step modified the source branch or any file arriving
                       from it — §6b's source-only block shows each arriving
                       file's product blob equal to its source blob, and
                       §7a/§7b show the pin's content surviving byte-for-byte.
                       **Neither OPEN row was disposed, valued, annotated, or
                       cross-referenced** — §7c quotes them arriving intact, and
                       §7a's byte-identity is the proof that no retrospective
                       annotation could have been inserted. **Neither task
                       `P2-XI-RULINGS-02` authorizes was begun, scheduled, or
                       constrained.** **The arriving `ξ(G) | COND-1..4`
                       assembly was not relabelled, summarised, or
                       condition-stripped** — this report quotes the label
                       intact and draws no survival conclusion from it.
    A5  DID NOT FIRE   No contributed path or status outside the manifest; no
                       both-changed path; no source-unchanged path whose
                       product blob differs from the Base's; no main-unchanged
                       contributed path whose product blob differs from the
                       source's; and no M3c failure on any of its three limbs.

---

## 12. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session; nothing here
    needs it
    repository non-shallow at both suite runs

---

## 13. Stops and clarifications (Amendment B)

**Primary category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — two items
recorded, neither resolved here.

### 13a. The chronology inverts on `main`, and that is the record

**The ledger measurement predates the PI ruling. The ruling reached `main`
first.** After this integration `main` carries both, in the reverse of the order
they were made.

**Nothing was done to hide or repair that.** The register record's chronology
statement is on `main` unchanged; the ledger artifact arrives byte-identical to
the state the ruling was issued on; and **no cross-reference was inserted into
the historical ledger artifact to reconcile the two** — which `M3c(i)`'s
byte-identity makes checkable rather than merely asserted.

**The pin remains the referent for the ruling's subject.** `8f9edfea` is an
ancestor of what landed here (measured, `M1`, 5 commits back from the source
tip), so the ledger state the ruling was issued on is now recoverable from
`main`'s history — while the addendum-bearing tip that also landed is **not**
that state, and this report says so verbatim at §0a.

### 13b. What arrived without a verdict

**The two OPEN rows arrived OPEN and remain so.** `main` now carries, together:
a conditional assembly with two valueless rows; a landed PI ruling deferring
their membership and authorizing two tasks; and **no progress on either task**.
That is the intended state, not an omission.

**No verdict travelled.** Every total on `main` from this task is labelled
`ξ(G) | COND-1..4`; no condition was stripped and no survival conclusion drawn.

### 13c. Rule 22

**No `INCONCLUSIVE` was recorded.** Every measurement returned a value: three
remote ref SHAs, one merge-base output, two ancestry exit statuses, two binding
digests, four commit SHAs, nine artifact digests, two path sets, nineteen
classified paths with their blob-id pairs, ten sweep pairs, three `M3c`
comparisons, and two suite results.

---

## 14. Push scope

Per `M5` and `BRANCHING_POLICY.md:34-37`, in this order: push the integration
branch; advance `refs/heads/main` by fast-forward to `H_integ` and push; run the
post-push ref audit; commit its output as an addendum **on the integration
branch ONLY**, with `origin/main` remaining `H_integ`.

**The source branch `science/xi-ledger-01` must not move, and
`science/integrate-xi-rulings-02` must not move.** Both are re-verified against
their `M1` values in the addendum.
