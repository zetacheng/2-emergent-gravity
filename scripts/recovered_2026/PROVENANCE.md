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

---

# Batch-2 addendum (2026-07-21) — recovered full session log

## The landed artifact

The PI recovered the **complete session log** of the historical session that
designed the βV precision campaign and landed it **byte-for-byte unmodified**:

| Item | Value |
|---|---|
| Landed path | `results/recovered-2026/session_log_full.md` |
| Original filename (PI-supplied) | begins `Claude睇完 paper 2…` (mixed Cantonese/English, ~74 KB) |
| Recovery date | 2026-07-21 |
| Source | PI-supplied |
| Completeness | **complete session** (not an excerpt) — this **RESOLVES** the earlier "full session log still sought" residue for the `n=32`/`−3.2(5)` provenance item |
| Bytes / SHA256 | 73853 bytes; sidecar `session_log_full.md.sha256` = `61c54701d7e61f31168aaadd0a6ee70c964f4b2175e92c1d9dd3a02749303a9c` |

The log is a **historical assistant/PI dialogue**: it establishes what the
session *claimed and configured*, **not** independently verified fact. Every
number below is **historically pinned/reported by the recovered session
message**, never "independently verified". Line numbers refer to
`session_log_full.md`.

## Run-record index (historically reported; NOT independently verified)

Each row is a numerical result **as reported in the log**, with grid, window,
and a locating quote/context. These are historical reports.

| # | Quantity | Reported value | grid `n` | mass window `ma` | Comparison / systematics note | Locate (line, quote-context) |
|---|---|---|---|---|---|---|
| R1 | scalar light-cone `c_χ²−1` (H(4) substrate) | `5×10⁻¹³` | `32⁴`, conv. vs `48⁴` | "symmetry-protected zero"; `ξ_χ=−0.078` vs `ξ_f=−0.250`, `Δξ≈0.17` | L42 "c_χ² − 1 = 5×10⁻¹³" |
| R2 | scalar `c_χ²` (no spacetime symmetry) | `1.22 … 3.77` | cubic-space Hamiltonian | splits as `1/ln(Λ/m)` — reproduces Collins et al. | L44 "c_χ² = 1.22 至 3.77" |
| R3 | graviton light-cone `Z_h(time)/Z_h(space)` | `1` (10 sig. figs) | across `ma=0.25–1.0` | robust to missing contact terms; `ξ_h=−0.055` | L82 |
| R4 | bubble `Z_h` (pre-seagull) | `+6.7, +4.9, +2.8 ×10⁻³` /species | 3 masses | Wilson-vertex on/off changes magnitude 8%, not sign; `tt_check.py` n=12/16/20 to 1% | L83–84 |
| R5 | Ward-complete `Z_cov` (covariant EH coeff) | `−1.29×10⁻³` (negative) | grid-converged | `c₄≈+6.9×10⁻³`; TT weights axis 2/5, face 1/3, body 3/10; closes 3%; overturns R4's sign | L94 (cf. `ward_analysis_summary.txt`) |
| R6 | machinery checks (Ward) | bubble+seagull vs exact `10⁻⁶`; photon Ward `2×10⁻¹⁴`; `Z_A>0` | — | sign anchor | L92 |
| R7 | boson `β_B` (`m²ln m²`) | `+2.50(13)×10⁻⁴` | `n=32` ratio test | matches continuum `1/(384π²)` to 5%; `n=48` "too slow", used `n=32` (grid systematics cancel) | L115–117 |
| R8 | fermion:scalar `m²log` ratio | `2:1` (convention-free) | — | benchmark that pins the extraction; `(1−6ξ)/384π²`, `ξ>1/6` flips sign | L113 |
| R9 | lattice `G_c` (scalar) | `5.93` | `I₀` extrap `0.0844`, offset-grid 1% | `ξ_ind=(1/6)(3−L)`; `ξ_eff>1/6 ⇒ L<2` (fails) — Finding 4 | L154 |
| **R10** | **Proca `β_V` (direct, Finding 5)** | **`−7.2×10⁻⁴`** vs pred. `−7.9×10⁻⁴` (9%) | **`n=32`** | **`m_V a = 0.11–0.20`** | **ratio `β_V/β_B = −3.2(5)`; subwindows `−2.6` and `−3.4`; wide/heavy window drifts to `−5` (m⁴ln m² longitudinal artifact)** | **L219–220** |
| R11 | Proca verification chain | flat eig `{ŝ²+m²×3, m²}` to `10⁻¹⁴`; Sherman–Morrison prop `10⁻¹⁵`; constant-h `10⁻⁸` | — | — | L221 |
| **R12** | **gfvec `β_gfvec/β_B` (Solodukhin route)** | **`≈ −2.4 … −2.9`** (target `−2`) | (summary) | **`0.125–0.55`** | **same summary quotes `Proca/B = −3.2(5)`; `130 s`/point; 5% needs `ma≈0.05, n=48`** | **L229** |
| R13 | finite-q gf-seagull validation | position-space full determinant `0.500000` hit | — | `~10⁻⁶` rel. precision | script NOT among recovered files → reported, not re-verified | L227, L229 |
| R14 | vector-channel criticality `Π_V(0)` | `+0.297 / +0.264 / +0.228` | — | `m_f=0.05/0.2/0.5`; `G_c^V≈3.4–4.4` — **matches `batch2/calibrate.py` `anchors_V`** | L232 |
| R15 | axial `Π_A(0)` | `≈ −0.19` (negative) | — | axial always heavy ⇒ `n_V=1`; Paper-3 example `m_V≈9 M_Pl, Λ≈66 M_Pl` | L236–237 |

