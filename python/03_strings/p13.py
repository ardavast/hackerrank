#!/usr/bin/env python3
# coding: utf-8

"""
The Minion Game
https://www.hackerrank.com/challenges/the-minion-game
"""


class Player:
    """Player class."""
    def __init__(self, name):
        self.name = name
        self.score = 0


if __name__ == '__main__':
    vowels = 'AEIOU'
    player1 = Player('Stuart')
    player2 = Player('Kevin')
    word = input()

    for (i, c) in enumerate(word):
        if c in vowels:
            player2.score += len(word) - i
        else:
            player1.score += len(word) - i

    if player1.score > player2.score:
        print('{} {}'.format(player1.name, player1.score))
    elif player1.score < player2.score:
        print('{} {}'.format(player2.name, player2.score))
    else:
        print('Draw')
