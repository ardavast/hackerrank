#!/usr/bin/env python3
# coding: utf-8

"""
Polar Coordinates
https://www.hackerrank.com/challenges/polar-coordinates
"""

from cmath import polar

if __name__ == '__main__':
    z = complex(input())

    mag, phase = polar(z)

    print(mag)
    print(phase)
