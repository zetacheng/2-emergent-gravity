# Task report — `P2-PHASE-01`: Fierz-matrix verification and stationary-branch depths

Function: Executor
Date: 2026-08-07
Task classification: MATERIAL (branch only; integration is a separate
authorization after result review)
Executor: Claude Code (sandboxed container)

Authority: `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
Derivation note: `derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md`

**Both deliverables are derivations. Neither decides anything.**
**`P2-PHASE-01` remains `PROPOSED` and not runnable.** No gate is
registered, no status changed, no prerequisite draft adopted, and no
admissibility verdict reached.

---

## 1. Identification

| Item | Value |
| --- | --- |
| Branch | `gate/p2-phase-01-fierz-and-branch-depths` |
| Base (evidence base) | `9609677576b6d0d77a0813c93673aed81b0c4d5f` |
| Commit 1 (specification) | `0e52e52c98c0abfcd60228d48ad789689a96b389` |
| Commit 2 (derivation note) | `e7b3b9a934ba6f1583eef9c791a0bac5be26b1e2` |
| Commit 3 (script, results, test) | `311d1f25b7cd0a678500a4e4914cc2a50c5ccee7` |
| Pre-report head | `311d1f25b7cd0a678500a4e4914cc2a50c5ccee7` |
| UTC token `{HHMM}` | `0356`, observed `2026-08-07T03:56:15Z` |
| Specification blob SHA-256 | `3a187c1064ea491650959400eb825b62f7a969ff0294928e7ff87ed253a88539` |
| Pre-evaluation amendment commit | **does not exist** — no domain reduction was required |

### Commit messages, exactly as stored

Commit 1:

```text
specs: record the P2-PHASE-01 fierz-and-branch-depths authority

Commits the PI specification for the two P2-PHASE-01 derivations:
(a) verification of the frozen Phase-A Fierz matrix by independent
reconstruction, and (b) reduced-potential values at every stationary
branch of the exploratory scalar study.

Section 8 records the PI ruling of 2026-08-07 on the gamma5 source
disagreement found during the read-only convention inspection: the
Phase-A freeze definition governs, and the CANONICAL_INTERACTION.json
vocabulary entry carrying an extra factor of I is not authoritative for
this task. No frozen artifact is modified; the inconsistent entry is
recorded as a repository finding for a separate governance task.

P2-PHASE-01 remains PROPOSED. Nothing here registers a gate, changes a
status, adopts a prerequisite draft, or reaches an admissibility
verdict.
```

Commit 2:

```text
derivations: fix the Fierz verification and branch-depth analytic content

Commits the derivation note before any production code, per AGENTS.md
research rule 3. It fixes, before any number exists:

- the Phase-A freeze conventions governing derivation (a), including the
  PI-ruled gamma5 definition;
- the lambda-algebra determination, derived from the frozen generator
  normalisation, which makes derivation (a) executable;
- the exchange map, the projection formula for the Fierz matrix, and the
  blind-then-expose protocol;
- the mandatory canonical-to-Fierz pseudoscalar conversion;
- the internal singlet/traceless split, derived from the frozen
  normalisation and singlet definition;
- for derivation (b), the existing reduced potential by reference, its
  units, sign convention, and the fact that its absolute zero is not
  determined by the frozen material;
- the frozen evaluation domain, correspondence rule, stability algorithm
  and depth-ordering rule.

No channel, orientation, potential zero, or branch characterisation is
selected. P2-PHASE-01 remains PROPOSED.
```

Commit 3:

```text
p2-phase-01: verify the frozen Fierz matrix and evaluate branch depths

Adds the production script, the machine-readable results artifact, and a
new test file for the two derivations fixed by the derivation note.

Derivation (a): the 5x5 representation-family Fierz matrix is
reconstructed independently from the Phase-A freeze conventions and
proved equal to the frozen matrix_rational entry by entry as exact
rationals. The two frozen copies agree with each other. Basis
completeness, trace normalisation, generator normalisation, the
256-component compound kernel identity and involution are all verified
rather than asserted. Induced coefficients are reported after the
mandatory canonical-to-Fierz pseudoscalar conversion, with singlet and
traceless pieces separate.

Derivation (b): the reduced scalar potential of the pinned exploratory
study is evaluated at every stationary branch on all six grid/shift
combinations and all sixteen couplings, reusing that study's own
reconstruction rather than building a new one. Depth is reported only as
potential_minus_trivial, because the frozen material does not fix the
absolute zero.

No Hubbard-Stratonovich channel, V/A/T orientation, potential zero or
branch characterisation is selected. P2-PHASE-01 remains PROPOSED.
```

**Trailer hygiene.** Each message was inspected with `cat -A` before the
commit and read back from the commit object afterwards. **For every
commit, two trailers were suppressed at authoring time** — a
`Co-Authored-By:` line and a `Claude-Session:` URL line that the
executor's harness convention would otherwise append. **The suppression
is a fact, not an absence:** the scan of the stored messages returns
zero hits for `co-authored-by`, `claude-session`, `session_`,
`claude.ai`, `generated with` and `signed-off-by`.

### Intended commit-4 (report) message

```text
docs: report the P2-PHASE-01 Fierz verification and branch-depth results

Records the A0-A7 evidence for both derivations: the pinned-input
verification, the blind-fixation digest, the element-by-element equality
proof against the frozen matrix_rational, the exchange map and kernel
identity, the induced coefficients after the mandatory pseudoscalar
conversion, the basis and generator checks, involution, and the
branch-depth table with cross-grid stability.

