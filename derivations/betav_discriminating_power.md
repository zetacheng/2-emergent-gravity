# Derivation note — `P2-BETAV-CIRC-01`: does the lattice `β_V` test discriminate?

**Kind:** methodological audit (does a reported confirmation have the power it
claims?).

## The question (narrowed)

Paper 2 Finding 5 reports `β_V/β_B|_lat = −3.2(5)` against analytic `−3`
(eq. `betaVlat`) and says the mass scan "confirms the sign reversal
decisively". The sharp question is **not** "reproduce `−3.2(5)`". It is:

> **Can the extraction distinguish `−3` from anything else, or would it return
> `−3` regardless of the species fed in?** If the latter, Finding 5's lattice
> confirmation is circular and must be withdrawn *as a confirmation*.

## What the paper's extraction measures

From the paper (Finding 5): a lattice Proca field is coupled to the background
metric ("exact geometric coefficients `√g g⁻¹⊗g⁻¹` and `√g g⁻¹`, forward
differences, numerical `h`-derivatives"), validated to reproduce the flat Proca
eigenvalue structure `{ŝ²+m²(×3), m²}`; the longitudinal lattice mode "has
exactly no kinetic term (forward differences commute), realizing the
compensating-scalar structure of the Proca determinant at finite spacing". `Z_V`
is then the axis-TT slope, and `β_V` its `m²ln m²` coefficient from a mass scan.

So the extraction computes the **`m²`-log part of the axis-TT slope by numerical
metric-derivatives of `ln det` of the metric-coupled operator**. This is the
Seeley–DeWitt `a_1` (curvature response) realized numerically — it is *not* a
flat-space tadpole times an analytic factor (an earlier mischaracterization, now
corrected). The species content enters through the determinant structure.

## Where species dependence enters — the discriminating test

Generalize the Proca determinant to

```
Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²) · det^{+1/2}(Δ^{(0)}+m²)^k ,   k ∈ ℝ,
```

`k=1` being the physical Proca (one compensating scalar). The induced ratio,
from the `a_1` recipe (P2-HK-01 conventions), is

```
β_V(k)/β_B = −(k + 2)     [ k=1 → −3 ; k=0 → −2 ; k=2 → −4 ; k=3 → −5 ].
```

(Derivation: vector factor contributes `−p·K·(tr a_1/R) = −(½)K(−1/3)=+K/6`;
scalar`^k` factor `det^{+k/2}` has `p=−k/2`, contributing `+kK/12`;
`β_V(k)=K(2+k)/12`, and `β_B=−K/12`.) Computed in
`scripts/betav_discriminating.py`.

**The target ratio is structure-dependent.** Therefore an extraction that
returned `−3` for `k≠1` would be provably circular; a faithful extraction must
return `−(k+2)`. Because `k` enters the determinant *explicitly*, the paper's
numerical `h`-derivative of `ln det` genuinely depends on `k`, so at the level
of the coefficient the test **is discriminating**, not degenerate.

## What this settles, and what stays OPEN

- **Settled (analytic layer):** the `β_V/β_B` target is not a constant `−3`; it
  tracks the determinant structure. The lattice extraction, which differentiates
  a structure-dependent `ln det`, therefore has genuine discriminating power
  against an *error in the heat-kernel evaluation of the coefficient for a given
  structure*. Finding 5 is a legitimate numerical-vs-analytic cross-check.
- **Nuance (not circular, but limited):** the extraction shares its **input
  assumption** — the Proca determinant structure `{3 transverse + 1
  no-kinetic-longitudinal}` — with the analytic derivation (the paper *validates*
  the lattice operator against exactly that eigenvalue structure). So the test
  confirms the coefficient *given* the structure; it does **not** independently
  establish that the emergent vector *has* that structure. Finding 5's `−3`
  should be read as "confirmed for the Proca structure", not "structure-free".
- **OPEN (numerical layer):** reproducing the paper's specific `−3.2(5)` and
  testing its "longitudinal-sector `1/m²`-enhanced `m⁴ln m²` artifact"
  hypothesis (which drives heavy-mass windows "to ratios near `−5`" — note `−5`
  is exactly the `k=3` value, suggesting the artifact mimics an extra
  compensating power) requires implementing the curved-background lattice Proca
  determinant with numerical `h`-derivatives. That is a substantial
  implementation not completed in this sweep. Registered `OPEN` with the kill
  criterion below.

## Kill criterion (registered)

Implement the paper's extraction; feed it the `k≠1` structure. **If it returns
`−3` (or `−(2+1)`) regardless of `k`, the extraction is circular and Finding 5's
lattice confirmation is withdrawn as a confirmation.** If it returns `−(k+2)`,
the extraction discriminates and Finding 5 stands (as a coefficient check for
the Proca structure).

## Cross-repo consequence (flag only)

The companion `3-vector-sector` (claim `P3-C-004`, `VERIFIED`) quotes
`β_V/β_B = −3.2(5)` in its abstract. If this gate ever fires (extraction found
circular), that quotation is affected. **Flagged in `MIGRATION.md`; that
repository is not edited here.**

## Implementing script

`scripts/betav_discriminating.py` (`python -m scripts.betav_discriminating`).
