"""`P2-PHASE-01`: channel character of the Fierz-induced interaction.

Two deliverables, both derivations:

(a) the algebraic channel character of the induced singlet V and A, reported
    in three layers that are never collapsed --- the frozen algebraic
    coefficient (unconditional), the exponent-level Hubbard-Stratonovich
    coefficient (conditional on a mapping that may not be frozen), and the
    physical attractive/repulsive label (which needs more than the second);
(b) whether the particle-particle (diquark) channel is computable at all
    from what is frozen.

This is a computation, not a ruling.  It modifies no frozen artifact, selects
no Hubbard-Stratonovich channel, and selects no charge-conjugation
convention.  `OPEN-AC-1` is untouched and `P2-PHASE-01` remains PROPOSED.
"""

from __future__ import annotations

import hashlib
import json
import linecache
import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
CANONICAL = ROOT / "derivations/CANONICAL_INTERACTION.md"
FIERZ_NOTE = ROOT / "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md"
FIERZ_RESULT = (
    ROOT / "results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json"
)
SIGN_ADDENDUM = ROOT / "derivations/P2-PHASE-01_fierz_sign_addendum.md"
GAP_NOTE = ROOT / "derivations/P2-GAP-01_gap_criticality.md"
CONVENTIONS = ROOT / "CONVENTIONS.md"

OUT = ROOT / "results/P2-PHASE-01/channel-character/channel_character.json"

# The frozen JSON blocks live on fixed lines of the freeze document.
BASIS_BLOCK_LINE = 98
DECOMPOSITION_BLOCK_LINE = 116

# The 2026-08-07 ruling: matrix_rational is stored unsigned and s_G is applied
# exactly once at operator use.
S_G = -1

G, N = sp.symbols("G N", positive=True)


# ------------------------------------------------------------ inputs ------
def repository_inputs() -> list[str]:
    """Every repository file this script reads, by path."""
    return [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        "derivations/CANONICAL_INTERACTION.md",
        "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md",
        "results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json",
        "derivations/P2-PHASE-01_fierz_sign_addendum.md",
        "derivations/P2-GAP-01_gap_criticality.md",
        "CONVENTIONS.md",
        "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py",
    ]


def frozen_basis_block() -> dict:
    return json.loads(linecache.getline(str(FREEZE), BASIS_BLOCK_LINE))


def frozen_decomposition() -> list[dict]:
    block = json.loads(linecache.getline(str(FREEZE), DECOMPOSITION_BLOCK_LINE))
    return block["interaction_decomposition"]


# ---------------------------------------------------------- layer 1a -----
def canonical_coefficient() -> sp.Expr:
    """Read the canonical per-family coefficient from the frozen block.

    Both supported families carry the same coefficient; that is asserted
    rather than assumed, so a freeze that disagreed would fail here.
    """
    decomposition = frozen_decomposition()
    coefficients = {item["coefficient"] for item in decomposition}
    if len(coefficients) != 1:
        raise AssertionError(f"frozen families disagree on coefficient: {coefficients}")
    return sp.sympify(coefficients.pop(), locals={"G": G, "N": N})


