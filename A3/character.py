def generate_name():
    """
    Input character name.

    :return: A string of the inputted name.
    """
    return input('What\'s your name?: ')


def player_character(x_coord: int, y_coord: int) -> dict:
    """
    Return a dictionary containing all character values.

    :param x_coord: Integer.
    :precondition: Must be a value in the board.
    :param y_coord: Integer.
    :precondition: Must be a value in the board.
    :postcondition: Adds generated name and position coordinates to dictionary..
    :return: A dictionary with all the character stats.
    """
    the_character = {'Name:': generate_name(),
                     'Style Level:': [10, 1],  # SL list: 1st value is max SL, second is current SL
                     'Inventory:': [],
                     'Cash:': 0,
                     'Position:': [x_coord, y_coord]}
    return the_character


def print_character(a_character: dict):
    """
    Print the character in a visually appealing way.

    :param a_character: Dictionary.
    :precondition: Must have values inside of it.
    :postcondition: Prints the values in a nice, orderly fashion.
    """
    for stat_name, stat_info in a_character.items():
        if isinstance(stat_info, list):
            stat_list = stat_name + ' '
            for index in range(0, len(stat_info)):
                stat_list += str(stat_info[index])
                if len(stat_info) - 1 > index:
                    stat_list += ', '
            print(stat_list)
        else:
            print(stat_name, stat_info)

