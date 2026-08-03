"""EXPLORATORY / non-canonical probe #2: Euclidean -> Hamiltonian reconstruction.
Companion to EXPLORATORY_lattice_geometry_response.py (which is Hamiltonian-native);
this one demonstrates the P2-LATTICE-ONTOLOGY-01 §1b claims from the OTHER side:
input is ONLY a Euclidean configuration-weight system (2D anisotropic Ising,
Boltzmann weights exp(K s s'), no Hamiltonian anywhere in the input)."""
import numpy as np

def transfer_matrix(L, Kx, Kt):
    """Symmetric row-to-row transfer matrix built purely from Boltzmann weights:
    T = V_intra^(1/2) V_inter V_intra^(1/2)."""
    dim = 2**L
    spins = np.array([[1 if (s >> i) & 1 else -1 for i in range(L)]
                      for s in range(dim)])
    intra = np.exp(Kx * np.sum(spins * np.roll(spins, -1, axis=1), axis=1))
    inter = np.exp(Kt * (spins @ spins.T))
    Vh = np.sqrt(intra)
    return Vh[:, None] * inter * Vh[None, :]

def gaps(L, Kx, Kt, n=4):
    w = np.sort(np.linalg.eigvalsh(transfer_matrix(L, Kx, Kt)))[::-1]
    return np.all(w > 0), -np.log(w[1:n+1] / w[0])

if __name__ == "__main__":
    print("A) POSITIVE TRANSFER MATRIX: T > 0 permits H = -log(T)/a,")
    print("   a self-adjoint derived Hamiltonian in this finite model.")
    print("   This illustrates, but does not by itself prove, full OS")
    print("   reflection positivity for the target H(4) fermion action.")
    for (Kx, Kt) in [(0.4, 0.4), (0.3, 0.5), (0.44068, 0.44068)]:
        pos, m = gaps(10, Kx, Kt)
        print(f"   Kx={Kx:.3f} Kt={Kt:.3f}  all eigenvalues>0: {pos}   gaps: "
              f"{m[0]:.4f}, {m[1]:.4f}, {m[2]:.4f}")

    print("\nB) EXACT AXIS INDEPENDENCE: one Euclidean system, two slicings, one Z.")
    print("   Tr T_t^Lt (dim 2^Lx)  ==  Tr T_x^Lx (dim 2^Lt)  to machine precision:")
    for (Lx, Lt, Kx, Kt) in [(8,10,0.35,0.52),(6,12,0.3,0.61668),(9,7,0.45,0.25)]:
        wt = np.linalg.eigvalsh(transfer_matrix(Lx, Kx, Kt))
        wx = np.linalg.eigvalsh(transfer_matrix(Lt, Kt, Kx))
        lt = np.log(np.sum(wt**Lt)); lx = np.log(np.sum(wx**Lx))
        print(f"   Lx={Lx} Lt={Lt}: logZ_t={lt:.12f} logZ_x={lx:.12f} |diff|={abs(lt-lx):.1e}")
    print("   NOTE: the exact statement is Z-equality. Excited-gap RATIOS between")
    print("   slicings need NOT match off criticality at finite L (momentum modes,")
    print("   anisotropic velocity); an earlier draft tested ratios and saw a")
    print("   deviation GROWING with L (2%->7%, L=6->12) -- that was a wrong test,")
    print("   not a failure of axis independence. Recorded as a design lesson.")

    print("\nC) RECONSTRUCTION QUALITY: at the exact anisotropic critical line")
    print("   sinh(2Kx)sinh(2Kt)=1, the derived H must be a c=1/2 CFT Hamiltonian:")
    Kx = 0.3; Kt = 0.5*np.arcsinh(1/np.sinh(2*Kx))
    print(f"   critical pair Kx={Kx}, Kt={Kt:.5f}")
    for L in (6, 8, 10, 12):
        _, m = gaps(L, Kx, Kt, n=2)
        print(f"    L={L:3d}   m1*L = {m[0]*L:.4f}   m2/m1 = {m[1]/m[0]:.4f}")
    print("   m1*L -> const: derived H is gapless/critical (1/L scaling).")
    print("   m2/m1 -> 8: the Ising CFT operator-dimension ratio x_eps/x_sigma")
    print("   = 1/(1/8) = 8. The derived H reproduces the tested low-lying Ising-CFT scaling")
    print("   dimensions in this finite-size probe. (An earlier draft comment predicted '->2'; the data said 8,")
    print("   and 8 is the correct CFT value -- comment corrected to follow data.)")

# ---------------------------------------------------------------------------
# STATUS: EXPLORATORY / non-canonical. Not preregistered, not adopted.
# WHAT IT SHOWS (P2-LATTICE-ONTOLOGY-01 §1b, numerically, in 2D Ising):
#   1. A pure configuration-weight system yields a POSITIVE transfer matrix
#      (transfer-matrix positivity manifest for this Ising construction) => a self-adjoint derived Hamiltonian
#      exists though none was input.
#   2. Axis independence holds EXACTLY at the partition-function level
#      (machine precision), the correct formulation of "any axis is time".
#   3. At the known critical line the derived H shows finite-size spectral behaviour
#      consistent with the expected c=1/2 Ising CFT (m1*L const; m2/m1 -> 8
#      = x_eps/x_sigma): reconstruction reproduces
#      the expected low-energy Ising Hamiltonian spectrum, not merely an
#      arbitrary positive generator.
# WHAT IT DOES NOT SHOW: this is 2D Ising (bosonic spins), not H(4) fermions;
#   fermionic reconstruction adds Grassmann/doubling structure; nothing here
#   involves geometry response or gravity; it illustrates the internal viability of the ontology's
#   FORMULATION claim (§1b) in a finite 2D bosonic example, not any
#   physical coefficient. Two design errors
#   made and corrected during development are recorded inline above.
# ---------------------------------------------------------------------------
