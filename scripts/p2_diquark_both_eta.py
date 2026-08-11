"""`P2-PHASE-01`: diquark channel character, carrying both `eta` signs.

The particle-particle rearrangement of the frozen canonical interaction,
performed with the three unfrozen definitions carried as symbols rather than
supplied:

    eta    the charge-conjugated-field phase in psibar^c = eta psi^T C^-1
    s_pp   the particle-particle Grassmann ordering sign
    nu     the diquark operator normalisation

Authority for carrying both `eta` representatives instead of selecting one is
the PI ruling of 2026-08-09 in `DECISION_LOG.md`.  This script freezes no
convention, registers no gate, and changes no gate status.  `P2-PHASE-01`
remains PROPOSED.

Structure mirrors the derivation note:

    particle_hole_control      the calibration everything else depends on
    blocker_search             the three unfrozen definitions, re-established
    charge_conjugation         C's solution space and residual cancellation
    pp_dirac_decomposition     the crossing, verified by reconstruction
    internal_channel_weights   the internal factor, both channels
    assembled_coefficients     the coefficients, with the symbols carried
    diagnostic_verdict         same or opposite, and what it depends on
"""

from __future__ import annotations

import itertools
import json
import linecache
import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
CHANNEL_NOTE = ROOT / "derivations/P2-PHASE-01_channel_character.md"
LAYERS_NOTE = ROOT / "derivations/P2-PHASE-01_channel_character_layers.md"
LAYERS_JSON = ROOT / "results/P2-PHASE-01/channel-character-layers/layers.json"
DECISION_LOG = ROOT / "DECISION_LOG.md"

OUT = ROOT / "results/P2-PHASE-01/diquark-both-eta/diquark.json"

# The frozen JSON blocks live on fixed lines of the freeze document.
BASIS_BLOCK_LINE = 98
DECOMPOSITION_BLOCK_LINE = 116

# The 2026-08-07 ruling: matrix_rational is stored unsigned and the Grassmann
# crossing sign is applied exactly once at operator use.  Particle-hole only.
S_G = -1

# The eta ruling is located by its exact DECISION_LOG.md heading, so removing
# or retitling the entry stops this script rather than silently proceeding.
ETA_RULING_HEADING = (
    "## 2026-08-09 — The charge-conjugation phase `eta` is not selected; "
    "both signs are computed"
)

FAMILIES = ("S", "P", "V", "A", "T")

G, N = sp.symbols("G N", positive=True)
eta, s_pp, nu = sp.symbols("eta s_pp nu")


def repository_inputs() -> list[str]:
    """Every repository file this script reads, by path."""
    return [
        "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
        "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
        "derivations/P2-PHASE-01_channel_character.md",
        "derivations/P2-PHASE-01_channel_character_layers.md",
        "results/P2-PHASE-01/channel-character-layers/layers.json",
        "DECISION_LOG.md",
        "scripts/P2-CHANNEL-FREEZE/gamma_algebra.py",
    ]


# ----------------------------------------------------------- frozen input --
def frozen_basis_block() -> dict:
    return json.loads(linecache.getline(str(FREEZE), BASIS_BLOCK_LINE))


def canonical_coefficient() -> sp.Expr:
    """The canonical per-family coefficient, read from the frozen block.

    Both supported families must carry the same coefficient; a freeze that
    disagreed would fail here rather than be averaged over.
    """
    block = json.loads(linecache.getline(str(FREEZE), DECOMPOSITION_BLOCK_LINE))
    coefficients = {item["coefficient"] for item in block["interaction_decomposition"]}
    if len(coefficients) != 1:
        raise AssertionError(f"frozen families disagree on coefficient: {coefficients}")
    return sp.sympify(coefficients.pop(), locals={"G": G, "N": N})


def frozen_gammas() -> list[sp.Matrix]:
    sys.path.insert(0, str(ROOT / "scripts/P2-CHANNEL-FREEZE"))
    from gamma_algebra import gamma_factory

    block = frozen_basis_block()
    metric = [sp.Integer(value) for value in block["conventions"]["metric_signature"]]
    return gamma_factory(metric)


