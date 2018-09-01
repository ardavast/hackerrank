#!/usr/bin/env python3
# coding: utf-8

"""
XML 1 - Find the Score
https://www.hackerrank.com/challenges/xml-1-find-the-score
"""

import xml.etree.ElementTree as etree


def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(x) for x in node.getchildren())


if __name__ == '__main__':
    n = int(input())

    s = ''
    for _ in range(n):
        s += input()

    tree = etree.ElementTree(etree.fromstring(s))
    root = tree.getroot()

    print(get_attr_number(root))
