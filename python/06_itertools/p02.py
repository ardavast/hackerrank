#!/usr/bin/env python3
# coding: utf-8

"""
itertools.permutations()
https://www.hackerrank.com/challenges/itertools-permutations
"""

from itertools import permutations

if __name__ == '__main__':
    line = input().split()
    s = line[0]
    k = int(line[1])

    for permutation in permutations(sorted(s), k):
        print(''.join(permutation))
