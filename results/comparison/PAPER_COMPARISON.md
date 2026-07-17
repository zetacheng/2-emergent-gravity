# Paper 2 v2.15 — independent recomputation vs. paper claims

**Gate scripts (all committed before this comparison):** `P2-HK-01`,
`P2-GAP-01`, `P2-BETA-01`. This file is the Task-6 comparison and is a
*separate, later* commit than the gates, per pre-registration discipline.

**Paper source.** `paper/emergent_gr_paper_v2_15.tex` was **not supplied** in
this repository at comparison time (only `paper/README.md` and
`paper/figures/` are present). The comparison is therefore made against the
specific numerical claims of Paper 2 v2.15 as transcribed into the task
specification and the reviewer-confirmed algebra. This substitution is recorded
here and in `DECISION_LOG.md`; if the `.tex` is later imported, the table
should be re-checked against it directly.

---

## ⚠️ DISAGREEMENTS (stated first)

### D1 — `β_F` differs by exactly a factor of 2 (Dirac vs Weyl). LOAD-BEARING.

Independent heat-kernel computation (`P2-HK-01`), for a standard **4-component
Dirac** fermion:

```
β_F = −1/(96 π²)   (magnitude 1.055e-3),   β_F/β_B = 2.
```

Paper 2 v2.15 uses `β_F = 1/(192 π²)` (magnitude 5.277e-4), i.e. `β_F/β_B = 1`.
The two disagree by **exactly a factor of 2**.

- **The disagreement:** the Seeley–DeWitt `a_1` trace for a Dirac operator is
  `tr a_1 = −R/3` (`dim = 4`, `E = R/4·𝟙₄`), giving `β_F = −1/(96π²) = 2 β_B`.
  This is unambiguous for a 4-component Dirac fermion.
- **Candidate reconciliation (recorded separately, not adopted):** the paper's
  value equals the contribution of a single **2-component Weyl** fermion
  (`dim = 2`, `tr a_1 = −R/6`, `β = −1/(192π²) = β_B`). If Paper 2's "fermion"
  and its "per unit 4N" normalization count 2-component (Weyl) fields, the
  paper value follows. The physical model ("lattice fermion fields", Wilson) is
  naturally 4-component Dirac, which would make the paper's `β_F` too small by
  2. **Reviewer must adjudicate the intended fermion content.**

**Downstream propagation of D1 (this is why it is load-bearing):**

| Quantity | Paper (Weyl `β_F`) | This repo (Dirac `β_F`) |
|---|---|---|
| `4 G_c β_F` (continuum, `G_c=8π²`) | `1/6` | `1/3` |
| `4 G_c β_F` (lattice, `G_c=5.86`) | `0.0125` | `0.0247` |
| survival `ξ_ind = 4G_cβ_F(3−L) > 1/6` ⟹ | `L < 2` ⟹ `m > 0.368 Λ` | `L < 2.5` ⟹ `m > 0.287 Λ` |

The paper's headline **survival window** (`m > e⁻¹Λ ≈ 0.368 Λ`) depends on
`4G_cβ_F = 1/6`, which holds only with the Weyl-normalized `β_F`. With a Dirac
fermion the window widens to `m > 0.287 Λ`. The reviewer-confirmed *algebra*
(`4G_cβ_F = 1/6 ⟹ L < 2`) is correct; what it consumes — the value of `β_F` —
is what disagrees.

### D2 — lattice `I_0` (and hence lattice `G_c`) differ by ≈1.2%.

```
I_0^lat  = 0.085388 ± 0.00002   (this repo)   vs   0.0844   (paper)   → +1.17%
G_c^lat  = 5.8556               (this repo)   vs   5.924    (paper)   → −1.15%
```

