from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import roll_for_advantage
from unittest.mock import patch
import io


class TestRollForAdvantage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_for_advantage(self, mock_stdout):
        roll_for_advantage({'Name': 'A'}, {'Name': 'B'})
        output = roll_for_advantage({'Name': 'A'}, {'Name': 'B'})
        self.assertTrue(mock_stdout.getvalue(), output)

