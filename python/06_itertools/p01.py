#!/usr/bin/env python3
# coding: utf-8

"""
itertools.product()
https://www.hackerrank.com/challenges/itertools-product
"""

from itertools import product

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(*product(a, b))
