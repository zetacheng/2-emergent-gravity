# D-1 literature coverage audit — execution 3 report

Authority: `specs/2026-08-16T1952Z_d1-literature-coverage-audit.md`  
Branch: `science/d1-literature-coverage-audit-3`  
Evidence base: `b27926aad0d3a1ef39f5e7e886f8571657c5687c`  
Measured head: commit 3, `86e2710ca3f04715519bd82b2fd8cac21274a75e`

## 1. A3 — scholarly-access precondition, reported first

**PASS.** arXiv supplied an abstract record and full-text link for Neuberger's `hep-lat/9707022`, so the global precondition passed and the audit proceeded.

| Host/route attempted | Outcome in this execution |
|---|---|
| `https://arxiv.org/abs/hep-lat/9707022` | Accessible: abstract plus PDF/full-text routes. |
| `https://doi.org/10.1016/S0370-2693(97)01368-3` | Direct DOI route rejected by the browsing safety layer. |
| ScienceDirect publisher page for that DOI | HTTP 403. |

Historical comparison: execution 1 had 12 scholarly hosts return HTTP 403 and its non-scholarly control also returned HTTP 403, which diagnosed a global sandbox block. Execution 3 instead had work/host-dependent access and used per-work fetch depth throughout.

## 2. A13a — environment conformance before dependent measurements

Rule 13's order, including Amendment D's step 0, was run before the measurements below:

    (0) location/workspace   C:\Users\User\Phy_Projects\Paper 2\.agents\d1-literature-coverage-audit-3
                             branch science/d1-literature-coverage-audit-3
                             HEAD 86e2710c…; isolated sibling worktree
    (1) execution identity  zeta-3070\codexsandboxoffline
    (2) interpreter         Python 3.12.10; declared validator venv
                             C:\p2-validator\venv
    (3) permissions         worktree owner ZETA-3070\Zeta Cheng; git reads
                             used an ephemeral safe.directory setting
    (4) filesystem/history  not shallow; 434 commits at commit 3
    (5) packages            pytest 9.1.1, ruff 0.16.1, numpy 2.5.1,
                             sympy 1.14.0 — present and importable
    (6) process/harness     no conflicting Python/pytest process observed

One environment restoration was needed: pytest inherited the inaccessible host path
`C:\Users\User\AppData\Local\Temp\pytest-of-Zeta Cheng`. The first full run
therefore produced 96 setup errors (`228 passed, 2 deselected`). `TEMP` and
`TMP` were redirected to this session's writable scratch root and the suite was
rerun. No repository content was touched to make the environment work. Neither of
Rule 13's two failure-order wordings was exercised after that restoration.

## 3. A1–A2 — repository identity, refs, branch, spec and review

MEASURED before ref interpretation, origin was
`https://github.com/zetacheng/2-emergent-gravity.git`, which identifies
`zetacheng/2-emergent-gravity`.

After fetch:

    refs/remotes/origin/main  b27926aad0d3a1ef39f5e7e886f8571657c5687c
    refs/heads/main           fd5f6b967644f8866c7f4188fd10bd68e604ce18
    local-main ancestor?      yes, exit 0

The local ref lagged and was not changed. Before creation,
`science/d1-literature-coverage-audit-3` did not exist. Execution 3 was cut
from the authoritative remote-tracking ref in its isolated worktree. The
existing execution-2 worktree/branch was not touched.

The supplied specification was committed byte-for-byte. MEASURED SHA-256:
`44d575363cd8cfea6444acd2bdcc56eed6d8bdcfbee707247d6a67c911582889`.
The supplied review contains the field `Reviewed specification SHA-256` with
that exact digest and was committed byte-for-byte; its own MEASURED SHA-256 is
`c15390a1deb9b5aed4ea56b14e9e49ba774ce263aad375a2e9d8833c770e3f4c`.

## 4. A4 — baseline claims and gap

Read from `derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md` at the
evidence base:

- L1, lines 256–274: Osterwalder–Schrader 1973/1975 reconstruction axioms;
  continuum reconstruction, explicitly not action-specific RP coverage.
