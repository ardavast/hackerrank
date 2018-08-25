#!/usr/bin/env python3
# coding: utf-8

"""
itertools.combinations_with_replacement()
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
"""

from itertools import combinations_with_replacement

if __name__ == '__main__':
    line = input().split()
    s = line[0]
    k = int(line[1])

    for combination in combinations_with_replacement(sorted(s), k):
        print(''.join(combination))
