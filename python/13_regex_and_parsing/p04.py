#!/usr/bin/env python3
# coding: utf-8

"""
Re.findall() & Re.finditer()
https://www.hackerrank.com/challenges/re-findall-re-finditer
"""

import string
import re

if __name__ == '__main__':
    vowels = 'aeiou'
    consonants = re.sub(r'[{}]'.format(vowels), '', string.ascii_lowercase)
    re_cvc = r"(?<=[{0}])([{1}]{{2,}})[{0}]".format(consonants, vowels)

    line = input()

    l = re.findall(re_cvc, line, re.I)
    if l:
        for match in l:
            print(match)
        else:
            print('-1')
