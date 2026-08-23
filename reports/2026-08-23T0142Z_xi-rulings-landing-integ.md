# Report — `P2-XI-RULINGS-LANDING-INTEG` v4: transport of the executed landing to `main`

    Specification   specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md
    Review          reviews/chatgpt/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md
    Branch          science/integrate-xi-rulings-landing-01
    Base            main @ 6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Source          science/xi-rulings-landing-01 @
                    190f61c4dde4068f1f5987cd555e0eff57f6bee0
    Scope of file   `M1` through `M5`. **`M6` is post-push and is excluded from
                    this file by construction**, and is recorded in the
                    branch-only addendum commit the specification requires.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/xi-rulings-landing-01 @ 190f61c4
    repository is shallow   false — `.git/shallow` absent,
                            `git rev-parse --is-shallow-repository` = false,
                            638 commits reachable from origin/main at M1
    UTC at report           2026-08-23T0142Z

**The full-clone condition is recorded because `M5` requires it.** The
shallow-clone governance-test artifact — six failures that are an artifact of a
truncated history and not a measurement of the substrate — cannot arise here,
and both `M5` runs were made on a non-shallow tree with the flag recorded at
each run.

---

## 1. Bindings verified before any write

    ARTIFACT                     SHA-256                                                            BYTES
    integration specification    e976f06e3502331ec8409f9548002388700d00ee652cf8438390c2f208eccc57   13855
    its pre-execution review     1b9c5afaa4f76023a288af998fc90a8d3e9d4f0d7308deee6058e9fa5eb733ee    5641

The review carries `Reviewed specification SHA-256` twice, at its lines 4 and
139, and `e976f06e3502331ec8409f9548002388700d00ee652cf8438390c2f208eccc57` is
the only 64-hex string in it. It equals the specification's sha256. Verdict
`APPROVE FOR EXECUTION`.

**The two Date fields disagree and are recorded as supplied.** The review's
`**Review date:** 2026-08-22`; the specification's `Date           2026-08-23`.
**The binding is by SHA-256, not by date**, and neither field was altered.

---

## 2. `M1` — pre-merge ref audit, before any write

**Taken from `git ls-remote origin`, full SHAs. No abbreviated form was used
for any check.**

    refs/heads/main                             6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    refs/heads/science/xi-rulings-landing-01    190f61c4dde4068f1f5987cd555e0eff57f6bee0
    refs/heads/science/xi-b0a                   012bdff3bac990344a1a0ad288b2665a5304b501

**`origin/main` against the specification's Base:**

    measured   6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    Base       6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    EQUAL

**Source tip against the specification's Source field.** The specification
records `190f61c4` and states it is "the handover reference" with the full form
recorded at `M1`. **The abbreviation was used only to check the leading
characters of the full SHA, never as an identity:**

    full SHA                190f61c4dde4068f1f5987cd555e0eff57f6bee0
    its first 8 characters  190f61c4
    Source field            190f61c4
    PREFIX MATCHES

**Ancestor check, full SHA to full SHA, with the command and its output
recorded:**

    command  git merge-base --is-ancestor \
               6da1f7cb8ea1d28d7deadb8a938c67365b28384c \
               190f61c4dde4068f1f5987cd555e0eff57f6bee0
    exit     0  ->  origin/main IS an ancestor of the source tip
    strict   main != source tip, confirmed by direct string comparison
    merge-base                6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    commits main..source      4

**`A1` did not fire.** The integration branch was created only after every
value above was measured and compared.

---

## 3. `M1b` — pre-execution provenance commits, before the merge

**Order executed, with nothing between:**

    1  branch cut     science/integrate-xi-rulings-landing-01 at
                      6da1f7cb8ea1d28d7deadb8a938c67365b28384c
    2  binding measured BEFORE the spec commit
                      spec file sha256
                        e976f06e3502331ec8409f9548002388700d00ee652cf8438390c2f208eccc57
                      digest the review declares
                        e976f06e3502331ec8409f9548002388700d00ee652cf8438390c2f208eccc57
                      EQUAL
    3  spec commit    dc4cef994590071f2c16aa83a769e3ef33e387d8
                      committed blob sha256
                        e976f06e3502331ec8409f9548002388700d00ee652cf8438390c2f208eccc57
    4  review commit  4b80a9ced00767d470f80e2d90c6cc4981bbae2e

    M1b tip           4b80a9ced00767d470f80e2d90c6cc4981bbae2e
    commits base..M1b tip   2

**The two commits, in order, with no intervening commit:**

    dc4cef9  spec(P2-XI-RULINGS-LANDING-INTEG): transport of the executed landing to main
    4b80a9c  review(P2-XI-RULINGS-LANDING-INTEG): ChatGPT pre-execution review, APPROVE FOR EXECUTION

