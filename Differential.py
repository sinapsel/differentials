#-*-coding:utf8;-*-

from Algebra import DualNum as dual
import math as rm

class D(dual):
    def __init__(self, fst = 0, snd = 0, pair = None, cpy = None):
        super().__init__(fst, snd, pair)
        if cpy != None: self = cpy    
    def __truediv__(self, other): # (u/v)' = (u'v - v'u)/v^2
        #return D(self.R() / other.R(), (self.I()*other.R() - other.I()*self.R())/(other.R()**2))
        return self * D(1/other.R(), -(other.I())/(other.R()**2))
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
    def __call__(self, f, x):
        return f(*(map(lambda p: D(p,1), x))).I()
    
def dfdx(f, x):
    return Df()(f, x)

    
pow = D.__pow__
sqrt = D.sqrt
sin = D.sin
cos = D.cos
tan = tg = D.tan
cot = ctg= D.cot
exp = D.exp
ln = log = D.log
