"""Normalisation audit: reconcile Paper 3's `G_omega` with the derived coefficient.

Produces one row of the evidence table `derivations/CANONICAL_INTERACTION.md`
§5 requires for its own ratification: the *normalizations match* row.

It ratifies nothing, removes no banner, and modifies no Paper-3 content.  The
vector singlet coefficient is RECOMPUTED here from the frozen canonical
interaction and the frozen Fierz matrix; the unmerged channel-character branch
is consulted only afterwards, and only to quote the normalisation it declares
and to compare values.

The Paper-3 side is read from a read-only clone of the pinned external
revision.  Quotations are quotations: no Paper-3 file is copied into this
repository, and the clone lives outside it.
"""

from __future__ import annotations

import hashlib
import json
import linecache
import subprocess
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
FIERZ_JSON = ROOT / "results/P2-CHANNEL-FREEZE/fierz_matrix.json"
CANONICAL = ROOT / "derivations/CANONICAL_INTERACTION.md"
SIGN_ADDENDUM = ROOT / "derivations/P2-PHASE-01_fierz_sign_addendum.md"

OUT = ROOT / "results/P2-PHASE-01/normalisation-audit/g_omega_audit.json"

BASIS_BLOCK_LINE = 98
DECOMPOSITION_BLOCK_LINE = 116

# The 2026-08-07 ruling: matrix_rational is stored unsigned; s_G once at use.
S_G = -1

# External evidence base, read-only.
PAPER3_REPO = Path("/workspace/zetacheng/3-vector-sector")
PAPER3_REVISION = "8c363ef08368f5c022278ea5f36e01496be3d5ca"
PAPER3_NOTE = "derivations/u3-fierz/u3_fierz.md"
PAPER3_NOTE_SHA256 = (
    "6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49"
)

# The unmerged branch, consulted only for its declared normalisation.
CHANNEL_CHARACTER_COMMIT = "cb604a4e3a96f9120787a685120f205d8e4c7c88"
CHANNEL_CHARACTER_PATH = (
    "results/P2-PHASE-01/channel-character/channel_character.json"
)

G, N = sp.symbols("G N", positive=True)


# ------------------------------------------------------------ inputs ------
def repository_inputs() -> dict[str, list[str]]:
    """Every repository file read, by path, across both repositories."""
    return {
        "2-emergent-gravity": [
            "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md",
            "results/P2-CHANNEL-FREEZE/fierz_matrix.json",
            "derivations/CANONICAL_INTERACTION.md",
            "derivations/P2-PHASE-01_fierz_sign_addendum.md",
            "results/P2-PHASE-01/channel-character/channel_character.json"
            "  [read from the unmerged branch object, not the base tree]",
        ],
        "3-vector-sector (read-only, external pin)": [
            "derivations/u3-fierz/u3_fierz.md",
        ],
    }


def _paper3_note_lines() -> list[str]:
    """Read the pinned Paper-3 note from the object store.  Read-only."""
    blob = subprocess.run(
        ["git", "-C", str(PAPER3_REPO), "cat-file", "blob",
         f"{PAPER3_REVISION}:{PAPER3_NOTE}"],
        capture_output=True, check=True,
    ).stdout
    digest = hashlib.sha256(blob).hexdigest()
    if digest != PAPER3_NOTE_SHA256:
        raise AssertionError(
            f"external pin mismatch: {digest} != {PAPER3_NOTE_SHA256}"
        )
    return blob.decode("utf-8").splitlines()


def paper3_normalisation() -> dict:
    """Quote the definition under which Paper 3 states G_omega."""
    lines = _paper3_note_lines()

    def quote(number: int) -> str:
        return lines[number - 1]

    convention_line = 10
    assembly_lines = (185, 190)
    quoted_assembly = [quote(n) for n in range(*assembly_lines)] + [
        quote(assembly_lines[1])
    ]
    if "L_V = (G_V/2) J_mu J^mu" not in quote(convention_line):
        raise AssertionError("Paper 3 convention line moved; re-locate it")
    if "G_omega = -G/N" not in quote(190):
        raise AssertionError("Paper 3 G_omega line moved; re-locate it")
    return {
        "source_repository": "zetacheng/3-vector-sector",
        "pinned_revision": PAPER3_REVISION,
        "source_path": PAPER3_NOTE,
        "source_sha256": PAPER3_NOTE_SHA256,
        "convention_line_number": convention_line,
        "convention_quoted": quote(convention_line),
        "classification_line_number": 11,
        "classification_quoted": quote(11),
        "assembly_line_numbers": list(range(185, 191)),
        "assembly_quoted": quoted_assembly,
        "coefficient_of_J_dot_J_as_written": "-(G/2N)",
        "G_omega_as_written": "-G/N",
        "carries_a_factor_of_one_half": True,
        "half_factor_origin": "L_V = (G_V/2) J_mu J^mu, the reported coupling "
                              "is twice the operator coefficient",
    }


