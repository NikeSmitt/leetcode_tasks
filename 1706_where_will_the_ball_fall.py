from typing import List

"""
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after
dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box. """


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        output = []
        
        l = len(grid)
        
        def helper(row, col, grid):
            if row == len(grid):
                return col
            
            next_col = col + grid[row][col]
            
            if next_col < 0 or next_col > len(grid[0]) - 1 or grid[row][next_col] != grid[row][col]:
                return -1
            return helper(row + 1, next_col, grid)
        
        for i in range(len(grid[0])):
            output.append(helper(0, i, grid))
        
        return output


if __name__ == '__main__':
    s = Solution()
    g = [[1, 1, 1, -1, -1],
         [1, 1, 1, -1, -1],
         [-1, -1, -1, 1, 1],
         [1, 1, 1, 1, -1],
         [-1, -1, -1, -1, -1]]
    print(s.findBall(g) == [1, -1, -1, -1, -1])
    print(s.findBall(g))
    
    g = [[1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1]]
    print(s.findBall(g) == [0, 1, 2, 3, 4, -1])
    print(s.findBall(g))
    
    g = [[-1, 1, 1, -1, 1, 1, -1], [-1, -1, 1, -1, -1, -1, -1]]
    print(s.findBall(g) == [-2, -1, -1, -1, 4, -1, -1])
    print(s.findBall(g))
