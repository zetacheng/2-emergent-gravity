# Result — `P2-BETAV-CIRC-01`: `β_V` discriminating-power audit

**Gate:** `P2-BETAV-CIRC-01`. **Derivation:** `derivations/betav_discriminating_power.md`.
**Script:** `scripts/betav_discriminating.py` (`python -m scripts.betav_discriminating`).

Analytic layer: the target ratio for the generalized structure
`det^{−1/2}(Δ^{(1)})·det^{+1/2}(Δ^{(0)})^k` is `β_V/β_B = −(k+2)`
(`k=1→−3`), so it is **structure-dependent** — the extraction is not degenerate
and an honest lattice pipeline must track `k`. The full curved-background
lattice Proca reproduction (to test whether the paper's numerics actually track
`k`, and the longitudinal-artifact hypothesis) is registered **OPEN**.

- `raw/betav_discriminating.json` — authoritative output.
- `regen/` — non-authoritative re-runs (gitignored).
