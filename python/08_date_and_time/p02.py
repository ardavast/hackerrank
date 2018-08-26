#!/usr/bin/env python3
# coding: utf-8

"""
Time Delta
https://www.hackerrank.com/challenges/python-time-delta
"""

import datetime

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        ts1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
        ts2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")

        dt = ts1 - ts2

        print(int(abs(dt.total_seconds())))
