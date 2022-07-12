# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be
# planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer
# n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_modified = flowerbed[:]
        count = 0
        for i in range(len(flowerbed_modified)):
            if flowerbed_modified[i] == 0:
                left_pos = (i == 0) or (flowerbed_modified[i - 1] == 0)
                right_pos = (i == len(flowerbed_modified) - 1) or (flowerbed_modified[i + 1] == 0)
                
                if left_pos and right_pos:
                    count += 1
                    flowerbed_modified[i] = 1
        
        return count >= n


if __name__ == '__main__':
    s = Solution()
    print(s.can_place_flowers([1, 0, 0, 0, 1], 1))
    print(s.can_place_flowers([1, 0, 0, 0, 1], 2))
