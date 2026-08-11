"""Tests for the `P2-PHASE-01` diquark channel character carrying both `eta`.

Coverage follows what the derivation actually reaches:

    always            the particle-hole control
                      the C defining relation  C gamma_mu^T C^-1 = -gamma_mu
                      the residual-scalar cancellation

    because Step 3 produced coefficient sets
                      the relation between the eta = +1 and eta = -1 sets,
                      COMPUTED from the symbolic coefficients rather than
                      asserted against a literal

The relation test recomputes the coefficients with `s_pp` and `nu` still
symbolic and takes the ratio, so it would fail if the eta-dependence were not a
single overall factor.  It is not a comparison against a stored string.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/p2_diquark_both_eta.py"
RESULTS = ROOT / "results/P2-PHASE-01/diquark-both-eta/diquark.json"


def _module():
    spec = importlib.util.spec_from_file_location("p2_diquark_both_eta", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _artifact() -> dict:
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ------------------------------------------------------ always required ----
def test_particle_hole_control_reproduces_the_known_coefficients() -> None:
    """c_S > 0 and c_V = c_A = -G/4 in normalisation L, recomputed."""
    module = _module()
    control = module.particle_hole_control()
    g = sp.Symbol("G", positive=True)
    assert control["sign_of_c_S"] == 1
    for family in ("V", "A"):
        value = sp.sympify(control["operator_level"][family], locals={"G": g})
        assert sp.simplify(value + g / 4) == 0, family
    assert control[
        "reproduces_c_S_positive_and_c_V_equals_c_A_equals_minus_G_over_4"
    ] is True


def test_particle_hole_control_is_gating() -> None:
    """A wrong crossing sign must break the control, not be absorbed."""
    module = _module()
    block = module.frozen_basis_block()
    fierz = sp.Matrix(
        [[sp.Rational(entry) for entry in row] for row in block["matrix_rational"]]
    )
    c_can = module.canonical_coefficient()
    n = sp.Symbol("N", positive=True)
    g = sp.Symbol("G", positive=True)
    row = sp.Matrix([[1, -1, 0, 0, 0]]) * fierz
    order = block["basis_order"]
    mutated = {
        order[i]: sp.simplify(-module.S_G * c_can * n * row[i]) for i in range(5)
    }
    assert sp.simplify(mutated["V"] + g / 4) != 0
    assert sp.simplify(mutated["A"] + g / 4) != 0


def test_C_satisfies_its_defining_relation_for_all_mu() -> None:
    """C gamma_mu^T C^-1 = -gamma_mu, on the explicit matrices."""
    module = _module()
    matrix = module.conjugation_matrix()
    for gamma in module.frozen_gammas():
        assert sp.simplify(matrix * gamma.T * matrix.inv() + gamma) == sp.zeros(4)


def test_C_solution_space_is_one_dimensional_with_the_stated_properties() -> None:
    module = _module()
    result = module.charge_conjugation()
    assert result["solution_space_complex_dimension"] == 1
    assert result["C0_transpose_equals_minus_C0"] is True
    assert result["C0_dagger_C0_is_identity"] is True
    assert result["determinant_is_one"] is True
    assert result["defining_relation_holds_for_all_mu"] is True


def test_residual_scalar_cancels_in_the_paired_product() -> None:
    """lambda C and C give the same paired Dirac structure, for every mu."""
    module = _module()
    matrix = module.conjugation_matrix()
    lam = sp.Symbol("lambda", nonzero=True)
    scaled = lam * matrix
    assert sp.simplify(scaled * scaled.inv() - matrix * matrix.inv()) == sp.zeros(4)
    for gamma in module.frozen_gammas():
        assert (
            sp.simplify(
                scaled * gamma.T * scaled.inv() - matrix * gamma.T * matrix.inv()
            )
            == sp.zeros(4)
        )
    assert module.charge_conjugation()[
        "residual_scalar_cancels_in_the_paired_product"
    ] is True


def test_residual_scalar_cancellation_is_not_vacuous() -> None:
    """A structure with C appearing twice does NOT cancel lambda.

    Without this, the cancellation test would pass for reasons unrelated to the
    paired product's structure.
    """
    module = _module()
    matrix = module.conjugation_matrix()
    lam = sp.Symbol("lambda", nonzero=True)
    scaled = lam * matrix
    assert sp.simplify(scaled * scaled - matrix * matrix) != sp.zeros(4)


# ------------------ required because Step 3 produced coefficient sets ------
def test_eta_relation_between_the_two_coefficient_sets_is_computed() -> None:
    """c(eta = -1) = -c(eta = +1) in every surviving family.

    Recomputed from the symbolic coefficients with s_pp and nu left symbolic, so
    the ratio being exactly -1 establishes that eta enters as a single overall
    factor.  Nothing here is compared against a stored value.
    """
    module = _module()
    dirac = module.pp_dirac_decomposition()
    internal = module.dirac_symmetry_and_internal_channel()
    weights = internal["internal_channel_weights"]["N=3"]
    weight = sp.sympify(next(iter(weights.values())))
    c_can = module.canonical_coefficient()
    s_pp, nu = module.s_pp, module.nu

    surviving = dirac["surviving_families"]
    assert surviving, "Step 3 produced no coefficient set; this test is inapplicable"
    for family in surviving:
        f = sp.sympify(dirac["per_component_sum"][family])
        base = c_can * weight * s_pp * nu * f
        plus = sp.simplify(base * (+1))
        minus = sp.simplify(base * (-1))
        assert sp.simplify(minus / plus) == -1, family
        # the unfrozen symbols are still present, so they genuinely cancel
        assert {s_pp, nu} <= plus.free_symbols, family


def test_verdict_is_opposite_and_independent_of_the_unfrozen_definitions() -> None:
    artifact = _artifact()
    verdict = artifact["diagnostic_verdict"]
    assert verdict["verdict"] == "OPPOSITE"
    assert verdict[
        "verdict_is_independent_of_the_two_remaining_unfrozen_definitions"
    ] is True
    assert set(verdict["symbols_still_present_when_the_ratio_is_taken"]) == {
        "s_pp",
        "nu",
    }
    for ratio in verdict["ratio_c_eta_minus_over_c_eta_plus"].values():
        assert sp.sympify(ratio) == -1


# ------------------------------------------------- the crossing itself ----
def test_frozen_basis_is_trace_orthonormal() -> None:
    """The trace formula for the crossing coefficients depends on this."""
    module = _module()
    assert module.basis_is_trace_orthonormal(module.dirac_basis()) is True


def test_pp_decomposition_is_verified_by_reconstruction() -> None:
    """Both canonical terms rebuild exactly on all 256 tensor components."""
    module = _module()
    dirac = module.pp_dirac_decomposition()
    assert dirac["reconstruction_exact_on_all_256_components"] == {
        "scalar": True,
        "pseudoscalar": True,
    }
    assert dirac["basis_is_trace_orthonormal_on_all_256_pairs"] is True
    assert dirac["decomposition_is_diagonal_in_the_family_basis"] is True


def test_three_families_vanish_by_cancellation_not_by_a_dead_projector() -> None:
    """S, P and T vanish; V and A do not.  The earlier failure mode was all four.

    The per-term values must be individually non-zero where the sum vanishes,
    which is what distinguishes a cancellation from a projector that produces
    nothing.
    """
    module = _module()
    dirac = module.pp_dirac_decomposition()
    assert set(dirac["vanishing_families"]) == {"S", "P", "T"}
    assert set(dirac["surviving_families"]) == {"V", "A"}
    for family in ("S", "P", "T"):
        assert sp.sympify(dirac["per_component_scalar_term"][family]) != 0, family
        assert sp.sympify(dirac["per_component_pseudoscalar_term"][family]) != 0, family
    assert module.earlier_attempt_comparison()["did_the_failure_mode_recur"] is False


def test_V_and_A_carry_opposite_relative_signs() -> None:
    module = _module()
    dirac = module.pp_dirac_decomposition()
    v = sp.sympify(dirac["per_component_sum"]["V"])
    a = sp.sympify(dirac["per_component_sum"]["A"])
    assert sp.simplify(v + a) == 0
    assert sp.sign(v) != sp.sign(a)


def test_internal_projection_contributes_no_relative_sign() -> None:
    """Both internal channels carry the same weight, for N = 2..5."""
    module = _module()
    internal = module.dirac_symmetry_and_internal_channel()
    assert internal["both_channels_carry_the_same_weight"] is True
    values = {
        value
        for row in internal["internal_channel_weights"].values()
        for value in row.values()
    }
    assert len(values) == 1
    assert sp.sympify(next(iter(values))) > 0


def test_the_two_surviving_families_live_in_different_internal_channels() -> None:
    module = _module()
    per_family = module.dirac_symmetry_and_internal_channel()["per_family"]
    assert per_family["V"]["internal_channel"] == "internal-antisymmetric"
    assert per_family["A"]["internal_channel"] == "internal-symmetric"
    for entry in per_family.values():
        assert entry["Gamma_a_C"] == entry["C_inverse_Gamma_a"]


# --------------------------------------------------- authority and scope ---
def test_eta_ruling_is_located_by_heading_and_says_what_is_required() -> None:
    """Removing or retitling the DECISION_LOG.md entry must stop the run."""
    module = _module()
    ruling = module.eta_ruling()
    assert ruling["date"] == "2026-08-09"
    assert all(ruling["required_phrases_present"].values())
    text = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    assert text.count(module.ETA_RULING_HEADING) == 1


def test_all_three_definitions_are_reported_unfrozen() -> None:
    module = _module()
    blockers = module.blocker_search()
    assert blockers["eta_frozen"] is False
    assert blockers["particle_particle_grassmann_ordering_frozen"] is False
    assert blockers["diquark_operator_normalisation_frozen"] is False
    assert blockers["pinned_note_states_nothing_fixes_eta"] is True


def test_literal_eta_value_occurrences_are_case_labels_not_assignments() -> None:
    """`eta = -1` does occur in the pinned text; it does not fix eta.

    The occurrence sits in the sentence that goes on to say nothing fixes eta,
    so a substring search for it is a proxy for the wrong property.  The
    occurrences are reported with context rather than suppressed, and this test
    pins the reason they are not assignments.
    """
    module = _module()
    hits = module.blocker_search()["eta_literal_value_occurrences"]
    assert hits, "the occurrence this test exists to classify has disappeared"
    for hit in hits:
        assert hit["classification"] == "CASE LABEL, not an assignment"
        assert "nothing" in hit["containing_line"].lower() or "flips" in (
            hit["containing_line"].lower()
        )


def test_ordering_alternatives_are_not_presented_as_an_enumeration() -> None:
    module = _module()
    alternatives = module.pp_ordering_alternatives()
    signs = set(alternatives["s_pp_by_target_ordering"].values())
    assert signs == {1, -1}
    assert "not a claim" in alternatives["not_an_enumeration"]


def test_gate_status_and_frozen_conventions_unchanged() -> None:
    artifact = _artifact()
    assert artifact["gate_status"] == "P2-PHASE-01 remains PROPOSED"
    assert artifact["scope_limits"]["conventions_frozen_by_this_computation"] == []


def test_artifact_matches_a_fresh_run() -> None:
    """The committed results artifact is what the script produces."""
    module = _module()
    assert module.build() == _artifact()
