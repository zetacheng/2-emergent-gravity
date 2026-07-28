import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_channel_freeze_machine_verifier():
    subprocess.run(
        [sys.executable, "scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py"],
        cwd=ROOT,
        check=True,
    )


def test_channel_freeze_phase_a_frozen_with_hash():
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    block = gates.split("## P2-CHANNEL-FREEZE-01", 1)[1].split("\n## ", 1)[0]
    assert "Status: PROPOSED" in block
    assert "Freeze state: PHASE-A FROZEN" in block
    assert "Metric state: PHASE-B PENDING" in block
    assert "SI-2 admissibility: BLOCKED UNTIL PHASE-B FREEZE" in block
    digest = hashlib.sha256(
        (ROOT / "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md").read_bytes()
    ).hexdigest()
    assert digest in block


def test_channel_freeze_vector_path_analytic():
    block = (
        (ROOT / "GATES.md")
        .read_text(encoding="utf-8")
        .split("## P2-CHANNEL-FREEZE-01", 1)[1]
        .split("\n## ", 1)[0]
    )
    assert "8c363ef08368f5c022278ea5f36e01496be3d5ca" in block
    assert "no validation from `−3.2(5)`" in block
