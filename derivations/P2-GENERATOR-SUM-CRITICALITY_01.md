# Derivation note — generator-sum mean-field scalar criticality

**Kind:** original-model calculation (leading-order / mean-field gap
equation). Produced under the Researcher/Executor functions; records a
derivation, decides nothing. `P2-GAP-01` keeps `PASS`; `P2-PHASE-01` keeps
`PROPOSED`.

**Authority:** `specs/2026-08-08T2350Z_generator-sum-criticality.md`.
Committed before the production script per `AGENTS.md` rule 3.

## 0. Question

`P2-GAP-01` obtained `G_c = 1/(2·I_0)` from the **singlet-only** form
`L_int = G_N (ψ̄ψ)²`. Does that critical coupling transfer to the full
U(N) **generator-sum** canonical interaction under the same uniform
flavour-singlet scalar condensate? The `P2-PHASE-01` exploratory note
adopts `1 = 2 G I_0` verbatim from `P2-GAP-01`; the generator-sum
combinatorics behind it were never performed. This note performs them.

## 1. Frozen inputs (read-only; every value quoted, none supplied)

- **Canonical interaction** (Phase-A freeze §D machine block):
  `X = (G/(2N)) * Sum( bilinear(lam(A),Id4)**2 + bilinear(lam(A),I*gamma5)**2, (A,0,N**2-1) )`,
  the single independent coupling `G`.
- **Bilinears:** `S^A = ψ̄ (λ^A ⊗ 1_4) ψ`, `P^A = ψ̄ (λ^A ⊗ iγ_5) ψ`
  (freeze §A).
- **Generator normalisation** (freeze §C `un_generator_normalization`):
  `Tr(λ^A λ^B) = 2 δ^{AB}`, `A = 0 … N²−1`, singlet `λ^0 = √(2/N)·1_N`.
  The set `{λ^A}_{A=0}^{N²−1}` is a **complete Hermitian basis** of the
  N×N complex matrices (N² of them).
- **Dirac trace** (freeze §C): `trace(Id4) = 4`.
- **Exponent mapping** (`DECISION_LOG.md`, PI ruling 2026-08-08):
  `X` sits in the Boltzmann exponent, `exp(-S_E) ⊃ exp(+X)`; for a channel
  written `c·J²` the HS coefficient is `g = +2c`. This fixes the scalar
  channel as attractive (real auxiliary admissible), the sign under which
  `P2-GAP-01` PASSed.
- **Gap-equation machinery / `I_0`** (`P2-GAP-01`):
  `Σ = 2 G Σ B(Σ)`, `B(Σ) = ∫ d⁴p/(2π)⁴ 1/D(p;Σ)` the **untraced** scalar
  bubble; `I_0 ≡ B(0)`. `G` there is the channel coupling with the Dirac
  trace absorbed (`G = 4 G_N`), so the prefactor is exactly 2.
- **Condensate ansatz** (`P2-PHASE-01` exploratory note): uniform scalar
  self-energy `M̂ = a·M`, i.e. flavour-diagonal `⟨ψ̄_i ψ_j⟩ = δ_{ij} Φ`
  with a common per-flavour Dirac-traced amplitude `Φ` and a common
  dynamical mass `m` on every flavour.

## 2. The completeness relation is a consequence of the frozen facts

The rearrangement below needs `Σ_A (λ^A)_{ij} (λ^A)_{kl}`. This is **not a
new input**: it follows from the two frozen facts that `{λ^A}` is a
complete Hermitian basis and `Tr(λ^A λ^B) = 2 δ^{AB}`. Any N×N matrix `M`
expands as `M = Σ_A c_A λ^A` with `c_A = (1/2) Tr(λ^A M)`. Take `M = E_{lk}`
(the matrix unit, `(E_{lk})_{ij} = δ_{il} δ_{jk}`); then
`c_A = (1/2) Tr(λ^A E_{lk}) = (1/2) (λ^A)_{kl}`, so

    δ_{il} δ_{jk} = Σ_A (1/2) (λ^A)_{kl} (λ^A)_{ij}
    ⟹  Σ_{A=0}^{N²−1} (λ^A)_{ij} (λ^A)_{kl} = 2 δ_{il} δ_{jk}.      (C)

(C) is verified for `N = 2,3,4` against explicitly constructed bases by the
script — computed, not asserted. No `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`
arises: nothing outside the freeze is used.

## 3. Control (a): singlet-only `L_int = G_N (ψ̄ψ)²`

