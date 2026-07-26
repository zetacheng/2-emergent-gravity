"""Exact, document-block-only verifier for P2-CHANNEL-FREEZE-01 Phase A."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "derivations" / "P2-CHANNEL-FREEZE-01_phaseA_freeze.md"
COMPANION = ROOT / "derivations" / "CANONICAL_INTERACTION.json"
ARTIFACT = ROOT / "results" / "P2-CHANNEL-FREEZE" / "fierz_matrix.json"
SIDECAR = ARTIFACT.with_suffix(".json.sha256")
MARKDOWN_SHA = "27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81"
COMPANION_SHA = "f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blocks() -> tuple[dict, dict]:
    raw = DOC.read_text(encoding="utf-8")
    found = re.findall(r"```json\n(.*?)\n```", raw, flags=re.S)
    assert len(found) == 2, "document must have exactly two canonical JSON blocks"
    return json.loads(found[0]), json.loads(found[1])


def expected_matrix() -> sp.Matrix:
    q = sp.Rational
    return sp.Matrix(
        [
            [q(1, 4), q(1, 4), q(1, 4), q(1, 4), q(1, 4)],
            [q(1, 4), q(1, 4), -q(1, 4), -q(1, 4), q(1, 4)],
            [1, -1, -q(1, 2), q(1, 2), 0],
            [1, -1, q(1, 2), -q(1, 2), 0],
            [q(3, 2), q(3, 2), 0, 0, -q(1, 2)],
        ]
    )


def canonical(expr: str) -> str:
    return re.sub(r"\s+", "", expr)


def verify() -> None:
    c_block, d_block = blocks()
    assert list(c_block) == [
        "basis_order",
        "basis_elements",
        "conventions",
        "matrix_rational",
    ]
    assert c_block["basis_order"] == ["S", "P", "V", "A", "T"]
    assert [item["basis_id"] for item in c_block["basis_elements"]] == c_block[
        "basis_order"
    ]
    conventions = c_block["conventions"]
    for key in (
        "metric_signature",
        "gamma5_definition",
        "sigma_definition",
        "dirac_trace_normalization",
        "un_generator_normalization",
        "grassmann_crossing_sign",
        "singlet_traceless_order",
        "compound_index_order",
    ):
        assert key in conventions
    assert conventions["grassmann_crossing_sign"] == "-1"
    matrix = sp.Matrix(
        [[sp.sympify(x) for x in row] for row in c_block["matrix_rational"]]
    )
    assert matrix == expected_matrix(), "exact Fierz matrix mismatch"
    assert matrix * matrix == sp.eye(5), "Fierz involution failed"
    assert matrix.rank() == 5, "family rank mismatch"
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert artifact == {
        "basis_order": c_block["basis_order"],
        "matrix_rational": c_block["matrix_rational"],
    }
    declared_hash = SIDECAR.read_text(encoding="utf-8").split()[0]
    assert declared_hash == sha256(ARTIFACT), "artifact sidecar mismatch"

    assert sha256(ROOT / "derivations" / "CANONICAL_INTERACTION.md") == MARKDOWN_SHA
    assert sha256(COMPANION) == COMPANION_SHA
    companion = json.loads(COMPANION.read_text(encoding="utf-8"))
    assert companion["source_markdown_path"] == "derivations/CANONICAL_INTERACTION.md"
    assert companion["source_markdown_sha256"] == MARKDOWN_SHA
    assert list(d_block) == [
        "canonical_interaction",
        "interaction_coordinates",
        "auxiliary_parameters",
        "interaction_decomposition",
        "stated_ranks",
        "hs_field_families",
        "kij_registry",
        "exclusions",
    ]
    frozen = d_block["canonical_interaction"]
    assert frozen["source_path"] == companion["source_markdown_path"]
    assert frozen["source_sha256"] == MARKDOWN_SHA
    assert canonical(frozen["expression"]) == canonical(
        companion["canonical_interaction_expression"]
    )
    coords = d_block["interaction_coordinates"]
    assert (
        len(coords) == 1
        and coords[0]["coordinate_id"] == "G"
        and coords[0]["scan_eligible"] is True
    )
    assert all(
        item["scan_eligible"] is False for item in d_block["auxiliary_parameters"]
    )
    decomposition = d_block["interaction_decomposition"]
    assert [x["family_id"] for x in decomposition] == ["S", "P"]
    reconstructed = (
        "(G/(2*N))*Sum(bilinear(lam(A),Id4)**2+"
        "bilinear(lam(A),I*gamma5)**2,(A,0,N**2-1))"
    )
    assert canonical(reconstructed) == canonical(
        companion["canonical_interaction_expression"]
    )
    ranks = d_block["stated_ranks"]
    assert ranks == {
        "interaction_coordinate_rank": "1",
        "fierz_family_rank": "5",
        "kij_component_count": "16*N**2",
    }
    families = d_block["hs_field_families"]
    registry = d_block["kij_registry"]
    assert len(families) == len(registry) == 5
    family_ids = [x["family_id"] for x in families]
    assert family_ids == ["S", "P", "V", "A", "T"] and len(set(family_ids)) == 5
    assert {x["family_id"] for x in registry} == set(family_ids)
    assert len({x["field_label"] for x in registry}) == 5
    assert all(x["candidate_for_kij"] is True for x in families)
    assert all(x["included"] is True and x["exclusion_id"] is None for x in registry)
    assert d_block["exclusions"] == []


if __name__ == "__main__":
    verify()
    print("P2-CHANNEL-FREEZE Phase-A exact verification: PASS")
