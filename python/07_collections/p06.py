#!/usr/bin/env python3
# coding: utf-8

"""
Collections.deque()
https://www.hackerrank.com/challenges/py-collections-deque
"""

from collections import deque

if __name__ == '__main__':
    deq = deque()
    n = int(input())

    for i in range(n):
        cmd = input().split()

        if cmd[0] == 'append':
            deq.append(int(cmd[1]))
        elif cmd[0] == 'pop':
            deq.pop()
        elif cmd[0] == 'popleft':
            deq.popleft()
        elif cmd[0] == 'appendleft':
            deq.appendleft(int(cmd[1]))

    print(*deq)
