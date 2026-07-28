"""Mutation tests proving the Phase-A checker consumes frozen data."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"
REPORT = ROOT / "reports/2026-07-26_channel-freeze-phaseA_verifier-rebuild-4.md"
sys.path.insert(0, str(PATH.parent))
SPEC = importlib.util.spec_from_file_location("phase_check", PATH)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def data():
    c_block, d_block = CHECK.blocks()
    companion = json.loads(
        (ROOT / "derivations/CANONICAL_INTERACTION.json").read_text(encoding="utf-8")
    )
    return copy.deepcopy(c_block), copy.deepcopy(d_block), copy.deepcopy(companion)


MUTATIONS = [
    ("tensor", "tensor normalization mismatch"),
    ("matrix", "computed Fierz matrix mismatch"),
    ("coefficient", "reconstruction mismatch"),
    ("duplicate", "duplicate field_label"),
    ("removed", "component-domain coverage omission"),
    ("companion", "companion mismatch"),
    ("metric", "unsupported metric signature"),
    ("basis", "gram matrix normalization mismatch"),
    ("rule", "component-domain completeness mismatch"),
]


def mutation_error(mutation):
    c_block, d_block, companion = data()
    if mutation == "tensor":
        c_block["basis_elements"][-1]["expression"] = "I*gamma(mu)*gamma(nu)"
    elif mutation == "matrix":
        c_block["matrix_rational"][0][0] = "1/3"
    elif mutation == "coefficient":
        d_block["interaction_decomposition"][0]["coefficient"] = "G/N"
    elif mutation == "duplicate":
        duplicate = copy.deepcopy(d_block["kij_registry"][0])
        duplicate["family_id"] = "P"
        d_block["kij_registry"].append(duplicate)
    elif mutation == "removed":
        d_block["kij_registry"].pop()
    elif mutation == "companion":
        companion["canonical_interaction_expression"] = companion[
            "canonical_interaction_expression"
        ].replace("G/(2*N)", "G/N")
    elif mutation == "metric":
        c_block["conventions"]["metric_signature"] = ["1", "1", "1", "-1"]
    elif mutation == "basis":
        c_block["basis_elements"][3]["expression"] = "gamma(mu)*gamma5"
    else:
        c_block["basis_elements"][2]["component_rule"] = "mu=0..2"
    with pytest.raises(CHECK.VerificationError) as caught:
        CHECK.verify(c_block, d_block, companion)
    return str(caught.value)


@pytest.mark.parametrize(("mutation", "tag"), MUTATIONS)
def test_checker_rejects_each_frozen_data_corruption(mutation, tag):
    assert mutation_error(mutation) == tag


def test_gamma5_definition_is_evaluated_from_the_typed_ast():
    c_block, d_block, companion = data()
    c_block["conventions"]["gamma5_definition"] = "-gamma(0)*gamma(1)*gamma(2)*gamma(3)"
    with pytest.raises(
        CHECK.VerificationError, match="gamma5 parsed-definition mismatch"
    ):
        CHECK.verify(c_block, d_block, companion)


def test_singlet_extractor_ignores_surrounding_companion_prose():
    c_block, d_block, companion = data()
    companion["vocabulary"]["lam(A)"] = (
        "incidental words; lam(0) = sqrt(2/N)*IdN; more incidental words"
    )
    CHECK.verify(c_block, d_block, companion)


@pytest.mark.parametrize(
    "value,tag",
    [
        (
            "lam(0) = sqrt(2/N)*IdN; lam(0) = sqrt(2/N)*IdN",
            "singlet declaration mismatch",
        ),
        ("lam(0) = sqrt(1/N)*IdN", "singlet normalization mismatch"),
        ("U(N) generator with no singlet declaration", "singlet declaration mismatch"),
    ],
)
def test_singlet_declaration_regressions(value, tag):
    c_block, d_block, companion = data()
    companion["vocabulary"]["lam(A)"] = value
    with pytest.raises(CHECK.VerificationError, match=tag):
        CHECK.verify(c_block, d_block, companion)


def _rename_bound_everywhere(c_block, d_block, companion, *, tuple_name, lam_name):
    old_tuple, new_tuple = "(A,0,N**2-1)", f"({tuple_name},0,N**2-1)"
    old_tuple_spaced, new_tuple_spaced = "(A, 0, N**2-1)", f"({tuple_name}, 0, N**2-1)"
    old_lam, new_lam = "lam(A)", f"lam({lam_name})"
    for record in d_block["interaction_decomposition"]:
        record["operator_expression"] = (
            record["operator_expression"]
            .replace(old_tuple, new_tuple)
            .replace(old_lam, new_lam)
        )
    d_block["canonical_interaction"]["expression"] = (
        d_block["canonical_interaction"]["expression"]
        .replace(old_tuple, new_tuple)
        .replace(old_lam, new_lam)
    )
    companion["canonical_interaction_expression"] = (
        companion["canonical_interaction_expression"]
        .replace(old_tuple, new_tuple)
        .replace(old_tuple_spaced, new_tuple_spaced)
        .replace(old_lam, new_lam)
    )


def test_generator_sum_alpha_renaming_is_structural():
    c_block, d_block, companion = data()
    _rename_bound_everywhere(c_block, d_block, companion, tuple_name="B", lam_name="B")
    CHECK.verify(c_block, d_block, companion)


@pytest.mark.parametrize(("tuple_name", "lam_name"), [("B", "A"), ("A", "B")])
def test_generator_sum_partial_alpha_renaming_is_rejected(tuple_name, lam_name):
    c_block, d_block, companion = data()
    _rename_bound_everywhere(
        c_block, d_block, companion, tuple_name=tuple_name, lam_name=lam_name
    )
    with pytest.raises(CHECK.VerificationError, match="generator sum mismatch"):
        CHECK.verify(c_block, d_block, companion)


def test_accuracy_report_uses_captured_mutation_tags():
    report = REPORT.read_text(encoding="utf-8")
    for mutation, expected in MUTATIONS:
        actual = mutation_error(mutation)
        assert actual == expected
        assert f"| {mutation} | {expected} | {actual} | PASS |" in report
    for statement in (
        "gamma5 parsed-definition mismatch",
        "duplicate parsed declarations",
        "absent declaration",
        "sqrt(1/N)*IdN",
        "`A` to `B` binder rename passes",
        "binder-only and occurrence-only",
    ):
        assert statement in report
