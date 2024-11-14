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
# approach:
# we need check each row to make sure that there are no duplicates. it must have a unique number
# We need to check for each column to make sure that there are no duplicates it must have a unique numner
# separate out into a 3x3 box, and make sure that everythign there has no duplicates

# What do we consider valid? 
# No duplicates.

def isValidSudoku(board: list[list[str]]) -> bool:
    def is_valid(nums: list[str]) -> bool:
        seen = set()
        for num in nums:
            if num != ".":
                if num in seen:
                    return False
                else:
                    seen.add(num)
        return True
    

    for row in range(9):
        if not is_valid(board[row]):
            return False
    
    for col in range(9):
        val = []
        for row in range(9):
            val.append(board[row][col])
        if not is_valid(val):
            return False

    for row_box in range(0, 9, 3):
        for col_box in range(0, 9, 3):
            val = []
            for row in range(row_box, row_box + 3):
                for col in range(col_box, col_box + 3):
                    val.append(board[row][col])
            if not is_valid(val):
                return False
    return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "5", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSudoku(board1))  # Output: True
print(isValidSudoku(board2))  # Output: False



    


