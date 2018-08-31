#!/usr/bin/env python3
# coding: utf-8

"""
Hex Color Code
https://www.hackerrank.com/challenges/hex-color-code
"""

import re

if __name__ == '__main__':
    re_rgb = re.compile(r'[ ,:(](#(?:[a-f0-9]{3}|[a-f0-9]{6}))[ ,;)]', re.I)
    n = int(input())

    for _ in range(n):
        s = input()

        for m in re.finditer(re_rgb, s):
            print(m.group(1))
