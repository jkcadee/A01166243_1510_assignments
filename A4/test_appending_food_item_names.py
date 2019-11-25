from unittest import TestCase
from A01166243_1510_assignments.A4.question_7 import appending_food_item_names


class TestAppendingFoodItemNames(TestCase):
    def test_appending_food_item_names(self):
        food_item_names = []
        appending_food_item_names(food_item_names)
        self.assertEqual(['lettuce',
                          'carrot',
                          'apple',
                          'bread',
                          'pasta',
                          'rice',
                          'milk',
                          'cheese',
                          'yogurt',
                          'beef',
                          'chicken',
                          'butter'], food_item_names)
