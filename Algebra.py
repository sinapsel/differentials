#-*-coding:utf8;-*-

from Pair import Pair as num

class DualNum(num): #< <N, N>, +, *>
    def __init__(self, fst = 0, snd = 0, pair = None, cpy = None):
        super().__init__(fst, snd, pair)
        if cpy != None: self = cpy
        self.R = self.real = self.fst
        self.I = self.imaginary = self.snd
    
    @classmethod
    def is_parent(cls, a, b):
        return (b.__class__).__bases__[0] == a.__class__
    @classmethod
    def relative(cls, a, b): # <siblings | child | parent | aliens>
        return [a,b] if type(a) == type(b) else [b] if a.is_parent(a,b) else [a] if a.is_parent(b,a) else None
    @classmethod
    def new(cls, fst = 0, snd = 0, pair = None, cpy = None):
        return DualNum(fst, snd)

    def __add__(self, other):
        if self.relative(self, other) == None:
            other = self.new(other)
        return self.relative(self, other)[0].new(self.R()+other.R(), self.I() + other.I())
        #return DualNum(pair = tuple(map(lambda x,y: x+y, self.tpl(), other.tpl())))
    def __neg__(self):
        return self.new(-self.R(), -self.I())
    def __mul__(self, other):
        if self.relative(self, other) == None:
            other = self.new(other)
        return self.relative(self, other)[0].new(self.R() * other.R(), self.I()*other.R() + self.R()*other.I())
    def __truediv__(self, other): # (u/v)' = (u'v - v'u)/v^2
        if self.relative(self, other) == None:
            other = self.new(other)
        return self.relative(self, other)[0].new(self.R() / other.R(), (self.I()*other.R() - other.I()*self.R())/(other.R()**2))



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
