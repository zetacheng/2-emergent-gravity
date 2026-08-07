# Execution report — repair the Phase-A freeze checker's sign handling

Authority: `specs/2026-08-07T1424Z_freeze-checker-sign-repair.md`
Evidence base: `236f71c69ef9abec33ef0d808724ce80af037710`
Branch: `fix/freeze-checker-sign-repair`
Classification: MATERIAL. Branch only; no merge, no PR.

**No frozen data and no scientific result changed.** The Phase-A freeze,
`matrix_rational`, `fierz_matrix.json` and its sidecar, `vocab_parser.py`
and the freeze mutation suite are blob-identical to the evidence base.

This report is written at head `f8873aa02c22f7110c957bfbc5b9d5120d7e80fb`
and does not contain its own commit SHA, the final branch head, or any
evidence whose production depends on the report commit. Those are
returned separately as post-report evidence.

---

## 1. Why the sign is applied zero times rather than once — in my own words

The specification told me the answer; the reasoning below is mine, so
that if it is wrong the premise can be rejected rather than inherited.

`basis_freeze_check.py` exists to answer one question: **are the numbers
tabulated in `matrix_rational` the right numbers?** It answers it by
reconstruction — it builds the Dirac/internal exchange matrix from the
frozen basis elements, the frozen trace and generator normalisations,
and the frozen crossing permutation `(α,β,γ,δ) → (α,δ,γ,β)`, and asserts
the reconstruction equals the stored table.

The Grassmann crossing sign is not an input to that reconstruction. It
is not a property of the Dirac algebra or of the internal generators at
all. It is the **parity of a fermionic reordering**: when the two `psi`
legs of a four-fermion monomial are exchanged, the anticommuting fields
must be permuted past one another, and that permutation is odd, giving
`s_G = −1`. Nothing about which 5×5 rational numbers the exchange matrix
contains depends on it. It is a factor that appears when you go **from
the matrix to the operator**, one layer below this checker.

The 2026-08-07 ruling states where that factor lives:

    K_exch = s_G · M · K_direct ,     s_G = −1

`M` is what this checker validates. `s_G` multiplies `M` at the point of
operator use, exactly once. So the number of times this checker should
apply it is **zero** — not because the sign does not matter, but because
this checker is not the place where it matters.

The count of one is not merely suboptimal; it is unreachable without
corrupting data. Applying `s_G` once would make `computed_fierz` differ
from the stored `matrix_rational` by an overall `−1`; the existing
`require(computed_fierz == frozen_fierz)` would fail; and the only way to
make it pass again would be to negate all 25 entries of a hash-pinned
frozen artifact. That inverts the relationship between validator and
data: the checker would be forcing the freeze to change so that the
checker's new arithmetic could be right. I take that as decisive, and I
would take it as decisive even without the ruling.

**What I am not saying.** I am not saying the sign is irrelevant. `s_G`
is what turns the matrix-level induced coefficients of `P2-PHASE-01`,
`V: +G/4` and `A: +G/4`, into the operator-level `V: −G/4` and
`A: −G/4`. It is load-bearing. The accurate statement is: *the crossing
sign is irrelevant to what `basis_freeze_check.py` validates, because
that checker validates the unsigned stored matrix; it is load-bearing at
operator use.*

**One consequence I want on the record.** Because the checker is
correctly blind to the field, "the checker does not reject a flipped
declaration" is not a defect to be fixed in the checker. The defect was
that the code *looked* as though it were validating the field while
provably doing nothing with it. The repair removes the appearance and
records the reason; it does not add validation there, because validation
there would be wrong.

## 2. A1 — Pinned inputs

Read from the git objects at the evidence base, not from a worktree.

    $ for p in <the six paths>; do git cat-file blob 236f71c6…:$p | sha256sum; done

    scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
      b3123855c225c6832c890c42fda6b03b4b8b81eef69a1c69ae654d7523367fdb   MATCH
    scripts/P2-CHANNEL-FREEZE/vocab_parser.py
      40c566632272fde76c053b0a42d5fc83054cfc85a3e23ab79aa5f9e1719c5606   MATCH
    tests/test_channel_freeze_mutations.py
      4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0   MATCH
    tests/test_channel_freeze_phase_a.py
      80ee0e834287e5f5c2185c881633e656454ff9e7935382dabc6370e16c204d3d   MATCH
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9   MATCH

