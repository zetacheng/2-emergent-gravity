"""Measurement for `P2-BETAV-EXTCOMP-01`: the mass-log content of the ten
external components, retained and discarded.

**This is a DIAGNOSTIC.** It lives outside ``scripts/recon2026/`` and modifies
no existing file. It performs the two-step extraction per component:

    step 1   at fixed mass, vary q; the q^2 coefficient of the component's
             Pi(q) is that component's Z(m^2)
    step 2   vary mass; the m^2 ln(m^2) coefficient of Z(m^2) is that
             component's beta

Step 1 is what `EXT-01` performed at ONE mass. This script performs it per
mass and then performs step 2.

Every analysis choice is read from landed code or from the task's committed
pre-registration; none is chosen here. The component definitions, the bubble,
the q grid, both fit forms and the solver all come from landed modules.

Imports, disclosed because the governing specification requires it. This
script imports the landed ``ext01_discarded_external_space`` diagnostic for the
component definitions and the per-component bubble, and ``mlog_coeff`` for the
mass-log fit. Through the first it transitively imports ``proca_loop``,
``seagull_check`` and ``mlog_coeff`` from ``scripts/recovered_2026/``.
``proca_loop``'s module docstring carries an analytic target for the species
ratio. **Nothing here reads, prints, stores or compares against it.**

**``reproduce_betav`` is NOT imported.** Its mass-window values are read as
literals below, cited to the lines that define them, precisely so that the
anchor value in that module is never loaded.

**No beta_B is computed, and no ratio of a beta_V-class quantity to a
beta_B-class one is formed.** The only ratios produced are discarded-to-
retained, both within the external-component decomposition.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

_DIAG = Path(__file__).resolve().parent
sys.path.insert(0, str(_DIAG))

import ext01_discarded_external_space as ext01  # noqa: E402

sys.path.insert(0, str(_DIAG.parent / "recovered_2026"))
import mlog_coeff as ml  # noqa: E402
import proca_loop as pl  # noqa: E402

# --------------------------------------------------------------------------
# Frozen by the pre-registration commit. Every value is READ; see PART 1 of
# derivations/P2-BETAV-EXTCOMP-01_external-component-mass-log.md for the line
# that fixes each.
# --------------------------------------------------------------------------
EXTENT = ext01.EXTENT                      # 12, ext01:57
Q_GRID = ext01.Q_GRID                      # proca_loop.slope default
RETAINED = ext01.RETAINED                  # ext01:63-69
DISCARDED = ext01.DISCARDED                # ext01:71-79

# reproduce_betav.py:62-63, read as literals so that module is not imported
WINDOWS = {
    "LIGHT": np.linspace(0.11, 0.30, 7),
    "HEAVY": np.linspace(0.20, 0.45, 7),
}
FIT_FORMS = {"V2a_with_m4": True, "V2b_no_m4": False}

W_RETAINED = 1.0 / len(RETAINED)           # landed: proca_loop.py:130 `/ 5.0`
V_DISCARDED = 1.0 / len(DISCARDED)         # THIS TASK'S CHOICE, same form


def _labels_and_recipes():
    labels = [(n, "retained") for n, _, _ in RETAINED] + \
             [(n, "discarded") for n, _, _ in DISCARDED]
    recipes = [r for _, _, r in RETAINED] + [r for _, _, r in DISCARDED]
    return labels, recipes


def step1_Z(masses, dJ2, dJ, recipes):
    """Per component, per mass: the q^2 coefficient of Pi(q).

    Uses the landed per-component bubble and the landed even-power fit.
    Returns Z with shape (n_mass, n_component), plus per-fit diagnostics.
    """
    Z, diag = [], []
    for m in masses:
        series = np.stack([
            ext01.component_bubble(float(q), EXTENT, float(m), dJ2, dJ, recipes)
            for q in Q_GRID
        ])                                   # (nq, ncomp)
        A = np.vander(np.asarray(Q_GRID, float) ** 2, 3, increasing=True)
        cond = float(np.linalg.cond(A))
        rank = int(np.linalg.matrix_rank(A))
        row, rdiag = [], []
        for i in range(series.shape[1]):
            coef, *_ = np.linalg.lstsq(A, series[:, i], rcond=None)
            resid = float(np.abs(A @ coef - series[:, i]).max())
            row.append(float(coef[1]))
            rdiag.append({"residual_max_abs": resid})
        Z.append(row)
        diag.append({"mass": float(m), "design_condition": cond,
                     "design_rank": rank, "n_columns": A.shape[1],
                     "per_component": rdiag})
    return np.array(Z), diag


def step2_beta(masses, Z, with_m4):
    """Per component: the m^2 ln(m^2) coefficient, by the landed fit."""
    m2 = np.asarray(masses, float) ** 2
    cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
    if with_m4:
        cols.append(m2 ** 2)
    A = np.stack(cols, axis=1)
    cond = float(np.linalg.cond(A))
    rank = int(np.linalg.matrix_rank(A))
    betas, resids, status = [], [], []
    for i in range(Z.shape[1]):
        coef, resid = ml.fit_mlog(m2, Z[:, i], with_m4=with_m4)
        b = float(coef[2])
        if not np.isfinite(b):
            status.append("FAILS: NON-FINITE")
        elif rank < A.shape[1]:
            status.append("FAILS: EXACTLY SINGULAR")
        else:
            status.append("REPORTED")
        betas.append(b)
        resids.append(float(resid))
    return (np.array(betas), resids, status,
            {"design_condition": cond, "design_rank": rank,
             "n_columns": A.shape[1]})


def measure_cost(masses, dJ2, dJ, recipes):
    """`M3`: the wall time of ONE mass point, and the projected total."""
    t0 = time.perf_counter()
    for q in Q_GRID:
        ext01.component_bubble(float(q), EXTENT, float(masses[0]), dJ2, dJ,
                               recipes)
    one = time.perf_counter() - t0
    total_points = sum(len(w) for w in WINDOWS.values())
    return {"seconds_one_mass_point": one,
            "n_mass_points_total": total_points,
            "projected_total_seconds": one * total_points,
            "q_grid_size": len(Q_GRID), "n_components": len(recipes)}


def run():
    labels, recipes = _labels_and_recipes()
    dJ2, dJ, _, _ = pl.derivsV()

    cost = measure_cost(WINDOWS["LIGHT"], dJ2, dJ, recipes)

    per_window = {}
    for wname, masses in WINDOWS.items():
        Z, zdiag = step1_Z(masses, dJ2, dJ, recipes)
        per_window[wname] = {"masses": [float(m) for m in masses],
                             "Z": Z.tolist(), "step1_diagnostics": zdiag}

    variants = {}
    for wname in WINDOWS:
        Z = np.array(per_window[wname]["Z"])
        for fname, with_m4 in FIT_FORMS.items():
            betas, resids, status, d = step2_beta(
                per_window[wname]["masses"], Z, with_m4)
            ret = np.array([b for b, (_, g) in zip(betas, labels)
                            if g == "retained"])
            dis = np.array([b for b, (_, g) in zip(betas, labels)
                            if g == "discarded"])
            B_R = float(W_RETAINED * ret.sum())
            B_D = float(V_DISCARDED * dis.sum())
            abs_R = float((W_RETAINED * np.abs(ret)).sum())
            abs_D = float((V_DISCARDED * np.abs(dis)).sum())
            variants[f"{wname}|{fname}"] = {
                "window": wname, "fit_form": fname,
                "beta": {lab: float(b) for (lab, _), b in zip(labels, betas)},
                "status": {lab: s for (lab, _), s in zip(labels, status)},
                "residual_max_abs": {lab: r
                                     for (lab, _), r in zip(labels, resids)},
                "step2_design": d,
                "B_R": B_R, "B_D": B_D,
                "R_signed": float(abs(B_D) / abs(B_R)) if B_R != 0.0 else None,
                "R_abs": float(abs_D / abs_R) if abs_R != 0.0 else None,
            }

    # `E5`: one component's beta recomputed in a second independent pass.
    wname, fname = "LIGHT", "V2a_with_m4"
    Zb, _ = step1_Z(WINDOWS[wname], dJ2, dJ, recipes)
    betas_b, _, _, _ = step2_beta(WINDOWS[wname], Zb, FIT_FORMS[fname])
    first = variants[f"{wname}|{fname}"]["beta"][labels[0][0]]
    second = float(betas_b[0])
    repro = {"component": labels[0][0], "variant": f"{wname}|{fname}",
             "first_pass": first, "second_pass": second,
             "identical_at_printed_precision":
                 f"{first:.12e}" == f"{second:.12e}"}

    # `M1` weight identity: the landed axis-TT bubble against the mean of the
    # per-component bubbles over the five retained recipes.
    q0, mtest = float(Q_GRID[0]), float(WINDOWS["LIGHT"][0])
    landed = float(pl.g2_axis_proca(q0, EXTENT, mtest, dJ2, dJ))
    percomp = ext01.component_bubble(q0, EXTENT, mtest, dJ2, dJ,
                                     [r for _, _, r in RETAINED])
    mean_percomp = float(W_RETAINED * percomp.sum())
    weight_check = {"q0": q0, "mass": mtest,
                    "landed_g2_axis_proca": landed,
                    "mean_of_per_component_over_retained": mean_percomp,
                    "abs_difference": abs(landed - mean_percomp),
                    "relative_difference":
                        abs(landed - mean_percomp) / abs(landed)
                        if landed != 0.0 else None}

    return {"parameters": {
                "extent": EXTENT, "q_grid": list(map(float, Q_GRID)),
                "windows": {k: [float(x) for x in v]
                            for k, v in WINDOWS.items()},
                "fit_forms": FIT_FORMS,
                "w_retained": W_RETAINED, "v_discarded": V_DISCARDED,
                "n_retained": len(RETAINED), "n_discarded": len(DISCARDED)},
            "cost": cost, "weight_identity_check": weight_check,
            "per_window": per_window, "variants": variants,
            "reproduction_check": repro}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    out = run()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=1, sort_keys=True),
                        encoding="utf-8")
    c = out["cost"]
    print(f"M3 cost: one mass point {c['seconds_one_mass_point']:.2f}s, "
          f"{c['n_mass_points_total']} points, projected "
          f"{c['projected_total_seconds']:.1f}s")
    w = out["weight_identity_check"]
    print(f"weight identity: landed {w['landed_g2_axis_proca']:.12e}  "
          f"mean-per-component {w['mean_of_per_component_over_retained']:.12e}  "
          f"reldiff {w['relative_difference']:.3e}")
    print(f"written: {args.out}")


if __name__ == "__main__":
    main()
