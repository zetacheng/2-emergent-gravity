"""
Ward-complete one-loop graviton kernel for lattice Wilson fermions.

Prescription ("minimal vierbein-link"):
  - symmetric vierbein  e = (1+h)^{1/2}  (exact),  E = e^{-1},
    edet = det e = sqrt(det(1+h))
  - kinetic hopping (dir mu):  coefficient  F^mu_a = edet * E^mu_a,
    placed at the link midpoint  -> form factor sin(k_mu + q_mu/2)
  - Wilson hopping (dir mu):    coefficient  G^mu  = edet * (g^{-1})^{mu mu},
    midpoint -> form factor cos(k_mu + q_mu/2)
  - site terms (mass m and Wilson 4r):  coefficient edet, at the site
    -> no form factor
  - spin connection: contributes only an axial (gamma gamma5) vertex in
    the symmetric gauge; its one-loop traces vanish identically, so it
    drops from the quadratic kernel (proved in the paper text).

All h-derivatives of F, edet, G are taken NUMERICALLY (central finite
differences on the exact matrix functions), eliminating hand-expansion
errors.  The h(x)-locality of the coefficients makes the two-graviton
(seagull) vertex carry zero net momentum through the link, hence the
seagull tadpole is exactly q-independent.

Kernel (coefficient of (1/2) h(q) h(-q), per fermion species):
   Gamma2(q) = B(q) + T
   B  = +int_BZ tr[ S(k) U(k,q) S(k+q) U(k+q,-q) ]   (bubble)
   T  = -int_BZ tr[ S(k) V2(k) ]                      (seagull, q-indep)
   one-point:  Theta(ab) = -int_BZ tr[ S(k) U0(k) ]  ->  rho_v

Consistency checks (must pass before Z_h is trusted):
  C1: Theta proportional to delta_{ab}
  C2: Gamma2(q->0) == rho_v * d2(sqrt g)        (CC structure)
  C3: transversality of Gamma2 - rho_v d2(sqrt g) at small q
Then:
  Z_h = d/dq^2 of TT-projected [Gamma2(q) - CC part];  M_Pl^2 = 4 N Z_h / a^2.
"""

import numpy as np

# ---------------- gamma matrices (Euclidean, Hermitian) ----------------
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2, Z2 = np.eye(2, dtype=complex), np.zeros((2, 2), dtype=complex)
GAM = [np.block([[Z2, -1j * s1], [1j * s1, Z2]]),
       np.block([[Z2, -1j * s2], [1j * s2, Z2]]),
       np.block([[Z2, -1j * s3], [1j * s3, Z2]]),
       np.block([[I2, Z2], [Z2, -I2]])]

PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]


# ------------- exact geometric coefficient functions of h --------------
def geom(h):
    """h: real symmetric 4x4.  Returns F[mu,a], edet, G[mu]."""
    g = np.eye(4) + h
    w, v = np.linalg.eigh(g)
    e = v @ np.diag(np.sqrt(w)) @ v.T          # vierbein (1+h)^{1/2}
    E = v @ np.diag(1.0 / np.sqrt(w)) @ v.T    # inverse vierbein
    edet = np.prod(np.sqrt(w))
    ginv = v @ np.diag(1.0 / w) @ v.T
    F = edet * E                               # F[mu,a] (symmetric here)
    G = edet * np.diag(ginv)                   # G[mu]
    return F, edet, G


def hmat(idx_vals):
    h = np.zeros((4, 4))
    for (a, b), val in idx_vals:
        h[a, b] += val
        if a != b:
            h[b, a] += val
    return h


EPSF = 1e-3

def first_derivs():
    """dF[pair][mu,a], dedet[pair], dG[pair][mu] (symmetric-pair derivs)."""
    dF, dE, dG = {}, {}, {}
    for p in PAIRS:
        Fp, ep, Gp = geom(hmat([(p, +EPSF)]))
        Fm, em, Gm = geom(hmat([(p, -EPSF)]))
        dF[p] = (Fp - Fm) / (2 * EPSF)
        dE[p] = (ep - em) / (2 * EPSF)
        dG[p] = (Gp - Gm) / (2 * EPSF)
    return dF, dE, dG