- L2, lines 276–293: Osterwalder–Seiler 1978 Wilson gauge/fermion RP
  recollection; reflection details and exact conditions were not recalled,
  and the programme four-fermion non-gauge action was not covered.
- L3, lines 295–311: **no author/work recalled**; scope and coverage not
  recalled; expressly incomplete and not counted as a structured claim.
- L4, lines 313–329: Neuberger overlap definition and
  Hernández–Jansen–Lüscher locality; explicitly locality only, not RP.
- Lines 331–335 count three structured claims (L1, L2, L4), four entries
  marked unverified, and one incomplete gap (L3).

Thus the source contains three claims and one literature gap, not four claims.

## 5. A5 and A8 — citation depth and bounded search

| Key | Identifier | Fetch depth | Coverage role |
|---|---|---:|---|
| OS73 | DOI `10.1007/BF01645738` | FULL TEXT | reconstruction background only |
| OS75 | DOI `10.1007/BF01608978` | FULL TEXT | reconstruction background only |
| OS78 | DOI `10.1016/0003-4916(78)90039-8` | ABSTRACT | Wilson kinetic route corroboration |
| MP87 | DOI `10.1007/BF01221251` | FULL TEXT | naive/Wilson kinetic RP, load-bearing |
| N97 | arXiv `hep-lat/9707022`; DOI `10.1016/S0370-2693(97)01368-3` | FULL TEXT | overlap definition, not RP |
| HJL98 | arXiv `hep-lat/9808010`; DOI `10.1016/S0550-3213(99)00213-8` | FULL TEXT | overlap locality, not RP |
| KU10 | arXiv `1005.3751`; DOI `10.1103/PhysRevD.82.114503` | FULL TEXT | overlap RP, load-bearing |
| GK22 | arXiv `2209.06031`; DOI `10.1007/s00220-023-04858-8` | FULL TEXT | staggered Hamiltonian route evidence |
| FG26 | arXiv `2606.13075` | FULL TEXT | naive/staggered interacting RP, load-bearing |
| STW81 | DOI `10.1016/0550-3213(81)90200-5` | ABSTRACT | formulation context only |
| L77 | DOI `10.1007/BF01614090` | NOT FETCHED | encountered, not pursued; transfer-matrix-only bearing |

Counts: **10 fetched** (8 full text, 2 abstract, 0 listing-only), **0 recalled
statements**, and **1 encountered/not pursued**. OS78 is the only
abstract-only item close to load-bearing; its missing article-level
hypotheses prevent it from supporting `COVERED`. STW81 supports no verdict.
Search-result snippets located works but were not used as evidence.

L77 is the sole encountered work not pursued: its identifier was pinned, but a
transfer-matrix construction alone cannot settle proposition (ii).

## 6. A6 — applicability declarations

| Work | Candidates applicability-tested | Not an applicability candidate |
|---|---|---|
| OS73 | none | all four: reconstruction, not action-specific RP |
| OS75 | none | all four: reconstruction, not action-specific RP |
| OS78 | Wilson | naive, staggered, overlap: different formulation |
| MP87 | Wilson; naive via explicit `r=0` discussion | staggered, overlap: different operators |
| N97 | none | definition is not RP, including for overlap |
| HJL98 | none | locality is not RP, including for overlap |
| KU10 | overlap | naive, Wilson, staggered: different operators |
| GK22 | none for (ii); staggered route evidence only | Hamiltonian/infrared-bound result is not OS positivity of the programme Euclidean action |
| FG26 | naive, staggered | Wilson, overlap: different operators |
| STW81 | none | abstract-only context supplies no inspected RP theorem |

Full seven-axis and theorem-hypothesis mapping for every relevant pair:

