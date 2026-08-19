# Execution report — integrate the spin-channel scope assessment, and land it

**Task:** `science/integrate-channel-b0`
**Specification:** `specs/2026-08-19T0138Z_integrate-channel-b0.md`
**Review:** `reviews/chatgpt/2026-08-19T0138Z_integrate-channel-b0.md`
**Declared evidence base:** `7ae371994a8bb940e6f6d6b9c9868c96adcfaca9`
**Source branch:** `science/channel-b0-spin-scope @ 8c27a606643ef315d11e1a1dad8875aa2f1029b1`

**Measurement head for everything in this report: commit 3,
`012f14af4abb2415aad606010e40584bd58eb10b`.** Nothing here claims to
measure commit 4. Commit 4 is this file, and every figure that depends on
it is labelled **INTENDED**. The post-report layer — A12 final, A17-final,
A15 and A16 after the advance, A19 for commit 4, the push, the remote
read-back, final ancestry — is returned to the Reviewer in chat and is
**not** written into this file.

---

## 0. Execution order

Criterion numbering is not execution order. The normative order was run:
**A3 environment first**, then **A1 refs**, then **A2 review binding**,
then A4 onward. §4's own text requires this of A3 ("run FIRST") and §8
repeats it.

---

## A3 — Environment conformance, run FIRST (MEASURED)

**Amendment D step 0 — execution location, worktree identity, resolved
HEAD.**

    execution location   /tmp/claude-0/-home-user-2-emergent-gravity/
                         30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/ichb0
    worktree identity    linked worktree of /home/user/2-emergent-gravity
                         (.git is a 59-byte gitdir pointer file, not a directory)
    resolved HEAD        012f14af4abb2415aad606010e40584bd58eb10b

**Rule 13's diagnostic order.**

    shallow clone?            no
    commits reachable, HEAD   423
    commits, all refs         547
    Python                    3.11.15
    pytest                    9.1.1
    numpy                     2.4.6
    sympy                     1.14.0
    ruff                      0.15.8
    scipy                     ABSENT

**`scipy` is absent for the twelfth consecutive task**, while
`pyproject.toml:12` declares `scipy>=1.11`. No validator in this
repository imports it, so nothing fails; the declaration and the
environment simply disagree, and they have disagreed across every task in
this line. Recorded, not repaired — §3 forbids modifying any file.

**`docs/local/execution_environment.md` continues to declare a Windows
environment** (`zeta-3070\codexsandboxoffline`, Python 3.12,
`C:\p2-validator\venv`). That environment has never been the one
executing. Recorded, not repaired.

**Rule 13 carries two diagnostic orders — a known open item.** **No
environment failure occurred in this task, so neither order was
exercised** as a failure path. I do not name one as the operative order.

---

## A1 — Repository and refs (MEASURED)

**`origin` remote URL, verbatim, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

**After `git fetch origin`, pasted from `git rev-parse`:**

    refs/remotes/origin/main   7ae371994a8bb940e6f6d6b9c9868c96adcfaca9
    declared base              7ae371994a8bb940e6f6d6b9c9868c96adcfaca9

**Equal. `main` has not advanced beyond the declared base. No stop.**

**Source tip, pasted from `git rev-parse`:**

    refs/remotes/origin/science/channel-b0-spin-scope
      8c27a606643ef315d11e1a1dad8875aa2f1029b1

Confirmed three ways — the remote-tracking ref, the local branch, and
`git rev-parse 8c27a606^{commit}` — all resolving to
`8c27a606643ef315d11e1a1dad8875aa2f1029b1`. It matches the specification.

    git merge-base --is-ancestor 8c27a606 origin/main   exit 1

**Not an ancestor of `main`.** The merge is real work, not a no-op.

**`EPS-B0` ancestry on this base** (A9's confirmation, measured here
because it is a ref fact):

    git merge-base --is-ancestor efb8d63f origin/main   exit 0
    git cat-file -e origin/main:derivations/
      P2-EPS-B0_epsilon-tractability-scope.md            exit 0

**`EPS-B0` is on this task's evidence base**, both as an ancestor commit
and as a present artifact path. The substitution recorded in §10 was
performed correctly.

---

## A2 — Review committed, unedited, SHA bound (MEASURED)

**Field presence checked before value.** The committed review carries the
literal string `Reviewed specification SHA-256:` — present, one
occurrence, populated with a 64-hex value rather than a placeholder.

    sha256(specification, as committed)
      6e48206f72ebaf23e149b76c0b9505f1a0c76dcc3cd55219ebcd2fc6e0cd10ed
    review's bound SHA
      6e48206f72ebaf23e149b76c0b9505f1a0c76dcc3cd55219ebcd2fc6e0cd10ed

**MATCH.** The review's approval is bound to exactly these specification
bytes. Verdict `APPROVE FOR EXECUTION`. Committed unedited as commit 2.

---

## A4 — Merge parentage, three separately derived measurements (MEASURED)

Each value derived by its own command, not read off one listing:

    parent 1   git rev-parse 012f14af^1   5eca61dca0d1f83f611e65eadb2812a00c1ba9c3
    parent 2   git rev-parse 012f14af^2   8c27a606643ef315d11e1a1dad8875aa2f1029b1
    merge-base git merge-base 5eca61dc 8c27a606
                                          af145d5a3e36e6bca62f038092748ada3abdcec1

    git merge-base --is-ancestor 222d8620 5eca61dc   exit 0

