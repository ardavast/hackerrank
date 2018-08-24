#!/usr/bin/env python3
# coding: utf-8

"""
String Formatting
https://www.hackerrank.com/challenges/python-string-formatting
"""

if __name__ == '__main__':
    n = int(input())

    pad = len("{:b}".format(n))
    for i in range(1, n + 1):
        print('{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}'.format(i, pad))
