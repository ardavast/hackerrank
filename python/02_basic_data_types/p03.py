#!/usr/bin/env python3
# coding: utf-8

"""
Nested Lists
https://www.hackerrank.com/challenges/nested-list
"""

from collections import defaultdict

if __name__ == '__main__':
    n = int(input())

    marks = defaultdict(list)
    for _ in range(n):
        name = input()
        score = float(input())
        marks[score].append(name)

    last2_score = sorted(set(marks.keys()))[1]

    for name in sorted(marks[last2_score]):
        print(name)
