from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import check_if_dead


class TestCheckIfDead(TestCase):
    def test_check_if_dead_player(self):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 0], 'Cash:': 0}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        cash = 100
        self.assertEqual(True, check_if_dead(opponent, player, cash))

    def test_check_if_dead_opponent(self):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 0}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 0]}
        cash = 100
        self.assertEqual(True, check_if_dead(opponent, player, cash))

    def test_check_if_dead_no_one_dies(self):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 0}
        opponent = {'Name:': 'Defender', 'Style Level:': [5, 5]}
        cash = 100
        self.assertEqual(False, check_if_dead(opponent, player, cash))
