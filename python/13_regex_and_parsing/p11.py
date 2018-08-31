#!/usr/bin/env python3
# coding: utf-8

"""
HTML Parser - Part 1
https://www.hackerrank.com/challenges/html-parser-part-1
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print('-> {} > {}'.format(name, value))

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for name, value in attrs:
            print('-> {} > {}'.format(name, value))

    def handle_endtag(self, tag):
        print("End   :", tag)


if __name__ == '__main__':
    parser = MyHTMLParser()
    n = int(input())

    for _ in range(n):
        s = input()
        parser.feed(s)
