import random
import A01166243_1510_assignments.A3.character
import A01166243_1510_assignments.A3.monster


def roll_die(rolls, sides):
    number = 0
    if rolls < 1 or sides <= 1:
        return 0
    for x in range(1, rolls + 1):
        number += random.randint(1, sides)
    return number


def create_board(row_size, col_size):
    space = 'x'
    playing_board = []
    for row in range(row_size):
        sub_list = []
        for column in range(col_size):
            sub_list.append(space)
        playing_board.append(sub_list)
    return playing_board


# def player_movement(board, move):  # List (board)
#     for row in range(len(board)):
#         for column in range(len(board[row])):


def display_board(play_board):
    for index in range(len(play_board)):
        for index_two in range(len(play_board[index])):
            if index_two == len(play_board[index]) - 1:
                print(play_board[index][index_two])
            else:
                print(play_board[index][index_two], end=" ")


display_board(create_board(5, 5))