The A5 fixed-string scan counts, the final scope check, the validators
at the report head and the stored message of this commit are post-report
evidence and are deliberately absent here: the report cannot contain
evidence whose production depends on its own commit.
```

**This report records neither its own commit SHA nor the final branch
head**, and does not record its own A5 scan counts (§6 of the
specification).

---

## 2. A1 — frozen material verified, and the pinned-input digests

All eight pinned digests were verified at the evidence base before use,
and the sidecar was checked against both the pinned value and the file's
committed content.

```text
PINNED INPUT DIGESTS at the evidence base 9609677576b6d0d77a0813c93673aed81b0c4d5f
  MATCH    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
           expected fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
           actual   fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
  MATCH    results/P2-CHANNEL-FREEZE/fierz_matrix.json
           expected 5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
           actual   5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
  MATCH    derivations/CANONICAL_INTERACTION.md
           expected 27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
           actual   27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
  MATCH    derivations/CANONICAL_INTERACTION.json
           expected f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1
           actual   f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1
  MATCH    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
           expected 80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599
           actual   80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599
  MATCH    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
           expected a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028
           actual   a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028
  MATCH    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
           expected d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4
           actual   d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4
  MATCH    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
           expected a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73
           actual   a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73

SIDECAR results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256:
  5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9  fierz_matrix.json
  -> agrees with the pinned value and with the file's committed content: yes
```

**The canonical interaction is exactly as §0 of the specification quotes
it.** From `derivations/CANONICAL_INTERACTION.json`:

```text
"canonical_interaction_expression":
  "(G/(2*N)) * Sum( bilinear(lam(A), Id4)**2 + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )"
```

`interaction_decomposition` lists **only S and P** as supported. It is
located in the Phase-A freeze (line 116), **not** in
`CANONICAL_INTERACTION.json` as the specification's phrasing might
suggest:

```text
"interaction_decomposition":[
  {"family_id":"S","operator_expression":"Sum(bilinear(lam(A),Id4)**2,(A,0,N**2-1))",
    "coefficient":"G/(2*N)","support":true},
  {"family_id":"P","operator_expression":"Sum(bilinear(lam(A),I*gamma5)**2,(A,0,N**2-1))",
    "coefficient":"G/(2*N)","support":true}]
```

**One difference was found and is recorded as a first-class finding**
(§8.1): the `vocabulary.gamma5` entry of `CANONICAL_INTERACTION.json`
disagrees with the Phase-A freeze. It was reported as a STOP, and the PI
ruled on it; the ruling is reproduced in §8 of the committed
specification. `CANONICAL_INTERACTION.json` was **not** modified.

---

## 3. Derivation (a) — Deliverables 1–6

### 3.1 Deliverable 1 and the blind-fixation chronology

Phase 1 was honoured. `matrix_rational` occupies exactly one line of the
freeze document (line 98); the conventions were extracted
programmatically **with that key explicitly withheld**, so neither
frozen copy was parsed or printed before the reconstruction existed.

```text
BLIND FIXATION
  scratch artifact : <scratch>/blind_fierz.json
  SHA-256          : 5d920bc70c897d15c81727bf9f1508e3352528043f58f14ff1ed63f0495d75f1
  recorded at      : 2026-08-07T04:02:59Z
  exposure of the frozen matrices occurred only after this timestamp
```

Reconstruction, from the declared conventions alone, using

    M[a][c] = (1/16) * Sum_i trace(Gamma^a_i Gamma^c_k Gamma^a_i Gamma^c_k)

whose `k`-independence is itself checked (all 25 family pairs:
**k-independent = True**).

### 3.2 Deliverable 2 — element-by-element equality, exact rationals

**Step 1, the two frozen copies compared to each other first**, as §0
requires: the freeze's embedded `matrix_rational` and
`results/P2-CHANNEL-FREEZE/fierz_matrix.json` are **identical in all 25
entries**.

Frozen `matrix_rational` (rows `a`, columns `b`, order `[S,P,V,A,T]`):

```text
               S       P       V       A       T
      S      1/4     1/4     1/4     1/4     1/4
      P      1/4     1/4    -1/4    -1/4     1/4
      V        1      -1    -1/2     1/2       0
      A        1      -1     1/2    -1/2       0
      T      3/2     3/2       0       0    -1/2
```

Reconstruction (without the crossing sign):

```text
               S       P       V       A       T
      S      1/4     1/4     1/4     1/4     1/4
      P      1/4     1/4    -1/4    -1/4     1/4
      V        1      -1    -1/2     1/2       0
      A        1      -1     1/2    -1/2       0
      T      3/2     3/2       0       0    -1/2
```

Entry-by-entry comparison, exact rationals, no tolerance:

```text
   SS: 1/4==1/4 OK | SP: 1/4==1/4 OK | SV: 1/4==1/4 OK | SA: 1/4==1/4 OK | ST: 1/4==1/4 OK
   PS: 1/4==1/4 OK | PP: 1/4==1/4 OK | PV: -1/4==-1/4 OK | PA: -1/4==-1/4 OK | PT: 1/4==1/4 OK
   VS: 1==1 OK | VP: -1==-1 OK | VV: -1/2==-1/2 OK | VA: 1/2==1/2 OK | VT: 0==0 OK
   AS: 1==1 OK | AP: -1==-1 OK | AV: 1/2==1/2 OK | AA: -1/2==-1/2 OK | AT: 0==0 OK
   TS: 3/2==3/2 OK | TP: 3/2==3/2 OK | TV: 0==0 OK | TA: 0==0 OK | TT: -1/2==-1/2 OK
