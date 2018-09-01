#!/usr/bin/env python3
# coding: utf-8

"""
XML2 - Find the Maximum Depth
https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth
"""

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth

    if maxdepth <= level:
        maxdepth += 1

    for e in elem:
        depth(e, level + 1)


if __name__ == '__main__':
    n = int(input())

    s = ''
    for _ in range(n):
        s += input()

    tree = etree.ElementTree(etree.fromstring(s))
    depth(tree.getroot(), -1)

    print(maxdepth)
