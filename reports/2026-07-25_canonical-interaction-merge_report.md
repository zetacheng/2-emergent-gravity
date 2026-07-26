# Canonical-interaction merge verification report

**Date:** 2026-07-25  
**Merged branch:** `docs/canonical-interaction`

## Guard 0 — executor-local EOL configuration

The following executor-local values were printed after configuration:

```text
core.autocrlf: false
core.eol: lf
```

They were not committed.

## Guard 1 — reviewed remote refs and structure

After `git fetch`:

```text
origin/main: 48b85d186b8fac54ed9d78eb3575990d28da486a
origin/docs/canonical-interaction: 78872798c7f638434996f190450af3223b9cfedf
merge-base ancestry exit: 0
commit count from main base: 4
```

The diff from the verified main base to the reviewed landing tip contained
exactly these paths:

```text
DECISION_LOG.md
derivations/CANONICAL_INTERACTION.md
reports/2026-07-25_canonical-interaction_evidence.md
reports/2026-07-25_canonical-interaction_landing_report.md
```

## Guard 2 — pinned merge

`main` was first verified equal to `origin/main` at
`48b85d186b8fac54ed9d78eb3575990d28da486a`.  The reviewed landing SHA
`78872798c7f638434996f190450af3223b9cfedf` was merged with the required
no-fast-forward merge command and frozen message.

Merge commit (pre-report HEAD):
`d51fea326ceea6a3748791b3f17a8a8a1562ca89`.

## Guard 3 — post-merge verification

- The merged `HEAD` contains the reviewed landing SHA (`merge-base --is-ancestor`
  exit 0).
- `derivations/CANONICAL_INTERACTION.md` SHA-256:
  `27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`.
  The PowerShell SHA-256 facility was used because this executor shell does not
  provide a `sha256sum` launcher.
- The §5 title phrase `verified at landing; evidence` occurred once.
- `VERIFIED (landing evidence table` occurred exactly twice.
- `DECISION_LOG.md` contains the `P2-ACT-CANONICAL-ALIGN-01` tracking entry.
- `python -m pytest tests -q`: `50 passed, 2 deselected`, exit 0.
- `python -m ruff check .`: `All checks passed!`, exit 0.
- `GATES.md` is byte-identical to
  `48b85d186b8fac54ed9d78eb3575990d28da486a` (`git diff --exit-code` exit 0).
- The quarantine/P2-C9 diff scan had no hits.
- The working tree was clean before this report was created.

The `docs/canonical-interaction` landing branch must remain present.  It was
not deleted, and this report contains neither its own commit SHA nor post-push
remote output.
