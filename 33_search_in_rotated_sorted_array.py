# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (
# 0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in
# nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        
        left = 0
        right = len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot
        
        print(nums[left:right])
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
    print(s.search([1], 0) == -1)
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
    print(s.search([1, 2, 3, 0], 0) == 3)
    print(s.search([7, 0, 1, 2, 3, 4], 0) == 1)
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
    print(s.search([1, 2, 3], 2) == 1)
    print(s.search([3, 1], 3) == 0)
