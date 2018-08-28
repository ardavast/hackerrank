#!/usr/bin/env python3
# coding: utf-8

"""
Reduce Function
https://www.hackerrank.com/challenges/reduce-function
"""

import operator
from functools import reduce
from fractions import Fraction


def prod(fracs):
    return reduce(operator.mul, fracs)


if __name__ == '__main__':
    i = int(input())

    fracs = []
    for _ in range(i):
        n, m = [int(x) for x in input().split()]
        fracs.append(Fraction(n, m))

    result = prod(fracs)

    print('{} {}'.format(result.numerator, result.denominator))
