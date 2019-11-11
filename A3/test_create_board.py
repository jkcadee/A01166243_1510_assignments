from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import create_board


class TestCreateBoard(TestCase):
    def test_create_board_zero(self):
        self.assertEqual([], create_board(0, 0))

    def test_create_board_one(self):
        self.assertEqual([[(0, 0)]], create_board(1, 1))

    def test_create_board_five(self):
        self.assertEqual([[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
                          [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
                          [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
                          [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
                          [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]], create_board(5, 5))
