#!/usr/bin/env python3
# coding: utf-8

"""
Set .union() Operation
https://www.hackerrank.com/challenges/py-set-union
"""

if __name__ == '__main__':
    input()
    s1 = set([int(x) for x in input().split()])
    input()
    s2 = set([int(x) for x in input().split()])

    print(len(s1 | s2))