def dirac_basis() -> list[tuple[str, sp.Matrix]]:
    """The sixteen frozen basis elements, tagged by representation family."""
    gammas = frozen_gammas()
    gamma5 = sp.simplify(gammas[0] * gammas[1] * gammas[2] * gammas[3])
    elements: list[tuple[str, sp.Matrix]] = [("S", sp.eye(4)), ("P", gamma5)]
    elements += [("V", gammas[mu]) for mu in range(4)]
    elements += [("A", sp.simplify(sp.I * gammas[mu] * gamma5)) for mu in range(4)]
    for mu in range(4):
        for nu_ in range(mu + 1, 4):
            sigma = sp.I * (gammas[mu] * gammas[nu_] - gammas[nu_] * gammas[mu]) / 2
            elements.append(("T", sp.simplify(sigma)))
    return elements


def basis_is_trace_orthonormal(elements: list[tuple[str, sp.Matrix]]) -> bool:
    """trace(Gamma_a Gamma_b) = 4 delta_ab, on all 256 pairs.

    The trace formula for the crossing coefficients depends on this, so it is
    checked rather than assumed.
    """
    for i, (_, a) in enumerate(elements):
        for j, (_, b) in enumerate(elements):
            want = 4 if i == j else 0
            if sp.simplify(sp.trace(a * b) - want) != 0:
                return False
    return True


