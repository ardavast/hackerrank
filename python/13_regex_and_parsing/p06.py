#!/usr/bin/env python3
# coding: utf-8

"""
Regex Substitution
https://www.hackerrank.com/challenges/re-sub-regex-substitution
"""

import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()

        s = re.sub(r'(?<= )&&(?= )', 'and', s)
        s = re.sub(r'(?<= )\|\|(?= )', 'or', s)

        print(s)
