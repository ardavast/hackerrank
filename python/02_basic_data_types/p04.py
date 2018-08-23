#!/usr/bin/env python3
# coding: utf-8

"""
Finding the percentage
https://www.hackerrank.com/challenges/finding-the-percentage
"""

from statistics import mean

if __name__ == '__main__':
    n = int(input())

    marks = {}
    for _ in range(n):
        name, *scores = input().split()
        scores = [float(x) for x in scores]
        marks[name] = scores

    name = input()
    avg = mean(marks[name])

    print('{:.2f}'.format(avg))