```

**All 25 entries agree exactly.** The algebra of the freeze is confirmed
by an independent reconstruction that never saw it.

### 3.3 A first-class finding — where `grassmann_crossing_sign` sits

**The frozen matrix equals the reconstruction WITHOUT the `-1` factor.**
Applying `grassmann_crossing_sign = -1` as the specification and the
freeze's §C prose describe gives the exact global negative of the frozen
matrix: 21 of 25 entries differ in sign (the four zeros coincide).

```text
reconstruction WITH the crossing sign (-1):
               S       P       V       A       T
      S     -1/4    -1/4    -1/4    -1/4    -1/4
      P     -1/4    -1/4     1/4     1/4    -1/4
      V       -1       1     1/2    -1/2       0
      A       -1       1    -1/2     1/2       0
      T     -3/2    -3/2       0       0     1/2

frozen + signed_reconstruction == 0  (exact global sign flip): True
```

**This is reported, not resolved.** Three observations bear on it and
none of them settles it:

- The freeze lists `grassmann_crossing_sign` as a **separate convention
  field**, which is consistent with the tabulated matrix being the pure
  Dirac-algebra exchange matrix and the sign being applied on use.
- The freeze's §C prose says the algebra "and the Grassmann crossing
  sign `-1` fix the following exact exchange matrix", which reads the
  other way.
- The repository's own Phase-A checker builds the matrix as
  `computed_fierz = (sign * projector * crossing * embedding).T * sign`
  (`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:462`). With `sign`
  a scalar `-1`, the two factors **cancel**, so the checker validates
  the unsigned matrix — consistent with the frozen entries, and
  consistent with my reconstruction.

**Involution cannot discriminate**, since `M² = (−M)² = 1`. The
consequence for Deliverable 4 is stated in §3.6. Classified
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` (§8.2).

### 3.4 Deliverable 3 — the exchange map, and the kernel identity

- **Legs exchanged:** the two `psi` legs, `psi_2 <-> psi_4`. The two
  `psibar` legs are left in place.
- **Dirac and internal indices are exchanged JOINTLY**, because the
  permutation acts on field operators and each field carries both index
  types. There is no independent internal-only exchange.
- **Where the `-1` enters:** restoring the reference ordering
  `psibar_1 psi_2 psibar_3 psi_4` from the exchanged ordering
  `psibar_1 psi_4 psibar_3 psi_2` is an odd permutation of anticommuting
  fields. It is a **single overall factor**, not per family and not per
  component.
- **`compound_index_order = [dirac_family, internal_family, component]`**
  reads a compound label outermost-first: Dirac family
  `a in {S,P,V,A,T}`, then internal family label `A`, then the
  component index within the Dirac family (`mu=0..3` for V and A,
  `0<=mu<nu<=3` for T, single for S and P). The compound basis element
  is `lam(A) (x) Gamma^a_i`.

**The compound kernel equality is demonstrated, not asserted** — all
`4^4 = 256` index combinations checked per family, exact residual zero:

```text
max |LHS - RHS| per family, over 256 components each:
  S: 0    P: 0    V: 0    A: 0    T: 0
```

### 3.5 Deliverable 5 — completeness, traces, generators

```text
sixteen elements                         : 16
rank of their span in the 4x4 matrices   : 16   (spans; no residual)
linearly independent                     : True
all Hermitian                            : True
all square to Id4                        : True
trace(Id4)                               : 4
orthogonality trace(G^a G^b) = 4 delta   : True
trace proportionality constant per family: S=4  P=4  V=4  A=4  T=4
gamma5 Hermitian                         : True
gamma5^2 = Id4                           : True

generator checks (explicit N):
  N=2  generators 4  = N^2 ; trace(lam^A lam^B)=2delta True ; completeness True ; lam0=sqrt(2/N)Id True
  N=3  generators 9  = N^2 ; trace(lam^A lam^B)=2delta True ; completeness True ; lam0=sqrt(2/N)Id True
  N=4  generators 16 = N^2 ; trace(lam^A lam^B)=2delta True ; completeness True ; lam0=sqrt(2/N)Id True
```

**How the `A = 0..N²−1` index set enters.** Because the set includes the
singlet, the generators span the full space of `N×N` matrices, and the
declared normalisation fixes the completeness relation with no residual
freedom:

    Sum_A (lam(A))_{ij} (lam(A))_{kl} = 2 delta_{il} delta_{kj}

verified explicitly for `N = 2, 3, 4`. This is the relation the internal
rearrangement uses.

### 3.6 Deliverable 4 — induced coefficients, after the mandatory conversion

**Before conversion** (canonical operators, `P` built from `I*gamma5`):

```text
S: G/(2*N)    P: G/(2*N)    V: 0    A: 0    T: 0
```

**After conversion** into the frozen `[S,P,V,A,T]` basis, using
`(bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2` with
`gamma5` in the PI-ruled Phase-A sense:

```text
S: G/(2*N)    P: -G/(2*N)   V: 0    A: 0    T: 0
```

**The verified matrix was applied only to the converted vector.** The
Dirac row after the matrix is

```text
S: 0    P: 0    V: 1/2    A: 1/2    T: 0
```

**Singlet / traceless split, derived from the declared normalisation
(not invented).** By §3.5 the exchanged internal structure is
`Id_N (x) Id_N` with an overall factor 2, and `Id_N = sqrt(N/2) lam(0)`,
so the internal factor is `2 * (N/2) = N`, which cancels the `1/N` of
the canonical prefactor:

