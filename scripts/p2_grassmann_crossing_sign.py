"""`P2-CHANNEL-FREEZE-01`: the Grassmann crossing sign, by explicit exchange.

Answers one question and tests a second:

A3a  the operator-level Grassmann exchange sign ``s_G``, from an explicit
     four-fermion monomial under the permutation frozen by the specification;
A3b  whether the frozen material contains a defining kernel equation that
     fixes how ``matrix_rational`` stores that sign.

It also reports a sign-blind chiral cross-check and characterises the freeze
checker's double application of the scalar sign.

This is a computation, not a ruling.  It modifies no frozen artifact, no
checker and no mutation suite, and it selects no convention.
"""

from __future__ import annotations

import hashlib
import json
import linecache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
CHECKER = ROOT / "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"
MUTATIONS = ROOT / "tests/test_channel_freeze_mutations.py"
OUT = (ROOT / "results/P2-CHANNEL-FREEZE/grassmann-crossing-sign"
       / "crossing_sign.json")

DECLARED_CROSSING_SIGN = -1

# The normative orderings, from section 2 of the authority specification.
START_ORDER = ["psibar_1", "psi_2", "psibar_3", "psi_4"]
FINAL_ORDER = ["psibar_1", "psi_4", "psibar_3", "psi_2"]


# --------------------------------------------------------------- A2 ------
def explicit_anticommutation():
    """Reorder START_ORDER into FINAL_ORDER by adjacent swaps only.

    Every object is Grassmann-odd, so each adjacent swap contributes -1.
    Gamma, lam^A and the index contractions are commuting c-numbers and
    carry no sign, so the whole sign is the ordering parity.
    """
    seq = list(START_ORDER)
    sign = 1
    steps = []
    # Selection-sort into the target order using adjacent transpositions,
    # which makes every contributing anticommutation explicit.
    for target_pos, label in enumerate(FINAL_ORDER):
        cur = seq.index(label)
        while cur > target_pos:
            a, b = seq[cur - 1], seq[cur]
            seq[cur - 1], seq[cur] = seq[cur], seq[cur - 1]
            sign = -sign
            cur -= 1
            steps.append({
                "step": len(steps) + 1,
                "moved": b,
                "past": a,
                "sign_of_this_anticommutation": -1,
                "ordering_after": list(seq),
                "cumulative_sign": sign,
            })
    return sign, steps, seq


def note_route():
    """The specific three-step decomposition listed in the derivation note.

    A permutation has many decompositions into adjacent transpositions; the
    note names one and ``explicit_anticommutation`` happens to find another.
    Both must give the same sign, and both are reported.
    """
    seq = list(START_ORDER)
    sign = 1
    steps = []
    plan = [("psi_2", "psibar_3"), ("psi_2", "psi_4"), ("psi_4", "psibar_3")]
    for moved, past in plan:
        i, j = seq.index(moved), seq.index(past)
        if abs(i - j) != 1:
            raise AssertionError(f"{moved} and {past} are not adjacent in {seq}")
        seq[i], seq[j] = seq[j], seq[i]
        sign = -sign
        steps.append({
            "step": len(steps) + 1,
            "moved": moved,
            "past": past,
            "sign_of_this_anticommutation": -1,
            "ordering_after": list(seq),
            "cumulative_sign": sign,
        })
    return sign, steps, seq


def permutation_parity():
    """Independent route: parity of the permutation of the label sequence."""
    perm = [START_ORDER.index(label) for label in FINAL_ORDER]
    # count inversions
    inversions = sum(1 for a in range(len(perm))
                     for b in range(a + 1, len(perm)) if perm[a] > perm[b])
    cycles, seen = [], set()
    for start in range(len(perm)):
        if start in seen:
            continue
        cycle, node = [], start
        while node not in seen:
            seen.add(node)
            cycle.append(node)
            node = perm[node]
        if len(cycle) > 1:
            cycles.append(cycle)
    transpositions = sum(len(c) - 1 for c in cycles)
    return {
        "permutation_one_line": perm,
        "inversions": inversions,
        "nontrivial_cycles": cycles,
        "transposition_count": transpositions,
        "sign_from_inversions": (-1) ** inversions,
        "sign_from_transpositions": (-1) ** transpositions,
    }