My value is numerically robust (grid refinement `n=64,96,128`; straight-vs-
offset-grid spread `3e-6`), so the ≈1.2% gap is **outside** my numerical
uncertainty. It is small and plausibly a minor integrand-definition or
numerical-precision difference in the paper (which itself quotes agreement "at
the 1% level"), but it is a genuine, recorded disagreement, not a match.

---

## Comparison table

| Quantity | Paper 2 v2.15 | This repository | Agreement | Notes |
|---|---|---|---|---|
| `β_B` (continuum, magnitude) | `1/(192π²)=5.28e-4` | `1/(192π²)=5.28e-4` (exact) | **agree** | exact; tol = exact rational |
| `β_B` (lattice) | "5% of continuum" | `5.44e-4` (`+3.1%` of continuum) | **agree** | within my `±9%` fit systematics; better than paper's 5% |
| `β_F/β_B` | `1` (from `β_F=1/192π²`) | `2` | **DISAGREE** | see D1; Dirac vs Weyl factor 2 |
| `β_V/β_B` (analytic) | `−3` | `−3` (exact) | **agree** | exact; Proca det structure |
| `β_V/β_B` (lattice) | `−3.2(5)` | not tested | **not tested** | see "Not computed" below |
| `β_B(ξ)` | (not transcribed) | `−(1−6ξ)/(192π²)`, ratio `1−6ξ` | **not tested** | paper number not available; conformal null at `ξ=1/6` |
| `G_c` (continuum) | `8π²/Λ²` (implied) | `8π²/Λ²`, `c=8` (exact) | **agree** | exact under `1=2G_cI_0` |
| `G_c` (lattice) | `5.924` | `5.8556` | **DISAGREE (≈1.2%)** | see D2 |
| `I_0` (lattice) | `0.0844` | `0.085388(20)` | **DISAGREE (≈1.2%)** | see D2; tol = my numeric unc. `2e-5` |
| `I_0` (continuum) | (only lattice given) | `1/(16π²)=6.33e-3` | **not tested** | consistent with derivation |
| `4 G_c β_F` (continuum) | `1/6` | `1/3` (Dirac) / `1/6` (Weyl) | **DISAGREE** | inherits D1 factor 2 |
| `4 G_c β_F` (lattice) | `0.0125` | `0.0247` (Dirac) / `0.0124` (Weyl) | **DISAGREE** | inherits D1 factor 2 |
| `ξ_ind` survival window | `m > 0.368 Λ` | `m > 0.287 Λ` (Dirac) / `0.368 Λ` (Weyl) | **DISAGREE** | inherits D1 factor 2 |

### Tolerance justifications

- **Exact rows** (`β_B` cont., `β_V/β_B`, `G_c` cont., `β_F/β_B`): symbolic;
  agreement means exact equality of rationals, disagreement means unequal
  rationals. No numerical tolerance.
- **`I_0`/`G_c` lattice:** tolerance = my own numerical uncertainty `2e-5`
  (`0.02%`), from grid refinement + offset-grid spread. The paper values lie
  `~1.2%` away, i.e. `~50σ` outside — recorded as disagreement.
- **`β_B` lattice:** tolerance = my own fit-systematics spread `±0.5e-4`
  (`±9%`), from window/ansatz variation. The continuum value lies `+3.1%`
  inside — recorded as agreement.
- None of these tolerances was chosen to make a paper number land inside; each
  is derived from this repository's numerics.

## Agreements (summary)

`β_B` (continuum, exact), `β_B` (lattice, few-percent), `β_V/β_B = −3` (exact),
`G_c` continuum (`c=8`, exact). The bosonic sector reproduces the paper
cleanly.

## Not computed this sweep (see gate `P2-BETAV-01`)

- **Lattice `β_V/β_B` (`−3.2(5)`).** A genuine lattice extraction requires
  putting a massive vector on the lattice and reading the induced graviton
  coefficient from a curved/weak-field background including the longitudinal
  (Stueckelberg) modes — where the paper reports lattice artifacts. A flat-space
  tadpole would only re-derive the analytic `−3` by construction (the flat-space
  loop integral is species-independent; the ratio lives entirely in the exact
  `a_1` traces), adding nothing. Deferred as a separate sweep. Evidence status:
  "paper text only, no archived provenance."

## Bottom line

The **bosonic** inputs (`β_B`, `β_V/β_B`, continuum `G_c`) reproduce Paper 2
cleanly. The **fermionic** input `β_F` disagrees by exactly a factor of 2
(Dirac vs Weyl), and because `β_F` feeds `4G_cβ_F` and the survival window,
that factor of 2 propagates into the paper's headline structural claim. The
lattice `I_0`/`G_c` differ at the `~1.2%` level. These disagreements are left
for reviewer adjudication; no convention was retrofitted to erase them.
