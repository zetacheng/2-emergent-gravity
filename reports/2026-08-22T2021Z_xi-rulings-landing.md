# Report — `P2-XI-RULINGS-LANDING-01`: verbatim landing of the issued PI ruling document, its document review, and the Ruling-2 hypothesis registration

    Specification   specs/2026-08-22T2001Z_xi-rulings-landing_v2.md
    Review          reviews/chatgpt/2026-08-22T2001Z_xi-rulings-landing_v2.md
    Branch          science/xi-rulings-landing-01
    Base            6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Merge           NONE performed. `main` did not move.
    Push scope      this task's branch only. See §7.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location     /home/user/2-emergent-gravity
    worktree toplevel      /home/user/2-emergent-gravity
    branch at start        science/xi-b0a @ 012bdff3bac990344a1a0ad288b2665a5304b501
    observed origin/main   6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    branch cut             science/xi-rulings-landing-01 at 6da1f7cb, worktree
                           clean at the cut
    branch tip at report   aeaf173f1d26923b631eb6a32be98aed29ed261e (before this
                           report's own commit)
    UTC at cut             2026-08-22T2021Z

All base-side reads use committed blobs (`git cat-file blob 6da1f7cb…:<path>`),
not the working tree.

---

## 1. Bindings verified before any write

**Four artifacts were supplied. All four were digested before the branch was
cut.**

    ARTIFACT                     SHA-256                                                            BYTES
    issued ruling document       1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941    5227
    document review              c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364    5608
    landing specification        23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee   16069
    landing-spec review          e252589cb010db0009e6382a85e6621253a6a8200a3c5628390433e6fca8477b    5099

**Specification binding (Rule 18, Amendment N).** The landing-spec review
carries `Reviewed specification SHA-256` twice (lines 4 and 119), equal to
`23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee`, which
equals the sha256 of the committed specification blob at `dde6d1e`. Verdict
`APPROVE FOR EXECUTION`.

**Issuance binding (§0a, `A1`).** The supplied issued-document bytes digest to
`1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941` and to git
blob id `f793f9fd866f563480fbec6168553a2b967aea8f` — both equal to the values
§0a pre-registers. **`A1` did not fire, and the branch was cut only after this
check.**

Commit order (Rule 15):

    dde6d1e  spec       the landing specification
    69133c7  review     its bound pre-execution review
    aeaf173  decisions  the landing itself
    (this)   report     this report, last

---

## 2. Measurements — every output as matched text, every digest in full

### `M1` — byte identity of the issued document

    sha256    1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
    blob id   f793f9fd866f563480fbec6168553a2b967aea8f
    bytes     5227
    handed-over bytes vs landed file: `cmp -s` reports identical

Re-measured from the branch tip `aeaf173f`, over
`decisions/P2-XI-RULINGS-01.issued.md`:

    sha256    1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
    blob id   f793f9fd866f563480fbec6168553a2b967aea8f

**The file was copied, not retyped, reflowed, or re-encoded.**

### `M2` — byte identity of the review artifact

    sha256    c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364
    blob id   6fcf0631e2f57da42871314d9fc252f48d655279
    bytes     5608

**This is its first recorded hash.** Provenance per §0a: transmitted by the PI
in session, 2026-08-22. No independent pre-committed hash of the review
artifact exists.

**The SHA-256 the review artifact declares itself bound to, extracted verbatim
from inside the landed blob:**

    1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941

The extraction found exactly one 64-hex string in the artifact, at its lines 4
and 127. **Verdict string, as matched text:** line 7,
`**Document-review verdict:** ` + backtick + `FIT FOR RECORDING` + backtick;
line 123, `**` + backtick + `DOCUMENT REVIEW: FIT FOR RECORDING` + backtick +
`**`.

Re-measured from the branch tip: sha256 unchanged, and
`git cat-file blob | cmp -` against the handed-over bytes reports identical.

### `M3` — carrier extraction

From `results/recovered-2026/session_log_full.md` at the base SHA (the file has
239 lines, so both line numbers resolve):

    line 177   584 bytes with its terminator, 583 without
               sha256 of the extracted line (with terminator)
               287917d667c6ab089a620dc27e7cef8290b2309d216bb39b40db2a19bc8fe388
    line 197   349 bytes with its terminator, 348 without
               sha256 of the extracted line (with terminator)
               9c5b43b1d0b27332afad53296bcf8d3c1861dec25ba7172d0dad74d5f12a3ba1

**The extracted text, reproduced here as matched text:**

```text
**個負號真正嚟自邊度**:**留意一個關鍵事實**——**我哋量度到** minimal scalar(boson!)**嘅貢獻同** fermion **係同號嘅。即係話呢個負號根本唔係** fermion **嘅特性**,**亦唔係任何「物質** vs **反物質」嘅特性。真正嘅分水嶺係** **conformal coupling ξ = 1/6**:**一個場對** curvature **嘅耦合方式決定佢喺「屏蔽」定「反屏蔽」嗰邊**,**而所有普通**(minimal)**物質都坐喺屏蔽嗰邊。可以郁個符號嘅旋鈕唔係粒子嘅電荷**,**而係粒子嘅** **spin 同曲率耦合結構。**  
```

```text
**二**,**符號嘅物理根源寫出嚟先睇到**:**翻盤嘅唔係** statistics**、唔係** charge,**係** spin-1 fluctuation **對** curvature **嘅耦合**(Δ⁽¹⁾ **入面個** R_μν **項**)**壓倒咗** conformal-weight **項。呢個正式回答咗你上次「反物質」嘅問題**:**個** dial **一直喺** spin **結構度。**
```

**`M3`'s `A3` test applied, and the result recorded either way.** Both lines
mention sign, coupling, and species: line 177 carries 個負號 / 同號 (sign),
耦合方式 (coupling), and `minimal scalar` / `fermion` (species); line 197
carries 符號 (sign), 耦合 (coupling), and `statistics` / `spin-1 fluctuation`
(species). **`A3` did not fire, and no search was made for a different line.**

The extracted bytes are placed in `assumptions/H-XI-SIGN-01.md` inside fenced
blocks. **A blockquote prefix would have altered them**; the fenced form keeps
the landed bytes byte-identical to the extraction, which is what `C3` measures.
Line 177 carries two trailing spaces, and they survive.

### `M4` — Statement SHA

**The pin convention was determined by measurement, not assumed.** The
specification says "per the `H-EXT-01` pin convention" without restating it, so
six candidate byte forms of `H-EXT-01`'s own statement were digested and
compared against its landed pin
`e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47`. **Exactly
one reproduced it:** the blockquote content with `> ` prefixes stripped, lines
joined by `\n`, plus one trailing newline. The other five did not.

Applied to `H-XI-SIGN-01`'s landed statement, whose exact-statement bytes are

    'In the induced ξ ledger, the sign is driven by coupling structure\nrather than species.\n'

the digest is

    8731037c16e485fd40d279cef827421cd733bc438ff828f1408dbdbd15488e90

Re-measured from the branch tip by re-extracting the blockquote from the landed
file: **identical**, and equal to the `Statement SHA` field the entry carries.

### `M5` — register append

    base DECISION_LOG.md       2988 lines, 128409 bytes
    product DECISION_LOG.md    3086 lines, 132565 bytes
    diff                       98 insertions, 0 deletions
    byte-prefix                the complete base bytes are an exact prefix of
                               the product bytes — verified by
                               `product.startswith(base)` over the raw bytes

The appended entry records: decision key `2026-08-22-xi-rulings-01`; issued-file
path `decisions/P2-XI-RULINGS-01.issued.md`; issuance SHA-256
`1f39b0f9…7a2f6941`; the review verdict string `FIT FOR RECORDING`; and the
`H-XI-SIGN-01` registration with `Statement SHA`
`8731037c…15488e90`.

### `M6` — suite

Measured at both ends, as the review's §12 execution note requires.

    at the base SHA 6da1f7cb, before any write   332 passed, 2 deselected in 45.77s
    at the branch tip aeaf173f                   332 passed, 2 deselected in 41.66s

Counts recorded verbatim as the runner reported them.

---

## 3. Acceptance criteria

    C1  (M1)  PASS   The recorded sha256 equals
                     1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
                     and the blob id equals
                     f793f9fd866f563480fbec6168553a2b967aea8f; both reproduce
                     under re-measurement from the branch tip.
    C2  (M2)  PASS   The SHA-256 the review artifact declares is an exact
                     string match to C1's issuance digest, and the landed
                     review file is byte-identical to the handed-over bytes
                     under re-measurement from the branch tip.
    C3  (M3)  PASS   Both carrier lines land in H-XI-SIGN-01.md
                     byte-identical to the M3 extraction — 583 and 348 bytes
                     respectively, compared as bytes, not as rendered text.
    C4  (M4)  PASS   The Statement SHA field holds the digest M4 measured, and
                     re-measurement from the branch tip reproduces it.
    C5  (M5)  PASS   The DECISION_LOG.md diff is 98 insertions and 0
                     deletions, and the base bytes are an exact prefix of the
                     product. No pre-existing line is modified.
    C6  (M6)  PASS   No test fails at the branch tip that passes at the base.
                     Both ends measured; the counts are identical.

---

## 4. Abort conditions

    A1  DID NOT FIRE   Both digests measured in M1 agree with §0a. The check
                       ran before the branch was cut and before any write.
    A2  DISCHARGED     The Reviewer's concurrence with the §1 structure
                       disposition is on record (review §6, `CONCUR`). The
                       structure executed is §1's: issued file plus register
                       record, plus the standalone review original. No
                       regression against §1 occurred.
    A3  DID NOT FIRE   Both line numbers resolve at the base SHA and both
                       extractions mention sign, coupling and species. No
                       substitute location was sought.
    A4  DID NOT FIRE   No conflict between the issued rulings and landed
                       repository text was surfaced, and no internal
                       contradiction among the rulings' requirements as they
                       bear on this landing. The registered statement is
                       byte-identical to the specification's §2 blockquote —
                       not narrower, broader, or more specific — and the
                       falsifier defines no criterion narrower than that
                       statement. The carrier's sharper wording (spin, and
                       curvature-coupling structure) is quoted as carrier and
                       kept out of the statement, which is the v1 defect this
                       v2 exists to prevent.
    A5  DID NOT FIRE   Integrability was checked without moving any ref:
                       `origin/main` (6da1f7cb) is a strict ancestor of the
                       branch tip, so `main` would advance by fast-forward
                       from its reviewed evidence base; and
                       `git merge-tree --write-tree origin/main HEAD` returned
                       a clean tree (6fae8161) with no conflict, exit 0.

