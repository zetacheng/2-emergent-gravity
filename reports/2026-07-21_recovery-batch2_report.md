# Canonical report — recovery batch 2 (gauge-fixed vector, Ward summary, Fierz foundations, Wilson-frame & overlap eras)

**Date:** 2026-07-21. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `recover/batch2-gfvec-and-foundations` (off `main` = `aaa3694`).
**Type:** provenance recovery + gate addendum. **No merge, no PR.** No gate
status change; `−3.2(5)` quarantine untouched; `CLAIMS.md` untouched.

## 1. Files landed (verbatim) + sha256

Historical originals under `scripts/recovered_2026/batch2/` (ruff-excluded like
batch-1 originals); documents under `results/recovered-2026/`.

**Gravity-engine era (gauge-fixed / Solodukhin):**

| File | sha256 |
|---|---|
| `batch2/gfvec_loop.py` | `cb8b2f656d218c3c5a1e94608586ab68edd7c71d8b19f8328793d8218d83b310` |
| `batch2/precision_campaign.py` | `d425f7193fa021a69893f0e50b1ef54de631adb62f85ef411ad6c23342050fb2` |

**Foundations era (Fierz / HS basis):**

| File | sha256 |
|---|---|
| `batch2/fierz_verify.py` | `bb83b82dcf35ab4f794cd0172d6be226f01799bd0d4cfe2a512adde55e28e196` |
| `batch2/grassmann_check.py` | `2ea213e794395f799003f5da7a5f56f4ebaf19829f74975e9ea000454034c164` |
| `batch2/pairing_fierz.py` | `9cf72e88e36405ca07d23575c56398cb52391a5e1b650f9895f5b1e0675d8f0f` |

**Wilson-frame era:**

| File | sha256 |
|---|---|
| `batch2/cc_split.py` | `3089f301895fd4cf6ca91bdd720f18ab9ea2b8dead91808cb537462cf90fd751` |
| `batch2/ep_test.py` | `91b688b9ad77f298984968a28ca3966c78b76eb004f08ff322d16235bab8f450` |
| `batch2/sigma_direct.py` | `8769fd1838658fef3b5341ff43ba0152f63556daad1ff77cbe74d2a7e34bafe0` |
| `batch2/calibrate.py` | `79c41f15548031c98636abcb9a4809861eeea736d0340ef7d8c9d305b97da4b7` |
| `batch2/doubler_diag.py` | `a949eed6ff8a47da53c689137783f43c233820fefa8cb5fa85b5378fc611ccaa` |
| `batch2/spectrum_bigV.py` | `84c170e7d249d32de95287fc9f800d51051d2fe2b5d8038c97b607238b543430` |

**Overlap era:**

| File | sha256 |
|---|---|
| `batch2/overlap_phase1.py` | `e9521e0ddf20e92e33fcab2689c20066e26b4e8d4844592b751d378c90c8ec46` |
| `batch2/overlap_phase2.py` | `439ccc2a2ee0262360a5ff0a0529d37239be97a3aac56cd6c560e9c9e5c4576c` |

**Documents (`results/recovered-2026/`):**

| File | sha256 |
|---|---|
| `emergent_gr_paper_v2_7.tex` | `bdb0aacccfe22bbc465a2ae014d330e0828a02c2c876e7dc8991b06b800088e9` |
| `ward_analysis_summary.txt` | `53e0a7dffe1294a17de5a19a91f725c765d76a66cd63b16084c1c0f7355a8850` |

## 2. Dedup results (Task-1 requirement)

Checked `overlap_phase{1,2}.py`, `fierz_verify.py`, `grassmann_check.py`,
`pairing_fierz.py`, `gfvec_loop.py` against the whole repo (outside `.git`):
**none existed anywhere before this batch.** All land as **new**; no existing
working copy was overwritten, so no version-fork note was needed. (Had any
byte-differed from an in-repo copy, the recovered one would have landed under
`batch2/` with a version note and the current copy left untouched.) The
re-uploaded `calibrate.py` / `doubler_diag.py` were byte-identical to their
first upload.

