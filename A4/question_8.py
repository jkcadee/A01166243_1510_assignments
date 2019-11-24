import doctest


def digit_1(clock_lines_dict: dict, clock_num_list: list, number_of_lines: int) -> int:
    """
    Return the max amount of lines for digit 1.

    :param clock_lines_dict: Dictionary.
    :precondition: Must be {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}
    :param clock_num_list: List.
    :precondition: Must be an empty list.
    :param number_of_lines: Integer.
    :precondition: Must at 0.
    :postcondition: Adds the time into the clock_num_list as the digit. Adds the amount of lines into the
                    number_of_lines.
    :return: The integer stored inside of number_of_lines.

    """
    for time, lines in clock_lines_dict.items():
        if time == 1:
            clock_num_list.append(time)
            number_of_lines += lines
    return number_of_lines


def digit_2_to_4(clock_lines_dict: dict, clock_num_list: list, number_of_lines: int, start: int, end: int) -> int:
    """
    Return the max amount of lines for digits 2 - 4

    :param clock_lines_dict: Dictionary.
    :precondition: Must be {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}
    :param clock_num_list: List.
    :precondition: Must be have 1 value in list.
    :param number_of_lines: Integer.
    :precondition: Must be positive integer.
    :param start: Integer.
    :precondition: Must be 0.
    :param end: Integer.
    :precondition: Must be the final acceptable number in the specific digit slot. (12-hour clock).
    :postcondition: Adds the time into the clock_num_list as the digit. Adds the amount of lines into the
                    number_of_lines.
    :return: The integer stored inside of number_of_lines.
    """
    dict_value = 0
    highest_key = 0
    for time, lines in clock_lines_dict.items():
        if start <= time <= end:
            if dict_value < lines:
                dict_value = lines
                highest_key = time
    clock_num_list.append(highest_key)
    number_of_lines += dict_value
    return number_of_lines


def clock_num_list_formatting(clock_num_list: list) -> str:
    """
    Return the clock_num_list reformatted into a time.

    :param clock_num_list: List.
    :precondition: Must have 4 values in the list.
    :postcondition: Reformat the list into a time as a string.
    :return: A reformatted string for the time.
    """
    return f"{clock_num_list[0]}{clock_num_list[1]}:{clock_num_list[2]}{clock_num_list[3]}"


def im_not_sleepy():
    """

    :return:
    """
    clock_lines_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}
    clock_num_list = []
    number_of_lines = 0
    number_of_lines = digit_1(clock_lines_dict, clock_num_list, number_of_lines)
    number_of_lines = digit_2_to_4(clock_lines_dict, clock_num_list, number_of_lines, 0, 2)
    number_of_lines = digit_2_to_4(clock_lines_dict, clock_num_list, number_of_lines, 0, 5)
    number_of_lines = digit_2_to_4(clock_lines_dict, clock_num_list, number_of_lines, 0, 9)
    return f"The time that requires the highest amount of bars is {clock_num_list_formatting(clock_num_list)}. The " \
           f"amount of bars is {str(number_of_lines)}."


def main():
    print(im_not_sleepy())


if __name__ == "__main__":
    main()