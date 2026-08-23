# Report — `P2-XI-RULINGS-02-INTEG`: transport of the executed ruling landing to `main`

    Specification   specs/2026-08-23T1800Z_xi-rulings-02-integ.md
    Review          reviews/chatgpt/2026-08-23T1800Z_xi-rulings-02-integ.md
    Branch          science/integrate-xi-rulings-02
    Base            main @ 9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Source          science/xi-rulings-02-landing @
                    6c7a1f7238273214f87fe0d9b76111a7e5f45a6c
    Scope of file   `M1` through `M4`. **`M5` is post-push and is excluded from
                    this file by construction**, recorded in the branch-only
                    addendum.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/xi-rulings-02-landing @ 6c7a1f72
    repository is shallow   false
    UTC at report           2026-08-23T1903Z

## 0a. Ordering against the concurrently supplied addendum task

**Two specifications were supplied together.** `P2-XI-LEDGER-01-COUNT-ADDENDUM`
moves the tip of `science/xi-ledger-01`, a ref this task records at `M1` and
re-verifies unmoved at `M5`.

**This integration was executed FIRST, to completion, before that task began.**
The two are therefore sequential and not interleaved, and this task's `C5`
comparison is against a ref that did not move during it. The Reviewer's §8
contemplates the other order too — "whether unchanged or later advanced by
another authorized task" — but running this first keeps
`science/xi-ledger-01` at the pin throughout the very task that lands the
register record quoting that pin, which is the simplest state to audit.

---

## 1. Bindings verified before any write

    ARTIFACT                     SHA-256                                                            BYTES
    integration specification    3672a9126e3bba40817d186f04346ddb2111301d69f186638f0745c016d6f69c   11580
    its pre-execution review     cacd8b1ef6594b448ee8eb9cbbcbc2205592f57cf893f5fa543ba3b035fc09b6    4745

The review carries `Reviewed specification SHA-256` twice, at lines 4 and 120,
and `3672a9126e3bba40817d186f04346ddb2111301d69f186638f0745c016d6f69c` is the
only 64-hex string in it. It equals the specification's sha256 and the sha256
of the committed spec blob at `44778d9`. Verdict `APPROVE FOR EXECUTION`. The
review has no pre-committed hash; the digest above is its first recorded one,
provenance transmitted by the PI in session.

---

## 2. `M1` — pre-merge ref audit, before any write

**From `git ls-remote origin`, full SHAs.**

    refs/heads/main                          9eefe4c85c646b96ce334426598bc0e405f6e3d5
    refs/heads/science/xi-rulings-02-landing 6c7a1f7238273214f87fe0d9b76111a7e5f45a6c
    refs/heads/science/xi-ledger-01          8f9edfead214b5bb3337924c18c5d241274e97c3

    origin/main vs Base       measured 9eefe4c8…  Base 9eefe4c8…    EQUAL
    source tip vs Source      measured 6c7a1f72…  Source 6c7a1f72…  EQUAL (full string)

**The topology was measured, not assumed.** The specification states the source
descends from the Base; that is a claim this task checks:

    command   git merge-base 9eefe4c85c646b96ce334426598bc0e405f6e3d5 \
                             6c7a1f7238273214f87fe0d9b76111a7e5f45a6c
    output    9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Base      9eefe4c85c646b96ce334426598bc0e405f6e3d5
    EQUAL — the merge-base IS the Base, as a full-string match

    git merge-base --is-ancestor <Base> <source>   exit 0 — Base IS an ancestor
    commits Base..source                           4

**`science/xi-ledger-01` recorded at `8f9edfead214b5bb3337924c18c5d241274e97c3`.**
Per the Reviewer's §13 execution note this SHA is **ref-state evidence only and
is not a replacement for the ruling subject pin**; the authoritative subject
remains the commit the landed register record identifies, which happens to be
the same value here and remains so regardless of any later authorized movement
of the branch.

**`A1` did not fire.** The branch was cut only after every value above was
measured.

---