def second_derivs():
    """d2F[p1][p2], d2edet[p1][p2], d2G[p1][p2]."""
    d2F, d2E, d2G = {}, {}, {}
    F0, e0, G0 = geom(np.zeros((4, 4)))
    for p1 in PAIRS:
        d2F[p1], d2E[p1], d2G[p1] = {}, {}, {}
        for p2 in PAIRS:
            if p1 == p2:
                Fp, ep, Gp = geom(hmat([(p1, +EPSF)]))
                Fm, em, Gm = geom(hmat([(p1, -EPSF)]))
                d2F[p1][p2] = (Fp - 2 * F0 + Fm) / EPSF**2
                d2E[p1][p2] = (ep - 2 * e0 + em) / EPSF**2
                d2G[p1][p2] = (Gp - 2 * G0 + Gm) / EPSF**2
            else:
                Fpp, epp, Gpp = geom(hmat([(p1, +EPSF), (p2, +EPSF)]))
                Fpm, epm, Gpm = geom(hmat([(p1, +EPSF), (p2, -EPSF)]))
                Fmp, emp, Gmp = geom(hmat([(p1, -EPSF), (p2, +EPSF)]))
                Fmm, emm, Gmm = geom(hmat([(p1, -EPSF), (p2, -EPSF)]))
                d2F[p1][p2] = (Fpp - Fpm - Fmp + Fmm) / (4 * EPSF**2)
                d2E[p1][p2] = (epp - epm - emp + emm) / (4 * EPSF**2)
                d2G[p1][p2] = (Gpp - Gpm - Gmp + Gmm) / (4 * EPSF**2)
    return d2F, d2E, d2G


def d2_sqrtg():
    """Second derivatives of sqrt(det g) -> CC kernel structure."""
    out = {}
    e0 = 1.0
    for p1 in PAIRS:
        out[p1] = {}
        for p2 in PAIRS:
            if p1 == p2:
                ep = np.sqrt(np.linalg.det(np.eye(4) + hmat([(p1, +EPSF)])))
                em = np.sqrt(np.linalg.det(np.eye(4) + hmat([(p1, -EPSF)])))
                out[p1][p2] = (ep - 2 * e0 + em) / EPSF**2
            else:
                vv = []
                for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    h = hmat([(p1, sa * EPSF), (p2, sb * EPSF)])
                    vv.append(np.sqrt(np.linalg.det(np.eye(4) + h)))
                out[p1][p2] = (vv[0] - vv[1] - vv[2] + vv[3]) / (4 * EPSF**2)
    return out


# ----------------------- lattice fermion pieces ------------------------
def propagator(kk, m, r):
    s = [np.sin(kk[mu]) for mu in range(4)]
    W = m + r * sum(1.0 - np.cos(kk[mu]) for mu in range(4))
    D = sum(x * x for x in s) + W * W
    S = np.zeros((W.size, 4, 4), dtype=complex)
    for mu in range(4):
        S += -1j * s[mu].reshape(-1, 1, 1) * GAM[mu]
    S += W.reshape(-1, 1, 1) * np.eye(4)
    return S / D.reshape(-1, 1, 1)


def vertex_U(kk, q, pair, dF, dE, dG, m, r):
    """One-graviton vertex U^{pair}(k,q): midpoint form factors."""
    sb = [np.sin(kk[mu] + q[mu] / 2.0) for mu in range(4)]
    cb = [np.cos(kk[mu] + q[mu] / 2.0) for mu in range(4)]
    npts = kk[0].size
    U = np.zeros((npts, 4, 4), dtype=complex)
    for mu in range(4):
        for a in range(4):
            c = dF[pair][mu, a]
            if abs(c) > 1e-12:
                U += (1j * c) * sb[mu].reshape(-1, 1, 1) * GAM[a]
        cw = -r * dG[pair][mu]
        if abs(cw) > 1e-12:
            U += cw * cb[mu].reshape(-1, 1, 1) * np.eye(4)
    U += (dE[pair] * (m + 4.0 * r)) * np.tile(np.eye(4), (npts, 1, 1))
    return U


