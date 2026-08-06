# Task report — adopt the function-based role model and record the dual-executor arrangement

Function: Executor
Date: 2026-08-06
Task classification: MATERIAL (branch only; integration is a separate
authorization after result review)
Specification: `specs/2026-08-06T0456Z_role-model-and-executors.md`
Executor: Claude Code (sandboxed container)

**This report is the deliverable.** The conversational summary that
accompanies it is a convenience.

**This task decided nothing.** It records decisions the PI made on
2026-08-06 and transcribes text supplied in the specification. Where the
specification's supplied text and my judgement could have differed, the
supplied text was used and the disagreement is recorded in
§11 rather than resolved.

---

## 1. Identification

| Item | Value |
| --- | --- |
| Branch | `review/role-model-and-executors` |
| Base commit | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| Commit 1 (specification) | `031540028a57c4132f395aa9ad4b1e573c910ea6` |
| Commit 2 (content changes) | `a021eedc6bf540edb54f580b0c31bcf35fb4a8ae` |
| Pre-report head | `a021eedc6bf540edb54f580b0c31bcf35fb4a8ae` (= commit 2) |
| UTC token `{HHMM}` | `0456` |
| Observed UTC timestamp when the token was taken | `2026-08-06T04:56:17Z` |
| Specification blob SHA-256 | `f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd` |

**Commit 1 message.** The authored message is a single subject line with
no body:

```text
specs: record the approved role-model and dual-executor specification
```

The stored message additionally carries **two trailer lines added by the
commit tooling, not authored by me** — a `Co-Authored-By:` line and a
`Claude-Session:` line. They are described rather than reproduced,
because they carry a session URL and a tool version string that do not
belong in a committed repository record; they cannot be removed without
rewriting history, which is prohibited. Verify with
`git log --format=%B -1 031540028a57c4132f395aa9ad4b1e573c910ea6`, which
yields the subject line above, a blank line, and those two trailers, in
that order, and nothing else. Commit 2 and commit 3 were created with
`git commit -F -` and carry no trailers.

**Commit 2 message**, exactly as stored:

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
  the specification blob committed as commit 1.

Capability statements in the dual-executor section are PI-supplied
operational findings and current observations, not re-verified here and
not permanent guarantees.
```

**Intended commit-3 message** (the commit that adds this report):

```text
docs: task report for the function-based role model and dual-executor record

Records A0-A7 raw evidence, A8-pre scope evidence and A9-pre validator
output for the role-model adoption on this branch. Commit 3's own SHA,
the final branch head, A8-final and A9-final are returned as
post-commit evidence and are deliberately absent here: the report
cannot contain its own commit.
```

**This report does not record commit 3's SHA or the final branch head.**
It cannot: commit 3 is this report.

---

## 2. A0 — the approved specification, committed as commit 1

### 2.1 Mechanical part

```text
A0 — commit 1 mechanical evidence

$ git diff-tree --no-commit-id --name-status -r --find-renames --find-copies a0e9d11b7281f0c2185aa8d517bae009ab54807f 0315400
A	specs/2026-08-06T0456Z_role-model-and-executors.md

$ git diff-tree --no-commit-id --numstat -r a0e9d11b 0315400
543	0	specs/2026-08-06T0456Z_role-model-and-executors.md

$ git ls-tree --full-tree -r --name-only 0315400 -- specs/
specs/2026-08-06T0456Z_role-model-and-executors.md

$ git rev-parse 0315400
031540028a57c4132f395aa9ad4b1e573c910ea6

$ git cat-file blob 0315400:specs/2026-08-06T0456Z_role-model-and-executors.md | sha256sum   (method A)
f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd  -

$ pipe-free control: hashlib over git-show bytes
f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd 26351 bytes
CRLF present: False | lone CR: False
final byte: b'\n'

$ token consistency: specification path vs report path
spec token = 0456  report token = 0456  identical = True

$ ancestry: every later commit descends from commit 1
  0315400 is ancestor of $c: yes
