#!/usr/bin/env python3
# coding: utf-8

"""
Write a function
https://www.hackerrank.com/challenges/write-a-function
"""


def is_leap(year: int) -> bool:
    """Return True if year is leap."""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
