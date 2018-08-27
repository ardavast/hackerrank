#!/usr/bin/env python3
# coding: utf-8

"""
Any or All
https://www.hackerrank.com/challenges/any-or-all
"""

if __name__ == '__main__':
    input()
    l = input().split()

    print(all([int(x) > 0 for x in l] and
          any([x == x[::-1] for x in l])))