Single Dirac fermion, as in `P2-GAP-01`. Hartree (direct) self-energy from
`(ψ̄ψ)²` — two ways to place the mean field on the two bilinears, hence the
factor 2:

    Σ = 2 G_N ⟨ψ̄ψ⟩ .

The tadpole with Dirac trace explicit: `⟨ψ̄ψ⟩ = −tr_D ∫_p 1/(iγ·p + m) =
−4 m B(m)`; the 4 is `trace(Id4)`. Attractive sign (exponent ruling), so
the self-consistent dynamical mass obeys

    m = 2 G_N · 4 m B(m) = 8 G_N m B(m) .

Linearising at `m→0` (`B(0)=I_0`):

    1 = 8 G_N I_0 .                                              (a)

Absorbing the trace into the channel coupling `G = 4 G_N`:

    1 = 2 G I_0   ⟹   G_c = 1/(2 I_0) .                          (a′)

This reproduces `P2-GAP-01` exactly (prefactor 2). **Gate A2.** In the
coefficient-in-front normalisation (the coefficient literally multiplying
the interaction), the control critical coupling is `G_{N,c} = 1/(8 I_0)`.

## 4. Generator-sum (b): the scalar mean field

Only the scalar terms `(S^A)²` can feed a scalar condensate; under the
scalar ansatz `⟨P^A⟩ = 0`, so `(P^A)²` gives no scalar self-energy at
Hartree order. Work with `X_S = (G/(2N)) Σ_A (S^A)²`.

### 4.1 Which generators acquire a mean field (an output)

`⟨S^A⟩ = Σ_{kl} (λ^A)_{kl} ⟨ψ̄_k ψ_l⟩ = Σ_{kl} (λ^A)_{kl} δ_{kl} Φ =
Tr(λ^A) · Φ`. With `Tr(λ^0) = √(2/N)·N = √(2N)` and `Tr(λ^A) = 0` for the
traceless `A ≠ 0`:

    ⟨S^0⟩ = √(2N) · Φ ,      ⟨S^A⟩ = 0   (A ≠ 0).                 (M)

So **only the singlet generator `A = 0` acquires a non-zero mean field**
under the singlet ansatz — a determined result, not an assumption. The
traceless generators contribute nothing to the scalar tadpole because
their mean field vanishes.

### 4.2 The self-energy, `λ^A` sums carried explicitly

Hartree self-energy from `(G/(2N)) Σ_A (S^A)²`, factor 2 from the two
placements of the mean field:

    Σ_{ij} = 2 · (G/(2N)) · Σ_A (λ^A)_{ij} ⟨S^A⟩
           = (G/N) Σ_A (λ^A)_{ij} ⟨S^A⟩ .

Insert (M); only `A = 0` survives:

    Σ_{ij} = (G/N) (λ^0)_{ij} · √(2N) Φ
           = (G/N) · √(2/N) δ_{ij} · √(2N) Φ
           = (G/N) · √(2/N)·√(2N) · Φ δ_{ij}
           = (G/N) · 2 · Φ δ_{ij}                                (√(2/N)·√(2N) = √4 = 2)
           = (2G/N) Φ δ_{ij} .                                   (S)

Equivalently, the generator-independent identity
`Σ_A λ^A Tr(λ^A) = λ^0 Tr(λ^0) = √(2/N)·√(2N)·1_N = 2·1_N` — verified for
`N=2,3,4` by the script — makes the `N`-independence of that factor 2
explicit.

**Cross-check via completeness (C).** `Σ_A (S^A)² = Σ_A (ψ̄_iλ^A_{ij}ψ_j)
(ψ̄_kλ^A_{kl}ψ_l) = Σ_{ijkl}[Σ_A λ^A_{ij}λ^A_{kl}](ψ̄_iψ_j)(ψ̄_kψ_l) =
2 Σ_{ij}(ψ̄_iψ_j)(ψ̄_jψ_i)` by (C). The two Hartree contractions of this
Fierz-rearranged form each give `Σ_i Φ (ψ̄_iψ_i)`, so
`X_S → (G/(2N))·2·[2Φ Σ_iψ̄_iψ_i]`⁄(mean-field, one bilinear fixed) =
`(2G/N) Φ Σ_i ψ̄_iψ_i`, i.e. per-flavour mass `(2G/N)Φ`, identical to (S).
The two routes agree.

### 4.3 Gap equation and critical coupling

Each flavour carries mass `m = Σ_{ii} = (2G/N) Φ`, with the same Dirac
tadpole `Φ = ⟨ψ̄_iψ_i⟩ = −4 m B(m)` (trace 4 explicit). Attractive sign:

    m = (2G/N) · 4 m B(m) = (8/N) G m B(m) ,

