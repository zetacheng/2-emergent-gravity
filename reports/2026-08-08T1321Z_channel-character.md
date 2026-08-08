# Execution report — channel character of the Fierz-induced interaction

Authority: `specs/2026-08-08T1321Z_channel-character.md`
Evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`
Branch: `gate/p2-channel-character`
Classification: MATERIAL. Branch only; no merge, no PR.

**Both deliverables are derivations.** No gate is registered, no status
changed, no Hubbard–Stratonovich channel selected, no charge-conjugation
convention selected. **`P2-PHASE-01` remains `PROPOSED`.** `OPEN-AC-1`
is untouched.

Written at head `163513b229161f9c45cff6fe51ecaf4a5f10a999`; it contains
neither its own commit SHA nor the final branch head.

---

## 1. The scalar control, first

Everything downstream depends on it, so it is reported before any other
result.

**Calibrated against the operator `P2-GAP-01` actually used**, quoted
from the pinned note:

    "See `CONVENTIONS.md`. Euclidean `d=4`; attractive scalar (`ψ̄ψ`) channel;"
    ""NJL" normalization `L_int = G_N(ψ̄ψ)²`, one has `G = 4 G_N` and the gap"

Singlet-projecting the frozen canonical interaction into that same
operator, using only the frozen `lam(0) = sqrt(2/N)·Id_N`:

    operator                     (psibar psi)**2
    internal normalisation       lam(0) = sqrt(2/N) Id_N, frozen
    factor-of-two convention     G_GAP = 4 * G_N, absorbing trace(Id4) = 4
    G_N from the frozen singlet  G/N**2
    G_GAP from the frozen singlet 4*G/N**2
    sign of G_N                  +1
    control_passes               True

**Same operator, same internal normalisation, same factor-of-two
convention, positive sign — matching `P2-GAP-01`'s attractive scalar
channel. The Layer-1a control passes, so no STOP arose.**

**What the control does not test**, recorded so it is not over-read: it
does not re-derive `G_c = 1/(2 I_0)` for the generator-sum interaction.
`P2-GAP-01` worked from the singlet-only `L_int = G_N (psibar psi)²`;
the mean-field combinatorics of the full `U(N)` generator sum were not
performed there and are not performed here. The control tests the
operator, the normalisation map and the sign — which is what A2 gates
on — not the full combinatorial chain.

## 2. A1 — pinned inputs

Read from the git objects at the evidence base, not from a worktree. All
seven matched; **no STOP.**

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9   MATCH
    derivations/CANONICAL_INTERACTION.md
      27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81   MATCH
    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
      c7e5744c9744780b6eb205c08ff9b65393e0055d7ebf04f2e0fc406d028edeb5   MATCH
    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
      9bf14f51cc1fbdf4523debe70ad91164bc6d9c96d75f3450b7bce6d43514ec1d   MATCH
    derivations/P2-PHASE-01_fierz_sign_addendum.md
      a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df   MATCH
    derivations/P2-GAP-01_gap_criticality.md
      17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00   MATCH

## 3. A3 — Layer 1a. Unconditional.

**Normalisation is stated before any number**, because a coefficient is
meaningless without the operator it multiplies. Two normalisations are
carried side by side and never mixed:

    normalisation L :  coefficient of  (psibar lam(0) Gamma psi)^2
    normalisation P :  coefficient of  (psibar Gamma psi)^2
    relation        :  c_P = (2/N) * c_L,  from lam(0) = sqrt(2/N) Id_N

**Computed by the script, not asserted.** The chain, with every step
read from the frozen material:

    canonical coefficient read from the freeze's interaction_decomposition
                                          G/(2*N)     (both supported families)
    v_canonical           [G/(2*N), G/(2*N), 0, 0, 0]
    v_frozen after the mandatory (I*gamma5)^2 = -(gamma5)^2 conversion
                          [G/(2*N), -G/(2*N), 0, 0, 0]
    dirac row after the frozen matrix     [0, 0, 1/2, 1/2, 0]
    s_G applied exactly once at operator use              -1

Result:

    channel                     normalisation L   normalisation P   sign
    scalar singlet (direct)         +G/(2*N)         +G/N**2         +1
    induced V singlet (operator)      -G/4           -G/(2*N)        -1
    induced A singlet (operator)      -G/4           -G/(2*N)        -1
    induced S, P, T                     0                0            0

**The scalar coefficient is positive; the induced V and A coefficients
are negative. This is unconditional** — it needs no knowledge of how the
expression enters the Euclidean exponent, and it stands whatever the
later layers do. The sign is the same in both normalisations, so it is
not an artefact of either.

### 3.1 A normalisation observation on the exploratory pairing

The authority's exploratory calculation pairs the scalar singlet as
`+G/N²` with the induced vector singlet as `−G/4`. **Both values are
correct, but they are stated in different normalisations**: `+G/N²` is
normalisation P and `−G/4` is normalisation L. In a single normalisation
the pair is `(+G/(2N), −G/4)` or `(+G/N², −G/(2N))`.

**The sign conclusion is unaffected**, which is why this is recorded as
an observation rather than a disagreement. The magnitudes as paired are
not directly comparable, and a later reader comparing them would draw a
wrong ratio.

## 4. A3a — Layer 1b. Withheld.

The HS identity `exp[(g/2)J²] = ∫dΦ exp[−Φ²/(2g) + ΦJ]` converges only
for `g > 0`, and `g` is an exponent-level quantity, not `2c`.

**The search of the frozen material**, over the seven pinned files plus
`CONVENTIONS.md`, for `S_E`, `Euclidean action`, `Wick`, `Boltzmann`,
`L_E`, `S_int`, `exp(-`, `exp[-`, `e^{-`, `action density`,
`Lagrangian`, `enters the exponent`:

    S_E  2      Wick  1      Euclidean action  1      all others  0
    explicit_L_to_S_E_mapping_found : False

Everything it found, quoted:

- `CONVENTIONS.md`, "Sign of the action": *"Euclidean action `S_E ≥ 0`;
  `Z = ∫ e^{−S_E}`, effective action `W = −ln Z`."*
- `CONVENTIONS.md`, "Wick rotation": *"All loop integrals performed in
  Euclidean signature."*

These fix the **form** of the Boltzmann weight. Neither says which term
of which functional the canonical four-fermion expression is.

**Against that**, `CANONICAL_INTERACTION.md` §2 writes *"The canonical
action:"* and then

    L = Σ_a ψ̄_a (iγ^μ ∂_μ) ψ_a + (G/2N) Σ_A [S^A² + P^A²]

with a **Minkowski** kinetic operator `iγ^μ∂_μ`, while every convention
governing the algebra — including the freeze's own `metric_signature
(1,1,1,1)` — is **Euclidean**. **No Wick-rotation rule connecting the two
is recorded anywhere in the frozen material.**

### **Verdict: `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL`.**

**Both branches are reported, because one of them is inconsistent with
what the repository has already executed:**

    branch (i)  expression already in the exponent,  g = +2c
        scalar   g = +2*G/N**2   > 0    real linear HS field admissible
        V and A  g = -G/N        < 0    no real linear HS field

    branch (ii) expression is a term of S_E,         g = -2c
        scalar   g = -2*G/N**2   < 0    no real linear HS field
        V and A  g = +G/N        > 0    real linear HS field admissible

**Branch (ii) contradicts `P2-GAP-01`'s executed calculation**, which
introduces a *real* scalar auxiliary `Σ` for the attractive scalar
channel and obtains `G_c = 1/(2 I_0)`. A scalar channel with `g < 0`
admits no real linear HS field, so branch (ii) cannot be the convention
that calculation operated under.

**This is an inference from usage, not a frozen definition, and the
artifact labels it so.** It does not resolve the layer; the verdict
above stands. **Fixing the mapping is a PI decision this report informs
and does not take.**

## 5. A3b — Layer 2. Withheld.

"Attractive" and "repulsive" are claims about two-body forces and bound
states. **Real-HS admissibility is not the same statement**: a negative
`g` forces an imaginary HS contour, which is not by itself the absence
of an interaction in that channel. Layer 2 needs the exponent mapping
**and** a criterion tying a coefficient's sign to a force label.

The frozen material supplies two **anchor points** and no general
criterion:

- `CONVENTIONS.md`, "Definition of attractive and repulsive channels":
  *"Scalar (`ψ̄ψ`) condensate channel is the attractive channel driving
  the gap; the four-fermion coupling `G > 0` is attractive there."*
  This labels **one** channel; it states no rule mapping an arbitrary
  channel's coefficient sign to a label.
- `CANONICAL_INTERACTION.md` §3 and §7(b): the vector-singlet Fierz image
  `G_ω = −G/N` recorded as **repulsive**, and the classification
  *"`G_V < 0` repulsive/ω survives"*. That is a second anchor of the same
  sign convention — but it is a **recorded Paper-3 claim**, its source
  note `derivations/u3-fierz/u3_fierz.md` is **not present in this
  repository** (verified: the directory does not exist), and
  `CANONICAL_INTERACTION.md` carries a DRAFT v0.5 banner reading
  *"Nothing here has governing force until the ratification record
  replaces this banner"*.

Since Layer 1b is withheld, **Layer 2 is withheld:
`ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.**

**Conditionally** — under branch (i), the only branch consistent with
`P2-GAP-01`'s executed real-auxiliary treatment, and reading the two
anchors as a common sign convention — the induced singlet V and A would
be **repulsive** and the scalar **attractive**. That is a conditional
consequence, not this report's verdict.

### 5.1 `U''(0)` is not offered as corroboration

For the bare quadratic term `U(Φ) = Φ²/(2g)`, `U''(0) = 1/g` — the
Layer-1b sign test restated in other symbols. For the fermion-integrated
effective potential `U''(0) = 1/g − Π(0)`, whose sign **changes with the
coupling**: an attractive scalar channel still has `U''(0) > 0` below
`G_c`. **`attractive ⇔ U''(0) > 0` is false**, and no curvature is
offered anywhere in this work as evidence for a force label.

## 6. A4 — convention dependence

The Layer-1a signs depend on: the Euclidean `metric_signature (1,1,1,1)`
with Hermitian gammas, which fixes the frozen Fierz matrix; the
mandatory `(I*gamma5)² = −(gamma5)²` basis conversion, without which the
induced coefficients carry a wrong pseudoscalar sign while every
matrix-level check still passes; and the 2026-08-07 ruling that
`matrix_rational` is stored unsigned with `s_G = −1` applied exactly once
at operator use.

**If the `s_G` ruling were reversed** — `matrix_rational` held to store
the sign already, so no further factor at operator use — then

    induced V singlet   -G/4     ->   +G/4      (normalisation L)
    induced A singlet   -G/4     ->   +G/4
                        -G/(2N)  ->   +G/(2N)   (normalisation P)
    scalar singlet      unchanged: it is direct, not Fierz-induced

**Every sign statement about the induced channels reverses**, and with it
the conditional Layer-2 reading of §5. The **structural** results are
untouched: `S`, `P` and `T` still vanish; `V` and `A` remain equal and
purely singlet; the exchanged form remains purely left-right, because an
overall sign multiplies all four chiral coefficients equally.

## 7. A5 — diquark executability

Worked through the authority's four ordered steps, in order, and not
stopped at the first.

**Step 1 — is `C` fixed by the frozen material? No.** Searching the seven
pinned files plus `CONVENTIONS.md`:

    charge conjugation 0   charge-conjugation 0   conjugation matrix 0
    psi^c 0   psi_c 0   diquark 0   particle-particle 0   particle–particle 0

**The null result is auditable, not asserted.** A case-insensitive `c *=`
search returns six hits; all six are lowercase `c` — `G_c` in
`P2-GAP-01` lines 30, 53, 67, `c = 8` at line 90, `c=8` at line 109, and
the `I_0` row of `CONVENTIONS.md`. None concerns charge conjugation. A
case-sensitive search for a standalone capital `C` returns nothing.

**Step 2 — does the defining relation fix `C` up to a scalar? Yes, and
this is computed.** `C γ_μ^T C⁻¹ = −γ_μ`, equivalently
`C γ_μ^T + γ_μ C = 0`, is a linear system on the sixteen entries of `C`
in the frozen Euclidean representation. Its solution space has **complex
dimension exactly 1**, so every admissible `C` is `λC₀` for one nonzero
complex `λ`, with no further discrete freedom. The representative

    [ 0   1   0   0 ]
    [-1   0   0   0 ]
    [ 0   0   0  -1 ]
    [ 0   0   1   0 ]

satisfies the defining relation for all four `μ`, is antisymmetric
(`Cᵀ = −C`), is unitary (`C†C = Id4`), and has `det C = 1`.

**Step 3 — does the residual scalar affect the channel character? No.**
A particle–particle pairing puts `C` and `C⁻¹` in the two conjugate
factors, one each, so the Dirac structure carries `λ⁺¹λ⁻¹ = 1`. Verified
by substitution: `(λC) γ_μ^T (λC)⁻¹ = C γ_μ^T C⁻¹` for all `μ`.
**The absence of a frozen `C` is therefore NOT the obstruction.**

**Step 0 — the obstruction is here.** The remaining pp operator
definitions are not frozen:

- **the charge-conjugated field definition.** In Euclidean signature `ψ`
  and `ψ̄` are independent Grassmann variables, so `ψ̄^c` is not derivable
  from `ψ^c` by conjugation — it must be *defined*. The sign/phase `η` in
  `ψ̄^c = η ψᵀC⁻¹` appears **once** in the paired product, so it
  **flips the coefficient sign** for `η = −1`. Nothing fixes `η`.
- **the pp Grassmann ordering.** The freeze fixes `compound_index_order
  [dirac_family, internal_family, component]` and a crossing sign for the
  *particle–hole* exchange `(α,β,γ,δ) → (α,δ,γ,β)`. A particle–particle
  pairing is a **different permutation**, and no ordering convention is
  frozen for it.
- **the diquark operator normalisation.** Not stated anywhere.

### **Step 4 verdict: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`**,

reached at step 4 and not before, with the dependence shown: the pp
channel character is invariant under the residual freedom in `C` but is
**not** invariant under the un-frozen `η`.

**No `C` was selected and no pp projection was constructed.** Building
one would require supplying exactly the conventions step 0 shows to be
missing. The authority records an earlier exploratory diquark projection
that returned zero in all four families and treats it as a failed
attempt rather than a finding; **it was not repeated.**

**A blocked (b) does not block (a)**, and (a) is delivered in full.

## 8. What this narrows for `OPEN-AC-1` — evidence, not a recommendation

Stated as findings. **No channel is selected; `OPEN-AC-1` is the PI's.**

1. **Layer 1a is unconditional and is now on the record**: scalar
   positive, induced V and A negative, in both normalisations, with
   `S`, `P`, `T` exactly zero.
2. **The set of channels admitting a real linear auxiliary field is
   complementary between the two exponent branches.** Under branch (i)
   the scalar admits one and V/A do not; under branch (ii) exactly the
   reverse. So `OPEN-AC-1` cannot be narrowed by real-HS admissibility
   until the exponent mapping is fixed — **and fixing that mapping is a
   smaller, sharper decision than choosing a channel.**
3. **One branch is already excluded by executed work**, not by argument:
   branch (ii) would have denied `P2-GAP-01` the real `Σ` it used.
4. **The T channel carries exactly zero induced coefficient**, so no HS
   field is induced there by this rearrangement at this order. That is a
   result, not an omission.
5. **The particle–particle channel is not eliminated — it is
   unevaluated.** §7 shows why, and shows that the missing piece is three
   named conventions, not a calculation.

**Nothing here says a composite vector is excluded.** This computes the
sign of the induced singlet V and A in the *particle–hole* rearrangement
only. A repulsive `ψ̄γ_μψ` channel would not by itself exclude a bound
state in another channel, and the particle–particle channel — the one
where such a question would naturally be asked — is precisely the one
this task could not evaluate.

## 9. Was an exit code, tool failure or missing convention treated as a negative result?

**No — and the question was checked deliberately at each of the three
places it could have happened.**

1. **The missing exponent mapping (§4).** A search returning zero hits is
   a *failure to observe a definition*, not evidence that the mapping is
   `−2c`. It is reported as `NOT DEFINED BY THE FROZEN MATERIAL`, with
   both branches carried forward, rather than defaulted to either.
2. **The missing `C` (§7).** Step 1's zero hits are reported as "not
   fixed by the frozen material", **not** as "no `C` exists" — and steps
   2–3 then showed a `C` does exist and is unique up to a scalar. Had the
   null search been treated as a negative result, the task would have
   stopped at step 1 and discarded a real, computable finding.
3. **The missing pp conventions (§7, step 0).** Reported as an
   unevaluated channel, not as a channel with a zero or absent
   coefficient. The authority's own record of an exploratory projection
   returning zero in all four families is exactly the shape of error this
   avoids: an implausible zero from a construction resting on supplied
   conventions.

**One genuine tool-invocation event occurred and is recorded in §11,
Finding 1** — `ruff` exited 1 on two `E501` diagnostics in a file I had
just authored. That is a real lint failure in my own code, correctly
treated as such and fixed; it is not an instance of the pattern above,
and I note it here only so the two are not conflated.

## 10. A6 — fixed-string check

Over the artifacts authored by this task and **excluding the committed
specification**, which necessarily contains these terms in its own
prohibitions. **The result differs depending on whether this report is
itself in scope, and both runs are given.**

**Run A — the four non-report artifacts** (derivation note, script,
results artifact, test file):

    "we choose"            0 hits
    "we select"            0 hits
    "the HS channel is"    0 hits
    "Paper 3 is excluded"  0 hits
    "no composite vector"  0 hits
    TOTAL                  0

**Run B — the same four plus this report**, which is also an authored
artifact: **exactly one hit per string, five in total.** Each is the
corresponding row of Run A's table immediately above — this section
quoting its own search string. Each hit's sentence is therefore a line
of the form *string, then a count of zero* — a report of a search, not
an assertion of the thing searched for.

**A check that documents its own string list cannot avoid matching
itself**, and the strings were not reworded to evade the match, because
the specification says the count is not to be driven to zero. **The
Run-B count is a fixed point of its own reporting**: printing a second
table of per-string counts would have made it ten, so this section prints
the table once and states Run B's result in prose. Run A's zero is the
number that carries information; Run B's five is an artefact of the
report describing the check.

**No hit anywhere asserts.** The nearest substantive phrasings this work
contains are disclaimers, worded so as not to match at all: *"No `C` was
selected"*, *"No channel is selected"*, *"Nothing here says a composite
vector is excluded"*, *"the particle–particle channel is not eliminated —
it is unevaluated"*.

An earlier draft of this section reported "Total: 0 hits" on the strength
of Run A alone, before this report existed to be scanned. **That was
correct for the four artifacts and wrong as a statement about the
authored set**, and it is corrected here rather than left standing; the
post-report re-run is returned with the post-report evidence.

## 11. A8 — nothing pre-existing disturbed

Blob OIDs read from the objects at the evidence base:

    GATES.md        bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md  2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md       5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml  9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL

No gate, gate status, verdict, artifact digest, hash-pinned artifact or
pre-existing test was modified; the base-to-head change list contains
additions only (§13).

### Repository inputs actually read, by path

Recorded in the artifact and reproduced here:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    derivations/CANONICAL_INTERACTION.md
    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
    derivations/P2-PHASE-01_fierz_sign_addendum.md
    derivations/P2-GAP-01_gap_criticality.md
    CONVENTIONS.md
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py

**None of the three prohibited sources appears**: the quarantined
`−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and the historical
Finding 5 extraction were **NOT READ**. A test asserts the recorded list
matches the script's declaration, that every listed path exists, and that
no path contains `BETAV-CIRC`, `3.2(5)`, `Finding 5` or `finding_5`.

## 12. A7 — deliverables, and A10-pre, A11

### 12.1 Deliverables

    derivations/P2-PHASE-01_channel_character.md               derivation note
    scripts/p2_channel_character.py                            script
    results/P2-PHASE-01/channel-character/channel_character.json  results artifact
    tests/test_p2_channel_character.py                         23 tests
    reports/2026-08-08T1321Z_channel-character.md              this report

**The tests follow the three layers and stop where the layers stop.**
Layer 1a is tested for its computed values and signs in both
normalisations; Layer 1b is tested for being *correctly withheld* and for
the conditional branch arithmetic — that the two branches differ by a
sign in every channel, and that branch (ii) is the one inconsistent with
`P2-GAP-01` — never for a resolved admissibility; Layer 2 likewise. The
diquark tests assert the null search, the one-dimensional solution space,
the defining relation, the residual-scalar invariance, and that no
convention was selected. **No test asserts a quantity this specification
permits to be undefined.**

The artifact is **byte-reproducible**: two consecutive runs gave
`093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f` both
times, and the A11 lint fix (a line-wrap and a moved comment) left it
unchanged.

### 12.2 A10-pre, at head `163513b2`

    $ python -m pytest tests/test_repository_structure.py        ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py              -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py                -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py            ->  8 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py -> 14 passed              exit 0
    $ python -m pytest tests/test_p2_grassmann_crossing_sign.py  -> 19 passed              exit 0
    $ python -m pytest tests/test_p2_channel_character.py        -> 23 passed              exit 0

All seven exit 0. Exit statuses were captured from `python -m pytest`
itself, not from the tail of a pipeline. `pytest` on `PATH` is 9.0.2 and
`python -m pytest` is 9.1.1 on this host; the specification mandates the
latter and that is what was run.

### 12.3 A11 — lint

    $ ruff --version
    ruff 0.15.8
    $ ruff check scripts/p2_channel_character.py tests/test_p2_channel_character.py
    All checks passed!
    === exit 0 ===

Run from the repository root so `[tool.ruff]` applies (`line-length = 88`,
`select = ["E", "F", "I"]`). Only the two Python files this task authored
were linted; the three Markdown files are not Python. Pre-existing
diagnostics elsewhere were not touched.

## 13. A9 — scope

### 13.1 Manifest template

Held with a `{PUSHED_HEAD}` placeholder so its digest does not depend on
the report commit. SHA-256:
`43f1925ce5c23dd7df18ab2cf35b5418e51002777d78476a48dfc823619a8230`.

    {
      "base": "eb88a2c9174cfda746c266924e741a6f88134234",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-08T1321Z_channel-character.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_channel_character.md"},
        {"operation": "add", "path": "scripts/p2_channel_character.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/channel-character/channel_character.json"},
        {"operation": "add", "path": "tests/test_p2_channel_character.py"},
        {"operation": "add", "path": "reports/2026-08-08T1321Z_channel-character.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Six additions, zero modifications**, matching A9. The `{HHMM}` token
resolved to `1321` at commit 1 and is reused throughout. The resolved
manifest, its SHA-256 and the checker JSON at the pushed head are
post-report evidence.

### 13.2 Pre-report scope check

At head `163513b2`, where the report commit does not yet exist, so five
additions rather than six:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "eb88a2c9174cfda746c266924e741a6f88134234",
      "failures": [],
      "head": "163513b229161f9c45cff6fe51ecaf4a5f10a999",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-PHASE-01_channel_character.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/channel-character/channel_character.json"
        },
        {
          "operation": "add",
          "path": "scripts/p2_channel_character.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-08T1321Z_channel-character.md"
        },
        {
          "operation": "add",
          "path": "tests/test_p2_channel_character.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` empty, no forbidden operation, **zero modifications** — which
for this task is the criterion that matters, since nothing pre-existing
may move.

## 14. A12 — branch only

    refs/remotes/origin/main   eb88a2c9174cfda746c266924e741a6f88134234
    remote refs/heads/main     eb88a2c9174cfda746c266924e741a6f88134234
    local main                 0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)

**Local `main` was not repaired**, as instructed. `gate/p2-channel-character`
was created from `eb88a2c9…` in a separate worktree; the primary worktree
was not touched. **No branch was deleted or renamed.** No merge, no PR,
no force-push, no history rewrite.

## 15. Stops and clarifications

**Stops: none.** A1 matched on all seven pins and the scalar Layer-1a
control passed, so neither STOP condition fired. The Layer-1b and Layer-2
withholdings are **satisfactory outcomes under A2/A3a/A3b**, not stops.

**Finding 1 — `OBSERVATION_METHOD_ERROR`, mine, caught by the tool.**
`ruff check` exited 1 on two `E501` diagnostics (89 and 91 columns) in
`scripts/p2_channel_character.py`, one a long path constant and one a
trailing comment. Both were in code I had just written; both were fixed
by a line-wrap and a moved comment. **The results artifact was re-run and
is byte-identical**, confirming the fix was cosmetic. Recorded because
A11 is a criterion and a first-attempt failure against it is a fact, not
something to present as having passed first time.

**Finding 2 — `REPOSITORY_DEFECT`, pre-existing, not repaired here.**
`derivations/CANONICAL_INTERACTION.md` §2 states the canonical
interaction as a Lagrangian with the **Minkowski** kinetic operator
`iγ^μ∂_μ`, while `CONVENTIONS.md` and the Phase-A freeze mandate
**Euclidean** signature throughout, and **no Wick-rotation rule
connecting them is recorded**. This is the direct cause of the Layer-1b
withholding: the governing source writes the action in one signature and
the algebra is done in another, with no stated bridge. **Fixing it is a
governance task, not this one**, and the file is a frozen pinned input
here.

**Finding 3 — `REPOSITORY_DEFECT`, pre-existing, secondary.**
`CANONICAL_INTERACTION.md` carries a DRAFT v0.5 banner reading *"Nothing
here has governing force until the ratification record replaces this
banner"* **and**, at its foot, a completed ratification record. Both
cannot be operative. This matters for Layer 2: §7(b)'s `G_V < 0`
repulsive classification is one of only two anchor points available, and
its governing force is ambiguous on the document's own terms.

**Finding 4 — secondary, an unresolved numerical comparison.**
`CANONICAL_INTERACTION.md` §3 records the vector-singlet Fierz image as
`G_ω = −G/N`. This task's induced V singlet is `−G/(2N)` in
normalisation P and `−G/4` in normalisation L; neither equals `−G/N` for
general `N`. **The signs agree; the magnitudes do not**, and the
discrepancy cannot be resolved here because the source note
`derivations/u3-fierz/u3_fierz.md` is at a Paper-3 commit and **is not
present in this repository** (verified: the directory does not exist).
The most likely explanation is a different definition of what `G_ω`
multiplies — the same normalisation trap as §3.1 — but **I did not verify
that and am not asserting it.** Flagged for the PI.

**Clarification 1 — the branch-(ii) exclusion is an inference from
usage.** §4 reports that branch (ii) contradicts `P2-GAP-01`'s executed
real-`Σ` treatment. That is a statement about what the repository has
*done*, not about what it has *defined*, and it is labelled as such in
both the artifact and the derivation note. **It does not convert Layer 1b
into a resolved layer**, and I have deliberately not written the verdict
as though it did.

**Clarification 2 — `CONVENTIONS.md` was read but is not in A1's pin
list.** It carries both the `Z = ∫e^{−S_E}` entry and the "Definition of
attractive and repulsive channels" entry, which are the two most
load-bearing quotations in §4 and §5. It is recorded in the artifact's
`repository_inputs_read` and its blob is verified unchanged (§11). I note
the omission from A1 because a file this decisive to the outcome would
normally be pinned.

**Clarification 3 — `scripts/P2-CHANNEL-FREEZE/gamma_algebra.py` was
imported** to build the frozen Euclidean gamma matrices for §7, rather
than constructing a representation myself. It is recorded as a
repository input. Using the repository's own factory avoids introducing
a representation convention that is not frozen.

## 16. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A12 were met as written. The
three-layer structure in particular was satisfiable exactly because it
permits withholding — an earlier framing that demanded the HS sign
unconditionally would not have been.

Three things I would have specified differently:

**(a) `CONVENTIONS.md` should be in A1's pin list.** Clarification 2. Two
of its rows carry the whole weight of Layers 1b and 2. A task whose
verdict turns on a file's exact wording should pin that file's digest.

**(b) A6's fixed-string list cannot distinguish assertion from
disclaimer, and the specification knows it** — it says so, and asks for
sentences. That is the right call, but it means the check's value is
entirely in the reading, not the count. I would add one string that is
hard to write innocently, such as `is excluded`, precisely because a hit
would then demand explanation rather than being trivially absent. As
specified, all five returned zero, which tells the Reviewer less than a
hit would have.

**(c) §3's step ordering lists step 0 last-but-first.** The steps are
numbered `0,1,2,3,4` and the text says "work through these in order",
but step 0 is the one that ultimately decides, and it is stated after the
`C`-specific steps in the surrounding prose. I worked 1→2→3→0→4, which is
the order in which the evidence actually accumulates, and reported it
that way. Naming that order explicitly would remove the ambiguity.

One thing I would keep exactly as written: **the instruction to continue
past step 1 rather than stopping at the absent `C`.** Stopping there
would have produced "unresolved, no convention frozen" — true but nearly
useless. Continuing produced the actually useful result: `C` is unique up
to a scalar, that scalar cancels, and the real obstruction is three
*other* conventions, one of which is a single sign. **That turns an open
question into a specific, small decision the PI can take.**

## 17. Commits, and commit-message hygiene

**Commit 1** — `3f48afdc6332e2fb3c3bbe02847cf88fa2bda1d3`

    spec: channel character of the Fierz-induced interaction

    Records the PI specification for the channel-character derivation,
    evidence base eb88a2c9174cfda746c266924e741a6f88134234, transcribed
    verbatim.

    Derivation (a) reports the character of the induced singlet V and A in
    three layers that must not be collapsed: the frozen algebraic
    coefficient, unconditional; the exponent-level Hubbard-Stratonovich
    coefficient, conditional on a mapping that may not be frozen; and the
    physical attractive/repulsive label, which needs more than the second.
    The scalar channel is a control calibrated against the operator and
    normalisation P2-GAP-01 actually used.

    Derivation (b) is an executability determination for the diquark
    channel, to be worked through four ordered steps rather than stopped at
    the absence of a frozen charge-conjugation matrix.

    Neither deliverable selects a Hubbard-Stratonovich channel; OPEN-AC-1
    remains the PI's. P2-PHASE-01 remains PROPOSED.

**Commit 2** — `9c26b0945056fd18c68a9768173afe2957ae7813`

    derivation: channel character of the induced V and A, in three layers

    Fixes the analytic content before any production code, per AGENTS.md
    rule 3.

    Layer 1a is unconditional: with G > 0 the scalar singlet coefficient is
    positive and the induced V and A singlet coefficients are negative, in
    both of the two normalisations the note keeps explicitly apart. The
    scalar control passes against the operator, internal normalisation and
    factor-of-two convention P2-GAP-01 actually used.

    Layer 1b is withheld. CONVENTIONS.md fixes Z = integral exp(-S_E) but
    nothing states whether the canonical four-fermion expression is a term
    of S_E or already sits in the exponent, and the one document that writes
    the action writes it with a Minkowski kinetic operator while the algebra
    is Euclidean, with no Wick rule recorded. Both branches are reported;
    one is inconsistent with P2-GAP-01's executed real-auxiliary treatment,
    recorded as an inference from usage rather than a definition.

    Layer 2 is withheld in consequence.

    For the diquark channel the note reaches step 4. The defining relation
    fixes C up to a single complex scalar, computed, and that scalar cancels
    between the paired conjugate factors. The obstruction is step 0: the
    charge-conjugated field convention, the particle-particle Grassmann
    ordering and the diquark normalisation are unfrozen, and the first of
    them flips the sign. No C is selected and no projection is built.

**Commit 3** — `163513b229161f9c45cff6fe51ecaf4a5f10a999`

    feat: compute the channel character of the induced V and A in three layers

    Adds the script, the results artifact and the test file for the
    P2-PHASE-01 channel-character derivation.

    Layer 1a is computed from the frozen material rather than asserted: the
    per-family coefficient G/(2*N) is read from the freeze's
    interaction_decomposition, the mandatory I*gamma5 conversion is applied,
    the frozen matrix acts on the converted vector, and s_G is applied once
    at operator use. Scalar +G/(2*N), induced V and A -G/4 in the lam(0)
    normalisation; +G/N**2 and -G/(2*N) in the plain one. The scalar control
    against P2-GAP-01's operator, internal normalisation and factor-of-two
    convention passes with a positive coefficient.

    Layer 1b is withheld and Layer 2 with it, each with the search that
    established the withholding. Both exponent branches are reported; the
    branch that would forbid a real scalar auxiliary is flagged as
    inconsistent with P2-GAP-01's executed treatment, as an inference from
    usage rather than a definition.

    For the diquark channel the script solves the defining relation as a
    linear system, finds the solution space to be one complex dimension, and
    verifies that the residual scalar cancels between the paired conjugate
    factors. The obstruction is the unfrozen charge-conjugated field
    convention, which flips the sign. No C is selected and no projection is
    constructed.

    The artifact is byte-reproducible across runs.

**Intended report commit message** (commit 4):

    docs: report the channel character of the Fierz-induced interaction

    Records A1-A12 for the three-layer channel-character derivation and the
    diquark executability determination.

    The scalar Layer-1a control passes against P2-GAP-01's operator and
    normalisation. Layer 1a is unconditional: scalar positive, induced V and
    A negative, in both normalisations, with S, P and T exactly zero. Layer
    1b is withheld as REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN
    MATERIAL, and Layer 2 with it, each with its search. The diquark
    determination reaches step 4: C is unique up to a scalar that cancels,
    and the obstruction is three unfrozen particle-particle conventions.

    Also records that the exploratory pairing quotes its two coefficients in
    different normalisations, and two pre-existing defects in
    CANONICAL_INTERACTION.md that bear on the withheld layers.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this branch
by composing the message in a file and committing with `git commit -F`,
never with `-m`.

    commit 1  3f48afdc   suppressed: Co-Authored-By, Claude-Session
    commit 2  9c26b094   suppressed: Co-Authored-By, Claude-Session
    commit 3  163513b2   suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)   suppression applied identically; stored message
                         read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` matched nothing in either form, for all three commits.

**Suppression is a fact disclosed here, not an absence** — a convention
that would have added the trailers was deliberately bypassed.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
