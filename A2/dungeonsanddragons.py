import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Rolls a die with an inputted amount of rolls and sides.
    >>> roll_die(0, 0)
    0
    """
    number = 0
    if number_of_rolls < 1 or number_of_sides <= 1:
        return 0
    for x in range(1, number_of_rolls + 1):
        number += random.randint(1, number_of_sides)
    return number


"""
Return the sum of a integer created from a set of random numbers based on the number of rolls and the die's sides.

:param number_of_rolls: positive integer, must be more than 1.
:param number_of_sides: positive integer, must be more than 0.
:precondition: Both parameters must be positive integers and rolls must be more than 1.
:postcondition: Receive an integer equivalent to the sum of a "die" created by the number_of_sides and rolled however
                many times as specified by number_of_rolls.
:return: An integer equal to the sum of a die created by number_of_sides rolled by number_of_rolls times.
"""


# print(roll_die(3, 6))


def choose_inventory():
    """Chooses an amount of items from a list depending on the number inputted."""
    store_list = ["1. Mango's Smashing Steel-Toed Boots",
                  "2. The Swedish Sniper Longbow",
                  "3. Crown of the Mews",
                  "4. Engraved APEX: MMXV Cloak",
                  "5. The Bottomless Hungrypouch",
                  "6. Plup's Sensational Pulper",
                  "7. Zain's Crimson Falchion",
                  "8. Lightning's Summit Axe",
                  "9. The Godslayer's Tome",
                  "10. Cody's Convenient ice Blasting Dragon Wand",
                  "11. Scale Armour of The Red-Sun",
                  "12. Wizzy's Excellent Falcon-Grade Kneepads",
                  "13. 20XX-Calibrated Shinegoggles",
                  "14. The Inseparable 'Pew' and 'Fat' Daggers",
                  "15. Johnny's Flaming Falcon-Grade Gloves",
                  "16. Staff of Eternal Melee"]
    temp_stored_items = []

    print('\nWelcome to "The Script!" Adventurer! \nHmm, you look new \'round these parts... \nTell you what, '
          'your first selections here are on me!')
    # Flavour text for the scenario.
    for x in range(0, len(store_list)):
        print('\nHere\'s is our selection:')
        for item in range(0, len(store_list)):
            print(store_list[item])
        pick_item = int(input('\nWhat would you like to buy? (-1 to exit) \n'))
        if pick_item == -1:
            print('\nThank you for your service! Good luck out there Adventurer.')
            break
        elif pick_item == 0:
            print('Hey, you can\'t choose zero items!')
        elif pick_item > 0:
            temp_item = store_list[pick_item - 1]
            space_pos = temp_item.find(' ')
            item_to_print = temp_item[space_pos + 1: len(temp_item)]
            temp_stored_items.append(item_to_print)
            print('\nThank you for your purchase!')
        else:
            print('Hey you can only pick items from the store list!')
    return temp_stored_items

    # OLD CODE
    # if inventory == [] and selection == 0:
    #     return []
    # elif selection < 0:
    #     print("Hey! You can't have negative items!")
    #     return []
    # elif selection > len(inventory):
    #     print("You are over encumbered.")
    #     over_encumbered_list = inventory.copy()
    #     return sorted(over_encumbered_list)
    # elif selection == len(inventory):
    #     equal_list = inventory.copy()
    #     return sorted(equal_list)
    # else:
    #     result = random.choices(inventory, k=selection)
    #     return sorted(result)


"""
Return a list, with your chosen number of items as how many elements are in the list.

:precondition: List must hae at least one element in it, and integer must be positive.
:postcondition: Create a list with the same amount of elements as what is specified in the parameter.
:return: A list with the chosen amount of elements (determined by parameter) in it. 
"""


# print(choose_inventory(['Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'], 4))
# 'Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'

def generate_consonant():
    """Generates a consonant."""
    consonant = "BCDFGHJKLMNPQRSTVWXYZ"
    return random.sample(consonant, 1)


"""
Return a list of one character selected randomly from the string of consonants

:postcondition: Return a list of one character selected randomly from the string.
:return: A list with a single character. 
"""


def generate_vowel():
    """Generates a vowel."""
    vowel = "AEIOUY"
    return random.sample(vowel, 1)


"""
Return a list of one character randomly selected from the string of vowels.