def this_repository_normalisation() -> dict:
    """Quote the normalisation the channel-character artifact declares.

    Read from the unmerged branch object.  Only the DECLARATION is used
    here; the value is recomputed independently below.
    """
    blob = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "blob",
         f"{CHANNEL_CHARACTER_COMMIT}:{CHANNEL_CHARACTER_PATH}"],
        capture_output=True, check=True,
    ).stdout
    payload = json.loads(blob)
    layer = payload["layer_1a"]
    return {
        "source_path": CHANNEL_CHARACTER_PATH,
        "source_commit": CHANNEL_CHARACTER_COMMIT,
        "source_status": "UNMERGED BRANCH gate/p2-channel-character; absent "
                         "from the evidence base; quoted for its declaration "
                         "only, not consumed as an input",
        "normalisation_L_definition": layer["normalisation_L_definition"],
        "normalisation_P_definition": layer["normalisation_P_definition"],
        "normalisation_relation": layer["normalisation_relation"],
        "reported_induced_V_singlet": layer["channels"]["induced_V_singlet"],
        "carries_a_factor_of_one_half": False,
        "note": "Neither declared normalisation carries a factor of one half; "
                "both are plain coefficients of a squared bilinear. G_omega is "
                "a third quantity, defined by Paper 3's (G_V/2) convention.",
    }


# ------------------------------------------------- independent recompute --
def recompute_vector_singlet() -> dict:
    """Recompute from the frozen material.  Not transcribed."""
    block = json.loads(linecache.getline(str(FREEZE), BASIS_BLOCK_LINE))
    order = block["basis_order"]
    fierz = sp.Matrix(
        [[sp.Rational(entry) for entry in row] for row in block["matrix_rational"]]
    )
    standalone = json.loads(FIERZ_JSON.read_text(encoding="utf-8"))
    if standalone["matrix_rational"] != block["matrix_rational"]:
        raise AssertionError("standalone Fierz artifact disagrees with the freeze")

    decomposition = json.loads(
        linecache.getline(str(FREEZE), DECOMPOSITION_BLOCK_LINE)
    )["interaction_decomposition"]
    coefficients = {item["coefficient"] for item in decomposition}
    if len(coefficients) != 1:
        raise AssertionError(f"frozen families disagree: {coefficients}")
    c_can = sp.sympify(coefficients.pop(), locals={"G": G, "N": N})

    v_frozen = sp.Matrix([[c_can, -c_can, 0, 0, 0]])
    dirac_row = (v_frozen / c_can) * fierz
    index_v = order.index("V")
    c_dirac = dirac_row[index_v]

    # inside the Fierzed bracket, before the (G/2N) prefactor
    c_bracket = sp.simplify(S_G * c_dirac * N)
    c_l = sp.simplify(c_can * c_bracket)
    c_j = sp.simplify(c_l * sp.Integer(2) / N)
    g_omega = sp.simplify(2 * c_j)

    return {
        "method": "recomputed from the frozen interaction_decomposition and "
                  "the frozen matrix_rational; the unmerged branch's value was "
                  "not read before this computation",
        "canonical_per_family_coefficient": str(c_can),
        "dirac_row_after_frozen_matrix": [str(x) for x in dirac_row],
        "c_V_dirac": str(c_dirac),
        "s_G_applied_once_at_operator_use": S_G,
        "c_V_bracket_general_N": str(c_bracket),
        "c_V_bracket_at_N_3": str(sp.simplify(c_bracket.subs(N, 3))),
        "c_L_coefficient_of_lam0_bilinear_squared": str(c_l),
        "c_J_coefficient_of_J_dot_J": str(c_j),
        "G_omega_equals_twice_c_J": str(g_omega),
    }


