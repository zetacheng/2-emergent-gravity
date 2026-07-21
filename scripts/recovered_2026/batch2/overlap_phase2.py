import numpy as np
from overlap_phase1 import overlap_pieces, RHO
r=1.0

def bub_q0_improved(m,n):
    """q=0 bubbles with improved vertices Gamma = B (1 - D/2rho) for V,A,T; S,P as phase1."""
    p=2*np.pi*(np.arange(n)+0.5)/n
    P1,P2,P3=np.meshgrid(p,p,p,indexing='ij')
    acc={k:0.0 for k in ['S','P','V','A','T']}
    for p0 in p:
        grid=np.stack([np.full(P1.shape,p0),P1,P2,P3],axis=-1).reshape(-1,4)
        A,c,a0,b0,s,s2=overlap_pieces(grid,m)
        D=A*A+c*c*s2
        X0=(a0*A-b0*c*s2)/D; X1=(-(a0*c+b0*A))/D   # X = F S = X0 + i gs X1
        acc['S']+=np.sum(4*(X0*X0 - s2*X1*X1))
        acc['P']+=np.sum(4*(X0*X0 + s2*X1*X1))
        # improved vector: tr[g_nu X g_nu X] avg_nu ; g_nu(gs)g_nu = 2 s_nu g_nu - gs
        # tr[g_nu (X0+igsX1) g_nu (X0+igsX1)] per nu:
        #  = 4[X0^2] + (i^2) tr[g_nu gs g_nu gs] X1^2 + cross(i X0 X1)(tr[g_nu gs g_nu + g_nu g_nu gs]) 
        # cross traces vanish (odd gammas). tr[g_nu gs g_nu gs] = tr[(2 s_nu g_nu - gs)gs] = 4(2 s_nu^2 - s2)
        # per-nu: 4 X0^2 - X1^2 * 4(2 s_nu^2 - s2); avg_nu: 4[X0^2 - X1^2 (s2/2 - s2)] = 4[X0^2 + X1^2 s2/2]
        acc['V']+=np.sum(4*(X0*X0 + 0.5*s2*X1*X1))
        # improved axial g_nu g5: g5 flips X0 sign in one factor: tr -> 4[-X0^2 + X1^2 s2/2]
        acc['A']+=np.sum(4*(-X0*X0 + 0.5*s2*X1*X1))
        # improved tensor pair-avg: from Wilson-era pattern: 4[X0^2] avg (M^2 -> X0^2 role)
        acc['T']+=np.sum(4*(X0*X0))
    V=float(n)**4
    return {k:acc[k]/V for k in acc}

def Pi_spatial(m,n,kmag,ch):
    """Pi_channel at real spatial external momentum along axis 1. Improved vertices."""
    p=2*np.pi*(np.arange(n)+0.5)/n
    P1,P2,P3=np.meshgrid(p,p,p,indexing='ij')
    tot=0.0
    for p0 in p:
        grid=np.stack([np.full(P1.shape,p0),P1,P2,P3],axis=-1).reshape(-1,4)
        gq=grid.copy(); gq[:,1]+=kmag
        A,c,a0,b0,s,s2=overlap_pieces(grid,m)
        Aq,cq,a0q,b0q,sq,s2q=overlap_pieces(gq,m)
        D=A*A+c*c*s2; Dq=Aq*Aq+cq*cq*s2q
        X0=(a0*A-b0*c*s2)/D; X1=(-(a0*c+b0*A))/D
        Y0=(a0q*Aq-b0q*cq*s2q)/Dq; Y1=(-(a0q*cq+b0q*Aq))/Dq
        ssp=np.sum(s*sq,axis=1)
        if ch=='S': tot+=np.sum(4*(X0*Y0 - ssp*X1*Y1))
        elif ch=='P': tot+=np.sum(4*(X0*Y0 + ssp*X1*Y1))
    return tot/float(n)**4

