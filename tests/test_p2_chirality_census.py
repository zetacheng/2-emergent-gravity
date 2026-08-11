"""Tests for the `P2-PHASE-01` chirality census.

Everything is computed here rather than hard-coded, except where a test exists
specifically to pin what the artifact records.

    Step A    the factorisation identity, with and without the i
    Step B/C1 the particle-hole classification, all four entries
    Step C2   the particle-particle classification, all four entries, and that
              it is INVERTED relative to C1 in field labels
    Step D    the criterion's prediction against the computed support

The LL/RR-restriction check is deliberately NOT tested: the specification
explains why it is close to tautological, and a test of it would lock in a proxy.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/p2_chirality_census.py"
RESULTS = ROOT / "results/P2-PHASE-01/chirality-census/census.json"

FAMILIES = ("S", "P", "V", "A", "T")
OPPOSITE_PH = ("S", "P", "T")
SAME_PH = ("V", "A")


def _module():
    spec = importlib.util.spec_from_file_location("p2_chirality_census", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _artifact() -> dict:
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------- Step A: factorise ----
def test_frozen_factorisation_is_exact() -> None:
    """S^2 + P^2 = 2[P_R(x)P_L + P_L(x)P_R], recomputed."""
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        g = factory()
        g5 = module.gamma5(g)
        identity = np.eye(4, dtype=complex)
        p_l, p_r = module.projectors(g)
        source = module.kron4(identity, identity) + module.kron4(1j * g5, 1j * g5)
        factorised = 2 * (module.kron4(p_r, p_l) + module.kron4(p_l, p_r))
        assert np.max(np.abs(source - factorised)) < 1e-12


def test_no_i_factorisation_is_exact_and_is_the_other_pairing() -> None:
    """Without the i the source becomes the DOUBLED census, not the mixed one."""
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        g = factory()
        g5 = module.gamma5(g)
        identity = np.eye(4, dtype=complex)
        p_l, p_r = module.projectors(g)
        source = module.kron4(identity, identity) + module.kron4(g5, g5)
        doubled = 2 * (module.kron4(p_r, p_r) + module.kron4(p_l, p_l))
        mixed = 2 * (module.kron4(p_r, p_l) + module.kron4(p_l, p_r))
        assert np.max(np.abs(source - doubled)) < 1e-12
        assert np.max(np.abs(source - mixed)) > 1e-9


def test_the_factor_four_form_is_an_operator_not_a_tensor_identity() -> None:
    """4 P_R(x)P_L alone does NOT reproduce the source; the symmetrised form does."""
    module = _module()
    g = module.gammas_frozen_factory()
    g5 = module.gamma5(g)
    identity = np.eye(4, dtype=complex)
    p_l, p_r = module.projectors(g)
    source = module.kron4(identity, identity) + module.kron4(1j * g5, 1j * g5)
    assert np.max(np.abs(source - 4 * module.kron4(p_r, p_l))) > 1e-9


# ----------------------------------------- Step B / C1: particle-hole ------
def test_particle_hole_classification_all_four_entries() -> None:
    """S, P, T opposite-chirality; V, A same-chirality.  All four entries."""
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        tables = module.chirality_tables(factory())["C1_particle_hole"]
        for family in OPPOSITE_PH:
            entry = tables[family]["vanishes"]
            assert entry["P_L_G_P_R"] is True and entry["P_R_G_P_L"] is True, family
            assert entry["P_L_G_P_L"] is False and entry["P_R_G_P_R"] is False, family
            assert tables[family]["type"] == "OPPOSITE-chirality", family
        for family in SAME_PH:
            entry = tables[family]["vanishes"]
            assert entry["P_L_G_P_L"] is True and entry["P_R_G_P_R"] is True, family
            assert entry["P_L_G_P_R"] is False and entry["P_R_G_P_L"] is False, family
            assert tables[family]["type"] == "SAME-chirality", family


def test_the_bar_flip_is_what_the_ph_translation_depends_on() -> None:
    """psibar_L = psibar P_R, so psibar_L Gamma psi_R corresponds to P_R Gamma P_R.

    Placing the projector the other way inverts the whole classification, which is
    the error the census exists to rule out.
    """
    module = _module()
    g = module.gammas_frozen_factory()
    p_l, p_r = module.projectors(g)
    scalar = np.eye(4, dtype=complex)
    vector = g[0]
    # opposite-chirality bilinear psibar_L Gamma psi_R  <->  P_R Gamma P_R
    assert np.max(np.abs(p_r @ scalar @ p_r)) > 1e-9
    assert np.max(np.abs(p_r @ vector @ p_r)) < 1e-9
    # same-chirality bilinear psibar_L Gamma psi_L  <->  P_R Gamma P_L
    assert np.max(np.abs(p_r @ scalar @ p_l)) < 1e-9
    assert np.max(np.abs(p_r @ vector @ p_l)) > 1e-9


# ------------------------------------ Step C2: particle-particle -----------
def test_particle_particle_classification_all_four_entries() -> None:
    """S, P, T same-chirality qq; V, A opposite-chirality qq.  All four entries."""
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        tables = module.chirality_tables(factory())["C2_particle_particle"]
        for family in OPPOSITE_PH:
            entry = tables[family]["vanishes"]
            assert entry["LR"] is True and entry["RL"] is True, family
            assert entry["LL"] is False and entry["RR"] is False, family
            assert tables[family]["type"] == "SAME-chirality qq", family
        for family in SAME_PH:
            entry = tables[family]["vanishes"]
            assert entry["LL"] is True and entry["RR"] is True, family
            assert entry["LR"] is False and entry["RL"] is False, family
            assert tables[family]["type"] == "OPPOSITE-chirality qq", family


def test_the_two_classifications_are_inverted_in_field_labels() -> None:
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        tables = module.chirality_tables(factory())
        assert tables["classifications_are_inverted_in_field_labels"] is True
        for family in FAMILIES:
            ph = tables["C1_particle_hole"][family]["type"]
            pp = tables["C2_particle_particle"][family]["type"]
            assert (ph == "OPPOSITE-chirality") == (pp == "SAME-chirality qq"), family


def test_the_inversion_is_the_bar_flip_not_a_different_projector_pattern() -> None:
    """The two projector tables have IDENTICAL non-zero patterns.

    This is the refinement the derivation note records: the inversion lives in the
    translation to field labels, not in the algebra of the projector entries.
    """
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        tables = module.chirality_tables(factory())
        assert tables["projector_index_patterns_are_identical"] is True


def test_the_C_relation_is_what_prevents_a_second_flip() -> None:
    """C g5^T C^-1 = +g5, hence P_X^T C^-1 = C^-1 P_X: no flip on the pp side."""
    module = _module()
    for factory in module.REPRESENTATIONS.values():
        g = factory()
        matrix_c, dimension = module.conjugation_matrix(g)
        assert dimension == 1
        inverse = np.linalg.inv(matrix_c)
        assert np.allclose(matrix_c @ module.gamma5(g).T @ inverse, module.gamma5(g),
                           atol=1e-9)
        for projector in module.projectors(g):
            assert np.allclose(projector.T @ inverse, inverse @ projector, atol=1e-9)


# ------------------------------------------------- representation check ----
def test_the_tables_are_representation_independent() -> None:
    module = _module()
    names = list(module.REPRESENTATIONS)
    first = module.chirality_tables(module.REPRESENTATIONS[names[0]]())
    second = module.chirality_tables(module.REPRESENTATIONS[names[1]]())
    assert first["C1_particle_hole"] == second["C1_particle_hole"]
    assert first["C2_particle_particle"] == second["C2_particle_particle"]


def test_the_two_representations_are_genuinely_different_matrices() -> None:
    """Otherwise the representation-independence check would be vacuous."""
    module = _module()
    first = module.gammas_frozen_factory()
    second = module.gammas_independent()
    assert any(not np.allclose(a, b, atol=1e-9) for a, b in zip(first, second))


# ------------------------------------------------------- Step D: predict ---
def test_the_criterion_predicts_the_support_in_all_three_cases() -> None:
    """Recomputed from the frozen Fierz matrix, then scored against the criterion."""
    module = _module()
    block = json.loads(
        [
            line
            for line in module.FREEZE.read_text(encoding="utf-8").splitlines()
            if line.startswith('{"basis_order"')
        ][0]
    )
    fierz = sp.Matrix(
        [[sp.Rational(e) for e in row] for row in block["matrix_rational"]]
    )
    order = block["basis_order"]
    for key, row in module.SOURCE_ROWS.items():
        exchanged = sp.Matrix([row]) * fierz
        computed = sorted(
            order[i] for i in range(len(order))
            if sp.simplify(module.S_G * exchanged[i]) != 0
        )
        predicted = sorted(module.PREDICTIONS[key]["predicted_nonzero"])
        assert computed == predicted, (key, computed, predicted)


def test_the_predictions_were_recorded_before_the_computation() -> None:
    """The predictions live in the derivation note, an earlier commit."""
    note = ROOT / "derivations/P2-PHASE-01_chirality_census.md"
    text = note.read_text(encoding="utf-8")
    assert "PREDICT: `V` and `A` non-zero" in text
    assert "PREDICT: `S`, `P`, `T` non-zero" in text
    assert "PREDICT: all five families non-zero" in text
    assert _artifact()["step_D_falsification"][
        "prediction_recorded_before_computation"
    ] is True


def test_the_no_i_case_moves_the_support_and_is_not_a_repeat() -> None:
    """D1 must differ from D0, or the falsification test would be empty."""
    cases = _artifact()["step_D_falsification"]["cases"]
    frozen_nz = cases["D0_frozen"]["computed_nonzero"]
    no_i_nz = cases["D1_no_i"]["computed_nonzero"]
    assert frozen_nz != no_i_nz
    assert set(cases["D0_frozen"]["computed_nonzero"]) == {"V", "A"}
    assert set(cases["D1_no_i"]["computed_nonzero"]) == {"S", "P", "T"}


def test_the_chosen_case_exercises_the_no_exclusion_branch() -> None:
    """D4 predicts NO family vanishes; four of five could have."""
    case = _artifact()["step_D_falsification"]["cases"]["D4_chosen"]
    assert case["predicted_zero"] == []
    assert sorted(case["computed_nonzero"]) == sorted(FAMILIES)
    assert case["prediction_correct"] is True


# --------------------------------------------------- authority and scope ---
def test_the_freeze_still_states_the_load_bearing_conventions() -> None:
    module = _module()
    frozen = module.frozen_conventions()
    assert all(count > 0 for count in frozen["occurrence_counts"].values())
    assert "raise AssertionError" in SCRIPT.read_text(encoding="utf-8")


def test_the_census_agrees_with_the_pinned_particle_hole_result() -> None:
    comparison = _artifact()["comparison_with_the_pinned_particle_hole_result"]
    assert comparison["agree"] is True
    assert sorted(comparison["pinned_vanishing_families"]) == ["P", "S", "T"]


def test_no_pp_decomposition_and_no_slot_map() -> None:
    tables = _artifact()["step_BC_chirality_tables"]["frozen_factory"]
    assert tables["no_pp_coefficient_decomposition_performed"] is True
    assert tables["no_slot_map_chosen"] is True
    assert _artifact()["step_D_falsification"]["channel_tested"] == (
        "particle-hole ONLY"
    )


def test_scope_limits_hold() -> None:
    scope = _artifact()["scope_limits"]
    assert scope["gate_status"] == "P2-PHASE-01 remains PROPOSED"
    assert scope["conventions_frozen_by_this_task"] == []
    assert scope["new_programme_coefficient_or_channel_character_result"] is False
    assert scope["census_does_not_explain_the_inter_channel_sign"] is True
    assert set(scope["branches_not_read"]) == {
        "gate/p2-diquark-both-eta",
        "gate/p2-diquark-adjudication",
    }


def test_the_argument_states_what_it_does_not_explain() -> None:
    missing = _artifact()["step_E_not_explained"]["does_not_explain"]
    assert any("inter-channel sign" in item for item in missing)
    assert any("magnitude" in item for item in missing)


def test_artifact_matches_a_fresh_run() -> None:
    module = _module()
    assert module.build() == _artifact()
