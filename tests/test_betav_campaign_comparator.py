"""Negative / reachability tests for the betaV comparator (prereg Amendment 1).

The target-literal blindness guard applies to harness_compute.py, not to these
non-blind comparator tests; fixture values are arbitrary.

Synthetic hand-built compute-JSON structures (no physics runs) exercise the
required-variant validity rule, the uniform denominator rule, the
diagnostics-gate-the-audit manifest rule, the manifest/keyed-record and
extended-basis component rules, the integrity/scientific exit contract, and the
mechanical reachability of PASS / FAIL / INCONCLUSIVE.
"""

import importlib.util
import math
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPARE = ROOT / "scripts" / "P2-BETAV-CAMPAIGN" / "compare.py"

_spec = importlib.util.spec_from_file_location("cmp_neg", COMPARE)
cmp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cmp)

MASSES = [0.05, 0.08, 0.10, 0.12]


def _z(beta, m):
    return None if beta is None else beta * (m * m * math.log(m * m))


def _species(beta, valid=True):
    return {"Z": {repr(m): _z(beta, m) for m in MASSES},
            "mass_fit": {"valid": bool(valid and beta is not None),
                         "beta": beta, "basis": "m4"}}


def _variant(betas, valids=None):
    valids = valids or {}
    sp = {s: _species(betas[s], valids.get(s, True))
          for s in betas}
    return {"class": "VERDICT", "masses": MASSES, "basis": "m4", "species": sp}


def _good_diags():
    return {
        "gfvec-v2-seagull": {"executed": True, "valid": True,
                             "record_path": "x"},
        "extended-basis": {"executed": True, "valid": True, "record_path": "x",
                           "required_components": ["proca", "gfvec", "boson",
                                                   "D"],
                           "components": {c: {"valid": True}
                                          for c in ("proca", "gfvec", "boson",
                                                    "D")}}}


def doc_P(base, other):
    """audit-shaped doc: two verdict variants (baseline, v2)."""
    return {"arm": "P", "arm_config": {"species": ["proca", "gfvec", "boson"]},
            "required_diagnostics": ["gfvec-v2-seagull", "extended-basis"],
            "diagnostics": _good_diags(),
            "variants": {"baseline": base, "v2": other}}


def doc_H(base, other):
    """numrepro-shaped doc: species proca+boson, no required diagnostics."""
    return {"arm": "H", "arm_config": {"species": ["proca", "boson"]},
            "required_diagnostics": [], "diagnostics": {},
            "variants": {"baseline": base, "window-shift": other}}


# betas with R_cons = proca - gfvec + boson = 0
_CLEAN = {"proca": -2e-4, "gfvec": -3e-4, "boson": -1e-4}


# --------------------- Case 1: invalid required verdict variant ---------------------
def test_case1_invalid_required_variant():
    base = _variant(_CLEAN)
    bad = _variant(_CLEAN, valids={"proca": False})
    a = cmp.audit(doc_P(base, bad))
    assert a["harness_invalid"] and "HARNESS INVALID" in a["verdict"]
    h = cmp.historical_criterion(doc_P(base, bad))
    assert h["assessable"] is False and h["outcome"] == "NOT ASSESSABLE"
    # numrepro (Arm-H shape): INCONCLUSIVE, sigma NOT computed from reduced set
    nH = cmp.numrepro(doc_H(_variant({"proca": -3e-4, "boson": 1e-4}),
                            _variant({"proca": -3e-4, "boson": 1e-4},
                                     valids={"proca": False})))
    assert nH["verdict"] == "INCONCLUSIVE" and nH["assessable"] is False
    assert "sigma_H" not in nH


