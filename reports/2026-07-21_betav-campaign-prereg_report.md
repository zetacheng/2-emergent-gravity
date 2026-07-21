# Report — P2-BETAV decisive campaign: pre-registration + blind harness + non-decisive pilot

**Date:** 2026-07-21. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `gate/p2-betav-campaign-prereg` (off `main` = `20f96f1`).
**No merge, no PR.** **No decisive run in this task.** This branch pre-registers
the rules, builds the blind harness, and validates it on a non-decisive pilot;
the decisive runs (Arm H, then Arm P) are a separate, subsequently authorized
task pending ChatGPT review + PI approval.

## 1. What this campaign is

The historical session designed `precision_campaign.py` as the programme's own
decisive test and **never ran it** (session log R10/R12; DECISION_LOG
historical-criterion entry). This task rebuilds that computation under modern
discipline, serving **two registered gates kept strictly distinct**:

- **`P2-BETAV-CIRC-01`** — the operator/determinant-identity **audit**: the
  Solodukhin quotient `Γ_Proca = Γ_minvec − Γ_scalar` (as implemented in
  `gfvec_loop.py`), numerically `R_cons = β_proca − β_gfvec + β_boson = 0`.
- **`P2-BETAV-NUMREPRO-01`** — numerical **reproduction** of `−3.2(5)` at the
  historical configuration, plus the programme's own historical promotion
  criterion (both ratios at `−2.00`/`−3.00`).

**Scope (binding):** an audit PASS establishes the operators obey the claimed
identity (correct `−3` multiplicity bookkeeping); per Phase-1 every pipeline step
is linear, so it **cannot** establish strong historical non-circularity. A
NUMREPRO PASS reproduces a number; **neither, alone, promotes `P2-C9`** —
promotion is a separate dual-gate PI+reviewer decision. The `−3.2(5)` quarantine
is untouched.

## 2. Pre-registration document

`derivations/P2-BETAV-CAMPAIGN_prereg.md` (sha256
`3ec4265dac1e7ee6c8ebb60910009b983f777f3bf418613c64859ed9ddfed0e7`) freezes, in
order: (a) the two-tier identity structure + `τ_num` floor + Tier-1↔Tier-2
machine cross-check; (a2) the per-species extractor freeze + `τ_Z` seagull
sensitivity rule; (a3) the `fit_mlog` basis limitation (`m⁴` but not `m⁴ln m²`)
and the extended-basis diagnostic; (a4) the pilot-amendment invalidation rule;
(b) the two decisive configurations (Arm H `n=32`, Arm P `n=48`) with eps/mass
grids frozen **by value**; (c0)–(c6) the acceptance rules; (d) the battery;
(e) the two pilot mutation anchors; (f) determinism/cross-machine protocol;
(g) the blindness protocol.

**Two pre-registered honest expectations recorded verbatim:**
- **(c2) NUMREPRO:** because the historical subwindows already give `−2.6`/`−3.4`
  (R10), the window-shift verdict variant alone can give `σ_H ≈ 0.4`, so the 2σ
  interval can exceed the band `[−3.7, −2.7]` and the verdict can be INCONCLUSIVE
  **even under perfect reproduction of `−3.2(5)`** — a statement about the
  configuration's discriminating power, not a failure of the identity.
- **(c5) historical criterion:** the coarse historical `gfvec/B ≈ −2.4…−2.9`
  (R12) is **outside** `[−2.10, −1.90]`; Arm P genuinely tests whether the fine
  configuration pulls it to `−2.0`. A FAIL is a live possibility and will be
  recorded exactly like a PASS.

**Resolving-power ceiling (c1):** the audit adds `2σ_C ≤ δ_audit = 0.05` so a
noisier battery cannot *widen* the tolerance into a PASS. NUMREPRO deliberately
has **no** such ceiling (there a larger σ makes PASS harder).

**Verdict vs diagnostic-only classification (c6):** only VERDICT variants
(baseline, eps-drop-largest/smallest, fit-order, mass-drop-one, and Arm-H
window-shift) enter any σ or PASS/FAIL. DIAGNOSTIC-ONLY variants (gfvec-v2
seagull sensitivity, extended `m⁴ln m²` fit, pilot mutation anchors) are computed
and reported but **never** enter a verdict — a diagnostic must not be able to
change the verdict it diagnoses. A finite gfvec-v2/bubble difference is reported
as `SEAGULL-SENSITIVITY DETECTED` (a finding, not a FAIL); only *failure to
execute* a diagnostic is `HARNESS INVALID / AUDIT INCONCLUSIVE`.

## 3. Blind harness design

- `scripts/P2-BETAV-CAMPAIGN/harness_compute.py` — loads the recovered
  scientific **functions** via an explicit `sys.path` arrangement (parent
  `recovered_2026/` + `batch2/`; no originals copied/edited), computes per-species
  `Z(m)` (recovered `g2_axis_*` kernels + faithful `fit_even`/`fit_mlog` with full
  rank/κ/residual/dof diagnostics) for every variant in the frozen table, and
  writes `results/P2-BETAV-CAMPAIGN/raw/<arm>.json` **plus an external sha256
  sidecar**. It contains **no target numbers**, prints **no ratios/verdicts**, and
  the JSON contains **no** ratios/verdicts/bands and **not its own hash**
  (self-reference rule). Registered source set (hashed into the JSON): the 5
  recovered modules + `harness_compute.py`.
- `scripts/P2-BETAV-CAMPAIGN/compare.py` — the non-blind stage; **refuses to run**
  unless, in order: (1) sidecar hash verifies; (2) prereg-doc hash matches;
  (3) registered-source hashes match; (4) compute commit is an ancestor of HEAD;
  (5) schema version matches. Then applies (c1)–(c6), quoting the prereg doc.

