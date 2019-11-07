import random
from A01166243_1510_assignments.A3.character import *
from A01166243_1510_assignments.A3.monster import *


def roll_die(rolls, sides):
    number = 0
    if rolls < 1 or sides <= 1:
        return 0
    for x in range(1, rolls + 1):
        number += random.randint(1, sides)
    return number


def create_board(row_size, col_size):
    playing_board = []
    for row in range(row_size):
        sub_list = []
        for column in range(col_size):
            sub_list.append((column, row))
        playing_board.append(sub_list)
    return playing_board


def user_choice():
    """
    Return a user input of N, S, E, W.

    :precondition: Input must be N, S, E, W.
    :postcondition: Returns the input capitalized.
    :return: The input capitalized.
    """
    move = input('Where would you like to move? (Use N, S, E, W to move North, South, East or West.) \n')
    return move.capitalize()


def player_movement(character_coordinates: list, maximum_limit: int, current_position: int, direction: str) -> list:
    if direction in ('N', 'W'):
        if character_coordinates[current_position] != 0:
            character_coordinates[current_position] -= 1
    elif direction in ('S', 'E'):
        if character_coordinates[current_position] != maximum_limit - 1:
            character_coordinates[current_position] += 1
    return character_coordinates


def display_board(play_board: list, character: dict):
    character_key = character['Position:']
    for index in range(len(play_board)):
        for index_two in range(len(play_board[index])):
            character_current_position = [index, index_two]
            if character_current_position == character_key:
                if index_two == len(play_board[index]) - 1:
                    print('c')
                else:
                    print('c', end=" ")
            else:
                if index_two == len(play_board[index]) - 1:
                    print('x')
                else:
                    print('x', end=" ")


def game():
    display_board(create_board(5, 5), player_character(roll_die(1, 3), roll_die(1, 3)))


def main():
    game()


if __name__ == '__main__':
    main()