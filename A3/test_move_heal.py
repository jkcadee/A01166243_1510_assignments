from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import move_heal
from unittest.mock import patch
import io


class TestMoveHeal(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_heal_not_max(self, mock_stdout):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 7]}
        expected_output = f"You now have {player['Style Level:'][1] + 2} style points.\n"
        move_heal(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_heal_not_max_9(self, mock_stdout):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 9]}
        expected_output = f"You now have {player['Style Level:'][1] + 1} style points.\n"
        move_heal(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_heal_max(self, mock_stdout):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10]}
        expected_output = "You've got max style points.\n"
        move_heal(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)