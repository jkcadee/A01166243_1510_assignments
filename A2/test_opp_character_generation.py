from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import opp_character_generation
from unittest.mock import patch


class TestOppCharacterGeneration(TestCase):
    @patch('random.randint', return_value=2)
    def test_opp_character_generation_name(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Name'], str))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_race(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Race'], str))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_class(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Class'], str))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_hp(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['HP'], list))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_dex(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Dexterity:'], int))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_exp(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Experience'], int))

    @patch('random.randint', return_value=2)
    def test_opp_character_generation_inv(self, mock_random):
        opp_char = opp_character_generation()
        self.assertTrue(isinstance(opp_char['Inventory'], list))