def bubble(q, n, m, r, dF, dE, dG):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    grids = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    kk = [g.ravel() for g in grids]
    kkq = [kk[mu] + q[mu] for mu in range(4)]
    S1, S2 = propagator(kk, m, r), propagator(kkq, m, r)
    mq = tuple(-x for x in q)
    X, Y = {}, {}
    for p in PAIRS:
        U1 = vertex_U(kk, q, p, dF, dE, dG, m, r)        # U(k, q)
        U2 = vertex_U(kkq, mq, p, dF, dE, dG, m, r)      # U(k+q, -q)
        X[p] = np.einsum("pij,pjk->pik", S1, U1)         # S(k) U(k,q)
        Y[p] = np.einsum("pij,pjk->pik", S2, U2)         # S(k+q) U(k+q,-q)
    B = {}
    for p1 in PAIRS:
        for p2 in PAIRS:
            B[(p1, p2)] = np.einsum("pij,pji->p", X[p1], Y[p2]).mean().real
    return B


def seagull_and_onepoint(n, m, r, dF, dE, dG, d2F, d2E, d2G):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    grids = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    kk = [g.ravel() for g in grids]
    S = propagator(kk, m, r)
    s = [np.sin(kk[mu]) for mu in range(4)]
    c = [np.cos(kk[mu]) for mu in range(4)]
    # traces needed:  tr[S gamma_a] = -4 i s_a / D ;  tr[S] = 4 W / D
    trSg = [np.einsum("pij,ji->p", S, GAM[a]) for a in range(4)]
    trS = np.einsum("pii->p", S)

    def tadpole_of(dF_, dE_, dG_):
        val = 0.0
        for mu in range(4):
            for a in range(4):
                cf = dF_[mu, a]
                if abs(cf) > 1e-12:
                    val += (1j * cf) * (s[mu] * trSg[a]).mean()
            cw = -r * dG_[mu]
            if abs(cw) > 1e-12:
                val += cw * (c[mu] * trS).mean()
        val += dE_ * (m + 4.0 * r) * trS.mean()
        return val.real

    Theta = {p: -tadpole_of(dF[p], dE[p], dG[p]) for p in PAIRS}
    T = {}
    for p1 in PAIRS:
        for p2 in PAIRS:
            T[(p1, p2)] = -tadpole_of(d2F[p1][p2], d2E[p1][p2], d2G[p1][p2])
    return Theta, T


# ------------------------ projectors and fits --------------------------
def to_tensor(D):
    """dict over (pair,pair) -> full (4,4,4,4) with symmetric-deriv
    convention: off-diagonal pairs represent h_ab+h_ba, so the kernel in
    natural tensor components carries 1/ (multiplicity) factors."""
    Tn = np.zeros((4, 4, 4, 4))
    for (a, b), (cc, d) in D.keys():
        val = D[((a, b), (cc, d))]
        w1 = 1.0 if a == b else 0.5
        w2 = 1.0 if cc == d else 0.5
        v = val * w1 * w2
        for (x, y) in {(a, b), (b, a)}:
            for (u, w) in {(cc, d), (d, cc)}:
                Tn[x, y, u, w] = v
    return Tn


def theta_tensor(Theta):
    M = np.zeros((4, 4))
    for (a, b) in PAIRS:
        v = Theta[(a, b)] * (1.0 if a == b else 0.5)
        M[a, b] = v
        M[b, a] = v
    return M


def projectors(q):
    q = np.asarray(q, float)
    om = np.outer(q, q) / np.dot(q, q)
    th = np.eye(4) - om
    P2 = np.zeros((4, 4, 4, 4))
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    P2[a, b, cc, d] = (0.5 * (th[a, cc] * th[b, d]
                                              + th[a, d] * th[b, cc])
                                       - th[a, b] * th[cc, d] / 3.0)
    return P2


def fit_even(eps, vals, order=2):
    A = np.vander(eps**2, order + 1, increasing=True)
    coef, *_ = np.linalg.lstsq(A, vals, rcond=None)
    return coef


