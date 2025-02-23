import doctest


def gcd(a: int, b: int) -> int:
    """
    Return the greatest common denominator of two numbers.

    :param a: Integer.
    :precondition: Must be larger than b, (-25 > 18 in this case).
    :param b: Integer.
    :precondition: Must be smaller than a.
    :postcondition: Generates the greatest common denominator based on the two parameters.
    :return: An integer which is the greatest common denominator of the two parameters.

    >>> gcd(-123, 6)
    3
    >>> gcd(50, 30)
    10
    >>> gcd(-57, -8)
    1
    """
    remainder = a % b
    return gcd(b, remainder) if remainder != 0 else abs(b)


def main():
    """Runs the functions in the program."""
    try:
        print(gcd(70, 9))
    except ZeroDivisionError:
        raise ZeroDivisionError


if __name__ == "__main__":
    main()
    doctest.testmod()
