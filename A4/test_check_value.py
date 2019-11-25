from unittest import TestCase
from A01166243_1510_assignments.A4.question_3 import check_value


class TestCheckValue(TestCase):
    def test_check_value_e(self):
        self.assertEqual('e', check_value('red'))

    def test_check_value_h(self):
        self.assertEqual('h', check_value('white'))

    def test_check_value_l(self):
        self.assertEqual('l', check_value('blue'))