```

The two independent digest methods agree:
`git cat-file blob … | sha256sum` and a pipe-free `hashlib.sha256` over
`git show` bytes both give
`f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd`.
Commit 1 adds exactly one path, `specs/…`, and nothing else (`A` is the
only name-status record). The specification path and this report path
carry the same token `0456`.

### 2.2 Attestation part — not machine-provable

**There is no canonical input object to compare against**, so what
follows is a declaration, not a proof of equality with conversation
text.

I am aware of the following, and of nothing else:

- **No truncation.** Every section of the specification as received
  (title, evidence-base header, §0 the quoted conflict, §1 objective
  including all four supplied blockquotes, §2 acceptance criteria A0–A10
  including both A8 manifest blocks, the evidence-layering section, §3
  invariants and prohibitions, §4 report contract including the five
  stop categories) is present in the committed blob.
- **No intentional rewording or omission.** The prose is transcribed as
  received, including emphasis markers.
- **One class of transformation I did apply, and disclose here:** the
  specification was received as chat text; I wrote it to a UTF-8 file
  with LF line endings and a single trailing newline. The committed blob
  contains no CRLF pair and no lone CR (verified above), is 26,351
  bytes, and ends in `0x0A`. Indentation of the supplied indented blocks
  (the §0 quotations, the A1/A1a/A6 literal blocks, and the two A8
  manifest templates) is preserved as four-space code indentation, which
  is how it was received.
- **No normalisation of the supplied verbatim blocks.** The A1a
  historical block and the A6 staleness notice were transcribed into the
  specification and, separately, into the target files, and both are
  verified byte-for-byte in §3 below. That cross-check would have
  detected a silent reflow of either block.
- I did not reflow, reorder, renumber, or "tidy" any part of the
  specification. `specs/` did not exist and was created by commit 1.

---

## 3. A1–A7 — raw verifier output at commit 2

**How these were produced.** A scratch verifier outside the repository
read the files and the Git objects at commit
`a021eedc6bf540edb54f580b0c31bcf35fb4a8ae`. It is scratch tooling and is
not committed. Every check is a fixed-string count, a byte comparison, or
a Git object comparison; the underlying primitives are
`git show <rev>:<path>` (file bytes),
`git ls-tree -r --full-tree --format='%(objectmode) %(objecttype) %(objectname) %(path)'`
(blob enumeration and blob ids),
`git ls-tree -d --name-only` (immediate child directories), and
`git diff --name-status --find-renames --find-copies <base> <head> -- <prefixes>`
(add/delete/rename/copy/type-change detection). No value was accepted as
quoted; all were read from the objects.

Region split for A1: the operative region is everything before the
historical heading
`### Historical role assignment — superseded 2026-08-06`; the historical
region runs from that heading to the next heading of the same or higher
level. Text after the historical region (the `## Research rules` tail) is
in neither region and is reported as `tail` for completeness.

```text
$ python3 acheck.py a021eedc6bf540edb54f580b0c31bcf35fb4a8ae
A1 regions: operative=4317B  historical=1020B  tail=946B

A1 — present exactly once, operative region:
   OK    op=1 hist=0  'Roles are functions. Assignments are current'
   OK    op=1 hist=0  'The Researcher and Reviewer functions are exchanged'
   OK    op=1 hist=0  "does not by itself expand the Executor's authorized scope"
   OK    op=1 hist=0  'Incidental implementation exchanges'
A1 — present at least once, operative region:
   OK    op=3  'Researcher'
   OK    op=4  'Reviewer'
   OK    op=4  'Executor'
A1 — present exactly once, historical region only:
   OK    op=0 hist=1  'Claude is the independent reviewer/discriminator'
A1 — count in operative region of each superseded phrase must be 0:
   OK    op=0  'ChatGPT handles conceptual discussion'
   OK    op=0  'Codex handles repository maintenance'
   OK    op=0  'Claude is the independent reviewer/discriminator'
A1 — no region holds both an operative and a historical copy:
   OK    disjoint 'Roles are functions. Assignments are current' (op=1 hist=0)
   OK    disjoint 'ChatGPT handles conceptual discussion' (op=0 hist=1)
   OK    disjoint 'Codex handles repository maintenance' (op=0 hist=1)
   OK    disjoint 'Claude is the independent reviewer/discriminator' (op=0 hist=1)

A1a — historical block byte-for-byte:
   OK    verbatim present count=1

A2 — reviews/README.md literals, present exactly once:
   OK    count=1  'created or substantively amended after'
   OK    count=1  'Existing records remain valid historical evidence'
   OK    count=1  'Function:'
A2 — reviews/ immediate child directories:
      base=['chatgpt', 'claude', 'codex', 'pi']
      head=['chatgpt', 'claude', 'codex', 'pi']
   OK    base set ['chatgpt', 'claude', 'codex', 'pi']
   OK    head set ['chatgpt', 'claude', 'codex', 'pi']
A2 — pre-existing reviews/ blobs enumerated at base: 9
      name-status base->head under reviews/:
        M	reviews/README.md
   OK    only reviews/README.md modified, nothing added/deleted/renamed (observed 'M\treviews/README.md')
   OK    blob equal reviews/chatgpt/.gitkeep 8b137891791f
   OK    blob equal reviews/claude/.gitkeep 8b137891791f
   OK    blob equal reviews/claude/2026-07-19-paper2-followup.md 2df402bdbca1
   OK    blob equal reviews/claude/2026-08-01-p2-lattice-ontology-01.md 667211398098
   OK    blob equal reviews/codex/2026-08-04-p2-phase-01-feasibility-inventory.md 1c78b0e2ca4a
   OK    blob equal reviews/pi/2026-08-03-governance-tools-environment-authorization.md 930748ed2773
   OK    blob equal reviews/pi/2026-08-03-outcome-based-task-specification-amendment.md dad02415788f
   OK    blob equal reviews/pi/2026-08-03-p2-dual-pipeline-probe-repin.md 1e9be1f8dbbf

A3 — dual-executor arrangement in AGENTS.md:
   OK    count=3  'Codex'
   OK    count=2  'Claude Code'
   OK    count=1  'RTX 4070 Ti'
   OK    count=1  'sandboxed'
   OK    count=1  'As recorded by PI decision on 2026-08-06'

A4 — rule 8 reconciliation:
   OK    'rule 8' count=5
   OK    governing statement present verbatim
      CONVENTIONS.md base=('100644', 'blob', '2d4f735c55a14fdfc5d1031a58698a8ca075fbbd')  head=('100644', 'blob', '2d4f735c55a14fdfc5d1031a58698a8ca075fbbd')
   OK    CONVENTIONS.md byte-identical (blob id + mode + type)

A5 — DECISION_LOG.md field literals (spec sha256=f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd):
   OK    count=1  'Date: 2026-08-06'
   OK    count=1  'Decision owner: Principal Investigator'
   OK    count=1  'Superseded documents: AGENTS.md role section; reviews/README.md'
   OK    count=1  'Effect: prospective only'
   OK    count=1  'No retrospective relabelling of existing reviews/ records'
   OK    count=1  'Reference: CONVENTIONS.md rule 8'
   OK    count=1  'Specification SHA-256: f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd'
   OK    count=1  'Specification path: specs/2026-08-06T0456Z_role-model-and-executors.md'
   OK    pure byte-prefix append (base bytes intact)
      appended 2726 bytes

A6 — staleness notices:
   OK    HANDOFF.md: notice verbatim count=1
   OK    HANDOFF.md: head == base with ONLY the 4-line block inserted immediately below the title line (base 63L -> head 67L)
   OK    HANDOFF.md: deleting exactly the inserted block restores base bytes
   OK    PROGRESS.md: notice verbatim count=1
   OK    PROGRESS.md: head == base with ONLY the 4-line block inserted immediately below the title line (base 66L -> head 70L)
   OK    PROGRESS.md: deleting exactly the inserted block restores base bytes

A7 — protected base blob paths enumerated: 144
   OK    base-vs-head blob id mismatches = []
   OK    name-status over protected prefixes (add/delete/rename/type_change included) = ''
      first 3 enumerated: CONVENTIONS.md=2d4f735c55a1, GATES.md=bd4820513217, derivations/CANONICAL_INTERACTION.json=0c992d83bbd7
      last  3 enumerated: tests/test_p2_phase01_scalar_exploratory.py=5e47fc98fe50, tests/test_repository_structure.py=7d63880dd0b9, tests/test_si1_governance.py=a8aefafce1c2

ALL CHECKS OK

process exit status: 0
```