# --------------------- Case 2: denominator magnitude + sign ---------------------
def test_case2_denominator_rule():
    tiny = _variant({"proca": -3e-4, "boson": 1e-11})   # |bB| below tau_denom
    n1 = cmp.numrepro(doc_H(_variant({"proca": -3e-4, "boson": 1e-4}), tiny))
    assert n1["verdict"] == "INCONCLUSIVE" and n1["assessable"] is False
    assert "R_H" not in n1  # no huge ratio emitted
    flip = _variant({"proca": -3e-4, "boson": 1e-4})    # sign opposite baseline
    n2 = cmp.numrepro(doc_H(_variant({"proca": -3e-4, "boson": -1e-4}), flip))
    assert n2["verdict"] == "INCONCLUSIVE" and n2["assessable"] is False


# --------------------- Case 3/4/7/8: diagnostics gate the audit ---------------------
def test_case3_seagull_failed_to_execute():
    d = doc_P(_variant(_CLEAN), _variant(_CLEAN))
    d["diagnostics"]["gfvec-v2-seagull"]["valid"] = False
    a = cmp.audit(d)
    assert a["harness_invalid"] and a["verdict"].startswith("HARNESS INVALID")


def test_case4_required_diagnostic_marked_not_executed():
    d = doc_P(_variant(_CLEAN), _variant(_CLEAN))
    d["diagnostics"]["extended-basis"]["executed"] = False
    a = cmp.audit(d)
    assert a["harness_invalid"] and a["verdict"].startswith("HARNESS INVALID")


def test_case7_manifest_keyed_record_absent():
    d = doc_P(_variant(_CLEAN), _variant(_CLEAN))
    del d["diagnostics"]["extended-basis"]   # id in manifest, record absent
    a = cmp.audit(d)
    assert a["harness_invalid"]
    gate = a["diagnostics_gate"]["extended-basis"]
    assert gate["reason"] == "keyed record absent"


def test_case8_extended_basis_partial_component():
    d = doc_P(_variant(_CLEAN), _variant(_CLEAN))
    d["diagnostics"]["extended-basis"]["components"]["D"]["valid"] = False
    a = cmp.audit(d)
    assert a["harness_invalid"] and a["verdict"].startswith("HARNESS INVALID")


# --------------------- Case 5: mixed Arm-H variant invalid ---------------------
def test_case5_mixed_armH_variant_invalid():
    base = _variant({"proca": -3e-4, "boson": 1e-4})
    ws = _variant({"proca": -3e-4, "boson": 1e-4}, valids={"boson": False})
    n = cmp.numrepro(doc_H(base, ws))
    assert n["verdict"] == "INCONCLUSIVE" and n["assessable"] is False
    assert "sigma_H" not in n  # no recomputed smaller sigma


# --------------------- Case 6: exit-code contract ---------------------
def test_case6_exit_code_contract():
    assert cmp._exit_code({"integrity_status": "VERIFIED",
                           "scientific_status": "ASSESSABLE"}) == 0
    assert cmp._exit_code({"integrity_status": "VERIFIED",
                           "scientific_status": "HARNESS_INVALID"}) == 1
    assert cmp._exit_code({"integrity_status": "REFUSED",
                           "scientific_status": "ASSESSABLE"}) == 1


# --------------------- Case 9: reachability PASS / FAIL / INCONCLUSIVE ------
def test_case9_reachability():
    # PASS: R_cons = 0, sigma tiny (both variants identical)
    a_pass = cmp.audit(doc_P(_variant(_CLEAN), deepcopy(_variant(_CLEAN))))
    assert a_pass["verdict"] == "PASS"
    # FAIL: baseline C_cons large (~0.5), sigma tiny
    off = {"proca": -2e-4 + 0.5e-4, "gfvec": -3e-4, "boson": -1e-4}  # R=0.5|bB|
    a_fail = cmp.audit(doc_P(_variant(off), _variant(off)))
    assert a_fail["verdict"] == "FAIL"
    # INCONCLUSIVE (insufficient resolving power): valid but 2 sigma_C > 0.05
    spread = {"proca": -2e-4 + 0.1e-4, "gfvec": -3e-4, "boson": -1e-4}  # C=0.1
    a_inc = cmp.audit(doc_P(_variant(_CLEAN), _variant(spread)))
    assert a_inc["verdict"].startswith("INCONCLUSIVE") \
        and a_inc["assessable"] is True
