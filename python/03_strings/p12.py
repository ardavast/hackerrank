#!/usr/bin/env python3
# coding: utf-8

"""
Capitalize!
https://www.hackerrank.com/challenges/capitalize
"""

import re


def cap(s):
    """Capitalize the first character of s."""
    return s[0].upper() + s[1:]


if __name__ == '__main__':
    line = input()
    line = re.sub(r'(\w+)', lambda x: cap(x.group(1)), line)
    print(line)
