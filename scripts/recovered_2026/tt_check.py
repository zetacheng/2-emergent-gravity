"""
One-loop lattice stress-tensor two-point function for Wilson fermions.

  B_{mu nu, rho sigma}(q) = mean_k  tr[ V_{mu nu}(k,k+q) S(k+q)
                                        V_{rho sigma}(k+q,k) S(k) ]

Euclidean quadratic effective kernel: Gamma^(2) = N * B(q)  (per species).
Deliverables:
  (1) TT-projected kernel G2(q): isotropy of the q^2 coefficient
      (graviton-channel light-cone check, robust against contact terms),
  (2) sign and size of Z_h = dG2/dq^2 (first-pass c2 estimate;
      contact/seagull terms deferred -- tested for prescription
      sensitivity by switching the Wilson-term vertex on/off),
  (3) dim-6 anisotropy xi_h of the graviton channel (axis vs diagonal),
      to compare with xi_f (fermion) and xi_chi (scalar channel).

Vertex prescription (declared):
  gamma part (sine-improved, symmetric):
     V^g_{mu nu}(k,k') = (i/4)[ g_mu (s_nu(k)+s_nu(k'))
                              + g_nu (s_mu(k)+s_mu(k')) ]
  Wilson part (diagonal, optional):
     V^W_{mu nu}(k,k') = (r/4) delta_{mu nu} (cos k_mu + cos k'_mu) * 1
  Pure-trace EMT pieces (-delta_{mu nu} L) drop identically under the
  TT projection and are omitted.

Lattice units a = 1, N = 1 (overall N trivial).
"""

import numpy as np

# ---------------- Euclidean gamma matrices (Hermitian) ----------------
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)

GAM = [
    np.block([[Z2, -1j * s1], [1j * s1, Z2]]),
    np.block([[Z2, -1j * s2], [1j * s2, Z2]]),
    np.block([[Z2, -1j * s3], [1j * s3, Z2]]),
    np.block([[I2, Z2], [Z2, -I2]]),
]
for a in range(4):       # sanity: Clifford algebra
    for b in range(4):
        assert np.allclose(GAM[a] @ GAM[b] + GAM[b] @ GAM[a],
                           2.0 * (a == b) * np.eye(4))

PAIRS = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]  # 10 pairs


def propagator(kk, m, r):
    """S(k) = (-i gamma.s + W)/(s^2+W^2), kk: list of 4 arrays."""
    s = [np.sin(kk[mu]) for mu in range(4)]
    W = m + r * sum(1.0 - np.cos(kk[mu]) for mu in range(4))
    D = sum(x * x for x in s) + W * W
    npts = W.size
    S = np.zeros((npts, 4, 4), dtype=complex)
    for mu in range(4):
        S += -1j * s[mu].reshape(-1, 1, 1) * GAM[mu]
    S += W.reshape(-1, 1, 1) * np.eye(4)
    S /= D.reshape(-1, 1, 1)
    return S


def vertex(kk, kkp, mu, nu, r, wilson_vertex=True):
    """V_{mu nu}(k, k') as (npts,4,4)."""
    sa = np.sin(kk[nu]) + np.sin(kkp[nu])
    sb = np.sin(kk[mu]) + np.sin(kkp[mu])
    V = (1j / 4.0) * (sa.reshape(-1, 1, 1) * GAM[mu]
                      + sb.reshape(-1, 1, 1) * GAM[nu])
    if wilson_vertex and mu == nu:
        c = (r / 4.0) * (np.cos(kk[mu]) + np.cos(kkp[mu]))
        V = V + c.reshape(-1, 1, 1) * np.eye(4)
    return V


def tt_bubble(q, n=16, m=0.5, r=1.0, wilson_vertex=True):
    """Full B_{mu nu, rho sigma}(q) as a (4,4,4,4) real array."""
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    grids = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    kk = [g.ravel() for g in grids]
    kkp = [kk[mu] + q[mu] for mu in range(4)]
    S1 = propagator(kk, m, r)
    S2 = propagator(kkp, m, r)

    X = {}
    for (mu, nu) in PAIRS:
        V = vertex(kk, kkp, mu, nu, r, wilson_vertex)
        X[(mu, nu)] = (np.einsum("pij,pjk->pik", V, S2),
                       np.einsum("pij,pjk->pik", V, S1))

    B = np.zeros((4, 4, 4, 4))
    for (mu, nu) in PAIRS:
        for (rho, sg) in PAIRS:
            val = np.einsum("pij,pji->p", X[(mu, nu)][0],
                            X[(rho, sg)][1]).mean()
            v = val.real
            for (a, b) in {(mu, nu), (nu, mu)}:
                for (c, d) in {(rho, sg), (sg, rho)}:
                    B[a, b, c, d] = v
    return B


