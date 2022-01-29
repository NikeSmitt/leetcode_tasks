# Given an array, rotate the array to the right by k steps, where k is non-negative.


import unittest
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return
    k %= len(nums)
    nums.reverse()
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = k, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


class TestRotate(unittest.TestCase):

    def test_one_value_array(self):
        array = [1]
        rotate(array, 10)
        self.assertEqual([1], array)

    def test_case_1(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        rotate(array, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], array)
