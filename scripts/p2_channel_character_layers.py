#!/usr/bin/env python3
"""`P2-PHASE-01` — Layer 1b and Layer 2 of the channel character.

Implements `derivations/P2-PHASE-01_channel_character_layers.md`.

The two layers the channel-character derivation withheld are computed
here from two PI rulings recorded in `DECISION_LOG.md`, both dated
2026-08-08:

    Euclidean exponent mapping        g = +2c
    Attraction/repulsion convention   g > 0 ATTRACTIVE, g < 0 REPULSIVE

**Both are parsed out of `DECISION_LOG.md` rather than hard-coded.**  If
either entry is absent, or states something other than what this script
expects to find, execution stops.  A recomputation that claims to
consume a ruling must fail when the ruling is removed; otherwise its
outputs never depended on it.

`G_c` does not enter.  The generator-sum criticality result concerns the
critical coupling, not a channel coefficient.

This is a computation, not a ruling.  It registers no gate, changes no
status, selects no Hubbard-Stratonovich channel, and freezes no diquark
convention.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DECISION_LOG = ROOT / "DECISION_LOG.md"
CHANNEL_SCRIPT = ROOT / "scripts/p2_channel_character.py"
CHANNEL_JSON = ROOT / "results/P2-PHASE-01/channel-character/channel_character.json"

OUT = ROOT / "results/P2-PHASE-01/channel-character-layers/layers.json"

# The specification's pins, verified before any of them is used.
PINS = {
    "derivations/P2-PHASE-01_channel_character.md":
        "380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f",
    "results/P2-PHASE-01/channel-character/channel_character.json":
        "093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f",
    "scripts/p2_channel_character.py":
        "521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126",
    "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md":
        "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
}

# The two DECISION_LOG entries this computation consumes, by heading.
EXPONENT_MAPPING_HEADING = (
    "## 2026-08-08 — Euclidean exponent mapping: "
    "the canonical interaction is written in the exponent"
)
LABEL_RULING_HEADING = (
    "## 2026-08-08 — Attraction/repulsion sign convention: "
    "the label is assigned to the sign of g"
)

CHANNELS = ("scalar_singlet_direct", "induced_V_singlet", "induced_A_singlet")

G, N = sp.symbols("G N", positive=True)


# ------------------------------------------------------------ inputs ------
def repository_inputs() -> list[str]:
    """Every repository file this script reads, by path."""
    return [
        "DECISION_LOG.md",
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "derivations/P2-PHASE-01_channel_character.md",
        "results/P2-PHASE-01/channel-character/channel_character.json",
        "scripts/p2_channel_character.py",
    ]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_pins() -> dict:
    """Fail loudly before any pinned input is consumed."""
    observed = {}
    for rel, expected in PINS.items():
        got = digest(ROOT / rel)
        observed[rel] = got
        if got != expected:
            raise AssertionError(f"pin mismatch for {rel}: {got} != {expected}")
    return observed


def _normalise(text: str) -> str:
    """Strip the Markdown representation, keep the substantive text.

    Blockquote markers, emphasis and code delimiters are removed and all
    whitespace is collapsed, so a phrase is found whether or not the
    author wrapped a line or put backticks round a symbol.  En dashes are
    left alone: `Hubbard-Stratonovich` is spelled with one.
    """
    lines = []
    for line in text.split("\n"):
        if line.startswith("> "):
            line = line[2:]
        elif line == ">":
            line = ""
        lines.append(line)
    joined = "\n".join(lines).replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", joined).strip()


def decision_log_entry(heading: str) -> str:
    """Return one top-level `DECISION_LOG.md` entry, by exact heading."""
    text = DECISION_LOG.read_text(encoding="utf-8")
    if text.count(heading) != 1:
        raise AssertionError(
            f"expected exactly one DECISION_LOG entry {heading!r}, "
            f"found {text.count(heading)}"
        )
    start = text.index(heading)
    nxt = text.find("\n## ", start + len(heading))
    return text[start:] if nxt < 0 else text[start:nxt]


# ------------------------------------------- the rulings, as parsed -------
def exponent_mapping_factor() -> dict:
    """Read `g = +2c` out of the exponent mapping ruling.

    Returns the factor relating the exponent-level coefficient `g` to the
    interaction-expression coefficient `c`.  It is read, not assumed: a
    ruling stating `g = -2c` would be honoured, and the labels computed
    downstream would move with it.
    """
    entry = decision_log_entry(EXPONENT_MAPPING_HEADING)
    normalised = _normalise(entry)
    match = re.search(r"\bg\s*=\s*([+-]?)\s*2\s*c\b", normalised)
    if match is None:
        raise AssertionError(
            "the exponent mapping ruling does not state g = <sign>2c; "
            "this computation has no mapping to consume"
        )
    sign = -1 if match.group(1) == "-" else +1
    return {
        "decision_log_entry": EXPONENT_MAPPING_HEADING,
        "statement_found": match.group(0),
        "factor": 2 * sign,
        "relation": f"g = {'+' if sign > 0 else '-'}2c",
    }


def label_rule() -> dict:
    """Read the sign-to-label rule out of the attraction/repulsion ruling.

    Both halves must be present.  A ruling naming only one sign leaves
    the other undefined, and this script will not invent it.
    """
    entry = decision_log_entry(LABEL_RULING_HEADING)
    normalised = _normalise(entry)
    positive = re.search(r"g > 0 is labelled ([A-Z]+)", normalised)
    negative = re.search(r"g < 0 is labelled ([A-Z]+)", normalised)
    if positive is None or negative is None:
        raise AssertionError(
            "the attraction/repulsion ruling does not label both signs of g; "
            "this computation has no sign-to-label rule to consume"
        )
    return {
        "decision_log_entry": LABEL_RULING_HEADING,
        "statements_found": [positive.group(0), negative.group(0)],
        "labels": {"+1": positive.group(1), "-1": negative.group(1)},
    }


# ---------------------------------------------------- layer 1a control ----
def _load_pinned_module():
    """Import the pinned channel-character script by file location."""
    spec = importlib.util.spec_from_file_location(
        "p2_channel_character_pinned", CHANNEL_SCRIPT
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def layer_1a_control() -> dict:
    """Re-execute the pinned Layer 1a and compare it to the pinned artifact.

    Exact symbolic comparison, both normalisations, every channel.  This
    is gating: everything downstream is a function of `c`.
    """
    recomputed = _load_pinned_module().layer_1a()["channels"]
    artifact = json.loads(CHANNEL_JSON.read_text(encoding="utf-8"))
    pinned = artifact["layer_1a"]["channels"]

    comparisons = {}
    agree = True
    for name in CHANNELS:
        entry = {}
        for field in ("normalisation_L", "normalisation_P"):
            lhs = sp.sympify(recomputed[name][field], locals={"G": G, "N": N})
            rhs = sp.sympify(pinned[name][field], locals={"G": G, "N": N})
            same = sp.simplify(lhs - rhs) == 0
            agree &= same
            entry[field] = {
                "recomputed": str(lhs),
                "pinned": str(rhs),
                "symbolic_difference": str(sp.simplify(lhs - rhs)),
                "equal": bool(same),
            }
        sign_same = recomputed[name]["sign"] == pinned[name]["sign"]
        agree &= sign_same
        entry["sign"] = {
            "recomputed": recomputed[name]["sign"],
            "pinned": pinned[name]["sign"],
            "equal": bool(sign_same),
        }
        comparisons[name] = entry

    return {
        "layer": "1a — frozen algebraic coefficient; UNCONDITIONAL",
        "method": (
            "re-executed layer_1a() of the pinned scripts/p2_channel_character.py, "
            "which reads the frozen basis block and matrix_rational, and compared "
            "every coefficient as an exact symbolic difference against the pinned "
            "results/P2-PHASE-01/channel-character/channel_character.json"
        ),
        "comparisons": comparisons,
        "control_passes": bool(agree),
        "gating": "disagreement is a STOP; everything downstream is a function of c",
    }


# ------------------------------------------------------------ layers ------
def coefficients_from_control(control: dict) -> dict:
    """The verified `c` per channel, in both normalisations."""
    return {
        name: {
            "normalisation_L": sp.sympify(
                control["comparisons"][name]["normalisation_L"]["recomputed"],
                locals={"G": G, "N": N},
            ),
            "normalisation_P": sp.sympify(
                control["comparisons"][name]["normalisation_P"]["recomputed"],
                locals={"G": G, "N": N},
            ),
        }
        for name in CHANNELS
    }


def layer_1b(coefficients: dict, mapping: dict) -> dict:
    """`g` per channel, computed from `c` by the ruling's factor."""
    factor = sp.Integer(mapping["factor"])
    channels = {}
    for name in CHANNELS:
        g_L = sp.simplify(factor * coefficients[name]["normalisation_L"])
        g_P = sp.simplify(factor * coefficients[name]["normalisation_P"])
        sign_L = int(sp.sign(g_L))
        sign_P = int(sp.sign(g_P))
        if sign_L != sign_P:
            raise AssertionError(
                f"{name}: sign differs between normalisations, which is "
                "impossible for c_P = (2/N) c_L with N > 0"
            )
        channels[name] = {
            "c_in_normalisation_L": str(coefficients[name]["normalisation_L"]),
            "c_in_normalisation_P": str(coefficients[name]["normalisation_P"]),
            "g_in_normalisation_L": str(g_L),
            "g_in_normalisation_P": str(g_P),
            "sign_of_g": sign_L,
            "real_linear_HS_field_admissible": bool(sign_L > 0),
        }
    return {
        "layer": "1b — exponent / HS coefficient; CONDITIONAL on the mapping",
        "basis": mapping,
        "identity": (
            "exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J], "
            "convergent only for g > 0"
        ),
        "g_is_exponent_level": (
            "g is not the same kind of object as c; it equals 2c here because "
            "the exponent mapping ruling says so, not by identity"
        ),
        "real_HS_meaning": (
            "whether the standard linear Hubbard-Stratonovich representation "
            "with a real Gaussian auxiliary field converges; it is not a "
            "statement about two-body forces, and False is not the absence of "
            "an interaction in the channel"
        ),
        "channels": channels,
    }


