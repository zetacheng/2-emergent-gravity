"""Operator-level checks of the recovered lattice Proca determinant.

Phase-1 adjudication support for `P2-BETAV-CIRC-01` (NO k-scan, NO target).
Records, from the *actual* recovered `proca_loop.py` / `boson_loop.py`
operators:

1. the flat Proca kernel eigenstructure `{p̂²+m² (×3), m² (×1)}`;
2. the longitudinal eigenvalue is exactly `m²`, invariant under `p̂²`
   (ultralocal), whereas the external scalar operator is `Δ₀ = p̂²+m²`
   (propagating) — so the two are different operators;
3. the propagator eigenvalues: transverse `1/(p̂²+m²)`, longitudinal `1/m²`;
4. whether the one-graviton vertex `δM` keeps the flat transverse/longitudinal
   split block-diagonal (it does not — off-block elements are nonzero).

No numerical target (`−3`, `−(k+2)`) appears here. Outputs go to
`results/P2-BETAV-CIRC-01/decomp/regen/` (gitignored).

Run::

    python scripts/betav_decomp_check.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "recovered_2026"))

import proca_loop as pl  # noqa: E402
from boson_loop import MB_flat  # noqa: E402


def _phat2(kv):
    a = np.array([np.exp(1j * kv[mu]) - 1.0 for mu in range(4)])
    return float(np.sum(np.abs(a) ** 2)), a


def proca_eigenstructure(m, momenta):
    out = []
    for kv in momenta:
        kk = [np.array([kv[mu]]) for mu in range(4)]
        M = pl.M_full(kk, np.zeros((4, 4)), m)[0]
        ev = np.sort(np.linalg.eigvalsh(M)).tolist()
        p2, _ = _phat2(kv)
        out.append({"k": list(kv), "phat2": p2, "phat2_plus_m2": p2 + m * m,
                    "m2": m * m, "eigenvalues": [round(x, 8) for x in ev]})
    return out


def longitudinal_invariance(m, momenta):
    # smallest eigenvalue (longitudinal) vs m^2 across momenta with varying p̂^2
    rows = []
    for kv in momenta:
        kk = [np.array([kv[mu]]) for mu in range(4)]
        M = pl.M_full(kk, np.zeros((4, 4)), m)[0]
        lam_min = float(np.min(np.linalg.eigvalsh(M).real))
        p2, _ = _phat2(kv)
        rows.append({"phat2": p2, "long_eigenvalue": lam_min})
    spread = max(r["long_eigenvalue"] for r in rows) - min(
        r["long_eigenvalue"] for r in rows)
    return {"rows": rows, "m2": m * m,
            "long_eigenvalue_spread_over_phat2": spread}


def scalar_vs_longitudinal(m, momenta):
    # external scalar operator Delta0 = p̂^2 + m^2 (propagating) vs Proca
    # longitudinal factor m^2 (ultralocal). Compare, and their propagators.
    rows = []
    for kv in momenta:
        kk = [np.array([kv[mu]]) for mu in range(4)]
        delta0 = float(MB_flat(kk, m)[0])                 # p̂^2 + m^2
        p2, _ = _phat2(kv)
        # Proca longitudinal propagator eigenvalue (from G_flat acting on â)
        G = pl.G_flat(kk, m)[0]
        _, a = _phat2(kv)
        ah = a / np.linalg.norm(a)
        long_prop = float(np.real(ah.conj() @ G @ ah))
        rows.append({"phat2": p2, "scalar_Delta0": delta0,
                     "proca_long_factor_m2": m * m,
                     "long_propagator_eig": long_prop,
                     "one_over_m2": 1.0 / (m * m)})
    return rows


def vertex_TL_mixing(m, kv, q, pairs):
    dJ2, dJ, _, _ = pl.derivsV()
    kk = [np.array([kv[mu]]) for mu in range(4)]
    _, a = _phat2(kv)
    ah = a / np.linalg.norm(a)
    Q, _ = np.linalg.qr(np.column_stack([ah, np.eye(4)]))
    Tb = Q[:, 1:4]  # 3 transverse directions
    rows = []
    for p in pairs:
        U = pl.vertexV(kk, q, dJ2[p], dJ[p], m)[0]
        off = np.abs(Tb.conj().T @ U @ ah)          # <T|delta M|L>
        rows.append({"pair": list(p),
                     "max_offblock_T_L": float(np.max(off)),
                     "offblock_T_L": [float(x) for x in off]})
    max_mix = max(r["max_offblock_T_L"] for r in rows)
    return {"rows": rows, "max_transverse_longitudinal_mixing": max_mix}


def results_dict():
    m = 0.3
    momenta = [(0.4, 0, 0, 0), (0.5, 0.7, 0, 0), (1.0, 0.3, 0.9, 0.2),
               (0.2, 0.2, 0.2, 0.2)]
    from seagull_check import PAIRS
    return {
        "m": m,
        "note": ("operator-level checks only; NO k-scan, NO numerical target. "
                 "Longitudinal factor is ultralocal m^2, not the propagating "
                 "scalar Delta0 = phat^2+m^2; graviton vertex mixes T and L."),
        "proca_eigenstructure": proca_eigenstructure(m, momenta),
        "longitudinal_invariance": longitudinal_invariance(m, momenta),
        "scalar_vs_longitudinal": scalar_vs_longitudinal(m, momenta),
        "vertex_TL_mixing": vertex_TL_mixing(m, (0.5, 0.7, 0.2, 0.0),
                                             (0.25, 0, 0, 0), PAIRS),
    }


def main():
    res = results_dict()
    regen = (_HERE.parent / "results" / "P2-BETAV-CIRC-01" / "decomp" / "regen")
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "decomp_check.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("P2-BETAV-CIRC-01 operator-level decomposition checks (no target)")
    print("=" * 62)
    es = res["proca_eigenstructure"][1]
    print(f"  Proca eigenvalues @k={es['k']}: {es['eigenvalues']}")
    print(f"    -> {{phat^2+m^2={es['phat2_plus_m2']:.4f} x3, "
          f"m^2={es['m2']:.4f} x1}}")
    li = res["longitudinal_invariance"]
    print(f"  longitudinal eigenvalue spread over varying phat^2: "
          f"{li['long_eigenvalue_spread_over_phat2']:.2e}  (m^2={li['m2']:.4f})")
    sv = res["scalar_vs_longitudinal"][1]
    print(f"  scalar Delta0=phat^2+m^2={sv['scalar_Delta0']:.4f}  vs  "
          f"proca longitudinal m^2={sv['proca_long_factor_m2']:.4f}  "
          f"(long propagator eig={sv['long_propagator_eig']:.4f} ~ 1/m^2="
          f"{sv['one_over_m2']:.4f})")
    mx = res["vertex_TL_mixing"]["max_transverse_longitudinal_mixing"]
    print(f"  max |<T| delta M |L>| (graviton vertex T-L mixing): {mx:.4f}  "
          f"(nonzero => no invariant split)")


if __name__ == "__main__":
    main()
