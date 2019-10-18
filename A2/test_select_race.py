from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import select_race
from unittest.mock import patch


class TestSelectRace(TestCase):
    @patch('builtins.input', side_effect=[0])
    def test_select_race_dragonborn(self, mock_input):
        race = select_race()
        expected_race = 'Dragonborn'
        self.assertEqual(expected_race, race)

    @patch('builtins.input', side_effect=[8])
    def test_select_race_tiefling(self, mock_input):
        race = select_race()
        expected_race = 'Tiefling'
        self.assertEqual(expected_race, race)

    @patch('builtins.input', side_effect=[4])
    def test_select_race_half_elf(self, mock_input):
        race = select_race()
        expected_race = 'Half-Elf'
        self.assertEqual(expected_race, race)
