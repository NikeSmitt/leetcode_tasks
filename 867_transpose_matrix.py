# Given a 2D integer array m, return the transpose of m.

# The transpose of a m is the m flipped over its main diagonal,
# switching the m's row and column indices.

# Hint
# We don't need any special algorithms to do this. You just need to know what the transpose of a matrix looks like.
# Rows become columns and vice versa!
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                result[i][j] = matrix[j][i]
        return result


if __name__ == '__main__':
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert s.transpose(m) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    m = [[1, 2, 3], [4, 5, 6]]
    assert s.transpose(m) == [[1, 4], [2, 5], [3, 6]]
    
    print('All ok!')
