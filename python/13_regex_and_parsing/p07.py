#!/usr/bin/env python3
# coding: utf-8

"""
Validating Roman Numerals
https://www.hackerrank.com/challenges/validate-a-roman-number
"""

import re

if __name__ == '__main__':
    re_roman = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    s = input()
    print(bool(re.match(s, line)))
