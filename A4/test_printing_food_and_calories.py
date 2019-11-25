from unittest import TestCase
from A01166243_1510_assignments.A4.question_7 import printing_food_and_calories
from unittest.mock import patch
import io


class TestPrintingFoodAndCalories(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printing_food_and_calories(self, mock_output):
        expected_output = f"\nFood Items: {sorted(['Garlic', 'Pasta', 'Tomato', 'Cheese'])}\nTotal Calories: {500}" \
                          f" Average Calories: {41.7}\n\n"
        printing_food_and_calories(['Garlic', 'Pasta', 'Tomato', 'Cheese'], 500)
        self.assertEqual(expected_output, mock_output.getvalue())
