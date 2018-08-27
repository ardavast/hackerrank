#!/usr/bin/env python3
# coding: utf-8

"""
Classes: Dealing with Complex Numbers
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
"""


class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{:.2f}{:+.2f}i'.format(self.real, self.imag)


if __name__ == '__main__':
    line = [float(x) for x in input().split()]
    x = Complex(line[0], line[1])
    line = [float(x) for x in input().split()]
    y = Complex(line[0], line[1])

    ops = [x + y, x - y, x * y, x / y, x.mod(), y.mod()]

    for op in ops:
        print(str(op))
