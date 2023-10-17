"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        l, r = 0, len(output[0])
        t, b = 0, len(output)
        c = 1
        while l < r and t < b:
            for i in range(l, r):
                output[t][i] = c
                c += 1
            t += 1
            for i in range(t, b):
                output[i][r - 1] = c
                c += 1
            r -= 1
            
            if not (l < r and t < b):
                break
            
            for i in range(r - 1, l - 1, -1):
                output[b - 1][i] = c
                c += 1
            b -= 1
            for i in range(b - 1, t - 1, -1):
                output[i][l] = c
                c += 1
            l += 1
        return output


if __name__ == '__main__':
    s = Solution()
    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(1) == [[1]]
