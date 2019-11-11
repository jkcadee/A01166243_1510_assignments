from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_valid_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([1, 0], validate_move(5, player_dictionary, 'S'))

    def test_validate_move_not_valid_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], validate_move(5, player_dictionary, 'N'))

    def test_validate_move_valid_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 1], validate_move(5, player_dictionary, 'E'))

    def test_validate_move_not_valid_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], validate_move(5, player_dictionary, 'W'))

    def test_validate_move_valid_diff_space_N(self):
        player_dictionary = {'Position:': [2, 2]}
        self.assertEqual([1, 2], validate_move(5, player_dictionary, 'N'))

    def test_validate_move_valid_diff_space_W(self):
        player_dictionary = {'Position:': [2, 2]}
        self.assertEqual([2, 1], validate_move(5, player_dictionary, 'W'))

    def test_validate_move_max_1_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], validate_move(1, player_dictionary, 'S'))

    def test_validate_move_max_1_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], validate_move(1, player_dictionary, 'E'))
