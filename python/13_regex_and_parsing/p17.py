#!/usr/bin/env python3
# coding: utf-8

"""
Matrix Script
https://www.hackerrank.com/challenges/matrix-script
"""

import re

if __name__ == '__main__':
    n, m = [int(x) for x in input()]

    matrix = []
    for _ in range(n):
        matrix.append(input())

    s = ''
    for i in range(m):
        for j in range(n):
            s += matrix[j][i]

    s = re.sub(r'(\b[^0-9A-Za-z]\b', ' ', s)

    print(s)
