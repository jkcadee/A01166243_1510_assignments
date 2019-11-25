from unittest import TestCase
from A01166243_1510_assignments.A4.question_8 import clock_num_list_formatting


class TestClockNumListFormatting(TestCase):
    def test_clock_num_list_formatting_1_0_0_8(self):
        self.assertEqual("10:08", clock_num_list_formatting([1, 0, 0, 8]))

    def test_clock_num_list_formatting_1_1_0_0(self):
        self.assertEqual("11:00", clock_num_list_formatting([1, 1, 0, 0]))

    def test_clock_num_list_formatting_1_2_3_0(self):
        self.assertEqual("12:30", clock_num_list_formatting([1, 2, 3, 0]))
