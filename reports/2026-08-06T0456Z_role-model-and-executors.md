# Task report — function-based role model and dual-executor record (clean rebuild)

Function: Executor
Date: 2026-08-06
Task classification: MATERIAL (branch only; integration is a separate
authorization after result review)
Executor: Claude Code (sandboxed container)

## 0. Identification — three artifacts, two specifications

**This report's filename alone will mislead a later reader**, so the
three artifacts it depends on are named first:

```text
Execution authority:  specs/2026-08-06T1218Z_role-model-clean-rebuild.md
Reproduced original:  specs/2026-08-06T0456Z_role-model-and-executors.md
Report path:          reports/2026-08-06T0456Z_role-model-and-executors.md
```

**Two different specifications are involved and they are not the same
artifact.**

- `specs/2026-08-06T1218Z_role-model-clean-rebuild.md` is the
  specification **this execution was performed under**. It authorized the
  rebuild, and it did not exist before this branch.
- `specs/2026-08-06T0456Z_role-model-and-executors.md` is the **original**
  role-model specification. On this branch it is not an authority; it is
  **content**, reproduced byte-for-byte in commit 2 as one of the six
  source artifacts, because it is one of the artifacts the original task
  produced.

**The report filename retains the `0456` token in order to produce the
intended final repository path.** That retention does **not** mean the
rebuild's own specification carries the `0456` token — it carries
`1218`. **This report is the execution report for the rebuild**, not only
for the original task: every commit identity, tree id, scope result and
validator run below was produced on the clean branch, not copied from the
reviewed one.

### The reviewed branch is preserved

**`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` is preserved unmodified** as
the execution and negative-provenance record — including the commit-1
metadata defect that this rebuild exists to remove from the history that
would reach `main`. It was not deleted, renamed, force-pushed or
modified. Verified at task end in §2.

### Why this branch exists

The reviewed branch was correct in content: seven declared paths, correct
commit layering, protected paths unchanged, the role model landed as
approved. It was rebuilt for one reason only — its commit
`031540028a57c4132f395aa9ad4b1e573c910ea6` carried two trailers that no
specification authorized, and commit messages are immutable. **This
rebuild removes that metadata from the history that would enter `main`,
and makes the single wording correction authorized in A4. Nothing else is
changed.**

---

## 1. Identification of this execution

| Item | Value |
| --- | --- |
| Branch | `review/role-model-and-executors-clean` |
| Base commit | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| Commit 1 (rebuild authority) | `7740f45e2d30647704804484e547c45542a21c84` |
| Commit 2 (content) | `cb9e70c5707870e9dce7076ceeabd2a58115cb32` |
| Commit 2 tree | `30a28bb0fc8b55f61005929b7a8b7b7350e5c495` |
| Source-reference tree (reviewed commit 2) | `752de58f149f2a25a27caa1b1199b2e4f1f1066a` |
| Pre-report head | `cb9e70c5707870e9dce7076ceeabd2a58115cb32` (= commit 2) |
| UTC token `{HHMM}` for the rebuild spec | `1218` |
| Observed UTC timestamp when the token was taken | `2026-08-06T12:18:58Z` |
| Rebuild-spec blob id | `d1ac6be3a8e30769351f8740f7540d551d9ed958` |
| Rebuild-spec blob SHA-256 | `d07e923d16f516ecbd723deb2259c945a5a995da711eb401c54d80a76dc1a6ea` |
| `AGENTS.md` blob at commit 2 (post-A4) | `5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3` |
| `AGENTS.md` source blob (reviewed branch) | `15a29880d5196cee79dbd76eeab59224eb83d994` |

**The commit-2 tree is `30a28bb0…`, not the source-reference tree
`752de58f…`, and that is expected.** The source-reference tree does not
carry the verdict. Two differences separate them, both required by the
specification:

```text
$ git diff --name-status 752de58f149f2a25a27caa1b1199b2e4f1f1066a 30a28bb0fc8b55f61005929b7a8b7b7350e5c495
M	AGENTS.md
A	specs/2026-08-06T1218Z_role-model-clean-rebuild.md
```

`M AGENTS.md` is the A4 replacement, proved in §4 to be the only content
difference. `A specs/…1218Z…` is the rebuild's own authority artifact,
which by §5 of the specification is not a source artifact and is not
expected to be byte-identical to anything on the reviewed branch. **There
is no third difference.**

### Commit 1 message, complete, exactly as stored

```text
specs: record the clean-rebuild execution authority

Commits the approved specification authorizing the rebuild of the
role-model branch with clean commit metadata, so that this branch's
report has a corresponding instruction in the repository.

This is the rebuild's own authority artifact. It is distinct from the
original role-model specification, which is reproduced as content in
the next commit under its own 0456 token.
```

### Commit 2 message, complete, exactly as stored

