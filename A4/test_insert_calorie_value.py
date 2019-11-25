from unittest import TestCase
from A01166243_1510_assignments.A4.question_7 import insert_calorie_value
from unittest.mock import patch


class TestInsertCalorieValue(TestCase):
    @patch('builtins.input', side_effect=['15'])
    def test_insert_calorie_value(self, mock_input):
        new_item = mock_input
        insert_calorie_value(new_item)
        self.assertTrue(new_item, int)
