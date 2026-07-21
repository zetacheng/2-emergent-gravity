# Addendum — recovery batch 2: full session log landed; `−3.2(5)` provenance pinned

**Date:** 2026-07-21. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `recover/batch2-gfvec-and-foundations` (continues; **no merge, no
PR**). Companion to `reports/2026-07-21_recovery-batch2_report.md`.
**No gate status change; `P2-C9` and the `−3.2(5)` quarantine untouched.**

## 1. Landed artifact

`results/recovered-2026/session_log_full.md` — the **complete** historical
session log, landed **byte-for-byte unmodified** (no injected header, no
whitespace normalization, no re-encoding). Provenance recorded externally:

- sidecar `results/recovered-2026/session_log_full.md.sha256` =
  `61c54701d7e61f31168aaadd0a6ee70c964f4b2175e92c1d9dd3a02749303a9c`
  (SHA256 of the landed bytes; 73853 bytes);
- `PROVENANCE.md` batch-2 addendum: original filename begins `Claude睇完 paper 2…`,
  recovery date 2026-07-21, PI-supplied, **complete-session** status — this
  **resolves** the earlier "full session log still sought" residue.

The log is a historical dialogue: it establishes what the session *claimed and
configured*, **not** independently verified fact. A **run-record index** (15
rows, R1–R15) of every reported number — with grid, mass window, and a locating
line/quote — is in `PROVENANCE.md`, each labelled *historically reported, not
independently verified*.

## 2. The five established facts (each historically reported, not verified)

1. **Run configurations pinned via the run-record index** (not collapsed into
   one). The `−3.2(5)` value has **two** distinct reported windows: direct Proca
   (R10: `n=32`, `m_V a=0.11–0.20`, `β_V=−7.2×10⁻⁴` vs `−7.9×10⁻⁴`, ratio
   `−3.2(5)`, subwindows `−2.6`/`−3.4`) and the gfvec/precision summary (R12:
   window `0.125–0.55`, `gfvec/B≈−2.4…−2.9`), plus the `n=48` boson
   grid-systematics test (R7).
2. **`precision_campaign.py` was never executed** (packaged and handed to the PI;
   PI confirms not run). `precision_results.json` reclassified as the **output of
   a never-run computation**.
3. **The gf seagull is reported NOT q-independent** (`J` spans two sites; locality
   lemma fails); full `q`-dependent placement derived and validated end-to-end
   with a position-space full determinant at finite `q` (**reported**: `0.500000`
   at `~10⁻⁶`). Script not among recovered files → reported, not re-verified.
   **Scope clarification (verbatim):** *this q-dependent-seagull statement
   concerns the separate gauge-fixed/minimal-vector `gfvec` construction. It does
   not contradict the Phase-1 report's implementation-specific statement that the
   seagull in the recovered `proca_loop` slope extractor is q-independent.*
4. **The historical runs were not blind** — targets (`−2`, `−3`) were openly
   known. Recorded as fact, not accusation; it is why the modern blind-harness
   requirement exists.
5. **The historical promotion criterion was pre-stated and never met** — upgrade
   to "lattice-established" required both ratios at `−2.00` and `−3.00`, and the
   campaign never ran. **The current `−3.2(5)` quarantine therefore enforces the
   programme's own historical criterion, not a retroactive standard.** (Also in
   `DECISION_LOG.md`.)

**Corroboration with landed code** (not verification): R14's `Π_V(0) =
+0.297/+0.264/+0.228` are exactly `batch2/calibrate.py`'s `anchors_V`; R5's
`Z_cov` matches `ward_analysis_summary.txt`; R12's `ma≈0.05, n=48` matches
`batch2/precision_campaign.py`.

## 3. `MISSING.md` changes

- **#2 (`precision_results.json`)** → reclassified: *"The PI confirms that the
  packaged `precision_campaign.py` was never executed. Accordingly,
  `precision_results.json` is no longer classified as a lost historical output;
  it is the output of a never-run computation."* Unlock is now **run it (blind
  harness) for the first time** (NUMREPRO / audit path).
- **#3 (the `n=32` driver/session)** → **resolved (session side)**: the full log
  is landed with the run records; residue = any standalone driver script beyond
  the in-session runs.
- **#6 (new)** → the position-space full-determinant finite-q validation script
  (the `0.500000` end-to-end check of the `q`-dependent gf seagull).

## 4. NUMREPRO gate note

`P2-BETAV-NUMREPRO-01` gains a dated **2026-07-21** note pinning the historical
target configuration as pre-registration **input** (per the run-record index; at
minimum `n=32` windows `0.11–0.20` and `0.125–0.55`, `n=48` boson grid test,
`gfvec/B≈−2.4…−2.9`) — historically reported, not independently verified. When
the gate's PASS/FAIL rules are pre-registered, the reproduction must target this
configuration via a **blind harness**. **Status stays `PROPOSED`**; `P2-C9` and
the quarantine untouched.

## 5. Guards (clean checkout at pre-report HEAD)

- `python -m pytest tests -q`: **34 passed, 2 deselected**.
- `python -m pytest tests -q -m "slow or not slow"`: **36 passed**.
- `tests/test_si1_governance.py`: **12 passed**.
- `ruff check .`: **All checks passed**.
- `git status --porcelain`: **clean**.
- Invariants: `P2-BETAV-CIRC-01` = `SPECIFIED`; `P2-BETAV-NUMREPRO-01` =
  `PROPOSED`; `P2-C9` = `PROPOSED`; `−3.2(5)` quarantined; `CLAIMS.md` untouched.

## 6. Commit chronology (this addendum, continuing the batch-2 branch)

```
2edba5f provenance: land full historical session log (byte-for-byte + sidecar sha256)
5959de5 provenance: run-record index + pin -3.2(5) config; NUMREPRO pre-registration note
```

Pre-report HEAD: `5959de5`. This report addendum is the next commit; per the
attestation pattern its own SHA is not embedded here (given in the task
response). `git ls-remote --heads origin` is captured in the task response after
the push.