**The review artifact's first recorded digest.** No pre-committed hash of this
artifact exists; its sha256 is recorded here for the first time:

    1b9c5afaa4f76023a288af998fc90a8d3e9d4f0d7308deee6058e9fa5eb733ee
    provenance: transmitted by the PI in session

---

## 4. `M2` — merge construction

    M_merge     b698b059e6fa5f40d63c1917a2e2539e3e1a3de8
    parent 1    4b80a9ced00767d470f80e2d90c6cc4981bbae2e   (the M1b tip)
    parent 2    190f61c4dde4068f1f5987cd555e0eff57f6bee0   (the source tip)
    parent count 2
    merge-base of the two parents
                6da1f7cb8ea1d28d7deadb8a938c67365b28384c   (the Base)

Merged with `--no-ff` per `BRANCHING_POLICY.md:29-30`. **`M_merge` is the
source-transport object and is not the final tip.**

**`A2`, first limb — conflict-free.** Unmerged paths: 0. Working tree clean
immediately after the merge. **No content was authored or resolved inside the
merge.**

---

## 5. `M3` — arriving-blob verification, from the merge product

**Measured from `b698b059e6fa5f40d63c1917a2e2539e3e1a3de8`. Every digest in
full, measured then expected.**

    decisions/P2-XI-RULINGS-01.issued.md
      measured sha256   1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
      expected sha256   1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
      measured blob id  f793f9fd866f563480fbec6168553a2b967aea8f
      expected blob id  f793f9fd866f563480fbec6168553a2b967aea8f
      MATCH

    reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md
      measured          c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364
      expected          c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364
      MATCH

    specs/2026-08-22T2001Z_xi-rulings-landing_v2.md
      measured          23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee
      expected          23973a59cba041590f8f461b542ef48348d11212313a28ff9e6c24e2e59c4eee
      MATCH

    reviews/chatgpt/2026-08-22T2001Z_xi-rulings-landing_v2.md
      measured          e252589cb010db0009e6382a85e6621253a6a8200a3c5628390433e6fca8477b
      expected          e252589cb010db0009e6382a85e6621253a6a8200a3c5628390433e6fca8477b
      MATCH

**`H-XI-SIGN-01`'s Statement SHA, re-derived rather than copied.** The pin
convention the landing task measured was re-applied to the arriving file:
blockquote prefix stripped, lines newline-joined, one trailing newline.

    exact-statement bytes, as re-extracted from the merge product
      'In the induced ξ ledger, the sign is driven by coupling structure\nrather than species.\n'
    measured          8731037c16e485fd40d279cef827421cd733bc438ff828f1408dbdbd15488e90
    expected          8731037c16e485fd40d279cef827421cd733bc438ff828f1408dbdbd15488e90
    MATCH

**`A2`, second limb — no digest mismatch.** **The hypothesis was not
re-authored, the ruling was not re-adjudicated, and Ruling 2's
forward-terminology effect was not exercised.**

---

## 6. `M4` — canonical decision record, then index

### 6a. The canonical record

    path   decisions/2026-08-23-xi-landing-executor-identity.md

**The ruling was extracted from the committed specification blob, not
retyped:**

    extraction        git cat-file blob <spec-blob>:specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md
                      | sed -n '89,93p'
    extracted bytes   326
    sha256            ca6dbb3c30c37c99074594d4dcfb23692b230f146b800999d7287f36e84ff95f

**It is landed inside a fenced block with §0a's `> ` markers intact**, so that
the landed bytes are the specification's bytes rather than a re-rendering of
them. A blockquote would have re-prefixed lines that already carry the marker,
and **`C4` measures bytes, not rendered sameness.** This repository has had
three checks defeated by exactly that class of alteration.

**Byte comparison, landed block against specification lines 89–93:**

    specification §0a bytes   326   sha256 ca6dbb3c…e84ff95f
    landed block bytes        326   sha256 ca6dbb3c…e84ff95f
    BYTE-IDENTICAL            True

The record carries, per `M4(a)`: the task affected; issuance (PI, in session,
2026-08-23); the ruling verbatim; the scope (executor identity only, no
scientific, measurement, scope or acceptance change, no re-execution); and the
historical fact that `specs/2026-08-22T2001Z_xi-rulings-landing_v2.md`'s
`Execution` field read `Executor (Codex) only` and is superseded for executor
identity only, for that execution only, under `AGENTS.md:86`. **PART 2 is
marked `REVIEW PENDING`** per `decisions/README.md`.

**What the record does not land:** the forward executor-field convention. It is
a Researcher authoring practice unless and until the PI issues it as a ruling.