def layer_1a() -> dict:
    """The frozen algebraic coefficients.  Unconditional.

    Two normalisations are carried side by side and never mixed:

        L : coefficient of (psibar lam(0) Gamma psi)^2
        P : coefficient of (psibar Gamma psi)^2,  related by c_P = (2/N) c_L
    """
    block = frozen_basis_block()
    order = block["basis_order"]
    fierz = sp.Matrix(
        [[sp.Rational(entry) for entry in row] for row in block["matrix_rational"]]
    )
    standalone = json.loads(FIERZ_JSON.read_text(encoding="utf-8"))
    if standalone["matrix_rational"] != block["matrix_rational"]:
        raise AssertionError("standalone Fierz artifact disagrees with the freeze")

    c_can = canonical_coefficient()

    # canonical operators use I*gamma5; the frozen family basis uses gamma5.
    v_canonical = sp.Matrix([[c_can, c_can, 0, 0, 0]])
    v_frozen = sp.Matrix([[c_can, -c_can, 0, 0, 0]])
    dirac_row = (v_frozen / c_can) * fierz

    # internal factor: Sum_A lam(A)_ab lam(A)_cd = 2 delta_ad delta_cb with
    # Id_N = sqrt(N/2) lam(0) supplies N and makes the structure pure singlet.
    matrix_level_L = {
        order[i]: sp.simplify(c_can * N * dirac_row[i]) for i in range(len(order))
    }
    operator_level_L = {k: sp.simplify(S_G * v) for k, v in matrix_level_L.items()}

    # (psibar lam(0) Gamma psi)^2 = (2/N) (psibar Gamma psi)^2
    to_plain = sp.Integer(2) / N

    channels = {
        "scalar_singlet_direct": {
            "origin": "frozen canonical interaction, singlet term A=0",
            "normalisation_L": c_can,
            "normalisation_P": sp.simplify(c_can * to_plain),
        },
        "induced_V_singlet": {
            "origin": "Fierz image, operator level (s_G applied once)",
            "normalisation_L": operator_level_L["V"],
            "normalisation_P": sp.simplify(operator_level_L["V"] * to_plain),
        },
        "induced_A_singlet": {
            "origin": "Fierz image, operator level (s_G applied once)",
            "normalisation_L": operator_level_L["A"],
            "normalisation_P": sp.simplify(operator_level_L["A"] * to_plain),
        },
    }
    for entry in channels.values():
        entry["sign"] = int(sp.sign(entry["normalisation_L"]))
        entry["sign_of_P_normalisation"] = int(sp.sign(entry["normalisation_P"]))
        entry["normalisation_L"] = str(entry["normalisation_L"])
        entry["normalisation_P"] = str(entry["normalisation_P"])

    return {
        "layer": "1a — frozen algebraic coefficient; UNCONDITIONAL",
        "normalisation_L_definition": "coefficient of (psibar lam(0) Gamma psi)^2",
        "normalisation_P_definition": "coefficient of (psibar Gamma psi)^2",
        "normalisation_relation": "c_P = (2/N) * c_L, from lam(0) = sqrt(2/N) Id_N",
        "canonical_coefficient_read_from_freeze": str(c_can),
        "v_canonical": [str(x) for x in v_canonical],
        "v_frozen_after_I_gamma5_conversion": [str(x) for x in v_frozen],
        "dirac_row_after_frozen_matrix": [str(x) for x in dirac_row],
        "s_G_applied_once_at_operator_use": S_G,
        "matrix_level_normalisation_L": {k: str(v) for k, v in matrix_level_L.items()},
        "operator_level_normalisation_L": {
            k: str(v) for k, v in operator_level_L.items()
        },
        "channels": channels,
        "vanishing_families": [
            k for k, v in operator_level_L.items() if v == 0
        ],
        "note_on_the_exploratory_pairing":
            "The authority pairs the scalar as +G/N**2 and the induced vector "
            "as -G/4. Both values are correct but they are stated in DIFFERENT "
            "normalisations: +G/N**2 is normalisation P and -G/4 is "
            "normalisation L. In a single normalisation the pair is "
            "(+G/(2*N), -G/4) or (+G/N**2, -G/(2*N)). The sign conclusion is "
            "unaffected; the magnitudes as paired are not comparable.",
    }


def scalar_control() -> dict:
    """Calibrate against the operator P2-GAP-01 actually used.

    P2-GAP-01: L_int = G_N (psibar psi)^2 with G_GAP = 4 G_N, the 4 absorbing
    trace(Id4) = 4.  The control is at LAYER 1a only: same operator, same
    internal normalisation, same factor-of-two convention, same sign.
    """
    gap_text = GAP_NOTE.read_text(encoding="utf-8")
    quoted = [
        line.strip()
        for line in gap_text.splitlines()
        if "G_N" in line or "attractive scalar" in line
    ]
    c_can = canonical_coefficient()
    g_n = sp.simplify(c_can * sp.Integer(2) / N)
    g_gap = sp.simplify(4 * g_n)
    sign = int(sp.sign(g_n))
    return {
        "gate": "P2-GAP-01",
        "quoted_from_the_pinned_note": quoted,
        "operator": "(psibar psi)**2",
        "internal_normalisation": "lam(0) = sqrt(2/N) Id_N, frozen",
        "factor_of_two_convention": "G_GAP = 4 * G_N, absorbing trace(Id4) = 4",
        "G_N_from_the_frozen_singlet": str(g_n),
        "G_GAP_from_the_frozen_singlet": str(g_gap),
        "sign_of_G_N": sign,
        "P2_GAP_01_requires_attractive_scalar_i_e_positive": True,
        "control_passes": bool(sign > 0),
        "what_this_does_not_test":
            "It does not re-derive G_c = 1/(2 I_0) for the generator-sum "
            "interaction. P2-GAP-01 worked from the singlet-only form "
            "L_int = G_N (psibar psi)**2; the mean-field combinatorics of the "
            "full U(N) generator sum were not performed there and are not "
            "performed here.",
    }


