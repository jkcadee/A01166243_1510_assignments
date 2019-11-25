from unittest import TestCase
from A01166243_1510_assignments.A4.question_8 import im_not_sleepy


class TestImNotSleepy(TestCase):
    def test_im_not_sleepy(self):
        self.assertEqual(f"The time that requires the highest amount of bars is 10:08. The amount of bars is {21}.",
                         im_not_sleepy())
