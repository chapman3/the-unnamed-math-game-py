"""
The Unnamed Math Game
test_game.py

test modules for game.py
need one test for each module in game.py
  [X] handle_operation
  [X] init_numbers
  [X] init_white_belt
  [X] init_green_belt
  [X] init_red_belt
  [X] init_black_belt
  [] generate_ans
  [] solve_board
  [] request_hint

  TO-DO: Switch prints to assertions
"""
import game

def test_handle_operations():
    print("=== Testing: handle_operations ===")
    print("Expecting built in functions add, sub, mul, truediv")
    print(game.handle_operation('+'))
    print(game.handle_operation('-'))
    print(game.handle_operation('*'))
    print(game.handle_operation('/'))
    print("==================================")

def test_init_numbers():
    print("===== Testing:  init_numbers =====")
    print("Expecting randomized series of numbers 1-9")
    print(game.shuffle_numbers(game.nums))
    print("==================================")

def test_init_white_belt():
    print('==== Testing: init_white_belt ====')
    print('Expecting gameboard object, all ops +')
    game_board = game.init_white_belt()
    print(game_board.rows)
    print(game_board.cols)
    print(game_board.nums)
    print(game_board.ans)
    print("==================================")
    return

def test_init_green_belt():
    print('==== Testing: init_green_belt ====')
    print('Expecting gameboard object, ')
    print('row ops to +, col ops to -')
    game_board = game.init_green_belt()
    print(game_board.rows)
    print(game_board.cols)
    print(game_board.nums)
    print(game_board.ans)
    print("==================================")
    return

def test_init_red_belt():
    print('===== Testing: init_red_belt =====')
    print('Expecting gameboard object, ')
    print('row ops to +, col ops to *')
    game_board = game.init_red_belt()
    print(game_board.rows)
    print(game_board.cols)
    print(game_board.nums)
    print(game_board.ans)
    print("==================================")
    return

def test_init_black_belt():
    print('==== Testing: init_black_belt ====')
    print('Expecting gameboard object, with randomized operations. ')
    print('Row ops to + and -, col ops to * and /')
    game_board = game.init_black_belt()
    print(game_board.rows)
    print(game_board.cols)
    print(game_board.nums)
    print(game_board.ans)
    print("==================================")
    return

def test_generate_ans():
    print('===== Testing:  generate_ans =====')
    print("==================================")
    return

def test_solve_board():
    print('====== Testing: solve_board ======')
    print("==================================")
    return

def test_request_hint():
    print('====== testing request_hint ======')
    print("==================================")
    return

if __name__ == "__main__":
    print("======= Running Test Cases =======")
    print("==================================")

    #handle_operations
    test_handle_operations()

    #init_numbers
    test_init_numbers()

    #init_white_belt
    test_init_white_belt()

    #init_green_belt
    test_init_green_belt()

    #init_red_belt
    test_init_red_belt()

    #init_black_belt
    test_init_black_belt()

    #generate_ans
    #test_generate_ans()

    #request_hint
    #test_request_hint()
