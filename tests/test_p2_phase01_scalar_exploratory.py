"""Regression coverage for the exploratory scalar stationary study."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import p2_phase01_scalar_exploratory as scalar

ROOT = Path(__file__).resolve().parents[1]
RESULT = (
    ROOT
    / "results"
    / "P2-PHASE-01"
    / "exploratory-scalar-stationary"
    / "scalar_stationary.json"
)


def result_document() -> dict:
    return json.loads(RESULT.read_text(encoding="utf-8"))


def test_zero_mass_anchor_matches_reported_grid() -> None:
    document = result_document()
    reported = next(
        item
        for item in document["grid_results"]
        if item["n"] == 32 and item["shift"] == 0.0
    )
    quadrature = scalar.WilsonQuadrature(n=32, shift=0.0)
    assert quadrature.bubble(0.0) == pytest.approx(reported["I0_at_zero"], abs=1e-13)
    assert scalar.gc_from_i0(quadrature.bubble(0.0)) == pytest.approx(
        reported["Gc"], abs=1e-12
    )


def test_wilson_mass_reflection_is_not_symmetrized() -> None:
    quadrature = scalar.WilsonQuadrature(n=24, shift=0.0)
    assert quadrature.bubble(0.1) != pytest.approx(quadrature.bubble(-0.1), abs=1e-6)
    assert quadrature.bubble(0.7) == pytest.approx(
        quadrature.bubble(-8.7), abs=1e-12
    )


def test_reported_root_residuals_are_small() -> None:
    document = result_document()
    residuals = [
        root["stationarity_residual"]
        for grid in document["grid_results"]
        for row in grid["roots"]
        for root in row["roots"]
    ]
    assert max(residuals) < 3.0e-5


def test_reconstructed_potential_curvature_matches_full_derivative() -> None:
    quadrature = scalar.WilsonQuadrature(n=12, shift=0.25)
    coupling = 1.4 * scalar.gc_from_i0(quadrature.bubble(0.0))
    root = scalar.algebraic_roots(coupling, quadrature)[-1]
    analytic = scalar.reduced_curvature(root, coupling, quadrature)
    finite_difference = scalar.finite_difference_curvature(root, coupling, quadrature)
    assert finite_difference == pytest.approx(analytic, abs=1.0e-5)


def test_grid_refinement_schema_contains_three_sizes_and_offsets() -> None:
    document = result_document()
    records = document["grid_results"]
    assert {item["n"] for item in records} == {32, 40, 48}
    assert {item["shift"] for item in records} == {0.0, 0.25}
    assert all("small_mass_I0_difference" in item for item in records)
