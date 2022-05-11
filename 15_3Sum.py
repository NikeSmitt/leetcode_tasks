from typing import List


class Solution:
    """Given an integer array nums, return all the triplets
     [nums[i], nums[j], nums[k]] such that i != j, i != k,
     and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""
    
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        output = []
        last_base = float('-inf')
        
        nums = sorted(nums)
        
        for base in range(len(nums)):
            if nums[base] == last_base:
                continue
            
            last_base = nums[base]
            l, r = base + 1, len(nums) - 1
            last_l, last_r = float('-inf'), float('-inf')
            while l < r:
                sum_ = nums[base] + nums[l] + nums[r]
                if sum_ == target and nums[l] != last_l and nums[r] != last_r:
                    output.append([nums[base], nums[l], nums[r]])
                    last_r = nums[r]
                    last_l = nums[l]
                    l += 1
                    r -= 1
                elif sum_ < target:
                    l += 1
                else:
                    r -= 1
        return output


if __name__ == '__main__':
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]])
    ]
    solution = Solution()
    
    # test_func = solution.max_area
    test_func = solution.three_sum
    for h, res in cases:
        my_result = test_func(h)
        if my_result != res:
            print(f'We have a problem with testcase {h} -> {res} != {my_result=}')
        else:
            print(f'Testcase {h} OK!')
