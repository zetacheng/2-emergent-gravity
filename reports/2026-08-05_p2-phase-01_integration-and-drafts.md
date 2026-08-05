# `P2-PHASE-01` scalar-study integration and prerequisite drafts

## Scope and status

This record covers the integration of the reviewed exploratory scalar study,
the two prerequisite drafts, and the registry record that both drafts are **not
adopted** and remain **unsatisfied**. `P2-PHASE-01` remains `PROPOSED`. No
admissibility verdict, phase preference, or gate result is recorded here.

## Commit sequence

1. `a3fc1532df7903b32bb33bd815f3b567dbc7d13d` — explicit no-fast-forward
   merge of reviewed `explore/p2-phase-01-scalar` at
   `a2ed2af813a4c33c2b56ea98d8706f07ef375c10`.
2. `7a967c1902563506cd19eef75826a14f1fb52788` — the two prerequisite drafts.
3. `93b010a9790b22359cc00733e8d1c33ca31834b2` — initial registry record.
4. `355834e2414820e23b8e0ea28bcbed0468bd0dba` — correction of the two
   committed-content digests in `GATES.md`.

The recorded draft digests are raw SHA-256 values of the committed Git blob
bytes: `d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4`
for `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`, and
`a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73` for
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.

## Stops and clarifications

### 1. Merge guard read from the wrong worktree

**Where:** Stage 1, before A1.

**Exact output:**

```text
Get-Content : Cannot find path
'C:\Users\User\Phy_Projects\Paper 2\scripts\governance_tools\README.md'
because it does not exist.
```

**Stop correctness:** Correct. The required guard could not be run from the
worktree that was inspected.

**Category:** **observation-method error.** The active main worktree was on a
different run branch, not the pinned evidence-base revision; the tools exist
at both `86bb3942…` and `a2ed2af…`.

**Clarification/amendment:** Create the dedicated integration worktree at
`86bb3942e6a606133167ba0a4fe8dd858e62990b` first and run the tools from that
worktree; report the worktree used for each invocation.

### 2. Draft-digest mismatch

**Where:** Stage 4, A4a committed-content digest verification.

**Exact output:**

```text
Committed-state digests recorded in GATES.md
parameter-domain draft:     27936642a2b2fff7a2845a492c989cf2a3a3b092a6a9d9edc32d8ddefdf6aff8
admissibility-contract:     057932b0f9ed1ea115b189b614702d469122fbb25aea9f8db6d9288042e0b8d6

Final worktree file hashes observed
parameter-domain draft:     D8E154690E0B3D8131260A9ED0CE0EF804DD5652D21C022C6B29677B90D3EBA4
admissibility-contract:     A3EC0CB6F7968CF92528E2197F34AEDD86882EED08BFC58410142FDB875A9E73
```

**Stop correctness:** Correct. A4a required digest provenance to be checked
before pushing.

**Category:** **observation-method error, which produced a genuine registry
error now corrected in commit 4.** The initial hash command piped Git output
through a PowerShell text pipeline, altering the byte stream before hashing.
The resulting wrong values were then recorded in `GATES.md`; raw Git-blob
hashing established the correct values.

**Clarification/amendment:** Commit 4 changed only the two digest literals to
`d8e154…e3eba4` and `a3ec0c…a9e73`, using raw Git blob bytes written to
temporary files and hashed without a text-processing pipeline.

### 3. Scratch content-checker manifest used incomplete heading literals

**Where:** A6 rules-heading check.

**Exact output:**

```text
"count": 0,
"kind": "heading",
"status": "FAIL",
"value": "### 1."
```

The same result occurred for `### 2.` through `### 13.`, followed by:

```text
"kind": "heading_order",
"positions": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
"status": "FAIL"
```

**Stop correctness:** Correct. The declared content-checker invocation
reported a failure and was not silently ignored.

**Category:** **observation-method error.** The scratch manifest used exact
heading strings such as `### 1.`, whereas repository headings carry titles.
No repository finding follows.

**Clarification/amendment:** Use the content checker's `heading_prefixes`
semantics for the numbered headings; no repository content was changed for
this item.

## Outstanding work deliberately not decided

The prerequisite drafts retain their listed OPEN questions. In particular,
they do not decide the physical interpretation of negative-mass roots, whether
`Mhat = 1` is a bound, any P/V/A/T HS setup, or an admissibility rule.