**Commit 1 is an ancestor of parent 1.** Parent 2 is the source tip
exactly. Parentage is as specified.

---

## A5 — Conflict measurement, fresh at THIS base (MEASURED)

**§0's header recorded a dry run against `af145d5a`, a different base.
That result was not carried.** Re-measured at this base:

    git merge-tree --write-tree 5eca61dc 8c27a606
      exit 0
      tree ff23783274e2b5ba20405aced62084184a0663c2
      conflict list: EMPTY (zero lines)

    the merge itself
      exit 0
      git ls-files --unmerged | grep -c ''   0

**The conflict list is empty.** Zero unmerged paths after the merge.

---

## A6 — The six separation passages, re-read at the head (MEASURED)

Quoted verbatim from `paper/emergent_gr_paper_v2_15.tex` at commit 3.

**`:95-96`**

> verify this by explicit one-loop lattice computations in both the
> scalar channel and the graviton (stress-tensor) channel.

**`:574-576`**

> The light degrees of freedom of the theory are exclusively the
> collective bosonic modes: the angular condensate mode below, and
> the induced graviton of Section~\ref{sec:induced}.

**`:787-788`**

> so that the only possible massless pole resides in the TT spin-2
> channel.

**`:810-814`**

> A lattice measurement of the Barnes--Rivers--projected
> stress-tensor correlator, checking for a single $p^2 = 0$ pole in
> the spin-2 sector with vanishing spin-1/0 residues, is the decisive
> test; we identify it as the key numerical milestone for this
> programme.

**`:816-833`** — the universality subsection. Its first sentence scopes
itself to `eq:PiTT`:

> \subsection{Emergent gauge redundancy and universal coupling}
>
> Up to $\mathcal{O}(p^2/\Lambda^2)$ corrections, the quadratic
> action defined by Eq.~\eqref{eq:PiTT} is the Fierz--Pauli action,
> invariant under linearized diffeomorphisms
> $h_{\mu\nu} \to h_{\mu\nu} + \partial_\mu\xi_\nu
> + \partial_\nu\xi_\mu$ \cite{Fierz:1939ix}.
> This gauge redundancy is not imposed; it emerges from the infrared
> Ward identity.
> Gauge invariance of the linear matter coupling
> $\int h_{\mu\nu}X^{\mu\nu}$ requires
> $\partial_\mu X^{\mu\nu} = 0$, and in a local infrared effective
> theory the unique conserved symmetric tensor (up to improvements)
> is the energy-momentum tensor.
> Hence all matter couples as
> $\kappa\int d^4x\,h_{\mu\nu}T^{\mu\nu}$ with a common $\kappa$:
> the equivalence principle is an emergent consequence of the
> infrared gauge structure.

**It never mentions `θ̃`.**

**`:1531-1534`**

> Ref.~\cite{Cheng:2025sparc}, the lattice fermion framework
> produces both gravitational dynamics (induced sector) and
> ultralight dark-matter phenomenology (angular condensate mode)
> from the same microscopic Lagrangian~\eqref{eq:L0}.

**The verdict rests on these six passages, which state the separation in
the manuscript's own vocabulary.** Re-measured at the head:

    spin-0        0
    fifth force   0
    spin-1/0      1
    spin-2       11

**`spin-0` returns zero and `fifth force` returns zero, and NEITHER
ABSENCE WAS USED AS EVIDENCE.** An absent word establishes nothing about
a document; had the verdict rested on those two zeros it would have been
an argument from silence, and the source executor did not make it.

**`spin-1/0` returns one line, and that line decided the verdict.** It is
`:812`, inside the decisive-test sentence — the separation is stated
there as a *test criterion*: a single pole in the spin-2 sector *with
vanishing spin-1/0 residues*. A document that proposes measuring whether
the spin-1 and spin-0 residues vanish is a document that treats those
channels as distinct from the spin-2 channel.

**The specification's word list was wrong, and the specification said so
in advance.** `CHANNEL-B0` §3 stated that a separation expressed in other
terms would still be `CHANNELS SEPARATED` and the word list would be the
defect. The executor added `spin-1/0`, a term the list did not contain,
and that added term is what returned the line. Recorded because it is the
governing fact about how the verdict was reached: **the verdict came from
reading the argument, and an added search term — not the specified one —
is what surfaced the decisive line.**

---

## A7 — Object dependence, and the near-miss (MEASURED)

Six terms, case-insensitive, over the manuscript at commit 3:

    composition-dependent    0
    baryon number            0
    charge-to-mass           0
    Eötvös                   0
    test body                0
    torsion balance          0

**All six zero.** For completeness against an encoding hazard, `eotvos`
without the diacritic also returns **0**, so the zero is not an artifact
of the accented character failing to match.

**The near-miss.** Bare `composition` returns **5 lines**, and **all 5
are `decomposition`** — 5 of 5, measured by re-filtering the same five
lines. **Counting the bare-substring hits would have returned
`NON-UNIVERSAL`**, on a substring, with no composition dependence
anywhere in the document. It is the most consequential false positive
available in that task, and it was caught by inspecting the matched lines
rather than the count.

**`:634` says the coupling is to "visible (baryonic) matter".** That
names a **target**, not a charge law. A statement that a field couples to
baryonic matter does not say whether the coupling strength per unit mass
varies between a beryllium body and a titanium body — which is the
question universality asks.

