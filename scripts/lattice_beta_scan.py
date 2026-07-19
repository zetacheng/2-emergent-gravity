"""Gate ``P2-BETA-01`` — lattice mass-scan extraction of ``beta_B``.

Computes the induced Einstein--Hilbert kinetic coefficient of a minimally
coupled real scalar on the lattice,

    Z_lat(m^2) = (1/12) * int_BZ d^4p/(2pi)^4  1/(phat^2 + m^2),
    phat^2 = sum_mu 4 sin^2(p_mu/2),

scans ``m = m_B a in [0.125, 0.55]``, and fits

    Z(m) = z0 + z1 m^2 + beta m^2 ln(m^2) + z2 m^4

to extract ``beta_B``.  The uncertainty is the *spread* over fit window, ansatz
(with/without ``z2 m^4``), and lattice volume (infinite-volume BZ integral vs
finite ``L^4`` sums) -- not a formal fit error.

Contains no paper value and is not tuned toward one.  Run bare::

    python -m scripts.lattice_beta_scan
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

PREFACTOR = 1.0 / 12.0  # (1/6 - xi)/2 with xi = 0, minimal coupling


# ---------------------------------------------------------------------------
# The scalar tadpole <phi^2> on the lattice
# ---------------------------------------------------------------------------
def phi2_integral(m2: float, n: int = 96, shift: float = 0.5) -> float:
    """Infinite-volume BZ integral int 1/(phat^2 + m^2), midpoint quadrature.

    ``shift=0.5`` keeps nodes off p=0 (harmless here since m^2>0, but keeps the
    quadrature symmetric); ``phat^2 = sum 4 sin^2(p/2) = sum 2(1-cos p)``.
    Memory-safe: accumulates over slices of the first axis.
    """
    k = (np.arange(n) + shift) / n * 2.0 * math.pi - math.pi
    phat1 = 2.0 * (1.0 - np.cos(k))  # 4 sin^2(p/2) per axis
    p3 = phat1[:, None, None] + phat1[None, :, None] + phat1[None, None, :]
    total = 0.0
    for i in range(n):
        total += np.sum(1.0 / (p3 + phat1[i] + m2))
    return total / n**4


def phi2_finite_volume(m2: float, L: int) -> float:
    """Finite-volume L^4 momentum sum (1/L^4) sum_n 1/(phat^2 + m^2).

    Periodic momenta p_mu = 2 pi n_mu / L, n_mu = 0..L-1 (includes p=0, finite
    since m^2>0).  Used only as a lattice-volume systematic.
    """
    n = np.arange(L)
    k = 2.0 * math.pi * n / L
    phat1 = 2.0 * (1.0 - np.cos(k))
    p3 = phat1[:, None, None] + phat1[None, :, None] + phat1[None, None, :]
    total = 0.0
    for i in range(L):
        total += np.sum(1.0 / (p3 + phat1[i] + m2))
    return total / L**4


def Z_lat(m: float, n: int = 96) -> float:
    """Induced EH coefficient Z_lat(m^2) = (1/12) <phi^2>_lat."""
    return PREFACTOR * phi2_integral(m * m, n=n)


# ---------------------------------------------------------------------------
# Fit
# ---------------------------------------------------------------------------
def _design(masses: np.ndarray, with_m4: bool) -> np.ndarray:
    m2 = masses**2
    cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
    if with_m4:
        cols.append(m2**2)
    return np.vstack(cols).T


def fit_beta(masses, Z, with_m4: bool = True):
    """Linear least-squares fit; returns (beta, coefficients, residual_rms)."""
    A = _design(np.asarray(masses, float), with_m4)
    y = np.asarray(Z, float)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    rms = float(np.sqrt(np.mean(resid**2)))
    beta = float(coef[2])  # coefficient of m^2 ln m^2
    return beta, coef.tolist(), rms


# ---------------------------------------------------------------------------
# Scan + systematics
# ---------------------------------------------------------------------------
def default_masses():
    return np.linspace(0.125, 0.55, 18)


def run_systematics(n_grid: int = 128) -> dict:
    """Central fit + systematic variations.

    Primary uncertainty is the spread over fit *window* and *ansatz* at infinite
    volume.  The lattice-*volume* variation is reported separately as a
    convergence trend: small ``L`` is quadrature-limited (few momentum modes
    resolve the IR log poorly), so folding tiny ``L`` in as an equal-weight
    outlier would misstate the uncertainty.
    """
    masses = default_masses()
    Zinf = np.array([Z_lat(m, n=n_grid) for m in masses])

    # Central: full window, with m^4
    b0, c0, r0 = fit_beta(masses, Zinf, with_m4=True)

    # Primary systematics: window + ansatz, all at infinite volume
    primary = {"central_full_window_with_m4": b0}
    primary["no_m4"] = fit_beta(masses, Zinf, with_m4=False)[0]
    windows = {
        "win_0.15_0.50": (0.15, 0.50),
        "win_0.20_0.55": (0.20, 0.55),
        "win_0.125_0.45": (0.125, 0.45),
        "win_0.175_0.525": (0.175, 0.525),
    }
    for name, (lo, hi) in windows.items():
        sel = (masses >= lo - 1e-9) & (masses <= hi + 1e-9)
        primary[name] = fit_beta(masses[sel], Zinf[sel], with_m4=True)[0]

    # Volume convergence trend (reported separately, not in primary spread)
    volume_trend = {}
    for L in (24, 32, 48):
        ZL = np.array([PREFACTOR * phi2_finite_volume(m * m, L) for m in masses])
        volume_trend[f"L{L}"] = fit_beta(masses, ZL, with_m4=True)[0]
    volume_trend["Linf"] = b0

    pvals = np.array(list(primary.values()))
    return {
        "masses": masses.tolist(),
        "Z_inf_volume": Zinf.tolist(),
        "central_coefficients_[z0,z1,beta,z2]": c0,
        "central_residual_rms": r0,
        "primary_variants_window_ansatz": primary,
        "volume_trend": volume_trend,
        "beta_central": b0,
        "beta_primary_spread": float(pvals.max() - pvals.min()),
        "beta_primary_std": float(np.std(pvals)),
        "raw_tadpole_coefficient_beta_over_prefactor": b0 / PREFACTOR,
    }


def results_dict() -> dict:
    res = run_systematics()
    res["note"] = (
        "beta_B is the fitted coefficient of m^2 ln m^2 in Z=(1/12)<phi^2>_lat; "
        "sign is positive in this convention (P2-HK-01 uses opposite overall "
        "sign; magnitude is the robust quantity)."
    )
    return res


def main() -> None:
    res = results_dict()
    regen = Path(__file__).resolve().parents[1] / "results" / "P2-BETA-01" / "regen"
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "lattice_beta_scan.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    print("Gate P2-BETA-01 — lattice mass-scan extraction of beta_B")
    print("=" * 60)
    print(f"  scan: m in [{res['masses'][0]:.3f}, {res['masses'][-1]:.3f}], "
          f"{len(res['masses'])} points")
    print(f"  central beta_B = {res['beta_central']:.6e}")
    print(f"  1/(192 pi^2)   = {1.0/(192*math.pi**2):.6e}  (continuum target, mag.)")
    print("  primary variants (window + ansatz, infinite volume):")
    for k, v in res["primary_variants_window_ansatz"].items():
        print(f"    {k:26s} beta = {v:.6e}")
    print(f"  primary spread = {res['beta_primary_spread']:.3e}   "
          f"std = {res['beta_primary_std']:.3e}")
    print("  volume convergence trend (finite L^4 -> infinite):")
    for k, v in res["volume_trend"].items():
        print(f"    {k:6s} beta = {v:.6e}")


if __name__ == "__main__":
    main()
