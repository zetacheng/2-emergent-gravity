"""Tests for the `P2-PHASE-01` channel-character derivation.

The tests follow the three layers and stop where the layers stop. A test of
a quantity the authority permits to be undefined would be unsatisfiable, so
Layer 1b and Layer 2 are tested for being *correctly withheld* and for the
*conditional* branch arithmetic, never for a resolved admissibility or a
force label.

They deliberately do NOT assert that the frozen Fierz matrix equals itself,
and they do not assert any charge-conjugation convention.
"""

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import p2_channel_character as cc  # noqa: E402
from p2_channel_character import (  # noqa: E402
    S_G,
    canonical_coefficient,
    convention_dependence,
    diquark_executability,
    layer_1a,
    layer_1b,
    layer_2,
    scalar_control,
)

RESULTS = ROOT / "results/P2-PHASE-01/channel-character/channel_character.json"
G, N = sp.symbols("G N", positive=True)


def _expr(text):
    return sp.sympify(text, locals={"G": G, "N": N})


# ---- the scalar control, first: everything else depends on it -----------
def test_scalar_control_uses_the_p2_gap_01_operator_and_convention():
    out = scalar_control()
    assert out["operator"] == "(psibar psi)**2"
    assert out["factor_of_two_convention"] == (
        "G_GAP = 4 * G_N, absorbing trace(Id4) = 4"
    )
    assert "lam(0) = sqrt(2/N)" in out["internal_normalisation"]


def test_scalar_control_passes_with_a_positive_coefficient():
    out = scalar_control()
    assert _expr(out["G_N_from_the_frozen_singlet"]) == G / N**2
    assert _expr(out["G_GAP_from_the_frozen_singlet"]) == 4 * G / N**2
    assert out["sign_of_G_N"] == 1
    assert out["control_passes"] is True


def test_scalar_control_states_what_it_does_not_test():
    out = scalar_control()
    assert "does not re-derive G_c" in out["what_this_does_not_test"]


# ---- Layer 1a: unconditional, computed not asserted ---------------------
def test_canonical_coefficient_is_read_from_the_frozen_block():
    """Both supported families must carry the same frozen coefficient."""
    assert canonical_coefficient() == G / (2 * N)


def test_layer_1a_signs_scalar_positive_induced_negative():
    channels = layer_1a()["channels"]
    assert channels["scalar_singlet_direct"]["sign"] == +1
    assert channels["induced_V_singlet"]["sign"] == -1
    assert channels["induced_A_singlet"]["sign"] == -1
    # the sign must not be an artefact of the normalisation
    for entry in channels.values():
        assert entry["sign"] == entry["sign_of_P_normalisation"]


def test_layer_1a_coefficients_in_both_normalisations():
    channels = layer_1a()["channels"]
    assert _expr(channels["scalar_singlet_direct"]["normalisation_L"]) == G / (2 * N)
    assert _expr(channels["scalar_singlet_direct"]["normalisation_P"]) == G / N**2
    for name in ("induced_V_singlet", "induced_A_singlet"):
        assert _expr(channels[name]["normalisation_L"]) == -G / 4
        assert _expr(channels[name]["normalisation_P"]) == -G / (2 * N)


def test_normalisation_relation_is_the_frozen_singlet_definition():
    out = layer_1a()
    channels = out["channels"]
    for entry in channels.values():
        c_l = _expr(entry["normalisation_L"])
        c_p = _expr(entry["normalisation_P"])
        assert sp.simplify(c_p - (2 / N) * c_l) == 0


def test_induced_v_and_a_are_equal_and_s_p_t_vanish():
    out = layer_1a()
    operator = out["operator_level_normalisation_L"]
    assert _expr(operator["V"]) == _expr(operator["A"])
    assert set(out["vanishing_families"]) == {"S", "P", "T"}


def test_the_basis_conversion_flips_only_the_pseudoscalar():
    out = layer_1a()
    canonical = [_expr(x) for x in out["v_canonical"]]
    frozen = [_expr(x) for x in out["v_frozen_after_I_gamma5_conversion"]]
    assert canonical[0] == frozen[0]          # S unchanged
    assert canonical[1] == -frozen[1] != 0    # P flipped
    assert canonical[2:] == frozen[2:]        # V, A, T unchanged


def test_s_g_is_applied_exactly_once_at_operator_use():
    out = layer_1a()
    assert S_G == -1
    for family in ("V", "A"):
        matrix = _expr(out["matrix_level_normalisation_L"][family])
        operator = _expr(out["operator_level_normalisation_L"][family])
        assert operator == S_G * matrix
        assert matrix == G / 4


# ---- Layer 1b: withheld, and the conditional branch arithmetic ----------
def test_layer_1b_is_withheld_because_the_mapping_is_not_frozen():
    out = layer_1b(layer_1a())
    assert out["mapping_is_fixed_by_the_frozen_material"] is False
    assert out["verdict"] == (
        "REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL"
    )
    assert out["search"]["explicit_L_to_S_E_mapping_found"] is False