| Pair | Free/interacting | Reflection | Extent | Boundary conditions | Locality | Measure/determinant | Gauge |
|---|---|---|---|---|---|---|---|
| MP87→Wilson | FAIL: no programme NJL term | FAIL: site, programme unfrozen | FAIL: extent unmapped | FAIL: programme unfrozen | family-level ultralocal only | FAIL: gauge/Grassmann measure and observable algebra unmapped | FAIL: gauge theorem needs an unfrozen specialization |
| MP87→naive | FAIL: kinetic only | FAIL: link, programme unfrozen | FAIL: extent unmapped | FAIL: programme unfrozen | MAPPED at ultralocal family level | FAIL: source measure/observables unmapped | FAIL: gauge specialization unestablished |
| OS78→Wilson | UNKNOWN at abstract depth | UNKNOWN | UNKNOWN | UNKNOWN; programme also unfrozen | UNKNOWN | FAIL: hypotheses unavailable | FAIL: gauge specialization unavailable |
| FG26→naive | FAIL: scalar GN, not exact generator sum | FAIL: bond/link, programme unfrozen | FAIL: finite 2D torus vs 4D | FAIL: anti-periodic both axes | MAPPED at broad ultralocal level | FAIL: effective bosonic measure unmapped | MAPPED: non-gauge |
| FG26→staggered | FAIL: scalar GN, not exact generator sum | FAIL: bond/link, programme unfrozen | FAIL: finite 2D torus vs 4D | FAIL: anti-periodic both axes | broad family only; taste map missing | FAIL: effective bosonic measure unmapped | MAPPED: non-gauge |
| KU10→overlap | FAIL: free/different Yukawa interaction | FAIL: link, programme unfrozen | FAIL: finite `[-L+1,L]^4` | FAIL: AP time/P space, programme unfrozen | family-level exponential locality | FAIL: positivity cone/Yukawa measure not mapped to NJL | MAPPED: non-gauge |

Theorem-specific hypotheses, in full:

- **MP87→Wilson:** dimension 4 mapped; normalization unmapped; `r`
  unfrozen; `K<1/6` has no mass/hopping map; gauge-invariant observable
  algebra unfrozen; the `G>0` interaction is absent.
- **MP87→naive:** dimension 4 mapped; `0≤r≤1` with `r=0` maps the
  doubled family; normalization and mass/hopping domain unmapped; the
  `G>0` interaction is absent.
- **OS78→Wilson:** dimension, normalization, `r`, mass/hopping domain,
  coupling, volume, boundary and observable hypotheses are unknown at
  abstract depth; the exact interaction is not reported.
- **FG26→naive:** dimension 2 fails; even `N` fails symbolic unrestricted
  `N`; size divisibility and normalization are unmapped; `λ>0` is only
  sign-compatible because the operator differs; determinant reflection
  invariance H1, local Grassmann factorization H2, and cross-term
  decomposition H3 are unproved for the programme action.
- **FG26→staggered:** the same dimension, even-`N`, size, coupling and
  H1–H3 failures apply; staggered phases, normalization and the
  flavour/taste mapping are additionally unfrozen.
- **KU10→overlap:** dimension 4 maps; operator normalization does not;
  `0<m≤1` cannot map because programme `M0` is unfrozen; finite extent
  and boundary data are unfrozen; the strictly local Yukawa interaction
  does not supply an NJL auxiliary-field/measure junction.

GK22 and L77 are separately classified `ROUTE EVIDENCE`; neither contributed
to a proposition-(ii) verdict.

## 7. A7 — four proposition-(ii) verdicts and discrete burden

| Candidate | Verdict | Exact reason full coverage fails |
|---|---|---|
| naive | `PARTIAL` | MP87/FG26 give relevant RP evidence, but no 4D exact `U(N)` scalar+pseudoscalar generator-sum result; `N`, BCs and measure do not map |
| Wilson | `PARTIAL` | MP87 kinetic theorem is relevant, but `r`, `K`/mass, BC/reflection, non-gauge specialization and exact interaction do not map |
| staggered | `PARTIAL` | FG26 fills L3 with a 2D interacting theorem, but dimension, interaction/symmetry, even-`N`, BC, taste and measure hypotheses fail |
| overlap | `PARTIAL` | KU10 covers specified free overlap and a different Yukawa model, but `M0`, BCs and the NJL auxiliary-field/measure junction fail |

