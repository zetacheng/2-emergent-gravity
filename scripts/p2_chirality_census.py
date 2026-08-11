"""`P2-PHASE-01`: the chirality census — why S, P and T vanish in both channels.

Tests a structural explanation for a pattern the programme holds as two separate
numerical facts.  It is a counting argument over chirality, not a cancellation
of numbers, and it is arranged so it can fail.

    Step A   the factorisation of the frozen source, verified with a residual
    Step B   the family chirality classification, from the frozen basis
    Step C   chirality support: C1 particle-hole, C2 particle-particle, C3 the
             census of the source itself
    Step D   the falsification test: predict from the census, then compute
    Step E   what the argument does not explain

This script introduces NO new programme coefficient or channel-character result.
The coefficients in Step D are diagnostic reproductions used to test the
criterion.  Nothing is frozen and no convention is decided; `P2-PHASE-01`
remains PROPOSED.

The particle-particle side is established STRUCTURALLY, from the projector
algebra alone.  No particle-particle coefficient decomposition is performed and
no slot map is chosen, which is what allows the question to be asked while the
particle-particle ordering and the diquark normalisation remain unfrozen.  The
branches carrying those coefficients are not read.

The Step D predictions are recorded in the derivation note, which is an EARLIER
commit than this file.  The git history is the evidence of ordering.
"""

from __future__ import annotations

import hashlib
import json
import linecache
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
CHANNEL_NOTE = ROOT / "derivations/P2-PHASE-01_channel_character.md"
CHANNEL_JSON = ROOT / "results/P2-PHASE-01/channel-character/channel_character.json"

OUT = ROOT / "results/P2-PHASE-01/chirality-census/census.json"

BASIS_BLOCK_LINE = 98

# The 2026-08-07 ruling: matrix_rational is stored unsigned, s_G applied once.
S_G = -1

FAMILIES = ("S", "P", "V", "A", "T")
TOL = 1e-9


def repository_inputs() -> list[str]:
    """Every repository file this script reads, by path."""
    return [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "derivations/P2-PHASE-01_channel_character.md",
        "results/P2-PHASE-01/channel-character/channel_character.json",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py",
    ]


def branches_not_read() -> list[str]:
    return ["gate/p2-diquark-both-eta", "gate/p2-diquark-adjudication"]


# ------------------------------------------------------------ A3: frozen ---
def frozen_conventions() -> dict:
    """Verify by quotation that the freeze says what the argument needs.

    These are load-bearing: dropping the factors of i moves the surviving
    support.  A change in the freeze must stop this script, not be absorbed.
    """
    text = FREEZE.read_text(encoding="utf-8")
    literals = {
        "canonical_pseudoscalar_carries_i_gamma5": "(iγ₅)_{αβ}",
        "canonical_pseudoscalar_machine_block": "bilinear(lam(A),I*gamma5)**2",
        "A_family_element_carries_i": "A=I*gamma(mu)*gamma5",
        "T_family_element_carries_i":
            "T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2",
        "A_element_machine_block":
            '"basis_id":"A","expression":"I*gamma(mu)*gamma5"',
        "T_element_machine_block":
            '"basis_id":"T","expression":'
            '"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"',
        "gamma5_definition":
            '"gamma5_definition":"gamma(0)*gamma(1)*gamma(2)*gamma(3)"',
        "metric_signature": '"metric_signature":["1","1","1","1"]',
    }
    counts = {key: text.count(value) for key, value in literals.items()}
    missing = [key for key, count in counts.items() if count == 0]
    if missing:
        raise AssertionError(f"the freeze no longer states: {missing}")
    quoted = next(
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith("P^A(x) ≡")
    )
    return {
        "check_type": "EXACT LITERAL SUBSTRING on raw UTF-8; no normalisation",
        "literals": literals,
        "occurrence_counts": counts,
        "canonical_pseudoscalar_line_quoted": quoted,
    }


