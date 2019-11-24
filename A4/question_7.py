# Global Constant
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
             "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
             "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
             }


def adding_total_calories(total_calories):
    for item in _calories:
        total_calories = total_calories + _calories[item]
    return total_calories


def getting_calorie_value(new_item):
    new_item_calories = int(input("Enter calories for " + new_item + ": "))
    _calories[new_item] = new_item_calories


def appending_food_item_names(food_item_names):
    for item in _calories:
        food_item_names.append(item)


def printing_food_and_calories(food_item_names, total_calories):
    avg_calories = total_calories / len(_calories)
    print("\nFood Items:", sorted(food_item_names))
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)


# Input loop
def calories():
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        getting_calorie_value(new_item)
        total_calories = 0
        total_calories = adding_total_calories(total_calories)
        food_item_names = []
        appending_food_item_names(food_item_names)
        printing_food_and_calories(food_item_names, total_calories)
        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    calories()


if __name__ == "__main__":
    main()