## 3. `M1b` — pre-execution provenance commits, before the merge

    1  branch cut     science/integrate-xi-rulings-02 at 9eefe4c8
    2  binding measured BEFORE the spec commit
                      spec file sha256  3672a912…016d6f69c
                      review declares   3672a912…016d6f69c    EQUAL
    3  spec commit    44778d9
    4  review commit  cc2ec5af50d7419990c285355a5488905536e8ae

    M1b tip                 cc2ec5af50d7419990c285355a5488905536e8ae
    commits base..M1b tip   2

    44778d9  spec(P2-XI-RULINGS-02-INTEG): transport of the executed ruling landing to main
    cc2ec5a  review(P2-XI-RULINGS-02-INTEG): ChatGPT pre-execution review, APPROVE FOR EXECUTION

**Nothing was committed between them.**

---

## 4. `M2` — merge construction

    M_merge      ee2cabd3d5b5c683f2c5e1d267394d2781290a25
    parent 1     cc2ec5af50d7419990c285355a5488905536e8ae   (the M1b tip)
    parent 2     6c7a1f7238273214f87fe0d9b76111a7e5f45a6c   (the source tip)
    parent count 2
    merge-base of the two parents
                 9eefe4c85c646b96ce334426598bc0e405f6e3d5   (the Base, re-measured
                                                             in the act of merging)

`--no-ff` per `BRANCHING_POLICY.md:29-30`.

**`A2`, first limb — conflict-free.** Unmerged paths: 0; working tree clean.
**No content was authored or resolved inside the merge.**

---

## 5. `M3` — arriving-blob verification, from the merge product

**Measured from `ee2cabd3`. Every digest in full, measured then expected.**

    decisions/P2-XI-RULINGS-02.issued.md
      measured sha256   ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
      expected sha256   ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
      measured blob id  72a6b24c9289efde8a096e4e591ff01728323473
      expected blob id  72a6b24c9289efde8a096e4e591ff01728323473
      MATCH

    decisions/2026-08-23-xi-rulings-02.md
      measured  cf39e8999dd5d8c1c284cd3ef0c37bcc499959f358f02f4ad189e5d5b5b7d758
      expected  cf39e8999dd5d8c1c284cd3ef0c37bcc499959f358f02f4ad189e5d5b5b7d758   MATCH

    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
      measured  d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49
      expected  d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49   MATCH

    specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
      measured  c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da4750f926a14cc5
      expected  c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da4750f926a14cc5   MATCH

    reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
      measured  fafca91a0cfdc9a85e888509004958d0427ad537c073faf11b8b3c130fc274df
      expected  fafca91a0cfdc9a85e888509004958d0427ad537c073faf11b8b3c130fc274df   MATCH

    reports/2026-08-23T1540Z_xi-rulings-02-landing.md
      measured  e7c0cece291f22cc761836f404769c147c2dc6ecdda4b42b762fb814f2a945e3
      expected  e7c0cece291f22cc761836f404769c147c2dc6ecdda4b42b762fb814f2a945e3   MATCH

**`A2`, second limb — no digest mismatch.** The issued ruling retains both its
sha256 and its git blob identity through the merge; **the PI ruling was not
re-authored, paraphrased, or reinterpreted.**

---

## 6. `M3b` — fork-aware merge-hazard audit, from the merge product

    FORK     9eefe4c85c646b96ce334426598bc0e405f6e3d5  (the M1 merge-base, = Base)
    SOURCE   6c7a1f7238273214f87fe0d9b76111a7e5f45a6c
    BASE     9eefe4c85c646b96ce334426598bc0e405f6e3d5
    PRODUCT  ee2cabd3d5b5c683f2c5e1d267394d2781290a25

### 6a. `M3b(a)` — contributed path set

`git diff --name-status FORK..SOURCE`, verbatim:

```
M	DECISION_LOG.md
A	decisions/2026-08-23-xi-rulings-02.md
A	decisions/P2-XI-RULINGS-02.issued.md
A	reports/2026-08-23T1540Z_xi-rulings-02-landing.md
A	reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
A	reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
A	specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
```

    entries                                7
    status A                               6
    status M                               1, on DECISION_LOG.md
    any status outside {A, M}              0
    any SECOND M                           none
    paths outside §1a's seven-entry manifest   none

