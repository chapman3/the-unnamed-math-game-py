"""
The Unnamed Math Game
game_board.py

class describing object game_board which is initialized after a difficulty is selected.
"""

class Game_Board:

    def __init__(self, rows, cols, nums, ans):
        self.rows = rows
        self.cols = cols
        self.nums = nums
        self.ans = ans
        return

