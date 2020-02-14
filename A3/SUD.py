from A3.character import *
from A3.monster import *
from A3.constants import *
import doctest


def roll_die(rolls: int, sides: int) -> int:
    """Rolls a die with an inputted amount of rolls and sides.
    Return the sum of a integer created from a set of random numbers based on the number of rolls and the die's sides.

    :param rolls: positive integer, must be more than 1.
    :param sides: positive integer, must be more than 0.
    :precondition: Both parameters must be positive integers and rolls must be more than 1.
    :postcondition: Receive an integer equivalent to the sum of a "die" created by the number_of_sides and rolled however
                    many times as specified by number_of_rolls.
    :return: An integer equal to the sum of a die created by number_of_sides rolled by number_of_rolls times.

        >>> roll_die(0, 0)
        0
        """
    number = 0
    if rolls < 1 or sides <= 1:
        return 0
    for x in range(1, rolls + 1):
        number += random.randint(1, sides)
    return number


def create_board(row_size: int, col_size: int) -> list:
    """Return a game board with rows of lists that contain tuples by index (x, y).

    :param row_size: Int.
    :precondition: Must be an integer.
    :param col_size: Int.
    :precondition: Must be an integer.
    :postcondition: Creates a list with sub-lists containing tuples (x-coord, y-coord)
    :return: A list with (x-coord, y-coord) tuples. (0 - 4)

    >>> create_board(1, 1)
    [[(0, 0)]]
    >>> create_board(2, 2)
    [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]
    """
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


def player_movement(character_coordinates: dict, maximum_limit: int, direction: str) -> dict:
    """Return a list of changed character coordinates. The function also checks if the move is valid.

    N and W always subtract 1 from the position, and S and E always add one to the position.

    :param character_coordinates: A list.
    :precondition: Must be a list.
    :param maximum_limit: An int.
    :precondition: Must be an integer.
    :param direction: A string.
    :precondition: Must be a string.
    :postcondition: Returns the changed character list with either 1 added to x, y or 1 subtracted from x, y positions.
    :return: A list with 1 added to x, y or 1 subtracted from x, y positions. Will not move is coords == 0 or maximum.

    """
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
    else:
        print('Incorrect input.')
    return character


def display_board(play_board: list, character: dict):
    """
    Print an 'x' for an empty space, and a 'c' for where the character is.

    :param play_board: A list.
    :precondition: Must be a list.
    :param character: A list.
    :precondition: Must be a list.
    :postcondition: Prints an empty space 'x' and the character's location 'c'.
    """
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
    """Roll a die to see who goes first.
    Return a value based on which of the two characters roll higher.

    The code checks which roll is higher, then assigns that character as going first. If the rolls are the same, it keeps
    rolling until one of the numbers are higher.

    :param opp_one: Dictionary.
    :param opp_two: Dictionary.
    :preconditions: Both parameters must be dictionaries.
    :postcondition: Return a number indicating which character goes first.
    :return: A number that indicates which character's turn goes first.
    """
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


def combat(opponent_one: dict, opponent_two: dict):
    """
    Run all functions related to combat.

    :param opponent_one: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :param opponent_two: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :postcondition: Combat is run until someone dies.
    """
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
    """
    Simulate a combat round between two opponents.

    :param roll_to_hit: Integer.
    :precondition: Roll to hit must be between 1, 20
    :param opponent: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :postcondition: Deal damage if hit lands and print a message, print a message if attack misses.
    """
    if roll_to_hit > 10:
        damage = roll_die(1, 6)
        opponent['Style Level:'][1] -= damage
        print(f"{opponent['Name:']} was hit! You ({player['Name:']}) dealt {damage} damage to them. "
              f"They have {opponent['Style Level:'][1]} style points left. You ({player['Name:']}) have "
              f"{player['Style Level:'][1]} style points left.")
    else:
        print(f"Miss! {opponent['Name:']} has {opponent['Style Level:'][1]} style points left. You "
              f"({player['Name:']}) have {player['Style Level:'][1]} style points left.")


def switch_turns(turn_1_player: int) -> int:
    """
    Switches the order for the character that goes first.

    :param turn_1_player: An integer.
    :precondition: Must be 1 or 2.
    :return: An integer.
    """
    if turn_1_player == 1:
        return 2
    elif turn_1_player == 2:
        return 1


def check_if_dead(opponent: dict, player: dict, cash: int) -> bool:
    """
    Return a boolean based on whether or not the character is alive.

    :param opponent: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :param cash: Integer.
    :precondition: Must be higher than 0.
    :postcondition: Check whether or not the player or the opponent dead, if the opponent dies, the player receives
    cash.
    :return: A boolean based on if the characters are dead or not.
    """
    if player['Style Level:'][1] <= 0:
        die_action(player, opponent, cash)
        return True
    elif opponent['Style Level:'][1] <= 0:
        die_action(opponent, player, cash)
        return True
    return False


