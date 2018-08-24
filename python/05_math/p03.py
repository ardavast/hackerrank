#!/usr/bin/env python3
# coding: utf-8

"""
Triangle Quest 2
https://www.hackerrank.com/challenges/triangle-quest-2
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(((10 ** i - 1) // 9) ** 2)
