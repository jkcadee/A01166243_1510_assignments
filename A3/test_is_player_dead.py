from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import is_player_dead


class TestIsPlayerDead(TestCase):
    def test_is_player_dead_yes(self):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 0], 'Cash:': 0}
        self.assertEqual(True, is_player_dead(player))

    def test_is_player_dead_no(self):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 0}
        self.assertEqual(False, is_player_dead(player))
