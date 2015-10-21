#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the pig game"""
import random


class Die(object):
    """
    Attributes: None
    """
    def __init__(self):
        self.rolled = 0

    def throw(self):
        """
        Args:
            None

        Returns:
            rolled (int) : Random number between 1 and 6.

        Examples:
            >>> dice = Die()
            >>> dice.throw()
            >>> 3
        """
        self.rolled = random.choice(range(1, 7))
        return self.rolled


class Player(object):
    """
    Attributes: None
    """

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hold = False
        self.roll = False

    def choice(self):
        """
        Args:
            None
        """
        plyr_choice = raw_input('Choose to hold or roll? \'r\' or \'h\':').lower()
        if plyr_choice[:1] == 'r':
            self.hold = False
            self.roll = True
        elif plyr_choice[:1] == 'h':
            self.roll = False
            self.hold = True
        else:
            self.choice()


class Pig(object):
    """
    Attributes: None
    """

    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.turn_score = 0
        self.toss = random.randint(0, 1)
        self.current_player = None
        self.next_player = None
        self.die = Die()

        if self.toss == 0:
            self.current_player = self.player1
            self.next_player = self.player2
            self.turn()
        else:
            self.current_player = self.player2
            self.next_player = self.player1
            self.turn()

    def turn(self):
        """
        Args:
            None
        """
        while True:
            print '='*80
            print 'It\'s Player {}\'s turn.'.format(self.current_player.name)
            print 'Your score is {}.'.format(self.current_player.score)
            print 'Your score this turn {}.'.format(self.turn_score)
            print '\n'
            self.current_player.choice()
            if self.current_player.roll:
                self.die.throw()
                throw_val = self.die.rolled
                name = self.current_player.name
                player_score = throw_val + self.current_player.score
                if self.die.rolled == 1:
                    print '\n'
                    print 'Your turn is up, you rolled {}.'.format(throw_val)
                    print '*'*40
                    print '\n'
                    self.turn_score = 0
                    self.next_turn()
                    self.turn_score = 0
                elif player_score > 100:
                    print '\n'
                    print '*'*80
                    print 'You have gone over {}.'.format(name)
                    print 'You have a score of {}.'.format(player_score)
                    print 'You have lost the game'
                    break
                else:
                    print 'You have rolled {}.'.format(throw_val)
                    print '\n'
                    self.turn_score += throw_val
            elif self.current_player.hold:
                player_score = self.current_player.score + self.turn_score
                if player_score == 100:
                    print 'You are the Winner {}.'.format(self.current_player.name)
                    print 'You have a score of {}.'.format(self.current_player.score)
                    break
                elif player_score > 100:
                    plyr_name = self.current_player.name
                    print 'You\'ve gone over {}'.format(plyr_name)
                    break
                else:
                    self.current_player.score += self.turn_score
                    self.turn_score = 0
                    self.next_turn()
                    self.turn_score = 0

    def next_turn(self):
        """
        Args:
            None
        """
        next_in_line = self.current_player
        self.current_player = self.next_player
        self.next_player = next_in_line


if __name__ == '__main__':
    GAME = Pig('Mike', 'Cerna')