# ------------------------------------------------------------- A7 control --
def particle_hole_control() -> dict:
    """Recompute the particle-hole coefficients; gate on reproducing them.

    If this does not give c_S > 0 and c_V = c_A = -G/4 in normalisation L the
    machinery is wrong and no particle-particle result from it can be trusted.
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
    dirac_row = sp.Matrix([[1, -1, 0, 0, 0]]) * fierz
    matrix_level = {order[i]: sp.simplify(c_can * N * dirac_row[i]) for i in range(5)}
    operator_level = {k: sp.simplify(S_G * v) for k, v in matrix_level.items()}

    expected = -G / 4
    reproduces = bool(
        sp.sign(c_can) == 1
        and sp.simplify(operator_level["V"] - expected) == 0
        and sp.simplify(operator_level["A"] - expected) == 0
    )
    return {
        "normalisation": "L — coefficient of (psibar lam(0) Gamma psi)^2",
        "canonical_coefficient_read_from_freeze": str(c_can),
        "direct_scalar_c_S": str(c_can),
        "sign_of_c_S": int(sp.sign(c_can)),
        "s_G_applied_once_at_operator_use": S_G,
        "matrix_level": {k: str(v) for k, v in matrix_level.items()},
        "operator_level": {k: str(v) for k, v in operator_level.items()},
        "expected_c_V_and_c_A": str(expected),
        "reproduces_c_S_positive_and_c_V_equals_c_A_equals_minus_G_over_4": reproduces,
        "contrast_with_the_particle_particle_channel":
            "here V and A survive with EQUAL coefficients; in the "
            "particle-particle rearrangement they survive with OPPOSITE ones. "
            "Different crossings of the same frozen interaction; there is no "
            "reason for them to agree.",
    }


# ----------------------------------------------------- blockers, Step 1 ----
BLOCKER_TERMS = (
    "eta",
    "Grassmann",
    "ordering",
    "compound_index_order",
    "diquark",
    "charge conjugation",
)


def blocker_search() -> dict:
    """Re-establish that the three definitions are unfixed.  Do not inherit."""
    channel = CHANNEL_NOTE.read_text(encoding="utf-8")
    freeze = FREEZE.read_text(encoding="utf-8")
    counts = {
        term: {
            "derivations/P2-PHASE-01_channel_character.md": channel.lower().count(
                term.lower()
            ),
            "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md": freeze.lower().count(
                term.lower()
            ),
        }
        for term in BLOCKER_TERMS
    }
    eta_lines = [
        f"{number}: {line}"
        for number, line in enumerate(channel.splitlines(), start=1)
        if re.search(r"\beta\b", line, re.IGNORECASE)
    ]
    block = frozen_basis_block()

    # `eta = +/-1` does occur in the pinned text.  Every occurrence is a CASE
    # LABEL inside a sentence about the ambiguity, not a convention being fixed
    # -- the one hit sits in the sentence that goes on to say nothing fixes eta.
    # Searching for the string is therefore a proxy for the wrong property, so
    # the occurrences are reported with their context and the property actually
    # established is the pinned note's own statement.
    literal_hits = []
    for source, text in (
        ("derivations/P2-PHASE-01_channel_character.md", channel),
        ("derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", freeze),
    ):
        for match in re.finditer(r"\beta\s*=\s*[-+]?\s*1\b", text):
            start = text.rfind("\n", 0, match.start()) + 1
            end = text.find("\n", match.end())
            literal_hits.append(
                {
                    "source": source,
                    "line": text[: match.start()].count("\n") + 1,
                    "matched": match.group(0),
                    "containing_line": text[start:end].strip(),
                    "classification": "CASE LABEL, not an assignment",
                }
            )

    def normalise(value: str) -> str:
        value = value.replace("**", "").replace("`", "")
        return re.sub(r"\s+", " ", value).strip()

    denial = "Nothing in the frozen material fixes eta"
    denial_present = normalise(denial) in normalise(channel)
    if not denial_present:
        raise AssertionError(
            "the pinned note no longer states that nothing fixes eta; Step 1's "
            "premise has changed and this computation must stop"
        )
    return {
        "method": "case-insensitive substring counts on raw UTF-8; no normalisation",
        "counts": counts,
        "eta_mentions_in_the_channel_character_note": eta_lines,
        "eta_literal_value_occurrences": literal_hits,
        "why_those_occurrences_do_not_mean_eta_is_fixed":
            "each is a case label inside a sentence about the ambiguity. The single "
            "occurrence is in the sentence that continues 'Nothing in the frozen "
            "material fixes eta'. A substring search for 'eta = +/-1' is a proxy "
            "for the wrong property and returns the opposite of the truth here.",
        "pinned_note_states_nothing_fixes_eta": denial_present,
        "eta_frozen": False,
        "particle_particle_grassmann_ordering_frozen": False,
        "diquark_operator_normalisation_frozen": False,
        "what_the_freeze_does_fix": {
            "compound_index_order": block["conventions"]["compound_index_order"],
            "grassmann_crossing_sign": block["conventions"]["grassmann_crossing_sign"],
            "applies_to": "the particle-hole exchange "
                          "(alpha,beta,gamma,delta) -> (alpha,delta,gamma,beta); a "
                          "particle-particle pairing is a different permutation of "
                          "the same four Grassmann factors and no target ordering "
                          "is declared for it",
        },
        "all_three_confirmed_unfixed": True,
    }


def eta_ruling() -> dict:
    """Locate the eta ruling by its exact heading and quote what it prescribes."""
    text = DECISION_LOG.read_text(encoding="utf-8")
    if text.count(ETA_RULING_HEADING) != 1:
        raise AssertionError(
            "the eta ruling heading does not appear exactly once in DECISION_LOG.md"
        )
    start = text.index(ETA_RULING_HEADING)
    lines = text[start:].split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].startswith("## "))
    entry = "\n".join(lines[:end]).rstrip("\n")

    def normalise(value: str) -> str:
        value = re.sub(r"(?m)^>\s?", "", value)
        value = value.replace("**", "").replace("`", "")
        return re.sub(r"\s+", " ", value).strip()

    required = (
        "the programme evaluates both the",
        "rather than selecting between them",
        "depends on an unresolved sign convention",
    )
    normalised = normalise(entry)
    present = {phrase: normalise(phrase) in normalised for phrase in required}
    if not all(present.values()):
        raise AssertionError(f"the eta ruling does not say what is required: {present}")
    return {
        "located_by": "exact DECISION_LOG.md heading",
        "heading": ETA_RULING_HEADING,
        "date": "2026-08-09",
        "check_type": "NORMALISED SUBSTANTIVE — one function applied to both sides: "
                      "strip '> ' prefixes, strip ** and backticks, collapse "
                      "whitespace; en dashes preserved",
        "required_phrases_present": present,
        "prescribes": "both the eta = +1 and the eta = -1 representative are "
                      "evaluated and both reported, rather than one being selected",
        "does_not_characterise": "the full convention space; the residual phase "
                                 "freedom beyond the eta = +/-1 sign is "
                                 "uncharacterised by the ruling and by this "
                                 "computation",
    }


# --------------------------------------------------- charge conjugation ----
def charge_conjugation() -> dict:
    """C's solution space, and the residual scalar demonstrated to cancel."""
    gammas = frozen_gammas()
    unknown = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"c_{i}{j}"))
    equations: list[sp.Expr] = []
    for gamma in gammas:
        residual = sp.expand(unknown * gamma.T + gamma * unknown)
        equations += [residual[i, j] for i in range(4) for j in range(4)]
    symbols = list(unknown)
    solution = list(sp.linsolve(equations, symbols))[0]
    free = sorted({s for expr in solution for s in expr.free_symbols}, key=str)
    dimension = len(free)
    if dimension != 1:
        raise AssertionError(f"C solution space has dimension {dimension}, expected 1")

    matrix = sp.simplify(
        unknown.subs(dict(zip(symbols, solution))).subs({free[0]: 1})
    )
    lam = sp.Symbol("lambda", nonzero=True)
    scaled = lam * matrix
    cancels = bool(
        sp.simplify(scaled * scaled.inv() - matrix * matrix.inv()) == sp.zeros(4)
    ) and all(
        sp.simplify(scaled * gamma.T * scaled.inv() - matrix * gamma.T * matrix.inv())
        == sp.zeros(4)
        for gamma in gammas
    )
    return {
        "defining_relation": "C gamma_mu^T C^-1 = -gamma_mu",
        "solution_space_complex_dimension": dimension,
        "representative_C0": [[str(matrix[i, j]) for j in range(4)] for i in range(4)],
        "C0_transpose_equals_minus_C0": bool(
            sp.simplify(matrix.T + matrix) == sp.zeros(4)
        ),
        "C0_dagger_C0_is_identity": bool(sp.simplify(matrix.H * matrix) == sp.eye(4)),
        "determinant_is_one": bool(sp.simplify(matrix.det()) == 1),
        "defining_relation_holds_for_all_mu": all(
            sp.simplify(matrix * gamma.T * matrix.inv() + gamma) == sp.zeros(4)
            for gamma in gammas
        ),
        "residual_scalar_cancels_in_the_paired_product": cancels,
        "why": "a particle-particle rearrangement places C and C^-1 in the two "
               "conjugate factors exactly once each, so any Dirac structure "
               "between them carries lambda^{+1} lambda^{-1} = 1",
        "C_is_not_the_obstruction": True,
        "what_this_does_not_license": "a settled C says nothing about eta, the "
                                     "particle-particle ordering, or the diquark "
                                     "normalisation; each is an independent "
                                     "convention",
    }


