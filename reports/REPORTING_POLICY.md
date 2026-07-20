# Repository reporting policy

**Permanent, repository-level rule.** Applies automatically to future tasks
unless the Principal Investigator explicitly overrides it.

1. **Every substantial Codex task must create a canonical report inside**
   `reports/` (or an established repository-specific reports directory).
2. **Terminal output is only a concise summary.**
3. **The repository report is authoritative.**
4. The report must contain enough detail for ChatGPT, Claude, Codex, or a human
   reviewer to inspect the work **directly from GitHub**.
5. The user must **not** be required to copy terminal output into chat.
6. Reports must include, where applicable:
   - task purpose;
   - branch and base SHA;
   - files changed;
   - computations run;
   - raw outputs;
   - tests;
   - mutation demonstrations;
   - scientific verdicts;
   - ledger changes;
   - limitations;
   - commit SHAs;
   - remote refs;
   - clean-tree status.
7. A task is **not review-complete** until its canonical report has been
   committed and pushed.

## Naming convention

`reports/YYYY-MM-DD_<slug>_report.md` (e.g.
`reports/2026-07-20_P2-SI1-unblock_report.md`).
