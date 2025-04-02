class Matrix22():
    
    _m = [[0.0]*2]*2


    def __init__(self, m00:float=0.0, m01:float=0.0, m10:float=0.0, m11:float=0.0):
        self._m[0][0] = m00
        self._m[0][1] = m01
        self._m[1][0] = m10
        self._m[1][1] = m11


    def multiply(self, other:'Matrix22'):

        a = self._m
        b = other._m
        c = [[0]*2]*2

        for row in range(0, 2):
            for col in range(0, 2):

                # Dot product of the row of matrix A + 
                sum = 0.0
                for iter in range(0, 2):
                    sum += a[row][iter] * b[iter][col]

                c[row][col] = sum
        
        return c


def identity():
    return Matrix22(1.0, 0.0, 0.0, 1.0)


def null():
    return Matrix22()