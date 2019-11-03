import random


def roll_die(rolls, sides):
    number = 0
    if rolls < 1 or sides <= 1:
        return 0
    for x in range(1, rolls + 1):
        number += random.randint(1, sides)
    return number