**Verdict: `θ̃`'s universality is `UNSTATED`.** Not `NON-UNIVERSAL`.
Suppression by `ε` and by a mixing angle is a statement about
**magnitude**; it says nothing about whether the scalar charge varies
across bodies. The manuscript does not assert universal coupling for the
angular mode and does not assert composition dependence for it. **The
silence is the finding.**

---

## A8 — The equivalence principle: four-state status and four limits (MEASURED)

**Status: `DERIVED HERE`** — for the **spin-2 channel**, at the level of
the **linear coupling**.

`:825-831`, quoted:

> Gauge invariance of the linear matter coupling
> $\int h_{\mu\nu}X^{\mu\nu}$ requires
> $\partial_\mu X^{\mu\nu} = 0$, and in a local infrared effective
> theory the unique conserved symmetric tensor (up to improvements)
> is the energy-momentum tensor.
> Hence all matter couples as
> $\kappa\int d^4x\,h_{\mu\nu}T^{\mu\nu}$ with a common $\kappa$:

**Not merely `CLAIMED`:** the passage gives premises and a *Hence*. The
word "consequence" at `:832` is backed by the two sentences before it.

**Not `DERIVED ELSEWHERE AND CITED`:** the only citation in the
subsection is Fierz, and it is cited for the *form of the action*, not
for the universality conclusion.

**Not `TESTED`:** `Eötvös` 0, `test body` 0, `torsion balance` 0, and no
composition-dependence analysis anywhere in the repository.

**The four limits the source recorded, carried here rather than glossed:**

1. **It is four lines long.**
2. **It holds only "up to `O(p²/Λ²)` corrections"**, per `:818`.
3. **Its uniqueness premise is asserted, not proved here** — "in a local
   infrared effective theory … (up to improvements)" at `:827-829`.
4. **It is a statement at the level of the LINEAR coupling.**

**`DERIVED HERE` is the correct state of the four, and it is not the same
as established.** A landing that carried the label without the limits
would misrepresent it, which is why the limits are here and not in a
footnote.

---

## A9 — §1c carried verbatim, and the EPS-B0 relation (MEASURED)

Carried verbatim, as §1c requires:

> **Channel separation does not establish parameter independence.** The
> spin-0 and spin-2 observables may be conceptually distinct while the
> scalar channel's strength remains dependent on unresolved microscopic
> data through `ε`.

**`EPS-B0` is an ancestor of this task's base** — `efb8d63f`,
`--is-ancestor` **exit 0**, artifact present, both measured under A1.

**The relation, now that it may be stated.** The `CHANNEL-B0` executor
could not cite `EPS-B0`: it was absent from that task's base, and the
executor correctly did not reach for it. It is on this base, so it is
**landed evidence** here rather than a reporting constraint.

Landed `EPS-B0` verdict: **`BLOCKED PENDING A RULING`** — `ε`'s
computation depends on `R1`, an open node, and `EPS-B0`'s own rider
records that **no number follows even after `R1` is ruled**, because the
manuscript states `ε`'s magnitude as one "the dedicated computation left
open" (`:541-544`) and fixes `ε` by the observation-inward route
`SPARC → r_c → m_θ → ε` rather than from the microscopic theory.

**So both hold at once, and neither weakens the other:** the channels are
**separated**, and the scalar channel's **strength waits on an open
node**. Conceptual distinctness and parametric dependence are different
properties. This is the relation §1c names, now with an evidence base
under it.

**It changes nothing about universality.** `EPS-B0` speaks to strength
and closure. `UNSTATED` is a classification about whether the manuscript
states a charge law. Suppression by `ε`, dependence on unresolved
microscopic parameters, and failure to obtain a numerical coupling do
**not** establish composition dependence, and therefore do not license
`NON-UNIVERSAL`.

---

## A10 — The unexecuted milestone (MEASURED)

`:810-814` names the programme's **key numerical milestone**: a lattice
measurement of the Barnes–Rivers–projected stress-tensor correlator,
checking for a single `p² = 0` pole in the spin-2 sector **with vanishing
spin-1/0 residues**, described by the manuscript as "the decisive test".

**Searched, and reported. Not scoped** — §3 forbids performing,
designing, or scoping it, and this section does none of the three.

**`scripts/recovered_2026/tt_check.py`** is the nearest thing in the
repository. It **builds all four Barnes–Rivers projectors** and projects
the one-loop kernel onto the spin sectors, returning `g2, g1, g0s, g0w`
at `:135`. **It computes no pole and no residue:** a search of that file
for `pole`, `residue`, `nonperturb` and `milestone` returns **no lines at
all** (grep exit 1). Projecting a kernel onto spin channels is a
prerequisite for the milestone; it is not the milestone.

**Repository-wide, outside the manuscript and outside this task's own
governance files**, `spin-1/0` appears in exactly two places: the
`CHANNEL-B0` artifact (which is discussing this very question) and
`results/recovered-2026/emergent_gr_paper_v2_7.tex` (an earlier draft of
the same manuscript). `Barnes` adds only `tt_check.py`. Every `residue`
hit was inspected line by line: `P2-CHANNEL-FREEZE-01:211` and
`GATES.md:1180` are the same sentence about a negative-residue pole in a
different argument; `P2-BETAV-CAMPAIGN_prereg.md:70-73` is floating-point
numerical residue; `speed_check.py:89` is a contour-integration remark;
`PROVENANCE.md:165` is "residue" in the sense of an unresolved
loose end; `P2-FIERZSUM-01:472` lists residue/pole criteria among things
a *future* `P2-VECPOLE-01` would need; and `P2-LATTICE-ROUTE-01:295`
names "finite-volume pole extraction, and residue/overlap study" as work
a cross-check **would require**. **None of them performs the measurement.**

