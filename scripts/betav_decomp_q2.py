"""q^2-level transverse/longitudinal sector decomposition of the Proca bubble.

Phase-1 REVISION support for `P2-BETAV-CIRC-01` (still NO k-scan, NO target).

The material question is NOT whether the one-graviton vertex off-block norm
vanishes as q->0, but whether the MIXED sector contributes to the extracted
q^2 coefficient (the induced Z): a vertex mixing U_TL = O(q) still gives a
finite bubble term U_TL*U_LT = O(q^2).

We decompose the recovered Proca axis-TT bubble (same construction as
`proca_loop.g2_axis_proca`) into sectors using projectors built INDEPENDENTLY
from a(k) and a(k+q):

    Pi_bubble(q) = Pi_TT + Pi_TL + Pi_LT + Pi_LL,
    G1 -> P_X(k) G1,   G2 -> P_Y(k+q) G2,   X,Y in {T,L}.

For each sector we extract the q^2 coefficient [Pi_X(q)-Pi_X(0)]/q^2 by an
even fit, and report the observed small-q scaling exponent of |Pi_X(q)-Pi_X(0)|
(a log-log slope) WITHOUT fitting toward any supplied value.

Pre-registered protocol (fixed before running):
  * q-grids (three ranges, stability): R1=[.10,.16,.22,.28],
    R2=[.15,.25,.35,.45], R3=[.08,.12,.16,.20];
  * derivative epsilon: proca_loop.EPSF (= 1e-3, the recovered value);
  * fit form: Pi(q) = A + B q^2 + C q^4  (B is the sector's Z contribution);
  * scaling exponent: slope of log|Pi(q)-A| vs log q (A from the fit);
  * stability: compare B across the three ranges and n in {10,12};
  * seagull is q-independent by construction (delta^2 M carries no q) -> it
    contributes to Pi(0) only, not to B; verified separately, not assumed.

No numerical target (-3, -(k+2)) is encoded. Outputs ->
`results/P2-BETAV-CIRC-01/decomp/regen/` (gitignored).

Run::

    python scripts/betav_decomp_q2.py [--n N]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "recovered_2026"))

import proca_loop as pl  # noqa: E402
from mlog_coeff import TT_RECIPES  # noqa: E402


def _projectors(a):
    """P_L, P_T (npts,4,4) from a (npts,4) complex: P_L = a a^dag / (a^dag a).

    At a=0 (the BZ origin) the longitudinal direction is undefined and the Proca
    propagator is isotropic I/m^2; there P_L is set to 0 (measure-zero point).
    """
    s2 = np.sum(np.abs(a) ** 2, axis=1)                      # (npts,)
    safe = s2 > 1e-14
    PL = np.zeros((a.shape[0], 4, 4), dtype=complex)
    PL[safe] = (np.einsum("pu,pv->puv", a[safe], np.conj(a[safe]))
                / s2[safe, None, None])
    PT = np.eye(4)[None] - PL
    return PT, PL


def sector_bubble(q0, n, m, dJ2, dJ):
    """Return dict of sector Pi contributions {TT,TL,LT,LL,total} at axis q0."""
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    R2 = np.stack([sum(c * dJ2[p] for p, c in r) for r in TT_RECIPES])
    Rm = np.stack([sum(c * dJ[p] for p, c in r) for r in TT_RECIPES])
    acc = {kk: 0.0 for kk in ("TT", "TL", "LT", "LL", "total")}
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        G1 = pl.G_flat(kk, m)
        G2 = pl.G_flat(kkq, m)
        a1, b1 = pl.avec(kk), pl.avec(kkq)
        U1 = 2.0 * pl.kin_form(R2, np.conj(a1), b1) + m**2 * Rm[:, None, :, :]
        a2, b2 = pl.avec(kkq), pl.avec(kk)
        U2 = 2.0 * pl.kin_form(R2, np.conj(a2), b2) + m**2 * Rm[:, None, :, :]
        PTk, PLk = _projectors(pl.avec(kk))          # basis a(k)
        PTq, PLq = _projectors(pl.avec(kkq))         # basis a(k+q)
        Gk = {"T": np.einsum("pij,pjk->pik", PTk, G1),
              "L": np.einsum("pij,pjk->pik", PLk, G1)}
        Gq = {"T": np.einsum("pij,pjk->pik", PTq, G2),
              "L": np.einsum("pij,pjk->pik", PLq, G2)}
        for X in ("T", "L"):
            Xr = np.einsum("pij,rpjk->rpik", Gk[X], U1)
            for Y in ("T", "L"):
                Yr = np.einsum("pij,rpjk->rpik", Gq[Y], U2)
                val = (-0.5) * np.einsum("rpij,rpji->", Xr, Yr).real
                acc[X + Y] += val
        # full (no projectors) for consistency
        Xf = np.einsum("pij,rpjk->rpik", G1, U1)
        Yf = np.einsum("pij,rpjk->rpik", G2, U2)
        acc["total"] += (-0.5) * np.einsum("rpij,rpji->", Xf, Yf).real
    return {k: v / n**4 / 5.0 for k, v in acc.items()}


def _fit_even(eps, vals):
    A = np.vander(eps**2, 3, increasing=True)   # [1, q^2, q^4]
    coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
    return coef  # [A, B(q^2), C(q^4)]


def _loglog_exponent(eps, vals, A):
    y = np.abs(np.array(vals) - A)
    good = y > 0
    if good.sum() < 2:
        return None
    p = np.polyfit(np.log(eps[good]), np.log(y[good]), 1)[0]
    return float(p)


def run(n=12):
    m = 0.3
    dJ2, dJ, _, _ = pl.derivsV()
    ranges = {"R1": np.array([0.10, 0.16, 0.22, 0.28]),
              "R2": np.array([0.15, 0.25, 0.35, 0.45]),
              "R3": np.array([0.08, 0.12, 0.16, 0.20])}
    out = {"n": n, "m": m, "sectors": ["TT", "TL", "LT", "LL", "total"],
           "by_range": {}}
    for rname, eps in ranges.items():
        data = {s: [] for s in ("TT", "TL", "LT", "LL", "total")}
        for e in eps:
            sb = sector_bubble(float(e), n, m, dJ2, dJ)
            for s in data:
                data[s].append(sb[s])
        rec = {}
        for s in data:
            vals = np.array(data[s])
            coef = _fit_even(eps, vals)
            rec[s] = {"q2_coeff_B": float(coef[1]), "Pi0_A": float(coef[0]),
                      "scaling_exponent": _loglog_exponent(eps, vals, coef[0]),
                      "vals": [float(x) for x in vals]}
        # mixed = TL + LT combined q^2 coefficient
        mixed_vals = np.array(data["TL"]) + np.array(data["LT"])
        cm = _fit_even(eps, mixed_vals)
        rec["TL_plus_LT"] = {"q2_coeff_B": float(cm[1]), "Pi0_A": float(cm[0]),
                             "scaling_exponent": _loglog_exponent(
                                 eps, mixed_vals, cm[0])}
        # consistency: sum of sector q^2 coeffs vs total
        ssum = sum(rec[s]["q2_coeff_B"] for s in ("TT", "TL", "LT", "LL"))
        rec["_sum_sectors_q2"] = ssum
        rec["_total_q2"] = rec["total"]["q2_coeff_B"]
        rec["_consistency_abs_diff"] = abs(ssum - rec["total"]["q2_coeff_B"])
        out["by_range"][rname] = rec
    return out


def main():
    n = 12
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    res = run(n)
    regen = (_HERE.parent / "results" / "P2-BETAV-CIRC-01" / "decomp" / "regen")
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "decomp_q2.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("P2-BETAV-CIRC-01 q^2 sector decomposition (no target)")
    print("=" * 60)
    for rname, rec in res["by_range"].items():
        print(f"[{rname}]  (n={res['n']}, m={res['m']})")
        for s in ("TT", "TL_plus_LT", "LL", "total"):
            r = rec[s]
            exp = r.get("scaling_exponent")
            exps = f"{exp:.2f}" if exp is not None else "n/a"
            print(f"   {s:11s}: q^2 coeff = {r['q2_coeff_B']:+.4e}   "
                  f"scaling exp(Pi-Pi0 ~ q^p) = {exps}")
        print(f"   consistency |sum sectors - total| = "
              f"{rec['_consistency_abs_diff']:.2e}")


if __name__ == "__main__":
    main()
