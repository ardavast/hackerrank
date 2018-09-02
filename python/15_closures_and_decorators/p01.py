#!/usr/bin/env python3
# coding: utf-8

"""
Standardize Mobile Number Using Decorators
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
"""


def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
    return fun


@wrapper
def sort_phone(l):
        print(*sorted(l), sep='\n')


if __name__ == '__main__':
    n = int(input())

    l = []
    for _ in range(n):
        l.append(input())

    sort_phone(l)
