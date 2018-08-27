#!/usr/bin/env python3
# coding: utf-8

"""
Zipped!
https://www.hackerrank.com/challenges/zipped
"""

from statistics import mean

if __name__ == '__main__':
    _, rows = [int(x) for x in input().split()]

    marks = []
    for _ in range(rows):
        student_marks = [float(x) for x in input().split()]
        marks.append(student_marks)

    for student_marks in zip(*marks):
        print(mean(student_marks))
