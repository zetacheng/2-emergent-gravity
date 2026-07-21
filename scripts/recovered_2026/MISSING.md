# Missing artifacts registry (recovered_2026)

Artifacts referenced by, or needed to fully verify, the recovered historical
pipelines but **not yet recovered**. Listed with what each would unlock. Nothing
here is stubbed; a genuinely missing generator is recorded, not faked.

| # | Missing artifact | What it would unlock |
|---|---|---|
| 1 | **Ward-complete vierbein-link kernel code** — the generator of `results/recovered-2026/ward_analysis_summary.txt` (the minimal vierbein-link graviton-kernel computation). | Would allow **verifying the `Z_cov < 0` claim** (covariant kinetic coefficient negative; positive axis slope entirely the non-covariant hypercubic `c4` piece) that bears on the `M_Pl²` sign and SI-2 priors. Until then those claims are **recorded, not adopted** (see the `P2-BETAV-CIRC-01` addendum). |
| 2 | **`precision_results.json`** — the output of `batch2/precision_campaign.py`, if it was ever run to completion. | Would provide the **historical high-precision ratios** `β_gfvec/β_B`, `β_V/β_B`, and the consistency residual `proca − (gfvec − boson)` at N=48. (Any *re-run* must use a blind harness: the driver embeds the `−2.000`/`−3.000` targets.) |
| 3 | **The `n=32` driver/session** that produced `β_V = −7.2e-4` and `β_V/β_B = −3.2(5)`. | Would provide the **provenance of the quarantined Finding-5 value** `−3.2(5)` (`P2-C9`). The ChatGPT session log describing this run is itself **not yet landed**; if the PI supplies it, land it here as a provenance artifact. |
| 4 | **The fermion-`mlog` driver** — the run behind the `β_Dirac/β_B = 2` continuum benchmark. | Would provide the **historical fermion `m²ln m²` extraction** cross-checking the analytic `β_F/β_B = 2` (`P2-HK-01`) on the lattice, completing the species set (scalar `β_B` and vector `β_V` sign are already reproduced). |
| 5 | **The `fig_mlog.pdf` generator script.** | Would make the historical scalar-`β_B` figure (`results/recovered-2026/fig_mlog.pdf`, already landed as a static artifact) **regenerable** from source rather than kept only as a frozen PDF. |

## Notes

- Items 1–5 are **generators/outputs**, not source we can reconstruct by
  inspection; do not synthesize them. When the PI supplies any of them, land it
  verbatim under `scripts/recovered_2026/` (code) or `results/recovered-2026/`
  (data/documents) with an `sha256`, and update `PROVENANCE.md`.
- None of these blocks the batch-2 landing or its validation runs; they bound
  what can be **verified** later, and (item 1 especially) what may be **cited**.
