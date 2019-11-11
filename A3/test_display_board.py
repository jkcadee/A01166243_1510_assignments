from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import display_board, create_board
from unittest.mock import patch
import io


class TestDisplayBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_1_1(self, mock_stdout):
        player_dictionary = {'Position:': [0, 0]}
        expected_output = 'c\n'
        display_board(create_board(1, 1), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_2_2(self, mock_stdout):
        player_dictionary = {'Position:': [0, 0]}
        expected_output = 'c x\nx x\n'
        display_board(create_board(2, 2), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_5_5(self, mock_stdout):
        player_dictionary = {'Position:': [0, 0]}
        expected_output = 'c x x x x\nx x x x x\nx x x x x\nx x x x x\nx x x x x\n'
        display_board(create_board(5, 5), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_5_5_2_2(self, mock_stdout):
        player_dictionary = {'Position:': [2, 2]}
        expected_output = 'x x x x x\nx x x x x\nx x c x x\nx x x x x\nx x x x x\n'
        display_board(create_board(5, 5), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_2_3(self, mock_stdout):
        player_dictionary = {'Position:': [0, 0]}
        expected_output = 'c x x\nx x x\n'
        display_board(create_board(2, 3), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_0_0(self, mock_stdout):
        player_dictionary = {'Position:': [0, 0]}
        expected_output = ''
        display_board(create_board(0, 0), player_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

