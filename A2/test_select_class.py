from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import select_class
from unittest.mock import patch


class TestSelectClass(TestCase):
    @patch('builtins.input', side_effect=[0])
    def test_select_class_barbarian(self, mock_input):
        s_class = select_class()
        expected_class = 'Barbarian'
        self.assertEqual(expected_class, s_class)

    @patch('builtins.input', side_effect=[11])
    def test_select_class_wizard(self, mock_input):
        s_class = select_class()
        expected_class = 'Wizard'
        self.assertEqual(expected_class, s_class)

    @patch('builtins.input', side_effect=[5])
    def test_select_class(self, mock_input):
        s_class = select_class()
        expected_class = 'Monk'
        self.assertEqual(expected_class, s_class)
