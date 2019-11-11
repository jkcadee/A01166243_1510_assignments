from unittest import TestCase
from A01166243_1510_assignments.A3.monster import generate_vowel


class TestGenerateVowel(TestCase):
    def test_generate_vowel_is_in(self):
        vowel = "AEIOUY"
        self.assertTrue(''.join(generate_vowel()) in vowel)

    def test_generate_vowel_length(self):
        self.assertTrue(len(generate_vowel()) == 1, generate_vowel())
