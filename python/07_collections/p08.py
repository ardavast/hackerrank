#!/usr/bin/env python3
# coding: utf-8

"""
Piling Up!
https://www.hackerrank.com/challenges/piling-up
"""

from collections import deque


def pop(deq):
    if deq[0] >= deq[-1]:
        return deq.popleft()
    else:
        return deq.pop()

def can_pile(deq):
    top = pop(deq);

    while deq:
        if top < deq[0] or top < deq[-1]:
            return False

        top = pop(deq);

    return True

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        input()
        cubes = deque([int(x) for x in input().split()])

        if can_pile(cubes):
            print('Yes')
        else:
            print('No')