| family | induced coefficient, **singlet** | induced coefficient, **traceless** |
| --- | --- | --- |
| S | `0` | `0` |
| P | `0` | `0` |
| V | `G/4` | `0` |
| A | `G/4` | `0` |
| T | `0` | `0` |

**The vanishing S, P and T coefficients are results, not omissions**, and
so is the vanishing traceless column: the exchanged internal structure
is purely singlet under `lam(0) = sqrt(2/N) Id_N`, so no traceless
generator appears at all.

**Effect of the crossing-sign ambiguity of §3.3, stated without
resolving it.** The table above applies the **frozen** matrix, as the
specification directs ("apply the verified Fierz matrix"). Were the
`-1` applied on top, every entry above would flip sign — `V` and `A`
would read `-G/4` — and the zeros would remain zero. **The magnitudes,
the vanishing families and the purely-singlet structure are unaffected;
only the overall sign of the induced V and A coefficients is at stake.**

**No inference is drawn about the size of the mean-field ambiguity.**
That depends on which channel is bosonised and on the truncation, and is
`P2-FIERZSUM-01`'s subject, not this task's.

### 3.7 Deliverable 6 — involution, as it actually holds

```text
frozen * frozen =
               S       P       V       A       T
      S        1       0       0       0       0
      P        0       1       0       0       0
      V        0       0       1       0       0
      A        0       0       0       1       0
      T        0       0       0       0       1

frozen^2 == Identity : True
rank(frozen)         : 5
exact residual (frozen^2 - I) : all entries 0
unsigned^2 == Identity : True
signed^2   == Identity : True
```

Involution holds exactly, with zero residual — **and it holds for both
sign conventions**, which is why it cannot arbitrate §3.3. No convention
was adjusted to force anything; the outcome is reported as found.

---

## 4. Derivation (b) — potential values at each stationary branch

### 4.1 Conventions, stated before the numbers

- **The potential is the existing one.** `reconstructed_potential`,
  `WilsonQuadrature` and `first_derivative` are **imported** from
  `scripts/p2_phase01_scalar_exploratory.py`, so the quadrature, the
  Gauss–Legendre order and the grid construction are identical to the
  study that produced the roots. **No new potential was constructed.**
- **Units:** per site (per unit four-volume in lattice units), `a = 1`,
  `r = 1`; measure `d^4p/(2pi)^4`. Not per mode, not extensive.
- **Sign:** a more negative `potential_minus_trivial` is deeper.
- **The zero:** the frozen material supplies only the difference
  `V_red(Mhat) - V_red(0)`, and scopes its "declared common zero"
  explicitly to within this scalar ansatz. `V_red(0; G)` is not
  reconstructed anywhere. **`potential_value` is therefore reported as
  `NOT DEFINED UNDER THE FROZEN MATERIAL` and no zero was chosen**
  (§8.3). All analysis uses `potential_minus_trivial`, which the frozen
  formula defines outright.
- **Scope limit:** this is a comparison **within one potential**. It says
  nothing about cross-family comparison, which needs a common HS,
  measure and potential-zero normalisation that is not frozen —
  `OPEN-AC-3`, untouched.

### 4.2 Domain — evaluated in full, no reduction

**No pre-evaluation reduction was required, so the amendment commit of
§3 of the specification does not exist** and the derivation note was
never amended. All six grid/shift combinations and all sixteen couplings
were evaluated: 282 (grid, shift, coupling, branch) rows. The results
artifact records this explicitly under `domain_reduction`
(`"reduced": false`, `"amendment_commit": null`), together with both the
sets used and the sets frozen in the specification.

Cost, for the record: the full sweep runs in ~2.5 minutes wall time on
this host, well inside what the specification anticipated.

### 4.3 The branch depth table

`V` below is `potential_minus_trivial`; `sdp` is
`stable_decimal_places` over the participating grid/shift combinations;
every row rests on **all six** combinations.

