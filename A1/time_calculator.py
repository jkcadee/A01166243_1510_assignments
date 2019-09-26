def seconds_conversion(seconds, conversion):
    converted_number = seconds / conversion
    return int(converted_number)


"""
Return the quotient of the two parameters.

:param seconds: int 
:param conversion: int
:precondition: Both parameters must be an int
:postcondition: Divide seconds by conversion
:return: The quotient of the two parameters
"""


def remainder_seconds(seconds, conversion):
    remaining_seconds = seconds % conversion
    return remaining_seconds


"""
Return the remainder of the two parameters divided by each other.

:param seconds: int
:param conversion: int
:precondition: Both parameters must be an int
:postcondition: Take the remainder of seconds divided by conversion
:return: The remainder of the two parameters divided by each other
"""
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60


def time_calculator(seconds):
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


"""
Return the amount of seconds converted into days, hours, minutes and seconds.

:param seconds: int
:precondition: Parameter must be an int
:postcondition: Convert the number in parameter, seconds, into a string which displays days, hours, minutes and seconds
:return: A string with the parameter, seconds, converted into days, hours, minutes and seconds 
"""


def main():
    print(time_calculator(174580))
    return


"""
Executes the program
"""

if __name__ == "__main__":
    main()