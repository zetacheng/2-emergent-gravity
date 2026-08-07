"""`P2-PHASE-01`: Fierz-matrix verification and stationary-branch depths.

Two derivations, neither of which decides anything:

(a) an independent symbolic reconstruction of the 5x5 representation-family
    Fierz matrix from the Phase-A freeze conventions, proved equal to the
    frozen ``matrix_rational`` entry by entry as exact rationals, together
    with the basis-completeness, trace-normalisation, generator-normalisation
    and involution checks;

(b) the value of the reduced scalar effective potential at every stationary
    branch recorded by the pinned exploratory study, using that study's own
    potential reconstruction.

This is not a gate computation.  It selects no Hubbard-Stratonovich channel,
no V/A/T orientation, and no potential zero, and it characterises no branch.
"""

from __future__ import annotations

import decimal
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# The reduced potential is NOT reconstructed here.  It is imported from the
# pinned exploratory study so that the quadrature, the Gauss-Legendre order
# and the grid construction are identical to the run that produced the roots.
from p2_phase01_scalar_exploratory import (  # noqa: E402
    WilsonQuadrature,
    first_derivative,
    reconstructed_potential,
)

FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
EXPLORATORY = (ROOT / "results/P2-PHASE-01/exploratory-scalar-stationary"
               / "scalar_stationary.json")
OUT = (ROOT / "results/P2-PHASE-01/fierz-and-branch-depths"
       / "fierz_and_depths.json")

BASIS_ORDER = ["S", "P", "V", "A", "T"]
GRASSMANN_CROSSING_SIGN = -1
STORED_DECIMALS = 12

# ---------------------------------------------------------------- (a) ----
_PAULI = [sp.Matrix([[0, 1], [1, 0]]),
          sp.Matrix([[0, -sp.I], [sp.I, 0]]),
          sp.Matrix([[1, 0], [0, -1]])]


def _blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


def euclidean_gammas():
    """Hermitian Euclidean gammas for metric_signature (1,1,1,1)."""
    i2, z2 = sp.eye(2), sp.zeros(2)
    return [_blk(z2, i2, i2, z2)] + [
        _blk(z2, -sp.I * _PAULI[k], sp.I * _PAULI[k], z2) for k in range(3)
    ]


def dirac_basis():
    """The sixteen elements, grouped by family, in basis_order."""
    g = euclidean_gammas()
    # gamma5_definition (PI ruling of 2026-08-07): no extra factor of I.
    g5 = g[0] * g[1] * g[2] * g[3]
    # sigma_definition
    def sigma(mu, nu):
        return sp.I * (g[mu] * g[nu] - g[nu] * g[mu]) / 2
    return {
        "S": [sp.eye(4)],
        "P": [g5],
        "V": [g[m] for m in range(4)],
        "A": [sp.I * g[m] * g5 for m in range(4)],
        "T": [sigma(m, n) for m in range(4) for n in range(m + 1, 4)],
    }, g, g5


def reconstruct_matrix(fams):
    """M[a][c] = (1/16) Sum_i trace(G^a_i G^c_k G^a_i G^c_k), any fixed k.

    Returns the matrix WITHOUT the Grassmann crossing sign, and the
    k-independence evidence for the projection formula.
    """
    rows, kindep = [], []
    for a in BASIS_ORDER:
        row = []
        for c in BASIS_ORDER:
            vals = []
            for gck in fams[c]:
                tot = sp.Integer(0)
                for gai in fams[a]:
                    tot += sp.trace(gai * gck * gai * gck)
                vals.append(sp.nsimplify(sp.simplify(tot / 16)))
            kindep.append({
                "a": a, "c": c,
                "values_over_components": [str(v) for v in vals],
                "k_independent": bool(all(sp.simplify(v - vals[0]) == 0
                                          for v in vals)),
            })
            row.append(sp.Rational(vals[0]))
        rows.append(row)
    return sp.Matrix(rows), kindep