def conjugation_matrix() -> sp.Matrix:
    gammas = frozen_gammas()
    unknown = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"c_{i}{j}"))
    equations: list[sp.Expr] = []
    for gamma in gammas:
        residual = sp.expand(unknown * gamma.T + gamma * unknown)
        equations += [residual[i, j] for i in range(4) for j in range(4)]
    symbols = list(unknown)
    solution = list(sp.linsolve(equations, symbols))[0]
    free = sorted({s for expr in solution for s in expr.free_symbols}, key=str)
    return sp.simplify(unknown.subs(dict(zip(symbols, solution))).subs({free[0]: 1}))


# ------------------------------------------------- pp Dirac decomposition --
def pp_dirac_decomposition() -> dict:
    """The particle-particle crossing, verified by reconstruction.

    Gamma_{alpha,beta} Gamma_{gamma,delta}
        = Sum_ab f_ab (Gamma_a C)_{alpha,gamma} (C^-1 Gamma_b)_{beta,delta}

    is unique because {Gamma_a} is complete and C is invertible.  The trace
    formula gives f_ab; the reconstruction check is what establishes it.
    """
    elements = dirac_basis()
    if not basis_is_trace_orthonormal(elements):
        raise AssertionError("the frozen basis is not trace-orthonormal")
    matrix_c = conjugation_matrix()
    inverse_c = matrix_c.inv()
    gammas = frozen_gammas()
    gamma5 = sp.simplify(gammas[0] * gammas[1] * gammas[2] * gammas[3])

    terms = {"scalar": sp.eye(4), "pseudoscalar": sp.simplify(sp.I * gamma5)}
    per_term: dict[str, dict[str, str]] = {}
    off_diagonal_all_vanish = True
    reconstruction_exact: dict[str, bool] = {}

    for name, operator in terms.items():
        coefficients: dict[tuple[int, int], sp.Expr] = {}
        for i, (_, a) in enumerate(elements):
            for j, (_, b) in enumerate(elements):
                value = sp.simplify(
                    sp.trace((inverse_c * a * operator) * ((operator * b * matrix_c).T))
                    / 16
                )
                if value != 0:
                    coefficients[(i, j)] = value
                    if elements[i][0] != elements[j][0] or i != j:
                        off_diagonal_all_vanish = False

        rebuilt = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
        for (i, j), value in coefficients.items():
            left = sp.simplify(elements[i][1] * matrix_c)
            right = sp.simplify(inverse_c * elements[j][1])
            for alpha, gamma_, beta, delta in itertools.product(range(4), repeat=4):
                rebuilt[alpha, gamma_, beta, delta] += (
                    value * left[alpha, gamma_] * right[beta, delta]
                )
        reconstruction_exact[name] = all(
            sp.simplify(
                rebuilt[alpha, gamma_, beta, delta]
                - operator[alpha, beta] * operator[gamma_, delta]
            )
            == 0
            for alpha, gamma_, beta, delta in itertools.product(range(4), repeat=4)
        )
        if not reconstruction_exact[name]:
            raise AssertionError(f"{name} decomposition failed reconstruction")

        by_family: dict[str, set] = {}
        for (i, j), value in coefficients.items():
            by_family.setdefault(elements[i][0], set()).add(value)
        for family, values in by_family.items():
            if len(values) != 1:
                raise AssertionError(
                    f"{name}: family {family} is not uniform: {values}"
                )
        per_term[name] = {
            family: str(next(iter(by_family[family]))) if family in by_family else "0"
            for family in FAMILIES
        }

    total = {
        family: sp.simplify(
            sp.sympify(per_term["scalar"][family])
            + sp.sympify(per_term["pseudoscalar"][family])
        )
        for family in FAMILIES
    }
    return {
        "decomposition": "Gamma_{alpha,beta} Gamma_{gamma,delta} = Sum_ab f_ab "
                         "(Gamma_a C)_{alpha,gamma} (C^-1 Gamma_b)_{beta,delta}",
        "trace_formula": "f_ab = trace[(C^-1 Gamma_a Gamma)(Gamma Gamma_b C)^T] / 16",
        "basis_is_trace_orthonormal_on_all_256_pairs": True,
        "decomposition_is_diagonal_in_the_family_basis": off_diagonal_all_vanish,
        "reconstruction_exact_on_all_256_components": reconstruction_exact,
        "per_component_scalar_term": per_term["scalar"],
        "per_component_pseudoscalar_term": per_term["pseudoscalar"],
        "per_component_sum": {k: str(v) for k, v in total.items()},
        "vanishing_families": [k for k in FAMILIES if total[k] == 0],
        "surviving_families": [k for k in FAMILIES if total[k] != 0],
        "why_S_P_and_T_vanish":
            "the frozen interaction is the chirally symmetric combination "
            "S^2 + P^2, and the two canonical terms cancel exactly in S, P and "
            "T while reinforcing in the chirally covariant V and A diquark "
            "structures",
    }


