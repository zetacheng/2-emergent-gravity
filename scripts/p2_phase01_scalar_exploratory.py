"""Exploratory scalar stationary solutions for ``P2-PHASE-01`` at ``mu = 0``.

This is deliberately not a gate computation.  It evaluates only the uniform
scalar ansatz whose normalization is fixed by ``P2-GAP-01``.  The output never
classifies a phase as admissible, preferred, or excluded.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

GRID_SIZES = (32, 40, 48)
SHIFTS = (0.0, 0.25)
G_RATIOS = (
    0.8,
    0.9,
    0.98,
    0.99,
    1.0,
    1.01,
    1.02,
    1.05,
    1.1,
    1.2,
    1.4,
    1.6,
    1.8,
    2.0,
    2.5,
    3.0,
)
SMALL_MASSES = (0.01, 0.02, 0.04, 0.08, 0.12, 0.16)


def _axis(n: int, shift: float) -> np.ndarray:
    return (np.arange(n) + 0.5 + shift) * (2.0 * math.pi / n) - math.pi


@dataclass
class WilsonQuadrature:
    """Product-midpoint Wilson integral and its analytic mass derivative."""

    n: int
    shift: float
    _sin2: np.ndarray = field(init=False, repr=False)
    _omc: np.ndarray = field(init=False, repr=False)
    _s3: np.ndarray = field(init=False, repr=False)
    _w3: np.ndarray = field(init=False, repr=False)
    _cache: dict[float, tuple[float, float]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        axis = _axis(self.n, self.shift)
        self._sin2 = np.sin(axis) ** 2
        self._omc = 1.0 - np.cos(axis)
        self._s3 = (
            self._sin2[:, None, None]
            + self._sin2[None, :, None]
            + self._sin2[None, None, :]
        )
        self._w3 = (
            self._omc[:, None, None]
            + self._omc[None, :, None]
            + self._omc[None, None, :]
        )

    def bubble_and_derivative(self, mhat: float) -> tuple[float, float]:
        """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""
        key = round(float(mhat), 13)
        if key in self._cache:
            return self._cache[key]
        bubble = 0.0
        derivative = 0.0
        for index in range(self.n):
            s = self._s3 + self._sin2[index]
            w = mhat + self._w3 + self._omc[index]
            denominator = s + w * w
            bubble += float(np.sum(1.0 / denominator))
            derivative -= float(np.sum(2.0 * w / (denominator * denominator)))
        value = bubble / self.n**4, derivative / self.n**4
        self._cache[key] = value
        return value

    def bubble(self, mhat: float) -> float:
        return self.bubble_and_derivative(mhat)[0]


def gc_from_i0(i0: float) -> float:
    return 1.0 / (2.0 * i0)


def first_derivative(
    mhat: float, coupling: float, quadrature: WilsonQuadrature
) -> float:
    """Full reduced derivative retaining the prefactor that gives the zero root."""
    return mhat * (1.0 / (2.0 * coupling) - quadrature.bubble(mhat))


def reduced_curvature(
    mhat: float, coupling: float, quadrature: WilsonQuadrature
) -> float:
    """Analytic derivative of the complete reduced first derivative."""
    bubble, derivative = quadrature.bubble_and_derivative(mhat)
    return 1.0 / (2.0 * coupling) - bubble - mhat * derivative


def reconstructed_potential(
    mhat: float, coupling: float, quadrature: WilsonQuadrature, order: int = 24
) -> float:
    """Numerically reconstruct ``V_red(Mhat)-V_red(0)`` by Gauss-Legendre quadrature."""
    nodes, weights = np.polynomial.legendre.leggauss(order)
    points = 0.5 * mhat * (nodes + 1.0)
    integral = 0.5 * mhat * sum(
        weight * point * quadrature.bubble(float(point))
        for point, weight in zip(points, weights, strict=True)
    )
    return mhat * mhat / (4.0 * coupling) - integral


