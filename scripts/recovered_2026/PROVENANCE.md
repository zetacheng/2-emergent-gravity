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

---

# Batch 2 (2026-07-21) — gauge-fixed vector, Ward summary, Fierz foundations, Wilson-frame & overlap eras

Second tranche of historical originals recovered by the PI, landed **verbatim**
(unedited) under `scripts/recovered_2026/batch2/` (documents under
`results/recovered-2026/`). Each `sha256` is recorded below. These files are
ruff-excluded (`pyproject.toml`) exactly like the batch-1 originals: they are
frozen historical artifacts, not maintained source.

**Dedup result:** none of these filenames existed anywhere in the repo before
this batch (checked `overlap_phase{1,2}.py`, `fierz_verify.py`,
`grassmann_check.py`, `pairing_fierz.py`, `gfvec_loop.py`). All land as **new**;
no existing working copy was overwritten.

## Era: gravity-engine (gauge-fixed / Solodukhin route to βV)

| File | Role | Imports | sha256 |
|---|---|---|---|
| `gfvec_loop.py` | **Gauge-fixed minimal lattice vector.** Adds a covariant gauge-fixing term so the Proca operator becomes the *minimal* vector `Δ^{(1)}+m²` (no flat longitudinal band, diagonal propagator). Implements the **Solodukhin identity** `Γ_Proca = Γ_minvec − Γ_scalar(m)` (hence `β_V = β_gfvec − β_B`), a constant-`h` validation harness (`const_h_check_gf`) and a `q`-dependent gf seagull (`g2_axis_gfvec_v2`). | `seagull_check` (`PAIRS, hmat, fit_even, EPSF`), `mlog_coeff` (`TT_RECIPES`), `proca_loop` (`geomV, kin_form, avec, M_full`) | `cb8b2f656d218c3c5a1e94608586ab68edd7c71d8b19f8328793d8218d83b310` |
| `precision_campaign.py` | Historical **precision driver** (N=48, light masses) that fits `β_gfvec`, `β_proca`, `β_B` and checks the consistency relation `proca − (gfvec − boson) = 0`. **Hours-long; docstring embeds the analytic `−2.000`/`−3.000` targets** → any future β run must go through a blind harness. Not run here. | `gfvec_loop` (`derivsGF, slope_gf`), `proca_loop` (`derivsV, slope`), `mlog_coeff` (`g2_axis_boson, fit_mlog`), `boson_loop` (`derivsB`), `seagull_check` (`fit_even`) | `d425f7193fa021a69893f0e50b1ef54de631adb62f85ef411ad6c23342050fb2` |

## Era: foundations (Fierz / Hubbard–Stratonovich basis algebra)

| File | Role | Imports | sha256 |
|---|---|---|---|
| `fierz_verify.py` | Euclidean γ-matrix build; hermitian orthonormal 16-basis; **completeness + 5×5 Fierz exchange matrix**. Self-validating (asserts + printed booleans). Underpins the future `P2-CHANNEL-FREEZE-01` basis freeze. | numpy only (standalone) | `bb83b82dcf35ab4f794cd0172d6be226f01799bd0d4cfe2a512adde55e28e196` |
| `grassmann_check.py` | Grassmann engine: expands `Σ_A (ψ̄ Γ_A ψ)²` and checks the Fierz/exchange identity for `N=1,2`. | `fierz_verify` (`basis, g, g5`) | `2ea213e794395f799003f5da7a5f56f4ebaf19829f74975e9ea000454034c164` |
| `pairing_fierz.py` | Charge-conjugation `C=γ₂γ₄` checks; antisymmetric pairing channels; exact pairing-basis decomposition of `(ψ̄ψ)²+(ψ̄iγ₅ψ)²`. | `fierz_verify` (`basis, g, g5`) | `9cf72e88e36405ca07d23575c56398cb52391a5e1b650f9895f5b1e0675d8f0f` |

## Era: Wilson-frame (channel speed-splitting; N=32/48/64/96/128 drivers)