# --------------------------------------------------------------- A3b -----
def storage_convention_test():
    """Inspect the frozen material for a defining kernel equation."""
    freeze_text = FREEZE.read_text(encoding="utf-8")
    block = json.loads(linecache.getline(str(FREEZE), 98))
    standalone = json.loads(FIERZ_JSON.read_text(encoding="utf-8"))
    section_c = "\n".join(freeze_text.splitlines()[85:97])
    # A defining kernel equation would have to relate an exchanged kernel to
    # a direct one through the matrix.  Look for any such statement.
    markers = ["K_exch", "K_direct", "= M ", "M .", "M *",
               "defining equation", "kernel equation"]
    found = {m: freeze_text.count(m) for m in markers}
    return {
        "freeze_json_top_level_keys": list(block),
        "standalone_artifact_keys": list(standalone),
        "section_C_verbatim": section_c,
        "kernel_equation_markers_found": found,
        "defining_kernel_equation_present": any(v for v in found.values()),
        "verdict": "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY",
        "reasoning":
            "No defining kernel equation appears anywhere in the frozen "
            "material. The freeze's JSON block carries only basis_order, "
            "basis_elements, conventions and matrix_rational; the standalone "
            "artifact carries only basis_order and matrix_rational. The only "
            "prose describing the matrix's meaning is section C, which says "
            "the algebra 'and the Grassmann crossing sign -1 fix the "
            "following exact exchange matrix' without stating whether the "
            "tabulated entries include that sign. Both K_exch = M K_direct "
            "and K_exch = s_G M K_direct remain consistent with the frozen "
            "text.",
        "explicitly_not_used_as_evidence":
            "The numerical equality of an unsigned reconstruction with "
            "matrix_rational is NOT used here. That equality is consistent "
            "with either convention: it shows the entries match a signless "
            "construction, not that the defining equation omits the sign.",
    }


# --------------------------------------------------------------- A4 ------
def _gammas():
    pauli = [sp.Matrix([[0, 1], [1, 0]]),
             sp.Matrix([[0, -sp.I], [sp.I, 0]]),
             sp.Matrix([[1, 0], [0, -1]])]
    i2, z2 = sp.eye(2), sp.zeros(2)

    def blk(a, b, c, d):
        return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))

    return [blk(z2, i2, i2, z2)] + [
        blk(z2, -sp.I * pauli[k], sp.I * pauli[k], z2) for k in range(3)
    ]


