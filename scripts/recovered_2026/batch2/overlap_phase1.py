import numpy as np
from fierz_verify import g, g5

RHO=1.0; r=1.0
GM=[g[1],g[2],g[3],g[4]]

def overlap_pieces(p4grid, m):
    """p4grid: (K,4) momenta. Returns A,c (S=(A - i c g.s)/(A^2+c^2 s^2)),
    plus a0,b0 for F = a0 - i b0 g.s, and s vector."""
    s=np.sin(p4grid)                       # (K,4)
    Mw=r*np.sum(1-np.cos(p4grid),axis=1)   # (K,)
    s2=np.sum(s*s,axis=1)
    om=np.sqrt(s2+(Mw-RHO)**2)
    A0=RHO*(1+(Mw-RHO)/om); c0=RHO/om     # massless D_ov = A0 + i c0 g.s
    fac=(1-m/(2*RHO))
    A=fac*A0+m; c=fac*c0                   # massive D(m)
    a0=0.5*(1-(Mw-RHO)/om); b0=0.5/om      # F = 1 - D_ov/(2 rho)
    return A,c,a0,b0,s,s2

def gw_check():
    rng=np.random.default_rng(2); ok=True
    for _ in range(6):
        p=rng.uniform(-np.pi,np.pi,4)
        s=np.sin(p); Mw=r*np.sum(1-np.cos(p)); om=np.sqrt(s@s+(Mw-RHO)**2)
        Dov=RHO*((1+(Mw-RHO)/om)*np.eye(4)+1j*sum(s[i]*GM[i] for i in range(4))/om)
        lhs=g5@Dov+Dov@g5; rhs=(1.0/RHO)*Dov@g5@Dov
        ok&=np.allclose(lhs,rhs)
        # continuum limit
    p=np.array([0.01,0.02,-0.015,0.005])
    s=np.sin(p); Mw=r*np.sum(1-np.cos(p)); om=np.sqrt(s@s+(Mw-RHO)**2)
    Dov=RHO*((1+(Mw-RHO)/om)*np.eye(4)+1j*sum(s[i]*GM[i] for i in range(4))/om)
    cont=1j*sum(p[i]*GM[i] for i in range(4))
    return ok, np.linalg.norm(Dov-cont)/np.linalg.norm(cont)

def bubbles_q0(m,n):
    """criticality map at q=0 with improved S,P vertices and plain V,A,T."""
    p=2*np.pi*(np.arange(n)+0.5)/n         # half-shifted grid avoids p=0 zero mode
    acc={k:0.0 for k in ['S','P','V','A','T','tad']}
    P1,P2,P3=np.meshgrid(p,p,p,indexing='ij')
    for p0 in p:
        grid=np.stack([np.full(P1.shape,p0),P1,P2,P3],axis=-1).reshape(-1,4)
        A,c,a0,b0,s,s2=overlap_pieces(grid,m)
        D=A*A+c*c*s2
        # S(p) = (A - i c g.s)/D ; F = a0 - i b0 g.s ; vertices:
        # T_S = tr[F S F S]; T_P = tr[g5 F S g5 F S]
        # scalar algebra: let X = F S = (a0 - i b0 gs)(A - i c gs)/D
        #  = [a0 A - b0 c s2] /D + i gs[-a0 c - b0 A]/D  (using (gs)^2=s2)
        X0=(a0*A-b0*c*s2)/D; X1=(-(a0*c+b0*A))/D    # X = X0 + i gs X1
        # tr[X X] = 4(X0^2 - s2 X1^2) ; tr[g5 X g5 X] with g5 gs g5=-gs: 4(X0^2 + ... sign)
        acc['S']+=np.sum(4*(X0*X0 - s2*X1*X1))
        # P: g5 F S g5 F S: g5 X g5 = X0 - i gs X1 -> tr[(X0-igsX1)(X0+igsX1)] = 4(X0^2+s2 X1^2)
        acc['P']+=np.sum(4*(X0*X0 + s2*X1*X1))
        # V (nu-averaged, plain gamma_mu): tr[g_nu S g_nu S]:
        # S = S0 + i gs S1, S0=A/D, S1=-c/D
        S0=A/D; S1=-c/D
        # g_nu (i gs) g_nu summed/4: as before avg: tr -> 4(S0^2 + s2/2 * S1^2 *? )
        # from Wilson-era algebra: numerator (s2/2 + M^2)-pattern generalizes:
        # tr[g_nu S g_nu S] avg_nu = 4(S0^2 + S1^2*(s2 - 2*s2/4*2)/1) -- do directly:
        # g_nu gs g_nu (fixed nu) = 2 s_nu g_nu - gs ; average over nu:
        # tr avg = 4[S0^2 - S1^2*(avg(2 s_nu^2) - s2)] = 4[S0^2 - S1^2*(s2/2 - s2)] = 4[S0^2 + S1^2 s2/2]
        acc['V']+=np.sum(4*(S0*S0 + 0.5*s2*S1*S1))
        acc['A']+=np.sum(4*(-S0*S0 + 0.5*s2*S1*S1))
        acc['T']+=np.sum(4*(S0*S0))   # pair-averaged tensor: M^2-pattern -> S0^2
        acc['tad']+=np.sum(4*X0)      # improved condensate tadpole tr[F S]
    V=float(n)**4
    return {k:acc[k]/V for k in acc}

ok,cerr=gw_check()
print(f"GW relation (6 random momenta): {ok};  continuum-limit relative error at |p|~0.03: {cerr:.2e}")
for m,n in [(0.0,32),(0.0,48),(0.02,32),(0.05,32)]:
    b=bubbles_q0(m,n)
    print(f"m={m} n={n}: T_S={b['S']:.5f} T_P={b['P']:.5f} (S-P={b['S']-b['P']:+.2e})  T_V={b['V']:.5f} T_A={b['A']:.5f} T_T={b['T']:.5f}  tad={b['tad']:.5f}")

# Z_S sign via real spatial momentum (no analytic continuation needed)
def PiS_spatial(m,n,kmag):
    p=2*np.pi*(np.arange(n)+0.5)/n
    P1,P2,P3=np.meshgrid(p,p,p,indexing='ij')
    tot=0.0
    for p0 in p:
        grid=np.stack([np.full(P1.shape,p0),P1,P2,P3],axis=-1).reshape(-1,4)
        gridq=grid.copy(); gridq[:,1]+=kmag
        A,c,a0,b0,s,s2=overlap_pieces(grid,m)
        Aq,cq,a0q,b0q,sq,s2q=overlap_pieces(gridq,m)
        D=A*A+c*c*s2; Dq=Aq*Aq+cq*cq*s2q
        X0=(a0*A-b0*c*s2)/D; X1=(-(a0*c+b0*A))/D
        Y0=(a0q*Aq-b0q*cq*s2q)/Dq; Y1=(-(a0q*cq+b0q*Aq))/Dq
        ssp=np.sum(s*sq,axis=1)
        tot+=np.sum(4*(X0*Y0 - ssp*X1*Y1))
    return tot/float(n)**4
m,n=0.05,32
Pi0=PiS_spatial(m,n,0.0)
for k in [0.2,0.3]:
    Zs=-(PiS_spatial(m,n,k)-Pi0)/k**2
    print(f"Z_S(spatial, overlap) m={m} k={k}: {Zs:+.5f}   [Wilson value was NEGATIVE ~ -0.066]")
