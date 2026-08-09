"""Tests for `P2-PHASE-01` Layer 1b and Layer 2.

These lock the FULL mapping for all three channels, not only the scalar
control:

    c_S > 0  =>  g_S > 0  =>  ATTRACTIVE
    c_V < 0  =>  g_V < 0  =>  REPULSIVE
    c_A < 0  =>  g_A < 0  =>  REPULSIVE

plus the gating Layer-1a control.

`g = 2c` is tested as something the implementation *computes from a
ruling it reads*, not as a constant.  The mutation tests replace the
`DECISION_LOG.md` text with a reversed mapping and with a missing entry,
and require the outputs to move and the run to fail respectively.  A
recomputation whose outputs survive the removal of the ruling it cites
never consumed it.

They assert no bound-state conclusion, select no Hubbard-Stratonovich
channel, and freeze no diquark convention.
"""

import json
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import p2_channel_character_layers as ccl  # noqa: E402

RESULTS = ROOT / "results/P2-PHASE-01/channel-character-layers/layers.json"
G, N = sp.symbols("G N", positive=True)


def _expr(text):
    return sp.sympify(text, locals={"G": G, "N": N})


@pytest.fixture(scope="module")
def artifact():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def _use_log(tmp_path, monkeypatch, decision_log_text):
    """Point the module at a mutated `DECISION_LOG.md`."""
    log = tmp_path / "DECISION_LOG.md"
    log.write_text(decision_log_text, encoding="utf-8")
    monkeypatch.setattr(ccl, "DECISION_LOG", log)


def _run_isolated(tmp_path, monkeypatch, decision_log_text=None):
    """Run `main()` with the artifact redirected, optionally mutating the log."""
    monkeypatch.setattr(ccl, "OUT", tmp_path / "layers.json")
    if decision_log_text is not None:
        _use_log(tmp_path, monkeypatch, decision_log_text)
    return ccl.main()


def _layers_from_log(tmp_path, monkeypatch, decision_log_text):
    """Compute Layers 1b and 2 under a mutated log, past `main()`'s gate.

    `main()` stops when the scalar control fails, which is what it is for.
    These helpers exercise the layers themselves, so the effect of the
    mutation can be observed rather than only its rejection.
    """
    _use_log(tmp_path, monkeypatch, decision_log_text)
    mapping = ccl.exponent_mapping_factor()
    rule = ccl.label_rule()
    control = ccl.layer_1a_control()
    assert control["control_passes"] is True
    l1b = ccl.layer_1b(ccl.coefficients_from_control(control), mapping)
    return l1b, ccl.layer_2(l1b, rule)


# ---- the Layer 1a control, first: everything else depends on it ---------
def test_layer_1a_control_passes_against_the_pinned_artifact():
    control = ccl.layer_1a_control()
    assert control["control_passes"] is True
    for name in ccl.CHANNELS:
        entry = control["comparisons"][name]
        assert entry["normalisation_L"]["equal"] is True
        assert entry["normalisation_P"]["equal"] is True
        assert entry["sign"]["equal"] is True
        assert _expr(entry["normalisation_L"]["symbolic_difference"]) == 0
        assert _expr(entry["normalisation_P"]["symbolic_difference"]) == 0


def test_layer_1a_control_reproduces_the_pinned_coefficients():
    control = ccl.layer_1a_control()
    expected = {
        "scalar_singlet_direct": (G / (2 * N), G / N**2),
        "induced_V_singlet": (-G / 4, -G / (2 * N)),
        "induced_A_singlet": (-G / 4, -G / (2 * N)),
    }
    for name, (c_l, c_p) in expected.items():
        entry = control["comparisons"][name]
        assert _expr(entry["normalisation_L"]["recomputed"]) == c_l
        assert _expr(entry["normalisation_P"]["recomputed"]) == c_p


def test_the_pinned_inputs_still_match_their_digests():
    observed = ccl.verify_pins()
    assert observed == ccl.PINS


# ---- the full mapping, channel by channel ------------------------------
def test_scalar_channel_positive_c_gives_positive_g_and_attractive(artifact):
    entry = artifact["layer_1b"]["channels"]["scalar_singlet_direct"]
    assert sp.sign(_expr(entry["c_in_normalisation_L"])) == 1
    assert sp.sign(_expr(entry["c_in_normalisation_P"])) == 1
    assert entry["sign_of_g"] == 1
    assert entry["real_linear_HS_field_admissible"] is True
    assert artifact["layer_2"]["channels"]["scalar_singlet_direct"]["label"] == (
        "ATTRACTIVE"
    )


