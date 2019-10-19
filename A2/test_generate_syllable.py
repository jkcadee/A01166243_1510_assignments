from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_syllable


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_is_consonant(self):
        consonant = "BCDFGHJKLMNPQRSTVWXYZ"
        self.assertTrue(''.join(generate_syllable())[0] in consonant)

    def test_generate_syllable_is_vowel(self):
        vowel = "AEIOUY"
        self.assertTrue(''.join(generate_syllable())[1] in vowel)

    def test_generate_syllable_length(self):
        self.assertTrue(len(generate_syllable()) == 2, generate_syllable())


