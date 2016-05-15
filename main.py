import game


if __name__ == "__main__":
    new_game_board = game.init_white_belt()
    print(new_game_board.rows)
    print(new_game_board.cols)
    print(new_game_board.ans)
    print(new_game_board.nums)
    input_list = [None]*9
    input1 = input("What's R1C1?")
    input2 = input("What's R1C2?")
    input3 = input("What's R1C3?")
    input4 = input("What's R2C1?")
    input5 = input("What's R2C2?")
    input6 = input("What's R2C3?")
    input7 = input("What's R3C1?")
    input8 = input("What's R3C2?")
    input9 = input("What's R3C3?")
    input_list[0] = input1
    input_list[1] = input2
    input_list[2] = input3
    input_list[3] = input4
    input_list[4] = input5
    input_list[5] = input6
    input_list[6] = input7
    input_list[7] = input8
    input_list[8] = input9
    print(input_list)
    print(game.check_solution(input_list, new_game_board.ans))
    print(new_game_board.nums)