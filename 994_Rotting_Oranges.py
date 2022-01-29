# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
# return -1.
from typing import List
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    if not (len(grid) and len(grid[0])):
        return 0

    rotten = deque([])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                rotten.append((i, j))

    timer = 0

    if not rotten:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return timer

    while rotten:
        cur_len = len(rotten)
        for _ in range(cur_len):
            row, col = rotten.popleft()
            if row < len(grid) - 1 and grid[row + 1][col] == 1:
                rotten.append((row + 1, col))
                grid[row + 1][col] = 2
            if row > 0 and grid[row - 1][col] == 1:
                rotten.append((row - 1, col))
                grid[row - 1][col] = 2

            if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                rotten.append((row, col + 1))
                grid[row][col + 1] = 2

            if col > 0 and grid[row][col - 1] == 1:
                rotten.append((row, col - 1))
                grid[row][col - 1] = 2

        timer += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return timer - 1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
res = oranges_rotting(grid)
print(res == 4)
print(f'{res=}')

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
res = oranges_rotting(grid)
print(res == -1)
print(f'{res=}')

grid = [[0, 2]]
res = oranges_rotting(grid)
print(res == 0)
print(f'{res=}')