`GATES.md` returns **0** for `Barnes`, **0** for `milestone`, **0** for
`stress-tensor correlator`, and **0** for `spin-1/0` — the milestone is
not gated.

**The manuscript names its own decisive test, designates it the key
numerical milestone for the programme, and no artifact in this repository
performs it.**

The manuscript is itself explicit that this is unsettled: `:805-809`
records that whether the pole exists is "ultimately a nonperturbative
question". The separation of the channels is a statement about the
documents. Whether the spin-2 pole is there, with vanishing spin-1/0
residues, is not yet a measured fact of this programme.

---

## A11 — Nothing derived (MEASURED)

Searched the arriving artifact, the arriving report, and every commit
message in this task's range for three categories: **a statement about
what a channel should couple to**, **a computed magnitude**, and **a
claim that the equivalence principle holds**.

**Result, stated positionally rather than as a count.** Outside the
passages that exist precisely to record the search — the source report's
own §9.3 accounting table and the sentences describing it — **no line in
the artifact or the report makes any of the three statements**, and no
commit message in the range does either.

I state it this way deliberately. A report that must name its search
patterns necessarily matches them, so a raw count is guaranteed non-zero
and means nothing. `DET-01`'s A10 was reported as a count and produced
exactly that artefact; this section avoids repeating it.

Every hit was inspected. The artifact's one hit is `:122` — *"That names
what the mode couples to. It does not give a charge law"* — a **negation**
of the category, not an instance of it. The report's hits are its own
§9.3 table row and the two sentences that describe what that row measured.
The two commit-message hits on `universal` are the subject lines *"the
channels are separated and the universality claim is spin-2 only"*, which
scope a claim; they do not derive one.

**Nothing was derived in this task.** No coupling, no magnitude, no
charge law, and no assertion that the equivalence principle holds.

---

## A12 — Scope, measured against the frozen manifest (MEASURED, plus one INTENDED)

Measured fresh against base `7ae37199…`; not carried from the
specification.

**Cumulative, per commit:**

    commit 1  222d8620   1 path
      A  specs/2026-08-19T0138Z_integrate-channel-b0.md

    commit 2  5eca61dc   2 paths
      A  reviews/chatgpt/2026-08-19T0138Z_integrate-channel-b0.md
      A  specs/2026-08-19T0138Z_integrate-channel-b0.md

    commit 3  012f14af   6 paths
      A  derivations/P2-CHANNEL-B0_spin-channel-scope.md
      A  reports/2026-08-18T2219Z_channel-b0-spin-scope.md
      A  reviews/chatgpt/2026-08-18T2219Z_channel-b0-spin-scope.md
      A  reviews/chatgpt/2026-08-19T0138Z_integrate-channel-b0.md
      A  specs/2026-08-18T2219Z_channel-b0-spin-scope.md
      A  specs/2026-08-19T0138Z_integrate-channel-b0.md

    commit 4             7 paths          INTENDED
      the six above plus
         reports/2026-08-19T0138Z_integrate-channel-b0.md

**The source's contribution, measured separately** — `af145d5a…` to
`8c27a606…`:

    A  derivations/P2-CHANNEL-B0_spin-channel-scope.md
    A  reports/2026-08-18T2219Z_channel-b0-spin-scope.md
    A  reviews/chatgpt/2026-08-18T2219Z_channel-b0-spin-scope.md
    A  specs/2026-08-18T2219Z_channel-b0-spin-scope.md

    4 additions, 0 modifications

**Measured 1, 2, 6 cumulative and 4 contributed. The manifest states 7
additions and 0 modifications overall, with 1, 2, 6, 7 expected. Every
measured figure agrees. No stop.** The seventh path is this file and is
labelled INTENDED because commit 4 does not exist at the measurement head.

**Every status letter is `A`. Zero modifications, and none of the
forbidden operations** — delete, rename, copy, type change, unmerged,
unknown — **appears at any of the three commits.**

**The UTC time was measured, not assumed:** `2026-08-19T01:38:12Z`,
giving the token `0138Z` used in every path above.

**`append_only: DECISION_LOG.md` was treated as a checker-configuration
declaration and NOT as an authorisation to write that file.**
`DECISION_LOG.md` is unchanged at 89541 bytes at both ends — see A17's P3
evidence, which measures it independently.

---

## A13 — Which merge case (MEASURED)

**Reported separately, and not conflated:**

    merge-base       af145d5a3e36e6bca62f038092748ada3abdcec1
    evidence base    7ae371994a8bb940e6f6d6b9c9868c96adcfaca9

**They are NOT equal.** This is the first integration in this line where
they differ. The source branched from `af145d5a…`; `EPS-B0` then landed
and advanced `main` to `7ae37199…`, so this task's base is strictly later
than the merge-base.

**Eight commits lie between the merge-base and the evidence base** — the
whole `EPS-B0` scope task and its integration. **None of them touched an
arriving path**, and **all four arriving paths are ABSENT at the evidence
base**, so there is nothing for the merge to reconcile on those paths.
That is why A5's conflict list is empty despite the divergent bases.

