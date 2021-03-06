"""
The Unnamed Math Game
game.py

Contains the main game logic functions for the unnamed math game.
colored belt modes represent karate belts
Functions:
  [X] handle_operation
  [X] init_numbers
  [X] init_white_belt
  [X] init_green_belt
  [X] init_red_belt
  [X] init_black_belt
  [X] generate_ans
  [X] check_solution
  [] request_hint
"""
from random import shuffle, choice
import operator
from game_board import Game_Board

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

ans_dict = {
    'row1ans': '', 'row2ans': '', 'row3ans': '',
    'col1ans': '', 'col2ans': '', 'col3ans': ''
}

input_ans_dict = {
    'row1ans': '', 'row2ans': '', 'row3ans': '',
    'col1ans': '', 'col2ans': '', 'col3ans': ''
}

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

nums = [(i+1) for i in range(9)]

def handle_operation(op):
    '''
    arguments:
        op: operation type
            accepted inputs are '+', '-', '*', '/'
    return:
        standard operator to be used with two arguments
    '''
    return ops[op]

def shuffle_numbers(numbers):
    '''
    arguments:
        none
    return:
        shuffled list of numbers 1-9
    '''
    shuffle(numbers)
    return numbers

def init_white_belt():
    '''
    arguments:
        none
    return:
        easiest game mode starting game board
            all addition operations
    '''
    numbers = shuffle_numbers(nums)
    for rowop in rowops:
        rowops[rowop] = '+'
    for colop in colops:
        colops[colop] = '+'
    ans = generate_ans(ans_dict, numbers)
    return Game_Board(rowops,colops,numbers,ans)

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
    numbers = shuffle_numbers(nums)
    for rowop in rowops:
        rowops[rowop] = '+'
    for colop in colops:
        colops[colop] = '-'
    ans = generate_ans(ans_dict, numbers)
    return Game_Board(rowops,colops,numbers,ans)

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
    numbers = shuffle_numbers(nums)
    for rowop in rowops:
        rowops[rowop] = '+'
    for colop in colops:
        colops[colop] = '*'
    ans = generate_ans(ans_dict, numbers)
    return Game_Board(rowops,colops,numbers,ans)

def init_black_belt():
    '''
    arguments:
        none
    return:
        hardest game mode starting game board
            ##SUBJECT TO CHANGE##
            Randomized operations all around
    '''
    numbers = shuffle_numbers(nums)
    for rowop in rowops:
        rowops[rowop] = choice(['+', '-'])
    for colop in colops:
        colops[colop] = choice(['*', '/'])
    ans = generate_ans(ans_dict, numbers)
    return Game_Board(rowops,colops,numbers,ans)

def generate_ans(ans, numbers):
    '''
    arguments:
        ans: empty answer dictionary
    return:
        answer dictionary
    '''
    #row1ans - numbers 0,1,2 with row1op1, row1op2
    row1op1 = handle_operation(rowops['row1op1'])
    row1op2 = handle_operation(rowops['row1op2'])
    ans['row1ans'] = row1op2(row1op1(numbers[0],numbers[1]),numbers[2])

    #row2ans - numbers 3,4,5 with row2op1, row2op2
    row2op1 = handle_operation(rowops['row2op1'])
    row2op2 = handle_operation(rowops['row2op2'])
    ans['row2ans'] = row2op2(row2op1(numbers[3],numbers[4]),numbers[5])

    #row3ans - numbers 6,7,8 with row3op1, row3op2
    row3op1 = handle_operation(rowops['row3op1'])
    row3op2 = handle_operation(rowops['row3op2'])
    ans['row3ans'] = row3op2(row3op1(numbers[6],numbers[7]),numbers[8])

    #col1ans - numbers 0,3,6 with col1op1, col1op2
    col1op1 = handle_operation(colops['col1op1'])
    col1op2 = handle_operation(colops['col1op2'])
    ans['col1ans'] = col1op2(col1op1(numbers[0],numbers[3]),numbers[6])

    #col2ans - numbers 1,4,7 with col2op1, col2op2
    col2op1 = handle_operation(colops['col2op1'])
    col2op2 = handle_operation(colops['col2op2'])
    ans['col2ans'] = col2op2(col2op1(numbers[1],numbers[4]),numbers[7])

    #col3ans - numbers 2,5,8 with col3op1, col3op2
    col3op1 = handle_operation(colops['col3op1'])
    col3op2 = handle_operation(colops['col3op2'])
    ans['col3ans'] = col3op2(col3op1(numbers[2],numbers[5]),numbers[8])

    return ans

def check_solution(user_input, ans):
    '''
    arguments:
        user_input: user input solution to game board
        ans: ans dict already generated on game initialization
    return:
        true if user input is a valid solution
        false otherwise
    '''
    inputAns = generate_ans(input_ans_dict, user_input)
    return inputAns == ans

def request_hint():
    '''
    arguments:
        none
    return:
        selects a random grid value and displays
    '''
    return

