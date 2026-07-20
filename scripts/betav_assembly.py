"""Gate ``P2-BETAV-ASSEMBLY-01`` -- determinant-bookkeeping regression.

**This is NOT the circularity test of P2-BETAV-CIRC-01.** The historical
Finding 5 lattice Proca pipeline is not present in this repository (see
``results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md``), so its projection /
normalization cannot be exercised. This gate answers a *narrower,
implementation-only* question:

    Given the SHARED scalar lattice tadpole integral and the Proca determinant
    powers, does the assembly code preserve the k-dependence correctly (no
    hardcoded -3)?

Construction. The induced log coefficient of any mode is
``beta = -p * (tr a_1 / R) * C``, where ``C`` is the m^2 ln m^2 coefficient of
the ONE shared lattice tadpole ``<phi^2>_lat = int 1/(phat^2 + m^2)`` (the
P2-BETA-01 scalar integral). For the generalized Proca structure
``det^{-1/2}(Delta^(1)) . det^{+1/2}(Delta^(0))^k``:

    beta_B      = -(+1/2)(1/6) C          = -C/12
    beta_V(k)   = -(+1/2)(-1/3) C  +  -(-(k/2))(1/6) C  = C(2+k)/12
    R_k = beta_V(k)/beta_B = -(k+2).

Because numerator and denominator are the SAME integral C times different
rational prefactors, **C cancels exactly**: R_k is independent of the grid, so
the ratio's variant spread is ~machine zero (numerator and denominator are
fully correlated -- do NOT divide two independent beta scatters). This exact
cancellation is *precisely why this construction has no power to test the
historical projection*: it can only replay the bookkeeping. It DOES verify the
code reads ``k`` and does not hardcode -3.

Mutation anchor (on the scalar determinant power, the analogue of a projection
that freezes the compensating sector at the Proca value): freezing the scalar
power to 1 collapses R_k -> -3 for every k. That the anchor then fails proves
only that the code reads ``k`` -- NOT that any real pipeline is non-circular.

Run bare::

    python -m scripts.betav_assembly
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .lattice_beta_scan import fit_beta, phi2_integral

# Seeley-DeWitt per-factor data (from P2-HK-01), as exact rationals-in-float.
_VEC = (0.5, -1.0 / 3.0)       # (p, tr a_1 / R) : vector 1-form
_SCALAR = (0.5, 1.0 / 6.0)     # (p, tr a_1 / R) : one compensating scalar unit


def tadpole_log_coeff(n: int = 64, shift: float = 0.5,
                      lo: float = 0.125, hi: float = 0.55, npts: int = 14) -> float:
    """C = the m^2 ln m^2 coefficient of the SHARED scalar lattice tadpole.

    This is the single lattice integral both beta_B and beta_V are built from.
    """
    masses = np.linspace(lo, hi, npts)
    phi2 = np.array([phi2_integral(m * m, n=n, shift=shift) for m in masses])
    # fit_beta returns beta = coeff of m^2 ln m^2 in the supplied observable
    beta, _, _ = fit_beta(masses, phi2, with_m4=True)
    return float(beta)


def beta_B(C: float) -> float:
    """Reference scalar (minimal) coefficient assembled from the shared C."""
    p, tra1 = _SCALAR
    return -p * tra1 * C  # = -C/12


def beta_V(C: float, k: float, freeze_scalar_power: bool = False) -> float:
    """Proca-structure coefficient for det^{-1/2}(Delta^1).det^{+1/2}(Delta^0)^k.

    ``freeze_scalar_power=True`` is the MUTATION: it hardcodes the scalar power
    to 1 (the Proca value), collapsing every k to -3.
    """
    pv, trv = _VEC
    ps, trs = _SCALAR
    kk = 1.0 if freeze_scalar_power else k
    vec = -pv * trv * C            # +C/6
    scal = -(-(kk) * ps) * trs * C  # +kk*C/12  (scalar^k -> p = -k/2)
    return vec + scal


def ratio(C: float, k: float, freeze_scalar_power: bool = False) -> float:
    return beta_V(C, k, freeze_scalar_power) / beta_B(C)


K_GRID = (0.0, 1.0, 2.0, 3.0, 0.5)


def results_dict() -> dict:
    # Several grid/window variants; C differs per variant, R_k must not.
    variants = [
        dict(n=48, shift=0.5, lo=0.125, hi=0.55, npts=14),
        dict(n=64, shift=0.5, lo=0.125, hi=0.55, npts=14),
        dict(n=64, shift=0.25, lo=0.15, hi=0.50, npts=12),
    ]
    Cs = [tadpole_log_coeff(**v) for v in variants]

    per_k = {}
    for k in K_GRID:
        rs = [ratio(C, k) for C in Cs]  # R_k per variant (SAME grid num & den)
        per_k[str(k)] = {
            "R_k_mean": float(np.mean(rs)),
            "R_k_ratio_variant_spread": float(max(rs) - min(rs)),
            "target_minus_k_plus_2": -(k + 2.0),
        }
    # Mutation: freeze scalar power to 1 -> collapse to -3 for every k
    mutated = {str(k): ratio(Cs[1], k, freeze_scalar_power=True) for k in K_GRID}

    return {
        "gate": "P2-BETAV-ASSEMBLY-01",
        "does_not_close": "P2-BETAV-CIRC-01",
        "shared_tadpole_C_per_variant": Cs,
        "beta_B_per_variant": [beta_B(C) for C in Cs],
        "per_k": per_k,
        "mutation_freeze_scalar_power_1": mutated,
        "note": ("R_k = -(k+2) with ~machine-zero ratio spread because the "
                 "shared integral C cancels (fully correlated num/den). This is "
                 "bookkeeping realized on the lattice integral; it verifies the "
                 "code reads k and does not hardcode -3. It does NOT test the "
                 "historical Finding 5 projection and does NOT close "
                 "P2-BETAV-CIRC-01."),
    }


def main() -> None:
    res = results_dict()
    regen = (Path(__file__).resolve().parents[1] / "results"
             / "P2-BETAV-ASSEMBLY-01" / "regen")
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "betav_assembly.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print("Gate P2-BETAV-ASSEMBLY-01 -- determinant bookkeeping regression")
    print("=" * 62)
    print("  (does NOT close P2-BETAV-CIRC-01; historical pipeline absent)")
    print(f"  shared tadpole C per variant: "
          f"{[round(c, 6) for c in res['shared_tadpole_C_per_variant']]}")
    print("  k-scan (R_k realized on the shared lattice integral):")
    for k, d in res["per_k"].items():
        print(f"    k={k:>3}: R_k = {d['R_k_mean']:+.6f}  "
              f"(ratio variant spread {d['R_k_ratio_variant_spread']:.2e}; "
              f"target {d['target_minus_k_plus_2']:+.1f})")
    print("  MUTATION (freeze scalar power=1) -> collapses to -3 for all k:")
    for k, r in res["mutation_freeze_scalar_power_1"].items():
        print(f"    k={k:>3}: R = {r:+.4f}")
    print("  C cancels in the ratio -> spread ~ machine zero -> this "
          "construction\n  cannot test the historical projection.")


if __name__ == "__main__":
    main()
