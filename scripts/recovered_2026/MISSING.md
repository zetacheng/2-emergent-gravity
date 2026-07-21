# Missing artifacts registry (recovered_2026)

Artifacts referenced by, or needed to fully verify, the recovered historical
pipelines but **not yet recovered**. Listed with what each would unlock. Nothing
here is stubbed; a genuinely missing generator is recorded, not faked.

| # | Missing artifact | What it would unlock |
|---|---|---|
| 1 | **Ward-complete vierbein-link kernel code** — the generator of `results/recovered-2026/ward_analysis_summary.txt` (the minimal vierbein-link graviton-kernel computation). | Would allow **verifying the `Z_cov < 0` claim** (covariant kinetic coefficient negative; positive axis slope entirely the non-covariant hypercubic `c4` piece) that bears on the `M_Pl²` sign and SI-2 priors. Until then those claims are **recorded, not adopted** (see the `P2-BETAV-CIRC-01` addendum). |
| 2 | **`precision_results.json`** — the output of `batch2/precision_campaign.py`. | **Reclassified (2026-07-21):** *The PI confirms that the packaged `precision_campaign.py` was never executed. Accordingly, `precision_results.json` is no longer classified as a lost historical output; it is the output of a never-run computation.* The unlock is now **"run it (blind harness) for the first time"** — the `P2-BETAV-NUMREPRO-01` / operator-identity-audit path (targets `−2.000`/`−3.000` are embedded in the driver and must be stripped before any comparison). |
| 3 | **The `n=32` driver/session** that produced `β_V = −7.2e-4` and `β_V/β_B = −3.2(5)`. | **Resolved (session side), 2026-07-21:** the complete session log is landed (`results/recovered-2026/session_log_full.md`) and contains the run records and configurations (see the `PROVENANCE.md` run-record index, R10/R12/R14). **Residue:** any *standalone driver script* beyond the in-session runs remains unrecovered; only the session record is closed. |
| 4 | **The fermion-`mlog` driver** — the run behind the `β_Dirac/β_B = 2` continuum benchmark. | Would provide the **historical fermion `m²ln m²` extraction** cross-checking the analytic `β_F/β_B = 2` (`P2-HK-01`) on the lattice, completing the species set (scalar `β_B` and vector `β_V` sign are already reproduced). |
| 5 | **The `fig_mlog.pdf` generator script.** | Would make the historical scalar-`β_B` figure (`results/recovered-2026/fig_mlog.pdf`, already landed as a static artifact) **regenerable** from source rather than kept only as a frozen PDF. |
| 6 | **The position-space full-determinant finite-q validation script** — the end-to-end check that hit `0.500000` at `~10⁻⁶` relative precision, validating the placement of the `q`-dependent gauge-fixed seagull (session log R13, L227/L229). | Would allow **re-verifying the strongest historical validation of the gauge-fixed (Solodukhin) pipeline** — currently that `0.500000` result is *historically reported, not re-verified* because the script is not among the recovered files. |

## Notes

- Items 1–6 are **generators/outputs**, not source we can reconstruct by
  inspection; do not synthesize them. When the PI supplies any of them, land it
  verbatim under `scripts/recovered_2026/` (code) or `results/recovered-2026/`
  (data/documents) with an `sha256`, and update `PROVENANCE.md`.
- None of these blocks the batch-2 landing or its validation runs; they bound
  what can be **verified** later, and (item 1 especially) what may be **cited**.