def pinned_inputs() -> dict:
    """A1: three digest-pinned inputs; a mismatch raises."""
    expected = {
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md":
            "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
        "derivations/P2-PHASE-01_channel_character.md":
            "380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f",
        "results/P2-PHASE-01/channel-character/channel_character.json":
            "093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f",
    }
    checked = {}
    for path, digest in expected.items():
        observed = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        checked[path] = {
            "expected": digest,
            "observed": observed,
            "match": observed == digest,
        }
        if observed != digest:
            raise AssertionError(f"pinned input {path} does not match")
    return checked


# ------------------------------------------------------------- machinery ---
def gammas_frozen_factory() -> list[np.ndarray]:
    import importlib.util

    path = ROOT / "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py"
    spec = importlib.util.spec_from_file_location("gamma_algebra", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    block = json.loads(linecache.getline(str(FREEZE), BASIS_BLOCK_LINE))
    metric = [sp.Integer(v) for v in block["conventions"]["metric_signature"]]
    return [np.array(m.tolist(), dtype=complex) for m in module.gamma_factory(metric)]


def gammas_independent() -> list[np.ndarray]:
    """A second Euclidean Hermitian set, written independently of the factory."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    return [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, i2)]


REPRESENTATIONS = {
    "frozen_factory": gammas_frozen_factory,
    "independent_kron": gammas_independent,
}


def gamma5(g: list[np.ndarray]) -> np.ndarray:
    """The frozen definition: gamma5 = g0 g1 g2 g3."""
    return g[0] @ g[1] @ g[2] @ g[3]


def projectors(g: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    g5 = gamma5(g)
    identity = np.eye(4, dtype=complex)
    return (identity - g5) / 2, (identity + g5) / 2


def family_basis(g: list[np.ndarray]) -> list[tuple[str, np.ndarray]]:
    """The frozen sixteen, with the factors of i the freeze fixes on A and T."""
    g5 = gamma5(g)
    elements: list[tuple[str, np.ndarray]] = [
        ("S", np.eye(4, dtype=complex)),
        ("P", g5),
    ]
    elements += [("V", g[m]) for m in range(4)]
    elements += [("A", 1j * g[m] @ g5) for m in range(4)]
    for m in range(4):
        for n in range(m + 1, 4):
            elements.append(("T", 1j * (g[m] @ g[n] - g[n] @ g[m]) / 2))
    return elements


def conjugation_matrix(g: list[np.ndarray]) -> tuple[np.ndarray, int]:
    """C from the null space of C g_m^T + g_m C = 0 over a general complex 4x4."""
    blocks = []
    for m in range(4):
        rows = np.zeros((16, 16), dtype=complex)
        transposed = g[m].T
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for n in range(4):
                        rows[i * 4 + j, k * 4 + n] = (
                            (1 if i == k else 0) * transposed[n, j]
                            + g[m][i, k] * (1 if n == j else 0)
                        )
        blocks.append(rows)
    _, singular, vh = np.linalg.svd(np.vstack(blocks))
    return vh[-1].conj().reshape(4, 4), int(np.sum(singular < TOL))


def _vanishes(matrix: np.ndarray) -> bool:
    return bool(np.max(np.abs(matrix)) < TOL)


def kron4(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """The ordered rank-4 tensor T[a,b,c,d] = left[a,b] right[c,d]."""
    return np.einsum("ab,cd->abcd", left, right)


# ---------------------------------------------------- Step A: factorise ----
def step_A(g: list[np.ndarray]) -> dict:
    """The factorisation, verified with a residual rather than asserted."""
    g5 = gamma5(g)
    identity = np.eye(4, dtype=complex)
    p_l, p_r = projectors(g)

    frozen = kron4(identity, identity) + kron4(1j * g5, 1j * g5)
    no_i = kron4(identity, identity) + kron4(g5, g5)
    frozen_factorised = 2 * (kron4(p_r, p_l) + kron4(p_l, p_r))
    no_i_factorised = 2 * (kron4(p_r, p_r) + kron4(p_l, p_l))

    return {
        "frozen_source": "I(x)I + (i g5)(x)(i g5) = I(x)I - g5(x)g5",
        "frozen_factorised": "2 [ P_R(x)P_L + P_L(x)P_R ]",
        "frozen_residual_max": float(np.max(np.abs(frozen - frozen_factorised))),
        "no_i_source": "I(x)I + g5(x)g5",
        "no_i_factorised": "2 [ P_R(x)P_R + P_L(x)P_L ]",
        "no_i_residual_max": float(np.max(np.abs(no_i - no_i_factorised))),
        "note_on_the_factor_four":
            "4 (psibar_L psi_R)(psibar_R psi_L) is an OPERATOR statement: the two "
            "bilinears are Grassmann-even and commute, so the two orderings are the "
            "same operator. It is NOT an identity on the ORDERED rank-4 tensor.",
        "residual_against_4_P_R_kron_P_L": float(
            np.max(np.abs(frozen - 4 * kron4(p_r, p_l)))
        ),
    }


# ----------------------------------- Steps B and C: the chirality tables ---
def chirality_tables(g: list[np.ndarray]) -> dict:
    """C1 and C2, all four entries each, none omitted as redundant."""
    p_l, p_r = projectors(g)
    matrix_c, null_dimension = conjugation_matrix(g)
    inverse_c = np.linalg.inv(matrix_c)
    if null_dimension != 1:
        raise AssertionError(f"C null space has dimension {null_dimension}")

    relation_holds = bool(
        np.allclose(matrix_c @ gamma5(g).T @ inverse_c, gamma5(g), atol=TOL)
    )
    no_flip = all(
        np.allclose(p.T @ inverse_c, inverse_c @ p, atol=TOL) for p in (p_l, p_r)
    )
    if not (relation_holds and no_flip):
        raise AssertionError("the frozen C relation does not hold as required")

    c1: dict[str, dict] = {}
    c2: dict[str, dict] = {}
    for family, element in family_basis(g):
        ph = {
            "P_L_G_P_L": _vanishes(p_l @ element @ p_l),
            "P_L_G_P_R": _vanishes(p_l @ element @ p_r),
            "P_R_G_P_L": _vanishes(p_r @ element @ p_l),
            "P_R_G_P_R": _vanishes(p_r @ element @ p_r),
        }
        pp = {
            "LL": _vanishes(p_l.T @ inverse_c @ element @ p_l),
            "LR": _vanishes(p_l.T @ inverse_c @ element @ p_r),
            "RL": _vanishes(p_r.T @ inverse_c @ element @ p_l),
            "RR": _vanishes(p_r.T @ inverse_c @ element @ p_r),
        }
        for table, entry in ((c1, ph), (c2, pp)):
            if family in table and table[family]["vanishes"] != entry:
                raise AssertionError(f"family {family} is not uniform")
            table[family] = {"vanishes": entry}

    # ph: psibar_X Gamma psi_Y  <->  P_Xbar Gamma P_Y, so the bar flips one index.
    for family in FAMILIES:
        ph = c1[family]["vanishes"]
        same = (not ph["P_L_G_P_R"]) or (not ph["P_R_G_P_L"])
        opposite = (not ph["P_L_G_P_L"]) or (not ph["P_R_G_P_R"])
        c1[family]["type"] = (
            "SAME-chirality" if same and not opposite
            else "OPPOSITE-chirality" if opposite and not same
            else "MIXED"
        )
        # pp: no bar, so no flip.
        pp = c2[family]["vanishes"]
        same_qq = (not pp["LL"]) or (not pp["RR"])
        opposite_qq = (not pp["LR"]) or (not pp["RL"])
        c2[family]["type"] = (
            "SAME-chirality qq" if same_qq and not opposite_qq
            else "OPPOSITE-chirality qq" if opposite_qq and not same_qq
            else "MIXED"
        )

    def is_inverted(family: str) -> bool:
        ph_opposite = c1[family]["type"] == "OPPOSITE-chirality"
        pp_same = c2[family]["type"] == "SAME-chirality qq"
        return ph_opposite == pp_same

    inverted = all(is_inverted(f) for f in FAMILIES)
    projector_patterns_identical = all(
        list(c1[f]["vanishes"].values()) == list(c2[f]["vanishes"].values())
        for f in FAMILIES
    )
    return {
        "placement_convention": {
            "P_L": "(1 - g5)/2",
            "P_R": "(1 + g5)/2",
            "psibar_L": "psibar P_R  — the bar FLIPS the projector",
            "ph_translation": "psibar_X Gamma psi_Y  <->  P_Xbar Gamma P_Y",
            "pp_translation": "psi_X^T C^-1 Gamma psi_Y  <->  P_X^T C^-1 Gamma P_Y",
        },
        "C_null_space_dimension": null_dimension,
        "C_gamma5_relation_holds": relation_holds,
        "P_X_transpose_C_inverse_equals_C_inverse_P_X": no_flip,
        "C1_particle_hole": c1,
        "C2_particle_particle": c2,
        "classifications_are_inverted_in_field_labels": inverted,
        "projector_index_patterns_are_identical": projector_patterns_identical,
        "what_the_inversion_actually_is":
            "the two projector tables have IDENTICAL non-zero patterns. The "
            "inversion is the bar-flip psibar_L = psibar P_R on the particle-hole "
            "side together with the ABSENCE of a flip on the particle-particle "
            "side. C g5^T C^-1 = +g5 is what delivers that absence: had it been "
            "-g5, the pp side would have flipped too and the two classifications "
            "would have AGREED in field labels.",
        "no_pp_coefficient_decomposition_performed": True,
        "no_slot_map_chosen": True,
    }


def step_C3_census(g: list[np.ndarray]) -> dict:
    """The census of the source itself, computed."""
    g5 = gamma5(g)
    identity = np.eye(4, dtype=complex)
    p_l, p_r = projectors(g)
    sources = {
        "frozen": kron4(identity, identity) + kron4(1j * g5, 1j * g5),
        "no_i": kron4(identity, identity) + kron4(g5, g5),
    }
    components = {
        "psibar_L psi_R x psibar_R psi_L": (p_r, p_l),
        "psibar_R psi_L x psibar_L psi_R": (p_l, p_r),
        "psibar_L psi_R x psibar_L psi_R": (p_r, p_r),
        "psibar_R psi_L x psibar_R psi_L": (p_l, p_l),
    }
    out: dict[str, dict] = {}
    for name, tensor in sources.items():
        row = {}
        for label, (k1, k2) in components.items():
            numerator = np.einsum("abcd,ab,cd->", tensor, np.conj(k1), np.conj(k2))
            denominator = np.einsum(
                "ab,cd,ab,cd->", k1, k2, np.conj(k1), np.conj(k2)
            )
            row[label] = float(np.round((numerator / denominator).real, 9))
        out[name] = row
    return {
        "coefficients": out,
        "frozen_census": "psibar_L, psi_R, psibar_R, psi_L — one of each",
        "no_i_census": "psibar_L, psi_R, psibar_L, psi_R — two of each, doubled "
                       "(plus the L <-> R mirror term)",
        "ll_rr_restriction_note":
            "the frozen source has exactly 0 in the doubled components, so "
            "projecting it onto an LL/RR-type sector and finding zero is close to "
            "tautological. Recorded for completeness; NOT offered as support. "
            "Step D carries the falsification.",
    }


# ------------------------------------------------- Step D: falsification ---
CRITERION = (
    "Write the interaction's rank-4 tensor in the chiral projector basis as a sum "
    "of terms K1 (x) K2 with K in {P_L, P_R}. Each term fixes the chirality of the "
    "four fields psibar_a psi_b psibar_c psi_d. The particle-hole exchange re-pairs "
    "them as (psibar_a psi_d)(psibar_c psi_b). If every term gives SAME-chirality "
    "exchange pairs, only V and A can appear and S, P, T must vanish. If every term "
    "gives OPPOSITE-chirality exchange pairs, only S, P, T can appear and V, A must "
    "vanish. If terms of both kinds are present, no family is excluded."
)

# Recorded in derivations/P2-PHASE-01_chirality_census.md, an EARLIER COMMIT than
# this file.  The git history is the evidence of ordering.
PREDICTIONS = {
    "D0_frozen": {
        "interaction": "S^2 + P^2 with the frozen P = i*gamma5",
        "census": "one of each; exchange pairs (psibar_L psi_L) and "
                  "(psibar_R psi_R), both SAME",
        "predicted_nonzero": ["V", "A"],
        "predicted_zero": ["S", "P", "T"],
    },
    "D1_no_i": {
        "interaction": "S^2 + (gamma5 term)^2, the i dropped",
        "census": "doubled; exchange pairs (psibar_L psi_R) and "
                  "(psibar_L psi_R), both OPPOSITE",
        "predicted_nonzero": ["S", "P", "T"],
        "predicted_zero": ["V", "A"],
    },
    "D4_chosen": {
        "interaction": "(psibar i*gamma5 psi)^2 only, with the frozen i",
        "why_chosen": "the criterion's two exclusion branches are the easy ones; a "
                      "criterion that only ever forbids things can look successful "
                      "without discriminating. The no-exclusion branch is where a "
                      "criterion fitted after seeing the answer would most likely "
                      "fail, so that is the branch worth testing.",
        "census": "-g5(x)g5 = -P_R(x)P_R + P_R(x)P_L + P_L(x)P_R - P_L(x)P_L: BOTH "
                  "one-of-each and doubled terms, so the third branch applies",
        "predicted_nonzero": ["S", "P", "V", "A", "T"],
        "predicted_zero": [],
    },
}

# Source rows in the FROZEN family basis (S, P, V, A, T).  The canonical operators
# use i*gamma5 while the frozen family basis uses gamma5, hence the sign on P.
SOURCE_ROWS = {
    "D0_frozen": [1, -1, 0, 0, 0],
    "D1_no_i": [1, 1, 0, 0, 0],
    "D4_chosen": [0, -1, 0, 0, 0],
}


def step_D() -> dict:
    """Compute the particle-hole exchange support and score the predictions."""
    block = json.loads(linecache.getline(str(FREEZE), BASIS_BLOCK_LINE))
    standalone = json.loads(FIERZ_JSON.read_text(encoding="utf-8"))
    if standalone["matrix_rational"] != block["matrix_rational"]:
        raise AssertionError("standalone Fierz artifact disagrees with the freeze")
    fierz = sp.Matrix(
        [[sp.Rational(entry) for entry in row] for row in block["matrix_rational"]]
    )
    order = block["basis_order"]

    results: dict[str, dict] = {}
    for key, row in SOURCE_ROWS.items():
        exchanged = sp.Matrix([row]) * fierz
        coefficients = {
            order[i]: sp.simplify(S_G * exchanged[i]) for i in range(len(order))
        }
        nonzero = sorted(k for k, v in coefficients.items() if v != 0)
        zero = sorted(k for k, v in coefficients.items() if v == 0)
        predicted = PREDICTIONS[key]
        correct = (
            nonzero == sorted(predicted["predicted_nonzero"])
            and zero == sorted(predicted["predicted_zero"])
        )
        results[key] = {
            **predicted,
            "source_row_in_the_frozen_basis": row,
            "computed_coefficients": {k: str(v) for k, v in coefficients.items()},
            "computed_nonzero": nonzero,
            "computed_zero": zero,
            "prediction_correct": correct,
        }
    return {
        "criterion": CRITERION,
        "prediction_recorded_before_computation": True,
        "evidence_of_ordering": "the predictions are in "
                                "derivations/P2-PHASE-01_chirality_census.md, "
                                "committed before this script",
        "s_G_applied_once": S_G,
        "cases": results,
        "all_predictions_correct": all(
            case["prediction_correct"] for case in results.values()
        ),
        "channel_tested": "particle-hole ONLY",
        "why_not_particle_particle":
            "a particle-particle coefficient decomposition would require the "
            "unfrozen pp Grassmann ordering. The pp side is tested structurally, "
            "through C2 and C3, and no coefficient decomposition is performed.",
    }


def comparison_with_the_pinned_result() -> dict:
    """Compare D0 with the recorded particle-hole coefficients on main."""
    pinned = json.loads(CHANNEL_JSON.read_text(encoding="utf-8"))["layer_1a"]
    return {
        "pinned_operator_level_normalisation_L":
            pinned["operator_level_normalisation_L"],
        "pinned_vanishing_families": pinned["vanishing_families"],
        "pinned_dirac_row": pinned["dirac_row_after_frozen_matrix"],
        "census_predicted_vanishing": PREDICTIONS["D0_frozen"]["predicted_zero"],
        "agree": sorted(pinned["vanishing_families"])
                 == sorted(PREDICTIONS["D0_frozen"]["predicted_zero"]),
        "note": "the pinned coefficients carry the canonical factor and s_G; the "
                "census predicts which families vanish, not their magnitude",
    }


# ---------------------------------------------------------------- Step E ---
def step_E() -> dict:
    return {
        "does_not_explain": [
            "the inter-channel sign: V = +A in particle-hole against V = -A in "
            "particle-particle. A census counts fields; it does not distinguish "
            "them, and this task does not attempt it.",
            "the magnitudes. The census says which families can form, not with "
            "what coefficient; -G/4 is not derived here.",
            "the V/A degeneracy in the particle-hole channel: both exchange pairs "
            "are same-chirality and the census does not separate them.",
            "anything about states. Which operators can form is not a bound-state "
            "or pole calculation.",
            "the particle-particle coefficients, which are not computed here.",
        ],
    }


def scope_limits() -> dict:
    return {
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "conventions_frozen_by_this_task": [],
        "new_programme_coefficient_or_channel_character_result": False,
        "coefficients_are_diagnostic_reproductions_only": True,
        "branches_not_read": branches_not_read(),
        "no_composite_vector_statement": "this is a structural argument about "
                                         "which operators can form, not a "
                                         "bound-state calculation",
        "no_diquark_channel_settled": "eta, the pp Grassmann ordering and the "
                                      "diquark normalisation remain unfrozen, and "
                                      "the branches carrying those coefficients "
                                      "are not integrated",
        "no_hubbard_stratonovich_selection": True,
        "census_does_not_explain_the_inter_channel_sign": True,
    }


def build() -> dict:
    tables = {
        name: chirality_tables(factory()) for name, factory in REPRESENTATIONS.items()
    }
    names = list(tables)
    agree = all(
        tables[names[0]][key] == tables[names[1]][key]
        for key in ("C1_particle_hole", "C2_particle_particle")
    )
    return {
        "gate": "P2-PHASE-01",
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "deliverable": "the chirality census",
        "repository_inputs": repository_inputs(),
        "pinned_inputs": pinned_inputs(),
        "frozen_conventions": frozen_conventions(),
        "step_A_factorisation": {
            name: step_A(factory()) for name, factory in REPRESENTATIONS.items()
        },
        "step_BC_chirality_tables": tables,
        "representation_independence": {
            "representations": names,
            "C1_and_C2_agree_in_both": agree,
            "if_they_did_not": "the classification would be representation-"
                               "dependent and the argument would fail; that would "
                               "be reported rather than resolved by choosing one",
        },
        "step_C3_census": {
            name: step_C3_census(factory()) for name, factory in REPRESENTATIONS.items()
        },
        "step_D_falsification": step_D(),
        "comparison_with_the_pinned_particle_hole_result":
            comparison_with_the_pinned_result(),
        "step_E_not_explained": step_E(),
        "scope_limits": scope_limits(),
    }


def main() -> None:
    payload = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