Counts: `COVERED 0`, `PARTIAL 4`, `NO COVERAGE FOUND 0`,
`NOT DETERMINABLE 0`.

Of B0's four candidate-specific proposition-(ii) construction units,
**0 are replaced by literature-applicability work and 4 remain full or open**.
No fractional reduction is claimed.

## 8. A9 — no selection and no proof-route design

The artifact, this uncommitted report, and commit messages were searched
case-insensitively for forms of `select`, `rank`, `prefer`, `proof route`
and `construct`. Matches are scope prohibitions, bibliographic titles,
descriptions of fetched authors' constructions, and explicit non-selection
statements. No sentence selects, eliminates, ranks or prefers a candidate, and
no missing proof is designed.

Candidate treatment length in the artifact:

    naive       25 lines, 371 whitespace tokens
    Wilson      25 lines, 356 whitespace tokens
    staggered   25 lines, 365 whitespace tokens
    overlap     25 lines, 350 whitespace tokens

Line lengths happen to be equal; token lengths differ. The differences reflect
the genuinely different source bases and failing hypotheses (FG26/MP87,
MP87/OS78, FG26/GK22, KU10/N97/HJL98), not levelling or candidate merit.
The audit prompted interest in a future applicability/proof task chiefly at
the auxiliary-field/measure junction shared by the interaction question, but
it did not design that route or select a candidate.

## 9. Rule 16 — four junctions

1. Literature applicability is not an independent repository proof of the
   theorem. A fully mapped published theorem would apply mathematically, but
   repository-level applicability derivation and provenance are distinct.
2. Coverage is not physics evidence and is not candidate merit. More literature
   means only that a formulation has been studied more under related hypotheses.
3. This bounded audit fetched 10 works and retains 0 recalled statements.
   `NO COVERAGE FOUND` would mean no fetched work applies, not that no work
   exists.
4. L3 was a gap, not a claim. FG26 fills the naming/search gap with a fetched
   staggered theorem, but only partially: it does not fill the programme's
   proposition-(ii) coverage gap.

The assembled set therefore does not establish the exact programme RP result
for any candidate, does not independently reprove its sources, and does not
support a physical ranking.

## 10. A10–A12 — scope, unchanged base files, gates and pins

At commit 3, MEASURED scope is three additions and zero modifications:

    A derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
    A reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md
    A specs/2026-08-16T1952Z_d1-literature-coverage-audit.md

INTENDED final scope at commit 4 is exactly four additions and zero
modifications, adding only
`reports/2026-08-16T1952Z_d1-literature-coverage-audit.md`.
Forbidden delete, rename, copy, type-change, unmerged and unknown operations
remain absent.

There were 439 paths at the evidence base. MEASURED, all 439 were compared and
all 439 are blob-identical at commit 3; changed-existing count is zero.

Gate/pin invariants, MEASURED at commit 3:

    ^## P2- sections                         14
    P2-PHASE-01                              Status: PROPOSED
    microscopic-parameter prerequisite      SATISFIED
    input-admissibility prerequisite         SATISFIED
    microscopic-parameter pin/recomputed     4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214 / MATCH
    input-admissibility pin/recomputed        e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3 / MATCH

## 11. A13 — task checker at commit 3

All four invocations exited 0 with overall `PASS`. In every output, P3 and
P7 report `declared_source: specification`; P7 reports 14 sections at base
and head; `DECLARATION_CONFLICT` occurs zero times. A pass at zero did not
occur. RUN 1 was observational and discovered the one task specification.
RUN 2 named only this task's specification and was stop-governing.

