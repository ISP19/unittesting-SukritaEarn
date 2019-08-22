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
        if type(numerator) != int or type(denominator) != int:
            raise ValueError
        
        if denominator == 0 and numerator != 0:
            if numerator < 0:
                numerator = -1
            else:
                numerator = 1
        elif numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator
        elif denominator < 0:
            numerator = -numerator
            denominator = abs(denominator)

        if denominator == 0 and numerator == 0:
            numerator = 0
            denominator = 0
        else:
            gcd = math.gcd(int(numerator), int(denominator))
            numerator /= gcd
            denominator /= gcd
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.numerator == 0 and self.denominator == 0:
            numerator = 0
            denominator = 0
        elif frac.numerator == 0 and frac.denominator == 0:
            numerator = 0
            denominator = 0
        elif self.denominator == 0 and frac.denominator == 0:
            if self.numerator + frac.numerator > 0:
                numerator = 1
            elif self.numerator + frac.numerator < 0:
                numerator = -1
            else:
                numerator = 0
            denominator = 0
        else:
            numerator = (self.numerator * frac.denominator) + (self.denominator * frac.numerator)
            denominator = self.denominator * frac.denominator
        return Fraction(int(numerator), int(denominator))

    def __sub__(self, frac):
        """Return the difference of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        if self.numerator == 0 and self.denominator == 0:
            numerator = 0
            denominator = 0
        elif frac.numerator == 0 and frac.denominator == 0:
            numerator = 0
            denominator = 0
        elif self.denominator == 0 and frac.denominator == 0:
            if self.numerator - frac.numerator > 0:
                numerator = 1
            elif self.numerator - frac.numerator < 0:
                numerator = -1
            else:
                numerator = 0
            denominator = 0
        else:
            numerator = (self.numerator * frac.denominator) - (self.denominator * frac.numerator)
            denominator = self.denominator * frac.denominator
        return Fraction(int(numerator), int(denominator))

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = (a*c)/(b*d)
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        return Fraction(int(numerator), int(denominator))

    def __truediv__(self, frac):
        """Return the quotient of two fractions as a new fraction.
           Use the standard formula  a/b / c/d = (a*d)/(b*c)
        """
        numerator = self.numerator * frac.denominator
        denominator = self.denominator * frac.numerator
        return Fraction(int(numerator), int(denominator))

    def __neg__(self):
        """Return the fraction in a negative form as a new fraction."""
        numerator = -self.numerator
        denominator = self.denominator
        return Fraction(int(numerator), int(denominator))

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        if self.denominator == 0 and frac.denominator == 0:
            if self.numerator == frac.numerator:
                return True
            else:
                return False
        return self.numerator == frac.numerator and self.denominator == frac.denominator

    def __str__(self):
        if self.denominator == 0 and self.numerator == 0:
            return "Indeterminate form"
        elif self.denominator == 0 and self.numerator == 1:
            return "Infinity"
        elif self.denominator == 0 and self.numerator == -1:
            return "-Infinity"
        elif self.denominator == 1:
            return "{}".format(int(self.numerator))
        else:
            return "{}/{}".format(int(self.numerator), int(self.denominator))

