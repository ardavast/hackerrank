#!/usr/bin/env python3
# coding: utf-8

"""
Word Order
https://www.hackerrank.com/challenges/word-order
"""

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    words = OrderedDict()

    for _ in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1

    print(len(words))
    print(*words.values())
