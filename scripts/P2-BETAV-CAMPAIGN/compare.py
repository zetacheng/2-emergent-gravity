"""Comparison / acceptance stage for the P2-BETAV decisive campaign.

Separate from the blind compute harness (prereg (g)). Reads a frozen compute
JSON, REFUSES to run unless five integrity checks pass in order, then applies
the pre-registered acceptance rules (prereg (c1)-(c7)) and emits a verdict table
with diagnostics reported separately.

Exit-code contract (prereg (c7) / Amendment 1). The output carries two
top-level fields:
    integrity_status  : "VERIFIED" | "REFUSED"
    scientific_status : "ASSESSABLE" | "HARNESS_INVALID"
Exit 0 requires integrity_status=VERIFIED AND scientific_status=ASSESSABLE, and
covers PASS, FAIL, and scientifically-assessable INCONCLUSIVE (insufficient
resolving power; NUMREPRO interval straddling a band boundary). Exit non-zero
covers: integrity REFUSED; HARNESS INVALID; any required verdict variant
invalid; any required diagnostic missing/invalid; denominator invalidity making
a criterion not-assessable; runtime/schema error. Automation must never mistake
a harness-invalid run for success.

The target numbers and bands live here (this is the non-blind stage). Not run in
the pre-registration task except on the non-decisive pilot.

Usage::

    python scripts/P2-BETAV-CAMPAIGN/compare.py --json <raw>/pilot.json
    python scripts/P2-BETAV-CAMPAIGN/compare.py --mutation-check \
        --base <raw>/pilot.json --mutated <raw>/pilot_mut_gfvec_scale.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[1]

SCHEMA_VERSION = "p2-betav-campaign/compute/v2"

# ---- frozen acceptance numbers (prereg (c)); this is the NON-blind stage ----
DELTA_AUDIT = 0.05                      # (c1) resolving-power ceiling
NUMREPRO_BAND = (-3.7, -2.7)           # (c2)
CRIT_GFVEC_BAND = (-2.10, -1.90)       # (c5)
CRIT_PROCA_BAND = (-3.15, -2.85)       # (c5)
CRIT_SIGMA_GF = 0.10                   # (c5) 5% of |target|=2
CRIT_SIGMA_PROCA = 0.15                # (c5) 5% of |target|=3
FLOOR_ABS = 1e-10
FLOOR_REL = 1e-6
VERDICT_CLASS = "VERDICT"


# ----------------------------- refuse gate -----------------------------
def _sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _is_ancestor(commit):
    try:
        subprocess.check_call(
            ["git", "-C", str(_ROOT), "merge-base", "--is-ancestor",
             commit, "HEAD"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def refuse_checks(json_path):
    """Five checks, IN ORDER. Returns (ok, doc, log); stops at first failure."""
    log = []
    json_path = Path(json_path)
    sidecar = Path(str(json_path) + ".sha256")
    if not sidecar.exists():
        return False, None, log + ["(1) sidecar missing"]
    want = sidecar.read_text().split()[0]
    got = hashlib.sha256(json_path.read_bytes()).hexdigest()
    if want != got:
        return False, None, log + [f"(1) sidecar hash mismatch {got}!={want}"]
    log.append("(1) sidecar hash OK")
    doc = json.loads(json_path.read_text())
    prereg = _ROOT / "derivations" / "P2-BETAV-CAMPAIGN_prereg.md"
    if doc.get("prereg_sha256") != _sha256_file(prereg):
        return False, None, log + ["(2) prereg-doc hash mismatch"]
    log.append("(2) prereg-doc hash OK")
    for name, rec in doc.get("registered_sources", {}).items():
        p = _ROOT / rec["path"]
        if not p.exists() or _sha256_file(p) != rec["sha256"]:
            return False, None, log + [f"(3) source hash mismatch: {name}"]
    log.append("(3) registered-source hashes OK")
    commit = doc.get("compute_git_commit", "")
    if not _is_ancestor(commit):
        return False, None, log + [f"(4) compute commit not ancestor: {commit}"]
    log.append("(4) compute commit is ancestor of HEAD")
    if doc.get("schema_version") != SCHEMA_VERSION:
        return False, None, log + ["(5) schema version mismatch"]
    log.append("(5) schema version OK")
    return True, doc, log


# ----------------------------- helpers -----------------------------
def _beta(doc, variant, species):
    v = doc["variants"].get(variant, {})
    sp = v.get("species", {}).get(species, {})
    mf = sp.get("mass_fit", {})
    return mf.get("beta"), bool(mf.get("valid", False))


def _verdict_variants(doc):
    return [name for name, v in doc["variants"].items()
            if v.get("class") == VERDICT_CLASS]


def _baseline_floor(doc):
    """tau_num, tau_denom from baseline betas (prereg (a)/(c3))."""
    bp, _ = _beta(doc, "baseline", "proca")
    bb, _ = _beta(doc, "baseline", "boson")
    bg, _ = _beta(doc, "baseline", "gfvec")
    mags = [abs(x) for x in (bp, bg, bb) if x is not None]
    m = max(mags) if mags else 0.0
    tau = FLOOR_ABS + FLOOR_REL * m
    return tau, tau, bp, bg, bb


def _denom_valid(bd, vd, tau_denom, base_sign):
    return bool(vd and bd is not None and abs(bd) > tau_denom
                and (bd > 0) == base_sign)


def _strict_ratio_battery(doc, num, den):
    """Paired ratio num/den over ALL required verdict variants (prereg (c7)-i,
    (c7)-ii). NOT assessable if any required variant is invalid or any
    denominator fails (c3); invalid variants are never silently dropped."""
    tau_denom = _baseline_floor(doc)[1]
    bd0, vd0 = _beta(doc, "baseline", den)
    if not (vd0 and bd0 is not None) or abs(bd0) <= tau_denom:
        return {"assessable": False, "reason": "baseline denominator invalid",
                "invalid_variants": ["baseline"]}
    base_sign = bd0 > 0
    invalid, vals = [], {}
    for var in _verdict_variants(doc):
        bn, vn = _beta(doc, var, num)
        bd, vd = _beta(doc, var, den)
        if not (vn and bn is not None) or not _denom_valid(bd, vd, tau_denom,
                                                           base_sign):
            invalid.append(var)
            continue
        vals[var] = bn / bd
    if invalid:
        return {"assessable": False,
                "reason": "required verdict variant(s) invalid",
                "invalid_variants": invalid, "n_valid": len(vals)}
    c = vals["baseline"]
    sigma = max((abs(vals[v] - c) for v in vals), default=0.0)
    return {"assessable": True, "central": c, "sigma": sigma,
            "n_variants": len(vals), "per_variant": vals}


def _diagnostics_gate(doc):
    """Iterate the frozen required_diagnostics manifest and validate each keyed
    record (prereg (c7)-iii). Returns (ok, detail). Absence == failure."""
    manifest = doc.get("required_diagnostics", [])
    records = doc.get("diagnostics", {})
    detail = {}
    ok = True
    for did in manifest:
        rec = records.get(did)
        if rec is None:  # manifest/keyed-record mismatch
            detail[did] = {"ok": False, "reason": "keyed record absent"}
            ok = False
            continue
        if not rec.get("executed", False) or not rec.get("valid", False):
            detail[did] = {"ok": False,
                           "reason": "not executed / not valid",
                           "executed": rec.get("executed"),
                           "valid": rec.get("valid")}
            ok = False
            continue
        if did == "extended-basis":
            comps = rec.get("components", {})
            need = rec.get("required_components",
                           ["proca", "gfvec", "boson", "D"])
            bad = [c for c in need
                   if not comps.get(c, {}).get("valid", False)]
            if bad:
                detail[did] = {"ok": False,
                               "reason": f"invalid components {bad}"}
                ok = False
                continue
        detail[did] = {"ok": True}
    return ok, detail


# ----------------------------- rule application -----------------------------
def _fit_D(doc, variant):
    """beta of D(m)=Z_proca-Z_gfvec+Z_boson via the recovered fit basis."""
    v = doc["variants"][variant]
    masses, basis = v["masses"], v["basis"]
    try:
        import numpy as np
        zc = {sp: [v["species"][sp]["Z"][repr(m)] for m in masses]
              for sp in ("proca", "gfvec", "boson")}
        dvals = [zc["proca"][i] - zc["gfvec"][i] + zc["boson"][i]
                 for i in range(len(masses))]
        m2 = np.asarray(masses, float) ** 2
        cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
        if basis in ("m4", "ext5"):
            cols.append(m2 ** 2)
        if basis == "ext5":
            cols.append(m2 ** 2 * np.log(m2))
        a = np.stack(cols, axis=1)
        if a.shape[0] < a.shape[1]:
            return None
        coef, *_ = np.linalg.lstsq(a, np.asarray(dvals, float), rcond=None)
        return float(coef[2])
    except Exception:
        return None


def audit(doc):
    """Arm-P operator-identity audit (prereg (c1)); diagnostics gate first."""
    out = {"kind": "audit"}
    species = doc["arm_config"]["species"]
    if not {"proca", "gfvec", "boson"} <= set(species):
        out.update(verdict="N/A (no gfvec; audit is Arm-P only)",
                   assessable=True, harness_invalid=False)
        return out

    # (B.3) diagnostics gate BEFORE any verdict
    dg_ok, dg_detail = _diagnostics_gate(doc)
    out["diagnostics_gate"] = dg_detail
    if not dg_ok:
        out.update(verdict="HARNESS INVALID / AUDIT INCONCLUSIVE",
                   reason="required diagnostic missing/invalid",
                   assessable=False, harness_invalid=True)
        return out

    tau_num, tau_denom, bp0, bg0, bb0 = _baseline_floor(doc)
    if bb0 is None or abs(bb0) <= tau_denom:
        out.update(verdict="HARNESS INVALID / AUDIT INCONCLUSIVE",
                   reason="baseline denominator invalid",
                   assessable=False, harness_invalid=True)
        return out
    base_sign = bb0 > 0
    tau_C = tau_num / abs(bb0)

    # (B.1) all required verdict variants must be valid (never dropped)
    ccons, invalid, xchecks = {}, [], {}
    for var in _verdict_variants(doc):
        bp, vp = _beta(doc, var, "proca")
        bg, vg = _beta(doc, var, "gfvec")
        bb, vb = _beta(doc, var, "boson")
        if not (vp and vg and vb) or not _denom_valid(bb, vb, tau_denom,
                                                      base_sign):
            invalid.append(var)
            continue
        R = bp - bg + bb
        ccons[var] = R / abs(bb)
        beta_D = _fit_D(doc, var)
        xchecks[var] = (None if beta_D is None else abs(beta_D - R))
    if invalid:
        out.update(verdict="HARNESS INVALID / AUDIT INCONCLUSIVE",
                   reason="required verdict variant(s) invalid",
                   invalid_verdict_variants=invalid,
                   assessable=False, harness_invalid=True)
        return out
    # Tier-1<->Tier-2 machine cross-check must pass for EVERY verdict variant
    xfail = [v for v, d in xchecks.items() if d is None or d > tau_num]
    out["xcheck_tau_num"] = tau_num
    out["xcheck_max"] = max((d for d in xchecks.values() if d is not None),
                            default=None)
    if xfail:
        out.update(verdict="HARNESS INVALID / AUDIT INCONCLUSIVE",
                   reason=f"Tier1<->Tier2 cross-check failed: {xfail}",
                   assessable=False, harness_invalid=True)
        return out
    c_base = ccons["baseline"]
    sigma_C = max((abs(ccons[v] - c_base) for v in ccons), default=0.0)
    tol = max(2 * sigma_C, tau_C)
    out.update(C_cons_baseline=c_base, sigma_C=sigma_C, tau_C=tau_C,
               tol=tol, twosigma=2 * sigma_C, delta_audit=DELTA_AUDIT,
               gfvec_over_B=_strict_ratio_battery(doc, "gfvec", "boson"),
               proca_over_B=_strict_ratio_battery(doc, "proca", "boson"),
               harness_invalid=False)
    if 2 * sigma_C > DELTA_AUDIT:
        out.update(verdict="INCONCLUSIVE (insufficient resolving power)",
                   assessable=True)
    elif abs(c_base) <= tol:
        out.update(verdict="PASS", assessable=True)
    else:
        out.update(verdict="FAIL", assessable=True)
    return out


def numrepro(doc):
    """Arm-H NUMREPRO (prereg (c2)). R_H = beta_proca/beta_boson."""
    out = {"kind": "numrepro"}
    rb = _strict_ratio_battery(doc, "proca", "boson")
    if not rb["assessable"]:
        out.update(verdict="INCONCLUSIVE", reason=rb["reason"],
                   invalid_variants=rb.get("invalid_variants"),
                   assessable=False, harness_invalid=True)
        return out
    R, sigma = rb["central"], rb["sigma"]
    lo, hi = R - 2 * sigma, R + 2 * sigma
    out.update(R_H=R, sigma_H=sigma, interval=[lo, hi],
               band=list(NUMREPRO_BAND), per_variant=rb["per_variant"],
               harness_invalid=False, assessable=True)
    if NUMREPRO_BAND[0] <= lo and hi <= NUMREPRO_BAND[1]:
        out["verdict"] = "PASS"
    elif hi < NUMREPRO_BAND[0] or lo > NUMREPRO_BAND[1]:
        out["verdict"] = "FAIL"
    else:
        out["verdict"] = "INCONCLUSIVE"  # interval straddle: assessable
    return out


def historical_criterion(doc):
    """Arm-P recorded outcome (prereg (c5)); recorded, not an action."""
    gf = _strict_ratio_battery(doc, "gfvec", "boson")
    pr = _strict_ratio_battery(doc, "proca", "boson")
    if not (gf["assessable"] and pr["assessable"]):
        return {"kind": "historical-criterion", "outcome": "NOT ASSESSABLE",
                "reason": "a required ratio path is invalid",
                "gfvec_over_B": gf, "proca_over_B": pr,
                "assessable": False, "harness_invalid": True}
    gf_ok = (CRIT_GFVEC_BAND[0] <= gf["central"] <= CRIT_GFVEC_BAND[1]
             and gf["sigma"] <= CRIT_SIGMA_GF)
    pr_ok = (CRIT_PROCA_BAND[0] <= pr["central"] <= CRIT_PROCA_BAND[1]
             and pr["sigma"] <= CRIT_SIGMA_PROCA)
    return {"kind": "historical-criterion", "gfvec_over_B": gf,
            "proca_over_B": pr, "met": bool(gf_ok and pr_ok),
            "assessable": True, "harness_invalid": False,
            "note": "recorded outcome; promotion is a separate PI+reviewer step"}


def seagull_diagnostic(doc):
    """gfvec-v2 vs bubble sensitivity (prereg (a2)/(c6)); diagnostic-only."""
    if "gfvec-v2-seagull" not in doc["variants"]:
        return {"kind": "seagull", "status": "not present"}
    v2 = doc["variants"]["gfvec-v2-seagull"]["species"].get("gfvec_v2", {})
    base = doc["variants"]["baseline"]["species"].get("gfvec", {})
    if not v2 or not base:
        return {"kind": "seagull", "status": "HARNESS INVALID (missing series)"}
    import numpy as np
    masses = doc["variants"]["gfvec-v2-seagull"]["masses"]
    try:
        zv2 = np.array([v2["Z"][repr(m)] for m in masses], float)
        zbb = np.array([base["Z"][repr(m)] for m in masses], float)
    except Exception:
        return {"kind": "seagull", "status": "HARNESS INVALID (Z access)"}
    if not (np.all(np.isfinite(zv2)) and np.all(np.isfinite(zbb))):
        return {"kind": "seagull", "status": "HARNESS INVALID (non-finite)"}
    tau_Z = FLOOR_ABS + FLOOR_REL * max(np.abs(zv2).max(), np.abs(zbb).max())
    dZmax = float(np.abs(zv2 - zbb).max())
    bv2 = v2.get("mass_fit", {}).get("beta")
    bbb = base.get("mass_fit", {}).get("beta")
    bb0 = _baseline_floor(doc)[4]
    status = ("SEAGULL-SENSITIVITY DETECTED" if dZmax > tau_Z
              else "consistent (<= tau_Z)")
    return {"kind": "seagull", "status": status, "dZ_max": dZmax,
            "tau_Z": tau_Z,
            "dbeta": (None if bv2 is None or bbb is None else bv2 - bbb),
            "dbeta_over_absBbase": (None if (bv2 is None or bbb is None
                                    or not bb0) else (bv2 - bbb) / abs(bb0))}


# ----------------------------- mutation check -----------------------------
def mutation_check(base_path, mutated_path):
    ok, base, log = refuse_checks(base_path)
    if not ok:
        return {"status": "REFUSED (base)", "log": log,
                "integrity_status": "REFUSED"}
    ok2, mut, log2 = refuse_checks(mutated_path)
    if not ok2:
        return {"status": "REFUSED (mutated)", "log": log2,
                "integrity_status": "REFUSED"}
    tau_num, _, bp0, bg0, bb0 = _baseline_floor(base)
    bpm, _ = _beta(mut, "baseline", "proca")
    bgm, _ = _beta(mut, "baseline", "gfvec")
    bbm, _ = _beta(mut, "baseline", "boson")
    a1_obs = (bpm - bgm + bbm) - (bp0 - bg0 + bb0)
    a1_exp = -0.1 * bg0
    a1_ok = abs(a1_obs - a1_exp) <= tau_num
    a2_obs = (bp0 - bg0 - bb0) - (bp0 - bg0 + bb0)
    a2_exp = -2.0 * bb0
    a2_ok = abs(a2_obs - a2_exp) <= tau_num
    return {"status": "OK" if (a1_ok and a2_ok) else "HARNESS INVALID",
            "integrity_status": "VERIFIED", "tau_num": tau_num,
            "anchor1_gfvec_scale": {"observed": a1_obs, "expected": a1_exp,
                                    "pass": bool(a1_ok)},
            "anchor2_boson_sign": {"observed": a2_obs, "expected": a2_exp,
                                   "pass": bool(a2_ok)}}


# ----------------------------- driver -----------------------------
def run(json_path):
    ok, doc, log = refuse_checks(json_path)
    result = {"refuse_log": log}
    if not ok:
        result.update(status="REFUSED", integrity_status="REFUSED",
                      scientific_status="HARNESS_INVALID")
        return result
    result.update(status="verified", integrity_status="VERIFIED",
                  arm=doc["arm"], non_decisive=(doc["arm"] == "pilot"))
    subresults = []
    if {"proca", "gfvec", "boson"} <= set(doc["arm_config"]["species"]):
        result["audit"] = audit(doc)
        result["historical_criterion"] = historical_criterion(doc)
        result["seagull_diagnostic"] = seagull_diagnostic(doc)
        subresults += [result["audit"], result["historical_criterion"]]
    if set(doc["arm_config"]["species"]) == {"proca", "boson"}:
        result["numrepro"] = numrepro(doc)
        subresults.append(result["numrepro"])
    harness_invalid = any(sr.get("harness_invalid", False) for sr in subresults)
    result["scientific_status"] = ("HARNESS_INVALID" if harness_invalid
                                   else "ASSESSABLE")
    return result


def _exit_code(res):
    return 0 if (res.get("integrity_status") == "VERIFIED"
                 and res.get("scientific_status") == "ASSESSABLE") else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--mutation-check", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("--mutated")
    args = ap.parse_args(argv)
    if args.mutation_check:
        res = mutation_check(args.base, args.mutated)
        code = 0 if res.get("status") == "OK" else 1
    else:
        res = run(args.json)
        code = _exit_code(res)
    print(json.dumps(res, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())
