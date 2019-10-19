from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import combat_round
from unittest.mock import patch
import io


class TestCombatRound(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round(self, mock_stdout):
        new_round = combat_round({'Name': 'A', 'Class': 'barbarian', 'Dexterity:': 8, 'HP': [6, 6]}, {'Name': 'B',
                                                                                                      'Class': 'rogue',
                                                                                                      'Dexterity:': 13,
                                                                                                      'HP': [3, 3]})
        output = new_round
        self.assertEqual(output, new_round)