def layer_2(layer_1b_result: dict, rule: dict) -> dict:
    """The label per channel, assigned to the sign of `g` by the ruling."""
    labels = rule["labels"]
    channels = {}
    for name in CHANNELS:
        sign = layer_1b_result["channels"][name]["sign_of_g"]
        key = "+1" if sign > 0 else "-1"
        if sign == 0:
            raise AssertionError(f"{name}: g vanishes; the ruling labels no zero")
        channels[name] = {
            "sign_of_g": sign,
            "label": labels[key],
        }
    return {
        "layer": "2 — physical label; assigned to the sign of g by ruling",
        "basis": rule,
        "basis_is_not_a_derivation": (
            "the ruling assigns a name to a sign; nothing here is derived from "
            "the frozen material, and reversing the exponent mapping reverses "
            "every label"
        ),
        "scope_limit": (
            "the label characterises the sign of the interaction in the "
            "specified channel; it does not establish that condensation "
            "occurs, nor the existence or absence of a two-body bound state, "
            "resonance or composite excitation"
        ),
        "channels": channels,
    }


def scalar_control(layer_2_result: dict, rule: dict) -> dict:
    """`P2-GAP-01` calls its positive-coupling scalar channel attractive."""
    label = layer_2_result["channels"]["scalar_singlet_direct"]["label"]
    expected = rule["labels"]["+1"]
    return {
        "gate": "P2-GAP-01",
        "expected_label": expected,
        "observed_label": label,
        "control_passes": bool(label == expected),
        "gating": (
            "a scalar label other than the positive-sign label means the chain "
            "from c through g to the label is wrong, and the V and A results "
            "cannot be trusted either"
        ),
        "what_this_does_not_test": (
            "it does not re-derive G_c = 1/(2 I_0) and does not lift P2-GAP-01 "
            "to the generator-sum interaction; G_c does not enter this "
            "computation at all"
        ),
    }