**The contributed set equals §1a's manifest exactly**: the six `A` paths of
`M3`, plus `DECISION_LOG.md` at `M`. **No second `M`, no `D`, no `R`.** No
manifest expansion was needed, and the specification admits none.

### 6b. `M3b(b)` — union classification

`P_source` (`FORK..SOURCE`), verbatim — the seven paths above, `|P_source| = 7`.

`P_main` (`FORK..BASE`), verbatim:

```
(empty — the command produced no output)
```

    |P_main| = 0

    |P_union| = 7
    (1,0) source-only      7
    (0,1) main-only        0
    (1,1) both-changed     0     <- P_overlap
    (0,0)                  0
    7 + 0 + 0 + 0 = 7 = |P_union| — the classes are exclusive and exhaust it

**`(1,0)` source-only — product blob must equal the SOURCE blob:**

    DECISION_LOG.md                                          5879d746b8b1530e4370fd6b5ed8f0be9f47bcd0  EQUAL
    decisions/2026-08-23-xi-rulings-02.md                     9c16433e150ed81d13232521a0923db643f3db25  EQUAL
    decisions/P2-XI-RULINGS-02.issued.md                      72a6b24c9289efde8a096e4e591ff01728323473  EQUAL
    reports/2026-08-23T1540Z_xi-rulings-02-landing.md         d49292a8e5e799ac7335f8468a1cdb6ded06fadf  EQUAL
    reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
                                                              0584d6b9f7338c9326cba58b29339b23d9b098a1  EQUAL
    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
                                                              7bc4bdc4551540d7d6c50c73457aef717271c9a0  EQUAL
    specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md        0daee554749c5a87ca92483332016f38842445ba  EQUAL

each compared pairwise, product blob against source blob.

**`(0,1)` main-only — class empty; nothing to compare.**

**`(1,1)` both-changed — `P_overlap` = `[]`, `|P_overlap| = 0`, EMPTY as
pre-registered.**

**Emptiness is a measured comparison over the classified union, NOT an
inference from `FORK == Base`.** Each of the seven union paths was tested for
membership in both changed-sets; none returned `(1,1)`. Had one, `A5` would
have fired with all four blob ids — fork, source, Base, product.

### 6c. `M3b(c)` — main-preservation sweep

    swept paths (P_main \ P_source)   0   — VACUOUS

**Recorded as measured rather than skipped**, per the specification's "Expected
vacuous; record it as measured". The sweep set was computed and found empty; it
was not assumed empty from the topology.

### 6d. `M3b(d)` — append-only re-verification of the one modified path

**`DECISION_LOG.md` carries status `M`. That letter is not treated as safe.**

    Base DECISION_LOG.md bytes                              135360
    merge-product bytes                                     138776
    bytes added                                               3416
    base bytes are an exact byte-prefix of the product        True

**The prefix relation is the evidence, not the status letter.** No pre-existing
`DECISION_LOG.md` byte survives the merge altered.

**`A5` did not fire on any limb.**

---

## 7. `M4` — suite, on a full tree, at both ends

    BASE
      commit     9eefe4c85c646b96ce334426598bc0e405f6e3d5
      tree SHA   16d79bf232c02c11a7209595140f7f7d6d290114
      shallow    false
      result, verbatim   332 passed, 2 deselected in 54.48s

    POST-MERGE INTEGRATION TREE
      commit     ee2cabd3d5b5c683f2c5e1d267394d2781290a25
      tree SHA   e89bfcec738a307e5d5737311bbc98305f50db87
      shallow    false
      result, verbatim   332 passed, 2 deselected in 47.15s

**No test fails on the post-merge tree that passes at the base.** Both failure
sets empty; counts identical, as expected for a task that adds no code.

---

## 8. `M4b` — report commit and the final tip

This file is the report. **The tip after this commit is `H_integ`.**

**No suite re-run is required and none was made.** The suite was measured on the
post-merge tree, and `H_integ` differs from that tested tree only by this report
artifact. **That difference is measured, not asserted** — the `git diff --stat`
is recorded in the addendum, written after `H_integ` exists.

