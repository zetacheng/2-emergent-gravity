"""Blind compute harness for the P2-BETAV decisive campaign.

Emits raw Z(m) tables and fitted betas per species/variant to frozen JSON with
an EXTERNAL sha256 sidecar. Contains NO target numbers and prints NO ratios,
verdicts, or bands (see the prereg document, section (g)). The comparison and
all acceptance rules live in `compare.py`, a separate, later-committed script.

Rules are frozen in `derivations/P2-BETAV-CAMPAIGN_prereg.md`; this file imports
the recovered scientific *functions* (never their target-bearing docstrings /
drivers) and reproduces the one-line `slope*` wrappers so that eps-fit
diagnostics are exposed.

Usage::

    python scripts/P2-BETAV-CAMPAIGN/harness_compute.py --arm pilot
    python scripts/P2-BETAV-CAMPAIGN/harness_compute.py --arm H
    python scripts/P2-BETAV-CAMPAIGN/harness_compute.py --arm P
    python scripts/P2-BETAV-CAMPAIGN/harness_compute.py --arm pilot --mutate gfvec_scale
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "p2-betav-campaign/compute/v2"

# Per-arm frozen required-diagnostics manifest (prereg §(c7) / schema addition).
# Audit-shaped arms (P, pilot) require both diagnostics; Arm H requires none.
REQUIRED_DIAGNOSTICS = {
    "P": ["gfvec-v2-seagull", "extended-basis"],
    "pilot": ["gfvec-v2-seagull", "extended-basis"],
    "H": [],
}

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[1]
_REC = _ROOT / "scripts" / "recovered_2026"
_BATCH2 = _REC / "batch2"

# Controlled loader: recovered parent modules first, gfvec_loop (batch2) after,
# so `import gfvec_loop` resolves in batch2 while its bare `from proca_loop
# import ...` resolves in the parent. No originals are copied or edited.
for _p in (str(_REC), str(_BATCH2)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import boson_loop  # noqa: E402
import gfvec_loop  # noqa: E402
import mlog_coeff  # noqa: E402
import proca_loop  # noqa: E402
import seagull_check  # noqa: E402,F401  (registered source; loaded for hash+import check)

# Registered source set (frozen; see prereg "Registered source set").
REGISTERED_SOURCES = {
    "proca_loop.py": _REC / "proca_loop.py",
    "gfvec_loop.py": _BATCH2 / "gfvec_loop.py",
    "mlog_coeff.py": _REC / "mlog_coeff.py",
    "boson_loop.py": _REC / "boson_loop.py",
    "seagull_check.py": _REC / "seagull_check.py",
    "harness_compute.py": _HERE / "harness_compute.py",
}
PREREG_DOC = _ROOT / "derivations" / "P2-BETAV-CAMPAIGN_prereg.md"

# ----------------------------- frozen configs -----------------------------
# Eps and mass grids frozen BY VALUE (never by reference to a module default).
CONFIG = {
    "H": {
        "n": 32,
        "species": ["proca", "boson"],
        "eps": [0.10, 0.16, 0.22, 0.28],
        "masses_baseline": [0.11, 0.14, 0.17, 0.20],
        "masses_shift": [0.12, 0.15, 0.18],
    },
    "P": {
        "n": 48,
        "species": ["proca", "gfvec", "boson"],
        "eps": [0.08, 0.13, 0.18, 0.23],
        "masses_baseline": [0.05, 0.065, 0.08, 0.10, 0.12],
        "masses_shift": [],
    },
    "pilot": {
        "n": 16,
        "species": ["proca", "gfvec", "boson"],
        "eps": [0.10, 0.16, 0.22, 0.28],  # Amendment 1 (A1): 4 pts == EPS_H
        "masses_baseline": [0.10, 0.12, 0.14, 0.17, 0.20],
        "masses_shift": [],
    },
}


def _mass_union(cfg):
    seen, out = set(), []
    for m in list(cfg["masses_baseline"]) + list(cfg["masses_shift"]):
        key = repr(m)
        if key not in seen:
            seen.add(key)
            out.append(m)
    return out


def _variant_table(arm, cfg):
    """Frozen per-arm variant table (prereg (c4)). Returns a list of dicts:
    name, cls (VERDICT/DIAGNOSTIC-ONLY), eps (list), masses (list), basis."""
    eps = list(cfg["eps"])
    mb = list(cfg["masses_baseline"])
    ms = list(cfg["masses_shift"])
    audit_arm = arm in ("P", "pilot")  # three-species / audit shape
    v = []
    v.append(dict(name="baseline", cls="VERDICT", eps=eps, masses=mb, basis="m4"))
    v.append(dict(name="eps-drop-largest", cls="VERDICT", eps=eps[:-1],
                  masses=mb, basis="m4"))
    v.append(dict(name="eps-drop-smallest", cls="VERDICT", eps=eps[1:],
                  masses=mb, basis="m4"))
    v.append(dict(name="fit-order", cls="VERDICT", eps=eps, masses=mb,
                  basis="nom4"))
    # mass-drop-one: Arm H forces nom4 (frozen; 3 pts < 4 cols otherwise).
    drop_basis = "nom4" if arm == "H" else "m4"
    for i in range(len(mb)):
        v.append(dict(name=f"mass-drop-one[{i}]", cls="VERDICT", eps=eps,
                      masses=[mb[j] for j in range(len(mb)) if j != i],
                      basis=drop_basis))
    if arm == "H":
        v.append(dict(name="window-shift", cls="VERDICT", eps=eps, masses=ms,
                      basis="nom4"))
    if audit_arm:
        v.append(dict(name="gfvec-v2-seagull", cls="DIAGNOSTIC-ONLY", eps=eps,
                      masses=mb, basis="m4"))
        v.append(dict(name="extended-basis", cls="DIAGNOSTIC-ONLY", eps=eps,
                      masses=mb, basis="ext5"))
    return v


# ----------------------------- fit helpers -----------------------------
def _mass_design(m2, basis):
    m2 = np.asarray(m2, dtype=float)
    cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
    if basis in ("m4", "ext5"):
        cols.append(m2 ** 2)
    if basis == "ext5":
        cols.append(m2 ** 2 * np.log(m2))
    return np.stack(cols, axis=1)


def _mass_fit(masses, zvals, basis):
    """fit_mlog-faithful mass fit with full diagnostics. beta = coef[2]."""
    m2 = np.asarray(masses, dtype=float) ** 2
    y = np.asarray(zvals, dtype=float)
    A = _mass_design(m2, basis)
    npts, ncol = A.shape
    out = {"basis": basis, "n_points": int(npts), "n_columns": int(ncol),
           "dof": int(npts - ncol)}
    if npts < ncol:
        out.update(valid=False, reason="underdetermined (n_points<n_columns)",
                   beta=None, coef=None, rank=int(np.linalg.matrix_rank(A)),
                   cond=None, resid=None)
        return out
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    rank = int(np.linalg.matrix_rank(A))
    cond = float(np.linalg.cond(A))
    resid = float(np.abs(A @ coef - y).max())
    finite = bool(np.all(np.isfinite(coef)))
    valid = bool(finite and rank == ncol and np.isfinite(cond) and cond <= 1e12)
    out.update(valid=valid, beta=float(coef[2]),
               coef=[float(c) for c in coef], rank=rank, cond=cond,
               resid=resid,
               residual_note=("dof=0 (residual vacuous)" if npts == ncol
                              else "ok"))
    return out


def _eps_fit(eps, vals):
    """fit_even(order=2)-faithful eps fit. Z = coef[1] (eps^2 coefficient)."""
    eps = np.asarray(eps, dtype=float)
    vals = np.asarray(vals, dtype=float)
    A = np.vander(eps ** 2, 3, increasing=True)
    npts, ncol = A.shape
    d = {"n_points": int(npts), "n_columns": int(ncol), "dof": int(npts - ncol)}
    if npts < ncol:
        d.update(valid=False, reason="underdetermined (n_points<n_columns)",
                 Z=None, rank=int(np.linalg.matrix_rank(A)), cond=None,
                 resid=None)
        return d
    coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
    rank = int(np.linalg.matrix_rank(A))
    cond = float(np.linalg.cond(A))
    resid = float(np.abs(A @ coef - vals).max())
    valid = bool(np.all(np.isfinite(coef)) and rank == ncol
                 and np.isfinite(cond) and cond <= 1e12)
    d.update(valid=valid, Z=float(coef[1]), rank=rank, cond=cond, resid=resid,
             residual_note=("dof=0 (residual vacuous)" if npts == ncol
                            else "ok"))
    return d


# ----------------------------- physics kernels -----------------------------
def _build_derivs(species_set):
    D = {}
    if "proca" in species_set:
        dJ2, dJ, _, _ = proca_loop.derivsV()
        D["proca"] = (dJ2, dJ)
    if "gfvec" in species_set:
        D["gfvec"] = gfvec_loop.derivsGF()          # (dJ2, dJ, dE)
        D["gfvec2"] = gfvec_loop.derivs2GF()        # (d2J, d2E)
    if "boson" in species_set:
        dJ, dE, _, _ = boson_loop.derivsB()
        D["boson"] = (dJ, dE)
    return D


def _kernel(species, e, n, m, D):
    if species == "proca":
        return float(proca_loop.g2_axis_proca(e, n, m, D["proca"][0],
                                              D["proca"][1]))
    if species == "gfvec":
        return float(gfvec_loop.g2_axis_gfvec(e, n, m, *D["gfvec"]))
    if species == "gfvec_v2":
        return float(gfvec_loop.g2_axis_gfvec_v2(e, n, m, *D["gfvec"],
                                                 *D["gfvec2"]))
    if species == "boson":
        return float(mlog_coeff.g2_axis_boson(e, n, m, D["boson"][0],
                                              D["boson"][1]))
    raise ValueError(species)


# ----------------------------- metadata -----------------------------
def _sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _git_head():
    try:
        return subprocess.check_output(
            ["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
            text=True).strip()
    except Exception as exc:  # pragma: no cover
        return f"unknown ({exc})"


def _blas_info():
    info = {}
    try:
        cfg = np.__config__.show(mode="dicts")  # numpy >= 1.25
        if isinstance(cfg, dict):
            info = {k: cfg[k] for k in cfg if "blas" in k.lower()
                    or "lapack" in k.lower()}
    except Exception:
        try:
            info = {"blas_opt": str(np.__config__.get_info("blas_opt"))}
        except Exception:
            info = {"note": "blas info unavailable"}
    return info


# ----------------------------- driver -----------------------------
def compute(arm, mutate="none"):
    cfg = CONFIG[arm]
    n = cfg["n"]
    species_set = list(cfg["species"])
    kernels = list(species_set)
    if "gfvec" in species_set:
        kernels.append("gfvec_v2")  # for the diagnostic-only v2 variant
    masses = _mass_union(cfg)
    eps_full = list(cfg["eps"])

    D = _build_derivs(species_set)

    # Master raw g2-axis table: species -> mass -> eps -> value.
    raw = {sp: {} for sp in kernels}
    for sp in kernels:
        for m in masses:
            raw[sp][repr(m)] = {repr(e): _kernel(sp, e, n, m, D)
                                for e in eps_full}

    def z_series(sp_kernel, variant, scale=1.0):
        """Z(m) over the variant's masses/eps, with eps-fit diagnostics."""
        zdict, epsdiag = {}, {}
        for m in variant["masses"]:
            vals = [raw[sp_kernel][repr(m)][repr(e)] * scale
                    for e in variant["eps"]]
            fit = _eps_fit(variant["eps"], vals)
            epsdiag[repr(m)] = fit
            zdict[repr(m)] = fit["Z"]
        return zdict, epsdiag

    variants_out = {}
    for var in _variant_table(arm, cfg):
        vres = {"class": var["cls"], "eps": var["eps"], "masses": var["masses"],
                "basis": var["basis"], "species": {}}
        # which kernel per species label in this variant
        sp_labels = list(species_set)
        if var["name"] == "gfvec-v2-seagull":
            # replace gfvec bubble by the v2 kernel for this diagnostic
            sp_labels = ["gfvec_v2" if s == "gfvec" else s for s in sp_labels]
        for sp in sp_labels:
            scale = 1.1 if (mutate == "gfvec_scale"
                            and sp in ("gfvec", "gfvec_v2")) else 1.0
            zdict, epsdiag = z_series(sp, var, scale=scale)
            zvals = [zdict[repr(m)] for m in var["masses"]]
            if any(z is None for z in zvals):
                mfit = {"valid": False, "reason": "eps-fit invalid",
                        "basis": var["basis"], "beta": None,
                        "n_points": len(zvals)}
            else:
                mfit = _mass_fit(var["masses"], zvals, var["basis"])
            vres["species"][sp] = {"Z": zdict, "eps_fits": epsdiag,
                                   "mass_fit": mfit}
        variants_out[var["name"]] = vres

    required_diags, diagnostics = _build_diagnostics(arm, variants_out)

    doc = {
        "schema_version": SCHEMA_VERSION,
        "arm": arm,
        "mutation": mutate,
        "required_diagnostics": required_diags,
        "diagnostics": diagnostics,
        "compute_git_commit": _git_head(),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "platform": platform.platform(),
        "blas_info": _blas_info(),
        "prereg_sha256": _sha256_file(PREREG_DOC),
        "registered_sources": {
            name: {"path": str(p.relative_to(_ROOT)), "sha256": _sha256_file(p)}
            for name, p in REGISTERED_SOURCES.items()},
        "arm_config": {"n": n, "species": species_set, "eps": eps_full,
                       "masses_union": masses,
                       "masses_baseline": cfg["masses_baseline"],
                       "masses_shift": cfg["masses_shift"],
                       "variant_table_id": f"prereg-c4/{arm}"},
        "raw_g2axis": raw,
        "variants": variants_out,
    }
    return doc