def finite_difference_curvature(
    mhat: float, coupling: float, quadrature: WilsonQuadrature, h: float = 2.0e-3
) -> float:
    center = reconstructed_potential(mhat, coupling, quadrature)
    upper = reconstructed_potential(mhat + h, coupling, quadrature)
    lower = reconstructed_potential(mhat - h, coupling, quadrature)
    return (upper - 2.0 * center + lower) / (h * h)


def divided_gap(mhat: float, coupling: float, quadrature: WilsonQuadrature) -> float:
    return 1.0 - 2.0 * coupling * quadrature.bubble(mhat)


def bisect_root(
    left: float, right: float, coupling: float, quadrature: WilsonQuadrature
) -> float:
    """Bracketed root of the divided equation, used only away from the zero root."""
    f_left = divided_gap(left, coupling, quadrature)
    f_right = divided_gap(right, coupling, quadrature)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0.0:
        raise ValueError(f"unbracketed root on [{left}, {right}]")
    # The bracket width after 17 iterations is below 1e-4, comfortably below
    # the quadrature drift reported by the three-grid convergence study.
    for _ in range(17):
        middle = 0.5 * (left + right)
        f_middle = divided_gap(middle, coupling, quadrature)
        if f_left * f_middle <= 0.0:
            right, f_right = middle, f_middle
        else:
            left, f_left = middle, f_middle
    return 0.5 * (left + right)


def algebraic_roots(coupling: float, quadrature: WilsonQuadrature) -> list[float]:
    """Roots in the two monotonic Wilson-complement sectors plus the zero branch."""
    roots = [0.0]
    for left, right in ((-12.0, -4.0), (-4.0, 4.0)):
        root = bisect_root(left, right, coupling, quadrature)
        if all(abs(root - known) > 2.0e-4 for known in roots):
            roots.append(root)
    return sorted(roots)


def root_record(mhat: float, coupling: float, quadrature: WilsonQuadrature) -> dict:
    bubble = quadrature.bubble(mhat)
    gap_factor = divided_gap(mhat, coupling, quadrature)
    residual = (
        abs(gap_factor)
        if mhat
        else abs(first_derivative(mhat, coupling, quadrature))
    )
    return {
        "mhat": mhat,
        "stationarity_residual": residual,
        "divided_gap_factor": gap_factor,
        "reduced_curvature": reduced_curvature(mhat, coupling, quadrature),
        "I0": bubble,
        "branch": "trivial" if mhat == 0.0 else "nontrivial_algebraic",
    }


def grid_result(n: int, shift: float) -> dict:
    quadrature = WilsonQuadrature(n=n, shift=shift)
    i0 = quadrature.bubble(0.0)
    gc = gc_from_i0(i0)
    rows = []
    for ratio in G_RATIOS:
        coupling = ratio * gc
        roots = [
            root_record(root, coupling, quadrature)
            for root in algebraic_roots(coupling, quadrature)
        ]
        rows.append({"G_over_Gc": ratio, "G": coupling, "roots": roots})
    return {
        "n": n,
        "shift": shift,
        "I0_at_zero": i0,
        "Gc": gc,
        "roots": rows,
        "mhat_one_crossing_G_over_Gc": i0 / quadrature.bubble(1.0),
        "small_mass_I0_difference": [
            {
                "mhat": value,
                "I0_zero_minus_I0_mhat": i0 - quadrature.bubble(value),
            }
            for value in SMALL_MASSES
        ],
    }


def power_fit(points: list[tuple[float, float]]) -> dict:
    x = np.asarray([math.log(delta) for delta, mass in points])
    y = np.asarray([math.log(mass) for delta, mass in points])
    slope, intercept = np.polyfit(x, y, 1)
    fitted = slope * x + intercept
    return {
        "points": len(points),
        "beta": float(slope),
        "prefactor": float(math.exp(intercept)),
        "log_rms_residual": float(math.sqrt(np.mean((y - fitted) ** 2))),
    }


