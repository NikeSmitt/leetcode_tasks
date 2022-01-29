# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.

# Note that you must do this in-place without making a copy of the array.
from typing import List
import unittest


def move_zeroes(nums: List[int]) -> None:
    last_non_zero = 0

    # for i in range(0, len(nums)):
    #     if nums[i] != 0:
    #         nums[last_non_zero] = nums[i]
    #         last_non_zero += 1
    #
    # for i in range(last_non_zero, len(nums)):
    #     nums[i] = 0

    for pointer in range(len(nums)):
        if nums[pointer] != 0:
            nums[last_non_zero], nums[pointer] = nums[pointer], nums[last_non_zero]
            last_non_zero += 1


class TestMoveZeroes(unittest.TestCase):

    def test_one_value_arr(self):
        array = [0]
        move_zeroes(array)
        self.assertEqual([0], array)

    def test_case_1(self):
        source = [0, 1, 0, 3, 12]
        move_zeroes(source)
        self.assertEqual([1, 3, 12, 0, 0], source)

    def test_case_2(self):
        source = [0, 1, 0, 0, 0, 100, 0, 5]
        move_zeroes(source)
        self.assertEqual([1, 100, 5, 0, 0, 0, 0, 0], source)

        [0, 0, 0, ..., 0, 1]

    def test_case_3(self):
        source = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        move_zeroes(source)
        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 0, 0], source)
