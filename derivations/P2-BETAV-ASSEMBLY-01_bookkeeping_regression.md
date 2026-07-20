# Derivation note — `P2-BETAV-ASSEMBLY-01`: determinant-bookkeeping regression

**Kind:** numerical proxy / implementation regression. **This gate does NOT
close `P2-BETAV-CIRC-01`.**

## Why this gate exists (and what it is not)

The circularity question of `P2-BETAV-CIRC-01` — *did the historical Finding 5
lattice pipeline's projection/normalization secretly fix the ratio at `−3`?* —
cannot be answered here, because that pipeline is not in the repository
(`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`, verdict NOT LOCATED). This
gate answers only an **implementation-regression** question:

> Given the shared scalar lattice tadpole integral and the Proca determinant
> powers, does the assembly code preserve the `k`-dependence correctly, with no
> hardcoded `−3`?

## Construction

The induced `m²ln m²` coefficient of any mode is `β = −p (tr a_1/R) C`, where
`C` is the `m²ln m²` coefficient of the **one shared** lattice tadpole
`⟨φ²⟩_lat = ∫_BZ 1/(p̂²+m²)` (the `P2-BETA-01` scalar integral), extracted by
the same linear fit. For `det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)^k`:

```
β_B      = −(+½)(1/6) C            = −C/12
β_V(k)   = −(+½)(−1/3) C  −(−(k/2))(1/6) C  = C(2+k)/12
R_k      = β_V(k)/β_B = −(k+2).
```

## The decisive property: `C` cancels

Numerator and denominator are the **same** integral `C` times different rational
prefactors, so `C` cancels exactly. Consequences:

1. `R_k = −(k+2)` is **independent of the grid**; the ratio's variant spread is
   ~machine zero (verified: `≤ 9e-16` across `n=48/64`, shifts `0.5/0.25`, two
   windows). Numerator and denominator are **fully correlated** — the tolerance
   is a propagated *ratio* error, not two independent `β` scatters divided.
2. Because the shared integral cancels, this construction has **no power** to
   test the historical projection. It is bookkeeping realized on the lattice
   integral. It verifies only that the code reads `k` and does not hardcode `−3`.

## Mutation anchor (on the scalar determinant power)

Freezing the scalar determinant power to `1` (the analogue of a projection that
pins the compensating sector at the Proca value) collapses `R_k → −3` for every
`k`. The `k`-scan anchor then fails. **Caveat, stated in the gate:** this proves
only that the code reads `k`; it does **not** show any real pipeline is
non-circular.

## Pre-registered decision rule (for THIS gate only)

- `k`-dependence preserved (`R_k = −(k+2)`, `k=2 → −4`) and mutation collapses to
  `−3` → `PASS` (on its own, implementation-only terms).
- This gate can never return `FAIL`-for-circularity or `PASS`-for-non-circularity
  of the historical pipeline; those verdicts belong to `P2-BETAV-CIRC-01`, which
  is `SUSPENDED`.

## Implementing script

`scripts/betav_assembly.py` (`python -m scripts.betav_assembly`).
