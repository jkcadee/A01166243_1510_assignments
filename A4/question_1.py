import doctest


def sieve_multiples(number_list: list) -> list:
    """
    Return a list of prime numbers generated from the parameter list.

    :param number_list: List.
    :precondition: Must be a list with at least one element higher or at 2. Values must be integers. Values my be
    concurrent.
    :postcondition: Loop through the list and determine which values are prime numbers. The prime numbers are added to a
    separate list and that list is returned.
    :return: The list of generated prime numbers.

    >>> sieve_multiples([2, 3, 4, 5, 6, 7, 8])
    [2, 3, 5, 7]
    >>> sieve_multiples([3, 4, 5, 6, 7, 8, 9, 10, 11])
    [2, 3, 5, 7, 11]
    """
    prime_number_list = [2]
    for x in number_list:
        copy_prime_number_list = prime_number_list.copy()
        prime = True
        for y in copy_prime_number_list:
            if x % y == 0:
                prime = False
                break
        if prime:
            prime_number_list.append(x)
    return prime_number_list


def eratothenes(upperbound: int) -> list:
    """
    Return a list of only prime numbers, based on how many elements are inside the generated all_numbers list.

    :param upperbound: Integer.
    :precondition: Must be an integer higher than zero.
    :postcondition: Removes any numbers that are not prime numbers from the all_numbers list and returns a list of prime
    numbers from taken from values from the all_numbers list.
    :return: A list of prime numbers taken from all_numbers list.

    >>> eratothenes(5)
    [2, 3, 5]
    >>> eratothenes(1)
    []
    >>> eratothenes(10)
    [2, 3, 5, 7]
    """
    all_numbers = [i for i in range(0, upperbound + 1)]
    all_numbers.remove(0)
    all_numbers.remove(1)
    return all_numbers if len(all_numbers) == 0 else sieve_multiples(all_numbers)


def main():
    """Runs functions in program"""
    print(eratothenes(30))


if __name__ == "__main__":
    doctest.testmod()
