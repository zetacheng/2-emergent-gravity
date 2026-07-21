"""Consistency checks for the SI-1 dependency clarification (P2-SI1-UNBLOCK-01).

These guard the governance invariants, not any numerical result:
- P2-BETAV-CIRC-01 stays SUSPENDED and P2-BETAV-RECON-01 stays PROPOSED;
- the Paper 3 analytic input is pinned to the exact commit;
- the historical Finding 5 value is quarantined as unreproduced, never
  presented as validated (its claim stays PROPOSED).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER3_PINNED = "8c363ef08368f5c022278ea5f36e01496be3d5ca"


def _gate_status(gate_id: str) -> str:
    """Return the first 'Status:' line following the '## <gate_id>' heading."""
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    seen = False
    for line in lines:
        if line.startswith(f"## {gate_id} "):
            seen = True
            continue
        if seen and line.startswith("Status:"):
            return line
    raise AssertionError(f"no Status line found for {gate_id}")


def test_circ01_is_specified_after_recovery():
    # The gate left SUSPENDED only because the historical pipeline was RECOVERED
    # (not because the question was waved away). It is now in the allowed state
    # SPECIFIED (runnable, not run) -- never PASS/FAIL until the k-scan runs.
    status = _gate_status("P2-BETAV-CIRC-01")
    assert "SPECIFIED" in status
    assert "PASS" not in status and "FAIL" not in status
    # the recovery must be recorded in the gate body
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "recovered" in gates and "runnable but not yet run" in gates


def test_recon01_remains_proposed():
    assert "PROPOSED" in _gate_status("P2-BETAV-RECON-01")


def test_assembly01_remains_pass():
    assert "PASS" in _gate_status("P2-BETAV-ASSEMBLY-01")


def test_paper3_analytic_input_is_pinned():
    for rel in ("GATES.md", "results/P2-SI1-DEPENDENCY.md",
                "derivations/P2-SI1-UNBLOCK-01.md", "MIGRATION.md"):
        assert PAPER3_PINNED in (ROOT / rel).read_text(encoding="utf-8"), rel


def test_finding5_value_quarantined_as_unreproduced():
    # In the dependency record and MIGRATION, the historical value must appear
    # together with "unreproduced".
    for rel in ("results/P2-SI1-DEPENDENCY.md", "MIGRATION.md"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        assert "3.2(5)" in t and "unreproduced" in t, rel


def test_finding5_claim_not_promoted():
    # P2-C9 (the -3.2(5) claim) must remain PROPOSED, never VERIFIED/SUPPORTED.
    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    row = next(ln for ln in claims.splitlines()
               if ln.strip().startswith("| P2-C9 "))
    assert "3.2(5)" in row
    assert "PROPOSED" in row
    assert "VERIFIED" not in row and "SUPPORTED" not in row


def test_no_claim_is_verified():
    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    # No table row may carry the VERIFIED status.
    assert not re.search(r"\|\s*VERIFIED\s*\|", claims)


def test_channel_freeze_no_longer_requires_circ_pass():
    # The channel-freeze dependency must state it no longer requires CIRC-01 PASS.
    text = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "no longer requires" in text and "P2-BETAV-CIRC-01" in text


def test_canonical_reports_and_policy_exist():
    for rel in ("reports/REPORTING_POLICY.md",
                "reports/2026-07-20_P2-SI1-unblock_report.md",
                "reports/2026-07-20_P2-BETAV-provenance-merge_report.md"):
        assert (ROOT / rel).is_file(), rel
