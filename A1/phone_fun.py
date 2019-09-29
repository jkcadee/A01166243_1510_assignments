import doctest


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


"""
Return a character converted from a character to it's appropriate corresponding digit or hyphen.

The function takes a character and checks it through the if/elif/else statement. Whenever the if/elif/else statement is
satisfied, it converts the character to it's corresponding digit or hyphen.

:param input_string: string
:precondition: Parameter must be a string
:postcondition: Get a character that has been converted to it's corresponding digit or hyphen
:return: A character converted to it's corresponding digit or hyphen
"""


def number_translator():
    """Takes an inputted phone number and turns the characters into numbers"""
    phone_number = input("Input a ten-digit phone number (XXX-XXX-XXXX): ")
    digit_1 = translation(phone_number[0])
    digit_2 = translation(phone_number[1])
    digit_3 = translation(phone_number[2])
    hyphen_1 = translation(phone_number[3])
    digit_4 = translation(phone_number[4])
    digit_5 = translation(phone_number[5])
    digit_6 = translation(phone_number[6])
    hyphen_2 = translation(phone_number[7])
    digit_7 = translation(phone_number[8])
    digit_8 = translation(phone_number[9])
    digit_9 = translation(phone_number[10])
    digit_10 = translation(phone_number[11])
# Each value here represents a digit (or hyphen) in the inputted phone number XXX-XXX-XXXX
    translated_number = digit_1 \
        + digit_2 \
        + digit_3 \
        + hyphen_1 \
        + digit_4 \
        + digit_5 \
        + digit_6 \
        + hyphen_2 \
        + digit_7 \
        + digit_8 \
        + digit_9 \
        + digit_10
    return translated_number


"""
Return the phone number as a string of numbers from 0 to 9 and two hyphens.

The string is passed through the translation function by each index, translating each one into it's corresponding digit
or hyphen. It is then concatenated and the result is returned.



:precondition: Phone number must only be in the format XXX-XXX-XXXX
:postcondition: The phone number translated into only digits and hyphens in the format of XXX-XXX-XXXX
:return: A string with only digits and hyphens in the format XXX-XXX-XXXX
"""


def main():
    """Executes the program"""
    print(number_translator())
    return


if __name__ == "__main__":
    main()
    doctest.testmod()
"""
I used decomposition and recognizing patterns (repetition) to determine that the translation function could be put into 
a different function. It repeats the same code multiple times until the inputted string is properly converted. I used 
automation to make the number_translator function as the process of concatenating the string can be easily automated 
once you have the converted numbers.
"""