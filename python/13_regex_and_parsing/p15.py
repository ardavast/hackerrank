#!/usr/bin/env python3
# coding: utf-8

"""
Validating Credit Card Numbers
https://www.hackerrank.com/challenges/validating-credit-card-number
"""

import re


def is_valid(s):
    if (s[0] in '456' and
        re.match(r'(?:\d{16}|\d{4}-\d{4}-\d{4}-\d{4})$', s) and
        not re.search(r'(\d)\1\1\1', s.replace('-', ''))):
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        if is_valid(s):
            print('Valid')
        else:
            print('Invalid')