def test_induced_v_channel_negative_c_gives_negative_g_and_repulsive(artifact):
    entry = artifact["layer_1b"]["channels"]["induced_V_singlet"]
    assert sp.sign(_expr(entry["c_in_normalisation_L"])) == -1
    assert sp.sign(_expr(entry["c_in_normalisation_P"])) == -1
    assert entry["sign_of_g"] == -1
    assert entry["real_linear_HS_field_admissible"] is False
    assert artifact["layer_2"]["channels"]["induced_V_singlet"]["label"] == "REPULSIVE"


def test_induced_a_channel_negative_c_gives_negative_g_and_repulsive(artifact):
    entry = artifact["layer_1b"]["channels"]["induced_A_singlet"]
    assert sp.sign(_expr(entry["c_in_normalisation_L"])) == -1
    assert sp.sign(_expr(entry["c_in_normalisation_P"])) == -1
    assert entry["sign_of_g"] == -1
    assert entry["real_linear_HS_field_admissible"] is False
    assert artifact["layer_2"]["channels"]["induced_A_singlet"]["label"] == "REPULSIVE"


def test_g_equals_two_c_in_both_normalisations_for_every_channel(artifact):
    for name in ccl.CHANNELS:
        entry = artifact["layer_1b"]["channels"][name]
        assert _expr(entry["g_in_normalisation_L"]) == 2 * _expr(
            entry["c_in_normalisation_L"]
        )
        assert _expr(entry["g_in_normalisation_P"]) == 2 * _expr(
            entry["c_in_normalisation_P"]
        )


def test_the_label_is_the_same_in_either_normalisation(artifact):
    """`c_P = (2/N) c_L` with `N > 0` cannot move a sign."""
    for name in ccl.CHANNELS:
        entry = artifact["layer_1b"]["channels"][name]
        assert sp.sign(_expr(entry["g_in_normalisation_L"])) == sp.sign(
            _expr(entry["g_in_normalisation_P"])
        )


def test_scalar_control_is_gating_and_passes(artifact):
    assert artifact["scalar_control"]["gate"] == "P2-GAP-01"
    assert artifact["scalar_control"]["expected_label"] == "ATTRACTIVE"
    assert artifact["scalar_control"]["observed_label"] == "ATTRACTIVE"
    assert artifact["scalar_control"]["control_passes"] is True


# ---- the mapping is read, not hard-coded -------------------------------
def test_the_mapping_factor_is_parsed_out_of_the_decision_log():
    mapping = ccl.exponent_mapping_factor()
    assert mapping["decision_log_entry"] == ccl.EXPONENT_MAPPING_HEADING
    assert mapping["factor"] == 2
    assert mapping["relation"] == "g = +2c"
    assert "2c" in mapping["statement_found"].replace(" ", "")


def test_the_label_rule_is_parsed_out_of_the_decision_log():
    rule = ccl.label_rule()
    assert rule["decision_log_entry"] == ccl.LABEL_RULING_HEADING
    assert rule["labels"] == {"+1": "ATTRACTIVE", "-1": "REPULSIVE"}


def test_reversing_the_mapping_in_the_log_flips_every_g_and_every_label(
    tmp_path, monkeypatch
):
    """The outputs move with the ruling, so they are not constants."""
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace("g = +2c", "g = -2c")
    assert mutated != text

    l1b, l2 = _layers_from_log(tmp_path, monkeypatch, mutated)

    assert l1b["basis"]["factor"] == -2
    for name in ccl.CHANNELS:
        assert _expr(l1b["channels"][name]["g_in_normalisation_L"]) == -2 * _expr(
            l1b["channels"][name]["c_in_normalisation_L"]
        )
    assert l2["channels"]["scalar_singlet_direct"]["label"] == "REPULSIVE"
    assert l2["channels"]["induced_V_singlet"]["label"] == "ATTRACTIVE"
    assert l2["channels"]["induced_A_singlet"]["label"] == "ATTRACTIVE"


def test_reversing_the_mapping_also_reverses_real_hs_admissibility(
    tmp_path, monkeypatch
):
    text = ccl.DECISION_LOG.read_text(encoding="utf-8").replace("g = +2c", "g = -2c")
    l1b, _ = _layers_from_log(tmp_path, monkeypatch, text)
    channels = l1b["channels"]
    assert channels["scalar_singlet_direct"]["real_linear_HS_field_admissible"] is False
    assert channels["induced_V_singlet"]["real_linear_HS_field_admissible"] is True
    assert channels["induced_A_singlet"]["real_linear_HS_field_admissible"] is True


