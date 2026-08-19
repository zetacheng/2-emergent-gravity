"""Diagnostic for `P2-RECON-EXT-01`: the external space the axis-TT projection
discards.

**This is a DIAGNOSTIC, not part of any reconstruction.**  It lives outside
``scripts/recon2026/`` deliberately: the clean-room construction is frozen and
this script is not part of it.  It modifies no existing file.

What it does.  The recovered Proca bubble is a bilinear form on the ten
independent components of the symmetric external perturbation ``h_{mu nu}``.
The axis-TT projection retains five of those ten.  This script evaluates the
same bubble on each of the ten orthonormal components separately -- five
retained, five discarded -- at one pre-registered parameter point, and reports
each component's ``q^2`` coefficient and its share of the sum over all ten.

What it does NOT do, and these are constraints of the governing specification:

  * it computes no ``beta`` quantity of any species, no ratio of two such
    quantities, and nothing the frozen anchor ranges over (K1);
  * it performs no scan over the determinant power; that power is fixed at the
    pre-registered value and, as ``report_k_usage`` records, the bubble does
    not take it as an argument at all (K2);
  * it reads no target from ``GATES.md`` (K3).

Imports, disclosed because the governing specification requires it.  This
script imports ``proca_loop``, ``seagull_check`` and ``mlog_coeff`` from
``scripts/recovered_2026/``.  ``proca_loop``'s module docstring carries an
analytic target for the species ratio.  Nothing in this script reads, prints,
stores or compares against it; the imports are used for the geometric
derivatives, the flat propagator, the kinetic bilinear form, and the retained
recipes.

Run::

    python scripts/diagnostics/ext01_discarded_external_space.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_RECOVERED = Path(__file__).resolve().parents[1] / "recovered_2026"
sys.path.insert(0, str(_RECOVERED))

import proca_loop as pl  # noqa: E402
from mlog_coeff import TT_RECIPES  # noqa: E402
from seagull_check import PAIRS, hmat  # noqa: E402

# --------------------------------------------------------------------------
# pre-registered parameters -- fixed in the artifact before this file existed
# --------------------------------------------------------------------------
K_DETERMINANT_POWER = 1
EXTENT = 12
MASS = 0.3
Q_GRID = (0.10, 0.16, 0.22, 0.28)

# --------------------------------------------------------------------------
# the ten orthonormal external components
# --------------------------------------------------------------------------
RETAINED = [
    ("R1", "(h11 - h22)/sqrt(2)", TT_RECIPES[0]),
    ("R2", "(h11 + h22 - 2 h33)/sqrt(6)", TT_RECIPES[1]),
    ("R3", "(1,2) direction", TT_RECIPES[2]),
    ("R4", "(1,3) direction", TT_RECIPES[3]),
    ("R5", "(2,3) direction", TT_RECIPES[4]),
]

DISCARDED = [
    ("D1", "h00", [((0, 0), 1.0)]),
    ("D2", "(0,1) direction", [((0, 1), 1 / np.sqrt(2))]),
    ("D3", "(0,2) direction", [((0, 2), 1 / np.sqrt(2))]),
    ("D4", "(0,3) direction", [((0, 3), 1 / np.sqrt(2))]),
    ("D5", "spatial trace (h11 + h22 + h33)/sqrt(3)",
     [((1, 1), 1 / np.sqrt(3)), ((2, 2), 1 / np.sqrt(3)),
      ((3, 3), 1 / np.sqrt(3))]),
]


def basis_check():
    """Orthonormality and completeness of the ten, in the Frobenius norm."""
    mats = np.stack([hmat(r) for _, _, r in RETAINED + DISCARDED])
    gram = np.einsum("iab,jab->ij", mats, mats)
    identity = np.eye(mats.shape[0])
    return {
        "n_retained": len(RETAINED),
        "n_discarded": len(DISCARDED),
        "n_total": len(RETAINED) + len(DISCARDED),
        "n_pairs_full_space": len(PAIRS),
        "gram_max_abs_deviation_from_identity": float(
            np.abs(gram - identity).max()
        ),
        "orthonormal": bool(np.allclose(gram, identity, atol=1e-12)),
        "rank": int(np.linalg.matrix_rank(mats.reshape(mats.shape[0], -1))),
    }


def component_bubble(q0, n, m, dJ2, dJ, recipes):
    """The bubble evaluated on each supplied external component.

    Same construction as the recovered axis-TT bubble, with the external
    contraction taken over the supplied components instead of over the five
    retained ones, and WITHOUT the internal transverse/longitudinal split.
    Returns one value per component, not averaged.
    """
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    R2 = np.stack([sum(c * dJ2[p] for p, c in r) for r in recipes])
    Rm = np.stack([sum(c * dJ[p] for p, c in r) for r in recipes])
    acc = np.zeros(len(recipes))
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        G1 = pl.G_flat(kk, m)
        G2 = pl.G_flat(kkq, m)
        a1, b1 = pl.avec(kk), pl.avec(kkq)
        U1 = 2.0 * pl.kin_form(R2, np.conj(a1), b1) + m**2 * Rm[:, None, :, :]
        a2, b2 = pl.avec(kkq), pl.avec(kk)
        U2 = 2.0 * pl.kin_form(R2, np.conj(a2), b2) + m**2 * Rm[:, None, :, :]
        X = np.einsum("pij,rpjk->rpik", G1, U1)
        Y = np.einsum("pij,rpjk->rpik", G2, U2)
        acc += (-0.5) * np.einsum("rpij,rpji->r", X, Y).real
    return acc / n**4


def fit_even(eps, vals):
    A = np.vander(np.asarray(eps, float) ** 2, 3, increasing=True)
    coef, *_ = np.linalg.lstsq(A, np.asarray(vals, float), rcond=None)
    return coef


def loglog_exponent(eps, vals, a0):
    eps = np.asarray(eps, float)
    d = np.abs(np.asarray(vals, float) - a0)
    if np.any(d <= 0):
        return None
    slope = np.polyfit(np.log(eps), np.log(d), 1)[0]
    return float(slope)


def report_k_usage():
    """Which of the functions used here takes the determinant power.

    Measured rather than asserted: the bubble's call signatures are inspected,
    not described from memory.
    """
    import inspect

    names = {}
    for func in (component_bubble, pl.G_flat, pl.avec, pl.kin_form, pl.derivsV):
        names[func.__name__] = list(
            inspect.signature(func).parameters.keys()
        )
    return names


def run():
    labels = [(n, d) for n, d, _ in RETAINED] + [(n, d) for n, d, _ in DISCARDED]
    recipes = [r for _, _, r in RETAINED] + [r for _, _, r in DISCARDED]

    dJ2, dJ, _, _ = pl.derivsV()
    series = []
    for q0 in Q_GRID:
        series.append(component_bubble(float(q0), EXTENT, MASS, dJ2, dJ, recipes))
    series = np.stack(series)  # (nq, ncomp)

    rows = []
    for i, (name, desc) in enumerate(labels):
        vals = series[:, i]
        coef = fit_even(Q_GRID, vals)
        rows.append(
            {
                "component": name,
                "description": desc,
                "group": "retained" if i < len(RETAINED) else "discarded",
                "q2_coefficient": float(coef[1]),
                "pi0": float(coef[0]),
                "scaling_exponent": loglog_exponent(Q_GRID, vals, coef[0]),
                "values": [float(v) for v in vals],
            }
        )

    total = sum(r["q2_coefficient"] for r in rows)
    ret = sum(r["q2_coefficient"] for r in rows if r["group"] == "retained")
    dis = sum(r["q2_coefficient"] for r in rows if r["group"] == "discarded")
    for r in rows:
        r["fraction_of_total"] = (
            float(r["q2_coefficient"] / total) if total != 0.0 else None
        )

    return {
        "parameters": {
            "k_determinant_power": K_DETERMINANT_POWER,
            "extent": EXTENT,
            "mass": MASS,
            "q_grid": list(Q_GRID),
            "epsf": float(pl.EPSF),
            "fit_form": "Pi(q) = A + B q^2 + C q^4",
        },
        "basis_check": basis_check(),
        "k_usage": report_k_usage(),
        "rows": rows,
        "sum_q2_all_ten": float(total),
        "sum_q2_retained": float(ret),
        "sum_q2_discarded": float(dis),
        "retained_fraction": float(ret / total) if total != 0.0 else None,
        "discarded_fraction": float(dis / total) if total != 0.0 else None,
        "mean_q2_retained": float(ret / len(RETAINED)),
    }


def main():
    out = run()
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