Every A1–A7 criterion passed as specified. Note in particular:

- **A1**: all four exactly-once literals are at count 1 in the operative
  region and 0 in the historical region; all three superseded phrases are
  at count 0 in the operative region; no phrase appears in both regions.
- **A2**: the only pre-existing `reviews/` path changed is
  `reviews/README.md` — the modification the criterion requires. The
  other eight pre-existing blobs are bit-identical, including
  `reviews/codex/2026-08-04-p2-phase-01-feasibility-inventory.md`, and
  the immediate child directory set is `chatgpt, claude, codex, pi` at
  both base and head. Nothing under `reviews/` was added, deleted,
  renamed or relabelled.
- **A4**: `CONVENTIONS.md` is byte-identical at base and head — same
  blob id `2d4f735c55a14fdfc5d1031a58698a8ca075fbbd`, same mode, same
  type. No rule was created, renumbered or reworded.
- **A6**: for each of `HANDOFF.md` and `PROGRESS.md`, the head file is
  exactly the base file with the four-line notice inserted immediately
  below the title line — verified twice, once by line-list equality
  against a constructed expectation and once by showing that deleting
  exactly those four lines restores the base bytes.
- **A7**: 144 base blob paths were enumerated under `tests/`,
  `scripts/`, `derivations/`, `results/` plus `GATES.md`,
  `CONVENTIONS.md`, `pyproject.toml`; every one has an identical blob id
  at head, and the name-status diff over those prefixes is empty, so
  there is no added, deleted, renamed or type-changed path.

### 3.1 A5 — the `DECISION_LOG.md` entry as landed

All eight field literals are present exactly once (see the block above),
and the file is a pure byte-prefix append: the base bytes are unchanged
and 2,726 bytes were appended. The entry uses the file's existing
`## <date> — <title>` / `### Decision` / `### Reason` format.

---

## 4. A8-pre — scope check against commit 2

### 4.1 The supplied manifest TEMPLATE, reproduced

```text
base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
mode: exact
add:
  specs/2026-08-06T{HHMM}Z_role-model-and-executors.md
modify:
  AGENTS.md
  reviews/README.md
  HANDOFF.md
  PROGRESS.md
  DECISION_LOG.md
forbidden_operations:
  delete, rename, copy, type_change, unmerged, unknown
```

### 4.2 The RESOLVED invocation manifest

Created outside the repository at
`<scratch>/a8_pre.json`; **no manifest file is committed.** Exactly the
two permitted transformations were applied: the single `{HHMM}`
occurrence was replaced by the token `0456` fixed by commit 1, and the
computed `head` field was added. No path, operation assignment, `mode`,
`base`, or forbidden-operation entry was changed. The template's
`add:`/`modify:` grouping is expressed in the checker's input language as
`{"operation": …, "path": …}` records in the same order; `optional`
was left absent, which the tool treats as the empty list.

