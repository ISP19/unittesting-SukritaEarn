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

    def test_init(self):
        a = Fraction(2,4)
        self.assertEqual(1, a.numerator)
        self.assertEqual(2, a.denominator)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))

    def test_sub(self):
        pass

    def test_mul(self):
        pass

    def test_neg(self):
        pass

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
    
    def test_impossible_case(self):
        with self.assertRaises(ValueError):
            self.assertEqual(ValueError, Fraction(1,0))
            self.assertEqual(ValueError, Fraction(-1,-0))
            self.assertEqual(ValueError, Fraction(0,0))
            self.assertEqual(ValueError, Fraction(5,-0))
    
    def test_numerator_is_zero(self):
        self.assertEqual(Fraction(0,8), Fraction(0,-3))
        self.assertEqual(Fraction(-0,100), Fraction(-0,-5))
        self.assertEqual(Fraction(-0,9), Fraction(0,-9))
