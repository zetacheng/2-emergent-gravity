# Canonical report — P2-BETAV-CIRC-01 determinant-decomposition adjudication (Phase 1, revised)

**Date:** 2026-07-20 (revised same day). **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `gate/p2-betav-decomp` (off `main` = `2c396fc`).
**Type:** derivation/adjudication — **no k-scan**, no numerical target.

## 1. Executive summary

Phase-1 adjudication of whether a `k`-scan of `P2-BETAV-CIRC-01` can be *defined*
from the recovered code. **Verdict: `DECOMP-UNAVAILABLE-AS-RECOVERED`** — no
valid compensator-power deformation is available from the recovered
implementation as-is; the `boson_loop` scalar is not the flat Proca longitudinal
eigenfactor and cannot be substituted without an extra identity; the original
additive k-scan is invalid (and would be `LINEAR-ONLY`); **but** a clean-room
lattice Stueckelberg / gauge-fixed construction is **not excluded**. This
revision tightened the analysis to the `q²` level and withdrew an over-stated
mixing claim. Gate statuses and the `−3.2(5)` quarantine are unchanged.

## 2. Corrected transverse–longitudinal analysis (the core of the revision)

The earlier report measured T–L mixing via a single-momentum vertex off-block
norm (`0.17`) — the **wrong basis**. Redone correctly (`scripts/betav_decomp_q2.py`):
projectors built independently from `a(k)` and `a(k+q)`, decomposing the
recovered axis-TT bubble `Π = Π_TT+Π_TL+Π_LT+Π_LL` and extracting each sector's
`q²` coefficient (the induced-`Z` contribution) over three q-ranges,
`n∈{10,12}`, `m=0.3`. Sector `q²` coeffs sum to the total to `<1e-12`.

| sector | `q²` coefficient (n=12) | share | scaling exp `Π−Π(0)~q^p` |
|---|---|---|---|
| TT | `+2.12e-2` | `≈96.5%` | `≈1.99` |
| LL | `+6.8e-4` | `≈3.1%` | `≈1.97` |
| **TL+LT (mixed)** | **`+9.0e-5`** | **`≈0.4%`** | **`≈1.98` (q²)** |
| total | `+2.20e-2` | 100% | `≈1.99` |

Grid/range-stable: mixed `q²` coeff `8.7e-5` (n=10) ↔ `9.1e-5` (n=12).

**Findings.**
- The one-graviton vertex mixing `U_TL` **vanishes as `q→0`** (earlier `0.17`
  figure withdrawn — wrong basis).
- **But** the mixed **bubble** contributes at `O(q²)` (exp `≈1.98`), exactly the
  regime that sources an induced kinetic term: the mixed `q²` coefficient is
  **nonzero** and basis/grid-stable.
- It is **small** (`≈0.4%` of `Z`). An *approximate* T/L split holds
  (TT+LL ≈ 99.6%); an **exact invariant additive split fails only at the ≈0.4%
  level**.

In the recovered implementation used for this slope extraction, the seagull term
is `q`-independent (the recovered slope extractor is bubble-only; `δ²M` and the
single-propagator tadpole carry no external `q`) and therefore does not
contribute to the fitted `q²` coefficient — verified in this implementation, not
asserted as a general theorem.

## 3. Neutralized language (Fixes 2–4)

- The ultralocal `m²` factor is called **"the longitudinal spectral factor of
  the complete non-minimal Proca operator"** (not "the compensator sector" —
  whether it *is* the analytic compensator is unresolved absent a lattice
  Stueckelberg derivation).
- **"different `m²ln m²` content" downgraded:** their flat spectral factors have
  different momentum dependence (`m²` ultralocal vs `ŝ²+m²` propagating);
  therefore equality of their **induced** `m²ln m²` contributions cannot be
  assumed and would require a full metric-variation identity the recovered code
  does not provide (the extracted quantity is a second metric variation, not the
  flat `ln det`).
- **Continuum Stueckelberg identity softened:** no such gauge-fixed determinant-
  quotient identity is implemented or demonstrated by the recovered code; the
  equivalence to the recovered operator remains **unestablished (neither proven
  nor refuted)**.

## 4. The determinant `proca_loop.py` computes

