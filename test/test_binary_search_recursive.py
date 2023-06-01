import unittest
from typing import Any

from search import binary_search_recursive


class TestBinarySearch(unittest.TestCase):
    def test_when_collection_is_empty(self):
        collection: list[Any] = []
        search: int = 1
        left_idx: int = 0
        right_idx: int = len(collection) - 1

        self.assertFalse(
            binary_search_recursive(collection, search, left_idx, right_idx)
        )

    def test_when_collection_is_not_empty(self):
        collection: list[Any] = [
            -6,
            -5,
            -1,
            0,
            1,
            4,
            4,
            5,
            6,
            8,
            9,
            10,
            30,
            34,
            56,
            100,
        ]
        search: int = 4
        left_idx: int = 0
        right_idx: int = len(collection) - 1

        self.assertTrue(
            binary_search_recursive(collection, search, left_idx, right_idx)
        )

    def test_when_item_not_in_collection(self):
        collection: list[Any] = [
            -6,
            -5,
            -1,
            0,
            1,
            4,
            4,
            5,
            6,
            8,
            9,
            10,
            30,
            34,
            56,
            100,
        ]
        search: int = -100
        left_idx: int = 0
        right_idx: int = len(collection) - 1

        self.assertFalse(
            binary_search_recursive(collection, search, left_idx, right_idx)
        )

    def test_when_item_in_collection(self):
        collection: list[Any] = [
            -6,
            -5,
            -1,
            0,
            1,
            4,
            4,
            5,
            6,
            8,
            9,
            10,
            30,
            34,
            56,
            100,
        ]
        search: int = -5
        left_idx: int = 0
        right_idx: int = len(collection) - 1

        self.assertTrue(
            binary_search_recursive(collection, search, left_idx, right_idx)
        )


if __name__ == "__main__":
    unittest.main()