def test_layer_1b_branches_differ_by_a_sign_in_every_channel():
    out = layer_1b(layer_1a())
    first = out["branches"]["branch_i_expression_already_in_the_exponent"]["channels"]
    second = out["branches"]["branch_ii_expression_is_a_term_of_S_E"]["channels"]
    for name in first:
        g_one = _expr(first[name]["g_in_normalisation_P"])
        g_two = _expr(second[name]["g_in_normalisation_P"])
        assert sp.simplify(g_one + g_two) == 0
        assert first[name]["real_linear_HS_field_admissible"] is not (
            second[name]["real_linear_HS_field_admissible"]
        )


def test_branch_ii_is_the_one_inconsistent_with_p2_gap_01():
    """P2-GAP-01 used a REAL scalar auxiliary; branch (ii) forbids one."""
    out = layer_1b(layer_1a())
    inference = out["usage_inference"]
    assert inference["branch_i_scalar_admits_real_HS"] is True
    assert inference["branch_ii_scalar_admits_real_HS"] is False
    assert inference["branch_ii_consistent_with_P2_GAP_01"] is False
    assert "INFERENCE FROM USAGE, NOT A FROZEN DEFINITION" in inference["status"]


# ---- Layer 2: withheld ---------------------------------------------------
def test_layer_2_is_withheld_and_supplies_no_general_criterion():
    out = layer_2(mapping_is_fixed=False)
    assert out["verdict"] == "ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL"
    assert out["anchors_supply_a_general_criterion"] is False
    assert "u3_fierz.md is NOT present" in out["why_not"]


def test_layer_2_does_not_use_curvature_as_corroboration():
    out = layer_2(mapping_is_fixed=False)
    assert "the same sign test restated" in out["u_double_prime_is_not_a_second_route"]


# ---- convention dependence ----------------------------------------------
def test_reversing_the_s_g_ruling_flips_only_the_induced_channels():
    out = convention_dependence(layer_1a())
    reversed_signs = out["if_the_s_G_ruling_were_reversed"][
        "induced_coefficients_become"
    ]
    assert reversed_signs["scalar_singlet_direct"]["changed"] is False
    for name in ("induced_V_singlet", "induced_A_singlet"):
        assert reversed_signs[name]["changed"] is True
        assert _expr(reversed_signs[name]["normalisation_L"]) == +G / 4


# ---- derivation (b): the executability determination --------------------
def test_charge_conjugation_is_absent_from_the_frozen_material():
    out = diquark_executability()
    assert out["step_1_C_fixed_by_the_frozen_material"] is False
    assert all(count == 0 for count in out["step_1_marker_counts"].values())


def test_defining_relation_fixes_c_up_to_one_complex_scalar():
    """C gamma_mu^T C^-1 = -gamma_mu, solved as a linear system."""
    out = diquark_executability()
    assert out["step_2_solution_space_complex_dimension"] == 1
    assert out["step_2_C_unique_up_to_a_nonzero_scalar"] is True
    checks = out["step_2_checks"]
    assert checks["defining_relation_holds_for_all_mu"] is True
    assert checks["antisymmetric_C_transpose_equals_minus_C"] is True
    assert checks["unitary_C_dagger_C_is_identity"] is True


def test_the_residual_scalar_is_not_the_obstruction():
    out = diquark_executability()
    assert out["step_3_channel_character_invariant_under_residual_scalar"] is True


def test_step_0_is_the_obstruction_and_the_verdict_is_reached_at_step_4():
    out = diquark_executability()
    assert out["step_0_all_pp_operator_definitions_fixed"] is False
    assert out["step_4_verdict"] == "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY"
    assert "C is NOT the obstruction" in out["step_4_dependence_that_forces_it"]


def test_no_convention_was_selected_and_no_projection_built():
    out = diquark_executability()
    assert out["no_C_selected"] is True
    assert out["no_pp_projection_constructed"] is True


# ---- the artifact --------------------------------------------------------
def test_results_artifact_keeps_the_three_layers_separate():
    payload = json.loads(RESULTS.read_text(encoding="utf-8"))
    assert payload["layer_1a"]["channels"]["induced_V_singlet"]["sign"] == -1
    assert payload["layer_1b"]["verdict"] == (
        "REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL"
    )
    assert payload["layer_2"]["verdict"] == (
        "ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL"
    )
    assert payload["gate_status"] == "P2-PHASE-01 remains PROPOSED"
    for value in payload["exclusions_confirmed"].values():
        assert value == "NOT READ"


def test_recorded_inputs_exclude_the_three_prohibited_sources():
    payload = json.loads(RESULTS.read_text(encoding="utf-8"))
    inputs = payload["repository_inputs_read"]
    assert inputs == cc.repository_inputs()
    forbidden = ("BETAV-CIRC", "3.2(5)", "Finding 5", "finding_5")
    for path in inputs:
        assert not any(token in path for token in forbidden)
        assert (ROOT / path).exists()
