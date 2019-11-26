def selection_sort(unsorted_list):
    """
    Sorts the given list.

    :param unsorted_list: List.
    :precondition: List must only contain integers and have more than one value.
    :postcondition: Swap all elements in the list to be in ascending order.
    """
    swap = True
    while swap:
        swap = False
        for index, value in enumerate(unsorted_list):
            if index < len(unsorted_list) - 1:
                if value > unsorted_list[index + 1]:
                    unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]
                    swap = True


def main():
    """Runs the functions"""
    a_list = [0, -1, 9, 30, 8]
    try:
        selection_sort(a_list)
    except TypeError:
        raise TypeError('Must be a list of sortable items! (More than one element).')
    else:
        print(a_list)


if __name__ == "__main__":
    main()