def _build_diagnostics(arm, variants_out):
    """Frozen required-diagnostics manifest + structured keyed records
    (prereg §(c7) / schema addition). Comparator iterates the manifest."""
    req = list(REQUIRED_DIAGNOSTICS.get(arm, []))
    diags = {}
    for did in req:
        if did == "gfvec-v2-seagull":
            v = variants_out.get("gfvec-v2-seagull")
            executed = v is not None and "gfvec_v2" in v.get("species", {})
            valid = bool(executed and v["species"]["gfvec_v2"]["mass_fit"]
                         .get("valid", False))
            diags[did] = {
                "executed": bool(executed), "valid": valid,
                "record_path": "variants.gfvec-v2-seagull.species.gfvec_v2"}
        elif did == "extended-basis":
            v = variants_out.get("extended-basis")
            executed = v is not None
            comps = {}
            if executed:
                masses = v["masses"]
                for sp in ("proca", "gfvec", "boson"):
                    mf = v["species"].get(sp, {}).get("mass_fit", {})
                    comps[sp] = {
                        "valid": bool(mf.get("valid", False)),
                        "record_path":
                            f"variants.extended-basis.species.{sp}.mass_fit"}
                # the D = Z_P - Z_G + Z_B component, extended (5-column) fit
                try:
                    zc = {s: [v["species"][s]["Z"][repr(m)] for m in masses]
                          for s in ("proca", "gfvec", "boson")}
                    dz = [zc["proca"][i] - zc["gfvec"][i] + zc["boson"][i]
                          for i in range(len(masses))]
                    dfit = _mass_fit(masses, dz, "ext5")
                    comps["D"] = {"valid": bool(dfit.get("valid", False)),
                                  "mass_fit": dfit,
                                  "record_path":
                                  "diagnostics.extended-basis.components.D"}
                except Exception as exc:  # pragma: no cover
                    comps["D"] = {"valid": False, "error": str(exc),
                                  "record_path":
                                  "diagnostics.extended-basis.components.D"}
            allv = bool(executed and all(
                comps.get(c, {}).get("valid", False)
                for c in ("proca", "gfvec", "boson", "D")))
            diags[did] = {
                "executed": bool(executed), "valid": allv,
                "record_path": "variants.extended-basis",
                "required_components": ["proca", "gfvec", "boson", "D"],
                "components": comps}
    return req, diags


