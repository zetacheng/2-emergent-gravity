# Task report — the Grassmann crossing sign, by explicit single-leg exchange

Function: Executor
Date: 2026-08-07
Task classification: MATERIAL (branch only; integration is a separate
authorization after result review)
Executor: Claude Code (sandboxed container)

Authority: `specs/2026-08-07T1159Z_grassmann-crossing-sign.md`
Derivation note: `derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md`

**This is a computation, not a ruling.** It reports what the algebra
gives. Whether the Phase-A freeze is amended, and how, is a PI decision
outside this task. No frozen artifact, checker or mutation suite was
modified.

**One question was answered and one was tested.** `s_G` is
**ESTABLISHED**; the matrix-storage convention is
**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`**.

---

## 1. Identification

| Item | Value |
| --- | --- |
| Branch | `gate/p2-grassmann-crossing-sign` |
| Base (evidence base) | `9609677576b6d0d77a0813c93673aed81b0c4d5f` |
| Commit 1 (specification) | `d652f7791aa9b9dc0377db0caa6787e3b3831a91` |
| Commit 2 (derivation note) | `86018c26c6f0a0d7a1346638b26df0fc6701fb4f` |
| Commit 3 (script, results, test) | `787a858ed62370df0b9a5aa27fddbf5b0dc47774` |
| Pre-report head | `787a858ed62370df0b9a5aa27fddbf5b0dc47774` |
| UTC token `{HHMM}` | `1159`, observed `2026-08-07T11:59:04Z` |
| Specification blob SHA-256 | `56d8264eff9bd4fd26d73b21813589b0b6059657d96690b7ae7799f0e23887fd` |

### Commit messages, exactly as stored

Commit 1:

```text
specs: record the Grassmann crossing-sign ratification authority

Commits the PI specification for the single-question task: determine the
operator-level Grassmann exchange sign by explicit four-fermion monomial
calculation under the frozen permutation, and test separately whether the
frozen material fixes how matrix_rational stores it.

The permutation is frozen by the specification: psibar_1 psi_2 psibar_3
psi_4 rearranged to the 1-4 / 3-2 pairing with final order psibar_1 psi_4
psibar_3 psi_2. No other reading of "exchange" is in scope.

Nothing frozen is modified. The freeze, basis_freeze_check.py and the
mutation suite are read-only inputs; the missing tenth mutation is a
known gap and a separate task.
```

Commit 2:

```text
derivations: fix the Grassmann crossing-sign analytic content

Commits the derivation note before any production code, per AGENTS.md
research rule 3. It fixes, before any output exists:

- the frozen conventions and chiral projectors, none of which is chosen
  here;
- the normative monomial, the normative starting and final Grassmann
  orderings, and the three adjacent anticommutations whose product is
  the operator-level crossing sign;
- the requirement that the sign be obtained twice independently, by
  explicit anticommutation and by permutation parity, and that the two
  agree;
- the storage question as a SEPARATE test of whether the frozen material
  contains a defining kernel equation, with the explicit rule that
  numerical equality of an unsigned reconstruction with matrix_rational
  is not evidence for it;
- the sign-blind chiral cross-check with frozen projectors;
- the characterisation of the checker's double application of the scalar
  sign, by direct substitution and without modifying it.

Nothing frozen is modified and no ruling is taken.
```

Commit 3:

```text
p2-channel-freeze-01: compute the Grassmann crossing sign explicitly

Adds the script, the results artifact and a new test file.

The operator-level exchange sign is obtained from the explicit
four-fermion monomial under the permutation frozen by the specification,
by four independent routes: an adjacent-transposition selection sort, the
three-step decomposition named in the derivation note, an inversion count
and a cycle decomposition. All four agree.

The storage question is treated separately and is not answered from the
numerical equality of an unsigned reconstruction with matrix_rational.
The sign-blind chiral decomposition and the checker's invariance under
flipping the declared sign are recorded with their outputs.

