"""
One-loop check of emergent limiting-speed universality.

Scalar HS channel bubble Pi(p) for Wilson fermions on:
  (A) 4D Euclidean hypercubic lattice (H(4) symmetric substrate)
  (B) continuous time + 3D cubic spatial lattice (no time-space symmetry)

Boson inverse propagator: K(p) = 1/G - Pi(p) = K0 + A_t p0^2 + A_s p1^2 + O(p^4)
Emergent boson speed^2:  c_chi^2 = A_s / A_t   (fermion IR speed = 1 by construction)

Dim-6 anisotropy (case A): K = K0 + A p^2 + B (p^2)^2 + C6 * sum_mu p_mu^4
  xi_chi = C6 / A  -> momentum-dependent speed deviation  delta c^2(k) ~ xi * (k a)^2
Fermion analogue (analytic, Wilson):  C6_f = -1/3 - m r/12,  A_f = 1 + m r.

Conventions: lattice units a = 1, N = 1 (overall N cancels in all ratios).
"""

import numpy as np

# ----------------------------------------------------------------------
# Part A: Euclidean H(4) lattice, Wilson fermions
# ----------------------------------------------------------------------

def pi_H4(p, n=40, m=0.5, r=1.0):
    """Scalar-channel bubble on the 4D hypercubic lattice at external p."""
    k = 2.0 * np.pi * np.arange(n) / n - np.pi
    K = np.meshgrid(k, k, k, k, indexing="ij")
    s1 = [np.sin(K[mu]) for mu in range(4)]
    s2 = [np.sin(K[mu] + p[mu]) for mu in range(4)]
    W1 = m + r * sum(1.0 - np.cos(K[mu]) for mu in range(4))
    W2 = m + r * sum(1.0 - np.cos(K[mu] + p[mu]) for mu in range(4))
    D1 = sum(x * x for x in s1) + W1 * W1
    D2 = sum(x * x for x in s2) + W2 * W2
    num = W1 * W2 - sum(s1[mu] * s2[mu] for mu in range(4))
    return -4.0 * np.mean(num / (D1 * D2))   # mean over BZ = int d^4k/(2pi)^4


def fit_even(eps, vals, order=3):
    """Fit vals(eps) = c0 + c1 eps^2 + c2 eps^4 (+ c3 eps^6)."""
    Adesign = np.vander(eps**2, order + 1, increasing=True)
    coef, *_ = np.linalg.lstsq(Adesign, vals, rcond=None)
    return coef  # [c0, c1(quad), c2(quartic), ...]


def part_A(n=40, m=0.5, r=1.0):
    eps = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
    dirs = {
        "time axis  (e0)":      lambda e: (e, 0, 0, 0),
        "space axis (e1)":      lambda e: (0, e, 0, 0),
        "diagonal (1,1,1,1)/2": lambda e: (e / 2, e / 2, e / 2, e / 2),
    }
    res = {}
    for name, pf in dirs.items():
        vals = np.array([pi_H4(pf(e), n=n, m=m, r=r) for e in eps])
        res[name] = fit_even(eps, vals)

    A_t = -res["time axis  (e0)"][1]      # K = 1/G - Pi, kinetic coeff = -dPi
    A_s = -res["space axis (e1)"][1]
    Q_axis = -res["time axis  (e0)"][2]   # quartic along axis  : B + C6
    Q_diag = -res["diagonal (1,1,1,1)/2"][2]  # quartic on diagonal: B + C6/4
    C6 = (4.0 / 3.0) * (Q_axis - Q_diag)
    A = A_t
    xi_chi = C6 / A

    # Fermion analytic values (Wilson, axis expansion of D(k)):
    A_f = 1.0 + m * r
    C6_f = -1.0 / 3.0 - m * r / 12.0
    xi_f = C6_f / A_f

    print("=" * 70)
    print(f"PART A: H(4) Euclidean lattice   (n={n}^4, m a = {m}, r = {r})")
    print("=" * 70)
    print(f"  A_time  = {A_t:+.8e}")
    print(f"  A_space = {A_s:+.8e}")
    print(f"  c_chi^2 = A_space/A_time = {A_s / A_t:.12f}")
    print(f"  -> dim-4 speed splitting: {abs(A_s / A_t - 1.0):.2e}  (symmetry-protected zero)")
    print()
    print(f"  dim-6 anisotropy:  C6(boson) = {C6:+.6e},  A = {A:+.6e}")
    print(f"     xi_chi (boson)   = C6/A   = {xi_chi:+.6f}")
    print(f"     xi_f   (fermion, analytic)= {xi_f:+.6f}")
    print(f"     channel splitting xi_chi - xi_f = {xi_chi - xi_f:+.6f}")
    print(f"  -> momentum-dependent speed difference between channels:")
    print(f"     |delta c^2(k)| ~ |xi_chi - xi_f| * (k/Lambda)^2")
    return A_s / A_t, xi_chi, xi_f