**The four blob comparisons, source tip against merge result:**

    derivations/P2-CHANNEL-B0_spin-channel-scope.md   633973b64973…  IDENTICAL
    reports/2026-08-18T2219Z_channel-b0-spin-scope.md f21ab0fe579c…  IDENTICAL
    reviews/chatgpt/2026-08-18T2219Z_…-spin-scope.md  2da5a1fddef6…  IDENTICAL
    specs/2026-08-18T2219Z_channel-b0-spin-scope.md   9acfd6cd6882…  IDENTICAL

**All four identical.** The merge transported the source's bytes
unaltered; the later base changed nothing about what arrived.

---

## A14 — Nothing existing changed (MEASURED)

    paths in the base tree, compared          512
    paths differing base → head that existed
      at the base                               0

    paper/emergent_gr_paper_v2_15.tex
      blob at 7ae37199   c8246f890b07f53ab8094981cbd5a02972fda4c1
      blob at 012f14af   c8246f890b07f53ab8094981cbd5a02972fda4c1

**Identical blob id at both ends.** The manuscript under verification was
not touched — which is the point of the whole exercise: the verification
line reads the manuscript and never edits it.

The full base-to-head diff contains **six** entries and **every one is an
addition**; zero entries are modifications or deletions. Confirmed
individually for `GATES.md`, `CONVENTIONS.md`, the `EPS-B0` artifact
(`2b3e513424d4266e5f741903594cf23e93131c1f` at both ends), the two
`scripts/recon2026/` files, `tests/test_recon2026_flat_limit.py`, both
registers, and the entire `results/` subtree — all blob-identical.

**`derivations/P2-*` re-measured, not carried: 50 at the base, 51 at the
head.** The one added file is `P2-CHANNEL-B0_spin-channel-scope.md`, the
arriving artifact. Nothing else in that directory moved.

---

## A15 — Gate invariants and pins, read SCOPED (MEASURED)

Read at commit 3, scoped to `^## P2-` headings rather than to any
substring:

    ^## P2- count                14
    P2-PHASE-01 Status           PROPOSED
    prerequisite 1               SATISFIED
    prerequisite 2               SATISFIED
    both pins                    recomputed and matching

**All four invariants hold.** The pins were recomputed from the pinned
content, not read back from the stored value.

---

## A16 — Superseded branches not merged (MEASURED, before the advance)

    52f65117   exit 1
    ebd531ab   exit 1
    40168469   exit 1
    7146a093   exit 1
    10c260b9   exit 1
    d64cd912   exit 1

**Six separate `git merge-base --is-ancestor` invocations, six exit
statuses, all 1. None of the six superseded branches is an ancestor of
commit 3.** The after-the-advance re-run belongs to the post-report
layer and is returned in chat.

---

## A17 — The checker over this task's own range (MEASURED)

Invoked as `python3 -m scripts.governance_tools.task_checker --repo .
--config <json>`, base as declared, **head commit 3**, four invocations
(two runs × two prospectivity readings). **All four exited 0.**

**The output was PARSED, not grepped.** This matters and is not a
formality: the property list is a **JSON array of objects** with keys
`id`, `status`, `classification`, `evidence` — so a dictionary lookup by
property name returns `None`, and a grep for `PASS` counts the word where
it occurs inside the `does_not_establish` prose. Every figure below comes
from `json.load` and indexing into the parsed structure.

### RUN 1 config, verbatim (INCLUSIVE; the EXCLUSIVE config differs only in that field)

```json
{
  "base": "7ae371994a8bb940e6f6d6b9c9868c96adcfaca9",
  "head": "012f14af4abb2415aad606010e40584bd58eb10b",
  "append_only_paths": [
    "DECISION_LOG.md"
  ],
  "authorised_modified_gates": [],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "inclusivity": "INCLUSIVE"
  },
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 config, verbatim (INCLUSIVE; the EXCLUSIVE config differs only in that field)

```json
{
  "base": "7ae371994a8bb940e6f6d6b9c9868c96adcfaca9",
  "head": "012f14af4abb2415aad606010e40584bd58eb10b",
  "specification_paths": [
    "specs/2026-08-19T0138Z_integrate-channel-b0.md"
  ],
  "append_only_paths": [
    "DECISION_LOG.md"
  ],
  "authorised_modified_gates": [],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "inclusivity": "INCLUSIVE"
  },
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### Parsed results — identical across all four invocations

    overall            PASS
    properties         9   (a JSON array, length 9)
    PASS count         9
    NON_GREEN values   none
      (no NOT_DECLARED, no NOT_PARSEABLE, no DECLARATION_CONFLICT
       anywhere in any of the four documents)

    P1 PASS  PARTIAL     scope manifest arithmetic
    P2 PASS  MECHANICAL
    P3 PASS  PARTIAL     append-only on both measures
    P4 PASS  MECHANICAL
    P5 PASS  PARTIAL
    P6 PASS  PARTIAL
    P7 PASS  PARTIAL     gate integrity
    P8 PASS  MECHANICAL
    P9 PASS  MECHANICAL  reports carry a Stops and clarifications section

    commits_in_range                7
    commits_on_first_parent_line    3
    prospectivity commits_in_scope  3
    prospectivity out_of_scope      []   (empty)

**`PASS` is 9, not zero. No stop on that ground.** The stop condition
"`PASS` at zero" was checked by counting parsed `status` fields, which is
the only way to check it that means anything.

`overall_note`, verbatim from the output:

> INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE
> mean a subject was missing, and a missing subject must never read as a
> pass.

