from unittest import TestCase
from A01166243_1510_assignments.A3.character import generate_name
from unittest.mock import patch


class TestGenerateName(TestCase):
    @patch('builtins.input', side_effect=['J'])
    def test_generate_name(self, mock_input):
        name_value = generate_name()
        expected_output = 'J'
        self.assertEqual(expected_output, name_value)

    @patch('builtins.input', side_effect=['Jkcadee'])
    def test_generate_name_long(self, mock_input):
        name_value = generate_name()
        expected_output = 'Jkcadee'
        self.assertEqual(expected_output, name_value)

    @patch('builtins.input', side_effect=[''])
    def test_generate_name_empty(self, mock_input):
        name_value = generate_name()
        expected_output = ''
        self.assertEqual(expected_output, name_value)