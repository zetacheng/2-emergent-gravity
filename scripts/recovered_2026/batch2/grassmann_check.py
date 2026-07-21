import numpy as np
from itertools import product
from fierz_verify import basis, g, g5  # reuse matrices

# Grassmann engine: operators = dict{ (sorted generator tuple with sign) : coeff }
# generators: psi_0..psi_{4N-1}, psibar_0..: encode as ints; psibar = 100+i
def normal_order(term):
    """term: (tuple_of_gens, coeff). Bubble-sort to canonical order, tracking sign."""
    gens, c = list(term[0]), term[1]
    n=len(gens); sign=1
    for i in range(n):
        for j in range(n-1-i):
            if gens[j] > gens[j+1]:
                gens[j],gens[j+1]=gens[j+1],gens[j]
                sign=-sign
            elif gens[j]==gens[j+1]:
                return None  # nilpotent
    return (tuple(gens), sign*c)

def add(D, gens, c):
    t = normal_order((gens,c))
    if t is None: return
    D[t[0]] = D.get(t[0],0)+t[1]

def bilinear_pair_expand(M1, M2, N):
    """expand (psibar M1 psi)(psibar M2 psi) with flavor-singlet bilinears, N flavors.
    generator encoding: psi_{a,i} -> 4*a+i ; psibar_{a,i} -> 1000+4*a+i"""
    D={}
    for a in range(N):
        for b in range(N):
            for i,j,k,l in product(range(4),repeat=4):
                c = M1[i,j]*M2[k,l]
                if abs(c)<1e-14: continue
                gens=(1000+4*a+i, 4*a+j, 1000+4*b+k, 4*b+l)
                add(D, gens, c)
    return D

def exchange_expand(N):
    """4 * sum_ab (psibar_a psi_b)(psibar_b psi_a)"""
    D={}
    for a in range(N):
        for b in range(N):
            for i,j in product(range(4),repeat=2):
                gens=(1000+4*a+i, 4*b+i, 1000+4*b+j, 4*a+j)
                add(D, gens, 4.0)
    return D

def dsub(D1,D2):
    D=dict(D1)
    for k,v in D2.items(): D[k]=D.get(k,0)-v
    return {k:v for k,v in D.items() if abs(v)>1e-10}

for N in [1,2]:
    total={}
    for lab,B in basis:  # hermitian orthonormal 16
        Dx = bilinear_pair_expand(B,B,N)
        for k,v in Dx.items(): total[k]=total.get(k,0)+v
    total={k:v for k,v in total.items() if abs(v)>1e-10}
    diffP = dsub(total, exchange_expand(N))
    diffM = dsub(total, {k:-v for k,v in exchange_expand(N).items()})
    print(f"N={N}: Sum_A (pbar G_A p)^2  ==  +4 Sum_ab exchange: {len(diffP)==0};   == -4 Sum_ab: {len(diffM)==0}")
