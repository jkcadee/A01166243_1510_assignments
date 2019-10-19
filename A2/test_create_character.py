from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import create_character
from unittest.mock import patch


class TestCreateCharacter(TestCase):
    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_name(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Name'], str))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_race(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Race'], str))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_class(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Class'], str))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_health(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['HP'], list))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_stren(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Strength:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_dex(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Dexterity:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_const(self, mock_input):
        char_name = create_character(2)
        self.assertTrue(isinstance(char_name['Constitution:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_intel(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Intelligence:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_wis(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Wisdom:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_char(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Charisma:'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_exp(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Experience'], int))

    @patch('builtins.input', side_effect=[2, 2, 2, -1])
    def test_create_character_inv(self, mock_input):
        char = create_character(2)
        self.assertTrue(isinstance(char['Inventory'], list))
