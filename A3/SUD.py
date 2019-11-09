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


def player_movement(character_coordinates: dict, maximum_limit: int, direction: str) -> dict:  # FIX THIS
    current_position = character_coordinates['Position:']
    if direction in 'N':
        if current_position[0] != 0:
            current_position[0] -= 1
    elif direction in 'S':
        if current_position[0] != maximum_limit - 1:
            current_position[0] += 1
    elif direction in 'W':
        if current_position[1] != 0:
            current_position[1] -= 1
    elif direction in 'E':
        if current_position[1] != maximum_limit - 1:
            current_position[1] += 1
    return current_position


def validate_move(maximum: int, character: dict, direction: str) -> dict:
    """
    Return a list with the modified character list from move_character.

    When direction is N or S, 1 is added or subtracted from the y-coord. When direction is E or W, 1 is added or
    subtracted from the x-coord,

    :param maximum: An int.
    :precondition: Must be an integer.
    :param character: A list.
    :precondition: Must be a list.
    :param direction: A string.
    :precondition: Must be a string.
    :postcondition: Returns the changed character list from move_character depending on which direction was selected.
    :return: A list modified by move_character depending on the direction selected.


    """
    if direction in ('N', 'S'):
        character = player_movement(character, maximum, direction)
    elif direction in ('E', 'W'):
        character = player_movement(character, maximum, direction)
    return character


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


def roll_for_advantage(opp_one, opp_two):
    """Roll a die to see who goes first."""
    opp_one_goes_first = False
    opp_two_goes_first = False
    roll_again = True
    while roll_again:
        opp_one_roll = roll_die(1, 20)
        opp_two_roll = roll_die(1, 20)
        if opp_one_roll > opp_two_roll:
            opp_one_goes_first = True
            print(f"{opp_one['Name']} rolls {opp_one_roll}, they go first!")
            roll_again = False
        elif opp_one_roll < opp_two_roll:
            opp_two_goes_first += True
            print(f"{opp_two['Name']} rolls {opp_two_roll}, they go first!")
            roll_again = False
    if opp_one_goes_first:
        return 1
    elif opp_two_goes_first:
        return 2


def combat(opponent_one, opponent_two):
    player = roll_for_advantage(opponent_one, opponent_two)
    opponent = {}
    this_player = {}
    if player == 1:
        this_player = opponent_one
        opponent = opponent_two
    elif player == 2:
        this_player = opponent_two
        opponent = opponent_one
    turn_roll_dice = roll_die(1, 20)
    # combat
    if player == 1:
        player = 2
    elif player == 2:
        player = 1


def game():
    character = player_character(roll_die(1, 3), roll_die(1, 3))
    print(character['Position:'])
    board = create_board(5, 5)
    while True:
        display_board(board, character)
        character['Position:'] = validate_move(5, character, user_choice())


def main():
    game()


if __name__ == '__main__':
    main()