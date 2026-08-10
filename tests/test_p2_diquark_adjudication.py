"""Tests for the `P2-PHASE-01` diquark decomposition adjudication.

The claims under test are the ones the adjudication actually rests on:

    the two gamma representations are equivalent, so the representation
      difference cannot be the cause
    the scalar canonical tensors agree and the pseudoscalar ones differ by
      exactly -1
    the particle-particle slot map is identical in the two methods
    the design matrices differ on the A and T columns only, by a factor of i
    restoring the two frozen conventions reproduces method A exactly
    the frozen material fixes both disputed conventions

Each is recomputed here rather than read back from the artifact, except where a
test exists specifically to pin what the artifact records.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/p2_diquark_adjudication.py"
RESULTS = ROOT / "results/P2-PHASE-01/diquark-adjudication/adjudication.json"

FAMILIES = ("S", "P", "V", "A", "T")
METHOD_A_SUM = {"S": 0.0, "P": 0.0, "V": 0.5, "A": -0.5, "T": 0.0}
METHOD_B_SUM = {"S": -0.5, "P": -0.5, "V": 0.0, "A": 0.0, "T": -0.5}


def _module():
    spec = importlib.util.spec_from_file_location("p2_diquark_adjudication", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _artifact() -> dict:
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def _matrices(module, which: str):
    """Return (gammas, C) for method A or method B, C from the null space."""
    gammas = module.gammas_A() if which == "A" else module.gammas_B()
    _, raw = module.conjugation_null_space(gammas)
    if which == "A":
        reference = np.array(
            [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=complex
        )
    else:
        reference = gammas[0] @ gammas[2]
    return gammas, module.normalise_C(raw, reference)


# ------------------------------------------------------ L1: the matrices ---
def test_both_gamma_sets_are_valid_clifford_representations() -> None:
    module = _module()
    for which in ("A", "B"):
        gammas = module.gammas_A() if which == "A" else module.gammas_B()
        checks = module.clifford_checks(gammas)
        assert all(checks.values()), (which, checks)


def test_C_comes_from_a_null_space_of_dimension_one() -> None:
    """A basis search is a proxy; the null space is computed."""
    module = _module()
    for which in ("A", "B"):
        gammas = module.gammas_A() if which == "A" else module.gammas_B()
        info, _ = module.conjugation_null_space(gammas)
        assert info["null_space_dimension_computed"] == 1, which
        assert info["system_shape"] == [64, 16], which


def test_C_satisfies_its_defining_relation_and_is_antisymmetric() -> None:
    module = _module()
    for which in ("A", "B"):
        gammas, matrix_c = _matrices(module, which)
        assert np.allclose(matrix_c.T, -matrix_c, atol=1e-9), which
        inverse = np.linalg.inv(matrix_c)
        for gamma in gammas:
            assert np.allclose(
                matrix_c @ gamma.T @ inverse, -gamma, atol=1e-9
            ), which


def test_method_B_C_is_g0_g2() -> None:
    module = _module()
    gammas, matrix_c = _matrices(module, "B")
    assert np.allclose(matrix_c, gammas[0] @ gammas[2], atol=1e-9)


def test_the_two_representations_are_equivalent() -> None:
    """If they were not, the representation could be the cause; it is not."""
    module = _module()
    info, transform = module.similarity_transform(module.gammas_B(), module.gammas_A())
    assert info["null_space_dimension"] == 1
    assert info["maps_every_gamma"] is True
    assert info["maps_gamma5"] is True
    assert abs(np.linalg.det(transform)) > 1e-9


# ------------------------------------------- L2: the canonical tensors -----
def test_scalar_canonical_tensors_agree_and_pseudoscalar_differ_by_minus_one() -> None:
    """Compared SEPARATELY; a summed comparison would hide the scalar agreement."""
    module = _module()
    ga, gb = module.gammas_A(), module.gammas_B()
    _, transform = module.similarity_transform(gb, ga)

    t_a_s = module.target_vector(np.eye(4, dtype=complex))
    t_b_s = module.transform_tensor(
        module.target_vector(np.eye(4, dtype=complex)), transform
    )
    assert np.allclose(t_a_s, t_b_s, atol=1e-9)

    t_a_p = module.target_vector(1j * module.gamma5(ga))
    t_b_p = module.transform_tensor(module.target_vector(module.gamma5(gb)), transform)
    assert not np.allclose(t_a_p, t_b_p, atol=1e-9)
    assert np.allclose(t_a_p, -t_b_p, atol=1e-9)


def test_the_factor_is_exactly_i_squared_and_not_something_else() -> None:
    """(i*g5)_{ab}(i*g5)_{cd} = -(g5)_{ab}(g5)_{cd}, so the factor is -1 exactly."""
    module = _module()
    g5 = module.gamma5(module.gammas_B())
    with_i = module.target_vector(1j * g5)
    without = module.target_vector(g5)
    assert np.allclose(with_i, -without, atol=1e-12)
    assert not np.allclose(with_i, without, atol=1e-9)


# ------------------------------------------------- L3: the slot map --------
def test_the_pp_slot_map_is_identical_in_both_methods() -> None:
    """The load-bearing negative result: this is NOT an ordering divergence."""
    artifact = _artifact()
    layer = artifact["layer_comparison"]["L3"]
    assert layer["verdict"] == "IDENTICAL"
    assert layer["row_index_pair"].startswith("(a,c)")
    assert layer["column_index_pair"].startswith("(b,d)")
    assert layer["grassmann_sign_applied_before_projection"] == {
        "A": False,
        "B": False,
    }
    assert layer["eta_or_s_pp_or_nu_applied_before_projection"] == {
        "A": False,
        "B": False,
    }


def test_target_vector_uses_the_stated_index_positions() -> None:
    """t is flattened (a,c,b,d) with a,c the psibar pair and b,d the psi pair."""
    module = _module()
    operator = np.arange(16, dtype=complex).reshape(4, 4)
    flat = module.target_vector(operator).reshape(4, 4, 4, 4)
    for a in range(4):
        for c in range(4):
            for b in range(4):
                for d in range(4):
                    assert flat[a, c, b, d] == operator[a, b] * operator[c, d]


# ------------------------------------------------ L5: the design matrix ----
def test_design_matrices_are_full_rank_so_f_is_unique() -> None:
    module = _module()
    for which, with_i in (("A", True), ("B", False)):
        gammas, matrix_c = _matrices(module, which)
        matrix, _ = module.design_matrix(module.family_basis(gammas, with_i), matrix_c)
        assert np.linalg.matrix_rank(matrix, tol=1e-9) == 256, which


def test_design_matrices_differ_on_A_and_T_only_by_a_factor_of_i() -> None:
    module = _module()
    ga, gb = module.gammas_A(), module.gammas_B()
    _, transform = module.similarity_transform(gb, ga)
    inverse = np.linalg.inv(transform)
    basis_a = module.family_basis(ga, True)
    basis_b = module.family_basis(gb, False)
    expected = {"S": 1, "P": 1, "V": 1, "A": 1j, "T": 1j}
    for family in FAMILIES:
        element_a = next(e for f, e in basis_a if f == family)
        element_b = transform @ next(e for f, e in basis_b if f == family) @ inverse
        assert np.allclose(element_a, expected[family] * element_b, atol=1e-9), family


def test_the_i_flips_only_the_diagonal_A_and_T_coefficients() -> None:
    """f_pp carries Gamma_p twice, so a factor i on Gamma_p gives i^-2 = -1."""
    module = _module()
    gammas, matrix_c = _matrices(module, "B")
    target = module.target_vector(np.eye(4, dtype=complex))
    without = module.design_matrix(module.family_basis(gammas, False), matrix_c)
    with_i = module.design_matrix(module.family_basis(gammas, True), matrix_c)
    f_without = module.extract(*without, target)["per_component_by_family"]
    f_with = module.extract(*with_i, target)["per_component_by_family"]
    for family in ("S", "P", "V"):
        assert abs(f_without[family] - f_with[family]) < 1e-9, family
    for family in ("A", "T"):
        assert abs(f_without[family] + f_with[family]) < 1e-9, family


# --------------------------------------------------------- the ablation ----
def test_restoring_both_frozen_conventions_reproduces_method_A() -> None:
    """Method B's own machinery, with the frozen conventions, gives method A."""
    artifact = _artifact()
    ablation = artifact["ablation"]
    assert ablation["row_4_equals_method_A"] is True
    assert ablation["row_5_equals_method_A"] is True
    assert ablation["row_1_equals_method_B"] is True
    assert ablation["row_6_equals_method_B"] is True
    assert ablation["nothing_left_unaccounted"] is True


