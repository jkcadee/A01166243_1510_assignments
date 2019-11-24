import doctest


def check_value(element: str) -> str:
    """
    Return a the first element in a string.

    :param element: String.
    :precondition: String must have at least two characters inside of it.
    :postcondition: Will return the element at index one in the string.
    :return: The element at index one in the string.

    >>> check_value('red')
    'e'
    >>> check_value('white')
    'h'
    >>> check_value('blue')
    'l'
    """
    return element[1]


def dijkstra(colour_list: list) -> None:
    """
    Sorts the colour list.

    :param colour_list: List.
    :precondition: List must have 'red', 'white' and 'blue' within it.
    :postcondition: Sorts colours in the order of the dutch flag.
    :return: A sorted list with the colours in the order of the dutch flag.
    """
    colour_list.sort(key=check_value)


def main():
    """Runs the functions"""
    dutch = ['red', 'white', 'blue', 'red', 'blue', 'white', 'blue', 'red', 'white']
    dijkstra(dutch)
    print(dutch)


if __name__ == "__main__":
    main()
    doctest.testmod()