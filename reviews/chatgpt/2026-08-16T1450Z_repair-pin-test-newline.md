# Review — Repair Pin-Test Newline Specification

**Reviewed artifact:** `SPEC repair pin test newline(1).md`  
**Reviewed specification SHA-256:** `242f2339dd8c055a4f821b28ff08c6463bfdf3c49327647982c7182508847c31`  
**Review date:** 2026-08-16  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above. The complete specification was reviewed against the authoritative `tests/test_gate_pins.py` state previously inspected at the frozen repository evidence base.

The review specifically re-checks the defect explanation, `_HEX_A` control value, LF/CRLF byte-level reasoning, proposed one-line repair, scope restrictions, evidential labels, acceptance criteria, and commit/report discipline.

## 1. Defect identification — PASS

The revised specification correctly identifies the platform-dependent defect.

The test fixture writes `"content\n"` through `Path.write_text`. Without an explicit newline policy, platform newline translation can make the resulting bytes platform-dependent.

The relevant control constant is correctly identified as:

`_HEX_A = "a" * 64`

The specification no longer claims that the LF digest collides with `_HEX_A`.

## 2. Byte-level reasoning — PASS

The specification correctly distinguishes the two byte sequences:

- LF fixture bytes: `b"content\n"`
- CRLF-translated fixture bytes: `b"content\r\n"`

Their SHA-256 digests differ, and both differ from `_HEX_A`.

Accordingly, the first assertion (`measured != _HEX_A`) is not the platform-dependent failure. The platform-dependent failure is the second assertion comparing the measured file digest with the digest of literal LF bytes.

This matches the authoritative test structure.

## 3. Proposed repair — PASS

The proposed repair:

```python
artifact.write_text("content\n", encoding="utf-8", newline="")
```

is appropriately minimal.

It fixes the synthetic fixture bytes rather than weakening the assertion, changing the expected digest, modifying production pin-validation logic, or introducing platform-specific branching.

## 4. Scope discipline — PASS

The specification correctly limits the repair to the identified synthetic fixture write.

Other `write_text` sites are reported rather than opportunistically modified. The task does not introduce a helper, lint rule, `conftest` policy, or class-wide newline rewrite.

This is consistent with the specification's stated narrow repair scope.

## 5. Evidence labels — PASS

The specification correctly distinguishes locally measured evidence from derived cross-platform behaviour.

A Linux execution that does not reproduce the Windows failure must not claim that it measured the Windows failure locally. The CRLF failure mechanism may be reported as `DERIVED` from the byte-level transformation and digest comparison.

This is the appropriate epistemic treatment.

## 6. Test expectations — PASS

The specification does not require an artificial change in the Linux test count merely to demonstrate that the repair occurred.

Where the pre-repair Linux suite already passes, the expected before/after suite result may remain unchanged. The repair is justified by the cross-platform fixture semantics and the specified verification evidence, not by manufacturing a Linux regression.

## 7. Rule 16 / repair-boundary treatment — PASS

The specification correctly treats this as a targeted repair, not a proof that every text-writing fixture in the repository is platform-independent.

The remaining similar sites are findings outside the repair scope. The specification does not overstate the one-line change as a class-wide solution.

## 8. Acceptance criteria and history discipline — PASS

The acceptance criteria, staged checks, and commit/report layering are internally consistent with the narrow repair.

The final post-report verification is observational and does not require rewriting an already committed report merely to incorporate measurements that the specification intentionally places after that report stage.

No acceptance criterion requires an unauthorised expansion of the repair scope.

## Final verdict

**`APPROVE FOR EXECUTION`**

The previous factual defect concerning `_HEX_A` has been corrected. The revised specification now gives an accurate byte-level explanation of the platform-dependent failure and proposes a minimal repair consistent with the repository test structure.

I find no remaining scientific, technical, evidential, scope, or governance defect requiring another specification revision before execution.

This approval applies **only** to the specification with SHA-256:

`242f2339dd8c055a4f821b28ff08c6463bfdf3c49327647982c7182508847c31`