No frozen artifact, checker or mutation suite is modified. No ruling is
taken on how or whether the freeze should be corrected.
```

**Trailer hygiene, per commit.** Each proposed message was inspected
before the commit and each stored message read back from the commit
object afterwards. **For commits 1, 2 and 3 alike, two trailers were
suppressed at authoring time** — a `Co-Authored-By:` line and a
`Claude-Session:` URL line that this executor's harness convention would
otherwise append. **The suppression is a fact to disclose, not an
absence.** The scan of each stored message returns zero hits for
`co-authored-by`, `claude-session`, `session_`, `claude.ai`,
`generated with` and `signed-off-by`.

### Intended report commit message

```text
docs: report the Grassmann crossing sign and the storage-convention test

Records the explicit four-fermion exchange calculation establishing
s_G = -1 by four independent routes, the separate test showing the frozen
material contains no defining kernel equation, the sign-blind chiral
decomposition, and the freeze checker's invariance under flipping the
declared sign.

The final scope check, A9-final, the push and this commit's own stored
message are post-report evidence and are deliberately absent here.
```

Its authoring-time trailer suppression is the same two lines. **This
report records neither its own commit SHA nor the final branch head.**

---

## 2. A1 — pinned inputs verified

```text
PINNED INPUTS at the evidence base 9609677576b6d0d77a0813c93673aed81b0c4d5f
  MATCH     derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
            expected fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
            actual   fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
  MATCH     results/P2-CHANNEL-FREEZE/fierz_matrix.json
            expected 5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
            actual   5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
  MATCH     derivations/CANONICAL_INTERACTION.md
            expected 27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
            actual   27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
  MATCH     scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
            expected b3123855c225c6832c890c42fda6b03b4b8b81eef69a1c69ae654d7523367fdb
            actual   b3123855c225c6832c890c42fda6b03b4b8b81eef69a1c69ae654d7523367fdb
  MATCH     tests/test_channel_freeze_mutations.py
            expected 4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0
            actual   4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0
  MATCH     tests/test_channel_freeze_phase_a.py
            expected 80ee0e834287e5f5c2185c881633e656454ff9e7935382dabc6370e16c204d3d
            actual   80ee0e834287e5f5c2185c881633e656454ff9e7935382dabc6370e16c204d3d
```

---

## 3. A2 / A3a — the Grassmann exchange sign

### 3.1 The monomial and the frozen permutation

```text
( psibar^{i}_{alpha}  Gamma_{alpha beta}  lam^{A}_{ij}  psi^{j}_{beta} )
( psibar^{k}_{gamma}  Gamma_{gamma delta} lam^{A}_{kl}  psi^{l}_{delta} )

  1 = psibar^{i}_{alpha}      2 = psi^{j}_{beta}
  3 = psibar^{k}_{gamma}      4 = psi^{l}_{delta}

  starting order (normative):  psibar_1  psi_2  psibar_3  psi_4
  final order    (normative):  psibar_1  psi_4  psibar_3  psi_2
```

**Legs exchanged: `psi_2` and `psi_4`.** The two `psibar` legs do not
move. `Gamma`, `lam^A` and every index contraction are commuting
c-numbers and contribute no sign, so the entire question is the parity of
the reordering of the four Grassmann objects.

### 3.2 Every anticommutation, shown

Each adjacent exchange of two Grassmann-odd objects contributes exactly
`-1`.

**Route 1 — adjacent-transposition selection sort (what the script
executes):**

```text
  step 1: move     psi_4 past psibar_3  sign -1  ->  psibar_1 psi_2 psi_4 psibar_3   cumulative -1
  step 2: move     psi_4 past psi_2     sign -1  ->  psibar_1 psi_4 psi_2 psibar_3   cumulative +1
  step 3: move  psibar_3 past psi_2     sign -1  ->  psibar_1 psi_4 psibar_3 psi_2   cumulative -1
```

**Route 2 — the three-step decomposition named in the derivation note:**

```text
  step 1: move     psi_2 past psibar_3  sign -1  ->  psibar_1 psibar_3 psi_2 psi_4   cumulative -1
  step 2: move     psi_2 past psi_4     sign -1  ->  psibar_1 psibar_3 psi_4 psi_2   cumulative +1
  step 3: move     psi_4 past psibar_3  sign -1  ->  psibar_1 psi_4 psibar_3 psi_2   cumulative -1