### `declared_source` — reported as measured, which is not per-property

**The specification asks for `declared_source` for each property.
Measured across all four outputs, `declared_source` is not a
per-property field at all.** It occurs **exactly twice** in each
document, and in both cases nested inside `evidence`:

    /properties[2]/evidence/declared_source  =  "specification"      (P3)
    /properties[6]/evidence/declared_source  =  "specification"      (P7)

**The other seven properties have no `declared_source` key**, at any
depth. P3 and P7 are the two properties that consume a caller-supplied
declared set — `append_only` and `authorised_gates` respectively — so
they are the only two for which the question "where did the declaration
come from" has a subject. **For both, the answer is `specification`:**
the checker read the declaration out of the specification file and it
agreed with the config.

I report the field as it exists rather than manufacturing a value for the
seven properties that do not carry one.

### P3 evidence — the declaration agreed from both directions

    declared_key                 append_only
    declared                     ["DECISION_LOG.md"]
    declared_by_specification    ["DECISION_LOG.md"]
    supplied_by_config           ["DECISION_LOG.md"]
    declared_source              specification

    DECISION_LOG.md
      base_bytes                    89541
      head_bytes                    89541
      base_is_byte_prefix_of_head   true
      deleted_lines_base_to_head    0
      commits_with_deletions        []
      status                        PASS

**Both measures.** The file is byte-identical and the base is a byte
prefix of the head — append-only is satisfied vacuously, because nothing
was appended. This is the independent confirmation that
`append_only: DECISION_LOG.md` was not read as a licence to write.

### P7 evidence — the section count

    gates_path                GATES.md
    section_count_base        14
    section_count_head        14
    raw_heading_count_base    14
    raw_heading_count_head    14
    added_sections            []
    removed_sections          []
    authorised_modified       []
    unauthorised_changed      []
    declared                  []
    declared_by_specification []
    supplied_by_config        []
    declared_source           specification

**`P7` reports fourteen sections**, as required — and reports fourteen at
**both** ends, with the raw heading count agreeing with the scoped
section count, so the fourteen is not an artefact of a lenient heading
match. **`unauthorised_changed` is empty against an empty authorised
set**, which is the strict reading: nothing may change, and nothing did.

### P9 evidence

    reports/2026-08-18T2219Z_channel-b0-spin-scope.md
      heading_present   true
      status            PASS

The one report arriving in this range carries its **Stops and
clarifications** section. This file carries one too, but this file is
commit 4 and is outside the measured range by construction.

### What RUN 1 did

**RUN 1 is observational: it names no specification and lets the checker
discover every specification in the range.** It discovered **two**, and
this is the whole reason both runs are required.

    RUN 1, P1 evidence — 2 blocks

      specs/2026-08-18T2219Z_channel-b0-spin-scope.md
        parse OK   stated 4   counted 4
        "stated: 4 additions, 0 modifications"
        counted_set:
          derivations/P2-CHANNEL-B0_spin-channel-scope.md
          reports/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
          reviews/chatgpt/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
          specs/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md

      specs/2026-08-19T0138Z_integrate-channel-b0.md
        parse OK   stated 7   counted 7
        "stated: 7 additions, 0 modifications"
        counted_set:  the seven paths of §4's manifest

    RUN 2, P1 evidence — 1 block
      specs/2026-08-19T0138Z_integrate-channel-b0.md only

**Two specifications are simultaneously in range, declaring different
totals — 4 and 7 — and no `DECLARATION_CONFLICT` is raised.**

This is the **C3 multi-specification residual**, and it is **unregistered**.
`_declarations_from_specs` compares `append_only_paths` and
`authorised_modified_gates` across the specifications it finds; it does
**not** compare the stated scope totals. Both specifications declare the
same append-only path and the same empty gate set, so the comparison the
checker performs finds nothing to disagree about, and the disagreement it
does not perform — 4 against 7 — passes unnoticed.

The arithmetic is individually correct in both cases: each specification's
stated total matches the set of paths its own manifest block enumerates,
which is exactly what `P1`'s `does_not_establish` says it checks and no
more. Nothing is wrong here. What is unregistered is that a reader seeing
`P1 PASS` under RUN 1 might take it as a statement about *the range's*
scope, when it is two independent per-specification statements.

**This is the seventh independent range in which the residual has been
observed, and the fourth with genuinely differing declarations.** I record
it again rather than treating repetition as registration. **I did not
adjust the config or the specification's declarations to make RUN 2 pass**
— §8 forbids it, and RUN 2 passed as issued.

**RUN 2 is stop-governing.** RUN 2 named only this task's specification,
returned `overall: PASS` with nine `PASS` properties and no `NON_GREEN`
value, under both prospectivity readings. **No stop.**

### The two prospectivity readings

    RUN 1  INCLUSIVE vs EXCLUSIVE   differ at exactly one line (314):
                                    the "inclusivity" field itself
    RUN 2  INCLUSIVE vs EXCLUSIVE   differ at exactly one line (291):
                                    the "inclusivity" field itself

**The reading does not change any verdict.** `commits_in_scope` is 3 and
`commits_out_of_scope` is empty under both — every commit in this task's
first-parent line is on the far side of the `ce86b534…` boundary either
way, so the boundary's inclusivity has nothing to decide. The scope note,
verbatim:

> P2, P5, P8 and P9 walk the task's own first-parent line; commits
> arriving by merge were governed by the task that made them.

