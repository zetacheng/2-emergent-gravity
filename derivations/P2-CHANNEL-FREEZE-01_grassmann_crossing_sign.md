# Derivation note — `P2-CHANNEL-FREEZE-01`: the Grassmann crossing sign

**Kind:** a single-question derivation. It fixes the analytic content
**before any output is produced**, so the algebra is reviewable before
the result can influence it.

**This is a computation, not a ruling.** It determines what the algebra
gives. Whether the Phase-A freeze is then amended, and how, is a PI
decision outside this task. No frozen artifact, no checker and no
mutation suite is modified.

Authority: `specs/2026-08-07T1159Z_grassmann-crossing-sign.md`.

---

## 0. Conventions — frozen, not chosen

From `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (SHA-256
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`):
Euclidean `metric_signature (1,1,1,1)`; `gamma5 =
gamma(0)*gamma(1)*gamma(2)*gamma(3)`, Hermitian with `gamma5^2 = Id4`
(PI ruling of 2026-08-07); `dirac_trace_normalization trace(Id4) = 4`;
`un_generator_normalization trace(lam(A) lam(B)) = 2 delta_AB`;
`grassmann_crossing_sign: -1`; `basis_order [S, P, V, A, T]` with
`S = Id4`, `P = gamma5`, `V = gamma(mu)`, `A = I*gamma(mu)*gamma5`,
`T = I*(gamma(mu)gamma(nu) - gamma(nu)gamma(mu))/2`.

The chiral projectors are frozen by the specification, not selected
here:

    P_L = (Id4 - gamma5)/2        P_R = (Id4 + gamma5)/2

Every convention this derivation needs is declared. Nothing had to be
supplied by the executor, so no convention gap is reported.

## 1. The Grassmann exchange sign — what is computed

### 1.1 The monomial and the frozen permutation

Spinor indices are `alpha beta gamma delta`; internal indices are
`i j k l`. No index letter carries two roles. The four-fermion monomial
is

    ( psibar^{i}_{alpha}  Gamma_{alpha beta}  lam^{A}_{ij}  psi^{j}_{beta} )
    ( psibar^{k}_{gamma}  Gamma_{gamma delta} lam^{A}_{kl}  psi^{l}_{delta} )

The four Grassmann objects, labelled in the order written:

    1 = psibar^{i}_{alpha}    2 = psi^{j}_{beta}
    3 = psibar^{k}_{gamma}    4 = psi^{l}_{delta}

**Starting Grassmann order** (normative):

    psibar_1  psi_2  psibar_3  psi_4

**Final Grassmann order** (normative), being the pairing 1–4, 3–2:

    psibar_1  psi_4  psibar_3  psi_2

`Gamma`, `lam^A` and all index contractions are ordinary commuting
c-number coefficients. **Only the ordering of the four Grassmann objects
carries a sign**, so the whole question reduces to the parity of the
permutation taking the first sequence of labels to the second.

**The permutation is `(1,2,3,4) -> (1,4,3,2)`**, i.e. the transposition
exchanging the objects in positions 2 and 4 — objects `psi_2` and
`psi_4`. `psibar_1` and `psibar_3` do not move. A transposition is odd,
so the expected parity is `-1`; the derivation below obtains it by
explicit adjacent anticommutations rather than by citing parity.

### 1.2 The anticommutations to be performed

Every Grassmann object is odd, so exchanging any adjacent pair
contributes exactly `-1`. Three adjacent exchanges suffice, and each is
recorded with its own sign:

    step 1   move psi_2 past psibar_3
    step 2   move psi_2 past psi_4
    step 3   move psi_4 past psibar_3

The product of the three signs is the operator-level crossing sign
`s_G`. **The result is reported as computed, not as expected**, and is
then compared with the declared `grassmann_crossing_sign = -1`.

The calculation is carried out twice and independently in the
accompanying script: once by explicit step-by-step adjacent
anticommutation as above, and once by an independent permutation-parity
computation on the label sequence. **They must agree**; disagreement
would be a defect in the calculation, not a result.

