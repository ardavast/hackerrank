#!/usr/bin/env python3
# coding: utf-8

"""
HTML Parser - Part 2
https://www.hackerrank.com/challenges/html-parser-part-2
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)


if __name__ == '__main__':
    n = int(input())

    s = ''
    for _ in range(n):
        s += input().rstrip() + '\n'

    parser = MyHTMLParser()
    parser.feed(s)
