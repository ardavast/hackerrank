#!/usr/bin/env python3
# coding: utf-8

"""
collections.Counter()
https://www.hackerrank.com/challenges/collections-counter
"""

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoes = Counter([int(x) for x in input().split()])
    n = int(input())

    total = 0
    for _ in range(n):
        size, price = [int(x) for x in input().split()]
        if shoes[size]:
            total += price
            shoes[size] -= 1

    print(total)