def kernel_identity_holds(fams, M):
    """Demonstrate the 256-component tensor equality the matrix asserts."""
    report = {}
    for a in BASIS_ORDER:
        lhs = {}
        for gai in fams[a]:
            for al in range(4):
                for be in range(4):
                    for ga in range(4):
                        for de in range(4):
                            k = (al, be, ga, de)
                            lhs[k] = lhs.get(k, 0) + gai[al, be] * gai[ga, de]
        rhs = {}
        for bi, b in enumerate(BASIS_ORDER):
            coeff = M[BASIS_ORDER.index(a), bi]
            if coeff == 0:
                continue
            for gbj in fams[b]:
                for al in range(4):
                    for be in range(4):
                        for ga in range(4):
                            for de in range(4):
                                k = (al, be, ga, de)
                                rhs[k] = rhs.get(k, 0) + coeff * \
                                    gbj[al, de] * gbj[ga, be]
        residual = max(
            abs(sp.simplify(lhs.get(k, 0) - rhs.get(k, 0)))
            for k in set(lhs) | set(rhs)
        )
        report[a] = {"components_checked": 256,
                     "max_abs_residual": str(sp.simplify(residual)),
                     "holds": bool(sp.simplify(residual) == 0)}
    return report


def basis_checks(fams, g, g5):
    """Deliverable 5: completeness, trace normalisation, hermiticity."""
    flat = [(f, i, m) for f in BASIS_ORDER for i, m in enumerate(fams[f])]
    cols = [sp.Matrix(16, 1, lambda r, _c: m[r // 4, r % 4]) for _, _, m in flat]
    span = sp.Matrix.hstack(*cols)
    trace_const = {}
    ortho_ok = True
    for f in BASIS_ORDER:
        consts = {sp.simplify(sp.trace(m * m)) for m in fams[f]}
        trace_const[f] = str(consts.pop()) if len(consts) == 1 else "NON-UNIFORM"
    for fa, ia, ma in flat:
        for fb, ib, mb in flat:
            t = sp.simplify(sp.trace(ma * mb))
            want = 4 if (fa == fb and ia == ib) else 0
            if t != want:
                ortho_ok = False
    return {
        "element_count": len(flat),
        "rank_of_span": int(span.rank()),
        "spans_4x4_matrices": int(span.rank()) == 16,
        "linearly_independent": int(span.rank()) == len(flat),
        "trace_Id4": str(sp.trace(sp.eye(4))),
        "all_hermitian": bool(all(sp.simplify(m.H - m) == sp.zeros(4)
                                  for _, _, m in flat)),
        "all_square_to_Id4": bool(all(sp.simplify(m * m - sp.eye(4))
                                      == sp.zeros(4) for _, _, m in flat)),
        "trace_proportionality_constant_per_family": trace_const,
        "orthogonality_trace_GaGb_eq_4delta": ortho_ok,
        "gamma5_hermitian": bool(sp.simplify(g5.H - g5) == sp.zeros(4)),
        "gamma5_squares_to_Id4": bool(sp.simplify(g5 * g5 - sp.eye(4))
                                    == sp.zeros(4)),
        "gammas_hermitian": bool(all(sp.simplify(m.H - m) == sp.zeros(4)
                                     for m in g)),
    }


def _su_n_generators(n):
    """A complete set lam(A), A=0..n^2-1, with trace(lam^A lam^B)=2 delta."""
    mats = [sp.sqrt(sp.Rational(2, n)) * sp.eye(n)]
    for i in range(n):
        for j in range(i + 1, n):
            e = sp.zeros(n)
            e[i, j] = 1
            e[j, i] = 1
            mats.append(e)
            f = sp.zeros(n)
            f[i, j] = -sp.I
            f[j, i] = sp.I
            mats.append(f)
    for k in range(1, n):
        d = sp.zeros(n)
        for i in range(k):
            d[i, i] = 1
        d[k, k] = -k
        mats.append(sp.sqrt(sp.Rational(2, k * (k + 1))) * d)
    return mats


def generator_checks(ns=(2, 3, 4)):
    """Deliverable 5: trace(lam lam)=2 delta and the completeness relation."""
    out = {}
    for n in ns:
        lam = _su_n_generators(n)
        norm_ok = all(
            sp.simplify(sp.trace(lam[a] * lam[b]) - (2 if a == b else 0)) == 0
            for a in range(len(lam)) for b in range(len(lam))
        )
        comp_ok = True
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for m in range(n):
                        lhs = sum(g[i, j] * g[k, m] for g in lam)
                        rhs = 2 * (1 if i == m else 0) * (1 if k == j else 0)
                        if sp.simplify(lhs - rhs) != 0:
                            comp_ok = False
        out[str(n)] = {
            "generator_count": len(lam),
            "expected_count": n * n,
            "trace_lamA_lamB_eq_2delta": bool(norm_ok),
            "completeness_sum_lamA_ij_lamA_kl_eq_2_delta_il_delta_kj": comp_ok,
            "singlet_is_sqrt_2_over_n_times_identity":
                bool(sp.simplify(lam[0] - sp.sqrt(sp.Rational(2, n))
                                 * sp.eye(n)) == sp.zeros(n)),
        }
    return out


def induced_coefficients(frozen):
    """Deliverable 4, applied ONLY to the converted vector."""
    G, N = sp.symbols("G N", positive=True)
    v_canonical = [G / (2 * N), G / (2 * N), 0, 0, 0]
    # (bilinear(lam, I*gamma5))**2 = -(bilinear(lam, gamma5))**2
    v_frozen = [G / (2 * N), -G / (2 * N), 0, 0, 0]
    unit = sp.Matrix([[1, -1, 0, 0, 0]])
    dirac = unit * frozen                      # row vector over [S,P,V,A,T]
    # internal factor: 2 (completeness) * N/2 (Id_N = sqrt(N/2) lam0) = N
    singlet = [sp.simplify(G / (2 * N) * N * dirac[0, j]) for j in range(5)]
    return {
        "canonical_vector_before_conversion":
            {b: str(v) for b, v in zip(BASIS_ORDER, v_canonical)},
        "converted_vector_in_frozen_basis":
            {b: str(v) for b, v in zip(BASIS_ORDER, v_frozen)},
        "conversion_rule":
            "(bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2",
        "dirac_row_after_matrix":
            {b: str(dirac[0, j]) for j, b in enumerate(BASIS_ORDER)},
        "internal_factor_derivation":
            "Sum_A lam(A)_ab lam(A)_cd = 2 delta_ad delta_cb ; "
            "Id_N = sqrt(N/2) lam(0) ; 2 * (N/2) = N",
        "induced_coefficient_singlet":
            {b: str(singlet[j]) for j, b in enumerate(BASIS_ORDER)},
        "induced_coefficient_traceless":
            {b: "0" for b in BASIS_ORDER},
        "traceless_vanishes_because":
            "the exchanged internal structure is Id_N x Id_N, which is pure "
            "singlet under lam(0) = sqrt(2/N) Id_N; no traceless generator "
            "appears. A vanishing coefficient is a result, not an omission.",
    }


def derivation_a():
    fams, g, g5 = dirac_basis()
    M, kindep = reconstruct_matrix(fams)
    F_signed = GRASSMANN_CROSSING_SIGN * M
    frozen_embedded = json.loads(FREEZE.read_text(encoding="utf-8")
                                 .splitlines()[97])["matrix_rational"]
    frozen_standalone = json.loads(FIERZ_JSON.read_text(encoding="utf-8"))
    Fz = sp.Matrix(5, 5, lambda i, j: sp.Rational(
        sp.nsimplify(str(frozen_embedded[i][j]))))
    Sa = sp.Matrix(5, 5, lambda i, j: sp.Rational(
        sp.nsimplify(str(frozen_standalone["matrix_rational"][i][j]))))
    copies_agree = [[bool(Fz[i, j] == Sa[i, j]) for j in range(5)]
                    for i in range(5)]
    unsigned_cmp = [[{"a": BASIS_ORDER[i], "b": BASIS_ORDER[j],
                      "reconstructed": str(M[i, j]), "frozen": str(Fz[i, j]),
                      "equal": bool(M[i, j] == Fz[i, j])}
                     for j in range(5)] for i in range(5)]
    return {
        "status": "EXECUTED",
        "projection_formula":
            "M[a][c] = (1/16) Sum_i trace(G^a_i G^c_k G^a_i G^c_k)",
        "projection_formula_k_independence": kindep,
        "reconstructed_matrix_without_crossing_sign":
            [[str(M[i, j]) for j in range(5)] for i in range(5)],
        "reconstructed_matrix_with_crossing_sign":
            [[str(F_signed[i, j]) for j in range(5)] for i in range(5)],
        "frozen_matrix_embedded_in_freeze":
            [[str(Fz[i, j]) for j in range(5)] for i in range(5)],
        "frozen_matrix_standalone_json":
            [[str(Sa[i, j]) for j in range(5)] for i in range(5)],
        "two_frozen_copies_agree_entrywise": copies_agree,
        "two_frozen_copies_identical": all(all(r) for r in copies_agree),
        "elementwise_comparison_unsigned_vs_frozen": unsigned_cmp,
        "unsigned_reconstruction_equals_frozen":
            all(c["equal"] for row in unsigned_cmp for c in row),
        "signed_reconstruction_equals_frozen":
            bool(sp.simplify(F_signed - Fz) == sp.zeros(5, 5)),
        "frozen_equals_minus_signed_reconstruction":
            bool(sp.simplify(F_signed + Fz) == sp.zeros(5, 5)),
        "crossing_sign_placement_finding":
            "The frozen matrix_rational equals the reconstruction WITHOUT the "
            "grassmann_crossing_sign factor. Where the -1 is applied is not "
            "determined by the frozen material; it is reported, not resolved.",
        "kernel_identity": kernel_identity_holds(fams, M),
        "basis_checks": basis_checks(fams, g, g5),
        "generator_checks": generator_checks(),
        "involution": {
            "frozen_squared_is_identity":
                bool(sp.simplify(Fz * Fz - sp.eye(5)) == sp.zeros(5, 5)),
            "unsigned_squared_is_identity":
                bool(sp.simplify(M * M - sp.eye(5)) == sp.zeros(5, 5)),
            "signed_squared_is_identity":
                bool(sp.simplify(F_signed * F_signed - sp.eye(5))
                     == sp.zeros(5, 5)),
            "frozen_squared":
                [[str((Fz * Fz)[i, j]) for j in range(5)] for i in range(5)],
            "exact_residual_frozen_squared_minus_identity":
                [[str((Fz * Fz - sp.eye(5))[i, j]) for j in range(5)]
                 for i in range(5)],
            "rank_frozen": int(Fz.rank()),
            "note": "Both the signed and unsigned forms are involutory, so "
                    "involution does not discriminate the crossing-sign "
                    "placement. Reported as found; no convention adjusted.",
        },
        "induced_coefficients": induced_coefficients(Fz),
    }


# ---------------------------------------------------------------- (b) ----
def _q(value, places):
    """Frozen rounding: via the decimal representation, ROUND_HALF_EVEN."""
    d = decimal.Decimal(f"{value:.{STORED_DECIMALS}f}")
    return d.quantize(decimal.Decimal(1).scaleb(-places),
                      rounding=decimal.ROUND_HALF_EVEN)


def stable_decimal_places(values):
    d_max = STORED_DECIMALS
    best, status = None, None
    for d in range(d_max, -1, -1):
        qs = {_q(v, d) for v in values}
        if len(qs) == 1:
            best = d
            break
    if best is None:
        status = "NO_NON_NEGATIVE_DECIMAL_PLACE_AGREEMENT"
        best = 0
    elif best == 0:
        status = "AGREEMENT_AT_ZERO_DECIMAL_PLACES"
    else:
        status = "AGREEMENT_THROUGH_D_MAX" if best == d_max else "AGREEMENT"
    return best, status


def derivation_b():
    study = json.loads(EXPLORATORY.read_text(encoding="utf-8"))
    rows = []
    for grid in study["grid_results"]:
        n, shift = grid["n"], grid["shift"]
        quad = WilsonQuadrature(n=n, shift=shift)
        for block in grid["roots"]:
            ratio, coupling = block["G_over_Gc"], block["G"]
            trivial = float(reconstructed_potential(0.0, coupling, quad))
            for root in block["roots"]:
                mhat = root["mhat"]
                dv = float(reconstructed_potential(mhat, coupling, quad))
                rows.append({
                    "n": n, "shift": shift,
                    "G_over_Gc": ratio, "G": coupling,
                    "mhat": mhat,
                    "stationarity_residual": root["stationarity_residual"],
                    "potential_value": "NOT DEFINED UNDER THE FROZEN MATERIAL",
                    "potential_minus_trivial": float(dv - trivial),
                    "reduced_curvature": root["reduced_curvature"],
                    "branch": root["branch"],
                })
    # frozen correspondence rule
    combos = sorted({(r["n"], r["shift"]) for r in rows})
    aggregates = []
    for ratio in sorted({r["G_over_Gc"] for r in rows}):
        per = {c: [r for r in rows if (r["n"], r["shift"]) == c
                   and r["G_over_Gc"] == ratio] for c in combos}
        sectors = {"zero": lambda m: m == 0.0,
                   "negative": lambda m: m < 0.0,
                   "positive": lambda m: m > 0.0}
        for sector, pred in sectors.items():
            counts = {c: sorted([r for r in per[c] if pred(r["mhat"])],
                                key=lambda r: r["mhat"]) for c in combos}
            sizes = {len(v) for v in counts.values()}
            depth = max(sizes) if sizes else 0
            for ordinal in range(depth):
                participating = [c for c in combos
                                 if len(counts[c]) > ordinal]
                one_to_one = (len(sizes) == 1 and
                              len(participating) == len(combos))
                vals = [counts[c][ordinal]["potential_minus_trivial"]
                        for c in participating]
                entry = {
                    "G_over_Gc": ratio, "sign_sector": sector,
                    "ordinal": ordinal,
                    "stability_combinations": len(participating),
                    "combinations_frozen_in_specification": len(combos),
                    "mhat_by_combination": {
                        f"n{c[0]}_shift{c[1]}": counts[c][ordinal]["mhat"]
                        for c in participating},
                }
                if not one_to_one:
                    entry.update({
                        "potential_min_across_grids": None,
                        "potential_max_across_grids": None,
                        "potential_spread": None,
                        "stable_decimal_places": None,
                        "stability_status":
                            "UNRESOLVED CROSS-GRID CORRESPONDENCE: root counts "
                            "differ between grid/shift combinations",
                    })
                else:
                    sd, status = stable_decimal_places(vals)
                    entry.update({
                        "potential_min_across_grids": float(min(vals)),
                        "potential_max_across_grids": float(max(vals)),
                        "potential_spread": float(max(vals) - min(vals)),
                        "stable_decimal_places": sd,
                        "stability_status": status,
                    })
                aggregates.append(entry)
    # depth resolution by disjoint envelopes, per coupling
    resolution = []
    for ratio in sorted({a["G_over_Gc"] for a in aggregates}):
        band = [a for a in aggregates if a["G_over_Gc"] == ratio
                and a["potential_min_across_grids"] is not None]
        for i in range(len(band)):
            for j in range(i + 1, len(band)):
                x, y = band[i], band[j]
                disjoint = (x["potential_max_across_grids"]
                            < y["potential_min_across_grids"]) or \
                           (y["potential_max_across_grids"]
                            < x["potential_min_across_grids"])
                deeper = None
                if disjoint:
                    deeper = (f'{x["sign_sector"]}#{x["ordinal"]}'
                              if x["potential_max_across_grids"]
                              < y["potential_min_across_grids"]
                              else f'{y["sign_sector"]}#{y["ordinal"]}')
                resolution.append({
                    "G_over_Gc": ratio,
                    "branch_1": f'{x["sign_sector"]}#{x["ordinal"]}',
                    "branch_2": f'{y["sign_sector"]}#{y["ordinal"]}',
                    "envelopes_disjoint": bool(disjoint),
                    "depth_resolved": bool(disjoint),
                    "more_negative_branch": deeper,
                })
    # regression anchor + derivative check, self-generated by this task
    quad = WilsonQuadrature(n=32, shift=0.0)
    gc = 1.0 / (2.0 * quad.bubble(0.0))
    anchor_g = 1.2 * gc
    anchor = {
        "n": 32, "shift": 0.0, "G_over_Gc": 1.2, "G": anchor_g,
        "mhat": 0.5,
        "potential_minus_trivial": float(
            reconstructed_potential(0.5, anchor_g, quad)),
        "provenance": "SELF-GENERATED BY THIS TASK; a regression anchor "
                      "against future drift, NOT independent validation of "
                      "correctness, and NOT a pre-existing frozen number.",
    }
    deriv = []
    for mh in (0.0, 0.1, 0.5, 1.0):
        h = 1e-5
        num = float((reconstructed_potential(mh + h, anchor_g, quad)
                     - reconstructed_potential(mh - h, anchor_g, quad)) / (2 * h))
        ana = float(first_derivative(mh, anchor_g, quad))
        deriv.append({"mhat": mh, "numerical_dV": num,
                      "analytic_first_derivative": ana,
                      "abs_difference": float(abs(num - ana))})
    return {
        "status": "EXECUTED",
        "potential_source": "derivations/P2-PHASE-01_scalar_stationary_"
                            "exploratory.md; reconstructed_potential imported "
                            "from scripts/p2_phase01_scalar_exploratory.py",
        "potential_zero":
            "NOT DEFINED UNDER THE FROZEN MATERIAL; only "
            "V_red(Mhat)-V_red(0) is fixed. Classified "
            "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY.",
        "units": "per site (per unit four-volume in lattice units), a=1, r=1",
        "sign_convention": "more negative potential_minus_trivial = deeper",
        "cross_family_comparison": "OUT OF SCOPE (OPEN-AC-3): no common HS, "
                                   "measure or potential-zero normalisation "
                                   "is frozen",
        "rounding_rule": "decimal representation at 12 stored decimals, "
                         "decimal.ROUND_HALF_EVEN; binary float round() not used",
        "domain_reduction": {
            "reduced": False,
            "grids_used": [list(c) for c in combos],
            "grids_frozen_in_specification":
                [[32, 0.0], [32, 0.25], [40, 0.0], [40, 0.25],
                 [48, 0.0], [48, 0.25]],
            "couplings_used": sorted({r["G_over_Gc"] for r in rows}),
            "couplings_frozen_in_specification":
                [0.8, 0.9, 0.98, 0.99, 1.0, 1.01, 1.02, 1.05,
                 1.1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0],
            "amendment_commit": None,
            "note": "No pre-evaluation reduction was required, so no "
                    "amendment commit exists.",
        },
        "rows": rows,
        "aggregates": aggregates,
        "depth_resolution": resolution,
        "regression_anchor": anchor,
        "derivative_check": deriv,
    }


def _jsonable(obj):
    """Coerce numpy/sympy scalars that json does not natively handle."""
    if obj.__class__.__name__ in ("bool_", "BooleanTrue", "BooleanFalse"):
        return bool(obj)
    if hasattr(obj, "__float__"):
        return float(obj)
    return str(obj)


def main():
    inputs = [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        "results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json",
        "scripts/p2_phase01_scalar_exploratory.py",
    ]
    payload = {
        "study": "P2-PHASE-01 Fierz-matrix verification and stationary-branch "
                 "potential depths",
        "status": "DERIVATION; not a gate result; no admissibility verdict; "
                  "P2-PHASE-01 remains PROPOSED",
        "authority":
            "specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md",
        "derivation_note":
            "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md",
        "repository_inputs_read": inputs,
        "input_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                         for p in inputs},
        "exclusions_confirmed": {
            "quarantined_-3.2(5)": "NOT READ",
            "suspended_P2-BETAV-CIRC-01_result": "NOT READ",
            "historical_Finding_5_extraction": "NOT READ",
            "evidence": "repository_inputs_read above is the complete list of "
                        "repository paths opened by this script.",
        },
        "decisions_taken": {
            "hubbard_stratonovich_channel": "NONE SELECTED (OPEN-AC-1)",
            "vat_orientation_or_components": "NONE SELECTED",
            "potential_zero": "NONE SELECTED",
            "branch_characterisation": "NONE MADE (OPEN-AC-2)",
        },
        "derivation_a_fierz": derivation_a(),
        "derivation_b_branch_depths": derivation_b(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True,
                              default=_jsonable) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT}")
    return payload


if __name__ == "__main__":
    main()
