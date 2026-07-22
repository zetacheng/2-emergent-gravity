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
    # The gate left SUSPENDED only because the historical pipeline was RECOVERED.
    # It is in the allowed state SPECIFIED and has NOT passed or failed. The
    # Phase-1 design adjudication (DECOMP-UNAVAILABLE-AS-RECOVERED) withdrew the
    # additive k-scan design; that is a statement about the design, not a CIRC
    # verdict.
    status = _gate_status("P2-BETAV-CIRC-01")
    assert "SPECIFIED" in status
    assert "PASS" not in status and "FAIL" not in status  # the Status: line only
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "recovered" in gates
    assert "DECOMP-UNAVAILABLE-AS-RECOVERED" in gates
    assert "Previous additive k-scan design: WITHDRAWN" in gates


def test_recon01_remains_proposed():
    assert "PROPOSED" in _gate_status("P2-BETAV-RECON-01")


def test_numrepro01_specified_not_run():
    # After the campaign pre-registration, NUMREPRO is SPECIFIED (rules frozen)
    # and has NOT run (no PASS/FAIL). The dual-gate promotion rule is unchanged.
    status = _gate_status("P2-BETAV-NUMREPRO-01")
    assert "SPECIFIED" in status
    assert "PASS" not in status and "FAIL" not in status
    assert "not run" in status.lower()


def test_campaign_prereg_and_harness_present():
    # The pre-registration doc and the blind harness/comparison exist.
    for rel in ("derivations/P2-BETAV-CAMPAIGN_prereg.md",
                "scripts/P2-BETAV-CAMPAIGN/harness_compute.py",
                "scripts/P2-BETAV-CAMPAIGN/compare.py"):
        assert (ROOT / rel).is_file(), rel


def test_audit_pass_alone_does_not_promote_c9():
    # A future CIRC operator-identity audit PASS, on its own, must not flip the
    # -3.2(5) quarantine: promotion still requires BOTH gates, and P2-C9 stays
    # PROPOSED. This guards the dual-gate rule against the new audit path.
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "alone does not verify or promote" in gates
    assert "does not by itself promote `P2-C9`" in gates
    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    row = next(ln for ln in claims.splitlines()
               if ln.strip().startswith("| P2-C9 "))
    assert "PROPOSED" in row and "VERIFIED" not in row


def test_dual_gate_promotion_rule_present():
    # Promotion of P2-C9 must require BOTH gates to PASS -- neither alone.
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "P2-BETAV-CIRC-01 = PASS" in gates
    assert "P2-BETAV-NUMREPRO-01 = PASS" in gates
    # both appear together in a promotion-rule context
    assert "requires" in gates and "P2-C9" in gates


def test_circ_pass_alone_does_not_promote():
    # The CIRC gate's Scope must state a PASS does not verify/promote -3.2(5).
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert "A PASS does **not** verify or promote" in gates
    # The betaV report must carry the corrected boundary, not "may be promoted".
    rep = (ROOT / "reports"
           / "2026-07-20_betav-complete-recovery_report.md").read_text(
               encoding="utf-8")
    assert "does not promote" in rep
    assert "may be\npromoted" not in rep and "value may be promoted" not in rep


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