```json
{
    "base": "a0e9d11b7281f0c2185aa8d517bae009ab54807f",
    "head": "a021eedc6bf540edb54f580b0c31bcf35fb4a8ae",
    "mode": "exact",
    "required": [
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
`5e457698f4d4a12d8935a445b2918ecc61cd12b6ac1d793014b404b8d161d8af`

```text
$ sha256sum a8_pre.json
5e457698f4d4a12d8935a445b2918ecc61cd12b6ac1d793014b404b8d161d8af  a8_pre.json
```

**Proof that all resolved paths carry the token fixed by commit 1:**

```text
tokenised paths: ['specs/2026-08-06T0456Z_role-model-and-executors.md']
tokens: ['0456']  all == 0456: True
unresolved {HHMM} anywhere: False
```

Commit 1's filename is
`specs/2026-08-06T0456Z_role-model-and-executors.md` (see §2.1,
`git ls-tree`), so `0456` is the token fixed by commit 1.

### 4.3 Complete A8-pre output

Run on a clean detached worktree at commit 2.

```text
$ python -m scripts.governance_tools.scope_checker --repo . --manifest a8_pre.json
{
  "base": "a0e9d11b7281f0c2185aa8d517bae009ab54807f",
  "failures": [],
  "head": "a021eedc6bf540edb54f580b0c31bcf35fb4a8ae",
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
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}

process exit status: 0
```

`overall: PASS`, `failures: []`, and `observed_operations` lists exactly
the six declared records — five `modify` and one `add` — with no
seventh.

**A8-pre shows only that the content changes were within scope before the
report was added.** It cannot confirm that this report's own path is
inside the frozen manifest; only A8-final can, and A8-final carries the
scope verdict. A8-final is returned as post-commit evidence, not written
here, because its `head` is this report's own commit.

---

## 5. A9-pre — validators on a clean worktree at commit 2

Five validators run individually, before this report file existed, on a
clean detached worktree at commit
`a021eedc6bf540edb54f580b0c31bcf35fb4a8ae`. Cache provider disabled
(`-p no:cacheprovider`), bytecode writing suppressed
(`PYTHONDONTWRITEBYTECODE=1`), `--basetemp` outside the repository. The
worktree was verified clean before and after the runs.

```text
A9-pre — five validators, individually, on a clean worktree at commit 2

worktree: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
worktree HEAD: a021eedc6bf540edb54f580b0c31bcf35fb4a8ae
worktree status --porcelain: (empty above == clean)

$ python -VV
Python 3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
$ python -c "import pytest; print(pytest.__version__)"
9.1.1
$ python -m pytest --version
pytest 9.1.1
$ which python; python -c "import sys; print(sys.executable)"
/usr/local/bin/python
/usr/local/bin/python
================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_repository_structure.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-c2
----------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
configfile: pyproject.toml
collected 4 items

tests/test_repository_structure.py ....                                  [100%]

============================== 4 passed in 0.03s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.62 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_si1_governance.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-c2
----------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
configfile: pyproject.toml
collected 14 items

tests/test_si1_governance.py ..............                              [100%]

============================== 14 passed in 0.07s ==============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.39 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_gate_anchors.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-c2
----------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
configfile: pyproject.toml
collected 20 items / 2 deselected / 18 selected

tests/test_gate_anchors.py ..................                            [100%]

======================= 18 passed, 2 deselected in 9.85s =======================
----------------------------------------------------------------
process exit status: 0
wall time: 10.41 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_governance_tools.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-c2
----------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
configfile: pyproject.toml
collected 8 items

tests/test_governance_tools.py ........                                  [100%]

============================== 8 passed in 1.63s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 1.86 s

================================================================
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_scalar_exploratory.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-c2
----------------------------------------------------------------
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-c2
configfile: pyproject.toml
collected 5 items

tests/test_p2_phase01_scalar_exploratory.py .....                        [100%]

============================== 5 passed in 0.27s ===============================
----------------------------------------------------------------
process exit status: 0
wall time: 0.53 s
```

**A9-pre summary:** five runs, five genuine exit-0 statuses, 49 tests
collected and passed, 2 deselected in `tests/test_gate_anchors.py` by its
own marker configuration. No run reported "no tests ran" or "no
applicable files". Interpreter Python 3.11.15, pytest 9.1.1, platform
linux.

**A9-pre shows only that the content changes passed before the report was
added. A9-final carries the acceptance verdict** and is returned as
post-commit evidence.

---

## 6. A10 — branch only, and the state of `main`

```text
$ git rev-parse --abbrev-ref HEAD
review/role-model-and-executors
$ git rev-parse main
0f7961747abe2a18b436c0b1e5b928f425ea4d9a
$ git rev-parse origin/main
a0e9d11b7281f0c2185aa8d517bae009ab54807f
$ git rev-parse review/role-model-and-executors
a021eedc6bf540edb54f580b0c31bcf35fb4a8ae
$ git merge-base --is-ancestor a0e9d11b7281f0c2185aa8d517bae009ab54807f review/role-model-and-executors; echo $?
0
$ git log --format="%H %s" a0e9d11b..review/role-model-and-executors
a021eedc6bf540edb54f580b0c31bcf35fb4a8ae Adopt the function-based role model; record the dual-executor arrangement
031540028a57c4132f395aa9ad4b1e573c910ea6 specs: record the approved role-model and dual-executor specification
$ git reflog show main -n 3
0f79617 main@{0}: commit: docs: Arm H decisive merge verification report
3c0c484 main@{1}: merge 9b0ceed: Merge made by the 'ort' strategy.
11c8ee9 main@{2}: commit: docs: canonical report for the betaV campaign prereg + fix-round merge
$ CONVENTIONS.md rule-8 sentence relied on:
particular agent.

