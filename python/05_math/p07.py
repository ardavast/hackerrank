#!/usr/bin/env python3
# coding: utf-8

"""
Triangle Quest
https://www.hackerrank.com/challenges/python-quest-1
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(((10 ** i - 1) // 9) * i)