def _out_paths(arm, mutate):
    base = f"{arm}" if mutate == "none" else f"{arm}_mut_{mutate}"
    out_dir = _ROOT / "results" / "P2-BETAV-CAMPAIGN" / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{base}.json", out_dir / f"{base}.json.sha256"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=["H", "P", "pilot"])
    ap.add_argument("--mutate", default="none",
                    choices=["none", "gfvec_scale"])
    args = ap.parse_args(argv)
    if args.mutate != "none" and args.arm != "pilot":
        ap.error("mutations are pilot-only (prereg (e))")

    doc = compute(args.arm, mutate=args.mutate)
    json_path, sidecar_path = _out_paths(args.arm, args.mutate)
    payload = json.dumps(doc, indent=2, sort_keys=True) + "\n"
    json_path.write_text(payload, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    sidecar_path.write_text(f"{digest}  {json_path.name}\n",
                            encoding="utf-8", newline="\n")
    # Blind status line only: NO ratios, NO betas, NO verdicts.
    nvar = len(doc["variants"])
    print(f"[harness_compute] arm={args.arm} mutate={args.mutate} "
          f"variants={nvar} masses={len(doc['arm_config']['masses_union'])} "
          f"wrote {json_path.relative_to(_ROOT)} (+sidecar)")


if __name__ == "__main__":
    main()
