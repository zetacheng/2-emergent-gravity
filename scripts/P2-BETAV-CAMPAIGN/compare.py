"""Comparison / acceptance stage for the P2-BETAV decisive campaign.

Separate from the blind compute harness (prereg (g)). Reads a frozen compute
JSON, REFUSES to run unless five integrity checks pass in order, then applies
the pre-registered acceptance rules (prereg (c1)-(c6)) and emits a verdict
table with diagnostics reported separately.

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

SCHEMA_VERSION = "p2-betav-campaign/compute/v1"

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
    """Five checks, IN ORDER (prereg compare.py contract). Returns (ok, doc,
    log). Stops at the first failure."""
    log = []
    json_path = Path(json_path)
    # (1) sidecar hash verifies
    sidecar = Path(str(json_path) + ".sha256")
    if not sidecar.exists():
        return False, None, log + ["(1) sidecar missing"]
    want = sidecar.read_text().split()[0]
    got = hashlib.sha256(json_path.read_bytes()).hexdigest()
    if want != got:
        return False, None, log + [f"(1) sidecar hash mismatch {got}!={want}"]
    log.append("(1) sidecar hash OK")
    doc = json.loads(json_path.read_text())
    # (2) prereg-document hash recorded in JSON matches working tree
    prereg = _ROOT / "derivations" / "P2-BETAV-CAMPAIGN_prereg.md"
    if doc.get("prereg_sha256") != _sha256_file(prereg):
        return False, None, log + ["(2) prereg-doc hash mismatch"]
    log.append("(2) prereg-doc hash OK")
    # (3) registered-source hashes match working tree
    for name, rec in doc.get("registered_sources", {}).items():
        p = _ROOT / rec["path"]
        if not p.exists() or _sha256_file(p) != rec["sha256"]:
            return False, None, log + [f"(3) source hash mismatch: {name}"]
    log.append("(3) registered-source hashes OK")
    # (4) recorded compute commit is an ancestor of HEAD
    commit = doc.get("compute_git_commit", "")
    if not _is_ancestor(commit):
        return False, None, log + [f"(4) compute commit not ancestor: {commit}"]
    log.append("(4) compute commit is ancestor of HEAD")
    # (5) schema version matches
    if doc.get("schema_version") != SCHEMA_VERSION:
        return False, None, log + ["(5) schema version mismatch"]
    log.append("(5) schema version OK")
    return True, doc, log


# ----------------------------- rule application -----------------------------
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
    bg, vg = _beta(doc, "baseline", "gfvec")
    mags = [abs(x) for x in (bp, bg, bb) if x is not None]
    m = max(mags) if mags else 0.0
    tau_num = FLOOR_ABS + FLOOR_REL * m
    tau_denom = tau_num  # same max-of-baseline construction
    return tau_num, tau_denom, bp, bg, bb


def audit(doc):
    """Arm-P operator-identity audit (prereg (c1))."""
    out = {"kind": "audit"}
    species = doc["arm_config"]["species"]
    if not {"proca", "gfvec", "boson"} <= set(species):
        out["verdict"] = "N/A (arm has no gfvec; audit is Arm-P only)"
        return out
    tau_num, tau_denom, bp0, bg0, bb0 = _baseline_floor(doc)
    if bb0 is None or abs(bb0) <= tau_denom:
        out["verdict"] = "HARNESS INVALID / AUDIT INCONCLUSIVE"
        out["reason"] = "baseline denominator invalid"
        return out
    tau_C = tau_num / abs(bb0)

    # paired C_cons per valid verdict variant; validity + denominator checks
    ccons = {}
    invalid = []
    xchecks = {}
    for var in _verdict_variants(doc):
        bp, vp = _beta(doc, var, "proca")
        bg, vg = _beta(doc, var, "gfvec")
        bb, vb = _beta(doc, var, "boson")
        if not (vp and vg and vb):
            invalid.append((var, "a fit invalid"))
            continue
        if abs(bb) <= tau_denom or (bb0 != 0 and (bb > 0) != (bb0 > 0)):
            invalid.append((var, "denominator invalid/sign-flip"))
            continue
        R = bp - bg + bb
        ccons[var] = R / abs(bb)
        # Tier-1<->Tier-2 machine cross-check for this variant
        beta_D = _fit_D(doc, var)
        if beta_D is None:
            xchecks[var] = ("no-D", None)
        else:
            xchecks[var] = ("ok", abs(beta_D - R))
    out["invalid_verdict_variants"] = invalid
    if invalid:
        out["verdict"] = "HARNESS INVALID / AUDIT INCONCLUSIVE"
        out["reason"] = "one or more verdict variants invalid"
        return out
    # cross-checks must pass for EVERY verdict variant
    xfail = [v for v, (s, d) in xchecks.items()
             if s == "no-D" or (d is not None and d > tau_num)]
    out["xcheck_tau_num"] = tau_num
    out["xcheck_max"] = max((d for _, d in xchecks.values() if d is not None),
                            default=None)
    if xfail:
        out["verdict"] = "HARNESS INVALID / AUDIT INCONCLUSIVE"
        out["reason"] = f"Tier1<->Tier2 cross-check failed: {xfail}"
        return out
    c_base = ccons["baseline"]
    sigma_C = max((abs(ccons[v] - c_base) for v in ccons), default=0.0)
    tol = max(2 * sigma_C, tau_C)
    out.update(C_cons_baseline=c_base, sigma_C=sigma_C, tau_C=tau_C,
               tol=tol, twosigma=2 * sigma_C, delta_audit=DELTA_AUDIT)
    # ratios with (c0) uncertainties
    out["gfvec_over_B"] = _ratio_battery(doc, "gfvec", "boson")
    out["proca_over_B"] = _ratio_battery(doc, "proca", "boson")
    if 2 * sigma_C > DELTA_AUDIT:
        out["verdict"] = "INCONCLUSIVE (insufficient resolving power)"
    elif abs(c_base) <= tol:
        out["verdict"] = "PASS"
    else:
        out["verdict"] = "FAIL"
    return out


def _fit_D(doc, variant):
    """beta of D(m)=Z_proca-Z_gfvec+Z_boson via the recovered fit basis."""
    v = doc["variants"][variant]
    masses = v["masses"]
    basis = v["basis"]
    try:
        import numpy as np
        zc = {}
        for sp in ("proca", "gfvec", "boson"):
            zc[sp] = [v["species"][sp]["Z"][repr(m)] for m in masses]
        D = [zc["proca"][i] - zc["gfvec"][i] + zc["boson"][i]
             for i in range(len(masses))]
        m2 = np.asarray(masses, float) ** 2
        cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
        if basis in ("m4", "ext5"):
            cols.append(m2 ** 2)
        if basis == "ext5":
            cols.append(m2 ** 2 * np.log(m2))
        A = np.stack(cols, axis=1)
        if A.shape[0] < A.shape[1]:
            return None
        coef, *_ = np.linalg.lstsq(A, np.asarray(D, float), rcond=None)
        return float(coef[2])
    except Exception:
        return None


def _ratio_battery(doc, num, den):
    """Paired ratio num/den, central=baseline, sigma over valid verdict
    variants (prereg (c0))."""
    vals = {}
    for var in _verdict_variants(doc):
        bn, vn = _beta(doc, var, num)
        bd, vd = _beta(doc, var, den)
        if vn and vd and bd not in (None, 0):
            vals[var] = bn / bd
    if "baseline" not in vals:
        return {"central": None, "sigma": None, "n_variants": len(vals)}
    c = vals["baseline"]
    sigma = max((abs(vals[v] - c) for v in vals), default=0.0)
    return {"central": c, "sigma": sigma, "n_variants": len(vals),
            "per_variant": vals}


def numrepro(doc):
    """Arm-H NUMREPRO (prereg (c2)). R_H = beta_proca/beta_boson."""
    out = {"kind": "numrepro"}
    rb = _ratio_battery(doc, "proca", "boson")
    if rb["central"] is None:
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = "no valid baseline ratio"
        return out
    # denominator sign stability across verdict variants
    signs = set()
    for var in _verdict_variants(doc):
        bb, vb = _beta(doc, var, "boson")
        if vb and bb is not None:
            signs.add(bb > 0)
    R, sigma = rb["central"], rb["sigma"]
    lo, hi = R - 2 * sigma, R + 2 * sigma
    out.update(R_H=R, sigma_H=sigma, interval=[lo, hi], band=list(NUMREPRO_BAND),
               denom_sign_stable=(len(signs) == 1))
    if len(signs) != 1:
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = "beta_B crosses zero across variants"
        return out
    if NUMREPRO_BAND[0] <= lo and hi <= NUMREPRO_BAND[1]:
        out["verdict"] = "PASS"
    elif hi < NUMREPRO_BAND[0] or lo > NUMREPRO_BAND[1]:
        out["verdict"] = "FAIL"
    else:
        out["verdict"] = "INCONCLUSIVE"
    return out


def historical_criterion(doc):
    """Arm-P recorded outcome (prereg (c5)); recorded, not an action."""
    gf = _ratio_battery(doc, "gfvec", "boson")
    pr = _ratio_battery(doc, "proca", "boson")
    if gf["central"] is None or pr["central"] is None:
        return {"kind": "historical-criterion", "outcome": "N/A"}
    gf_ok = (CRIT_GFVEC_BAND[0] <= gf["central"] <= CRIT_GFVEC_BAND[1]
             and gf["sigma"] is not None and gf["sigma"] <= CRIT_SIGMA_GF)
    pr_ok = (CRIT_PROCA_BAND[0] <= pr["central"] <= CRIT_PROCA_BAND[1]
             and pr["sigma"] is not None and pr["sigma"] <= CRIT_SIGMA_PROCA)
    return {"kind": "historical-criterion",
            "gfvec_over_B": gf, "proca_over_B": pr,
            "met": bool(gf_ok and pr_ok),
            "note": "recorded outcome; promotion is a separate PI+reviewer step"}


def seagull_diagnostic(doc):
    """gfvec-v2 vs bubble sensitivity (prereg (a2)/(c6)); diagnostic-only."""
    if "gfvec-v2-seagull" not in doc["variants"]:
        return {"kind": "seagull", "status": "not present"}
    v2 = doc["variants"]["gfvec-v2-seagull"]["species"].get("gfvec_v2", {})
    base = doc["variants"]["baseline"]["species"].get("gfvec", {})
    if not v2 or not base:
        return {"kind": "seagull", "status": "HARNESS INVALID (missing series)"}
    masses = doc["variants"]["gfvec-v2-seagull"]["masses"]
    import numpy as np
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
    _, _, _, _, bb0 = _baseline_floor(doc)
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
        return {"status": "REFUSED (base)", "log": log}
    ok2, mut, log2 = refuse_checks(mutated_path)
    if not ok2:
        return {"status": "REFUSED (mutated)", "log": log2}
    tau_num, _, bp0, bg0, bb0 = _baseline_floor(base)
    # anchor 1: gfvec scale x1.1 -> Delta R_cons = -0.1 * beta_gfvec(base)
    bpm, _ = _beta(mut, "baseline", "proca")
    bgm, _ = _beta(mut, "baseline", "gfvec")
    bbm, _ = _beta(mut, "baseline", "boson")
    R_base = bp0 - bg0 + bb0
    R_mut = bpm - bgm + bbm
    a1_obs = R_mut - R_base
    a1_exp = -0.1 * bg0
    a1_ok = abs(a1_obs - a1_exp) <= tau_num
    # anchor 2: boson sign flip in the combination (base JSON alone)
    R_signflip = bp0 - bg0 - bb0
    a2_obs = R_signflip - R_base
    a2_exp = -2.0 * bb0
    a2_ok = abs(a2_obs - a2_exp) <= tau_num
    return {"status": "OK" if (a1_ok and a2_ok) else "HARNESS INVALID",
            "tau_num": tau_num,
            "anchor1_gfvec_scale": {"observed": a1_obs, "expected": a1_exp,
                                    "pass": bool(a1_ok)},
            "anchor2_boson_sign": {"observed": a2_obs, "expected": a2_exp,
                                   "pass": bool(a2_ok)}}


# ----------------------------- driver -----------------------------
def run(json_path):
    ok, doc, log = refuse_checks(json_path)
    result = {"refuse_log": log}
    if not ok:
        result["status"] = "REFUSED"
        return result
    result["status"] = "verified"
    result["arm"] = doc["arm"]
    result["non_decisive"] = (doc["arm"] == "pilot")
    if {"proca", "gfvec", "boson"} <= set(doc["arm_config"]["species"]):
        result["audit"] = audit(doc)
        result["historical_criterion"] = historical_criterion(doc)
        result["seagull_diagnostic"] = seagull_diagnostic(doc)
    if set(doc["arm_config"]["species"]) == {"proca", "boson"}:
        result["numrepro"] = numrepro(doc)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--mutation-check", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("--mutated")
    args = ap.parse_args(argv)
    if args.mutation_check:
        res = mutation_check(args.base, args.mutated)
    else:
        res = run(args.json)
    print(json.dumps(res, indent=2, sort_keys=True))
    # exit non-zero only on integrity refusal / harness invalidity
    bad = res.get("status") in ("REFUSED", "HARNESS INVALID") \
        or res.get("status", "").startswith("REFUSED")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
