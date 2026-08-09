# Execution report — land the attraction/repulsion ruling and recompute Layer 1b and Layer 2

Specification: `specs/2026-08-09T0300Z_attraction-ruling-and-layers.md`
Specification evidence base: `3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`
Branch: `gate/p2-attraction-ruling-and-layers`
Pre-report head: `61d165b58951664be5a71affc45bd28b950194e5`

**Outcome.** The ruling is landed. Both withheld layers are recomputed
and both gating controls pass. The scalar singlet is `ATTRACTIVE`; the
induced V and A singlets are `REPULSIVE`. No gate is registered, no
status is changed, no frozen or pinned artifact is modified, no
Hubbard–Stratonovich channel is selected, no diquark convention is
frozen, and the programme registry is untouched.

**One thing the Reviewer should read before the results**, because it
bears on how much the recomputation is worth: §12 answers whether any
acceptance criterion here could have been satisfied by a computation
that never used the ruling. The short answer is that **A4 could, and
A5–A7 could have been satisfied by an implementation that hard-coded
the same numbers.** What forces consumption is a design choice, not a
criterion.

---

## 1. A15 — refs, read from the remote

    refs/remotes/origin/main    3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    remote refs/heads/main      3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b
    local refs/heads/main       0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both remote refs resolve to the specification's base. **Local `main` is
stale by design and was not repaired.** The branch was created from
`3b3d3b2e…` in a separate worktree; no `main` ref was moved.

`review/role-model-and-executors` remains at
`10c260b96882ac12610f78840aeeabd07be2d7cb`. **No branch was deleted.**

## 2. A1 — pinned inputs, verified before use

Digests taken from the git objects at the base and from the working
tree; all four matched the specification, and the two readings agree.

    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f   MATCH
    results/P2-PHASE-01/channel-character/channel_character.json
      093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f   MATCH
    scripts/p2_channel_character.py
      521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126   MATCH
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH

The script re-verifies all four at run time and refuses to proceed on a
mismatch, so the artifact cannot be produced from unpinned inputs.

## 3. A2 — the exponent mapping ruling, located on `main`

Found in `DECISION_LOG.md` on `3b3d3b2e…` at line 1236, as a single
top-level entry:

    ## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent

    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: supplies a convention absent from the frozen material

with, inside the verbatim ruling text:

    > it enters the Euclidean action with a minus sign:
    >
    >     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
    >
    > Consequently, for a channel whose coefficient in `X` is written
    > `c * J**2`, the Hubbard–Stratonovich coefficient is
    >
    >     g = +2c

**The premise holds; no stop.**

## 4. A3 — the ruling recorded

One new top-level `DECISION_LOG.md` entry at line 1393:

    ## 2026-08-08 — Attraction/repulsion sign convention: the label is assigned to the sign of g