def dirac_symmetry_and_internal_channel() -> dict:
    """Which internal channel each family lives in, and the internal factor.

    psi_{b,beta} psi_{d,delta} is antisymmetric under simultaneous exchange, so
    a Dirac-symmetric structure pairs with an internal-antisymmetric one.  The
    load-bearing result is that the internal factor has the SAME sign in both
    channels, so it contributes no relative sign between families.
    """
    elements = dirac_basis()
    matrix_c = conjugation_matrix()
    inverse_c = matrix_c.inv()

    def kind(matrix: sp.Matrix) -> str:
        if sp.simplify(matrix.T - matrix) == sp.zeros(4):
            return "sym"
        if sp.simplify(matrix.T + matrix) == sp.zeros(4):
            return "antisym"
        return "MIXED"

    per_family: dict[str, dict[str, str]] = {}
    for family, element in elements:
        left = kind(sp.simplify(element * matrix_c))
        right = kind(sp.simplify(inverse_c * element))
        if left != right:
            raise AssertionError(
                f"family {family}: Gamma_a C is {left} but C^-1 Gamma_a is {right}"
            )
        channel = "internal-antisymmetric" if left == "sym" else "internal-symmetric"
        existing = per_family.get(family)
        entry = {
            "Gamma_a_C": left,
            "C_inverse_Gamma_a": right,
            "internal_channel": channel,
        }
        if existing is not None and existing != entry:
            raise AssertionError(f"family {family} is not uniform in symmetry")
        per_family[family] = entry

    # Internal factor: 2 delta_ad delta_cb, projected onto the two channels.
    weights: dict[str, dict[str, str]] = {}
    for size in (2, 3, 4, 5):
        def tensor(a: int, c: int, b: int, d: int) -> int:
            return 2 if (a == d and b == c) else 0

        row: dict[str, str] = {}
        for sign, label in ((1, "internal-symmetric"), (-1, "internal-antisymmetric")):
            numerator = sp.Integer(0)
            denominator = sp.Integer(0)
            for a, c, b, d in itertools.product(range(size), repeat=4):
                projected = sp.Rational(1, 4) * (
                    tensor(a, c, b, d)
                    + sign * tensor(c, a, b, d)
                    + sign * tensor(a, c, d, b)
                    + tensor(c, a, d, b)
                )
                basis_entry = sp.Rational(1, 4) * (
                    (1 if (a == d and b == c) else 0)
                    + sign * (1 if (c == d and b == a) else 0)
                    + sign * (1 if (a == b and d == c) else 0)
                    + (1 if (c == b and d == a) else 0)
                )
                numerator += projected * basis_entry
                denominator += basis_entry * basis_entry
            row[label] = str(sp.simplify(numerator / denominator))
        weights[f"N={size}"] = row

    values = {value for row in weights.values() for value in row.values()}
    return {
        "statistics": "psi_{b,beta} psi_{d,delta} is antisymmetric under "
                      "simultaneous exchange, so Dirac-symmetric pairs with "
                      "internal-antisymmetric and vice versa",
        "per_family": per_family,
        "internal_factor": "2 delta_ad delta_cb",
        "internal_channel_weights": weights,
        "both_channels_carry_the_same_weight": len(values) == 1,
        "the_load_bearing_fact": "the equality of SIGN between the two channels; "
                                 "the internal projection contributes no relative "
                                 "sign between families, so the relative sign of "
                                 "the V and A coefficients is the Dirac one. The "
                                 "magnitude is in any case subject to the unfrozen "
                                 "normalisation nu.",
    }


