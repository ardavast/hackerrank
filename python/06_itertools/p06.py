#!/usr/bin/env python3
# coding: utf-8

"""
Iterables and Iterators
https://www.hackerrank.com/challenges/iterables-and-iterators
"""

from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    l = input().split()[:n]
    k = int(input())

    a = 0
    length = 0
    for combination in combinations(l, k):
        if any([x == 'a' for x in combination]):
            a += 1
        length += 1

    print(a / length)