def conversion() -> dict:
    """The conversion, symbolically, with its factor and origin."""
    c_j = sp.Symbol("c_J")
    return {
        "paper3_convention": "L_V = (G_V/2) J_mu J^mu",
        "relation": "G_omega = 2 * c_J",
        "conversion_factor": 2,
        "factor_origin": "the explicit 1/2 in L_V = (G_V/2) J_mu J^mu at line "
                         "10 of the Paper-3 note; a definitional prefactor on "
                         "the reported coupling, not an algebraic step",
        "symbolic_check": str(sp.simplify(2 * c_j)),
        "secondary_conversion": {
            "relation": "c_J = (2/N) * c_L",
            "origin": "the frozen lam(0) = sqrt(2/N) Id_N; Paper 3 performs "
                      "the same step at its Level 3, writing sqrt(2/3) for N=3",
        },
    }


def verdict(recomputed: dict, paper3: dict) -> dict:
    """One of the three named verdicts, selected by the evidence."""
    c_j = sp.sympify(recomputed["c_J_coefficient_of_J_dot_J"],
                     locals={"G": G, "N": N})
    paper3_c_j = sp.sympify("-(G/(2*N))", locals={"G": G, "N": N})
    paper3_g_omega = sp.sympify("-G/N", locals={"G": G, "N": N})
    coefficients_agree = bool(sp.simplify(c_j - paper3_c_j) == 0)
    mapping_agrees = bool(sp.simplify(2 * c_j - paper3_g_omega) == 0)
    both_stated = bool(
        paper3["carries_a_factor_of_one_half"] is True
        and "L_V = (G_V/2)" in paper3["convention_quoted"]
    )
    if coefficients_agree and mapping_agrees and both_stated:
        chosen = "NORMALISATION MAPPING"
    elif both_stated and not coefficients_agree:
        chosen = "REPOSITORY_DEFECT"
    else:
        chosen = "UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY"
    return {
        "verdict": chosen,
        "same_operator_same_normalisation_agree": coefficients_agree,
        "mapping_reproduces_G_omega": mapping_agrees,
        "both_normalisations_stated_precisely": both_stated,
        "recomputed_c_J": str(c_j),
        "paper3_c_J_as_written": str(paper3_c_j),
        "paper3_G_omega_as_written": str(paper3_g_omega),
        "decisive_evidence":
            "Line 189 of the Paper-3 note writes the coefficient of J_mu J^mu "
            "explicitly as -(G/2N) BEFORE converting it to G_omega. That is "
            "the same number this repository derives, in the same operator "
            "normalisation, on the same page. The two documents never "
            "disagreed about a coefficient, only about which quantity they "
            "name.",
        "neither_value_adjusted": True,
    }


def comparison_with_channel_character(recomputed: dict, declared: dict) -> dict:
    """Compare AFTER computing, per the authority's ordering."""
    reported = declared["reported_induced_V_singlet"]
    c_l_theirs = sp.sympify(reported["normalisation_L"], locals={"G": G, "N": N})
    c_j_theirs = sp.sympify(reported["normalisation_P"], locals={"G": G, "N": N})
    c_l_mine = sp.sympify(recomputed["c_L_coefficient_of_lam0_bilinear_squared"],
                          locals={"G": G, "N": N})
    c_j_mine = sp.sympify(recomputed["c_J_coefficient_of_J_dot_J"],
                          locals={"G": G, "N": N})
    agree = bool(
        sp.simplify(c_l_theirs - c_l_mine) == 0
        and sp.simplify(c_j_theirs - c_j_mine) == 0
    )
    return {
        "channel_character_c_L": str(c_l_theirs),
        "recomputed_c_L": str(c_l_mine),
        "channel_character_c_J": str(c_j_theirs),
        "recomputed_c_J": str(c_j_mine),
        "agree": agree,
        "status": "CORROBORATION" if agree else "DISAGREEMENT — a finding "
                                                "about the channel-character "
                                                "result and a STOP",
        "independence_caveat":
            "Both computations run the same chain over the same frozen "
            "material and were authored in the same session. This corroborates "
            "the CHAIN, not the judgement behind it. The genuinely independent "
            "check is Paper 3, which re-derives its Fierz table from 16-dim "
            "completeness at N=3 by a different route and reproduces every "
            "intermediate quantity.",
    }


