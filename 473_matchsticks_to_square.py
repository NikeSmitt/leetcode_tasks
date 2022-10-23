# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        sum_ = sum(matchsticks)
        if sum_ % 4:
            return False
        
        side = sum_ // 4
        
        def helper(sides, sticks, i=0):
            if i == len(sticks):
                if len(set(sides)) == 1:
                    return True
                return False
            for j in range(i, len(sticks)):
                
                if sides[0] + sticks[j] <= side:
                    sides[0] += sticks[j]
                    if helper(sides, sticks, i + 1):
                        return True
                    sides[0] -= sticks[j]
                
                if sides[1] + sticks[j] <= side:
                    sides[1] += sticks[j]
                    if helper(sides, sticks, i + 1):
                        return True
                    sides[1] -= sticks[j]
                
                if sides[2] + sticks[j] <= side:
                    sides[2] += sticks[j]
                    if helper(sides, sticks, i + 1):
                        return True
                    sides[2] -= sticks[j]
                
                if sides[3] + sticks[j] <= side:
                    sides[3] += sticks[j]
                    if helper(sides, sticks, i + 1):
                        return True
                    sides[3] -= sticks[j]
            return False
        
        return helper([0, 0, 0, 0], matchsticks, 0)


if __name__ == '__main__':
    s = Solution()
    assert not s.makesquare([2, 3, 5])
    assert not s.makesquare([1, 1, 1, 2])
    assert s.makesquare([1, 1, 2, 2, 2])
    assert not s.makesquare([3, 3, 3, 3, 4])
    print('Tested!')
