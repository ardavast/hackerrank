#!/usr/bin/env python3
# coding: utf-8

"""
Introduction to Sets
https://www.hackerrank.com/challenges/py-introduction-to-sets
"""

from statistics import mean

if __name__ == '__main__':
    n = int(input())
    heights = [int(x) for x in input().split()]
    heights = heights[:n]

    unique_heights = set(heights)

    print(mean(unique_heights))
