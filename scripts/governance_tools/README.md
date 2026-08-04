# Governance tools

This package contains the read-only tooling required by `CONVENTIONS.md` rules
11–12. It is discoverable through the repository's existing `scripts/`
convention and this local README.

All commands emit structured JSON. Exit `0` means every evaluated governance
condition passed, `2` means a governance condition failed, and `3` means a
malformed manifest, unresolved input, or internal tool failure. A declared
`NOT_EVALUATED` condition is reported as such and does not count as a pass.

Run from the repository root:

```text
python -m scripts.governance_tools.scope_checker --manifest scope.json
python -m scripts.governance_tools.content_checker --manifest content.json
python -m scripts.governance_tools.merge_guard --config merge.json
python -m scripts.governance_tools.spec_consistency_checker --spec criteria.json
```

Scope manifests declare Git operation records, not only paths. `required` and
`optional` contain `{operation, path}` records, or `{operation, from, to}` for
renames and copies; `forbidden_operations` denies entire operation classes.
The operation vocabulary is `add`, `modify`, `delete`, `rename`, `copy`,
`type_change`, `unmerged`, and `unknown`. `exact` requires every required
record; `subset` permits a subset of declared required/optional records.

The merge guard has distinct `PRE_MERGE` and `POST_MERGE` modes. The former
checks the supplied working tree against the required
`expected_worktree_head` revision. This field has no default: callers may
declare any resolvable commit expression, including a reviewed base, a reviewed
branch head, or a named third revision. The guard resolves it before comparing
it with the worktree's `HEAD`; attachment is reported only as metadata. The
latter checks an existing merge commit. Neither mode mutates a repository.

Content literals use one of three explicit match modes: `substring`,
`line_substring`, or `exact_line`. The last is appropriate for a forbidden
fragment which is only forbidden as a complete line.

The consistency checker intentionally supports a small formal language:
`file_hash`, `changed_files`, and `prefix_hash` with an explicit line-count
boundary. It reports formal conflicts, malformed/underspecified criteria, and
ordinary state mismatches separately; it does not interpret arbitrary prose.
Conflict identities are domain-aware: a file hash is keyed by criterion kind,
resolved commit, and normalized repository-relative path; a changed-file
condition also includes its resolved base and head commits. There are no
implicit cross-domain invariants.
