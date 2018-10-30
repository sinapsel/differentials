class Matrix:
    def __init__(self, arr = [[0]], shape = (1,1), n = 1, m = 1, init_value = 0, cpy = None):
        if cpy != None:
            self._arr = cpy._arr
            self._n = cpy._n
            self._m = cpy._m
        elif arr != [[0]]:
            self._arr = arr
            self._n = len(arr)
            self._m = len(arr[0])
        else:
            if m == 1 and n == 1:
                m, n = shape
            self._arr = [[init_value for j in range(m)] for i in range(n)]
            self._n = n
            self._m = m
            
    def __str__(self):
        ss = ''
        if self._n >= 2:
            start = '/' + ' '.join(map(str, self._arr[0])) + '\\\n'
            end = '\\' + ' '.join(map(str, self._arr[self._n - 1])) + '/\n'
            bdy = ''.join(['|' + ' '.join(map(str, self._arr[i])) + '|\n' for i in range(1, self._n - 1)])
            ss = start + bdy + end
        else:
            ss = '<' + ' '.join(map(str, self._arr[0])) + '>\n'
        return ss
    def __repr__(self):
        return self._arr.__repr__()
    def shape(self):
        return (self._n, self._m)
    @classmethod    
    def unit(cls, n):
        return Matrix(arr = [[1 * int(i == j) for j in range(n)] for i in range(n)])
    @classmethod
    def zero(cls, n):
        return Matrix(arr = [[0 for j in range(n)] for i in range(n)])
    @classmethod
    def rndint(cls, shape, M):
        from random import randint as r
        return Matrix(arr = [[r(0,M) for j in range(shape[1])] for i in range(shape[0])])
        
    def set_eig(self):
        self._arr = [ [1 * int(i == j) for j in range(self._m)] for i in range(self._n)]
    def set_ouh(self):
        self._arr = [ [0 for j in range(self._m)] for i in range(self._n)]
    
    def T(self):
        return Matrix(arr = list(map(list, zip(*self._arr))))
    @classmethod
    def scalar(cls, a, b):
        return sum(map(lambda x: x[0]*x[1], list(map(list, zip(a,b)))))
    
    def __add__(self, other):
        if self.shape() == other.shape():
            return Matrix(arr = list(map(lambda x,y: list(map(lambda x,y: x + y, x, y)), self._arr, other._arr)))
        else:
            raise ValueError
    def __mul__(self, other):
        if type(other) == type(self):
            if self.shape()[1] == other.shape()[0]: #MxN * PxQ = MxQ, N = P
                return Matrix(arr = [[Matrix.scalar(i, j) for j in other.T()._arr] for i in self._arr])
                #rO = other.T()._arr
                #return Matrix(arr = list(map(lambda x: list(map(lambda y: Matrix.scalar(x,y), rO)), self._arr)))
            else:
                raise ValueError
        else:
            return Matrix(arr = list(map(lambda x: list(map(lambda x: x * other, x)), self._arr)))
    
    def __truediv__(self, other):
        return self * other ** -1
    
    def __neg__(self):
        return self * (-1)
    def __sub__(self, other):
        return self + (-other)
    
    def __radd__(self, other):  # a + b
        return self + other
    def __rsub__(self, other):  # a - b
        return other + (- self)
    def __rmul__(self, other):  # a * b
        return self * other
        
    def __iadd__(self, other):  # a += b
        self = self + other
        return self
    def __isub__(self, other):  # a -= b
        self = self - other
        return self
    def __imul__(self, other):  # a *= b
        self = self * other
        return self
    
    def __lt__
