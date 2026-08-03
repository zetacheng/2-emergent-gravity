"""EXPLORATORY / non-canonical probe. See STATUS block at the end of file.
Free lattice fermions, half filling; geometry = smooth local dilation of all
hoppings. Pure mode counting: no auxiliary fields, no channel decomposition,
no Fierz choice anywhere."""
import numpy as np


def E(N, eps, L, t2):
    j = np.arange(N)
    s = 1.0 + eps*np.cos(2*np.pi*j*(N//L)/N)
    H = np.zeros((N, N))
    # nearest neighbour
    H[j, (j+1) % N] -= 1.0*s
    H[(j+1) % N, j] -= 1.0*s
    # next-nearest neighbour (changes the UV band only)
    H[j, (j+2) % N] -= t2*s
    H[(j+2) % N, j] -= t2*s
    return np.sort(np.linalg.eigvalsh(H))[:N//2].sum()

N = 720

print("CONTROL 1 - locality at t2=0: a local grad^2 term gives dE*L^2/N = const")
eps = 0.04
for L in (24, 36, 48, 72, 144):
    dE = E(N, eps, L, 0.0) - E(N, 0.0, L, 0.0)
    print(f"   L={L:4d}   dE={dE:+.6e}   dE*L^2/N = {dE*L**2/N:+.6f}")

print("\nCONTROL 2 - quadratic response: a,b should scale as eps^2")
L = 72
for eps in (0.02, 0.04, 0.08):
    dE = E(N, eps, L, 0.0) - E(N, 0.0, L, 0.0)
    print(f"   eps={eps:5.3f}   dE={dE:+.6e}   dE/eps^2 = {dE/eps**2:+.6e}")

print("\nMAIN - separate the two responses by fitting across wavelengths:")
print("   g = cos(qx):  int g^2 = N/2 (L-independent);  int (dg)^2 = q^2 N/2")
print("   fit  dE = a*(N/2) + b*(q^2 N/2);  quote eps-normalized  a/eps^2, b/eps^2")
eps = 0.04
Ls = np.array([36, 48, 72, 90, 120, 144])
q2 = (2*np.pi/Ls)**2
A = np.vstack([np.full_like(q2, N/2), q2*N/2]).T
print("\n  t2      a/eps^2 (no-derivative)    b/eps^2 (gradient^2)     fit resid")
for t2 in (0.0, 0.1, 0.2, 0.3, 0.4):
    dE = np.array([E(N, eps, L, t2) - E(N, 0.0, L, t2) for L in Ls])
    (a, b), *_ = np.linalg.lstsq(A, dE, rcond=None)
    rel = np.abs(A@np.array([a, b]) - dE).max()/np.abs(dE).max()
    print(f" {t2:4.2f}   {a/eps**2:+.4e}              "
          f"{b/eps**2:+.4e}          {rel:.1e}")

print("\n  IR invariance: v_F = 2*sin(kF) + 4*t2*sin(2kF) at kF=pi/2")
print("  -> v_F = 2 for every t2")
