#!/usr/bin/env python3
# coding: utf-8

"""
Company Logo
https://www.hackerrank.com/challenges/most-commons
"""

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    s = input()

    cnt = OrderedCounter(sorted(s))

    for c in cnt.most_common(3):
        print(*c)
