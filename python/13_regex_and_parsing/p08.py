#!/usr/bin/env python3
# coding: utf-8

"""
Validating phone numbers
https://www.hackerrank.com/challenges/validating-the-phone-number
"""

import re

if __name__ == '__main__':
    re_phone = re.compile(r'^[789]\d{9}$')
    n = int(input())

    for _ in range(n):
        s = input()
        if re.match(re_phone, s):
            print('YES')
        else:
            print('NO')