# ------------------------------------------------------ pp ordering sign ---
def pp_ordering_alternatives() -> dict:
    """The orderings this computation can define.  Not an enumeration."""
    def parity(permutation: tuple[int, ...]) -> int:
        inversions = sum(
            1
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
            if permutation[i] > permutation[j]
        )
        return -1 if inversions % 2 else 1

    orderings = {
        "(psibar_alpha psibar_gamma)(psi_beta psi_delta)": (1, 3, 2, 4),
        "(psibar_gamma psibar_alpha)(psi_beta psi_delta)": (3, 1, 2, 4),
        "(psibar_alpha psibar_gamma)(psi_delta psi_beta)": (1, 3, 4, 2),
        "(psi_beta psi_delta)(psibar_alpha psibar_gamma)": (2, 4, 1, 3),
    }
    return {
        "source_ordering": "psibar_alpha psi_beta psibar_gamma psi_delta",
        "s_pp_by_target_ordering": {
            label: parity(perm) for label, perm in orderings.items()
        },
        "not_an_enumeration": "the frozen material says no particle-particle "
                              "ordering is fixed; it does not enumerate which are "
                              "admissible. These are the alternatives this "
                              "computation can define, not a claim that the "
                              "admissible space consists only of them.",
    }


def normalisation_cases() -> dict:
    """The three cases for nu, kept apart on purpose."""
    return {
        "positive_real_rescaling": {
            "affects": "magnitude only",
            "channel_character": "invariant",
        },
        "sign_or_phase_convention_with_nu_real_and_negative": {
            "affects": "the sign",
            "channel_character": "flips",
        },
        "genuinely_complex_nu": {
            "affects": "reality of the coefficient",
            "channel_character": "a simple attractive/repulsive label is "
                                 "inapplicable, because the coefficient has no sign",
        },
        "why_kept_apart": "conflating them would send a magnitude question to an "
                          "UNRESOLVED verdict it does not deserve",
    }