def test_the_representation_is_not_causal() -> None:
    artifact = _artifact()
    ablation = artifact["ablation"]
    assert ablation["representation_is_not_causal"] is True
    rows = ablation["rows"]
    assert rows[3]["sum"] == rows[4]["sum"]
    assert rows[0]["sum"] == rows[5]["sum"]


def test_the_two_reported_family_sums_are_the_ones_under_adjudication() -> None:
    artifact = _artifact()
    layer = artifact["layer_comparison"]["L6"]
    assert layer["method_A_sum"] == METHOD_A_SUM
    assert layer["method_B_sum"] == METHOD_B_SUM


# ----------------------------------------- the frozen material's authority --
def test_the_freeze_fixes_both_disputed_conventions() -> None:
    """Exact literal substring, no normalisation; each occurs at least once."""
    module = _module()
    frozen = module.frozen_conventions()
    assert all(count > 0 for count in frozen["occurrence_counts"].values())
    assert "i*gamma5" in frozen["conclusion"] or "i*gamma5" in str(frozen["literals"])
    text = (ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md").read_text(
        encoding="utf-8"
    )
    assert "(iγ₅)_{αβ}" in text
    assert "A=I*gamma(mu)*gamma5" in text


def test_frozen_conventions_check_stops_if_the_freeze_changes() -> None:
    """The quotations are load-bearing, so their absence must raise."""
    source = SCRIPT.read_text(encoding="utf-8")
    assert "the freeze no longer fixes" in source
    assert "raise AssertionError" in source


