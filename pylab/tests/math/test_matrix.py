import math
import random
import pylab.math.matrix
import unittest

class TestMatrix33(unittest.TestCase):

    def assert_matrix_values(self, m: pylab.math.matrix.Matrix33, values: any):
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(m._m[i][j], values[i][j], places=5)


    def assert_matrix_equals(self, m1: pylab.math.matrix.Matrix33, m2: pylab.math.matrix.Matrix33):
        self.assert_matrix_values(m1, m2._m)


    def assert_is_identity(self, m: pylab.math.matrix.Matrix33):
        self.assert_matrix_equals(m, pylab.math.matrix.identity())


    def assert_is_null(self, m: pylab.math.matrix.Matrix33):
        self.assert_matrix_equals(m, pylab.math.matrix.null())


    def test_identity(self):
        m = pylab.math.matrix.identity()
        self.assert_matrix_values(m, [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])


    def test_null(self):
        m = pylab.math.matrix.null()
        self.assert_matrix_values(m, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])


    def test_from_position(self):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        m = pylab.math.matrix.from_position(x, y)
        self.assertIsInstance(m, pylab.math.matrix.Matrix33)
        self.assert_matrix_values(m, [[1.0, 0.0, x], [0.0, 1.0, y], [0.0, 0.0, 1.0]])


    def test_from_rotation(self):
        deg = random.randint(-360, 360)
        rad = math.radians(deg)
        cos = math.cos(rad)
        sin = math.sin(rad)
        m = pylab.math.matrix.from_rotation(deg)
        self.assertIsInstance(m, pylab.math.matrix.Matrix33)
        self.assert_matrix_values(m, [[cos, -sin, 0.0], [sin, cos, 0.0], [0.0, 0.0, 1.0]])


    def test_from_scale(self):
        scaleX = random.randint(-1000, 1000)
        scaleY = random.randint(-1000, 1000)
        m = pylab.math.matrix.from_scale(scaleX, scaleY)
        self.assertIsInstance(m, pylab.math.matrix.Matrix33)
        self.assert_matrix_values(m, [[scaleX, 0.0, 0.0], [0.0, scaleY, 0.0], [0.0, 0.0, 1.0]])


    def test_from_scale_uniform(self):
        scale = random.randint(-1000, 1000)
        m = pylab.math.matrix.from_scale_uniform(scale)
        self.assertIsInstance(m, pylab.math.matrix.Matrix33)
        self.assert_matrix_values(m, [[scale, 0.0, 0.0], [0.0, scale, 0.0], [0.0, 0.0, 1.0]])


    def test_transpose(self):
        m1 = pylab.math.matrix.Matrix33(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = m1.transpose()
        self.assertIsInstance(m2, pylab.math.matrix.Matrix33)
        self.assert_matrix_values(m2, [[1.0, 4.0, 7.0], [2.0, 5.0, 8.0], [3.0, 6.0, 9.0]])


    def test_multiply(self):

        # Identity preservation
        m1 = pylab.math.matrix.identity()
        m2 = pylab.math.matrix.identity()
        m = m1.multiply(m2)
        self.assertIsInstance(m, pylab.math.matrix.Matrix33)
        self.assert_is_identity(m)

        # Null
        m1 = pylab.math.matrix.Matrix33(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m1 = pylab.math.matrix.null()
        m = m1.multiply(m2)
        self.assert_is_null(m)

        # Arbitrary multiplication
        m1 = pylab.math.matrix.Matrix33(1, 2, 3, 4, 5, 6, 7, 8, 9)
        m2 = pylab.math.matrix.Matrix33(9, 8, 7, 6, 5, 4, 3, 2, 1)
        m = m1.multiply(m2)

        m3 = pylab.math.matrix.Matrix33(30, 24, 18, 84, 69, 54, 138, 114, 90)
        self.assert_matrix_values(m, m3._m)

        # Null param
        m1 = pylab.math.matrix.identity()
        self.assertRaises(ValueError, m1.multiply, None)

        # Wrong param type
        m1 = pylab.math.matrix.identity()
        m2 = "dummy"
        self.assertRaises(TypeError, m1.multiply, m2)


if __name__ == '__main__':
    unittest.main()