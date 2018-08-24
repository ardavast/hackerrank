#!/usr/bin/env python3
# coding: utf-8

"""
Alphabet Rangoli
https://www.hackerrank.com/challenges/alphabet-rangoli
"""

from string import ascii_lowercase


def letters(n, width):
    """Return the letters for row n."""
    s = []

    for i in range(n + 1):
        s.append(ascii_lowercase[width - i - 1])

    s += s[-2::-1]

    return '-'.join(s)


if __name__ == '__main__':
    line = input().split()
    n = int(line[0])

    pad = 4 * n - 3

    for i in range(n):
        print(letters(i, n).center(pad, '-'))

    for i in range(n - 2, -1, -1):
        print(letters(i, n).center(pad, '-'))
