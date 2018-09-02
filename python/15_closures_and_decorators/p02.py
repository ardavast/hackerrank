#!/usr/bin/env python3
# coding: utf-8

"""
Decorators 2 - Name Directory
https://www.hackerrank.com/challenges/decorators-2-name-directory
"""


def person_lister(f):
    def inner(people):
        return [f(x) for x in sorted(people, key=lambda x: int(x[2]))]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    n = int(input())

    persons = []
    for _ in range(n):
        person = input().split()
        persons.append(person)

    print(*name_format(persons), sep='\n')
