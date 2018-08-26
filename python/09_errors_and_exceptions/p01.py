#!/usr/bin/env python3
# coding: utf-8

"""
Exceptions
https://www.hackerrank.com/challenges/exceptions
"""

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        try:
            a, b = [int(x) for x in input().split()]
            print(a // b)
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code: {}".format(e))