### 6b. The index append

    DECISION_LOG.md at the base (main 6da1f7cb)      128409 bytes
    DECISION_LOG.md as it arrives in the merge product 132565 bytes, 3086 lines
    DECISION_LOG.md after this task's append          135360 bytes
    bytes added by this task                            2795
    diff                                              67 insertions, 0 deletions

    base bytes are an exact byte-prefix of the product           True
    merge-product bytes are an exact byte-prefix of the product  True

**Both prefix relations are recorded**, because the append-only obligation
holds against the base and against the arriving state, and only the second
would catch a modification made inside this task to a line that arrived in the
merge.

**The entry is a pointer.** It records the decision key, a one-line subject, and
the path of the canonical record. **It does not transcribe the ruling** — under
the landed ruling that a specification transcribing an adjudication is evidence
of its content and not its canonical provenance record, a second transcription
would create a second place for one text to drift. The path it names exists in
the same commit.

    post-M4 commit    e2109a74624525dd7eb49cbc77134e13799dbea4
    post-M4 tree SHA  1cafacf96f3957fc2b4851f28a5d55cc29cd6cbe

---

## 7. `M5` — suite, on a full tree, at both ends

**Both runs on a non-shallow tree, with the flag recorded at each run and the
tested tree identified by SHA.**

    BASE
      commit     6da1f7cb8ea1d28d7deadb8a938c67365b28384c
      tree SHA   c63dce6bcdfb1e0bed80588e7d759b44867faae1
      shallow    false
      worktree   0 modified paths
      result, verbatim as the runner reported it
                 332 passed, 2 deselected in 43.14s

    POST-M4 INTEGRATION TREE
      commit     e2109a74624525dd7eb49cbc77134e13799dbea4
      tree SHA   1cafacf96f3957fc2b4851f28a5d55cc29cd6cbe
      shallow    false   (.git/shallow absent; 646 commits reachable)
      worktree   0 modified paths
      result, verbatim as the runner reported it
                 332 passed, 2 deselected in 38.16s

**No test fails on the post-M4 integration tree that passes at the base.** The
failure sets are both empty and the counts are identical.

---

## 8. `M5b` — report commit and the final tip

This file is the report. **The integration branch tip after this commit is
`H_integ`.**

**No suite re-run at `H_integ` is required, and none was made.** The suite was
measured on the post-M4 tree, and `H_integ` differs from that tested tree only
by this report artifact. **That difference is measured, not asserted** — the
`git diff --stat` between the tested tree and `H_integ` is recorded in the
addendum commit, which is written after `H_integ` exists and can therefore
observe it.

---

## 9. Acceptance criteria

`C6` is post-push and is evaluated in the branch-only addendum.

    C1  (M1)      PASS   origin/main equals the Base
                         (6da1f7cb8ea1d28d7deadb8a938c67365b28384c, string
                         equality on the full SHA); the ancestor check exits 0
                         on full SHAs; the source tip's leading characters
                         match the Source field's abbreviation and its full
                         SHA is 190f61c4dde4068f1f5987cd555e0eff57f6bee0.
    C2  (M1b, M2) PASS   M_merge b698b059 has exactly two parents, the M1b tip
                         4b80a9ce first and the source tip 190f61c4 second;
                         the M1b tip descends from the base by exactly two
                         commits, the spec then its review; and the spec's
                         sha256 equals the digest the review declares, as
                         measured at M1b before the spec commit.
    C3  (M3)      PASS   Every digest equals its expected value as a full
                         64-character string match, recorded in §5 above:
                         four artifact digests, one git blob id, and the
                         re-derived Statement SHA.
    C4  (M4)      PASS   The canonical record exists at
                         decisions/2026-08-23-xi-landing-executor-identity.md
                         with the ruling byte-identical to §0a (326 bytes,
                         sha256 ca6dbb3c…e84ff95f, compared as bytes); the
                         DECISION_LOG append is byte-prefix-preserving against
                         both the base and the merge product; and the entry
                         names that path, which exists.
    C5  (M5)      PASS   on its first limb: no test fails on the post-M4 tree
                         that passes at the base. **Its second limb — that
                         H_integ differs from the tested tree only by the
                         report — is measured in the addendum**, because the
                         diff cannot be taken until H_integ exists.

---

