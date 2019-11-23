def check_value(element):
    return element % 2


def dijkstra(colour_list: list) -> None:
    sorted(colour_list, key=check_value)


dutch = ['red', 'white', 'blue', 'red', 'blue', 'white', 'blue', 'red']
test = [1, 2, 4, 5]

sorted(test, key=check_value)
# dijkstra(test)
print(test)
# dijkstra(dutch)
# print(dutch)
