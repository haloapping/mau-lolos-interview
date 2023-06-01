import unittest

from search import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_when_collection_is_empty(self):
        collection = []
        search = 1

        self.assertFalse(linear_search(collection, search))

    def test_when_collection_is_not_empty(self):
        collection = [12, 3, 1, 9, 10, -10, 11, 43, 23, 0, 1]
        search = 1

        self.assertTrue(linear_search(collection, search))

    def test_when_item_not_in_collection(self):
        collection = [12, 3, 1, 9, 10, -10, 11, 43, 23, 0, 1]
        search = -1

        self.assertFalse(linear_search(collection, search))

    def test_when_item_in_collection(self):
        collection = [12, 3, 1, 9, 10, -10, 11, 43, 23, 0, 1]
        search = 43

        self.assertTrue(linear_search(collection, search))


if __name__ == "__main__":
    unittest.main()
