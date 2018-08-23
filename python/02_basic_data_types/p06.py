#!/usr/bin/env python3
# coding: utf-8

"""
Tuples
https://www.hackerrank.com/challenges/python-tuples
"""

if __name__ == '__main__':
    input()
    t = tuple([int(x) for x in input().split()])
    print(hash(t))
