#!/usr/bin/env python3
# coding: utf-8

"""
The Captain's Room
https://www.hackerrank.com/challenges/py-the-captains-room
"""

from collections import Counter

if __name__ == '__main__':
    input()
    l = [int(x) for x in input().split()]

    ctr = Counter(l)

    for k, v in ctr.items():
        if v == 1:
            print(k)
            break
