from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import combat_round
from unittest.mock import patch
import io


class TestCombatRound(TestCase):
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_hit(self, mock_stdout, mock_random):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10]}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        damage = 1
        expected_output = f"{opponent['Name:']} was hit! You ({player['Name:']}) dealt {damage} damage to them. " \
                          f"They have {opponent['Style Level:'][1] - damage} style points left. You ({player['Name:']}) " \
                          f"have {player['Style Level:'][1]} style points left.\n"
        combat_round(12, opponent, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_miss(self, mock_stdout):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10]}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        expected_output = f"Miss! {opponent['Name:']} has {opponent['Style Level:'][1]} style points left. You " \
                          f"({player['Name:']}) have {player['Style Level:'][1]} style points left.\n"
        combat_round(9, opponent, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
