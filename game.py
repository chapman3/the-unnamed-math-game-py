"""
The Unnamed Math Game
game.py

Contains the main game logic functions for the unnamed math game.
colored belt modes represent karate belts
Functions:
  [X] handle_operation
  [X] init_numbers
  [] init_white_belt
  [] init_green_belt
  [] init_red_belt
  [] init_black_belt
  [] solve_board
  [] request_hint
"""
from random import shuffle
import operator

rowops = {
    'row1op1': '', 'row1op2': '',
    'row2op1': '', 'row2op2': '',
    'row3op1': '', 'row3op2': ''
}

colops = {
    'col1op1': '', 'col1op2': '',
    'col2op1': '', 'col2op2': '',
    'col3op1': '', 'col3op2': ''
}

ans = {
    'row1ans': '', 'row2ans': '', 'row3ans': '',
    'col1ans': '', 'col2ans': '', 'col3ans': ''
}

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.div
}

def handle_operation(op):
    '''
    arguments:
        op: operation type
            accepted inputs are '+', '-', '*', '/'
    return:
        standard operator to be used with two arguments
    '''
    return ops[op]

def init_numbers():
    '''
    arguments:
        none
    return:
        shuffled list of numbers 1-9
    '''
    numbers = [[i+1] for i in range(9)]
    numbers = shuffle(numbers)
    return numbers

def init_white_belt():
    '''
    arguments:
        none
    return:
        easiest game mode starting game board
            all addition operations
    '''
    numbers = init_numbers()

def init_green_belt():
    '''
    arguments:
        none
    return:
        medium game mode starting game board
            ##SUBJECT TO CHANGE##
            all addition operations on rows
            all subtraction operation on columns
    '''
    numbers = init_numbers()

def init_red_belt():
    '''
    arguments:
        none
    return:
        hard game mode starting game board
            ##SUBJECT TO CHANGE##
            all addition operations on rows
            all multiplication operations on columns
    '''
    numbers = init_numbers()

def init_black_belt():
    '''
    arguments:
        none
    return:
        hardest game mode starting game board
            ##SUBJECT TO CHANGE##
            Randomized operations all around
    '''
    numbers = init_numbers()

def solve_board():
    '''
    arguments:
        none
    return:
        solution to game board (updates ans properties)
    '''
    return

def request_hint():
    '''
    arguments:
        none
    return:
        selects a random grid value and displays
    '''
    return

