#!/usr/bin/env python3
# coding: utf-8

"""
Merge the Tools!
https://www.hackerrank.com/challenges/merge-the-tools
"""


def remove_repeated(s):
    """Remove all repeated occurences of the characters in s."""
    result = ''
    seen = set()

    for c in s:
        if c not in seen:
            result += c
        seen.add(c)

    return result


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = ''

    for i in range(0, len(s), n):
        print(remove_repeated(s[i:i + n]))
