"""Task ``P2-XI-LEDGER-01`` — the conditional analytic ξ ledger, Phase 1.

Assembles a CONDITIONAL ``xi(G)`` from the landed heat-kernel coefficients,
decomposed by curvature-coupling structure, and computes the decision margin
against the landed survival threshold.

**Every total this module produces is conditional on COND-1..4 of
``specs/2026-08-23T0600Z_xi-ledger-01_v3.md``.** The bare symbol ``xi(G)`` is
never used here for a number. Two ledger rows are OPEN and carry no value: the
condensate scalar's own fluctuation loop (Q-M2) and the Hubbard--Stratonovich
Jacobian/normalization term (Q-M3). This module neither estimates nor bounds
them, and assigning them zero is exactly what the OPEN status forbids.

Every constant below is taken from a landed line quoted in the derivation note
``derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md``; none is recalled
from memory and none is a target value.

Run bare from the repository root::

    python -m scripts.xi_ledger
"""

from __future__ import annotations

import sympy as sp

# ---------------------------------------------------------------------------
# Symbols and the landed heat-kernel prefactor
# ---------------------------------------------------------------------------
pi = sp.pi
xi_sym = sp.Symbol("xi", real=True)
L = sp.Symbol("L", positive=True)

#: ``K ≡ (4π)^{−2} = 1/(16π²)`` — P2-HK-01:81.
K = sp.Rational(1, 16) / pi**2

# ---------------------------------------------------------------------------
# §1a — the pre-registered evaluation grid, frozen in the specification
# ---------------------------------------------------------------------------
#: The specification's §1a range and representative points. M4 evaluates these
#: and no others; no point may be added, removed, or retuned at execution time.
L_RANGE = (sp.Rational(1, 2), sp.Integer(20))
L_POINTS = (
    sp.Rational(1, 2),
    sp.Integer(1),
    sp.Integer(2),
    sp.Integer(3),
    sp.Integer(5),
    sp.Integer(10),
    sp.Integer(20),
)

# ---------------------------------------------------------------------------
# The three curvature-coupling classes (M2)
# ---------------------------------------------------------------------------
# This module's operationalization of Ruling 2's axis, pre-registered by the
# specification's M2. The classes partition the landed ``a_1`` of
# CONVENTIONS.md:16, ``a_1 = tr[(1/6)R·𝟙 − E]``:
#
#   UNIVERSAL_R6  the ``(1/6)R·𝟙`` term — present for every bundle, weighted by
#                 the bundle dimension ``d_s``; carries no species coupling.
#   ENDOMORPHISM  the ``−E`` term where ``E`` is fixed by the species' own
#                 kinetic operator: Lichnerowicz ``(1/4)R·𝟙₄`` for Dirac
#                 (CONVENTIONS.md:18), ``R^{μ}{}_{ν}`` for the Proca vector
#                 part (CONVENTIONS.md:19).
#   EXPLICIT_XI_R the ``−E`` term where ``E = ξR`` comes from an action-level
#                 non-minimal coupling ``½ξRφ²`` (CONVENTIONS.md:17).
#
# ENDOMORPHISM and EXPLICIT_XI_R are both ``E`` contributions in the landed
# ``a_1``; what separates them is fixed by landed text, not chosen here — the
# first is implied by the species' kinetic operator, the second is a coupling
# written into the action.
UNIVERSAL_R6 = "universal R/6"
ENDOMORPHISM = "endomorphism (bundle)"
EXPLICIT_XI_R = "explicit xi*R"

CLASSES = (UNIVERSAL_R6, ENDOMORPHISM, EXPLICIT_XI_R)


class Factor:
    """One determinant factor of a species, as the landed table records it.

    ``dim``  bundle dimension ``d_s = tr 𝟙``               (P2-HK-01:62-68)
    ``p``    log-det prefactor ``p_s``                     (CONVENTIONS.md:21)
    ``e_endo``  ``tr E / R`` from the kinetic operator      (bundle-structural)
    ``e_xi``    ``tr E / R`` from an action-level ``ξR``    (non-minimal)
    """

    def __init__(self, name, dim, p, e_endo=sp.Integer(0), e_xi=sp.Integer(0)):
        self.name = name
        self.dim = sp.sympify(dim)
        self.p = sp.sympify(p)
        self.e_endo = sp.sympify(e_endo)
        self.e_xi = sp.sympify(e_xi)

    def per_class(self):
        """``β`` contributions of this factor, split by curvature-coupling class.

        From ``β_s = −p_s K (tr a_1/R)`` (CONVENTIONS.md:21) with
        ``tr a_1/R = d_s/6 − e_s`` (P2-HK-01:60), linearity in ``tr a_1/R``
        gives one term per class.
        """
        return {
            UNIVERSAL_R6: sp.simplify(-self.p * K * self.dim / 6),
            ENDOMORPHISM: sp.simplify(self.p * K * self.e_endo),
            EXPLICIT_XI_R: sp.simplify(self.p * K * self.e_xi),
        }


#: The landed species, one entry per determinant factor (P2-HK-01:62-68).
SPECIES = {
    "scalar_minimal": [Factor("real scalar", 1, sp.Rational(1, 2))],
    "scalar_nonminimal": [
        Factor("non-minimal scalar", 1, sp.Rational(1, 2), e_xi=xi_sym)
    ],
    "fermion_dirac": [
        Factor("Dirac fermion", 4, sp.Rational(-1, 2), e_endo=sp.Integer(1))
    ],
    "vector_proca": [
        Factor("Proca vector part", 4, sp.Rational(1, 2), e_endo=sp.Integer(1)),
        Factor("Stueckelberg scalar part", 1, sp.Rational(-1, 2)),
    ],
}


