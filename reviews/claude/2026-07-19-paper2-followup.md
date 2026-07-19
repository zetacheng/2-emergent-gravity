# Paper 2 normalization, gap, and βV-circularity follow-up review

Reviewed branch: `claude/paper-2-independent-verification-dysdp0` at
`de754ea6d7aff94c253b29bb80aea9ebb70cd54f`.

Repository: `zetacheng/2-emergent-gravity`.

Independent reviewer. Date: 2026-07-19.

## Checks performed independently

1. **D1 retraction.**
   The earlier D1 discrepancy was correctly withdrawn. It mixed the report-side
   `Z(β_F)` normalization with the paper-side `G_c` convention, producing an
   apparent factor-of-two conflict that was not a physical contradiction.

2. **P2-NORM-01.**
   The recorded normalization adjudication is accepted. The factor of two is a
   bookkeeping/normalization effect, uniform across scalar, Dirac, and Proca
   species, with `R_Z = 2`. The paper relation

   > `4 G_c β_F = 1/6`

   is internally consistent; the report-side `1/3` resulted from convention
   mixing. The already-recorded residual caveat concerning the axis-TT-slope
   mapping remains and is not promoted.

3. **P2-GAP-01.**
   The recorded gap resolution is accepted. The continuum `I_0` evaluation is
   exact, and the lattice result agrees at matched mass. The earlier
   approximately `1.2%` difference was a mass-matching issue rather than a
   genuine continuum–lattice inconsistency.

4. **P2-BETAV-CIRC-01 analytic layer.**
   The analytic script was rerun independently. The target ratio is

   > `R(k) = -(k + 2)`,

   and is therefore structure-dependent. The committed mutation/discrimination
   anchor confirms that distinct `k` values are not degenerate. This establishes
   that a faithful extraction has discriminating power in principle.

5. **P2-BETAV-CIRC-01 full lattice layer.**
   The full curved-background lattice Proca reproduction has not been performed.
   The decisive test remains to feed the actual lattice extraction a `k ≠ 1`
   structure and determine whether the extracted ratio follows `-(k + 2)` or
   remains fixed near `-3`.
   Accordingly, the full gate remains OPEN. It is neither passed nor failed.

6. **Executability and tests.**
   The repository suite passes on the reviewed branch. The βV analytic script
   runs directly through the repository-supported invocation, and the committed
   discrimination/mutation anchor is live.

## Cross-repository consequence

Paper 3's quoted value near `-3.2(5)` is not invalidated by this review, but the
dependency remains unresolved/suspended until the full lattice discrimination
test is completed.

P3-C-004, concerning `C_6 = -G_V/2`, is structurally independent of the
unresolved numerical extraction and is unaffected.

## Disposition

The Paper 2 follow-up is accepted.

* D1 retraction stands.
* P2-NORM-01 stands at its migrated/recorded resolved status.
* P2-GAP-01 stands at its migrated/recorded resolved status.
* The analytic layer of P2-BETAV-CIRC-01 is accepted.
* The full P2-BETAV-CIRC-01 gate remains OPEN.
* Nothing is promoted to VERIFIED.

The next scientific task is the full curved-background lattice Proca
discrimination test with `k ≠ 1`.
