"""Tests for ``P2-XI-LEDGER-01`` — the conditional analytic ξ ledger, Phase 1.

Every expected value below is the landed value quoted in
``derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md`` with its
``path:line``. These tests check the assembly against the landed record; they
assign no value to any OPEN ledger row, and a test that did so would contradict
the OPEN status it is meant to protect.
"""

from __future__ import annotations

import sympy as sp

from scripts.xi_ledger import (
    CLASSES,
    FOUR_G_BETA_F,
    L_POINTS,
    L_RANGE,
    OPEN_ROWS,
    THRESHOLD,
    K,
    L,
    delta_xi_flip,
    f0,
    r_margin,
    species_per_class,
    species_total,
    survival_L_boundary,
    survival_mass_boundary,
    xi_cond,
    xi_sym,
)


# --- M2: per-species totals against the M1-extracted values ----------------
# P2-HK-01:84-87.
def test_species_totals_reproduce_landed_values():
    assert sp.simplify(species_total("scalar_minimal") - (-K / 12)) == 0
    assert sp.simplify(species_total("fermion_dirac") - (-K / 6)) == 0
    assert sp.simplify(species_total("vector_proca") - (K / 4)) == 0
    # β_B(ξ) = −K(1/6 − ξ)/2, P2-HK-01:85.
    expected = -K * (sp.Rational(1, 6) - xi_sym) / 2
    assert sp.simplify(species_total("scalar_nonminimal") - expected) == 0


def test_species_totals_equal_the_sum_over_coupling_classes():
    """The decomposition is a partition: classes sum to the species total."""
    for key in ("scalar_minimal", "scalar_nonminimal", "fermion_dirac",
                "vector_proca"):
        per = species_per_class(key)
        assert set(per) == set(CLASSES)
        assert sp.simplify(sum(per.values()) - species_total(key)) == 0


def test_minimal_species_carry_no_explicit_xi_R_term():
    """Only the non-minimal scalar carries an action-level ξR — CONVENTIONS.md:17."""
    for key in ("scalar_minimal", "fermion_dirac", "vector_proca"):
        assert species_per_class(key)["explicit xi*R"] == 0
    assert species_per_class("scalar_nonminimal")["explicit xi*R"] != 0


# --- M2: the three convention-independent ratios ---------------------------
# P2-HK-01:93-95.
def test_ratios_reproduce_landed_values():
    b_B = species_total("scalar_minimal")
    b_F = species_total("fermion_dirac")
    b_V = species_total("vector_proca")
    b_Bxi = species_total("scalar_nonminimal")
    assert sp.simplify(b_F / b_B - 2) == 0
    assert sp.simplify(b_V / b_B + 3) == 0
    assert sp.simplify(sp.expand(b_Bxi / b_B) - (1 - 6 * xi_sym)) == 0


# --- M4: the two survival-window boundaries, derived ----------------------
# P2-NORM-01:83 records m > 0.368Λ (1/6 convention) and m > 0.287Λ (1/3).
def test_survival_boundaries_reproduce_landed_masses():
    assert survival_L_boundary("Z_paper") == 2
    assert survival_L_boundary("Z_here") == sp.Rational(5, 2)
    m_paper = sp.N(survival_mass_boundary("Z_paper"), 20)
    m_here = sp.N(survival_mass_boundary("Z_here"), 20)
    assert round(float(m_paper), 3) == 0.368
    assert round(float(m_here), 3) == 0.287


def test_survival_boundary_is_where_the_conditional_total_meets_the_threshold():
    for conv in FOUR_G_BETA_F:
        at_boundary = xi_cond(conv).subs(L, survival_L_boundary(conv))
        assert sp.simplify(at_boundary - THRESHOLD) == 0


# --- M4: the conditional total and the frozen margin normalization --------
def test_conditional_total_is_the_landed_chain():
    """ξ_ind = 4Gβ_F(3−L) — P2-NORM-01:26, with P2-NORM-01:57's two values."""
    for conv, value in FOUR_G_BETA_F.items():
        assert sp.simplify(xi_cond(conv) - value * (3 - L)) == 0


def test_margin_normalization_is_the_L_independent_coefficient_scale():
    """F0 ≡ |4Gβ_F| — §1a. It must not depend on L, and must not vanish."""
    for conv in FOUR_G_BETA_F:
        assert f0(conv).free_symbols == set()
        assert f0(conv) != 0
        assert sp.simplify(f0(conv) - sp.Abs(FOUR_G_BETA_F[conv])) == 0


def test_margin_is_finite_at_every_representative_point_including_L_equals_3():
    """The rejected normalization vanishes at L = 3; this one does not."""
    for conv in FOUR_G_BETA_F:
        for Lv in L_POINTS:
            assert sp.N(r_margin(conv, Lv)).is_finite
        assert sp.simplify(delta_xi_flip(conv, 3) - THRESHOLD) == 0


def test_margin_is_the_distance_to_the_threshold():
    for conv in FOUR_G_BETA_F:
        for Lv in L_POINTS:
            expected = sp.Abs(THRESHOLD - xi_cond(conv).subs(L, Lv))
            assert sp.simplify(delta_xi_flip(conv, Lv) - expected) == 0


def test_the_L_grid_is_the_frozen_one():
    """§1a's grid is pre-registered; execution may not add or retune points."""
    assert L_RANGE == (sp.Rational(1, 2), sp.Integer(20))
    assert L_POINTS == (
        sp.Rational(1, 2), sp.Integer(1), sp.Integer(2), sp.Integer(3),
        sp.Integer(5), sp.Integer(10), sp.Integer(20),
    )
    assert all(L_RANGE[0] <= p <= L_RANGE[1] for p in L_POINTS)


# --- M3: the OPEN rows carry no numeric value ------------------------------
def test_open_rows_are_present_and_valueless():
    memberships = {row["membership"] for row in OPEN_ROWS}
    assert memberships == {"OPEN(Q-M2)", "OPEN(Q-M3)"}
    for row in OPEN_ROWS:
        assert row["value"] is None
        assert not isinstance(row["value"], (int, float, sp.Basic))
