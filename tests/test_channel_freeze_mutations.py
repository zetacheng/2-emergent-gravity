import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"
sys.path.insert(0, str(PATH.parent))
SPEC = importlib.util.spec_from_file_location("phase_check", PATH)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def data():
    c, d = CHECK.blocks()
    companion = json.loads(
        (ROOT / "derivations/CANONICAL_INTERACTION.json").read_text()
    )
    return copy.deepcopy(c), copy.deepcopy(d), copy.deepcopy(companion)


@pytest.mark.parametrize(
    "mutation", ["tensor", "matrix", "coefficient", "duplicate", "removed", "companion"]
)
def test_checker_rejects_frozen_data_mutation(mutation):
    c, d, companion = data()
    if mutation == "tensor":
        c["basis_elements"][-1]["expression"] = "I*gamma(mu)*gamma(nu)"
    elif mutation == "matrix":
        c["matrix_rational"][0][0] = "1/3"
    elif mutation == "coefficient":
        d["interaction_decomposition"][0]["coefficient"] = "G/N"
    elif mutation == "duplicate":
        d["kij_registry"].append(copy.deepcopy(d["kij_registry"][0]))
    elif mutation == "removed":
        d["kij_registry"].pop()
    else:
        companion["canonical_interaction_expression"] = companion[
            "canonical_interaction_expression"
        ].replace("G/(2*N)", "G/N")
    with pytest.raises(AssertionError):
        CHECK.verify(c, d, companion)