```text
Adopt the function-based role model; record the dual-executor arrangement

Records decisions already made by the PI (2026-08-06). No scientific
content, gate, claim, or CONVENTIONS.md rule is touched.

- AGENTS.md: role separation restated as functions with current
  assignments (PI / Researcher / Reviewer / Executor); the
  Researcher-Reviewer exchange and the limits on minor corrections are
  stated; the dual-executor arrangement (Codex on the PI workstation,
  Claude Code in a sandboxed container) is recorded with its capability
  difference; rule 8 is identified as governing where the older role
  text conflicted; the superseded fixed-agent text is preserved verbatim
  under an explicitly non-operative historical heading.
- reviews/README.md: records created or substantively amended after this
  decision must carry a Function: header; existing records remain valid
  historical evidence and are not relabelled.
- HANDOFF.md, PROGRESS.md: staleness notice inserted below the title
  line; no other bytes changed.
- DECISION_LOG.md: append-only entry recording the adoption, pinned to
  the specification blob reproduced here.
- specs/2026-08-06T0456Z_role-model-and-executors.md: the original
  approved specification, reproduced byte-for-byte as content.

Capability statements in the dual-executor section are PI-supplied
operational findings and current observations, not re-verified by that
task and not permanent guarantees.

Five of the six artifacts are byte-identical to the reviewed branch
review/role-model-and-executors. AGENTS.md differs by exactly one
PI-authorized replacement: "this task" becomes "the task recorded in
specs/2026-08-06T0456Z_role-model-and-executors.md", which restores the
antecedent the phrase lost when it moved into a standing document.
```

### Intended commit-3 message

```text
docs: execution report for the clean rebuild of the role-model branch

Regenerated evidence for review/role-model-and-executors-clean: A0-A5
raw output, the A4 single-hunk diff, A6-pre scope evidence and A7-pre
validator output, all produced on this branch rather than copied from
the reviewed one.

Commit 3's own SHA, the final branch head, A6-final and A7-final are
returned as post-commit evidence and are deliberately absent here: the
report cannot contain its own commit.
```

**This report records neither commit 3's SHA nor the final branch head.**
It cannot: commit 3 is this report.

---

## 2. Commit-message hygiene — the point of this task

### 2.1 What the defect actually was

**Diagnosed before any commit was created.** The trailers on the reviewed
commit 1 were **not** injected by an automatic mechanism inside the
repository:

```text
$ git config --get core.hooksPath
(unset)
$ git config --get commit.template
(unset)
$ ls .git/hooks/            # non-sample entries
(none)
```

There is no `prepare-commit-msg` hook, no commit template and no
`core.hooksPath`. The trailers came from a **standing convention in the
executor's own harness**, which I applied when creating the reviewed
commit 1 and did not apply when creating the reviewed commits 2 and 3 —
which is exactly why the defect appeared in one commit and not the
others. `git commit -F <file>` stores the given bytes and nothing else.

**Consequence for the standing concern the specification raises:** the
convention will keep proposing those trailers, so the defence is the
per-commit inspection required by §2, not a one-off repair. Every commit
on this branch was created with `git commit -F <file>` from a message
file inspected byte-for-byte with `cat -A` beforehand, and read back from
the commit object afterwards.

### 2.2 Per-commit inspection, both directions

| Commit | Pre-commit inspection | Post-commit `git log -1 --format=%B` | Unauthorized trailer |
| --- | --- | --- | --- |
| 1 `7740f45` | `cat -A` of the message file, shown in full | read back, shown in §1 | none |
| 2 `cb9e70c` | `cat -A` of the message file, shown in full | read back, shown in §1 | none |
| 3 | `cat -A` before creation | read back after creation | none — returned as post-commit evidence |

**Trailers suppressed, and which.** For every commit on this branch I
suppressed the two trailers the harness convention would otherwise have
appended, and which §2 of the specification forbids: a
`Co-Authored-By:` line naming a tool version, and a `Claude-Session:`
line carrying a session URL. **No commit on this branch carries either.**
No other attribution was introduced, no tool was installed, and **no
persistent user or global configuration was changed** — the suppression
is achieved solely by choosing `git commit -F <file>` and writing the
authorized message.

Automated scan of all commits on this branch, case-insensitive, for
`co-authored-by`, `claude-session`, `session_`, `claude.ai`, `opus`,
`generated with`, `signed-off-by`: **zero hits** (see §3, hygiene
block).

### 2.3 What is NOT a message trailer, and is disclosed rather than removed

Two things live in the **commit object headers**, not in the message
body, and `git log -1 --format=%B` does not show them:

```text
$ git config --show-origin --get commit.gpgsign
file:/root/.gitconfig	true
$ git config --list --show-scope | grep '^global'
global	user.name=Claude
global	user.email=noreply@anthropic.com
global	user.signingkey=…
global	commit.gpgsign=true
```

1. **An SSH signature** (`gpgsig` header), because `commit.gpgsign=true`
   in global configuration.
2. **Author and committer identity** `Claude <noreply@anthropic.com>`,
   from global `user.name` / `user.email`.

**Both are pre-existing global configuration, both are present on the
reviewed commits the PI accepted** — including `a021eed…`, which §2 of
the specification cites as trailer-free — and **§2 forbids me from
changing persistent user or global configuration**, which is the only way
to alter them. They are therefore disclosed here rather than removed.
They are not message content and not within the class §2 describes; if
the PI considers commit-object identity or signing to be in scope, that
is a separate decision requiring a configuration change this task does
not authorize.

---

## 3. A0, A1, A2, A5 — raw verifier output at commit 2

**How these were produced.** A scratch verifier outside the repository
read Git objects only. Primitives:
`git rev-parse`, `git merge-base`, `git rev-list --count`,
`git reflog show`,
`git ls-tree -r --full-tree --format='%(objectmode) %(objecttype) %(objectname) %(path)'`,
`git diff-tree --no-commit-id --name-status -r --find-renames --find-copies`,
`git diff --name-status --find-renames --find-copies`, and
`git log -1 --format=%B`. No value was accepted as quoted; all were read
from the objects. The verifier is scratch tooling and is not committed.

