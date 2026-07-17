"""Gate ``P2-GAP-01`` — continuum and lattice gap-equation criticality.

Derives and computes the critical scalar-channel four-fermion coupling ``G_c``:

* continuum, sharp Euclidean 4-ball ``|p| < Lambda``: ``I_0 = Lambda^2/(16 pi^2)``,
  ``G_c = 1/(2 I_0) = 8 pi^2 / Lambda^2`` (exact, ``c = 8`` in ``c pi^2/Lambda^2``);
* lattice, Wilson ``r = 1``: ``I_0`` is the untraced scalar bubble at the chiral
  point, ``I_0 = int_BZ 1/(sum_mu sin^2 p_mu + W(p)^2)``, ``W = sum_mu(1-cos p_mu)``.

The relation ``G_c = 1/(2 I_0)`` is derived in
``derivations/P2-GAP-01_gap_criticality.md`` (channel-coupling normalization,
Dirac trace absorbed into ``G``). No paper value appears here or tunes anything.

Run bare from the repository root::

    python -m scripts.gap_criticality
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------------
# Continuum, sharp 4-ball
# ---------------------------------------------------------------------------
def continuum_I0(Lambda: float = 1.0) -> float:
    """I_0^cont = Lambda^2/(16 pi^2) (untraced scalar bubble, |p|<Lambda)."""
    return Lambda**2 / (16.0 * math.pi**2)


def continuum_Gc(Lambda: float = 1.0) -> float:
    """G_c = 1/(2 I_0) = 8 pi^2/Lambda^2 (c = 8 in c pi^2/Lambda^2)."""
    return 1.0 / (2.0 * continuum_I0(Lambda))


def continuum_c() -> float:
    """The exact coefficient c in G_c = c pi^2 / Lambda^2 (= 8)."""
    return continuum_Gc(1.0) / math.pi**2


# ---------------------------------------------------------------------------
# Lattice, Wilson r = 1
# ---------------------------------------------------------------------------
def _axis(n: int, shift: float) -> np.ndarray:
    """Product-midpoint nodes on (-pi, pi]; shift in [0,1) offsets the grid."""
    return (np.arange(n) + 0.5 + shift) / n * 2.0 * math.pi - math.pi


def lattice_I0(n: int = 96, r: float = 1.0, shift: float = 0.0,
               m: float = 0.0) -> float:
    """Lattice gap-equation integral I_0 (Wilson) by BZ product quadrature.

    I_0 = int_BZ d^4p/(2pi)^4  1/(sum_mu sin^2 p_mu + W(p)^2),
    W(p) = m + r sum_mu (1 - cos p_mu).  Memory-safe: sums over slices of the
    first axis.  ``shift`` selects a half-shifted (offset) grid for the
    convergence cross-check.  ``m`` is the fermion reference mass entering the
    Wilson term: ``m=0`` is the massless chiral point; a small ``m`` (e.g.
    0.02) is the value at which a lattice gap-equation evaluation is done.
    """
    k = _axis(n, shift)
    sin2 = np.sin(k) ** 2
    omc = 1.0 - np.cos(k)  # 1 - cos p on each axis
    # precompute the 3D inner sums once
    s3 = sin2[:, None, None] + sin2[None, :, None] + sin2[None, None, :]
    w3 = omc[:, None, None] + omc[None, :, None] + omc[None, None, :]
    total = 0.0
    for i in range(n):
        s = s3 + sin2[i]
        w = m + r * (w3 + omc[i])
        total += np.sum(1.0 / (s + w * w))
    return total / n**4


def lattice_I0_finite_volume(L: int, r: float = 1.0, m: float = 0.0) -> float:
    """Finite-volume L^4 momentum sum for I_0 (periodic momenta p=2 pi n/L).

    Mirrors the paper's finite-lattice evaluation (e.g. its ``0.0845 at
    ma=0.02 on 64^4``).  The p=0 mode is finite whenever ``m>0``; if ``m=0``
    it is dropped (the massless zero mode).
    """
    k = 2.0 * math.pi * np.arange(L) / L
    sin2 = np.sin(k) ** 2
    omc = 1.0 - np.cos(k)
    s3 = sin2[:, None, None] + sin2[None, :, None] + sin2[None, None, :]
    w3 = omc[:, None, None] + omc[None, :, None] + omc[None, None, :]
    total = 0.0
    for i in range(L):
        s = s3 + sin2[i]
        w = m + r * (w3 + omc[i])
        d = s + w * w
        with np.errstate(divide="ignore"):
            inv = 1.0 / d
        if m == 0.0:
            inv[~np.isfinite(inv)] = 0.0
        total += np.sum(inv)
    return total / L**4


def lattice_Gc(I0: float) -> float:
    """G_c = 1/(2 I_0)."""
    return 1.0 / (2.0 * I0)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def lattice_convergence(sizes=(64, 96, 128), shifts=(0.0, 0.25)) -> dict:
    """Grid-refinement and offset-grid cross-check for the lattice I_0.

    Both shifts keep every node off the p=0 integrable singularity (a node
    lands on the origin only for shift=0.5 with even n), while sampling the
    integrand differently, so their agreement bounds the discretization error.
    """
    table = {}
    for n in sizes:
        table[n] = {f"shift_{s}": lattice_I0(n=n, shift=s) for s in shifts}
    return table


def reference_mass_evaluation(m_ref: float = 0.02) -> dict:
    """Evaluate I_0 at a small reference fermion mass (the paper's setup).

    The paper evaluates I_0 with the Wilson term W = m + sum(1-cos p) at a small
    reference mass (its quoted '0.0845 at ma=0.02 on 64^4'), not in the strict
    massless limit.  This function reports the matched-convention comparison.
    """
    i0_massless = lattice_I0(n=128, m=0.0)
    i0_ref_inf = lattice_I0(n=128, m=m_ref)
    i0_ref_64 = lattice_I0_finite_volume(L=64, m=m_ref)
    return {
        "m_ref": m_ref,
        "I0_massless_inf_vol": i0_massless,
        "I0_ref_mass_inf_vol": i0_ref_inf,
        "I0_ref_mass_L64": i0_ref_64,
        "Gc_ref_mass_inf_vol": lattice_Gc(i0_ref_inf),
    }


def results_dict() -> dict:
    conv = lattice_convergence()
    # Best estimate: finest grid, average of straight and offset grids.
    nmax = max(conv)
    best_vals = list(conv[nmax].values())
    I0_lat = float(np.mean(best_vals))
    I0_spread = float(abs(best_vals[0] - best_vals[-1]))  # straight vs offset
    return {
        "relation": "G_c = 1/(2 I_0), I_0 = untraced scalar bubble",
        "continuum": {
            "I0": continuum_I0(1.0),
            "I0_exact": "Lambda^2/(16 pi^2)",
            "Gc": continuum_Gc(1.0),
            "Gc_exact": "8 pi^2 / Lambda^2",
            "c_in_c_pi2_over_Lambda2": continuum_c(),
        },
        "lattice_massless_chiral_point": {
            "integrand": "1/(sum_mu sin^2 p_mu + (sum_mu (1-cos p_mu))^2)",
            "convergence": {str(n): v for n, v in conv.items()},
            "I0": I0_lat,
            "I0_straight_vs_offset_spread": I0_spread,
            "Gc": lattice_Gc(I0_lat),
        },
        "lattice_reference_mass": reference_mass_evaluation(0.02),
    }


def main() -> None:
    res = results_dict()
    regen = Path(__file__).resolve().parents[1] / "results" / "P2-GAP-01" / "regen"
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "gap_criticality.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    c = res["continuum"]
    lat = res["lattice_massless_chiral_point"]
    ref = res["lattice_reference_mass"]
    print("Gate P2-GAP-01 — gap-equation criticality")
    print("=" * 56)
    print("Continuum (sharp 4-ball):")
    print(f"  I_0 = {c['I0']:.8f}  = {c['I0_exact']}")
    cval = c["c_in_c_pi2_over_Lambda2"]
    print(f"  G_c = {c['Gc']:.6f}  = {c['Gc_exact']}  (c = {cval:.6f})")
    print("Lattice (Wilson r=1), massless chiral point m=0:")
    for n, v in lat["convergence"].items():
        cells = "  ".join(f"{k}={val:.6f}" for k, val in v.items())
        print(f"  n={n:>3}: {cells}")
    print(f"  I_0 = {lat['I0']:.6f}  (straight vs offset spread "
          f"{lat['I0_straight_vs_offset_spread']:.2e})  G_c = {lat['Gc']:.6f}")
    print(f"Lattice at reference mass ma={ref['m_ref']} (paper's setup):")
    print(f"  I_0 (inf vol)  = {ref['I0_ref_mass_inf_vol']:.6f}  "
          f"G_c = {ref['Gc_ref_mass_inf_vol']:.6f}")
    print(f"  I_0 (64^4)     = {ref['I0_ref_mass_L64']:.6f}")


if __name__ == "__main__":
    main()
