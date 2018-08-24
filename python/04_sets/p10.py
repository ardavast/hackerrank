#!/usr/bin/env python3
# coding: utf-8

"""
Set Mutations
https://www.hackerrank.com/challenges/py-set-mutations
"""

if __name__ == '__main__':
    input()
    s = set([int(x) for x in input().split()])
    n = int(input())

    for _ in range(n):
        cmd, *args = input().split()
        args = set([int(x) for x in input().split()])

        if cmd == 'update':
            s |= args
        elif cmd == 'intersection_update':
            s &= args
        elif cmd == 'symmetric_difference_update':
            s ^= args
        elif cmd == 'difference_update':
            s -= args

    print(sum(s))
