import unittest
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return [nums[0] ** 2]

    i = 0
    while i < len(nums) - 1 and nums[i] < 0:
        i += 1
    output = []
    left, right = i - 1, i
    while left >= 0 and right <= len(nums) - 1:
        if abs(nums[left]) < abs(nums[right]):
            output.append(nums[left] ** 2)
            left -= 1
        elif abs(nums[left]) > abs(nums[right]):
            output.append(nums[right] ** 2)
            right += 1
        else:
            output.append(nums[left] ** 2)
            output.append(nums[right] ** 2)
            left -= 1
            right += 1

    while left >= 0:
        output.append(nums[left] ** 2)
        left -= 1

    while right < len(nums):
        output.append(nums[right] ** 2)
        right += 1

    return output


class TestSortedSquares(unittest.TestCase):

    def test_one_value_array(self):
        self.assertEqual([100], sorted_squares([10]))

    def test_case_1(self):
        res = sorted_squares([-4, -1, 0, 3, 10])
        expect = [0, 1, 9, 16, 100]
        self.assertEqual(expect, res)

    def test_case_2(self):
        res = sorted_squares([-4, -1, 1, 3, 10])
        expect = [1, 1, 9, 16, 100]
        self.assertEqual(expect, res)

    def test_case_all_positive(self):
        res = sorted_squares([1, 2, 3, 5, 10])
        expect = [1, 4, 9, 25, 100]
        self.assertEqual(expect, res)


    def test_case_all_negative(self):
        res = sorted_squares([-100, -50, -3, -2, -1])
        expect = [1, 4, 9, 2500, 10000]
        self.assertEqual(expect, res)


    def test_case_all_negative(self):
        res = sorted_squares([-1, 2, 2])
        expect = [1, 4, 4]
        self.assertEqual(expect, res)
