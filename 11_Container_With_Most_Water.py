from typing import List


class Solution:
    
    def max_area(self, height: List[int]) -> int:
        """ brute force solution """
        max_area = 0
        
        for left in range(len(height) - 1):
            for right in range(left + 1, len(height)):
                water_wall = min(height[left], height[right])
                water_area = (right - left) * water_wall
                max_area = max(max_area, water_area)
        return max_area
    
    def max_area_pointers(self, height: List[int]) -> int:
        """ two pointers solution """
        
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left != right:
            water_wall = min(height[left], height[right])
            water_area = (right - left) * water_wall
            max_area = max(max_area, water_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


if __name__ == '__main__':
    cases = [
        ([1, 1], 1),
        ([1, 2, 1], 2),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    ]
    solution = Solution()
    
    # test_func = solution.max_area
    test_func = solution.max_area_pointers
    
    for h, res in cases:
        my_result = test_func(h)
        if my_result != res:
            print(f'We have a problem with testcase {h} -> {res} != {my_result=}')
        else:
            print(f'Testcase {h} OK!')
