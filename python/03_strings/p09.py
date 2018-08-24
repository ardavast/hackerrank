#!/usr/bin/env python3
# coding: utf-8

"""
Designer Door Mat
https://www.hackerrank.com/challenges/designer-door-mat
"""

if __name__ == '__main__':
    line = input().split()
    n, m = [int(x) for x in line[:2]]

    for i in range(n // 2):
        print(('.|.' * (2 * i + 1)).center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(n // 2 - 1, -1, -1):
        print(('.|.' * (2 * i + 1)).center(m, '-'))