```

Both reach the normative final ordering
`psibar_1 psi_4 psibar_3 psi_2` in three adjacent anticommutations, and
both give `-1`. They are different decompositions of the same
permutation; see §8.3.

**Routes 3 and 4 — permutation parity, independent of any decomposition:**

```text
  permutation (one-line, 0-based)  : [0, 3, 2, 1]
  nontrivial cycles                : [[1, 3]]   -> a single transposition of positions 2 and 4
  transposition count              : 1  -> sign -1
  inversion count                  : 3  -> sign -1
```

The permutation is the single transposition of the objects in positions
2 and 4 — exactly the exchange `psi_2 <-> psi_4`. It is odd.

### 3.3 The result

```text
  derivation_note_decomposition          -1
  explicit_selection_sort                -1
  permutation_parity_inversions          -1
  permutation_parity_transpositions      -1
  all routes agree                       : True
  s_G                                    : -1
  declared grassmann_crossing_sign       : -1
  s_G == declared                        : True
```

**`s_G = -1`.** It **equals** the declared
`grassmann_crossing_sign = -1` of the Phase-A freeze.

**So the declared value is correct as an operator-level statement.** The
freeze's declaration is ratified by explicit calculation, which is what
this task was for. That is a statement about the operator algebra and
nothing more.

---

## 4. A3b — the storage convention: tested, not answered

**Verdict: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.**

The question is whether the frozen material's defining kernel equation
selects

    K_exch = M . K_direct           (matrix stores the sign)
    K_exch = s_G . M . K_direct     (sign applied on use)

**There is no defining kernel equation anywhere in the frozen material.**

```text
  freeze JSON top-level keys   : ['basis_order', 'basis_elements', 'conventions', 'matrix_rational']
  standalone artifact keys     : ['basis_order', 'matrix_rational']
  kernel-equation markers found: {'= M ': 0, 'K_direct': 0, 'K_exch': 0, 'M *': 0, 'M .': 0, 'defining equation': 0, 'kernel equation': 0}
  defining kernel equation present: False
  verdict                      : UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY
```

The freeze's JSON block carries only `basis_order`, `basis_elements`,
`conventions` and `matrix_rational`; the standalone artifact carries only
`basis_order` and `matrix_rational`. Neither contains an equation
relating an exchanged kernel to a direct one. Every marker that such an
equation would have to contain occurs zero times in the freeze document.

**The only prose describing what the matrix means is §C, quoted in
full:**

```text
## §C — Exact representation-family Fierz map

Level: **representation family** (not component rank).  Euclidean hermitian
Dirac basis: `S=Id4`, `P=gamma5`, `V=gamma(mu)`,
`A=I*gamma(mu)*gamma5`, and
`T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2`, with component counts
`1,1,4,4,6`.  The recovered `fierz_verify.py` algebra and the Grassmann
crossing sign `-1` fix the following exact exchange matrix; its square is the
identity and its family rank is five.  All strings are canonical exact SymPy
expressions; no float is used.

```json
```

The operative sentence is *"The recovered `fierz_verify.py` algebra and
the Grassmann crossing sign `-1` fix the following exact exchange
matrix"*. **It says the sign participates in fixing the matrix. It does
not say whether the tabulated entries include it.** Both readings survive
that sentence, and nothing else in the frozen material discriminates.

**What was deliberately NOT used as evidence.** The numerical equality of
an unsigned reconstruction with `matrix_rational` — established in the
previous task — is **not** used here to infer the storage convention.
That equality is consistent with either convention: it shows the entries
match a signless construction, not that the defining equation omits the
sign. A test in the accompanying suite asserts that this disclaimer is
present and that the verdict does not rest on that inference.

---

## 5. A4 — the chiral decomposition (sign-blind)

Projectors frozen by the specification, `P_L = (Id4 - gamma5)/2`,
`P_R = (Id4 + gamma5)/2`, with the Phase-A `gamma5`.

