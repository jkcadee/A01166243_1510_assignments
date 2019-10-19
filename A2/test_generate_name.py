from unittest import TestCase
from A01166243_1510_labs.Lab05.Lab05 import generate_name


class TestGenerateName(TestCase):
    def test_generate_name_no_syllables(self):
        self.assertEqual('', generate_name(0))

    def test_generate_name_length(self):
        self.assertEqual(len(generate_name(2)), 4)

    def test_generate_name_syllable(self):
        consonant = "BCDFGHJKLMNPQRSTVWXYZ"
        vowel = "AEIOUY"
        name = generate_name(2)
        self.assertTrue(name[0] in consonant
                        and name[1].capitalize() in vowel
                        and name[2].capitalize() in consonant
                        and name[3].capitalize() in vowel)