```text
$ python3 rcheck.py cb9e70c5707870e9dce7076ceeabd2a58115cb32 7740f45e2d30647704804484e547c45542a21c84 cb9e70c5707870e9dce7076ceeabd2a58115cb32
A0 — new branch from the pinned base; reviewed branch untouched
   OK    review/role-model-and-executors-clean resolves to head cb9e70c5707870e9dce7076ceeabd2a58115cb32
   OK    merge-base(base, head) == base  (a0e9d11b7281f0c2185aa8d517bae009ab54807f)
   OK    commits above base = 2
   OK    review/role-model-and-executors still resolves to 10c260b96882ac12610f78840aeeabd07be2d7cb
   OK    reviewed branch reflog head unchanged
      reviewed-branch reflog (most recent 3):
        10c260b review/role-model-and-executors@{0}: commit: docs: task report for the function-based role model and dual-executor record
        a021eed review/role-model-and-executors@{1}: commit: Adopt the function-based role model; record the dual-executor arrangement
        0315400 review/role-model-and-executors@{2}: commit: specs: record the approved role-model and dual-executor specification

A1 — source artifacts reproduced at commit 2
   OK    byte-identical  specs/2026-08-06T0456Z_role-model-and-executors.md
            expected 05472d8d339b1f89e6dee265ea7a14190ee01d21
            actual   05472d8d339b1f89e6dee265ea7a14190ee01d21
   OK    AGENTS.md differs from source (A4): source 15a29880d5196cee79dbd76eeab59224eb83d994 -> head 5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3
   OK    byte-identical  reviews/README.md
            expected 9ef4ec5e68091e6f7f226a5ad69e64aa81d0b038
            actual   9ef4ec5e68091e6f7f226a5ad69e64aa81d0b038
   OK    byte-identical  HANDOFF.md
            expected e60026120d933c1977ad0568506d292721cce2e8
            actual   e60026120d933c1977ad0568506d292721cce2e8
   OK    byte-identical  PROGRESS.md
            expected 5ef6e65a1e3f927d92b708c6527eab0f839d569c
            actual   5ef6e65a1e3f927d92b708c6527eab0f839d569c
   OK    byte-identical  DECISION_LOG.md
            expected 0464b854c8adf57b2e79841a2d754bccf2c68a05
            actual   0464b854c8adf57b2e79841a2d754bccf2c68a05

A2 — commit layering
   OK    commit 1 adds exactly the clean-rebuild spec: 'A\tspecs/2026-08-06T1218Z_role-model-clean-rebuild.md'
   OK    commit 2 touches exactly the six content paths
            M	AGENTS.md
            M	DECISION_LOG.md
            M	HANDOFF.md
            M	PROGRESS.md
            M	reviews/README.md
            A	specs/2026-08-06T0456Z_role-model-and-executors.md
   OK    commit 2's parent is commit 1
   OK    commit 1's parent is the base
      two distinct specification artifacts present at commit 2:
        05472d8d339b1f89e6dee265ea7a14190ee01d21  specs/2026-08-06T0456Z_role-model-and-executors.md
        d1ac6be3a8e30769351f8740f7540d551d9ed958  specs/2026-08-06T1218Z_role-model-clean-rebuild.md
   OK    exactly two specs/ blobs at commit 2 (2)
   OK    both the rebuild authority and the reproduced original are present

A5 — protected paths unchanged
      base blob paths enumerated: 144   head: 144
   OK    base-vs-head mismatches/deletions = []
   OK    paths added under the protected prefixes = []
   OK    name-status over protected prefixes (catches add/delete/rename/copy/type_change) = ''
   OK    CONVENTIONS.md  base 2d4f735c55a14fdfc5d1031a58698a8ca075fbbd  head 2d4f735c55a14fdfc5d1031a58698a8ca075fbbd
   OK    GATES.md  base bd4820513217ae7e1c493328dc49536e69b8cfb8  head bd4820513217ae7e1c493328dc49536e69b8cfb8
   OK    pyproject.toml  base 9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4  head 9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4
      first 3 enumerated: CONVENTIONS.md=2d4f735c55a1, GATES.md=bd4820513217, derivations/CANONICAL_INTERACTION.json=0c992d83bbd7
      last  3 enumerated: tests/test_p2_phase01_scalar_exploratory.py=5e47fc98fe50, tests/test_repository_structure.py=7d63880dd0b9, tests/test_si1_governance.py=a8aefafce1c2

Commit-message hygiene — complete stored messages, all commits
   OK    commit 1 7740f45: unauthorized trailer scan = []
      commit 1 message: 428 bytes, 9 lines
   OK    commit 2 cb9e70c: unauthorized trailer scan = []
      commit 2 message: 1789 bytes, 32 lines

ALL CHECKS OK

process exit status: 0
```

Reading the four criteria off that output:

- **A0** — the branch was created from the exact pinned base
  (`merge-base(base, head) == base`), carries exactly two commits above
  it at this point, and **`review/role-model-and-executors` still
  resolves to `10c260b96882ac12610f78840aeeabd07be2d7cb`**, with its
  reflog head unchanged at `@{0}`.
- **A1** — the five artifacts that must not change are **byte-identical
  to the source blob ids given in the specification**, each verified
  against the reviewed branch first and then reproduced.
  `AGENTS.md` differs, as A4 requires, and only as A4 requires (§4).