def die_action(dead_player: dict, live_player: dict, cash: int):
    """
    Determine if the user or computer dies in combat.

    :param dead_player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :param live_player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :param cash: Integer.
    :precondition: Must be a value over 0.
    :postcondition: Prints whether or not the user or computer dies. Puts cash into the user dictionary if the computer
    dies.
    """
    key = 'Cash:'
    if key in dead_player:
        print(f"Your ({dead_player['Name:']}) style is been demolished. Back to the drawing board.")
    else:
        print(f"{dead_player['Name:']}'s style has been dismantled. You're free to keep searching for your fit.")
        live_player['Cash:'] += cash
        print(f"You ({live_player['Name:']}) received ${cash}!")


def combat_initiation(player: dict, foe: dict):
    """
    Set up the combat loop.

    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :param foe: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :postcondition: Run the while loop. If L is pressed, the character flees and may take damage. If F is pressed, the
    fight is started.
    """
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
    """
    Heals the player if they step on an empty space.

    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :postcondition: Heal the player if they have less than max health.
    """
    if player['Style Level:'][1] == 9:
        player['Style Level:'][1] += 1
        print(f"You now have {player['Style Level:'][1]} style points.")
    elif player['Style Level:'][1] < player['Style Level:'][0]:
        player['Style Level:'][1] += 2
        print(f"You now have {player['Style Level:'][1]} style points.")
    elif player['Style Level:'][1] >= player['Style Level:'][0]:
        player['Style Level:'][1] = player['Style Level:'][0]
        print("You've got max style points.")


def move_event_chance(player: dict, foe: dict, event_spawner: int, store_list: list, store_prices: list) -> bool:
    """
    Return a boolean that states whether or not the player is dead.

    Run an if/else statement that determines what happens when the player moves. Will return False if player is alive.

    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:', 'Cash:'.
    :param foe: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :param event_spawner: Integer.
    :precondition: Must be from 1 - 4.
    :param store_list: List.
    :precondition: Must have at least one item in it.
    :param store_prices: List.
    :precondition: Must have at least one item in it.
    :return: A boolean that states whether or not the player dies.
    """
    if event_spawner == 1:
        combat_initiation(player, foe)
        return is_player_dead(player)
    elif event_spawner == 2:
        shopping(store_list, player, store_prices)
    else:
        move_heal(player)
    return False


def is_player_dead(player: dict) -> bool:
    """
    Return a boolean if the player is dead or not.

    :param player: Dictionary.
    :precondition: Dictionary must have 'Name:', 'Style Level:'.
    :return: A boolean depending if the player is dead or not
    """
    if player['Style Level:'][1] <= 0:
        return True
    return False


def money_generator():
    """
    Return an integer denoting how much money is received.

    :return: A number based on how lucky the player is.
    """
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


def shopping(store_list: list, player: dict, store_prices: list) -> list:
    """
    Return a list based on what items were bought.

    :param store_list: List.
    :precondition: Must have at least one item in it.
    :param player: Dictionary.
    :precondition: Dictionary must have 'Cash:'.
    :param store_prices: List.
    :precondition: Must have at least one item in it.
    :postcondition: Appends an item into the list based on if it can be bought.
    :return: A list of bought items.
    """
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
    """
    Check if the player has enough money to buy the items in the store list.

    :param store_prices: List.
    :precondition: Must have at least one item in it.
    :param player: Dictionary.
    :precondition: Dictionary must have 'Cash:'.
    :param pick_item: Integer.
    :precondition: Must be a number + 1 the store list index.
    :param store_list: List.
    :precondition: Must have at least one item in it.
    :param temp_stored_items: List.
    :precondition: Must have at least one item in it.
    :postcondition: Will check if the character has enough money to buy the item. It will get added to their inventory
    if yes.
    """
    current_money = player['Cash:']
    if store_prices[pick_item - 1] <= current_money:
        temp_item = store_list[pick_item - 1]
        space_pos = temp_item.find(' ')
        item_to_print = temp_item[space_pos + 1: len(temp_item)]
        temp_stored_items.append(item_to_print)
        print(f'\nYou have purchased {item_to_print}. Thank you for your purchase!')


def game():
    """
    Runs game logic.
    """
    print("Welcome to 'Find Your Fit'!, feel free to play for as long as you want, there is no win condition.")
    character = player_character(roll_die(1, 3), roll_die(1, 3))
    board = create_board(5, 5)
    game_over = False
    print('Your character is:')
    print_character(character)
    while not game_over:
        foe = opp_character()
        display_board(board, character)
        print(character['Position:'])
        print(f"Your items are {character['Inventory:']}")
        direction = user_choice()
        if direction == 'Q':
            print('Thanks for playing!')
            break
        character['Position:'] = validate_move(5, character, direction)
        event = roll_die(1, 4)
        stop = move_event_chance(character, foe, event, STORE_LIST, STORE_PRICES)
        if stop:
            break


def main():
    """Runs main functions (game).
    """
    game()
    doctest.testmod()


if __name__ == '__main__':
    main()
