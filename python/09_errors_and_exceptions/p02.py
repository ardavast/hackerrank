#!/usr/bin/env python3
# coding: utf-8

"""
Incorrect Regex
https://www.hackerrank.com/challenges/incorrect-regex
"""

import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        try:
            re.compile(input())
            print('True')
        except re.error:
            print('False')
