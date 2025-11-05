from math import gcd

class Rational:
    """
    A class to represent rational numbers (fractions) with operator overloading support.
    """

    def __init__(self, numerator, denominator=1):
        """
        Initialize a Rational number.

        Parameters:
        - numerator: The numerator of the rational number.
        - denominator: The denominator of the rational number (must not be zero).

        The fraction is automatically reduced to its simplest form.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

        if self.denominator < 0:  # Normalize sign (denominator always positive)
            self.numerator *= -1
            self.denominator *= -1


    # c = a + b ==== a.__add__(b)
    def __add__(self, other):
        """
        Add two rational numbers.

        Returns:
        - A new Rational object representing the sum.
        """
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # c = a - b
    def __sub__(self, other):
        """
        Subtract one rational number from another.

        Returns:
        - A new Rational object representing the difference.
        """
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)
    # c = a * b
    #1/2 * 4/5 == 4/10
    # 4/2 * 14 = Rational(56, 2)
    #
    def __mul__(self, other):
        """
        Multiply two rational numbers or a rational and an integer.

        Returns:
        - A new Rational object representing the product.
        """
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        return Rational(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        """
        Divide one rational number by another.

        Returns:
        - A new Rational object representing the quotient.
        """
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    # if a == b:
    #a = Rational(1, 5)
    # a == 0.2
    def __eq__(self, other):
        """
        Check if two rational numbers are equal.

        Returns:
        - True if equal, otherwise False.
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    # 1/5 < 2/3
    def __lt__(self, other):
        """
        Check if one rational number is less than another.

        Returns:
        - True if self < other, otherwise False.
        """
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        """
        Check if one rational number is less than or equal to another.

        Returns:
        - True if self <= other, otherwise False.
        """
        return self < other or self == other

    def __gt__(self, other):
        """
        Check if one rational number is greater than another.

        Returns:
        - True if self > other, otherwise False.
        """
        return not self <= other

    def __ge__(self, other):
        """
        Check if one rational number is greater than or equal to another.

        Returns:
        - True if self >= other, otherwise False.
        """
        return not self < other

    def __ne__(self, other):
        """
        Check if two rational numbers are not equal.

        Returns:
        - True if not equal, otherwise False.
        """
        return not self == other

    def __str__(self):
        """
        Return a human-readable string representation of the rational number.
        """
        return f"{self.numerator}/{self.denominator}"
    #
    def __repr__(self):
        """
        Return an official string representation of the rational number.
        """
        return f"Rational({self.numerator}, {self.denominator})"


# Example usage (you can remove this part if you only want the class):
if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(3, 4)
    print(r1, "+", r2, "=", r1 + r2)
    print("r1 - r2 =", r1 - r2)
    print("r1 * r2 =", r1 * r2)
    print("r1 / r2 =", r1 / r2)
    print("r1 == r2?", r1 == r2)
    print("r1 < r2?", r1 < r2)
    str(Rational(1,5))

    print(Rational.__le__.__doc__)



"""
1      3 
-   +  -  =  
2      4 

"""