def small_mass_analysis(finest: dict) -> dict:
    points = [
        (item["mhat"], item["I0_zero_minus_I0_mhat"])
        for item in finest["small_mass_I0_difference"]
    ]
    x = np.asarray([math.log(mhat) for mhat, _ in points])
    y = np.asarray([math.log(delta) for _, delta in points])
    slope, intercept = np.polyfit(x, y, 1)
    fitted = slope * x + intercept
    return {
        "fit": "I0(0)-I0(Mhat) = coefficient * Mhat**alpha",
        "alpha": float(slope),
        "coefficient": float(math.exp(intercept)),
        "log_rms_residual": float(math.sqrt(np.mean((y - fitted) ** 2))),
        "points": [
            {"mhat": mhat, "I0_zero_minus_I0_mhat": delta}
            for mhat, delta in points
        ],
    }


def onset_analysis(finest: dict) -> dict:
    positive = []
    for row in finest["roots"]:
        ratio = row["G_over_Gc"]
        roots = [item["mhat"] for item in row["roots"] if item["mhat"] > 1.0e-4]
        if ratio > 1.0 and roots:
            positive.append((ratio - 1.0, roots[-1]))
    windows = {
        "1.01_to_1.10": [point for point in positive if point[0] <= 0.10],
        "1.02_to_1.20": [point for point in positive if 0.02 <= point[0] <= 0.20],
        "1.05_to_1.40": [point for point in positive if 0.05 <= point[0] <= 0.40],
    }
    local = []
    for first, second in zip(positive, positive[1:]):
        local.append(
            {
                "between_G_over_Gc": [first[0] + 1.0, second[0] + 1.0],
                "beta_effective": math.log(second[1] / first[1])
                / math.log(second[0] / first[0]),
            }
        )
    return {
        "small_mass_behavior": small_mass_analysis(finest),
        "bare_power_fits": {
            name: power_fit(points)
            for name, points in windows.items()
            if len(points) >= 2
        },
        "local_effective_exponents": local,
        "near_critical_exclusion": (
            "G/Gc-1 < 0.01 is excluded from fits because root/grid resolution "
            "dominates there."
        ),
        "logarithmic_fit": (
            "not attempted: the fitted small-Mhat difference is close to a "
            "regular linear power, so a logarithmic correction is not motivated "
            "by this finite-grid diagnostic."
        ),
    }


def symmetry_check(finest_n: int) -> dict:
    quadrature = WilsonQuadrature(n=finest_n, shift=0.0)
    sign_pairs = []
    complement_pairs = []
    for mhat in (0.1, 0.5, 1.0):
        positive = quadrature.bubble(mhat)
        negative = quadrature.bubble(-mhat)
        sign_pairs.append(
            {
                "mhat": mhat,
                "I0_positive": positive,
                "I0_negative": negative,
                "ratio_negative_over_positive": negative / positive,
            }
        )
    for mhat in (-1.3, -0.4, 0.7, 1.8):
        first = quadrature.bubble(mhat)
        second = quadrature.bubble(-8.0 - mhat)
        complement_pairs.append(
            {
                "mhat": mhat,
                "complement": -8.0 - mhat,
                "absolute_difference": abs(first - second),
            }
        )
    return {
        "Mhat_to_negative_Mhat": (
            "not a symmetry: the frozen Wilson integral differs at every tested "
            "nonzero mass."
        ),
        "sign_pairs": sign_pairs,
        "wilson_complement_relation": (
            "I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu; numerically "
            "checked below."
        ),
        "complement_pairs": complement_pairs,
    }


