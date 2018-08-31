#!/usr/bin/env python3
# coding: utf-8

"""
Detect HTML Tags, Attributes and Attribute Values
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print('-> {} > {}'.format(name, value))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print('-> {} > {}'.format(name, value))


if __name__ == '__main__':
    n = int(input())

    s = ''
    for _ in range(n):
        s += input().rstrip() + '\n'

    parser = MyHTMLParser()
    parser.feed(s)