---

## 9. Acceptance criteria

`C5` is post-push and is evaluated in the branch-only addendum.

    C1  (M1)      PASS   origin/main equals the Base; the merge-base equals the
                         Base as a full-string match; the source tip equals the
                         Source field in full.
    C2  (M1b, M2) PASS   M_merge ee2cabd3 has exactly two parents, the M1b tip
                         cc2ec5af first and the source tip 6c7a1f72 second; the
                         M1b tip descends from the base by exactly two commits,
                         spec then review; the spec's sha256 equals the digest
                         the review declares, measured at M1b before the spec
                         commit.
    C3  (M3)      PASS   All six digests equal their expected values as full
                         64-character string matches, plus the issued ruling's
                         git blob id.
    C3b (M3b)     PASS   The contributed set equals the seven-entry manifest
                         with its stated statuses (§6a); the union
                         classification assigns each of the 7 P_union paths to
                         exactly one class with its blob rule satisfied (§6b);
                         the measured P_overlap is empty; the
                         main-preservation sweep is recorded as measured and
                         vacuous (§6c); and the DECISION_LOG.md prefix
                         relation holds (§6d).
    C4  (M4)      PASS   on its first limb: no test fails on the post-merge
                         tree that passes at the base. **Its second limb — that
                         H_integ differs from the tested tree only by the
                         report — is measured in the addendum.**

---

## 10. Abort conditions

    A1  DID NOT FIRE   Every M1 value agrees with the Base, the Source, and the
                       stated merge-base relation. Checks ran before the branch
                       existed.
    A2  DID NOT FIRE   Conflict-free merge (0 unmerged paths, clean tree) and
                       no digest mismatch in the merge product.
    A3  NOT YET REACHED at this commit; evaluated at push time and recorded in
                       the addendum. The Base is an ancestor of the integration
                       branch by construction.
    A4  DID NOT FIRE   No step modified the source branch or any file arriving
                       from it — §6b's source-only block shows each arriving
                       file's product blob equal to its source blob — and
                       **neither task the arriving ruling authorizes was begun,
                       scheduled, or constrained.** No specification was
                       drafted for either; no method, precondition, ordering
                       beyond the issued RULING 4, or scope was added; and the
                       ruling's scientific content is not reinterpreted
                       anywhere in this task's artifacts.
    A5  DID NOT FIRE   On every limb: no contributed path or status outside
                       §1a's manifest; no second M; no path in the both-changed
                       class; no source-unchanged path whose product blob
                       differs from the Base's; no main-unchanged contributed
                       path whose product blob differs from the source's; and
                       the DECISION_LOG.md prefix relation holds.

---

## 11. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session; nothing here
    needs it
    repository non-shallow at both suite runs

---

## 12. Stops and clarifications (Amendment B)

**Primary category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — two items
recorded, neither resolved here because resolving them is not this task's.

### 12a. The ruling's subject is still not on `main`

`P2-XI-RULINGS-02` disposes the two OPEN rows of `P2-XI-LEDGER-01`. **After
this integration, `main` carries the ruling but still not the ledger.** The
landed register record states that chronology at its §4, with the full-SHA
referent, and this task changes nothing about it.

**The subject pin is unaffected by anything this task did**, and — as the
Reviewer's §8 and §13 both note — **it is also unaffected by any later
authorized movement of `science/xi-ledger-01`.** A pin denotes a commit, not a
branch tip. The concurrently supplied addendum task moves that tip; **the pin
`8f9edfead214b5bb3337924c18c5d241274e97c3` continues to denote the ledger state
the ruling was issued on**, and the later ledger integration must preserve that
distinction.

### 12b. Landing authority is not exercising it

**Neither authorized task was begun.** `main` now carries the authority for the
`Q-M3` dependence check and the `Q-M2` scope assessment; **it carries no
progress on either**, and this task added none. Each remains a separate
specification subject to the normal pre-execution review gate.

### 12c. Rule 22

**No `INCONCLUSIVE` was recorded.** Every measurement returned a value: three
remote ref SHAs, one merge-base output, one ancestor exit status, two binding
digests, four commit SHAs, six artifact digests with one blob id, two path sets,
seven classified paths with their blob-id pairs, one vacuous sweep, one prefix
relation with its byte counts, and two suite results.

