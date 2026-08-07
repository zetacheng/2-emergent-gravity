# Task specification — two derivations for `P2-PHASE-01`: Fierz-induced channel coefficients, and stationary-branch potential depths

Specification evidence base: `9609677576b6d0d77a0813c93673aed81b0c4d5f`
Required verification target: the same commit.

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Both deliverables are DERIVATIONS. Neither decides anything.** They
supply the evidence needed before two of `P2-PHASE-01`'s open items can
be answered, and they are chosen precisely because they require no
physics decision that has not already been made and frozen.

**`P2-PHASE-01` remains `PROPOSED` and not runnable.** Nothing here
registers a gate, changes a status, adopts a prerequisite draft, or
reaches an admissibility verdict.

**`AGENTS.md` research rule 3 applies:** commit a derivation note before
production code. See A0.

---

## 0. What the frozen material actually says, and what changed

At the evidence base, `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`
records the canonical interaction as

    (G/(2*N))*Sum(bilinear(lam(A),Id4)**2 + bilinear(lam(A),I*gamma5)**2,
                  (A,0,N**2-1))

with `interaction_decomposition` listing **only S and P** as supported.

**A previous draft of this specification asked you to derive the Fierz
rearrangement. That was wrong, and the correction is the point of this
version.** The Phase-A freeze ALREADY contains a complete Fierz
specification: the S/P/V/A/T basis with explicit expressions, the full
conventions block, and a frozen 5×5 `matrix_rational`. A companion
artifact exists at `results/P2-CHANNEL-FREEZE/fierz_matrix.json` with a
recorded digest.

**So the task is VERIFICATION, not derivation.** Re-deriving would
produce a second answer standing beside a frozen one, with no declared
relationship between them — the worst available outcome. Instead you
independently reconstruct the matrix from the declared conventions and
**prove element-by-element equality with the frozen one.**

**The conventions are declared and are NOT yours to choose.** From the
freeze:

    metric_signature:            (1, 1, 1, 1)
    gamma5_definition:           gamma(0)*gamma(1)*gamma(2)*gamma(3)
    sigma_definition:            I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2
    dirac_trace_normalization:   trace(Id4) = 4
    un_generator_normalization:  trace(lam(A)*lam(B)) = 2*KroneckerDelta(A,B)
    grassmann_crossing_sign:     -1
    singlet_traceless_order:     [singlet, traceless]
    compound_index_order:        [dirac_family, internal_family, component]
    basis_order:                 [S, P, V, A, T]

**This settles the λ-algebra question a previous draft left open.** The
generator normalisation is frozen. If you nevertheless find it
insufficient to fix the rearrangement uniquely, that is a finding —
report it and stop derivation (a) — but do not treat the question as
open by default.

**Pinned inputs. Verify each digest before use; any mismatch is a
STOP:**

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

**Also verify the sidecar.** `results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256`
records a digest for that file; check that it agrees with the value
above and with the file's actual committed content. **A sidecar
disagreement is a STOP and a repository finding**, not something to
resolve by preferring one source.

**And cross-check the two copies of the matrix.** The freeze document's
embedded `matrix_rational` and the standalone `fierz_matrix.json` must
agree entry by entry as exact rationals. **If they disagree, STOP** —
which of the two governs would be a governance question, and this task
has no authority to settle it.

    derivations/CANONICAL_INTERACTION.md
    27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81

    derivations/CANONICAL_INTERACTION.json
    f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028

**Authority order, so you never have to choose.** The Phase-A freeze
governs the Fierz basis, conventions and matrix. `CANONICAL_INTERACTION`
governs the interaction expression. `results/P2-CHANNEL-FREEZE/fierz_matrix.json`
is a companion artifact of the freeze and is expected to agree with it.
**If any two of these three disagree on any point, STOP and report the
disagreement; do not reconcile them and do not select a preferred
source.**

## 1. Objective

Paper 2 carries two derivations with machine-checkable results:

**(a)** the Fierz rearrangement of the frozen canonical interaction into
the complete five-family basis, giving each family's induced coefficient
and sign in terms of `G` and `N`, with the algebra verified rather than
asserted;

**(b)** the VALUE of the reduced scalar effective potential at every
stationary branch found by the exploratory study, so that branch depths
can be compared within that single potential.

## 2. Derivation (a) — reconstruct the Fierz matrix and prove equality

**The workflow is two-phase, and the phases are normative.** §0 asks you
to cross-check the two frozen copies of the matrix; this deliverable
asks you not to look at either first. Both are satisfiable, but only in
this order — and the conventions and `matrix_rational` sit in the same
file, so "read the freeze" is not an atomic act.

