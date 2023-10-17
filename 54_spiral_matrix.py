"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

"""
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
"""
from typing import List


class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        output = []
        while l < r and t < b:
            for i in range(l, r):
                output.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                output.append(matrix[i][r - 1])
            r -= 1
            
            if not (l < r and t < b):
                break
                
            for i in range(r - 1, l - 1, -1):
                output.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                output.append(matrix[i][l])
            l += 1
            
        return output


if __name__ == '__main__':
    s = Solution()
    # assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
