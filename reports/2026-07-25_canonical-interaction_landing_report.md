# Canonical-interaction landing report

**Date:** 2026-07-25  
**Branch:** `docs/canonical-interaction`

## Part 0

- Executor-local checkout configuration was verified as `core.autocrlf=false`
  and `core.eol=lf`; neither setting is a repository change.
- `origin/main` and the initial local `HEAD` both resolved to
  `48b85d186b8fac54ed9d78eb3575990d28da486a`.
- The working tree was clean before branching from `main`.
- The unrelated `gate/p2-channel-freeze` branch was not checked out, edited,
  merged, or otherwise touched.

## Evidence outcome

All eight required rows passed.  The complete clean-clone evidence table is
`reports/2026-07-25_canonical-interaction_evidence.md`:

1. Paper-3's starting interaction matches the generator-sum form at its pinned
   `N=3` specialization.
2. Generator normalizations match.
3. The pinned Paper-3 derivation gives `G_omega = -G/N`.
4. The full `P3-C-001` registry entry records status `VERIFIED`.
5. The Paper-3 clean-clone suite exited zero with the registry-matching 12/12
   result; its captured-output digest is recorded in the evidence table.
6. The metric, Euclidean Fierz-Clifford, `i gamma_5`, and sign conventions are
   compatible as tabulated in the evidence report.
7. The specified Paper-3 commit exists and is readable as a commit object.
8. Both clean clones were clean at the evidence-stage checks; this branch is
   checked clean again after the final report commit before push.

## Landing integrity

- Supplied input SHA-256 before use:
  `b9d62bb26f68b3c07b06ddab78aca7400730c9e33a3b8c6da308fe1b57285929`.
- The byte copy before substitutions matched that input digest.
- Landed file: `derivations/CANONICAL_INTERACTION.md`.
- Final landed-file SHA-256:
  `27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`.

The supplied-versus-landed diff contains exactly the authorized changes:

1. §5's title now cites the landing evidence report.
2. §7(b) now reads `VERIFIED (landing evidence table, row 6).`
3. §7(c) now reads `VERIFIED (landing evidence table, rows 1–5).`
4. The ratification record's PI-approval placeholder is filled as `Zeta Cheng,
   PI / 2026-07-25`.

No other document text was edited.

## Tracking entry

`DECISION_LOG.md` received the repository-template entry
`P2-ACT-CANONICAL-ALIGN-01`.  It registers the mandatory future action to align
the Paper-2 manuscript's interaction presentation with the ratified
generator-sum source.  No manuscript source was changed in this task.

## Verification

- `python -m pytest tests -q` (bundled runtime): `50 passed, 2 deselected`;
  exit code 0.
- The standalone `ruff` launcher was unavailable on this shell's PATH; the
  installed tool was run as `python -m ruff check .`: `All checks passed!`;
  exit code 0.

## Commit chronology through pre-report HEAD

1. `48b85d186b8fac54ed9d78eb3575990d28da486a` — verified `main` base.
2. `ab1f2b7a704f0bb9fee91459d4f2f59153a2af43` — eight-row evidence report.
3. `a86dfe616c4deb898abf4ff7b654f887970ce85e` — ratified canonical interaction
   document.
4. `8f6571b4be294796a092a04535e5793126c8f776` — registered manuscript-alignment
   tracking entry.

The report intentionally omits its own commit SHA and post-push remote output.
