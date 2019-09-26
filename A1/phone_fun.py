def translation(input_string):
    if input_string == "-":
        result = "-"
    elif input_string == "A" or input_string == "B" or input_string == "C":
        result = "2"
    elif input_string == "D" or input_string == "E" or input_string == "F":
        result = "3"
    elif input_string == "G" or input_string == "H" or input_string == "I":
        result = "4"
    elif input_string == "J" or input_string == "K" or input_string == "L":
        result = "5"
    elif input_string == "M" or input_string == "N" or input_string == "O":
        result = "6"
    elif input_string == "P" or input_string == "Q" or input_string == "R" or input_string == "S":
        result = "7"
    elif input_string == "T" or input_string == "U" or input_string == "V":
        result = "8"
    elif input_string == "W" or input_string == "X" or input_string == "Y" or input_string == "Z":
        result = "9"
    elif 0 <= int(input_string) <= 9:
        result = input_string
    else:
        result = 0
    return result


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
    phone_number = input("Input a ten-digit phone number (XXX-XXX-XXXX): ")
    result = translation(phone_number[0])
    result_1 = translation(phone_number[1])
    result_2 = translation(phone_number[2])
    result_3 = translation(phone_number[3])
    result_4 = translation(phone_number[4])
    result_5 = translation(phone_number[5])
    result_6 = translation(phone_number[6])
    result_7 = translation(phone_number[7])
    result_8 = translation(phone_number[8])
    result_9 = translation(phone_number[9])
    result_10 = translation(phone_number[10])
    result_11 = translation(phone_number[11])
    translated_number = result \
        + result_1 \
        + result_2 \
        + result_3 \
        + result_4 \
        + result_5 \
        + result_6 \
        + result_7 \
        + result_8 \
        + result_9 \
        + result_10 \
        + result_11
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
    print(number_translator())
    return


"""
Execute the program
"""


if __name__ == "__main__":
    main()
