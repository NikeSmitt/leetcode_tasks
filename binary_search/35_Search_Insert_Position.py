# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

import unittest
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    if not len(nums):
        return 0

    left, right = 0, len(nums) - 1

    mid = 0

    while right >= left:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1


class TestSearchInsert(unittest.TestCase):

    def test_empty_array(self):
        res = search_insert([], 1)
        self.assertEqual(0, res, 'Empty array insert wrong position')

    def test_one_value_array_lower_target(self):
        res = search_insert([100], 0)
        self.assertEqual(0, res)

    def test_one_value_array_greater_target(self):
        res = search_insert([100], 200)
        self.assertEqual(1, res)

    def test_example_1(self):
        res = search_insert([1, 3, 5, 6], 5)
        self.assertEqual(2, res)

    def test_example_2(self):
        res = search_insert([1, 3, 5, 6], 2)
        self.assertEqual(1, res)

    def test_example_3(self):
        res = search_insert([1, 3, 5, 6], 7)
        self.assertEqual(4, res)
