"""Computed, typed verification for the frozen Phase-A JSON blocks.

The document supplies all basis, convention, coordinate, and registry data.
This checker supplies only exact linear algebra and a parameterised gamma factory.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import sympy as sp
from gamma_algebra import gamma_factory
from vocab_parser import (
    canonical_operator,
    component_rule,
    descriptor,
    expand_basis_expression,
    parse_generator_normalization,
    parse_grassmann_sign,
    parse_metric,
    parse_trace_normalization,
)

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "derivations" / "P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
COMPANION = ROOT / "derivations" / "CANONICAL_INTERACTION.json"
ARTIFACT = ROOT / "results" / "P2-CHANNEL-FREEZE" / "fierz_matrix.json"
SIDECAR = ARTIFACT.with_suffix(".json.sha256")
MARKDOWN = ROOT / "derivations" / "CANONICAL_INTERACTION.md"
GATES = ROOT / "GATES.md"
MARKDOWN_SHA = "27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81"
COMPANION_SHA = "f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1"
N = sp.Symbol("N", nonzero=True)
G = sp.Symbol("G", nonzero=True)


class VerificationError(AssertionError):
    """A labelled frozen-verification obligation failed."""


def require(condition: bool, tag: str) -> None:
    if not condition:
        raise VerificationError(tag)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blocks(raw: str | None = None) -> tuple[dict, dict]:
    text = DOC.read_text(encoding="utf-8") if raw is None else raw
    found = re.findall(r"```json\r?\n(.*?)\r?\n```", text, flags=re.S)
    require(len(found) == 2, "document JSON-block count mismatch")
    return json.loads(found[0]), json.loads(found[1])


def _matrix_from_strings(rows: list[list[str]]) -> sp.Matrix:
    def atom(value: str) -> sp.Expr:
        if re.fullmatch(r"-?\d+", value):
            return sp.Integer(value)
        if re.fullmatch(r"-?\d+/\d+", value):
            numerator, denominator = value.split("/")
            return sp.Rational(int(numerator), int(denominator))
        raise VerificationError("matrix expression outside frozen scalar grammar")

    return sp.Matrix([[atom(value) for value in row] for row in rows])


def _coefficient(value: str) -> sp.Expr:
    compact = value.replace(" ", "")
    if compact == "G/(2*N)":
        return G / (2 * N)
    if compact == "G/N":
        return G / N
    if compact == "G":
        return G
    raise VerificationError("decomposition coefficient outside frozen scalar grammar")


def _canonical_sum(terms: list[str], coefficient: sp.Expr) -> str:
    contents = []
    for term in terms:
        prefix = "Sum("
        suffix = ",(A,0,N**2-1))"
        require(
            term.startswith(prefix) and term.endswith(suffix), "reconstruction mismatch"
        )
        contents.append(term[len(prefix) : -len(suffix)])
    joined = "+".join(contents)
    if coefficient == G / (2 * N):
        prefix = "(G/(2*N))"
    elif coefficient == G / N:
        prefix = "(G/N)"
    else:
        prefix = str(coefficient).replace(" ", "")
    return f"{prefix}*Sum({joined},(A,0,N**2-1))"


def _pair_vector(matrix: sp.Matrix) -> sp.Matrix:
    vector = sp.zeros(256, 1)
    for alpha in range(4):
        for beta in range(4):
            for gamma in range(4):
                for delta in range(4):
                    vector[((alpha * 4 + beta) * 4 + gamma) * 4 + delta] = (
                        matrix[alpha, beta] * matrix[gamma, delta]
                    )
    return vector


def _crossing_pair_map() -> sp.Matrix:
    result = sp.zeros(256)
    for alpha in range(4):
        for beta in range(4):
            for gamma in range(4):
                for delta in range(4):
                    source = ((alpha * 4 + beta) * 4 + gamma) * 4 + delta
                    target = ((alpha * 4 + delta) * 4 + gamma) * 4 + beta
                    result[target, source] = 1
    return result


def _family_embedding(families: list[list[sp.Matrix]]) -> sp.Matrix:
    return sp.Matrix.hstack(
        *[
            sum((_pair_vector(item) for item in family), sp.zeros(256, 1))
            for family in families
        ]
    )


def _extract_heading_region(path: Path, start: str, next_heading: str) -> bytes:
    payload = path.read_bytes()
    lines = payload.splitlines(keepends=True)
    starts = [
        index
        for index, line in enumerate(lines)
        if line.startswith(start.encode("utf-8"))
    ]
    require(len(starts) == 1, "quotation source heading mismatch")
    begin = starts[0]
    ends = [
        index
        for index in range(begin + 1, len(lines))
        if lines[index].startswith(next_heading.encode("utf-8"))
    ]
    require(bool(ends), "quotation source end heading mismatch")
    return b"".join(lines[begin : ends[0]])


def _marker_region(marker_begin: str, marker_end: str) -> bytes:
    payload = DOC.read_bytes()
    begin_match = re.search(
        re.escape(marker_begin.encode("utf-8")) + b"\\r?\\n", payload
    )
    end_match = re.search(b"\\r?\\n" + re.escape(marker_end.encode("utf-8")), payload)
    require(
        begin_match is not None and end_match is not None, "quotation marker mismatch"
    )
    separator = end_match.group()[: -len(marker_end.encode("utf-8"))]
    return payload[begin_match.end() : end_match.start()] + separator


def verify_quotations() -> None:
    require(
        _marker_region(
            "<!-- BEGIN VERBATIM CANONICAL §2 -->", "<!-- END VERBATIM CANONICAL §2 -->"
        )
        == _extract_heading_region(MARKDOWN, "## §2", "## §3"),
        "canonical quotation byte mismatch",
    )
    require(
        _marker_region(
            "<!-- BEGIN VERBATIM GATES SI-2 -->", "<!-- END VERBATIM GATES SI-2 -->"
        )
        == _extract_heading_region(GATES, "## P2-MULTIPHASE-GRAV-01", "## "),
        "gate quotation byte mismatch",
    )


def verify(
    c_override: dict | None = None,
    d_override: dict | None = None,
    companion_override: dict | None = None,
) -> dict:
    c_block, d_block = blocks() if c_override is None else (c_override, d_override)
    require(
        list(c_block)
        == ["basis_order", "basis_elements", "conventions", "matrix_rational"],
        "basis block schema mismatch",
    )
    require(
        [item["basis_id"] for item in c_block["basis_elements"]]
        == c_block["basis_order"],
        "basis order mismatch",
    )
    conventions = c_block["conventions"]
    metric = parse_metric(conventions["metric_signature"])
    try:
        gammas = gamma_factory(metric)
    except ValueError as error:
        raise VerificationError("unsupported metric signature") from error
    require(
        all(
            gammas[mu] * gammas[nu] + gammas[nu] * gammas[mu]
            == 2 * metric[mu] * sp.eye(4)
            if mu == nu
            else gammas[mu] * gammas[nu] + gammas[nu] * gammas[mu] == sp.zeros(4)
            for mu in range(4)
            for nu in range(4)
        ),
        "clifford relation mismatch",
    )
    gamma5 = gammas[0] * gammas[1] * gammas[2] * gammas[3]
    require(
        conventions["gamma5_definition"].replace(" ", "")
        == "gamma(0)*gamma(1)*gamma(2)*gamma(3)",
        "gamma5 definition mismatch",
    )
    require(
        gamma5 * gamma5 == sp.eye(4)
        and gamma5.H == gamma5
        and all(gamma5 * gamma + gamma * gamma5 == sp.zeros(4) for gamma in gammas),
        "gamma5 algebra mismatch",
    )
    trace_norm = parse_trace_normalization(conventions["dirac_trace_normalization"])
    generator_norm, generator_domain = parse_generator_normalization(
        conventions["un_generator_normalization"]
    )
    require(
        generator_norm == 2 and generator_domain.cardinality == N**2,
        "internal normalization mismatch",
    )
    require(
        "lam(A)" in canonical_operator(d_block["canonical_interaction"]["expression"]),
        "internal convention mismatch",
    )
    tensor = next(item for item in c_block["basis_elements"] if item["basis_id"] == "T")
    require(
        tensor["expression"] == conventions["sigma_definition"],
        "tensor normalization mismatch",
    )
    family_components = [
        expand_basis_expression(
            item["expression"], component_rule(item["component_rule"]), gammas, gamma5
        )
        for item in c_block["basis_elements"]
    ]
    flat = [matrix for family in family_components for matrix in family]
    require(len(flat) == 16, "component-domain completeness mismatch")
    gram = sp.Matrix([[sp.trace(left.H * right) for right in flat] for left in flat])
    require(
        all(matrix.H == matrix for matrix in flat) and gram == trace_norm * sp.eye(16),
        "gram matrix normalization mismatch",
    )
    require(gram.rank() == 16, "gram matrix rank mismatch")
    embedding = _family_embedding(family_components)
    pair_gram = embedding.T * embedding
    require(pair_gram.det() != 0, "pair-space aggregation singular")
    projector = pair_gram.inv() * embedding.T
    require(projector * embedding == sp.eye(5), "pair-space aggregation mismatch")
    crossing = _crossing_pair_map()
    sign = parse_grassmann_sign(conventions["grassmann_crossing_sign"])
    # The frozen matrix is a coefficient-row action; dualising the computed
    # pair-space column action supplies its exact, typed orientation.
    computed_fierz = (sign * projector * crossing * embedding).T * sign
    frozen_fierz = _matrix_from_strings(c_block["matrix_rational"])
    require(computed_fierz == frozen_fierz, "computed Fierz matrix mismatch")
    require(
        computed_fierz * computed_fierz == sp.eye(5), "crossing matrix not involutory"
    )
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    require(
        artifact
        == {
            "basis_order": c_block["basis_order"],
            "matrix_rational": c_block["matrix_rational"],
        },
        "Fierz artifact mismatch",
    )
    require(
        SIDECAR.read_text(encoding="utf-8").split()[0] == sha256(ARTIFACT),
        "artifact sidecar mismatch",
    )
    require(
        sha256(MARKDOWN) == MARKDOWN_SHA and sha256(COMPANION) == COMPANION_SHA,
        "source hash mismatch",
    )
    companion = companion_override or json.loads(COMPANION.read_text(encoding="utf-8"))
    require(
        companion["source_markdown_sha256"] == MARKDOWN_SHA,
        "companion markdown pin mismatch",
    )
    canonical = canonical_operator(d_block["canonical_interaction"]["expression"])
    external = canonical_operator(companion["canonical_interaction_expression"])
    require(canonical == external, "companion mismatch")
    decomposition = d_block["interaction_decomposition"]
    terms = [canonical_operator(item["operator_expression"]) for item in decomposition]
    coefficients = [_coefficient(item["coefficient"]) for item in decomposition]
    require(len(set(coefficients)) == 1, "reconstruction mismatch")
    reconstructed = _canonical_sum(terms, coefficients[0])
    require(reconstructed == external, "reconstruction mismatch")
    coordinates = d_block["interaction_coordinates"]
    require(
        all(item["scan_eligible"] for item in coordinates),
        "coordinate eligibility mismatch",
    )
    jacobian = sp.Matrix(
        [[sp.diff(coefficient, G) for _ in coordinates] for coefficient in coefficients]
    )
    coordinate_rank = jacobian.rank()
    require(
        coordinate_rank == int(d_block["stated_ranks"]["interaction_coordinate_rank"]),
        "interaction-coordinate rank mismatch",
    )
    require(
        computed_fierz.rank() == int(d_block["stated_ranks"]["fierz_family_rank"]),
        "Fierz family rank mismatch",
    )
    columns = [jacobian[:, index] for index in range(jacobian.cols)]
    require(
        all(column != sp.zeros(column.rows, 1) for column in columns),
        "zero microscopic direction",
    )
    for left in range(len(columns)):
        for right in range(left + 1, len(columns)):
            orbit_left = (columns[left], computed_fierz * columns[left])
            orbit_right = (columns[right], computed_fierz * columns[right])
            for first in orbit_left:
                for second in orbit_right:
                    proportional = all(
                        sp.cancel(first[row] * second[col] - first[col] * second[row])
                        == 0
                        for row in range(first.rows)
                        for col in range(first.rows)
                    )
                    require(not proportional, "Fierz-orbit duplicate")
    families = d_block["hs_field_families"]
    registry = d_block["kij_registry"]
    require(
        len({item["field_label"] for item in registry}) == len(registry),
        "duplicate field_label",
    )
    family_domains = {
        item["family_id"]: descriptor(item["components"][0]) for item in families
    }
    registry_domains = {
        item["family_id"]: descriptor(item["component_id"]) for item in registry
    }
    require(
        set(family_domains) == set(registry_domains),
        "component-domain coverage omission",
    )
    for family, domain in family_domains.items():
        require(
            domain == registry_domains[family], "component-domain completeness mismatch"
        )
    cardinality = sp.expand(
        sum(domain.cardinality for domain in family_domains.values())
    )
    stated = d_block["stated_ranks"]["kij_component_count"]
    require(cardinality == 16 * N**2 and stated == "16*N**2", "cardinality mismatch")
    require(not d_block["exclusions"], "exclusion registry mismatch")
    verify_quotations()
    return {
        "gram": gram,
        "fierz": computed_fierz,
        "coordinate_rank": coordinate_rank,
        "fierz_rank": computed_fierz.rank(),
        "cardinality": cardinality,
        "family_cardinalities": {
            key: value.cardinality for key, value in family_domains.items()
        },
    }


if __name__ == "__main__":
    verify()
    print("P2-CHANNEL-FREEZE Phase-A exact verification: PASS")
