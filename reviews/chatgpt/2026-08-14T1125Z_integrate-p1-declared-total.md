# Pre-execution review — integrate the declared-total `P1` grammar, and land it

**Disposition: APPROVED**

**Reviewed specification SHA-256:** `9ba407bf136075ac23e76161cc0644f9fbe0d260c6ad135edf3c6d900e399576`

**Reviewed file:** `SPEC integrate p1 declared total.md`

## Review conclusion

The specification is approved for execution as written.

The blocking issue identified in the previous review has been corrected. A9 now distinguishes the exact range governed by the source task's original A10 from the range governed by its A10-final:

- A9a uses base `1cb5550f…` and head `f02a7116…`, the source task's commit-4 pre-report head.
- A9b separately uses base `1cb5550f…` and head `8ff032e7…`, the branch tip and A10-final head.
- Both runs are explicitly labelled EVIDENCE, and the specification requires the report to state that the source task's A10 remains undischarged and that neither run discharges it.

This preserves the distinction the specification is designed to enforce: later evidence about what a repaired checker would report is not retroactive discharge of a stopped criterion.

## Scope and integration review

The scope arithmetic is internally consistent. At the merge commit the expected range is five additions and three modifications; after the report commit the final range is six additions and three modifications. The six source-contributed paths are separated from the three paths authored by this integration task.

A6 correctly treats the three auto-merged files differently from the three source additions. The source additions must remain blob-identical to the source tip, while each auto-merged file must differ from both the source and current-main versions. A7 then checks the behaviour that matters after that textual merge: the repaired P7 grammar must still parse 14 of 14 raw gate headings, and the declared-total P1 grammar and `parse_scope_block` handling of `stated:` must both remain present.

A11 provides an independent collection guard for the auto-merged test file by requiring the pytest count to rise from 301 and requiring the delta to be explained. This is an appropriate landing precondition for two independently modified parser/test files being auto-merged.

## Governance and evidence layering

The stale merge base is disclosed rather than normalised away. The specification does not infer semantic order-independence from a clean merge and does not rebase or re-cut the source branch.

The report/landing layering is coherent: commits 1 and 2 precede the merge, the committed report measures through commit 3 only, A10-final and the final validator run occur at commit 4 before landing, and authoritative `main` advances only by verified fast-forward.

The Rule 16 limits are appropriately preserved. Landing P1 does not close the broader enforcement gap; increased P1 coverage is attributed to newer specifications adopting the declared syntax rather than to increased backward compatibility; the source A10 remains undischarged; and the two gate-heading grammars remain independently defined even while they currently agree.

## Non-blocking observation

The specification is intentionally demanding in A6: requiring each auto-merged blob to differ from both parents is valid for the measured merge described here, because both sides are known to contain real changes to each of the three files. If the measured merge unexpectedly changes shape, the correct action under this specification is to STOP rather than reinterpret the criterion.

## Approval

No blocking inconsistency remains. The task may proceed under Rule 15 and Rule 18 exactly as specified.

This review approves the uploaded specification identified by the SHA-256 above. A file with different bytes or a different digest is not covered by this approval.
