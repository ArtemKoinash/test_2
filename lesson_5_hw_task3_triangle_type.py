import unittest

from Lesson_3HW import triangle_type

class TestLeapTear(unittest.TestCase):
    def test_0(self):
        res = triangle_type(50, 12, 10)
        self.assertTrue(res, )

    def test_1(self):
        res = triangle_type(10, 10, 10)
        self.assertEqual(res, 'Equilateral triangle')

    def test_2(self):
        res = triangle_type(15, 15, 10)
        self.assertEqual(res, 'Isosceles triangle')

    def test_3(self):
        res = triangle_type(10, 13, 15)
        self.assertEqual(res, 'Versatile triangle')

if __name__ =="__main__":
    unittest.main()

