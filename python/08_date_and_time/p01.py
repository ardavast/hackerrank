#!/usr/bin/env python3
# coding: utf-8

"""
Calendar Module
https://www.hackerrank.com/challenges/calendar-module
"""

import datetime

if __name__ == '__main__':
    ts = input()

    dt = datetime.datetime.strptime(ts, "%m %d %Y")
    day = dt.strftime("%A")

    print(day.upper())
