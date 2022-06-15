# You are given an m x n binary m grid. An island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [
# [0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    ground_coordinates = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ground_coordinates.add((i, j))

    # print(ground_coordinates)

    max_area = 0

    while ground_coordinates:
        current_island = set()
        current_island.add(ground_coordinates.pop())

        current_area = 0

        while current_island:
            i, j = current_island.pop()
            current_area += 1
            if (i, j + 1) in ground_coordinates:
                current_island.add((i, j + 1))
                ground_coordinates.remove((i, j + 1))

            if (i, j - 1) in ground_coordinates:
                current_island.add((i, j - 1))
                ground_coordinates.remove((i, j - 1))

            if (i + 1, j) in ground_coordinates:
                current_island.add((i + 1, j))
                ground_coordinates.remove((i + 1, j))

            if (i - 1, j) in ground_coordinates:
                current_island.add((i - 1, j))
                ground_coordinates.remove((i - 1, j))

        max_area = max(max_area, current_area)

    return max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(max_area_of_island(grid))
