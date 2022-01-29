# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
from pprint import pprint
from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    dist = [[float('inf')] * len(mat[i]) for i in range(len(mat))]
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] == 0:
                dist[row][col] = 0
            else:
                if col > 0:
                    dist[row][col] = min(dist[row][col], dist[row][col - 1] + 1)
                if row > 0:
                    dist[row][col] = min(dist[row][col], dist[row - 1][col] + 1)

    # основной прикол в то том, чтобы пройти просмотреть нижнюю и правую с конца в начало

    for row in range(len(mat) - 1, -1, -1):
        for col in range(len(mat[row]) - 1, -1, -1):

            if col + 1 < len(mat[row]):
                dist[row][col] = min(dist[row][col], dist[row][col + 1] + 1)
            if row + 1 < len(mat):
                dist[row][col] = min(dist[row][col], dist[row + 1][col] + 1)

    return dist


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# res = update_matrix(mat)
# pprint(res)

mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# res = update_matrix(mat)
# pprint(res)

mat = [
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1]]

# my = [
#     [0, 1, 0, 1, 2],
#     [1, 2, 0, 0, 1],
#     [0, 0, 0, 1, 0],
#     [1, 0, 1, 2, 1],
#     [2, 0, 0, 0, 1]
# ]

expect = [
    [0, 1, 0, 1, 2],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1]]

res = update_matrix(mat)
print('result')
pprint(res)
# print('source')
# pprint(mat)
print('expect')
pprint(expect)
print(res == expect)

mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
       [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

res = update_matrix(mat)

expect = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
          [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
          [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]

print(res == expect)
