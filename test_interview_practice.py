import unittest

from interview_practice.arrays.main import first_duplicate
from interview_practice.common_techniques.main import contains_duplicates

class TestArrays(unittest.TestCase):

    def test_first_duplicate_1(self):
        a = [2, 1, 3, 5, 3, 2]
        result = first_duplicate(a)
        self.assertEqual(result, 3)

    def test_first_duplicate_2(self):
        a = [2, 2]
        result = first_duplicate(a)
        self.assertEqual(result, 2)

class TestCommonTechniques(unittest.TestCase):
    def test_contains_duplicates_1(self):
        a=[1, 2, 3, 1]
        result = contains_duplicates(a)
        self.assertTrue(result)

    def test_contains_duplicates_2(self):
        a=[3, 1]
        result = contains_duplicates(a)
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()
