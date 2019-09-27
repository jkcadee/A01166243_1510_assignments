import random


def number_generator():
    """Creates six random numbers and orders them from lowest to highest"""
    length = 6
    set_of_six_numbers = random.sample(range(1, 49), length)
# Creating the list of six numbers
    set_of_six_numbers.sort()
    return set_of_six_numbers


"""
Return a list of specified length with numbers between 1 and 49 going from lowest to highest.

:precondition: Length of the list must be specified
:postcondition: A list containing the amount of numbers specified in the length variable
:return: A list that is the specified length with numbers between 1 and 49, sorted from lowest to highest.
"""


def main():
    """Executes the program"""
    print(number_generator())


if __name__ == "__main__":
    main()

