# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents
# water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell
# is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter
# of the island.
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def island_perimeter(grid: List[List[int]]) -> int:
        perimeter = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]:
                    perimeter += 4
                    if x < len(grid) - 1 and grid[x + 1][y]:
                        perimeter -= 1
                    if x > 0 and grid[x - 1][y]:
                        perimeter -= 1
                    if y < len(grid[0]) - 1 and grid[x][y + 1]:
                        perimeter -= 1
                    if y > 0 and grid[x][y - 1]:
                        perimeter -= 1
                
        return perimeter


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    res = 16
    
    print(Solution.island_perimeter(grid))

    grid = [[1]]
    res = 4

    print(Solution.island_perimeter(grid))