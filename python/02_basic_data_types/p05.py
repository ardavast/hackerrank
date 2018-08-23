#!/usr/bin/env python3
# coding: utf-8

"""
Lists
https://www.hackerrank.com/challenges/python-lists
"""

if __name__ == '__main__':
    l = []
    n = int(input())

    for i in range(n):
        cmd = input().split()

        if cmd[0] == 'insert':
            l.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(l)
        elif cmd[0] == 'remove':
            l.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            l.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            l.sort()
        elif cmd[0] == 'pop':
            l.pop()
        elif cmd[0] == 'reverse':
            l.reverse()
