#!/usr/bin/env python3
# coding: utf-8

"""
itertools.combinations()
https://www.hackerrank.com/challenges/itertools-combinations
"""

from itertools import combinations

if __name__ == '__main__':
    line = input().split()
    s = line[0]
    k = int(line[1])

    for i in range(1, k + 1):
        for combination in combinations(sorted(s), i):
            print(''.join(combination))