---

## 5. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session; nothing here
    needs it

No environment restoration was needed; the declared environment was already in
place from earlier in this session.

---

## 6. Stops and clarifications (Amendment B)

**Primary category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.**

Two items are recorded. **Neither changed any measurement, and neither is a
defect finding against the specification or its review.**

### 6a. The specification names a different executor

The specification's §0 states `Execution — Executor (Codex) only. The
Researcher holds no write access and this specification grants none.` **This
task was executed by Claude Code.**

The ground for proceeding, stated rather than assumed: `AGENTS.md:86` provides
that **"The PI announces which executor is in use."** The PI supplied the four
artifacts in session with the instruction to process the specification, which
is that announcement. `AGENTS.md:79-84` places "short deterministic
verification, preparation and audit" with Claude Code, and this task is
transport with no computation and no long-running job.

**What was not done, and is worth stating:** `AGENTS.md:48-49` provides that an
instruction from the PI does not by itself expand the Executor's authorized
scope. **Nothing here expanded scope.** The work performed is exactly what the
reviewed specification measures; only the identity of the performing executor
differs, and that identity is what `AGENTS.md:86` reserves to the PI.

**Returned for the PI to confirm or correct**, since a specification field and
an in-session announcement disagree on their face.

### 6b. Whether this task integrates to `main`

**It did not, and `main` did not move.** The reading is recorded because the
specification admits two.

    THE READING TAKEN     This is a work task on a `science/*` branch. `A5` is
                          a precondition check on integrability, discharged by
                          measurement without moving a ref. Integration is a
                          separate specification.

    WHAT SUPPORTS IT      §6's deliverables name no integration branch, no
                          landing record, and no merge product. §3's `M1`–`M6`
                          contain no merge measurement and §4's `C1`–`C6` no
                          merge criterion. `C1`, `C2` and `C4` each say "from
                          the branch tip", and `M6` says "from the branch
                          tip". §0 carries no `Merge` field. §7 shows the
                          author treating integration as a separate task
                          class ("Do not integrate science/xi-b0a; that
                          integration is a separate task"). The review's §13
                          defers to "the specification's exact ... merge, and
                          push-scope requirements", and the specification
                          fixes none beyond the branch.

    THE OTHER READING     `A5`'s wording — "The branch cannot integrate into
                          main by the landed science/* path ... STOP" — could
                          be read as presupposing that this task performs that
                          integration.

    WHY IT WAS NOT TAKEN  Performing a merge and advancing `main` would be a
                          landing product that no measurement measures and no
                          criterion evaluates. Adding it would be the executor
                          supplying an authorization the reviewed
                          specification does not carry.

**Consequence for push scope, which differs between the two readings.**
`docs/BRANCHING_POLICY.md:34-37` provides that **during landing** only the
integration branch and `refs/heads/main` may be pushed and the source branch
must not move. Under the reading taken, no landing is in progress, so pushing
`science/xi-rulings-landing-01` is in scope and nothing else is pushed. **Under
the other reading the branch push would have been out of scope** — which is why
the reading is recorded here rather than left implicit.

**If the PI intended the integration, it is a separate specification and this
branch is ready for it**: `A5`'s measurement establishes a clean fast-forward
from `6da1f7cb`.

### 6c. Rule 22

**No `INCONCLUSIVE` was recorded**, so Rule 22's subclass-and-resolution-path
requirement has no subject in this task. Every measurement returned a value:
five digests in full, two extracted carrier lines, one append arithmetic, and
two suite counts.

**Nothing measured after this report will be written back.** Anything the
Reviewer raises is returned in chat.

---

## 7. Push scope

`refs/heads/science/xi-rulings-landing-01` only.

`refs/heads/main` is not pushed and did not move — it stands at `6da1f7cb`.
`science/xi-b0a` is not touched and stands at `012bdff3` locally and on the
remote. No merge, no force-push, no `--force-with-lease`, no branch deletion,
no history rewrite.

**A stop hook may ask for the session branch to be pushed. It is declined**,
per `docs/BRANCHING_POLICY.md:37` and §6b above.

---

## 8. Non-goals, checked as prohibitions (§7 of the specification)

    Do not reword any existing repository text under Ruling 2
        HELD. `git diff --name-status 6da1f7cb..HEAD` shows one modified
        path, DECISION_LOG.md, and that modification is a pure append.
        No existing text was reworded.

    Do not open, modify, or classify anything in the XI ledger itself
        HELD. No ledger artifact exists or was created. Nothing was
        classified.

    Do not integrate science/xi-b0a
        HELD. It is unmoved at 012bdff3 and is not a merge parent of
        anything on this branch.

    Do not push beyond the branch scope fixed in BRANCHING_POLICY.md
        HELD. See §7.

---

## 9. Governance checker (`P1`–`P9`)

Run over `6da1f7cb..HEAD` with
`specs/2026-08-22T2001Z_xi-rulings-landing_v2.md` as the subject specification.

    P1  NOT_PARSEABLE   the specification declares no `add:` scope total; it
                        states its deliverables as a §6 list. The checker's
                        own `does_not_establish` field states that
                        NOT_PARSEABLE "is not a pass and is not a finding
                        about that specification's scope."
    P2  PASS            Rule 15 commit order
    P3  PASS            append-only, on both measures
    P4  PASS            superseded branches not merged
    P5  NOT_APPLICABLE  no merge commit in range — this task merges nothing
    P6  PASS            commit-message hygiene
    P7  PASS            gate integrity — no gate section changed
    P8  PASS            Rule 15 placement and specification-first
    P9  PASS            report carries "Stops and clarifications"

    overall  INCOMPLETE, on `P1` alone

**Recorded honestly rather than smoothed:** run against the specification
alone, `P3` and `P7` report `NOT_DECLARED`, because this specification declares
neither an append-only set nor an authorised-gate set. They read `PASS` above
because the sets were supplied to the checker by this task —
`append_only_paths` as `["DECISION_LOG.md"]`, which `M5` measured, and
`authorised_modified_gates` as the empty set, the empty set meaning "nothing
may change". **The checker states it is silent about whether a supplied set is
the right one or complete.** Both are consistent with what the diff shows: one
modified path, a pure append, and no gate section touched.
