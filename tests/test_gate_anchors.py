"""Regression anchors for gates P2-HK-01, P2-GAP-01, P2-BETA-01.

These import and run the *real* gate functions (never re-typed constants) and
compare against **this repository's own** computed values. Each numeric anchor
is paired with a *mutation-detection* companion assertion: a perturbed value
must fall outside the tolerance used, proving the tolerance actually
discriminates. Slow, full-resolution recomputations are marked ``@pytest.mark.slow``.
"""

import math

import pytest
import sympy as sp

from scripts import betav_discriminating as bvd
from scripts import gap_criticality as gap
from scripts import hk_species as hk
from scripts import lattice_beta_scan as lbs
from scripts import normalization_chain as norm

PI = sp.pi


# ===========================================================================
# P2-HK-01 — heat-kernel species coefficients (symbolic, fast)
# ===========================================================================
def test_hk_beta_values_exact():
    assert sp.simplify(hk.beta("scalar_min") - (-1 / (192 * PI**2))) == 0
    assert sp.simplify(hk.beta("dirac") - (-1 / (96 * PI**2))) == 0
    assert sp.simplify(hk.beta("proca") - (1 / (64 * PI**2))) == 0


def test_hk_ratios_exact():
    r = hk.ratios()
    assert sp.simplify(r["beta_F/beta_B"] - 2) == 0
    assert sp.simplify(r["beta_V/beta_B"] - (-3)) == 0
    xi = sp.Symbol("xi", real=True)
    assert sp.simplify(r["beta_B(xi)/beta_B"] - (1 - 6 * xi)) == 0


def test_hk_proper_time_second_route():
    assert sp.simplify(hk.proper_time_log_coefficient() - 1) == 0


def test_hk_mutation_dirac_is_not_weyl():
    # Mutation-detection companion: the Dirac anchor must DISCRIMINATE the
    # 4-component Dirac value 1/(96 pi^2) from the 2-component (Weyl / paper)
    # value 1/(192 pi^2). If they were equal the anchor would be worthless.
    assert sp.simplify(hk.beta("dirac") - (-1 / (192 * PI**2))) != 0
    assert sp.simplify(hk.ratios()["beta_F/beta_B"] - 1) != 0


# ===========================================================================
# P2-GAP-01 — gap-equation criticality
# ===========================================================================
def test_gap_continuum_exact():
    assert gap.continuum_c() == pytest.approx(8.0, abs=1e-12)
    assert gap.continuum_I0(1.0) == pytest.approx(1.0 / (16 * math.pi**2), rel=1e-12)
    assert gap.continuum_Gc(1.0) == pytest.approx(8 * math.pi**2, rel=1e-12)


def test_gap_continuum_mutation():
    # Companion: the exact continuum c is 8, not 7 or 9; tolerance 1e-6 excludes
    # any neighbouring integer.
    assert abs(gap.continuum_c() - 7.0) > 1e-6
    assert abs(gap.continuum_c() - 9.0) > 1e-6


LATTICE_I0_CONVERGED = 0.085388  # this repo's converged value (n=128)
LATTICE_I0_TOL = 1.0e-4          # covers n=48 grid drift (~3e-5) with margin


def test_gap_lattice_I0_fast():
    # Real integral at a modest grid; must land near the converged value.
    i0 = gap.lattice_I0(n=48, shift=0.0)
    assert i0 == pytest.approx(LATTICE_I0_CONVERGED, abs=LATTICE_I0_TOL)


def test_gap_lattice_mutation_excludes_paper_value():
    # Companion: the tolerance discriminates our value from the paper's 0.0844
    # (the recorded ~1.2% disagreement, |0.0854-0.0844| ~ 1e-3 >> tol).
    i0 = gap.lattice_I0(n=48, shift=0.0)
    assert abs(i0 - 0.0844) > LATTICE_I0_TOL


@pytest.mark.slow
def test_gap_lattice_I0_high_resolution():
    i0 = gap.lattice_I0(n=128, shift=0.0)
    assert i0 == pytest.approx(LATTICE_I0_CONVERGED, abs=5e-5)
    # straight vs offset grid agreement (discretization bound)
    i0_off = gap.lattice_I0(n=128, shift=0.25)
    assert abs(i0 - i0_off) < 1e-4


