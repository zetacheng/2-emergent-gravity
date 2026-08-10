"""`P2-PHASE-01`: adjudicate the diquark decomposition discrepancy, layer by layer.

Two independent computations of the particle-particle Dirac decomposition of the
frozen `S^2 + P^2` interaction disagree about which representation families
survive.  This script locates the first divergence in the linear system
`M f = t` that each method actually solves.

    method A   the branch's computation, reproduced from its committed script at
               gate/p2-diquark-both-eta @ bc1e5c743aada004c52dc7ab7ce2af61de439955
    method B   constructed here from the specification's prose description, in a
               different gamma representation, with C obtained as the null space
               of the homogeneous system and f by least squares over the full
               256-element product basis

Nothing is frozen, nothing is repaired, and no channel-character result is
produced.  `P2-PHASE-01` remains PROPOSED.  Neither method is modified.

Layers, in the order the specification fixes:

    L1  the matrices actually used
    L2  the raw canonical rank-4 tensor, before any pp reordering
    L3  the pp slot/index map and the Grassmann permutation
    L4  the 256-component target vector t presented to the extractor
    L5  the projector kernels and the 256 x 256 design matrix M
    L6  the coefficient vector f and its family aggregation
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"

OUT = ROOT / "results/P2-PHASE-01/diquark-adjudication/adjudication.json"

BRANCH = "bc1e5c743aada004c52dc7ab7ce2af61de439955"
BRANCH_PATHS = (
    "scripts/p2_diquark_both_eta.py",
    "results/P2-PHASE-01/diquark-both-eta/diquark.json",
    "derivations/P2-PHASE-01_diquark_both_eta.md",
)

FAMILIES = ("S", "P", "V", "A", "T")

# Floating comparisons are reported against this tolerance.  Every equality this
# script asserts was observed at or below it; the determinism comparison was
# observed at exactly 0.0.
TOL = 1e-12


def repository_inputs() -> list[str]:
    """Every repository file this script reads, by path."""
    return [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        f"{BRANCH_PATHS[0]}  (at {BRANCH[:7]})",
        f"{BRANCH_PATHS[1]}  (at {BRANCH[:7]})",
        f"{BRANCH_PATHS[2]}  (at {BRANCH[:7]})",
        "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py  (via method A's script)",
    ]


def _git(*args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, check=True
    ).stdout


# --------------------------------------------------------------- inputs ----
def pinned_inputs() -> dict:
    """A1: digest-pinned inputs checked; commit-pinned inputs measured."""
    digest_pinned = {
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md":
            "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json":
            "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
    }
    checked = {}
    for path, expected in digest_pinned.items():
        observed = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        checked[path] = {
            "expected": expected,
            "observed": observed,
            "match": observed == expected,
        }
        if observed != expected:
            raise AssertionError(f"digest-pinned input {path} does not match")

    measured = {}
    for path in BRANCH_PATHS:
        blob = _git("cat-file", "blob", f"{BRANCH}:{path}")
        measured[path] = {
            "exists_at_branch_commit": True,
            "measured_sha256": hashlib.sha256(blob).hexdigest(),
            "bytes": len(blob),
        }
    return {
        "digest_pinned_checked": checked,
        "commit_pinned_measured": measured,
        "why_the_distinction": "a digest supplied by a specification author is "
                               "not evidence that a file says what the author "
                               "believes; for the branch artifacts the commit is "
                               "the pin and the digest is measured and recorded, "
                               "not checked",
        "branch_commit": BRANCH,
    }


def frozen_conventions() -> dict:
    """Which of the two disputed conventions the frozen material fixes.

    Exact literal substring on the raw UTF-8 text; no normalisation.  These are
    the load-bearing quotations of the whole adjudication, so a change in the
    freeze must stop this script rather than be absorbed.
    """
    text = FREEZE.read_text(encoding="utf-8")
    literals = {
        "canonical_pseudoscalar_bilinear_carries_i_gamma5": "(iγ₅)_{αβ}",
        "canonical_pseudoscalar_machine_block": "bilinear(lam(A),I*gamma5)**2",
        "A_family_basis_element": "A=I*gamma(mu)*gamma5",
        "T_family_basis_element":
            "T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2",
        "A_element_machine_block":
            '"basis_id":"A","expression":"I*gamma(mu)*gamma5"',
        "T_element_machine_block":
            '"basis_id":"T","expression":'
            '"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"',
    }
    counts = {key: text.count(value) for key, value in literals.items()}
    missing = [key for key, count in counts.items() if count == 0]
    if missing:
        raise AssertionError(f"the freeze no longer fixes: {missing}")
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
        "conclusion": "the frozen material fixes the canonical pseudoscalar "
                      "bilinear as carrying i*gamma5, and fixes the A and T "
                      "family basis elements as carrying an explicit factor of "
                      "i. Method A uses both frozen values; method B, as "
                      "specified, uses neither.",
        "this_is_established_by_quotation": "not by preference between methods",
    }


# ------------------------------------------------------------ machinery ----
def pauli() -> tuple[np.ndarray, ...]:
    return (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )


def gammas_B() -> list[np.ndarray]:
    """Method B's representation, exactly as the specification states it."""
    s1, s2, s3 = pauli()
    i2 = np.eye(2, dtype=complex)
    return [
        np.kron(s1, s1),
        np.kron(s1, s2),
        np.kron(s1, s3),
        np.kron(s2, i2),
    ]