These are FUNCTIONS, not fixed agents: specification/theory,
execution/experimentation, and independent review/verification. **PI
authorization sits above all three** — adoption, exceptions, and final
decisions are the PI's, and no rule in this section transfers that
authority.
```

| Item | Value |
| --- | --- |
| Task branch | `review/role-model-and-executors` |
| Task branch base | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |
| local `main` | `0f7961747abe2a18b436c0b1e5b928f425ea4d9a` |
| `origin/main` | `a0e9d11b7281f0c2185aa8d517bae009ab54807f` |

`main` was not checked out, modified, reset, merged into, or pushed. The
branch was created from the exact base and both branch commits descend
from it.

**`origin/main` has advanced beyond local `main` through other authorized
work, and is reported rather than altered.** Local `main`
(`0f79617`, "docs: Arm H decisive merge verification report") is a strict
ancestor of `origin/main` (`a0e9d11b`, "reports: record P2-PHASE-01
integration stops and clarifications"); `git merge-base --is-ancestor`
exits 0 in that direction and there are no commits on local `main` that
are absent from `origin/main`. The 89 intervening commits are the
P2-CHANNEL-FREEZE-01 Phase-A, governance-tools, rules 8–12,
P2-LATTICE-ONTOLOGY-01, Arm-P and P2-PHASE-01 work. The task base is
`origin/main`, i.e. the current remote tip, not the stale local
`main` — which is what the specification's evidence base names. Nothing
here required action and nothing was taken.

---

## 7. Superseded and superseding role text, side by side

### 7.1 `AGENTS.md`

**Superseded** (`a0e9d11b:AGENTS.md`, the whole of `## Role separation`
at the base revision):

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

**Superseding** (commit 2, the whole `## Role separation` body above its
subsections — verified to be a verbatim substring of the committed file):

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
and the `DECISION_LOG.md` entry. The three superseded phrases appear zero
times in the operative region.

**The substantive change** is not cosmetic. The base text assigned three
named agents to three fixed jobs — ChatGPT conceptual, Codex
repository, Claude review. The superseding text names four functions and
attaches a *current* assignment to each, so that an exchange of the
Researcher and Reviewer functions is a change of assignment rather than a
contradiction of the document. It also adds two things the base text did
not contain: the Reviewer's agreement as a precondition on normative task
instructions, and an explicit ceiling on minor corrections.

### 7.2 `reviews/README.md`

**Superseded** (`a0e9d11b:reviews/README.md`, in full):

```text
# Reviews

Store independent review records here. ChatGPT material may document planning
and interpretation but does not certify numerical results. Claude reviews
derivations and results, identifies overclaims, and records a gate verdict.
Final acceptance or rejection belongs to the Principal Investigator.
```

**Superseding** (commit 2): the by-author layout is retained and
described; a `Function:` header is required on every review, Researcher
record, Executor record, or PI authorization **created or substantively
amended after** the 2026-08-06 decision; and existing records are
declared to remain valid historical evidence, not retrospectively
non-conforming. The superseded paragraph is preserved as a labelled
non-operative blockquote under
`## Historical role assignment — superseded 2026-08-06`.

**This report carries `Function: Executor`** in its header, as the first
record created under the new requirement.

---

## 8. Provenance of the capability statements

The specification requires this report to distinguish what the task
verified from what it merely recorded. The dual-executor section asserts
things this task did not re-test, and must not read as though it did.

| Statement as recorded in `AGENTS.md` | Classification |
| --- | --- |
| Two executors are in use, selected per task by the PI according to quota and capability | **PI-supplied fact** (a decision, recorded on PI instruction) |
| They are not interchangeable, and the difference is material rather than administrative | **PI-supplied characterisation** |
| Codex runs on the PI's workstation | **PI-supplied fact.** Not observable from this container. |
| The workstation has a GPU (RTX 4070 Ti) | **PI-supplied fact.** Not observable from this container; no GPU inventory was taken. |
| The workstation has no short process-termination limit | **PI-supplied fact**, not re-verified here. |
| Claude Code runs in a sandboxed container | **Verified directly**, trivially: this task ran there. |
| Claude Code reaches genuine exit 0 on the validator suite | **Verified directly, at this revision, in this session** — §5 above: five individual runs, five exit-0 statuses, 49 tests collected and passed. This is a current observation at commit 2, not a permanent guarantee. |
| …"which the workstation currently cannot" | **PI-supplied observation about the other host.** Not re-verified here, and not verifiable from here. |
| Claude Code is ephemeral and starts from a stale tree each session | **Current environment observation, verified indirectly this session:** local `main` was `0f79617` while `origin/main` was `a0e9d11b`, 89 commits ahead (§6). That is the stale-tree behaviour, observed once, not a guarantee. |
| Claude Code "has been observed to lose a long-running job" | **Prior-session observation, recorded, not reproduced here.** No long-running job was launched by this task. |
| Short deterministic verification, preparation and audit belong here; decisive multi-hour runs do not | **PI allocation decision**, recorded. Not a measurement. |

**Nothing in the dual-executor section was established by this task
except the two rows marked "verified directly", and both of those are
observations at one revision in one session.** The `AGENTS.md` text
carries this limit in its own words: the capability statements are
"PI-supplied operational findings and current observations", "not
re-verified by this task and are not permanent capability guarantees".

---

## 9. Does recording this model expose any further conflict?

