#!/usr/bin/env python3
# coding: utf-8

"""
Mutations
https://www.hackerrank.com/challenges/python-mutations
"""

if __name__ == '__main__':
    s = input()
    line = input().split()
    pos = int(line[0])
    c = line[1]

    s = s[:pos] + c + s[pos + 1:]

    print(s)
