import random


def generate_consonant():
    """Generates a consonant."""
    consonant = "BCDFGHJKLMNPQRSTVWXYZ"
    return random.sample(consonant, 1)


def generate_vowel():
    """Generates a vowel."""
    vowel = "AEIOUY"
    return random.sample(vowel, 1)


def generate_syllable():
    """Generates a syllable using a consonant and a vowel."""
    syllable = generate_consonant() + generate_vowel()
    return syllable


def random_name(name_length):
    syllable = ''
    for x in range(1, name_length + 1):
        name = ''.join(generate_syllable())
        syllable += name
    return syllable.capitalize()


def opp_character():
    the_character = {'Name:': random_name(random.randint(1, 3)),
                     'Style Level:': [5, 5],  # SL list: 1st value is max SL, second is current SL
                     }
    return the_character
