#-*-coding:utf8;-*-

from Algebra import DualNum as dual
import math as rm

class D(dual):
    def __init__(self, fst = 0, snd = 0, pair = None, cpy = None):
        super().__init__(fst, snd, pair)
        if cpy != None: self = cpy    
    def __truediv__(self, other): # (u/v)' = (u'v - v'u)/v^2
        if type(self) != type(other):
            other = D(other)
        return D(self.R() / other.R(), (self.I()*other.R() - other.I()*self.R())/(other.R()**2))
        #return self * D(1/other.R(), -(other.I())/(other.R()**2))
    def __pow__(self, other):
        if type(other) == type(self):
            pass
        else:
            return D(self.R() ** other, other * self.R()**(other-1) * self.I()) # (f^n)' = nf^(n-1)*f'
    def sqrt (self): #(sqrt(x))'=1/2sqrt(x)
        return D(rm.sqrt(self.R()), 0.5*self.I()/rm.sqrt(self.R()))
    def sin(self):
        return D(rm.sin(self.R()), rm.cos(self.R())*self.I())
    def cos(self):
        return D(rm.cos(self.R()), -1*rm.sin(self.R())*self.I())
    def exp (self):
        return D(rm.exp(self.R()), rm.exp(self.R())*self.I())
    def log (self):
        return D(rm.log(self.R()), self.I()/self.R())
    def tan(self):
        return sin(self)/cos(self)
    def cot(self):
        return cos(self)/sin(self)
    
class Df:
    def get_pair(self, f, x):
        return f(D(x,1)) 
    def __call__(self, f, x):
        return f(*(map(lambda p: D(p,1), x))).I()
    
def dfdarg(f, args):
    return Df()(f, args)

def root_1(f, a = -100, b = 100, eps = 0.001):
    x_0 = (a+b)/2
    while abs(f(x_0)) > eps or x_0 == 0 and (x_0 >= a and b >= x_0):
        u, v = Df().get_pair(f, x_0).tpl()
        if v == 0:
            if u == 0: return x_0
            v += eps
        x_0 -= u/v
        #print(x_0, u,v)
    return x_0
        
    
pow = D.__pow__
sqrt = D.sqrt
sin = D.sin
cos = D.cos
tan = tg = D.tan
cot = ctg= D.cot
exp = D.exp
ln = log = D.log
