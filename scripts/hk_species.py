"""Gate ``P2-HK-01`` — heat-kernel species coefficients from first principles.

Computes, symbolically, the coefficient ``beta_s`` of the ``m**2 * ln(m**2)``
term in the induced Einstein--Hilbert kinetic coefficient ``Z(m**2)`` for each
matter species, from the Seeley--DeWitt expansion, together with the
convention-independent ratios ``beta_F/beta_B``, ``beta_V/beta_B``,
``beta_B(xi)/beta_B``.

Conventions are locked in ``CONVENTIONS.md`` and the derivation note
``derivations/P2-HK-01_heat_kernel_species.md``. This module contains no paper
value and is not tuned toward one.

Run bare from the repository root::

    python -m scripts.hk_species
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------
pi = sp.pi
xi = sp.Symbol("xi", real=True)

#: (4*pi)**-2 = 1/(16*pi**2), the heat-kernel prefactor K.
K = sp.Rational(1, 16) / pi**2


# ---------------------------------------------------------------------------
# Heat-kernel data per determinant factor
# ---------------------------------------------------------------------------
# Each species is a list of determinant factors. For a factor:
#   dim        : bundle dimension tr(1)
#   e_over_R   : tr(E)/R  (E is the endomorphism in Delta = -grad^2 + E)
#   p          : log-det prefactor (+1/2 per det^{-1/2}, -1/2 per det^{+1/2}
#                or a fermion loop)
# a_1 recipe:  tr a_1 / R = dim/6 - e_over_R.
# beta_s     = sum over factors of  -p * K * (tr a_1 / R).


def _tr_a1_over_R(dim, e_over_R):
    """tr(a_1)/R for one determinant factor: dim/6 - tr(E)/R."""
    return sp.Rational(dim, 6) - e_over_R


def species_factors():
    """Return the determinant-factor data for each species.

    Values that are exact rationals are given as :class:`sympy.Rational`; the
    non-minimal scalar uses the symbol ``xi``.
    """
    return {
        "scalar_min": [dict(dim=1, e_over_R=sp.Integer(0), p=sp.Rational(1, 2))],
        "scalar_xi": [dict(dim=1, e_over_R=xi, p=sp.Rational(1, 2))],
        # Dirac: E = (1/4) R * 1_4  => tr(E)/R = 4*(1/4) = 1 ; fermion loop p=-1/2
        "dirac": [dict(dim=4, e_over_R=sp.Integer(1), p=sp.Rational(-1, 2))],
        # Proca: det^{-1/2}(vector) * det^{+1/2}(scalar)
        # vector 1-form Laplacian: E^mu_nu = R^mu_nu => tr(E)/R = 1, p=+1/2
        # Stueckelberg scalar: E=0, det^{+1/2} => p=-1/2
        "proca": [
            dict(dim=4, e_over_R=sp.Integer(1), p=sp.Rational(1, 2)),
            dict(dim=1, e_over_R=sp.Integer(0), p=sp.Rational(-1, 2)),
        ],
    }


def tr_a1_over_R(species):
    """Total tr(a_1)/R summed over a species' determinant factors."""
    factors = species_factors()[species]
    return sp.simplify(sum(_tr_a1_over_R(f["dim"], f["e_over_R"]) for f in factors))


def beta(species):
    """Species coefficient beta_s of m^2 ln m^2 in Z(m^2), exact (in pi)."""
    factors = species_factors()[species]
    total = sp.Integer(0)
    for f in factors:
        total += -f["p"] * K * _tr_a1_over_R(f["dim"], f["e_over_R"])
    return sp.simplify(total)


def ratios():
    """Convention-independent ratios of species coefficients."""
    bB = beta("scalar_min")
    return {
        "beta_F/beta_B": sp.nsimplify(sp.simplify(beta("dirac") / bB)),
        "beta_V/beta_B": sp.nsimplify(sp.simplify(beta("proca") / bB)),
        "beta_B(xi)/beta_B": sp.simplify(beta("scalar_xi") / bB),
    }


# ---------------------------------------------------------------------------
# Route 2: proper-time / incomplete-gamma extraction of the m^2 ln m^2 piece
# ---------------------------------------------------------------------------
def proper_time_log_coefficient():
    """Independent second route.

    Evaluate the proper-time integral with UV cutoff tau > 1/Lambda^2,

        int_{1/Lambda^2}^infty dtau tau^{-2} e^{-tau m^2}
            = m^2 * Gamma(-1, m^2/Lambda^2),

    and return the coefficient of ``m^2 ln(m^2)`` in its small-mass expansion.
    Must equal +1, confirming Z ⊃ beta_s m^2 ln m^2 with
    beta_s = -p_s (4pi)^{-2} (tr a_1 / R), independently of the a_1 route.
    """
    m2, Lam2 = sp.symbols("m2 Lambda2", positive=True)
    x = m2 / Lam2
    # Gamma(-1, x) small-x expansion: 1/x + ln x + (gamma-1) + O(x)
    integral = m2 * sp.uppergamma(-1, x)
    ser = sp.series(integral, m2, 0, 2).removeO()
    # coefficient of m2*log(m2): expand log(m2/Lambda2) = log(m2)-log(Lambda2)
    ser = sp.expand(ser.rewrite(sp.log))
    coeff = ser.coeff(m2, 1).coeff(sp.log(m2), 1)
    return sp.simplify(coeff)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def _as_rational_over_pi2(expr):
    """Express ``expr`` as c/pi**2 and return the exact rational c (or None)."""
    c = sp.simplify(expr * pi**2)
    if c.free_symbols:
        return None
    r = sp.nsimplify(c, rational=True)
    return Fraction(int(sp.fraction(r)[0]), int(sp.fraction(r)[1]))


def results_dict():
    out = {"convention": "beta_s = -p_s (4pi)^-2 (tr a_1 / R); K = 1/(16 pi^2)"}
    betas = {}
    for name in ("scalar_min", "scalar_xi", "dirac", "proca"):
        b = beta(name)
        rat = _as_rational_over_pi2(b)
        betas[name] = {
            "tr_a1_over_R": str(tr_a1_over_R(name)),
            "beta_exact": sp.sstr(b),
            "beta_as_c_over_pi2": (str(rat) if rat is not None else None),
            "beta_float": (float(b) if not b.free_symbols else None),
        }
    out["beta"] = betas
    out["ratios"] = {k: sp.sstr(v) for k, v in ratios().items()}
    out["proper_time_log_coefficient"] = sp.sstr(proper_time_log_coefficient())
    return out


def main():
    res = results_dict()
    regen = Path(__file__).resolve().parents[1] / "results" / "P2-HK-01" / "regen"
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "hk_species.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    print("Gate P2-HK-01 — heat-kernel species coefficients")
    print("=" * 56)
    for name, d in res["beta"].items():
        c = d["beta_as_c_over_pi2"]
        tag = f"({c})/pi^2" if c else d["beta_exact"]
        print(f"  {name:12s}: tr a_1/R = {d['tr_a1_over_R']:>8s}   beta = {tag}")
    print("-" * 56)
    for k, v in res["ratios"].items():
        print(f"  {k:20s} = {v}")
    print("-" * 56)
    print(f"  proper-time m^2 ln m^2 coefficient (route 2) = "
          f"{res['proper_time_log_coefficient']}")


if __name__ == "__main__":
    main()