# ------------------------------------------- method A: no defect asserted ---
def test_method_A_reproduces_its_committed_artifact_and_is_deterministic() -> None:
    artifact = _artifact()
    run = artifact["method_A_reproduction"]
    assert run["script_modified"] is False
    assert run["deterministic_over_the_complete_payload"] is True
    assert run["no_field_ignored"] is True
    assert run["reproduces_its_committed_artifact"] is True
    assert run["per_component_sum"] == run["recorded_per_component_sum"]


def test_method_A_trace_formula_agrees_with_least_squares() -> None:
    artifact = _artifact()
    consistency = artifact["method_A_internal_consistency"]
    assert consistency["trace_formula_agrees_with_least_squares"] is True
    for term in ("scalar", "pseudoscalar"):
        result = consistency["least_squares_on_method_A_own_system"][term]
        assert result["rank"] == 256
        assert result["max_reconstruction_residual"] < 1e-9
        assert result["max_abs_off_family_coefficient"] < 1e-9


def test_no_implementation_defect_is_asserted() -> None:
    artifact = _artifact()
    case = artifact["case_decision"]
    assert case["implementation_defect_case_applies"] is False
    assert case["ordering_index_map_case_applies"] is False
    assert artifact["scope_limits"]["defects_repaired"] == []


# --------------------------------------------------------- case and scope --
def test_the_case_is_the_canonical_construction_and_the_first_layer_is_L2() -> None:
    artifact = _artifact()
    assert artifact["layer_comparison"]["first_diverging_layer"] == "L2"
    assert artifact["case_decision"]["case"].startswith("canonical construction")
    assert (
        artifact["case_decision"]["scalar_tensors_compared_separately"]["identical"]
        is True
    )
    assert (
        artifact["case_decision"]["pseudoscalar_tensors_compared_separately"][
            "identical"
        ]
        is False
    )


def test_the_independence_claim_is_answered_without_overreach() -> None:
    artifact = _artifact()
    claim = artifact["independence_claim"]
    assert claim["not_contradicted"] is True
    assert claim["not_further_supported"] is True
    assert "harmless" in claim["what_is_NOT_concluded"]


def test_nothing_frozen_no_channel_character_branch_untouched() -> None:
    artifact = _artifact()
    scope = artifact["scope_limits"]
    assert scope["gate_status"] == "P2-PHASE-01 remains PROPOSED"
    assert scope["conventions_frozen_by_this_adjudication"] == []
    assert scope["channel_character_result_produced"] is False
    assert scope["branch_under_adjudication"]["modified"] is False
    assert scope["branch_under_adjudication"]["integrated"] is False
    assert scope["still_unresolved"]


def test_commit_pinned_inputs_are_measured_not_checked() -> None:
    """No expected digest is supplied for the three branch artifacts."""
    artifact = _artifact()
    pinned = artifact["pinned_inputs"]
    for entry in pinned["commit_pinned_measured"].values():
        assert entry["exists_at_branch_commit"] is True
        assert len(entry["measured_sha256"]) == 64
        assert "expected" not in entry
    for entry in pinned["digest_pinned_checked"].values():
        assert entry["match"] is True
