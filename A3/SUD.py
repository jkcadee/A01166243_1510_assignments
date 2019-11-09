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
            print(f"{opp_one['Name:']} rolls {opp_one_roll}, they go first!")
            roll_again = False
        elif opp_one_roll < opp_two_roll:
            opp_two_goes_first = True
            print(f"{opp_two['Name:']} rolls {opp_two_roll}, they go first!")
            roll_again = False
    if opp_one_goes_first:
        return 1
    elif opp_two_goes_first:
        return 2


def combat(opponent_one, opponent_two):
    turn_1_player = roll_for_advantage(opponent_one, opponent_two)
    opponent = {}
    player = {}
    if turn_1_player == 1:
        player = opponent_one
        opponent = opponent_two
    elif turn_1_player == 2:
        player = opponent_two
        opponent = opponent_one
    roll_hit = roll_die(1, 20)
    combat_round(roll_hit, opponent, player,)
    switch_turns(turn_1_player)


def combat_round(roll_to_hit: int, opponent: dict, player: dict):
    still_alive = True
    while still_alive:
        if roll_to_hit > 10:
            opponent['Style Level:'][1] -= roll_die(1, 6)
            print(opponent['Style Level:'])
            if player['Style Level:'][1] <= 0:
                print(f"You ({opponent['Name:']}) have been killed in battle.")
                still_alive = False
            elif opponent['Style Level:'][1] <= 0:
                print(f"{opponent['Name:']} has been killed in battle. You are victorious!")
                still_alive = False
        else:
            print(f"Miss! {opponent['Name:']} has {opponent['Style Level:'][1]} hit points left. You "
                  f"({player['Name:']}) have {player['Style Level:'][1]} hit points left.")


def switch_turns(turn_1_player: int) -> int:
    if turn_1_player == 1:
        return 2
    elif turn_1_player == 2:
        return 1


def game():
    character = player_character(roll_die(1, 3), roll_die(1, 3))
    foe = opp_character()
    # board = create_board(5, 5)
    # while True:
    #     display_board(board, character)
    #     character['Position:'] = validate_move(5, character, user_choice())
    combat(character, foe)

def main():
    game()


if __name__ == '__main__':
    main()