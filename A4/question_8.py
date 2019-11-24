def digit_1(clock_lines_dict: dict, clock_num_list: list, number_of_lines: int):
    for k, v in clock_lines_dict.items():
        if k == 1:
            clock_num_list.append(k)
            number_of_lines += v
    return number_of_lines


def digit_2_to_4(clock_lines_dict: dict, clock_num_list: list, number_of_lines: int, start: int, end: int):
    dict_value = 0
    highest_key = 0
    for k, v in clock_lines_dict.items():
        if start <= k <= end:
            if dict_value < v:
                dict_value = v
                highest_key = k
    clock_num_list.append(highest_key)
    number_of_lines += dict_value
    return number_of_lines


def clock_num_list_formatting(clock_num_list: list):
    return f"{clock_num_list[0]}{clock_num_list[1]}:{clock_num_list[2]}{clock_num_list[3]}"


def im_not_sleepy():
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