def selection_sort(unsorted_list):
    swap = True
    while swap:
        swap = False
        for index, value in enumerate(unsorted_list):
            if index < len(unsorted_list) - 1:
                if value > unsorted_list[index + 1]:
                    unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]
                    swap = True


def main():
    a_list = [0, -1, 9, 30, 8]
    selection_sort(a_list)
    print(a_list)


if __name__ == "__main__":
    main()