**Yes. Two further conflicts of the same kind remain in the repository,
and a third, weaker one.** None is inside the seven executor-writable
paths, so all three are reported and none is touched. The conflict this
task resolves was found by a reviewer reading the repository; these were
found by the same method extended to the rest of the tree.

```text
=== further-conflict survey: committed artifacts that name fixed agents in a role capacity ===

$ git grep -n -i -E "Claude is the|ChatGPT (handles|material)|Codex handles|independent reviewer|the reviewer is|reviewer/discriminator" a021eed -- ":!specs/" ":!reports/" ":!reviews/"
a021eed:AGENTS.md:101:- ChatGPT handles conceptual discussion, physical interpretation, analytic
a021eed:AGENTS.md:104:- Codex handles repository maintenance, implementation, tests, regression
a021eed:AGENTS.md:107:- Claude is the independent reviewer/discriminator, issues gate verdicts,
a021eed:PROGRESS.md:25:The normalization/gap/circularity follow-up has **one independent reviewer
a021eed:README.md:36:Claude acts as an independent reviewer and discriminator: reviewing derivations

$ CONVENTIONS.md rule 8 as landed:
RULE 8 HEADING NOT FOUND

$ docs/ inventory at commit 2:
docs/BRANCHING_POLICY.md
docs/RESEARCH_WORKFLOW.md
docs/RESULT_SCHEMA.md
docs/local/README.md
docs/local/execution_environment.md

$ docs/ role/agent mentions:
a021eed:docs/BRANCHING_POLICY.md:22:- Paper branches may update `.tex` only after reviewer acceptance.
a021eed:docs/RESEARCH_WORKFLOW.md:11:### ChatGPT
a021eed:docs/RESEARCH_WORKFLOW.md:13:ChatGPT supports conceptual discussion, physical interpretation, analytic
a021eed:docs/RESEARCH_WORKFLOW.md:15:and identification of assumptions and competing interpretations. ChatGPT does
a021eed:docs/RESEARCH_WORKFLOW.md:18:### Codex
a021eed:docs/RESEARCH_WORKFLOW.md:20:Codex maintains the repository, implements symbolic and numerical work, creates
a021eed:docs/RESEARCH_WORKFLOW.md:22:enforces branch and commit discipline. Codex must not promote a result into a
a021eed:docs/RESEARCH_WORKFLOW.md:25:### Claude
a021eed:docs/RESEARCH_WORKFLOW.md:27:Claude independently reviews and discriminates among derivations and results,
a021eed:docs/RESEARCH_WORKFLOW.md:47:8. Submit the derivation and result record for independent Claude review.
a021eed:docs/RESEARCH_WORKFLOW.md:51:    only after reviewer acceptance and the Principal Investigator's decision.
a021eed:docs/local/execution_environment.md:7:| Execution identity | `zeta-3070\\codexsandboxoffline` |
```

### 9.1 `docs/RESEARCH_WORKFLOW.md` — an unreconciled duplicate of the superseded model

`docs/RESEARCH_WORKFLOW.md` lines 11–27 contain a full fixed-agent role
section — `### ChatGPT`, `### Codex`, `### Claude` — which is the same
model, in the same terms, as the `AGENTS.md` text this task supersedes.
Line 47 adds "Submit the derivation and result record for independent
Claude review", making the fixed assignment operative in a procedure
rather than only descriptive.

**This is the more serious of the two.** After commit 2, `AGENTS.md` says
roles are functions with current assignments and that rule 8 governs,
while `docs/RESEARCH_WORKFLOW.md` still says Claude is the reviewer. A
reader who consults `docs/` and not `AGENTS.md` gets the superseded
model with nothing marking it as superseded — which is the precise defect
this task was run to remove, displaced one directory. Recording the
function-based model does not create this conflict, but it does make it
newly visible and newly load-bearing.

### 9.2 `README.md:36` — the same statement in the repository front door

`README.md:36` reads "Claude acts as an independent reviewer and
discriminator: reviewing derivations…". Same defect, higher visibility,
smaller extent — one sentence rather than a section.

### 9.3 `docs/local/execution_environment.md` — a single declared execution identity

The file declares `Execution identity | zeta-3070\codexsandboxoffline`,
i.e. one Windows workstation identity. The dual-executor arrangement
recorded by this task has **two** execution hosts with materially
different capabilities. The document does not contemplate a second host,
so a specification whose acceptance criteria depend on the declared
environment is now ambiguous as to which host it describes. This is
adjacent to the already-open PI item about the Windows-versus-Linux host
declaration and is not resolved here.

### 9.4 `CONVENTIONS.md` — no conflict found

Rule 8 (`### 8. Responsibility separation`) is consistent with the model
recorded here and is the reason the reconciliation subsection can point
to it rather than to a new rule. The sentences relied on are:

```text
Two distinct review functions may be exercised by two independent
reviewers … These are functions, not fixed assignments to a
particular agent.

These are FUNCTIONS, not fixed agents: specification/theory,
execution/experimentation, and independent review/verification. **PI
authorization sits above all three** — adoption, exceptions, and final
decisions are the PI's, and no rule in this section transfers that
authority.
```

The `AGENTS.md` reconciliation subsection asserts only that where the
older role text and rule 8 conflicted, rule 8 governs, and states
explicitly that rule 8 is not modified, renumbered, or reworded. The
blob comparison in §3 confirms the file is untouched.