def species_per_class(key):
    """Per-class ``β`` contributions of a species, summed over its factors."""
    out = {c: sp.Integer(0) for c in CLASSES}
    for factor in SPECIES[key]:
        for c, v in factor.per_class().items():
            out[c] += v
    return {c: sp.simplify(v) for c, v in out.items()}


def species_total(key):
    """``β_s`` for a species, as the sum over its curvature-coupling classes."""
    return sp.simplify(sum(species_per_class(key).values()))


# ---------------------------------------------------------------------------
# M4 — the conditional total and the decision margin
# ---------------------------------------------------------------------------
#: The two landed conventions of ``4 G_c β_F`` — P2-NORM-01:57.
FOUR_G_BETA_F = {
    "Z_paper": sp.Rational(1, 6),
    "Z_here": sp.Rational(1, 3),
}

#: The landed survival threshold ``ξ_eff > 1/6`` — P2-NORM-01:83's window is the
#: consequence of this threshold; the threshold itself is CONVENTIONS.md:17's
#: conformal value, quoted in the derivation note.
THRESHOLD = sp.Rational(1, 6)


def xi_cond(convention):
    """``ξ(G) | COND-1..4`` as a function of ``L``, in one landed convention.

    The landed chain is ``ξ_ind = 4Gβ_F(3−L)`` — P2-NORM-01:26.
    """
    return FOUR_G_BETA_F[convention] * (3 - L)


def f0(convention):
    """``F0 ≡ |4Gβ_F|`` — §1a's frozen, L-independent margin normalization."""
    return sp.Abs(FOUR_G_BETA_F[convention])


def delta_xi_flip(convention, L_value):
    """``|δξ_flip(L)|`` — the size an added ledger term would need to cross 1/6.

    A property of the assembled function only. **It is not an estimate of the
    Q-M2 or Q-M3 terms**, whose magnitude and sign this task does not address.
    """
    return sp.Abs(THRESHOLD - xi_cond(convention).subs(L, L_value))


def r_margin(convention, L_value):
    """``r_margin(L) = |δξ_flip(L)| / F0`` under §1a's frozen normalization."""
    return sp.simplify(delta_xi_flip(convention, L_value) / f0(convention))


def survival_L_boundary(convention):
    """The ``L`` at which ``ξ(G) | COND-1..4`` meets the threshold, derived."""
    sol = sp.solve(sp.Eq(xi_cond(convention), THRESHOLD), L)
    assert len(sol) == 1, sol
    return sp.nsimplify(sol[0])


def survival_mass_boundary(convention):
    """The mass boundary in units of ``Λ``, derived from the ``L`` boundary.

    ``L ≡ ln(Λ²/m²)`` with ``m`` in units of ``Λ`` — CONVENTIONS.md:22 — so
    ``m = exp(−L/2)``.
    """
    return sp.exp(-survival_L_boundary(convention) / 2)


# ---------------------------------------------------------------------------
# The ledger (M3) — membership is a status, never a number
# ---------------------------------------------------------------------------
#: Rows whose membership is not LANDED carry no numeric value anywhere.
OPEN_ROWS = (
    {
        "row": "condensate scalar's own fluctuation loop",
        "membership": "OPEN(Q-M2)",
        "value": None,
    },
    {
        "row": "Hubbard-Stratonovich Jacobian / normalization term",
        "membership": "OPEN(Q-M3)",
        "value": None,
    },
)


def main():
    print("P2-XI-LEDGER-01 — conditional analytic xi ledger (Phase 1)")
    print("All totals are xi(G) | COND-1..4. Two ledger rows are OPEN and")
    print("carry no value; this module does not estimate or bound them.\n")

    print("M2 — per-species x per-class beta coefficients (units of K = 1/(16*pi**2))")
    for key in SPECIES:
        per = species_per_class(key)
        cells = "  ".join(
            f"{c}={sp.nsimplify(sp.simplify(v / K))}" for c, v in per.items()
        )
        print(f"  {key:20s} {cells}")
        tot = sp.nsimplify(sp.simplify(species_total(key) / K))
        print(f"  {'':20s} total = ({tot}) * K")
    print()

    print("M4 — conditional total and margin, per landed convention")
    for conv in FOUR_G_BETA_F:
        print(f"  {conv}: xi(G)|COND-1..4 = {xi_cond(conv)}   F0 = {f0(conv)}")
        print(
            f"    survival boundary  L = {survival_L_boundary(conv)}"
            f"   m/Lambda = {str(sp.N(survival_mass_boundary(conv), 6))}"
        )
        for Lv in L_POINTS:
            xc = str(sp.N(xi_cond(conv).subs(L, Lv), 8))
            dx = str(sp.N(delta_xi_flip(conv, Lv), 8))
            rm = str(sp.N(r_margin(conv, Lv), 8))
            print(
                f"    L={str(Lv):>4}  xi|COND = {xc:>13}"
                f"  |d_xi_flip| = {dx:>13}  r_margin = {rm:>13}"
            )
    print()

    print("M3 — OPEN rows (no numeric value, by construction)")
    for row in OPEN_ROWS:
        print(f"  {row['membership']:12s} {row['row']}  value={row['value']}")


if __name__ == "__main__":
    main()
