import numpy as np
from itertools import product
from fierz_verify import basis, g, g5
np.set_printoptions(precision=4, suppress=True)

# ---- charge conjugation: C gamma_mu C^-1 = -gamma_mu^T ----
C = g[2]@g[4]
ok=all(np.allclose(C@g[mu]@np.linalg.inv(C), -g[mu].T) for mu in range(1,5))
print("C = g2 g4 satisfies C gmu C^-1 = -gmu^T:", ok, "| C antisymmetric:", np.allclose(C.T,-C))

# ---- identity check: C S(-p)^T C^-1 = S(p) for Wilson (numeric spot check) ----
def Sprop(p, m=0.3, r=1.0):
    s=sum(np.sin(p[mu-1])*g[mu] for mu in range(1,5))
    M=m+r*sum(1-np.cos(p[mu-1]) for mu in range(1,5))
    A=-1j*s+M*np.eye(4)
    return np.linalg.inv(A) @ np.eye(4) * 1.0 if False else np.linalg.inv((-1j*s+M*np.eye(4)))
rng=np.random.default_rng(1)
ok2=True
for _ in range(5):
    p=rng.uniform(-np.pi,np.pi,4)
    lhs=C@Sprop(-p).T@np.linalg.inv(C); rhs=Sprop(p)
    ok2 &= np.allclose(lhs,rhs)
print("C S(-p)^T C^-1 = S(p) (Wilson, incl. mass+r):", ok2)

# ---- pairing basis for N=1: antisymmetric C*Gamma ----
pair_ch=[]
for lab,B in basis:
    CB=C@B
    if np.allclose(CB.T,-CB): pair_ch.append((lab,B))
print("antisymmetric pairing channels (N=1):", [l for l,_ in pair_ch])

# ---- Grassmann engine (4 components, N=1) ----
def norm(term):
    gens,c=list(term[0]),term[1]; sign=1
    for i in range(len(gens)):
        for j in range(len(gens)-1-i):
            if gens[j]>gens[j+1]: gens[j],gens[j+1]=gens[j+1],gens[j]; sign=-sign
            elif gens[j]==gens[j+1]: return None
    return (tuple(gens),sign*c)
def add(D,gens,c):
    t=norm((gens,c))
    if t: D[t[0]]=D.get(t[0],0)+t[1]
# psi_i -> i ; psibar_i -> 100+i
def ph_quartic(M1,M2):
    D={}
    for i,j,k,l in product(range(4),repeat=4):
        c=M1[i,j]*M2[k,l]
        if abs(c)>1e-14: add(D,(100+i,j,100+k,l),c)
    return D
def pair_quartic(B1,B2):
    """(psibar B1 C psibar^T)(psi^T C B2 psi)"""
    D={}
    A1=B1@C; A2=C@B2
    for i,j,k,l in product(range(4),repeat=4):
        c=A1[i,j]*A2[k,l]
        if abs(c)>1e-14: add(D,(100+i,100+j,k,l),c)
    return D
def tovec(D,keys): return np.array([D.get(k,0) for k in keys],dtype=complex)

# L_int quartic part: (pbar p)^2 + (pbar i g5 p)^2
L={}
for M in [np.eye(4), 1j*g5]:
    Dx=ph_quartic(M,M)
    for k,v in Dx.items(): L[k]=L.get(k,0)+v
keys=sorted(set(L)|{k for a,_ in pair_ch for b,_ in pair_ch for k in pair_quartic(_ ,_)})
# build full key set from all pairing quartics
allD=[]; labels=[]
for (la,Ba) in pair_ch:
    for (lb,Bb) in pair_ch:
        allD.append(pair_quartic(Ba,Bb)); labels.append((la,lb))
keys=sorted(set().union(*[set(d) for d in allD], set(L)))
Amat=np.array([tovec(d,keys) for d in allD]).T
bvec=tovec(L,keys)
coef,res,rank,_=np.linalg.lstsq(Amat,bvec,rcond=None)
resid=np.linalg.norm(Amat@coef-bvec)
print(f"exact decomposition residual: {resid:.2e} (rank {rank}/{len(labels)})")
print("\nnonzero pairing coefficients of (pbar p)^2+(pbar i g5 p)^2:")
for (la,lb),c in zip(labels,coef):
    if abs(c)>1e-10:
        d = '(diag)' if la==lb else ''
        print(f"  ({la},{lb}): {c.real:+.4f}{'' if abs(c.imag)<1e-10 else f' {c.imag:+.4f}i'} {d}")
