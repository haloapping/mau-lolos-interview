import unittest

from search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_when_collection_is_empty(self):
        collection = []
        search = 1

        self.assertFalse(binary_search(collection, search))

    def test_when_collection_is_not_empty(self):
        collection = [-6, -5, -1, 0, 1, 4, 4, 5, 6, 8, 9, 10, 30, 34, 56, 100]
        search = 4

        self.assertTrue(binary_search(collection, search))

    def test_when_item_not_in_collection(self):
        collection = [-6, -5, -1, 0, 1, 4, 4, 5, 6, 8, 9, 10, 30, 34, 56, 100]
        search = -100

        self.assertFalse(binary_search(collection, search))

    def test_when_item_in_collection(self):
        collection = [-6, -5, -1, 0, 1, 4, 4, 5, 6, 8, 9, 10, 30, 34, 56, 100]
        search = -5

        self.assertTrue(binary_search(collection, search))


if __name__ == "__main__":
    unittest.main()