:postcondition: Return a list of one character selected randomly from the string.
:return: A list with a single character.
"""


def generate_syllable():
    """Generates a syllable using a consonant and a vowel."""
    syllable = generate_consonant() + generate_vowel()
    return syllable


"""
Return a list with two characters, one generated by generate_consonant and the other by generate_vowel.

:postcondition: Create a list of two characters, generated by the helper functions.
:return: A list with two characters.
"""


def generate_name(syllables):
    """Generates a name from the amount of syllables inputted."""
    syllable = ''
    for x in range(1, syllables + 1):
        name = ''.join(generate_syllable())
        syllable += name
    return syllable.capitalize()


"""
Return a string created by calling generate_syllable the amount of times syllables is called.

:param syllables: A positive integer.
:precondition: Syllables must be a positive integer.
:postcondition: Creating a string with however many syllables as specified by the parameter.  
:return: A string with however many syllables as specified by the parameter.
"""


def select_race():
    races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
    selecting_race = int(input(f'Select your race, Traveler... {races} \n (Input a number in the range 0 - 8) \n'))
    return races[selecting_race]


"""
Return the input for selected race.

:precondition: Input must be one of the nine races.
:postcondition: An inputted integer corresponding to the index of one of the nine races.
:return: An inputted integer corresponding to the index of consisting of one of the nine races.
"""


def select_class():
    classes = ['Barbarian', 'Bard', 'Cleric',
               'Druid', 'Fighter', 'Monk',
               'Paladin', 'Ranger', 'Rogue',
               'Sorcerer', 'Warlock', 'Wizard']
    selecting_class = int(input(f'\nSelect your class, Traveler... {classes} \n (Input a number in the range 0 - 11) '
                                f'\n'))
    return classes[selecting_class]


"""
Return the input for selected class.

:precondition: Input must be one of the twelve classes.
:postcondition: An inputted integer corresponding to the index of one the twelve classes.
:return: An inputted integer corresponding to the index of one of the twelve classes.
"""


def get_health(chosen_class):
    if chosen_class == 'barbarian':
        health = roll_die(1, 12)
        return health
    elif chosen_class == 'fighter' or chosen_class == 'paladin' or chosen_class == 'ranger':
        health = roll_die(1, 10)
        return health
    elif chosen_class == 'bard' or chosen_class == 'cleric' or chosen_class == 'druid' or \
            chosen_class == 'monk' or chosen_class == 'rogue' or chosen_class == 'warlock':
        health = roll_die(1, 8)
        return health
    elif chosen_class == 'sorcerer' or chosen_class == 'wizard':
        health = roll_die(1, 6)
        return health
    else:
        health = 0
        return health


"""
Return a random integer which is the health value.

:param chosen_class: String which holds the chosen class from select_class.
:precondition: One of the twelve classes must be in the parameter.
:postcondition: A random integer denoting the max health of the character.
:return: An integer which is a randomly generated health value.
"""


def create_character(name_length):
    """Creates a dictionary with a character's name and stats, alongside other values."""
    choose_race = select_race().lower()
    choose_class = select_class().lower()
    max_health = get_health(choose_class)
    print('\nYour body materializes in front of your eyes.\nYou fall out of the sky and hit the ground with a loud'
          ' "THUD".\nYou open your eyes to see a yawning grassy meadow, with the bright blue sky above. \nA cool '
          'breeze grazes your cheek as you scan your surroundings. \nYour eyes land on a shop emblazoned with a '
          'familiar cross-circle sign hanging atop it\'s roof. \nYou enter the shop...')
    # Flavour text for the scenario.
    character_list = {'Name': generate_name(name_length),
                      'Race': choose_race,
                      'Class': choose_class,
                      'HP': [max_health, max_health],
                      'Strength:': roll_die(3, 6),
                      'Dexterity:': roll_die(3, 6),
                      'Constitution:': roll_die(3, 6),
                      'Intelligence:': roll_die(3, 6),
                      'Wisdom:': roll_die(3, 6),
                      'Charisma:': roll_die(3, 6),
                      'Experience': 0,
                      'Inventory': choose_inventory()}
    print('\nYou leave the shop with your haul. You set off north, towards the snowy mountains. Your character stats '
          'are now:')
    # Flavour text for the scenario.
    return character_list


