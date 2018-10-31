#-*-coding:utf8;-*-

from Algebra import DualNum as dual
import math as rm

class D(dual):
    def __init__(self, fst = 0, snd = 0, pair = None, cpy = None):
        super(D, self).__init__(fst, snd, pair)
        if cpy != None: self = cpy    

    @classmethod
    def new(cls, fst = 0, snd = 0, pair = None, cpy = None):
        return D(fst, snd)

    def __truediv__(self, other): # (u/v)' = (u'v - v'u)/v^2
        if type(self) != type(other):
            other = D(other)
        return D(self.R() / other.R(), (self.I()*other.R() - other.I()*self.R())/(other.R()**2))
    def __rtruediv__(self, other): #other/self
        if type(self) != type(other):
            other = D(other)
        return D(other.R() / self.R(), (other.I()*self.R() - self.I()*other.R())/(self.R()**2))
        #return self * D(1/other.R(), -(other.I())/(other.R()**2))
    def __pow__(self, other):
        if type(other) == type(self):
            pass
        else:
            return D(self.R() ** other, other * self.R()**(other-1) * self.I()) # (f^n)' = nf^(n-1)*f'

    #trigonometry
    def acos(self):
        return D(rm.acos(self.R()), -1 / rm.sqrt(1 - self.R()**2) * self.I()) 
    def acosh(self):
        return D(rm.acosh(self.R()), 1 / rm.sqrt(self.R()**2 - 1) * self.I())
    def asin(self):
        return D(rm.asin(self.R()), 1 / rm.sqrt(1 - self.R()**2) * self.I())
    def asinh(self):
        return D(rm.asinh(self.R()), 1 / rm.sqrt(self.R()**2 + 1) * self.I())
    def atan(self):
        return D(rm.atan(self.R()), 1 / (self.R()**2 + 1) * self.I())
    def atanh(self):
        return D(rm.atanh(self.R()), 1 / (1 - self.R()**2) * self.I())
    def cos(self):
        return D(rm.cos(self.R()), - rm.sin(self.R()) * self.I())
    def cosh(self):
        return D(rm.cosh(self.R()), rm.sinh(self.R()) * self.I())
    def sin(self):
        return D(rm.sin(self.R()), rm.cos(self.R()) * self.I())
    def sinh(self):
        return D(rm.sinh(self.R()), rm.cosh(self.R()) * self.I())
    def tan(self):
        return D(rm.tan(self.R()), 1 / rm.cos(self.R())**2 * self.I())
    def tanh(self):
        return D(rm.tanh(self.R()), 1 / rm.cosh(self.R()) ** 2 * self.I())
    def cot(self):
        return cos(self)/sin(self)


    def sqrt (self): #(sqrt(x))'=1/2sqrt(x)
        return D(rm.sqrt(self.R()), 0.5*self.I()/rm.sqrt(self.R()))
    def exp (self):
        return D(rm.exp(self.R()), rm.exp(self.R())*self.I())
    def log (self):
        return D(rm.log(self.R()), self.I()/self.R())

    
class Df:
    def get_pair(self, f, x):
        return f(*(map(lambda p: D(p,1), x))).tpl()
    def __call__(self, f, x):
        return f(*(map(lambda p: D(p,1), x))).I()
    
def dfdarg(f, args):
    return Df()(f, args)
    

###LINKS to functions    

pow = D.__pow__
acos = D.acos
acosh = D.acosh
asin = D.asin
asinh = D.asinh
atan = D.atan
atanh = D.atanh
cos = D.cos
cosh = D.cosh
sin = D.sin
sinh = D.sinh
tan = tg = D.tan
tanh = D.tanh
cot = ctg = D.cot
sqrt = D.sqrt
exp = D.exp
ln = log = D.log
lg = lambda x: ln(x) / D(rm.log(10))
pi = D(rm.pi, 0)
e = D(rm.e, 0)