import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
        denominator = self.denominator * frac.denominator
        if numerator < 0 or denominator < 0:
            negative = -1
        negative = 1
        gcd = math.gcd(abs(numerator), abs(denominator))
        numerator /= gcd * negative
        denominator /= gcd
        return Fraction(numerator, denominator)

    def __sub__(self, frac):
        """Return the difference of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        numerator = (self.numerator * frac.denominator) - (self.denominator * frac.numerator)
        denominator = self.denominator * frac.denominator
        if numerator < 0 or denominator < 0:
            negative = -1
        negative = 1
        gcd = math.gcd(abs(numerator), abs(denominator))
        numerator /= gcd * negative
        denominator /= gcd
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = (a*c)/(b*d)
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        if numerator < 0 or denominator < 0:
            negative = -1
        negative = 1
        gcd = math.gcd(abs(numerator), abs(denominator))
        numerator /= gcd * negative
        denominator /= gcd
        return Fraction(numerator, denominator)

    def __div__(self, frac):
        """Return the quotient of two fractions as a new fraction.
           Use the standard formula  a/b / c/d = (a*d)/(b*c)
        """
        numerator = self.numerator * frac.denominator
        denominator = self.denominator * frac.numerator
        if numerator < 0 or denominator < 0:
            negative = -1
        negative = 1
        gcd = math.gcd(abs(numerator), abs(denominator))
        numerator /= gcd * negative
        denominator /= gcd
        return Fraction(numerator, denominator)

    def __neg__(self):
        """Return the fraction in a negative form as a new fraction."""
        numerator = -self.numerator
        denominator = self.denominator 
        gcd = math.gcd(abs(numerator), abs(denominator))
        numerator /= gcd
        denominator /= gcd
        return Fraction(numerator, denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        gcd1 = math.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator /= gcd1
        self.denominator /= gcd1
        gcd2 = math.gcd(abs(self.numerator), abs(self.denominator))
        frac.numerator /= gcd2
        frac.denominator /= gcd2
        return self.numerator == frac.numerator and self.denominator == frac.denominator

    def __repr__(self):
        gcd = math.gcd(int(abs(self.numerator)), int(abs(self.denominator)))
        self.numerator /= gcd
        self.denominator /= gcd
        if self.denominator == 1:
            return "{}".format(int(self.numerator))
        if self.numerator < 0 and self.denominator < 0:
            return "{}/{}".format(int(abs(self.numerator)), int(abs(self.denominator)))
        if self.denominator < 0:
            return "{}/{}".format(int(-self.numerator), int(abs(self.denominator)))
        return "{}/{}".format(int(self.numerator), int(self.denominator))
