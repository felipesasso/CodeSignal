import unittest

from interview_practice.arrays.main import first_duplicate

class FirstDuplicate(unittest.TestCase):

    def test_1(self):
        a = [2, 1, 3, 5, 3, 2]
        result = first_duplicate(a)
        self.assertEqual(result, 3)

    def test_2(self):
        a = [2, 2]
        result = first_duplicate(a)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
