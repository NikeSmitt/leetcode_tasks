# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.
from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        output = []
        temp = []
        
        def helper(start, stop, candidate):
            if len(candidate) == k:
                output.append(candidate[:])
                return
            
            for i in range(start, stop + 1):
                temp.append(i)
                helper(i + 1, stop, temp)
                temp.pop()
        helper(1, n, temp)
        
        return output


if __name__ == '__main__':
    print(Solution.combine(4, 2))
    