from unittest import TestCase
from A01166243_1510_assignments.A4.question_1 import sieve_multiples


class TestSieveMultiples(TestCase):
    def test_sieve_multiples_2(self):
        self.assertEqual([2], sieve_multiples([2]))

    def test_sieve_multiples_5(self):
        self.assertEqual([2, 3, 5], sieve_multiples([2, 3, 4, 5]))

    def test_sieve_multiples_10(self):
        self.assertEqual([2, 3, 5, 7], sieve_multiples([2, 3, 4, 5, 6, 7, 8, 9, 10]))
