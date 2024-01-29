#!/usr/bin/python3

class Fraction:
    def __init__(self, n, d):
        self.numerator, self.denominator = Fraction.reduce(n, d)

    @staticmethod
    def gcd(a,b):
        """The gcd method calculates the greatest common divisor of two numbers,
        atleast one of which is not 0.
        The gcd is the largest positive integer that can divide two or more numbers,
        without a remainder.
        """
        while b != 0:
            """This loop will continue as long as b is not zero.
            When b becomes zero, then this loop will end and the
            method will return.
            """
            a, b = b, a % b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
if __name__ == "__main__":
    a = Fraction(8, 24)
    print(a)

