import unittest

from shuffle import knuth_shuffle


class TestKnuthShuffle(unittest.TestCase):
    def test_shuffle_nums(self):
        nums = [1, 4, 3, 2, 1, 4, 4, 1, 5, 7]

        self.assertNotEqual(nums, knuth_shuffle(nums))

    def test_shuffle_string(self):
        strings = ["ping", "pong", "pang", "peng", "pung"]

        self.assertNotEqual(strings, knuth_shuffle(strings))