def test_the_scalar_control_catches_a_reversed_mapping(tmp_path, monkeypatch):
    """The gating control is what stops a reversed chain from being written."""
    text = ccl.DECISION_LOG.read_text(encoding="utf-8").replace("g = +2c", "g = -2c")
    with pytest.raises(AssertionError, match="scalar control failed"):
        _run_isolated(tmp_path, monkeypatch, text)


def test_swapping_the_labels_in_the_log_swaps_the_reported_labels(
    tmp_path, monkeypatch
):
    """Layer 2 carries no independent notion of which sign is attractive."""
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace(
        "**`g > 0` is labelled\n> ATTRACTIVE**", "`g > 0` is labelled REPULSIVE"
    ).replace("`g < 0` is labelled REPULSIVE", "`g < 0` is labelled ATTRACTIVE")
    assert mutated != text

    _, l2 = _layers_from_log(tmp_path, monkeypatch, mutated)
    assert l2["basis"]["labels"] == {"+1": "REPULSIVE", "-1": "ATTRACTIVE"}
    assert l2["channels"]["scalar_singlet_direct"]["label"] == "REPULSIVE"


def test_removing_the_exponent_mapping_entry_stops_the_run(tmp_path, monkeypatch):
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace(ccl.EXPONENT_MAPPING_HEADING, "## 2026-08-08 — removed")
    with pytest.raises(AssertionError, match="DECISION_LOG entry"):
        _run_isolated(tmp_path, monkeypatch, mutated)


def test_removing_the_label_ruling_entry_stops_the_run(tmp_path, monkeypatch):
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace(ccl.LABEL_RULING_HEADING, "## 2026-08-08 — removed")
    with pytest.raises(AssertionError, match="DECISION_LOG entry"):
        _run_isolated(tmp_path, monkeypatch, mutated)


def test_a_mapping_entry_that_states_no_relation_stops_the_run(
    tmp_path, monkeypatch
):
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace("g = +2c", "the mapping is left open")
    with pytest.raises(AssertionError, match="no mapping to consume"):
        _run_isolated(tmp_path, monkeypatch, mutated)


def test_a_ruling_labelling_only_one_sign_stops_the_run(tmp_path, monkeypatch):
    text = ccl.DECISION_LOG.read_text(encoding="utf-8")
    mutated = text.replace("`g < 0` is labelled REPULSIVE", "the negative sign is open")
    with pytest.raises(AssertionError, match="does not label both signs"):
        _run_isolated(tmp_path, monkeypatch, mutated)


# ---- what the artifact must keep saying --------------------------------
def test_the_artifact_records_its_conditionality_and_registers_no_gate(artifact):
    assert artifact["gate_status"] == "P2-PHASE-01 remains PROPOSED"
    assert "chain" in artifact["conditionality"]
    assert "neither derived from the frozen material" in artifact["conditionality"]
    assert "no gate registered" in artifact["status"]


def test_layer_2_states_that_the_ruling_is_a_basis_and_not_a_derivation(artifact):
    basis = artifact["layer_2"]["basis_is_not_a_derivation"]
    assert "assigns a name to a sign" in basis
    assert "does not establish that condensation" in artifact["layer_2"]["scope_limit"]
    assert "bound state" in artifact["layer_2"]["scope_limit"]


def test_real_hs_admissibility_is_not_offered_as_a_force_statement(artifact):
    meaning = artifact["layer_1b"]["real_HS_meaning"]
    assert "not a statement about two-body forces" in meaning
    assert "not the absence of an interaction" in meaning


def test_the_diquark_channel_is_restated_as_still_blocked(artifact):
    diquark = artifact["diquark"]
    assert diquark["touched_by_this_task"] is False
    assert diquark["all_pp_operator_definitions_fixed"] is False
    assert diquark["channel_picture_is_not_complete"] is True
    assert set(diquark["still_unfrozen"].values()) == {False}


def test_open_ac_1_is_untouched_and_reported_as_evidence(artifact):
    open_ac = artifact["open_ac_1"]
    assert "no Hubbard-Stratonovich channel is selected" in open_ac["status"]
    assert open_ac["channels_admitting_a_real_linear_auxiliary_field"] == [
        "scalar_singlet_direct"
    ]
    assert "evidence, not a recommendation" in open_ac["what_this_is"]


def test_g_c_is_recorded_as_not_entering(artifact):
    assert "not a channel coefficient" in artifact["G_c_does_not_enter"]
    assert "G_c does not enter" in artifact["scalar_control"]["what_this_does_not_test"]


def test_recorded_inputs_exclude_the_three_prohibited_sources(artifact):
    assert set(artifact["exclusions_confirmed"].values()) == {"NOT READ"}
    for path in artifact["repository_inputs_read"]:
        assert (ROOT / path).is_file()
