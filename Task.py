#-*-coding:utf8;-*-

import Methods
from Differential import *
from Methods import root1a

class Task0:
    '''
    Две машины едут вдоль прямой, одна с постоянной скоростю v = {10 км/ч}, вторая начинает с u = {1 км/ч} и постоянным ускорением в a = {0.2 км/ч}. За какое время первая машина догонит вторую, если расстояние между ними было s0 = {-5 км} (по ОХ координата первой больше)?
    '''
    def __init__(self, v = 10, u = 1, a = 0.2, s0 = -5):
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

class Task1:
    '''
        Найти минимум функции f(x) = cos(x), {-2}<=x<={15}
    '''
    def __init__(self, a = -2, b = 15):
        self.a, self.b = a, b

    '''
        Функция f(x)
    '''
    def f(self, x): return cos(x)
    '''
        Применим к фукции метод градиентного спуска и найдем min f(x) = f(argmin(x))
    '''
    def solve(self):
        a, b = self.a, self.b
        f = self.f
        self.argmin_x = Methods.gradient_descent(f, domain=((a,b),), start = ((a+b)/2,))[0] #function of one argument
        self.min_f = f(self.argmin_x)
    def __str__(self):
        self.solve()
        return 'Task:\t{task}\n\tfor f(x) = cos x, min f(x) = f ({x}) = {f}, where x in [{a};{b}]'.format(task = str(type(self)).split('.')[-1], x = self.argmin_x, f = self.min_f, a = self.a, b = self.b)
    def __call__(self):
        return str(self)


if __name__ == '__main__':
    print("T =", Task0().solve())
    print(Task1()()) #In: %timeit Task1()() Out: 1000 loops, best of 3: 497 µs per loop