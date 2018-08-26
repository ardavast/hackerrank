#!/usr/bin/env python3
# coding: utf-8

"""
Collections.namedtuple()
https://www.hackerrank.com/challenges/py-collections-namedtuple
"""

from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    col_names = input().split()
    Row = namedtuple('Row', col_names)

    total = 0
    for _ in range(n):
        row = Row(*input().split())
        total += int(row.MARKS)

    print("{:.2f}".format(total / n))
