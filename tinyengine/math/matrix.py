import math

class Matrix33():
    
    _m = [[0.0 for c in range(3)] for r in range(3)]

    def __init__(self, m00:float=0.0, m01:float=0.0, m02:float=0.0, m10:float=0.0, m11:float=0.0, m12:float=0.0, m20:float=0.0, m21:float=0.0, m22:float=0.0):
        self._m[0][0] = m00
        self._m[0][1] = m01
        self._m[0][2] = m02

        self._m[1][0] = m10
        self._m[1][1] = m11
        self._m[1][2] = m12

        self._m[2][0] = m20
        self._m[2][1] = m21
        self._m[2][2] = m22


    def determinant(self) -> float:
        a = self._m[0][0] * (self._m[1][1] * self._m[2][2] - self._m[1][2] * self._m[2][1])
        b = self._m[0][1] * (self._m[1][0] * self._m[2][2] - self._m[1][2] * self._m[2][0])
        c = self._m[0][2] * (self._m[1][0] * self._m[2][1] - self._m[1][1] * self._m[2][0])
        return a - b + c


    def is_invertible(self) -> bool:
        return not math.isclose(self.determinant(), 0.0)


    def inverse(self) -> 'Matrix33':
        det = self.determinant()
        if self.is_invertible():
            raise ValueError("Matrix is not invertible")

        a = self._m
        b = [[0.0 for c in range(3)] for r in range(3)]

        b[0][0] = (a[1][1] * a[2][2] - a[1][2] * a[2][1]) / det
        b[0][1] = (a[0][2] * a[2][1] - a[0][1] * a[2][2]) / det
        b[0][2] = (a[0][1] * a[1][2] - a[0][2] * a[1][1]) / det

        b[1][0] = (a[1][2] * a[2][0] - a[1][0] * a[2][2]) / det
        b[1][1] = (a[0][0] * a[2][2] - a[0][2] * a[2][0]) / det
        b[1][2] = (a[0][2] * a[1][0] - a[0][0] * a[1][2]) / det

        b[2][0] = (a[1][0] * a[2][1] - a[1][1] * a[2][0]) / det
        b[2][1] = (a[0][1] * a[2][0] - a[0][0] * a[2][1]) / det
        b[2][2] = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) / det

        return Matrix33(
            b[0][0], b[0][1], b[0][2],
            b[1][0], b[1][1], b[1][2],
            b[2][0], b[2][1], b[2][2],
        )

    def multiply(self, other:'Matrix33') -> 'Matrix33':

        if other is None:
            raise ValueError("Matrix33 cannot be multiplied with None")

        if not isinstance(other, Matrix33):
            raise TypeError("Matrix33 can only be multiplied with another Matrix33")

        a = self._m
        b = other._m
        c = [[0.0 for c in range(3)] for r in range(3)]

        for row in range(0, 3):
            for col in range(0, 3):

                # Dot product of the row of matrix A + 
                sum = 0.0
                for iter in range(0, 3):
                    sum += a[row][iter] * b[iter][col]

                c[row][col] = sum
        
        return Matrix33(
            c[0][0], c[0][1], c[0][2],
            c[1][0], c[1][1], c[1][2],
            c[2][0], c[2][1], c[2][2],
        )
    

    def transpose(self) -> 'Matrix33':
        a = self._m
        b = [[0.0 for c in range(3)] for r in range(3)]

        for row in range(0, 3):
            for col in range(0, 3):
                b[row][col] = a[col][row]

        return Matrix33(
            b[0][0], b[0][1], b[0][2],
            b[1][0], b[1][1], b[1][2],
            b[2][0], b[2][1], b[2][2],
        )


def from_position(x: float = 0.0, y: float = 0.0) -> 'Matrix33':
    return Matrix33(
        1.0, 0.0, x,
        0.0, 1.0, y,
        0.0, 0.0, 1.0
    )


def from_rotation(degrees: float = 0.0) -> 'Matrix33':
    rad = math.radians(degrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    return Matrix33(
        cos, -sin, 0.0,
        sin,  cos, 0.0,
        0.0,  0.0, 1.0
    )


def from_scale(x: float = 1.0, y: float = 1.0) -> 'Matrix33':
    return Matrix33(
          x, 0.0, 0.0,
        0.0,   y, 0.0,
        0.0, 0.0, 1.0
    )


def from_scale_uniform(scale: float = 1.0) -> 'Matrix33':
    return from_scale(scale, scale)


def identity() -> 'Matrix33':
    return Matrix33(
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0
    )


def null() -> 'Matrix33':
    return Matrix33()
