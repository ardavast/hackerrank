#!/usr/bin/env python3
# coding: utf-8

"""
Collections.OrderedDict()
https://www.hackerrank.com/challenges/py-collections-ordereddict
"""

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    total = OrderedDict()

    for _ in range(n):
        line = input().split()
        item, price = ' '.join(line[:-1]), int(line[-1])
        total[item] = total.get(item, 0) + price

    for item in total:
        print('{} {}'.format(item, total[item]))