```text
  direct   S^2 - P^2   expanded = 4*S_L*S_R
      LL=0   LR=2   RL=2   RR=0    purely left-right: True
  exchanged V^2 + A^2  expanded = 4*J_L*J_R
      LL=0   LR=2   RL=2   RR=0    purely left-right: True
  projector checks: {'P_L_P_R_orthogonal': True, 'P_L_idempotent': True, 'P_L_plus_P_R_is_Id4': True, 'P_R_idempotent': True, 'gamma5_hermitian': True, 'gamma5_squares_to_Id4': True}
```

**Both the direct and the exchanged forms are purely left-right**:
`LL = RR = 0` in each, with `LR = RL = 2` under the symmetric split.
`S^2 - P^2 = 4 S_L S_R` and `V^2 + A^2 = 4 J_L J_R`.

**This agrees with the expectation stated in the specification**, which
invited contradiction. It does not corroborate `s_G`: an overall sign
multiplies all four coefficients equally, so the check is blind to it by
construction. What it does corroborate is the *structure* of the
rearrangement — that the exchanged form lands in the current channel with
the same chirality pattern the scalar channel had.

`S^2 - P^2` here is the canonical interaction after the already-ratified
`I*gamma5 -> gamma5` conversion, not a new interaction choice.

---

## 6. A5 — the checker's double application, characterised

```text
  expression : (sign * projector * crossing * embedding).T * sign
  source     : scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:462
  sign = -1  -> [['2', '4'], ['1', '3']]
  sign = +1  -> [['2', '4'], ['1', '3']]
  invariant under sign flip            : True
  mutation suite covers the field      : False
  checker modified by this task        : False
```

**The expression is invariant under `sign -> -sign`.** `sign` is a scalar
and `.T` does not act on a scalar factor, so the two occurrences multiply
to `sign^2 = +1`. The checker therefore validates the same matrix whether
the freeze declares `-1` or `+1`.

**`tests/test_channel_freeze_mutations.py` contains no mutation of this
field**, so a flipped declaration would pass every existing check
silently. **The checker was not modified, and neither was the mutation
suite** — the missing tenth mutation is a known gap and a separate task.

---

## 7. A6–A8 — deliverables, integrity, scope

| deliverable | path |
| --- | --- |
| specification | `specs/2026-08-07T1159Z_grassmann-crossing-sign.md` |
| derivation note | `derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md` |
| script | `scripts/p2_grassmann_crossing_sign.py` |
| results | `results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json` |
| test file | `tests/test_p2_grassmann_crossing_sign.py` |
| report | `reports/2026-08-07T1159Z_grassmann-crossing-sign.md` |

The 15 tests cover the three things this task is about: the explicit
exchange sign (six tests, including agreement of all four routes and the
permutation's identity as a single transposition); the chiral
decomposition (four tests, including an explicit sign-blindness test);
and the checker's sign invariance plus the mutation-suite gap (two
tests). Two further tests lock the storage verdict **and** the disclaimer
that it is not inferred from numerical equality. **No test asserts that
the frozen matrix equals itself.**

### A7 — nothing pre-existing disturbed

```text
$ git diff --name-status --find-renames --find-copies 9609677576b6d0d77a0813c93673aed81b0c4d5f 787a858ed62370df0b9a5aa27fddbf5b0dc47774
A	derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md
A	results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
A	scripts/p2_grassmann_crossing_sign.py
A	specs/2026-08-07T1159Z_grassmann-crossing-sign.md
A	tests/test_p2_grassmann_crossing_sign.py
[end — additions only, no modification of anything pre-existing]

blob identity of every artifact this task must not touch:
  GATES.md                                                   IDENTICAL  bd4820513217ae7e1c493328dc49536e69b8cfb8
  CONVENTIONS.md                                             IDENTICAL  2d4f735c55a14fdfc5d1031a58698a8ca075fbbd
  AGENTS.md                                                  IDENTICAL  5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3
  pyproject.toml                                             IDENTICAL  9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4
  CLAIMS.md                                                  IDENTICAL  df75ff4de2146fff64ce4995f295c603e7d5b861
  derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md          IDENTICAL  0be773f6a52c759abd23438c66da6b43bca44930
  scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py            IDENTICAL  c26920627eb38e2ef01349f23e3b7b63608278e4
  scripts/P2-CHANNEL-FREEZE/vocab_parser.py                  IDENTICAL  20800bc649924fd0629b3232615dae4c4fac36a7
  tests/test_channel_freeze_mutations.py                     IDENTICAL  d938e2c4d2ca460c344fe1cda4a713794f7fd0c0
  tests/test_channel_freeze_phase_a.py                       IDENTICAL  cce7be76b667b2a1bb7a5e0169325603419dda63
  results/P2-CHANNEL-FREEZE/fierz_matrix.json                IDENTICAL  5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8
  results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256         IDENTICAL  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf
  derivations/CANONICAL_INTERACTION.json                     IDENTICAL  0c992d83bbd740357938d62d55a9343a2333cb71

pre-existing tests/ unchanged, only the new file added:
  base: 11  head: 12
  pre-existing MODIFIED: []
  ADDED: ['tests/test_p2_grassmann_crossing_sign.py']
  REMOVED: []
```

