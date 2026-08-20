# Landing record — `P2-ADJUDICATION-SOURCE-02`

**A retrospective provenance landing.** It records a document that was acted on
before any record of it existed, and disposes of one known divergence between
that document and a landed transcription of it. **It produces no scientific
result and moves no gate.**

    Source branch   science/adjudication-source-02
                    ba94f802208676ddb6f05e5c9a8b8002861867f6
    Base            46a9c28697fd5b918c6b3d346bd76f8b68ae6d82
    Fork point      46a9c28697fd5b918c6b3d346bd76f8b68ae6d82
    Merge product   636705b778cf59301a65bf27961a82b905fd74c6

**The fork point and `main` are the same commit.** `main` did not advance during
this task, and that is what makes the revert hazard structurally absent rather
than merely unobserved.

---

## 1. What landed

**`decisions/2026-08-20-adjudication-source.md`** — the adjudication document,
recorded under

    RETROSPECTIVELY RECORDED AND PI-CONFIRMED AT LANDING
    — ORIGINAL ISSUANCE NOT ESTABLISHED

carrying every item measured from the PI-confirmed source in its stated words,
each item's landed state, and the two ratifications the PI made at this landing.

**`docs/GOVERNANCE-DEBT.md`** — an additive correction beneath `G-13`, carrying
both texts of the divergent item in full, the three levels kept apart, and the
finding that the existing block's `registered verbatim` label is not supported
by the evidence. **The quoted block is retained exactly as landed.** `G-13`
remains `OPEN` and its disposition is unchanged.

**`DECISION_LOG.md`** — `R-8` through `R-12`, five open records, none answered.

## 2. What did NOT land, and is not decided

**Which text of the divergent item was originally issued.** The exact
byte-level wording of the original session cannot be established, and this
landing does not establish it. What it determines is which wording governs the
record being made now — a different question, at a different level.

**Any item's effective date.** No date is fixed, in either direction. The
forward error — recording the document as adjudicated at issuance — and the
backward error — recording that unlanded items had no authority until now — are
both barred in terms by the record itself.

**Whether other `verbatim` labels hold.** One label was measured. No other was.
The question is `R-12`'s and belongs to the provenance census.

**Rule 17.** No governance or epistemic classification is added that the
reviewed material did not carry. The five records are registered as open
records and settle nothing; the two PI ratifications are recorded as
ratifications made at this landing, with no representation that either was
authorised earlier.

---

## 3. The merge, measured

### `M10` — dry-run merge (MEASURED)

`git merge-tree --write-tree --messages` against the base returned tree
`37838a3b67e0429a8205be7a709b61c14d86222b`, exit `0`, **no conflicting paths
listed.** `A2` does not fire.

### `M6` — the revert hazard: the subject set is non-empty, the risk set is empty (MEASURED)

Paths present on both the base and the branch at differing blobs — measured by
`git diff --name-only --diff-filter=M`, not assumed — are two:

    DECISION_LOG.md
      fork     e540dd963b7956e2595f4c72cdf0bd3996e02943
      branch   83aea265f8e6ca224abc8afde2970b5ef7da1d1b
      main     e540dd963b7956e2595f4c72cdf0bd3996e02943
      product  83aea265f8e6ca224abc8afde2970b5ef7da1d1b

    docs/GOVERNANCE-DEBT.md
      fork     e5582dfa0dc3433e45e9168f3e7d150a70f03ce1
      branch   c87359e143af62d9a87ec35429ed6bb487db2e42
      main     e5582dfa0dc3433e45e9168f3e7d150a70f03ce1
      product  c87359e143af62d9a87ec35429ed6bb487db2e42

**HOW THE EMPTINESS WAS ESTABLISHED, two ways and both recorded.**

**Structurally:** the fork point and `origin/main` resolve to the same commit,
`46a9c286`, so there is no path at which `main` could carry a blob newer than
the fork's.

**Per path:** `git diff --name-only <fork> <origin/main>` returns an empty
listing. The empty result is the measurement, not the absence of one.

**In both rows `main` equals `fork`, so no path was changed on both sides.**
Amendment P(b)'s line-survival obligation governs a file auto-merged from two
sides that both changed it; **that case does not arise here, and its
non-arising is established by the blob equality above rather than assumed from
a clean merge.** `A5` does not fire.

### `M8` — validators, both sides, in real worktrees (MEASURED)

    merge product  636705b   332 passed, 2 deselected, exit 0
    base           46a9c28   332 passed, 2 deselected, exit 0

Run in two detached worktrees created for the purpose, each identified by its
resolved `HEAD`. **No failure on the product, so none that is not also present
at the base.** `A3` does not fire.

### `M9` — two measurements, and they do not differ (MEASURED)

    (a) base-relative       git diff --name-only 46a9c286..636705b
    (b) own contribution    git diff --name-only 46a9c286..ba94f80

Both return the same five paths:

    DECISION_LOG.md
    decisions/2026-08-20-adjudication-source.md
    docs/GOVERNANCE-DEBT.md
    reviews/chatgpt/2026-08-20T1705Z_adjudication-source-02.md
    specs/2026-08-20T1705Z_adjudication-source-02.md

**They are identical**, and they are identical because the fork point and the
base are the same commit. **Recorded as two measurements that agree, not as one
measurement taken twice.**

### `M7` — the governing clause (MEASURED)

`docs/BRANCHING_POLICY.md:25-40`, `## Science branch integration`: `--no-ff`
into a dedicated integration branch; squash/rebase integration prohibited;
"During landing, only the integration branch and `refs/heads/main` may be
pushed"; "Source branch, session branches and unrelated refs must not move";
"`main` advances only by fast-forward from its reviewed evidence base to the
completed integration head." **No contradiction with §3. `A4` does not fire.**

### `M11` — the pins this task must not move (MEASURED)

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Both unchanged. Neither containing file was modified: `CONVENTIONS.md` is blob
`5be8e49bee9b61fe4688807066e55650d4ed0cd7` and `assumptions/H-EXT-01.md` is
blob `3d3d3a0b6c9adb7dba46c608ee270b0b90966146` at the base and on the merge
product alike.

---

## 4. Append-only, verified by byte prefix

`DECISION_LOG.md` grew from `112339` to `117791` bytes. The **first `112339`
bytes of the new file** hash to
`5eb972fcde2158ab05196e45135fcfbc9441e8694dbad5761655a114c84adb5c`, which is the
SHA-256 of the base blob's full content. **The prefix is unchanged byte for
byte**; the entry is an append.

`docs/GOVERNANCE-DEBT.md` is not declared append-only, and its change is
nonetheless purely additive: `121` insertions and `0` deletions, in **one hunk
at `--unified=0`** — the diff context is named because a hunk count is a
property of a change and a context together. The entry's text through `:344` is
byte-identical to the base.