# ---------------------------------------------------------- layer 1b -----
EXPONENT_MARKERS = [
    "S_E", "Euclidean action", "Wick", "Boltzmann", "L_E", "S_int",
    "exp(-", "exp[-", "e^{-", "action density", "Lagrangian",
    "enters the exponent",
]


def exponent_mapping_search() -> dict:
    """Search the frozen material for how the interaction enters the exponent."""
    sources = {
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md": FREEZE,
        "derivations/CANONICAL_INTERACTION.md": CANONICAL,
        "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md": FIERZ_NOTE,
        "derivations/P2-PHASE-01_fierz_sign_addendum.md": SIGN_ADDENDUM,
        "derivations/P2-GAP-01_gap_criticality.md": GAP_NOTE,
        "CONVENTIONS.md": CONVENTIONS,
    }
    counts: dict[str, int] = {}
    quotes: list[str] = []
    for marker in EXPONENT_MARKERS:
        total = 0
        for label, path in sources.items():
            text = path.read_text(encoding="utf-8")
            hits = text.count(marker)
            total += hits
            if hits and marker in {"S_E", "Wick", "Euclidean action"}:
                for line in text.splitlines():
                    if marker in line and line.strip() not in quotes:
                        quotes.append(f"{label}: {line.strip()}")
        counts[marker] = total
    # a mapping statement would have to relate the two functionals explicitly
    mapping_patterns = [
        r"S_E\s*=\s*-\s*(∫|Integral|int)",
        r"S_E\s*=\s*(∫|Integral|int)\s*L_E",
        r"L\s*(->|→)\s*S_E",
    ]
    mapping_found = any(
        re.search(pattern, path.read_text(encoding="utf-8"))
        for pattern in mapping_patterns
        for path in sources.values()
    )
    return {
        "sources_searched": sorted(sources),
        "marker_counts": counts,
        "quotes": quotes,
        "explicit_L_to_S_E_mapping_found": bool(mapping_found),
    }


def layer_1b(coefficients: dict) -> dict:
    """The exponent-level HS coefficient, conditional on the mapping."""
    search = exponent_mapping_search()
    mapping_is_fixed = search["explicit_L_to_S_E_mapping_found"]

    branches = {}
    for label, factor, description in (
        ("branch_i_expression_already_in_the_exponent", 2,
         "weight carries exp[+c J^2]; g = +2c"),
        ("branch_ii_expression_is_a_term_of_S_E", -2,
         "weight carries exp[-c J^2]; g = -2c"),
    ):
        per_channel = {}
        for name, entry in coefficients["channels"].items():
            c_p = sp.sympify(entry["normalisation_P"], locals={"G": G, "N": N})
            g_val = sp.simplify(factor * c_p)
            per_channel[name] = {
                "g_in_normalisation_P": str(g_val),
                "sign_of_g": int(sp.sign(g_val)),
                "real_linear_HS_field_admissible": bool(sp.sign(g_val) > 0),
            }
        branches[label] = {"description": description, "channels": per_channel}

    scalar_i = branches["branch_i_expression_already_in_the_exponent"][
        "channels"]["scalar_singlet_direct"]["real_linear_HS_field_admissible"]
    scalar_ii = branches["branch_ii_expression_is_a_term_of_S_E"][
        "channels"]["scalar_singlet_direct"]["real_linear_HS_field_admissible"]

    return {
        "layer": "1b — exponent / HS coefficient; CONDITIONAL on the mapping",
        "identity": "exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J], "
                    "convergent only for g > 0",
        "g_is_not_2c": "g is an exponent-level quantity; the mapping supplies "
                       "the sign relating it to the algebraic coefficient c",
        "search": search,
        "mapping_is_fixed_by_the_frozen_material": bool(mapping_is_fixed),
        "verdict": "REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN MATERIAL"
                   if not mapping_is_fixed else "MAPPING FIXED",
        "branches": branches,
        "usage_inference": {
            "statement":
                "P2-GAP-01 introduces a REAL scalar auxiliary Sigma for the "
                "attractive scalar channel and obtains G_c = 1/(2 I_0). A "
                "scalar channel with g < 0 admits no real linear HS field, so "
                "branch (ii) cannot be the convention that calculation "
                "operated under.",
            "branch_i_scalar_admits_real_HS": bool(scalar_i),
            "branch_ii_scalar_admits_real_HS": bool(scalar_ii),
            "branch_ii_consistent_with_P2_GAP_01": bool(scalar_ii),
            "status": "INFERENCE FROM USAGE, NOT A FROZEN DEFINITION. It does "
                      "not resolve this layer; the verdict above stands. "
                      "Fixing the mapping is a PI decision.",
        },
    }


