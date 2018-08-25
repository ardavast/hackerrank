#!/usr/bin/env python3
# coding: utf-8

"""
Maximize It!
https://www.hackerrank.com/challenges/maximize-it
"""

from itertools import product

if __name__ == '__main__':
    line = input().split()
    k, m = [int(x) for x in line[:2]]

    l = []
    for _ in range(k):
        line = input().split()
        l.append([int(x) for x in line[1:]])

    def s(l):
        return sum([x * x for x in l]) % m

    print(max(map(s, product(*l))))
