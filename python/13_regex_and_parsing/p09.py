#!/usr/bin/env python3
# coding: utf-8

"""
Validating and Parsing Email Addresses
https://www.hackerrank.com/challenges/validating-named-email-addresses
"""

import re
import email.utils

if __name__ == '__main__':
    re_email = re.compile(r'^[a-z][a-z0-9\._-]+@[a-z]+\.[a-z]{1,3}$', re.I)
    n = int(input())

    for _ in range(n):
        s = input()
        name, email_addr = email.utils.parseaddr(s)
        if re.match(re_email, email_addr):
            print(email.utils.formataddr((name, email_addr)))