def paper3_intermediate_agreement(recomputed: dict) -> dict:
    """Paper 3's intermediates, level by level — stronger than the endpoint."""
    rows = [
        ("c_V_dirac", "+1/2", recomputed["c_V_dirac"]),
        ("c_V_bracket_at_N_3", "-3/2", recomputed["c_V_bracket_at_N_3"]),
        ("coefficient_of_lam0_bilinear_squared", "-G/4",
         recomputed["c_L_coefficient_of_lam0_bilinear_squared"]),
        ("coefficient_of_J_dot_J", "-G/(2*N)",
         recomputed["c_J_coefficient_of_J_dot_J"]),
        ("G_omega", "-G/N", recomputed["G_omega_equals_twice_c_J"]),
    ]
    comparison = []
    for name, paper3_value, mine in rows:
        left = sp.sympify(paper3_value, locals={"G": G, "N": N})
        right = sp.sympify(mine, locals={"G": G, "N": N})
        comparison.append({
            "quantity": name,
            "paper3": paper3_value,
            "recomputed": mine,
            "agree": bool(sp.simplify(left - right) == 0),
        })
    return {
        "levels": comparison,
        "all_levels_agree": all(item["agree"] for item in comparison),
        "why_this_matters":
            "Agreement at every intermediate level, not only at the endpoint, "
            "rules out compensating errors. Paper 3 also applies the crossing "
            "sign once at operator use, matching the 2026-08-07 ruling; had it "
            "not, endpoint agreement would have been accidental.",
    }


# ------------------------------------------------------------- main ------
def main() -> dict:
    paper3 = paper3_normalisation()
    recomputed = recompute_vector_singlet()
    declared = this_repository_normalisation()
    audit = verdict(recomputed, paper3)
    comparison = comparison_with_channel_character(recomputed, declared)
    if not comparison["agree"]:
        raise AssertionError(
            "recomputation disagrees with the channel-character result; "
            "this is a finding about that result and a STOP"
        )

    payload = {
        "study": "Normalisation audit: G_omega against the derived vector "
                 "coefficient",
        "status": "EVIDENCE PRODUCTION; one row of the CANONICAL_INTERACTION.md "
                  "§5 evidence table; ratifies nothing, removes no banner, "
                  "modifies no Paper-3 content",
        "authority": "specs/2026-08-08T1354Z_normalisation-audit.md",
        "derivation_note": "derivations/P2-NORMALISATION-AUDIT_g_omega.md",
        "repository_inputs_read": repository_inputs(),
        "input_sha256": {
            "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md":
                hashlib.sha256(FREEZE.read_bytes()).hexdigest(),
            "results/P2-CHANNEL-FREEZE/fierz_matrix.json":
                hashlib.sha256(FIERZ_JSON.read_bytes()).hexdigest(),
            "derivations/CANONICAL_INTERACTION.md":
                hashlib.sha256(CANONICAL.read_bytes()).hexdigest(),
            "derivations/P2-PHASE-01_fierz_sign_addendum.md":
                hashlib.sha256(SIGN_ADDENDUM.read_bytes()).hexdigest(),
            f"[external] {PAPER3_NOTE}": PAPER3_NOTE_SHA256,
        },
        "exclusions_confirmed": {
            "quarantined_-3.2(5)": "NOT READ",
            "suspended_P2-BETAV-CIRC-01_result": "NOT READ",
            "historical_Finding_5_extraction": "NOT READ",
        },
        "external_evidence_availability": "AVAILABLE; the pinned revision was "
                                          "fetched and its digest matched",
        "paper3_normalisation": paper3,
        "this_repository_normalisation": declared,
        "conversion": conversion(),
        "independent_recomputation": recomputed,
        "paper3_intermediate_agreement": paper3_intermediate_agreement(recomputed),
        "comparison_with_channel_character": comparison,
        "audit_verdict": audit,
        "rows_not_closed_by_this_audit": [
            "starting-interaction match (path, line range, pinned SHA)",
            "G_omega provenance to its derivation equation reference",
            "claim status VERIFIED (registry path and entry)",
            "test count (command and output digest)",
            "convention-compatibility table",
        ],
        "banner_status": "derivations/CANONICAL_INTERACTION.md retains its "
                         "DRAFT v0.5 ratification-candidate banner; this task "
                         "does not modify that file",
        "gate_status": "P2-PHASE-01 remains PROPOSED",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT}")
    return payload


if __name__ == "__main__":
    main()
