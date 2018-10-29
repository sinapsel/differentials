#-*-coding:utf8;-*-

from Pair import Pair as num

class DualNum(num): #< <N, N>, +, *>
    def __init__(self, fst = 0, snd = 0, pair = None, cpy = None):
        super().__init__(fst, snd, pair)
        if cpy != None: self = cpy
        self.R = self.real = self.fst
        self.I = self.imaginary = self.snd
        
    def __add__(self, other):
        if type(self) != type(other): # other in N
            other = DualNum(other) # (c)' = 0
        return DualNum(self.R()+other.R(), self.I() + other.I())
        #return DualNum(pair = tuple(map(lambda x,y: x+y, self.tpl(), other.tpl())))
    def __neg__(self):
        return DualNum(pair = tuple(map(lambda x: -x, self.tpl())))
    def __mul__(self, other):
        if type(self) != type(other):
            other = DualNum(other)
        return DualNum(self.R() * other.R(), self.I()*other.R() + self.R()*other.I())
    def __truediv__(self, other): # (u/v)' = (u'v - v'u)/v^2
        if type(self) != type(other):
            other = DualNum(other)
        return DualNum(self.R() / other.R(), (self.I()*other.R() - other.I()*self.R())/(other.R()**2))

    def __sub__(self, other):   # a - b = a + (-b)
        return self + (-other)
    
    def __radd__(self, a):      # b + a = a + b
        return self + a
    def __rsub__(self, a):      # b - a = a + (-b)
        return a + (-self)
    def __rmul__(self, a):      # b * a = a * b
        return self * a
        
    def __iadd__(self, a):      # a += b
        self = self + a
        return self
    def __isub__(self, a):      # a -= b
        self = self - a
        return self
    def __imul__(self, a):      # a *= b
        self = self * a
        return self
