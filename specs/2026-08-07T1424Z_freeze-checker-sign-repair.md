# Task specification — repair the Phase-A freeze checker's sign handling and close the mutation gap

Specification evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This repairs validation machinery. It changes no frozen data and no
scientific result.** The Phase-A freeze, its `matrix_rational`, and the
`fierz_matrix.json` companion are all untouched.

---

## 0. The three defects, and why the obvious fix is wrong

The `P2-PHASE-01` and crossing-sign tasks established these from the
repository:

**(i) The checker's sign application is inert.** At
`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py`:

    sign = parse_grassmann_sign(conventions["grassmann_crossing_sign"])
    computed_fierz = (sign * projector * crossing * embedding).T * sign

The scalar appears twice and `.T` does not touch a scalar, so the two
occurrences multiply to `sign² = +1` for either declared value.
`computed_fierz` is identical whether the freeze declares `-1` or `+1`.

**(ii) The mutation suite does not cover the field.**
`tests/test_channel_freeze_mutations.py` has no `grassmann` mutation.
Flipping the declared value would pass every existing check silently.

**(iii) `vocab_parser.py` was never pinned** in the specifications that
made substantive claims about how the field is consumed, although it
holds `parse_grassmann_sign`.

**The obvious repair — apply the sign once instead of twice — is
WRONG, and this is the central point of this task.**

Under the PI ruling of 2026-08-07, now recorded in `DECISION_LOG.md`,
**`matrix_rational` is stored UNSIGNED** and `s_G` is applied **once at
operator use**. The checker validates the stored matrix, not an operator
use. **Therefore the checker should apply the sign ZERO times.**

Applying it once would make `computed_fierz` differ from the frozen
`matrix_rational` by an overall `−1`, and `require(computed_fierz ==
frozen_fierz)` would fail — which could only be "fixed" by editing a
hash-pinned frozen artifact. **That is the trap. Do not take it.**

**Consequence for the mutation.** If the checker correctly ignores the
sign, then a mutation flipping `grassmann_crossing_sign` **must not**
make the checker fail — the checker is designed to be blind to it. So
the tenth mutation cannot live in the checker's mutation suite in the
form the other nine take.

**Where it belongs instead:** the operator-level consumer.
`scripts/p2_grassmann_crossing_sign.py`, landed at the evidence base,
verifies that the computed `s_G` equals the declared value. **That
consumer is where a flipped declaration must be caught**, and where the
new coverage goes.

**A note on the record.** The correct phrasing is that the checker does
not apply the sign **because the sign belongs to the operator layer** —
not that "the sign is irrelevant". `s_G = −1` is load-bearing: it is
what turns the matrix-level `+G/4` into the operator-level `−G/4`. Use
that phrasing in the derivation note and report.

## 1. Objective

`basis_freeze_check.py` validates the stored matrix without applying the
crossing sign, with the reason recorded in the code; a flipped
`grassmann_crossing_sign` is caught by a test at the operator layer;
`vocab_parser.py`'s role is documented; and every existing freeze
assertion still passes unchanged.

## 2. What to change, and what must not change

**Change 1 — remove the inert double application.** In
`basis_freeze_check.py`, compute the matrix without the sign factor. The
existing comment about dualising describes `.T` and stays; **add a
comment stating that the crossing sign is deliberately NOT applied here
because `matrix_rational` is stored unsigned per the 2026-08-07 ruling,
and that the sign is applied once at operator use.**

**`computed_fierz` must be unchanged by this edit**, since the two
factors already cancelled. **Demonstrate that**: report the matrix
before and after, and show they are equal entry by entry.

**Keep reading and validating the field.** `parse_grassmann_sign` still
runs, so a malformed value is still rejected. **Removing the parse would
be a regression**: well-formedness checking is the one thing the checker
legitimately does with this field.

**Change 2 — operator-layer coverage.** Add a test asserting that
`scripts/p2_grassmann_crossing_sign.py`'s comparison **fails when the
declared value is flipped**. Place it in
`tests/test_p2_grassmann_crossing_sign.py`, the existing test file for
that consumer.

**Do not add a `grassmann` entry to `MUTATIONS` in
`tests/test_channel_freeze_mutations.py`.** That list drives
`test_checker_rejects_each_frozen_data_corruption`, which asserts the
checker REJECTS each corruption. After Change 1 the checker correctly
ignores the sign, so such an entry would assert a rejection that must
not happen. **Adding it would encode the defect as a requirement.**

**Change 3 — document `vocab_parser.py`'s role** in the derivation note:
it holds `parse_grassmann_sign`, which accepts exactly `±1`, so a
garbage value is caught but a wrong value is not. **This is
documentation, not a code change.**

**What must not change:**

- `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`
- `results/P2-CHANNEL-FREEZE/fierz_matrix.json` and its `.sha256`
- `scripts/P2-CHANNEL-FREEZE/vocab_parser.py`
- the `MUTATIONS` list, and every existing test in either freeze suite
- `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`, `pyproject.toml`

## 3. Acceptance criteria

**A0 — Commit order.** Commit 1 is this specification under `specs/`.
Commit 2 is the derivation note under `derivations/`, before any code
change, per `AGENTS.md` rule 3. Commits 3+ carry the code, test and
report. **Parent 1 of any commit is whatever you are standing on; do not
specify it independently.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
    b3123855c225c6832c890c42fda6b03b4b8b81eef69a1c69ae654d7523367fdb

    scripts/P2-CHANNEL-FREEZE/vocab_parser.py
    40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606

    tests/test_channel_freeze_mutations.py
    4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0

    tests/test_channel_freeze_phase_a.py
    80ee0e834287e5f5c2185c881633e656454ff9e7935382dabc6370e16c204d3d

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

