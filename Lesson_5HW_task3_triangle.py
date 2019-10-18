import unittest

from Lesson_3HW import triangle

class TestLeapTear(unittest.TestCase):
    def test_0(self):
        res = triangle(12, 15, 14)
        self.assertTrue(res, ok)

    def test_1(self):
        res = triangle(14, 14, 14)
        self.assertTrue(res, ok)

    def test_2(self):
        res = triangle(50, 11, 14)
        self.assertFalse(res, bad)

if __name__ =="__main__":
    unittest.main()