## 4. Machine guards (added to the governance suite)

`tests/test_betav_campaign_guards.py` — four layered guards (substring search
alone is insufficient):
1. **AST numeric-literal guard** on `harness_compute.py`: rejects the target
   constants as `UnaryOp(USub, Constant(x))` for `x∈{2,2.0,3,3.0,3.2}` (handles
   `-3.0` → USub+Constant) and bare `Constant(3.2)`.
2. **Stdout blindness guard:** exercises the harness print path and asserts stdout
   contains no ratio/verdict/band/target vocabulary (case-insensitive).
3. **Output-schema guard:** validates the committed pilot JSON (no
   ratio/verdict/target keys; no self-hash; class labels + diagnostics present).
4. **Refuse-order guard:** asserts `compare.py` runs all five refuse-checks in
   order `(1)…(5)`, plus a tamper test that a modified body is caught at check (1).

## 5. Non-decisive pilot (harness validation only)

Pilot config (frozen): `n=16`, `M_pilot=[0.10,0.12,0.14,0.17,0.20]`,
`EPS_pilot=[0.10,0.18,0.26]`. **Every pilot output is NON-DECISIVE; pilot numbers
may not be cited for any gate.** Artifacts (committed, with sidecars):

- `results/P2-BETAV-CAMPAIGN/raw/pilot.json` (sha256
  `9e438c2d2c7f3a135c4a4cd224d829efe647c7edd3ca5d1259dcedaad63ac741`)
- `results/P2-BETAV-CAMPAIGN/raw/pilot_mut_gfvec_scale.json` (sha256
  `38c5e9c9bfa37a48f7e64a72e026a831a6df76d054f42b71425e376d0ae7a930`)
- `results/P2-BETAV-CAMPAIGN/pilot_comparison.json`,
  `results/P2-BETAV-CAMPAIGN/pilot_mutation_check.json`

**Pilot end-to-end result (mechanics, not physics):**
- All five refuse-checks pass in order on `pilot.json`.
- The pilot audit returns `HARNESS INVALID / AUDIT INCONCLUSIVE` **by design**:
  the 3-eps pilot grid makes the eps-drop verdict variants underdetermined
  (2 points < 3 columns), and the harness **correctly refuses** them per (c3).
  This validates the underdetermined-refusal path; it is **not** a decisive audit
  verdict (the pilot is a structure/mechanics test).
- **Seagull diagnostic:** `dZ_max = 6.1e-14 ≤ τ_Z = 2.2e-8` → `consistent`
  (matches the prereg's exploratory ~1e-14 expectation); `Δβ/|β_B| ≈ 8e-8`.
- **Mutation anchors (both PASS, within `τ_num = 9.26e-9`):**
  - anchor 1 (gfvec ×1.1): `ΔR_cons` observed `8.97055e-4` vs expected
    `−0.1·β_gfvec = 8.97055e-4` (diff ~1.7e-11);
  - anchor 2 (boson sign): observed `−2.36365e-4` vs expected `−2·β_boson`
    (diff ~3e-20).

**Floor calibration:** the pilot's clean-FP residues sit far below `τ_num`; no
`τ_num` recalibration was needed, so **no prereg amendment** was made and the
(a4) invalidation rule did not trigger. The committed pilot artifacts carry the
final prereg-doc hash `3ec4265d…`.

## 6. Gate bookkeeping (no outcomes)

- **`P2-BETAV-NUMREPRO-01`: `PROPOSED → SPECIFIED`** (rules registered in the
  prereg doc; **not run**).
- **`P2-BETAV-CIRC-01`: stays `SPECIFIED`**; the "Current registered test" field
  now points to prereg §(c1)/§(c4)/§(c6)/§(e) and carries the scope statement.
- **`P2-C9` and the `−3.2(5)` quarantine: untouched.** New governance test
  `test_audit_pass_alone_does_not_promote_c9` guards that a future audit PASS
  alone cannot flip the quarantine (dual-gate rule intact).

## 7. Guards, tests (clean checkout)

- `python -m pytest tests -q`: **41 passed, 2 deselected**.
- `python -m pytest tests -q -m "slow or not slow"`: **43 passed**.
- `tests/test_si1_governance.py`: **14 passed** (was 12; +2: NUMREPRO-SPECIFIED
  and audit-pass-alone).
- `tests/test_betav_campaign_guards.py`: **5 passed** (the four guards; guard 4
  has a check-order test and a tamper test).
- `ruff check .`: **All checks passed** (campaign scripts are linted, not
  excluded; batch2 originals remain excluded).

## 8. Commit chronology (off `main` `20f96f1`)

```
362d830 prereg: P2-BETAV campaign (audit + NUMREPRO) — rules frozen before compute
f45b547 harness: blind compute + separated comparison for the betaV campaign
db002d7 pilot: non-decisive harness validation + mutation anchors
deb4a3c gate: register campaign rules (NUMREPRO -> SPECIFIED; CIRC audit rules filled)
```

Pre-report HEAD: `deb4a3c`. The chronology is prereg → harness → pilot compute →
(pilot comparison committed with the pilot) → gate bookkeeping. This report is the
next commit; per the self-reference rule its own SHA is given in the task
response, not embedded. `git ls-remote --heads origin` is in the task response
after the push.

## 9. Next (separate task, authorized only after review + PI approval)

The decisive runs — **Arm H** (NUMREPRO), then **Arm P** (audit + historical
criterion; hours, may run on the PI's machine with the frozen harness, outputs
committed via sha256 sidecars per §(f)) — followed by their **comparison**
commits (compute commit precedes comparison commit). No band widening, no rule
change after results; `τ_num` is frozen once the decisive compute begins.