## 3. Import-closure results (Task-1 requirement)

Verified against the batch-1 originals (all symbols present, nothing stubbed):

- `gfvec_loop.py` → `proca_loop.{geomV, kin_form, avec, M_full}` (`M_full` at
  `proca_loop.py:100`), `mlog_coeff.TT_RECIPES`,
  `seagull_check.{PAIRS, hmat, fit_even, EPSF}` — **all resolve**.
- `precision_campaign.py` → `gfvec_loop.{derivsGF, slope_gf}`,
  `proca_loop.{derivsV, slope}`, `mlog_coeff.{g2_axis_boson, fit_mlog}`,
  `boson_loop.derivsB`, `seagull_check.fit_even` — **all resolve**.
- Foundations: `grassmann_check.py` / `pairing_fierz.py` →
  `fierz_verify.{basis, g, g5}`; `overlap_phase1.py` → `fierz_verify.{g, g5}`;
  `overlap_phase2.py` → `overlap_phase1.{overlap_pieces, RHO}` — **all resolve**.

No unresolved import found. Genuinely missing *generators* (not imports) are in
`scripts/recovered_2026/MISSING.md`.

## 4. Validation outputs (Task-2; full detail in `results/recovered-2026/BATCH2_VALIDATION.md`)

**Fierz foundations — VALIDATES** (self-validating, exit 0):
- `fierz_verify.py`: completeness `True`; 5×5 Fierz exchange matrix printed.
- `grassmann_check.py`: `Σ_A (ψ̄Γ_Aψ)² == −4 Σ_ab exchange : True` for `N=1,2`
  (the `+4` variant correctly `False` — physical identity carries the Grassmann
  minus sign).
- `pairing_fierz.py` (supplementary): `C=γ₂γ₄` checks `True`;
  `C S(−p)ᵀ C⁻¹ = S(p)` `True`; pairing decomposition residual `5.21e-15`
  (rank 36/36).

**Gauge-fixed constant-h machinery — VALIDATES** (`const_h_check_gf`, `m=0.5`):

```
n=6:  (0,0)(0,0) exact=+2.871710e-01 pert=+2.871713e-01 diff=2.7e-07
      (0,1)(0,1) exact=+7.072147e-01 pert=+7.072152e-01 diff=5.2e-07
      (0,0)(1,1) exact=-9.614086e-02 pert=-9.614102e-02 diff=1.6e-07
n=8:  (0,0)(0,0) exact=+2.879797e-01 pert=+2.879800e-01 diff=2.7e-07
      (0,1)(0,1) exact=+7.071655e-01 pert=+7.071660e-01 diff=5.1e-07
      (0,0)(1,1) exact=-9.633869e-02 pert=-9.633885e-02 diff=1.6e-07
```

Perturbative bubble+seagull vs exact `½⟨ln det M_minvec⟩` agree to `~1e-7` (the
`O(EPSF²)` FD floor). Validates the determinant-quotient *implementation*; **no
β extraction, no ratio target evaluated.**

**`precision_campaign.py` — NOT RUN** (hours; docstring embeds `−2.000`/`−3.000`
targets → any future β run must use a **blind harness**).

## 5. Gate addendum text (Task-3; added to `P2-BETAV-CIRC-01` and `DECISION_LOG.md`)

A dated **2026-07-21 addendum** was added to the gate body (Phase-1 verdict and
its token **unchanged**). Substance:

- the registered operator/determinant-identity audit now has a **concrete
  recovered object** — the Solodukhin quotient `Γ_Proca = Γ_minvec − Γ_scalar(m)`
  in `gfvec_loop.py`; the audit will examine it at the operator level and via the
  consistency relation `β_proca − (β_gfvec − β_boson) = 0` (pre-encoded in
  `precision_campaign.py`);
- PASS/FAIL/INCONCLUSIVE rules remain to be **pre-registered before any run**;
  any β-extraction run must use a **blind harness** (historical files embed the
  analytic targets);
