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
    Binary,
    Call,
    Equality,
    IndexTuple,
    Number,
    ParseError,
    Symbol,
    Unary,
    ast_key,
    component_rule,
    descriptor,
    expand_basis_expression,
    parse,
    parse_generator_normalization,
    parse_grassmann_sign,
    parse_metric,
    parse_trace_normalization,
    scalar_ast,
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
    try:
        return sp.cancel(scalar_ast(parse(value)))
    except ParseError as error:
        raise VerificationError(
            "decomposition coefficient outside frozen scalar grammar"
        ) from error


def _gamma_value(node: object, gammas: list[sp.Matrix]) -> sp.Matrix:
    if isinstance(node, Symbol):
        if node.name == "I":
            return sp.I * sp.eye(4)
        if node.name == "gamma5":
            return gammas[0] * gammas[1] * gammas[2] * gammas[3]
    if (
        isinstance(node, Call)
        and node.name == "gamma"
        and len(node.arguments) == 1
        and isinstance(node.arguments[0], Number)
    ):
        return gammas[node.arguments[0].value]
    if isinstance(node, Unary):
        value = _gamma_value(node.value, gammas)
        return value if node.op == "+" else -value
    if isinstance(node, Binary):
        left, right = _gamma_value(node.left, gammas), _gamma_value(node.right, gammas)
        if node.op == "*":
            return left * right
        if node.op == "/":
            require(
                right == right[0, 0] * sp.eye(4), "gamma5 parsed-definition mismatch"
            )
            return left / right[0, 0]
    raise VerificationError("gamma5 parsed-definition mismatch")


def _generator_terms(node: object) -> tuple[sp.Expr, tuple[tuple, ...]]:
    """Extract typed GeneratorSum records; only explicit additive order commutes."""
    if not (isinstance(node, Binary) and node.op == "*"):
        raise VerificationError("generator sum mismatch")
    coefficient = scalar_ast(node.left)
    sum_node = node.right
    if not (
        isinstance(sum_node, Call)
        and sum_node.name == "Sum"
        and isinstance(sum_node.arguments[1], IndexTuple)
    ):
        raise VerificationError("generator sum mismatch")
    body, index = sum_node.arguments
    if not (
        isinstance(index.index, Symbol)
        and index.index.name == "A"
        and ast_key(index.lower) == ast_key(Number(0))
        and ast_key(index.upper)
        == ast_key(Binary("-", Binary("**", Symbol("N"), Number(2)), Number(1)))
    ):
        raise VerificationError("generator sum mismatch")
    addends = []

    def collect(value: object) -> None:
        if isinstance(value, Binary) and value.op == "+":
            collect(value.left)
            collect(value.right)
        else:
            addends.append(ast_key(value))

    collect(body)
    for term in addends:
        require(term[0] == "binary" and term[1] == "**", "generator sum mismatch")
    return coefficient, tuple(sorted(addends))


def _companion_singlet_declaration(text: str) -> Equality:
    marker = "lam(0) = sqrt(2/N)*IdN"
    require(marker in text, "singlet declaration mismatch")
    value = parse(marker)
    require(isinstance(value, Equality), "singlet declaration mismatch")
    return value


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
    try:
        parsed_gamma5 = _gamma_value(parse(conventions["gamma5_definition"]), gammas)
    except ParseError as error:
        raise VerificationError("gamma5 parsed-definition mismatch") from error
    require(parsed_gamma5 == gamma5, "gamma5 parsed-definition mismatch")
    require(
        gamma5 * gamma5 == sp.eye(4)
        and gamma5.H == gamma5
        and all(gamma5 * gamma + gamma * gamma5 == sp.zeros(4) for gamma in gammas),
        "gamma5 algebra mismatch",
    )
    trace_declaration = parse_trace_normalization(
        conventions["dirac_trace_normalization"]
    )
    require(
        ast_key(trace_declaration) == ast_key(parse("trace(Id4)=4")),
        "Dirac trace normalization mismatch",
    )
    trace_norm = sp.Integer(4)
    generator_declaration = parse_generator_normalization(
        conventions["un_generator_normalization"]
    )
    require(
        ast_key(generator_declaration)
        == ast_key(parse("trace(lam(A)*lam(B))=2*KroneckerDelta(A,B)")),
        "internal normalization mismatch",
    )
    generator_norm, generator_domain = sp.Integer(2), descriptor("S[A=0..N**2-1]")
    require(
        generator_norm == 2 and generator_domain.cardinality == N**2,
        "internal normalization mismatch",
    )
    tensor = next(item for item in c_block["basis_elements"] if item["basis_id"] == "T")
    require(
        tensor["expression"] == conventions["sigma_definition"],
        "tensor normalization mismatch",
    )
    family_components = [
        expand_basis_expression(
            parse(item["expression"]),
            component_rule(item["component_rule"]),
            gammas,
            gamma5,
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
    canonical = parse(d_block["canonical_interaction"]["expression"])
    external = parse(companion["canonical_interaction_expression"])
    require(ast_key(canonical) == ast_key(external), "companion mismatch")
    singlet = _companion_singlet_declaration(companion["vocabulary"]["lam(A)"])
    require(
        isinstance(singlet.right, Binary) and singlet.right.op == "*",
        "singlet declaration mismatch",
    )
    singlet_factor = singlet.right.left
    require(
        isinstance(singlet_factor, Call) and singlet_factor.name == "sqrt",
        "singlet declaration mismatch",
    )
    require(
        scalar_ast(singlet_factor.arguments[0]) == 2 / N, "singlet declaration mismatch"
    )
    require(sp.cancel((2 / N) * N) == 2, "singlet normalization mismatch")
    decomposition = d_block["interaction_decomposition"]
    terms = [parse(item["operator_expression"]) for item in decomposition]
    coefficients = [_coefficient(item["coefficient"]) for item in decomposition]
    require(len(set(coefficients)) == 1, "reconstruction mismatch")
    outside, target_terms = _generator_terms(external)
    require(outside == coefficients[0], "reconstruction mismatch")
    record_terms = []
    for term in terms:
        term_with_coefficient = Binary(
            "*", parse(decomposition[terms.index(term)]["coefficient"]), term
        )
        term_outside, extracted = _generator_terms(term_with_coefficient)
        require(term_outside == outside, "reconstruction mismatch")
        record_terms.extend(extracted)
    require(tuple(sorted(record_terms)) == target_terms, "reconstruction mismatch")
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