### RUN 1 INCLUSIVE config, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 1 INCLUSIVE output, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "commits_in_range": 3,
  "commits_on_first_parent_line": 3,
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "overall": "PASS",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "append_only": [
            "DECISION_LOG.md"
          ],
          "authorised_gates": [],
          "counted": 4,
          "counted_add": 4,
          "counted_modify": 0,
          "counted_set": [
            "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
            "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
          ],
          "parse": "OK",
          "path": "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
          "stated": 4,
          "stated_add": 4,
          "stated_modify": 0,
          "stated_record": "stated: 4 additions, 0 modifications"
        }
      ],
      "id": "P1",
      "status": "PASS",
      "title": "scope manifest arithmetic"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "commits": [
          {
            "adds_review": false,
            "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
            "work_paths": [
              "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
            ]
          }
        ],
        "first_review_commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
        "first_work_commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
        "in_scope": 3,
        "out_of_scope": []
      },
      "id": "P2",
      "status": "PASS",
      "title": "Rule 15 commit order"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
      "evidence": {
        "declared": [
          "DECISION_LOG.md"
        ],
        "declared_by_specification": [
          "DECISION_LOG.md"
        ],
        "declared_key": "append_only",
        "declared_source": "specification",
        "paths": [
          {
            "base_bytes": 89541,
            "base_is_byte_prefix_of_head": true,
            "commits_with_deletions": [],
            "deleted_lines_base_to_head": 0,
            "head_bytes": 89541,
            "path": "DECISION_LOG.md",
            "status": "PASS"
          }
        ],
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [
          "DECISION_LOG.md"
        ]
      },
      "id": "P3",
      "status": "PASS",
      "title": "append-only on both measures"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "entries": [
          {
            "branch": "fix/pi-decisions-and-deferred",
            "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "fix/pi-decisions-v2",
            "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-v2",
            "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-and-superseded",
            "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "review/role-model-and-executors",
            "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "gate/p2-land-diquark-line",
            "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          }
        ],
        "register_path": "docs/BRANCHING_POLICY.md"
      },
      "id": "P4",
      "status": "PASS",
      "title": "superseded branches are not merged"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
      "evidence": {
        "merges": []
      },
      "id": "P5",
      "reason": "no merge commit in range",
      "status": "NOT_APPLICABLE",
      "title": "merge parentage against recomputed facts"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
      "evidence": [
        {
          "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
          "matches": [],
          "status": "PASS"
        }
      ],
      "id": "P6",
      "status": "PASS",
      "title": "commit-message hygiene"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
      "evidence": {
        "added_sections": [],
        "authorised_modified": [],
        "declared": [],
        "declared_by_specification": [],
        "declared_key": "authorised_gates",
        "declared_source": "specification",
        "gates_path": "GATES.md",
        "raw_heading_count_base": 14,
        "raw_heading_count_head": 14,
        "removed_sections": [],
        "section_count_base": 14,
        "section_count_head": 14,
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [],
        "unauthorised_changed": []
      },
      "id": "P7",
      "status": "PASS",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
        "first_commit_paths": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ]
      },
      "id": "P8",
      "status": "PASS",
      "title": "Rule 15 placement and specification-first"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {},
      "id": "P9",
      "reason": "range adds no report",
      "status": "NOT_APPLICABLE",
      "title": "reports carry a Stops and clarifications section"
    }
  ],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "commits_in_scope": 3,
    "commits_out_of_scope": [],
    "inclusivity": "INCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```