"""
Return a dictionary with the name of the character and their stats, inventory, race, class and health.

:param name_length: A positive integer.
:precondition: Parameter must be a positive integer over 0.
:postcondition: Create a dictionary with the name, stats, inventory, race, class and health of the character.
:return: A dictionary with a name, stats, inventory, race, class and health.
"""


# print(create_character(3))


def opp_character_generation():
    """Creates a dictionary with a character's name and stats, alongside other values. The values are all randomized."""
    name = generate_name(roll_die(1, 3))
    opp_race = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
    opp_class = ['Barbarian', 'Bard', 'Cleric',
                 'Druid', 'Fighter', 'Monk',
                 'Paladin', 'Ranger', 'Rogue',
                 'Sorcerer', 'Warlock', 'Wizard']
    opp_select_race = opp_race[(roll_die(1, 9) - 1)].lower()
    opp_select_class = opp_class[(roll_die(1, 12) - 1)].lower()
    opp_max_health = get_health(opp_select_class)
    opp_char_list = {'Name': name,
                     'Race': opp_select_race,
                     'Class': opp_select_class,
                     'HP': [opp_max_health, opp_max_health],
                     'Strength:': roll_die(3, 6),
                     'Dexterity:': roll_die(3, 6),
                     'Constitution:': roll_die(3, 6),
                     'Intelligence:': roll_die(3, 6),
                     'Wisdom:': roll_die(3, 6),
                     'Charisma:': roll_die(3, 6),
                     'Experience': 0,
                     'Inventory': []}
    return opp_char_list


"""
Return a dictionary with the name of the character and their stats, inventory, race, class and health.

Selecting race and class are randomized through a die roll. The name is generated from 1 - 3 syllables in length.

:param name_length: A positive integer.
:precondition: Parameter must be a positive integer over 0.
:postcondition: Create a dictionary with the name, stats, inventory, race, class and health of the character.
:return: A dictionary with a name, stats, inventory, race, class and health.
"""


# print(opp_character_generation())
def roll_for_advantage(opp_one, opp_two):
    """Roll a die to see who goes first."""
    opp_one_goes_first = 0
    opp_two_goes_first = 0
    roll_again = 1
    while roll_again == 1:
        opp_one_roll = roll_die(1, 20)
        opp_two_roll = roll_die(1, 20)
        if opp_one_roll > opp_two_roll:
            opp_one_goes_first += 1
            print(f"{opp_one['Name']} rolls {opp_one_roll}, they go first!")
            roll_again = 0
        elif opp_one_roll < opp_two_roll:
            opp_two_goes_first += 1
            print(f"{opp_two['Name']} rolls {opp_two_roll}, they go first!")
            roll_again = 0
    if opp_one_goes_first == 1:
        return 1
    elif opp_two_goes_first == 1:
        return 2


"""
Return a value based on which of the two characters roll higher.

The code checks which roll is higher, then assigns that character as going first. If the rolls are the same, it keeps 
rolling until one of the numbers are higher.

:param opp_one: Dictionary.
:param opp_two: Dictionary.
:preconditions: Both parameters must be dictionaries.
:postcondition: Return a number indicating which character goes first.
:return: A number that indicates which character's turn goes first.
"""

# roll_for_advantage(opp_character_generation(),opp_character_generation())