def channel_executability() -> list[dict]:
    common_missing = [
        "HS normalization",
        "uniform condensate ansatz",
        "common zero and measure normalization for cross-family potentials",
    ]
    return [
        {
            "family": "S",
            "executable": True,
            "basis": (
                "P2-GAP-01 fixes the scalar channel normalization, uniform "
                "self-energy ansatz, and reduced gap functional."
            ),
        },
        {
            "family": "P",
            "executable": False,
            "missing": common_missing
            + [
                "frozen quadratic G projection/sign for a pseudoscalar "
                "mean-field potential"
            ],
        },
        {
            "family": "V",
            "executable": False,
            "missing": common_missing
            + [
                "uniform vector direction and Lorentz/H(4) component choice",
                "internal generator choice",
            ],
        },
        {
            "family": "A",
            "executable": False,
            "missing": common_missing
            + [
                "uniform axial direction and Lorentz/H(4) component choice",
                "internal generator choice",
            ],
        },
        {
            "family": "T",
            "executable": False,
            "missing": common_missing
            + [
                "tensor-plane and Lorentz/H(4) component choice",
                "internal generator choice",
            ],
        },
    ]


def build_results() -> dict:
    grids = [grid_result(n, shift) for n in GRID_SIZES for shift in SHIFTS]
    finest = next(
        item
        for item in grids
        if item["n"] == max(GRID_SIZES) and item["shift"] == 0.25
    )
    validation_quad = WilsonQuadrature(n=16, shift=0.25)
    validation_gc = gc_from_i0(validation_quad.bubble(0.0))
    validation_root = algebraic_roots(1.4 * validation_gc, validation_quad)[-1]
    analytic = reduced_curvature(validation_root, 1.4 * validation_gc, validation_quad)
    finite_difference = finite_difference_curvature(
        validation_root, 1.4 * validation_gc, validation_quad
    )
    source = Path(__file__).read_bytes()
    return {
        "study": "P2-PHASE-01 exploratory scalar stationary solutions",
        "status": "EXPLORATORY; not a gate result; no admissibility verdict",
        "mu": 0.0,
        "script": str(Path(__file__).relative_to(Path(__file__).parents[1])).replace(
            "\\", "/"
        ),
        "script_sha256": hashlib.sha256(source).hexdigest(),
        "frozen_relation": (
            "1 = 2 G I0(Mhat); full derivative is Mhat*(1/(2G)-I0(Mhat))"
        ),
        "quadrature": "4D product-midpoint BZ grid; shifts 0.0 and 0.25",
        "grid_results": grids,
        "symmetry": symmetry_check(max(GRID_SIZES)),
        "onset": onset_analysis(finest),
        "onset_by_grid": [
            {"n": item["n"], "shift": item["shift"], "analysis": onset_analysis(item)}
            for item in grids
        ],
        "curvature_regression": {
            "n": 16,
            "shift": 0.25,
            "G_over_Gc": 1.4,
            "mhat": validation_root,
            "analytic_full_derivative": analytic,
            "finite_difference_reconstructed_potential": finite_difference,
            "absolute_difference": abs(analytic - finite_difference),
        },
        "channel_executability": channel_executability(),
        "exclusions": [
            "quarantined -3.2(5)",
            "suspended P2-BETAV-CIRC-01 result",
            "historical Finding 5 extraction",
        ],
        "limitations": [
            "restricted to a uniform scalar ansatz at mu=0",
            "one-dimensional curvature is not the full multichannel Hessian",
            "no cross-family effective-potential comparison is constructed",
        ],
    }


def main() -> None:
    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "P2-PHASE-01"
        / "exploratory-scalar-stationary"
    )
    output.mkdir(parents=True, exist_ok=True)
    result = build_results()
    path = output / "scalar_stationary.json"
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    anchor = result["grid_results"][-1]
    print("P2-PHASE-01 exploratory scalar stationary study (mu=0)")
    print(f"wrote {path}")
    print(f"finest I0(0) = {anchor['I0_at_zero']:.8f}; Gc = {anchor['Gc']:.8f}")


if __name__ == "__main__":
    main()
