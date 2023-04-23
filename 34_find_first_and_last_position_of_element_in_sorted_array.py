# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_pos(n, t):
            l, r = 0, len(nums) - 1
            res = -1
            
            while l <= r:
                mid = (l + r) // 2
                if n[mid] > t:
                    r = mid - 1
                elif n[mid] < t:
                    l = mid + 1
                else:
                    res = mid
                    r = mid - 1
            return res
        
        def right_pos(n, t):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if n[mid] < t:
                    l = mid + 1
                elif n[mid] > t:
                    r = mid - 1
                else:
                    res = mid
                    l = mid + 1
            return res
        
        left = left_pos(nums, target)
        right = right_pos(nums, target)
        return [left, right]


if __name__ == '__main__':
    s = Solution()
    # print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    # print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(s.searchRange([1], 1))