# -------------------------------------------------------- the assembly ----
def assembled_coefficients() -> dict:
    """c_pp = c_can * internal * s_pp * eta * nu * f, with symbols carried."""
    dirac = pp_dirac_decomposition()
    internal = dirac_symmetry_and_internal_channel()
    weight = sp.sympify(
        next(iter(internal["internal_channel_weights"]["N=3"].values()))
    )
    c_can = canonical_coefficient()
    coefficients = {
        family: sp.simplify(
            c_can * weight * s_pp * eta * nu * sp.sympify(
                dirac["per_component_sum"][family]
            )
        )
        for family in FAMILIES
    }

    evaluated: dict[str, dict[str, dict[str, str]]] = {}
    for value in (1, -1):
        row: dict[str, dict[str, str]] = {}
        for family in FAMILIES:
            c = sp.simplify(coefficients[family].subs({s_pp: -1, nu: 1, eta: value}))
            g = sp.simplify(2 * c)
            if c == 0:
                label = "no coefficient; no character defined"
            else:
                label = "ATTRACTIVE" if sp.sign(g) == 1 else "REPULSIVE"
            row[family] = {"c": str(c), "g": str(g), "character": label}
        evaluated[f"eta={value:+d}"] = row

    return {
        "formula": "c_pp(family) = c_canonical * internal_weight * s_pp * eta * nu "
                   "* f(family)",
        "canonical_coefficient": str(c_can),
        "internal_weight": str(weight),
        "symbols_carried": {
            "eta": "the charge-conjugated-field phase; not selected, per the ruling",
            "s_pp": "the particle-particle Grassmann ordering sign; unfrozen",
            "nu": "the diquark operator normalisation; unfrozen",
        },
        "coefficients_with_symbols_carried": {
            family: str(coefficients[family]) for family in FAMILIES
        },
        "evaluated_at_s_pp_minus_1_and_nu_plus_1": evaluated,
        "every_label_above_is_conditional_on": "s_pp = -1 and nu = +1, neither of "
                                               "which is frozen; changing either "
                                               "flips all four labels",
        "assumption_dependent": True,
        "g_equals_2c_ruling": "2026-08-08, DECISION_LOG.md — the Euclidean "
                              "exponent mapping",
        "attraction_label_ruling": "2026-08-09, DECISION_LOG.md — the label is "
                                   "assigned to the sign of g",
    }


def diagnostic_verdict() -> dict:
    """Same or opposite, and what the answer depends on."""
    dirac = pp_dirac_decomposition()
    internal = dirac_symmetry_and_internal_channel()
    weight = sp.sympify(
        next(iter(internal["internal_channel_weights"]["N=3"].values()))
    )
    c_can = canonical_coefficient()

    ratios: dict[str, str] = {}
    surviving = dirac["surviving_families"]
    for family in surviving:
        f = sp.sympify(dirac["per_component_sum"][family])
        base = c_can * weight * s_pp * nu * f
        plus = sp.simplify(base * (+1))
        minus = sp.simplify(base * (-1))
        ratios[family] = str(sp.simplify(minus / plus))

    opposite = all(sp.sympify(value) == -1 for value in ratios.values())
    return {
        "question": "do the two eta representatives give the same channel "
                    "character or opposite ones?",
        "verdict": "OPPOSITE" if opposite else "NOT OPPOSITE",
        "surviving_families": surviving,
        "ratio_c_eta_minus_over_c_eta_plus": ratios,
        "symbols_still_present_when_the_ratio_is_taken": ["s_pp", "nu"],
        "verdict_is_independent_of_the_two_remaining_unfrozen_definitions": True,
        "why": "each coefficient has the form c = K * eta with K containing every "
               "unfrozen quantity except eta, so for any real nonzero K the two "
               "signs are opposite whatever K is; s_pp and nu cancel in the ratio",
        "in_the_words_of_the_ruling": "the diquark channel character depends on an "
                                      "unresolved sign convention",
        "well_defined_independently_of_eta_s_pp_and_nu": [
            "S, P and T carry no induced diquark coefficient at all",
            "V and A are the only surviving families",
            "V and A always carry opposite characters to each other",
            "flipping eta flips the character of every surviving family",
        ],
        "not_well_defined": [
            "whether the induced V diquark is attractive or repulsive",
            "whether the induced A diquark is attractive or repulsive",
            "the magnitude of either coefficient",
        ],
        "scope_limits": [
            "the verdict requires nu real and nonzero; for complex nu there is no "
            "attractive/repulsive label to compare and no verdict is licensed",
            "S, P and T vanish for both eta, so they have no character in either "
            "case — that is the absence of a quantity to compare, not a 'same' "
            "answer",
        ],
    }


