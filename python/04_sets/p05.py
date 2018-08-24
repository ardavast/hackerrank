#!/usr/bin/env python3
# coding: utf-8

"""
Set .discard(), .remove() & .pop()
https://www.hackerrank.com/challenges/py-set-discard-remove-pop
"""

if __name__ == '__main__':
    input()
    s = set([int(x) for x in input().split()])
    n = int(input())

    for _ in range(n):
        cmd = input().split()

        if cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
        elif cmd[0] == 'pop':
            s.pop()

    print(sum(s))