## 10. Abort conditions

    A1  DID NOT FIRE   Every M1 value agrees with the specification's Base and
                       Source, and the ancestor check exits 0. The check ran
                       before the branch was created and before any write.
    A2  DID NOT FIRE   The merge is conflict-free (0 unmerged paths, clean
                       tree) and M3 found no digest mismatch in the merge
                       product.
    A3  NOT YET REACHED at the time of this commit. Advancing main is a
                       fast-forward: origin/main is a strict ancestor of the
                       integration branch, established at M1 and unchanged
                       since. The condition is evaluated at push time and
                       recorded in the addendum.
    A4  DID NOT FIRE   No step modified the source branch, any file arriving
                       from it, or any pre-existing DECISION_LOG.md byte. The
                       source branch is unmoved at 190f61c4 (re-verified at
                       M6, in the addendum). Both byte-prefix relations in §6b
                       hold, which is the measurement that would have caught a
                       modification to an arriving DECISION_LOG.md byte.

---

## 11. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session; nothing here
    needs it
    repository non-shallow throughout, verified at both M5 runs

No environment restoration was needed.

---

## 12. Governance checker (`P1`–`P9`), on the post-M4 tree

Run over `6da1f7cb..e2109a74` with the v4 specification as subject, the
append-only set `["DECISION_LOG.md"]`, an empty authorised-gate set, and the
merge facts of §4 supplied for `P5`.

    P1  NOT_PARSEABLE   the specification declares no `add:` scope total; it
                        states its deliverables as a §4 list. The checker's own
                        `does_not_establish` field states that NOT_PARSEABLE
                        "is not a pass and is not a finding about that
                        specification's scope."
    P2  PASS            Rule 15 commit order
    P3  PASS            append-only, on both measures
    P4  PASS            superseded branches not merged
    P5  PASS            merge parentage AGREES with the recorded facts —
                        recomputed parents and merge-base match §4 exactly
    P6  PASS            commit-message hygiene
    P7  PASS            gate integrity — no gate section changed
    P8  PASS            Rule 15 placement and specification-first
    P9  PASS            report carries "Stops and clarifications"

    overall  INCOMPLETE, on `P1` alone
    commits in range 8; on the first-parent line 4

**Recorded honestly:** `P3` and `P7` report `NOT_DECLARED` when run against the
specification alone, because this specification declares neither set; they read
`PASS` because the sets were supplied by this task — the append-only set being
the one `M4(b)` measured, and the gate set empty, which the checker reads as
"nothing may change". **The checker states it is silent about whether a
supplied set is the right one or complete.** Both are consistent with the diff:
one pre-existing path modified, by pure append, and no gate section touched.

---

## 13. Stops and clarifications (Amendment B)

**Primary category: `ENVIRONMENT`** — one item, and it is a discharged
precondition rather than an obstruction.

### 13a. The full-clone requirement, discharged rather than assumed

`M5` requires a full tree and records that a shallow one is not a valid
substrate, the six governance-test failures it produces being an artifact of
truncated history. **The condition was checked rather than assumed**, at three
points: before `M1` (`.git/shallow` absent, `is-shallow-repository` false, 638
commits reachable from `origin/main`), and again at each of the two `M5` runs,
with the flag and the reachable-commit count recorded beside each result. **No
shallow-clone artifact could have entered either measurement.**

The repository was unshallowed earlier in this session under Rule 13's standing
authorization to restore the declared execution environment; that restoration
is on record in the onboarding task's report and is not repeated here.

### 13b. Nothing else stopped, and nothing was reconciled

**`A1`, `A2` and `A4` did not fire and `A3` was not yet reachable.** No conflict
between the arriving result and landed repository text was surfaced, and
nothing was reconciled inside this task.

**No `INCONCLUSIVE` was recorded**, so Rule 22's subclass-and-resolution-path
requirement has no subject. Every measurement returned a value: three remote
ref SHAs, one ancestor exit status, two binding digests, six commit SHAs, six
artifact digests, one blob id, one re-derived Statement SHA, one extraction
digest, three byte-prefix relations, and two suite results.

**One item is carried forward for the addendum, not for the PI:** `C5`'s second
limb and `C6` are measurements this file cannot contain, because they are
observations of objects that do not exist until this commit is made and pushed.
**That is why they are in the addendum**, and the addendum is on the
integration branch only.

**Nothing measured after the addendum will be written back.** Anything the
Reviewer raises is returned in chat.

---

## 14. Push scope

Per `M6` and `BRANCHING_POLICY.md:34-37`, in this order:

    1  push the integration branch science/integrate-xi-rulings-landing-01
    2  advance refs/heads/main by fast-forward to H_integ — NOT to M_merge —
       and push
    3  post-push ref audit
    4  the audit's output into an addendum commit on the integration branch
       ONLY, pushed to that branch and not to main; origin/main remains H_integ

**The source branch `science/xi-rulings-landing-01` must not move**, and
`science/xi-b0a` is unrelated to this task and must not move. Both are
re-verified against their `M1` values in the addendum.

**A stop hook may ask for the session branch to be pushed. It is declined**,
per `docs/BRANCHING_POLICY.md:37`.
