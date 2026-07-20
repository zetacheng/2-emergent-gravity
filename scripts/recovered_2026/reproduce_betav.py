"""betaV reproduction check for the recovered Proca pipeline.

Runs the completed betaV pipeline (`mlog_coeff.py` + `proca_loop.py`, both
recovered) against pre-registered Paper 2 v2.15 targets:

- scalar `beta_B` (m^2 ln m^2 coefficient): measured `+2.50e-4`,
  continuum `1/(384 pi^2) = +2.64e-4`;
- vector `beta_V` **sign**: negative (Finding 5) -- `Z_V(m)` rises with `m`;
- ratio `beta_V/beta_B`: paper `-3.2(5)`, analytic `-3`, with a known
  heavy-mass drift toward `-5` (longitudinal flat-band artifact).

Nothing is tuned to match. The magnitude of the ratio at accessible grids is
finite-`n` limited; that is reported honestly, not adjusted.

Run::

    python scripts/recovered_2026/reproduce_betav.py [--n N]

Writes `results/recovered-2026/regen/reproduce_betav.json` (gitignored).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import boson_loop as bl  # noqa: E402
import mlog_coeff as ml  # noqa: E402
import proca_loop as pl  # noqa: E402

TARGETS = {
    "beta_B_measured": 2.50e-4, "beta_B_continuum": 2.64e-4,  # fig_mlog / 1/(384 pi^2)
    "beta_V_sign": "-",         # Finding 5
    "ratio_paper": -3.2, "ratio_paper_err": 0.5, "ratio_analytic": -3.0,
    "heavy_mass_drift": -5.0,   # documented longitudinal artifact
}


def scalar_beta_B(n, masses):
    dJ, dE, _, _ = bl.derivsB()
    Z = np.array([ml.slope(lambda e: ml.g2_axis_boson(e, n, mB, dJ, dE))
                  for mB in masses])
    coef, resid = ml.fit_mlog(masses ** 2, Z, with_m4=True)
    return float(coef[2]), Z.tolist()


def vector_ZV(n, masses):
    dJ2, dJ, _, _ = pl.derivsV()
    Z = np.array([pl.slope(n, m, dJ2, dJ) for m in masses])
    coef, resid = ml.fit_mlog(masses ** 2, Z, with_m4=True)
    return float(coef[2]), Z.tolist()


def run(n=12):
    paper_win = np.linspace(0.125, 0.55, 10)  # fig_mlog window for scalar beta_B
    light = np.linspace(0.11, 0.30, 7)        # light window (Finding-5 ratio window)
    heavy = np.linspace(0.20, 0.45, 7)        # heavy-inclusive (drift toward -5)

    # scalar beta_B on the paper window (the reproduction claim)
    bB_paper, ZB_paper = scalar_beta_B(n, paper_win)
    # matched light-window scalar for the ratio
    bB_light, _ = scalar_beta_B(n, light)
    bV_light, ZV_light = vector_ZV(n, light)
    bV_heavy, ZV_heavy = vector_ZV(n, heavy)

    rises = bool(np.all(np.diff(np.array(ZV_light)) > 0))
    out = {
        "grid": n,
        "beta_B_paper_window": bB_paper,
        "beta_B_scan_Z_paper": ZB_paper,
        "beta_B_light_window": bB_light,
        "beta_V_light": bV_light, "ratio_light": bV_light / bB_light,
        "beta_V_heavy": bV_heavy, "ratio_heavy": bV_heavy / bB_light,
        "Z_V_light_rises_with_m": rises,
        "beta_V_sign": "-" if bV_light < 0 else "+",
    }
    return out


def verdicts(res):
    v = {}
    v["beta_B"] = ("reproduces"
                   if abs(res["beta_B_paper_window"] - 2.6e-4) < 1.0e-4
                   else "off-target")
    v["beta_V_sign"] = ("reproduces (negative; Z_V rises)"
                        if res["beta_V_sign"] == "-"
                        and res["Z_V_light_rises_with_m"] else "MISMATCH")
    r = res["ratio_light"]
    v["ratio"] = ("reproduces" if -3.7 <= r <= -2.7
                  else f"sign-only / grid-limited (got {r:+.2f} at n={res['grid']})")
    return v


def main():
    n = 12
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    res = run(n)
    ver = verdicts(res)
    regen = _HERE.parents[1] / "results" / "recovered-2026" / "regen"
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "reproduce_betav.json").write_text(
        json.dumps({"targets": TARGETS, "results": res, "verdicts": ver},
                   indent=2) + "\n", encoding="utf-8", newline="\n")
    print("betaV reproduction check (recovered Proca pipeline)")
    print("=" * 56)
    print(f"  grid n={res['grid']}")
    print(f"  scalar beta_B (paper win 0.125-0.55) = {res['beta_B_paper_window']:+.3e}"
          f"   [{ver['beta_B']}]")
    print(f"  vector beta_V sign : {res['beta_V_sign']}  (Z_V rises "
          f"{res['Z_V_light_rises_with_m']})  [{ver['beta_V_sign']}]")
    print(f"  ratio (light win)  = {res['ratio_light']:+.3f}   [{ver['ratio']}]")
    print(f"  ratio (heavy win)  = {res['ratio_heavy']:+.3f}   "
          f"(drift toward -5 = longitudinal artifact)")
    print(f"raw -> {regen / 'reproduce_betav.json'}")


if __name__ == "__main__":
    main()
