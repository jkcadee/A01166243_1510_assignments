import random


def number_generator():
    length = 6
    numbers = "123456789"
    set_of_six_numbers = random.sample(numbers, length)
    set_of_six_numbers.sort()
    return set_of_six_numbers


def main():
    print(number_generator())


if __name__ == "__main__":
    main()