Flat `M_{μν}=(ŝ²+m²)δ−a_μa_ν*`, spectrum `{ŝ²+m²(×3), m²(×1)}`,
`det M=m²(ŝ²+m²)³`; `Z` = axis-TT `q²` slope (bubble-only). Longitudinal factor
ultralocal `m²` (invariant over `p̂²` to `3e-16`); propagators `1/(ŝ²+m²)`
transverse, `1/m²` longitudinal. Operator checks: `scripts/betav_decomp_check.py`.

## 5. Longitudinal `m²` vs external scalar `Δ₀` — different operators (support (b))

`Δ₀ = ŝ²+m²` (propagating, `1/(ŝ²+m²)`) ≠ Proca longitudinal `m²` (ultralocal,
`1/m²`). The recovered external scalar loop is **not identical** to the flat
longitudinal eigenfactor and cannot be substituted without an additional
operator identity. Solid.

## 6. Non-linearity audit (support (a))

`TT_RECIPES` (linear), `/5` (linear), `fit_mlog` = linear least squares (linear),
ratio by fixed `k`-independent `β_B` (linear). Every relevant step is linear ⟹
the withdrawn additive `Z_V+k·Z_S` scan is `LINEAR-ONLY` (bookkeeping, not
circularity). A non-linear circular mechanism would require a `k`-dependent
`β_B`/window/normalization, absent from the recovered pipeline.

## 7. Verdict and the supports that hold

**`DECOMP-UNAVAILABLE-AS-RECOVERED`.**
- **(a)** additive `Z_V+k·Z_S` design invalid + `LINEAR-ONLY` — *holds, solid*.
- **(b)** external `boson_loop` scalar ≠ flat Proca longitudinal eigenfactor —
  *holds, solid*.
- **(c)** no **exactly** invariant T/L split (mixed `q²` term nonzero,
  basis/grid-stable) — *holds, but mild: ≈0.4% of `Z`; approximate split at 99.6%*.

Dropped/qualified: the unconditional "no operator-defined deformation can exist"
and the gross "inseparable mixing (0.17)" claim. Next step (unchanged): an
operator/determinant-identity audit ((a)-analog vs (d)) or a clean-room
`P2-BETAV-RECON-01` — **not** the withdrawn k-scan. This is a statement about the
*design*, not a CIRC verdict.

## 8. Gate specification updated (not status), quarantine held

`GATES.md` `P2-BETAV-CIRC-01` now uses separated fields:
`Status: SPECIFIED` / `Phase-1 design adjudication: DECOMP-UNAVAILABLE-AS-RECOVERED`
/ `Previous additive k-scan design: WITHDRAWN` / `Current registered test:
operator/determinant-identity audit (rules to be pre-registered)`. The CIRC gate
has **not** passed or failed. `P2-BETAV-NUMREPRO-01` = `PROPOSED`; `P2-C9` =
`PROPOSED`; `β_V/β_B=−3.2(5)` quarantined/unreproduced. `CLAIMS.md` untouched.

## 9. Tests, ruff, status (self-contained)

- `python -m pytest tests -q`: **34 passed, 2 deselected** (12 governance tests
  green, including the quarantine and no-promotion guards).
- `python -m pytest tests -q -m "slow or not slow"`: **36 passed**.
- `ruff check .`: **All checks passed.**
- `git status --porcelain`: **clean** (the `decomp/regen/` outputs are gitignored).

## 10. Commit chronology (this branch, off `main` `2c396fc`)

1. `6fd54d3` derivation: operator-level checks of the recovered Proca determinant (no target)
2. `82157de` derivation: determinant decomposition (Phase 1, original)
3. `3df1476` docs: original adjudication report
4. `3228656` chore: gitignore nested `results/**/regen`
5. `aebcf38` derivation: q²-level T/L sector decomposition of the Proca bubble (no target) — **revision, executable, committed before interpretation**
6. `3ef51cc` docs: tighten adjudication to `DECOMP-UNAVAILABLE-AS-RECOVERED` (derivation + GATES + DECISION_LOG + governance test)
7. **this report commit** — the branch HEAD (identified by the git ref; see
   `git ls-remote --heads origin`).

Post-adjudication HEAD (before this report commit): `3ef51cc`. The executable
`q²` check (5) precedes the interpretive commits (6, this report).

## What comes next (not this task)

Because the outcome is `DECOMP-UNAVAILABLE-AS-RECOVERED`, the next step is the
reformulated operator/determinant-identity circularity audit or the clean-room
`P2-BETAV-RECON-01` — not a k-scan. `−3.2(5)` promotion stays with
`P2-BETAV-NUMREPRO-01`, untouched.