### A8 — the frozen six-path manifest, reported in full

```text
base: 9609677576b6d0d77a0813c93673aed81b0c4d5f
head: <the report commit>
mode: exact
add:
  specs/2026-08-07T1159Z_grassmann-crossing-sign.md
  derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md
  scripts/p2_grassmann_crossing_sign.py
  results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
  tests/test_p2_grassmann_crossing_sign.py
  reports/2026-08-07T1159Z_grassmann-crossing-sign.md
forbidden_operations:
  delete, rename, copy, type_change, unmerged, unknown
```

All six are additions. The scope-checker JSON at the committed head is
post-report evidence.

---

## 8. A9-pre — validators at the pre-report head

```text
A9-pre — validators at the pre-report head 787a858ed62370df0b9a5aa27fddbf5b0dc47774
$ git rev-parse HEAD
787a858ed62370df0b9a5aa27fddbf5b0dc47774
$ git status --porcelain (before)
[end]
$ python --version
Python 3.11.15
$ python -m pytest --version
pytest 9.1.1
----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_repository_structure.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 4 items

tests/test_repository_structure.py ....                                  [100%]

============================== 4 passed in 0.02s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.26 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_si1_governance.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 14 items

tests/test_si1_governance.py ..............                              [100%]

============================== 14 passed in 0.04s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.23 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_gate_anchors.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 20 items / 2 deselected / 18 selected

tests/test_gate_anchors.py ..................                            [100%]

======================= 18 passed, 2 deselected in 5.76s =======================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 6.04 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_governance_tools.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 8 items

tests/test_governance_tools.py ........                                  [100%]

============================== 8 passed in 1.22s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 1.40 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_grassmann_crossing_sign.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 15 items

tests/test_p2_grassmann_crossing_sign.py ...............                 [100%]

============================== 15 passed in 0.44s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.70 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_channel_freeze_phase_a.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 3 items

tests/test_channel_freeze_phase_a.py ...                                 [100%]

============================== 3 passed in 0.69s ===============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 0.86 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_channel_freeze_mutations.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gbt
--- complete stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/gw-pre
configfile: pyproject.toml
collected 18 items

tests/test_channel_freeze_mutations.py ..................                [100%]

============================== 18 passed in 1.89s ==============================
[end stdout]
--- complete stderr:
[end stderr]
--- exit status: 0
--- wall time: 2.13 s

$ git status --porcelain (after)
[end]
```

All seven reached genuine exit 0 with tests collected and run; none
reported "no tests ran". `python -m pytest` throughout, as the
specification requires. **The two freeze suites are included as
regression evidence that this branch changed no freeze behaviour**, and
they pass unchanged.

---

## 9. What follows for the `P2-PHASE-01` induced V and A coefficients

**Sign only.** Their magnitude and structure are already established
there and are neither restated nor re-derived here.

`s_G = -1` is now established. **That does not by itself flip the
`P2-PHASE-01` induced V and A coefficients**, because whether the frozen
matrix already carries that factor is precisely the storage question
that §4 reports as unresolved. Concretely:

- if the freeze intends `K_exch = M . K_direct`, the reported values
  stand;
- if it intends `K_exch = s_G . M . K_direct`, they acquire the factor
  `s_G = -1`.