### RUN 1 EXCLUSIVE config, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "EXCLUSIVE"},
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 1 EXCLUSIVE output, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "commits_in_range": 3,
  "commits_on_first_parent_line": 3,
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "overall": "PASS",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "append_only": [
            "DECISION_LOG.md"
          ],
          "authorised_gates": [],
          "counted": 4,
          "counted_add": 4,
          "counted_modify": 0,
          "counted_set": [
            "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
            "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
          ],
          "parse": "OK",
          "path": "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
          "stated": 4,
          "stated_add": 4,
          "stated_modify": 0,
          "stated_record": "stated: 4 additions, 0 modifications"
        }
      ],
      "id": "P1",
      "status": "PASS",
      "title": "scope manifest arithmetic"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "commits": [
          {
            "adds_review": false,
            "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
            "work_paths": [
              "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
            ]
          }
        ],
        "first_review_commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
        "first_work_commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
        "in_scope": 3,
        "out_of_scope": []
      },
      "id": "P2",
      "status": "PASS",
      "title": "Rule 15 commit order"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
      "evidence": {
        "declared": [
          "DECISION_LOG.md"
        ],
        "declared_by_specification": [
          "DECISION_LOG.md"
        ],
        "declared_key": "append_only",
        "declared_source": "specification",
        "paths": [
          {
            "base_bytes": 89541,
            "base_is_byte_prefix_of_head": true,
            "commits_with_deletions": [],
            "deleted_lines_base_to_head": 0,
            "head_bytes": 89541,
            "path": "DECISION_LOG.md",
            "status": "PASS"
          }
        ],
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [
          "DECISION_LOG.md"
        ]
      },
      "id": "P3",
      "status": "PASS",
      "title": "append-only on both measures"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "entries": [
          {
            "branch": "fix/pi-decisions-and-deferred",
            "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "fix/pi-decisions-v2",
            "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-v2",
            "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-and-superseded",
            "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "review/role-model-and-executors",
            "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "gate/p2-land-diquark-line",
            "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          }
        ],
        "register_path": "docs/BRANCHING_POLICY.md"
      },
      "id": "P4",
      "status": "PASS",
      "title": "superseded branches are not merged"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
      "evidence": {
        "merges": []
      },
      "id": "P5",
      "reason": "no merge commit in range",
      "status": "NOT_APPLICABLE",
      "title": "merge parentage against recomputed facts"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
      "evidence": [
        {
          "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
          "matches": [],
          "status": "PASS"
        }
      ],
      "id": "P6",
      "status": "PASS",
      "title": "commit-message hygiene"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
      "evidence": {
        "added_sections": [],
        "authorised_modified": [],
        "declared": [],
        "declared_by_specification": [],
        "declared_key": "authorised_gates",
        "declared_source": "specification",
        "gates_path": "GATES.md",
        "raw_heading_count_base": 14,
        "raw_heading_count_head": 14,
        "removed_sections": [],
        "section_count_base": 14,
        "section_count_head": 14,
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [],
        "unauthorised_changed": []
      },
      "id": "P7",
      "status": "PASS",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
        "first_commit_paths": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ]
      },
      "id": "P8",
      "status": "PASS",
      "title": "Rule 15 placement and specification-first"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {},
      "id": "P9",
      "reason": "range adds no report",
      "status": "NOT_APPLICABLE",
      "title": "reports carry a Stops and clarifications section"
    }
  ],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "commits_in_scope": 3,
    "commits_out_of_scope": [],
    "inclusivity": "EXCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```

