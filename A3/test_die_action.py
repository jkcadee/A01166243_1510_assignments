from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import die_action
from unittest.mock import patch
import io


class TestDieAction(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_die_action_player_dies(self, mock_stdout):
        dead_player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 0}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        expected_output = f"Your ({dead_player['Name:']}) style is been demolished. Back to the drawing board.\n"
        die_action(dead_player, opponent, 100)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_die_action_opponent_dies(self, mock_stdout):
        live_player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 0}
        dead_player = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        cash = 100
        expected_output = f"{dead_player['Name:']}'s style has been dismantled. You're free to keep searching for " \
                          f"your fit.\nYou ({live_player['Name:']}) received ${cash}!\n"
        die_action(dead_player, live_player, cash)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
