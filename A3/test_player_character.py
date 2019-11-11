from unittest import TestCase
from A01166243_1510_assignments.A3.character import player_character
from unittest.mock import patch


class TestPlayerCharacter(TestCase):
    @patch('builtins.input', side_effect=['J'])
    def test_player_character_name(self, mock_input):
        player = player_character(1, 1)
        self.assertTrue(isinstance(player['Name:'], str))

    @patch('builtins.input', side_effect=['J'])
    def test_player_character_style_level(self, mock_input):
        player = player_character(1, 1)
        self.assertTrue(isinstance(player['Style Level:'], list))

    @patch('builtins.input', side_effect=['J'])
    def test_player_character_inventory(self, mock_input):
        player = player_character(1, 1)
        self.assertTrue(isinstance(player['Inventory:'], list))

    @patch('builtins.input', side_effect=['J'])
    def test_player_character_cash(self, mock_input):
        player = player_character(1, 1)
        self.assertTrue(isinstance(player['Cash:'], int))

    @patch('builtins.input', side_effect=['J'])
    def test_player_character_position(self, mock_input):
        player = player_character(1, 1)
        self.assertTrue(isinstance(player['Position:'], list))