def combat_round(opponent_one, opponent_two):
    """Simulate a combat round between two opponents."""
    who_rolled = roll_for_advantage(opponent_one, opponent_two)
    player = 0
    if who_rolled == 1:
        player += 1
    elif who_rolled == 2:
        player += 2
    opponent = {}
    this_player = {}
    # To store a value, either 1 or 2, to determine which opponent goes first.
    for turn in range(0, 2):
        # Loops until 2 turns have gone. Character going first attacks, and the other defends. Roles switch after 1
        # attack.
        if player == 1:
            this_player = opponent_one
            opponent = opponent_two
        elif player == 2:
            this_player = opponent_two
            opponent = opponent_one
        turn_roll_dice = roll_die(1, 20)
        print(f"You ({this_player['Name']}) rolled {turn_roll_dice}!")
        if turn_roll_dice > opponent['Dexterity:']:
            damage = get_health(this_player['Class'])
            opponent['HP'][1] -= damage
            print(f"{opponent['Name']} was hit! You ({this_player['Name']}) dealt {damage} damage to them. "
                  f"They have {opponent['HP'][1]} hit points left. You ({this_player['Name']}) have "
                  f"{this_player['HP'][1]} hit points left.")
            if opponent_one['HP'][1] <= 0:
                print(f"You ({opponent_one['Name']}) have been killed in battle. Your soul floats towards the heavens"
                      f"...")
                break
            elif opponent_two['HP'][1] <= 0:
                print(f"{opponent_two['Name']} has been killed in battle. You are victorious!")
                break
        # The loop will stop if one of the characters dies.
        else:
            print(f"Miss! {opponent['Name']} has {opponent['HP'][1]} hit points left. You ({this_player['Name']}) have "
                  f"{this_player['HP'][1]} hit points left.")
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

    # THIS CODE IS UNTIL A CHARACTER'S HEALTH IS <= 0
    # while opponent_one['HP'][1] > 0 and opponent_two['HP'][1] > 0:
    #     if player == 1:
    #         this_player = opponent_one
    #         opponent = opponent_two
    #     elif player == 2:
    #         this_player = opponent_two
    #         opponent = opponent_one
    #     turn_roll_dice = roll_die(1, 20)
    #     print(f"You ({this_player['Name']}) rolled {turn_roll_dice}!")
    #     if turn_roll_dice > opponent['Dexterity:']:
    #         damage = get_health(this_player['Class'])
    #         opponent['HP'][1] -= damage
    #         print(f"{opponent['Name']} was hit! You ({this_player['Name']}) dealt {damage} damage to them. "
    #               f"They have {opponent['HP'][1]} hit points left. You ({this_player['Name']}) have "
    #               f"{this_player['HP'][1]} hit points left.")
    #     else:
    #         print(f"Miss! {opponent['Name']} has {opponent['HP'][1]} hit points left. You ({this_player['Name']}) have "
    #               f"{this_player['HP'][1]} hit points left.")
    #     if player == 1:
    #         player = 2
    #     elif player == 2:
    #         player = 1
    # if opponent_one['HP'][1] <= 0:
    #     print(f"{opponent_one['Name']} has been killed in battle.")
    # else:
    #     print(f"{opponent_two['Name']} has been killed in battle.")


"""
Simulate one round of combat.

The first part determines which of the two characters (parameters) goes first.

The second part is a loop that processes one turn for each character. The character that goes first rolls a dice to hit,
if the roll is higher than the dexterity of the other character, they hit and deal damage based on the hit die of their
class. If they roll a number lower than the dexterity of the other character, they miss and the turn switches to the
next character. This repeats so the character that did not go first is attacking and the character that attacked is
defending. 

:param opponent_one: Must be a dictionary with the key values 'Name', 'HP', 'Class' and 'Dexterity'.
:param opponent_two: Must be a dictionary with the key values 'Name', 'HP', 'Class' and 'Dexterity'.
:precondition: Must be a dictionary and have the key values 'Name', 'HP', 'Class' and 'Dexterity'.
:postcondition: Print the result of one combat round (two characters attacking, how much damage they take and if they
die for not.
:return: The results of combat, printed into a series of strings.  
"""


# print(combat_round(opp_character_generation(), opp_character_generation()))


def print_character(character):
    """Prints character."""
    for character_stat, character_stat_info in character.items():
        print(character_stat, character_stat_info)


"""
Print a list with a name the length of the parameter and the stats.

:param character: A positive integer over 0.
:precondition: Parameter must be positive and over 0.
:postcondition: Print created dictionary from create_character.
:return: Print a dictionary with a name, stats, race, class, exp, and inventory.
"""


# print_character(create_character(3))


def main():
    """Runs the functions created earlier in the file."""
    print('Ah! A visitor... Welcome to Fountain of Dreams, Traveler... \nI am the Goddess of Melee... \nI will give '
          'your spirit... corporeal form... \nStart by entering the number of syllables you want in your name...')
    number_of_syllables = int(input())
    print(f'You\'ve chosen {number_of_syllables} as the number of syllables in your name. Now...\n')
    character_created = create_character(number_of_syllables)
    print_character(character_created)
    opp_character = opp_character_generation()
    print('\nOn your way to Icicle Mountain, you encounter an enemy!\n')
    print(f"It's {character_created['Name']} versus {opp_character['Name']}!\n")
    print_character(character_created)
    print('\n')
    print_character(opp_character)
    print('\n')
    combat_round(character_created, opp_character)


if __name__ == "__main__":
    main()
    doctest.testmod()