---

## 13. Push scope

Per `M5` and `BRANCHING_POLICY.md:34-37`, in this order: push the integration
branch; advance `refs/heads/main` by fast-forward to `H_integ` and push; run
the post-push ref audit; commit its output as an addendum **on the integration
branch ONLY**, with `origin/main` remaining `H_integ`.

**The source branch `science/xi-rulings-02-landing` must not move, and
`science/xi-ledger-01` must not move by this task.** Both are re-verified
against their `M1` values in the addendum.

---

# ADDENDUM — `M5`, `C4`'s second limb, and `C5`

**On the integration branch ONLY.** Not on `main`; `origin/main` remains
`H_integ`. It exists because `C4`'s second limb and `C5` observe objects that do
not exist until `H_integ` is committed and pushed.

## A1. `H_integ`

    H_integ   6c1af3cace259663a288354b1725bdd923d3b1fc

## A2. `C4`, second limb — measured, not asserted

`git diff --stat` between the tested tree and `H_integ`:

```
 reports/2026-08-23T1903Z_xi-rulings-02-integ.md | 405 ++++++++++++++++++++++++
 1 file changed, 405 insertions(+)
```

`git diff --name-status`:

```
A	reports/2026-08-23T1903Z_xi-rulings-02-integ.md
```

    tested tree (post-merge)   ee2cabd3d5b5c683f2c5e1d267394d2781290a25
    H_integ                    6c1af3cace259663a288354b1725bdd923d3b1fc
    files changed              1 — the report artifact

**`C4` PASSES on both limbs.**

## A3. `M5` — push order executed

    1  pushed science/integrate-xi-rulings-02  (new branch)
    2  advanced refs/heads/main by fast-forward to H_integ:
         9eefe4c..6c1af3c  6c1af3cace259663a288354b1725bdd923d3b1fc -> main
    3  post-push ref audit, below
    4  this addendum, committed and pushed to the integration branch only

**`A3` did not fire.** `origin/main` was re-read as `9eefe4c8…` immediately
before the push and confirmed a strict ancestor of `H_integ`; the push output
carries the two-dot form `9eefe4c..6c1af3c`, which git prints only for a
fast-forward.

## A4. Post-push ref audit, from `git ls-remote origin`, full SHAs

    6c1af3cace259663a288354b1725bdd923d3b1fc  refs/heads/main
    6c1af3cace259663a288354b1725bdd923d3b1fc  refs/heads/science/integrate-xi-rulings-02
    8f9edfead214b5bb3337924c18c5d241274e97c3  refs/heads/science/xi-ledger-01
    6c7a1f7238273214f87fe0d9b76111a7e5f45a6c  refs/heads/science/xi-rulings-02-landing

Against their `M1` values:

    main                            now 6c1af3ca…  H_integ 6c1af3ca…   EQUAL
    science/xi-rulings-02-landing   now 6c7a1f72…  M1 6c7a1f72…        UNMOVED
    science/xi-ledger-01            now 8f9edfea…  M1 8f9edfea…        UNMOVED

**`science/xi-ledger-01` did not move during this task**, which is what `C5`
requires of it. **Any later movement by the separately authorized addendum task
is that task's, not this one's, and does not affect the ruling subject pin** —
the pin denotes a commit, not a branch tip.

## A5. `C5`

    C5  (M5)  PASS   origin/main equals H_integ; the source branch and
                     science/xi-ledger-01 are unmoved from their M1 values; and
                     this addendum commit is on the integration branch only,
                     with origin/main remaining H_integ.

## A6. `A4` — final confirmation

    source branch unmoved                                     confirmed above
    arriving files, re-measured at M3                          all six MATCH
    arriving files, product blob vs source blob (M3b(b))       all seven EQUAL
    DECISION_LOG.md: base bytes an exact prefix of the product True
    P_overlap (both-changed class)                             empty
    contributed paths/statuses outside the manifest            none
    either authorized task begun, scheduled, or constrained    NO
