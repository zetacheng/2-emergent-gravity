# `P2-LATTICE-MICROSPEC-01` — reflection-positivity literature coverage

**STATUS: NOT CONDUCTED. The `D-1` network precondition failed.**

This file exists because the specification requires it to exist. It records
the precondition failure and the hosts attempted, and nothing else. **It
records no literature claim, no identifier, no fetch, no applicability
mapping, no axis table, and no coverage verdict for any candidate.**

---

## 1. What this file would have contained, and does not

`D-1` was to determine what the published literature already establishes
about Osterwalder–Schrader reflection positivity for the frozen `U(N)`
chiral NJL interaction taken together with each of the four candidate
kinetic operators, and — precisely — what it does not.

**Every conclusion of that kind requires a fetched work.** The
specification is explicit that a work identified but not fetched may be
recorded only as `NOT FETCHED` or `RECALLED` and cannot support a
`COVERED` verdict, and that an audit conducted from memory would be worse
than no audit, being exactly the failure the task exists to correct.

**No work was fetched. No work was identified for the record. Nothing is
recorded here that a later task could mistake for evidence.**

## 2. The precondition, as tested

Measured 2026-08-16, in the execution container, against the authoritative
`main` at `bfef924c368658cac85c04ed18d96eb4450afba6`.

### 2.1 Fetch path 1 — HTTPS through the container's egress proxy

    HOST / URL                                                  RESULT

    arxiv.org         /abs/hep-lat/9707022                      curl (56) CONNECT tunnel failed, response 403; http_code 000
    export.arxiv.org  /abs/hep-lat/9707022                      curl (56) CONNECT tunnel failed, response 403; http_code 000
    doi.org           /10.1016/0003-4916(78)90039-8             curl (56) CONNECT tunnel failed, response 403; http_code 000
    link.springer.com /article/10.1007/BF01645738               curl (56) CONNECT tunnel failed, response 403; http_code 000
    www.sciencedirect.com /science/article/pii/0003491678900398 curl (56) CONNECT tunnel failed, response 403; http_code 000
    projecteuclid.org /journals/communications-in-mathematical-physics
                                                                curl (56) CONNECT tunnel failed, response 403; http_code 000
    pos.sissa.it      /105/267/pdf                              curl (56) CONNECT tunnel failed, response 403; http_code 000
    api.semanticscholar.org /graph/v1/paper/DOI:...             curl (56) CONNECT tunnel failed, response 403; http_code 000
    inspirehep.net    /api/literature?q=arxiv:hep-lat/9707022   curl (56) CONNECT tunnel failed, response 403; http_code 000
    www.osti.gov      /                                         curl (56) CONNECT tunnel failed, response 403; http_code 000
    inis.iaea.org     /records/w5b1b-sr829                      curl (56) CONNECT tunnel failed, response 403; http_code 000
    example.com       /                                         curl (56) CONNECT tunnel failed, response 403; http_code 000

**Eleven scholarly or bibliographic hosts, zero reached.**

`example.com` is a NON-SCHOLARLY CONTROL and is blocked identically. The
denial is therefore not specific to scholarly publishers; it is a general
egress policy.

### 2.2 Fetch path 2 — the environment's own fetch tool

A second, independent fetch path was tried, so that the finding does not
rest on one client's configuration.

    arxiv.org, export.arxiv.org, doi.org, link.springer.com,
    www.sciencedirect.com, projecteuclid.org, pos.sissa.it,
    inis.iaea.org, api.semanticscholar.org, example.com

    EVERY ONE:  EGRESS_BLOCKED — "blocked by the network egress proxy"

**Two independent fetch paths, the same result on every host.**

### 2.3 Controls — the network itself is not down

    pypi.org      /simple/     http_code 200   (reached)
    github.com    /            http_code 400   (reached; gateway-level response)

**The container has working outbound HTTPS to package and code hosts.**
What is unavailable is scholarly and bibliographic egress specifically, by
policy.

### 2.4 The proxy's own account of the denials

The container's egress proxy reports, for each attempted scholarly host:

    kind    connect_rejected
    detail  gateway answered 403 to CONNECT (policy denial or upstream failure)

**This is an organisational policy denial, not a local misconfiguration and
not a transport fault.** The environment's operating instructions state
that policy denials of this kind are to be reported rather than retried,
and no attempt was made to circumvent them: TLS verification was not
disabled, the proxy was not unset, and no alternative route was sought.

### 2.5 A search path returned results, and was deliberately not used

**Disclosed because a later reader must not conclude that nothing at all
came back.**

One web-search invocation, made as a probe of a third and distinct path,
returned result titles and URLs together with prose synthesised from
snippets. **It fetched nothing.** No document was retrieved, no page bytes
were obtained, and no evidential depth — listing, abstract or full text —
could be established for any work. **Every URL it returned is among the
hosts blocked above.**

**No work, identifier, title, claim or statement from that probe is
recorded in this file or relied on anywhere in `D-1`.** Search-result prose
is not a fetch, and treating it as one would reproduce the recalled-content
failure this audit exists to correct.

## 3. The consequence, stated plainly

**The `D-1` global precondition failed. The audit was not conducted.**

Per the specification, the task stops at the precondition and the
applicability, verdict and burden work is not attempted. **This is a
complete outcome, not a partial one.** The finding it establishes is:

> **Conducting this audit requires an executor with library or scholarly
> network access. This container does not have it, and no amount of care
> within it would substitute.**

**No coverage verdict is recorded for any of the four candidate kinetic
operators.** No candidate is selected, eliminated, ranked or preferred, no
proof route is designed, `B0`'s construction estimate is neither re-derived
nor revised, no register entry is added, and no existing file is modified.

**The reflection-positivity obligation frozen at `P2-LATTICE-ONTOLOGY-01`
line 181 is untouched by this file.** Nothing here reduces it, and nothing
here bears on it.

## 4. What a future executor needs

**Whoever repeats this task needs fetch access to at least:**

    arxiv.org or export.arxiv.org      preprint abstracts and full text
    doi.org                            DOI resolution
    the publisher hosts behind those DOIs, for works predating arXiv

**Abstract-only access will not be enough for the works that matter most.**
The specification records why: an abstract of a 1978 or 1987 paper will not
usually state the reflection type, the boundary conditions, or the
parameter restrictions, and those are exactly the hypotheses a coverage
mapping turns on.

**This paragraph is a statement of what access is required. It is not a
search plan, and it names no work.**
