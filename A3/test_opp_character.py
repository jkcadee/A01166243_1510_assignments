from unittest import TestCase
from A01166243_1510_assignments.A3.monster import opp_character
from unittest.mock import patch


class TestOppCharacter(TestCase):
    @patch('random.randint', return_value=3)
    def test_opp_character_name(self, mock_random):
        opp_char = opp_character()
        self.assertTrue(isinstance(opp_char['Name:'], str))

    @patch('random.randint', return_value=3)
    def test_opp_character_style_level(self, mock_random):
        opp_char = opp_character()
        self.assertTrue(isinstance(opp_char['Style Level:'], list))