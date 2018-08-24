#!/usr/bin/env python3
# coding: utf-8

"""
Symmetric Difference
https://www.hackerrank.com/challenges/symmetric-difference
"""

if __name__ == '__main__':
    input()
    s1 = set([int(x) for x in input().split()])
    input()
    s2 = set([int(x) for x in input().split()])

    for n in sorted(s1 ^ s2):
        print(n)