# ===========================================================================
# P2-BETA-01 — lattice mass-scan beta_B
# ===========================================================================
def test_fit_beta_recovers_known_coefficient():
    # Unit test of the real fitter against a *synthetic* known beta (not a
    # paper constant): Z = 1 + 2 m^2 + B m^2 ln m^2 + 0.5 m^4, B known.
    import numpy as np

    masses = np.linspace(0.125, 0.55, 18)
    m2 = masses**2
    B = 7.3e-4
    Z = 1.0 + 2.0 * m2 + B * m2 * np.log(m2) + 0.5 * m2**2
    beta, _, rms = lbs.fit_beta(masses, Z, with_m4=True)
    assert beta == pytest.approx(B, rel=1e-6)
    assert rms < 1e-12
    # Companion: a wrong target is rejected by the same tolerance.
    assert abs(beta - 2 * B) > 1e-6 * B


BETA_B_BAND = (4.5e-4, 6.5e-4)  # from this repo's own scan systematics


def test_beta_scan_reduced_fast():
    import numpy as np

    masses = np.linspace(0.15, 0.5, 6)
    Z = np.array([lbs.PREFACTOR * lbs.phi2_integral(m * m, n=48) for m in masses])
    beta, _, _ = lbs.fit_beta(masses, Z, with_m4=True)
    assert BETA_B_BAND[0] < beta < BETA_B_BAND[1]


def test_beta_scan_mutation_band_is_discriminating():
    # Companion: the acceptance band excludes grossly wrong values.
    assert not (BETA_B_BAND[0] < 2.0e-3 < BETA_B_BAND[1])
    assert not (BETA_B_BAND[0] < 1.0e-4 < BETA_B_BAND[1])


@pytest.mark.slow
def test_beta_scan_full_systematics():
    res = lbs.run_systematics()
    assert 5.0e-4 < res["beta_central"] < 6.0e-4
    assert res["beta_primary_spread"] < 1.0e-4
    # volume trend converges toward the infinite-volume value
    vt = res["volume_trend"]
    assert abs(vt["L48"] - vt["Linf"]) < abs(vt["L24"] - vt["Linf"])


# ===========================================================================
# P2-GAP-01 — I_0 resolution at the paper's reference mass
# ===========================================================================
def test_gap_I0_reference_mass_matches_paper():
    # At ma=0.02 the untraced bubble drops to ~0.0843 (paper 0.0844), resolving
    # the first report's D2. Massless value (~0.0854) is a different definition.
    i0_ref = gap.lattice_I0(n=96, m=0.02)
    i0_massless = gap.lattice_I0(n=96, m=0.0)
    assert i0_ref == pytest.approx(0.08434, abs=2e-4)
    # Companion: the reference-mass value is genuinely BELOW the massless one
    # (the effect that resolves D2), by clearly more than numerical scatter.
    assert i0_massless - i0_ref > 5e-4


# ===========================================================================
# P2-NORM-01 — uniform factor 2 in Z
# ===========================================================================
def test_norm_factor_two_is_uniform():
    res = norm.results_dict()
    for s, d in res["species_betas"].items():
        assert d["ratio_here_over_paper"] == pytest.approx(2.0, abs=1e-9), s


def test_norm_four_Gc_betaF_conventions():
    assert norm.four_Gc_betaF("paper") == pytest.approx(1.0 / 6.0, rel=1e-9)
    assert norm.four_Gc_betaF("here") == pytest.approx(1.0 / 3.0, rel=1e-9)
    # Companion: the two conventions are genuinely a factor 2 apart, not equal.
    assert abs(norm.four_Gc_betaF("here") - norm.four_Gc_betaF("paper")) > 0.1


# ===========================================================================
# P2-BETAV-CIRC-01 — discriminating power (structure-dependent target)
# ===========================================================================
def test_betav_ratio_is_structure_dependent():
    assert float(bvd.ratio_V_over_B(1)) == pytest.approx(-3.0, abs=1e-9)
    assert float(bvd.ratio_V_over_B(2)) == pytest.approx(-4.0, abs=1e-9)
    assert float(bvd.ratio_V_over_B(3)) == pytest.approx(-5.0, abs=1e-9)


def test_betav_mutation_not_degenerate():
    # Mutation-detection companion: if the target were "-3 regardless" the test
    # would be circular. It is not: k=1 and k=2 give different ratios.
    assert float(bvd.ratio_V_over_B(1)) != float(bvd.ratio_V_over_B(2))
