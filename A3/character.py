def generate_name():
    return input('What\'s your name?: ')


# def character_coords(x_coord: int, y_coord: int) -> list:
#     return [x_coord, y_coord]


def player_character(x_coord: int, y_coord: int) -> dict:
    the_character = {'Name:': generate_name(),
                     'Style Level:': [10, 10],  # SL list: 1st value is max SL, second is current SL
                     'Inventory:': [],
                     'Position:': [x_coord, y_coord]}
    return the_character


def print_character(a_character):  # Must always be a dictionary
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


# print_character(player_character())
