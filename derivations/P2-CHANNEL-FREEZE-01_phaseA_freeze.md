# P2-CHANNEL-FREEZE-01 — Phase-A algebraic freeze

**Status:** Phase-A freeze only; no SI-2 calculation or Phase-B metric is
frozen here.  The governing source is
`derivations/CANONICAL_INTERACTION.md`, §2, SHA-256
`27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`;
ratification evidence is `reports/2026-07-25_canonical-interaction_evidence.md`.

## §A — Canonical interaction

The governing source designates the U(N) chiral NJL interaction.  Its §2
definitions are: `ψ_{aα}` has Dirac index `α=1…4` and internal index
`a=1…N`; `Tr[λ^A λ^B]=2δ^{AB}` and `λ^0=sqrt(2/N)·1_N`; and

```
S^A = Sum_{a,b=1}^N Sum_{α,β=1}^4 psibar_{aα}(λ^A)_{ab}(1)_{αβ}ψ_{bβ}
P^A = Sum_{a,b=1}^N Sum_{α,β=1}^4 psibar_{aα}(λ^A)_{ab}(iγ5)_{αβ}ψ_{bβ}
L = Sum_a psibar_a(iγ^μ∂_μ)ψ_a + (G/(2N)) Sum_{A=0}^{N**2-1}[S^A**2+P^A**2].
```

Thus `G>0` is the sole independent four-fermion coupling; `N` remains
symbolic and `Λ=a**-1` is a regulator scale, not a channel coupling.  The
historical `Lgen` and `L0` forms are superseded shorthand as governed by that
source, not re-adjudicated here.

## §B — Independent coordinates and redundancies

The machine companion fixes the interaction as `G` times one invariant
generator sum.  Therefore the microscopic interaction-coordinate rank is one:
varying `G` changes the canonical action, whereas every Fierz coefficient is
fixed by the crossing map below.  Fierz representations are redundant
coordinates for the same interaction and cannot be scanned separately.

> A parameter counts as a genuinely free microscopic coordinate only if varying it changes the canonical action itself. Changing HS normalization, field rescaling, basis choice, Fierz representation, or a redundant parametrization does not create a new scan coordinate.

| genuine microscopic coordinate | exact expression | scan eligible |
| --- | --- | --- |
| `G` | `G` | yes |

| auxiliary representation parameter | reason | scan eligible |
| --- | --- | --- |
| `HS_scale` | HS normalization / field rescaling | no |
| `Fierz_basis` | basis choice / crossing representation | no |
| `g_c` per channel | rejected T1 multi-coupling extension | no |

