import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0)
        self.assertEqual("0", f.__str__())
        f = Fraction(0,0)
        self.assertEqual("Indeterminate form", f.__str__())
        f = Fraction(1,0)
        self.assertEqual("Infinity", f.__str__())
        f = Fraction(-1,0)
        self.assertEqual("-Infinity", f.__str__())
        f = Fraction(4,0)
        self.assertEqual("Infinity", f.__str__())
        f = Fraction(-100,0)
        self.assertEqual("-Infinity", f.__str__())

    def test_init(self):
        a = Fraction(2,4)
        self.assertEqual(1, a.numerator)
        self.assertEqual(2, a.denominator)
        b = Fraction(-3,9)
        self.assertEqual(-1, b.numerator)
        self.assertEqual(3, b.denominator)
        c = Fraction(4,-2)
        self.assertEqual(-2, c.numerator)
        self.assertEqual(1, c.denominator)
        d = Fraction(-800, -200)
        self.assertEqual(4, d.numerator)
        self.assertEqual(1, d.denominator)
        e = Fraction(-4)
        self.assertEqual(-4, e.numerator)
        self.assertEqual(1, e.denominator)
        g = Fraction(5)
        self.assertEqual(5, g.numerator)
        self.assertEqual(1, g.denominator)
        h = Fraction(0,1)
        self.assertEqual(0, h.numerator)
        self.assertEqual(1, h.denominator)
        i = Fraction(-1,0)
        self.assertEqual(-1, i.numerator)
        self.assertEqual(0, i.denominator)
        j = Fraction(-3,0)
        self.assertEqual(-1, j.numerator)
        self.assertEqual(0, j.denominator)
        k = Fraction(0,0)
        self.assertEqual(0, k.numerator)
        self.assertEqual(0, k.denominator)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(-10,7), Fraction(7,-49)+Fraction(-18,14))
        self.assertEqual(Fraction(4,-8), Fraction(-5,-10)+Fraction(100,-100))
        self.assertEqual(Fraction(-5,-15), Fraction(1)+Fraction(2,-3))
        self.assertEqual(Fraction(0), Fraction(6,12)+Fraction(-1,2))
        self.assertEqual(Fraction(1,0), Fraction(3,0)+Fraction(5,0))
        self.assertEqual(Fraction(-1,0), Fraction(-3,0)+Fraction(0))
        self.assertEqual(Fraction(-1,0), Fraction(-8,0)+Fraction(-1,0))
        self.assertEqual(Fraction(1,0), Fraction(4,5)+Fraction(9,0))
        self.assertEqual(Fraction(0,0), Fraction(-1,0)+Fraction(1,0))
        self.assertEqual(Fraction(0,0), Fraction(5,0)+Fraction(-6,0))
        self.assertEqual(Fraction(0,0), Fraction(-3,0)+Fraction(0,0))

    def test_sub(self):
        self.assertEqual(Fraction(5), Fraction(-200,-2)-Fraction(950,10))
        self.assertEqual(Fraction(-8,9), Fraction(4,-18)-Fraction(2,3))
        self.assertEqual(Fraction(3,-3), Fraction(-15,-3)-Fraction(6))
        self.assertEqual(Fraction(-100,-4), Fraction(-40,-2)-Fraction(40,-8))
        self.assertEqual(Fraction(0), Fraction(1,-2)-Fraction(-1,2))
        self.assertEqual(Fraction(-1,0), Fraction(2,4)-Fraction(8,0))
        self.assertEqual(Fraction(1,0), Fraction(90,0)-Fraction(3,4))
        self.assertEqual(Fraction(-1,0), Fraction(-6,0)-Fraction(2,0))
        self.assertEqual(Fraction(1,0), Fraction(0)-Fraction(-4,0))
        self.assertEqual(Fraction(0,0), Fraction(5,0)-Fraction(3,0))
        self.assertEqual(Fraction(0,0), Fraction(-7,0)-Fraction(-9,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)-Fraction(0,0))

    def test_mul(self):
        self.assertEqual(Fraction(7,10), Fraction(-2,-7)*Fraction(49,20))
        self.assertEqual(Fraction(-1000,3000), Fraction(-10,1000)*Fraction(100,3))
        self.assertEqual(Fraction(-20,-4), Fraction(-30,6)*Fraction(-1))
        self.assertEqual(Fraction(0), Fraction(0)*Fraction(-2413,3231))
        self.assertEqual(Fraction(3,9), Fraction(-1)*Fraction(1,-3))
        self.assertEqual(Fraction(-1,0), Fraction(2)*Fraction(-200,0))
        self.assertEqual(Fraction(1,0), Fraction(90,0)*Fraction(9))
        self.assertEqual(Fraction(-1,0), Fraction(-1,0)*Fraction(1,0))
        self.assertEqual(Fraction(1,0), Fraction(-3)*Fraction(-4,0))
        self.assertEqual(Fraction(0,0), Fraction(0)*Fraction(8,0))
        self.assertEqual(Fraction(0,0), Fraction(-7,0)*Fraction(0,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)*Fraction(7,0))

    def test_truediv(self):
        self.assertEqual(Fraction(3,7), Fraction(-1)/Fraction(7,-3))
        self.assertEqual(Fraction(28,-7), Fraction(-500,250)/Fraction(3,6))
        self.assertEqual(Fraction(-1,0), Fraction(20,-12)/Fraction(0))
        self.assertEqual(Fraction(1,0), Fraction(99,12)/Fraction(0))
        self.assertEqual(Fraction(0), Fraction(0)/Fraction(567,765))
        self.assertEqual(Fraction(1,0), Fraction(9,0)/Fraction(1000))
        self.assertEqual(Fraction(-1,0), Fraction(-9,0)/Fraction(1))
        self.assertEqual(Fraction(1,0), Fraction(1,0)/Fraction(2,3))
        self.assertEqual(Fraction(0,0), Fraction(-1,0)/Fraction(3,0))
        self.assertEqual(Fraction(0,0), Fraction(-4,0)/Fraction(-6,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)/Fraction(-1,0))
        self.assertEqual(Fraction(0,0), Fraction(1,0)/Fraction(-1,0))

    def test_neg(self):
        self.assertEqual(Fraction(4), -Fraction(8,-2))
        self.assertEqual(Fraction(-7,2), -Fraction(21,6))
        self.assertEqual(Fraction(9,-12), -Fraction(-3,-4))
        self.assertEqual(Fraction(-4,-5), -Fraction(-160,200))
        self.assertEqual(Fraction(1,0), -Fraction(-1,0))
        self.assertEqual(Fraction(0,0), -Fraction(0,0))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        i = Fraction(10,0)
        j = Fraction(5,0)
        k = Fraction(-20,0)
        self.assertTrue(i == j)
        self.assertFalse(i == k)
        self.assertTrue(Fraction(1,0) == i)
        self.assertTrue(Fraction(-1,0) == k)
        l = Fraction(8000,-2000)
        m = Fraction(-4000,1000)
        self.assertTrue(l.__eq__(m))
        n = Fraction(5)
        o = Fraction(5, 1)
        self.assertTrue(n == o)
        self.assertTrue(n.__eq__(o))
        p = Fraction(1,0)
        q = Fraction(-1,0)
        self.assertFalse(p == q)
        self.assertTrue(p.__eq__(-q))

    def test_value_error_case(self):
        with self.assertRaises(ValueError):
            Fraction("w", "e")
        with self.assertRaises(ValueError):
            Fraction("3","2")
        with self.assertRaises(ValueError):
            Fraction([1],[9])
        with self.assertRaises(ValueError):
            Fraction("5",6)
        with self.assertRaises(ValueError):
            Fraction(-5,"-6")

    def test_denominator_is_zero(self):
        self.assertEqual(Fraction(1,0), Fraction(5,-0))
        self.assertEqual(Fraction(-1,0), Fraction(-33,0))
        self.assertEqual(Fraction(-1,0), Fraction(-17,-0))
    
    def test_numerator_is_zero(self):
        self.assertEqual(Fraction(0,8), Fraction(0,-3))
        self.assertEqual(Fraction(-0,100), Fraction(-0,-5))
        self.assertEqual(Fraction(-0,9), Fraction(0,-9))