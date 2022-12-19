from typing import List


class Solution:
    """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.

        Example 1:

        Input: board =
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        Output: true
        Example 2:

        Input: board =
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        Output: false
        Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    """
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        n = 9
        # Use an array to record the status
        rows = [[0] * n for _ in range(n)]
        cols = [[0] * n for _ in range(n)]
        boxes = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # Check if the position is filled with number
                if board[i][j] == ".":
                    continue

                pos = int(board[i][j]) - 1
                # Check the row
                if rows[i][pos] == 1:
                    return False
                rows[i][pos] = 1

                # Check the column
                if cols[j][pos] == 1:
                    return False
                cols[j][pos] = 1

                # Check the box
                idx = (i // 3) * 3 + j // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == ".":
                    continue

                # check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # check col
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # check box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True




