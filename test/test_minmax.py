import unittest

from search import max, min


class TestMinMax(unittest.TestCase):
    def test_min_when_collection_is_empty(self):
        nums = []

        with self.assertRaises(ValueError):
            min(nums)

    def test_max_when_collection_is_empty(self):
        nums = []

        with self.assertRaises(ValueError):
            max(nums)

    def test_min_when_collection_is_not_empty(self):
        nums = [23, 1, 4, 6, 3, 2, 1, 7, 8, 9, 0, -1, 2, 5]

        self.assertEqual(min(nums), -1)

    def test_max_when_collection_is_not_empty(self):
        nums = [23, 1, 4, 6, 3, 2, 1, 7, 8, 9, 0, -1, 2, 5]

        self.assertEqual(max(nums), 23)
