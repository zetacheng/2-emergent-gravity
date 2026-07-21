import numpy as np, sys
r=1.0
def Z_pair(m,n,eps,Es=(0.01,0.02,0.03)):
    xi=1.0+eps
    p=2*np.pi*np.arange(n)/n
    p1=p.reshape(n,1,1); p2=p.reshape(1,n,1); p3=p.reshape(1,1,n)
    s1,s2_,s3=np.sin(p1),np.sin(p2),np.sin(p3)
    w_spat=(1-np.cos(p1))+(1-np.cos(p2))+(1-np.cos(p3)); V=float(n)**4
    z0V=0.0; z0D=0.0
    for p0 in p:
        s0=xi*np.sin(p0); M=m+r*(xi*(1-np.cos(p0))+w_spat)
        D=s0**2+s1**2+s2_**2+s3**2+M**2; w=1.0/(D*D)
        ss=s0**2+s1**2+s2_**2+s3**2
        z0V+=np.sum(w*4*(ss-2*s2_**2+M*M)); z0D+=np.sum(w*8*s2_**2)
    z0V/=V; z0D/=V
    out={}
    for d in ['t','s']:
        ZV=[];ZD=[]
        for E in Es:
            aV=0.0;aD=0.0
            for p0 in p:
                s0=xi*np.sin(p0); M=m+r*(xi*(1-np.cos(p0))+w_spat)
                D=s0**2+s1**2+s2_**2+s3**2+M**2
                if d=='t':
                    z=p0+1j*E; s0p=xi*np.sin(z); s1p=s1
                    Mp=m+r*(xi*(1-np.cos(z))+w_spat)
                else:
                    s0p=s0; s1p=np.sin(p1+E)
                    Mp=m+r*(xi*(1-np.cos(p0))+(1-np.cos(p1+E))+(1-np.cos(p2))+(1-np.cos(p3)))
                Dp=s0p**2+s1p**2+s2_**2+s3**2+Mp**2; w=1.0/(D*Dp)
                ss=s0*s0p+s1*s1p+s2_**2+s3**2
                aV+=np.sum(w*4*(ss-2*s2_**2+M*Mp)).real
                aD+=np.sum(w*8*s2_**2).real
            ZV.append((aV/V-z0V)/E**2); ZD.append((aD/V-z0D)/E**2)
        E2=np.array(Es)**2; A=np.vstack([np.ones(3),E2]).T
        out[d]=(np.linalg.lstsq(A,np.array(ZV),rcond=None)[0][0],
                np.linalg.lstsq(A,np.array(ZD),rcond=None)[0][0])
    return out
def sigma_direct(m,n,eps=0.05):
    o0=Z_pair(m,n,0.0); o1=Z_pair(m,n,eps)
    def sig(o):
        ZVt,dZt=o['t']; ZVs,dZs=o['s']; ZVs=-ZVs; dZs=-dZs
        ZPt=ZVt+dZt
        return (dZs*ZVt - dZt*ZVs)/(ZPt*ZVs)
    return (sig(o1)-sig(o0))/eps
if __name__=='__main__':
    m=float(sys.argv[1]); n=int(sys.argv[2])
    print(f"m={m} n={n}: sigma_PV(direct) = {sigma_direct(m,n):+.5f}", flush=True)