- **A2** — commit 1 adds exactly the rebuild specification and nothing
  else; commit 2 touches exactly the six content paths; parentage is
  base → commit 1 → commit 2. **Both specification artifacts are present
  at commit 2 and are distinct blobs** — `05472d8d…` (reproduced
  original) and `d1ac6be3…` (rebuild authority) — so the rebuild's own
  authority is recorded rather than conflated with the original.
- **A5** — 144 base blob paths enumerated under `tests/`, `scripts/`,
  `derivations/`, `results/` plus `GATES.md`, `CONVENTIONS.md`,
  `pyproject.toml`; every one identical at head; the name-status diff
  over those prefixes is empty, so nothing was added, deleted, renamed,
  copied or type-changed. `CONVENTIONS.md` is byte-identical
  (`2d4f735c…`): no rule created, renumbered or reworded.

---

## 4. A4 — the single authorized content delta

**Correction as specified:** in `AGENTS.md`, `this task` in the sentence
`not re-verified by this task` is replaced by
`the task recorded in specs/2026-08-06T0456Z_role-model-and-executors.md`,
restoring the antecedent the phrase lost when it moved into a standing
document. This is the only content change permitted, and the only one
made.

```text
=== A4 — single-file diff: source blob 15a29880 -> commit-2 AGENTS.md ===
$ git --no-pager diff --no-index --src-prefix=a/AGENTS.md@15a29880/ --dst-prefix=b/AGENTS.md@head/ <src> AGENTS.md
diff --git a/AGENTS.md@15a29880/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/AGENTS_src.md b/AGENTS.md@head/AGENTS.md
index 15a2988..5e60b5f 100644
--- a/AGENTS.md@15a29880/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/AGENTS_src.md
+++ b/AGENTS.md@head/AGENTS.md
@@ -68,8 +68,9 @@ selected per task by the PI according to quota and capability. **They
 are not interchangeable, and the difference is material rather than
 administrative.** The capability statements below are PI-supplied
 operational findings and current observations; they are **not
-re-verified by this task and are not permanent capability
-guarantees:**
+re-verified by the task recorded in
+specs/2026-08-06T0456Z_role-model-and-executors.md and are not
+permanent capability guarantees:**
 
 - **Codex** — runs on the PI's workstation, which has a GPU
   (RTX 4070 Ti) and no short process-termination limit. **Decisive
(git diff --no-index exits 1 when files differ; that is the expected status here)

hunk count (@@ lines): 1

=== 112-char line: is it mine? ===
longest line, source: 112 | head: 112 -> unchanged: True
that line (pre-existing, not introduced by A4):
   '12. Follow `CONVENTIONS.md` “Execution discipline for decisive runs and merges” for decisive-run and merge work.'
lines I introduced, with lengths:
    35  're-verified by the task recorded in'
    62  'specs/2026-08-06T0456Z_role-model-and-executors.md and are not'
    34  'permanent capability guarantees:**'
A. source contains 'not re-verified by this task and': True
B. head contains 'not re-verified by <NEW> and': True
C. substitution applied ONCE to normalised source == normalised head: True
D. occurrences of 'this task' in source / head: 1 / 0
E. identical prefix lines 70, identical suffix lines 59; changed region is ONE contiguous block: source 71..72 -> head 71..73
```

**Three independent confirmations that A4 is the only difference:**

1. **One hunk.** `git diff --no-index` against the source blob produces
   exactly one `@@` hunk.
2. **One contiguous region.** 70 identical leading lines and 59 identical
   trailing lines bracket a single changed block: source lines 71–72
   become head lines 71–73.
3. **Substitution-exact.** Applying the substitution **once** to the
   whitespace-normalised source reproduces the whitespace-normalised head
   **exactly**. This is the strongest of the three, because it proves the
   re-wrapping is content-neutral: no word was added, dropped or reordered
   anywhere in the file. `this task` occurs once in the source and zero
   times at head.

**On the re-wrap.** The replacement text is 49 characters longer than
what it replaces. Substituting in place would have left a 118-character
line in a document otherwise wrapped near 70. I re-wrapped the sentence
across three lines instead, which is an incidental implementation choice
under `CONVENTIONS.md` rule 8, and proved it content-neutral by check 3
above. The longest line in the file is unchanged at 112 characters and is
pre-existing (`## Research rules` item 12), not introduced here.

---

## 5. A6-pre — scope check against commit 2

### 5.1 Supplied manifest TEMPLATE, reproduced

```text
base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
mode: exact
add:
  specs/2026-08-06T{HHMM}Z_role-model-clean-rebuild.md
  specs/2026-08-06T0456Z_role-model-and-executors.md
modify:
  AGENTS.md
  reviews/README.md
  HANDOFF.md
  PROGRESS.md
  DECISION_LOG.md
forbidden_operations:
  delete, rename, copy, type_change, unmerged, unknown
```

### 5.2 RESOLVED invocation manifest

Created outside the repository; **no manifest file is committed.** Only
the two permitted transformations were applied: the **single** `{HHMM}`
placeholder resolved to `1218`, the token fixed by commit 1, and the
computed `head` added. **The `0456` token in the reproduced original's
path was not regenerated** — it belongs to the original task. No path,
operation assignment, `mode`, `base` or forbidden-operation entry was
changed. The template's `add:`/`modify:` grouping is expressed in the
checker's input language as `{"operation": …, "path": …}` records in the
same order; `optional` is absent, which the tool treats as the empty
list.