# ----------------------------------------------------------- layer 2 -----
def layer_2(mapping_is_fixed: bool) -> dict:
    """The physical attractive/repulsive label, which may not be available."""
    conventions = CONVENTIONS.read_text(encoding="utf-8")
    anchor_lines = [
        line.strip()
        for line in conventions.splitlines()
        if "attractive" in line.lower()
    ]
    canonical = CANONICAL.read_text(encoding="utf-8")
    canonical_anchor = [
        line.strip()
        for line in canonical.splitlines()
        if "repulsive" in line.lower()
    ]
    return {
        "layer": "2 — physical label; requires MORE than layer 1b",
        "why_not_the_same_as_1b":
            "Real-HS admissibility is not a statement about two-body forces. A "
            "negative g forces an imaginary HS contour, which is not by itself "
            "the absence of an interaction in that channel.",
        "conventions_anchor": anchor_lines,
        "canonical_interaction_anchor": canonical_anchor,
        "anchors_supply_a_general_criterion": False,
        "why_not":
            "CONVENTIONS.md labels ONE channel (scalar, G > 0, attractive); it "
            "states no rule mapping an arbitrary channel's coefficient sign to "
            "a force label. CANONICAL_INTERACTION.md's G_V < 0 repulsive "
            "classification is a recorded Paper-3 claim whose source note "
            "derivations/u3-fierz/u3_fierz.md is NOT present in this "
            "repository, in a document carrying a DRAFT v0.5 no-governing-force "
            "banner.",
        "verdict": "ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL"
                   if not mapping_is_fixed else "MAPPING FIXED; see report",
        "conditional_consequence":
            "Under branch (i) — the only branch consistent with P2-GAP-01's "
            "executed real-auxiliary treatment — and reading the two anchors as "
            "a common sign convention, the induced singlet V and A would be "
            "repulsive and the scalar attractive. Stated as a conditional "
            "consequence, not as a verdict.",
        "u_double_prime_is_not_a_second_route":
            "For the bare quadratic term U(Phi) = Phi^2/(2g), U''(0) = 1/g — "
            "the same sign test restated. For the fermion-integrated effective "
            "potential U''(0) = 1/g - Pi(0), whose sign changes with the "
            "coupling: an attractive scalar channel still has U''(0) > 0 below "
            "G_c. No curvature is offered here as evidence for a force label.",
    }


# --------------------------------------------------- convention notes ----
def convention_dependence(coefficients: dict) -> dict:
    """What the Layer-1a signs depend on, including the s_G reversal."""
    reversed_signs = {}
    for name, entry in coefficients["channels"].items():
        if name == "scalar_singlet_direct":
            reversed_signs[name] = {
                "normalisation_L": entry["normalisation_L"],
                "normalisation_P": entry["normalisation_P"],
                "changed": False,
            }
            continue
        c_l = sp.sympify(entry["normalisation_L"], locals={"G": G, "N": N})
        c_p = sp.sympify(entry["normalisation_P"], locals={"G": G, "N": N})
        reversed_signs[name] = {
            "normalisation_L": str(sp.simplify(-c_l)),
            "normalisation_P": str(sp.simplify(-c_p)),
            "changed": True,
        }
    return {
        "depends_on": [
            "Euclidean metric_signature (1,1,1,1) with Hermitian gammas",
            "the mandatory (I*gamma5)^2 = -(gamma5)^2 basis conversion",
            "the 2026-08-07 ruling: matrix_rational stored unsigned, s_G "
            "applied exactly once at operator use",
        ],
        "if_the_s_G_ruling_were_reversed": {
            "meaning": "matrix_rational would be held to store the sign "
                       "already, so no further factor at operator use",
            "induced_coefficients_become": reversed_signs,
            "scalar_channel_untouched": "the scalar is direct, not "
                                        "Fierz-induced, so it does not move",
            "structure_untouched":
                "S, P and T still vanish; V and A remain equal and purely "
                "singlet; the exchanged form remains purely left-right, "
                "because an overall sign multiplies all four chiral "
                "coefficients equally",
        },
        "composite_vector_scope":
            "This computes the sign of the induced singlet V and A in the "
            "particle-hole rearrangement only. The particle-particle channel "
            "is not computed. No statement is made about whether a massive "
            "composite vector can form; that would concern channels this "
            "derivation does not examine.",
    }


