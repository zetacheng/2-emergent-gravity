# PI authorization record — governance-tools validator environment

**Authorization date:** 2026-08-03  
**Originating task evidence base:** `3302b612b954af6369fc01a2e9a85cfb4f682a07`  
**Applies to branch/task:** `governance/rules-8-12-tools` — governance tools
implementation and validation task

The PI authorized, mid-task and in response to a correct stop, the following
external-environment work: locating or installing a Python interpreter;
creating an external virtual environment containing only `pytest`, `ruff`,
`numpy`, and `sympy`; and adding the dedicated worktree to Git's
`safe.directory` configuration.

This authorization means that work was not a deviation. The originating
specification's blanket prohibition on environment repair was over-broad: the
authorized work changed no repository content, frozen scientific input,
acceptance criterion, or validator strictness. It restored the ability to
execute already-authorized checks in an external environment. It does not
assert that runtime versions cannot affect results.

Resolved versions used:

- Python 3.12.10
- pytest 9.1.1
- ruff 0.16.1
- numpy 2.5.1
- sympy 1.14.0

This is not a general installation precedent. Introducing undeclared
dependencies, or altering lint or validator configuration, remains prohibited.