```json
{
    "base": "a0e9d11b7281f0c2185aa8d517bae009ab54807f",
    "head": "cb9e70c5707870e9dce7076ceeabd2a58115cb32",
    "mode": "exact",
    "required": [
        {"operation": "add", "path": "specs/2026-08-06T1218Z_role-model-clean-rebuild.md"},
        {"operation": "add", "path": "specs/2026-08-06T0456Z_role-model-and-executors.md"},
        {"operation": "modify", "path": "AGENTS.md"},
        {"operation": "modify", "path": "reviews/README.md"},
        {"operation": "modify", "path": "HANDOFF.md"},
        {"operation": "modify", "path": "PROGRESS.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
    ],
    "forbidden_operations": [
        "delete",
        "rename",
        "copy",
        "type_change",
        "unmerged",
        "unknown"
    ]
}
```

**Resolved manifest SHA-256:**
`6bd13752286746e200f2a6c733e2164ea5c1390b425d69e6f72bf5540a165a6e`

```text
$ sha256sum a6_pre.json
6bd13752286746e200f2a6c733e2164ea5c1390b425d69e6f72bf5540a165a6e  a6_pre.json
```

**Token proof:**

```text
  1218  specs/2026-08-06T1218Z_role-model-clean-rebuild.md
  0456  specs/2026-08-06T0456Z_role-model-and-executors.md
  rebuild-spec token == 1218 (fixed by commit 1): True
  original-spec token == 0456 (NOT regenerated): True
  unresolved {HHMM} anywhere: False
```

### 5.3 Complete A6-pre output

Run on a clean detached worktree at commit 2, verified clean beforehand.

```text
$ python -m scripts.governance_tools.scope_checker --repo . --manifest a6_pre.json
--- stdout:
{
  "base": "a0e9d11b7281f0c2185aa8d517bae009ab54807f",
  "failures": [],
  "head": "cb9e70c5707870e9dce7076ceeabd2a58115cb32",
  "mode": "exact",
  "observed_operations": [
    {
      "operation": "modify",
      "path": "AGENTS.md"
    },
    {
      "operation": "modify",
      "path": "DECISION_LOG.md"
    },
    {
      "operation": "modify",
      "path": "HANDOFF.md"
    },
    {
      "operation": "modify",
      "path": "PROGRESS.md"
    },
    {
      "operation": "modify",
      "path": "reviews/README.md"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-06T0456Z_role-model-and-executors.md"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-06T1218Z_role-model-clean-rebuild.md"
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}
--- stderr:
(empty)

process exit status: 0
```

`overall: PASS`, `failures: []`, and `observed_operations` lists exactly
the seven declared records — five `modify` and two `add` — with no
eighth.

**A6-pre shows only that the content changes were within scope before the
report was added.** It cannot confirm that this report's own path is
inside the frozen manifest; only **A6-final can, and A6-final carries the
scope verdict.** A6-final is returned as post-commit evidence, not
written here, because its `head` is this report's own commit.

---

## 6. A7-pre — validators on a clean worktree at commit 2

Five validators run individually, **before this report file existed**, on
a clean detached worktree at commit `cb9e70c5707870e9dce7076ceeabd2a58115cb32`. Cache provider disabled
(`-p no:cacheprovider`), bytecode writing suppressed
(`PYTHONDONTWRITEBYTECODE=1`), `--basetemp` outside the repository.
stdout and stderr were captured together (`2>&1`) so the transcript below
is complete. The worktree was verified clean before and after.

```text
A7-pre — five validators, individually, clean worktree at commit 2 (before the report exists)
worktree: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
worktree HEAD: cb9e70c5707870e9dce7076ceeabd2a58115cb32
worktree status --porcelain (pre-run): (empty == clean)
report file present at commit 2: 0
0

$ python -VV
Python 3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
$ python -m pytest --version
pytest 9.1.1
$ python -c "import sys; print(sys.executable)"
/usr/local/bin/python
================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_repository_structure.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rbt-c2
---------------- stdout + stderr (2>&1, complete) ----------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
configfile: pyproject.toml
collected 4 items

tests/test_repository_structure.py ....                                  [100%]

============================== 4 passed in 0.02s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.49 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_si1_governance.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rbt-c2
---------------- stdout + stderr (2>&1, complete) ----------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
configfile: pyproject.toml
collected 14 items

tests/test_si1_governance.py ..............                              [100%]

============================== 14 passed in 0.05s ==============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.26 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_gate_anchors.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rbt-c2
---------------- stdout + stderr (2>&1, complete) ----------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
configfile: pyproject.toml
collected 20 items / 2 deselected / 18 selected

tests/test_gate_anchors.py ..................                            [100%]

======================= 18 passed, 2 deselected in 9.96s =======================
----------------------------------------------------------------
process exit status: 0
wall time: 10.50 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_governance_tools.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rbt-c2
---------------- stdout + stderr (2>&1, complete) ----------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
configfile: pyproject.toml
collected 8 items

tests/test_governance_tools.py ........                                  [100%]

============================== 8 passed in 1.71s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 1.97 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_scalar_exploratory.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rbt-c2
---------------- stdout + stderr (2>&1, complete) ----------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/rb-c2
configfile: pyproject.toml
collected 5 items

tests/test_p2_phase01_scalar_exploratory.py .....                        [100%]

============================== 5 passed in 0.28s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.54 s

worktree status --porcelain (post-run): (empty == still clean)
```

