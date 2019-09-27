import random


def number_generator():
    length = 6
    set_of_six_numbers = random.sample(range(1, 49), length)
    set_of_six_numbers.sort()
    return set_of_six_numbers


def main():
    print(number_generator())


if __name__ == "__main__":
    main()

