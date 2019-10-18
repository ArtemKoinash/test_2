import unittest
from Lesson_3HW import is_leap_year

class TestLeapTear(unittest.TestCase):
    def test_0(self):
        res = is_leap_year(1989)
        self.assertFalse(res)

    def test_1(self):
        res = is_leap_year(2000)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()