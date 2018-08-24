#!/usr/bin/env python3
# coding: utf-8

"""
String Validators
https://www.hackerrank.com/challenges/string-validators
"""

if __name__ == '__main__':
    tests = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    s = input()

    for test in tests:
        print(any(test(c) for c in s))
