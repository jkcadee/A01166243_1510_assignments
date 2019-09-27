import random
# Importing random.randint


def rock_paper_scissors():
    """Takes an input and produces a string based on the input and the output of the random number generator"""
    r_p_s = random.randint(0, 2)
# Rock = 0, Scissors = 1, Paper = 2
    guess = input("Input either rock, paper or scissors: ").strip().capitalize()
    if guess == "Paper" or guess == "Rock" or guess == "Scissors":
        print(r_p_s)
    else:
        print("Invalid input.")
    if r_p_s == 0 and guess == "Paper":
        print("You won!")
    elif r_p_s == 1 and guess == "Rock":
        print("You won!")
    elif r_p_s == 2 and guess == "Scissors":
        print("You won!")
    elif r_p_s == 0 and guess == "Rock":
        print("You tied.")
    elif r_p_s == 1 and guess == "Scissors":
        print("You tied.")
    elif r_p_s == 2 and guess == "Paper":
        print("You tied.")
    elif r_p_s == 0 and guess == "Scissors":
        print("You lost.")
    elif r_p_s == 1 and guess == "Paper":
        print("You lost.")
    elif r_p_s == 2 and guess == "Rock":
        print("You lost.")
    return


"""
Return a message that says, "You won!", "You tied." or "You lost.", 
depending the the input and the number randomly generated.

:precondition: The inputted value must be an integer between 0 and 2
:postcondition: Receiving one of the three string listed above
:return: A string containing "You won!", "You tied." or "You lost." depending on the input and randomly generated
        number
"""


def main():
    """Executes the program"""
    rock_paper_scissors()
    return


if __name__ == "__main__":
    main()
