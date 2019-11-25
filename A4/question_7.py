import doctest

# Global Constant
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
             "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
             "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
             }


def adding_total_calories(total_calories: int) -> int:
    """
    Return the total amount of calories for each item in the _calories dictionary.

    :param total_calories: Integer.
    :precondition: Must be greater than 0.
    :postcondition: Calculate the total amount of calories in the dictionary.
    :return: The total calories in the dictionary.

    >>> adding_total_calories(0)
    1505
    >>> adding_total_calories(1)
    1506
    """
    for item in _calories:
        total_calories = total_calories + _calories[item]
    return total_calories


def insert_calorie_value(new_item: str) -> None:
    """
    Inserting a new value into the calories dictionary.

    :param new_item: String.
    :precondition: Must be a number.
    :postcondition: Add the new calorie amount into the dictionary.
    """
    new_item_calories = int(input("Enter calories for " + new_item + ": "))
    _calories[new_item] = new_item_calories


def appending_food_item_names(food_item_names: list) -> None:
    """
    Add the food item into the dictionary.

    :param food_item_names: List.
    :precondition: Must have at least one object, that is a food object.
    :postcondition: Add a food item into food_item_names.
    """
    for item in _calories:
        food_item_names.append(item)


def printing_food_and_calories(food_item_names: list, total_calories: int) -> None:
    """
    Print the food items, total calories and average calories.

    :param food_item_names: List.
    :precondition: Must not be an empty list.
    :param total_calories: Integer.
    :precondition: Must be an integer equal to or higher than 0.
    :postcondition: Print out the list of food items, the total calories they contain and the average calories between
                    them.
    """
    avg_calories = total_calories / len(_calories)
    print("\nFood Items:", sorted(food_item_names))
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)


# Input loop
def calories() -> None:
    """
    Ask user for a food item and add it to list, calculate the average the calories and the total calories. Press q to
    quit.

    :precondition: The food item must be a string and a food item. The calories must be integers.
    :postcondition: Print out the food item list, the average and total calories.
    """
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        insert_calorie_value(new_item)
        total_calories = 0
        total_calories = adding_total_calories(total_calories)
        food_item_names = []
        appending_food_item_names(food_item_names)
        printing_food_and_calories(food_item_names, total_calories)
        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    """Runs the functions"""
    calories()


if __name__ == "__main__":
    main()
    doctest.testmod()
