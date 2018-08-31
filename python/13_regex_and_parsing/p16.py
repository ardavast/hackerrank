#!/usr/bin/env python3
# coding: utf-8

"""
Validating Postal Codes
https://www.hackerrank.com/challenges/validating-postalcode
"""

import re


def is_valid(s):
    if (re.match(r'[1-9][0-9]{5}$') and
        re.findall(r'(\d)(?=\d\1)', s) < 2):
        return True
    else:
        return False


if __name__ == '__main__':
    s = input()
    print(is_valid(s))
