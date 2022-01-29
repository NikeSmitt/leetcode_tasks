# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any
# order.
from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        
        output = []
        temp = nums[:]
        
        def helper(start, stop, candidate):
            if start == stop:
                output.append(candidate[:])
                return
            for i in range(start, stop + 1):
                candidate[start], candidate[i] = candidate[i], candidate[start]
                helper(start + 1, stop, candidate)
                candidate[start], candidate[i] = candidate[i], candidate[start]

        helper(0, len(nums) - 1, temp)
        return output
    
    
if __name__ == '__main__':
    

    
    nums = [1, 2, 3]
    res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    print(Solution.permute(nums))
    
    nums = [0, 1]
    res = [[0, 1], [1, 0]]

    nums = [1]
    res = [[1]]
