def dijkstra(colour_list: list) -> None:
    for index, value in enumerate(colour_list):
        if value == "red":
            colour_list[index], colour_list[index - 1] = colour_list[index - 1], colour_list[index]


dutch = ['red', 'white', 'blue', 'red', 'blue']
dijkstra(dutch)
print(dutch)