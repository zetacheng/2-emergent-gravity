"""Gate ``P2-BETAV-CIRC-01`` — discriminating power of the beta_V/beta_B test.

Paper 2's Finding 5 confirms ``beta_V/beta_B = -3`` on the lattice
(``-3.2(5)``).  The sharp question (not "reproduce -3.2(5)"): **can the
extraction distinguish -3 from anything else, or does it return -3 by
construction?**

Test at the analytic layer that the paper's lattice-numerical layer must agree
with: feed a hypothetical species with the modified determinant structure

    det^{-1/2}(Delta^(1)+m^2) . det^{+1/2}(Delta^(0)+m^2)^k ,   k != 1,

and compute the true induced ratio.  If the ratio is structure-dependent, an
extraction that returned -3 regardless would be circular; a faithful extraction
must track the structure.

Analytic result (Seeley-DeWitt a_1, per P2-HK-01 conventions):

    beta_V(k)/beta_B = -(2 + k)      [k=1 -> -3, the Proca value].

So the target is structure-dependent -> the test is NOT degenerate.  The full
confirmation that the paper's *lattice* pipeline tracks ``k`` (rather than
normalising it out) is registered OPEN in GATES.md.

Run bare::

    python -m scripts.betav_discriminating
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

# Per-factor Seeley-DeWitt data (see derivations/P2-HK-01):
#   vector 1-form: dim=4, tr E/R=1 -> tr a_1/R = 4/6 - 1 = -1/3, prefactor +1/2
#   scalar:        dim=1, tr E/R=0 -> tr a_1/R = 1/6,  prefactor -1/2 per power
K = sp.Rational(1, 16) / sp.pi**2
VEC_TRA1 = sp.Rational(4, 6) - 1     # -1/3
SCAL_TRA1 = sp.Rational(1, 6)
BETA_B = -sp.Rational(1, 2) * K * SCAL_TRA1  # real-scalar reference = -1/(192 pi^2)


def beta_V(k) -> sp.Expr:
    """Induced beta_V for det^{-1/2}(Delta^(1)) . det^{+1/2}(Delta^(0))^k.

    Vector factor: prefactor p=+1/2.  Scalar^k factor: det^{+k/2} -> p=-k/2.
    beta = sum over factors of  -p * K * (tr a_1 / R).
    """
    k = sp.nsimplify(k)
    vec = -sp.Rational(1, 2) * K * VEC_TRA1
    scal = -(-k / 2) * K * SCAL_TRA1
    return sp.simplify(vec + scal)


def ratio_V_over_B(k) -> sp.Expr:
    return sp.simplify(beta_V(k) / BETA_B)


def results_dict() -> dict:
    ks = [0, 1, 2, 3, sp.Rational(1, 2)]
    table = {}
    for k in ks:
        r = ratio_V_over_B(k)
        table[str(k)] = {"beta_V_over_beta_B": sp.sstr(r), "float": float(r)}
    # symbolic closed form
    ksym = sp.Symbol("k", positive=True)
    closed = sp.simplify(ratio_V_over_B(ksym))
    return {
        "closed_form_ratio": sp.sstr(closed),  # expect -(k+2)
        "proca_k1_ratio": float(ratio_V_over_B(1)),  # -3
        "table_over_k": table,
        "discriminating": float(ratio_V_over_B(1)) != float(ratio_V_over_B(2)),
        "note": "Target ratio depends on the determinant structure k; an "
                "extraction returning -3 for k!=1 would be circular.",
    }


def main() -> None:
    res = results_dict()
    regen = (Path(__file__).resolve().parents[1] / "results"
             / "P2-BETAV-CIRC-01" / "regen")
    regen.mkdir(parents=True, exist_ok=True)
    (regen / "betav_discriminating.json").write_text(
        json.dumps(res, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print("Gate P2-BETAV-CIRC-01 — discriminating power (analytic layer)")
    print("=" * 60)
    print(f"  closed form: beta_V/beta_B = {res['closed_form_ratio']}  (k+2, "
          f"negated)")
    for k, d in res["table_over_k"].items():
        print(f"    k={k:>3}: beta_V/beta_B = {d['beta_V_over_beta_B']:>6}  "
              f"({d['float']:+.3f})")
    print(f"  discriminating (k=1 vs k=2 differ)? {res['discriminating']}")
    print("  => target is structure-dependent; a faithful extraction must "
          "track k.")


if __name__ == "__main__":
    main()