```text
  G/Gc    sector  #            V_min            V_max       spread  sdp  status
   0.8      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   0.8  negative  0     -3.917258250     -3.915645985    1.612e-03    2  AGREEMENT
   0.8  negative  1      0.000607879      0.000614145    6.266e-06    5  AGREEMENT
   0.9      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   0.9  negative  0     -4.267309608     -4.265752235    1.557e-03    2  AGREEMENT
   0.9  negative  1      0.000054210      0.000055189    9.792e-07    4  AGREEMENT
  0.98      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
  0.98  negative  0     -4.505905108     -4.503988512    1.917e-03    1  AGREEMENT
  0.98  negative  1      0.000000329      0.000000333    4.094e-09    8  AGREEMENT
  0.99      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
  0.99  negative  0     -4.533740623     -4.531830859    1.910e-03    2  AGREEMENT
  0.99  negative  1      0.000000040      0.000000040    2.572e-10    9  AGREEMENT
   1.0      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.0  negative  0     -4.561175404     -4.559277209    1.898e-03    2  AGREEMENT
  1.01      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
  1.01  negative  0     -4.588216635     -4.586333046    1.884e-03    2  AGREEMENT
  1.01  positive  0     -0.000000037     -0.000000037    2.364e-10    9  AGREEMENT
  1.02      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
  1.02  negative  0     -4.614872360     -4.613004039    1.868e-03    2  AGREEMENT
  1.02  positive  0     -0.000000290     -0.000000287    3.176e-09    8  AGREEMENT
  1.05      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
  1.05  negative  0     -4.692599843     -4.690781076    1.819e-03    2  AGREEMENT
  1.05  positive  0     -0.000004160     -0.000004091    6.874e-08    6  AGREEMENT
   1.1      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.1  negative  0     -4.815110703     -4.813364629    1.746e-03    1  AGREEMENT
   1.1  positive  0     -0.000029374     -0.000028928    4.456e-07    6  AGREEMENT
   1.2      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.2  negative  0     -5.036280244     -5.035093346    1.187e-03    2  AGREEMENT
   1.2  positive  0     -0.000191271     -0.000189330    1.941e-06    5  AGREEMENT
   1.4      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.4  negative  0     -5.396797104     -5.396260997    5.361e-04    2  AGREEMENT
   1.4  positive  0     -0.001104334     -0.001097831    6.503e-06    5  AGREEMENT
   1.6      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.6  negative  0     -5.681600516     -5.680637929    9.626e-04    2  AGREEMENT
   1.6  positive  0     -0.002848733     -0.002836622    1.211e-05    4  AGREEMENT
   1.8      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   1.8  negative  0     -5.917759885     -5.916951209    8.087e-04    2  AGREEMENT
   1.8  positive  0     -0.005343298     -0.005325154    1.814e-05    4  AGREEMENT
   2.0      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   2.0  negative  0     -6.113911169     -6.113025718    8.855e-04    2  AGREEMENT
   2.0  positive  0     -0.008466161     -0.008441880    2.428e-05    3  AGREEMENT
   2.5      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   2.5  negative  0     -6.503823459     -6.503376364    4.471e-04    2  AGREEMENT
   2.5  positive  0     -0.018284051     -0.018244897    3.915e-05    3  AGREEMENT
   3.0      zero  0      0.000000000      0.000000000    0.000e+00   12  AGREEMENT_THROUGH_D_MAX
   3.0  negative  0     -6.787536875     -6.786872556    6.643e-04    2  AGREEMENT
   3.0  positive  0     -0.029922959     -0.029870221    5.274e-05    4  AGREEMENT

depth resolution (disjoint envelopes) — all pairs at each coupling:
  total pairs: 46; resolved: 46; unresolved: 0
  G/Gc=  0.8        zero#0 vs negative#0   disjoint=True  more negative: negative#0
  G/Gc=  0.8        zero#0 vs negative#1   disjoint=True  more negative: zero#0
  G/Gc=  0.8    negative#0 vs negative#1   disjoint=True  more negative: negative#0
  G/Gc=  0.9        zero#0 vs negative#0   disjoint=True  more negative: negative#0
  G/Gc=  0.9        zero#0 vs negative#1   disjoint=True  more negative: zero#0
  G/Gc=  0.9    negative#0 vs negative#1   disjoint=True  more negative: negative#0
  ...
```

Reading the table:

- The trivial branch is `0` identically on all six grids, agreeing
  through `d_max = 12`; its `stability_status` is
  `AGREEMENT_THROUGH_D_MAX`, which is what distinguishes it from a bare
  `stable_decimal_places = 0`.
- The deep negative-`M̂` branch is stable to 1–2 decimal places with a
  spread of order `1e-3`; the shallow branches are stable to 3–9 decimal
  places with spreads down to `1e-10`.
- **Every one of the 46 pairwise depth comparisons is RESOLVED** — all
  `[V_min, V_max]` envelopes at a given coupling are disjoint. None had
  to be left unranked.
- No branch had UNRESOLVED CROSS-GRID CORRESPONDENCE: root counts agreed
  across all six combinations at every coupling.

**The depth ordering is reported as an observation and nothing more.**
Whether any branch is the physical ground state, and whether the
negative-mass branch is a physical phase or a doubler sector, is
`OPEN-AC-2` and is not answered here.

### 4.4 Regression anchor and derivative check

```text
regression anchor (SELF-GENERATED BY THIS TASK, recorded in the results artifact;
a regression anchor against future drift, NOT independent validation, and NOT a
pre-existing frozen number):
  n = 32, shift = 0.0, G/G_c = 1.2, Mhat = 0.5
  potential_minus_trivial = 0.00019130050729523028   (NONZERO)

independent derivative check, |numerical dV/dMhat - analytic V'_red|:
  Mhat = 0.0  ->  1.73e-12   (stationary point: analytic derivative is exactly 0)
  Mhat = 0.1  ->  1.65e-12
  Mhat = 0.5  ->  8.28e-13   (non-stationary: analytic derivative is nonzero)
  Mhat = 1.0  ->  1.13e-13
```

---

## 5. A5 — no decision taken, verified rather than declared

### 5.1 Path-by-path statement

| path | HS channel selected? | V/A/T orientation selected? |
| --- | --- | --- |
| `derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md` | **No** | **No** |
| `scripts/p2_phase01_fierz_and_depths.py` | **No** | **No** |
| `results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json` | **No** | **No** |
| `tests/test_p2_phase01_fierz_and_depths.py` | **No** | **No** |
| `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` | **No** | **No** |

The results artifact carries this machine-readably under
`decisions_taken`: `hubbard_stratonovich_channel: NONE SELECTED
(OPEN-AC-1)`, `vat_orientation_or_components: NONE SELECTED`,
`potential_zero: NONE SELECTED`, `branch_characterisation: NONE MADE
(OPEN-AC-2)`.

### 5.2 Fixed-string scan — terms and rule stated here, counts returned post-report

