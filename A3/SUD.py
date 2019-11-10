from A01166243_1510_assignments.A3.character import *
from A01166243_1510_assignments.A3.monster import *
from A01166243_1510_assignments.A3.constants import *


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
            sub_list.append((row, column))
        playing_board.append(sub_list)
    return playing_board


def user_choice():
    """
    Return a user input of N, S, E, W or Q.

    :precondition: Input must be N, S, E, W.
    :postcondition: Returns the input capitalized.
    :return: The input capitalized.
    """
    move = input('Where would you like to move? (Use N, S, E, W to move North, South, East or West. Press Q to quit '
                 'the game.) \n')
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
    cash = money_generator()
    dead = False
    while not dead:
        if turn_1_player == 1:
            player = opponent_one
            opponent = opponent_two
        elif turn_1_player == 2:
            player = opponent_two
            opponent = opponent_one
        roll_hit = roll_die(1, 20)
        combat_round(roll_hit, opponent, player)
        turn_1_player = switch_turns(turn_1_player)
        if check_if_dead(opponent, player, cash):
            dead = True


def combat_round(roll_to_hit: int, opponent: dict, player: dict):
    if roll_to_hit > 10:
        opponent['Style Level:'][1] -= roll_die(1, 6)
        print(opponent['Style Level:'])
    else:
        print(f"Miss! {opponent['Name:']} has {opponent['Style Level:'][1]} hit points left. You "
              f"({player['Name:']}) have {player['Style Level:'][1]} hit points left.")


def switch_turns(turn_1_player: int) -> int:
    if turn_1_player == 1:
        return 2
    elif turn_1_player == 2:
        return 1


def check_if_dead(opponent: dict, player: dict, cash: int) -> bool:
    if player['Style Level:'][1] <= 0:
        print(f"Your ({opponent['Name:']}) style is been demolished. Back to the drawing board.")
        return True
    elif opponent['Style Level:'][1] <= 0:
        print(f"{opponent['Name:']}'s style has been dismantled. You're free to keep searching for your fit.")
        player['Cash:'] += cash
        print(f"You ({player['Name:']}) received ${cash}!")
        return True
    return False


def combat_initiation(player: dict, foe: dict):
    print(f'{foe["Name:"]} has challenges your style!')
    user_input = input('Stay and fight or leave? (Press F to fight and L to leave)\n').capitalize()
    flee = False
    while not flee:
        if user_input == 'F':
            combat(player, foe)
            flee = True
        elif user_input == 'L':
            flee = True
            flee_chance_damage = roll_die(1, 10)
            if flee_chance_damage == 1:
                damage = roll_die(1, 4)
                player['Style Level:'][1] -= damage
                print(f'You ({player["Name:"]}) got {damage} points off your style!')
            else:
                print(f'You ({player["Name:"]}) got away successfully!')


def move_heal(player: dict):
    if player['Style Level:'][1] < player['Style Level:'][0]:
        player['Style Level:'][1] += 2
    elif player['Style Level:'][1] >= player['Style Level:'][0]:
        player['Style Level:'][1] = player['Style Level:'][0]


def move_event_chance(player: dict, foe: dict, event_spawner: int, store_list: list, store_prices: list) -> bool:
    if event_spawner == 1:
        combat_initiation(player, foe)
        return is_player_dead(player)
    elif event_spawner == 2:
        shopping(store_list, player, store_prices)
    else:
        move_heal(player)
    return False


def is_player_dead(player):
    if player['Style Level:'][1] <= 0:
        return True
    return False


def money_generator():
    luck = roll_die(1, 5)
    if luck == 1:
        money_received = random.randint(1, 2) * 100
        return money_received
    elif luck == 2:
        money_received = random.randint(2, 4) * 100
        return money_received
    elif luck == 3:
        money_received = random.randint(4, 6) * 100
        return money_received
    elif luck == 4:
        money_received = random.randint(6, 8) * 100
        return money_received
    elif luck == 5:
        money_received = random.randint(8, 10) * 100
        return money_received


def shopping(store_list: list, player: dict, store_prices: list):
    temp_stored_items = []
    current_money = player['Cash:']
    while True:
        print('\nHere\'s is our selection:')
        print(f'You have ${current_money} in your wallet.')
        for item in range(0, len(store_list)):
            print(store_list[item])
        pick_item = int(input('\nWhat would you like to buy? (-1 to exit) \n'))
        if pick_item == -1:
            print('\nThank you for your purchase(s).')
            break
        elif pick_item > 0:
            check_if_can_buy(STORE_PRICES, player, pick_item, STORE_LIST, temp_stored_items)
            if store_prices[pick_item - 1] > current_money:
                print(f'This item costs ${store_prices[pick_item - 1]}! You only have ${current_money}.')
            if store_prices[pick_item - 1] <= current_money:
                current_money -= store_prices[pick_item - 1]
        else:
            print('\nThat\'s not a valid option!')
    return temp_stored_items


def check_if_can_buy(store_prices: list, player: dict, pick_item: int, store_list: list, temp_stored_items: list):
    current_money = player['Cash:']
    if store_prices[pick_item - 1] <= current_money:
        temp_item = store_list[pick_item - 1]
        space_pos = temp_item.find(' ')
        item_to_print = temp_item[space_pos + 1: len(temp_item)]
        temp_stored_items.append(item_to_print)
        print('\nThank you for your purchase!')


def game():
    character = player_character(roll_die(1, 3), roll_die(1, 3))
    foe = opp_character()
    board = create_board(5, 5)
    game_over = False
    while not game_over:
        display_board(board, character)
        print(character['Position:'])
        direction = user_choice()
        if direction == 'Q':
            break
        character['Position:'] = validate_move(5, character, direction)
        event = roll_die(1, 4)
        stop = move_event_chance(character, foe, event, STORE_LIST, STORE_PRICES)
        if stop:
            break
    # combat_initiation(character, foe)
    # print(f'You got ${money_generator()}!')
    # shopping(STORE_LIST, character, STORE_PRICES)
    # move_heal(character)
    # print(character['Style Level:'])


def main():
    game()


if __name__ == '__main__':
    main()