That is why `commits_in_range` is 7 while
`commits_on_first_parent_line` is 3: four commits arrived by the merge
and were governed by `CHANNEL-B0`, not by this task.

---

## A18 — Validators (MEASURED)

At commit 3:

    332 passed, 2 deselected in 39.46s
    exit status 0

**Matches the expected 332 passed, 2 deselected.**

---

## A19 — Commit-message hygiene, commits 1–3 (MEASURED)

**Rule 20 binds this task.** Measured on the message body alone
(`git log -1 --format='%B'`), with the author/committer identity reported
separately so that the identity's `noreply@anthropic.com` is not confused
with a message-body trailer.

    commit 1  222d8620  "spec: integrate and land the spin-channel scope assessment"
              body 2 lines, 60 bytes
    commit 2  5eca61dc  "review: pre-execution review for the spin-channel integration"
              body 2 lines, 63 bytes
    commit 3  012f14af  "merge: integrate the spin-channel scope assessment"
              body 2 lines, 52 bytes

    Per commit, in the message body, case-insensitive:
      Co-Authored-By    0
      claude.ai         0
      Generated with    0
      Claude Code       0
      Claude            0
      opus              0
      sonnet            0
      Claude-Session    0
      anthropic         0
      http              0

**All zero on all three.** No co-author trailer, no session URL, no
"Generated with" line, no model identifier of any kind.

The git identity is `Claude <noreply@anthropic.com>` for author and
committer on all three commits. That is the configured repository
identity, not message content; **no hygiene repair was needed and none
was performed**, so Rule 20's narrow permission to rewrite a message
before pushing was not exercised.

**Commit 4's intended message:**

    report: the channels are separated and the universality claim is spin-2 only

A19 for commit 4 belongs to the post-report layer and is returned in chat.

---

## Rule 16 assessment — five junctions, all five

**Rule 16 is operative.**

### First — `CHANNELS SEPARATED` is a finding about the documents

The verdict says the manuscript distinguishes the spin-2 TT sector from
the scalar/angular sector clearly and consistently, in six places, in its
own vocabulary. **It does not establish that the separation is physically
correct**, and **it does not establish that either channel behaves as
claimed.** A document can be perfectly clear about a structure that turns
out not to exist. Whether the spin-2 pole is there at all is, by the
manuscript's own `:805-809`, "ultimately a nonperturbative question", and
by `:810-814` it awaits a measurement nobody has made.

### Second — `UNSTATED` is not `UNIVERSAL`, and this is the one a reader will compress

**The manuscript does not say `θ̃` couples universally. It does not say it
couples non-universally either.** Every form of object dependence returns
zero. `:634` names a target — "visible (baryonic) matter" — and a target
is not a charge law.

**The silence is the finding.** It is not a weak version of universality
and it is not evidence of composition dependence. It is the absence of a
statement, and the correct classification of an absent statement is that
it is absent.

**And a substring search on `composition` would have produced the
opposite answer from five instances of `decomposition`.** Five lines
match; five of five are `decomposition`; counting them would have
returned `NON-UNIVERSAL` on a word fragment. The finding survived only
because the matched lines were read rather than counted.

### Third — `DERIVED HERE` carries four limits and applies to the spin-2 channel at linear order

`DERIVED HERE` is the right label of the four available: there is a real
argument at `:825-831` with premises and a *Hence*, not a bare claim; the
only citation is Fierz for the action's form, not for the conclusion; and
nothing tests it.

**It is not a demonstration that the equivalence principle holds in this
theory.** The four limits, restated because this is the junction where
they would otherwise be dropped:

1. the derivation is **four lines long**;
2. it holds **only up to `O(p²/Λ²)` corrections** (`:818`);
3. its uniqueness premise is **asserted, not proved here** — "in a local
   infrared effective theory … (up to improvements)" (`:827-829`);
4. it is a statement at the level of the **linear** coupling.

Nonlinear equivalence-principle validity, scalar-channel universality,
and test-body phenomenology are all outside what this supports.

### Fourth — the programme's own decisive test is unexecuted

`:810-814` names the test and calls it "the decisive test", "the key
numerical milestone for this programme". **No artifact in this repository
performs it.** `tt_check.py` builds the four Barnes–Rivers projectors and
stops there — no pole, no residue. `GATES.md` does not gate it.

**The programme's key numerical milestone, by its own designation, is
unexecuted.** Reported, not scoped.

### Fifth — channel separation does not establish parameter independence

Per §1c, carried verbatim in A9. **`EPS-B0` is now on the base and
establishes that `ε` is blocked pending an open node** (`R1`), with the
rider that no number follows even after that node is ruled.

**So the scalar channel is conceptually distinct and parametrically
dependent at the same time.** Those are not in tension; they are answers
to different questions. Separation is about whether the observables are
distinct. Parameter independence is about whether the strength of one can
be fixed without resolving microscopic data the programme has not
resolved. **The first holds. The second does not.**

---

## Did landing a favourable verdict make me scrutinise it less?

**It is a real risk and it applies here more than in the previous
integrations.** Every prior task in this line landed a verdict that
constrained the manuscript — `NOT DETERMINABLE`, a rider that does not
survive `δ/δg`, `FORM DERIVED / SCALE FITTED`, `BLOCKED PENDING A
RULING`. This one lands `CHANNELS SEPARATED` and `DERIVED HERE`: the
manuscript comes out well. A verification line that checks unfavourable
verdicts hard and favourable ones softly is not a verification line.

