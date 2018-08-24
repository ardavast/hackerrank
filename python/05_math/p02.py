#!/usr/bin/env python3
# coding: utf-8

"""
Find Angle MBC
https://www.hackerrank.com/challenges/find-angle
"""

from math import atan2, degrees

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    mbc = atan2(ab, bc)

    print('{}°'.format(round(degrees(mbc))))
