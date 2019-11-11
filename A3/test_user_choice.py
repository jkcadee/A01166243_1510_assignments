from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import user_choice
from unittest.mock import patch


class TestUserChoice(TestCase):
    @patch('builtins.input', side_effect=['N'])
    def test_user_choice_N(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'N'
        self.assertEqual(expected_value, the_actual_value)

    @patch('builtins.input', side_effect=['S'])
    def test_user_choice_S(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'S'
        self.assertEqual(expected_value, the_actual_value)

    @patch('builtins.input', side_effect=['E'])
    def test_user_choice_E(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'E'
        self.assertEqual(expected_value, the_actual_value)

    @patch('builtins.input', side_effect=['W'])
    def test_user_choice_W(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'W'
        self.assertEqual(expected_value, the_actual_value)

    @patch('builtins.input', side_effect=['D'])
    def test_user_choice_not_right(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'D'
        self.assertEqual(expected_value, the_actual_value)

    @patch('builtins.input', side_effect=['n'])
    def test_user_choice_lower_case(self, mock_input):
        the_actual_value = user_choice()
        expected_value = 'N'
        self.assertEqual(expected_value, the_actual_value)
