"""Validation driver for the clean-room metric-coupled Proca operators.

Runs the five validations this stage owes, none of which involves any final
ratio target:

  (a) the flat 1-form spectrum, against the analytically required structure;
  (b) transverse/longitudinal separation off the flat point, measured on this
      construction alone;
  (c) the compensating scalar's spectrum, propagating and not ultralocal;
  (d) behaviour under lattice refinement and enlargement, over two extents and
      two masses;
  (e) the numerical derivative machinery, validated against two independent
      known answers -- a closed-form mass derivative and a symmetry-enforced
      vanishing background derivative -- with Richardson extrapolation.

Nothing here computes a determinant ratio, varies a determinant power, or
compares any quantity against an external target.  Run as::

    python -m scripts.recon2026.flat_validation
"""

from __future__ import annotations

import numpy as np

from scripts.recon2026.proca_curved import (
    DIM,
    LatticeGeometry,
    cosine_weak_field,
    flat_metric,
    flat_scalar_eigenvalues,
    flat_vector_block,
    logdet_operator,
    longitudinal_projector_flat,
    phat2,
    scalar_operator,
    vector_operator,
)

# The weak-field background used throughout (C6 of proca_curved).  The
# wavevector's half period, L / (2 * q_0), is an integer for every extent used
# below, which validation (e2) relies on.
BACKGROUND_PATTERN = np.array(
    [
        [1.0, 0.3, 0.0, 0.0],
        [0.3, -1.0, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.2],
        [0.0, 0.0, 0.2, -0.5],
    ],
    dtype=float,
)
BACKGROUND_WAVEVECTOR = np.array([1, 0, 0, 0], dtype=float)


# ----------------------------------------------------------------------------
# (a) the flat 1-form spectrum
# ----------------------------------------------------------------------------


def analytic_flat_vector_spectrum(geom: LatticeGeometry, mass_squared):
    """The required flat spectrum: three transverse bands and one flat band.

    Per momentum ``p``: ``phat2(p) + m^2`` with multiplicity three, and ``m^2``
    with multiplicity one.  At ``p == 0`` the transverse bands degenerate onto
    ``m^2`` as well, so the total multiplicity of ``m^2`` is ``nsite + 3``, not
    ``nsite``.
    """
    two_pi_over_l = 2.0 * np.pi / geom.extent
    out = []
    for c in geom.coords:
        p = two_pi_over_l * np.asarray(c, dtype=float)
        out.extend([phat2(p) + float(mass_squared)] * 3)
        out.append(float(mass_squared))
    return np.sort(np.array(out, dtype=float))