def chiral_decomposition():
    """Sign-blind structural check on the direct and exchanged forms.

    Uses symbols for the chiral bilinears, so the result is exact and does
    not depend on any numerical representation.
    """
    g = _gammas()
    g5 = g[0] * g[1] * g[2] * g[3]
    p_l = (sp.eye(4) - g5) / 2
    p_r = (sp.eye(4) + g5) / 2
    projector_checks = {
        "P_L_idempotent": bool(sp.simplify(p_l * p_l - p_l) == sp.zeros(4)),
        "P_R_idempotent": bool(sp.simplify(p_r * p_r - p_r) == sp.zeros(4)),
        "P_L_plus_P_R_is_Id4": bool(sp.simplify(p_l + p_r - sp.eye(4))
                                    == sp.zeros(4)),
        "P_L_P_R_orthogonal": bool(sp.simplify(p_l * p_r) == sp.zeros(4)),
        "gamma5_hermitian": bool(sp.simplify(g5.H - g5) == sp.zeros(4)),
        "gamma5_squares_to_Id4": bool(sp.simplify(g5 * g5 - sp.eye(4))
                                      == sp.zeros(4)),
    }
    sl, sr, jl, jr = sp.symbols("S_L S_R J_L J_R", commutative=True)

    def split(expr):
        """Coefficients of LL, LR, RL, RR under the symmetric split."""
        poly = sp.expand(expr)
        c_ll = poly.coeff(sl, 2).coeff(sr, 0) if poly.has(sl) else 0
        c_rr = poly.coeff(sr, 2).coeff(sl, 0) if poly.has(sr) else 0
        cross = sp.expand(poly).coeff(sl, 1).coeff(sr, 1)
        return (sp.simplify(c_ll), sp.simplify(cross / 2),
                sp.simplify(cross / 2), sp.simplify(c_rr))

    # Direct scalar channel, AFTER the ratified I*gamma5 -> gamma5 conversion:
    #   S = S_L + S_R ,  P = S_R - S_L  ,  interaction = S^2 - P^2
    s_expr = sl + sr
    p_expr = sr - sl
    direct = sp.expand(s_expr ** 2 - p_expr ** 2)
    d_ll, d_lr, d_rl, d_rr = split(direct)

    # Exchanged current channel, frozen A = I*gamma(mu)*gamma5:
    #   V = J_L + J_R ,  A = I (J_R - J_L) ,  combination = V^2 + A^2
    v_expr = jl + jr
    a_expr = sp.I * (jr - jl)
    exchanged = sp.expand(v_expr ** 2 + a_expr ** 2)
    poly = sp.expand(exchanged)
    e_ll = sp.simplify(poly.coeff(jl, 2).coeff(jr, 0))
    e_rr = sp.simplify(poly.coeff(jr, 2).coeff(jl, 0))
    e_cross = sp.simplify(poly.coeff(jl, 1).coeff(jr, 1))

    return {
        "projector_convention": {
            "P_L": "(Id4 - gamma5)/2",
            "P_R": "(Id4 + gamma5)/2",
            "checks": projector_checks,
        },
        "direct_scalar_channel": {
            "interaction": "S**2 - P**2  (canonical form after the ratified "
                           "I*gamma5 -> gamma5 basis conversion)",
            "S_in_chiral_bilinears": "S_L + S_R",
            "P_in_chiral_bilinears": "S_R - S_L",
            "expanded": str(direct),
            "LL": str(d_ll), "LR": str(d_lr),
            "RL": str(d_rl), "RR": str(d_rr),
            "purely_left_right": bool(d_ll == 0 and d_rr == 0),
        },
        "exchanged_current_channel": {
            "combination": "V**2 + A**2 with the frozen A = I*gamma(mu)*gamma5",
            "V_in_chiral_currents": "J_L + J_R",
            "A_in_chiral_currents": "I*(J_R - J_L)",
            "expanded": str(exchanged),
            "LL": str(e_ll), "LR": str(sp.simplify(e_cross / 2)),
            "RL": str(sp.simplify(e_cross / 2)), "RR": str(e_rr),
            "purely_left_right": bool(e_ll == 0 and e_rr == 0),
        },
        "note": "Sign-blind: an overall sign multiplies all four "
                "coefficients equally, so this check cannot bear on s_G.",
    }


# --------------------------------------------------------------- A5 ------
def checker_sign_invariance():
    """Direct substitution into (sign * X).T * sign for both sign values."""
    projector = sp.Matrix([[1, 2], [3, 4]])
    crossing = sp.Matrix([[0, 1], [1, 0]])
    embedding = sp.eye(2)
    outputs = {}
    for value in (-1, 1):
        sign = sp.Integer(value)
        result = (sign * projector * crossing * embedding).T * sign
        outputs[str(value)] = [[str(result[i, j]) for j in range(2)]
                               for i in range(2)]
    invariant = outputs["-1"] == outputs["1"]
    return {
        "expression": "(sign * projector * crossing * embedding).T * sign",
        "source": "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:462",
        "output_for_sign_minus_1": outputs["-1"],
        "output_for_sign_plus_1": outputs["1"],
        "invariant_under_sign_flip": invariant,
        "reason": "sign is a scalar and transposition does not act on a "
                  "scalar factor, so the two occurrences multiply to "
                  "sign**2 = +1 for either declared value.",
        "mutation_suite_covers_the_field":
            "grassmann" in MUTATIONS.read_text(encoding="utf-8"),
        "checker_modified_by_this_task": False,
    }


