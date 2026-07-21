# Recovered historical lattice gravity engine (2026)

## What these files are

These files are **historical originals**, written to produce Paper 2's gravity
Findings, **recovered by the Principal Investigator in 2026** after having been
believed lost. They are landed here **verbatim** (unedited); each file's
`sha256` is recorded below and in `GATES.md`.

| File | Role | sha256 |
|---|---|---|
| `seagull_check.py` | **Root engine.** Ward-complete one-loop **fermion** graviton kernel (symmetric vierbein-link prescription, numerical `h`-derivatives). Produces `Z_h`, `xi_h`, `rho_v`, `M_Pl² = 4 N Z_h`. Engine behind **Finding 3** (universal coefficient) and **Finding 4** (`ξ_ind < 0`, the minimal-model induced-gravity result). | `6ec034e5a30e24d205c43c7dd0ea39c90a89f67c9db0da6e734a68862acefd90` |
| `boson_loop.py` | Condensate-scalar (real scalar) graviton loop; imports `seagull_check`. | `32d6a4e0b9cca8ec4debb80758f77d0574d98a299492cb1ab9cfe2fdd26c08c2` |
| `tt_check.py` | Fermion `⟨TT⟩` two-point; `Z_h`, `C6`/`xi_h`; self-contained. | `a40592a3b320cd9f118b3d96bd61abb10d5b20087d6b7a201dae5deabf90ba00` |
| `speed_check.py` | Emergent limiting-speed universality (light-cone); self-contained. | `8a374601161dd324795c2f1c9f7cc9d48031d83c5cc05e9896ae1e2814b1044c` |
| `structure_decomp.py` | O(q²) TT structure-decomposition tool; imports `seagull_check`. | `87d311fa4d86bb1c6862ace85bdd2c4a232db4f44e1662696f46c7226675fb9a` |
| `mlog_coeff.py` | **`m²ln m²` extractor + the 5 fixed TT projection recipes (`TT_RECIPES`)** and `fit_mlog`. Imports `seagull_check`, `boson_loop`. | `9f4343f14e70e57122e62d4aa12a3c8b7f708455af03fa74cd18d87751d107f3` |
| `proca_loop.py` | **βV body** — lattice Proca graviton loop (`Z_V(m)`). Imports `seagull_check`, `mlog_coeff`. | `b2361db94eae0995a5a81b16552bb8cd5b4afa049d015ea9401e3b8eac1bc8f5` |

Provenance artifact: `results/recovered-2026/fig_mlog.pdf` (historical scalar
`β_B` figure; `β_B^meas=+2.50e-4`, `β_B^cont=1/(384π²)=+2.64e-4`), sha256
`11cdd36c19b73f67200802a87e5720a7700239d2d94e081a5f118bc069bf565e`.

## βV pipeline: the "partial recovery" note is now RESOLVED

The earlier recovery recorded βV as **partial** because `mlog_coeff.py` (a
dependency of `proca_loop.py`) was missing. **`mlog_coeff.py` has now been
recovered.** The βV pipeline is **complete and runs**: `proca_loop.py` imports a
present `mlog_coeff`, and the scalar `β_B` and vector `β_V` sign reproduce (see
`results/recovered-2026/BETAV_REPRODUCTION.md`).

**Key structural fact (load-bearing for the circularity question).**
`TT_RECIPES` is **5 fixed, unit-normalized, `k`-independent** transverse-
traceless polarizations, used **identically** for the fermion, scalar, and
vector loops. It has **no mechanism to normalize the determinant power `k`
away**. Therefore the historical circularity worry for `P2-BETAV-CIRC-01`
(does the projection secretly force `−3`?) is **runnable and testable** — not
answerable by inspection alone, and not built into the projection. Whether the
extraction actually tracks `−(k+2)` is the job of the `k`-scan discrimination
test (a *separate* task); this recovery only makes it runnable.

## Why a dated recovery directory (not the main `scripts/` tree)

These files are placed in `scripts/recovered_2026/`, **not** silently merged
into the main `scripts/` tree, so that:

- the recovery is **auditable** — clearly a 2026 recovery of historical
  originals, not code that was always present;
- the honesty rule is visible: a recovered file counts as **provenance** only if
  it **reproduces the paper number** (see `results/recovered-2026/REPRODUCTION.md`
  and gate `P2-GRAV-ENGINE-RECOVERED-01`), or is explicitly labelled unverified;
- the recovered originals are never edited — their contents are frozen and
  hash-pinned above.

## Relation to `MIGRATION.md`

`MIGRATION.md` previously stated Paper 2 "has no legacy repository, no archived
script … nothing can be re-run." With the βV pipeline now complete, that
statement is **fully superseded for Paper 2's gravity sector**: the
fermion/scalar/TT graviton-kernel engine **and** the βV (Proca) pipeline are
recovered and run, reproducing the Finding 3/4 sign structure, the light-cone
numbers, the scalar `β_B`, and the vector `β_V` sign.

## Honesty note

Recovering these files **enables** verification; it does not by itself change
any historical verdict. No claim is upgraded or downgraded by the recovery
itself. In particular, `β_V/β_B = −3.2(5)` remains an **unpromoted, quarantined**
paper value: the βV magnitude at accessible grids is longitudinal-artifact
limited (see `BETAV_REPRODUCTION.md`), and the discrimination verdict is the
job of the separate `P2-BETAV-CIRC-01` `k`-scan — recovery ≠ verification.
