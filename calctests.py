import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.subtract(9, 3), 6)

    def test_multiply(self):
        c = Calculator()
        self.assertEqual(c.mutiply(9, 3), 27)

    def test_divide(self):
        c = Calculator()
        self.assertEqual(c.divide(12, 3), 4)

    def test_square(self):
        c = Calculator()
        self.assertEqual(c.square(3), 9)

    def test_exp(self):
        c = Calculator()
        self.assertEqual(c.exp(2, 3), 8)

    def test_square_root(self):
        c = Calculator()
        self.assertEqual(c.square_root(9), 3)

    def inv(self):
        c = Calculator()
        self.assertEqual(c.inv(4), 0.25)

    def sine(self):
        c = Calculator()
        self.assertEqual(c.sine(30), -0.98803162409)

    def sine(self):
        c = Calculator()
        self.assertEqual(c.sine(math.degree(30)), 0.5)

    def cosine(self):
        c = Calculator()
        self.assertEqual(c.cosine(60), -0.98803162409)

    def cosine(self):
        c = Calculator()
        self.assertEqual(c.cosine(math.degree(60)), 0.5)

    def tangent(self):
        c = Calculator()
        self.assertEqual(c.tagent(45), 1.61977519054)

    def tangent(self):
        c = Calculator()
        self.assertEqual(c.tagent(math.degree((45)), 1))

    def invSin(self):
        c = Calculator()
        self.assertEqual(c.invSin(0.5), 0.52359878)

    def invSin(self):
        c = Calculator()
        self.assertEqual(c.invSin(math.degree(0.5)), 30)

    def invCos(self):
        c = Calculator()
        self.assertEqual(c.invCos(0.5), 1.04719755)

    def invCos(self):
        c = Calculator()
        self.assertEqual(c.invCos(math.degree(0.5)), 60)

    def invTan(self):
        c = Calculator()
        self.assertEqual(c.invSin(1), 0.78539816)

    def invTan(self):
        c = Calculator()
        self.assertEqual(c.invSin(math.degree(1)), 45)

    def switch_sign(self):
        c = Calculator()
        self.assertEqual(c.swith_sign(2), -2)

    def factorial(self):
        c = Calculator()
        self.assertEqual(c.factorial(math.facotrial(4), 24))

    def log_base_10(self):
        c = Calculator()
        self.assertEqual(c.log_base_10(math.log10(100), 2))

    def inv_base_10(self):
        c = Calculator()
        self.assertEqual(c.inv_base_10(2), 100)

    def log_base_e(self):
        c = Calculator()
        self.assertEqual(c.log_base_e(2.718281828), 1)

    def inv_base_e(self):
        c = Calculator()
        self.assertEqual(c.inv_base_e(math.exp(1)), 2.718281828)

    def log_base_y(self):
        c = Calculator()
        self.assertEqual(c.log_base_y(log(4, 2)), 2)

if __name__ == '__main__':
    unittest.main()
