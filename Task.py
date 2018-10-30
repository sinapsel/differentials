#-*-coding:utf8;-*-

import Methods
from Methods import root1a

class Task0:
    '''
    Две машины едут вдоль прямой, одна с постоянной скоростю v = {10 км/ч}, вторая начинает с u = {1 км/ч} и постоянным ускорением в a = {0.2 км/ч}. За какое время первая машина догонит вторую, если расстояние между ними было s0 = {5 км} (по ОХ координата первой больше)?
    '''
    def __init__(self, v, u, a, s0):
        self.v, self.u, self.a, self.s0 = v, u, a, s0
    
    '''
    x1(t) = vt
    x2(t) = s0 + ut + a*t^2/2
    x1(T) = x2(T), s0 + (u-v)T + a*T^2/2 = 0 where T is variable
    Найдем корни функции phi(T) = a*T^2/2 + (u-v)*T + s0 = 0, где T больше 0 
    '''
    def solve(self):
        v, u, a, s0 = self.v, self.u, self.a, self.s0
        return root1a(f = lambda T: 0.5*a * T ** 2 + (u - v)*T + s0, method = Methods.newtonraphson, domain = (0,1e10))

if __name__ == '__main__':
    Task0(10, 1, 0.2, 5).solve()