> **Phase 1 — before independent reconstruction.** Verify only the
> pinned byte digests and the sidecar digest. Read only the declared
> conventions, the basis definitions, the canonical interaction, and the
> internal-generator normalisation. **Do not parse, print, inspect or
> otherwise expose either frozen `matrix_rational`.**
>
> **Blind-result fixation.** Reconstruct the 5×5 matrix independently,
> serialise it to a scratch artifact outside the repository, and
> **record that artifact's SHA-256 before exposing either frozen
> matrix.** Report that digest.
>
> **Phase 2 — only after fixation.** Parse the freeze document's
> embedded `matrix_rational` and the standalone JSON matrix. **First
> compare those two frozen copies to each other**, then compare your
> reconstruction entry-by-entry against them.

**This gives "independent" an auditable chronology instead of an
attestation.** The scratch digest, recorded before exposure, is what
makes the claim checkable.

**Deliverable 1 — independent reconstruction.** From the declared
conventions of §0 and nothing else, construct the 5×5 Fierz matrix
symbolically, as exact rationals, under Phase 1 above.

**Deliverable 2 — element-by-element equality.** Compare your matrix to
the frozen `matrix_rational` **entry by entry as exact rationals, not
numerically and not up to a tolerance.** Report the full 5×5 comparison.

**Any disagreement in any entry is a STOP and a first-class finding.**
Do not adjust your reconstruction to match, and do not adjust the frozen
matrix. A mismatch would mean either the freeze or the conventions are
wrong, and that is a governance matter, not something to smooth over.

**Deliverable 3 — the exchange map, stated explicitly.** Report: which
fermion legs are exchanged; whether Dirac and internal indices are
exchanged jointly or separately; where `grassmann_crossing_sign = -1`
enters; and how `compound_index_order` maps a compound index to
`(dirac_family, internal_family, component)`. **Demonstrate the compound
kernel equality that your matrix asserts**, rather than asserting it.

**Deliverable 4 — induced coefficients, AFTER a mandatory basis
conversion.**

