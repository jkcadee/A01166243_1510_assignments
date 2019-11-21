import doctest


def eratothenes(upperbound: int) -> list:
    """
    Return a list of only prime numbers, based on how many elements are inside the generated all_numbers list.

    :param upperbound: Integer.
    :precondition: Must be an integer higher than zero.
    :postcondition: Removes any numbers that are not prime numbers from the all_numbers list and returns a list of prime
    numbers from taken from values from the all_numbers list.
    :return: A list of prime numbers taken from all_numbers list.

    # >>> eratothenes(5)
    # [2, 3, 5]
    # >>> eratothenes(1)
    # []
    # >>> eratothenes(10)
    # [2, 3, 5, 7]
    # >>> eratothenes(-1)
    # Wrong input!
    """
    if upperbound <= 0:
        raise ValueError("Invalid Number.")
    bool_primes_list = [True for i in range(0, upperbound + 1)]
    bool_primes_list[0] = False
    bool_primes_list[1] = False
    for index, value in enumerate(bool_primes_list):
        if value:
            for multiple in range(index+index, upperbound + 1, index):
                bool_primes_list[multiple] = False
    primes_list = [index for index, value in enumerate(bool_primes_list) if value]
    return primes_list


def main():
    """Runs functions in program"""
    print(eratothenes(30))


if __name__ == "__main__":
    main()
    doctest.testmod()
