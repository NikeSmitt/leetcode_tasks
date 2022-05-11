from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return -1

        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle

        return -1


class TestBinarySearch(unittest.TestCase):

    def setUp(self) -> None:
        self.task = Solution()

    def tearDown(self) -> None:
        del self.task

    def test_empty_arr(self):
        arr = []
        target = 1000
        res = self.task.search(arr, target)
        self.assertEqual(res, -1, f'Empty array error output')

    def test_one_value_array(self):
        arr = [0]
        target = 1
        res = self.task.search(arr, target)
        self.assertEqual(res, -1, f'One value array error')

    def test_one_value_array_2(self):
        arr = [0]
        target = 0
        res = self.task.search(arr, target)
        self.assertEqual(res, 0, f'One value array error')

    def test_two_values_array(self):
        arr = [0, 100]
        target = 50
        res = self.task.search(arr, target)
        self.assertEqual(res, -1, f'Two value array error')

    def test_two_values_array_2(self):
        arr = [0, 100]
        target = 100
        res = self.task.search(arr, target)
        self.assertEqual(res, 1, f'Two value array error')

    def test_many_values_array(self):
        arr = [0, 100, 200]
        target = 100
        res = self.task.search(arr, target)
        self.assertEqual(res, 1, f'Two value array error')

    def test_many_values_array_2(self):
        arr = [0, 100, 200, 300]
        target = 150
        res = self.task.search(arr, target)
        self.assertEqual(res, -1, f'Two value array error')

    def test_many_values_array_3(self):
        arr = [-1, 0, 3, 5, 9, 12]
        target = 9
        res = self.task.search(arr, target)
        self.assertEqual(res, 4, f'Two value array error')


if __name__ == '__main__':
    unittest.main()