**The canonical interaction and the Fierz basis do not use the same
pseudoscalar.** Verified at the evidence base: the canonical interaction
writes `bilinear(lam(A), I*gamma5)`, while the frozen Fierz family basis
defines `"basis_id":"P","expression":"gamma5"`. At the squared-operator
level this is a sign:

    (bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2

**Conversion is mandatory before the matrix is applied.** Report the
canonical coefficient vector BEFORE conversion, and the coefficient
vector in the frozen `[S,P,V,A,T]` basis AFTER conversion. **Apply the
verified Fierz matrix only to the converted vector.**

**Direct application to an unconverted `(S,P) = (1,1)` vector is
prohibited.** This is the failure this deliverable exists to prevent:
every matrix-level check — reconstruction, equality, involution, trace,
completeness — passes unchanged while the induced coefficients carry a
wrong pseudoscalar sign.

Then report each
family's induced coefficient as an exact expression in `G` and `N`,
**with singlet and traceless pieces reported separately**, per
`singlet_traceless_order`.

**If the frozen 5×5 matrix does not by itself resolve the
singlet/traceless split** — it is a Dirac-family matrix, and the
internal-index decomposition may require the `λ^A` completeness relation
in addition — **derive the split from the declared generator
normalisation and say explicitly that you did, showing the step.** If
the declared material is insufficient to fix it, report the induced
coefficients WITHOUT the split and record the gap as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`. **Do not invent an
internal-index convention.**

**This gap does NOT block derivation (a) or the task.** Deliverables 1,
2, 3, 5 and 6 — the reconstruction, the element-by-element equality
proof, the exchange map, the normalisation checks and the involution —
are all independent of the internal-index split and remain required.
Only the split within Deliverable 4 is affected. **Record the gap,
deliver the unsplit coefficients, and continue**; the STOP conditions of
this task are the digest mismatches, the source disagreements, and a
`matrix_rational` mismatch, not this. **A vanishing coefficient is a result, not an
omission.**

**Deliverable 5 — basis completeness and trace normalisation, verified
explicitly.** These underpin every entry of the matrix and are the two
checks a wrong reconstruction most often passes by accident, so they are
deliverables in their own right rather than assumptions:

- **Completeness:** demonstrate that `{1, γ₅, γ^μ, γ^μγ₅, σ^{μν}}` under
  the declared `gamma5_definition` and `sigma_definition` spans the
  4×4 matrices — sixteen elements, linearly independent, no residual.
- **Trace normalisation:** verify `trace(Id4) = 4` and the orthogonality
  `trace(Γ^a Γ^b) ∝ δ^{ab}` under the declared conventions, reporting
  the proportionality constant per family.
- **Generator normalisation:** verify
  `trace(lam(A) lam(B)) = 2 δ_AB` as declared, and state how the
  `A = 0..N²−1` index set including the singlet enters the completeness
  relation used in the rearrangement.

**Deliverable 6 — involution, as it actually holds.** Apply the
transformation twice and report the outcome for these conventions.
Involution is a property of the specific transformation, not a universal
law. **Report what you find, not what you expected**; if double
application does not return the original, report the exact residual and
**do not adjust the convention to force involution.**

**What you must NOT do, and one inference you must NOT draw:**

- **Do not choose a Hubbard–Stratonovich channel.** That is `OPEN-AC-1`
  and belongs to the PI.
- **Do not choose a V/A/T orientation or component structure.**
- **Do not infer the size of the mean-field ambiguity from the size of
  the bare Fierz coefficients.** They are not the same quantity. The
  mean-field ambiguity depends on which channel is bosonised and on the
  truncation, and it is `P2-FIERZSUM-01`'s subject. **Report the
  coefficients; do not report what they imply about how much the HS
  choice matters.** A previous draft asked for exactly that inference
  and was wrong to.

## 3. Derivation (b) — potential values at each stationary branch

The exploratory results record, per root, `mhat`,
`stationarity_residual`, `reduced_curvature` and `I0` — **but not the
potential value.** Depth cannot be compared without it.

Using the reduced effective potential already reconstructed in
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` — **the same
potential, the same zero, the same conventions; do not construct a new
one** — report for every stationary branch at every scanned coupling:
`M̂`; the potential value; the curvature; and the potential value
relative to the trivial branch `M̂ = 0`.

**Freeze and state the conventions before reporting numbers**, because a
"depth" is meaningless without them: the integration constant or
reference point that fixes the potential's zero; whether values are per
unit volume, per site, or per mode; and the sign convention, i.e.
whether a deeper branch is more negative. **Where the existing
derivation already fixes one of these, cite it; where it does not, that
gap is itself a finding.**

**Specifically, on the additive constant.** If the pinned scalar
derivation does not uniquely fix it, **do not choose one.** Report
`potential_value` as `NOT DEFINED UNDER THE FROZEN MATERIAL`, continue
to report `potential_minus_trivial`, and classify the missing zero as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`. **This does not block the
within-potential depth-difference analysis**, which depends only on
differences: the envelope comparison, the correspondence rule and the
depth resolution all remain required and are computed from
`potential_minus_trivial`.

**This comparison is WITHIN the single reconstructed scalar potential.**
It is legitimate there because all branches share one potential and one
zero. **It says nothing about cross-family comparison**, which requires
a common HS, measure and potential-zero normalisation that is not
frozen — that remains `OPEN-AC-3`. State this limit in the derivation.

**The evaluation domain is frozen HERE, before any result is seen.**
Use exactly the grid/shift set and coupling set of the exploratory
study, taken from its pinned results artifact:

    grids (n, shift):  (32,0.0) (32,0.25) (40,0.0) (40,0.25)
                       (48,0.0) (48,0.25)
    couplings G/G_c:   0.8 0.9 0.98 0.99 1.0 1.01 1.02 1.05
                       1.1 1.2 1.4 1.6 1.8 2.0 2.5 3.0

**Stability is judged across the six grid/shift combinations**, and a
digit counts as stable only if it is unchanged across all six.

**Branch correspondence across grids is fixed here, before any potential
is evaluated.** Without a matching rule, "stable across all six" is
undefined once a coupling has several roots, and you would have to
invent one. The rule, chosen to carry no physical judgement:

> At fixed `G/G_c`, roots are partitioned by sign. `mhat = 0` matches
> only itself. Within each nonzero sign sector, roots are ordered
> monotonically by `mhat`, and equal ordinal positions define
> corresponding branches across grid/shift combinations. **If root
> counts differ between combinations, or the rule does not yield a
> one-to-one correspondence, that branch has UNRESOLVED CROSS-GRID
> CORRESPONDENCE: assign it no stable-digit count and no cross-grid
> depth ordering, and report it as such.**

**Comparisons are made at fixed `G/G_c`, not at fixed absolute `G`.**
`G_c` is grid-dependent, so corresponding points need not share an
absolute `G`; that is expected and is not a discrepancy.

**You may not reduce this domain after seeing results.** If cost forces
a reduction, **decide and record it BEFORE evaluating potentials.** A reduction
announced only in the final report cannot be distinguished from one
chosen afterwards, so it must be committed first.

**This is an authorized amendment to the derivation note, and it is the
only content amendment to it this task permits.** Land it as its own
commit, after commit 2 and **before any commit containing a computed
potential value**:

    commit N   derivations/…_fierz_verification_and_branch_depths.md
               amended: pre-evaluation domain reduction and its reason

The commit message must state that it is a pre-evaluation reduction. The
report must record this commit's SHA and quote the amendment.

**If no reduction is needed, this commit does not exist** and the
derivation note is never amended. **Do not create an empty or
placeholder amendment commit.**

State what you will drop and why, then run. A reduction chosen after
values are in hand can select the couplings at which branches happen to
separate, which is precisely the failure mode this rule prevents.

**If the potential evaluation is materially more expensive than the
root-finding already performed** — for instance because it requires an
integral over `M̂` at every grid point — **report the cost, reduce the
grid set or coupling set as needed, and state precisely what was
reduced and why.** Do not silently drop a control, and do not spend
hours on a convergence sweep whose cost the specification did not
anticipate. A reduced but disclosed control is acceptable; an
undisclosed one is not.

**Report the raw values, not only the ordering.** For each branch at
each coupling give the potential value itself and the numerical
difference from the trivial branch.

**Cross-grid numerical stability is NON-STATISTICAL, and the algorithm
is frozen here.** Grid-to-grid variation is convergence behaviour, not
Gaussian error, and must not be dressed as a statistical uncertainty.

> For each corresponding branch at fixed `G/G_c`, over all grid/shift
> combinations participating in that comparison, let
>
>     V_min   = min(V_i)
>     V_max   = max(V_i)
>     spread  = V_max - V_min
>
> **Report all three.**
>
> **`stable_decimal_places` is bounded above**, because otherwise it is
> undefined whenever the values agree exactly — a trivial branch at
> `V = 0` across all six grids satisfies the condition for every `d`,
> and no largest integer exists.
>
> Let `d_max` be the **minimum number of decimal places explicitly
> stored** for the participating potential values.
> **`stable_decimal_places`** is the largest integer `d` with
> `0 <= d <= d_max` for which all participating values, quantized to `d`
> decimal places, are identical. **If they remain identical through
> `d_max`, report `d_max`.**
>
> **`stable_decimal_places = 0` is ambiguous on its own and must be
> disambiguated by `stability_status`:** it does not by itself assert
> agreement after rounding to zero decimal places. `stability_status`
> records whether agreement exists at `d = 0`, or whether no
> non-negative decimal-place agreement exists at all. **Those are
> different findings and must not share a bare `0`.**
>
> **The rounding rule is frozen, not stated by you.** Convert each
> potential value to a decimal string at its stored precision, then
> quantize with **decimal round-half-to-even
> (`decimal.ROUND_HALF_EVEN`)**. The same rule applies to every grid,
> coupling and branch. **No alternative rounding or truncation rule is
> permitted, and binary-float `round()` is NOT this rule** — go through
> the decimal representation, so that half-way cases such as `1.245`
> and `1.255` cannot resolve differently between implementations.
>
> **Depth ordering uses envelopes, not an inferred error.** Two branches
> are RESOLVED in depth only if their `[V_min, V_max]` intervals are
> DISJOINT. **If the intervals overlap, report them as unresolved in
> depth at the available grid resolution and do not rank them.**

This removes the choices a previous draft left open — decimal places
versus significant digits, rounding versus truncation, max-min versus
half-range versus standard deviation, summed uncertainties versus
interval overlap — each of which could change whether two branches count
as ordered.

**Report the depth ordering as an observation and stop there.** Whether
the deepest branch is the physical ground state, and whether the
negative-mass branch is a physical phase or a doubler sector, is
`OPEN-AC-2` and is not yours to answer. **In particular, do not describe
any branch as "the vacuum", "preferred", "physical", or "an artifact".**

## 4. Acceptance criteria

**A0 — Derivation note before any production code, per `AGENTS.md`
rule 3.** The derivation note is committed under `derivations/` **before
any production code**, and after the specification commit. It is
**commit 2**, not commit 1; the ordering below is normative and
supersedes any reading of this criterion's heading as requiring the note
to be first overall.

**Commit order, stated once so it is not inferred.**

    commit 1  this specification, under specs/    (§5)
    commit 2  the derivation note, under derivations/
    commit 3+ script, results, test file, report

**§5's "commit this specification as commit 1" and rule 3's "derivation
note before production code" are both satisfied by that order**: the
specification is an authority artifact, not production code, so
committing it first does not precede the note in the sense rule 3
governs. The note still precedes every line of production code.

**Where the λ-algebra determination fits.** It is a READ-ONLY inspection
of frozen material, not production code, so perform it **before writing
the note** — after commit 1, before commit 2. **Establish it first, then
write the note recording either the determined algebra or the blocked
finding, then proceed to code.** This avoids writing a note that fixes
conventions for a derivation that turns out not to be executable. It
must fix, before numbers exist: the Fierz conventions and trace
normalisation for (a); the reduced potential and its zero for (b), by
reference to the existing derivation; the checks of §2; and the
convergence controls of §3. **Write it as a derivation, not a plan** —
its purpose is that the analytic content is reviewable before the
numerics can influence it.

**A1 — Frozen material verified.** The canonical interaction and
`interaction_decomposition` at the evidence base are as quoted in §0.
Quote what you find. **Any difference → stop.**

**A2 — Fierz result, with all applicable Deliverables 1–6 of §2
performed and reported**, each with its output. Coefficients exact and symbolic in `G`
and `N`.

**A3 — Involution demonstrated**, not asserted.

**Conditional clause — read this before A6, A8 and A9.** The λ-algebra
question is settled by the frozen `un_generator_normalization` of §0, so
this branch is not expected to trigger. It remains as a safety net: if
you nevertheless find the declared conventions insufficient to fix the
rearrangement uniquely, or a pinned digest mismatches, or the Phase-A
freeze and `CANONICAL_INTERACTION` disagree, then derivation (a) is
blocked. In that case:

- **A2 and A3** are recorded as
  **`NOT EXECUTABLE — BLOCKED`, naming which of the three causes applies**, with the
  precise missing definition and the evidence for that conclusion.
  **That is a satisfactory outcome for those two criteria, not a
  failure.**
- **A6's required tests reduce accordingly:** the involution, trace
  normalisation and sixteen-element completeness tests belong to (a) and
  are recorded as not executable for the same reason. **The potential
  reference-point test remains required**, since (b) still runs.
- **A8's six-path change set stands regardless.** The derivation note
  records both derivations, including (a)'s blocked determination and
  its evidence; the script and results artifact carry (b). **A blocked
  (a) does not remove any path from the manifest** — the note and the
  report must exist either way, and an empty or absent artifact would
  itself be a scope failure.
- **A9's new-test-file requirement stands**, covering whatever (b)
  establishes.

**Both derivations are delivered in one branch under one manifest,
whether or not (a) executes.**

**A4 — Potential values**, per branch per coupling, with convergence
evidence and stable digits identified. **The results artifact records,
per (grid, shift, coupling, branch):** `n`, `shift`, `G_over_Gc`, `G`,
`mhat`, `stationarity_residual`, `potential_value`,
`potential_minus_trivial`, `reduced_curvature`, and the aggregate
stability fields `stability_combinations`, `potential_min_across_grids`,
`potential_max_across_grids`, `potential_spread` and
`stable_decimal_places`. **Where cross-grid correspondence is
unresolved, the aggregate fields are `null` and `stability_status`
records why.** Machine-readable; the report may summarise
it but the artifact carries the numbers.

**If the evaluation domain was reduced under the pre-evaluation
amendment, the artifact records the reduction explicitly**, so a reader
of the JSON alone is not misled about what was evaluated: the grid/shift
and coupling sets actually used; the sets originally frozen in this
specification; and the amendment commit's SHA. **A stable-digit count
derived from fewer than the six frozen grid/shift combinations must be
labelled with the number of combinations it rests on** — a digit
"stable across two grids" is not the same claim as one stable across
six, and the artifact must not let the two read alike.

**A5 — No decision taken, verified rather than declared.** Provide, in
the report:

- a fixed-string check over **the artifacts you author in this task** —
  the derivation note, script, results artifact, test file and report.
  **The derivation note is INCLUDED**, and will legitimately contain
  some of these terms when it states what it does not conclude; that is
  what the context requirement is for. Check for the terms `the vacuum`, `preferred`, `physical phase`,
  `artifact`, `ground state`, and `is the true`, with the count and,
  for any non-zero count, the surrounding sentence, so a reviewer can
  judge each use in context. **Only the committed specification is
  excluded from this scan**, because it necessarily contains these terms
  in its own prohibitions and scanning it would guarantee false
  positives. **No other authored artifact is exempt.**

  **This scan cannot be driven to zero, and must not be.** §3 requires
  the derivation and report to state that they do NOT determine whether
  a branch is the physical ground state, which necessarily contains
  `ground state`; and `OPEN-AC-2` is itself framed as whether the
  negative-mass branch is a physical phase or a doubler artifact, which
  cannot be cited without the words. **Reporting a required abstention
  is a legitimate use.** What the scan exists to expose is a term used
  to ASSERT a characterisation — `the deepest branch is the vacuum`,
  `this branch is preferred` — as against one used to DISCLAIM it.
  Report every hit with its sentence and say which kind it is; **do not
  reword a required abstention to avoid a hit.**
  **A non-zero count is not a failure** — quoting this specification's
  prohibitions, or stating that a branch was NOT characterised as any of
  these, is legitimate. The check exists so a reviewer can judge each
  use, not so the count can be driven to zero;
- an explicit statement, path by path, that no HS channel and no V/A/T
  orientation was selected;
- confirmation from the repository that `GATES.md` and the two
  prerequisite artifacts named here are byte-identical to the evidence
  base. **They are named because "the two prerequisite drafts" is not
  uniquely determined by this specification, and you should not supply
  the reference from memory:**

      derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
      d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4

      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73

**A negative claim asserted in prose is not evidence.** These checks
make the abstention auditable.

**A6 — Deliverables.** A derivation note (A0), a script under
`scripts/`, results under `results/`, a test file, and a report. **Tests
are required, not discretionary**: an untested symbolic rearrangement
supports nothing. At minimum the tests must cover Deliverables 2, 5 and 6 of §2 —
element-by-element equality with the frozen `matrix_rational`, basis
completeness, trace and generator normalisation, and involution as it
actually holds — **plus a dedicated test locking the canonical-to-Fierz
basis conversion of Deliverable 4**, asserting the pseudoscalar sign
explicitly so that an unconverted vector cannot pass — together with the
potential reconstruction.

**The potential test must not be satisfiable by a trivial
implementation.** A test asserting only `ΔV(M̂=0) = 0` passes for any
function that vanishes at zero, including one that is identically zero.
Require at least: a NONZERO reference value at a stated `M̂ ≠ 0` and
stated grid, checked to a stated tolerance. **That reference value is
computed by this task and recorded in the results artifact; it is not a
pre-existing frozen number and must not be described as one.** State in
the test file and the report that it is self-generated, so the test is
read as a regression anchor against future drift rather than as
independent validation of correctness. Also require: and **an independent
derivative check** — that the numerical derivative of the reconstructed
potential reproduces the reduced first derivative used for
root-finding at several `M̂`, including at least one stationary point
where it must vanish and one non-stationary point where it must not.

**A7 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, **pre-existing** test file,
`GATES.md`, `CONVENTIONS.md`, `AGENTS.md`, or `pyproject.toml` is
modified. **Adding a new test file is authorized by A6 and A8 and is
not a modification of any pre-existing test.** Verify
`GATES.md`'s blob is unchanged by reading the object.

**A8 — Scope, and how the manifest is fixed.** The authorized change
set is exactly six paths: this specification under `specs/`; the
derivation note under `derivations/`; a script under `scripts/`; a
results artifact under `results/`; a NEW test file under `tests/`; and
the report under `reports/`. **All six are additions.**

**The optional amendment does not change this.** If the pre-evaluation
reduction commit exists, the derivation note is added in commit 2 and
amended in a later commit on the same branch — but **at the branch head,
measured against the evidence base, it is still a single ADDED path.**
`mode: exact` is evaluated on the base-to-head difference, not on the
per-commit history, so the six-path add-only manifest holds either way.
**Do not add a `modify` entry for it, and do not create a second
manifest.** Report the intermediate history separately, in prose.

**The concrete paths are frozen here; you choose none of them** except
the `{HHMM}Z` token, which is fixed once by commit 1 and reused
verbatim:

    specs/2026-08-07T{HHMM}Z_p2-phase-01-fierz-and-branch-depths.md
    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
    scripts/p2_phase01_fierz_and_depths.py
    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
    tests/test_p2_phase01_fierz_and_depths.py
    reports/2026-08-07T{HHMM}Z_p2-phase-01-fierz-and-branch-depths.md

**Report the manifest in full before running the checker**, and report
the scope-checker JSON including `observed_operations`. **An exact scope
manifest whose paths the executor selects is not a frozen manifest** —
that was the defect this replaces.

**The new test file is an authorized addition under `tests/`.** A7's
prohibition on modifying existing tests is a prohibition on MODIFYING
pre-existing test files; it does not forbid adding a new one, which A6
requires. Verify that every pre-existing path under `tests/` is
unchanged by blob comparison, and that the only `tests/` change is your
addition.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>` — **that exact invocation, since `pytest` and
`python -m pytest` resolve to different versions on your host**:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`, and your new test file.

**Genuine exit 0 is required for each.** For the five pre-existing
files, running them is a regression check on this branch: they are not
expected to exercise your new code, and **"they passed" is not evidence
that the new derivation is correct** — that is what your new test file
is for. If any pre-existing file reports "no tests ran", that is a
finding, not a pass.
Report each command, complete stdout and stderr, exit status, wall time,
and the Python and pytest versions.

**A10 — Branch only, with `main` named precisely.** The previous
integration deliberately did NOT move local `main`; what advanced to
`9609677576b6d0d77a0813c93673aed81b0c4d5f` was `origin/main` and remote
`refs/heads/main`. **A criterion reading "local `main` equals
96096775…" would therefore already be false before you start**, and you
would correctly stop.

Before execution, verify that **`refs/remotes/origin/main` and remote
`refs/heads/main`** both resolve to
`9609677576b6d0d77a0813c93673aed81b0c4d5f`. Create the task branch from
that pinned commit.

**None of local `main`, `origin/main`, or remote `main` may be moved by
this task.** Report all three separately at the end. **A stale local
`main` is not to be fast-forwarded or otherwise repaired under this
authorization** — report its value as observed.

Push the task branch only.

## 5. Invariants and prohibitions

- **Commit this specification as commit 1** under
  `specs/2026-08-07T{HHMM}Z_p2-phase-01-fierz-and-branch-depths.md`,
  transcribed faithfully; report its committed blob SHA-256. The report
  filename uses the same `{HHMM}Z` token.
- **Commit-message hygiene:** inspect the proposed message before each
  commit AND the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. If one appears
  despite pre-commit inspection, **STOP before pushing**. Report, for
  each commit, whether any trailer was suppressed and which — **an
  authoring-time suppression is a fact to disclose, not an absence.**
- **Decide nothing.** Where the frozen material does not determine an
  answer, report the gap; do not close it.
- Do not construct a new effective potential for (b); use the existing
  one.
- No registered gate, gate status, verdict, digest, or hash-pinned
  artifact may be modified.
- Do not consume: the quarantined `−3.2(5)`; the suspended
  `P2-BETAV-CIRC-01` result; the historical Finding 5 extraction.
  **Confirm this concretely**: list every repository input your
  derivation and script actually read, by path, and show that none of
  the three appears among them. A bare assertion of non-consumption is
  not evidence.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: `docs/BRANCHING_POLICY.md` enumerates `gate/`,
  `paper/`, `review/`, `fix/`, `archive/`; the policy-versus-practice
  contradiction remains an open PI item. Use
  `gate/p2-phase-01-fierz-and-branch-depths`. If you judge that this
  conflicts, stop and report.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything**; report anything missing as a finding.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own development iteration.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Evidence layering — read before the report contract

**The report cannot contain evidence whose production depends on the
report commit.** A8-final examines a branch head that includes the
report; A9-final should run at that head; A10 pushes it. Writing those
back would require a further commit, which would move the head again and
invalidate them — the same recursion resolved in the role-model
integration.

**Committed report evidence layer.** The report records everything
available BEFORE the report commit: the derivation outputs; the
authored-artifact checks; the pinned-input verification; the blind
fixation digest; validators run on the pre-report content; and the
INTENDED final scope manifest. It also records the base, the earlier
commit SHAs and messages, the pre-report head, and the intended report
commit message.

**Post-report evidence layer — returned to the Reviewer, NOT written
back into the report.** After the report is committed: run the final
exact scope check against the committed branch head; run the validators
on a clean worktree at that head; push the branch; and return complete
raw **A8-final, A9-final and A10** evidence conversationally.

**Two further checks are post-report for the same reason, and were
missed when this layering was first written.**

**A5 fixed-string scan layering.** The scan includes the report, and
its output is written with surrounding sentences — so writing a hit such
as `"This work does not identify the physical ground state"` into the
report ADDS an occurrence of `ground state`, changing the count. There
is no fixed point. **The committed report states the intended scan terms
and the classification rule, but NOT its own final counts.** After the
report commit, scan the final committed versions of the derivation note,
script, results artifact, test file and report, and return every hit
with its surrounding sentence conversationally. **Do not amend the
report with the scan output.**

A5's other evidence — the `GATES.md` blob, the prerequisite-draft blobs,
and the path-by-path statement that no HS channel or V/A/T orientation
was selected — is unaffected and stays in the report.

**Final report-commit hygiene is post-report evidence.** A stored commit
message can only be read after the commit exists. The report records its
PROPOSED commit message and any authoring-time trailer suppression known
before committing. **After the report commit, read the stored message
back from the commit object, perform the trailer scan, and return the
raw result. Do not amend the report to record its own stored commit
message.** For every earlier commit, both the proposed and stored
messages go in the report as normal.

**Do not amend the report to insert evidence whose production depends on
the report commit itself.** A5-final, the final report-commit hygiene,
A8-final, A9-final and A10 are all post-commit evidence by definition.

## 7. Report contract

The committed report is the deliverable for its layer; the
conversational return carries the post-commit layer.

- raw output for A0–A7 in the committed report, except as §6 layers
  otherwise; **returned as post-commit evidence: the A5-final
  fixed-string scan, the final report-commit message hygiene, A8-final,
  A9-final and A10** — with scope-checker JSON verbatim including
  `observed_operations`;
- the Fierz coefficients as exact expressions, and Deliverables 1–6
  with their outputs;
- the branch depth table, with stable digits identified;
- the verified coefficients themselves, singlet and traceless pieces
  separate. **Do NOT report what they imply about how much the HS choice
  matters** — §2 forbids that inference, and an earlier draft wrongly
  requested it;
- **anything the derivations reveal that `OPEN-AC-1`, `OPEN-AC-2` or
  `OPEN-AC-3` will have to address, and which of them these results
  narrow.** This is the main product;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently. **You have supplied several high-value observations this
  week; this question is not a formality.**

---

## 8. PI ruling and specification amendment — γ₅ source disagreement

**Recorded here so the branch is self-contained and reproducible.**

During the read-only convention inspection required by A0 — performed
after commit 1 and before the derivation note — the Executor found that
two pinned sources assign different meanings to the token `gamma5`:

    Phase-A freeze, conventions.gamma5_definition
        gamma(0)*gamma(1)*gamma(2)*gamma(3)          gamma5^2 = +Id4, Hermitian

    derivations/CANONICAL_INTERACTION.json, vocabulary.gamma5
        I*gamma(0)*gamma(1)*gamma(2)*gamma(3)        gamma5^2 = -Id4, NOT Hermitian

This was reported as a STOP under §0's authority-order clause. The
disagreement is material: it reverses the sign of the squared
pseudoscalar bilinear that Deliverable 4 converts, i.e. it distinguishes
the interaction `S**2 + P**2` from `S**2 - P**2`.

**PI ruling, delivered 2026-08-07, reproduced verbatim:**

> For this task, the Phase-A freeze governs the definition of gamma5:
>
> gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)
>
> under the frozen Euclidean signature (1,1,1,1), with gamma5 Hermitian
> and gamma5^2 = Id4.
>
> The vocabulary.gamma5 entry in derivations/CANONICAL_INTERACTION.json,
> which inserts an additional factor of I, is an erroneous
> companion-artifact entry for this point. It is not authoritative for
> interpretation of the canonical interaction in this task. This ruling
> is supported by the Phase-A freeze, CONVENTIONS.md, the governing
> CANONICAL_INTERACTION.md, and the Phase-A checker assertions.
>
> Accordingly, Deliverable 4 uses:
>
> (bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2
>
> with gamma5 understood in the Phase-A-freeze sense.
>
> Record this PI ruling in commit 1's specification authority artifact so
> that the branch remains self-contained and reproducible. Then execute
> derivations (a) and (b) as originally scoped.
>
> Do not modify CANONICAL_INTERACTION.json or any other frozen/
> pre-existing artifact in this task. Record the inconsistent JSON
> vocabulary entry as a REPOSITORY_DEFECT finding. Its correction is a
> separate governance task.
>
> Also record a secondary process finding for later follow-up: the
> existing ratification process allowed a machine-readable companion to
> disagree semantically with its governing Markdown/convention sources.
> A future governance task should consider a machine check for
> duplicated normative fields across governing .md / companion .json
> pairs.
>
> This ruling resolves only the identified gamma5 source disagreement. It
> does not authorize any other reconciliation, convention choice, physics
> decision, or scope expansion.

**Consequences for this task, stated explicitly:**

1. Derivation (a) is NOT blocked. The §4 conditional clause is not
   triggered.
2. `gamma5` throughout this task means
   `gamma(0)*gamma(1)*gamma(2)*gamma(3)`.
3. `derivations/CANONICAL_INTERACTION.json` is NOT modified. It remains
   byte-identical to the evidence base.
4. The erroneous `vocabulary.gamma5` entry is recorded as a
   `REPOSITORY_DEFECT` finding in the report.
5. The ratification-process gap is recorded as a secondary process
   finding for a future governance task.