def validate_flat_vector_spectrum(extent=4, mass_squared=0.25):
    """Compare the constructed flat spectrum against the required structure.

    At ``h = 0`` the operator is exactly symmetric, which is measured rather
    than assumed, so ``eigvalsh`` is used.  A second, independent check compares
    ``log det`` of the whole position-space operator against the sum of
    ``log det`` over the analytic momentum-space blocks: the two agree only if
    the position-space construction factorises as the momentum-space kernel
    says it must.
    """
    geom = LatticeGeometry(extent)
    operator = vector_operator(geom, flat_metric(geom), mass_squared)
    asymmetry = float(
        np.linalg.norm(operator - operator.T) / np.linalg.norm(operator)
    )
    numeric = np.sort(np.linalg.eigvalsh(0.5 * (operator + operator.T)))
    required = analytic_flat_vector_spectrum(geom, mass_squared)
    flat_band = int(np.sum(np.abs(numeric - float(mass_squared)) < 1e-10))

    two_pi_over_l = 2.0 * np.pi / geom.extent
    block_logdet = 0.0
    for c in geom.coords:
        p = two_pi_over_l * np.asarray(c, dtype=float)
        _, value = np.linalg.slogdet(flat_vector_block(p, mass_squared))
        block_logdet += float(value)
    full_logdet = logdet_operator(operator)

    per_mode = []
    for c in geom.coords[:: max(1, geom.nsite // 8)]:
        p = two_pi_over_l * np.asarray(c, dtype=float)
        block_ev = np.sort(np.linalg.eigvalsh(flat_vector_block(p, mass_squared)).real)
        per_mode.append(
            {
                "coord": tuple(int(v) for v in c),
                "phat2": phat2(p),
                "eigenvalues": block_ev.tolist(),
            }
        )
    return {
        "extent": extent,
        "mass_squared": mass_squared,
        "relative_asymmetry": asymmetry,
        "max_abs_deviation": float(np.max(np.abs(numeric - required))),
        "flat_band_multiplicity": flat_band,
        "flat_band_multiplicity_required": geom.nsite + 3,
        "logdet_full_operator": full_logdet,
        "logdet_momentum_blocks": block_logdet,
        "logdet_absolute_difference": float(abs(full_logdet - block_logdet)),
        "sampled_momentum_blocks": per_mode,
    }


# ----------------------------------------------------------------------------
# (b) transverse / longitudinal separation
# ----------------------------------------------------------------------------


def _momentum_basis(geom: LatticeGeometry):
    """Unitary taking the position-space 1-form to a momentum-space 1-form."""
    n = geom.nsite
    two_pi_over_l = 2.0 * np.pi / geom.extent
    phases = np.exp(-1j * two_pi_over_l * (geom.coords @ geom.coords.T))
    dft = phases / np.sqrt(n)
    return np.kron(dft, np.eye(DIM))


def _flat_longitudinal_projector(geom: LatticeGeometry):
    """Block-diagonal flat longitudinal projector in the momentum basis."""
    dof = geom.nsite * DIM
    proj = np.zeros((dof, dof), dtype=complex)
    two_pi_over_l = 2.0 * np.pi / geom.extent
    for i, c in enumerate(geom.coords):
        p = two_pi_over_l * np.asarray(c, dtype=float)
        proj[i * DIM : (i + 1) * DIM, i * DIM : (i + 1) * DIM] = (
            longitudinal_projector_flat(p)
        )
    return proj


def measure_mixing(extent=4, mass_squared=0.25, amplitudes=(0.0, 0.02, 0.04, 0.08)):
    """Relative size of the block that mixes the flat transverse and longitudinal bands.

    The projectors are the FLAT ones; the background is the curved one.  Two
    forms are measured at each amplitude, because they do not agree:

    ``operator``      ``D1 + m^2 = G1^{-1} K1 + m^2`` -- the operator as
                      constructed under choice C5, in which the mass term is
                      exactly ``m^2`` times the identity;
    ``pre_division``  ``K1 + m^2 G1`` -- the Hessian of the action itself,
                      before dividing by the mass metric.

    The reported quantity in each case is ``||Pi_T X Pi_L||_F / ||X||_F``.  The
    gauge kernel of ``K1`` is metric-independent, because the field strength
    vanishes identically on ``A_mu = d_mu lambda`` whenever the forward
    differences commute -- so the first form has no mixing at all and the second
    does.  Both numbers are reported; neither is compared to anything external.
    """
    geom = LatticeGeometry(extent)
    unitary = _momentum_basis(geom)
    proj_l = _flat_longitudinal_projector(geom)
    proj_t = np.eye(geom.nsite * DIM, dtype=complex) - proj_l

    def relative_mixing(matrix):
        mom = unitary @ matrix.astype(complex) @ unitary.conj().T
        mixed = proj_t @ mom @ proj_l
        return (
            float(np.linalg.norm(mixed)),
            float(np.linalg.norm(mom)),
            float(np.linalg.norm(mixed) / np.linalg.norm(mom)),
        )

    rows = []
    for amp in amplitudes:
        if amp == 0.0:
            h = flat_metric(geom)
        else:
            h = cosine_weak_field(
                geom, amp, BACKGROUND_PATTERN, BACKGROUND_WAVEVECTOR
            )
        operator, hessian, mass_metric = vector_operator(
            geom, h, mass_squared, return_parts=True
        )
        op_mixed, op_norm, op_rel = relative_mixing(operator)
        pre = hessian + float(mass_squared) * mass_metric
        pre_mixed, pre_norm, pre_rel = relative_mixing(pre)
        gauge_kernel = relative_mixing(hessian)[0]
        rows.append(
            {
                "amplitude": float(amp),
                "mixed_frobenius": op_mixed,
                "operator_frobenius": op_norm,
                "relative_mixing": op_rel,
                "pre_division_mixed_frobenius": pre_mixed,
                "pre_division_frobenius": pre_norm,
                "pre_division_relative_mixing": pre_rel,
                "hessian_times_longitudinal_projector_norm": gauge_kernel,
            }
        )

    def leading_power(key):
        positive = [r for r in rows if r["amplitude"] > 0.0 and r[key] > 0.0]
        if len(positive) < 2:
            return None
        xs = np.log(np.array([r["amplitude"] for r in positive]))
        ys = np.log(np.array([r[key] for r in positive]))
        return float(np.polyfit(xs, ys, 1)[0])

    return {
        "extent": extent,
        "mass_squared": mass_squared,
        "rows": rows,
        "leading_power_in_amplitude": leading_power("relative_mixing"),
        "pre_division_leading_power_in_amplitude": leading_power(
            "pre_division_relative_mixing"
        ),
    }


# ----------------------------------------------------------------------------
# (c) the compensating scalar
# ----------------------------------------------------------------------------


def validate_compensating_scalar(extent=4, mass_squared=0.25):
    """The scalar must be ``Delta + m^2``, propagating, not the ultralocal ``m^2``."""
    geom = LatticeGeometry(extent)
    operator = scalar_operator(geom, flat_metric(geom), mass_squared)
    numeric = np.sort(np.linalg.eigvalsh(0.5 * (operator + operator.T)))
    required = flat_scalar_eigenvalues(geom, mass_squared)
    spread = float(numeric[-1] - numeric[0])
    return {
        "extent": extent,
        "mass_squared": mass_squared,
        "max_abs_deviation": float(np.max(np.abs(numeric - required))),
        "min_eigenvalue": float(numeric[0]),
        "max_eigenvalue": float(numeric[-1]),
        "eigenvalue_spread": spread,
        "distinct_eigenvalue_count": int(
            len(np.unique(np.round(numeric, 10)))
        ),
        "is_ultralocal": bool(spread < 1e-10),
    }


# ----------------------------------------------------------------------------
# (d) refinement and enlargement
# ----------------------------------------------------------------------------


def scan_extents_and_masses(extents=(4, 6), masses=(0.25, 1.0)):
    """Repeat (a) and (c) over two extents and two masses."""
    rows = []
    for extent in extents:
        for mass_squared in masses:
            vector = validate_flat_vector_spectrum(extent, mass_squared)
            scalar = validate_compensating_scalar(extent, mass_squared)
            rows.append(
                {
                    "extent": extent,
                    "mass_squared": mass_squared,
                    "vector_max_abs_deviation": vector["max_abs_deviation"],
                    "vector_flat_band_multiplicity": vector["flat_band_multiplicity"],
                    "vector_flat_band_required": vector[
                        "flat_band_multiplicity_required"
                    ],
                    "vector_logdet_absolute_difference": vector[
                        "logdet_absolute_difference"
                    ],
                    "vector_relative_asymmetry": vector["relative_asymmetry"],
                    "scalar_max_abs_deviation": scalar["max_abs_deviation"],
                    "scalar_min_eigenvalue": scalar["min_eigenvalue"],
                    "scalar_is_ultralocal": scalar["is_ultralocal"],
                }
            )
    return rows


# ----------------------------------------------------------------------------
# (e) the derivative machinery
# ----------------------------------------------------------------------------


def _central_difference(func, point, step):
    return (func(point + step) - func(point - step)) / (2.0 * step)


def _richardson(coarse, fine, order=2):
    """One Richardson step for a difference rule of the given order.

    With ``fine`` taken at half the coarse step, the leading error term cancels.
    """
    factor = 2.0**order
    return (factor * fine - coarse) / (factor - 1.0)


def validate_mass_derivative(extent=4, mass_squared=0.5, steps=(0.04, 0.02, 0.01)):
    """Numerical ``d/d(m^2) log det(D0 + m^2)`` against a closed form.

    The closed form is ``sum_p 1 / (phat2(p) + m^2)``, which is also
    ``trace (D0 + m^2)^{-1}`` -- an answer known independently of the
    construction and unrelated to any ratio target.
    """
    geom = LatticeGeometry(extent)
    h = flat_metric(geom)

    def logdet_at(value):
        return logdet_operator(scalar_operator(geom, h, value))

    two_pi_over_l = 2.0 * np.pi / geom.extent
    closed_form = 0.0
    for c in geom.coords:
        p = two_pi_over_l * np.asarray(c, dtype=float)
        closed_form += 1.0 / (phat2(p) + mass_squared)

    rows = []
    for step in steps:
        estimate = _central_difference(logdet_at, mass_squared, step)
        rows.append(
            {
                "step": float(step),
                "estimate": float(estimate),
                "absolute_error": float(abs(estimate - closed_form)),
            }
        )
    richardson = None
    if len(rows) >= 2:
        richardson = _richardson(rows[-2]["estimate"], rows[-1]["estimate"])
    return {
        "extent": extent,
        "mass_squared": mass_squared,
        "closed_form": float(closed_form),
        "rows": rows,
        "richardson_estimate": None if richardson is None else float(richardson),
        "richardson_absolute_error": (
            None if richardson is None else float(abs(richardson - closed_form))
        ),
    }


def validate_background_derivative(
    extent=4, mass_squared=0.5, steps=(0.02, 0.01, 0.005)
):
    """First and second background derivatives of ``log det(D1 + m^2)`` at ``h = 0``.

    The background is a single cosine whose half period is an integer number of
    lattice sites, so translating by that amount sends ``h -> -h`` while leaving
    the lattice invariant.  The determinant is therefore an even function of the
    amplitude and its FIRST derivative at zero vanishes exactly -- a known
    answer that tests the derivative machinery without any external target.
    The second derivative is not zero and is reported with a Richardson step.
    """
    geom = LatticeGeometry(extent)
    half_period, remainder = divmod(geom.extent, 2 * int(BACKGROUND_WAVEVECTOR[0]))
    symmetry_available = remainder == 0

    def logdet_at(amplitude):
        if amplitude == 0.0:
            h = flat_metric(geom)
        else:
            h = cosine_weak_field(
                geom, amplitude, BACKGROUND_PATTERN, BACKGROUND_WAVEVECTOR
            )
        return logdet_operator(vector_operator(geom, h, mass_squared))

    baseline = logdet_at(0.0)
    first_rows = []
    second_rows = []
    for step in steps:
        plus = logdet_at(step)
        minus = logdet_at(-step)
        first_rows.append(
            {
                "step": float(step),
                "first_derivative": float((plus - minus) / (2.0 * step)),
            }
        )
        second_rows.append(
            {
                "step": float(step),
                "second_derivative": float(
                    (plus - 2.0 * baseline + minus) / (step**2)
                ),
            }
        )
    richardson_second = _richardson(
        second_rows[-2]["second_derivative"], second_rows[-1]["second_derivative"]
    )
    return {
        "extent": extent,
        "mass_squared": mass_squared,
        "half_period_sites": int(half_period),
        "symmetry_available": bool(symmetry_available),
        "baseline_logdet": float(baseline),
        "first_derivative_rows": first_rows,
        "max_abs_first_derivative": float(
            max(abs(r["first_derivative"]) for r in first_rows)
        ),
        "second_derivative_rows": second_rows,
        "richardson_second_derivative": float(richardson_second),
    }


# ----------------------------------------------------------------------------
# driver
# ----------------------------------------------------------------------------


def run_all():
    return {
        "a_flat_vector_spectrum": validate_flat_vector_spectrum(),
        "b_mixing": measure_mixing(),
        "c_compensating_scalar": validate_compensating_scalar(),
        "d_extent_and_mass_scan": scan_extents_and_masses(),
        "e_mass_derivative": validate_mass_derivative(),
        "e_background_derivative": validate_background_derivative(),
    }


def main():  # pragma: no cover - reporting only
    import json

    print(json.dumps(run_all(), indent=2, sort_keys=True))


if __name__ == "__main__":  # pragma: no cover
    main()