def projectors(q):
    """Barnes-Rivers projectors for Euclidean momentum q (4-vector)."""
    q = np.asarray(q, dtype=float)
    q2 = np.dot(q, q)
    om = np.outer(q, q) / q2
    th = np.eye(4) - om
    P2 = np.zeros((4, 4, 4, 4))
    P1 = np.zeros((4, 4, 4, 4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    P2[a, b, c, d] = (0.5 * (th[a, c] * th[b, d]
                                             + th[a, d] * th[b, c])
                                      - th[a, b] * th[c, d] / 3.0)
                    P1[a, b, c, d] = 0.5 * (th[a, c] * om[b, d]
                                            + th[a, d] * om[b, c]
                                            + th[b, c] * om[a, d]
                                            + th[b, d] * om[a, c])
    P0s = np.einsum("ab,cd->abcd", th, th) / 3.0
    P0w = np.einsum("ab,cd->abcd", om, om)
    return P2, P1, P0s, P0w


def project(B, q):
    P2, P1, P0s, P0w = projectors(q)
    g2 = np.einsum("abcd,abcd->", P2, B) / 5.0
    g1 = np.einsum("abcd,abcd->", P1, B) / 3.0
    g0s = np.einsum("abcd,abcd->", P0s, B) / 1.0
    g0w = np.einsum("abcd,abcd->", P0w, B) / 1.0
    return g2, g1, g0s, g0w


def fit_even(eps, vals, order=2):
    A = np.vander(eps**2, order + 1, increasing=True)
    coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
    return coef


def run(n=16, m=0.5, r=1.0, wilson_vertex=True, label=""):
    eps = np.array([0.15, 0.25, 0.35, 0.45, 0.55])
    dirs = {
        "time (e0)": lambda e: (e, 0.0, 0.0, 0.0),
        "space (e1)": lambda e: (0.0, e, 0.0, 0.0),
        "diag": lambda e: (e / 2, e / 2, e / 2, e / 2),
    }
    G2 = {}
    for name, pf in dirs.items():
        G2[name] = np.array([project(tt_bubble(pf(e), n, m, r,
                                               wilson_vertex), pf(e))[0]
                             for e in eps])
    ct = fit_even(eps, G2["time (e0)"])
    cs = fit_even(eps, G2["space (e1)"])
    cd = fit_even(eps, G2["diag"])

    Zt, Zs = ct[1], cs[1]
    Q_axis, Q_diag = ct[2], cd[2]
    C6 = (4.0 / 3.0) * (Q_axis - Q_diag)
    xi_h = C6 / Zt
    xi_f = -(1.0 / 3.0 + m * r / 12.0) / (1.0 + m * r)

    print("-" * 68)
    print(f"{label}  (n={n}^4, m a={m}, r={r}, "
          f"Wilson vertex={'on' if wilson_vertex else 'off'})")
    print(f"  Z_h(time)  = {Zt:+.6e}")
    print(f"  Z_h(space) = {Zs:+.6e}")
    print(f"  isotropy:  Z_s/Z_t = {Zs / Zt:.10f}   "
          f"(graviton light-cone check)")
    print(f"  sign(Z_h) = {'+' if Zt > 0 else '-'}   "
          f"(bubble-only first-pass c2 estimate)")
    print(f"  dim-6:  xi_h = {xi_h:+.4f}   xi_f = {xi_f:+.4f}   "
          f"Delta(h-f) = {xi_h - xi_f:+.4f}")
    return Zt, Zs, xi_h


if __name__ == "__main__":
    print("=" * 68)
    print("ONE-LOOP <T T> LATTICE CHECK  (graviton channel)")
    print("=" * 68)

    # main run + prescription sensitivity
    run(n=16, m=0.5, r=1.0, wilson_vertex=True,
        label="MAIN")
    run(n=16, m=0.5, r=1.0, wilson_vertex=False,
        label="PRESCRIPTION TEST (gamma vertex only)")

    # mass dependence
    run(n=16, m=0.25, r=1.0, wilson_vertex=True, label="MASS m a = 0.25")
    run(n=16, m=1.0, r=1.0, wilson_vertex=True, label="MASS m a = 1.0")

    # grid convergence
    run(n=12, m=0.5, r=1.0, wilson_vertex=True, label="CONVERGENCE n=12")
    run(n=20, m=0.5, r=1.0, wilson_vertex=True, label="CONVERGENCE n=20")
