# Pre-execution review --- P7 repair and pin validator

reviewed specification SHA-256:
`e925f074d81af4ed11e32be371aaa6d3dbce2e8d76b7e5c22d1a432d2fe34dd2`

## Disposition

**APPROVED**

I reviewed the supplied specification as a whole. The three issues
raised in the preceding review have been resolved sufficiently for
execution.

## Review findings

The specification now correctly limits the P1/P7 integration claim. It
establishes only that the relevant implementation regions in
`task_checker.py` are disjoint and that P1 dry-merges cleanly into the
current main. It explicitly does **not** infer that the completed P1 and
P7 branches will be conflict-free or order-independent, and requires
integration to measure all three shared files.

The stale-pin demonstration is now confined to a disposable temporary
copy or detached temporary worktree. The task branch working tree is not
to be altered, the temporary tree is not committed, and it is removed
afterwards. This resolves the earlier conflict between the A6
measurement and the writable-path restrictions.

The heading-completeness contract now closes the all-zero case
explicitly: zero raw `P2` headings returns `NOT_PARSEABLE`. It also
requires equality of independently counted raw headings and parsed
sections at both base and head, so partial parsing such as 14/15 cannot
produce a clean `PASS`.

The pre-issue verification record has also been corrected. The former
statement that the two branches are independent is explicitly retracted;
the surviving measured claim is limited to the evidence actually
obtained.

The P7 repair, pin validator, fixtures, classification update, scope
manifest, evidence layering, and Rule 16 limits are internally coherent.
I found no remaining stop-level ambiguity or contradiction that should
prevent execution.

## Non-blocking observation

In §1a, the opening sentence "the question was whether they would
collide. Measured: they do not" is broader in isolation than the
immediately following limitation to `task_checker.py`. The remainder of
§1a and §9 remove the ambiguity explicitly, including the capitalised
statement that the specification makes no overall order-independence
claim. I therefore do not treat this wording as execution-changing or as
a reason to withhold approval.

## Execution boundary

Approval is for execution of this specification as supplied. It does not
approve integration of the resulting branch, does not discharge P1's
A10, and does not authorise changes outside the frozen manifest.

No scientific or gate-state conclusion is reviewed or approved by this
artifact.