| File | Role | Imports | sha256 |
|---|---|---|---|
| `cc_split.py` | Anisotropic-Wilson channel speed² split `σ_PV`; law-comparison (`1/L`, `1/L²`, `m`, `√m`). | numpy only | `3089f301895fd4cf6ca91bdd720f18ab9ea2b8dead91808cb537462cf90fd751` |
| `ep_test.py` | Channel `c²` (P,S,V2,A2) vs free-fermion pole dispersion, anisotropy `ε`. | numpy, scipy (`brentq`) | `91b688b9ad77f298984968a28ca3966c78b76eb004f08ff322d16235bab8f450` |
| `sigma_direct.py` | Direct `σ_PV` from paired `Z_V`/`ΔZ` temporal/spatial extraction (CLI `m n`). | numpy only | `8769fd1838658fef3b5341ff43ba0152f63556daad1ff77cbe74d2a7e34bafe0` |
| `calibrate.py` | Wilson `q=0` bubbles (S,P,V,A, tadpole) vs `anchorV` calibration + `G_c` candidates. | numpy only | `79c41f15548031c98636abcb9a4809861eeea736d0340ef7d8c9d305b97da4b7` |
| `doubler_diag.py` | Doubler diagnosis: central-only vs full BZ masked bubbles `Z_S`, `Z_Vs`. | numpy only | `a949eed6ff8a47da53c689137783f43c233820fefa8cb5fa85b5378fc611ccaa` |
| `spectrum_bigV.py` | Sliced `iE`-continuation bubbles (S,P,Vs,As); writes per-`(m,n)` JSON (CLI `m n`). | numpy only | `84c170e7d249d32de95287fc9f800d51051d2fe2b5d8038c97b607238b543430` |

## Era: overlap (Ginsparg–Wilson campaign; improved vertices)

| File | Role | Imports | sha256 |
|---|---|---|---|
| `overlap_phase1.py` | Overlap (GW) operator pieces; **GW-relation check**; improved S,P bubbles + criticality map; `Z_S` spatial sign (vs Wilson's negative value). | `fierz_verify` (`g, g5`) | `e9521e0ddf20e92e33fcab2689c20066e26b4e8d4844592b751d378c90c8ec46` |
| `overlap_phase2.py` | Improved vertices `Γ=B(1−D/2ρ)` for V,A,T; spatial/temporal `Z`; σ-mass from Goldstone condition (CLI task `A/B/C`). | `overlap_phase1` (`overlap_pieces, RHO`) | `439ccc2a2ee0262360a5ff0a0529d37239be97a3aac56cd6c560e9c9e5c4576c` |

## Documents (→ `results/recovered-2026/`)

| File | Role | sha256 |
|---|---|---|
| `emergent_gr_paper_v2_7.tex` | Historical paper version v2.7 (1426 lines). | `bdb0aacccfe22bbc465a2ae014d330e0828a02c2c876e7dc8991b06b800088e9` |
| `ward_analysis_summary.txt` | **Ward-complete vierbein-link graviton-kernel results document** (final results of the minimal vierbein-link prescription). **Recorded, not adopted** — its generating code is *not* recovered and its central claims (`Z_cov < 0`; positive axis slope entirely the non-covariant hypercubic `c4` piece) are **unverified**. See `MISSING.md` and the `P2-BETAV-CIRC-01` gate addendum. | `53e0a7dffe1294a17de5a19a91f725c765d76a66cd63b16084c1c0f7355a8850` |

## Import closure (verified present in batch-1 originals)

- `gfvec_loop.py` → `proca_loop.geomV/kin_form/avec/M_full` (`M_full` at
  `proca_loop.py:100`), `mlog_coeff.TT_RECIPES`, `seagull_check.PAIRS/hmat/fit_even/EPSF`
  — all present.
- `precision_campaign.py` → `gfvec_loop.derivsGF/slope_gf`,
  `proca_loop.derivsV/slope`, `mlog_coeff.g2_axis_boson/fit_mlog`,
  `boson_loop.derivsB`, `seagull_check.fit_even` — all present.

No unresolved import was found; nothing was stubbed. Genuinely missing
*generating* artifacts (e.g. the Ward vierbein-link kernel) are registered in
`scripts/recovered_2026/MISSING.md`.

## Honesty note (batch 2)

Same rule as batch 1: recovery **enables** verification, it does not grant it.
`gfvec_loop.py` gives the `P2-BETAV-CIRC-01` operator-identity audit a concrete
recovered object (the Solodukhin quotient), but no gate status changes, `P2-C9`
is not promoted, and `−3.2(5)` stays quarantined. The `ward_analysis_summary.txt`
claims are recorded for the record and **must not** be cited as established until
their generating computation is recovered or independently reproduced.
