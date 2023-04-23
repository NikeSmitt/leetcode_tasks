# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.


# Input: board = [
# ["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
#
# Output: [
# ["5","3","4","6","7","8","9","1","2"],
# ["6","7","2","1","9","5","3","4","8"],
# ["1","9","8","3","4","2","5","6","7"],
# ["8","5","9","7","6","1","4","2","3"],
# ["4","2","6","8","5","3","7","9","1"],
# ["7","1","3","9","2","4","8","5","6"],
# ["9","6","1","5","3","7","2","8","4"],
# ["2","8","7","4","1","9","6","3","5"],
# ["3","4","5","2","8","6","1","7","9"]
# ]
#
# Explanation: The input board is shown above and the only valid solution is shown below:
from typing import List


class Solution:
    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
    def is_line_free_for_candidate(self, line: list, candidate: str) -> bool:
        if line.count(candidate):
            return False
        return True
    
    def get_point_line(self, point: dict, board: List[List[str]]) -> List[str]:
        x = point.get('x')
        return board[x]
    
    def get_point_column(self, point: dict, board: List[List[str]]) -> List[str]:
        y = point['y']
        column = [board[n][y] for n in range(9)]
        return column
    
    def get_point_box(self, point: dict, board: List[List[str]]) -> List[str]:
        x, y = point.values()
        box_x = x // 3 * 3
        box_y = y // 3 * 3
        
        output = []
        
        for i in range(box_x, box_x + 3):
            for j in range(box_y, box_y + 3):
                output.append(board[i][j])
        return output
        
    
    def 