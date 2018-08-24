#!/usr/bin/env python3
# coding: utf-8

"""
Check Subset
https://www.hackerrank.com/challenges/py-check-subset
"""

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        input()
        s1 = set([int(x) for x in input().split()])
        input()
        s2 = set([int(x) for x in input().split()])
        print(s1 <= s2)
