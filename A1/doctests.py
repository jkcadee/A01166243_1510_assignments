import doctest

# roman_numerals


def divisor_for_roman_numeral(number_1, number_2):
    """Divides the first parameter by the second parameter
    >>> divisor_for_roman_numeral(10, 5)
    2.0
    >>> divisor_for_roman_numeral(8, 2)
    4.0
    """
    num = number_1 / number_2
    return num


def remainder_number(number_1, number_2):
    """Takes the remainder from the quotient of the first parameter divided by the second
    >>> remainder_number(8, 5)
    3
    >>> remainder_number(11, 10)
    1
    """
    remainder = number_1 % number_2
    return remainder


def convert_to_roman_numeral(positive_int):
    """Converts the number in the parameter into a string with characters signifying equivalent values in roman
        numerals

    >>> convert_to_roman_numeral(2)
    'II'
    >>> convert_to_roman_numeral(90)
    'XC'
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


# compound_interest


def compound_interest(principal, annual_interest, interest_compound_yearly, account_growth):
    """Takes four parameters and plugs them into a function of arithmetic operators
    >>> compound_interest(3, 0.2, 1, 5)
    7.464959999999998
    >>> compound_interest(2, 0.1, 6, 4)
    2.9738292358927154
    """
    result = principal * (1 + annual_interest / interest_compound_yearly) ** (interest_compound_yearly * account_growth)
    return float(result)


# time_calculator

def seconds_conversion(seconds, conversion):
    """Divides the first parameter by the second parameter
    >>> seconds_conversion(600, 60)
    10
    >>> seconds_conversion(3600, 3600)
    1
    """
    converted_number = seconds / conversion
    return int(converted_number)


def remainder_seconds(seconds, conversion):
    """Takes the remainder of the quotient of the first parameter divided by the second
    >>> remainder_seconds(500, 60)
    20
    >>> remainder_seconds(6500, 3600)
    2900
    """
    remaining_seconds = seconds % conversion
    return remaining_seconds


def time_calculator(seconds):
    """Converts the parameter into four different integers
    >>> time_calculator(40000)
    '0 days, 11 hours, 6 minutes, 40 seconds.'
    >>> time_calculator(590)
    '0 days, 0 hours, 9 minutes, 50 seconds.'
    """
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    if seconds >= seconds_in_day:
        days = seconds_conversion(seconds, seconds_in_day)
        seconds = remainder_seconds(seconds, seconds_in_day)
    else:
        days = 0
# Calculates the amount of days
    if seconds >= seconds_in_hour:
        hours = seconds_conversion(seconds, seconds_in_hour)
        seconds = remainder_seconds(seconds, seconds_in_hour)
    else:
        hours = 0
# Calculates the amount of hours
    if seconds >= seconds_in_minute:
        minutes = seconds_conversion(seconds, seconds_in_minute)
        seconds = remainder_seconds(seconds, seconds_in_minute)
    else:
        minutes = 0
# Calculates the amount of minutes
    if seconds >= 1:
        seconds = seconds_conversion(seconds, 1)
    else:
        seconds = 0
# Calculates the amount of seconds
    result = str(days) \
        + " " \
        + "days," \
        + " " \
        + str(hours) \
        + " " \
        + "hours," \
        + " " \
        + str(minutes) \
        + " " \
        + "minutes," \
        + " " \
        + str(seconds) \
        + " " \
        + "seconds."

    return result

# phone_fun


def translation(input_character):
    """Converts each letter into their corresponding number
    >>> translation("A")
    '2'
    >>> translation("-")
    '-'
    """
    if input_character == "-":
        converted_value = "-"
    elif input_character == "A" or input_character == "B" or input_character == "C":
        converted_value = "2"
    elif input_character == "D" or input_character == "E" or input_character == "F":
        converted_value = "3"
    elif input_character == "G" or input_character == "H" or input_character == "I":
        converted_value = "4"
    elif input_character == "J" or input_character == "K" or input_character == "L":
        converted_value = "5"
    elif input_character == "M" or input_character == "N" or input_character == "O":
        converted_value = "6"
    elif input_character == "P" or input_character == "Q" or input_character == "R" or input_character == "S":
        converted_value = "7"
    elif input_character == "T" or input_character == "U" or input_character == "V":
        converted_value = "8"
    elif input_character == "W" or input_character == "X" or input_character == "Y" or input_character == "Z":
        converted_value = "9"
    elif 0 <= int(input_character) <= 9:
        converted_value = input_character
    else:
        converted_value = 0
    return converted_value


if __name__ == "__main__":
    doctest.testmod()
