# Problem 36. Valid Sudoku
# Difficulty: Medium
#
# Description:
# Determine if a 9 x 9 Sudoku board is valid based on the following rules:
#  1. Each row must contain the digits 1-9 without repetition.
#  2. Each column must contain the digits 1-9 without repetition.
#  3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.
#
# Note:
# - A partially filled Sudoku board could be valid but not necessarily solvable.
# - Only the filled cells (i.e., cells containing digits) need to be validated.
#
# Example 1:
# Input:
# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
#
# Example 2:
# Input:
# board = [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: In this case, there are two 8's in the top-left 3x3 sub-box, making it invalid.
#
# Constraints:
# - board.length == 9
# - board[i].length == 9
# - board[i][j] is either a digit ('1'-'9') or '.'.
#
# Approach:
# - Check each row, column, and 3x3 sub-box to ensure that they contain no repeated digits.
# - Use a set to track digits for each row, column, and box, resetting the set after each row, column, or sub-box.
# - Return True if all checks pass; otherwise, return False.


def isValidSudoku(board: list[list[str]]) -> bool:
    pass