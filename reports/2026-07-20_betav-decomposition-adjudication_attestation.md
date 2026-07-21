# Attestation — P2-BETAV-CIRC-01 Phase-1 decomposition adjudication (branch `gate/p2-betav-decomp`)

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `gate/p2-betav-decomp`.
**Type:** pre-attestation record — commit-chronology + clean-checkout state,
captured **before** the attestation commit that carries this file. (A commit
cannot contain its own SHA; this file therefore records the branch through the
pre-attestation HEAD and deliberately does not embed the attestation commit's
own hash. Do not amend after committing to insert it — that would change the
SHA recursively.)

## Base commit

```
2c396fc9ffadfc961c636ae3e3aae7740a1f14a4  (main, base of gate/p2-betav-decomp)
```

## Branch-only commit chronology (`git log --reverse --format='%H %s' 2c396fc..HEAD`)

Every branch-only commit through the pre-attestation HEAD, in order, full SHA and
subject:

```
6fd54d3e43b76091c26017cc87577bcd1a36f099 derivation: operator-level checks of the recovered Proca determinant (no target)
82157de990b0060d639fe1504f69019d8365c58a derivation: determinant decomposition for P2-BETAV-CIRC-01 (Phase 1, no scan)
3df147686500eaf7a31cf17d29313cb1c04e4917 docs: betaV determinant-decomposition adjudication (DECOMP-NOT-REPRESENTABLE)
322865623f18e016609ac217e2f403ee54c7bda0 chore: gitignore nested results/**/regen (decomp check outputs)
aebcf3876b5916ad6224a8da927e6f146ce53adc derivation: q^2-level T/L sector decomposition of the Proca bubble (no target)
3ef51ccd8dfeddcce541fbe9902edb1f57dcb49b docs: tighten betaV Phase-1 adjudication to DECOMP-UNAVAILABLE-AS-RECOVERED
8523bb3ff305b9ed064a59be8afa86c8e078b5c1 docs: revise betaV decomposition adjudication report (q^2-level, DECOMP-UNAVAILABLE-AS-RECOVERED)
7b05217bc04791f4f790d4285a51f0ebec3b408c gates: rewrite P2-BETAV-CIRC-01 specification post-adjudication (k-scan withdrawn)
9bdc29b19bb6ab179d20065df9f16ea6b8e12475 scripts: deprecate wrong-basis T/L mixing check (superseded by q2-level analysis)
```

Named commits of record for this task's three consistency fixes:

- report revision (q²-level): `8523bb3ff305b9ed064a59be8afa86c8e078b5c1`
- **Fix 1** — GATES.md specification rewrite (k-scan withdrawn):
  `7b05217bc04791f4f790d4285a51f0ebec3b408c`
- **Fix 2** — deprecate wrong-basis T/L mixing check:
  `9bdc29b19bb6ab179d20065df9f16ea6b8e12475`

```
Pre-attestation HEAD: 9bdc29b19bb6ab179d20065df9f16ea6b8e12475
```

The attestation commit (Fix 3) that carries this file, together with the report
seagull-wording refinement, sits one commit **after** the pre-attestation HEAD;
its SHA is reported in the task response, not embedded here.

## Clean-checkout verification (at pre-attestation HEAD `9bdc29b`)

Fresh `git clone` of the branch, checked out at `9bdc29b`:

- `git status --porcelain`: **clean** (empty output).
- `python -m pytest tests -q`: **34 passed, 2 deselected**.
- `python -m pytest tests -q -m "slow or not slow"`: **36 passed**.
- `ruff check .`: **All checks passed.**
- Live-spec consistency (`sed -n '/## P2-BETAV-CIRC-01/,/## P2-BETAV-NUMREPRO-01/p'
  GATES.md | grep -nE 'runnable|decisive'`): **no hits** — the stale k-scan
  wording survives only inside the clearly-marked "Superseded specification
  (historical record)" block.

## Remote branch SHA observed immediately before the attestation commit

```
9bdc29b19bb6ab179d20065df9f16ea6b8e12475	refs/heads/gate/p2-betav-decomp
```

(`git ls-remote --heads origin gate/p2-betav-decomp`, observed after pushing the
Fix 1 / Fix 2 commits and before creating the attestation commit.)

## Invariants held (unchanged by this task)

- `P2-BETAV-CIRC-01` = `SPECIFIED`; Phase-1 design adjudication
  `DECOMP-UNAVAILABLE-AS-RECOVERED`; no CIRC PASS/FAIL.
- `P2-BETAV-NUMREPRO-01` = `PROPOSED`; `P2-C9` = `PROPOSED`.
- `β_V/β_B = −3.2(5)` quarantined/unreproduced; `CLAIMS.md` untouched.
