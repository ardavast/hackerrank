#!/usr/bin/env python3
# coding: utf-8

"""
Detect Floating Point Number
https://www.hackerrank.com/challenges/introduction-to-regex
"""

import re

if __name__ == '__main__':
    float_re = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
    n = int(input())

    for _ in range(n):
        s = input()
        print(bool(re.match(float_re, s)))
