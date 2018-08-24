#!/usr/bin/env python3
# coding: utf-8

"""
Set .add()
https://www.hackerrank.com/challenges/py-set-add
"""

if __name__ == '__main__':
    s = set()
    n = int(input())

    for _ in range(n):
        s.add(input())

    print(len(s))
