#!/usr/bin/env python3
# coding: utf-8

"""
Re.split()
https://www.hackerrank.com/challenges/re-split
"""

import re

if __name__ == '__main__':
    s = input()

    for s in re.split(r'[.,]', s):
        print(s)
