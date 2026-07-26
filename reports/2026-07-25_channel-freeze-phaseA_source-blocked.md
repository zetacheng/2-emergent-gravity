# P2-CHANNEL-FREEZE-01 Phase-A source-blocked report

## Outcome

Path S (source-blocked) was selected.  No single in-repository source was
found that both explicitly designates itself as the canonical governing
interaction and states the complete fixed four-fermion contraction (including
Dirac and internal/flavor indices) required by Phase A.  Consequently no
Phase-A freeze document, Fierz artifact, checker, gate edit, test edit, or
SI-2 computation was created.

`P2-CHANNEL-FREEZE-01` remains `PROPOSED`; the PI must supply or designate the
canonical interaction statement.

## Part 0

- Executor-local EOL configuration: `core.autocrlf=false`; `core.eol=lf`.
- Verified `origin/main` and local `HEAD`:
  `48b85d186b8fac54ed9d78eb3575990d28da486a`.
- Working tree was clean before this report was created.
- Branch: `gate/p2-channel-freeze`.

## Candidate-source audit

The following plausible in-repository sources were searched for a complete
canonical interaction statement.  Hashes are SHA-256 hashes of the examined
working-tree files.

| Source | SHA-256 | What it states | Why it is not a single canonical Phase-A source |
| --- | --- | --- | --- |
| `paper/emergent_gr_paper_v2_15.tex`, lines 238--271 | `be2551f19a82ba0ddc7ce92a3ced7faa25518db6e23a32ec117e511306e062cc` | Eq. `Lgen` gives a general channel-by-channel family with independent `G_i`; Eq. `L0` then gives a minimal scalar--pseudoscalar pair. | The file does not explicitly designate either expression as the repository's canonical governing interaction.  It presents distinct interaction choices, suppresses the requested full internal/flavor contraction, and its header records a v2.15 Fierz retraction/correction.  Choosing one expression here would be an unapproved adjudication, not a quotation from a single designated source. |
| `results/recovered-2026/emergent_gr_paper_v2_7.tex` | `bdb0aacccfe22bbc465a2ae014d330e0828a02c2c876e7dc8991b06b800088e9` | A recovered historical manuscript version. | It is a historical recovery artifact rather than an explicitly designated canonical interaction source; it cannot resolve the later corrected-Fierz convention without stitching sources. |
| `GATES.md`, `P2-CHANNEL-FREEZE-01`, lines 874--887 | `c4cb38b4acb43e26eea0441217982401de21b671139c0de3622affd2c9c3d109` | Requires the fixed interaction to be quoted verbatim in the future freeze document and lists it as an input. | It does not state the interaction or its contraction and therefore cannot be the requested governing source. |
| `CONVENTIONS.md` | `27be052fb1539556997263d30c9ea6d692a6cc0c38d9244aaeed90d1c62067b6` | Records flavor degeneracy, generator normalization, scalar attraction, and gamma conventions. | It contains conventions only, not the complete four-fermion interaction. |
| `derivations/P2-SI1-UNBLOCK-01.md` | `5e26354d4f52156baf6603484e7534f6f80795efd3f72dcc43d7a7a35d81d23c` | Records SI-1 governance and the Paper-3 vector-path dependency. | It does not give a complete canonical interaction statement. |
| `scripts/recovered_2026/batch2/fierz_verify.py`, `grassmann_check.py`, and `pairing_fierz.py` | `bb83b82dcf35ab4f794cd0172d6be226f01799bd0d4cfe2a512adde55e28e196`; `2ea213e794395f799003f5da7a5f56f4ebaf19829f74975e9ea000454034c164`; `9cf72e88e36405ca07d23575c56398cb52391a5e1b650f9895f5b1e0675d8f0f` | Recovered algebraic/Fierz checks and representations. | They provide machinery, not a source designated to govern the fixed microscopic action.  Using them to complete a manuscript expression would violate the no-stitching rule. |

## Missing canonical statement

To proceed on Path F, the repository needs one PI-designated in-repository
source that states, in one place:

1. the unique fixed four-fermion interaction to govern Paper 2;
2. its complete Dirac and internal/flavor index contraction and normalization;
3. the intended relation of all channel coefficients to the genuine
   microscopic coordinate(s); and
4. its canonical status after the corrected Paper-3 Fierz convention.

The manuscript's general multi-coupling expression, its restricted minimal
pair, later Fierz material, and recovered scripts must not be stitched into
such a statement.  That would create the missing canonical action rather than
freeze one.

## Scope guard

No channel inclusion or exclusion was made.  The governing independence rule
remains: “channel inclusion/exclusion is justified ONLY by the algebra and
symmetry of the fixed interaction and by adjudicated results meeting the
exclusion rule in §D. Nothing in this freeze may reference what would help or
hurt SI-2's outcome.”

## 2026-07-25 source-integrity preflight addendum (v2.14)

The original source block recorded above was resolved by the ratified canonical
interaction merged on `main`.  This addendum records a distinct v2.14
source-integrity preflight on the no-FF-synchronized
`gate/p2-channel-freeze` branch.  The synchronized branch contains
`derivations/CANONICAL_INTERACTION.md`; its SHA-256 is
`27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`, so
condition 1 passed.

The supplied `CANONICAL_INTERACTION.json` machine companion was not present in
the task attachment area.  Its actual SHA-256 is therefore unavailable, JSON
parsing cannot be attempted, and its recorded `source_markdown_path` and
`source_markdown_sha256` cannot be read.  This is an exact failure of
preflight condition 2.  Conditions 3--5 were not evaluated because the frozen
short-circuit rule applies; no copy was made, so condition 6 was not evaluated.

`derivations/CANONICAL_INTERACTION.json` does not exist in the working tree as
an uncommitted Task-0.5 artifact.  No freeze document, checker, result,
gate edit, or test edit was created.

`P2-CHANNEL-FREEZE-01` remains `PROPOSED`; the canonical-source integrity
chain does not match the ratified state — return to the PI.
