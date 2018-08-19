#!/usr/bin/env python3
# coding: utf-8

"""
Python If-Else
https://www.hackerrank.com/challenges/py-if-else
"""

if __name__ == '__main__':
    n = int(input())

    if n % 2 == 1:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
