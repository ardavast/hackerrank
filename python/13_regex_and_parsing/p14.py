#!/usr/bin/env python3
# coding: utf-8

"""
Validating UID
https://www.hackerrank.com/challenges/validating-uid
"""

import re


def is_valid(uid):
    if (len(set(uid)) == 10 and
        re.match(r'^[0-9A-Za-z]{10}$', uid) and
        len(re.findall(r'[A-Z]', uid)) >= 2 and
        len(re.findall(r'[0-9]', uid)) >= 3):
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