**A7-pre summary:** five runs, five genuine exit-0 statuses, 49 tests
collected and passed, 2 deselected in `tests/test_gate_anchors.py` by its
own marker configuration. No run reported "no tests ran". Python
3.11.15, pytest 9.1.1, platform linux, interpreter
`/usr/local/bin/python`.

**A7-pre shows only that the content changes passed before the report was
added. A7-final carries the acceptance verdict** and is returned as
post-commit evidence.

---

## 7. A8 — branch only, and the state of `main`

```text
$ git rev-parse --abbrev-ref HEAD
review/role-model-and-executors-clean
$ git rev-parse main
0f7961747abe2a18b436c0b1e5b928f425ea4d9a
$ git rev-parse origin/main
a0e9d11b7281f0c2185aa8d517bae009ab54807f
$ git ls-remote origin refs/heads/main
a0e9d11b7281f0c2185aa8d517bae009ab54807f	refs/heads/main
$ git rev-parse review/role-model-and-executors-clean   (task branch head)
cb9e70c5707870e9dce7076ceeabd2a58115cb32
$ git rev-parse review/role-model-and-executors          (reviewed branch, must be unchanged)
10c260b96882ac12610f78840aeeabd07be2d7cb
$ git merge-base --is-ancestor 0f79617 a0e9d11b; echo $?   (local main ancestor of origin/main)
0
$ git rev-list --count 0f79617..a0e9d11b   (commits origin/main is ahead)
79
$ git rev-list --count a0e9d11b..0f79617   (commits local main has that origin/main lacks)
0
$ git reflog show main -n 2
0f79617 main@{0}: commit: docs: Arm H decisive merge verification report
3c0c484 main@{1}: merge 9b0ceed: Merge made by the 'ort' strategy.
$ git log --format="%H %s" a0e9d11b..review/role-model-and-executors-clean
cb9e70c5707870e9dce7076ceeabd2a58115cb32 Adopt the function-based role model; record the dual-executor arrangement
7740f45e2d30647704804484e547c45542a21c84 specs: record the clean-rebuild execution authority
```

| Item | Value |
| --- | --- |
| Task branch | `review/role-model-and-executors-clean` |
| Task branch base | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| local `main` | `0f7961747abe2a18b436c0b1e5b928f425ea4d9a` |
| `origin/main` | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| remote `refs/heads/main` (`ls-remote`) | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| `review/role-model-and-executors` (preserved) | `10c260b96882ac12610f78840aeeabd07be2d7cb` |

`main` was not checked out, modified, reset, merged into or pushed —
local or remote. Its reflog head is unchanged at `main@{0}`.

**`origin/main` has advanced beyond local `main` through other authorized
work, and is reported rather than altered.** Local `main` (`0f79617`) is
a strict ancestor of `origin/main` (`a0e9d11b`): `git merge-base
--is-ancestor` exits 0 in that direction, `origin/main` is **79** commits
ahead, and local `main` holds nothing `origin/main` lacks. The task base
is `origin/main`, the current remote tip — which is what the
specification's evidence base names. Nothing here required action and
none was taken.

---

## 8. The role model as landed on this branch

This section is descriptive and unchanged in substance from the reviewed
report; the quotations below were re-extracted from **this branch's**
commit 2, not copied.

### 8.1 `AGENTS.md` — superseded

```text
## Role separation

- ChatGPT handles conceptual discussion, physical interpretation, analytic
  derivation planning, gate design, calculation specifications, assumptions,
  and competing interpretations. It does not certify numerical results.
- Codex handles repository maintenance, implementation, tests, regression
  anchors, reproducibility, result files, branches, and commits. It must not
  promote a result into a paper claim without review.
- Claude is the independent reviewer/discriminator, issues gate verdicts,
  identifies overclaims, and updates the paper only after accepted results.
- The User / Principal Investigator owns the programme, approves assumptions,
  gates, and scope changes, accepts or rejects verdicts, and authorizes paper
  updates.
```

### 8.2 `AGENTS.md` — superseding, as landed at commit 2

```text
**Roles are functions. Assignments are current, and change by PI
instruction.**

- **PI** — decides. Model conception, research direction, and all
  authorizations. *Currently: Zeta Cheng.*
- **Researcher** — builds the theory with the PI and supplies the
  background knowledge it needs; writes proposals; turns the PI's
  intent into verifiable specifications; revises against reviewer
  comment; and interprets executor results for the PI. *Currently:
  Claude (chat).*
- **Reviewer** — reviews specifications and executor results, and
  raises questions. **Every execution specification or other normative
  task instruction that establishes or changes the Executor's
  authority, and every integration authorization, requires the
  Reviewer's agreement before being issued to the Executor** — except
  where the governing rules expressly provide a standardized
  authorization or permit a recorded correction without a new review
  cycle. **Incidental implementation exchanges within an
  already-reviewed authorization are not separate review points**, per
  rules 8 and 11.
  *Currently: ChatGPT.*
- **Executor** — performs the work and is the only party that writes
  to the repository. *Currently: Codex and Claude Code, selected per
  task (see below).*

**The Researcher and Reviewer functions are exchanged from time to
time, by PI instruction, with the intent of placing the stronger
available capability in the Reviewer function.** An assignment
recorded here is current, not permanent.

**Minor corrections** may proceed without a further review cycle only
to the extent already authorized by `CONVENTIONS.md` rule 10 and the
current reviewed specification. They must be confined to
executor-editable artifacts; must not alter reviewed meaning,
objectives, claims, invariants, or frozen or hash-pinned content; and
must satisfy rule 10's reporting and mechanical-equivalence
requirements where applicable. **An instruction from the PI or the
Researcher does not by itself expand the Executor's authorized scope.**
Every such correction is recorded in the task report. Any substantive
or otherwise unauthorized change requires re-review, or a separately
committed PI authorization.
```

