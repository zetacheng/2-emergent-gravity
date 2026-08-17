"""Flat-limit regression anchor for the clean-room Proca operators.

`P2-BETAV-RECON-01`'s `Regression anchors` field reads `None yet (proposed)` in
`GATES.md`; this module is the first candidate anchor for it, and this task does
not modify the gate to register it.

Every assertion here is a statement about the constructed operators at ``h = 0``
or about the numerical-derivative machinery checked against an independently
known answer.  No assertion involves a determinant power, a determinant ratio,
or any target external to this construction.
"""

from __future__ import annotations

import numpy as np

from scripts.recon2026 import flat_validation as fv
from scripts.recon2026 import proca_curved as pc

EXTENT = 4
MASS_SQUARED = 0.25


def test_flat_one_form_spectrum_has_three_dispersing_bands_and_one_flat_band():
    """Three bands at ``phat2 + m^2`` and one exactly at ``m^2``, per momentum."""
    result = fv.validate_flat_vector_spectrum(EXTENT, MASS_SQUARED)
    assert result["relative_asymmetry"] < 1e-12
    assert result["max_abs_deviation"] < 1e-9
    assert result["flat_band_multiplicity"] == result["flat_band_multiplicity_required"]


def test_flat_one_form_longitudinal_band_is_momentum_independent():
    """The flat band does not disperse: it is ``m^2`` at every momentum."""
    geom = pc.LatticeGeometry(EXTENT)
    two_pi_over_l = 2.0 * np.pi / geom.extent
    for coord in geom.coords:
        momentum = two_pi_over_l * np.asarray(coord, dtype=float)
        eigenvalues = np.sort(
            np.linalg.eigvalsh(pc.flat_vector_block(momentum, MASS_SQUARED)).real
        )
        assert abs(eigenvalues[0] - MASS_SQUARED) < 1e-12
        expected = pc.phat2(momentum) + MASS_SQUARED
        for value in eigenvalues[1:]:
            assert abs(value - expected) < 1e-12


def test_position_space_determinant_matches_momentum_block_factorisation():
    """An independent global check that the construction factorises correctly."""
    result = fv.validate_flat_vector_spectrum(EXTENT, MASS_SQUARED)
    assert result["logdet_absolute_difference"] < 1e-8


def test_compensating_scalar_is_propagating_not_ultralocal():
    """``D0 + m^2`` must disperse as ``phat2 + m^2``, not sit at ``m^2``."""
    result = fv.validate_compensating_scalar(EXTENT, MASS_SQUARED)
    assert result["max_abs_deviation"] < 1e-9
    assert not result["is_ultralocal"]
    assert result["eigenvalue_spread"] > 1.0
    assert abs(result["min_eigenvalue"] - MASS_SQUARED) < 1e-9
    assert result["distinct_eigenvalue_count"] > 1


def test_transverse_longitudinal_mixing_vanishes_on_the_flat_background():
    """With ``h = 0`` the flat projectors must block-diagonalise the operator."""
    result = fv.measure_mixing(EXTENT, MASS_SQUARED, amplitudes=(0.0,))
    assert result["rows"][0]["amplitude"] == 0.0
    assert result["rows"][0]["relative_mixing"] < 1e-12


def test_gauge_kernel_of_the_field_strength_hessian_is_metric_independent():
    """``K1`` annihilates the flat longitudinal band on a CURVED background too.

    The field strength vanishes identically on ``A_mu = d_mu lambda`` because the
    forward differences commute, and that statement carries no metric.  The
    consequence, which choice C5 then inherits, is that ``D1 + m^2`` keeps an
    exactly flat, exactly unmixed longitudinal band at non-zero ``h`` -- while
    the Hessian of the action before dividing by the mass metric does NOT.
    """
    result = fv.measure_mixing(EXTENT, MASS_SQUARED, amplitudes=(0.0, 0.08))
    curved = result["rows"][-1]
    assert curved["amplitude"] == 0.08
    assert curved["hessian_times_longitudinal_projector_norm"] < 1e-10
    assert curved["relative_mixing"] < 1e-12
    assert curved["pre_division_relative_mixing"] > 1e-6


def test_mass_derivative_machinery_reproduces_the_closed_form():
    """``d/d(m^2) log det (D0 + m^2)`` against ``sum_p 1/(phat2 + m^2)``.

    The raw central difference is second order, so its tolerance is set by the
    step size rather than by machine precision; what is asserted is the ORDER of
    convergence -- the error must fall by a factor near four per halving -- and
    that one Richardson step buys several decades beyond it.
    """
    result = fv.validate_mass_derivative(EXTENT, 0.5)
    scale = abs(result["closed_form"])
    errors = [row["absolute_error"] for row in result["rows"]]
    assert errors[-1] / scale < 1e-5
    for coarse, fine in zip(errors, errors[1:]):
        assert 3.5 < coarse / fine < 4.5
    assert result["richardson_absolute_error"] is not None
    assert result["richardson_absolute_error"] / scale < 1e-7


def test_background_derivative_vanishes_at_zero_amplitude_by_symmetry():
    """The half-period translation makes ``log det`` even in the amplitude."""
    result = fv.validate_background_derivative(EXTENT, 0.5)
    assert result["symmetry_available"]
    scale = abs(result["baseline_logdet"])
    assert result["max_abs_first_derivative"] / scale < 1e-9
