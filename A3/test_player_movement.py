from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import player_movement


class TestPlayerMovement(TestCase):
    def test_player_movement_move_valid_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([1, 0], player_movement(player_dictionary, 5, 'S'))

    def test_player_movement_move_not_valid_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], player_movement(player_dictionary, 5, 'N'))

    def test_player_movement_move_valid_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 1], player_movement(player_dictionary, 5, 'E'))

    def test_player_movement_move_not_valid_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], player_movement(player_dictionary, 5, 'W'))

    def test_player_movement_move_valid_max_1_NS(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], player_movement(player_dictionary, 1, 'S'))

    def test_player_movement_move_valid_max_1_EW(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], player_movement(player_dictionary, 1, 'E'))

    def test_player_movement_empty_valid(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([1, 0], player_movement(player_dictionary, 0, 'S'))

    def test_player_movement_empty_not_valid(self):
        player_dictionary = {'Position:': [0, 0]}
        self.assertEqual([0, 0], player_movement(player_dictionary, 0, 'N'))