`docs/BRANCHING_POLICY.md:22` and `docs/RESEARCH_WORKFLOW.md:51` use
"reviewer acceptance" without naming an agent; these are consistent with
the function-based model and are not conflicts.

### 9.5 Recommended disposition, not taken here

Extending the same historical/superseded treatment to
`docs/RESEARCH_WORKFLOW.md` and `README.md:36` would be a small
docs-only task in the same shape as this one. **It is out of scope: those
paths are not in the seven executor-writable paths, and the choice
belongs to the PI, not to me.**

---

## 10. Authorization provenance of this specification

- The specification was issued to the Executor by the PI in this session
  as a complete task specification, headed "Task specification — adopt
  the function-based role model and record the dual-executor
  arrangement", classified MATERIAL, with an evidence base of
  `a0e9d11b7281f0c2185aa8d517bae009ab54807f`.
- It states its own authority basis: it "records decisions the PI has
  already made", and A0 reproduces the governing PI decision of
  2026-08-06 that approved specifications are committed while
  Researcher–Reviewer review exchanges are not.
- It is committed in full as commit 1 at
  `specs/2026-08-06T0456Z_role-model-and-executors.md`, blob SHA-256
  `f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd`,
  so every claim in this report has a corresponding instruction in the
  repository.
- **No mid-task amendment was issued.** No instruction changed after the
  specification was received, so there is nothing to reproduce verbatim
  under that heading. Had one been issued it would appear here in full.
- I hold no separate reviewer agreement artifact for this specification
  and did not verify one. Under the model being recorded, that agreement
  is a precondition on issuing the specification and sits with the PI and
  Reviewer; it is not an Executor-verifiable fact from inside the
  repository at this revision. **Recorded as a limit on this report, not
  as a defect.**

---

## 11. Stops and clarifications

**No stop occurred.** No command that reads or alters repository state
produced an unexpected result, and no criterion was unsatisfiable. The
items below are recorded for completeness; each categorised item carries
exactly one primary category. §11.6 is a clarification with no stop and
no category.

### 11.1 `OBSERVATION_METHOD_ERROR` — my own drafting and tooling, corrected before commit 2

Three defects, all mine, all in uncommitted working-tree content or in
scratch tooling, all corrected before commit 2 existed. Nothing was
rewritten: no commit was amended, because none of the three survived
into a commit.

1. **Line wrapping broke a required literal.** My first draft of
   `AGENTS.md` wrapped the minor-corrections sentence as
   `…does not by itself expand the Executor's authorized` / `scope.**`,
   so the A1 fixed string
   `does not by itself expand the Executor's authorized scope` was absent
   (`op=0 hist=0 FAIL`) while the sentence read correctly to a human. I
   reflowed the line; the literal is now contiguous and at count 1.
   **A criterion written as a contiguous fixed string is not satisfied by
   a semantically identical wrapped one, and that is the criterion
   working as intended** — it caught a real difference between what the
   file said and what the specification required it to say.
2. **I had dropped four words from a supplied blockquote.** My draft of
   the dual-executor paragraph read "they are **not permanent capability
   guarantees**", where §1 of the specification supplies "they are
   **not re-verified by this task and are not permanent capability
   guarantees**". A3's verifier does not check that phrase, so this would
   have passed unnoticed. I restored the supplied wording verbatim rather
   than keep my shorter version. See §11.3 for the one reservation I have
   about the restored phrase — which I recorded rather than acted on.
3. **My scratch verifier reported a false FAIL.** Run without an explicit
   head revision it read file *text* from the working tree but compared
   `reviews/` *blobs* between the base tree and commit 1's tree, where
   `reviews/README.md` is still unmodified — so it reported "changed
   pre-existing reviews/ paths = []" as a failure of its own
   expectation. The repository was correct; the tool was wrong. I
   replaced the tree-vs-tree comparison with a worktree-aware
   `git diff --name-status` and re-ran. The authoritative run in §3 is
   against commit 2, where the question does not arise.
   **Stop-on-unexpected-result applies to commands that read or alter
   repository state, not to my own scratch tooling; I corrected the
   tooling and am saying so.**

### 11.2 `ENVIRONMENT` — nothing missing, nothing installed

Rule 13's diagnostic order was not needed: every tool required by the
task was present. Python 3.11.15, pytest 9.1.1, `git`, and
`scripts/governance_tools` all resolved on first use. **Nothing was
installed.** All five validators reached genuine exit 0, so the
`NOT COMPLETED — DECLARED HOST LIMITATION` outcome the specification
provides for Codex did not arise here.

For the record, and consistent with §8: the ~120-second harness
termination declared for the workstation is **absent on this host**, and
no long-running job was launched by this task, so this session neither
reproduces nor contradicts the "lost a long-running job" observation.

### 11.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — "by this task", in a standing document

The supplied dual-executor blockquote contains "not re-verified by this
task". Transcribed into `AGENTS.md`, which is a standing document rather
than a task artifact, "this task" has no antecedent for a future reader:
it means the 2026-08-06 role-model task, but nothing in the sentence says
so. The surrounding text does anchor it — the section opens with "As
recorded by PI decision on 2026-08-06" — so the phrase is recoverable,
not wrong.

**I transcribed it verbatim and did not resolve it.** Rewriting it as
"not re-verified by the recording task" or similar would have been my
wording substituted for the PI's in the operative text of a governance
document, which §3 of the specification prohibits: "Do not decide
anything." **This is flagged for the Reviewer, not fixed.** It is a
wording matter with no effect on any acceptance criterion.

