from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import switch_turns


class TestSwitchTurns(TestCase):
    def test_switch_turns_1(self):
        self.assertEqual(2, switch_turns(1))

    def test_switch_turns_2(self):
        self.assertEqual(1, switch_turns(2))
