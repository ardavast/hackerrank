#!/usr/bin/env python3
# coding: utf-8

"""
Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
"""

if __name__ == '__main__':
    input()
    a = [int(x) for x in input().split()]
    second = sorted(set(a))[-2]
    print(second)
