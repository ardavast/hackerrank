#!/usr/bin/env python3
# coding: utf-8

"""
Map and Lambda Function
https://www.hackerrank.com/challenges/map-and-lambda-expression
"""


def fibonacci(n):
    l = [0, 1]
    for _ in range(n - 2):
        l.append(l[-2] + l[-1])

    return l[0:n]


if __name__ == '__main__':
    n = int(input())
    print([x ** 3 for x in fibonacci(n)])