**A2 — `computed_fierz` unchanged.** Report the 5×5 matrix computed by
the pre-edit and post-edit code, and show entry-by-entry equality as
exact rationals. **If they differ, STOP** — that would mean the two
factors were not in fact cancelling and the premise of this task is
wrong.

**A3 — Sign still parsed.** `parse_grassmann_sign` is still called and a
malformed value is still rejected. Demonstrate with a malformed input.

**A4 — Operator-layer test, exercising the PRODUCTION comparison
path.**

**Two different things must not be confused here.** Under a synthetic
flipped declaration, the **production comparison** in
`scripts/p2_grassmann_crossing_sign.py` must fail or reject as expected.
**The pytest test itself must PASS**, by asserting that rejection
occurred. **Do not require the pytest invocation to exit non-zero** —
A9 requires exit 0 for this file, and a test that fails the suite to
prove a point would contradict it.

Report the production failure/rejection evidence: what the production
code did when handed the flipped value, and what the test asserted about
it. **A test asserted to catch something, without evidence that the
production path actually rejected, is not evidence.**

**How the flip is supplied is normative, because the obvious shortcuts
produce fake coverage:**

- The demonstration MUST exercise the comparison in
  `scripts/p2_grassmann_crossing_sign.py`. Supply the flipped
  declaration through a synthetic or temporary input, or through an
  existing injectable function boundary.
- **Do not edit the repository freeze, even transiently.**
- **The test must fail because the PRODUCTION code compares a computed
  `s_G = −1` against a mutated declared `+1`** — not because the test
  itself asserts `−1 != +1`. A test that re-implements the comparison
  and then checks its own re-implementation covers nothing.

State which mechanism you used and why it exercises the production
path.

**A5 — `MUTATIONS` untouched.** `tests/test_channel_freeze_mutations.py`
blob-identical to the evidence base. **This is a criterion, not an
oversight**: the reason is in §2.

**A6 — Freeze data untouched.** The freeze document, `fierz_matrix.json`
and its sidecar, and `vocab_parser.py` blob-identical to the evidence
base. Read from the objects.

**A7 — Every existing assertion still passes.** Both freeze suites pass
unchanged: `tests/test_channel_freeze_phase_a.py` and
`tests/test_channel_freeze_mutations.py`.

**A8 — Scope.** Exactly these paths; the `{HHMM}Z` token is fixed once
by commit 1 and reused:

    add:
      specs/2026-08-07T{HHMM}Z_freeze-checker-sign-repair.md
      derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md
      reports/2026-08-07T{HHMM}Z_freeze-checker-sign-repair.md
    modify:
      scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
      tests/test_p2_grassmann_crossing_sign.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 3 additions and 2 modifications.** Report the
template, the resolved manifest, its SHA-256, and the checker JSON
including `observed_operations`.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`,
`tests/test_p2_phase01_fierz_and_depths.py`,
`tests/test_p2_grassmann_crossing_sign.py`,
`tests/test_channel_freeze_phase_a.py`,
`tests/test_channel_freeze_mutations.py`. **A9-pre** at the pre-report
head goes in the report; **A9-final** at the pushed head is post-report
evidence and carries the verdict.

**A10 — Lint clean, using the repository's configured tool.**
`pyproject.toml` configures `ruff` (`[tool.ruff]`, `[tool.ruff.lint]`).
Run `ruff check` on the files you author or edit, with the repository's
configuration, and report the exact command and its output.

**Pre-existing diagnostics elsewhere are not yours to fix** — in
particular the 8 known diagnostics on the hash-pinned
`scripts/euclidean_reconstruction.py`. If `ruff` is unavailable, that is
an `ENVIRONMENT` finding: report it and do not install anything.

**A11 — Branch only.** `refs/remotes/origin/main` and remote
`refs/heads/main` both `236f71c6…`; create the branch from that commit;
none of local `main`, `origin/main` or remote `main` is moved. **Local
`main` is stale by design — do not repair it.** Report all three. Push
the task branch only. **Delete no branch.**

## 4. Evidence layering

**Committed report:** A1–A7, A9-pre, A10, the earlier commit SHAs and
messages, the pre-report head, the intended report commit message and
its authoring-time trailer suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A9-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the five paths of A8 only.
- **Do not apply the crossing sign once in the checker.** Zero is the
  correct count; §0 explains why, and applying it once would force an
  edit to a hash-pinned frozen artifact.
- **Do not edit any frozen artifact**, the `MUTATIONS` list, or any
  existing test.
- **Do not write that "the sign is irrelevant".** It is irrelevant to
  what the checker validates; it is load-bearing at operator use.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/freeze-checker-sign-repair`. This prefix is
  within `docs/BRANCHING_POLICY.md` as written.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A10, scope-checker JSON verbatim including
  `observed_operations`;
- the pre-edit and post-edit `computed_fierz`, with the equality proof;
- **the PRODUCTION comparison shown REJECTING the flipped declaration,
  with the pytest test itself PASSING** by asserting that rejection —
  see A4; these are two different outcomes and the report must not
  conflate them;
- **why the sign is applied zero times rather than once**, in your own
  words — if that reasoning is wrong, this task's premise is wrong and
  we need to know;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
