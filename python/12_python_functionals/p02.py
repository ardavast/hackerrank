#!/usr/bin/env python3
# coding: utf-8

"""
Validating Email Addresses With a Filter
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
"""

import re


def fun(s):
    return bool(re.match(r'[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z0-9]{1,3}$', s))


if __name__ == '__main__':
    n = int(input())

    emails = []
    for _ in range(n):
        email = input()
        if fun(email):
            emails.append(email)

    print(sorted(emails))
