# Canonical-interaction ratification evidence table

**Date:** 2026-07-25  
**Paper 2 base:** `48b85d186b8fac54ed9d78eb3575990d28da486a`  
**Paper 3 pin:** `8c363ef08368f5c022278ea5f36e01496be3d5ca`

This is the clean-clone evidence required for ratification of
`derivations/CANONICAL_INTERACTION.md`.  All source quotations below were read
from the pinned Paper-3 checkout.  The final post-landing clean-tree check is
also recorded in the landing report.

| # | Assertion | Minimum evidence | Outcome |
| --- | --- | --- | --- |
| 1 | Paper-3 starting interaction is equivalent to the generator-sum form in §2 | `derivations/u3-fierz/u3_fierz.md` lines 4--8 quotes: “Fierz-exchanging the U(3) NJL bracket” and `L_int = (G / 2N) * Sum_{A=0}^{8} [ (psibar lambda^A psi)^2 + (psibar i gamma5 lambda^A psi)^2 ]`.  §2 of the supplied document states the same generator sum for symbolic `N`, with the same `G/(2N)` prefactor and scalar plus `i gamma_5` pseudoscalar bilinears; Paper 3 is its `N=3` specialization.  Pinned-file SHA-256: `6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49`. | PASS |
| 2 | Generator normalization matches | Paper 3, lines 37--41: `Tr[lambda^A lambda^B] = 2 delta^AB`, `lambda^0 = sqrt(2/3) 1_3`.  Supplied §2: `Tr[λ^A λ^B] = 2δ^{AB}`, `λ^0 = sqrt(2/N)·1_N`.  At `N=3`, the definitions coincide exactly. | PASS |
| 3 | `G_omega = -G/N` is derived there | Paper 3, §7 “Action-prefactor assembly”, lines 184--193: after restoring `L_int = (G/2N)*[...]`, it gives `L_int -> -(G/2N) J_mu J^mu = (G_omega/2) J_mu J^mu with G_omega = -G/N`, then classifies `G_V = G_omega = -G/N < 0` as repulsive. | PASS |
| 4 | Claim `P3-C-001` status is VERIFIED | `CLAIMS.md`, line 9 (full entry): `| P3-C-001 | Pure U(3) vector-singlet Fierz projection gives \`G_omega=-G/N\`. | VERIFIED | Migrated gate artifacts. Independently reproduced and accepted 2026-07-16 (clean-environment reproduction; mutation-tested anchors; archive verified within portable tolerances; 12/12 tests). See \`reviews/claude/2026-07-16-vector-sector.md\`. | P3-FIERZ-01 | §The model's own vector content: Fierz projection | 2026-07-16 |`  Pinned-file SHA-256: `c4be14e0dee52669da3635e59f4f49403958791036815ed11f8953f286dbb1d0`. | PASS |
| 5 | Paper-3 test suite passes | Clean-clone command: `C:\\Users\\User\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe -m pytest tests -q`.  Exit code: `0`.  Output: `12 passed in 63.65s (0:01:03)`, matching the registry’s recorded 12/12.  Captured-output SHA-256 (including the recorded exit line): `0444399ef970cfe9a771083ec9d0c57b2180f6ec12c861226e52f4edbbe881b0`. | PASS |
| 6 | Conventions are compatible | Paper 3 §1 lines 22--25 states mostly-minus `eta = diag(+1,-1,-1,-1)` for quoted physical statements, while Fierz numbers use Euclidean `{g_mu,g_nu}=2 delta_mu_nu`; lines 28--30 define hermitian `g5` with the pseudoscalar `i g5`; lines 37--39 give the generator normalization; lines 192--193 classify `G_V<0` as repulsive.  Paper 2 `CONVENTIONS.md` lines 12--13, 26--28, and 32 specifies Euclidean `(+,+,+,+)`, hermitian Euclidean Clifford algebra, hermitian `gamma_5`, and scalar-channel `G>0` attraction.  The metric use differs only by role (Paper 3 quotes physical statements in mostly-minus but computes Fierz ratios in the same Euclidean Clifford algebra); `i gamma_5` and the scalar-attractive/vector-negative-repulsive sign classification are compatible. | PASS |
| 7 | Pinned commit exists and is readable | On the Paper-3 clean clone, `git cat-file -t 8c363ef08368f5c022278ea5f36e01496be3d5ca` returned `commit`; `git log -1 --format=%H` returned `8c363ef08368f5c022278ea5f36e01496be3d5ca`. | PASS |
| 8 | Working trees clean | Before landing, `git status --porcelain` was empty in both the Paper-2 landing clone and the Paper-3 pinned clone.  After the Paper-3 test suite, the Paper-3 clone remained empty.  The Paper-2 post-landing clean-tree result is recorded after its commits in the landing report, without treating generated test output as a repository artifact. | PASS |
