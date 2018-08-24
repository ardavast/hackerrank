#!/usr/bin/env python3
# coding: utf-8

"""
Check Strict Superset
https://www.hackerrank.com/challenges/py-check-strict-superset
"""

if __name__ == '__main__':
    s1 = set([int(x) for x in input().split()])
    n = int(input())

    ret = True
    for _ in range(n):
        s2 = set([int(x) for x in input().split()])
        if not s1 > s2:
            ret = False
            break

    print(ret)