The superseded text is not deleted. It is preserved byte-for-byte under
`### Historical role assignment — superseded 2026-08-06`, explicitly
labelled non-operative, and cross-referenced to `CONVENTIONS.md` rule 8
and the `DECISION_LOG.md` entry.

**The substantive change.** The base text assigned three named agents to
three fixed jobs. The superseding text names four functions and attaches
a *current* assignment to each, so an exchange of the Researcher and
Reviewer functions is a change of assignment rather than a contradiction
of the document. It also adds two things the base text did not contain:
the Reviewer's agreement as a precondition on normative task
instructions, and an explicit ceiling on minor corrections.

### 8.3 `reviews/README.md` — superseded

```text
# Reviews

Store independent review records here. ChatGPT material may document planning
and interpretation but does not certify numerical results. Claude reviews
derivations and results, identifies overclaims, and records a gate verdict.
Final acceptance or rejection belongs to the Principal Investigator.
```

### 8.4 `reviews/README.md` — superseding

The by-author layout is retained and described; a `Function:` header is
required on every review, Researcher record, Executor record or PI
authorization **created or substantively amended after** the 2026-08-06
decision; existing records remain valid historical evidence and are not
retrospectively non-conforming. The superseded paragraph is preserved as
a labelled non-operative blockquote. **This report carries
`Function: Executor`** in its header.

---

## 9. Provenance of the capability statements

Unchanged in substance from the reviewed report, with the "verified
directly" rows **re-established on this branch** rather than inherited.

| Statement as recorded in `AGENTS.md` | Classification |
| --- | --- |
| Two executors are in use, selected per task by the PI according to quota and capability | **PI-supplied fact** (a decision, recorded on PI instruction) |
| They are not interchangeable, and the difference is material rather than administrative | **PI-supplied characterisation** |
| Codex runs on the PI's workstation | **PI-supplied fact.** Not observable from this container. |
| The workstation has a GPU (RTX 4070 Ti) | **PI-supplied fact.** Not observable from this container; no GPU inventory was taken. |
| The workstation has no short process-termination limit | **PI-supplied fact**, not re-verified here. |
| Claude Code runs in a sandboxed container | **Verified directly**, trivially: this task ran there. |
| Claude Code reaches genuine exit 0 on the validator suite | **Verified directly on THIS branch** — §6 above: five individual runs at commit `cb9e70c`, five exit-0 statuses, 49 tests collected and passed. A current observation at this revision, not a permanent guarantee. |
| …"which the workstation currently cannot" | **PI-supplied observation about the other host.** Not re-verified here, and not verifiable from here. |
| Claude Code is ephemeral and starts from a stale tree each session | **Current environment observation, verified indirectly again this session:** local `main` was `0f79617` while `origin/main` was `a0e9d11b`, 79 commits ahead (§7). Observed, not guaranteed. |
| Claude Code "has been observed to lose a long-running job" | **Prior-session observation, recorded, not reproduced here.** No long-running job was launched by this task. |
| Short deterministic verification, preparation and audit belong here; decisive multi-hour runs do not | **PI allocation decision**, recorded. Not a measurement. |

**Nothing in the dual-executor section was established by this task
except the two rows marked "verified directly".** After A4 the
`AGENTS.md` text now carries that limit with a resolvable antecedent: the
capability statements are "not re-verified by the task recorded in
specs/2026-08-06T0456Z_role-model-and-executors.md and are not permanent
capability guarantees".

---

## 10. Further conflicts — reported, not touched

The three conflicts found while executing the original task **remain
open and were deliberately not touched**, as §5 of this specification
directs: `docs/RESEARCH_WORKFLOW.md` (a full fixed-agent role section at
lines 11–27, made operative at line 47), `README.md:36` (the same
statement in one sentence), and `docs/local/execution_environment.md`
(one declared execution identity where two hosts are now recorded). They
are a separate authorized task. Re-confirmed present at this branch head
and unmodified: they lie outside the eight executor-writable paths, and
the A5 and A6 checks would have failed had any been edited.

---

## 11. Authorization provenance

- This execution was performed under
  `specs/2026-08-06T1218Z_role-model-clean-rebuild.md`, committed in full
  as commit 1, blob SHA-256
  `d07e923d16f516ecbd723deb2259c945a5a995da711eb401c54d80a76dc1a6ea`.
  Every claim in this report therefore has a corresponding instruction in
  the repository.
- That specification states its own authority: it authorizes the rebuild
  the previous specification could not, and authorizes exactly one
  content correction (A4).
- **No mid-task amendment was issued.** Nothing changed after the
  specification was received, so there is nothing to reproduce verbatim
  under that heading.
- I hold no separate Reviewer-agreement artifact for this specification
  and did not verify one. Under the model recorded here that agreement is
  a precondition on issuing the specification and sits with the PI and
  Reviewer; it is not an Executor-verifiable fact from inside the
  repository. **Recorded as a limit on this report, not as a defect.**

---

## 12. Stops and clarifications

**No stop occurred.** No command that reads or alters repository state
produced an unexpected result, no criterion was unsatisfiable, and no
unauthorized metadata appeared in any stored message. Each categorised
item below carries exactly one primary category.