- gate Status stays `SPECIFIED`; `P2-BETAV-NUMREPRO-01` stays `PROPOSED`; `P2-C9`
  and the `−3.2(5)` quarantine are **untouched**. The batch-2 recovery **does not
  reopen or overturn** the Phase-1 verdict (correct for the then-recovered
  additive-scan set); the additive k-scan stays **withdrawn**.

## 6. Ward summary — recorded, not adopted (Task-3)

`results/recovered-2026/ward_analysis_summary.txt` is recorded as a **historical
results document whose claims are recorded, not adopted**. Its central claims —
the covariant kinetic coefficient is **negative** (`Z_cov < 0`), and the earlier
positive axis slope was **entirely** the non-covariant hypercubic `c4` piece —
bear directly on the `M_Pl²` sign question and SI-2 priors, **but the generating
code (the Ward-complete vierbein-link kernel) is not recovered and the claims are
unverified** (`MISSING.md`, item 1). **No gate, paper text, or prior may cite
them as established** until the generating computation is recovered or
independently reproduced.

## 7. Missing-artifacts registry (Task-4; `scripts/recovered_2026/MISSING.md`)

1. **Ward-complete vierbein-link kernel code** — generator of the Ward summary;
   would allow verifying the `Z_cov < 0` claim.
2. **`precision_results.json`** — output of `precision_campaign.py` if ever run;
   the historical high-precision ratios (blind-harness re-run otherwise).
3. **The `n=32` driver/session** that produced `β_V=−7.2e-4` and `−3.2(5)` —
   provenance of the quarantined Finding-5 value (ChatGPT session log not yet
   landed; land verbatim if the PI supplies it).
4. **The fermion-`mlog` driver** — the `β_Dirac/β_B = 2` continuum benchmark run.
5. **The `fig_mlog.pdf` generator script** — to make the historical figure
   regenerable from source.

## 8. Routed elsewhere — NOT landed in this repo

Per the prompt scope, these are named for routing only and **not** landed here:

- **Paper 1:** `fiducial_rerun.py`, `cluster_test.py`
- **Paper 3:** `bs_induced_gv.py` (the BS / induced-`G_V` gate's object)
- **Paper 5:** `wzw_flow.py`, `skyrme_sign2.py`

(No sha256 recorded — not uploaded; if the PI wants them logged for the routing
record, they can be uploaded and hashed without landing.)

## 9. Guards (clean checkout at pre-report HEAD `f5f8b3c`)

Fresh clone of the branch:

- `python -m pytest tests -q`: **34 passed, 2 deselected**.
- `python -m pytest tests -q -m "slow or not slow"`: **36 passed**.
- `tests/test_si1_governance.py`: **12 passed** (quarantine + no-promotion guards).
- `ruff check .`: **All checks passed** (`batch2/` excluded).
- `git status --porcelain`: **clean**.
- Invariants: `P2-BETAV-CIRC-01` = `SPECIFIED`; `P2-BETAV-NUMREPRO-01` =
  `PROPOSED`; `P2-C9` = `PROPOSED`; `DECOMP-UNAVAILABLE-AS-RECOVERED` token
  intact; 2026-07-21 addendum present; `CLAIMS.md` untouched.

## 10. Commit chronology (branch off `main` `aaa3694`)

```
6a093db provenance: recover batch 2 (gfvec/Solodukhin, Ward summary, Fierz foundations, Wilson-frame era)
bb13913 provenance: batch-2 validation (Fierz algebra, gfvec constant-h machinery)
fe579ea gate: addendum — Solodukhin-quotient object recovered; Ward summary recorded not adopted
f5f8b3c provenance: missing-artifacts registry
```

Pre-report HEAD: `f5f8b3c7656f8722d13f2d38947a41f877f4fe25`. This report is the
next commit; per the attestation pattern its own SHA is not embedded here (given
in the task response). `git ls-remote --heads origin` is captured in the task
response after the push.
