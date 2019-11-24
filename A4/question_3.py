def check_value(element):
    """
    
    :param element:
    :return:
    """
    return element[1]


def dijkstra(colour_list: list) -> None:
    colour_list.sort(key=check_value)


def main():
    dutch = ['red', 'white', 'blue', 'red', 'blue', 'white', 'blue', 'red', 'white']
    dijkstra(dutch)
    print(dutch)


if __name__ == "__main__":
    main()