The scan covers the five artifacts this task authors — the derivation
note, script, results artifact, test file and report — and excludes only
the committed specification. Terms: `the vacuum`, `preferred`,
`physical phase`, `artifact`, `ground state`, `is the true`.

**Classification rule:** every hit is reported with its surrounding
sentence and classified as either an ASSERTION of a characterisation or
a DISCLAIMER of one. A non-zero count is not a failure; a required
abstention is a legitimate use and **will not be reworded to avoid a
hit**.

**The counts are NOT recorded here.** The scan includes this report, and
writing a hit with its sentence into this report would add occurrences
and change the count — there is no fixed point. Per §6 of the
specification the counts are post-report evidence, returned
conversationally.

### 5.3 Repository integrity

```text
=== A7 — nothing pre-existing disturbed (base -> pre-report head) ===
$ git diff --name-status --find-renames --find-copies 9609677576b6d0d77a0813c93673aed81b0c4d5f 311d1f25b7cd0a678500a4e4914cc2a50c5ccee7
A	derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
A	results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
A	scripts/p2_phase01_fierz_and_depths.py
A	specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
A	tests/test_p2_phase01_fierz_and_depths.py
[end — only additions expected]

$ git rev-parse 9609677576b6d0d77a0813c93673aed81b0c4d5f:GATES.md ; git rev-parse 311d1f25b7cd0a678500a4e4914cc2a50c5ccee7:GATES.md
bd4820513217ae7e1c493328dc49536e69b8cfb8
bd4820513217ae7e1c493328dc49536e69b8cfb8
  CONVENTIONS.md     base 2d4f735c55a14fdfc5d1031a58698a8ca075fbbd  head 2d4f735c55a14fdfc5d1031a58698a8ca075fbbd  identical=true
  AGENTS.md          base 5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3  head 5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3  identical=true
  pyproject.toml     base 9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4  head 9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4  identical=true
  CLAIMS.md          base df75ff4de2146fff64ce4995f295c603e7d5b861  head df75ff4de2146fff64ce4995f295c603e7d5b861  identical=true

=== pre-existing tests/ unchanged; only the new file added ===
  base tests/ files: 11  head tests/ files: 12
  pre-existing tests MODIFIED: []
  tests ADDED: ['tests/test_p2_phase01_fierz_and_depths.py']
  tests REMOVED: []

=== A5 — prerequisite drafts byte-identical to the evidence base ===
  derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    base d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4
    head d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4  identical=true
  derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    base a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73
    head a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73  identical=true
```

`GATES.md` blob is `bd4820513217ae7e1c493328dc49536e69b8cfb8` at both the
evidence base and the pre-report head — read from the object, not
quoted. Both named prerequisite drafts are byte-identical to the
evidence base.

### 5.4 Inputs actually read — non-consumption shown, not asserted

The script opened exactly these repository paths:

```text
derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
results/P2-CHANNEL-FREEZE/fierz_matrix.json
results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
scripts/p2_phase01_scalar_exploratory.py
```

with their SHA-256 values recorded in the results artifact under
`input_sha256`. **None of the three excluded items appears in that
list**: the quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01`
result, and the historical Finding 5 extraction were not read. The
artifact records this under `exclusions_confirmed` with the enumerated
list as the evidence.

---

## 6. A6 — deliverables, and what the tests actually lock

| deliverable | path |
| --- | --- |
| derivation note | `derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md` |
| script | `scripts/p2_phase01_fierz_and_depths.py` |
| results | `results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json` |
| test file | `tests/test_p2_phase01_fierz_and_depths.py` |
| report | `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` |

The 14 tests cover: element-by-element equality with the frozen
`matrix_rational` (Deliverable 2); agreement of the two frozen copies;
the observed crossing-sign placement; sixteen-element completeness,
Hermiticity, trace and generator normalisation (Deliverable 5);
involution and its non-discrimination of the sign (Deliverable 6); **a
dedicated test locking the canonical-to-Fierz conversion**, asserting the
pseudoscalar sign so an unconverted `(S,P) = (1,1)` vector cannot
reproduce the result (Deliverable 4); the nonzero self-generated
potential anchor; the derivative check at a stationary and a
non-stationary point; the undetermined potential zero; and the
`decisions_taken` block.

---

## 7. A8 — intended final scope manifest, and A9-pre

### 7.1 The frozen six-path manifest, reported in full before the checker runs

```text
base: 9609677576b6d0d77a0813c93673aed81b0c4d5f
head: <the report commit>
mode: exact
add:
  specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
  derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
  scripts/p2_phase01_fierz_and_depths.py
  results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
  tests/test_p2_phase01_fierz_and_depths.py
  reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md
forbidden_operations:
  delete, rename, copy, type_change, unmerged, unknown
```

**All six are additions**, and the intermediate history — commit 1
specification, commit 2 note, commit 3 script+results+test, commit 4
report — collapses to six added paths measured base-to-head. No
`modify` entry exists because the derivation note was never amended.

### 7.2 A9-pre — validators at the pre-report head

```text
A9-pre — validators at the pre-report head 311d1f25b7cd0a678500a4e4914cc2a50c5ccee7
$ git rev-parse HEAD
311d1f25b7cd0a678500a4e4914cc2a50c5ccee7
$ git status --porcelain
[end]
$ python --version
Python 3.11.15
$ python -m pytest --version
pytest 9.1.1
----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_repository_structure.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 4 items

tests/test_repository_structure.py ....                                  [100%]

============================== 4 passed in 0.02s ===============================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 0.25 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_si1_governance.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 14 items