### 12.1 `OBSERVATION_METHOD_ERROR` — my own scratch tooling, corrected

Two defects, both in scratch tooling outside the repository, both
corrected. Neither touched repository state, and no commit was affected.

1. **Unsupported `git diff` flag.** My first A4 evidence command used
   `git diff --no-index --label …`, which this Git build does not
   support; it exited 129 with a usage dump. I re-ran using
   `--src-prefix` / `--dst-prefix`, which this build does support. The
   evidence in §4 is from the corrected command. **Stop-on-unexpected-result
   applies to commands that read or alter repository state, not to my own
   scratch tooling; I corrected the tooling and am saying so.**
2. **A misleading `grep -c` guard.** In the A7-pre preamble a
   `grep -c … || echo 0` printed `0` twice, because `grep -c` prints `0`
   *and* exits non-zero when there are no matches. The value is correct —
   no report file exists at commit 2 — but the duplicated line is noise. I
   left the captured transcript as emitted rather than editing raw output.

### 12.2 `ENVIRONMENT` — nothing missing, nothing installed

Rule 13's diagnostic order was not needed: every required tool resolved
on first use — Python 3.11.15, pytest 9.1.1, `git`,
`scripts/governance_tools`. **Nothing was installed and no persistent or
global configuration was changed.** All five validators reached genuine
exit 0 in both A7 passes.

### 12.3 `REPOSITORY_DEFECT` — a factual error in the reviewed report, corrected here

The reviewed report at
`review/role-model-and-executors` @ `10c260b9…` states that `origin/main`
is **89** commits ahead of local `main`. The correct figure is **79**:

```text
$ git rev-list --count 0f79617..a0e9d11b
79
```

I produced the 89 by counting lines in a `git log` listing rather than
using `git rev-list --count` — an arithmetic slip in a committed record,
not a change in repository state. §7 of **this** report carries the
correct figure, derived from the counting command. **The reviewed report
is not edited**: it is preserved as the record of what happened, and this
is the correction of record. Nothing else in that report depends on the
number.

### 12.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — commit-object identity and signing

§2 forbids "automatically generated attribution" in commit messages and
separately forbids changing persistent user or global configuration.
Commit **object headers** — the SSH signature and the
`Claude <noreply@anthropic.com>` author/committer identity — are
generated automatically from global configuration and are not message
content. Removing them would require exactly the configuration change §2
prohibits. **I did not resolve this.** The headers are present, disclosed
in §2.3, and identical in kind to those on the reviewed commits the PI
accepted. **Flagged for the Reviewer**; if commit-object identity is
meant to be in scope, that needs a separate authorization.

### 12.5 The A4 re-wrap — clarification, no category

A4 specifies a text substitution, not a line layout. I re-wrapped the
affected sentence rather than leave a 118-character line, treated the
choice as incidental implementation under rule 8, and proved it
content-neutral mechanically (§4, check 3). Disclosed because a reviewer
diffing line-by-line will see three changed lines where the substitution
alone would have produced one.

### 12.6 Secondary findings

The three stale-role-text conflicts (§10) were carried forward from the
previous task, are classified `REPOSITORY_DEFECT` (the first two) and
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` (the third), and were
deliberately not acted on: this specification places them out of scope.

---

## 13. Ambiguous, unsatisfiable, or what I would have specified differently

- **Nothing was unsatisfiable.** Every criterion A0–A8 was checkable as
  written.
- **The rebuild's specification and the report do not share a token, and
  the specification says so — but nothing mechanical enforces it.** A6's
  manifests pin both paths, so a mismatch would fail the scope check;
  that is adequate. It is worth noting that the pairing convention
  established by the earlier task ("correlation is by timestamp") is
  **deliberately broken here**, and only the §0 identification block
  explains why. A reader who sees only the filenames will pair this
  report with the wrong specification. **If this pattern recurs, the
  report should carry the authority path as a header field**, not only in
  a prose section.
- **A4's replacement text is not given as a byte-for-byte block.** It is
  given inline as `the task recorded in specs/…`, and I had to decide
  whether the surrounding backticks were markdown delimiters or literal
  content, and whether to re-wrap. I read them as delimiters and did not
  add backticks in `AGENTS.md`. **Given that the previous task's
  four-word omission is the reason A4 exists at all, a replacement string
  intended to land byte-for-byte should be supplied in an indented
  verbatim block**, as A1a and A6 of the earlier specification were.
- **"One-hunk diff" is a weaker criterion than it looks.** A hunk is a
  diff-algorithm artifact: a large rewrite of one contiguous paragraph is
  also one hunk. The substitution-exactness check in §4 is what actually
  constrains the change, and I added it because the specified criterion
  would not have caught, for instance, a silently dropped word inside the
  re-wrapped sentence. **A future specification should ask for the
  substitution-exactness property directly.**
- **A1 pins source blob ids but not the reviewed branch's tree.** Pinning
  the six blobs plus the source-reference tree is nearly complete, but a
  seventh file could in principle have been introduced at commit 2 and
  caught only by A6's `mode: exact` manifest. The combination is sound;
  A1 read alone is not, and the specification is explicit that A6 carries
  part of the verdict.
- **The report cannot verify the Reviewer agreement that the model it
  records makes a precondition** (§11). This is inherent to the
  arrangement, not a defect in the specification: the Executor cannot see
  the review exchange, and by PI decision that exchange is not committed.