def diquark_status() -> dict:
    """Restated from the pinned artifact.  Nothing here changes it."""
    pinned = json.loads(CHANNEL_JSON.read_text(encoding="utf-8"))
    step0 = pinned["derivation_b_diquark_executability"]["step_0_detail"]
    return {
        "touched_by_this_task": False,
        "all_pp_operator_definitions_fixed": pinned[
            "derivation_b_diquark_executability"
        ]["step_0_all_pp_operator_definitions_fixed"],
        "still_unfrozen": {
            "charge_conjugated_field_definition_eta": step0[
                "charge_conjugated_field_definition_frozen"
            ],
            "particle_particle_grassmann_ordering": step0[
                "particle_particle_grassmann_ordering_frozen"
            ],
            "diquark_operator_normalisation": step0[
                "diquark_operator_normalisation_frozen"
            ],
        },
        "why_the_rulings_do_not_unblock_it": (
            "the exponent mapping and the sign-to-label rule supply a mapping "
            "and a naming convention; neither is a particle-particle operator "
            "definition, and eta appears once in the paired product and flips "
            "the coefficient sign"
        ),
        "channel_picture_is_not_complete": True,
    }


def open_ac_1(layer_1b_result: dict) -> dict:
    """Evidence bearing on `OPEN-AC-1`, which remains the PI's."""
    admissible = [
        name
        for name in CHANNELS
        if layer_1b_result["channels"][name]["real_linear_HS_field_admissible"]
    ]
    return {
        "status": "untouched; no Hubbard-Stratonovich channel is selected here",
        "channels_admitting_a_real_linear_auxiliary_field": admissible,
        "channels_not_admitting_one": [c for c in CHANNELS if c not in admissible],
        "what_this_is": (
            "evidence, not a recommendation: it narrows which of the three "
            "particle-hole channels computed here could carry the standard "
            "real linear representation, and says nothing about the "
            "particle-particle channel, which is not computed"
        ),
        "conditional_on": [
            EXPONENT_MAPPING_HEADING,
            LABEL_RULING_HEADING,
        ],
    }