### 11.4 Secondary findings, classified independently

The three conflicts in §9 were discovered while checking whether
recording this model exposes further conflict — a report-contract
requirement, not a stop. Classified independently:

| Finding | Category |
| --- | --- |
| `docs/RESEARCH_WORKFLOW.md` §§ ChatGPT/Codex/Claude and line 47 restate the superseded fixed-agent model, unmarked | `REPOSITORY_DEFECT` |
| `README.md:36` restates it in one sentence | `REPOSITORY_DEFECT` |
| `docs/local/execution_environment.md` declares one execution identity where two hosts are now recorded | `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` |

None was acted on. All three are outside the seven executor-writable
paths.

### 11.5 Commit-metadata trailers on commit 1 — clarification, no category

Commit 1 carries two trailer lines added by the commit tooling
(`Co-Authored-By:` and `Claude-Session:`), which commit 2 does not,
because commit 2 was created with `git commit -F -`. The trailers embed a
session URL and a tool version string in a permanent repository record.
**Disclosed rather than repaired:** removing them requires rewriting
history, which §3 of the specification prohibits, and their content
affects no acceptance criterion, no scientific claim, and no digest. §1
reproduces the authored subject line and describes the trailers rather
than reprinting them. Commit 3 uses the same trailer-free method as
commit 2.

### 11.6 Branch naming

`docs/BRANCHING_POLICY.md` enumerates `gate/`, `paper/`, `review/`,
`fix/`, `archive/`. The specification directs
`review/role-model-and-executors`, which is inside the enumerated set, so
I found no conflict to stop on. The policy-versus-practice contradiction
the specification names as an open PI item was neither used nor resolved.

---

## 12. Ambiguous, unsatisfiable, or what I would have specified differently

- **Nothing was unsatisfiable.** Every criterion A0–A10 was checkable as
  written, and the A1 wrapping failure in §11.1 is evidence the fixed-string
  form has real discriminating power rather than being ceremony.
- **A2's `Function:` literal is weaker than the requirement it guards.**
  The criterion asks for `Function:` present exactly once in
  `reviews/README.md`. The requirement is that *records* carry the header.
  A `README.md` that documents the field satisfies the check; so would a
  `README.md` that merely mentioned the word once in prose. The check
  cannot distinguish them, and it cannot see whether any actual record
  complies. I satisfied it by writing the field as an indented literal
  block, and separately by putting `Function: Executor` in this report's
  header — but that second act is discretionary, not required by any
  criterion. **A future specification could require the header on the
  task's own report and check it there**, which would make the rule
  self-demonstrating.
- **`Function:` at exactly-once is fragile against the rule's own future.**
  Any later expansion of `reviews/README.md` that shows a second example
  of the field will break A2 while improving the document. The count is
  the right shape for a phrase that must not be duplicated; it is the
  wrong shape for a field name that a reader may need illustrated twice.
- **A3 checks names, not the capability difference it asks for.** The
  criterion says "The capability difference must be stated, not only the
  names", but its verifier is five fixed strings, four of which are
  names. `RTX 4070 Ti` and `sandboxed` are the only two that gesture at
  capability, and neither would fail if the section said the two hosts
  were interchangeable. The substantive requirement here rests on review,
  not on the check — which the specification's own framing acknowledges
  by stating it in prose. I recorded the difference in the terms §1
  supplied.
- **The four supplied blockquotes in §1 have no byte-for-byte criterion,
  unlike A1a and A6.** A1a says "supplied verbatim … verify it
  byte-for-byte"; A6 says "verify by diff that each file's change is
  exactly this insertion". §1's role-model and dual-executor blockquotes
  say only "the role model to record", and the A1/A3 verifiers sample
  them with a handful of literals. That gap is what let my
  four-word omission (§11.1, item 2) pass every mechanical check. I
  caught it by reading the specification against the file, not by
  running anything. **If the §1 blockquotes are intended as frozen
  supplied content, they should carry an A1a-style byte-for-byte
  criterion**; if they are intended as content to be rendered into
  house style, then A1a and A6's stricter treatment should say why they
  differ. As written the three are inconsistent, and I resolved the
  inconsistency in the direction of verbatim transcription because §3
  forbids deciding.
- **The report cannot verify the Reviewer agreement that the model it
  records makes a precondition.** §10 records this. It is inherent to
  the arrangement rather than a defect in the specification: the
  Executor cannot see the review exchange, and by the PI decision in A0
  that exchange is deliberately not committed. The consequence worth
  stating is that the Reviewer's precondition is enforceable by the PI
  and Reviewer only, and no Executor report can attest to it.
- **A7's enumeration is a whitelist of prefixes, not of the tree.** It
  covers `tests/`, `scripts/`, `derivations/`, `results/`, `GATES.md`,
  `CONVENTIONS.md`, `pyproject.toml` — 144 blobs. It does not cover
  `docs/`, `README.md`, `CLAIMS.md`, `MIGRATION.md`, `reports/`, or the
  `.tex` sources. A8's `mode: exact` manifest does close that gap, since
  any operation outside the six declared records fails it, so the
  combination is sound. I mention it because A7 read alone looks like a
  whole-tree protection and is not.