**The sign therefore remains contingent, and this task narrows the
contingency from two unknowns to one.** Before, neither the value of
`s_G` nor the storage convention was established; now `s_G` is fixed by
calculation and only the storage convention is open. Resolving it is a
PI decision on the freeze, not a computation.

---

## 10. Stops and clarifications

**No stop occurred.** No pinned digest mismatched, no command that reads
or alters repository state produced an unexpected result, and every
convention this calculation needed was declared — so the
"undeclared convention" stop of §2 of the specification did not arise.

### 10.1 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the storage convention

§4. Reported with the inspected text quoted, not resolved, and
explicitly not inferred from numerical equality. **This is the outcome
the specification anticipated as satisfactory.**

### 10.2 `REPOSITORY_DEFECT` — the sign is declared but unenforced

Carried forward and now confirmed by direct substitution (§6): the sole
consumer applies the scalar twice, so the declared value cannot affect
any result, and no mutation covers the field. **Not acted on** — the
tenth mutation is a separate task, and this report takes no view on how
the checker should be corrected.

### 10.3 `OBSERVATION_METHOD_ERROR` — my note and my script named different decompositions

The derivation note (commit 2) lists the three-step decomposition
`psi_2` past `psibar_3`, then `psi_2` past `psi_4`, then `psi_4` past
`psibar_3`. The script's selection sort independently found a different
three-step route. **Both are valid decompositions of the same
permutation and both give `-1`**, but the note described a route the
script did not execute.

**Corrected by adding the note's route to the script as a second explicit
calculation** rather than by amending the note, so the report now shows
four independent routes agreeing. The note remains as committed; nothing
was rewritten. The discrepancy was in my description, never in the
result.

### 10.4 `ENVIRONMENT` — two pytest versions, nothing installed

`pytest` resolves to 9.0.2 on `PATH`, `python -m pytest` to 9.1.1. The
specification fixes the latter and every run used it. Nothing was
installed and no configuration changed.

### 10.5 Secondary finding, not acted on

The A7 sweep confirms `derivations/CANONICAL_INTERACTION.json` is
untouched. Its erroneous `vocabulary.gamma5` entry, ruled on by the PI on
2026-08-07 and recorded as a `REPOSITORY_DEFECT` in the previous task,
remains open and out of scope here.

---

## 11. Ambiguous, unsatisfiable, or what I would have specified differently

- **Freezing the permutation was the decisive design choice.** The
  previous task could not resolve this because "one exchange of the
  fermion legs" does not fix a sign — the answer depends entirely on the
  starting and ending orderings. By naming both orderings the
  specification made the question well-posed, and it then had exactly one
  answer. **This is worth generalising: any future specification asking
  for a Grassmann sign should name both orderings, never the exchange.**
- **Separating A3a from A3b was correct and I would keep it.** They look
  like one question and are two: one is an algebraic fact, the other a
  representation convention. Fusing them is how the earlier draft reached
  a wrong inference.
- **The explicit warning against inferring storage from numerical
  equality earned its place.** That inference is superficially
  compelling — an unsigned reconstruction matching all 25 entries feels
  like proof — and I would have been at risk of making it had the
  specification not named it and forbidden it. I added a test asserting
  the disclaimer so the prohibition is mechanically visible rather than
  only stated.
- **A5 is a strong criterion in a small package.** "Confirm by direct
  substitution that the expression is invariant" converts an argument
  about scalars and transposes into two printed outputs a reviewer can
  compare in one glance. More criteria should be written that way.
- **The chiral check's stated expectation was well handled.** Being told
  the expected answer *and* told that a disagreement would be the
  evidence removes the incentive to reproduce it. My result agrees, and
  I would have reported disagreement had I found it.
- **One thing I would add.** The specification pins
  `basis_freeze_check.py` and both freeze test files as inputs, which is
  right. It could also have pinned `scripts/P2-CHANNEL-FREEZE/vocab_parser.py`,
  which contains `parse_grassmann_sign` — the function that validates the
  field's well-formedness and is the other half of "how the sign is
  consumed". I read it and report that it accepts exactly `+-1`, but it
  was not under a digest.