# -------------------------------------------------------------- main ------
def main() -> dict:
    pins = verify_pins()

    mapping = exponent_mapping_factor()
    rule = label_rule()

    control = layer_1a_control()
    if not control["control_passes"]:
        raise AssertionError("Layer 1a control failed; STOP")

    coefficients = coefficients_from_control(control)
    l1b = layer_1b(coefficients, mapping)
    l2 = layer_2(l1b, rule)

    scalar = scalar_control(l2, rule)
    if not scalar["control_passes"]:
        raise AssertionError("scalar control failed; STOP")

    payload = {
        "study": "P2-PHASE-01 channel character — Layer 1b and Layer 2",
        "derivation_note": "derivations/P2-PHASE-01_channel_character_layers.md",
        "authority": "specs/2026-08-09T0300Z_attraction-ruling-and-layers.md",
        "status": (
            "DERIVATION; a computation, not a ruling; no gate registered, no "
            "status changed, no frozen or pinned artifact modified, no "
            "Hubbard-Stratonovich channel selected, no diquark convention "
            "frozen, no programme registry row changed"
        ),
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "conditionality": (
            "Layer 1b and Layer 2 are conditional on two PI rulings of "
            "2026-08-08, both parsed from DECISION_LOG.md by this script and "
            "neither derived from the frozen material; they are a chain, and "
            "reversing the exponent mapping reverses every label"
        ),
        "G_c_does_not_enter": (
            "the generator-sum criticality result concerns the critical "
            "coupling, not a channel coefficient; no reconciliation is "
            "attempted"
        ),
        "input_sha256": pins,
        "repository_inputs_read": repository_inputs(),
        "exclusions_confirmed": {
            "quarantined_-3.2(5)": "NOT READ",
            "suspended_P2-BETAV-CIRC-01_result": "NOT READ",
            "historical_Finding_5_extraction": "NOT READ",
        },
        "layer_1a_control": control,
        "layer_1b": l1b,
        "layer_2": l2,
        "scalar_control": scalar,
        "diquark": diquark_status(),
        "open_ac_1": open_ac_1(l1b),
        "composite_vector": (
            "no statement is made about whether a composite vector exists. A "
            "channel-character label is not a bound-state or pole "
            "calculation, and the ruling forbids that inference explicitly."
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return payload


if __name__ == "__main__":
    result = main()
    print(json.dumps(result["layer_2"]["channels"], indent=2, sort_keys=True))
    sys.exit(0)