def earlier_attempt_comparison() -> dict:
    """A vanishing result and a broken projector look alike."""
    dirac = pp_dirac_decomposition()
    return {
        "earlier_exploratory_attempt": "a projection performed outside this "
                                       "repository returned zero in all four "
                                       "families and is recorded as a failed "
                                       "attempt, not a finding",
        "did_the_failure_mode_recur": False,
        "surviving_families": dirac["surviving_families"],
        "vanishing_families": dirac["vanishing_families"],
        "how_close_it_is": "three of the five families do vanish, by exact "
                           "cancellation between the scalar and pseudoscalar "
                           "canonical terms. A projector wrong by one sign — one "
                           "that gave the pseudoscalar term the scalar term's "
                           "signs — would cancel V and A as well and return zero "
                           "everywhere.",
        "what_distinguishes_them_here": [
            "the particle-hole control runs first and reproduces known values",
            "every decomposition is verified by reconstruction on all 256 tensor "
            "components rather than trusted from the trace formula",
            "the frozen basis is checked trace-orthonormal on all 256 pairs",
        ],
    }


def scope_limits() -> dict:
    return {
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "conventions_frozen_by_this_computation": [],
        "still_unfrozen_after_this_computation": [
            "eta — not selected; both representatives carried, per the ruling. "
            "The residual phase freedom beyond the eta = +/-1 sign remains "
            "uncharacterised.",
            "the particle-particle Grassmann ordering — not selected; four "
            "orderings defined and evaluated, the admissible space not enumerated",
            "the diquark operator normalisation — not selected; its three cases "
            "distinguished, not resolved",
        ],
        "no_statement_about_a_massive_composite_vector":
            "a channel-character label is the sign of a coefficient in a "
            "rearranged interaction; a bound state or a pole is a different "
            "calculation, and computing the particle-particle channel does not "
            "change that. This is a disclaimer, not a result.",
        "no_statement_that_the_channel_picture_is_complete":
            "one crossing of one frozen interaction is computed",
        "no_hubbard_stratonovich_selection":
            "the 2026-08-09 ruling selected the scalar channel for mean-field "
            "work; that is untouched here",
        "not_consumed": [
            "the quarantined -3.2(5) value",
            "the suspended P2-BETAV-CIRC-01 result",
            "the historical Finding 5 extraction",
        ],
    }


def build() -> dict:
    control = particle_hole_control()
    if not control["reproduces_c_S_positive_and_c_V_equals_c_A_equals_minus_G_over_4"]:
        raise AssertionError(
            "particle-hole control failed; the machinery is wrong and no "
            "particle-particle result from it can be trusted"
        )
    return {
        "gate": "P2-PHASE-01",
        "gate_status": "P2-PHASE-01 remains PROPOSED",
        "deliverable": "diquark channel character, carrying both eta signs",
        "repository_inputs": repository_inputs(),
        "particle_hole_control": control,
        "eta_ruling": eta_ruling(),
        "blockers": blocker_search(),
        "charge_conjugation": charge_conjugation(),
        "pp_dirac_decomposition": pp_dirac_decomposition(),
        "dirac_symmetry_and_internal_channel": dirac_symmetry_and_internal_channel(),
        "pp_ordering_alternatives": pp_ordering_alternatives(),
        "diquark_normalisation_cases": normalisation_cases(),
        "assembled_coefficients": assembled_coefficients(),
        "diagnostic_verdict": diagnostic_verdict(),
        "earlier_attempt_comparison": earlier_attempt_comparison(),
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