The crossing-closed scaffolding is `S,P,V,A,T`; its coefficients are fixed,
not free or merely constrained-manifold parameters.  The source interaction
has support only on the generator-sum `S` and `P` terms; the other families are
required Fierz/HS representations and candidate kernel fields.

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
{"basis_order":["S","P","V","A","T"],"basis_elements":[{"basis_id":"S","expression":"Id4","component_rule":"single"},{"basis_id":"P","expression":"gamma5","component_rule":"single"},{"basis_id":"V","expression":"gamma(mu)","component_rule":"mu=0..3"},{"basis_id":"A","expression":"I*gamma(mu)*gamma5","component_rule":"mu=0..3"},{"basis_id":"T","expression":"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu)/2)","component_rule":"0<=mu<nu<=3"}],"conventions":{"metric_signature":["1","1","1","1"],"gamma5_definition":"gamma(0)*gamma(1)*gamma(2)*gamma(3)","sigma_definition":"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2","dirac_trace_normalization":"trace(Id4)=4","un_generator_normalization":"trace(lam(A)*lam(B))=2*KroneckerDelta(A,B)","grassmann_crossing_sign":"-1","singlet_traceless_order":["singlet","traceless"],"compound_index_order":["dirac_family","internal_family","component"]},"matrix_rational":[["1/4","1/4","1/4","1/4","1/4"],["1/4","1/4","-1/4","-1/4","1/4"],["1","-1","-1/2","1/2","0"],["1","-1","1/2","-1/2","0"],["3/2","3/2","0","0","-1/2"]]}
```

## §D — HS/K_ij inclusion

The complete bilinear basis is scaffolding; interaction support is the two
canonical generator sums; candidate fields are the full `S,P,V,A,T` indexed
families.  Inclusion precedes dynamics: condensation is a later SI-1 question.

> Previously adjudicated negative results may exclude a channel only if the cited result proves that the corresponding HS field is absent, algebraically redundant, forbidden by the fixed symmetries, or consistently decoupled from every admissible background and from the complete quadratic kernel. Failure of one proposed phenomenological role is not sufficient for exclusion.

> Every non-redundant HS field supported by the canonical interaction remains in the candidate K_ij mixing set unless exclusion is affirmatively proven under the exclusion rule. Absence of an implementation, absence of a known condensate, computational convenience, or failure of one phenomenological role is not evidence for exclusion.

No exclusion is asserted: the tensor Kalb–Ramond result is not an exclusion
from mixing.  Indexed component descriptors expand symbolically in `N`; their
total is `16*N**2`, keeping component count distinct from family rank.

```json
{"canonical_interaction":{"expression":"(G/(2*N))*Sum(bilinear(lam(A),Id4)**2+bilinear(lam(A),I*gamma5)**2,(A,0,N**2-1))","source_path":"derivations/CANONICAL_INTERACTION.md","source_sha256":"27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81"},"interaction_coordinates":[{"coordinate_id":"G","expression":"G","classification":"genuine_microscopic","scan_eligible":true}],"auxiliary_parameters":[{"parameter_id":"HS_scale","classification":"auxiliary_representation","scan_eligible":false,"reason":"HS normalization"},{"parameter_id":"Fierz_basis","classification":"auxiliary_representation","scan_eligible":false,"reason":"Fierz representation"}],"interaction_decomposition":[{"family_id":"S","operator_expression":"Sum(bilinear(lam(A),Id4)**2,(A,0,N**2-1))","coefficient":"G/(2*N)","support":true},{"family_id":"P","operator_expression":"Sum(bilinear(lam(A),I*gamma5)**2,(A,0,N**2-1))","coefficient":"G/(2*N)","support":true}],"stated_ranks":{"interaction_coordinate_rank":"1","fierz_family_rank":"5","kij_component_count":"16*N**2"},"hs_field_families":[{"family_id":"S","components":["S[A=0..N**2-1]"],"candidate_for_kij":true},{"family_id":"P","components":["P[A=0..N**2-1]"],"candidate_for_kij":true},{"family_id":"V","components":["V[mu=0..3,A=0..N**2-1]"],"candidate_for_kij":true},{"family_id":"A","components":["A[mu=0..3,A=0..N**2-1]"],"candidate_for_kij":true},{"family_id":"T","components":["T[0<=mu<nu<=3,A=0..N**2-1]"],"candidate_for_kij":true}],"kij_registry":[{"field_label":"sigma[A]","family_id":"S","component_id":"S[A=0..N**2-1]","included":true,"exclusion_id":null},{"field_label":"pi[A]","family_id":"P","component_id":"P[A=0..N**2-1]","included":true,"exclusion_id":null},{"field_label":"V[mu,A]","family_id":"V","component_id":"V[mu=0..3,A=0..N**2-1]","included":true,"exclusion_id":null},{"field_label":"A[mu,A]","family_id":"A","component_id":"A[mu=0..3,A=0..N**2-1]","included":true,"exclusion_id":null},{"field_label":"T[mu,nu,A]","family_id":"T","component_id":"T[0<=mu<nu<=3,A=0..N**2-1]","included":true,"exclusion_id":null}],"exclusions":[]}
```

The second block is the sole machine input for coordinates, decomposition,
ranks, families, registry, and provenance; no prose parsing is permitted by
the checker.  It must equal the independently parsed machine companion’s
canonical expression, and its decomposition must reconstruct that expression.

## §E — Paper-3 vector pin

`P2-BETAV-RECON-01` is PROPOSED, so the frozen path is `P3-C-001` /
`P3-FIERZ-01` at `8c363ef08368f5c022278ea5f36e01496be3d5ca`:
`G_omega=-G/N`, repulsive, with `D_00=g_0/(1+g_0Pi_V)->1/Pi_V`.
“Paper 3 pins the vector-channel coupling, sign, pole/screening conventions and admissible vector-sector input. The actual contribution of that channel to the mixed gravitational kernel remains a Paper 2 SI-2 computation and is not imported as already known.”

The betaV records remain NUMREPRO INCONCLUSIVE, CIRC INCONCLUSIVE
(insufficient resolving power), and historical criterion NOT MET; `-3.2(5)`
remains quarantined and unpromoted.

## §F — Phase-B contract (deferred)

From registered `P2-MULTIPHASE-GRAV-01`: CLEAN PASS requires a stable positive
measure healthy region; CONDITIONAL PASS is fine-tuned and not a theoretical
success; FAIL means every admissible phase has a negative Newtonian coupling,
negative-residue physical pole, unavoidable ghost/tachyon, or no viable
long-range mode.  HealthyGravity requires the full frozen-channel `K_ij`, a
long-range spin-2/Newtonian pole, positive physical-pole residue, no ghost or
tachyon, correct Newtonian sign, and stationary dynamically stable phase.
Phase B must separately preregister its domain, post-constraint measure,
gap-map, robust-neighbourhood rule, branches, sampling, resolution, volume CI,
boundaries and near-threshold handling.  It may not be drafted until this Phase
A branch is merged; the v1 scan range, volume floor, and robustness values have
no standing.

## §G — Integrity

Quoted/frozen sources: canonical markdown SHA above; machine companion
`derivations/CANONICAL_INTERACTION.json` SHA-256
`f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1`;
recovered Fierz source `scripts/recovered_2026/batch2/fierz_verify.py`;
and `GATES.md`.  This is a freeze without a verdict.  Adding a channel is an
AE-4 extension.  The two-phase split exists because metric rules require the
independent coordinates frozen here.  channel inclusion/exclusion is justified ONLY by the algebra and symmetry of the fixed interaction and by adjudicated results meeting the exclusion rule in §D. Nothing in this freeze may reference what would help or hurt SI-2's outcome.
