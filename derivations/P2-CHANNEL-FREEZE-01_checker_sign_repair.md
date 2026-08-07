# Derivation note — `P2-CHANNEL-FREEZE-01`: repairing the checker's sign handling

**Kind:** a repair note for validation machinery. It fixes the reasoning
**before the code is changed**, per `AGENTS.md` rule 3, so the argument
is reviewable independently of the diff that follows.

**This changes no frozen data and no scientific result.** The Phase-A
freeze, its `matrix_rational`, the `fierz_matrix.json` companion and its
sidecar, `vocab_parser.py`, and the freeze mutation suite are all
untouched. What changes is a checker's internal arithmetic and the
coverage of one consumer.

Authority: `specs/2026-08-07T1424Z_freeze-checker-sign-repair.md`.

---

## 0. Frozen inputs

Verified by SHA-256 against the specification's pins before any use, at
evidence base `236f71c69ef9abec33ef0d808724ce80af037710`:

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

All six matched. The freeze declares `grassmann_crossing_sign: "-1"`.

## 1. What the code does now

In `basis_freeze_check.py`, inside `verify()`:

    crossing = _crossing_pair_map()
    sign = parse_grassmann_sign(conventions["grassmann_crossing_sign"])
    # The frozen matrix is a coefficient-row action; dualising the computed
    # pair-space column action supplies its exact, typed orientation.
    computed_fierz = (sign * projector * crossing * embedding).T * sign
    frozen_fierz = _matrix_from_strings(c_block["matrix_rational"])
    require(computed_fierz == frozen_fierz, "computed Fierz matrix mismatch")

`sign` is a SymPy scalar `Integer(±1)`. Transposition does not act on a
scalar factor: `(s·X).T = s·(X.T)`. So the expression is

    (s · projector · crossing · embedding).T · s
      = s · (projector · crossing · embedding).T · s
      = s² · (projector · crossing · embedding).T
      = (projector · crossing · embedding).T          since s² = 1

for either admissible declared value. The two occurrences cancel
identically. `computed_fierz` — and therefore the `require` that
compares it with the frozen matrix — is **blind to the declared sign**.

The count of applications is therefore **zero in effect and two in
appearance**. The appearance is the problem: a reader sees the field
being consumed and reasonably concludes it is being validated.

## 2. Why the repair applies the sign zero times, not once

The tempting reading is that the double application is an off-by-one and
the fix is to apply the sign once. **That reading is wrong**, for a
reason about what this checker is for.

`basis_freeze_check.py` validates a **stored table**. It reconstructs
the Dirac/internal exchange matrix from the frozen basis, the frozen
normalisations and the frozen crossing permutation, and asserts that the
reconstruction equals the tabulated `matrix_rational`. The question it
answers is "are the frozen entries the right numbers?"

The Grassmann crossing sign answers a **different** question. It is not
a property of the Dirac/internal algebra at all — it is the parity of
the fermionic reordering that occurs when two `psi` legs are exchanged
inside a four-fermion monomial. It belongs to the passage from the
matrix to the operator, not to the matrix.

Under the PI ruling of 2026-08-07, recorded in `DECISION_LOG.md`,
`matrix_rational` is stored **unsigned**, and

    K_exch = s_G · M · K_direct ,      s_G = -1

with `s_G` applied **exactly once, at operator use**. `M` is what this
checker validates. `s_G` is applied downstream of it.

So the correct count for this checker is **zero**. Applying the sign
once would make `computed_fierz` differ from the stored `matrix_rational`
by an overall `-1`, `require(computed_fierz == frozen_fierz)` would
fail, and the only way to make it pass again would be to negate every
entry of a hash-pinned frozen artifact — changing frozen data to
accommodate a change in validation machinery. That is exactly backwards,
and this note records the reasoning so the temptation is not revisited.

**The sign is not irrelevant.** It is what turns the matrix-level
induced coefficients `V: +G/4`, `A: +G/4` of `P2-PHASE-01` into the
operator-level `V: -G/4`, `A: -G/4`. It is load-bearing — one layer
down from this checker. The precise statement is: *the crossing sign is
irrelevant to what `basis_freeze_check.py` validates, because that
checker validates the unsigned stored matrix; it is load-bearing at
operator use.*

## 3. The edit leaves `computed_fierz` unchanged

