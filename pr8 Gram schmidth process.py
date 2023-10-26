#find inner product of two vectors
def ips(x,y):
    p = 0
    for i in range(len(x)):
        p+= x[i]*y[i]
    return p

#find a norm of vector
def norm(x):
    import math as m
    nrm = m.sqrt(ips(x,x))
    return nrm

#find unit vector corresponding to given vector
def unit(u):
    p = [0]*len(u)
    for i in range(len(u)):
        p[i] = u[i]/norm(u)
    return p

#find projection of v on u
def proj(v,u):
    t = ips(u,v)/ips(u,u)
    p = [0]*len(u)
    for i in range(len(u)):
        p[i] = t*u[i]
    return p

#find orthogonal basis using gram schmidth process
def sub(u,v):
    p = [0]*len(u)
    for i in range(len(u)):
        p[i] = v[i]
    return p
def GSP(v):
    u = [0]*len(v)
    u[0] = v[0]
    for k in range(1,len(v)):
        s = v[k]
        for j in range(0,k):
            s = sub(s,proj(v[k],u[j]))
        u[k] = s
    un = [0]*len(v)
    for i in range(len(v)):
            un[i] = unit(u[i])
    return un