def main():
    sign, steps, final_seq = explicit_anticommutation()
    note_sign, note_steps, note_seq = note_route()
    parity = permutation_parity()
    inputs = [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py",
        "tests/test_channel_freeze_mutations.py",
    ]
    payload = {
        "study": "P2-CHANNEL-FREEZE-01 Grassmann crossing sign, by explicit "
                 "single-leg exchange",
        "status": "DERIVATION; a computation, not a ruling; no gate "
                  "registered, no status changed, no frozen artifact modified",
        "authority": "specs/2026-08-07T1159Z_grassmann-crossing-sign.md",
        "derivation_note":
            "derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md",
        "repository_inputs_read": inputs,
        "input_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                         for p in inputs},
        "exclusions_confirmed": {
            "quarantined_-3.2(5)": "NOT READ",
            "suspended_P2-BETAV-CIRC-01_result": "NOT READ",
            "historical_Finding_5_extraction": "NOT READ",
        },
        "A3a_grassmann_exchange_sign": {
            "monomial":
                "( psibar^{i}_{alpha} Gamma_{alpha beta} lam^{A}_{ij} "
                "psi^{j}_{beta} ) ( psibar^{k}_{gamma} Gamma_{gamma delta} "
                "lam^{A}_{kl} psi^{l}_{delta} )",
            "labels": {"1": "psibar^{i}_{alpha}", "2": "psi^{j}_{beta}",
                       "3": "psibar^{k}_{gamma}", "4": "psi^{l}_{delta}"},
            "starting_order": START_ORDER,
            "final_order": FINAL_ORDER,
            "legs_exchanged": "psi_2 and psi_4; the two psibar legs do not "
                              "move",
            "anticommutation_steps": steps,
            "anticommutation_steps_note_route": note_steps,
            "note_route_final_ordering": note_seq,
            "note_route_sign": note_sign,
            "final_ordering_reached": final_seq,
            "final_ordering_matches_normative_target":
                final_seq == FINAL_ORDER,
            "s_G": sign,
            "permutation_parity_cross_check": parity,
            "all_routes_agree": bool(
                sign == note_sign == parity["sign_from_inversions"]
                == parity["sign_from_transpositions"]),
            "routes": {
                "explicit_selection_sort": sign,
                "derivation_note_decomposition": note_sign,
                "permutation_parity_inversions":
                    parity["sign_from_inversions"],
                "permutation_parity_transpositions":
                    parity["sign_from_transpositions"],
            },
            "declared_grassmann_crossing_sign": DECLARED_CROSSING_SIGN,
            "s_G_equals_declared_value": bool(sign == DECLARED_CROSSING_SIGN),
        },
        "A3b_storage_convention": storage_convention_test(),
        "A4_chiral_decomposition": chiral_decomposition(),
        "A5_checker_sign_invariance": checker_sign_invariance(),
        "consequence_for_P2_PHASE_01": {
            "scope": "sign only; magnitude and structure of the induced V and "
                     "A coefficients are already established there and are "
                     "not restated or re-derived here",
            "statement":
                "s_G is established as -1. Whether the P2-PHASE-01 induced V "
                "and A coefficients carry that factor depends on the storage "
                "convention, which A3b reports as unresolved. The sign "
                "therefore remains contingent; it is NOT flipped by this "
                "result on its own.",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT}")
    return payload


if __name__ == "__main__":
    main()