def Pi_temporal_iE(m,n,E,ch):
    """continuation q0 -> iE with principal-branch sqrt in omega."""
    p=2*np.pi*(np.arange(n)+0.5)/n
    P1,P2,P3=np.meshgrid(p,p,p,indexing='ij')
    tot=0.0
    for p0 in p:
        grid=np.stack([np.full(P1.shape,p0),P1,P2,P3],axis=-1).reshape(-1,4)
        A,c,a0,b0,s,s2=overlap_pieces(grid,m)
        D=A*A+c*c*s2
        X0=(a0*A-b0*c*s2)/D; X1=(-(a0*c+b0*A))/D
        # shifted, complex p0+iE
        z=p0+1j*E
        s0=np.sin(z); s0=np.full(P1.size,s0) if np.isscalar(s0) else np.full(P1.size,s0)
        sp=np.stack([np.full(P1.size,np.sin(z)),np.sin(P1).ravel(),np.sin(P2).ravel(),np.sin(P3).ravel()],axis=-1)
        Mw=r*((1-np.cos(z))+ (1-np.cos(P1)).ravel()+(1-np.cos(P2)).ravel()+(1-np.cos(P3)).ravel())
        s2q=np.sum(sp*sp,axis=1)
        om=np.sqrt(s2q+(Mw-RHO)**2+0j)
        fac=(1-m/(2*RHO))
        Aq=fac*RHO*(1+(Mw-RHO)/om)+m; cq=fac*RHO/om
        a0q=0.5*(1-(Mw-RHO)/om); b0q=0.5/om
        Dq=Aq*Aq+cq*cq*s2q
        Y0=(a0q*Aq-b0q*cq*s2q)/Dq; Y1=(-(a0q*cq+b0q*Aq))/Dq
        ssp=np.sum(np.stack([np.sin(np.full(P1.size,p0)),np.sin(P1).ravel(),np.sin(P2).ravel(),np.sin(P3).ravel()],axis=-1)*sp,axis=1)
        if ch=='P': tot+=np.sum((4*(X0*Y0 + ssp*X1*Y1)).real)
        elif ch=='S': tot+=np.sum((4*(X0*Y0 - ssp*X1*Y1)).real)
    return tot/float(n)**4

if __name__=='__main__':
    import sys
    task=sys.argv[1]
    if task=='A':
        for m,n in [(0.0,32),(0.05,32)]:
            b=bub_q0_improved(m,n)
            print(f"m={m}: T_S={b['S']:+.5f} T_P={b['P']:+.5f} T_V={b['V']:+.5f} T_A={b['A']:+.5f} T_T={b['T']:+.5f}   V+A={b['V']+b['A']:+.2e}")
    elif task=='B':
        m,n=0.1,32
        Zs=-(Pi_spatial(m,n,0.2,'P')-Pi_spatial(m,n,1e-6,'P'))/0.2**2
        Zt=(Pi_temporal_iE(m,n,0.2,'P')-Pi_temporal_iE(m,n,1e-6,'P'))/0.2**2
        print(f"P-channel m={m}: Z_spatial={Zs:+.5f}  Z_temporal(iE)={Zt:+.5f}  ratio={Zt/Zs:+.4f}  [hypercubic symmetry demands 1]")
    elif task=='C':
        n=32
        for mdyn in [0.1,0.2]:
            PiP0=Pi_spatial(mdyn,n,1e-6,'P'); G=1.0/PiP0     # Goldstone condition
            PiS0=-Pi_spatial(mdyn,n,1e-6,'S')                 # physical Pi_S = -T_S
            k1,k2=0.15,0.25
            Zs=-((-Pi_spatial(mdyn,n,k2,'S'))-PiS0)/k2**2
            Zs1=-((-Pi_spatial(mdyn,n,k1,'S'))-PiS0)/k1**2
            Zphys=Zs1  # small-k value
            msig2=(1.0/G-PiS0)/Zphys
            print(f"m_dyn={mdyn}: G={G:.3f}  Pi_S(0)={PiS0:+.5f}  Z_S={Zphys:+.5f}(k={k1}) {Zs:+.5f}(k={k2})  m_sigma^2={msig2:+.5f} vs 4m^2={4*mdyn**2:.4f}  ratio={msig2/(4*mdyn**2):+.3f}")
