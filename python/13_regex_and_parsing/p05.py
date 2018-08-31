#!/usr/bin/env python3
# coding: utf-8

"""
Re.start() & Re.end()
https://www.hackerrank.com/challenges/re-start-re-end
"""

import re

s = input()
k = input()

if __name__ == '__main__':
    if re.search(k, s):
        pat = r'(?={})'.format(k)
        for m in re.finditer(pat, s):
            print((m.start(), m.start() + len(k) - 1))
    else:
        print((-1, -1))
