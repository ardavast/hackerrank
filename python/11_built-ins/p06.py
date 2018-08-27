#!/usr/bin/env python3
# coding: utf-8

"""
ginortS
https://www.hackerrank.com/challenges/ginorts
"""

import string


def sortfunc(c):
    chars = string.ascii_lowercase + string.ascii_uppercase + '1357902468'
    return chars.index(c)


if __name__ == '__main__':
    s = input()
    print(''.join(sorted(s, key=sortfunc)))
