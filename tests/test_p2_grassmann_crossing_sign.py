"""Tests for the `P2-CHANNEL-FREEZE-01` Grassmann crossing-sign derivation.

These test the three things this task is actually about: the explicit
exchange sign, the chiral decomposition, and the freeze checker's
invariance under flipping the declared sign.

They deliberately do NOT assert that the frozen matrix equals itself, which
would test nothing here. They also assert that the storage verdict is not
inferred from the numerical equality of an unsigned reconstruction with
`matrix_rational` — an inference this task is required not to make.
"""

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from p2_grassmann_crossing_sign import (  # noqa: E402
    DECLARED_CROSSING_SIGN,
    FINAL_ORDER,
    START_ORDER,
    checker_sign_invariance,
    chiral_decomposition,
    explicit_anticommutation,
    note_route,
    permutation_parity,
    storage_convention_test,
)

RESULTS = (ROOT / "results/P2-CHANNEL-FREEZE/grassmann-crossing-sign"
           / "crossing_sign.json")


# ---- the explicit exchange sign -----------------------------------------
def test_explicit_anticommutation_reaches_the_normative_final_order():
    _, _, seq = explicit_anticommutation()
    assert seq == FINAL_ORDER
    assert START_ORDER == ["psibar_1", "psi_2", "psibar_3", "psi_4"]
    assert FINAL_ORDER == ["psibar_1", "psi_4", "psibar_3", "psi_2"]


def test_every_step_is_an_adjacent_transposition_contributing_minus_one():
    _, steps, _ = explicit_anticommutation()
    assert steps, "the calculation must show its steps"
    for step in steps:
        assert step["sign_of_this_anticommutation"] == -1


def test_grassmann_exchange_sign_is_minus_one():
    sign, _, _ = explicit_anticommutation()
    assert sign == -1


def test_all_four_routes_agree_on_the_sign():
    """Two explicit decompositions and two parity computations."""
    explicit, _, _ = explicit_anticommutation()
    noted, _, note_seq = note_route()
    parity = permutation_parity()
    assert note_seq == FINAL_ORDER
    assert explicit == noted
    assert explicit == parity["sign_from_inversions"]
    assert explicit == parity["sign_from_transpositions"]


def test_permutation_is_the_single_transposition_of_the_two_psi_legs():
    parity = permutation_parity()
    assert parity["permutation_one_line"] == [0, 3, 2, 1]
    assert parity["transposition_count"] == 1
    assert parity["nontrivial_cycles"] == [[1, 3]]
    assert parity["inversions"] % 2 == 1, "an odd permutation"


def test_sign_matches_the_declared_freeze_value():
    sign, _, _ = explicit_anticommutation()
    assert sign == DECLARED_CROSSING_SIGN == -1


# ---- the storage question ------------------------------------------------
def test_storage_convention_is_reported_unresolved_with_evidence():
    out = storage_convention_test()
    assert out["verdict"] == "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY"
    assert out["defining_kernel_equation_present"] is False
    assert all(count == 0
               for count in out["kernel_equation_markers_found"].values())
    # the frozen material carries no equation, only these keys
    assert out["freeze_json_top_level_keys"] == [
        "basis_order", "basis_elements", "conventions", "matrix_rational"]
    assert out["standalone_artifact_keys"] == ["basis_order", "matrix_rational"]
    assert "section C" in out["reasoning"]


def test_storage_verdict_is_not_inferred_from_numerical_equality():
    """The forbidden inference must be explicitly disclaimed, not relied on."""
    out = storage_convention_test()
    assert "NOT used here" in out["explicitly_not_used_as_evidence"]
    assert "consistent with either convention" in \
        out["explicitly_not_used_as_evidence"]


# ---- the chiral decomposition -------------------------------------------
def test_projector_convention_is_the_frozen_one_and_is_consistent():
    checks = chiral_decomposition()["projector_convention"]
    assert checks["P_L"] == "(Id4 - gamma5)/2"
    assert checks["P_R"] == "(Id4 + gamma5)/2"
    for name, value in checks["checks"].items():
        assert value is True, name


def test_direct_scalar_channel_is_purely_left_right():
    direct = chiral_decomposition()["direct_scalar_channel"]
    assert sp.sympify(direct["LL"]) == 0
    assert sp.sympify(direct["RR"]) == 0
    assert sp.sympify(direct["LR"]) == sp.sympify(direct["RL"]) == 2
    assert direct["purely_left_right"] is True


def test_exchanged_current_channel_is_purely_left_right():
    exchanged = chiral_decomposition()["exchanged_current_channel"]
    assert sp.sympify(exchanged["LL"]) == 0
    assert sp.sympify(exchanged["RR"]) == 0
    assert sp.sympify(exchanged["LR"]) == sp.sympify(exchanged["RL"]) == 2
    assert exchanged["purely_left_right"] is True


def test_chiral_check_is_sign_blind():
    """Multiplying the interaction by -1 scales all four coefficients."""
    sl, sr = sp.symbols("S_L S_R")
    direct = sp.expand((sl + sr) ** 2 - (sr - sl) ** 2)
    assert sp.expand(-direct) == sp.expand(-4 * sl * sr)
    # the LL and RR coefficients stay zero under any overall sign
    assert sp.expand(-direct).coeff(sl, 2).coeff(sr, 0) == 0
    assert sp.expand(-direct).coeff(sr, 2).coeff(sl, 0) == 0


# ---- the checker's sign invariance ---------------------------------------
def test_checker_expression_is_invariant_under_flipping_the_sign():
    out = checker_sign_invariance()
    assert out["output_for_sign_minus_1"] == out["output_for_sign_plus_1"]
    assert out["invariant_under_sign_flip"] is True


def test_mutation_suite_does_not_cover_the_crossing_sign():
    """Records the known gap; the missing mutation is a separate task."""
    out = checker_sign_invariance()
    assert out["mutation_suite_covers_the_field"] is False
    assert out["checker_modified_by_this_task"] is False


# ---- the artifact --------------------------------------------------------
def test_results_artifact_records_both_results_separately():
    payload = json.loads(RESULTS.read_text(encoding="utf-8"))
    a3a = payload["A3a_grassmann_exchange_sign"]
    a3b = payload["A3b_storage_convention"]
    assert a3a["s_G"] == -1
    assert a3a["s_G_equals_declared_value"] is True
    assert a3a["all_routes_agree"] is True
    assert a3b["verdict"] == "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY"
    consequence = payload["consequence_for_P2_PHASE_01"]
    assert "contingent" in consequence["statement"]
    assert "NOT flipped" in consequence["statement"]