All six matched. No STOP. The freeze declares
`grassmann_crossing_sign: "-1"`.

## 3. The edit

    $ git diff --src-prefix=base/ --dst-prefix=head/ -- scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
    @@ -456,10 +456,17 @@ def verify(
         projector = pair_gram.inv() * embedding.T
         require(projector * embedding == sp.eye(5), "pair-space aggregation mismatch")
         crossing = _crossing_pair_map()
    -    sign = parse_grassmann_sign(conventions["grassmann_crossing_sign"])
    +    # The declared crossing sign is parsed so a malformed value is still
    +    # rejected, but it is deliberately NOT applied to the reconstruction:
    +    # per the 2026-08-07 ruling `matrix_rational` is stored unsigned, and
    +    # s_G is applied exactly once at operator use, downstream of what this
    +    # checker validates.  Applying it here would put the reconstruction an
    +    # overall -1 away from the frozen table.  It was previously applied
    +    # twice, which cancelled to the identity for either declared value.
    +    parse_grassmann_sign(conventions["grassmann_crossing_sign"])
         # The frozen matrix is a coefficient-row action; dualising the computed
         # pair-space column action supplies its exact, typed orientation.
    -    computed_fierz = (sign * projector * crossing * embedding).T * sign
    +    computed_fierz = (projector * crossing * embedding).T
         frozen_fierz = _matrix_from_strings(c_block["matrix_rational"])
         require(computed_fierz == frozen_fierz, "computed Fierz matrix mismatch")

The dualising comment is retained unchanged, as specified. The
`parse_grassmann_sign` call is retained; its return value is no longer
bound, because it is no longer used.

## 4. A2 — `computed_fierz` unchanged, entry by entry

Both expression forms were evaluated side by side in one process,
rebuilding `projector`, `crossing` and `embedding` with the checker's own
helpers (`blocks`, `parse_metric`, `gamma_factory`,
`expand_basis_expression`, `_family_embedding`, `_crossing_pair_map`),
so the two forms differ only in the sign factors under test.

    declared grassmann_crossing_sign in the freeze : '-1'
    parse_grassmann_sign(declared)                 : -1

    --- PRE-EDIT   computed_fierz = (sign*projector*crossing*embedding).T * sign ---
       [  1/4    1/4    1/4    1/4    1/4]
       [  1/4    1/4   -1/4   -1/4    1/4]
       [    1     -1   -1/2    1/2      0]
       [    1     -1    1/2   -1/2      0]
       [  3/2    3/2      0      0   -1/2]

    --- POST-EDIT  computed_fierz = (projector*crossing*embedding).T ---
       [  1/4    1/4    1/4    1/4    1/4]
       [  1/4    1/4   -1/4   -1/4    1/4]
       [    1     -1   -1/2    1/2      0]
       [    1     -1    1/2   -1/2      0]
       [  3/2    3/2      0      0   -1/2]

    --- FROZEN     matrix_rational ---
       [  1/4    1/4    1/4    1/4    1/4]
       [  1/4    1/4   -1/4   -1/4    1/4]
       [    1     -1   -1/2    1/2      0]
       [    1     -1    1/2   -1/2      0]
       [  3/2    3/2      0      0   -1/2]

    --- entry-by-entry equality, all 25 entries ---
      (a,b)    pre   post  pre==post  ==frozen
      (0,0)    1/4    1/4       True      True
      (0,1)    1/4    1/4       True      True
      (0,2)    1/4    1/4       True      True
      (0,3)    1/4    1/4       True      True
      (0,4)    1/4    1/4       True      True
      (1,0)    1/4    1/4       True      True
      (1,1)    1/4    1/4       True      True
      (1,2)   -1/4   -1/4       True      True
      (1,3)   -1/4   -1/4       True      True
      (1,4)    1/4    1/4       True      True
      (2,0)      1      1       True      True
      (2,1)     -1     -1       True      True
      (2,2)   -1/2   -1/2       True      True
      (2,3)    1/2    1/2       True      True
      (2,4)      0      0       True      True
      (3,0)      1      1       True      True
      (3,1)     -1     -1       True      True
      (3,2)    1/2    1/2       True      True
      (3,3)   -1/2   -1/2       True      True
      (3,4)      0      0       True      True
      (4,0)    3/2    3/2       True      True
      (4,1)    3/2    3/2       True      True
      (4,2)      0      0       True      True
      (4,3)      0      0       True      True
      (4,4)   -1/2   -1/2       True      True

    pre == post (whole matrix)   : True
    pre == frozen (whole matrix) : True
    post == frozen (whole matrix): True
    all 25 entries equal         : True

    --- both forms are blind to the declared value (independent check) ---
      sign=-1: pre-edit form == frozen -> True
      sign= 1: pre-edit form == frozen -> True
      post-edit form has no sign factor at all -> == frozen -> True

The comparison is of exact rationals throughout; no floating point is
involved. **The matrices are equal, so no STOP arose** — the premise
that the two factors were already cancelling is confirmed, not assumed.

The last block is the independent confirmation that the *pre-edit* code
was inert: substituting either admissible declared value into the old
expression reproduces the frozen matrix. That is the defect, stated
positively.

A second, independent route to the same conclusion: the edited checker's
`require(computed_fierz == frozen_fierz)` still passes against the
unmodified frozen artifact (§7), and the unedited checker passed against
the same artifact at the evidence base. Both therefore equal the frozen
matrix, hence each other.

## 5. A3 — the sign is still parsed, and malformed values are still rejected

Demonstrated through the **edited** checker end to end, by handing
`verify()` a `c_override` whose `grassmann_crossing_sign` is malformed.
The freeze on disk was not touched.

    baseline verify() with the real freeze:
      -> PASSED (no exception)

    A3: malformed grassmann_crossing_sign fed to the EDITED checker via c_override
         '0' -> REJECTED  ParseError: invalid grassmann crossing sign
         '2' -> REJECTED  ParseError: invalid grassmann crossing sign
      '-1/2' -> REJECTED  ParseError: invalid grassmann crossing sign
       '1.5' -> REJECTED  ParseError: invalid token in frozen expression
          '' -> REJECTED  ParseError: unexpected end of frozen expression
         'x' -> REJECTED  ParseError: outside frozen vocabulary: x

    control: an admissible but WRONG value is NOT rejected (by design)
        '-1' -> accepted, checker is blind to which of the two it is
         '1' -> accepted, checker is blind to which of the two it is

The control block is the point of §1 restated mechanically: the checker
distinguishes well-formed from malformed, and deliberately does not
distinguish right from wrong. That distinction is the operator layer's
job, and §6 is where it is now made.

## 6. A4 — the production comparison, shown rejecting a flipped declaration

**Two different outcomes, kept separate throughout this section:** the
**production** comparison must REJECT; the **pytest** test must PASS by
asserting that the rejection happened. Both are evidenced below.

### 6.1 Mechanism, and why it exercises the production path

The one place in the repository where a *computed* crossing sign meets a
*declared* one is `scripts/p2_grassmann_crossing_sign.py`, in `main()`:

    "declared_grassmann_crossing_sign": DECLARED_CROSSING_SIGN,
    "s_G_equals_declared_value": bool(sign == DECLARED_CROSSING_SIGN),

`sign` there is the output of `explicit_anticommutation()`, computed by
explicit adjacent transpositions at call time.

The flip is injected by rebinding the module attribute
`DECLARED_CROSSING_SIGN`, which `main()` reads as a global at call time.
The production `main()` is then invoked and its returned payload
inspected. In addition, `OUT` is rebound to a `tmp_path` file so the
production run writes nowhere in the repository.

Why this exercises the production path rather than a re-implementation:
the test computes nothing. It calls `consumer.main()` and reads the
values that function produced. The comparison `sign == DECLARED_CROSSING_SIGN`
is executed by the production module, on a `sign` the production module
derived, against a declaration the production module looked up. The test
asserts only on the recorded outcome.

Why the flip is supplied this way rather than by editing data: the
consumer does not read `grassmann_crossing_sign` from the freeze — the
declaration is the module-level literal `DECLARED_CROSSING_SIGN = -1`
(see §11, finding 2). That attribute is therefore the only injectable
boundary that reaches the comparison. **No repository file was edited,
transiently or otherwise**, which §6.3 verifies by bytes.

### 6.2 What the production code did

Run outside pytest, driving the production `main()` directly:

    --- PRODUCTION RUN 1: real declaration (no flip) ---
      s_G = -1
      routes = {"explicit_selection_sort": -1, "derivation_note_decomposition": -1,
                "permutation_parity_inversions": -1, "permutation_parity_transpositions": -1}
      all_routes_agree = true
      declared_grassmann_crossing_sign = -1
      s_G_equals_declared_value = true

    --- PRODUCTION RUN 2: declaration flipped to +1 ---
      s_G = -1
      routes = {"explicit_selection_sort": -1, "derivation_note_decomposition": -1,
                "permutation_parity_inversions": -1, "permutation_parity_transpositions": -1}
      all_routes_agree = true
      declared_grassmann_crossing_sign = 1
      s_G_equals_declared_value = false

    --- what the production code recorded, read back from its own artifact ---
      declared_grassmann_crossing_sign : 1
      s_G                              : -1
      s_G_equals_declared_value        : False

    --- keys whose value differs between the two production runs ---
      ['declared_grassmann_crossing_sign', 's_G_equals_declared_value']

**The production comparison rejected**: `s_G_equals_declared_value`
became `false`, both in the returned payload and in the JSON the
production code itself wrote. The computed `s_G` stayed `−1` and all four
derivation routes still agreed, so the rejection came from the
comparison and not from a disturbed calculation. The last block confirms
the flip changed exactly two recorded values: the declaration that was
injected, and the verdict the production comparison produced from it.

### 6.3 What the tests assert, and that they pass

Four tests were added to `tests/test_p2_grassmann_crossing_sign.py`:

- `test_production_comparison_accepts_the_real_declaration` — baseline;
  unflipped, `s_G_equals_declared_value is True`.
- `test_production_comparison_rejects_a_flipped_declaration` — the core
  assertion, `s_G_equals_declared_value is False` while `s_G == -1` and
  `set(routes.values()) == {-1}`.
- `test_flip_changes_only_the_declaration_and_the_verdict` — the set of
  differing keys between the two production payloads is exactly
  `{"declared_grassmann_crossing_sign", "s_G_equals_declared_value"}`,
  which localises the rejection to the comparison.
- `test_flip_demonstration_writes_no_repository_file` — the freeze
  document and the committed `crossing_sign.json` are byte-identical
  before and after the flipped production run, and the redirected
  temporary file does exist, so the run genuinely happened.

    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py -v
    ...
    tests/test_p2_grassmann_crossing_sign.py::test_production_comparison_accepts_the_real_declaration PASSED [ 78%]
    tests/test_p2_grassmann_crossing_sign.py::test_production_comparison_rejects_a_flipped_declaration PASSED [ 84%]
    tests/test_p2_grassmann_crossing_sign.py::test_flip_changes_only_the_declaration_and_the_verdict PASSED [ 89%]
    tests/test_p2_grassmann_crossing_sign.py::test_flip_demonstration_writes_no_repository_file PASSED [ 94%]
    tests/test_p2_grassmann_crossing_sign.py::test_results_artifact_records_both_results_separately PASSED [100%]

    ============================== 19 passed in 0.52s ==============================
    === exit 0 ===

15 tests before, 19 after; no existing test was modified. **The suite
exits 0**, as A9 requires, while the production comparison it drives
rejected — the two outcomes A4 insists on keeping apart.

Independently of pytest, the committed artifacts were hashed either side
of the demonstration:

    BEFORE  29b70d4bcc62dcc2938bc1db9137d4cc2162ca7693c51aaed382ff12718cc713  results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
    BEFORE  fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a  derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    AFTER   29b70d4bcc62dcc2938bc1db9137d4cc2162ca7693c51aaed382ff12718cc713  results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
    AFTER   fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a  derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md

    $ git status --porcelain=v1
     M scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
     M tests/test_p2_grassmann_crossing_sign.py

## 7. A5, A6 — `MUTATIONS`, freeze data and `vocab_parser.py` untouched

Compared by git blob OID against the evidence base, read from the object
store:

    PATH                                                 BASE_BLOB / WORKTREE_BLOB                  SAME
    tests/test_channel_freeze_mutations.py               d938e2c4d2ca460c344fe1cda4a713794f7fd0c0   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md    0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json          5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256   601a5db8871bd6bc2534a0a7aa33d7a70d8159cf   IDENTICAL
    scripts/P2-CHANNEL-FREEZE/vocab_parser.py            20800bc649924fd0629b3232615dae4c4fac36a7   IDENTICAL
    tests/test_channel_freeze_phase_a.py                 cce7be76b667b2a1bb7a5e0169325603419dda63   IDENTICAL
    GATES.md                                             bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                       2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                            5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml                                       9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL

    $ grep -c -i grassmann tests/test_channel_freeze_mutations.py
    0

**No `grassmann` entry was added to `MUTATIONS`, deliberately.** That
list drives `test_checker_rejects_each_frozen_data_corruption`, which
asserts the checker rejects each corruption. The checker is correctly
blind to this field, so such an entry would assert a rejection that must
not happen and would encode the defect as a requirement.

## 8. A7 — every existing assertion still passes

    $ python -m pytest tests/test_channel_freeze_phase_a.py -v
    tests/test_channel_freeze_phase_a.py::test_channel_freeze_machine_verifier PASSED [ 33%]
    tests/test_channel_freeze_phase_a.py::test_channel_freeze_phase_a_frozen_with_hash PASSED [ 66%]
    tests/test_channel_freeze_phase_a.py::test_channel_freeze_vector_path_analytic PASSED [100%]
    ============================== 3 passed in 0.53s ===============================
    === exit 0 ===

    $ python -m pytest tests/test_channel_freeze_mutations.py -v
    ...[matrix-computed Fierz matrix mismatch] PASSED [ 11%]
    ...
    ============================== 18 passed in 1.96s ==============================
    === exit 0 ===

Both suites are blob-identical to the evidence base and both pass
unchanged. The `matrix` mutation in particular still rejects with
`computed Fierz matrix mismatch`, which confirms the equality assertion
the edit touches is still live and still discriminating — the edit
removed an inert factor, not a check.

## 9. A9-pre — nine validators individually, at head `f8873aa0`

    $ python -m pytest tests/test_repository_structure.py            ->  4 passed   exit 0
    $ python -m pytest tests/test_si1_governance.py                  -> 14 passed   exit 0
    $ python -m pytest tests/test_gate_anchors.py                    -> 18 passed, 2 deselected   exit 0
    $ python -m pytest tests/test_governance_tools.py                ->  8 passed   exit 0
    $ python -m pytest tests/test_p2_phase01_scalar_exploratory.py   ->  5 passed   exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py     -> 14 passed   exit 0
    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py      -> 19 passed   exit 0
    $ python -m pytest tests/test_channel_freeze_phase_a.py          ->  3 passed   exit 0
    $ python -m pytest tests/test_channel_freeze_mutations.py        -> 18 passed   exit 0

All nine exit 0. `pytest` on `PATH` is 9.0.2 and `python -m pytest` is
9.1.1 in this environment; the specification mandates `python -m pytest`
and that is what was run, so the reported version is 9.1.1.

A9-final, at the pushed head, is post-report evidence and carries the
verdict.

## 10. A8 and A10 — scope and lint

### 10.1 Manifest template

Held with a `{PUSHED_HEAD}` placeholder so that its digest does not
depend on the report commit. SHA-256 of the template as written:
`3e61ab97a14791a3aeb3f6dcdfa9d66aa0adb7384756105238fafbecfb924c7b`.

    {
      "base": "236f71c69ef9abec33ef0d808724ce80af037710",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
        {"operation": "add", "path": "derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md"},
        {"operation": "add", "path": "reports/2026-08-07T1424Z_freeze-checker-sign-repair.md"},
        {"operation": "modify", "path": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"},
        {"operation": "modify", "path": "tests/test_p2_grassmann_crossing_sign.py"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Three additions and two modifications, matching A8. The resolved
manifest, its SHA-256 and the checker JSON at the pushed head are
post-report evidence.

### 10.2 Pre-report scope check

Run at head `f8873aa0`, where the report commit does not yet exist, so
its manifest carries four operations rather than five:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "236f71c69ef9abec33ef0d808724ce80af037710",
      "failures": [],
      "head": "f8873aa02c22f7110c957bfbc5b9d5120d7e80fb",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-CHANNEL-FREEZE-01_checker_sign_repair.md"
        },
        {
          "operation": "modify",
          "path": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-07T1424Z_freeze-checker-sign-repair.md"
        },
        {
          "operation": "modify",
          "path": "tests/test_p2_grassmann_crossing_sign.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` is empty and no forbidden operation appears. This is a
partial check by construction; the authoritative five-operation check is
post-report.

### 10.3 A10 — lint

    $ ruff --version
    ruff 0.15.8
    $ ruff check scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py tests/test_p2_grassmann_crossing_sign.py
    All checks passed!
    === exit 0 ===

Run from the repository root, so `[tool.ruff]` and `[tool.ruff.lint]` in
`pyproject.toml` apply (`line-length = 88`, `select = ["E", "F", "I"]`).
Only the two files this task authored or edited were linted; the three
Markdown files are not Python. The eight known pre-existing diagnostics
on the hash-pinned `scripts/euclidean_reconstruction.py` were not touched
and are not this task's to fix.

## 11. Stops and clarifications

**Stops: none.** No condition in the specification triggered a stop. In
particular A1 matched on all six pins, and A2's matrices were equal, so
the premise of the task held.

Findings, none of which is a stop:

**Finding 1 — `REPOSITORY_DEFECT` (the one this task repairs).** The
inert double application in `basis_freeze_check.py` presented as
validation of `grassmann_crossing_sign` while provably doing nothing with
it. Repaired.

**Finding 2 — `REPOSITORY_DEFECT`, residual, NOT repaired here.**
`DECLARED_CROSSING_SIGN = -1` is a literal in
`scripts/p2_grassmann_crossing_sign.py`; that consumer never reads
`grassmann_crossing_sign` from the freeze. So the new coverage catches
*"the consumer's declared constant disagrees with the computed sign"*. It
does **not** catch *"the freeze document's `grassmann_crossing_sign` was
flipped"* — such a flip reaches no comparison anywhere in the repository,
because no consumer compares that field against a computed `s_G`.

I state this rather than close it because closing it means editing
`scripts/p2_grassmann_crossing_sign.py`, which is not among A8's five
authorised paths. **The gap is narrowed, not eliminated**, and the report
should not be read as saying otherwise. A follow-up task making the
consumer read the freeze field would close it.

**Finding 3 — secondary, cosmetic.**
`scripts/p2_grassmann_crossing_sign.py` records
`"source": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:462"` inside
`checker_sign_invariance()`. After this edit that line number no longer
points at the expression it names. The file is not among the authorised
paths, so it is unchanged. There is a case for leaving it regardless: it
is a historical record of the defect as found, and
`test_checker_expression_is_invariant_under_flipping_the_sign` still
passes because that function reproduces the old expression locally rather
than reading the checker. Flagged for the PI to decide.

**Finding 4 — secondary, observation about the parser.**
`parse_grassmann_sign("--1")` returns `Integer(1)`: the frozen grammar
admits a doubled unary minus, and the result is an admissible value, so
this is not a well-formedness failure. It is worth recording only because
it is a second way an admissible-but-wrong value can enter while looking
superficially like the declared `-1`. `vocab_parser.py` is unmodified.

**Clarification 1 — where A4's "existing injectable function boundary"
landed.** A4 permitted "a synthetic or temporary input, or … an existing
injectable function boundary". There is no function parameter carrying
the declaration — it is read as a module global inside `main()` — so the
injectable boundary used is that module attribute, together with `OUT`
so the run writes to a temporary path. Both are rebound by pytest's
`monkeypatch` and restored automatically. I judged this within A4 rather
than a deviation, but flag the reading explicitly.

**Clarification 2 — what "the production comparison fails" means for
this consumer.** `scripts/p2_grassmann_crossing_sign.py` is a reporting
script: it records verdicts rather than raising. So its rejection of the
flipped declaration takes the form of recording
`s_G_equals_declared_value: false` — in the returned payload and in the
JSON it writes — not of an exception. §6.2 shows both. I take that as
satisfying "fails or rejects as expected"; if the PI intended a raising
consumer, that is a change to
`scripts/p2_grassmann_crossing_sign.py` and outside these authorised
paths.

## 12. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing in this specification was unsatisfiable.** All eleven criteria
were met as written; no defect required a ruling.

Two things I would have specified differently:

**(a) A8 does not authorise the path that would close the gap.** The
specification correctly identifies
`scripts/p2_grassmann_crossing_sign.py` as "the operator-level consumer
… where a flipped declaration must be caught", but authorises edits only
to the *test* file, not the consumer. Because the consumer hardcodes its
declaration, the strongest coverage reachable within scope is Finding 2's
partial one. I would have either added the consumer to the modify list
so it reads `grassmann_crossing_sign` from the freeze, or stated
explicitly that a partial closure is the intended outcome of this task
and the rest is queued. As written, the ambition of §0 ("that consumer is
where a flipped declaration must be caught") is slightly ahead of what
A8 permits.

**(b) A2 asks for the pre-edit matrix after the edit is made.** Taken
literally, reporting "the matrix computed by the pre-edit code" once the
pre-edit code no longer exists requires either reconstructing the old
expression or capturing it beforehand. I did the latter — the A2 harness
was run against the unedited checker's ingredients and evaluates both
forms in one process — and then re-confirmed post-edit via §8. Saying
which of the two is wanted would remove the ambiguity.

One thing I would keep exactly as written: the explicit warning in §0
that applying the sign once is the trap, together with the prohibition on
adding a `grassmann` mutation. Both are the kind of instruction that
prevents a plausible, confident, wrong repair, and I would not have
reached the "zero, not one" conclusion as quickly without the ruling
being cited.

## 13. Commits, and commit-message hygiene

Commits 1–3, at the pre-report head. The report commit's SHA is
necessarily absent from the report it commits; its intended message is
given below and its stored message is read back as post-report evidence.

**Commit 1** — `78d8a7d90f132e54a22c9585a80ee215d365f523`

    spec: repair the Phase-A freeze checker's sign handling

    Records the PI specification for the checker sign repair, evidence base
    236f71c69ef9abec33ef0d808724ce80af037710, transcribed verbatim.

    The checker applies the Grassmann crossing sign twice, and the two
    occurrences cancel. The repair removes both, applying it zero times:
    matrix_rational is stored unsigned per the 2026-08-07 ruling, and the
    sign belongs to the operator layer. Coverage for a flipped declaration
    goes to the operator-level consumer, not to the freeze mutation suite.

**Commit 2** — `78b6679f309f2c70ce094c9dd279f32b1fa755f3`

    derivation: why the freeze checker applies the crossing sign zero times

    Fixes the reasoning before the code change, per AGENTS.md rule 3.

    basis_freeze_check.py validates the stored, unsigned matrix_rational;
    the Grassmann crossing sign is the parity of a fermionic reordering and
    belongs to the passage from matrix to operator. Under the 2026-08-07
    ruling s_G is applied exactly once at operator use, so the correct count
    inside the checker is zero, not one. Applying it once would force an
    edit to a hash-pinned frozen artifact.

    Records that removing both inert factors leaves computed_fierz equal in
    all 25 entries, that parse_grassmann_sign must keep running, why the
    tenth mutation cannot live in the freeze mutation suite, vocab_parser's
    role and its limit, and the residual gap left by the consumer's
    hardcoded declaration.

**Commit 3** — `f8873aa02c22f7110c957bfbc5b9d5120d7e80fb`

    fix: stop the freeze checker applying the crossing sign, cover the flip

    basis_freeze_check.py applied parse_grassmann_sign's result twice around
    a transposition. Transposition does not act on a scalar, so the two
    occurrences multiplied to sign**2 = +1 and the reconstruction was blind
    to the declared value. Both occurrences are removed rather than reduced
    to one: matrix_rational is stored unsigned and s_G is applied once at
    operator use, so the correct count inside this checker is zero. Applying
    it once would leave the reconstruction an overall -1 from the frozen
    table and could only be reconciled by editing frozen data.

    computed_fierz is unchanged by the edit, equal in all 25 entries as
    exact rationals, and still equal to the frozen matrix_rational. The
    parse is kept, so a malformed declaration is still rejected.

    Coverage for a flipped declaration goes to the operator layer, where a
    computed s_G meets a declared one. Four tests drive the production
    comparison in scripts/p2_grassmann_crossing_sign.py through the module
    attribute it reads, with the artifact path redirected to a temporary
    directory; the production code reports the mismatch and the tests pass
    by asserting that it did. No repository file is written by the
    demonstration, and the freeze mutation suite is untouched: a grassmann
    entry there would assert a rejection that must not happen.

**Intended report commit message** (commit 4):

    docs: report the freeze checker sign repair

    Records A1-A7, A9-pre and A10 for the repair that stops
    basis_freeze_check.py applying the Grassmann crossing sign, together
    with the entry-by-entry demonstration that computed_fierz is unchanged
    and the evidence that the operator-layer production comparison rejects
    a flipped declaration while its pytest suite exits 0.

    Also records the residual gap: the consumer hardcodes its declaration
    rather than reading the freeze, so a flip of the freeze field itself
    still reaches no comparison.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this branch
by composing the message in a file and committing with `git commit -F`,
never with `-m` and never through a path that would append them.

    commit 1  78d8a7d9   suppressed: Co-Authored-By, Claude-Session
    commit 2  78b6679f   suppressed: Co-Authored-By, Claude-Session
    commit 3  f8873aa0   suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)   suppression applied identically; stored message
                         read back as post-report evidence

Each proposed message was inspected with `cat -A` before committing and
each stored message read back with `git log -1 --format=%B` after; a
`grep` for `co-authored-by`, `claude-session`, `claude.ai`,
`generated with` and `noreply@anthropic` returned no match on either the
proposed or the stored form, for all three commits.

**Suppression is a fact disclosed here, not an absence.** The trailers
were not merely missing; a convention that would have added them was
deliberately bypassed.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
They are noted so the Reviewer is not surprised by them.

## 14. A11 — branch only

Reported at the pre-report head; the final ref state is post-report
evidence.

    refs/remotes/origin/main        236f71c69ef9abec33ef0d808724ce80af037710
    remote refs/heads/main          236f71c69ef9abec33ef0d808724ce80af037710
    local main                      0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**Local `main` is stale by design and was not repaired**, as instructed.
None of the three was moved by this task. The branch
`fix/freeze-checker-sign-repair` was created from
`236f71c69ef9abec33ef0d808724ce80af037710` in a separate worktree; the
primary worktree remains on `gate/p2-grassmann-crossing-sign`. **No
branch was deleted or renamed.** No merge, no PR, no force-push, no
history rewrite.
