#!/usr/bin/env python3
# coding: utf-8

"""
Find a string
https://www.hackerrank.com/challenges/find-a-string
"""

import re

if __name__ == '__main__':
    s = input()
    subs = input()

    pat = '(?={})'.format(subs)
    print(len(re.findall(pat, s)))