# ------------------------------- driver --------------------------------
def run(n=16, m=0.5, r=1.0):
    print("=" * 70)
    print(f"WARD-COMPLETE GRAVITON KERNEL  (n={n}^4, m a={m}, r={r})")
    print("=" * 70)
    dF, dE, dG = first_derivs()
    d2F, d2E, d2G = second_derivs()

    Theta, T = seagull_and_onepoint(n, m, r, dF, dE, dG, d2F, d2E, d2G)
    Th = theta_tensor(Theta)
    diag = np.diag(Th)
    off = Th - np.diag(diag)
    print("C1  one-point <Theta_ab>:")
    print(f"    diag = {diag}")
    print(f"    max|offdiag| = {np.abs(off).max():.2e}   "
          f"max|diag spread| = {np.abs(diag - diag.mean()).max():.2e}")
    rho_v = 2.0 * diag.mean()      # Theta = (rho_v/2) delta
    print(f"    rho_v = {rho_v:+.6e}")

    Tsg = to_tensor(T)
    d2sg_nested = d2_sqrtg()
    d2sg = to_tensor({(p1, p2): d2sg_nested[p1][p2]
                      for p1 in PAIRS for p2 in PAIRS})
    CC = rho_v * d2sg

    # C2: q->0 limit of full kernel vs CC structure
    qsmall = (1e-3, 0.0, 0.0, 0.0)
    B0 = to_tensor(bubble(qsmall, n, m, r, dF, dE, dG))
    full0 = B0 + Tsg
    num = np.abs(full0 - CC).max()
    den = max(np.abs(CC).max(), 1e-30)
    print("C2  q->0 kernel vs rho_v * d2(sqrt g):")
    print(f"    max|Gamma2(0) - CC| = {num:.3e}   max|CC| = {den:.3e}"
          f"   ratio = {num / den:.3e}")

    # C3: transversality of subtracted kernel at small q
    eps = np.array([0.15, 0.25, 0.35, 0.45, 0.55])
    print("C3  Ward transversality of (Gamma2 - CC), q || e0:")
    for e in (0.2, 0.4):
        q = (e, 0.0, 0.0, 0.0)
        G = to_tensor(bubble(q, n, m, r, dF, dE, dG)) + Tsg - CC
        long_ = np.abs(np.einsum("a,abcd->bcd", np.array(q), G)).max()
        scale = np.abs(G).max() * e
        print(f"    q0={e}:  max|q.Gamma~| = {long_:.3e}   "
              f"(scale q*|Gamma~| = {scale:.3e},  ratio = {long_/scale:.3e})")

    # Z_h extraction: TT projection of subtracted kernel
    res = {}
    for name, pf in {"time": lambda e: (e, 0, 0, 0),
                     "space": lambda e: (0, e, 0, 0),
                     "diag": lambda e: (e/2, e/2, e/2, e/2)}.items():
        vals = []
        for e in eps:
            q = pf(e)
            G = to_tensor(bubble(q, n, m, r, dF, dE, dG)) + Tsg - CC
            P2 = projectors(q)
            vals.append(np.einsum("abcd,abcd->", P2, G) / 5.0)
        res[name] = fit_even(eps, np.array(vals))
    Zt, Zs = res["time"][1], res["space"][1]
    g0_t = res["time"][0]
    C6 = (4.0/3.0) * (res["time"][2] - res["diag"][2])
    print("RESULTS:")
    print(f"    TT q^0 residual (should be ~0): {g0_t:+.3e}")
    print(f"    Z_h(time)  = {Zt:+.6e}")
    print(f"    Z_h(space) = {Zs:+.6e}   isotropy Z_s/Z_t = {Zs/Zt:.10f}")
    print(f"    xi_h = C6/Z = {C6/Zt:+.4f}")
    print(f"    M_Pl^2 a^2 / N = 4 Z_h = {4*Zt:+.6e}")
    return Zt, rho_v


if __name__ == "__main__":
    for m in (0.25, 0.5, 1.0):
        run(n=16, m=m, r=1.0)
    run(n=20, m=0.5, r=1.0)   # convergence