linearise at `m→0`:

    1 = (8/N) G I_0   ⟹   G_c^{(b)} = N/(8 I_0) .                 (b)

The combinatorial factor produced by the generator sum is **8/N** (canonical
coupling, trace explicit): `2` (Hartree) × `4` (Dirac trace) × `(1/N)` from
the interplay of the canonical `1/(2N)` normalisation with the singlet
projection `√(2/N)·√(2N)=2`.

## 5. Comparison, ratio and transferability

Under one convention — each critical coupling measured as the coefficient
literally in front of its interaction, all computational conventions
(Euclidean, `I_0`, `tr 1_4 = 4`) identical:

    (a) G_{N,c}  = 1/(8 I_0)        [singlet-only, coefficient in front]
    (b) G_c      = N/(8 I_0)        [generator-sum, coefficient in front]
    ratio  R(N) = G_c^{(b)} / G_c^{(a)} = N .

This is the only convention giving the required `R(1) = 1` (at `N=1` the
generator sum is `X_S = G(ψ̄ψ)²`, the same interaction as the control, so
the criticalities must coincide — a consistency check the derivation must
pass). **`R(2)=2`, `R(3)=3`, `R(4)=4`.**

**Case: `N`-dependent** (the "more serious" case). The generator-sum
gap-equation prefactor is `8/N`, not the singlet-only `8`; equivalently
`G_c = 1/(2 I_0)` is a statement about the **trace-absorbed channel
coupling**, and it does **not** transfer to the **canonical coupling `G`**:
there the gap is `1 = (8/N) G I_0`, `G_c = N/(8 I_0)`.

**The step that differs** is §4.2: the canonical `1/(2N)` prefactor times
the singlet projection `⟨S^0⟩ = √(2N)Φ` and `(λ^0)_{ij} = √(2/N)δ_{ij}`
yields the per-flavour coefficient `2G/N` in place of the singlet-only
`2G_N` — an explicit `1/N` (with `G ↔ G_N` identified at `N=1`).

## 6. Consequence for the exploratory results (implication only)

The `P2-PHASE-01` exploratory note applied `1 = 2 G I_0` to the **canonical
coupling `G`**, i.e. it took `G_c = 1/(2 I_0)`. The value derived here for
the canonical coupling is `G_c = N/(8 I_0) = (N/4)·(1/(2 I_0))`. Hence every
position quoted in `G/G_c` (the `M̂=1` crossing at `G/G_c = 1.769`, the
282-row branch-depth table, the drafted domain bounds) carries an
`N`-dependent calibration factor `N/4`: correct only at `N = 4`, and
off by `1/2` at `N=2`, `3/4` at `N=3`. **The qualitative findings — local
stability, linear onset, a stable negative-mass branch — do not depend on
the scale and are expected to survive; only the `G/G_c` scale moves.** The
rescaling itself is a separate task and is **not** performed here.

## 7. Ansatz observation (no second ansatz supplied)

The frozen material fixes the **uniform flavour-singlet scalar condensate**
`⟨ψ̄_iψ_j⟩ = δ_{ij}Φ` (the exploratory `M̂ = aM`), and under it (M) shows
only the singlet generator condenses. An **adjoint** condensate
`⟨ψ̄_iψ_j⟩ ∝ (λ^B)_{ij}` (traceless `B`) would break the U(N) flavour
symmetry the freeze imposes and is **not** fixed by the frozen material;
whether the generator sum admits one is a different question, out of scope.
**The singlet ansatz is the only condensate the frozen material supports;**
no second ansatz is supplied here.

## 8. What this note does not do

Registers no gate, changes no status, ratifies nothing. It does not modify
`P2-GAP-01`, does not rescale the exploratory results, selects no HS channel
beyond the scalar one, and touches no diquark question. `P2-PHASE-01`
remains `PROPOSED`.

## 9. Repository inputs read (by path, read-only, at `51d4bbe1`)

- `derivations/P2-GAP-01_gap_criticality.md`
- `scripts/gap_criticality.py`
- `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`
- `derivations/P2-PHASE-01_scalar_stationary_exploratory.md`
- `DECISION_LOG.md` (exponent-mapping ruling, 2026-08-08)

The quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and the
historical Finding 5 extraction were **not** consumed.

## 10. Implementing script

`scripts/p2_generator_sum_criticality.py`
(`python -m scripts.p2_generator_sum_criticality`); results at
`results/P2-PHASE-01/generator-sum-criticality/criticality.json`.
