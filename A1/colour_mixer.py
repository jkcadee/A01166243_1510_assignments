def colour_mixer():
    colour = int(input("Enter your first colour (Red = 0) (Blue = 1) (Yellow = 2):"))
    colour_2 = int(input("Enter your second colour (Red - 0) (Blue = 1) (Yellow = 2):"))
    if colour + colour_2 == 1:
        print("Your secondary colour is purple.")
    elif colour + colour_2 == 2:
        print("Your secondary colour is orange.")
    elif colour + colour_2 == 3:
        print("Your secondary colour is green.")
    else:
        print("Invalid colour combination.")
    return


"""
Return the colour combination from two inputted values.

:precondition: Must input a number between 0 and 2
:postcondition: Output a string based on the operation from the two numbers inputted
:return: A string containing the colour combination
"""


def main():
    colour_mixer()
    return


"""
Executes the program
"""

if __name__ == "__main__":
    main()
