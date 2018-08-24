#!/usr/bin/env python3
# coding: utf-8

"""
No Idea!
https://www.hackerrank.com/challenges/no-idea
"""

if __name__ == '__main__':
    input()
    a = [int(x) for x in input().split()]
    happy = set([int(x) for x in input().split()])
    not_happy = set([int(x) for x in input().split()])

    happiness = 0
    for n in a:
        if n in happy:
            happiness += 1
        if n in not_happy:
            happiness -= 1

    print(happiness)
