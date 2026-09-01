# PI RULING — R-1: THE DECOUPLING OF THE ASSEMBLED CHAIN

    STATUS      ISSUED TEXT. This document is the ruling. Any
                translation, summary, or restatement elsewhere is a
                rendering of it.
    AUTHORITY   PI (Zeta Hoi-Ho Cheng)
    DATE        2026-08-31
    SUPERSEDES  The document of the same identifier bearing SHA-256
                f59511b5238a37c3500d5b1019a978ce177f97c9ea8ebc6fa97335af9a6796f8,
                which was reviewed FIT FOR RECORDING but not landed.
                Its RATIONALE named the exponent mapping as the second
                element not fixed by landed text. That was wrong:
                P2-XI-QM3-DEP-01 records the exponent mapping as FIXED
                at g = +2c by DECISION_LOG.md:1258-1262, and names the
                decoupling prescription as the second unfixed element.
                The correction is confined to that RATIONALE; every
                RULING line is unchanged.
    IDENTIFIER  P2-XI-RULINGS-03. A canonical repository decision key
                may be assigned externally at landing. Such filing
                metadata does not modify this ISSUED TEXT.
    SCOPE       R-1 of the resolution path recorded by
                P2-XI-QM3-DEP-01: which decoupling the assembled chain
                of the xi ledger comprises.
    LAYERING    Lines marked RULING are the decision. Lines marked
                RATIONALE are rendering, recorded for context, and are
                not to be cited as the ruling.

---

## RULING 1 — The decoupling of the assembled chain

RULING      The scope of the 2026-08-09 ruling "Mean-field channel for
            P2-PHASE-01: the scalar channel with a real auxiliary
            field" is extended from P2-PHASE-01 mean-field work to the
            assembled chain of the xi ledger. The assembled chain's
            decoupling is the scalar channel with a real auxiliary
            field, on the same terms the 2026-08-09 ruling states.

RULING      This is a choice of route for the chain, not a judgement
            about other channels. It carries forward, unchanged, the
            2026-08-09 ruling's own limits:
              - It does not close OPEN-AC-1. The Fierz ambiguity —
                that channels equivalent as operators are inequivalent
                after truncation — is unaffected by which channel is
                used, and the P/V/A/T mean-field construction remains
                open.
              - It is not a finding that the V and A representations
                are wrong. They remain deferred, not excluded, per
                DEFERRED-01.
              - Specifying the decoupling used is not a claim that
                decouplings are equivalent after truncation. The
                family-wide question remains the open item registered
                on 2026-08-24, whose escalation condition is unchanged
                by this ruling.

## RULING 2 — What this ruling does not supply

RULING      This ruling names the channel and the auxiliary field. It
            does not fix the exponent convention, the g-to-c mapping,
            the constraints or contour, the functional-measure
            treatment, or the mathematical definition of the
            normalization object the landed criterion names. Those are
            the decoupling prescription. Until such a prescription is
            landed, the decoupling of the assembled chain is named but
            not fully specified, and P2-XI-QM3-DEP-01's determination
            stands.

## RULING 3 — Authorization of the prescription task

RULING      A specification is authorized to land the decoupling
            prescription for the assembled chain in the sense
            P2-FIERZSUM-01.md:218-220 states — auxiliary variables,
            constraints, Jacobian, and an explicit statement of what
            is generated dynamically rather than introduced as an
            independent field. That task defines; it does not
            evaluate. It must not compute the curvature dependence of
            the normalization object, which remains the question
            P2-XI-QM3-DEP-01 was scoped to and which a re-run of that
            check, under a separate specification, is to answer. It
            must not resolve DET-01 or choose the functional measure.

RATIONALE   P2-XI-QM3-DEP-01 found two elements not fixed by landed
            text: which channel or set of channels the assembled
            chain's decoupling comprises, and the decoupling
            prescription — auxiliary variables, constraints,
            Jacobian. This ruling fixes the first. The second is a
            prescription question and is not fixed by naming a
            channel. The exponent mapping is NOT among the unfixed
            elements: that same artifact records it as fixed by
            landed text at g = +2c, DECISION_LOG.md:1258-1262. On the
            Researcher's reading, recorded in that artifact's own
            symmetry statement, R-1 and R-2 together would return
            UNIQUELY IDENTIFIED and R-1 alone does not.

## ROUTING

RULING      As established by P2-XI-RULINGS-01: review of this ruling
            document is mandatory as a document-quality and
            consistency review, non-gating as to the PI's substantive
            authority. The specification this ruling authorizes
            remains subject to the repository's normal pre-execution
            review gate. Model-level assumptions arising in that task
            are routed to the PI.

END OF ISSUED TEXT