# ------------------------------------------------------- derivation b ----
def _frozen_gammas() -> list[sp.Matrix]:
    import sys

    sys.path.insert(0, str(ROOT / "scripts/P2-CHANNEL-FREEZE"))
    from gamma_algebra import gamma_factory

    block = frozen_basis_block()
    metric = [sp.Integer(value) for value in block["conventions"]["metric_signature"]]
    return gamma_factory(metric)


CONJUGATION_MARKERS = [
    "charge conjugation", "charge-conjugation", "conjugation matrix",
    "psi^c", "psi_c", "diquark", "particle-particle", "particle–particle",
]


def diquark_executability() -> dict:
    """Steps 0-4 of the authority, in order.  No C is selected."""
    sources = {
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md": FREEZE,
        "derivations/CANONICAL_INTERACTION.md": CANONICAL,
        "derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md": FIERZ_NOTE,
        "derivations/P2-PHASE-01_fierz_sign_addendum.md": SIGN_ADDENDUM,
        "derivations/P2-GAP-01_gap_criticality.md": GAP_NOTE,
        "CONVENTIONS.md": CONVENTIONS,
    }
    marker_counts = {
        marker: sum(
            path.read_text(encoding="utf-8").lower().count(marker.lower())
            for path in sources.values()
        )
        for marker in CONJUGATION_MARKERS
    }
    step_1_fixed = any(marker_counts.values())

    # Step 2: solve C gamma_mu^T + gamma_mu C = 0 as a linear system.
    gammas = _frozen_gammas()
    unknown = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"c_{i}{j}"))
    equations = []
    for gamma in gammas:
        residual = unknown * gamma.T + gamma * unknown
        equations += [sp.expand(residual[i, j]) for i in range(4) for j in range(4)]
    symbols = list(unknown)
    solution = list(sp.linsolve(equations, symbols))[0]
    free = sorted({s for expr in solution for s in expr.free_symbols}, key=str)
    dimension = len(free)

    representative = None
    checks: dict[str, bool] = {}
    if dimension == 1:
        c_matrix = unknown.subs(dict(zip(symbols, solution))).subs({free[0]: 1})
        c_matrix = sp.simplify(c_matrix)
        checks = {
            "defining_relation_holds_for_all_mu": bool(
                all(
                    sp.simplify(c_matrix * gamma.T * c_matrix.inv() + gamma)
                    == sp.zeros(4)
                    for gamma in gammas
                )
            ),
            "antisymmetric_C_transpose_equals_minus_C": bool(
                sp.simplify(c_matrix.T + c_matrix) == sp.zeros(4)
            ),
            "unitary_C_dagger_C_is_identity": bool(
                sp.simplify(c_matrix.H * c_matrix) == sp.eye(4)
            ),
            "determinant_is_one": bool(sp.simplify(c_matrix.det()) == 1),
        }
        representative = [[str(c_matrix[i, j]) for j in range(4)] for i in range(4)]

        # Step 3: the residual scalar cancels between the paired factors.
        lam = sp.Symbol("lambda", nonzero=True)
        scaled = lam * c_matrix
        paired_unscaled = c_matrix * c_matrix.inv()
        paired_scaled = sp.simplify(scaled * scaled.inv())
        checks["residual_scalar_cancels_in_the_paired_product"] = bool(
            sp.simplify(paired_scaled - paired_unscaled) == sp.zeros(4)
        )
        # and explicitly for a Dirac structure sandwiched between them
        for gamma in gammas:
            lhs = sp.simplify(scaled * gamma.T * scaled.inv())
            rhs = sp.simplify(c_matrix * gamma.T * c_matrix.inv())
            if sp.simplify(lhs - rhs) != sp.zeros(4):
                checks["residual_scalar_cancels_in_the_paired_product"] = False

    # Step 0: the remaining pp operator definitions.
    block = frozen_basis_block()
    step_0 = {
        "charge_conjugated_field_definition_frozen": False,
        "why": "In Euclidean signature psi and psibar are independent Grassmann "
               "variables, so psibar^c is not derivable from psi^c by "
               "conjugation; it must be defined. The sign/phase eta in "
               "psibar^c = eta psi^T C^-1 appears ONCE in the paired product "
               "and therefore flips the coefficient sign for eta = -1.",
        "particle_particle_grassmann_ordering_frozen": False,
        "what_the_freeze_does_fix": {
            "compound_index_order": block["conventions"]["compound_index_order"],
            "grassmann_crossing_sign": block["conventions"]["grassmann_crossing_sign"],
            "applies_to": "the particle-hole exchange "
                          "(alpha,beta,gamma,delta) -> (alpha,delta,gamma,beta); "
                          "a particle-particle pairing is a different "
                          "permutation and no ordering convention is frozen "
                          "for it",
        },
        "diquark_operator_normalisation_frozen": False,
    }
    step_0_passes = all(
        value is True
        for key, value in step_0.items()
        if key.endswith("_frozen")
    )

    return {
        "step_0_all_pp_operator_definitions_fixed": step_0_passes,
        "step_0_detail": step_0,
        "step_1_C_fixed_by_the_frozen_material": bool(step_1_fixed),
        "step_1_marker_counts": marker_counts,
        "step_1_sources_searched": sorted(sources),
        "step_2_defining_relation": "C gamma_mu^T C^-1 = -gamma_mu",
        "step_2_solution_space_complex_dimension": dimension,
        "step_2_C_unique_up_to_a_nonzero_scalar": bool(dimension == 1),
        "step_2_representative_C": representative,
        "step_2_checks": checks,
        "step_3_channel_character_invariant_under_residual_scalar": bool(
            checks.get("residual_scalar_cancels_in_the_paired_product", False)
        ),
        "step_4_verdict": "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY",
        "step_4_dependence_that_forces_it":
            "The pp channel character is invariant under the residual freedom "
            "in C, so C is NOT the obstruction. It is not invariant under the "
            "un-frozen charge-conjugated-field convention eta, which appears "
            "once in the paired product and flips the sign. The frozen "
            "material fixes neither eta nor the pp Grassmann ordering nor the "
            "diquark normalisation.",
        "no_C_selected": True,
        "no_pp_projection_constructed": True,
        "why_no_projection":
            "Constructing it would require supplying exactly the conventions "
            "step 0 shows to be missing. The authority records an earlier "
            "exploratory diquark projection that returned zero in all four "
            "families and treats it as a failed attempt rather than a finding; "
            "it is not repeated here.",
    }


