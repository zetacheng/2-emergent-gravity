# D-1 reflection-positivity literature coverage audit

Execution token: `2026-08-16T1952Z`  
Scope: literature coverage only; no candidate selection, ranking, or proof design  
Programme interaction: the frozen local `U(N)_L × U(N)_R` chiral NJL generator sum

## 1. Audit question and verdict vocabulary

This audit asks, separately for the naive, Wilson, staggered, and overlap kinetic families, whether a fetched source establishes both:

1. reflection positivity (RP) for the relevant kinetic formulation; and
2. preservation of RP after adding the programme's exact local interaction

\[
  \frac{G}{2N}\sum_A\left[(S^A)^2+(P^A)^2\right],\qquad G>0,
\]

with the source hypotheses mapped to the programme's still-unfrozen microscopic data. The interaction is the canonical interaction frozen in `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`; the kinetic operator, boundary conditions, and other measure details remain delegated or unfrozen.

Verdicts are deliberately conservative:

- `COVERED`: fetched evidence establishes both propositions for the programme formulation, with every material hypothesis mapped.
- `PARTIAL`: fetched evidence establishes a relevant RP result, but at least one material formulation, interaction, dimension, parameter, boundary-condition, or measure hypothesis is not matched.
- `NO COVERAGE FOUND`: no fetched work establishes a relevant result. This is a bounded search result, not a claim that no result exists.
- `NOT DETERMINABLE`: access preconditions failed or relevant works could not be fetched to usable depth.

Literature applicability is not an independent repository proof. A verdict concerns coverage, not candidate merit or physical suitability.

## 2. Source-depth ledger

Search-result snippets were used only to locate works and identifiers; they are not evidence. `FULL TEXT` means the article body was inspected. `ABSTRACT` means only an abstract/metadata record was accessible. `NOT FETCHED` means the work was encountered but not used to support a verdict.