**Corroboration with landed code (not verification of the physics):** R14's
`Π_V(0)` values are exactly the `anchors_V = {0.05:0.297, 0.2:0.264, 0.5:0.228}`
hard-coded in `batch2/calibrate.py`; R5's `Z_cov` matches
`ward_analysis_summary.txt`; R12's "`ma≈0.05, n=48`" campaign matches
`batch2/precision_campaign.py` (`N=48`, `MASSES=[0.05,…,0.12]`). This shows the
log and the landed files are the same historical programme; it does **not** make
any reported number independently verified.

## The five established facts (each historically reported, not verified)

1. **Run configurations are historically pinned — see the run-record index
   above** (not collapsed into one config). The `−3.2(5)` value has **two**
   distinct reported windows: the direct Proca extraction (R10, `n=32`,
   `m_V a=0.11–0.20`, `β_V=−7.2×10⁻⁴` vs `−7.9×10⁻⁴`) and the gfvec/precision
   summary (R12, window `0.125–0.55`, `gfvec/B≈−2.4…−2.9`), plus the `n=48`
   boson grid-systematics test (R7). All are historical reports.

2. **`precision_campaign.py` was never executed.** The log shows it was
   *packaged and handed to the PI to run locally* (L229), and the PI confirms it
   was **not** run. Therefore `precision_results.json` is reclassified as **the
   output of a never-run computation**, not a lost historical output.

3. **The gf seagull is reported NOT q-independent.** The session reports that the
   covariant-divergence gf seagull is not `q`-independent (`J` spans two sites,
   the locality lemma fails), that it derived the full `q`-dependent placement,
   and that it validated this end-to-end with a position-space full determinant
   at finite `q` (**reported**: `0.500000` hit at `~10⁻⁶` relative precision,
   L227/L229). The script for that finite-q validation is **not** among the
   recovered files, so the claim is **historically reported, not re-verified**.
   **Scope clarification (recorded verbatim as required):** *this
   q-dependent-seagull statement concerns the separate gauge-fixed/minimal-vector
   `gfvec` construction. It does not contradict the Phase-1 report's
   implementation-specific statement that the seagull in the recovered
   `proca_loop` slope extractor is q-independent.*

4. **The historical runs were not blind.** The targets (`−2`, `−3`) were openly
   known during execution (they appear throughout the log and in the driver
   docstrings). Recorded as **fact, not accusation** — it is the reason the
   modern **blind-harness** requirement exists.

5. **The historical promotion criterion was pre-stated and never met.** The
   session's own standard was that the scenario upgrades to "lattice-established"
   **only if** the precision campaign lands **both** ratios at `−2.00` and
   `−3.00` (L239) — and that campaign never ran (fact 2). **The current `−3.2(5)`
   quarantine therefore enforces the programme's own historical criterion, not a
   retroactive standard.** (Also recorded in `DECISION_LOG.md`.)
