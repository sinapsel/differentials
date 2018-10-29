#-*-coding:utf8;-*-

from Num import Numer as N

class Pair:
    def __init__(self, fst = 0, snd = 0, pair = None):
        if pair != None:
            fst, snd = pair
        self.pair = (fst, snd)
    def fst(self):
        return self.pair[0]
    def snd(self):
        return self.pair[1]
    def tpl(self):
        return self.pair
    def __str__(self):
        return '<{fst} {snd}>'.format(fst = self.fst(), snd = self.snd())
    def __repr__(self):
        return (self.fst(), self.snd()).__repr__()
