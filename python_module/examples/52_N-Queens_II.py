class Solution:
    """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

        Given an integer n, return the number of distinct solutions to the n-queens puzzle.

        Example 1:

        Input: n = 4
        Output: 2
        Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
        Example 2:

        Input: n = 1
        Output: 1

        Constraints:

        1 <= n <= 9
    """
    def __init__(self):
        self.cnt = 0
    def totalNQueens1(self, n: int) -> int:
        if n < 1:
            return 0
        elif n == 1:
            return 1

        def checkBoard(columns: list, row: int, col: int) -> bool:
            for i in range(row):
                if columns[i] == col or abs(row - i) == abs(columns[i] - col):
                    return False
            return True

        def solveQueens(idx: int, columns: list):
            if idx == n:
                self.cnt += 1
                return

            for i in range(n):
                columns[idx] = i
                if checkBoard(columns, idx, i):
                    solveQueens(idx + 1, columns)

        columns = [0] * n
        solveQueens(0, columns)
        return self.cnt
    
    def totalNQueens2(self, n: int) -> int:
        def check(cols: list, row: int, col: int) -> bool:
            for i in range(row):
                if cols[i] == col or abs(row - i) == abs(cols[i] - col):
                    return False
            return True
        
        self.cnt = 0
        def helper(idx: int, cols: list):
            if idx == n:
                self.cnt += 1
                return
            
            for i in range(n):
                cols[idx] = i
                if check(cols, idx, i):
                    helper(idx + 1, cols)
        cols = [0] * n
        helper(0, cols)
        return self.cnt 