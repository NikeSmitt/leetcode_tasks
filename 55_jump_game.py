"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


"""
from typing import List


class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        step = 1
        for pos in range(len(nums) - 2, -1, -1):
            if nums[pos] < step:
                step += 1
            else:
                step = 1
        return nums[0] >= step


if __name__ == '__main__':
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4])
    assert not s.canJump([3, 2, 1, 0, 4])