**The source executor raised this about its own work and answered it by
producing six independent passages instead of two.** That is the right
kind of answer: it makes the verdict harder to reach, not easier.

**What I did.**

I **re-read all six passages at my own head** rather than accepting the
source's quotations, and quoted them here from the file at commit 3. The
manuscript blob is identical at both ends (A14), so the source could not
have been quoting a different text — but I checked rather than inferring
it from the blob id.

I **re-measured every count myself**: the six object-dependence terms,
the `composition` five and their five-of-five `decomposition` breakdown,
`spin-0`, `fifth force`, `spin-1/0`, `spin-2`. None was carried.

I **tested the load-bearing search for the failure mode that would have
flipped it**. The `decomposition` near-miss is the one that mattered: I
re-ran the filter rather than trusting the source's report of it, because
that single substring is the difference between `UNSTATED` and
`NON-UNIVERSAL`.

I **added the diacritic check** — `eotvos` without the accent, also zero —
because a zero from an encoding failure looks exactly like a zero from an
absent term, and the favourable reading of that zero is the one I wanted.

I **inspected every `residue` hit in the repository line by line** rather
than stopping at "the file list is short". Seven of the eight are about
something else entirely; the eighth names the work as future. Had I
counted files instead of reading lines, A10 could have gone the other
way.

I **read A11's hits instead of counting them**, and reported the result
positionally, because the count is guaranteed non-zero and a non-zero
count reported as a count would have looked like a violation where there
is none.

**And the two places where the scrutiny cut against the favourable
reading, which is the test of whether it was real:**

**The specification's word list was wrong.** `spin-0` and `fifth force`
both return zero. Those two zeros were available as evidence for the
separation and would have been the easy route. They establish nothing —
an absent word is not a finding about a document — and they were not
used. The verdict rests on the six passages and on `spin-1/0`, a term the
specification did not list.

**`DERIVED HERE` is reported with its four limits attached everywhere it
appears**, including in the Rule 16 junction where a summary would
naturally drop them. The label alone reads as a result. The label with
"four lines long, up to `O(p²/Λ²)`, uniqueness asserted not proved,
linear order only" reads as what it is.

**What I did not do.** I did not test the physics. The separation is a
property of the documents; whether the spin-2 pole exists with vanishing
spin-1/0 residues is unmeasured, and A10 says so. This report cannot tell
the Reviewer that the manuscript is right, only that it is clear and that
its own decisive test has not been run.

---

## Stops and clarifications

**`SPECIFICATION_DEFECT`** — none in this specification. One
observation that is not a defect: §4's A17 asks for `declared_source`
"for each" property, and the checker emits that field for only two of the
nine (P3 and P7, the two that consume a caller-supplied declared set).
Reported as measured under A17 rather than treated as a discrepancy,
since the request is satisfiable exactly where the field exists.

**`ENVIRONMENT`** — `scipy` is absent for the twelfth consecutive task
while `pyproject.toml:12` declares `scipy>=1.11`; no validator imports
it, so nothing failed. `docs/local/execution_environment.md` continues to
declare a Windows environment that has never executed this work. Both
recorded, neither repaired — §3 forbids modifying any file. **No
environment failure occurred**, so neither of Rule 13's two diagnostic
orders was exercised as a failure path.

**`OBSERVATION_METHOD_ERROR`** — none newly committed. Two method
hazards were live in this task and both were handled rather than hit:
the `decomposition` substring, which would have inverted A7's verdict if
counted rather than read; and A11's self-referential search, reported
positionally because a report naming its own search patterns necessarily
matches them. `DET-01`'s A10 is the recorded instance of that second
hazard being reported as a count.

**`REPOSITORY_DEFECT`** — the **C3 multi-specification residual remains
unregistered**, now observed in its **seventh** independent range and its
**fourth** with genuinely differing declarations. Two specifications sit
in RUN 1's range declaring totals of 4 and 7; `_declarations_from_specs`
compares `append_only_paths` and `authorised_modified_gates`, not stated
totals, so no `DECLARATION_CONFLICT` is raised and none should be under
the checker's current contract. Recorded again rather than allowed to
become routine.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — none. §8's clause
requiring a stop on an inconsistency between this specification and a
repository rule, or between two of its own instructions, was not
triggered: no such inconsistency was found.

**Two errors of my own, in earlier reports in this line, restated here so
they stay attached to the record rather than fading:** the `m_θ` tilde
count reported as "six of seven" is a count of non-exact lines, not of
tilde-bearing lines — four lines carry `\sim`; and the `Z_M` token occurs
on two lines, not three. Both were reported in the `integrate-eps-b0`
report and neither was repaired, because both arrive by merge and Rule 20
permits only pre-push message repair.

---

## Layering

**Everything above is measured at commit 3,
`012f14af4abb2415aad606010e40584bd58eb10b`**, except A12's seventh path
and commit 4's message, both labelled **INTENDED**.

**Not in this file, returned to the Reviewer in chat:** A12's final scope
measured base-to-commit-4; A17-final, RUN 2 re-run at commit 4; A15 and
A16 re-run after the advance; A19 for commit 4; the `--is-ancestor`
verification and its exit status; the push; the remote `main` read-back;
and the final ancestry including confirmation that
`science/channel-b0-spin-scope` still points at
`8c27a606643ef315d11e1a1dad8875aa2f1029b1`.