### RUN 2 INCLUSIVE config, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "specification_paths": ["specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"],
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 INCLUSIVE output, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "commits_in_range": 3,
  "commits_on_first_parent_line": 3,
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "overall": "PASS",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "append_only": [
            "DECISION_LOG.md"
          ],
          "authorised_gates": [],
          "counted": 4,
          "counted_add": 4,
          "counted_modify": 0,
          "counted_set": [
            "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
            "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
          ],
          "parse": "OK",
          "path": "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
          "stated": 4,
          "stated_add": 4,
          "stated_modify": 0,
          "stated_record": "stated: 4 additions, 0 modifications"
        }
      ],
      "id": "P1",
      "status": "PASS",
      "title": "scope manifest arithmetic"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "commits": [
          {
            "adds_review": false,
            "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
            "work_paths": [
              "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
            ]
          }
        ],
        "first_review_commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
        "first_work_commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
        "in_scope": 3,
        "out_of_scope": []
      },
      "id": "P2",
      "status": "PASS",
      "title": "Rule 15 commit order"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
      "evidence": {
        "declared": [
          "DECISION_LOG.md"
        ],
        "declared_by_specification": [
          "DECISION_LOG.md"
        ],
        "declared_key": "append_only",
        "declared_source": "specification",
        "paths": [
          {
            "base_bytes": 89541,
            "base_is_byte_prefix_of_head": true,
            "commits_with_deletions": [],
            "deleted_lines_base_to_head": 0,
            "head_bytes": 89541,
            "path": "DECISION_LOG.md",
            "status": "PASS"
          }
        ],
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [
          "DECISION_LOG.md"
        ]
      },
      "id": "P3",
      "status": "PASS",
      "title": "append-only on both measures"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "entries": [
          {
            "branch": "fix/pi-decisions-and-deferred",
            "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "fix/pi-decisions-v2",
            "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-v2",
            "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-and-superseded",
            "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "review/role-model-and-executors",
            "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "gate/p2-land-diquark-line",
            "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          }
        ],
        "register_path": "docs/BRANCHING_POLICY.md"
      },
      "id": "P4",
      "status": "PASS",
      "title": "superseded branches are not merged"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
      "evidence": {
        "merges": []
      },
      "id": "P5",
      "reason": "no merge commit in range",
      "status": "NOT_APPLICABLE",
      "title": "merge parentage against recomputed facts"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
      "evidence": [
        {
          "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
          "matches": [],
          "status": "PASS"
        }
      ],
      "id": "P6",
      "status": "PASS",
      "title": "commit-message hygiene"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
      "evidence": {
        "added_sections": [],
        "authorised_modified": [],
        "declared": [],
        "declared_by_specification": [],
        "declared_key": "authorised_gates",
        "declared_source": "specification",
        "gates_path": "GATES.md",
        "raw_heading_count_base": 14,
        "raw_heading_count_head": 14,
        "removed_sections": [],
        "section_count_base": 14,
        "section_count_head": 14,
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [],
        "unauthorised_changed": []
      },
      "id": "P7",
      "status": "PASS",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
        "first_commit_paths": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ]
      },
      "id": "P8",
      "status": "PASS",
      "title": "Rule 15 placement and specification-first"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {},
      "id": "P9",
      "reason": "range adds no report",
      "status": "NOT_APPLICABLE",
      "title": "reports carry a Stops and clarifications section"
    }
  ],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "commits_in_scope": 3,
    "commits_out_of_scope": [],
    "inclusivity": "INCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```

### RUN 2 EXCLUSIVE config, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "specification_paths": ["specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"],
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "EXCLUSIVE"},
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 EXCLUSIVE output, verbatim

