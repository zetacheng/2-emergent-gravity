"""Machine guards for the P2-BETAV blind campaign harness (prereg Task 2).

Four layered guards — substring search alone is insufficient, so all four are
in the governance suite:

1. AST numeric-literal guard on harness_compute.py (no target constants).
2. Subprocess/in-process stdout blindness guard (no ratio/verdict/band/target).
3. Output-schema guard on the committed pilot JSON (no ratio/verdict fields;
   no self-hash; required diagnostics + class labels present).
4. compare.py performs all five refuse-checks, in order, before comparing.
"""

import ast
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CAMP = ROOT / "scripts" / "P2-BETAV-CAMPAIGN"
HARNESS = CAMP / "harness_compute.py"
COMPARE = CAMP / "compare.py"
PILOT = ROOT / "results" / "P2-BETAV-CAMPAIGN" / "raw" / "pilot.json"

# Target constants that must never appear as literals in the blind harness.
FORBIDDEN_NEG = {2, 3, 2.0, 3.0, 3.2}


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ------------------------- Guard 1: AST literal guard -------------------------
def test_guard1_ast_no_target_literals():
    tree = ast.parse(HARNESS.read_text(encoding="utf-8"))
    bad = []
    for node in ast.walk(tree):
        # negative literals: Python parses -3.0 as UnaryOp(USub, Constant(3.0))
        if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)
                and isinstance(node.operand, ast.Constant)):
            val = node.operand.value
            if (isinstance(val, (int, float)) and not isinstance(val, bool)
                    and val in FORBIDDEN_NEG):
                bad.append(("neg-literal", val, node.lineno))
        # bare 3.2 in any float form
        if (isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float))
                and not isinstance(node.value, bool) and node.value == 3.2):
            bad.append(("bare-3.2", node.value, node.lineno))
    assert not bad, f"forbidden target literals in harness_compute.py: {bad}"


# ------------------------- Guard 2: stdout blindness -------------------------
def test_guard2_stdout_blindness(monkeypatch, capsys):
    hc = _load(HARNESS, "hc_guard2")
    # micro config exercises the identical print path cheaply (n=4)
    monkeypatch.setitem(hc.CONFIG, "pilot", {
        "n": 4, "species": ["proca", "gfvec", "boson"],
        "eps": [0.10, 0.18, 0.26],
        "masses_baseline": [0.5, 0.6], "masses_shift": []})
    # write under the repo (so the status line's relative_to(_ROOT) works),
    # then clean up; keeps _ROOT real for the registered-source hashing.
    outdir = ROOT / "results" / "P2-BETAV-CAMPAIGN" / "raw"
    jp = outdir / "_guard2_tmp.json"
    sp = outdir / "_guard2_tmp.json.sha256"
    monkeypatch.setattr(hc, "_out_paths", lambda arm, mut: (jp, sp))
    try:
        hc.main(["--arm", "pilot"])
        out = capsys.readouterr().out.lower()
    finally:
        jp.unlink(missing_ok=True)
        sp.unlink(missing_ok=True)
    forbidden = ["ratio", "verdict", "inconclusive", "band", "target",
                 "pass", "fail", "-2", "-3", "3.2", "β"]
    hits = [w for w in forbidden if w in out]
    assert not hits, f"blind harness stdout leaked vocabulary {hits}: {out!r}"


# ------------------------- Guard 3: output schema -------------------------
def _walk_keys(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k
            yield from _walk_keys(v)
    elif isinstance(obj, list):
        for it in obj:
            yield from _walk_keys(it)


def test_guard3_output_schema():
    if not PILOT.is_file():
        pytest.skip("pilot.json not yet committed (lands with the pilot commit)")
    raw = PILOT.read_text(encoding="utf-8")
    doc = json.loads(raw)
    required = {"schema_version", "prereg_sha256", "registered_sources",
                "arm_config", "raw_g2axis", "variants", "compute_git_commit",
                "required_diagnostics", "diagnostics"}
    assert required <= set(doc), f"missing keys: {required - set(doc)}"
    assert doc["schema_version"].endswith("/v2"), doc["schema_version"]
    # no ratio/verdict/target fields anywhere
    forbidden_keys = {"ratio", "verdict", "target", "band", "promote",
                      "c_cons", "r_h", "integrity_status", "scientific_status"}
    present = {k.lower() for k in _walk_keys(doc)}
    assert not (present & forbidden_keys), (present & forbidden_keys)
    # manifest: every required-diagnostic ID has a keyed record; extended-basis
    # declares its four components
    for did in doc["required_diagnostics"]:
        assert did in doc["diagnostics"], f"manifest id {did} has no record"
        rec = doc["diagnostics"][did]
        assert "executed" in rec and "valid" in rec and "record_path" in rec
    if "extended-basis" in doc["diagnostics"]:
        comps = doc["diagnostics"]["extended-basis"].get("components", {})
        assert {"proca", "gfvec", "boson", "D"} <= set(comps), comps
    # self-reference rule: the file's own sha256 must not appear inside it
    sidecar = Path(str(PILOT) + ".sha256").read_text().split()[0]
    assert sidecar not in raw, "JSON contains its own hash (self-reference)"
    # every variant carries a class label; the two diagnostics are present
    classes = {"VERDICT", "DIAGNOSTIC-ONLY"}
    for name, v in doc["variants"].items():
        assert v.get("class") in classes, f"{name} bad class {v.get('class')}"
        for sp, spd in v["species"].items():
            mf = spd["mass_fit"]
            assert "valid" in mf and "basis" in mf and "beta" in mf, (name, sp)
            assert "Z" in spd and "eps_fits" in spd, (name, sp)
    assert "gfvec-v2-seagull" in doc["variants"]
    assert "extended-basis" in doc["variants"]


# ------------------------- Guard 4: refuse-check order -------------------------
def test_guard4_compare_five_checks_in_order():
    if not PILOT.is_file():
        pytest.skip("pilot.json not yet committed (lands with the pilot commit)")
    cmp = _load(COMPARE, "cmp_guard4")
    ok, doc, log = cmp.refuse_checks(PILOT)
    assert ok, f"pilot failed refuse checks: {log}"
    # exactly five checks, numbered (1)..(5), strictly in order
    nums = [int(entry.split(")")[0].lstrip("(")) for entry in log]
    assert nums == [1, 2, 3, 4, 5], f"refuse-check order wrong: {log}"
    # the five mechanisms are actually implemented in compare.py source
    src = COMPARE.read_text(encoding="utf-8")
    for needle in ("sha256", "prereg_sha256", "registered_sources",
                   "merge-base", "--is-ancestor", "schema_version"):
        assert needle in src, f"compare.py missing mechanism: {needle}"


def test_guard4_refuse_rejects_schema_tamper(tmp_path):
    if not PILOT.is_file():
        pytest.skip("pilot.json not yet committed (lands with the pilot commit)")
    cmp = _load(COMPARE, "cmp_guard4b")
    # tamper the JSON body; sidecar hash (check 1) must catch it first
    bad = tmp_path / "pilot.json"
    doc = json.loads(PILOT.read_text())
    doc["schema_version"] = "tampered"
    bad.write_text(json.dumps(doc), encoding="utf-8")
    (tmp_path / "pilot.json.sha256").write_text(
        Path(str(PILOT) + ".sha256").read_text())  # stale hash
    ok, _, log = cmp.refuse_checks(bad)
    assert not ok and log[-1].startswith("(1)"), log
