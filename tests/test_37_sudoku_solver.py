import unittest

from backtracking.sudoku_solver_37 import Solution


class TestSudokuSolver(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.board = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]
    
    def test_check_sudoku_line_all_digits_unique(self):
        case = ['2', '3', '4', '5', '6', '7', '8', '9', '.']
        candidate = '1'
        self.assertTrue(self.solution.is_line_free_for_candidate(case, candidate))
    
    def test_check_sudoku_line_all_digits_not_unique(self):
        case = ['2', '3', '4', '5', '6', '7', '8', '9', '.']
        candidate = '2'
        self.assertFalse(self.solution.is_line_free_for_candidate(case, candidate))
    
    def test_get_line_from_point(self):
        point = {'x': 0, 'y': 0}
        line = self.board[0]
        self.assertEqual(self.solution.get_point_line(point, board=self.board), line)
        
        point = {'x': 2, 'y': 3}
        line = self.board[2]
        self.assertEqual(self.solution.get_point_line(point, board=self.board), line)
    
    def test_get_point_column(self):
        point = {'x': 0, 'y': 0}
        column = ['5', '6', '1', '8', '4', '7', '9', '2', '3']
        self.assertEqual(self.solution.get_point_column(point, self.board), column)
        
        point = {'x': 0, 'y': 0}
        column = ['3', '7', '9', '5', '2', '1', '6', '8', '4']
        self.assertNotEqual(self.solution.get_point_column(point, self.board), column)
    
    def test_get_point_box(self):
        point = {'x': 0, 'y': 0}
        right_box = ["5", "3", "4", "6", "7", "2", "1", "9", "8"]
        self.assertEqual(self.solution.get_point_box(point, self.board), right_box)
        
    def test_get_point_box_2(self):
        
        point = {'x': 5, 'y': 2}
        right_box = ["8", "5", "9", "4", "2", "6", "7", "1", "3"]
        self.assertEqual(self.solution.get_point_box(point, self.board), right_box)