```json
{
  "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
  "commits_in_range": 3,
  "commits_on_first_parent_line": 3,
  "head": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
  "overall": "PASS",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "append_only": [
            "DECISION_LOG.md"
          ],
          "authorised_gates": [],
          "counted": 4,
          "counted_add": 4,
          "counted_modify": 0,
          "counted_set": [
            "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
            "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
            "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
          ],
          "parse": "OK",
          "path": "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
          "stated": 4,
          "stated_add": 4,
          "stated_modify": 0,
          "stated_record": "stated: 4 additions, 0 modifications"
        }
      ],
      "id": "P1",
      "status": "PASS",
      "title": "scope manifest arithmetic"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "commits": [
          {
            "adds_review": false,
            "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
            "work_paths": [
              "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
            ]
          }
        ],
        "first_review_commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
        "first_work_commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
        "in_scope": 3,
        "out_of_scope": []
      },
      "id": "P2",
      "status": "PASS",
      "title": "Rule 15 commit order"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
      "evidence": {
        "declared": [
          "DECISION_LOG.md"
        ],
        "declared_by_specification": [
          "DECISION_LOG.md"
        ],
        "declared_key": "append_only",
        "declared_source": "specification",
        "paths": [
          {
            "base_bytes": 89541,
            "base_is_byte_prefix_of_head": true,
            "commits_with_deletions": [],
            "deleted_lines_base_to_head": 0,
            "head_bytes": 89541,
            "path": "DECISION_LOG.md",
            "status": "PASS"
          }
        ],
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [
          "DECISION_LOG.md"
        ]
      },
      "id": "P3",
      "status": "PASS",
      "title": "append-only on both measures"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "entries": [
          {
            "branch": "fix/pi-decisions-and-deferred",
            "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "fix/pi-decisions-v2",
            "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-v2",
            "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "governance/supply-protocol-and-superseded",
            "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "review/role-model-and-executors",
            "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          },
          {
            "branch": "gate/p2-land-diquark-line",
            "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
            "is_ancestor_of_head": false,
            "object_present": true,
            "status": "PASS"
          }
        ],
        "register_path": "docs/BRANCHING_POLICY.md"
      },
      "id": "P4",
      "status": "PASS",
      "title": "superseded branches are not merged"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
      "evidence": {
        "merges": []
      },
      "id": "P5",
      "reason": "no merge commit in range",
      "status": "NOT_APPLICABLE",
      "title": "merge parentage against recomputed facts"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
      "evidence": [
        {
          "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
          "matches": [],
          "status": "PASS"
        }
      ],
      "id": "P6",
      "status": "PASS",
      "title": "commit-message hygiene"
    },
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
      "evidence": {
        "added_sections": [],
        "authorised_modified": [],
        "declared": [],
        "declared_by_specification": [],
        "declared_key": "authorised_gates",
        "declared_source": "specification",
        "gates_path": "GATES.md",
        "raw_heading_count_base": 14,
        "raw_heading_count_head": 14,
        "removed_sections": [],
        "section_count_base": 14,
        "section_count_head": 14,
        "specification_paths_read": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "supplied_by_config": [],
        "unauthorised_changed": []
      },
      "id": "P7",
      "status": "PASS",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
        "first_commit_paths": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
        ]
      },
      "id": "P8",
      "status": "PASS",
      "title": "Rule 15 placement and specification-first"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {},
      "id": "P9",
      "reason": "range adds no report",
      "status": "NOT_APPLICABLE",
      "title": "reports carry a Stops and clarifications section"
    }
  ],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "commits_in_scope": 3,
    "commits_out_of_scope": [],
    "inclusivity": "EXCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```

## 12. A14 — validators at commit 3

After the environment restoration in §2, the specified full suite exited 0:

    324 passed, 2 deselected in 112.33s

This is the expected count. The repaired
`tests/test_gate_pins.py::test_a_stale_pin_is_detected` passed.

A non-governing `ruff check --no-cache .` diagnostic found 13 pre-existing
lint findings in existing scripts/tests. This task changed none of those
paths; the specification's validator criterion is the pytest count above.

## 13. A15 — chronology and commit-message hygiene

MEASURED commits 1–3 and stored messages:

    5d76e4026df421d41b385062b4b0dbaa203e6227
    spec: add D-1 literature coverage audit execution 3

    37d1a7e719f4016de61ace3756fd8a0c2105cf1f
    review: approve D-1 literature coverage audit execution 3

    86e2710ca3f04715519bd82b2fd8cac21274a75e
    derivation: audit D-1 reflection-positivity literature coverage

P6 reports `PASS` for all three: no prohibited trailer or URL in any message.
Rule 15 order is spec, review, work. The INTENDED commit-4 message is:

    report: record D-1 literature coverage audit execution 3

Final commit-4 hygiene is post-report evidence and is not claimed here.

## 14. Stops and clarifications

Primary stops: none.

- `SPECIFICATION_DEFECT`: none.
- `ENVIRONMENT`: no unresolved stop. The inaccessible inherited pytest temp
  directory was diagnosed and restored as described in §2.
- `OBSERVATION_METHOD_ERROR`: none unresolved. Search snippets were excluded
  from evidence; every scientific statement is labeled by actual fetch depth.
- `REPOSITORY_DEFECT`: no task-stopping defect. The optional ruff diagnostic's
  13 pre-existing findings are a separate, non-governing repository condition.
- `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`: none.

Secondary findings: publisher/DOI access remained host-dependent; OS78 and
STW81 were consequently limited to abstract depth. This did not block the
audit because full-text, load-bearing alternatives were available and no
`COVERED` verdict rests on either abstract.
