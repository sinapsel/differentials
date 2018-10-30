from Differential import *

def newtonraphson(f, domain = (0,100), eps = 1e-3):
    a, b = domain
    x_0 = (a+b)/2
    while abs(f(x_0)) > eps or x_0 == 0 and (x_0 >= a and b >= x_0):
        u, v = Df().get_pair(f, (x_0,))
        if v == 0:
            if u == 0: return x_0
            v += eps
        x_0 -= u/v
        #print(x_0, u,v)
    return x_0 if (x_0 >= a and b >= x_0) else None




def root(f, domain = ((0,100), ), eps = 1e-3):
    pass

def root1a(f, domain = (0,100), eps = 1e-3,  method = newtonraphson):
    return method(f = f, domain = domain, eps = eps)

def optimum(f, method):
    return method(f)