# ------------------------------------------------------------- main ------
def main() -> dict:
    inputs = repository_inputs()
    coefficients = layer_1a()
    control = scalar_control()
    if not control["control_passes"]:
        raise AssertionError(
            "scalar Layer-1a control failed; the coefficient chain is wrong "
            "and the V and A results cannot be trusted"
        )
    l1b = layer_1b(coefficients)
    l2 = layer_2(l1b["mapping_is_fixed_by_the_frozen_material"])

    payload = {
        "study": "P2-PHASE-01 channel character of the Fierz-induced interaction",
        "status": "DERIVATION; a computation, not a ruling; no gate registered, "
                  "no status changed, no frozen artifact modified, no "
                  "Hubbard-Stratonovich channel selected, no "
                  "charge-conjugation convention selected",
        "authority": "specs/2026-08-08T1321Z_channel-character.md",
        "derivation_note": "derivations/P2-PHASE-01_channel_character.md",
        "repository_inputs_read": inputs,
        "input_sha256": {
            path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            for path in inputs
        },
        "exclusions_confirmed": {
            "quarantined_-3.2(5)": "NOT READ",
            "suspended_P2-BETAV-CIRC-01_result": "NOT READ",
            "historical_Finding_5_extraction": "NOT READ",
        },
        "scalar_control": control,
        "layer_1a": coefficients,
        "layer_1b": l1b,
        "layer_2": l2,
        "convention_dependence": convention_dependence(coefficients),
        "derivation_b_diquark_executability": diquark_executability(),
        "open_ac_1": "untouched; this reports which channels admit a real "
                     "linear auxiliary field under each possible exponent "
                     "mapping, and reports that the mapping is not frozen",
        "gate_status": "P2-PHASE-01 remains PROPOSED",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT}")
    return payload


if __name__ == "__main__":
    main()
