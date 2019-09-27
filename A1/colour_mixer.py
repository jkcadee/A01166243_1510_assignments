def colour_mixer():
    """Takes an input and produces one of four strings depending on it"""
    colour = input("Enter your first colour:").strip().capitalize()
    colour_2 = input("Enter your second colour:").strip().capitalize()
    if colour == "Red" and colour_2 == "Blue":
        print("Your secondary colour is purple.")
    elif colour == "Yellow" and colour_2 == "Red":
        print("Your secondary colour is orange.")
    elif colour == "Blue" and colour_2 == "Yellow":
        print("Your secondary colour is green.")
    else:
        print("Invalid input and/or colour combination.")
    return


"""
Return the colour combination from two inputted values.

:precondition: Must input the correct three colours
:postcondition: Output a string based on the colours inputted
:return: A string containing the colour combination
"""


def main():
    """Executes the program"""
    colour_mixer()
    return


if __name__ == "__main__":
    main()