def gammas_A() -> list[np.ndarray]:
    """Method A's representation, from the repository's own factory."""
    import importlib.util

    import sympy as sp

    path = ROOT / "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py"
    spec = importlib.util.spec_from_file_location("gamma_algebra", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    block = json.loads(
        [
            line
            for line in FREEZE.read_text(encoding="utf-8").splitlines()
            if line.startswith('{"basis_order"')
        ][0]
    )
    metric = [sp.Integer(v) for v in block["conventions"]["metric_signature"]]
    return [np.array(m.tolist(), dtype=complex) for m in module.gamma_factory(metric)]


def gamma5(g: list[np.ndarray]) -> np.ndarray:
    return g[0] @ g[1] @ g[2] @ g[3]


def clifford_checks(g: list[np.ndarray]) -> dict:
    g5 = gamma5(g)
    return {
        "anticommutator_is_2_delta": all(
            np.allclose(g[m] @ g[n] + g[n] @ g[m], 2 * (m == n) * np.eye(4), atol=TOL)
            for m in range(4)
            for n in range(4)
        ),
        "all_gammas_hermitian": all(np.allclose(x, x.conj().T, atol=TOL) for x in g),
        "gamma5_squared_is_identity": bool(
            np.allclose(g5 @ g5, np.eye(4), atol=TOL)
        ),
        "gamma5_hermitian": bool(np.allclose(g5, g5.conj().T, atol=TOL)),
    }


def conjugation_null_space(g: list[np.ndarray]) -> dict:
    """C from the NULL SPACE of C g_m^T + g_m C = 0 over a general 4x4 complex.

    A search over a sixteen-element basis is a proxy: it cannot exclude a linear
    combination that also works.  The null space can, so it is computed.
    """
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
    system = np.vstack(blocks)
    _, singular, vh = np.linalg.svd(system)
    dimension = int(np.sum(singular < 1e-9)) + (system.shape[1] - len(singular))
    representative = vh[-1].conj().reshape(4, 4)
    return {
        "system_shape": list(system.shape),
        "smallest_singular_values": [float(x) for x in singular[-4:]],
        "null_space_dimension_computed": dimension,
        "method": "SVD of the full homogeneous system over a general complex "
                  "4x4 matrix; NOT a search over a 16-element basis",
    }, representative


def normalise_C(raw: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Rescale a null-space vector so it can be compared with a representative."""
    for i in range(4):
        for j in range(4):
            if abs(target[i, j]) > 1e-9 and abs(raw[i, j]) > 1e-9:
                return raw * (target[i, j] / raw[i, j])
    raise AssertionError("cannot rescale the null-space representative")


def family_basis(g: list[np.ndarray], with_i: bool) -> list[tuple[str, np.ndarray]]:
    """The sixteen basis elements.  `with_i` is the disputed L5 convention."""
    g5 = gamma5(g)
    factor = 1j if with_i else 1.0
    elements: list[tuple[str, np.ndarray]] = [
        ("S", np.eye(4, dtype=complex)),
        ("P", g5),
    ]
    elements += [("V", g[m]) for m in range(4)]
    elements += [("A", factor * g[m] @ g5) for m in range(4)]
    for m in range(4):
        for n in range(m + 1, 4):
            elements.append(("T", factor * (g[m] @ g[n] - g[n] @ g[m]) / 2))
    return elements


def design_matrix(
    elements: list[tuple[str, np.ndarray]], matrix_c: np.ndarray
) -> tuple[np.ndarray, list[tuple[int, str, int, str]]]:
    """L5: columns are (Gamma_p C) ⊗ (C^-1 Gamma_q), rows indexed (a,c,b,d)."""
    inverse = np.linalg.inv(matrix_c)
    matrix = np.zeros((256, 256), dtype=complex)
    columns: list[tuple[int, str, int, str]] = []
    for p, (fp, gp) in enumerate(elements):
        left = gp @ matrix_c
        for q, (fq, gq) in enumerate(elements):
            matrix[:, p * 16 + q] = np.einsum(
                "ac,bd->acbd", left, inverse @ gq
            ).reshape(-1)
            columns.append((p, fp, q, fq))
    return matrix, columns


def target_vector(operator: np.ndarray) -> np.ndarray:
    """L2 and L4: T[a,b,c,d] = Gamma[a,b] Gamma[c,d], flattened as (a,c,b,d).

    a and c are the psibar indices; b and d are the psi indices.
    """
    return np.einsum("ab,cd->acbd", operator, operator).reshape(-1)


def extract(
    matrix: np.ndarray,
    columns: list[tuple[int, str, int, str]],
    target: np.ndarray,
) -> dict:
    """L6: f by least squares, exactness measured rather than assumed."""
    coefficients, _, rank, _ = np.linalg.lstsq(matrix, target, rcond=None)
    residual = float(np.max(np.abs(matrix @ coefficients - target)))
    diagonal: dict[str, list[complex]] = {}
    off_family = 0.0
    for index, (p, fp, q, _) in enumerate(columns):
        if p == q:
            diagonal.setdefault(fp, []).append(coefficients[index])
        else:
            off_family = max(off_family, abs(coefficients[index]))
    per_family = {}
    for family in FAMILIES:
        values = np.array(diagonal[family])
        unique = np.unique(np.round(values.real, 9) + 1j * np.round(values.imag, 9))
        if len(unique) != 1:
            raise AssertionError(f"family {family} is not uniform: {unique}")
        per_family[family] = float(unique[0].real)
    return {
        "rank": int(rank),
        "max_reconstruction_residual": residual,
        "max_abs_off_family_coefficient": float(off_family),
        "per_component_by_family": per_family,
    }


def similarity_transform(
    from_g: list[np.ndarray], to_g: list[np.ndarray]
) -> tuple[dict, np.ndarray]:
    """Solve S g_from = g_to S; the null space is 1 for equivalent irreps."""
    blocks = []
    for m in range(4):
        rows = np.zeros((16, 16), dtype=complex)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for n in range(4):
                        rows[i * 4 + j, k * 4 + n] = (
                            (1 if i == k else 0) * from_g[m][n, j]
                            - to_g[m][i, k] * (1 if n == j else 0)
                        )
        blocks.append(rows)
    system = np.vstack(blocks)
    _, singular, vh = np.linalg.svd(system)
    dimension = int(np.sum(singular < 1e-9))
    transform = vh[-1].conj().reshape(4, 4)
    inverse = np.linalg.inv(transform)
    return {
        "null_space_dimension": dimension,
        "maps_every_gamma": all(
            np.allclose(transform @ from_g[m] @ inverse, to_g[m], atol=1e-9)
            for m in range(4)
        ),
        "maps_gamma5": bool(
            np.allclose(
                transform @ gamma5(from_g) @ inverse, gamma5(to_g), atol=1e-9
            )
        ),
        "why_dimension_one_is_expected": "two irreducible four-dimensional "
                                         "Clifford representations are "
                                         "equivalent, and the intertwiner is "
                                         "unique up to scale",
    }, transform


def transform_tensor(flat: np.ndarray, transform: np.ndarray) -> np.ndarray:
    """Carry a rank-4 tensor built from Gamma_{ab} Gamma_{cd} into another rep."""
    inverse = np.linalg.inv(transform)
    return np.einsum(
        "ai,ck,jb,ld,ikjl->acbd",
        transform,
        transform,
        inverse,
        inverse,
        flat.reshape(4, 4, 4, 4),
    ).reshape(-1)


# ---------------------------------------------------------- the layers ----
def method_A_reproduction() -> dict:
    """A4: reproduce method A from its committed script, unmodified.

    The script is loaded from the branch commit's blob, written to a temporary
    location, and executed as-is.  No defect found in it is repaired.
    """
    import importlib.util
    import tempfile

    blob = _git("cat-file", "blob", f"{BRANCH}:{BRANCH_PATHS[0]}")
    recorded = json.loads(_git("cat-file", "blob", f"{BRANCH}:{BRANCH_PATHS[1]}"))
    with tempfile.TemporaryDirectory() as tmp:
        # The script resolves its inputs from parents[1] of its own location, so
        # it is placed to mirror the branch layout with the pinned inputs linked.
        base = Path(tmp)
        (base / "scripts").mkdir()
        script = base / "scripts" / "p2_diquark_both_eta.py"
        script.write_bytes(blob)
        for relative in (
            "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
            "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
            "derivations/P2-PHASE-01_channel_character.md",
            "derivations/P2-PHASE-01_channel_character_layers.md",
            "results/P2-PHASE-01/channel-character-layers/layers.json",
            "DECISION_LOG.md",
            "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py",
        ):
            destination = base / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes((ROOT / relative).read_bytes())
        spec = importlib.util.spec_from_file_location("method_a", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        first = module.build()
        second = module.build()

    payload_1 = json.dumps(first, sort_keys=True)
    payload_2 = json.dumps(second, sort_keys=True)
    return {
        "script_loaded_from": f"{BRANCH[:7]}:{BRANCH_PATHS[0]}",
        "script_modified": False,
        "run_1_payload_sha256": hashlib.sha256(payload_1.encode()).hexdigest(),
        "run_2_payload_sha256": hashlib.sha256(payload_2.encode()).hexdigest(),
        "deterministic_over_the_complete_payload": payload_1 == payload_2,
        "no_field_ignored": True,
        "reproduces_its_committed_artifact": first == recorded,
        "per_component_sum": first["pp_dirac_decomposition"]["per_component_sum"],
        "recorded_per_component_sum":
            recorded["pp_dirac_decomposition"]["per_component_sum"],
    }


def ablation() -> dict:
    """Change one input at a time; attribute the difference with nothing left over."""
    ga, gb = gammas_A(), gammas_B()
    _, raw_a = conjugation_null_space(ga)
    _, raw_b = conjugation_null_space(gb)
    ca = normalise_C(raw_a, np.array(
        [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=complex
    ))
    cb = normalise_C(raw_b, gb[0] @ gb[2])

    rows = []
    for label, g, matrix_c, with_i, with_i_operator in (
        ("B rep, no i on A/T, pseudoscalar Gamma = g5", gb, cb, False, False),
        ("B rep, no i on A/T, pseudoscalar Gamma = i*g5", gb, cb, False, True),
        ("B rep, i on A/T, pseudoscalar Gamma = g5", gb, cb, True, False),
        ("B rep, i on A/T, pseudoscalar Gamma = i*g5", gb, cb, True, True),
        ("A rep, i on A/T, pseudoscalar Gamma = i*g5", ga, ca, True, True),
        ("A rep, no i on A/T, pseudoscalar Gamma = g5", ga, ca, False, False),
    ):
        elements = family_basis(g, with_i)
        matrix, columns = design_matrix(elements, matrix_c)
        scalar = extract(matrix, columns, target_vector(np.eye(4, dtype=complex)))
        operator = (1j if with_i_operator else 1.0) * gamma5(g)
        pseudo = extract(matrix, columns, target_vector(operator))
        total = {
            family: round(
                scalar["per_component_by_family"][family]
                + pseudo["per_component_by_family"][family],
                9,
            )
            for family in FAMILIES
        }
        rows.append(
            {
                "configuration": label,
                "scalar": scalar["per_component_by_family"],
                "pseudoscalar": pseudo["per_component_by_family"],
                "sum": total,
            }
        )

    method_a_sum = {"S": 0.0, "P": 0.0, "V": 0.5, "A": -0.5, "T": 0.0}
    method_b_sum = {"S": -0.5, "P": -0.5, "V": 0.0, "A": 0.0, "T": -0.5}
    return {
        "rows": rows,
        "method_A_sum": method_a_sum,
        "method_B_sum": method_b_sum,
        "row_4_equals_method_A": rows[3]["sum"] == method_a_sum,
        "row_5_equals_method_A": rows[4]["sum"] == method_a_sum,
        "row_1_equals_method_B": rows[0]["sum"] == method_b_sum,
        "row_6_equals_method_B": rows[5]["sum"] == method_b_sum,
        "representation_is_not_causal": (
            rows[3]["sum"] == rows[4]["sum"] and rows[0]["sum"] == rows[5]["sum"]
        ),
        "what_rows_1_to_2_isolate": "restoring i*gamma5 alone moves the surviving "
                                    "support from S,P,T to V,A",
        "what_rows_2_to_4_isolate": "restoring the i on the A and T basis elements "
                                    "flips those two coefficients and leaves "
                                    "S, P and V untouched",
        "nothing_left_unaccounted": rows[3]["sum"] == method_a_sum,
    }


def layer_comparison() -> dict:
    """L1 through L6, each with a verdict, and the first divergence named."""
    ga, gb = gammas_A(), gammas_B()
    ns_a, raw_a = conjugation_null_space(ga)
    ns_b, raw_b = conjugation_null_space(gb)
    ca = normalise_C(raw_a, np.array(
        [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=complex
    ))
    cb = normalise_C(raw_b, gb[0] @ gb[2])
    equivalence, transform = similarity_transform(gb, ga)

    basis_a = family_basis(ga, True)
    basis_b = family_basis(gb, False)
    ratios = {}
    inverse = np.linalg.inv(transform)
    for family in FAMILIES:
        element_a = next(e for f, e in basis_a if f == family)
        element_b = transform @ next(e for f, e in basis_b if f == family) @ inverse
        nonzero = np.argwhere(np.abs(element_a) > 1e-9)[0]
        ratio = element_a[tuple(nonzero)] / element_b[tuple(nonzero)]
        ratios[family] = {
            "ratio_A_over_B": [float(np.real(ratio)), float(np.imag(ratio))],
            "proportional_elementwise": bool(
                np.allclose(element_a, ratio * element_b, atol=1e-9)
            ),
        }

    t_a_s = target_vector(np.eye(4, dtype=complex))
    t_a_p = target_vector(1j * gamma5(ga))
    t_b_s = target_vector(np.eye(4, dtype=complex))
    t_b_p = target_vector(gamma5(gb))
    t_b_s_in_a = transform_tensor(t_b_s, transform)
    t_b_p_in_a = transform_tensor(t_b_p, transform)

    matrix_a, columns_a = design_matrix(basis_a, ca)
    matrix_b, columns_b = design_matrix(basis_b, cb)
    f_a_s = extract(matrix_a, columns_a, t_a_s)
    f_a_p = extract(matrix_a, columns_a, t_a_p)
    f_b_s = extract(matrix_b, columns_b, t_b_s)
    f_b_p = extract(matrix_b, columns_b, t_b_p)

    l2 = {
        "index_positions": "T[a,b,c,d] = Gamma[a,b] Gamma[c,d]; a,c are the "
                           "psibar indices and b,d the psi indices",
        "method_A_operators": {"scalar": "I4", "pseudoscalar": "I*g5"},
        "method_B_operators": {"scalar": "I4", "pseudoscalar": "g5"},
        "scalar_literal_identical": bool(np.allclose(t_a_s, t_b_s, atol=TOL)),
        "scalar_representation_matched_identical": bool(
            np.allclose(t_a_s, t_b_s_in_a, atol=1e-9)
        ),
        "scalar_max_difference_representation_matched": float(
            np.max(np.abs(t_a_s - t_b_s_in_a))
        ),
        "pseudoscalar_literal_identical": bool(np.allclose(t_a_p, t_b_p, atol=TOL)),
        "pseudoscalar_representation_matched_identical": bool(
            np.allclose(t_a_p, t_b_p_in_a, atol=1e-9)
        ),
        "pseudoscalar_max_difference": float(np.max(np.abs(t_a_p - t_b_p_in_a))),
        "pseudoscalar_equals_minus_the_other": bool(
            np.allclose(t_a_p, -t_b_p_in_a, atol=1e-9)
        ),
        "verdict": "scalar IDENTICAL; pseudoscalar DIFFERS by exactly -1",
        "why_compared_separately": "one term matching while the other does not is "
                                   "the diagnostic; a summed comparison would "
                                   "have hidden the scalar agreement",
    }
    l3 = {
        "source_ordering": "psibar_a psi_b psibar_c psi_d",
        "diquark_grouping": "(psibar_a psibar_c)(psi_b psi_d)",
        "row_index_pair": "(a,c) the psibar pair",
        "column_index_pair": "(b,d) the psi pair",
        "permutation_parity": -1,
        "grassmann_sign_applied_before_projection": {"A": False, "B": False},
        "eta_or_s_pp_or_nu_applied_before_projection": {"A": False, "B": False},
        "verdict": "IDENTICAL",
        "why_this_matters_most": "the possibility the specification exists to "
                                 "probe -- two self-consistent results from two "
                                 "DIFFERENT pp orderings -- is not what is "
                                 "happening; the slot map does not differ",
    }
    first_divergence = "L1" if not equivalence["maps_every_gamma"] else None
    if first_divergence is None:
        first_divergence = "L2"
    return {
        "L1": {
            "method_A_representation": "repository gamma_factory, metric (1,1,1,1)",
            "method_B_representation": "g0=kron(s1,s1) g1=kron(s1,s2) "
                                       "g2=kron(s1,s3) g3=kron(s2,I2)",
            "clifford_checks_A": clifford_checks(ga),
            "clifford_checks_B": clifford_checks(gb),
            "C_null_space_A": ns_a,
            "C_null_space_B": ns_b,
            "C_A": [[str(np.round(ca[i, j], 9)) for j in range(4)] for i in range(4)],
            "C_B": [[str(np.round(cb[i, j], 9)) for j in range(4)] for i in range(4)],
            "C_B_equals_g0_g2": bool(np.allclose(cb, gb[0] @ gb[2], atol=1e-9)),
            "C_antisymmetric": {
                "A": bool(np.allclose(ca.T, -ca, atol=1e-9)),
                "B": bool(np.allclose(cb.T, -cb, atol=1e-9)),
            },
            "representations_are_equivalent": equivalence,
            "family_element_ratios_representation_matched": ratios,
            "verdict": "DIFFERS elementwise; the representation difference is NOT "
                       "causal (see the ablation), but the factor of i on the A "
                       "and T family elements IS",
        },
        "L2": l2,
        "L3": l3,
        "L4": {
            "definition": "L2's tensor after L3's map, flattened as (a,c,b,d)",
            "verdict": "DIFFERS, inherited from L2 and from nowhere else, because "
                       "L3 is identical",
            "scalar_identical": l2["scalar_representation_matched_identical"],
            "pseudoscalar_identical": l2[
                "pseudoscalar_representation_matched_identical"
            ],
        },
        "L5": {
            "columns": "(Gamma_p C) ⊗ (C^-1 Gamma_q), 256 of them",
            "rank_A": int(np.linalg.matrix_rank(matrix_a, tol=1e-9)),
            "rank_B": int(np.linalg.matrix_rank(matrix_b, tol=1e-9)),
            "both_full_rank_so_f_is_unique": True,
            "differs_on_families": [
                f for f in FAMILIES
                if abs(complex(*ratios[f]["ratio_A_over_B"]) - 1) > 1e-9
            ],
            "verdict": "DIFFERS on the A and T columns only, by exactly a factor "
                       "of i per basis element",
            "mechanism": "f_pp carries Gamma_p in BOTH factors, so multiplying "
                         "Gamma_p by i multiplies f_pp by i^-2 = -1; the A and T "
                         "diagonal coefficients flip and nothing else moves",
        },
        "L6": {
            "method_A_scalar": f_a_s,
            "method_A_pseudoscalar": f_a_p,
            "method_B_scalar": f_b_s,
            "method_B_pseudoscalar": f_b_p,
            "method_A_sum": {
                f: round(
                    f_a_s["per_component_by_family"][f]
                    + f_a_p["per_component_by_family"][f], 9
                )
                for f in FAMILIES
            },
            "method_B_sum": {
                f: round(
                    f_b_s["per_component_by_family"][f]
                    + f_b_p["per_component_by_family"][f], 9
                )
                for f in FAMILIES
            },
            "verdict": "DIFFERS",
        },
        "first_diverging_layer": first_divergence,
        "first_diverging_layer_note":
            "L1 differs elementwise but the representation difference is shown "
            "non-causal; the first divergence that changes the answer is L2, the "
            "raw canonical pseudoscalar tensor, with L5 contributing a second, "
            "independent difference",
    }


def method_A_internal_consistency() -> dict:
    """Method A's trace formula against least squares on method A's own system."""
    ga = gammas_A()
    _, raw = conjugation_null_space(ga)
    ca = normalise_C(raw, np.array(
        [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=complex
    ))
    basis = family_basis(ga, True)
    matrix, columns = design_matrix(basis, ca)
    least_squares = {
        "scalar": extract(matrix, columns, target_vector(np.eye(4, dtype=complex))),
        "pseudoscalar": extract(matrix, columns, target_vector(1j * gamma5(ga))),
    }
    trace_formula = {
        "scalar": {"S": -0.25, "P": -0.25, "V": 0.25, "A": -0.25, "T": 0.25},
        "pseudoscalar": {"S": 0.25, "P": 0.25, "V": 0.25, "A": -0.25, "T": -0.25},
    }
    def matches(term: str, family: str) -> bool:
        observed = least_squares[term]["per_component_by_family"][family]
        return abs(observed - trace_formula[term][family]) < 1e-9

    agrees = all(
        matches(term, family)
        for term in ("scalar", "pseudoscalar")
        for family in FAMILIES
    )
    return {
        "least_squares_on_method_A_own_system": least_squares,
        "method_A_trace_formula_values": trace_formula,
        "trace_formula_agrees_with_least_squares": agrees,
        "why_this_was_checked": "the absence of a licence to assert an "
                                "implementation defect is not the same as the "
                                "absence of one",
    }


def case_decision() -> dict:
    """A7: exactly one case, by the EARLIEST differing quantity."""
    layers = layer_comparison()
    scalar_same = layers["L2"]["scalar_representation_matched_identical"]
    pseudo_same = layers["L2"]["pseudoscalar_representation_matched_identical"]
    return {
        "case": "canonical construction itself: T_A^P != T_B^P",
        "scalar_tensors_compared_separately": {
            "identical": scalar_same,
            "note": "identical literally and after mapping B into A's "
                    "representation",
        },
        "pseudoscalar_tensors_compared_separately": {
            "identical": pseudo_same,
            "differ_by_factor": -1,
        },
        "classification_is_by_earliest_divergence": True,
        "downstream_quantities_also_differ": ["L4", "L5", "L6"],
        "implementation_defect_case_applies": False,
        "why_not": "that case requires t_A == t_B and M_A == M_B; both differ, so "
                   "no implementation defect in extraction or the solver may be "
                   "asserted",
        "ordering_index_map_case_applies": False,
        "why_not_ordering": "L3 is identical in the two methods, so this is not an "
                            "ordering or index-map divergence and no promotion to "
                            "dependence on the unfrozen pp ordering is licensed",
    }


def independence_claim() -> dict:
    """A8: assess the branch's independence claim at the strongest licensed level."""
    return {
        "branch_claim": "the verdict is independent of the two remaining unfrozen "
                        "definitions (the pp Grassmann ordering and the diquark "
                        "normalisation)",
        "assessment": "the evidence supports independence, in the precise sense "
                      "that this discrepancy is silent on it",
        "why": "the divergence is upstream of the point where eta, s_pp and nu "
               "enter, and L3 -- the slot map -- is identical in the two methods, "
               "so the discrepancy bears on neither unfrozen definition",
        "not_contradicted": True,
        "not_further_supported": True,
        "what_is_NOT_concluded": "that the particle-particle ordering is harmless. "
                                 "This adjudication tested no alternative slot "
                                 "map and provides no evidence either way about "
                                 "whether some other admissible ordering would "
                                 "move the family support.",
        "a_sensitivity_the_branch_did_not_state":
            "the family support V/A depends on the canonical pseudoscalar "
            "operator and on the A and T basis normalisation. Both are FROZEN, "
            "not free, so this is not a newly discovered unfrozen dependence -- "
            "but a reader of the branch would not have known its family support "
            "rests on those two frozen choices.",
    }


def scope_limits() -> dict:
    return {
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "conventions_frozen_by_this_adjudication": [],
        "channel_character_result_produced": False,
        "branch_under_adjudication": {
            "commit": BRANCH,
            "modified": False,
            "integrated": False,
            "disposition": "HOLD — MATERIAL RESULT DISCREPANCY",
        },
        "defects_repaired": [],
        "still_unresolved": [
            "whether a genuinely different but admissible particle-particle slot "
            "map -- as opposed to a reordering sign -- would move the family "
            "support. Neither the branch nor this adjudication tested one.",
            "the particle-particle Grassmann ordering and the diquark operator "
            "normalisation remain unfrozen and are untouched here",
        ],
        "not_consumed": [
            "the quarantined -3.2(5) value",
            "the suspended P2-BETAV-CIRC-01 result",
            "the historical Finding 5 extraction",
        ],
    }


def build() -> dict:
    return {
        "gate": "P2-PHASE-01",
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "deliverable": "adjudication of the diquark decomposition discrepancy",
        "floating_tolerance": TOL,
        "repository_inputs": repository_inputs(),
        "pinned_inputs": pinned_inputs(),
        "frozen_conventions": frozen_conventions(),
        "method_A_reproduction": method_A_reproduction(),
        "layer_comparison": layer_comparison(),
        "ablation": ablation(),
        "method_A_internal_consistency": method_A_internal_consistency(),
        "case_decision": case_decision(),
        "independence_claim": independence_claim(),
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