# ----------------------------------------------------------------------
# Part B: continuous time + 3D cubic spatial lattice (Wilson term spatial)
# omega integral done analytically by residues.
# ----------------------------------------------------------------------

def pi_cont(p0, pvec, n=96, m=0.5, r=1.0):
    k = 2.0 * np.pi * np.arange(n) / n - np.pi
    KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
    Ks = (KX, KY, KZ)
    s1 = [np.sin(Ks[j]) for j in range(3)]
    s2 = [np.sin(Ks[j] + pvec[j]) for j in range(3)]
    W1 = m + r * sum(1.0 - np.cos(Ks[j]) for j in range(3))
    W2 = m + r * sum(1.0 - np.cos(Ks[j] + pvec[j]) for j in range(3))
    E1 = np.sqrt(sum(x * x for x in s1) + W1 * W1)
    E2 = np.sqrt(sum(x * x for x in s2) + W2 * W2)
    sdot = sum(s1[j] * s2[j] for j in range(3))

    def f(w):
        return W1 * W2 - w * (w + p0) - sdot

    w1 = 1j * E1
    w2 = -p0 + 1j * E2
    R1 = f(w1) / ((2j * E1) * ((w1 + p0) ** 2 + E2 ** 2))
    R2 = f(w2) / ((w2 ** 2 + E1 ** 2) * (2j * E2))
    val = 1j * (R1 + R2)            # = int dw/(2pi) num/(D1 D2)
    return -4.0 * np.mean(val.real)


def part_B(n=96, masses=(0.2, 0.5, 1.0), r=1.0):
    eps = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
    print()
    print("=" * 70)
    print(f"PART B: continuous time + cubic spatial lattice   (n={n}^3, r = {r})")
    print("=" * 70)
    out = []
    for m in masses:
        v_t = np.array([pi_cont(e, (0.0, 0.0, 0.0), n=n, m=m, r=r) for e in eps])
        v_s = np.array([pi_cont(0.0, (e, 0.0, 0.0), n=n, m=m, r=r) for e in eps])
        A_t = -fit_even(eps, v_t)[1]
        A_s = -fit_even(eps, v_s)[1]
        c2 = A_s / A_t
        out.append((m, c2))
        print(f"  m a = {m:4.2f}:  A_time = {A_t:+.6e}  A_space = {A_s:+.6e}"
              f"   c_chi^2 = {c2:.6f}   (c_f^2 = 1)")
    print()
    print("  -> WITHOUT a symmetry relating time and space directions,")
    print("     the boson and fermion limiting speeds split at O(1)/O(1/log):")
    for m, c2 in out:
        print(f"     m a = {m:4.2f}:  |c_chi^2 - c_f^2| = {abs(c2 - 1.0):.4f}")
    return out


if __name__ == "__main__":
    ratio, xi_chi, xi_f = part_A(n=40, m=0.5, r=1.0)
    out = part_B(n=96, masses=(0.2, 0.5, 1.0), r=1.0)

    print()
    print("=" * 70)
    print("CONVERGENCE CHECKS")
    print("=" * 70)
    # grid refinement, part A
    for n in (32, 48):
        e = 0.2
        v = pi_H4((e, 0, 0, 0), n=n)
        print(f"  Pi_H4(p0=0.2) at n={n}^4: {v:.10e}")
    v40 = pi_H4((0.2, 0, 0, 0), n=40)
    print(f"  Pi_H4(p0=0.2) at n=40^4: {v40:.10e}")
    for n in (64, 128):
        v = pi_cont(0.2, (0, 0, 0), n=n, m=0.5)
        print(f"  Pi_cont(p0=0.2) at n={n}^3: {v:.10e}")
