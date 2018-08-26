#!/usr/bin/env python3
# coding: utf-8

"""
DefaultDict Tutorial
https://www.hackerrank.com/challenges/defaultdict-tutorial
"""

from collections import defaultdict

if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    d = defaultdict(list)

    for i in range(n):
        line = input()
        d[line].append(i + 1)

    for _ in range(m):
        line = input()
        if line in d:
            print(*d[line])
        else:
            print('-1')
