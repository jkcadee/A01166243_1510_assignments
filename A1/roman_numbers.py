import doctest


def divisor_for_roman_numeral(number_1, number_2):
    """Divides the first parameter by the second parameter
    >>> divisor_for_roman_numeral(10, 5)
    2
    >>> divisor_for_roman_numeral(8, 2)
    4
    """
    num = number_1 / number_2
    return int(num)


"""
Return the quotient of two numbers.

:param number_1: int
:param number_2: int
:precondition: Both parameters must be an int
:postcondition: Divide number_1 by number_2
:return: The quotient of number_1 and number_2
"""


def remainder_number(number_1, number_2):
    """Takes the remainder from the quotient of the first parameter divided by the second
    >>> remainder_number(8, 5)
    3
    >>> remainder_number(11, 10)
    1
    """
    remainder = number_1 % number_2
    return remainder


"""
Return the remainder of two numbers.

:param number_1: int
:param number_2: int
:precondition: Both parameters must be an int
:postcondition: Take the remainder of number_1 divided by number_2
:return: The remainder of number_1 and number_2
"""
m = 1000
# Every 1000
cm = 900
# Every 900
d = 500
# Every 500
cd = 400
# Every 400
c = 100
# Every 100
xc = 90
# Every 90
l = 50
# Every 50
xl = 40
# Every 40
x = 10
# Every 10
ix = 9
# Every 9
v = 5
# Every 5
iv = 4
# Every 4
i = 1
# Every 1


def convert_to_roman_numeral(positive_int):
    """Converts the number in the parameter into a string with characters signifying equivalent values in roman
        numerals
        >>> convert_to_roman_numeral(2)
        'II'
        >>> convert_to_roman_numeral(90)
        'XC'
        """
    if positive_int >= m:
        num_of_m = divisor_for_roman_numeral(positive_int, m)
        positive_int = remainder_number(positive_int, m)
    else:
        num_of_m = 0
# Calculates the amount of M's
    if positive_int >= cm:
        num_of_cm = divisor_for_roman_numeral(positive_int, cm)
        positive_int = remainder_number(positive_int, cm)
    else:
        num_of_cm = 0
# Calculates the amount of CM's
    if positive_int >= d:
        num_of_d = divisor_for_roman_numeral(positive_int, d)
        positive_int = remainder_number(positive_int, d)
    else:
        num_of_d = 0
# Calculates the amount of D's
    if positive_int >= cd:
        num_of_cd = divisor_for_roman_numeral(positive_int, cd)
        positive_int = remainder_number(positive_int, cd)
    else:
        num_of_cd = 0
# Calculates the amount of CD's
    if positive_int >= c:
        num_of_c = divisor_for_roman_numeral(positive_int, c)
        positive_int = remainder_number(positive_int, c)
    else:
        num_of_c = 0
# Calculates the amount of C's
    if positive_int >= xc:
        num_of_xc = divisor_for_roman_numeral(positive_int, xc)
        positive_int = remainder_number(positive_int, xc)
    else:
        num_of_xc = 0
# Calculates the amount of XC's
    if positive_int >= l:
        num_of_l = divisor_for_roman_numeral(positive_int, l)
        positive_int = remainder_number(positive_int, l)
    else:
        num_of_l = 0
# Calculates the amount of L's
    if positive_int >= xl:
        num_of_xl = divisor_for_roman_numeral(positive_int, xl)
        positive_int = remainder_number(positive_int, xl)
    else:
        num_of_xl = 0
# Calculates the amount of XL's
    if positive_int >= x:
        num_of_x = divisor_for_roman_numeral(positive_int, x)
        positive_int = remainder_number(positive_int, x)
    else:
        num_of_x = 0
# Calculates the amount of X's
    if positive_int >= ix:
        num_of_ix = divisor_for_roman_numeral(positive_int, ix)
        positive_int = remainder_number(positive_int, ix)
    else:
        num_of_ix = 0
# Calculates the amount of IX's
    if positive_int >= v:
        num_of_v = divisor_for_roman_numeral(positive_int, v)
        positive_int = remainder_number(positive_int, v)
    else:
        num_of_v = 0
# Calculates the amount of V's
    if positive_int >= iv:
        num_of_iv = divisor_for_roman_numeral(positive_int, iv)
        positive_int = remainder_number(positive_int, iv)
    else:
        num_of_iv = 0
# Calculates the amount of IV's
    if positive_int >= i:
        num_of_i = divisor_for_roman_numeral(positive_int, i)
    else:
        num_of_i = 0
# Calculates the amount of I's
    result = str("M" * int(num_of_m)) \
        + str("CM" * int(num_of_cm)) \
        + str("D" * int(num_of_d)) \
        + str("CD" * int(num_of_cd)) \
        + str("C" * int(num_of_c)) \
        + str("XC" * int(num_of_xc)) \
        + str("L" * int(num_of_l)) \
        + str("XL" * int(num_of_xl)) \
        + str("X" * int(num_of_x)) \
        + str("IX" * int(num_of_ix)) \
        + str("V" * int(num_of_v)) \
        + str("IV" * int(num_of_iv)) \
        + str("I" * int(num_of_i))
# Concatenating the converted characters into a string for display
    return result


"""
Return the parameter converted into roman numerals.

:param positive_int: int
:precondition: Parameter must be an int
:postcondition: Print a string that is equivalent to the parameter
:return: A string equivalent to the parameter
"""


def main():
    """Executes the program"""
    print(convert_to_roman_numeral(1994))
    return


if __name__ == "__main__":
    main()
    doctest.testmod()
"""
For divisor_for_roman_numeral and remainder_number, I used decomposition, automation and pattern matching. The functions 
could have been split up from the main one and make use of repetitive operations that gain input in a similar way. The
convert_to_roman_numerals function uses automation with similar repetitive operations but also uses some pattern
matching when determining which value gets converted into which corresponding roman numeral. 
"""