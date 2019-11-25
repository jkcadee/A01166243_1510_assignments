from unittest import TestCase
from A01166243_1510_assignments.A4.question_7 import adding_total_calories


class TestAddingTotalCalories(TestCase):
    def test_adding_total_calories_1(self):
        self.assertEqual(1506, adding_total_calories(1))

    def test_adding_total_calories_10(self):
        self.assertEqual(1515, adding_total_calories(10))

    def test_adding_total_calories_100(self):
        self.assertEqual(1605, adding_total_calories(100))
