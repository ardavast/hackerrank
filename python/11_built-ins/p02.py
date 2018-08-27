#!/usr/bin/env python3
# coding: utf-8

"""
Input()
https://www.hackerrank.com/challenges/input
"""

if __name__ == '__main__':
    x, k = [int(x) for x in input().split()]
    s = input()

    print(eval(s) == k)