The substantive ruling text of §0 is reproduced **verbatim**: the 46
lines of the specification's blockquote were copied programmatically and
compared line by line against the source after insertion —
**identical, 46/46**. Structural metadata (`Date:`,
`Decision owner:`, `Effect:`, and the `### Reason`,
`### Consequences`, `### Related gate`, `### Related branch and files`
sections the file's format requires) was added around it, not inside it.

### 4.1 Append-only

    git diff --numstat 3b3d3b2e…61d165b… -- DECISION_LOG.md
      126     0       DECISION_LOG.md

    deleted lines (diff lines matching ^-[^-]):  0

**126 lines added, zero deleted.** The file grew from 1391 to 1517
lines.

### 4.2 The required phrases, checked against normalised text

Normalisation applied, all four steps: blockquote markers `> ` stripped;
`**` and backticks stripped; all whitespace collapsed to single spaces;
en dashes left alone. The en dash in `Hubbard–Stratonovich` was
confirmed to be `U+2013` on both sides of the comparison.

    PASS  count=1  'Date: 2026-08-08'
    PASS  count=1  'Decision owner: Principal Investigator'
    PASS  count=1  'g > 0 is labelled ATTRACTIVE'
    PASS  count=1  'The naming is not derived from Hubbard–Stratonovich admissibility'
    PASS  count=1  'The two are a chain, not independent constraints'
    PASS  count=1  'REPULSIVE in a'
    PASS  count=1  'is not a pole calculation'
    PASS  count=1  'It is not a derivation'
    ALL PRESENT: True

**All eight are inside the verbatim ruling text**, not in the metadata I
wrote around it. `Date:` and `Decision owner:` are the exceptions and
are metadata by construction.

### 4.3 The entry, quoted

    ## 2026-08-08 — Attraction/repulsion sign convention: the label is assigned to the sign of g

    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: supplies a convention absent from the frozen material

    ### Decision

    The PI ruling of 2026-08-08, reproduced verbatim:

    > **PI ruling, 2026-08-08 — attraction/repulsion sign convention.**
    >
    > Under the Euclidean exponent mapping ruling of the same date, a channel
    > whose Hubbard–Stratonovich coefficient satisfies **`g > 0` is labelled
    > ATTRACTIVE**; **`g < 0` is labelled REPULSIVE**.
    >
    > **The basis, in three separated steps.** Under the Euclidean exponent
    > mapping, a channel term with coefficient `g` appears as
    > `exp(+(g/2)J²)`. For `g > 0` the standard linear
    > Hubbard–Stratonovich representation uses a real Gaussian auxiliary
    > field; for `g < 0` that real contour is not available — **that is the
    > algebraic fact.** **The programme adopts ATTRACTIVE as the label for
    > the `g > 0` sign and REPULSIVE for the `g < 0` sign** — that is the
    > convention. This is consistent with `P2-GAP-01`'s description of its
    > positive-coupling scalar channel as attractive — that is the
    > consistency check. **The naming is not derived from
    > Hubbard–Stratonovich admissibility; it is assigned to that sign.**
    >
    > **`J = ψ̄Γψ` is a Grassmann composite.** Before bosonisation there is
    > no c-number configuration space on which "larger `|J|`" can be
    > compared pointwise, so **no appeal to enhanced configurations is made
    > here.** An earlier formulation did make one and was wrong to.
    >
    > **This ruling depends on the exponent mapping ruling of the same
    > date.** If that mapping were reversed, every channel's `g` reverses
    > and so does every label this ruling assigns. **The two are a chain,
    > not independent constraints**, and neither is derived from the frozen
    > material.
    >
    > **Scope limit.** The label characterises the sign of the interaction
    > in the specified Hubbard–Stratonovich channel. It is conventionally
    > associated with an attractive or repulsive tendency in that channel;
    > **it does not establish that condensation actually occurs.** Whether
    > it does depends on the full quadratic kernel — `Γ⁽²⁾(0) = 1/g − Π(0)`
    > — the fermion determinant, stability, and the critical coupling.
    > **Nor does it by itself establish the existence or absence of a
    > two-body bound state, resonance, or composite excitation.**
    >
    > **In particular: REPULSIVE in a `ψ̄ψ` channel does NOT imply that a
    > composite vector is absent.** That question requires its own
    > bound-state or pole analysis, and may also involve a differently
    > paired channel. **A channel-character label is not a pole
    > calculation.**
    >
    > **This supplies a convention for the item currently recorded in the
    > programme registry as `NOT DEFINED`. It is not a derivation.**

The `### Reason` and `### Consequences` sections follow in the file.
They record why the ruling was needed, that the withdrawn
enhanced-configurations argument is withdrawn rather than quietly
dropped, that the registry row is deliberately **not** changed here, and
that no gate status changes.

## 5. A4 — the Layer 1a control. Gating, and it passes.

**Method.** The recomputation imports the pinned
`scripts/p2_channel_character.py` by file location and re-executes its
`layer_1a()`, which reads the frozen basis block and the frozen
`matrix_rational` from the freeze document and from
`results/P2-CHANNEL-FREEZE/fierz_matrix.json`. Every coefficient is then
compared to the pinned `channel_character.json` as an **exact symbolic
difference**, in both normalisations, with `sympy`.

    channel                   field             recomputed      pinned    difference
    scalar_singlet_direct     normalisation_L      G/(2*N)     G/(2*N)             0
    scalar_singlet_direct     normalisation_P       G/N**2      G/N**2             0
    induced_V_singlet         normalisation_L         -G/4        -G/4             0
    induced_V_singlet         normalisation_P     -G/(2*N)    -G/(2*N)             0
    induced_A_singlet         normalisation_L         -G/4        -G/4             0
    induced_A_singlet         normalisation_P     -G/(2*N)    -G/(2*N)             0

    signs: +1 / +1, -1 / -1, -1 / -1        control_passes: True

**No stop.** Everything below is a function of these `c`.

## 6. A5 — Layer 1b

**Basis cited:** `DECISION_LOG.md` entry
`## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent`,
statement found `g = +2c`, factor `+2`.

    channel                     c_L         c_P          g_L         g_P    sign(g)  real HS
    scalar_singlet_direct   G/(2*N)      G/N**2          G/N    2*G/N**2       +1      yes
    induced_V_singlet          -G/4    -G/(2*N)         -G/2        -G/N       -1       no
    induced_A_singlet          -G/4    -G/(2*N)         -G/2        -G/N       -1       no

**`g` is computed, not asserted.** The factor is parsed out of the
`DECISION_LOG.md` entry at run time and multiplied into the verified `c`
symbolically. The values were not written into the script.

**"Real HS" means the Gaussian integral converges** — whether the
standard linear representation with a *real* auxiliary field is
available. A `no` is not the absence of an interaction in the channel,
and it is not a statement about two-body forces.

**Cross-check against the pinned artifact.** The pinned derivation
computed both possible mappings as branches without choosing between
them. Its branch (i), `weight carries exp[+c J^2]; g = +2c`, carries
`g_in_normalisation_P` values `2*G/N**2`, `-G/N`, `-G/N` for the scalar,
V and A. **These agree exactly with the table above.** The ruling did
not change the arithmetic; it chose which of the two arithmetics is the
programme's. See §12 — this is directly relevant to whether the ruling
was consumed.

**The sign is the same in either normalisation**, checked rather than
assumed: `c_P = (2/N) c_L` with `N > 0` cannot move a sign, and the
script raises if it ever did.

## 7. A6 — Layer 2

**Basis cited:** `DECISION_LOG.md` entry
`## 2026-08-08 — Attraction/repulsion sign convention: the label is assigned to the sign of g`,
statements found `g > 0 is labelled ATTRACTIVE` and
`g < 0 is labelled REPULSIVE`.

    channel                   sign(g)     label
    scalar_singlet_direct        +1     ATTRACTIVE
    induced_V_singlet            -1     REPULSIVE
    induced_A_singlet            -1     REPULSIVE

**Cited as basis, not as derivation.** The ruling assigns a name to a
sign. Nothing in this section is derived from the frozen material, and
every label here reverses if the exponent mapping is reversed — which
the tests demonstrate rather than assert.

**Scope, carried in the artifact:** the label characterises the sign of
the interaction in the specified channel. It does not establish that
condensation occurs — that depends on the full quadratic kernel, the
fermion determinant, stability and the critical coupling — and it
establishes nothing about the existence or absence of a two-body bound
state, resonance or composite excitation.

## 8. A7 — the scalar control. Gating, and it passes.

    gate                P2-GAP-01
    expected label      ATTRACTIVE
    observed label      ATTRACTIVE
    control_passes      True

`P2-GAP-01` describes its positive-coupling scalar channel as
attractive; the scalar singlet here has `c > 0`, hence `g > 0`, hence
the positive-sign label. **No stop.**

**What the control does not test.** It does not re-derive
`G_c = 1/(2·I_0)` and does not lift `P2-GAP-01` to the generator-sum
interaction. `G_c` does not enter this computation at any point, and no
reconciliation with it was attempted.

## 9. A8 — the diquark channel, restated

**This task does not touch it, and the channel picture is not
complete.** From the pinned artifact, unchanged:

    all particle-particle operator definitions fixed        False
      eta in psibar^c = eta psi^T C^-1                      not frozen
      particle-particle Grassmann ordering                  not frozen
      diquark operator normalisation                        not frozen

The obstruction is not the charge-conjugation matrix `C`: the pinned
derivation showed the defining relation fixes `C` up to a nonzero scalar
and that the scalar cancels in the paired product. It is `η`, which
appears once in the paired product and flips the coefficient sign.

**The two rulings consumed here do not unblock it.** They supply an
exponent mapping and a sign-to-label rule; neither is a
particle–particle operator definition.

## 10. A9 — fixed-string check

Scanned, per the specification, over the artifacts authored here
**excluding the committed specification**: the derivation note, the
script, the results artifact, the test file, and this report.

    string                          note  script  json  tests  report  total
    composite vector is excluded       0       0     0      0       1      1
    no composite vector                0       0     0      0       1      1
    rules out                          0       0     0      0       1      1
    we choose                          0       0     0      0       1      1
    the HS channel is                  0       0     0      0       1      1

**Every hit is in the table above**, in the column that names the string
being searched for. Each is the check reporting itself and asserts
nothing. Classification: **all five are legitimate; none is an
assertion.**

**On the four non-report artifacts the count is genuinely zero, and I
did not reword anything to make it so.** The required disclaimers are
present and are phrased in their own words:

- the derivation note, §6: "A repulsive label in a `ψ̄ψ` channel does not
  settle whether a composite vector exists", with the reason given;
- the results artifact, field `composite_vector`: "no statement is made
  about whether a composite vector exists. A channel-character label is
  not a bound-state or pole calculation, and the ruling forbids that
  inference explicitly."

Neither uses any of the five strings, because neither needs to. **The
disclaimers were written before this check was run**, not adjusted after
it.

**This table is a fixed point of its own reporting.** Writing it puts
each string into the report exactly once; running the check again over
the committed report reproduces the counts above unchanged. That is
stated rather than hidden, because a reader comparing a re-run against
this table deserves to know why the report's column is not zero.

**`DECISION_LOG.md` is not in the specification's list** and so is not
counted in the table. Scanned separately, the entry I authored contains
none of the five strings either; its own disclaimer is the ruling's
"does NOT imply that a composite vector is absent", which is not among
them.

## 11. `OPEN-AC-1` — what this narrows, as evidence

**Stated as evidence, not as a recommendation. No
Hubbard–Stratonovich channel is selected here, and the selection is the
PI's.**

Of the three particle-hole channels computed:

    admits a real linear auxiliary field       scalar_singlet_direct
    does not                                   induced_V_singlet
                                               induced_A_singlet

**What that narrows.** If a channel is to be bosonised by the standard
linear Hubbard–Stratonovich transformation with a real Gaussian
auxiliary field, then among these three only the scalar singlet
currently supports it under the landed mapping. That is a statement
about the availability of one representation.

**What it does not narrow.** It says nothing about the
particle–particle channel, which is not computed and remains blocked
(§9). It does not establish that a negative-`g` channel is inert, since
a rotated contour or a different representation is a separate question
this task did not examine. And it is conditional on both rulings: under
the reversed mapping the admissible set becomes the V and A singlets
instead, which the tests exhibit explicitly.

## 12. Would any acceptance criterion have been satisfiable without the ruling?

**Asked by the specification's report contract, and the honest answer is
uncomfortable, so it is given in full.**

**A4 does not use either ruling at all.** The Layer-1a control is a
comparison of the pinned `layer_1a()` against the pinned artifact. It
would pass identically if `DECISION_LOG.md` did not exist. That is by
design — it is a control — but it should not be counted as evidence that
the ruling was consumed.

**A5, A6 and A7 depend on the rulings for their values, but not for
their satisfaction.** An implementation that simply wrote
`g = 2 * c` and `{+1: "ATTRACTIVE", -1: "REPULSIVE"}` as literals would
have produced byte-identical layer values and labels, passed A5's
"computed by the script rather than asserted" (the arithmetic would
still be computed), passed A10's "`g = 2c` computed rather than
hard-coded" (the multiplication would still be performed), and cited the
rulings in prose. **Nothing in the criteria as written would have caught
it.**

**This is sharpened by a fact in §6:** the pinned artifact already
contained branch (i), whose `g` values are exactly the ones reported
here. A recomputation could have read them straight out of the pinned
JSON. The ruling's contribution is not the arithmetic — it is the
selection of which branch is the programme's.

**What was done instead, and why it is not merely decoration.** The
implementation locates each ruling in `DECISION_LOG.md` by its exact
heading, parses the mapping factor out of the ruling's own text with
`\bg\s*=\s*([+-]?)\s*2\s*c\b`, and parses both halves of the
sign-to-label rule out of the label ruling's normalised text. The
consequences are executed and tested:

    removing the exponent mapping entry            run stops
    removing the label ruling entry                run stops
    a mapping entry stating no relation            run stops
    a ruling labelling only one sign of g          run stops
    reversing the mapping to g = -2c               every g flips;
                                                   labels become
                                                   REPULSIVE / ATTRACTIVE
                                                   / ATTRACTIVE;
                                                   real-HS admissibility
                                                   inverts;
                                                   and main() then stops
                                                   on the scalar control
    swapping the two labels in the ruling          the reported labels swap

Six tests, all passing. **The outputs demonstrably move with the
rulings, and vanish without them.** But that is a property of the
implementation, freely chosen — **not something any acceptance criterion
required.** If regression-locking the *consumption* of a ruling, and not
only its recorded values, is to be a programme habit, it needs to be
written into the criteria.

## 13. A11 — nothing pre-existing disturbed

Blob hashes read from the git objects at base and at the pre-report
head:

    GATES.md                                             bd48205…  IDENTICAL
    CONVENTIONS.md                                       2d4f735…  IDENTICAL
    AGENTS.md                                            5e60b5f…  IDENTICAL
    pyproject.toml                                       9fc6fdd…  IDENTICAL
    derivations/CANONICAL_INTERACTION.md                 6e5d9e1…  IDENTICAL
    derivations/P2-GAP-01_gap_criticality.md             70b4383…  IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md    0be773f…  IDENTICAL
    derivations/P2-PHASE-01_channel_character.md         4b9e190…  IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json          5c3d572…  IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256   601a5db…  IDENTICAL
    results/P2-PHASE-01/channel-character/…json          e0fcdbb…  IDENTICAL
    scripts/p2_channel_character.py                      569543e…  IDENTICAL

`GATES.md` `^## P2-` anchor count: **14 before, 14 after.**
`P2-GAP-01` still reads `Status: PASS (continuum exact; lattice I_0
agrees with paper at matched mass)`, with no caveat added.
`P2-PHASE-01` still reads `Status: PROPOSED`.

**`DECISION_LOG.md` is modified by A3 and only by A3** — one appended
entry, 126 lines, zero deletions. No pre-existing test was modified.

## 14. A12 — scope

**Manifest template** (SHA-256
`1072afa5439a3e166ed16929697947b1b6028406008ab957d0527e9ec69ad51c`):

    {
      "base": "3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-09T0300Z_attraction-ruling-and-layers.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_channel_character_layers.md"},
        {"operation": "add", "path": "scripts/p2_channel_character_layers.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/channel-character-layers/layers.json"},
        {"operation": "add", "path": "tests/test_p2_channel_character_layers.py"},
        {"operation": "add", "path": "reports/2026-08-09T0300Z_attraction-ruling-and-layers.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Intended final resolution:** `head` set to the pushed head, all seven
records required, **6 additions and 1 modification**. An eighth path
would be a defect.

**Pre-report scope check**, at `61d165b…` with the report record removed
because the report does not yet exist — checker output verbatim:

    {
      "base": "3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b",
      "failures": [],
      "head": "61d165b58951664be5a71affc45bd28b950194e5",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "DECISION_LOG.md"
        },
        {
          "operation": "add",
          "path": "derivations/P2-PHASE-01_channel_character_layers.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/channel-character-layers/layers.json"
        },
        {
          "operation": "add",
          "path": "scripts/p2_channel_character_layers.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-09T0300Z_attraction-ruling-and-layers.md"
        },
        {
          "operation": "add",
          "path": "tests/test_p2_channel_character_layers.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }

    exit status 0

Raw `git diff --name-status` at the same head, as an independent
reading:

    M   DECISION_LOG.md
    A   derivations/P2-PHASE-01_channel_character_layers.md
    A   results/P2-PHASE-01/channel-character-layers/layers.json
    A   scripts/p2_channel_character_layers.py
    A   specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
    A   tests/test_p2_channel_character_layers.py

**The final scope check at the pushed head is post-report evidence** and
is returned to the Reviewer, not written back here.

## 15. A13-pre — validators at the pre-report head

Run individually with `python -m pytest <path>` — that exact
invocation, since `pytest` on this host resolves to 9.0.2 while
`python -m pytest` resolves to 9.1.1.

    tests/test_repository_structure.py            exit=0    4 passed
    tests/test_si1_governance.py                  exit=0   14 passed
    tests/test_gate_anchors.py                    exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py                exit=0    8 passed
    tests/test_p2_channel_character.py            exit=0   23 passed
    tests/test_p2_generator_sum_criticality.py    exit=0    7 passed
    tests/test_p2_channel_character_layers.py     exit=0   26 passed

`pytest 9.1.1`, Python 3.11.15. **A13-final at the pushed head is
post-report evidence** and carries the verdict.

## 16. A14 — lint

    $ ruff check scripts/p2_channel_character_layers.py tests/test_p2_channel_character_layers.py
    All checks passed!

    exit status 0        ruff 0.15.8

**Those two files only.** The other four authored paths are Markdown and
JSON, which `ruff` does not lint. Two `E501` diagnostics were raised on
an earlier draft of the script and one on the test file; all three were
line-length only and were fixed by rewrapping. The results artifact was
regenerated afterwards and its digest is unchanged at
`fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542`,
confirming the fixes were cosmetic. Pre-existing diagnostics elsewhere
were not touched.

## 17. A10 — deliverables

    derivations/P2-PHASE-01_channel_character_layers.md   derivation note
    scripts/p2_channel_character_layers.py                implementation
    results/P2-PHASE-01/channel-character-layers/layers.json   artifact
      sha256 fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542
    tests/test_p2_channel_character_layers.py             26 tests
    reports/2026-08-09T0300Z_attraction-ruling-and-layers.md   this report

The tests lock the full mapping for all three channels, not only the
scalar control:

    c_S > 0  =>  g_S > 0  =>  ATTRACTIVE      test_scalar_channel_…
    c_V < 0  =>  g_V < 0  =>  REPULSIVE       test_induced_v_channel_…
    c_A < 0  =>  g_A < 0  =>  REPULSIVE       test_induced_a_channel_…

plus the Layer-1a control against the pinned artifact, the pinned
digests, `g = 2c` in both normalisations for every channel, the
normalisation-independence of the sign, and the six mutation tests of
§12.

## 18. A0 — commit order, SHAs and messages

    commit 1  f6f609d2e911724aa341bceb7bd2994d45d51632
              specs/2026-08-09T0300Z_attraction-ruling-and-layers.md
              "docs: record the attraction/repulsion ruling task specification"

    commit 2  7bed9c6d192f5e5b30960e170e58ae6beeb70da0
              DECISION_LOG.md
              "docs: land the attraction/repulsion sign convention ruling"

    commit 3  fb5d91b457f6766c16bd483d13ed177ed151b994
              derivations/P2-PHASE-01_channel_character_layers.md
              "docs: derivation note for Layer 1b and Layer 2 of the channel character"

    commit 4  61d165b58951664be5a71affc45bd28b950194e5
              scripts/…, results/…, tests/…
              "compute: Layer 1b and Layer 2 script, result artifact, and regression test"

**Commit 2 precedes the derivation note**, as required: the note records
a computation that consumes the ruling, and the ruling is in the
repository before the note that cites it. **`{HHMM}Z` was fixed once by
commit 1 as `0300` and reused** for the report path and everywhere the
task is named. Parent 1 of each commit is the commit before it.

**The specification file is byte-identical to the specification as
issued**, with a single trailing newline added because the issued text
did not end in one and every other file in `specs/` does.

### Commit-message hygiene

Each message was written to a file, inspected for
`Co-Authored-By`, `Claude-Session`, `claude.ai`, `Generated with` and
`http` before committing, committed with `git commit -F <file>` and
never `-m`, and the stored message read back from the object afterwards
with `git log -1 --format=%B`.

    commit 1   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   trailers suppressed: Co-Authored-By, Claude-Session
    commit 3   trailers suppressed: Co-Authored-By, Claude-Session
    commit 4   trailers suppressed: Co-Authored-By, Claude-Session

**Suppression is a fact, not an absence.** This harness appends both
trailers by default; `-F` was used precisely to prevent that, and the
read-back confirmed neither reached any stored message. The intended
report commit message is below and was prepared the same way, with the
same two trailers suppressed:

    docs: report the attraction/repulsion ruling and the recomputed layers

    Records the landing of the attraction/repulsion sign convention
    ruling and the recomputation of Layer 1b and Layer 2 of the channel
    character. Both gating controls pass: the Layer-1a control
    reproduces every pinned coefficient as an exact symbolic zero, and
    the scalar singlet comes out ATTRACTIVE against P2-GAP-01.

    Layer 2: ATTRACTIVE for the scalar singlet, REPULSIVE for the
    induced V and A singlets, cited to the ruling as basis and not as
    derivation.

    States explicitly that A4 would have passed without either ruling
    and that A5-A7 would have been satisfiable by a hard-coded
    implementation, and what was done instead.

## 19. Repository inputs actually read, by path

    DECISION_LOG.md
    AGENTS.md
    GATES.md
    CONVENTIONS.md                       (blob hash only, not content)
    derivations/README.md
    derivations/P2-PHASE-01_channel_character.md
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md
    results/P2-PHASE-01/channel-character/channel_character.json
    results/P2-CHANNEL-FREEZE/fierz_matrix.json      (read by the pinned
                                                      layer_1a() at run time)
    scripts/p2_channel_character.py
    scripts/governance_tools/scope_checker.py
    specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md
    specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md
    tests/test_repository_structure.py
    tests/test_p2_channel_character.py

**Exclusions confirmed.** The quarantined `−3.2(5)`, the suspended
`P2-BETAV-CIRC-01` result, and the historical Finding 5 extraction were
**NOT READ**, and the artifact records that.

**Nothing was installed.** `sympy`, `pytest` and `ruff` were already
present.

## 20. Worktree states

    <scratch>/attr        the branch worktree; clean after commit 4,
                          on gate/p2-attraction-ruling-and-layers
    /home/user/2-emergent-gravity
                          the primary worktree; on
                          gate/p2-grassmann-crossing-sign at cf4c789,
                          not touched by this task

No other worktree was altered, and nothing was cleaned, stashed or
discarded anywhere.

## 21. Stops and clarifications

**No stop occurred.** Both gating controls passed and no
specification instruction proved inconsistent with a repository rule.

### `SPECIFICATION_DEFECT`

None.

### `ENVIRONMENT`

None.

### `OBSERVATION_METHOD_ERROR`

None reached an output. One was caught during development and is
recorded because the class of error matters more than this instance:
three mutation tests were first written to drive `main()`, which stops
on the gating scalar control, so a reversed mapping produced a *stop*
rather than an *observation of the flipped labels*. The tests would have
"passed" as stop-tests while never showing that the labels move. They
were rewritten to call the layer functions directly, with a separate
test asserting that `main()` does stop. **A gate that fires can hide the
measurement you were trying to take.**

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

None that blocked execution. Two are recorded as findings in §22.

## 22. Secondary findings, and what I would have specified differently

**1. The rulings are now load-bearing conventions living only in a
chronological log, and my implementation is coupled to their headings.**
The exponent mapping ruling and the label ruling are both consumed by
`scripts/p2_channel_character_layers.py`, which locates them by exact
`##` heading text. That coupling is deliberate — it is what makes the
consumption real and testable — but it means **renaming either heading
breaks the script**. The `CONVENTIONS.md` index entry deferred by
`specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md` §0(b) has
still not been written, and there are now **two** conventions in that
position rather than one. If that index task goes ahead, the two entry
headings should be treated as stable identifiers, or the index should
carry the machine-readable form and the script should read the index.

**2. `A9`'s artifact list omits `DECISION_LOG.md`.** The entry I
authored is an artifact of this task as much as the derivation note is.
I scanned it anyway (§10) and it is clean. I would have named it in the
list, or named the exclusion explicitly the way the specification
excludes the committed specification.

**3. `A5` and `A10` do not require what §12 asks about.** The report
contract asks whether the criteria could be met without consuming the
ruling; the answer is yes, and the criteria are where that would be
fixed. **"Computed rather than hard-coded" constrains the arithmetic,
not the provenance of the constant.** A criterion of the form "removing
the cited ruling from `DECISION_LOG.md` must cause the computation to
fail, demonstrated by a test" would close it. I implemented that, but a
future executor reading only the criteria would not.

**4. The `g = +2c` string is not unique in `DECISION_LOG.md`.** It
occurs three times on the branch head — inside the exponent mapping
ruling's verbatim text and twice in the prose around it. The parser is
unaffected, because it searches only within the located entry, but a
whole-file mutation touches all three. Recorded so a later reader does
not mistake the multiplicity for an error.

**5. Recurring, and raised for the fourth time.** The distinction
between "failure to observe" and "a negative result" — which §21's
`OBSERVATION_METHOD_ERROR` note is another instance of — is currently
re-stated in individual specifications. It belongs in `CONVENTIONS.md`
or `AGENTS.md`, where it would apply without being re-issued each time.
