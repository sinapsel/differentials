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


def gradient_descent(f, start = (0,), domain=((0,1),), eps = 1e-6, l = 1):
    point_0 = start
    grad = gradient(f, point_0)
    while rm.sqrt(sum(map(lambda x: x*x , grad))) > eps and sum(map(lambda x, y: x <= y[1] and x >= y[0], point_0, domain)) == len(start):
        point_0 = tuple([x - l * gradfx for x, gradfx in list(zip(point_0, grad)) ])
        grad = gradient(f, point_0)
        #point_0 = point_0 - l * gradient(f, point_0)
    return point_0



def root(f, domain = ((0,100), ), eps = 1e-3):
    pass

def root1a(f, domain = (0,100), eps = 1e-3,  method = newtonraphson):
    return method(f = f, domain = domain, eps = eps)

def optimum(f, method):
    return method(f)
