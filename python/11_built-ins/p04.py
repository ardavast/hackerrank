#!/usr/bin/env python3
# coding: utf-8

"""
Athlete Sort
https://www.hackerrank.com/challenges/python-sort-sort
"""

from operator import itemgetter

if __name__ == '__main__':
    rows, _ = [int(x) for x in input().split()]

    athletes = []
    for _ in range(rows):
        details = [int(x) for x in input().split()]
        athletes.append(details)

    column = int(input())
    for details in sorted(athletes, key=itemgetter(column)):
        print(*details)