## 2. The storage question — a separate question, and a test

The explicit calculation of §1 determines `s_G` unambiguously as an
**operator-level** fact. **It does not determine whether the frozen
`matrix_rational` already stores that sign.** That is a question about
the matrix's defining kernel equation — whether the freeze intends

    K_exch = M . K_direct           (matrix stores the sign)
    K_exch = s_G . M . K_direct     (sign applied on use)

which is a representation convention, not an algebraic fact.

**The numerical equality of an unsigned reconstruction with
`matrix_rational` does NOT settle it.** That equality is consistent with
either convention: it establishes that the tabulated entries match a
signless construction, not that the defining equation omits the sign.
This derivation therefore does not use that equality as evidence for the
storage convention, and the accompanying test asserts that the storage
verdict is not derived from it.

**The test performed** is an inspection of the frozen material for a
defining kernel equation: the freeze document, its embedded JSON block,
and the standalone `results/P2-CHANNEL-FREEZE/fierz_matrix.json`. If no
such equation is present, the storage convention is reported as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` with the inspected text
quoted, which is a satisfactory outcome and not a failure.

## 3. The chiral cross-check — structure, not sign

Independently of `s_G`, the chiral content of the direct and exchanged
forms is a structural check on the rearrangement. It is **sign-blind**:
an overall sign multiplies all four coefficients equally, so this check
cannot and does not bear on §1.

Write the chiral bilinears with the frozen projectors. For the scalar
channel, with `S_L = psibar lam P_L psi` and `S_R = psibar lam P_R psi`:

    S = psibar lam psi        = S_L + S_R
    P = psibar lam gamma5 psi = S_R - S_L

so that the direct interaction, **after the already-ratified
`I*gamma5 -> gamma5` basis conversion**, is `S^2 - P^2`. For the current
channel, with `J^L_mu = psibar gamma_mu P_L psi` and
`J^R_mu = psibar gamma_mu P_R psi`, and with the frozen `A` basis
element `I*gamma(mu)*gamma5`:

    V_mu = psibar gamma_mu psi              = J^L_mu + J^R_mu
    A_mu = psibar (I gamma_mu gamma5) psi   = I (J^R_mu - J^L_mu)

The four coefficients `LL`, `LR`, `RL`, `RR` are reported for both the
direct scalar combination `S^2 - P^2` and the exchanged current
combination `V^2 + A^2`, under the symmetric split in which a
`J^L . J^R` product is written half as `LR` and half as `RL`.

`S^2 - P^2` denotes the canonical interaction after the ratified basis
conversion. **It is not a new interaction choice**, and no interaction
is selected by this note.

## 4. The checker's double application — characterised, not modified

`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:462` computes

    computed_fierz = (sign * projector * crossing * embedding).T * sign

with `sign` a scalar `sp.Integer(+-1)`. Transposition does not act on a
scalar factor, so the two occurrences multiply to `sign^2 = +1`. The
accompanying script confirms this **by direct substitution**, evaluating
the expression for `sign = -1` and `sign = +1` and reporting both
outputs.

**The checker is not modified.** Nor is the freeze, nor the mutation
suite; the absence of a mutation covering `grassmann_crossing_sign` is a
known gap and belongs to a separate task.

## 5. What this note does NOT conclude

- **It does not rule on how the freeze should be corrected**, or whether
  it should be.
- **It does not select a storage convention** where the frozen material
  does not fix one.
- **It does not infer the storage convention from numerical equality**
  of an unsigned reconstruction with `matrix_rational`.
- **It does not re-derive the `P2-PHASE-01` induced coefficients.**
  Their magnitude and structure are already established there; this note
  bears only on their sign, and only to the extent that §2 leaves that
  contingent.

## 6. Exclusions

The quarantined `-3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and
the historical Finding 5 extraction are **not** inputs. The complete
list of repository paths read is enumerated in the results artifact.