| Key | Work and durable identifier | Depth | Role in this audit |
|---|---|---:|---|
| OS73 | K. Osterwalder and R. Schrader, “Axioms for Euclidean Green's Functions,” DOI [`10.1007/BF01645738`](https://doi.org/10.1007/BF01645738) | FULL TEXT | Reconstruction/background only; no action-specific coverage. |
| OS75 | K. Osterwalder and R. Schrader, “Axioms for Euclidean Green's Functions II,” DOI [`10.1007/BF01608978`](https://doi.org/10.1007/BF01608978) | FULL TEXT | Reconstruction/background only; no action-specific coverage. |
| OS78 | K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” DOI [`10.1016/0003-4916(78)90039-8`](https://doi.org/10.1016/0003-4916(78)90039-8) | ABSTRACT | Wilson gauge/fermion route evidence; abstract reports physical positivity, but article-level hypotheses were not available. |
| MP87 | P. Menotti and A. Pelissetto, “General Proof of Osterwalder-Schrader Positivity for the Wilson Action,” DOI [`10.1007/BF01221251`](https://doi.org/10.1007/BF01221251) | FULL TEXT | Load-bearing Wilson-family RP evidence; also explicitly discusses the `r=0` doubled-fermion limit for the earlier link-reflection argument. |
| N97 | H. Neuberger, “Exactly massless quarks on the lattice,” arXiv [`hep-lat/9707022`](https://arxiv.org/abs/hep-lat/9707022), DOI [`10.1016/S0370-2693(97)01368-3`](https://doi.org/10.1016/S0370-2693(97)01368-3) | FULL TEXT | Defines the overlap construction; not an RP theorem. |
| HJL98 | P. Hernández, K. Jansen, and M. Lüscher, “Locality properties of Neuberger's lattice Dirac operator,” arXiv [`hep-lat/9808010`](https://arxiv.org/abs/hep-lat/9808010), DOI [`10.1016/S0550-3213(99)00213-8`](https://doi.org/10.1016/S0550-3213(99)00213-8) | FULL TEXT | Exponential-locality evidence under gauge-field smoothness assumptions; not RP evidence. |
| KU10 | Y. Kikukawa and K. Usui, “Reflection Positivity of Free Overlap Fermions,” arXiv [`1005.3751`](https://arxiv.org/abs/1005.3751), DOI [`10.1103/PhysRevD.82.114503`](https://doi.org/10.1103/PhysRevD.82.114503) | FULL TEXT | Load-bearing overlap RP evidence for a specified free theory; includes a non-gauge chiral Yukawa example, not the programme interaction. |
| GK22 | T. Goto and T. Koma, “Spontaneous mass generation and chiral symmetry breaking in a lattice Nambu–Jona-Lasinio model,” arXiv [`2209.06031`](https://arxiv.org/abs/2209.06031), DOI [`10.1007/s00220-023-04858-8`](https://doi.org/10.1007/s00220-023-04858-8) | FULL TEXT | Staggered/Kogut–Susskind NJL route evidence in a Hamiltonian infrared-bound construction; not proposition-(ii) coverage for the Euclidean programme action. |
| FG26 | M. Fabbri and C. Goller, “Chiral Long-Range Order in three Euclidean Lattice Gross-Neveu Models,” arXiv [`2606.13075`](https://arxiv.org/abs/2606.13075) | FULL TEXT | Load-bearing interacting naive/staggered Euclidean RP evidence in two dimensions, with hypotheses that do not match the programme interaction. |
| STW81 | H. S. Sharatchandra, H. J. Thun, and P. Weisz, “Susskind fermions on a Euclidean lattice,” DOI [`10.1016/0550-3213(81)90200-5`](https://doi.org/10.1016/0550-3213(81)90200-5) | ABSTRACT | Staggered-formulation context only; not used as RP evidence. |
| L77 | M. Lüscher, “Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories,” DOI [`10.1007/BF01614090`](https://doi.org/10.1007/BF01614090) | NOT FETCHED | Encountered as transfer-matrix route evidence; not pursued because it does not by itself answer proposition (ii). |

Depth totals: 8 full texts, 2 abstract-only records, 1 encountered/not-fetched work, and 0 claims resting only on recollection. OS78 is the sole abstract-only item close to a load-bearing kinetic claim; because its detailed hypotheses were unavailable, it cannot support `COVERED`. No verdict below relies on STW81 or L77.

### 2.1 Applicability declaration for every fetched work

| Work | Candidates applicability-tested | Not an applicability candidate, and why |
|---|---|---|
| OS73 | None | Naive, Wilson, staggered, overlap: continuum reconstruction axioms are not action-specific RP or interaction-preservation theorems. |
| OS75 | None | All four: same class mismatch as OS73. |
| OS78 | Wilson | Naive, staggered, overlap: the accessible abstract identifies a Wilson gauge/fermion construction, not those formulations. |
| MP87 | Wilson; naive through the paper's explicit `r=0` discussion | Staggered and overlap: different operator classes. |
| N97 | None | All four: an overlap-definition paper is not an RP theorem; even for overlap it cannot bear on proposition (ii). |
| HJL98 | None | All four: locality is not RP; the overlap result therefore is not an applicability basis for proposition (ii). |
| KU10 | Overlap | Naive, Wilson, staggered: different operator classes. |
| GK22 | None for proposition-(ii) coverage; staggered `ROUTE EVIDENCE` only | Naive, Wilson, overlap: different formulation; staggered is Hamiltonian/infrared-bound route evidence rather than OS positivity of the programme Euclidean action. |
| FG26 | Naive; staggered | Wilson and overlap: different operator classes. |
| STW81 | None | All four: abstract-only formulation context supplies no inspected RP theorem; it is not used in a verdict. |

### 2.2 Seven-axis and theorem-hypothesis mapping

`MAPPED` below means the programme datum is frozen and shown to meet the source hypothesis. `FAIL` names a mismatch or an unfrozen datum. `UNKNOWN AT ABSTRACT DEPTH` cannot support coverage.

#### MP87 → Wilson

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `FAIL`: Wilson gauge/fermion action, not the programme's added four-fermion interaction. |
| 2. Reflection type | `FAIL`: site reflection is proved; programme reflection type is unfrozen. |
| 3. Lattice extent | `FAIL`: source finite-lattice/separation setup is not mapped to a frozen programme extent. |
| 4. Boundary conditions | `FAIL`: programme temporal boundary condition is unfrozen; adopting incompatible boundary data would make this basis unavailable. |
| 5. Locality assumptions | `MAPPED` only at family level: the Wilson operator is ultralocal; the exact programme operator parameters are not frozen. |
| 6. Measure/determinant | `FAIL`: source Grassmann/gauge measure and gauge-invariant observable algebra are not mapped to the programme non-gauge measure with the NJL term. |
| 7. Gauge content | `FAIL`: theorem is for a gauge theory; non-gauge specialization is plausible but is not frozen and demonstrated in the programme action. |

Theorem-specific hypotheses: four dimensions is `MAPPED`; Wilson operator normalization is `FAIL` (not convention-mapped); `r` is `FAIL` (programme value unfrozen); hopping parameter `K < 1/6` is `FAIL` (no programme `K`/mass mapping); gauge-invariant observables are `FAIL` (programme algebra unfrozen); arbitrary reflection-plane separation is source scope, not a programme defect; the programme coupling `G>0` is `FAIL` because the interaction is absent from the theorem. Applicability conclusion: `PARTIAL`, kinetic proposition only.

#### MP87 → naive

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `FAIL`: the `r=0` passage concerns the gauge/fermion kinetic proof, not the programme interaction. |
| 2. Reflection type | `FAIL`: the relevant passage invokes the earlier link-reflection proof; programme reflection type is unfrozen. |
| 3. Lattice extent | `FAIL`: no programme extent is frozen and mapped. |
| 4. Boundary conditions | `FAIL`: programme temporal boundary condition is unfrozen; an incompatible future choice would forfeit this basis. |
| 5. Locality assumptions | `MAPPED` at family level: naive fermions are ultralocal. |
| 6. Measure/determinant | `FAIL`: gauge/Grassmann measure and observable restrictions are not mapped to the programme NJL measure. |
| 7. Gauge content | `FAIL`: the cited result is in gauge theory and its non-gauge specialization is not fixed in the programme. |

Theorem-specific hypotheses: four dimensions is `MAPPED`; replacement `(r ± γ4)` with `0 ≤ r ≤ 1` and `r=0` is `MAPPED` at the doubled-family level; exact operator normalization is `FAIL`; mass/hopping domain is `FAIL` (not frozen/mapped); the exact `G>0` interaction is `FAIL` (absent). Applicability conclusion: `PARTIAL`, kinetic proposition only.

#### OS78 → Wilson (abstract-depth cross-check)

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `UNKNOWN AT ABSTRACT DEPTH`; abstract describes gauge fields and fermions, not the programme NJL term. |
| 2. Reflection type | `UNKNOWN AT ABSTRACT DEPTH`. |
| 3. Lattice extent | `UNKNOWN AT ABSTRACT DEPTH`. |
| 4. Boundary conditions | `UNKNOWN AT ABSTRACT DEPTH`; programme temporal boundary condition is also unfrozen. |
| 5. Locality assumptions | `UNKNOWN AT ABSTRACT DEPTH`. |
| 6. Measure/determinant | `FAIL`: detailed measure hypotheses were not fetched and cannot be mapped. |
| 7. Gauge content | `FAIL`: source is a gauge theory; non-gauge specialization is not established from the abstract. |

Theorem-specific hypotheses: dimension, operator normalization, `r`, mass/hopping domain, coupling range, finite-volume conditions, and observable algebra are all `UNKNOWN AT ABSTRACT DEPTH`; the exact programme interaction is not reported. Applicability conclusion: relevant corroboration only, never a `COVERED` basis.

#### FG26 → naive

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `FAIL`: interacting, but scalar Gross–Neveu rather than the frozen scalar-plus-pseudoscalar generator sum. |
| 2. Reflection type | `FAIL`: bond/link reflection is used; programme reflection is unfrozen. |
| 3. Lattice extent | `FAIL`: finite 2D torus with size divisibility conditions; programme extent is unfrozen and target dimension is 4D. |
| 4. Boundary conditions | `FAIL`: anti-periodic in both directions; programme temporal boundary condition is unfrozen, and a different future ruling would exclude the theorem. |
| 5. Locality assumptions | `MAPPED` at family level: naive kinetic and local interaction are ultralocal. |
| 6. Measure/determinant | `FAIL`: RP is for a specified effective bosonic measure after Hubbard–Stratonovich transformation; no equality/factorization map to the programme measure is supplied. |
| 7. Gauge content | `MAPPED`: both are non-gauge models. |

Theorem-specific hypotheses: dimension 2 is `FAIL` against 4; even `N` is `FAIL` against symbolic unrestricted `N`; lattice length divisibility is `FAIL` (unfrozen); operator normalization is `FAIL`; scalar coupling `λ>0` is sign-compatible with `G>0` but `FAIL` because the operators differ; determinant reflection invariance (H1), local Grassmann representation/factorization (H2), and kinetic cross-term decomposition (H3) are each `FAIL` because none is established for the programme action. Applicability conclusion: `PARTIAL`.

#### FG26 → staggered

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `FAIL`: interacting, but scalar Gross–Neveu rather than the programme generator sum. |
| 2. Reflection type | `FAIL`: source bond/link reflection is not mapped to a frozen programme reflection. |
| 3. Lattice extent | `FAIL`: finite 2D torus and size restrictions versus a 4D target with unfrozen extent. |
| 4. Boundary conditions | `FAIL`: anti-periodic in both directions; programme temporal condition is unfrozen and may later be incompatible. |
| 5. Locality assumptions | `MAPPED` at broad family level: source staggered kinetic term and interaction are ultralocal; exact taste realization remains unmapped. |
| 6. Measure/determinant | `FAIL`: effective bosonic determinant measure is not mapped to the programme Grassmann/auxiliary-field measure. |
| 7. Gauge content | `MAPPED`: both are non-gauge. |

Theorem-specific hypotheses: dimension 2 is `FAIL`; even `N` is `FAIL`; lattice length conditions are `FAIL`; exact staggered phases/operator normalization and flavour-to-taste map are `FAIL`; `λ>0` does not map the different interaction; H1 determinant reflection invariance, H2 local Grassmann factorization, and H3 kinetic cross-term decomposition are all `FAIL` for lack of a programme-action verification. Applicability conclusion: `PARTIAL`.

#### KU10 → overlap

| Common axis | Source result and programme mapping |
|---|---|
| 1. Free/interacting | `FAIL`: free overlap RP is proved and a different chiral Yukawa interaction is treated; the programme four-fermion interaction is not. |
| 2. Reflection type | `FAIL`: link reflection is proved; programme reflection type is unfrozen. |
| 3. Lattice extent | `FAIL`: finite `[-L+1,L]^4`; programme extent is unfrozen. |
| 4. Boundary conditions | `FAIL`: anti-periodic time and periodic space; programme temporal condition is unfrozen, and an incompatible ruling would exclude the theorem. |
| 5. Locality assumptions | `MAPPED` at family level: overlap is non-ultralocal and exponentially local in its domain; programme kernel/domain remains unfrozen. |
| 6. Measure/determinant | `FAIL`: source fermionic positivity cone and Yukawa measure are not mapped to an auxiliary-field representation of the programme NJL determinant. |
| 7. Gauge content | `MAPPED`: source is explicitly non-gauge, as are the candidate actions. |

Theorem-specific hypotheses: dimension 4 is `MAPPED`; source overlap normalization is `FAIL` (not convention-mapped); kernel parameter `0 < m ≤ 1` is `FAIL` because programme `M0` is unfrozen; finite even extent and boundary data are `FAIL`; strict locality of interactions holds for the source Yukawa term but is `FAIL` as a compositional bridge because the programme four-fermion/auxiliary-field measure is different; no programme mass or auxiliary coupling map is frozen. Applicability conclusion: `PARTIAL`.

### 2.3 Route evidence kept outside proposition (ii)

GK22 and the unfetched L77 transfer-matrix work are `ROUTE EVIDENCE` only. GK22's Hamiltonian Kogut–Susskind infrared-bound use of reflection positivity and L77's transfer-matrix construction contributed to no proposition-(ii) verdict. No transfer-matrix-only statement was treated as OS positivity of the programme Euclidean action or measure.

## 3. Repository baseline and the pre-audit gap

The earlier repository scope note contained three structured recollections and one explicit gap:

- L1 recalled OS reconstruction results, while correctly separating reconstruction from action-specific RP.
- L2 recalled a Wilson gauge/fermion RP route through Osterwalder–Seiler, but did not map the exact reflection or hypotheses.
- L3 named no staggered work and therefore was a literature gap rather than a claim.
- L4 named Neuberger and Hernández–Jansen–Lüscher, while correctly treating overlap definition/locality as distinct from RP.

This execution replaces none of the four open proof burdens. It does fill the L3 naming gap with a fetched, relevant theorem (FG26), but only at `PARTIAL` coverage because its formulation does not match the programme action.

## 4. Naive kinetic family

### Verdict: `PARTIAL`

#### Proposition (i): kinetic RP

MP87 reports that the earlier link-reflection Wilson-fermion proof continues to hold when its temporal projectors are replaced by `(r ± γ4)` for `0 ≤ r ≤ 1`, explicitly including `r=0`, the doubled-fermion case. This is directly relevant to a naive/doubled discretization and is full-text kinetic RP evidence. It is nevertheless not a complete mapping to the programme's naive candidate: the cited passage is a discussion of the earlier gauge-theory proof, not a new standalone theorem restated with the programme's finite-volume, boundary-condition, mass, and observable algebra conventions.

FG26 supplies independent full-text Euclidean evidence for a naive interacting lattice model. Its reflection construction is on a two-dimensional discrete torus, and its main RP result is formulated after a Hubbard–Stratonovich transformation through determinant reflection invariance, a local Grassmann representation/factorization, and a cross-reflection decomposition of the kinetic term. This confirms that naive fermions can participate in a rigorous interacting RP construction, but under a different microscopic model.

#### Proposition (ii): preservation under the programme interaction

No fetched work proves RP for the naive kinetic operator plus the exact four-dimensional `U(N)_L × U(N)_R` generator-sum scalar-and-pseudoscalar NJL interaction. FG26 treats a two-dimensional scalar Gross–Neveu interaction proportional to `(ψ̄ψ)^2`, assumes even flavour number, imposes anti-periodic boundary conditions in both directions, and uses its own effective-bosonic-measure formulation. Those hypotheses do not imply the programme interaction result.

#### Exact failures preventing `COVERED`

- **Interaction and symmetry:** FG26's scalar Gross–Neveu term and discrete chiral structure do not match the frozen generator sum containing both `S^A` and `P^A` with continuous `U(N)_L × U(N)_R` symmetry.
- **Dimension:** FG26 is two-dimensional; the programme target is four-dimensional.
- **Flavour domain:** FG26 requires even `N`; the programme leaves symbolic `N` without that restriction.
- **Boundary conditions and volume:** FG26 fixes a finite torus with anti-periodic conditions in both directions and divisibility conditions on its size; programme boundary conditions are unfrozen.
- **Measure/formulation:** the effective bosonic measure and factorization hypotheses are not mapped to the programme measure.
- **MP87 scope:** the relevant `r=0` statement belongs to a Wilson gauge-fermion link-reflection route and does not add the programme NJL interaction.

These are coverage failures, not negative statements about whether a suitable proof can be constructed.

## 5. Wilson kinetic family

### Verdict: `PARTIAL`

#### Proposition (i): kinetic RP

MP87 is full-text, action-specific evidence. It proves site-reflection OS positivity for the Wilson action with gauge fields and fermions, for gauge-invariant observables and arbitrary separation of the reflection plane, under a hopping-parameter condition `K < 1/6`. The paper explains its relation to the earlier link-reflection argument. OS78's accessible abstract independently reports a rigorous Euclidean lattice gauge/fermion construction and verification of physical positivity, but abstract depth is insufficient to recover all hypotheses and is used only as corroborating route evidence.

The kinetic result is therefore real and close to the programme Wilson family. It is not fully mapped: the programme dossier displays a conventional Wilson form and often illustrates `r=1`, but explicitly does not freeze `r`; it also does not freeze the mass/hopping parameter, boundary conditions, gauge specialization, or observable algebra needed to compare directly with MP87.

#### Proposition (ii): preservation under the programme interaction

Neither MP87 nor the abstract-only OS78 record treats the programme's local `U(N)_L × U(N)_R` generator-sum NJL term. A Wilson kinetic RP theorem does not automatically establish positivity after this additional four-fermion interaction; its reflection factorization and sign conditions must be checked for the exact interaction and measure. No fetched full text supplies that check.

#### Exact failures preventing `COVERED`

- **Wilson parameter:** the programme does not freeze `r`; the exact relation between its displayed operator and the source convention is therefore incomplete.
- **Mass/hopping domain:** MP87 assumes `K < 1/6`; no programme mass/hopping choice is frozen or mapped to this inequality.
- **Interaction:** the fetched Wilson theorems do not include the programme scalar-plus-pseudoscalar generator sum.
- **Boundary conditions and reflection:** programme boundary conditions are unfrozen, while link versus site reflection and finite-volume geometry matter to the source hypotheses.
- **Gauge/observable scope:** MP87 is stated with gauge fields and for gauge-invariant observables; the programme's intended non-gauge specialization and observable algebra have not been fixed and demonstrated to inherit the theorem.
- **Measure details:** microscopic measure normalization and reflection-factorization data remain delegated.

The evidence establishes a credible Wilson RP route, not full programme coverage and not a preference for Wilson fermions.

## 6. Staggered kinetic family

### Verdict: `PARTIAL`

#### Proposition (i): kinetic RP

FG26 fills the repository's prior L3 naming gap with a fetched theorem. It studies two-dimensional Euclidean naive and staggered Gross–Neveu models on discrete tori and proves reflection positivity of effective bosonic measures. The staggered model uses link/bond reflections and verifies the determinant-reflection, local-Grassmann-factorization, and kinetic cross-term conditions needed by its construction. This is direct Euclidean RP evidence for a named staggered formulation, not merely a generic recollection.

STW81 was available only at abstract depth and is retained as formulation context, not as evidence. GK22 gives a rigorous staggered/Kogut–Susskind NJL route in a Hamiltonian setting: it uses reflection positivity within an infrared-bound argument for a nearest-neighbour density interaction and notes a boundary hopping sign. That is useful route evidence, but it is not a theorem for the programme's Euclidean Grassmann action.

#### Proposition (ii): preservation under the programme interaction

The interacting theorem in FG26 is not for the programme interaction. Its ordinary staggered model is two-dimensional, uses a scalar Gross–Neveu interaction and discrete chiral structure, assumes even `N`, and fixes anti-periodic conditions in both directions. GK22 uses a Hamiltonian Kogut–Susskind model with a nearest-neighbour density interaction rather than the local generator-sum scalar-and-pseudoscalar term. Thus neither work establishes proposition (ii).

#### Exact failures preventing `COVERED`

- **Dimension:** FG26 is two-dimensional rather than four-dimensional.
- **Interaction and symmetry:** neither FG26's scalar Gross–Neveu term nor GK22's nearest-neighbour density interaction equals the programme's local `Σ_A[(S^A)^2+(P^A)^2]` interaction with continuous chiral symmetry.
- **Flavour/taste mapping:** FG26 assumes even `N`; the relationship among its flavours, staggered components/tastes, and the programme's symbolic `N` is not established.
- **Boundary conditions:** FG26 imposes anti-periodicity in both directions plus lattice-size divisibility; GK22 has a specific boundary hopping sign; the programme leaves boundary conditions unfrozen.
- **Formulation and measure:** FG26 proves positivity for an effective bosonic measure after a particular Hubbard–Stratonovich representation, while the programme's precise staggered action and measure are not frozen.
- **Hamiltonian versus Euclidean scope:** GK22's reflection-positive infrared-bound machinery cannot be substituted for an OS-positivity theorem for the programme Euclidean action without an explicit bridge.

L3 is therefore filled by a named and inspected result, but the full proof burden remains open.

## 7. Overlap kinetic family

### Verdict: `PARTIAL`

#### Proposition (i): kinetic RP

KU10 proves link-reflection positivity for free overlap fermions on a finite four-dimensional lattice. Its setup uses anti-periodic temporal and periodic spatial boundary conditions and an overlap-kernel parameter in the range `0 < m ≤ 1`. The proof is explicitly non-gauge. KU10 also extends the construction to a non-gauge chiral Yukawa model with strictly local interactions. This is direct, full-text overlap RP evidence and materially advances beyond the prior repository note, which had only the overlap definition and locality literature.

N97 defines the overlap construction, while HJL98 proves exponential locality of Neuberger's operator under stated kernel/gauge smoothness conditions. Neither paper proves RP. Locality is not interchangeable with reflection positivity, so these works do not strengthen the verdict beyond contextual parameter and formulation information.

#### Proposition (ii): preservation under the programme interaction

KU10's interacting example is a chiral Yukawa theory, not the programme's four-fermion NJL generator sum. The source does not establish that integrating in or out auxiliary fields yields the programme action with a reflection-positive measure under the programme conventions. In addition, the programme overlap kernel parameter `M0`, finite-volume boundary conditions, and precise measure remain unfrozen, so even the free theorem's hypotheses are not fully mapped.

#### Exact failures preventing `COVERED`

- **Kernel parameter:** KU10 assumes `0 < m ≤ 1` in its operator convention; the programme mentions but does not choose/freeze `M0`, and no convention mapping is fixed.
- **Boundary conditions:** KU10 fixes anti-periodic time and periodic space on a finite lattice; programme boundary conditions are unfrozen.
- **Interaction:** the KU10 chiral Yukawa example is not the local scalar-plus-pseudoscalar generator-sum four-fermion interaction.
- **Auxiliary-field/measure bridge:** no fetched source proves that a Hubbard–Stratonovich representation of the programme interaction meets KU10's positivity cone and factorization hypotheses.
- **Gauge scope:** KU10 is non-gauge; this matches a possible programme specialization only after that specialization is frozen, not before.
- **Definition/locality distinction:** N97 and HJL98 provide definition and locality, not action-specific RP.

The overlap route is supported for a specified free theory and a different interaction, but the programme result remains unproved.

## 8. Coverage matrix and burden accounting

| Kinetic family | Kinetic RP evidence | Exact programme interaction covered? | Verdict | Principal unmatched hypotheses |
|---|---|---:|---|---|
| Naive | MP87 `r=0` link-reflection discussion; FG26 2D interacting naive theorem | No | `PARTIAL` | 4D, exact `U(N)` scalar+pseudoscalar term, symbolic `N`, BCs, measure |
| Wilson | MP87 site-reflection theorem; OS78 abstract route evidence | No | `PARTIAL` | `r`, `K`/mass, exact interaction, BC/reflection, gauge/observable scope |
| Staggered | FG26 2D interacting staggered theorem; GK22 Hamiltonian route evidence | No | `PARTIAL` | 4D, exact interaction/symmetry, flavour/taste map, BCs, Euclidean measure |
| Overlap | KU10 free link-RP theorem and different Yukawa example | No | `PARTIAL` | `M0` convention/range, exact interaction, BCs, auxiliary-field measure bridge |

Verdict counts: `COVERED = 0`, `PARTIAL = 4`, `NO COVERAGE FOUND = 0`, `NOT DETERMINABLE = 0`.

Burden update: `0` of the four candidate proof burdens are replaced by literature applicability; `4` remain open in full. The staggered L3 literature-identification gap is filled only in the limited sense that a relevant named theorem is now available and inspected. It does not discharge either programme proposition.

## 9. Access and reproducibility note

For this execution, arXiv abstract and full-text links were reachable (tested with N97). The direct DOI safety route for N97 did not open, and its ScienceDirect publisher page returned HTTP 403; the arXiv copy supplied full-text depth. This contrasts with the historical first execution recorded in the handover, where all 12 scholarly hosts returned HTTP 403 and a non-scholarly control also returned HTTP 403, indicating a global sandbox block. Here, access varied by work and host, so every claim above is labeled at its actual per-work depth.

The audit is bounded by the works in the ledger. Absence of `COVERED` means no fetched source was shown to apply to the exact programme formulation; it is not an exhaustive non-existence claim. No candidate is selected, ranked, or recommended, and no proof route is designed here.