tests/test_si1_governance.py ..............                              [100%]

============================== 14 passed in 0.04s ==============================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 0.26 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_gate_anchors.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 20 items / 2 deselected / 18 selected

tests/test_gate_anchors.py ..................                            [100%]

======================= 18 passed, 2 deselected in 4.11s =======================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 4.53 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_governance_tools.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 8 items

tests/test_governance_tools.py ........                                  [100%]

============================== 8 passed in 1.25s ===============================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 1.48 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_scalar_exploratory.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 5 items

tests/test_p2_phase01_scalar_exploratory.py .....                        [100%]

============================== 5 passed in 0.14s ===============================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 0.36 s

----------------------------------------------------------------
$ PYTHONDONTWRITEBYTECODE=1 python -m pytest tests/test_p2_phase01_fierz_and_depths.py -p no:cacheprovider --basetemp=/tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/bt-pre
--- stdout:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/wt-pre
configfile: pyproject.toml
collected 14 items

tests/test_p2_phase01_fierz_and_depths.py ..............                 [100%]

============================== 14 passed in 1.70s ==============================
[end stdout]
--- stderr:
[end stderr]
--- exit status: 0
--- wall: 2.07 s

$ git status --porcelain (post-run)
[end]
```

All six reached genuine exit 0 with tests collected and run; none
reported "no tests ran". **`python -m pytest` was used throughout**, as
the specification requires, because `pytest` and `python -m pytest`
resolve to different versions on this host (see §8.4).

**The five pre-existing files passing is a regression check on this
branch only. It is not evidence that the new derivation is correct** —
that is what `tests/test_p2_phase01_fierz_and_depths.py` is for.

---

## 8. Stops and clarifications

**One stop occurred**, at the point A0's ordering was designed to catch
it: during the read-only convention inspection, after commit 1 and
before the derivation note.

### 8.1 `REPOSITORY_DEFECT` — the `gamma5` source disagreement (the stop)

Two pinned sources assign different meanings to the token `gamma5`:

| source | `gamma5` | `gamma5^2` | Hermitian |
| --- | --- | --- | --- |
| Phase-A freeze, `conventions.gamma5_definition` | `gamma(0)*gamma(1)*gamma(2)*gamma(3)` | `+Id4` | yes |
| `CANONICAL_INTERACTION.json`, `vocabulary.gamma5` | `I*gamma(0)*gamma(1)*gamma(2)*gamma(3)` | `-Id4` | no |

The disagreement is material: it reverses the sign of the squared
pseudoscalar bilinear, distinguishing `S**2 + P**2` from `S**2 - P**2`.
Three independent sources corroborate the freeze and contradict the JSON
companion — `CONVENTIONS.md:27` (`Hermitian`, `gamma_5**2 = 1`),
`CANONICAL_INTERACTION.md:52` (whose SHA-256 the JSON itself pins), and
`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:377-388`, which builds
`gamma5` without the `I` and asserts both properties.

**Reported as a STOP; not reconciled and no source preferred.** The PI
ruled that the Phase-A freeze governs; the ruling is reproduced verbatim
in §8 of the committed specification, which is what makes this branch
self-contained. `CANONICAL_INTERACTION.json` was **not** modified and
remains byte-identical to the evidence base. **Its correction is a
separate governance task.**

**Secondary process finding, for later follow-up:** the existing
ratification process permitted a machine-readable companion to disagree
semantically with its governing Markdown and convention sources. A
future governance task should consider a machine check for duplicated
normative fields across governing `.md` / companion `.json` pairs.

### 8.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — crossing-sign placement

Recorded in §3.3 and not resolved. It affects only the overall sign of
the induced `V` and `A` coefficients; magnitudes, vanishing families and
the purely-singlet structure are unaffected. The checker's
double-application of `sign` is evidence about intent but is not a
ruling, and I did not treat it as one.

### 8.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the potential zero

The frozen material fixes only `V_red(Mhat) - V_red(0)`.
`potential_value` is reported as `NOT DEFINED UNDER THE FROZEN
MATERIAL`; no zero was chosen. **This blocked nothing**: every
within-potential result — the envelope comparison, the correspondence
rule, the depth resolution — depends only on differences.

### 8.4 `ENVIRONMENT` — two pytest versions, nothing installed

`pytest` resolves to 9.0.2 (console script on `PATH`) and
`python -m pytest` to 9.1.1 (the module in the interpreter). The
specification fixes `python -m pytest`, which is what every run used.
Nothing was installed and no configuration was changed.

### 8.5 `OBSERVATION_METHOD_ERROR` — three defects of mine, corrected

All three were in my own code during development, none touched
repository state, and all were fixed before commit 3:

1. **Two JSON-serialisation failures.** The first run died on sympy
   Boolean objects; the second on `numpy.bool_`, whose class name is
   literally `bool` under NumPy 2 and which is not a `bool` subclass.
   Fixed by explicit `bool()`/`float()` coercion at the boundary plus a
   `default=` handler. **No numerical value was altered** — the artifact
   is bit-identical across the two successful runs (verified by `diff`).
2. **A test bug of mine.** `sympify("G/4")` builds an assumption-free
   `Symbol("G")` that never equals `Symbol("G", positive=True)`, so a
   set-containment assertion failed with the confusing message
   `assert {G} <= {G}`. Fixed by comparing symbol names.
3. **Lint.** `ruff` flagged four `E702` and one `E741` in my script;
   corrected. The regenerated artifact is bit-identical, confirming the
   fixes were cosmetic.

### 8.6 No other stop

No pinned digest mismatched. The sidecar agreed. The two frozen copies
of the matrix agreed with each other. No `matrix_rational` entry
disagreed with the reconstruction. No merge, no gate, no status, no
verdict and no hash-pinned artifact was touched.

---

## 9. What these results mean for `OPEN-AC-1`, `OPEN-AC-2`, `OPEN-AC-3`

This is the main product of the task.

### 9.1 `OPEN-AC-1` (which HS channel) — narrowed, materially

**The Fierz rearrangement of the frozen interaction generates exactly
two families, `V` and `A`, with equal singlet coefficients `G/4`, and
generates nothing in `S`, `P` or `T`.** Three consequences follow, none
of them a decision:

- **The exchange channel is not a free five-way choice.** Whatever HS
  scheme is eventually adopted, the bare exchange-channel content
  available from this interaction is `V` and `A` only. A specification
  that offers `T` as a candidate exchange channel would be offering
  something the algebra does not supply at this order.
- **`V` and `A` enter symmetrically**, with identical coefficients. Any
  scheme that treats them asymmetrically must import that asymmetry from
  somewhere other than the Fierz rearrangement.
- **The induced content is purely singlet.** The traceless coefficient
  is exactly zero, so an HS field carrying a traceless internal index has
  no bare exchange-channel source here. This is the sharpest of the
  three constraints and it comes directly from
  `lam(0) = sqrt(2/N) Id_N` plus the frozen normalisation.

**The unresolved sign of §3.3 does not weaken any of these**, because all
three are statements about which families are nonzero and how they
relate, not about the overall sign.

### 9.2 `OPEN-AC-2` (branch status) — the evidence is now sufficient to pose it sharply

Depth is now measured rather than assumed: all 46 pairwise comparisons
resolve at the available grid resolution, so `OPEN-AC-2` no longer has to
contend with the possibility that the branches are numerically
indistinguishable. **What `OPEN-AC-2` must still answer is unchanged**,
and this task does not touch it: which branch, if any, corresponds to a
physical state, and whether the negative-`M̂` branch is a physical phase
or a doubler sector. **The depth ordering does not answer that** — a
deeper branch of a reduced one-dimensional potential is not thereby
physical, particularly where the Wilson term makes `I0(M̂)` manifestly
asymmetric under `M̂ -> -M̂`, which the pinned study tests rather than
assumes.

One observation `OPEN-AC-2` will have to address: below `G/G_c = 1` the
second negative root sits at **positive** `potential_minus_trivial`
(a barrier relative to the trivial branch), while above `G/G_c = 1` a
positive-`M̂` root appears at **negative** `potential_minus_trivial`. The
qualitative change occurs at the critical coupling and is resolved by the
envelopes at every coupling either side of it.

### 9.3 `OPEN-AC-3` (cross-family comparison) — unchanged, and now precisely bounded

This task supplies **no** cross-family comparison and cannot: §4.1
records that the absolute potential zero is not fixed by the frozen
material even within the scalar family. **`OPEN-AC-3` therefore needs at
minimum two things that do not exist yet** — an absolute normalisation
for `V_red(0; G)`, and a common HS/measure convention across families.
The within-scalar depth table is a lower bound on what a cross-family
comparison would need, not a step toward one.

---

## 10. Ambiguous, unsatisfiable, or what I would have specified differently

- **`interaction_decomposition` is not where §0 implies.** §0 attributes
  it to the freeze while the surrounding sentence discusses
  `CANONICAL_INTERACTION`; it is in the freeze (line 116). Minor, but I
  had to search for it, and a path-plus-line citation would have removed
  the doubt.
- **The Deliverable-4 conversion identity is written in the disputed
  symbol.** `(bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A),
  gamma5))**2` is true only once `gamma5` is fixed — which was exactly
  what the sources disagreed about. The rule intended to protect the
  pseudoscalar sign was itself expressed in the ambiguous token. **A
  conversion rule should be stated in terms of an explicitly-defined
  operator**, e.g. by writing out `gamma(0)gamma(1)gamma(2)gamma(3)`.
- **Deliverable 2's STOP condition assumes the frozen matrix and "your
  matrix" are the same kind of object.** They differ by where the
  crossing sign sits, which is a convention question, not an algebra
  error — yet a literal reading makes 21 entries a STOP. **The criterion
  should say which convention the frozen table is in**, or ask for the
  comparison in both forms as I have reported it.
- **`d_max` is defined as "the minimum number of decimal places
  explicitly stored"**, which for float output is a property of the
  serialiser, not of the data. I fixed 12 decimals explicitly and said
  so. A future specification should state the stored precision itself
  rather than deriving it from the artifact.
- **The A5 scan term `artifact` is near-unusable in this repository.**
  Every governance document in this programme uses "artifact" in its
  ordinary sense — "the results artifact", "authority artifact" — dozens
  of times. It will dominate the hit list and bury the term that matters
  (`doubler artifact`). **I would scan for `doubler artifact` and
  `is an artifact` instead**, which target the characterisation without
  the noise.
- **The blind-fixation protocol worked and is worth keeping.** It cost
  almost nothing — one extra scratch file and a digest — and it is the
  only reason the independence claim in §3.1 is checkable rather than an
  attestation. The one thing that made it awkward is that the
  conventions and the matrix share a line in the freeze; **a future
  freeze should put normative conventions and derived results in
  separate files**, so "read the conventions" can be an atomic act.
