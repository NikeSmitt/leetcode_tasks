# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from
# the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
# the same color), and so on. Replace the color of all the aforementioned pixels with newColor.
#
# Return the modified image after performing the flood fill.
from typing import List
from collections import deque


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    target = image[sr][sc]
    pool = deque([(sr, sc)])
    while pool:
        x, y = pool.popleft()
        if image[x][y] == target and image[x][y] != new_color:
            image[x][y] = new_color
            if y + 1 < len(image[x]):
                pool.append((x, y + 1))
            if y - 1 >= 0:
                pool.append((x, y - 1))
            if x + 1 < len(image):
                pool.append((x + 1, y))
            if x - 1 >= 0:
                pool.append((x - 1, y))

    return image


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2

    assert flood_fill(image, sr, sc, newColor) == [[2, 2, 2], [2, 2, 2]]

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    assert flood_fill(image, sr, sc, newColor) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    assert flood_fill(image, sr, sc, newColor) == [[0, 0, 0], [0, 1, 1]]