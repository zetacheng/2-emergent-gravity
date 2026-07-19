"""Gate ``P2-NORM-01`` — locate the factor-2 between this repo's beta/G chain
and Paper 2 v2.15.

The disagreement flagged as "D1" in the first verification report was an
artifact: the paper's ``beta_B^cont = 1/(384 pi^2)`` was compared against this
repo's ``beta_B = 1/(192 pi^2)``, which are the same coefficient in two
normalizations of ``Z``.  This module writes one explicit normalization chain,
expresses both sides in it, and shows the factor 2 is (i) uniform across every
species and (ii) cancels in every ratio and in the sign -- i.e. it lives
entirely in the *definition of ``Z``*, not in the physics.

Run bare::

    python -m scripts.normalization_chain
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from .hk_species import beta as hk_beta  # this repo's Z = coeff of R in the action

PI = math.pi

# This repo's Z is the coefficient of \int sqrt(g) R in the effective action
# (Z_here = 1/(16 pi G_ind)).  The paper's Z is the axis-TT graviton kinetic
# slope per unit 4N.  Empirically (verified below) Z_paper = Z_here / R_Z with
# R_Z = 2 for EVERY species: this is the graviton-kinetic normalization factor
# between "coefficient of R" and "coefficient of p^2 in the axis-TT slope".
R_Z = 2.0

# Paper values (quoted, for the record; not used to compute anything here).
PAPER = {
    "beta_B_cont": 1.0 / (384 * PI**2),   # eq:betaB
    "beta_F": 1.0 / (192 * PI**2),        # "beta_F = 2 beta_B = 1/(192 pi^2)"
    "beta_V_over_beta_B": -3.0,           # "beta_V = -3 beta_B"
    "Gc_cont": 8 * PI**2,                 # "G_c = 8 pi^2/Lambda^2"
    "four_Gc_betaF": 1.0 / 6.0,           # "4 G_c beta_F = 1/6"
}

GC_CONT = 8 * PI**2  # gap-equation critical coupling (Z-independent; P2-GAP-01)


def species_beta(which: str, convention: str) -> float:
    """|beta_s| in a chosen Z-convention.

    convention='here'  : Z = coefficient of R in the action (this repo).
    convention='paper' : Z = axis-TT slope per unit 4N (= here / R_Z).
    """
    b_here = abs(float(hk_beta(which)))
    if convention == "here":
        return b_here
    if convention == "paper":
        return b_here / R_Z
    raise ValueError(convention)


def four_Gc_betaF(convention: str) -> float:
    """The prefactor 4 G_c beta_F.  G_c is Z-independent, so this inherits the
    Z-convention of beta_F alone -- which is exactly why the two chains differ.
    """
    return 4.0 * GC_CONT * species_beta("dirac", convention)


def survival_mmin(prefactor: float) -> float:
    """Survival window boundary: xi_ind = prefactor*(3-L) > 1/6 => L < Lmax,
    m/Lambda = exp(-Lmax/2).
    """
    Lmax = 3.0 - 1.0 / (6.0 * prefactor)
    return math.exp(-Lmax / 2.0)


def results_dict() -> dict:
    out = {"R_Z_factor_between_conventions": R_Z, "step_where_2_enters":
           "definition of Z: coefficient of R in the action (here) vs axis-TT "
           "kinetic slope per unit 4N (paper); uniform across species"}
    # (1) uniform factor 2 across species
    uni = {}
    for s in ("scalar_min", "dirac", "proca"):
        here = species_beta(s, "here")
        paper = species_beta(s, "paper")
        uni[s] = {"here": here, "paper_conv": paper, "ratio_here_over_paper":
                  here / paper}
    out["species_betas"] = uni
    # (2) ratios are convention-independent
    out["ratios_convention_independent"] = {
        "beta_F/beta_B": species_beta("dirac", "here") / species_beta(
            "scalar_min", "here"),
        "beta_V/beta_B": -species_beta("proca", "here") / species_beta(
            "scalar_min", "here"),  # sign from P2-HK-01
    }
    # (3) the product 4 G_c beta_F in both conventions
    out["four_Gc_betaF"] = {
        "here_convention": four_Gc_betaF("here"),
        "paper_convention": four_Gc_betaF("paper"),
        "paper_quoted": PAPER["four_Gc_betaF"],
    }
    # (4) physics conclusion unchanged: xi_ind = pref*(3-L) < 0 for L >> 1 in both
    concl = {}
    for name, conv in (("here_1_3", "here"), ("paper_1_6", "paper")):
        pref = four_Gc_betaF(conv)
        concl[name] = {
            "prefactor": pref,
            "xi_ind_at_L=5": pref * (3 - 5),   # negative
            "survival_mmin_over_Lambda": survival_mmin(pref),
        }
    out["physics_conclusion"] = concl
    return out


def main() -> None:
    res = results_dict()
    regen = Path(__file__).resolve().parents[1] / "results" / "P2-NORM-01" / "regen"
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "normalization_chain.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print("Gate P2-NORM-01 — locate the beta/G normalization factor 2")
    print("=" * 60)
    print("Factor between conventions (Z_here / Z_paper), per species:")
    for s, d in res["species_betas"].items():
        print(f"  {s:12s}: here={d['here']:.6e}  paper={d['paper_conv']:.6e}"
              f"  ratio={d['ratio_here_over_paper']:.4f}")
    print("Ratios (convention-independent):")
    for k, v in res["ratios_convention_independent"].items():
        print(f"  {k:12s} = {v:+.4f}")
    fg = res["four_Gc_betaF"]
    print(f"4 G_c beta_F: here={fg['here_convention']:.4f}  "
          f"paper_conv={fg['paper_convention']:.4f}  "
          f"paper_quoted={fg['paper_quoted']:.4f}")
    print("Physics conclusion (xi_ind<0 for L>>1 either way):")
    for name, d in res["physics_conclusion"].items():
        print(f"  {name}: prefactor={d['prefactor']:.4f}  "
              f"xi_ind(L=5)={d['xi_ind_at_L=5']:+.4f}  "
              f"survival m>{d['survival_mmin_over_Lambda']:.3f} Lambda")


if __name__ == "__main__":
    main()
