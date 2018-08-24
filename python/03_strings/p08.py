#!/usr/bin/env python3
# coding: utf-8

"""
Text Wrap
https://www.hackerrank.com/challenges/text-wrap
"""

from textwrap import wrap

s, max_width = input(), int(input())
for line in wrap(s, max_width):
    print(s)
