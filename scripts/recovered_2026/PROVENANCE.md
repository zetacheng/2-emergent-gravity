# Recovered historical lattice gravity engine (2026)

## What these files are

These five files are **historical originals**, written to produce Paper 2's
gravity Findings, **recovered by the Principal Investigator in 2026** after
having been believed lost. They are landed here **verbatim** (unedited); each
file's `sha256` is recorded below and in
`GATES.md` (gate `P2-BETAV`… → `P2-GRAV-ENGINE-RECOVERED-01`).

| File | Role | sha256 |
|---|---|---|
| `seagull_check.py` | **Root engine.** Ward-complete one-loop **fermion** graviton kernel (symmetric vierbein-link prescription, numerical `h`-derivatives). Produces `Z_h`, `xi_h`, `rho_v`, `M_Pl² = 4 N Z_h`. Engine behind **Finding 3** (universal coefficient) and **Finding 4** (`ξ_ind < 0`, the minimal-model induced-gravity result). | `6ec034e5a30e24d205c43c7dd0ea39c90a89f67c9db0da6e734a68862acefd90` |
| `boson_loop.py` | Condensate-scalar (real scalar) graviton loop; imports `seagull_check`. | `32d6a4e0b9cca8ec4debb80758f77d0574d98a299492cb1ab9cfe2fdd26c08c2` |
| `tt_check.py` | Fermion `⟨TT⟩` two-point; `Z_h`, `C6`/`xi_h`; self-contained. | `a40592a3b320cd9f118b3d96bd61abb10d5b20087d6b7a201dae5deabf90ba00` |
| `speed_check.py` | Emergent limiting-speed universality (light-cone); self-contained. | `8a374601161dd324795c2f1c9f7cc9d48031d83c5cc05e9896ae1e2814b1044c` |
| `structure_decomp.py` | O(q²) TT structure-decomposition tool; imports `seagull_check`. | `87d311fa4d86bb1c6862ace85bdd2c4a232db4f44e1662696f46c7226675fb9a` |

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
script … nothing can be re-run." That statement is now **partially
superseded**: the fermion/scalar/TT **graviton-kernel engine is recovered and
runs**, and reproduces the paper's Finding 3/4 sign structure and the
light-cone universality numbers (see the reproduction check). This does **not**
extend to the βV (Proca) sector — the incomplete `proca_loop.py` (missing its
`mlog_coeff` dependency) is **not** part of this recovery and is handled
separately; `P2-BETAV-CIRC-01` remains `SUSPENDED`.

## Honesty note

Recovering these files **enables** verification; it does not by itself change
any historical verdict. No claim is upgraded or downgraded by the recovery
itself. `proca_loop.py` is deliberately excluded from this Class-A recovery.

## The excluded file

`proca_loop.py` (the βV engine) is **not** included here: it is incomplete (its
`mlog_coeff` dependency is missing) and does not run. It is Class B, handled in a
separate task. Its absence here is intentional.