Because the two factors already cancelled, removing both changes
nothing. This is checked, not assumed. Rebuilding `projector`,
`crossing` and `embedding` with the checker's own helpers and evaluating
both forms gives, in exact rationals,

    (s·projector·crossing·embedding).T·s   and   (projector·crossing·embedding).T

    [  1/4   1/4   1/4   1/4   1/4 ]
    [  1/4   1/4  -1/4  -1/4   1/4 ]
    [    1    -1  -1/2   1/2     0 ]
    [    1    -1   1/2  -1/2     0 ]
    [  3/2   3/2     0     0  -1/2 ]

equal in all 25 entries, and both equal to the frozen `matrix_rational`.
Had they differed, the premise of this repair would have been wrong and
the task would stop; they do not.

## 4. The parse stays

`parse_grassmann_sign` continues to be called on
`conventions["grassmann_crossing_sign"]`, and its result continues to be
required to be well formed. Removing the call would be a **regression**:
well-formedness checking is the one legitimate thing this checker does
with the field, and it is the only place the freeze's declared value is
mechanically examined at all.

## 5. `vocab_parser.py`'s role, and its limit

`scripts/P2-CHANNEL-FREEZE/vocab_parser.py` holds the parser:

    def parse_grassmann_sign(text: str) -> sp.Integer:
        value = scalar_ast(parse(text))
        if value not in {sp.Integer(-1), sp.Integer(1)}:
            raise ParseError("invalid grassmann crossing sign")
        return value

It parses the declared text through the frozen vocabulary and admits
exactly the two values `-1` and `+1`.

**What it catches:** a malformed or out-of-range declaration — `0`, `2`,
`-1/2`, `1.5`, an empty string, a symbol outside the frozen vocabulary.
Each raises `ParseError`.

**What it cannot catch:** a *wrong but admissible* declaration. `+1` is
well formed, so `parse_grassmann_sign("1")` returns `Integer(1)`
without complaint. Well-formedness is not correctness, and no amount of
parser strictness can supply the difference — the parser has no access
to the exchange calculation that determines which of the two values is
right.

This is why the coverage for a flipped declaration cannot live in the
parser either, and must live at the layer that computes `s_G`.

**This section is documentation.** `vocab_parser.py` is not modified.
Its omission from earlier pin lists, despite holding the function that
consumes the field, is recorded as a finding rather than repaired here;
this note and the accompanying specification both pin it.

## 6. Where the coverage goes, and why not the mutation suite

`tests/test_channel_freeze_mutations.py` drives
`test_checker_rejects_each_frozen_data_corruption` from a `MUTATIONS`
list. Every entry asserts that corrupting one piece of frozen data makes
the checker **reject**.

A `grassmann` entry would assert that flipping the declared sign makes
`basis_freeze_check.py` fail. After the repair — and, in effect, before
it — the checker does not fail, and *should* not: it validates the
unsigned stored matrix, which does not depend on that field. Adding the
entry would demand a rejection that must not happen. **It would encode
the defect as a requirement.** `MUTATIONS` is therefore left exactly as
it is, deliberately.

The coverage belongs at the operator layer, in
`scripts/p2_grassmann_crossing_sign.py`, which computes `s_G` by
explicit anticommutation and then compares it against the declared
value:

    "declared_grassmann_crossing_sign": DECLARED_CROSSING_SIGN,
    "s_G_equals_declared_value": bool(sign == DECLARED_CROSSING_SIGN),

That comparison is the one place in the repository where a computed
crossing sign meets a declared one. A test in
`tests/test_p2_grassmann_crossing_sign.py` supplies a flipped
declaration through the module attribute the production code reads, runs
the production `main()`, and asserts that the production comparison
reports the mismatch — while the computed `s_G` stays `-1`, showing the
verdict comes from the comparison and not from the calculation.

The artifact destination is redirected to a temporary path for the same
run, so no repository file is written even transiently. The flip is
supplied to the consumer only; **the freeze is not edited, at any point,
in any form.**

## 7. Residual gap, stated plainly

`DECLARED_CROSSING_SIGN = -1` is a **literal in
`scripts/p2_grassmann_crossing_sign.py`**, not a value read from the
freeze. The new test therefore covers "the consumer's declared constant
disagrees with the computed sign". It does **not** cover "the freeze
document's `grassmann_crossing_sign` field was flipped": such a flip
would not reach this comparison, because no consumer reads that field
and compares it against a computed `s_G`.

Closing that gap means making the consumer read the freeze, which is
outside this task's authorised paths. It is recorded here and in the
report as a residual finding, not silently left implied.

## 8. What this note does not do

It registers no gate, changes no status, and selects no convention. It
does not restate or re-derive `s_G`, which was established by four
independent routes in
`derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md` and is
taken as given here. `P2-CHANNEL-FREEZE-01` remains `PROPOSED`.
