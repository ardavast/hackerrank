#!/usr/bin/env python3
# coding: utf-8

"""
Compress the String!
https://www.hackerrank.com/challenges/compress-the-string
"""

from itertools import groupby

if __name__ == '__main__':
    line = input()

    output = []
    for k, g in groupby(line):
        output.append((len(list(g)), int(k)))

    print(*output)
