from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import roll_die


class TestRollDie(TestCase):
    def test_roll_die_1(self):
        self.assertTrue(range(1, 6), roll_die(1, 6))

    def test_roll_die_2(self):
        self.assertTrue(range(3, 18), roll_die(3, 6))

    def test_roll_die_3(self):
        self.assertTrue(range(4, 32), roll_die(4, 8))

    def test_roll_die_0(self):
        self.assertEqual(0, roll_die(0, 1))

